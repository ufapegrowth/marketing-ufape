---
description: Toda segunda-feira, para revisar a mídia paga da semana anterior. Cadeia: gestor-de-midia -> analise-de-midia -> criativos-de-anuncio -> estrategia-de-midia -> gestor-de-midia
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Revisão semanal de mídia".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente gestor-de-midia para produzir a abertura da revisão: metas vigentes, canais ativos, verba gasta x planejada e o que mudou na semana (verba, criativos, página, rastreamento). Salve e passe o arquivo para a próxima etapa.
2. Use o agente analise-de-midia para produzir a revisão de mídia a partir das exportações dos canais ativos e do CRM, seguindo a skill diagnostico-de-midia (.claude/skills/diagnostico-de-midia/SKILL.md): regra dos dados suficientes, funil de cima para baixo e decisão escalar, manter, ajustar, pausar ou investigar por item. Salve e passe o arquivo para a próxima etapa.
3. Use o agente criativos-de-anuncio para produzir as variações que substituem os criativos cansados, no formato de cada canal. Salve e passe o arquivo para a próxima etapa.
4. Use o agente estrategia-de-midia para produzir o ajuste do plano e da divisão de verba, dentro da verba aprovada. Salve e passe o arquivo para a próxima etapa.
5. Use o agente gestor-de-midia para produzir o relatório semanal ao CMO (até 200 palavras, com fatos, hipóteses e dados que faltam) e a lista de mudanças em rascunho para aprovação humana. Salve e passe o arquivo para a próxima etapa.
6. Rode auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: decisões por canal aprovadas e entregues para um humano executar, criativos novos prontos para os cansados e relatório ao CMO entregue.
