# -*- coding: utf-8 -*-
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from processor import (
    parse_title_input,
    pre_narration_verification,
    generate_darkplanner_narration,
    generate_srt_blocks,
    export_to_downloads
)
from templates import get_gemini_instructions

def run_pipeline(input_str, custom_script_text=None, generate_real_audio=True, media_mode="I"):
    parsed = parse_title_input(input_str)
    title = parsed["title"]
    channel_code = parsed["channel_code"]
    duration_min = parsed["duration_min"]

    print(f"\n==================================================")
    print(f"       PIPELINE SKILL ROTEIRISTA")
    print(f"==================================================")
    print(f" Título: {title}")
    print(f" Código Canal: {channel_code}")
    print(f" Modo Mídia: {'[I] Imagens' if media_mode in ['I','1'] else '[V] Vídeos'}")
    print(f" Duração Alvo: {duration_min} MIN")

    if not custom_script_text:
        print(" [!] Nenhum texto de roteiro customizado fornecido. Gerando demonstrativo...")
        paragraphs = []
        for i in range(1, 15):
            tag = "[V]" if media_mode in ["V", "2"] else "[I]"
            paragraphs.append(f"{tag} Cena {i}: Revelando a história dramática de {title} no cenário da época bíblica.")
        script_body = " ".join([p[4:] if p.startswith(("[I]", "[V]")) else p for p in paragraphs])
    else:
        paragraphs = [p.strip() for p in custom_script_text.split('\n') if p.strip()]
        script_body = custom_script_text

    # STEP 1: PRE-NARRATION STRICT VERIFICATION
    print("\n--- [ETAPA 1/3] VERIFICAÇÃO PRÉ-NARRAÇÃO ---")
    verification = pre_narration_verification(script_body, title, duration_min)

    print(f" Meta de Palavras (140 WPM): {verification['target_word_count']} palavras")
    print(f" Faixa Permitida (+/-20%): {verification['min_allowed_words']} a {verification['max_allowed_words']} palavras")
    print(f" Palavras no Roteiro: {verification['word_count']} ({verification['diff_percentage']}% em relação à meta)")
    print(f" Verificação de Palavras: {'[APROVADO]' if verification['word_count_passed'] else '[REPROVADO - FORA DA FAIXA]'}")

    print(f" Idioma Detectado no Título: {verification['title_language']}")
    print(f" Idioma Detectado no Roteiro: {verification['script_language']}")
    print(f" Verificação de Idioma: {'[APROVADO]' if verification['language_match'] else '[REPROVADO - IDIOMAS DIFERENTES]'}")

    if not verification['is_valid']:
        print("\n [ATENÇÃO] A verificação pré-narração encontrou inconformidades!")
        print(" Ajuste o texto para a meta de palavras e idioma antes do envio final.")
    else:
        print(" [OK] Verificação pré-narração concluída com 100% de conformidade!")

    # STEP 2: NARRATION AUDIO & OFFICIAL DARKPLANNER SRT
    narration_bytes = None
    darkplanner_srt = None
    if generate_real_audio:
        if verification['is_valid']:
            print("\n--- [ETAPA 2/3] GERANDO NARRAÇÃO E LEGENDA POR TEMPO NA DARKPLANNER API ---")
            print(" Voz: Valentino (dc674015-b94c-4078-9538-4a7d1d612ce9)")
            narration_bytes, darkplanner_srt = generate_darkplanner_narration(script_body, title=title, media_mode=media_mode)
        else:
            raise RuntimeError("Verificação pré-narração reprovada. Ajuste o roteiro antes de enviar para a API.")

    # STEP 3: EXPORTING DARKPLANNER AUDIO & SRT PACKAGE
    print("\n--- [ETAPA 3/3] EXPORTANDO PACOTE DE LEGENDA POR TEMPO E ÁUDIO ---")
    if not darkplanner_srt or not narration_bytes:
        raise RuntimeError("FALHA CRÍTICA: O áudio ou a legenda por tempo (srtsynctempo.srt) não foram retornados pela API DarkPlanner.")

    srt_content = darkplanner_srt

    out_dir, audio_path, srt_path = export_to_downloads(title, narration_bytes, srt_content)
    print(f" [OK] Pacote gerado com sucesso em:")
    print(f"     Pasta: {out_dir}")
    print(f"     Áudio: {audio_path}")
    print(f"     SRT: {srt_path}")

    # STEP 4: GEMINI PROSE INSTRUCTION FOR CHAT
    gemini_instructions = get_gemini_instructions(channel_code, media_mode)

    return {
        "title": title,
        "verification": verification,
        "out_dir": out_dir,
        "audio_path": audio_path,
        "srt_path": srt_path,
        "srt_content": srt_content,
        "gemini_instructions": gemini_instructions
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
        run_pipeline(input_str)
    else:
        print("Uso: python run_roteirista.py \"<Titulo>, <Codigo_Canal> <Duracao>\"")
        print("Exemplo: python run_roteirista.py \"A historia de Moises, B1 20MIN\"")
