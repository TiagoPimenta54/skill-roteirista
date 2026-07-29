---
name: roteirista
description: Skill Roteirista automatiza a criação de roteiros para canais do YouTube (B1=Bíblico Ilustrado, BC/B2=Bíblico Cinematográfico, C=Outros canais). Realiza verificação pré-narração estrita (Idioma do Roteiro = Idioma do Título e Contagem de Palavras a 140 WPM com tolerância de ±20%). Gera áudio via DarkPlanner API (voz Valentino), produz legenda SRT LIMPA (sem tags nas legendas) e exporta a pasta na Downloads com narracao.mp3 e legenda.srt. Exibe no chat a instrução para o Gemini Online que gera os prompts com a tag [I] (nano banana 2) ou [V] (Veo 3).
---

# Skill Roteirista: Roteiros Bíblicos & Automação de Assets Visuais

Esta skill transforma um título recebido no formato especificado em um roteiro completo, realiza a **Verificação Pré-Narração Estrita** (idioma e quantidade de palavras com ±20% de tolerância a 140 WPM), envia a narração para a DarkPlanner API, constrói a legenda `.srt` limpa e ritmada e exporta os arquivos na pasta `Downloads`.

## Sintaxe de Entrada
`<Titulo>, <Codigo_Canal> <Duracao>`

*Exemplos*:
- `A historia de JO, B1 10MIN` -> Roteiro em **Português**, Canal Bíblico Ilustrado (`B1`), 10 minutos.
- `A historia de JO, BC 10MIN` -> Roteiro em **Português**, Canal Bíblico Cinematográfico (`BC`), 10 minutos.

---

## Estrutura Limpa dos Arquivos:
- **`legenda.srt`**: Legenda padrão **100% LIMPA**, sem prefixos `[I]`, `[V]` ou códigos dentro do texto falado da legenda.
- **Prompts do Gemini Online**: O Gemini Online lê o `legenda.srt` e gera as linhas dos prompts em inglês iniciando com `[I]` (imagens) ou `[V]` (vídeos).
