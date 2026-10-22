---
description: Quando houver data de vestibular, lançamento de turma ou promoção. Cadeia: estrategia-de-campanha -> estrategia-de-conteudo -> posts-sociais -> copy-de-mensagens -> analise-de-campanha
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Sprint de campanha".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente estrategia-de-campanha para produzir o briefing da campanha. Salve e passe o arquivo para a próxima etapa.
2. Use o agente estrategia-de-conteudo para produzir a lista de peças. Salve e passe o arquivo para a próxima etapa.
3. Use o agente posts-sociais para produzir as peças sociais. Salve e passe o arquivo para a próxima etapa.
4. Use o agente copy-de-mensagens para produzir os e-mails e as mensagens de WhatsApp. Salve e passe o arquivo para a próxima etapa.
5. Use o agente analise-de-campanha para produzir a revisão no ponto de checagem. Salve e passe o arquivo para a próxima etapa.
6. Rode auditorias/06-geracao-de-demanda.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: a campanha tiver rodado e sido revisada no ponto de checagem.
