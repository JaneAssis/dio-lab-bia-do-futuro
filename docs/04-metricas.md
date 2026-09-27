# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Usuário fez a pergunta e recebeu a resposta correta. |
| **Segurança** | O agente evitou inventar informações? | Ao ser perguntado de algo fora do escopo, informou que não sabia. |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugeriu peças de roupas baseados no biotipo definido. |
---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Pergunta de medição.
- **Pergunta:** como me medir?
- **Resposta esperada:** traz as informações do `guia_medição`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Medidas definidas.
- **Pergunta:** busto 55 quadril 88 cintura 44
- **Resposta esperada:** Resposta compatível com definições feitas no código.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que possui expertise limitada e sugere que cliente consulte sites de clima.
- **Resultado:** [ ] Correto  [ ] Incorreto  [x] Parcialmente correto

### Teste 4: Informação inexistente
- **Pergunta:** roupas que combinem com tipo de corpo coração
- **Resposta esperada:** Confunde o tipo de corpo citado (que não existe) com um tipo encontrado e recomenda peças.
- **Resultado:** [ ] Correto  [x] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- perguntas diretas ao conteúdo;
- dúvidas associadas ao formato de corpos;
- recomendações de peças;
- dúvidas sobre roupas que não estão no database mas que estão associadas aos tipos de corpos;

**O que pode melhorar:**
- aumentar o número de parâmetros;
- prompts mais acertivos;
- listas de palavras maiores;

---
