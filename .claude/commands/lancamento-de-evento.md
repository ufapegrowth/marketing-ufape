---
description: Lançamento de uma edição de evento (workshop ou simpósio) liberada para o marketing. Cadeia: cmo -> mensagens -> autoridade-docente -> criativos-de-anuncio -> posts-sociais -> copy-de-mensagens -> qa-de-marketing
argument-hint: [evento] [edição] [workshop ou simpósio]
---
Execute o workflow "Lançamento de evento".

Leia contexto/ufape-geral.md e contexto/eventos.md antes de começar. Na plataforma, os dados vêm da ficha congelada da liberação da edição (programação, palestrantes ou facilitadores, datas, local e preço); no terminal, de contexto/catalogo-de-cursos.md. Evento, edição e subtipo deste pedido: $ARGUMENTS

1. Use o agente cmo para produzir o plano da liberação: diagnóstico, metas, canais e o kit de templates/kit-de-lancamento-evento.md na variação do subtipo (workshop ou simpósio), com responsáveis e prazos. A página da edição sai pelo workflow /pagina-de-curso e, no simpósio, o plano de mídia pelo /plano-de-midia-da-turma, encomendados pelo CMO. Salve e passe o arquivo para a próxima etapa.
2. Use o agente mensagens para produzir a mensagem central da edição, sem números. Salve e passe o arquivo para a próxima etapa.
3. Use o agente autoridade-docente para produzir os posts por palestrante do simpósio, só de quem tem autorização registrada; no workshop, registre que a etapa não se aplica. Salve e passe o arquivo para a próxima etapa.
4. Use o agente criativos-de-anuncio para produzir os criativos do kit (skill matriz-de-criativos). Salve e passe o arquivo para a próxima etapa.
5. Use o agente posts-sociais para produzir os posts orgânicos do kit. Salve e passe o arquivo para a próxima etapa.
6. Use o agente copy-de-mensagens para produzir os e-mails e as mensagens de convite, lembrete, programação, véspera e dia, como textos para o CRM enviar. Salve e passe o arquivo para a próxima etapa.
7. Use o agente qa-de-marketing para rodar auditorias/05-social.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md em todas as peças.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: plano do CMO e peças do kit aprovados, e a página da edição encomendada pelo workflow próprio.
