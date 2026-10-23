---
description: Rode quando uma etapa da jornada do aluno não tem régua. Cadeia: jornada-do-aluno -> copy-de-mensagens -> qa-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Nova régua de relacionamento".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente jornada-do-aluno para produzir o mapa da etapa, com a lista de gatilhos e etiquetas do CRM e do Chatwoot que a equipe vai configurar. Salve e passe o arquivo para a próxima etapa.
2. Use o agente copy-de-mensagens para produzir os rascunhos de e-mail e WhatsApp. Salve e passe o arquivo para a próxima etapa.
3. Use o agente qa-de-marketing para produzir a revisão de qualidade. Salve e passe o arquivo para a próxima etapa.
4. Rode auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: régua pronta para ser ativada depois da sua revisão.
