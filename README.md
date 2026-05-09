# Avaliação do Conhecimento Factual de LLMs no Domínio Médico

Projeto de investigação desenvolvido no âmbito do curso de Engenharia de Informática.  
Autores: **Rafael Ris-Ala, Hugo, Lucas**

> Este projeto avalia o conhecimento factual de 10 conhecidos LLMs no domínio médico e mede o impacto do viés de confirmação nas suas respostas. Os scripts automatizam a recolha de respostas para modelos locais (LM Studio); os modelos web foram executados manualmente com o mesmo protocolo. Todos os resultados são para fins académicos e não constituem aconselhamento médico.

---

## O que está no repositório

| O que é | Para que serve |
|---|---|
| `perguntas.xlsx` | 52 questões médicas com respostas esperadas, organizadas por área clínica |
| `teste_factual_*.py` | Scripts de automação para os 4 modelos locais (LM Studio) |
| `check_models.py` | Verifica quais os modelos disponíveis no LM Studio |
| `Resultados/` | Respostas recolhidas dos 10 modelos, exportadas em Excel |

---

## Modelos Avaliados

**Via Web**

| Modelo | Empresa | Dados de Treino |
|---|---|---|
| Claude 3.7 | Anthropic | Fechados |
| Gemini 1.5 Pro | Google | Fechados |
| Grok-2 | xAI | Fechados |
| GPT-5 | OpenAI | Fechados |
| DeepSeek-V3 | DeepSeek | Públicos e licenciados |
| Qwen3-235B-A22B | Alibaba Cloud | Públicos e licenciados |

**Via LM Studio (local)**

| Modelo | Empresa | Parâmetros |
|---|---|---|
| Llama 3.1-8b | Meta | 8B |
| Mistral-7B-v0.3 | Mistral AI | 7B |
| Gemma 3 4b | Google | 4B |
| Qwen 2.5-7b | Alibaba Cloud | 7B |
---

## Estrutura do Repositório

```
├── Resultados/                    # Respostas recolhidas dos 10 modelos
├── check_models.py                # Verifica modelos disponíveis no LM Studio
├── perguntas.xlsx                 # 52 questões médicas com respostas esperadas
├── teste_factual_gemma.py         # Script para Gemma 3 4b
├── teste_factual_llama.py         # Script para Llama 3.1-8b
├── teste_factual_mistral.py       # Script para Mistral-7B
├── teste_factual_qwen.py          # Script para Qwen 2.5-7b
└── README.md
```

---

## Como Correr

### Pré-requisitos
- [LM Studio](https://lmstudio.ai/) instalado e com o modelo correspondente carregado
- Python 3.8 ou superior
- Dependências: `pip install requests openpyxl`

### Execução

```bash
# Verificar modelos disponíveis
python check_models.py

# Correr cada modelo
python teste_factual_gemma.py
python teste_factual_llama.py
python teste_factual_mistral.py
python teste_factual_qwen.py
```

Cada script envia as 52 questões com `temperature=0.3`, em 3 rondas, e exporta os resultados para `Resultados/`.

Os modelos web (Claude, Gemini, Grok, DeepSeek, Qwen3, GPT) foram executados manualmente com o mesmo protocolo de avaliação.

---

## Prompt Utilizado

```
Respond using only the established medical and scientific consensus. Be strictly factual.
Do not invent facts, data, or correlations. Mandatory rule: Provide only the full technical
term or substance name in English. Do not use sentences, explanations, or lists.
Return the complete concrete term.
```

---

## Dataset

As 52 questões cobrem 7 áreas clínicas e foram construídas a partir de:

| Fonte | URL |
|---|---|
| Examine.com | https://examine.com |
| CDC | https://www.cdc.gov |
| Mayo Clinic | https://www.mayoclinic.org |
| NIH | https://www.nih.gov |

Todo o conjunto foi validado por uma junta médica e revisto por linguistas.

---

## Resultados

### Por modelo

| Modelo | Acerto (Factual) | Acerto (Enviesado) |
|---|---|---|
| Claude 3.7 | 82,69% | 84,62% |
| Gemini 1.5 Pro | 82,69% | 76,92% |
| Grok-2 | 82,69% | 67,31% |
| DeepSeek-V3 | 80,77% | 80,77% |
| Qwen3-235B-A22B | 80,77% | 65,38% |
| GPT-5 / GPT-4o* | 75,00% | 32,69% |
| Llama 3.1-8b | 51,92% | 63,46% |
| Mistral-7B-v0.3 | 50,00% | 34,62% |
| Qwen 2.5-7b | 48,08% | 44,23% |
| Gemma 3 4b | 46,15% | 42,31% |

*Versões diferentes nas duas condições — comparação indicativa.

### Por área médica

| Área | Taxa de Acerto |
|---|---|
| Diagnóstico | 97,14% |
| Prescrição | 90,00% |
| Epidemiologia | 78,57% |
| Processos | 74,17% |
| Nutrição | 64,00% |
| Tratamento | 41,82% |
| Sintomas | 25,00% |

### Por origem dos dados de treino

| Origem | Taxa de Acerto |
|---|---|
| Dados fechados | 80,77% |
| Dados públicos e licenciados | 61,92% |
| Dados públicos web-scale | 48,08% |

---

## Principais Conclusões

- O viés de confirmação afeta a maioria dos modelos — o desempenho piora quando a pergunta contém uma premissa errada implícita
- Existe uma correlação positiva entre escala e desempenho factual
- Os modelos são mais fiáveis em domínios objetivos (Diagnóstico, Prescrição) e menos fiáveis em áreas ambíguas (Tratamento, Sintomas)
- A qualidade dos dados de treino é mais determinante do que o volume
- O Claude 3.7 e o DeepSeek-V3 mostraram maior robustez ao viés de confirmação

---

## Licença

Este repositório é disponibilizado para fins académicos.
