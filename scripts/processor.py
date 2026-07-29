# -*- coding: utf-8 -*-
"""
Processor module for Skill Roteirista.
Handles input parsing, language detection, pre-narration validation,
word count tolerance checks (140 WPM ±20%), SRT pacing generation,
DarkPlanner TTS API integration, and file export.
"""

import os
import sys
import re
import time
import json
import urllib.request
import ssl

DARK_PLANNER_API_KEY = "dpk_a24f6658de6f67ba3ebbf73ffe6c8fa77badcd9e36fcc524"
VALENTINO_VOICE_ID = "dc674015-b94c-4078-9538-4a7d1d612ce9"
DARK_PLANNER_BASE_URL = "https://app.darkplanner.com.br/api/v1/audio"
WPM_BASE = 140

def parse_title_input(input_str):
    """
    Parses input string into title, channel code, content type, and duration.
    Formats:
    - 'A historia de jo, BI 10 min' -> BI / B1 = Bíblico Ilustrado
    - 'A historia de jo, BC 10 min' -> BC / B2 = Bíblico Cinematográfico
    """
    cleaned = input_str.strip()
    match = re.search(r'^(.*?)[,\s]+([A-Za-z0-9]+)(?:[,\s]+([A-Za-z]))?[,\s]+(\d+)\s*(?:MIN|M)?$', cleaned, re.IGNORECASE)
    
    if match:
        title = match.group(1).strip()
        channel_code = match.group(2).upper()
        content_type = match.group(3).upper() if match.group(3) else "C"
        duration_min = int(match.group(4))
    else:
        parts = [p.strip() for p in cleaned.split(',')]
        if len(parts) >= 2:
            title = parts[0]
            rest = parts[1].split()
        else:
            tokens = cleaned.split()
            title = " ".join(tokens[:-2]) if len(tokens) > 2 else "Video_Roteiro"
            rest = tokens[-2:]

        channel_code = rest[0].upper() if len(rest) > 0 else "BI"
        content_type = "C"

        dur_str = "10"
        for t in rest:
            m = re.search(r'(\d+)', t)
            if m and t.upper() not in ["B1", "BI", "B2", "BC", "C1", "C2"]:
                dur_str = m.group(1)

        duration_min = int(dur_str) if dur_str.isdigit() else 10

    # Map BI to B1, BC to B2 for consistency
    if channel_code in ["BI", "B1"]:
        channel_code = "B1"
    elif channel_code in ["BC", "B2"]:
        channel_code = "BC"

    return {
        "title": title,
        "channel_code": channel_code,
        "content_type": content_type,
        "duration_min": duration_min
    }

def detect_language(text):
    """
    Robustly detects language (Portuguese, English, Spanish).
    """
    t_lower = text.lower()
    pt_keywords = ["história", "historia", "que", "para", "com", "não", "nao", "uma", "um", "do", "da", "seu", "sua", "de", "em", "por", "sobre", "senhor", "deus", "bíblia", "biblia"]
    en_keywords = ["the", "story", "of", "in", "and", "god", "bible", "life", "lord"]
    es_keywords = ["la", "el", "historia", "de", "dios", "biblia", "vida", "señor", "senor"]
    
    pt_score = sum(1 for w in pt_keywords if f" {w} " in f" {t_lower} ")
    en_score = sum(1 for w in en_keywords if f" {w} " in f" {t_lower} ")
    es_score = sum(1 for w in es_keywords if f" {w} " in f" {t_lower} ")

    if pt_score >= en_score and pt_score >= es_score:
        return "Portuguese"
    elif en_score > pt_score and en_score > es_score:
        return "English"
    else:
        return "Spanish"

def calculate_word_targets(duration_min):
    target = duration_min * WPM_BASE
    return {
        "target": target,
        "min_words": int(target * 0.8),
        "max_words": int(target * 1.2)
    }

def pre_narration_verification(script_text, title, duration_min):
    clean_text = re.sub(r'\[[IV]\]', '', script_text).strip()
    words = re.findall(r'\b\w+\b', clean_text)
    word_count = len(words)
    targets = calculate_word_targets(duration_min)

    word_count_passed = targets["min_words"] <= word_count <= targets["max_words"]
    diff_pct = round(((word_count - targets["target"]) / targets["target"]) * 100, 2)

    title_lang = detect_language(title)
    script_lang = detect_language(clean_text[:500])
    lang_passed = (title_lang == script_lang)

    is_all_valid = word_count_passed and lang_passed

    report = {
        "is_valid": is_all_valid,
        "title_language": title_lang,
        "script_language": script_lang,
        "language_match": lang_passed,
        "word_count": word_count,
        "target_word_count": targets["target"],
        "min_allowed_words": targets["min_words"],
        "max_allowed_words": targets["max_words"],
        "word_count_passed": word_count_passed,
        "diff_percentage": diff_pct
    }

    return report

