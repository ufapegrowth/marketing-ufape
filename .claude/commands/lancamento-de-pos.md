---
description: Lançamento ou relançamento de um curso de Pós-graduação. Cadeia: cmo -> pesquisa-de-persona -> estrategia-de-oferta -> iscas-digitais -> campanhas-de-nutricao -> criativos-de-anuncio -> qa-de-marketing
argument-hint: [curso de pós] [turma]
---
Execute o workflow "Lançamento de pós".

Leia contexto/ufape-geral.md e contexto/pos-graduacao.md antes de começar. Na plataforma, os dados de curso vêm da ficha congelada da liberação da turma; no terminal, de contexto/catalogo-de-cursos.md. Curso e turma deste pedido: $ARGUMENTS

1. Use o agente cmo para produzir o plano da liberação: diagnóstico, metas, os 8 canais (ativos e fora, com motivo) e o kit de templates/kit-de-lancamento-pos.md com responsáveis e prazos. A página da turma sai pelo workflow /pagina-de-curso e o plano de mídia pelo /plano-de-midia-da-turma, encomendados pelo CMO. Salve e passe o arquivo para a próxima etapa.
2. Use o agente pesquisa-de-persona para produzir a persona do curso (cargo, área, gatilho de carreira, objeções), a partir de alunos atuais e conversas do time de captação. Salve e passe o arquivo para a próxima etapa.
3. Use o agente estrategia-de-oferta para produzir a oferta de lançamento: condições, bônus e o diferencial do curso frente às alternativas. Salve e passe o arquivo para a próxima etapa.
4. Use o agente iscas-digitais para produzir a isca de lançamento (por exemplo, aula aberta ou webinar com o coordenador). Salve e passe o arquivo para a próxima etapa.
5. Use o agente campanhas-de-nutricao para produzir a régua de WhatsApp e e-mail para quem se inscreveu na isca. Salve e passe o arquivo para a próxima etapa.
6. Use o agente criativos-de-anuncio para produzir os criativos de Meta e LinkedIn do lançamento. Salve e passe o arquivo para a próxima etapa.
7. Use o agente qa-de-marketing para rodar auditorias/08-conversao.md e auditorias/conformidade-educacional.md em todas as peças.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano do CMO, oferta, isca, régua e criativos aprovados, e a página e o plano de mídia encomendados pelos workflows próprios.
