---
description: Última sexta-feira do mês. Cadeia: qa-de-marketing -> arquiteto-de-fluxos
argument-hint: [linha ou geral] [mês]
---
Execute o workflow "Arrumação mensal".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente qa-de-marketing para produzir a checagem por amostragem das saídas aprovadas no mês passado, com o que voltou para correção e por quê. Salve e passe o arquivo para a próxima etapa.
2. Use o agente arquiteto-de-fluxos para produzir as correções dos workflows que mais geraram retrabalho (etapas a cortar, juntar ou reforçar). Salve e passe o arquivo para a próxima etapa.
3. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: a checagem do mês está aprovada e cada workflow com retrabalho tem uma correção proposta.