def generate_darkplanner_narration(text, title="narracao"):
    clean_narration_text = re.sub(r'\[[IV]\]', '', text).strip()
    ctx = ssl.create_default_context()
    headers = {
        "X-API-Key": DARK_PLANNER_API_KEY,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    payload = {
        "text": clean_narration_text,
        "voice_id": VALENTINO_VOICE_ID,
        "title": title,
        "speed": 1.0
    }

    try:
        req = urllib.request.Request(
            f"{DARK_PLANNER_BASE_URL}/generate",
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method="POST"
        )
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            resp_data = json.loads(res.read().decode('utf-8'))
            if not resp_data.get("success"):
                print(f"[DarkPlanner API Error] {resp_data}")
                return None
            job_id = resp_data.get("job_id")
            print(f"[DarkPlanner API] Job {job_id} enviado. Processando narração...")

        for _ in range(40):
            time.sleep(2)
            req_st = urllib.request.Request(
                f"{DARK_PLANNER_BASE_URL}/status/{job_id}",
                headers=headers,
                method="GET"
            )
            with urllib.request.urlopen(req_st, context=ctx, timeout=10) as res_st:
                st_data = json.loads(res_st.read().decode('utf-8'))
                if st_data.get("status") == "completed":
                    print(f"[DarkPlanner API] Job {job_id} finalizado!")
                    break
                elif st_data.get("status") in ["failed", "error"]:
                    print(f"[DarkPlanner API Failed] {st_data}")
                    return None

        req_dl = urllib.request.Request(
            f"{DARK_PLANNER_BASE_URL}/download/{job_id}",
            headers=headers,
            method="GET"
        )
        with urllib.request.urlopen(req_dl, context=ctx, timeout=10) as res_dl:
            dl_data = json.loads(res_dl.read().decode('utf-8'))
            audio_url = dl_data.get("audio_url")
            
            if audio_url:
                dl_headers = {"X-API-Key": DARK_PLANNER_API_KEY, "User-Agent": "Mozilla/5.0"}
                req_audio = urllib.request.Request(audio_url, headers=dl_headers, method="GET")
                try:
                    with urllib.request.urlopen(req_audio, context=ctx, timeout=30) as res_a:
                        return res_a.read()
                except Exception:
                    req_audio_raw = urllib.request.Request(audio_url, headers={"User-Agent": "Mozilla/5.0"}, method="GET")
                    with urllib.request.urlopen(req_audio_raw, context=ctx, timeout=30) as res_a:
                        return res_a.read()

    except Exception as e:
        print(f"[DarkPlanner API Exception] {e}")

    return None

def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        secs += 1
        millis = 0
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def generate_srt_blocks(sentences, total_duration_sec):
    srt_blocks = []
    current_time = 0.0
    num_sentences = len(sentences)
    if num_sentences == 0:
        return ""

    for idx, sentence in enumerate(sentences, 1):
        clean_text = sentence.strip()
        if not clean_text:
            continue

        text_content = re.sub(r'^\[[IV]\]\s*', '', clean_text).strip()
        text_content = re.sub(r'^Cena\s+\d+:\s*', '', text_content).strip()

        if current_time < 60.0:
            clip_duration = min(6.0, max(3.0, (total_duration_sec - current_time) / (num_sentences - idx + 1)))
        else:
            clip_duration = min(9.5, max(7.0, (total_duration_sec - current_time) / (num_sentences - idx + 1)))

        start_time = current_time
        end_time = min(total_duration_sec, current_time + clip_duration)
        if idx == num_sentences:
            end_time = total_duration_sec

        start_str = format_timestamp(start_time)
        end_str = format_timestamp(end_time)

        srt_block = f"{idx}\n{start_str} --> {end_str}\n{text_content}\n"
        srt_blocks.append(srt_block)

        current_time = end_time

    return "\n".join(srt_blocks)

def export_to_downloads(title, narration_bytes, srt_content):
    sanitized_title = re.sub(r'[\\/*?:"<>|]', '_', title).strip().replace(' ', '_')
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    output_dir = os.path.join(downloads_dir, sanitized_title)

    os.makedirs(output_dir, exist_ok=True)

    audio_path = os.path.join(output_dir, "narracao.mp3")
    srt_path = os.path.join(output_dir, "legenda.srt")

    if narration_bytes:
        with open(audio_path, "wb") as f:
            f.write(narration_bytes)
    else:
        print("[!] Narração não foi gerada ou falhou. O arquivo narracao.mp3 não será criado sem o áudio real.")
        audio_path = None

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    return output_dir, audio_path, srt_path
