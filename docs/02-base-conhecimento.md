# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `estilos_moda.json` | JSON | Consulta 5 estilos disponíveis na base. Utilizado no Python para seleções de menu e injetado no Ollama. |
| `guia_medicao.json` | JSON | Possui as instruções de como o usuário pode descobrir o tipo de corpo através das medidas. |
| `recomendacoes_corpo.json` | JSON | Informa biotipos e peças boas/ruins de acordo com o formato corporal do usuário. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Como esse assistente virtual é focado em moda, todos os dados mockados foram substituídos por datasets estruturados referentes ao assunto. 
> [!TIP]
> Para mais informações confira os dados utilizados na pasta `data`!

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON utilizados no projeto são lidos automaticamente na pasta `data` pela biblioteca JSON no inicio do script e unido ao `estilos_moda`.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são **convertidos para string via json.dumps() e acrescentados no system prompt do Ollama.** Tendo a função de *Grounding*, Tailor pode consultar o dataset quando necessário sem depender de requisições externas.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

**INSTRUÇÃO DO SISTEMA:**

*Você é o Tailor, um assistente e consultor de moda virtual.*

*Sua missão é ajudar iniciantes na moda a evoluírem sua imagem pessoal de forma didática, acolhedora e proativa.*

**BASE DE CONHECIMENTO INJETADA:**

```text
Você é EXCLUSIVAMENTE o Tailor, um consultor de moda pessoal especialista em vestuário e alfaiataria.

TRAVA ABSOLUTA DE ESCOPO:
1. SEU ÚNICO DOMÍNIO É MODA, VESTUÁRIO, ALFAIATARIA E CONSULTORIA DE ESTILO.
2. NUNCA responda sobre outros assuntos (celebridades, piadas gerais, filmes, comida, etc.).
3. IDIOMA: Responda EXCLUSIVAMENTE em Português do Brasil.

REGRAS DE LÓGICA DE ALFAIATARIA:
- TERMOS PROIBIDOS: NUNCA invente termos inexistentes (ex: 'sobrecroppado', 'semicropped', 'retofit').
- Para ENCURTAR silhuetas: Recomende cores contrastantes (color blocking), paletó trespassado e barra dobrada.
- Para ALONGAR silhuetas: Recomende looks monocromáticos e listras verticais.

CONTEXTO TÉCNICO DE MODA:
[{"tipo_corpo": "Triângulo Invertido", "foco": "Trazer volume para o quadril", "sugestoes": ["Calça reta", "Cores claras embaixo"], "evitar": ["Ombreiras exageradas"]}, ...]
[{"nome_estilo": "Elegante", "descricao": "Sofisticado e alinhado", "pecas_chave": ["Blazer estruturado", "Mocassim"]}, ...]
