# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `estilos_moda.json` | JSON | Consulta 5 estilos disponíveis na base. |
| `guia_medicao.json` | JSON | Possui as instruções de como o usuário pode descobrir o tipo de corpo através das medidas. |
| `recomendacoes_corpo.json` | JSON | Informa as peças boas/ruins de acordo com o formato corporal do usuário. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Como esse assistente virtual é focado em moda, todos os dados mockados foram substituídos. 
> [!TIP]
> Para mais informações confira os dados utilizados na pasta `data`!

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON utilizados no projeto são lidos automaticamente na pasta `data` pela biblioteca JSON no inicio do script e unido ao `dataset_moda`.

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

```python
{
  "guia_medicao_fita_metrica": {
    "instrucoes_gerais": "Para descobrir o tipo de corpo, use uma fita métrica sem apertar a pele.",
    "passos_medicao": [
      "1. Ombro/Busto: Meça na parte mais larga do peito/ombros.",
      "2. Cintura: Meça a parte mais estreita do tronco.",
      "3. Quadril: Meça na parte mais larga do bumbum/quadril."
    ]
  },
  "estilos_disponiveis": [
    {
      "nome_estilo": "Casual (Clean Girl / Clean Boy)",
      "descricao": "Visual minimalista, básico e alinhado.",
      "pecas_chave": ["Camisetas básicas de algodão pesado", "Tênis branco minimalista"]
    }
  ],
  "recomendacoes_por_corpo": [
    {
      "tipo_corpo": "Triângulo Invertido",
      "foco": "Trazer volume para a parte de baixo do corpo.",
      "sugestoes": ["Calças pantalona", "Saias evasê"],
      "evitar": ["Ombreiras muito exageradas"]
    }
  ]
}
```
