---
description: Fim de campanha ou ponto de checagem (por exemplo, fim do vestibular ou fechamento de turma de pós). Cadeia: analise-de-campanha -> analista-de-dados -> backlog-de-otimizacao -> relatorios
argument-hint: [linha] [campanha ou curso]
---
Execute o workflow "Revisão pós-campanha".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente analise-de-campanha para produzir as metas versus realizado (leads, inscrições, matrículas, custo por lead e custo por matrícula). Salve e passe o arquivo para a próxima etapa.
2. Use o agente analista-de-dados para produzir os recortes mais profundos (por canal, curso, público e tempo entre lead e matrícula). Salve e passe o arquivo para a próxima etapa.
3. Use o agente backlog-de-otimizacao para produzir a lista manter, mudar, parar, priorizada pela skill matriz-gut (.claude/skills/matriz-gut/SKILL.md). Salve e passe o arquivo para a próxima etapa.
4. Use o agente relatorios para produzir o registro dos aprendizados para a diretoria (o que manter, mudar e parar na próxima campanha). Salve e passe o arquivo para a próxima etapa.
5. Rode a auditoria do departamento (auditorias/09-analytics.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: o registro dos aprendizados está aprovado e pronto para entrar no próximo briefing de campanha.
