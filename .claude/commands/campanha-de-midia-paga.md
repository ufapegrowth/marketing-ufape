---
description: Nova campanha de captação com verba aprovada. Cadeia: gestor-de-midia -> estrategia-de-midia -> criativos-de-anuncio -> anuncios-meta -> anuncios-google -> anuncios-tiktok -> anuncios-linkedin -> qa-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Campanha de mídia paga".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente gestor-de-midia para produzir as metas de CPL e de custo por matrícula da skill metas-de-custo (.claude/skills/metas-de-custo/SKILL.md) em três cenários, os canais ativados e fora (com motivo), a verba por canal e as encomendas a cada agente. Salve e passe o arquivo para a próxima etapa.
2. Use o agente estrategia-de-midia para produzir o plano de mídia detalhado a partir de templates/briefing-de-midia.md, dentro dos canais e da verba definidos pelo gestor. Salve e passe o arquivo para a próxima etapa.
3. Use o agente criativos-de-anuncio para produzir os conceitos, roteiros e a matriz de criativos pela skill matriz-de-criativos (conceitos que mudam pelo menos duas das 5 dimensões), no formato de cada canal ativado. Salve e passe o arquivo para a próxima etapa.
4. Use o agente anuncios-meta para produzir a estrutura de Meta Ads, se o gestor ativou a Meta; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
5. Use o agente anuncios-google para produzir a estrutura de Google Ads e YouTube Ads, se o gestor ativou o Google; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
6. Use o agente anuncios-tiktok para produzir a estrutura de TikTok Ads, se o gestor ativou o TikTok; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
7. Use o agente anuncios-linkedin para produzir a estrutura de LinkedIn Ads, se o gestor ativou o LinkedIn; se não, registre "canal não ativado" e siga. Salve e passe o arquivo para a próxima etapa.
8. Use o agente qa-de-marketing para revisar textos, links, UTMs e conversões de tudo. Salve e passe o arquivo para a próxima etapa.
9. Rode auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: metas, plano, criativos e estruturas dos canais ativados aprovados e entregues para um humano montar nas plataformas, com metas escritas antes de subir.
