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
    is_video = mode_str in ["V", "2", "VIDEO", "VIDEOS"] or True

    # 1. Determine Channel Style
    if channel_code in ["B2", "BC", "BIBLICO_CINEMATOGRAFICO"]:
        channel_name = "Bíblico Cinematográfico (BC)"
        visual_style = "Reconstrução histórica hiper-realista por IA. Fidelidade total à época bíblica (trajes de época, personagens, arquitetura bíblica, iluminação dramática natural)."
        vid_prompt_rule = "em PROSA FLUIDA E LINGUAGEM NATURAL CINEMATOGRÁFICA. OBRIGATÓRIO: NÃO use listas de palavras-chave ou tags separadas por vírgula (como ', 8k, photorealistic, slow motion'). Integre o movimento de câmera, a iluminação e a ação dos personagens de forma fluida em uma frase descritiva contínua."
        vid_example = "[V] A smooth cinematic camera shot glides slowly past ancient stone pillars at golden hour, revealing Job in traditional period garments praying quietly as a warm breeze moves his tunic."
        img_prompt_rule = "iniciando pela descrição da cena e colocando especificações técnicas no final."
    elif channel_code == "B1":
        channel_name = "Bíblico Ilustrado (B1)"
        visual_style = "Video Scribe, Whiteboard Explainer COLORIDO em fundo branco limpo."
        vid_prompt_rule = "em prosa fluida descrevendo o desenho sendo animado na tela em tempo real sem usar tags separadas por vírgula."
        vid_example = "[V] A vivid whiteboard scribe animation smoothly draws Job praying in ancient Uz with colorful digital lines on a clean white background, free of hands or drawing tools."
        img_prompt_rule = "iniciando pela descrição da cena e colocando especificações técnicas no final."
    else:
        channel_name = f"Canal Cinematográfico ({channel_code})"
        visual_style = f"Reconstrução estética por IA adaptada para o canal {channel_code}."
        vid_prompt_rule = "em linguagem natural fluida sem tags separadas por vírgula."
        vid_example = f"[V] A cinematic video shot glides past the historic scene for {channel_code}, depicting characters and atmosphere naturally in motion."
        img_prompt_rule = "iniciando pela descrição da cena com especificações no final."

    # Build Mode-Specific Prompt
    if is_video:
        target_model = "Veo 3 (Vídeo Cinematográfico)"
        specific_rules = f"""1. Leia o arquivo 'legenda.srt' anexo. Cada bloco do SRT corresponde a EXATAMENTE 1 Vídeo.
2. Para CADA bloco do SRT, gere 1 prompt detalhado de vídeo em Inglês para o Veo 3 {vid_prompt_rule}
3. REGRAS OBRIGATÓRIAS PARA O VEO 3 (PROSA FLUIDA):
   - PROIBIDO USAR TAGS SEPARADAS POR VÍRGULA: NÃO escreva ', 8k, photorealistic, hyper-realistic, slow motion, cinematic panning' no final do prompt.
   - LINGUAGEM NATURAL E CONTÍNUA: Integre o tipo de enquadramento, a ação dos personagens, a iluminação e o movimento de câmera em um único parágrafo/frase fluida e visual em Inglês.
4. Inicie CADA linha do prompt gerado obrigatoriamente com a tag [V].
5. O número total de prompts gerados DEVE ser EXATAMENTE igual ao número de blocos do arquivo SRT (N blocos = N Prompts)."""
        example = vid_example
    else:
        target_model = "nano banana 2"
        specific_rules = f"""1. Leia o arquivo 'legenda.srt' anexo. Cada bloco do SRT corresponde a EXATAMENTE 1 Imagem.
2. Para CADA bloco do SRT, gere 1 prompt detalhado de imagem em Inglês para o nano banana 2 {img_prompt_rule}
3. Inicie CADA linha do prompt gerado obrigatoriamente com a tag [I].
4. O número total de prompts gerados DEVE ser EXATAMENTE igual ao número de blocos do arquivo SRT (N blocos = N Prompts)."""
        example = "[I] Job kneeling and praying reverently under a peaceful sky in ancient Uz, surrounded by his livestock, colorful whiteboard explainer illustration, vibrant colorized line art on pure white background, no borders, no frame, no hands, no pens"

    instruction_text = f"""Você é um Engenheiro de Prompts especialista em geração de assets visuais para o {target_model}.

{channel_name}: {visual_style} Vamos usar vídeos [V] iniciando cada prompt com [V].

REGRAS DE PROCESSAMENTO DO ARQUIVO SRT:
{specific_rules}

FORMATO DE SAÍDA EXCLUSIVO:
Retorne APENAS os prompts em Inglês. NÃO inclua títulos, cabeçalhos, marcadores de bloco (ex: ---), timestamps, números de bloco ou texto falado. Apenas um prompt por linha, quebrando uma linha entre um prompt e outro.

Exemplo de saída esperada:
{example}
[V] A dramatic low-angle camera shot tracks a messenger running frantically across the dusty desert valley of Uz to deliver urgent news to Job under a tempestuous sky.

Analise o arquivo 'legenda.srt' anexo e gere a lista completa de prompts agora.
"""
    return instruction_text

if __name__ == "__main__":
    print(get_gemini_instructions("BC", "V"))
