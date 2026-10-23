---
description: Lançamento de uma turma de Curso Livre liberada para o marketing. Cadeia: cmo -> mensagens -> criativos-de-anuncio -> posts-sociais -> copy-de-mensagens -> qa-de-marketing
argument-hint: [curso livre] [turma]
---
Execute o workflow "Lançamento de turma livre".

Leia contexto/ufape-geral.md e contexto/cursos-livres.md antes de começar. Na plataforma, os dados de curso vêm da ficha congelada da liberação da turma; no terminal, de contexto/catalogo-de-cursos.md. Curso e turma deste pedido: $ARGUMENTS

1. Use o agente cmo para produzir o plano da liberação: diagnóstico, metas, os 8 canais (ativos e fora, com motivo) e o kit de templates/kit-de-lancamento-livres.md com responsáveis e prazos. A página da turma sai pelo workflow /pagina-de-curso e, se houver verba, o plano de mídia pelo /plano-de-midia-da-turma, encomendados pelo CMO. Salve e passe o arquivo para a próxima etapa.
2. Use o agente mensagens para produzir a mensagem central da turma e as respostas às principais objeções, sem números. Salve e passe o arquivo para a próxima etapa.
3. Use o agente criativos-de-anuncio para produzir os 2 criativos do kit (skill matriz-de-criativos). Salve e passe o arquivo para a próxima etapa.
4. Use o agente posts-sociais para produzir os 4 posts do kit. Salve e passe o arquivo para a próxima etapa.
5. Use o agente copy-de-mensagens para produzir as 3 mensagens de WhatsApp e o e-mail do kit, como textos para o CRM enviar. Salve e passe o arquivo para a próxima etapa.
6. Use o agente qa-de-marketing para rodar auditorias/05-social.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md em todas as peças.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano do CMO e peças do kit aprovados, e a página encomendada pelo workflow próprio.
