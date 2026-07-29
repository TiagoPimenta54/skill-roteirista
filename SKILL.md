---
name: roteirista
description: Skill Roteirista automatiza a criação de roteiros para canais do YouTube (B1=Bíblico Ilustrado, BC/B2=Bíblico Cinematográfico, C=Outros canais). Realiza verificação pré-narração estrita (Idioma do Roteiro = Idioma do Título e Contagem de Palavras a 140 WPM com tolerância de ±20%). Gera áudio via DarkPlanner API (voz Valentino), produz legenda SRT ritmada ([I]=Imagem, [V]=Vídeo) e exporta a pasta na Downloads com narracao.mp3 e legenda.srt. Exibe no chat a instrução para o Gemini Online (nano banana 2 para imagens [I] e Veo 3 para vídeos [V] com PROSA FLUIDA E LINGUAGEM NATURAL SEM TAGS SEPARADAS POR VÍRGULA).
---

# Skill Roteirista: Roteiros Bíblicos & Automação de Assets Visuais

Esta skill transforma um título recebido no formato especificado em um roteiro completo, realiza a **Verificação Pré-Narração Estrita** (idioma e quantidade de palavras com ±20% de tolerância a 140 WPM), envia a narração para a DarkPlanner API, constrói a legenda `.srt` ritmada e exporta os arquivos na pasta `Downloads`.

## Sintaxe de Entrada
`<Titulo>, <Codigo_Canal> <Duracao>`

*Exemplos*:
- `A historia de JO, B1 10MIN` -> Roteiro em **Português**, Canal Bíblico Ilustrado (`B1`), 10 minutos.
- `A historia de JO, BC 10MIN` -> Roteiro em **Português**, Canal Bíblico Cinematográfico (`BC`), 10 minutos.

---

## Regras de Prompts para o Veo 3 (Vídeos - `[V]`):
- **PROSA FLUIDA E LINGUAGEM NATURAL**: Prompts de vídeo para o Veo 3 devem ser escritos como uma frase/narrativa visual descritiva contínua em Inglês.
- **PROIBIDO TAGS SEPARADAS POR VÍRGULA**: Não usar listas robóticas de tags como `, 8k, photorealistic, slow motion, cinematic panning`.
- Integre o enquadramento, a ação dos personagens, a iluminação e o movimento de câmera de forma natural e fluida dentro da frase.
