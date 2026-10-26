# Auditoria técnica de SEO: faculdade.ufape.com.br e migração para o novo site

- Agente: seo-tecnico
- Linha: geral (Pós-graduação, Cursos Livres, Eventos e Graduação, no que toca a estrutura de URLs)
- Data: 26/10/2026 (etapa 1.17 da camada 1, plano do cmo)
- Status: rascunho para aprovação humana. Nada foi alterado no site no ar. Todas as correções são recomendações e chamados para o time do site (projeto ufape-site).
- Entradas lidas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md (seção "Padrão de nome"); contexto/catalogo-de-cursos.md (seção "Como usar", resumo e tabelas 1 a 9); saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1, 2 e 7, mais 3 e 8 para contexto); docs/auditoria-do-catalogo-2026-10-22.md; docs/auditoria-do-catalogo-2026-10-26.md; fichas em contexto/cursos/ (pos/678, 68662, 670, 68636, 694, 68655, 68641; graduacao/medicina-veterinaria e pedagogia; eventos/neuro-summit); .claude/skills/canibalizacao/SKILL.md; .claude/skills/schema-de-curso/SKILL.md. Pesquisa web em 26/10/2026 (fontes no fim).

## 0. Como ler este documento e o que NÃO foi possível fazer

Não consegui abrir o site ao vivo, rastrear, ver o Search Console, o sitemap, o robots.txt nem o HTML das páginas. Por isso:

- Tudo marcado como "Fato" vem das fichas, do catálogo ou das auditorias (texto da página copiado em 26/10/2026).
- Tudo que depende de comportamento do servidor, do sitemap, do HTML renderizado ou de dados de busca está marcado [SUPOSIÇÃO] ou [CONFIRMAR].
- A busca `site:faculdade.ufape.com.br` (duas consultas) não devolveu nenhuma página do domínio. Isso NÃO prova que o site está fora do índice: o comando `site:` na ferramenta de busca usada é pouco confiável. Só o Search Console responde. [CONFIRMAR]
- Nenhum número de cliques, impressões ou posição existe aqui. A skill canibalizacao exige exportação do Search Console para ordenar por cliques em risco; sem ela, a ordenação abaixo é por risco estrutural, não por tráfego.

## 1. Resumo para quem decide

1. O site atual tem um produto por turma, e cada turma tem página própria com o mesmo título e quase o mesmo texto. No catálogo, 55 páginas de pós correspondem a apenas 40 cursos. Em 12 cursos, 27 páginas repetem o mesmo nome. Isso divide a força de busca e confunde buscadores e assistentes de IA sobre qual é "a" página do curso.
2. Há páginas mortas, sem venda ou de edições passadas que seguem com endereço público: 1 produto de teste, 2 links fora do ar, 5 pós sem venda, 13 provas de bolsa antigas e 5 cursos livres sem venda. Uma das provas antigas ainda mostra o resultado com nome de uma pessoa aprovada (dado pessoal publicado; ver C2).
3. A migração para o novo site é a oportunidade de resolver tudo de uma vez, com uma regra: uma URL canônica por curso, turmas dentro dela e redirecionamento 301 por código de produto. O mapa completo de códigos está na seção 6.
4. A marcação estruturada (Course) ainda vale como sinal para entender a página, mas o Google aposentou o recurso visual "Course Info" em 2025. Não prometer estrela, carrossel ou preço na busca.
5. Duas verificações de alto risco no novo site que ninguém pode responder hoje: o texto do curso aparece no HTML sem executar JavaScript? O robots.txt trata separadamente robô de busca de IA e robô de treino?

## 2. Problemas por prioridade

Escala: crítico (perde busca ou confunde o cliente agora, ou pode quebrar a migração), vale corrigir, deixar para depois. Esforço (baixo, médio, alto) é estimativa minha [SUPOSIÇÃO], sem conhecer o código do ufape-site.

### CRÍTICO

#### C1. Várias páginas do mesmo curso, com mesmo nome e texto praticamente igual

- Fato (catálogo, seção 2): 12 cursos aparecem em mais de uma página de produto com exatamente o mesmo nome. Total de 27 páginas.

| Curso | Códigos (turma, local) |
|---|---|
| Pós-graduação em Anestesiologia Veterinária | 664 (VII, Goiânia, sem venda), 68607 (X, SP), 68609 (VIII, Goiânia) |
| Pós-graduação em Clínica Cirúrgica de Cães e Gatos | 535 (IV, Goiânia), 665 (VIII, SP), 68632 (V, Goiânia) |
| Pós-graduação em Internação Veterinária | 610 (SP), 614 (Goiânia), 615 (Belo Horizonte), todas sem venda |
| Pós-graduação em Oncologia Veterinária | 654 (VI, sem venda), 68628 (VII) |
| Pós-graduação em Neurologia e Neurocirurgia Veterinária | 701 (VIII), 68616 (IX) |
| Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | 663 (IV), 68635 (V) |
| Pós-graduação em Odontologia Veterinária | 678 (IV), 68662 (V) |
| Pós-graduação em Cardiologia Veterinária | 68605 (XI, SP), 289 (II, Goiânia) |
| Pós-graduação em Terapia Intensiva e Emergência Veterinária | 666 (XI, SP), 68623 (IV, Goiânia) |
| Pós-graduação em Pneumologia Veterinária | 670 (VII, fora do ar), 68636 (VIII) |
| Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | 68604 (VI), 68611 (VI, data "XX DE XX DE 202X") |
| Ultrassonografia de Pequenos Animais (escrito "Pós Graduação") | 706 (II), 68629 (III) |

