# -*- coding: utf-8 -*-
"""
Templates module for Skill Roteirista.
Generates streamlined prose instructions for Gemini Online to produce
line-by-line prompts for Nano Banana 2 [I] or Veo 3 [V] with ZERO extra formatting.
"""

def get_gemini_instructions(channel_code, media_mode="V"):
    """
    Generates specific, prose-style instructions for Gemini Online.
    channel_code:
    - B1: Bíblico Ilustrado (Whiteboard Explainer / Video Scribe)
    - BC or B2: Bíblico Cinematográfico (Reconstrução Histórica por IA)
    - C, C1, C2: Outros Canais Cinematográficos / Temáticos
    
    media_mode:
    - 'I' or '1': Imagens Apenas ([I] / Nano Banana 2)
    - 'V' or '2': Vídeos Apenas ([V] / Veo 3)
    """
    channel_code = str(channel_code).upper().strip()
    mode_str = str(media_mode).upper().strip()
    is_video = mode_str in ["V", "2", "VIDEO", "VIDEOS"] or True  # Defaulting video mode if requested

    # 1. Determine Channel Name and Visual Style
    if channel_code in ["B2", "BC", "BIBLICO_CINEMATOGRAFICO"]:
        channel_name = "Bíblico Cinematográfico (BC)"
        visual_style = "Reconstrução histórica hiper-realista por IA. Fidelidade total à época bíblica, representando personagens, trajes de época, cenários bíblicos imponentes, iluminação dramática (golden hour, chiaroscuro) e estética cinematográfica 8K."
        img_prompt_rule = "iniciando pela DESCRIÇÃO DA CENA HISTÓRICA e colocando a especificação técnica de iluminação/estética no final."
        vid_prompt_rule = "iniciando pela DESCRIÇÃO DA AÇÃO E MOVIMENTO DOS PERSONAGENS na cena e colocando as especificações técnicas de câmera e vídeo no final."
        vid_example = "[V] Job standing in his tunic looking at the vast desert sunset in ancient Uz as his livestock grazes in the distance, cinematic 8K video, hyper-realistic historical reconstruction, epic lighting, smooth camera panning, slow motion"
    elif channel_code == "B1":
        channel_name = "Bíblico Ilustrado (B1)"
        visual_style = "Video Scribe, Whiteboard Explainer (Desenho Explicativo). Ilustrações didáticas COLORIDAS (vibrant colors), preenchimento com cores vivas e suaves, traços pretos limpos e marcantes em fundo branco puro."
        img_prompt_rule = "iniciando pela DESCRIÇÃO DA CENA e colocando as especificações técnicas no final."
        vid_prompt_rule = "iniciando pela DESCRIÇÃO DA AÇÃO DO DESENHO na tela e colocando as especificações técnicas no final."
        vid_example = "[V] Colorful whiteboard scribe animation of Job praying in ancient Uz, smooth drawing effect, colorful digital line art on pure white background, no hands, no pens"
    else:
        channel_name = f"Canal Cinematográfico ({channel_code})"
        visual_style = f"Reconstrução histórica e estética por IA para o canal {channel_code}."
        img_prompt_rule = "iniciando pela descrição da cena com detalhes técnicos no final."
        vid_prompt_rule = "iniciando pela descrição da ação visual com especificações técnicas no final."
        vid_example = f"[V] Cinematic scene for {channel_code} showing realistic historical reconstruction, 8K video, cinematic camera movement, dramatic lighting"

    # Build Mode-Specific Prompt
    if is_video:
        target_model = "Veo 3 (Vídeo Cinematográfico)"
        specific_rules = f"""1. Leia o arquivo 'legenda.srt' anexo. Cada bloco do SRT corresponde a EXATAMENTE 1 Vídeo.
2. Para CADA bloco do SRT, gere 1 prompt detalhado de vídeo em Inglês para o Veo 3 {vid_prompt_rule}
3. ESTRUTURA OBRIGATÓRIA DO PROMPT DE VÍDEO:
   - PRIMEIRO: Descreva a AÇÃO E CENA DO VÍDEO (o que se vê, os personagens agindo, o movimento físico e o ambiente).
   - FINAL: Adicione as ESPECIFICAÇÕES TÉCNICAS DE VÍDEO E CÂMERA no final do prompt (ex: , cinematic 8K video, hyper-realistic historical reconstruction, epic dramatic lighting, smooth cinematic camera panning, slow motion).
4. Inicie CADA linha do prompt gerado obrigatoriamente com a tag [V].
5. O número total de prompts gerados DEVE ser EXATAMENTE igual ao número de blocos do arquivo SRT (N blocos = N Prompts)."""
        example = vid_example
    else:
        target_model = "nano banana 2"
        specific_rules = f"""1. Leia o arquivo 'legenda.srt' anexo. Cada bloco do SRT corresponde a EXATAMENTE 1 Imagem.
2. Para CADA bloco do SRT, gere 1 prompt detalhado de imagem em Inglês para o nano banana 2 {img_prompt_rule}
3. ESTRUTURA OBRIGATÓRIA DO PROMPT:
   - PRIMEIRO: Descreva a CENA (o que se vê, os personagens, as ações e os objetos).
   - FINAL: Adicione as ESPECIFICAÇÕES TÉCNICAS no final do prompt.
4. Inicie CADA linha do prompt gerado obrigatoriamente com a tag [I].
5. O número total de prompts gerados DEVE ser EXATAMENTE igual ao número de blocos do arquivo SRT (N blocos = N Prompts)."""
        example = "[I] Job kneeling and praying reverently under a peaceful sky in ancient Uz, surrounded by his livestock, colorful whiteboard explainer illustration, vibrant colorized line art on pure white background, no borders, no frame, no hands, no pens"

    instruction_text = f"""Você é um Engenheiro de Prompts especialista em geração de assets visuais para o {target_model}.

{channel_name}: {visual_style} Vamos usar vídeos [V] iniciando cada prompt com [V].

REGRAS DE PROCESSAMENTO DO ARQUIVO SRT:
{specific_rules}

FORMATO DE SAÍDA EXCLUSIVO:
Retorne APENAS os prompts em Inglês. NÃO inclua títulos, cabeçalhos, marcadores de bloco (ex: ---), timestamps, números de bloco ou texto falado. Apenas um prompt por linha, quebrando uma linha entre um prompt e outro.

Exemplo de saída esperada:
{example}
{example}

Analise o arquivo 'legenda.srt' anexo e gere a lista completa de prompts agora.
"""
    return instruction_text

if __name__ == "__main__":
    print(get_gemini_instructions("BC", "V"))
