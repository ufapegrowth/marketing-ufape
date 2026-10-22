---
description: Conteúdo da semana de uma linha (social, WhatsApp e e-mail), toda quinta-feira. Cadeia: estrategia-de-conteudo -> posts-sociais -> criador-de-ganchos -> copy-de-mensagens -> qa-de-marketing
argument-hint: [linha] [semana, ex.: 2026-11-02]
---
Execute o workflow "Lote semanal por linha".

Leia contexto/ufape-geral.md, o contexto da linha e contexto/catalogo-de-cursos.md antes de começar. Linha e semana deste pedido: $ARGUMENTS

1. Use o agente estrategia-de-conteudo para produzir os temas da semana, ligados às datas-chave da linha e aos cursos com status "aberto". Salve e passe o arquivo para a próxima etapa.
2. Use o agente posts-sociais para produzir de 5 a 7 posts. Salve e passe o arquivo para a próxima etapa.
3. Use o agente criador-de-ganchos para produzir primeiras linhas mais fortes para os posts. Salve e passe o arquivo para a próxima etapa.
4. Use o agente copy-de-mensagens para produzir o disparo de WhatsApp e o e-mail da semana para a base com consentimento. Salve e passe o arquivo para a próxima etapa.
5. Use o agente qa-de-marketing para rodar auditorias/05-social.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: posts, WhatsApp e e-mail da semana aprovados e agendados.
