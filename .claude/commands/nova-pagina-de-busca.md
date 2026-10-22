---
description: Rode quando houver uma palavra-chave prioritária sem página. Cadeia: pesquisa-de-palavras-chave -> lacunas-de-conteudo -> briefing-de-conteudo -> conteudo-longo -> seo-on-page -> qa-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Nova página de busca".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente pesquisa-de-palavras-chave para produzir a palavra-chave escolhida. Salve e passe o arquivo para a próxima etapa.
2. Use o agente lacunas-de-conteudo para produzir o encaixe no cluster. Salve e passe o arquivo para a próxima etapa.
3. Use o agente briefing-de-conteudo para produzir o briefing. Salve e passe o arquivo para a próxima etapa.
4. Use o agente conteudo-longo para produzir o rascunho. Salve e passe o arquivo para a próxima etapa.
5. Use o agente seo-on-page para produzir o rascunho otimizado. Salve e passe o arquivo para a próxima etapa.
6. Use o agente qa-de-marketing para produzir a revisão de QA. Salve e passe o arquivo para a próxima etapa.
7. Rode a auditoria do departamento (auditorias/03-busca.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: a página está no ar e recebe link da sua página pilar (em geral, a página do curso ou da área).
