---
description: Rode quando houver um tema do calendário aprovado. Cadeia: briefing-de-conteudo -> conteudo-longo -> editor-de-conteudo -> qa-de-marketing -> reaproveitamento
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Ideia a artigo publicado".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente briefing-de-conteudo para produzir o briefing. Salve e passe o arquivo para a próxima etapa.
2. Use o agente conteudo-longo para produzir o rascunho. Salve e passe o arquivo para a próxima etapa.
3. Use o agente editor-de-conteudo para produzir o rascunho editado. Salve e passe o arquivo para a próxima etapa.
4. Use o agente qa-de-marketing para produzir a revisão de QA. Salve e passe o arquivo para a próxima etapa.
5. Use o agente reaproveitamento para produzir o pacote de reaproveitamento. Salve e passe o arquivo para a próxima etapa.
6. Rode a auditoria do departamento (auditorias/04-qualidade-de-conteudo.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: o artigo está publicado e o pacote de reaproveitamento está agendado.
