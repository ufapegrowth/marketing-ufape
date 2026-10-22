---
description: Rode quando houver um curso novo ou um mercado novo (nova área, cidade ou modalidade). Cadeia: pesquisa-de-mercado -> inteligencia-concorrencia -> insights-de-alunos -> pesquisa-de-persona
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Do mercado à persona em uma tarde".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente pesquisa-de-mercado para produzir o briefing de mercado. Salve e passe o arquivo para a próxima etapa.
2. Use o agente inteligencia-concorrencia para produzir o mapa de concorrentes. Salve e passe o arquivo para a próxima etapa.
3. Use o agente insights-de-alunos para produzir o relatório de insights. Salve e passe o arquivo para a próxima etapa.
4. Use o agente pesquisa-de-persona para produzir o perfil de persona. Salve e passe o arquivo para a próxima etapa.
5. Rode a auditoria do departamento (auditorias/01-qualidade-de-pesquisa.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: perfil de persona salvo e aprovado por você.
