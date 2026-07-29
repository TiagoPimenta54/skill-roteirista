# Skill Roteirista (Antigravity)

Skill para **Google Antigravity** focada em criação automatizada de roteiros para canais do YouTube (Bíblico Ilustrado e Bíblico Cinematográfico), narração por IA via **DarkPlanner API** e geração de prompts para **nano banana 2** (imagens) e **Veo 3** (vídeos).

---

## 🚀 Funcionalidades principais

1. **Entrada flexível**:
   - `B1`: **Bíblico Ilustrado** -> Prompts no estilo Video Scribe / Whiteboard Explainer coloridos para o **nano banana 2** (`[I]`).
   - `BC` (ou `B2`): **Bíblico Cinematográfico** -> Prompts de reconstrução histórica por IA para o **Veo 3** (`[V]`).

2. **Verificação Pré-Narração Estrita**:
   - Validação de idioma (`Idioma do Roteiro == Idioma do Título`).
   - Validação de contagem de palavras (base `140 WPM` com faixa de tolerância de `±20%`).

3. **Integração Narração (DarkPlanner API)**:
   - Suporte oficial à voz `Valentino` (`dc674015-b94c-4078-9538-4a7d1d612ce9`).
   - Download automático do arquivo de áudio `narracao.mp3`.

4. **Legenda SRT e Ritmo Visual (Pacing)**:
   - Geração de `legenda.srt` ritmada.
   - Pacing: **3 a 6s** no primeiro minuto; **7 a 9.5s** (`[V]`) ou **4 a 15s** (`[I]`) após 1 minuto.

5. **Instruções no Chat para Gemini Online**:
   - Instruções em prosa direta, sem cabeçalhos ou timestamps desnecessários.
   - Prompts iniciando obrigatoriamente pela **descrição da cena/ação** e especificações técnicas no final.

---

## 🛠️ Estrutura de Arquivos

- `SKILL.md`: Definição e contrato da skill no Antigravity.
- `scripts/processor.py`: Parser, validação de WPM, DarkPlanner API e exportação de downloads.
- `scripts/templates.py`: Gerador de prompts para Gemini Online (nano banana 2 / Veo 3).
- `scripts/run_roteirista.py`: Executor do pipeline completo.

---

## 📦 Como Usar

Envie no chat do Antigravity no formato:
```text
A historia de JO, B1 10MIN
```
ou para o estilo cinematográfico:
```text
A historia de JO, BC 10MIN
```
