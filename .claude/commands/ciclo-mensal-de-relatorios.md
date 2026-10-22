---
description: Último dia útil do mês. Cadeia: analista-de-dados -> analise-de-campanha -> desempenho-de-conteudo -> relatorios -> backlog-de-otimizacao
argument-hint: [linha ou geral] [mês]
---
Execute o workflow "Ciclo mensal de relatórios".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente analista-de-dados para produzir os dados limpos e os insights (custo por lead, custo por matrícula, conversão lead para matrícula e receita da linha). Salve e passe o arquivo para a próxima etapa.
2. Use o agente analise-de-campanha para produzir as revisões das campanhas do mês. Salve e passe o arquivo para a próxima etapa.
3. Use o agente desempenho-de-conteudo para produzir o placar de conteúdo. Salve e passe o arquivo para a próxima etapa.
4. Use o agente relatorios para produzir o relatório de uma página, com templates/relatorio-mensal.md. Salve e passe o arquivo para a próxima etapa.
5. Use o agente backlog-de-otimizacao para produzir o backlog dos próximos 30 dias. Salve e passe o arquivo para a próxima etapa.
6. Rode a auditoria do departamento (auditorias/09-analytics.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: relatório e backlog compartilhados.
