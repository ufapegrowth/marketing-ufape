---
description: Última sexta-feira do mês. Cadeia: organizacao-de-sistemas -> documentacao -> qa-de-marketing -> arquiteto-de-fluxos
argument-hint: [linha ou geral] [mês]
---
Execute o workflow "Arrumação mensal".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente organizacao-de-sistemas para produzir as propostas de arrumação (mudanças de lugar e arquivamento, nunca exclusão). Salve e passe o arquivo para a próxima etapa.
2. Use o agente documentacao para produzir as atualizações dos documentos. Salve e passe o arquivo para a próxima etapa.
3. Use o agente qa-de-marketing para produzir a checagem por amostragem das saídas do mês passado. Salve e passe o arquivo para a próxima etapa.
4. Use o agente arquiteto-de-fluxos para produzir as correções dos fluxos. Salve e passe o arquivo para a próxima etapa.
5. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: pastas arrumadas, conhecimento/INDICE.md atualizado e documentos em dia.
