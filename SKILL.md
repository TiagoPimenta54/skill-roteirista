---
name: roteirista
description: Skill Roteirista automatiza a criação de roteiros para canais do YouTube (B1=Bíblico Ilustrado, B2=Bíblico Cinematográfico, C=Outros canais). Realiza verificação pré-narração estrita (Idioma do Roteiro = Idioma do Título e Contagem de Palavras a 140 WPM com tolerância de ±20%). Gera áudio via DarkPlanner API (voz Valentino), produz legenda SRT ritmada ([I]=Imagem, [V]=Vídeo) e exporta a pasta na Downloads com narracao.mp3 e legenda.srt. Exibe no chat a instrução em prosa para o Gemini Online (nano banana 2 para imagens [I] e Veo 3 para vídeos [V]), com regras para o B1 (DESCRIÇÃO DA CENA PRIMEIRO, ESPECIFICAÇÕES TÉCNICAS NO FINAL, COLORIDO, SEM BORDAS/MOLDURAS, SEM MÃOS/CANETAS E SEM MENÇÃO A 16:9).
---

# Skill Roteirista: Roteiros Bíblicos & Automação de Assets Visuais

Esta skill transforma um título recebido no formato especificado em um roteiro completo, realiza a **Verificação Pré-Narração Estrita** (idioma e quantidade de palavras com ±20% de tolerância a 140 WPM), envia a narração para a DarkPlanner API, constrói a legenda `.srt` ritmada e exporta os arquivos na pasta `Downloads`.

## Sintaxe de Entrada
`<Titulo>, <Codigo_Canal> <Duracao>`

*Exemplos*:
- `A historia de JO, B1 10MIN` -> Roteiro em **Português**, Canal Bíblico Ilustrado (`B1`), 10 minutos.
- `The Story of Job, B2 10MIN` -> Roteiro em **Inglês**, Canal Bíblico Cinematográfico (`B2`), 10 minutos.

---

## Estrutura Otimizada dos Prompts (`B1` - nano banana 2):
1. **DESCRIÇÃO DA CENA PRIMEIRO**: O prompt deve sempre iniciar descrevendo o que se vê na cena (personagens, ações, ambiente).
2. **ESPECIFICAÇÕES TÉCNICAS NO FINAL**: As diretrizes técnicas entram no final do prompt (ex: `, colorful whiteboard explainer illustration, vibrant colorized line art on pure white background, no borders, no frame, no hands, no pens`).
3. **SEM 16 POR 9**: Não incluir a menção `16:9` ou `16 por 9` nos prompts.
4. **COLORIDO & SEM FERRAMENTAS**: Desenho colorido em fundo branco, sem bordas, sem molduras de quadro, sem mãos humanas e sem canetas.
