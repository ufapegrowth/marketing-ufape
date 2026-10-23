---
description: Quando uma turma for liberada para o marketing com verba de mídia. Cadeia: gestor-de-midia -> estrategia-de-midia -> criativos-de-anuncio -> anuncios-meta -> anuncios-google -> anuncios-tiktok -> anuncios-linkedin -> qa-de-marketing
argument-hint: [linha] [curso e turma]
---
Execute o workflow "Plano de mídia da turma".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha, curso e turma deste pedido: $ARGUMENTS

1. Use o agente gestor-de-midia para produzir o plano de mídia da turma: metas pela skill metas-de-custo em três cenários, avaliação de Meta, Google e YouTube, TikTok e LinkedIn para esta turma, canais ativados e fora (com motivo), verba por canal e por semana, calendário até o início da turma e encomendas a cada agente. Salve e passe o arquivo para a próxima etapa.
2. Use o agente estrategia-de-midia para produzir o plano detalhado por canal ativado, com funil reverso, checkpoints e critérios de decisão. Salve e passe o arquivo para a próxima etapa.
3. Use o agente criativos-de-anuncio para produzir os conceitos e a matriz de criativos pela skill matriz-de-criativos, no formato de cada canal ativado. Salve e passe o arquivo para a próxima etapa.
4. Use o agente anuncios-meta para produzir a estrutura de Meta Ads, se a Meta foi ativada; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
5. Use o agente anuncios-google para produzir a estrutura de Google Ads e YouTube Ads, se o Google foi ativado; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
6. Use o agente anuncios-tiktok para produzir a estrutura de TikTok Ads, se o TikTok foi ativado; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
7. Use o agente anuncios-linkedin para produzir a estrutura de LinkedIn Ads, se o LinkedIn foi ativado; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
8. Use o agente qa-de-marketing para revisar textos, links, UTMs, conversões e conformidade de tudo. Salve e passe o arquivo para a próxima etapa.
9. Rode auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano da turma, criativos e estruturas dos canais ativados aprovados e entregues para um humano montar, com metas escritas antes de subir e o relatório semanal ao CMO agendado na revisão de segunda-feira.
