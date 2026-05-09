# Avaliação do Conhecimento Factual de LLMs no Domínio Médico

Projeto de investigação desenvolvido no âmbito do curso de Engenharia de Informática
Autores: **Rafael Ris-Ala, Hugo, Lucas**

---

## Descrição

Este projeto avalia o conhecimento factual de 10 grandes modelos de linguagem (LLMs) no domínio médico, utilizando um conjunto de 52 questões validadas por especialistas.

O estudo tem dois objetivos principais:
- Determinar a taxa de acerto de cada modelo em condições neutras (prompts factuais)
- Comparar esse desempenho com respostas obtidas através de prompts enviesados, para medir o impacto do viés de confirmação

---

## Contexto 

Os LLMs estão a ser utilizados de forma crescente no apoio à decisão clínica e na disponibilização de informação médica. O viés de confirmação — a tendência dos modelos para validar premissas incorretas presentes nas perguntas — representa um risco significativo neste contexto. Este projeto avalia empiricamente esse risco em 10 modelos populares.

---

## Modelos Avaliados

| Modelo | Empresa | Dados de Treino | Interface |
|---|---|---|---|
| Claude 3.7 | Anthropic | Fechados | Web |
| Gemini 1.5 Pro | Google | Fechados | Web |
| Grok-2 | xAI | Fechados | Web |
| GPT-5 | OpenAI | Fechados | Web |
| DeepSeek-V3 | DeepSeek | Públicos e licenciados | Web |
| Qwen3-235B-A22B | Alibaba Cloud | Públicos e licenciados | Web |
| Llama 3.1-8b | Meta | Públicos e licenciados | LM Studio |
| Mistral-7B-v0.3 | Mistral AI | Públicos e licenciados | LM Studio |
| Gemma 3 4b | Google | Públicos e licenciados | LM Studio |
| Qwen 2.5-7b | Alibaba Cloud | Públicos web-scale | LM Studio |

---

## Estrutura do Repositório

```
├── Resultados/                      # Respostas recolhidas dos 10 modelos
├── check_models.py                  # Script para verificar modelos disponíveis no LM Studio
├── perguntas.xlsx                   # 52 questões médicas com respostas esperadas
├── teste_factual_gemma.py           # Script de automação para o modelo Gemma 3 4b
├── teste_factual_llama.py           # Script de automação para o modelo Llama 3.1-8b
├── teste_factual_mistral.py         # Script de automação para o modelo Mistral-7B
├── teste_factual_qwen.py            # Script de automação para o modelo Qwen 2.5-7b
└── README.md
```

---

## Como Correr os Scripts (LM Studio)

### Pré-requisitos
- [LM Studio](https://lmstudio.ai/) instalado e com o modelo correspondente carregado
- Python 3.8 ou superior
- Dependências: `pip install requests openpyxl`

### Execução

```bash
python teste_factual_gemma.py
python teste_factual_llama.py
python teste_factual_mistral.py
python teste_factual_qwen.py
```

Cada script envia as 52 questões ao modelo local com `temperature=0.3` para garantir respostas determinísticas, recolhe as respostas em 3 rondas e exporta os resultados para um ficheiro Excel na pasta `Resultados/`.

Os modelos acessíveis via web (Claude, Gemini, Grok, DeepSeek, Qwen3, GPT) foram executados manualmente, seguindo o mesmo protocolo de avaliação.

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

As 52 questões foram construídas a partir de fontes médicas de referência:
- [Examine.com](https://examine.com)
- [CDC — Centers for Disease Control and Prevention](https://www.cdc.gov)
- [Mayo Clinic](https://www.mayoclinic.org)
- [NIH — National Institutes of Health](https://www.nih.gov)

As questões cobrem 7 áreas clínicas: **Diagnóstico, Prescrição, Epidemiologia, Processos, Nutrição, Tratamento e Sintomas**.

Todo o conjunto foi validado e revisto por linguistas para garantir clareza e controlo do viés linguístico.

---

## Resultados Principais

### Taxa de acerto por modelo (condição factual)

| Modelo | Taxa de Acerto |
|---|---|
| Claude 3.7 | 82,69% |
| Gemini 1.5 Pro | 82,69% |
| Grok-2 | 82,69% |
| DeepSeek-V3 | 80,77% |
| Qwen3-235B-A22B | 80,77% |
| GPT-5 | 75,00% |
| Llama 3.1-8b | 51,92% |
| Mistral-7B-v0.3 | 50,00% |
| Qwen 2.5-7b | 48,08% |
| Gemma 3 4b | 46,15% |

### Taxa de acerto por área médica

| Área | Taxa de Acerto |
|---|---|
| Diagnóstico | 97,14% |
| Prescrição | 90,00% |
| Epidemiologia | 78,57% |
| Processos | 74,17% |
| Nutrição | 64,00% |
| Tratamento | 41,82% |
| Sintomas | 25,00% |

### Taxa de acerto por origem dos dados de treino

| Origem | Taxa de Acerto |
|---|---|
| Dados fechados | 80,77% |
| Dados públicos e licenciados | 61,92% |
| Dados públicos web-scale | 48,08% |

---

## Principais Conclusões

- O viés de confirmação afeta a maioria dos modelos — o desempenho piora quando a pergunta contém uma premissa errada implícita
- Existe uma correlação positiva entre a escala do modelo e o desempenho factual
- Os modelos são mais fiáveis em domínios com respostas objetivas (Diagnóstico, Prescrição) e menos fiáveis em áreas ambíguas (Tratamento, Sintomas)
- A qualidade dos dados de treino é mais determinante do que o volume
- O Claude 3.7 e o DeepSeek-V3 mostraram maior robustez ao viés de confirmação

---

## Licença

Este repositório é disponibilizado para fins académicos.
