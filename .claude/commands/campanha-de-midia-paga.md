---
description: Nova campanha de captação com verba aprovada. Cadeia: estrategia-de-midia -> criativos-de-anuncio -> anuncios-meta -> anuncios-google -> qa-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Campanha de mídia paga".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente estrategia-de-midia para produzir o plano de mídia a partir de templates/briefing-de-midia.md, começando pelas metas de CPL e de custo por matrícula da skill metas-de-custo (.claude/skills/metas-de-custo/SKILL.md), em três cenários. Salve e passe o arquivo para a próxima etapa.
2. Use o agente criativos-de-anuncio para produzir os conceitos, roteiros e a matriz de criativos pela skill matriz-de-criativos (conceitos que mudam pelo menos duas das 5 dimensões). Salve e passe o arquivo para a próxima etapa.
3. Use o agente anuncios-meta para produzir a estrutura de Meta Ads. Salve e passe o arquivo para a próxima etapa.
4. Use o agente anuncios-google para produzir a estrutura de Google Ads. Salve e passe o arquivo para a próxima etapa.
5. Use o agente qa-de-marketing para revisar textos, links, UTMs e conversões de tudo. Salve e passe o arquivo para a próxima etapa.
6. Rode auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano, criativos e estruturas de Meta e Google aprovados e entregues para um humano montar nas plataformas, com metas escritas antes de subir.