- Exemplo concreto verificado nas fichas: Odontologia 678 (https://faculdade.ufape.com.br/produto/678/pos-graduacao-em-odontologia-veterinaria) e 68662 (https://faculdade.ufape.com.br/produto/68662/pos-graduacao-odontologia-veterinaria/sao-paulo). Mesmo H1 ("Pós-graduação em Odontologia Veterinária"), mesmos dois parágrafos de abertura, mesma carga horária (500 h), mesmo preço (30x de R$ 1.180,00), mesmo endereço. Diferem na turma (IV e V), na data e no slug.
- Exemplo 2: Pneumologia 670 (https://faculdade.ufape.com.br/produto/670/pos-graduacao-em-pneumologia-veterinaria) e 68636 (https://faculdade.ufape.com.br/produto/68636/pos-graduacao-em-pneumologia-veterinaria). O slug é idêntico; só muda o código. A 670 mostra "O produto requisitado não está mais disponível" e a 68636 é a turma VIII, aberta.
- O que isso custa, em linguagem simples: quando o médico veterinário digita "pós em odontologia veterinária", o Google precisa escolher uma entre duas páginas iguais, e pode alternar entre elas ou mostrar a mais antiga. A força de links e de visitas fica dividida ao meio. Para assistentes de IA, não há uma "página do curso" para citar. [SUPOSIÇÃO sobre o comportamento exato; o risco estrutural é fato.]
- Quem tem mais risco: os cursos oferecidos em SP e Goiânia (Anestesiologia, Clínica Cirúrgica, Cardiologia, Terapia Intensiva), porque as buscas por cidade e por especialidade se misturam.
- Esforço: médio (decisão de modelo, depois regra de redirecionamento).
- Correção recomendada: ver seções 4 e 5 (um curso, uma URL canônica; turmas dentro).
- Dados que faltam para provar canibalização: exportação de consultas e páginas do Search Console [CONFIRMAR]. Preciso saber se 678 e 68662 aparecem para a mesma consulta.

#### C2. Páginas sem venda, fora do ar ou de edições passadas que seguem acessíveis

- Fato (auditoria de 26/10, seção 8): 25 páginas sem venda ou fora do ar. Mais um produto de teste (seção 2 da auditoria).

| Grupo | Códigos | Observação |
|---|---|---|
| Produto de teste publicado | 183 (https://faculdade.ufape.com.br/produto/183/teste2026) | Dentro da categoria de Pós em Cardiologia. Preço: R$ 0,17 por parcela na auditoria de 22/10 e R$ 2,00 na de 26/10 (divergência a conferir). |
| Link fora do ar | 670 (pós Pneumologia), 68656 (prova de bolsa de Oftalmologia) | Mensagem "O produto requisitado não está mais disponível". Não sei se o servidor devolve 404 ou 200 com a mensagem (soft 404). [CONFIRMAR] |
| Pós sem venda ("avise-me") | 664, 654, 610, 614, 615 | Página no ar, sem compra. |
| Provas de bolsa antigas sem venda | 680, 681, 682, 684, 685, 687, 688, 689, 690, 691, 693, 694, 695 (13 páginas) | Edições passadas. |
| Cursos livres sem venda | 539, 592, 716, 68613, 715 | |
| Páginas fora do catálogo | 686 (recrutamento do corpo clínico), 638 (regras de estágio, fora do ar) | Não são cursos; decidir se ficam. |

- Exemplo: prova de bolsa 694 (https://faculdade.ufape.com.br/produto/694/prova-de-bolsa-de-estudos-para-pos-graduacao-lato-sensu-em-odontologia-veterinaria). Mostra "Avise-me", prova de 04 de fevereiro de 2026 (data passada), a lista de aprovados com o nome completo de uma candidata e o texto "reconhecida pelo Ministério da Educação (MEC)". Não reproduzo o nome aqui.
- O que isso custa: (a) o cliente chega por busca a uma página que não vende nada, e perde confiança; (b) o buscador gasta rastreamento em páginas inúteis e pode mostrar a edição antiga no lugar da atual; (c) a página 694 expõe dado pessoal de candidata em página pública e repete a frase de MEC que a conformidade da squad proíbe. O item (c) é urgente por LGPD e conformidade, e deve ser tratado como prioridade de atendimento ao titular, independentemente de SEO. Quem decide é a Ufape (jurídico e regulação). Correção do QA de 26/10: a auditoria de 26/10 (seção 2a) mostra que as 13 provas antigas (680 a 695) e a página 715 publicam nomes de aprovados; o chamado ao time do site cobre as 14 páginas.
- Esforço: baixo (retirar e redirecionar), com a regra da seção 5.
- Correção: nunca apagar sem redirecionar. Ver tabela de destinos na seção 6.

#### C3. Dados de turma conflitantes que podem ir para a busca e para a migração

- Fato (auditoria de 26/10, seções 3 a 5): 7 páginas com data diferente entre planilha e site, 3 com turma diferente, 2 com link provavelmente trocado.
- Exemplos com código: Odontologia 68662 (planilha 15/08/2026, site 24/04/2027); Ortopedia 662 (planilha 24/04/2027 turma V, site 15/08/2026 turma IV); Ecocardiografia 698 (planilha 28/11/2026, site 28/11/2027); Ventilação Mecânica 352 (planilha 24/05/2027, site 24/04/2027); endoscopia digestiva 623 (planilha 28/11/2026, site 01/08/2026).
- Fato: o produto 68611 (Diagnóstico por Imagem) está publicado com início "XX DE XX DE 202X". O 68634 (Workshop de Neuromonitorização, gravado) mostra 24 h e local "Saiba Mais", enquanto a página do evento (/neuro-summit/) e a Ufape informam 16 h.
- O que isso custa: o buscador pode exibir a data errada, e o cliente pode comprar achando que a turma começa em outra data. Para a migração, copiar esses dados sem corrigir leva o erro para o site novo e para a marcação estruturada.
- Regra do plano: a planilha é a fonte da verdade para datas. O novo site só deve ser alimentado depois da confirmação por turma [CONFIRMAR com a Ufape].
- Esforço: baixo no site, mas depende da decisão da Ufape (pedidos A6 e A12 do plano do cmo).

#### C4. Migração sem mapa de redirecionamento por código de produto

- Fato: o endereço atual segue /produto/<código>/<slug>, às vezes com /<turma>/<cidade> (exemplos: 68662 termina em /sao-paulo; 68617 em /v/sao-paulo; 539 em /vi/sao-paulo; 99 em /ii/goiania). O padrão novo decidido é /pos-graduacao/pos-graduacao-em-<área>. Fato: o slug varia para o mesmo curso (678 usa "pos-graduacao-em-odontologia-veterinaria"; 68662 usa "pos-graduacao-odontologia-veterinaria"; 650 usa "pos-graduacao-lato-em-medicina-de-felinos").
- Como o slug muda sem critério, a regra de redirecionamento não pode depender do slug. Precisa casar pelo código numérico.
- O que isso custa: se o site novo entrar sem 301, todo endereço antigo (inclusive os que estão em anúncios, e-mails, WhatsApp e links de parceiros) vira erro 404 e a busca perde o histórico de ranqueamento. Anúncios ativos de 707, 68604, 68606, 698, 68610 e 68608 apontam para páginas de produto atuais (visão de campanhas, citada no plano do cmo) [CONFIRMAR as URLs de destino exatas].
- Esforço: médio a alto. Correção na seção 6.

### VALE CORRIGIR

#### V1. Padrão de título e slug inconsistente

- Fato (catálogo, seção 2): 6 das 55 páginas de pós fogem do padrão "Pós-graduação em <área>": 706 e 68629 ("Pós Graduação em Ultrassonografia de Pequenos Animais"), 341 ("Pós Graduação em Medicina Interna Equina"), 333 ("Pós Graduação em Citopatologia Veterinária"), 659 ("Pós-graduação Cirurgia Cardiorrespiratória em Cães e Gatos", sem o "em") e 719 ("Pós-Graduação Inteligência Artificial na Saúde"). Nas provas de bolsa, os nomes mudam de formato entre as novas ("Prova de Bolsa de Estudos para Odontologia Veterinária") e as antigas ("Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Odontologia Veterinária"). A 680 inclui "Turma VI" no nome.
- Fato: o texto de uma página de pós usa caixa alta no corpo ("PÓS GRADUAÇÃO EM ODONTOLOGIA VETERINÁRIA"), variação que quebra a repetição do nome padrão.
- Regra do contexto: nome "Pós-graduação em <área>", slug "pos-graduacao-em-<área>", nunca "Pós em", "Pós Graduação", "Pós-Graduação" ou "Lato" (contexto/pos-graduacao.md). O CMS do admin aplica sozinho ao salvar; o site atual não.
- Esforço: baixo no site novo (a regra já existe no CMS); médio se tivesse que corrigir o site velho. Como o site velho sai, corrija só na migração.
- Observação: os textos copiados do site oficial nas fichas ficam como estão (registram o publicado). A correção é na página nova.

#### V2. Canibalização entre páginas do mesmo tema (além das turmas)

Análise estrutural pela skill canibalizacao, sem dados de busca. A coluna "cliques em risco" fica [CONFIRMAR] para todas, porque depende do Search Console.

| Consulta provável [SUPOSIÇÃO] | Páginas envolvidas | Página que fica (proposta) | Correção | Links internos a ajustar | Cliques em risco |
|---|---|---|---|---|---|
| "pós graduação odontologia veterinária" | 678, 68662, prova 68655, prova antiga 694 | página única do curso | juntar 678 e 68662 numa só; prova passa a ser bloco dentro dela; 694 redireciona | links de 68655, menus, blog | [CONFIRMAR] |
| "pós pneumologia veterinária" | 670 (fora do ar), 68636, prova 68659 | página única do curso | 670 redireciona para a página do curso | links do blog e da planilha | [CONFIRMAR] |
| "prova de bolsa ufape <especialidade>" | prova nova (ex.: 68655), prova antiga (ex.: 694), página do curso (que tem o bloco "Prova de bolsa. Clique aqui") | uma página de campanha (decisão A3 do plano) | mudar o alvo: prova mira "prova de bolsa", curso mira "pós em <área>" | botão "Clique aqui" da página do curso | [CONFIRMAR] |
| "curso endoscopia digestiva são paulo" | 623 e 68637 (mesmo preço, 12 h, 28/11/2026) | a que a Ufape escolher | juntar e redirecionar a outra | catálogo, anúncios | [CONFIRMAR] |
| "curso prático de imersão em cirurgia veterinária" | 99 (Goiânia), 433 (SP), mesmo título | uma página com duas turmas, ou duas páginas com cidade no título | mudar alvo por cidade | menus | [CONFIRMAR] |
| "grupo de estudo internação e terapia intensiva" | 643 (anual 2025/2026) e 713 (anual 2026) | 713 | 643 redireciona para 713 se a edição acabou [CONFIRMAR] | | [CONFIRMAR] |
| "grupo de estudo nefrologia" | 642 (2025/2026) e 712 (2026) | 712 | idem | | [CONFIRMAR] |
| "workshop neuromonitorização" | /neuro-summit/ (página do evento, fora do padrão /produto/) e produto 68634 (modalidade transmitida) | /neuro-summit/ | 68634 mira a compra da modalidade gravada; título e texto diferentes; canonical para a página do evento só se o conteúdo for o mesmo [CONFIRMAR] | campanhas já apontam para /neuro-summit/ | [CONFIRMAR] |
| "pós anestesiologia" | 586 (Direto ao Ponto, EAD), 657 (Avançada), 359 (Locorregional), 68607, 68609 | cada uma é um curso diferente: ficam separadas | garantir nome e primeira frase que distinguem a intenção (EAD, avançada, locorregional) | | [CONFIRMAR] |

- Atenção às regras da skill: nenhuma página de curso ativo é redirecionada sem acordo do responsável pelo site; página de curso encerrado tem redirecionamento para o curso ou a área mais próxima; todo número vem da exportação. Por isso as correções acima são propostas, não ordens.

#### V3. Marcação estruturada (dados estruturados)

- Fato: não tenho o HTML; não sei se há marcação hoje. [CONFIRMAR com Rich Results Test e inspeção de URL.]
- Fato (Google, 12/06/2025): o recurso "Course Info" deixou de aparecer nos resultados de busca e saiu do relatório do Search Console em 09/09/2025. Course em si continua um tipo válido do schema.org. Efeito prático: marcar curso ajuda a descrever a página para máquinas, mas não deve ser vendido internamente como "vai ganhar destaque na busca".
- Recomendação: marcar Course com provider (EducationalOrganization), CourseInstance por turma, FAQPage só se a pergunta estiver visível na página e Person só para docente com autorização registrada. Nada de preço ou de ato regulatório que não esteja no catálogo. A skill schema-de-curso orienta o texto.
- Exemplo de JSON-LD pronto para o chamado, usando somente dados do catálogo, para a Pós em Pneumologia 68636. As URLs do novo site são [SUPOSIÇÃO] pelo padrão decidido. Campos omitidos de propósito: preço e condições (esperar confirmação; ver P11), certificado (texto oficial ainda não existe: P1 do plano), docentes (autorização, P13). A data 17/04/2027 vem só do site; a planilha manda, então [CONFIRMAR NO CATÁLOGO] antes de publicar.

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Pós-graduação em Pneumologia Veterinária",
  "url": "https://faculdade.ufape.com.br/pos-graduacao/pos-graduacao-em-pneumologia-veterinaria",
  "provider": {
    "@type": "EducationalOrganization",
    "name": "Faculdade UFAPE",
    "url": "https://faculdade.ufape.com.br",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Av. 9 de Julho, 3939",
      "addressLocality": "São Paulo",
      "addressRegion": "SP",
      "postalCode": "01407-100",
      "addressCountry": "BR"
    }
  },
  "hasCourseInstance": [
    {
      "@type": "CourseInstance",
      "name": "Turma VIII",
      "courseMode": "blended",
      "startDate": "2027-04-17",
      "courseWorkload": "PT500H",
      "location": {
        "@type": "Place",
        "address": { "@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR" }
      }
    }
  ]
}
```

- Mapeamento "Semipresencial" para "blended" é [SUPOSIÇÃO]; confirmar com o seo-on-page na versão final.
- Consistência da marca (passo 4 da skill): o nome oficial usa "Faculdade UFAPE", também "Ufape Intercursos" (ufape-geral.md), com domínios diferentes: faculdade.ufape.com.br (loja), ufape.com.br (hospital veterinário) e e-mails em intercursos.com.br. Recomendo uma única descrição da instituição, com sameAs apontando para os perfis oficiais (Instagram @ufapevet, Facebook /Ufape) e para o domínio da Ufape Clínica. Perfis e portais externos não foram conferidos [CONFIRMAR].

#### V4. Conteúdo sem JavaScript e robôs de IA (verificação obrigatória do novo site)

- Fato: o CLAUDE.md do ufape-admin e do portal descreve projetos Lovable com roteamento por arquivo (routeTree.gen.ts) e build para Cloudflare. Não li o código do ufape-site, então não sei se renderiza no servidor.
- [SUPOSIÇÃO] Sites feitos com Lovable podem entregar a página como aplicação do navegador, com o texto aparecendo só depois de executar JavaScript. Muitos robôs de IA não executam JavaScript. Se for o caso, a página de curso pareceria vazia para eles.
- Teste simples para o time do site (sem ferramenta paga): pedir a página com `curl` e procurar no HTML bruto o nome do curso, a carga horária, o início da turma e o preço. Se aparecerem, está bom. Se só aparecer um contêiner vazio, abrir chamado crítico antes da migração.
- Robots.txt: [CONFIRMAR] o arquivo atual e o do novo site. Fato (documentação da OpenAI): o robô de busca (OAI-SearchBot) e o de treino (GPTBot) têm controles independentes no robots.txt; liberar um e bloquear o outro é possível. A decisão de liberar ou não o treino é da Ufape. A recomendação técnica mínima: permitir os robôs de busca de IA (para a Ufape ser citada) e decidir à parte sobre os de treino. Rascunho abaixo, a ser aprovado antes de qualquer uso. Conferir a lista de nomes de robôs na documentação de cada empresa antes de publicar (Google e Anthropic têm os seus; não verifiquei nesta rodada).

```
# Rascunho. Não aplicar sem aprovação da Ufape.
User-agent: OAI-SearchBot
Allow: /

# Decisão pendente da Ufape: permitir ou bloquear treino de modelos.
User-agent: GPTBot
Disallow: /     # [CONFIRMAR decisão]

User-agent: *
Disallow: /carrinho
Disallow: /checkout
Sitemap: https://faculdade.ufape.com.br/sitemap.xml
```

- Os caminhos /carrinho e /checkout são exemplos [SUPOSIÇÃO]; o time do site informa os reais.

#### V5. Turmas já iniciadas e ainda à venda (36 no catálogo)

- Fato (auditoria de 26/10, seção 6): 36 produtos com data de início passada e botão de compra ativo. Incluem 18 pós de turma em andamento (por exemplo 677 desde 11/07/2026; 68607 desde 24/10/2026) e cursos curtos de 1 a 3 dias cuja data já passou (por exemplo 599, de 20/06/2026; 625, de 01/10/2026).
- Em pós de módulos mensais pode ser entrada tardia intencional [CONFIRMAR política de entrada]. Em curso de 1 ou 2 dias, a página deveria sair de venda ou ganhar nova data.
- O que isso custa: o buscador mostra uma data passada ao lado de um botão de compra; para curso de dois dias, o cliente pode pagar por uma turma que não existe.
- Correção: máquina de estados da turma (seção 5).

#### V6. Páginas com data em branco ou sem data

- Fato (auditoria de 26/10, seção 7): 11 páginas sem data de início no site (para 718, 68668 e 68618 a planilha tem a data, que é a fonte válida), incluindo o 68611 com "XX DE XX DE 202X". Também 593, 576, 589, 590, 603, 604 e 404, 718, 68668, 68618.
- Custo: dado incompleto no resultado de busca e marcação estruturada sem startDate.
- Correção: página sem data não é indexável como "turma aberta". Use "em breve" noindex até ter data, ou não publique [CONFIRMAR com a Ufape].

#### V7. Marca homônima: UFAPE de Pernambuco

- Fato (pesquisa de 26/10/2026): as buscas por "ufape" retornam o domínio ufape.edu.br, que é a Universidade Federal do Agreste de Pernambuco (edital BIA-UFAPE 2026.1, por exemplo). A sigla é a mesma da Faculdade UFAPE.
- [SUPOSIÇÃO] Buscas só pela sigla trazem resultados de outra instituição. Isso reforça usar "Faculdade UFAPE" (e "Ufape Clínica" para o hospital) nos títulos, na marcação (name, alternateName, sameAs) e nas primeiras frases de cada página.
- Esforço: baixo. Entra no briefing do seo-on-page.

### DEIXAR PARA DEPOIS

- D1. Páginas por cidade (por exemplo "pós em anestesiologia veterinária em Goiânia") só se o Search Console mostrar demanda separada por cidade. Até lá, a cidade fica na tabela de turmas da página do curso. [CONFIRMAR com dados]
- D2. Versão em espanhol dos cursos de Lima (575, 605, 347, 501) com idioma declarado (hreflang) quando o novo site tiver rotas por idioma. Revisão por falante nativo continua obrigatória (P17 do plano).
- D3. Sitemaps separados por tipo (pós, livres, eventos, graduação) para facilitar a leitura do relatório de cobertura. Útil, não urgente.
- D4. Blog: não li nenhuma página do blog. Auditoria de títulos duplicados, links quebrados e páginas órfãs do blog fica para depois do rastreamento [CONFIRMAR acesso a rastreamento ou exportação].

## 3. O que não consegui checar (e quem pode)

| Checagem do método | Situação | Quem resolve |
|---|---|---|
| Páginas bloqueadas, noindex, canonical, cobertura do sitemap | Sem acesso | Time do site e Search Console |
| Velocidade e uso no celular (página de curso, área, blog, formulário) | Sem acesso | PageSpeed Insights e relatório de experiência do Search Console |
| Conteúdo sem JavaScript | Sem acesso; teste simples na V4 | Time do site |
| robots.txt do site atual | Sem acesso | Time do site |
| Links quebrados, cadeias de redirecionamento, páginas órfãs | Sem rastreamento | Exportação de rastreador (Screaming Frog ou equivalente) |
| Títulos duplicados na tag title | Só confirmo no H1 (fichas) | Rastreador |
| Canibalização com cliques | Sem Search Console | Exportação do Search Console (skill leitura-do-search-console) |

## 4. Recomendação de modelo de URL e de página para o novo site

1. Uma URL canônica por curso. Padrão decidido: /pos-graduacao/pos-graduacao-em-<área>. Exemplo: /pos-graduacao/pos-graduacao-em-odontologia-veterinaria.
2. As turmas ficam dentro da página do curso (tabela ou cartões com turma, cidade, modalidade, início, preço e botão de compra). Cada turma tem um identificador interno, mas NÃO uma URL indexável própria enquanto estiver aberta. Motivo: as turmas de um mesmo curso hoje têm texto igual e só mudam dados (turma, data, cidade, preço).
3. Quando houver cursos distintos com nome parecido, o slug traz o diferencial: pos-graduacao-em-anestesiologia-veterinaria, pos-graduacao-em-anestesiologia-avancada, pos-graduacao-em-anestesiologia-locorregional-veterinaria, e o EAD com "direto-ao-ponto" (586).
4. Se SP e Goiânia tiverem coordenação ou conteúdo diferentes para o mesmo curso, o texto da página explica; só criar URL por cidade se houver demanda comprovada (D1).
5. Provas de bolsa: em vez de um produto novo por edição e por cidade (hoje 36 páginas de provas, com 6 páginas para 3 títulos repetidos por cidade: 68639 e 68640, 68641 e 68642, 68643 e 68644), uma página de campanha da prova de bolsa, com bloco por especialidade (alinhado à decisão A3 do plano do cmo), e um bloco "Prova de bolsa" dentro de cada página de curso, com data da próxima edição. Se o Search Console mostrar busca específica por prova de bolsa de uma especialidade, aí vale uma URL por especialidade que dura de uma edição para a outra (sem código novo a cada edição).
6. Cursos livres e eventos: o padrão de URL ainda não está definido na decisão. Sugestão [SUPOSIÇÃO]: /cursos-livres/<slug> e /eventos/<slug>, mantendo /neuro-summit/ como está até a campanha de 20/11/2026 passar (campanhas pagas já apontam para ele).
7. Graduação: já existe /graduacao, /graduacao/pedagogia (ficha da Pedagogia) e /graduacao (ficha de Medicina Veterinária). A LP da Graduação é página separada que a squad nunca altera; as peças apontam para ela com UTM. Recomendo só que, na migração, os endereços atuais continuem funcionando por 301 ou sejam mantidos.
8. Título e descrição (tag title): <Nome padrão> | Faculdade UFAPE. O número da turma e a data entram no corpo da página e na marcação, não no título do curso (senão cada turma gera um título novo e o curso perde consistência). Detalhes e variações por cidade ficam com o agente seo-on-page.

## 5. Estados de uma turma ou edição (regra para o novo site)

| Estado | Condição (proposta) | Página | Indexação | Marcação |
|---|---|---|---|---|
| Aberta | início futuro e venda ativa | linha na tabela de turmas da página do curso | indexável (a página do curso) | CourseInstance com startDate; oferta só com preço confirmado |
| Em andamento, entrada permitida | início passado, venda ativa, política de entrada confirmada [CONFIRMAR] | mesma linha, com o aviso "turma em andamento" e as regras de entrada | indexável | sem urgência artificial |
| Sem data | página com data em branco ou "SEM DATA" | não publicar como turma | noindex ou fora do ar | sem startDate |
| Encerrada, sem venda | venda fechada ou "avise-me" | a linha some da página do curso e vai para o histórico interno | a URL antiga redireciona (301) para a página do curso | sem marcação |
| Curso descontinuado (sem turma futura planejada) | decisão da Ufape [CONFIRMAR] | a página do curso permanece só se houver lista de espera; senão 301 para a área mais próxima | | |

- Regra: antes de remover uma página de curso encerrado, sempre redirecionar para o curso ou a área mais próxima. Para 410 (removido de vez), só usar em itens sem nenhum equivalente, como o produto de teste.
- Fonte para o redirecionamento: o Google considera redirecionamento um sinal forte de que o destino deve ser a página canônica, e recomenda redirecionamento permanente quando uma duplicata é aposentada (documentação do Google sobre canonicalização).

## 6. Chamados prontos para o time do site (ufape-site)

Cada chamado traz problema, correção, esforço (estimativa [SUPOSIÇÃO]) e o que reconferir. Nenhum deve ser executado sem aprovação humana.

### Chamado SEO-01 (crítico): mapa de redirecionamento 301 por código de produto

- Problema: C4.
- Correção: criar uma tabela de redirecionamento com chave no código numérico. Qualquer endereço que comece com /produto/<código>/ (com ou sem slug, turma ou cidade depois) deve responder 301 em um único salto para a URL canônica nova. Não depender do slug.
- Regra para códigos sem equivalente (produto de teste, 686, 638): 410 ou 301 para a área, conforme decisão da Ufape.
- Manter a tabela por pelo menos 12 meses depois da troca. Fonte: orientação de Google reportada por veículo especializado (ver fontes); não consegui confirmar na documentação oficial, então tratar como boa prática [SUPOSIÇÃO].
- Mapa de destino das 55 páginas de pós (destino = sufixo depois de /pos-graduacao/pos-graduacao-em-):

| Destino (sufixo) | Códigos de origem |
|---|---|
| anestesiologia-veterinaria | 664, 68607, 68609 |
| anestesiologia-veterinaria-direto-ao-ponto | 586 |
| anestesiologia-avancada | 657 |
| anestesiologia-locorregional-veterinaria | 359 |
| oncologia-veterinaria | 654, 68628 |
| neurocirurgia-e-neuro-oncologia-veterinaria | 677 |
| neurologia-e-neurocirurgia-veterinaria | 701, 68616 |
| nutrologia-veterinaria | 564 |
| clinica-cirurgica-de-caes-e-gatos | 535, 665, 68632 |
| clinica-medica-e-emergencia-de-pequenos-animais | 663, 68635 |
| ultrassonografia-de-pequenos-animais | 706, 68629 |
| endoscopia-veterinaria | 653 |
| medicina-de-felinos | 650 |
| odontologia-veterinaria | 678, 68662 |
| dor-e-cuidados-paliativos-na-veterinaria | 554 |
| terapia-intensiva-e-emergencia-veterinaria | 666, 68623 |
| cirurgia-cardiorrespiratoria-em-caes-e-gatos | 659 |
| cardiologia-veterinaria | 68605, 289 |
| nefrologia-e-urologia-veterinaria | 68612 |
| oftalmologia-veterinaria | 707 |
| diagnostico-por-imagem-aplicado-a-clinica-medica-e-cirurgica-veterinaria | 68604, 68611 |
| gastroenterologia-veterinaria | 68606 |
| dermatologia-veterinaria | 68610 |
| ecocardiografia | 698 |
| hematologia-veterinaria | 68608 |
| medicina-interna-equina | 341 |
| patologia-clinica | 68615 |
| citopatologia-veterinaria | 333 |
| infectologia-veterinaria | 679 |
| fisioterapia-fisiatria-e-reabilitacao-veterinaria | 366 |
| pneumologia-veterinaria | 670, 68636 |
| endocrinologia-de-pequenos-animais | 68617 |
| ortopedia-veterinaria | 662 |
| inteligencia-artificial-na-saude | 719 |
| geriatria-veterinaria | 699 |
| obstetricia-neonatologia-e-biotecnologias-da-reproducao-em-caes-e-gatos | 382 |
| videocirurgia-veterinaria | 578 |
| ventilacao-mecanica | 352 |
| medicina-de-silvestres | 60 |
| internacao-veterinaria (ver nota) | 610, 614, 615 |

  - Total: 40 destinos para 55 códigos. Nomes de slug seguem o nome do catálogo, sem acento. [CONFIRMAR NO CATÁLOGO] se algum nome mudará no novo site.
  - Nota sobre Internação: nenhuma turma aberta. Sugestão: 301 para a página da área "Emergência e terapia intensiva" ou para terapia-intensiva-e-emergencia-veterinaria [SUPOSIÇÃO de proximidade; a Ufape decide se o curso volta].
  - Nota sobre 662 (Ortopedia) e 68662 (Odontologia): o link da planilha parece trocado (auditoria de 26/10, seção 3). Redirecionar pelo código está certo, mas a turma exibida na página nova precisa ser conferida antes de publicar.
- Mapa das provas de bolsa:

| Origem (código) | Situação | Destino proposto |
|---|---|---|
| 68639, 68640, 68641, 68642, 68643, 68644, 68645, 68646, 68647, 68648, 68649, 68650, 68651, 68652, 68653, 68654, 68655, 68657, 68658, 68659, 68660, 68661 (22) | abertas, prova em 27/11/2026 | página de campanha da prova de bolsa, bloco da especialidade; depois de 27/11, 301 para a página do curso |
| 68656 (Oftalmologia, fora do ar) | sem página | pós Oftalmologia (707) |
| 691 | antiga | bloco de Anestesiologia da campanha |
| 687 | antiga | bloco de Clínica Cirúrgica |
| 689 | antiga | bloco de Clínica Médica e Emergência |
| 695 | antiga | bloco de Dermatologia |
| 682 | antiga | bloco de Endocrinologia |
| 681 | antiga | bloco de Gastroenterologia |
| 684 | antiga | bloco de Hematologia |
| 680 | antiga | bloco de Medicina de Felinos |
| 688 | antiga | bloco de Nefrologia e Urologia |
| 694 | antiga | bloco de Odontologia |
| 685 | antiga | bloco de Oncologia |
| 690 | antiga | bloco de Terapia Intensiva |
| 693 | antiga | pós Videocirurgia (578), pois não há prova nova da área no catálogo |

- Cursos livres, grupos de estudos e eventos: usar o mesmo princípio (redirecionar por código ao curso atual, ou à área). Cursos livres encerrados sem equivalente (539, 592, 716, 68613, 715) vão à página de área mais próxima [SUPOSIÇÃO: 539 e 716 têm equivalente futuro em 68638, POCUS 06/03/2027, e em 591, ultrassonografia POC gravada]. Cursos duplicados (623 e 68637; 643 e 713; 642 e 712) dependem da decisão da Ufape sobre qual fica.
- Esforço: alto (levantamento de todos os 184 códigos do catálogo mais os produtos fora do catálogo). A tabela acima cobre pós e provas (91 códigos).
- Reconferir depois: (1) cada código antigo devolve 301 em um único salto; (2) nenhum destino devolve 404; (3) nenhum redirecionamento forma cadeia ou laço; (4) os anúncios ativos abrem a página certa; (5) o relatório de páginas do Search Console, nas duas semanas seguintes, sem salto de "Não encontrada (404)".

### Chamado SEO-02 (crítico): retirar o produto de teste e sanear páginas mortas

- Problema: C2.
- Correção: (a) produto 183: tirar do ar com 410 (sem equivalente) e conferir o valor (R$ 0,17 ou R$ 2,00); (b) 670 e 68656: ver o código HTTP; se devolverem 200 com a mensagem, corrigir para 301 ao curso (a 670 vai para pneumologia-veterinaria); (c) 664, 654, 610, 614, 615 e as 13 provas antigas: 301 conforme o mapa; (d) enquanto o site velho existir, tirar as 13 provas antigas e as pós sem venda do sitemap [CONFIRMAR existência no sitemap].
- Esforço: baixo.
- Reconferir: sitemap sem URLs 3xx, 4xx ou noindex; consulta `site:` pelo Search Console (relatório Páginas) sem as URLs antigas depois de algumas semanas; produto 183 sem aparecer em busca interna da loja.
- Chamado paralelo para a Ufape (fora de SEO): página 694 expõe nome de pessoa aprovada. Decidir retirada e conferir outras provas antigas.

### Chamado SEO-03 (crítico): corrigir dados de turma antes de alimentar o site novo

- Problema: C3.
- Correção: ninguém copia dado de data, turma ou carga horária do site velho para o novo. Fonte única: catálogo (datas da planilha). Itens a decidir primeiro: 68662, 662, 698, 352, 366, 623, 606, 68611, 68634 (carga horária 24 h versus 16 h).
- Esforço: baixo (técnico), depende da decisão da Ufape (pedidos A6 e A12).
- Reconferir: nenhuma data passada em turma "aberta" e nenhum campo "XX" ou "SEM DATA" publicado no site novo; startDate da marcação igual à data da página.

### Chamado SEO-04 (vale corrigir): modelo de curso com turmas dentro, canonical e título

- Problema: C1 e V1.
- Correção: implementar a página do curso com tabela de turmas; gerar o título e o slug pela regra "Pós-graduação em <área>" (o CMS do admin já aplica); canonical autorreferente em toda página indexável; páginas de turma encerradas redirecionam (seção 5).
- Esforço: médio.
- Reconferir: um H1 por página, sem H1 repetido entre cursos; cada URL canônica responde 200; nenhuma URL de turma aberta competindo com a página do curso; canonical presente no HTML inicial (não injetado por JavaScript).

### Chamado SEO-05 (vale corrigir): teste de conteúdo sem JavaScript e robots.txt

- Problema: V4.
- Correção: executar o teste com `curl` nas quatro páginas-modelo (curso, área, blog, formulário de inscrição), anexar o resultado; revisar o robots.txt do novo site conforme o rascunho (decisão da Ufape sobre robôs de treino).
- Esforço: baixo (teste); médio se for preciso renderização no servidor.
- Reconferir: nome do curso, carga horária, início e preço aparecem no HTML bruto; robots.txt publica sitemap; cada robô de IA aparece em linha própria.

### Chamado SEO-06 (vale corrigir): marcação estruturada

- Problema: V3.
- Correção: aplicar o JSON-LD acima como modelo (Course, CourseInstance, EducationalOrganization); FAQPage só com a pergunta visível; sem preço e sem certificação até a Ufape liberar.
- Esforço: baixo a médio.
- Reconferir: Rich Results Test sem erro crítico (lembrar que Course Info não gera mais recurso visual); startDate igual ao da página; sameAs com os perfis oficiais.

### Chamado SEO-07 (vale corrigir): estados da turma

- Problema: V5 e V6.
- Correção: implementar a tabela da seção 5 e a rotina de revisão semanal que compara planilha e site (recomendação da auditoria de 22/10).
- Esforço: médio.
- Reconferir: nenhuma turma com data passada mostrada como "aberta" sem a política de entrada; curso de 1 a 3 dias sai de venda no dia seguinte à data.

## 7. Itens para o Search Console [CONFIRMAR] (assim que houver acesso)

1. Relatório Páginas: URLs "Duplicada, o Google escolheu outra canônica", "Página com redirecionamento", "Não encontrada (404)", "Rastreada, não indexada" e "Soft 404" entre os códigos citados.
2. Relatório Desempenho (consultas e páginas): exportar 16 meses; cruzar consultas "pós <especialidade>" com os 12 grupos de C1 e com as provas de bolsa (V2).
3. Sitemap: se inclui os 25 produtos sem venda, o 183 e as 13 provas antigas.
4. Experiência na página e Core Web Vitals por modelo (curso, área, blog, formulário), sobretudo no celular.
5. Inspeção de URL para 678, 68662, 670, 68636, 694 e 183: canonical declarado versus escolhido pelo Google.
6. Consultas pela sigla "ufape" para medir a mistura com ufape.edu.br (V7).
7. Backlinks (relatório Links) das URLs antigas, para priorizar o que não pode quebrar.

## 8. Fatos, suposições e dados que faltam

### Fatos (com fonte)

- 55 páginas de pós no catálogo; 12 cursos repetem o mesmo nome em 27 páginas (contagem feita sobre contexto/catalogo-de-cursos.md, seção 2).
- Odontologia 678 e 68662: mesmo H1, mesmo texto de abertura, mesmo preço (fichas contexto/cursos/pos/678 e 68662). Turmas IV e V. Datas 15/08/2026 (site, 678) e 24/04/2027 (site, 68662), com 15/08/2026 na planilha para a 68662.
- Pneumologia 670: link fora do ar, "O produto requisitado não está mais disponível"; 68636 aberta, turma VIII, início 17 e 18/04/2027, slug igual ao da 670 (fichas e auditorias).
- Slugs de uma mesma pós variam: "pos-graduacao-em-odontologia-veterinaria" (678) e "pos-graduacao-odontologia-veterinaria" (68662); 650 usa "pos-graduacao-lato-em-medicina-de-felinos" (docs/auditoria-do-catalogo-2026-10-22.md).
- Padrão de endereço atual /produto/<código>/<slug>, às vezes /<turma>/<cidade> (fichas e auditoria de 22/10).
- Seis pós fora do padrão de nome (706, 68629, 341, 333, 659, 719), catálogo seção 2.
- 25 páginas sem venda ou fora do ar e o produto de teste 183 (auditorias de 22/10 e 26/10).
- 13 provas de bolsa antigas sem venda (680 a 695) e a 68656 fora do ar (catálogo seção 3).
- A ficha da prova antiga 694 contém lista de aprovados com nome, data de prova passada (04/02/2026) e o texto "reconhecida pelo Ministério da Educação (MEC)" (ficha contexto/cursos/pos/694).
- 36 produtos com data passada e venda ativa (auditoria de 26/10, seção 6). 11 páginas sem data no site (seção 7; 3 delas têm data na planilha).
- 46 páginas com "CERTIFICADO PELO MEC" (auditoria de 26/10, seção 9).
- O workshop de Neuromonitorização tem página própria (/neuro-summit/) e produto 68634 com 24 h e local "Saiba Mais", enquanto a Ufape confirmou 16 h (ficha de eventos e catálogo seção 9).
- Padrão decidido para o novo site: /pos-graduacao/pos-graduacao-em-<área>; nome "Pós-graduação em <área>" (contexto/pos-graduacao.md; briefing da tarefa).
- Graduação: /graduacao e /graduacao/pedagogia nas fichas.
- Google: "Course Info" saiu dos resultados em 2025 e do Search Console em 09/09/2025 (blog do Google, 12/06/2025, e cobertura secundária).
- Google: redirecionamento e rel="canonical" são sinais fortes de canonicalização; sitemap é sinal fraco; para aposentar duplicata, usar redirecionamento permanente (documentação do Google sobre canonicalização).
- OpenAI: o controle do robô de busca e do robô de treino são independentes no robots.txt (documentação de robôs da OpenAI).
- A busca por `site:faculdade.ufape.com.br` não devolveu páginas do domínio; as buscas por "ufape" trazem ufape.edu.br, a Universidade Federal do Agreste de Pernambuco.

### Suposições

- [SUPOSIÇÃO] O Google alterna ou escolhe a canônica errada entre as páginas de turma duplicadas (risco estrutural, sem dados de busca).
- [SUPOSIÇÃO] O servidor atual responde 200 com mensagem nas páginas "fora do ar" (soft 404); pode estar devolvendo 404.
- [SUPOSIÇÃO] Sites Lovable podem entregar o conteúdo só depois de JavaScript; não li o código do ufape-site.
- [SUPOSIÇÃO] Esforço de cada chamado.
- [SUPOSIÇÃO] Tabelas de destino de redirecionamento por proximidade de especialidade (Internação para Terapia Intensiva; 693 para Videocirurgia; 539 e 716 para POCUS).
- [SUPOSIÇÃO] Padrões de URL para cursos livres e eventos (/cursos-livres/, /eventos/); caminhos /carrinho e /checkout no robots.txt.
- [SUPOSIÇÃO] Mapeamento de "Semipresencial" para "blended" no schema.
- [SUPOSIÇÃO] Consultas prováveis na tabela da V2 (sem exportação de busca).
- [SUPOSIÇÃO] Manter os 301 por 12 meses, a partir de cobertura de imprensa especializada sobre orientação do Google; não verificada na documentação oficial.
- [SUPOSIÇÃO] Buscas só pela sigla trazem resultados de outra instituição.

### Dados que faltam

- [CONFIRMAR] Acesso ao Search Console (desempenho, páginas, sitemap, experiência) e ao GA4.
- [CONFIRMAR] robots.txt e sitemap atuais; código HTTP real das páginas fora do ar (670, 68656, 638).
- [CONFIRMAR] HTML renderizado e HTML bruto das quatro páginas-modelo; relatório de velocidade por modelo no celular.
- [CONFIRMAR] Rastreamento completo (links quebrados, cadeias de redirecionamento, páginas órfãs, título e descrição de cada página, blog).
- [CONFIRMAR] Se o site atual resolve a página só pelo código (ignorando o slug) e que canonical declara hoje.
- [CONFIRMAR] URLs de destino dos anúncios ativos (707, 68604, 68606, 698, 68610, 68608, 573, 623, 68614).
- [CONFIRMAR] Política de entrada em turma já iniciada (pós) e destino dos cursos descontinuados (Internação).
- [CONFIRMAR] Qual página fica nos casos duplicados: 623 e 68637, 643 e 713, 642 e 712, 99 e 433.
- [CONFIRMAR] Decisão da Ufape sobre robôs de treino de IA e sobre a retirada da prova 694 (dado pessoal).
- [CONFIRMAR NO CATÁLOGO] Data da turma VIII de Pneumologia (68636, só no site), data de 68662, preço e turma de 662, antes de alimentar o novo site.
- [CONFIRMAR] Texto oficial de certificação (P1 do plano), enquanto a frase "CERTIFICADO PELO MEC" estiver nas 46 páginas, não copiar para o site novo.
- [CONFIRMAR] Autorização de docentes para marcação Person (P13).
- [CONFIRMAR] Perfis oficiais e portais externos para sameAs e consistência da marca.

## Fontes

- Google Search Central, "Simplifying the search results page" (12/06/2025): https://developers.google.com/search/blog/2025/06/simplifying-search-results
- Cobertura sobre a remoção de tipos de dados estruturados e do relatório no Search Console (09/09/2025): https://ppc.land/google-deprecates-seven-structured-data-types-to-simplify-search-results/ e https://searchengineland.com/google-drops-reporting-on-several-structured-data-types-461744
- Google Search Central, canonicalização e duplicatas: https://developers.google.com/search/docs/advanced/guidelines/duplicate-content
- Orientação de manter redirecionamentos 301 por pelo menos um ano (fonte secundária): https://www.searchenginejournal.com/google-keep-301-redirects-in-place-for-a-year/ e https://searchengineland.com/url-changes-is-not-so-simple-for-google-search-378648
- OpenAI, visão geral dos robôs (OAI-SearchBot, GPTBot, ChatGPT-User): https://developers.openai.com/api/docs/bots
- Resultado de busca com a sigla UFAPE de Pernambuco (edital BIA, 2026.1): https://ufape.edu.br/sites/default/files/arquivos/Edital%20Interno%20n%20010%202026.1%20-%20BIA-UFAPE.docx%20-%20Programas%20Acad%C3%AAmicos%20da%20UFAPE.pdf
- Material interno: contexto/ufape-geral.md, contexto/pos-graduacao.md, contexto/catalogo-de-cursos.md, docs/auditoria-do-catalogo-2026-10-22.md, docs/auditoria-do-catalogo-2026-10-26.md, contexto/cursos/, saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md.

## Próximo passo

Próximo agente sugerido: seo-on-page (título, slug, descrição e estrutura da página do curso com turmas dentro). Antes de qualquer chamado ir ao time do site, passa pelo qa-de-marketing e pela aprovação da pessoa do marketing.
