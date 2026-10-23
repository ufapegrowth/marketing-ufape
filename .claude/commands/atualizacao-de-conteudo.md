---
description: Rode todo mês. Cadeia: desempenho-de-conteudo -> seo-on-page -> editor-de-conteudo -> reaproveitamento
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Atualização de conteúdo".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente desempenho-de-conteudo para produzir a lista de peças a atualizar. Salve e passe o arquivo para a próxima etapa.
2. Use o agente seo-on-page para produzir as correções de busca de cada peça: o que está desatualizado (datas, valores, condições, anos), o que falta em relação às páginas que vencem hoje, se a intenção mudou, o bloco de resposta citável da skill briefing-seo (.claude/skills/briefing-seo/SKILL.md) e o que cortar. Salve e passe o arquivo para a próxima etapa.
3. Use o agente editor-de-conteudo para produzir os rascunhos atualizados (confira datas de vestibular, valores e condições contra contexto/catalogo-de-cursos.md). Salve e passe o arquivo para a próxima etapa.
4. Use o agente reaproveitamento para produzir os novos trechos para os canais. Salve e passe o arquivo para a próxima etapa.
5. Rode as auditorias do departamento (auditorias/04-qualidade-de-conteudo.md e auditorias/03-busca.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: as 3 principais peças antigas foram atualizadas.
