---
description: Página da turma ou edição (Pós, Cursos Livres, workshop ou simpósio), com SEO, busca por IA e conversão, no formato templates/pagina-da-turma.md. Cadeia: pesquisa-de-palavras-chave -> mensagens -> landing-page -> seo-on-page -> otimizador-de-cta -> qa-de-marketing
argument-hint: [tipo] [curso] [turma ou edição]
---
Execute o workflow "Página de curso".

Leia contexto/ufape-geral.md e o contexto da linha antes de começar. Na plataforma, os dados de curso vêm da ficha congelada da liberação; no terminal, de contexto/catalogo-de-cursos.md. Tipo, curso e turma ou edição deste pedido: $ARGUMENTS

A saída final segue templates/pagina-da-turma.md (versão no topo do arquivo). A IA escreve só textos, FAQ, ordem, visibilidade e SEO; preço, datas, vagas, local, docentes e carga horária vêm do banco e nunca aparecem no texto. A Graduação não usa este workflow: a LP da Graduação é separada e nunca é alterada pela squad.

1. Use o agente pesquisa-de-palavras-chave para produzir a palavra-chave principal, as secundárias e as perguntas que o candidato faz a assistentes de IA sobre o curso. Salve e passe o arquivo para a próxima etapa.
2. Use o agente mensagens para produzir a mensagem central do curso e as respostas às 3 principais objeções, sem números. Salve e passe o arquivo para a próxima etapa.
3. Use o agente landing-page para produzir as seções de texto da página no formato de templates/pagina-da-turma.md, só as chaves do catálogo do tipo, com a ordem padrão ou uma ordem proposta com motivo. Salve e passe o arquivo para a próxima etapa.
4. Use o agente seo-on-page para produzir o título e a descrição de SEO, a resposta citável e as entidades, seguindo a skill visibilidade-em-ia, e a parte textual da marcação para buscadores seguindo a skill schema-de-curso. Salve e passe o arquivo para a próxima etapa.
5. Use o agente otimizador-de-cta para produzir o texto do formulário e do CTA final. Salve e passe o arquivo para a próxima etapa.
6. Use o agente qa-de-marketing para conferir o formato de templates/pagina-da-turma.md (seções obrigatórias presentes, nenhuma chave fora do catálogo, nenhum número no texto) e rodar auditorias/03-busca.md, auditorias/08-conversao.md e auditorias/conformidade-educacional.md.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: a página está no formato do template, aprovada pelo editor e pronta para a plataforma publicar.
