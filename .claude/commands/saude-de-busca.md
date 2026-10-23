---
description: Rode todo mês. Cadeia: seo-tecnico -> seo-on-page -> links-e-autoridade -> seo-on-page -> desempenho-de-conteudo
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Saúde de busca".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente seo-tecnico para produzir a auditoria técnica, com a leitura do Search Console pela skill leitura-do-search-console (.claude/skills/leitura-do-search-console/SKILL.md) quando houver exportação e a checagem da skill canibalizacao (.claude/skills/canibalizacao/SKILL.md). Salve e passe o arquivo para a próxima etapa.
2. Use o agente seo-on-page para produzir as correções das 5 principais páginas (priorize as páginas de curso). Salve e passe o arquivo para a próxima etapa.
3. Use o agente links-e-autoridade para produzir as correções de links internos e a lista de menções da skill mencoes-e-citacoes (.claude/skills/mencoes-e-citacoes/SKILL.md). Salve e passe o arquivo para a próxima etapa.
4. Use o agente seo-on-page para produzir a checagem de visibilidade em IA das perguntas prioritárias, pela skill visibilidade-em-ia (.claude/skills/visibilidade-em-ia/SKILL.md), com o roteiro de checagem manual. Salve e passe o arquivo para a próxima etapa.
5. Use o agente desempenho-de-conteudo para produzir o placar do conteúdo de busca. Salve e passe o arquivo para a próxima etapa.
6. Rode a auditoria do departamento (auditorias/03-busca.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: a lista de correções foi entregue ao responsável pelo site.
