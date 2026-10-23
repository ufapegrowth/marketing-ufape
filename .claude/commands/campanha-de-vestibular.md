---
description: Captação semestral da Graduação, de 8 a 10 semanas antes das provas. Cadeia: cmo -> estrategia-de-campanha -> estrategia-de-oferta -> estrategia-de-midia -> criativos-de-anuncio -> posts-sociais -> campanhas-de-nutricao -> qa-de-marketing
argument-hint: [edital] [curso]
---
Execute o workflow "Campanha de vestibular".

Leia contexto/ufape-geral.md e contexto/graduacao.md antes de começar. Na Graduação, a liberação é por edital mais curso; na plataforma, os dados vêm da ficha congelada; no terminal, de contexto/catalogo-de-cursos.md. Edital e curso deste pedido: $ARGUMENTS

A LP da Graduação é uma página separada e nunca é alterada pela squad: toda peça aponta para ela com a UTM gerada pela plataforma.

1. Use o agente cmo para produzir o plano da liberação: diagnóstico, metas, os 8 canais (ativos e fora, com motivo) e o kit de templates/kit-de-lancamento-graduacao.md com responsáveis e prazos ligados aos prazos do edital. Salve e passe o arquivo para a próxima etapa.
2. Use o agente estrategia-de-campanha para produzir o briefing da campanha (templates/briefing-de-campanha.md), com metas de inscritos e matrículas por curso e datas-chave do vestibular. Salve e passe o arquivo para a próxima etapa.
3. Use o agente estrategia-de-oferta para produzir a oferta do semestre: bolsas, descontos, condições e bônus, todos com regra e validade. Salve e passe o arquivo para a próxima etapa.
4. Use o agente estrategia-de-midia para produzir o plano de mídia com verba por curso e canal, começando pelas metas de CPL e de custo por matrícula de cada curso (skill metas-de-custo, .claude/skills/metas-de-custo/SKILL.md) e com a estrutura de lançamento por fases da skill estrutura-de-campanha-paga (captação, aquecimento, inscrições abertas e reta final). Salve e passe o arquivo para a próxima etapa.
5. Use o agente criativos-de-anuncio para produzir a matriz de criativos e os roteiros de vídeo curto. Salve e passe o arquivo para a próxima etapa.
6. Use o agente posts-sociais para produzir o calendário orgânico da campanha. Salve e passe o arquivo para a próxima etapa.
7. Use o agente campanhas-de-nutricao para produzir a régua de WhatsApp e e-mail do lead até a prova e da aprovação até a matrícula. Salve e passe o arquivo para a próxima etapa.
8. Use o agente qa-de-marketing para rodar auditorias/06-geracao-de-demanda.md, auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md em todas as peças.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano do CMO, oferta, plano de mídia, criativos, posts e régua aprovados e com dono para publicar, todos apontando para a LP da Graduação com UTM.
