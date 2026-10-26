# Análise CRO: Cursos Livres, grupo de estudos e evento (raio-x de uma página-modelo por tipo)

- **Agente:** analise-cro (departamento 08 Conversão), etapa 1.30 da camada 1
- **Linha:** livres (inclui uma página da linha eventos, o workshop de Neuromonitorização, porque a etapa pediu os dois tipos no mesmo arquivo)
- **Data:** 26/10/2026
- **Skill usada:** .claude/skills/raio-x-de-pagina/SKILL.md
- **Status:** rascunho para o qa-de-marketing e para a aprovação da pessoa do marketing. Nada foi publicado, enviado ou pago.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md
  - contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seções 4, 5, 7 e 9, para conferir dados)
  - templates/pagina-da-turma.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1, 2 e 7, e as seções 3 e 4 para prazos e ondas)
  - auditorias/08-conversao.md e auditorias/conformidade-educacional.md
  - Fichas (seção "Texto da página"): contexto/cursos/livres/573-curso-hands-on-de-ecocardiografia-veterinaria-basica-sao-paulo.md, contexto/cursos/livres/411-curso-de-ecocardiograma-em-pequenos-animais.md, contexto/cursos/livres/713-grupo-de-estudo-em-internacao-e-terapia-intensiva-anual-2026.md, contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
  - Leitura de apoio, só para comparar: contexto/cursos/livres/68665-grupo-de-estudos-em-cardiologia-e-ecocardiografia-veterinaria.md

## Como ler este documento

- **Evidência (E):** está no texto copiado da página, na ficha ou no catálogo, ou é conta feita a partir desses dados (a conta aparece indicada).
- **Hipótese (H):** opinião do agente sobre o efeito na conversão. Toda hipótese leva [SUPOSIÇÃO].
- **Lado de quem resolve:** SQUAD (texto que a squad escreve), SITE (mudança no site atual ou na plataforma nova) e UFAPE (decisão ou confirmação da Ufape).
- **Impacto:** alto, médio ou baixo, avaliação do agente, não medida.

### Limites desta análise

- Não há dado de tráfego, GA4, mapa de calor, gravação de sessão nem taxa de conversão. Tudo que depende de número vira [CONFIRMAR].
- Não consegui abrir faculdade.ufape.com.br. O texto copiado não mostra layout, imagens, botões flutuantes, cabeçalho, rodapé nem o botão de WhatsApp. O que digo sobre "primeira tela do celular" é inferido pela ordem do texto e é [SUPOSIÇÃO] até alguém abrir a página no celular. [CONFIRMAR no site, no celular]
- Que a maior parte dos candidatos chega pelo celular é [SUPOSIÇÃO] até confirmar no GA4.
- Teste A/B exige tráfego medido. Os testes abaixo são desenhos para o agente desenho-de-experimentos refinar.
- Pontos de conformidade (frase de certificação, urgência, preço no cartão, política de reembolso) vão para a lista de cada página. Não foram reescritos.
- Docentes: não são nomeados neste arquivo. Nomes e imagens só entram em peça com autorização registrada [CONFIRMAR autorização].

---

## Página 1: Curso livre presencial, 573 Curso Hands-On de Ecocardiografia Veterinária Básica (São Paulo)

**Dados conferidos no catálogo (seção 4):** São Paulo, modalidade escrita "Semiprensecial" (como está no site), início 14/11/2026 (planilha e site), 28 h, R$ 2.350,00 à vista (Pix ou boleto) ou 10x de R$ 303,00 no cartão, status aberto. Faltam 19 dias (conta a partir de 26/10/2026). Está na onda 1, com campanha ativa. A visão de campanhas mostra 29/11 para este curso, contra 14/11 do catálogo (pendência P6 do plano do cmo).

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | Título "Curso Hands-On de Ecocardiografia Veterinária Básica", com a técnica e o nível (E) | Passa |
| Para quem? | "Médicos Veterinários que buscam aprimorar suas habilidades..." só na seção PÚBLICO-ALVO, depois de programação e diferenciais (E). O topo diz "Domine a Técnica e Realize Diagnósticos Precisos" sem dizer para quem. | Passa em parte |
| Qual modalidade? | "Semiprensecial" (erro de grafia) e 28 horas. A divisão 16 h de prática e 12 h de teoria online aparece só mais abaixo (E) | Passa em parte |
| O que fazer agora? | "Garanta sua vaga!" e COMPRAR (E) | Passa |

### O que já funciona (E)

- Promessa de resultado concreta e coerente com o objetivo: "realizar cortes ecocardiográficos básicos com segurança e precisão".
- Diferenciais que respondem a "quanta prática real": 16 horas de imersão, exames em animais reais, supervisão, câmeras robóticas e monitores, casos clínicos reais.
- Programação com 7 tópicos específicos e carga horária dividida entre prática e teoria; as 12 h de teoria ficam gravadas por 6 meses.
- Data e horários informados.
- Preço à vista e parcelado informados no topo.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | Pagamento confuso e com atrito manual. O topo diz "à vista (Pix ou boleto) ou 10x de R$ 303,00 no cartão". O bloco INVESTIMENTO diz "À vista: R$ 2.350,00 (boleto bancário)", "Parcelado: Até 10x de R$ 303,00 carta de crédito" (provável erro de "cartão") e "6 x de 550 reais no boleto" com a instrução de pedir o boleto por e-mail à secretaria. O total no cartão (R$ 3.030,00, conta: 10 x 303) e no boleto parcelado (R$ 3.300,00, conta: 6 x 550) não é mostrado. O e-mail citado é diferente do e-mail da secretaria em ufape-geral.md (duvidas@intercursos.com.br). | Preço e condições | E; H (o pedido manual por e-mail derruba a compra) [SUPOSIÇÃO]; [CONFIRMAR qual e-mail e qual fluxo valem] | Alto | UFAPE e SITE |
| 2 | "Turma reduzida" e "Garanta sua vaga!" sem número de vagas, sem turma mínima e sem regra de cancelamento ou adiamento. As pós têm esse aviso; este curso não tem. | Confiança, urgência | E (ausência); H (insegurança de quem vai viajar) | Alto | UFAPE (regra), SQUAD (texto) |
| 3 | Horários divergentes e provisórios: sábado "das 08:00 às 18hs" na seção de data contra "08:00 às 13:00 e 14:00 às 19:00" em HORÁRIO; e a nota "poderá sofrer alteração, à combinar com a turma". Quem compra passagem não sabe a hora de saída do sábado. | Clareza da oferta | E | Médio a alto | UFAPE |
| 4 | Prova de autoridade fraca: um docente listado, só com nome e título; "profissionais experientes" está no plural. Sem depoimento, sem foto das aulas, sem bio. | Prova e confiança | E (ausência); H (efeito) | Médio a alto | UFAPE (autorização) e SITE |
| 5 | Falta definir o que é prática: quantos alunos por aparelho, quantos animais, se o aluno realiza o exame com as próprias mãos durante as 16 h. A promessa é boa, a medida é invisível. | Objeções sem resposta (quanto de prática real, objeção 3 da linha) | E (ausência); H | Médio a alto | UFAPE |
| 6 | Pré-requisitos e "o que levar" não existem. Para um curso "básico" e para quem chega de fora, falta dizer se precisa de experiência prévia e o que trazer. | Informação que falta | E | Médio | SQUAD e UFAPE |
| 7 | Logística de viagem (hospedagem, como chegar) ausente. Objeção 2 da linha (deslocamento). | Objeções sem resposta | E (ausência) | Médio | UFAPE |
| 8 | Só COMPRAR para R$ 2.350,00, sem "falar com o time". | Chamada para ação | E (ausência no texto); H [SUPOSIÇÃO] | Médio | SITE e SQUAD |
| 9 | Sem próximo passo para quem não pode ir em 14/11: não há link para o curso online de Ecocardiograma (411, no catálogo) nem para a Pós em Ecocardiografia (698, ver pendência P4 sobre a data no site). | Chamada para ação, venda cruzada | E (ausência); H [SUPOSIÇÃO] | Médio | SQUAD e SITE |
| 10 | Divergência de data entre o catálogo (14/11) e a visão de campanhas (29/11): se o anúncio levar uma data diferente da página, falha a regra "página de destino entrega o que o anúncio prometeu". | Conformidade | E (plano do cmo, P6) | Alto para o anúncio | UFAPE |
| 11 | "Semiprensecial" no topo e sem frase de certificação ou de que curso livre não é diploma. | Confiança, conformidade | E | Baixo a médio | UFAPE |

### Correções por prioridade

**O que a squad escreve**

1. Bloco "Investimento" em linguagem simples (a frase de apoio, sem valor): "Escolha a forma de pagamento que melhor cabe no seu bolso. Mostramos o valor de cada parcela e o total de cada opção, para você comparar antes de decidir. Tem dúvida? Fale com o time." Os valores e totais vêm do banco.
2. Bloco "Como é a prática" (texto sem número): "Você realiza os exames com os equipamentos do curso, em animais reais, com acompanhamento de quem ensina. A teoria vem gravada para você estudar antes e depois do encontro presencial. [CONFIRMAR: alunos por equipamento e por docente]".
3. Bloco "Para quem é e o que levar" a partir do público da ficha: médico veterinário que quer incluir ecocardiograma na rotina; clínico que já faz ultrassom e quer dominar o coração; profissional que precisa de segurança nos cortes básicos. [CONFIRMAR pré-requisitos]. "O que levar": [CONFIRMAR].
4. Bloco "Se a turma não fechar" (texto) depois da confirmação da regra: "Se o curso for adiado ou a turma não for formada, avisaremos [CONFIRMAR prazo] e [CONFIRMAR devolução]. Reserve passagem e hotel com essa informação em mãos."
5. Hero. Título (até 70 caracteres): "Curso Hands-On de Ecocardiografia Veterinária Básica". Subtítulo (até 160): "Aprenda os cortes ecocardiográficos básicos na prática, com animais reais, equipamentos de qualidade e acompanhamento de quem ensina." Os fatos vêm da ficha. Não prometer "o melhor diagnóstico".
6. FAQ: "Preciso ter experiência com ultrassom?" ([CONFIRMAR]), "A parte online fica por quanto tempo?" (resposta com o número do banco), "Posso pagar no boleto parcelado?" ([CONFIRMAR]), "O que acontece se eu não puder ir?" ([CONFIRMAR]).
7. Frase de apoio para o link do curso online 411 ("Quer começar pela teoria? Conheça o curso online de ecocardiograma"), só se a Ufape aprovar a venda cruzada.

**Site ou plataforma nova**

1. Checkout que ofereça Pix, cartão e boleto parcelado sem passar por e-mail. Mostrar total de cada opção. Corrigir "carta de crédito".
2. Campos de dado: vagas, turma mínima, política de adiamento, horários firmes (um só), modalidade com grafia correta.
3. WhatsApp ou formulário curto ao lado do COMPRAR, com eventos no GA4.
4. Link para o curso online 411 e para a pós de ecocardiografia, quando a data dela for corrigida no site.
5. Resumo de rotina em uma faixa no topo: dias, carga horária prática e online, local.

**Ufape**

- Quantidade de vagas, regra de turma mínima e de adiamento; horários finais; qual e-mail ou fluxo vale para boleto parcelado; qual data vale (14/11 ou 29/11).
- Dados reais de prática (alunos por equipamento e animais).
- Autorização para depoimento, imagem e bio do docente.

### As 3 principais correções com teste

**Correção 1: pagamento claro e sem passo manual (problema 1)**
- O que muda: totais por opção, checkout com boleto parcelado direto, correção de texto e de e-mail; frase de apoio do item 1.
- Hipótese [SUPOSIÇÃO]: se todas as formas de pagamento tiverem total claro e fecharem na própria página, mais visitantes que chegam ao botão concluem a compra, porque hoje o boleto parcelado depende de um e-mail.
- Teste: antes e depois (a data do curso é próxima e o tráfego provavelmente pequeno) ou A/B se o checkout permitir. Métrica primária: compras por visitante da página. Métrica de apoio: pedidos de boleto por e-mail à secretaria (contagem semanal). Proteção: percentual de compras no cartão com total maior. [CONFIRMAR dados]

**Correção 2: confiança na turma, com vagas, turma mínima e regra de adiamento (problema 2 e 3)**
- O que muda: campos de dado e bloco "Se a turma não fechar".
- Hipótese [SUPOSIÇÃO]: se a página disser quantas vagas existem e o que acontece se o curso não ocorrer, mais visitantes compram sem esperar, porque quem viaja teme perder passagem.
- Teste: antes e depois. Métrica: compras e conversas sobre "tem vaga" no WhatsApp. Se houver número real de vagas restantes, o site pode mostrar "vagas restantes" como informação real (a squad não escreve "últimas vagas" sem esse número). [CONFIRMAR dados]

**Correção 3: provar a prática (problemas 4 e 5)**
- O que muda: bloco "Como é a prática" com dados de equipamentos e alunos, bio curta e autorizada do docente, vídeo ou fotos da aula anterior (escolha do editor).
- Hipótese [SUPOSIÇÃO]: se a página mostrar de forma concreta a quantidade de prática e quem ensina, mais visitantes confiam e compram, porque a objeção do público é a quantidade real de prática.
- Teste: A/B do bloco novo contra o atual, métrica primária: cliques em COMPRAR e conversas por visitante. [CONFIRMAR tráfego]. Se o tráfego for baixo, deixar o teste para as próximas edições.

### Comparação com templates/pagina-da-turma.md (Cursos Livres)

| Seção do template | Na página 573 |
|---|---|
| hero | Existe, sem para quem |
| numeros | Existe |
| sobre | Existe (objetivo e imersão) |
| para_quem | Só no fim |
| conteudo | Existe (programação) |
| docentes | Um docente, sem bio |
| certificacao | Ausente |
| depoimentos | Ausente |
| investimento | Existe, com divergências |
| local_e_datas | Existe, horários divergentes |
| faq | Ausente |
| formulario | Ausente (só COMPRAR) |
| cta_final | Ausente |

### Conformidade (lista, não reescrita)

- Curso livre não pode sugerir diploma nem equivalência: a página não traz nada sobre certificação. Texto padrão [PREENCHER COM A REGULAÇÃO]. A seção de certificação fica oculta até haver texto aprovado.
- "Garanta sua vaga!" e "Turma reduzida": só com número real de vagas, que a página não mostra. Não usar "vagas limitadas" nem "últimas vagas" sem esse número.
- Superlativos ("o que há de melhor em diagnóstico por imagem" é do público-alvo; "equipamentos de última geração" é afirmação sobre a Ufape): exigem fonte verificável.
- Preço: a página mostra a parcela, mas não o total no cartão (R$ 3.030,00, conta) nem o total do boleto parcelado (R$ 3.300,00, conta). A regra da linha pede mostrar o total quando for diferente do à vista.
- Página de destino e anúncio: a data do catálogo (14/11) difere da visão de campanhas (29/11).
- Formulário de lead e checkout: finalidade dos dados e política de privacidade [CONFIRMAR no site].
- O e-mail citado na página difere do canal oficial de secretaria do contexto; confirmar.

---

## Página 2: Curso online gravado, 411 Curso de Ecocardiograma em Pequenos Animais (aberto, contínuo)

**Dados conferidos no catálogo (seção 5):** online, 12 h, R$ 420,00 à vista (Pix ou boleto) ou 6x de R$ 98,00 no cartão, status aberto (contínuo), venda o ano todo. Fonte "só no site". Escolhido como modelo por ter irmão presencial (573), preço de entrada e tópicos explícitos. A página tem "Turma I" mesmo sendo contínuo. Está no recorte de contínuos (onda 2).

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | "Curso de Ecocardiograma em Pequenos Animais", 12 horas, online (E) | Passa |
| Para quem? | PÚBLICO-ALVO só depois do cronograma (E) | Falha [SUPOSIÇÃO] |
| Qual modalidade? | "Online". Não diz se é gravado, ao vivo ou os dois (E). O cronograma e o título não resolvem; a ficha chama de "curso online" | Passa em parte |
| O que fazer agora? | COMPRAR (E) | Passa |

### O que já funciona (E)

- Preço de entrada baixo, em Pix, boleto ou cartão.
- Cronograma específico com 14 itens em ordem lógica (modos, função sistólica e diastólica, cardiomiopatias, valvopatia, hipertensão pulmonar, cardiopatias congênitas, prática).
- Público amplo bem descrito (intensivistas, anestesistas, clínicos, estudantes).
- Acesso por 120 dias e canal de dúvidas por e-mail informados.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | A página não tem texto de apresentação: não explica o que o aluno vai conseguir fazer, não diz por que este curso e não o conteúdo gratuito (objeção 1 da linha). Vai de preço e números direto para a lista de tópicos. | Clareza da oferta, valor percebido | E (ausência de texto sobre/objetivo); H (efeito) [SUPOSIÇÃO] | Alto | SQUAD |
| 2 | Regras de acesso escondidas e incompletas: "Curso completo disponível por 120 dias" fica na seção CONSIDERAÇÕES, no fim. A página não diz quando os 120 dias começam (na compra ou no primeiro acesso) nem se as aulas são gravadas. "Turma I" aparece em curso contínuo. | Preço e condições | E; H | Alto | SITE (campos) e UFAPE (regra) |
| 3 | Sem prova: sem aula de amostra, sem depoimento, sem bio do docente (um nome com título), sem foto, sem número de alunos. Em curso gravado de preço baixo, a amostra costuma pesar [SUPOSIÇÃO]. | Prova e confiança | E (ausência); H | Alto | UFAPE e SITE |
| 4 | Parcelamento sem total: 6x de R$ 98,00 somam R$ 588,00 (conta), 40% a mais que o à vista de R$ 420,00. O total não é mostrado. | Preço e condições | E (conta); H (efeito) | Médio | SITE |
| 5 | Contato: só "Tira dúvidas pelo e-mail" (não dá para saber se é suporte de aluno ou dúvida antes da compra). Há um link para a página de login da plataforma (https://intercursos.com.br/account/login) dentro da página de venda: leva o visitante para outro domínio e para uma tela de login. | Atrito e distração | E; H (vazamento de visitantes) [SUPOSIÇÃO] | Médio | SITE |
| 6 | Cronograma sem duração por tópico, sem quantidade de aulas e sem dizer onde está a "PRÁTICA DE ECOCARDIOGRAMA" em um curso 100% online. | Clareza | E | Médio | SITE e UFAPE |
| 7 | Sem próximo passo: não leva ao curso presencial hands-on (573), a outro curso online relacionado (por exemplo, eletrocardiograma 395) nem à pós. É a porta de entrada da linha, e a página não a usa. | Chamada para ação, venda cruzada | E (ausência); H [SUPOSIÇÃO] | Médio | SQUAD e SITE |
| 8 | Sem frase de certificação ou de que curso livre não é diploma. | Conformidade, confiança | E | Médio | UFAPE |
| 9 | Sem FAQ e sem formulário de lead. | Chamada para ação | E | Médio | SITE e SQUAD |

### Correções por prioridade

**O que a squad escreve**

1. Hero. Título: "Curso de Ecocardiograma em Pequenos Animais". Subtítulo (até 160 caracteres): "Aprenda a interpretar o ecocardiograma de cães e gatos com segurança, das medidas básicas às cardiopatias congênitas, no seu ritmo e pela plataforma da Ufape." (O "ritmo próprio" depende de confirmar que o conteúdo é gravado. [CONFIRMAR])
2. Bloco "Sobre" (2 a 3 parágrafos, sem número), baseado só no cronograma da ficha: o curso conduz da base (modos, mensuração e função cardíaca) às doenças mais comuns na rotina (cardiomiopatias, valvopatia mitral, hipertensão) e às cardiopatias congênitas, e fecha com prática de ecocardiograma. Trazer a pergunta que o clínico faz ("como sei que estou medindo e interpretando certo?"). [SUPOSIÇÃO: a dor do clínico; validar com o WhatsApp de vendas].
3. Bloco "Por que pagar se existe conteúdo gratuito" (objeção 1): em vez de atacar o conteúdo gratuito, mostrar o que a página prova: sequência organizada de tópicos, professor identificado, acesso por prazo definido, dúvidas por e-mail. [CONFIRMAR o que mais há: certificado, material, comunidade].
4. Bloco "Como funciona o acesso" logo abaixo do preço: onde assistir, por quanto tempo o conteúdo fica disponível (valor do banco), quando o prazo começa ([CONFIRMAR]) e como tirar dúvidas.
5. FAQ: "Preciso ter ecocardiógrafo?", "Posso assistir pelo celular?", "Recebo certificado?" (somente com o texto aprovado), "Qual a diferença entre este curso e o curso hands-on presencial?"
6. Frase para o próximo passo: "Quer treinar a técnica na prática? Conheça o curso presencial de ecocardiografia." [só se a Ufape aprovar a venda cruzada e a 573 estiver aberta]

**Site ou plataforma nova**

1. Campos de dado: tempo de acesso e início da contagem, número de aulas e duração por tópico, formato (gravado), troca de "Turma I" por rótulo de acesso contínuo.
2. Total do cartão mostrado (R$ 588,00 pela conta, conferir juros reais no checkout).
3. Remover ou trocar o link de login por um link de "já sou aluno" fora do fluxo de compra (rodapé), e abrir contato por WhatsApp ou formulário.
4. Aula de amostra (vídeo curto) e área de depoimentos, escolhidas pelo editor.
5. Link para cursos relacionados e para a pós.

**Ufape**

- Autorizar a aula de amostra, a bio e imagem do docente e depoimentos.
- Confirmar as regras de acesso (início e fim dos 120 dias, se há renovação) e se o curso tem certificado.
- Dizer se a "PRÁTICA DE ECOCARDIOGRAMA" é gravada, e como.

### As 3 principais correções com teste

**Correção 1: texto "Sobre" e hero com para quem e resultado (problema 1)**
- O que muda: hero e bloco "Sobre" do item 1 e 2.
- Hipótese [SUPOSIÇÃO]: se a página explicar o que o clínico consegue fazer depois do curso, mais visitantes clicam em COMPRAR, porque hoje a página só mostra uma lista de tópicos e um preço.
- Teste: A/B (página atual contra a nova), métrica primária: cliques em COMPRAR e compras por visitante. Métrica de apoio: tempo na página e rolagem. Tráfego de curso online costuma ser maior que o de turma presencial [SUPOSIÇÃO]; [CONFIRMAR] o número real.

**Correção 2: regras de acesso visíveis perto do preço, mais total do cartão (problemas 2 e 4)**
- O que muda: bloco "Como funciona o acesso" e total do parcelamento.
- Hipótese [SUPOSIÇÃO]: se o visitante vir o prazo e o formato antes de comprar, menos visitantes abandonam por dúvida sobre acesso, e menos pedidos de suporte chegam depois, porque hoje o prazo está no fim da página.
- Teste: A/B ou antes e depois. Métrica primária: compras por visitante. Proteção: perguntas sobre acesso no e-mail e no WhatsApp. [CONFIRMAR dados]

**Correção 3: prova com aula de amostra, bio do docente e depoimentos (problema 3)**
- O que muda: vídeo de amostra e prova de quem ensina, escolhidos pelo editor.
- Hipótese [SUPOSIÇÃO]: se o visitante ver um trecho da aula e quem ensina, a confiança sobe e mais visitantes compram, porque no gravado não há outra forma de testar o produto.
- Teste: A/B com e sem vídeo de amostra. Métrica primária: compras por visitante. Métrica de apoio: reprodução do vídeo. Proteção: tempo de carregamento da página no celular [CONFIRMAR].

### Comparação com templates/pagina-da-turma.md (Cursos Livres)

| Seção do template | Na página 411 |
|---|---|
| hero | Título e preço, sem subtítulo |
| numeros | Existe (horas, modalidade, turma, local) |
| sobre | Ausente |
| para_quem | Só no fim |
| conteudo | Existe (cronograma) |
| docentes | Um docente |
| certificacao | Ausente |
| depoimentos | Ausente |
| investimento | Existe, sem total do cartão |
| local_e_datas | Local é a plataforma; sem datas (contínuo) |
| faq | Ausente |
| formulario | Ausente |
| cta_final | Ausente |

### Conformidade (lista, não reescrita)

- Curso livre: texto de que não confere diploma nem equivale à pós [PREENCHER COM A REGULAÇÃO].
- Preço: mostrar o total do cartão (R$ 588,00, conta) quando for diferente do à vista (R$ 420,00).
- Estudantes de graduação aparecem no público. Confirmar se o certificado vale para eles e com qual texto.
- Sem urgência falsa: curso contínuo não tem "vagas limitadas".
- Depoimentos e imagem do docente: autorização registrada.
- Direito de arrependimento de compra online (7 dias) e política de reembolso: ver revisão jurídica da Ufape; a página não informa. [CONFIRMAR]
- Link para outro domínio (intercursos.com.br) na página de venda: conferir com a regra de página de destino sem redirecionamento inesperado.

---

## Página 3: Grupo de estudos, 713 Grupo de Estudo em Internação e Terapia Intensiva (Anual 2026)

**Dados conferidos no catálogo (seção 7):** online, "2 h" (no catálogo é a duração do encontro, não a carga total), R$ 734,00 à vista (Pix ou boleto) ou 10x de R$ 88,00 no cartão, status aberto (contínuo). Fonte "só no site". Existe duplicidade com 643 (Anual 2025/2026), pendência P7 do plano do cmo. O plano da onda 1 inclui os grupos 68665 e 68666 (R$ 100,00); este é o modelo de grupo anual de maior ticket.

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | Título "Grupo de Estudo em Internação e Terapia Intensiva - Anual 2026" (E). Quem não conhece o formato "grupo de estudo" não sabe se é aula, comunidade ou curso | Passa em parte |
| Para quem? | A página não tem público-alvo (E) | Falha |
| Qual modalidade? | Online (E) | Passa |
| O que fazer agora? | COMPRAR (E). Mas o período está confuso (ver problema 1) | Passa em parte |

### O que já funciona (E)

- Ementa muito concreta: 23 aulas com data, dia da semana e tema (por exemplo, choque, sepse, ventilação mecânica, gasometria, lesão renal aguda). Dá para ver o que se aprende.
- Formato bem descrito: discussão de casos, artigos, videoaulas, aulas demonstrativas com casos reais; grupo de WhatsApp para os links.
- Corpo docente amplo (20 docentes) e quatro deles marcados como "(EUA)". Esse é um sinal de autoridade que a página não explora em texto.
- Regras de acesso às gravações descritas (120 dias para as discussões, 30 dias para as demonstrativas, liberação 7 dias depois).
- Preço de entrada acessível para o ano.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | O produto é descrito de formas que se contradizem: faixa "JUNHO 2026/ MAIO 2027", ementa de 04/03/2026 a 23/12/2026 (mais uma aula "a definir"), nome "Anual 2026", "Inicio mês JUNHO 2025" em CONSIDERAÇÕES, "de 1 à 2 horas semanais" contra "encontros a cada 15 dias". O visitante não sabe o que compra nem por quanto tempo. | Clareza da oferta | E (frases lado a lado); H (efeito) | Alto | UFAPE (corrigir) e SQUAD (texto) |
| 2 | O que recebe quem entra agora? Pela ementa, 17 das 23 aulas já aconteceram em 26/10/2026 (a última é de 14/10/2026), restam 5 com data (de 28/10 a 23/12) e uma "a definir". As gravações ficam 120 dias e liberadas 7 dias depois; aulas antigas podem já ter vencido. O preço é o mesmo de quem entrou em março. A página não explica o que entra no valor para quem chega tarde. | Preço e condições | E (conta sobre a ementa); H (hesitação e reclamação pós-venda) [CONFIRMAR regras] | Alto | UFAPE e SQUAD |
| 3 | Sem "para quem": sem público, sem nível exigido, sem dizer se serve a clínico geral, residente ou intensivista. Sem explicação do que é um grupo de estudo para quem nunca fez. O texto de abertura é uma frase incompleta ("Fazer parte de uma comunidade que promova..."). | Clareza | E | Médio a alto | SQUAD |
| 4 | Política "em caso de desistência, o valor investido não será reembolsável" sem explicação do direito de arrependimento de compra online e sem total do cartão (10 x R$ 88,00 = R$ 880,00, 20% acima do à vista de R$ 734,00; conta). | Preço e condições, conformidade | E (conta); [CONFIRMAR com regulação e jurídico] | Médio a alto | UFAPE |
| 5 | Prova de autoridade só em lista de nomes (20), sem bios, sem depoimento de participantes do ciclo anterior, sem exemplo de encontro. | Prova | E (ausência); H | Médio | UFAPE e SITE |
| 6 | Duplicidade 643 e 713: duas páginas de grupo parecido (Anual 2025/2026 e Anual 2026) com o mesmo preço. O visitante e o anúncio podem cair na versão errada. | Confiança, atrito | E (catálogo e plano do cmo, P7) | Médio | UFAPE |
| 7 | Sem venda cruzada para a pós de Terapia Intensiva (turmas abertas no catálogo, 68635 e 68623) nem para outros cursos. É onde o grupo pode alimentar a pós [SUPOSIÇÃO]. | Chamada para ação | E (ausência); H | Médio | SQUAD e SITE |
| 8 | Erros de digitação ("experiencia", "qual sempre diferenciou", "Inicio mês JUNHO 2025"), duas aulas com tema parecido (aulas 09 e 14: "Gasometria e distúrbios ácido-base" e "Gasometria / função pulmonar"). | Confiança | E | Baixo a médio | UFAPE |
| 9 | Só COMPRAR, sem "falar com o time". | Chamada para ação | E (ausência) | Médio | SITE |

### Correções por prioridade

**O que a squad escreve**

1. Hero (depois que a Ufape definir período e frequência). Título: "Grupo de Estudo em Internação e Terapia Intensiva". Subtítulo (até 160 caracteres): "Discuta casos clínicos e artigos com especialistas, em encontros online periódicos, com acesso às gravações e comunidade no WhatsApp." Sem número, sem data. [CONFIRMAR frequência e período]
2. Bloco "O que é um grupo de estudo" (3 linhas): "Um grupo de estudo reúne médicos veterinários para discutir casos reais e a literatura mais recente de forma informal. Você participa ao vivo ou assiste às gravações, tira dúvidas e acompanha a rotina de quem atua na área."
3. Bloco "Para quem é": médico veterinário que atende pacientes críticos ou internados; clínico que quer rotina de atualização contínua; intensivista que quer discutir casos e ver demonstrações. [CONFIRMAR nível mínimo]
4. Bloco "O que está incluído quando você entra" (depende de decisão): encontros daqui para a frente, gravações dentro do prazo, grupo de WhatsApp, certificado (conforme regra [CONFIRMAR]). Linhas "se você entra com o ciclo em andamento": [CONFIRMAR: acesso a gravações anteriores, desconto proporcional ou renovação].
5. Frase de apoio do investimento e botão: "Entenda o que está incluído antes de decidir. Se ainda tiver dúvida, fale com o time."
6. FAQ: "Preciso estar ao vivo?", "Por quanto tempo fico com as gravações?", "Posso entrar com o grupo já em andamento?", "O que acontece se eu desistir?" (resposta da regra atual, em linguagem simples, com revisão da regulação), "Recebo certificado?" ([CONFIRMAR]).
7. Frase de próximo passo: "Quer se aprofundar? Conheça a pós-graduação em Terapia Intensiva e Emergência Veterinária" apenas depois de a Ufape aprovar a venda cruzada.

**Site ou plataforma nova**

1. Campos de dado: período real do ciclo, frequência, número de aulas e quantas restam, regra de acesso às gravações e para quem entra depois.
2. Mostrar o total do cartão (R$ 880,00, conta) e a regra de reembolso e arrependimento em linguagem simples, perto do botão.
3. Calendário recolhido e "próxima aula" em destaque (dado do banco).
4. Remover ou unificar 643 e 713 (decisão da Ufape).
5. WhatsApp ou formulário curto ao lado do COMPRAR; eventos no GA4.

**Ufape**

- Definir o período e a frequência corretos, o que o entrante tardio recebe, o preço para quem entra com o ciclo em andamento, e qual das duas páginas (643 ou 713) fica à venda.
- Revisão jurídica da frase de não reembolso.
- Bios curtas e autorização para citar docentes e a atuação no exterior.

### As 3 principais correções com teste

**Correção 1: uma descrição única e coerente do ciclo (problema 1)**
- O que muda: a Ufape corrige período, frequência e nome; a squad reescreve o hero e os blocos dos itens 1 a 3.
- Hipótese [SUPOSIÇÃO]: se a página disser sem contradição o que é o grupo, quando acontece e com que frequência, mais visitantes compram e menos pedem esclarecimento, porque hoje a página tem quatro descrições de período.
- Teste: antes e depois, acompanhando perguntas no WhatsApp e compras por visitante. A/B só se houver tráfego para os 713 e 643 juntos. [CONFIRMAR dados]

**Correção 2: "O que entra para quem chega com o ciclo em andamento" (problema 2)**
- O que muda: bloco do item 4 e campos de dado. Depende de decisão da Ufape sobre o produto para o entrante tardio (por exemplo, valor proporcional ou ciclo seguinte; decisão comercial, não da squad).
- Hipótese [SUPOSIÇÃO]: se a página disser o que o entrante tardio recebe, o preço parece justo e as reclamações pós-venda diminuem, porque hoje o valor integral é cobrado com 17 das 23 aulas já realizadas.
- Teste: antes e depois nas compras e nos pedidos de cancelamento ou reclamação nas primeiras semanas depois da compra. [CONFIRMAR dados de suporte]

**Correção 3: "Para quem" e "o que é um grupo de estudo" no topo (problema 3)**
- O que muda: itens 2 e 3 acima.
- Hipótese [SUPOSIÇÃO]: se o formato e o público forem explicados em linguagem simples, mais visitantes de primeira viagem avançam, porque hoje a página pressupõe que o leitor conhece o formato.
- Teste: A/B de topo (atual contra novo). Métrica primária: cliques em COMPRAR e compras por visitante. Métrica de apoio: rolagem. [CONFIRMAR tráfego]

### Comparação com templates/pagina-da-turma.md

- Não existe o tipo "grupo de estudos" no template (tipos: pos, livre, workshop, simposio). Hoje a página se aproxima do tipo "livre". Seções que faltam em relação ao tipo livre: sobre, para_quem, certificacao com texto aprovado, depoimentos, faq, formulario e cta_final.
- Seções específicas de grupo que o template não prevê: "proxima_aula" (dado), "regra_de_acesso_as_gravacoes" (dado) e "entrada_com_ciclo_em_andamento" (texto e dado). Recomendação ao cmo: criar o tipo na próxima versão do template (decisão P72).
- Comparação com 68665 (grupo de R$ 100,00): a página dele tem agenda em 2026 e 2027, horário "A COMBINAR COM A TURMA" e anotações internas em texto público ("Sugestão ... + ..."), o que indica rascunho sem revisão. Não analisei a 68665 em detalhe. Está fora do escopo desta etapa; fica como nota para o kit leve da onda 1.

### Conformidade (lista, não reescrita)

- Certificado: "Será entregue ao final do curso". Texto padrão de curso livre (não é diploma nem equivale à pós) [PREENCHER COM A REGULAÇÃO]. Condição para receber (presença mínima) não informada.
- Desistência sem reembolso: revisão jurídica e da regulação (direito de arrependimento de compra online) [CONFIRMAR].
- Preço no cartão: mostrar o total.
- Docentes e atuação no exterior: autorização e fonte para qualquer menção em peça.
- Duplicidade 643 e 713: anúncio não pode levar à versão errada.
- Datas e período conflitantes: a peça só usa o período depois de a Ufape definir.
- "A experiência prática será a grande inovação qual sempre diferenciou a UFAPE": afirmação de diferença sem fonte. Não repetir em peça.

---

## Página 4: Evento, Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia (linha eventos)

**Dados conferidos no catálogo (seção 9) e na ficha:** 20 e 21 de novembro de 2026 (planilha e página), Faculdade Ufape, Unidade 2, Av. Tiradentes, 960, São Paulo; presencial, 16 h (8 teóricas e 8 práticas), 30 vagas por ordem de inscrição; Workshop Presencial R$ 1.250,00; Workshop Transmitido + Gravado (só teoria de sexta-feira) R$ 450,00; aluno e ex-aluno com 20% de desconto pelo cupom SIMPNEUROMONIT (cupom confirmado pela Ufape em 26/10/2026). Faltam 25 dias. Campanhas pagas vão direto a esta página (decisão do cliente). Tipo no template: workshop.

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | Há três nomes na abertura ("Workshop de Neuromonitorização Veterinária", "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia" e "Neuromonitorização aplicada") e a frase "Do cérebro à analgesia: monitorando aquilo que realmente importa" (E) | Passa em parte |
| Para quem? | Parágrafo de abertura e faixa "Público alvo" no topo (E) | Passa |
| Qual modalidade? | "Evento presencial, sexta-feira teórica e sábado prático, somente 30 vagas, Certificado UFAPE" (E) | Passa |
| O que fazer agora? | Nenhum botão no texto copiado antes da programação. O bloco "Garanta a sua vaga" vem depois de toda a programação (E) | Falha [SUPOSIÇÃO: no celular, o preço e o botão ficam abaixo de uma programação longa. [CONFIRMAR no site]] |

### O que já funciona (E)

- Informação do evento muito completa: data, local, carga horária, vagas, dois dias com função clara, certificado.
- Programação detalhada por horário, com tema, resumo e responsável de cada bloco.
- Dois formatos de compra (presencial completo e só teoria, transmitida e gravada), com preço de cada um. Dá uma porta mais barata.
- FAQ real, que responde a objeção de nível ("É necessário saber interpretar EEG previamente? Não"), o formato e as vagas.
- Coordenação científica e docentes confirmados com função descrita.
- Certificado "conforme presença", sem frase ligada ao MEC.
- Vagas limitadas com número real (30), por ordem de inscrição.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | Preço e botão só depois de uma programação de dois dias. O topo não traz botão, preço nem "ver ingressos". | Chamada para ação | E (ordem do texto); H (efeito no celular) [SUPOSIÇÃO] | Alto | SITE |
| 2 | Cupom sem código visível: "20% de desconto usando o cupom" não mostra o código, e o vínculo é comprovado "com a secretaria" sem canal ou prazo. Não aparece o valor com desconto (R$ 1.000,00 e R$ 360,00, conta) nem o limite de uso. O público de aluno e ex-aluno é o mais quente. | Preço e condições | E; H [CONFIRMAR onde o código é divulgado e como é validado] | Alto | SITE e UFAPE |
| 3 | Forma de pagamento e parcelamento não aparecem (só o valor). A regra da linha pede mostrar parcelas, valor e condições. | Preço e condições | E (ausência); [CONFIRMAR NO CATÁLOGO] | Alto | SITE e UFAPE |
| 4 | Lista "inclui" ambígua: depois dos dois ingressos aparece uma lista única ("Certificado UFAPE conforme presença; Aulas teóricas da sexta-feira e treinamento prático do sábado; Apostila e material digital, se previsto"). Não fica claro o que o ingresso online recebe (não inclui o sábado) nem como a presença é medida no online. "Se previsto" não é promessa. | Clareza da oferta | E; H | Médio a alto | SITE e SQUAD |
| 5 | Informações práticas ausentes: almoço incluso?, o que levar, como chegar à Unidade 2 (endereço diferente da sede), onde ficar, política de cancelamento e de reembolso, o que acontece se o evento mudar. | Informações que faltam | E (ausência) | Médio a alto | UFAPE e SQUAD |
| 6 | Quatro convidados marcados "A definir" e a frase "A distribuição entre docentes segue em alinhamento com a coordenação" enfraquecem a programação, que já nomeia responsável para cada bloco. | Confiança | E; H | Médio | UFAPE (ocultar até confirmar) |
| 7 | Primeira edição, sem prova social: sem depoimento, sem edição anterior, sem parceiros citados. | Prova | E; H | Médio | UFAPE |
| 8 | Nome do evento muda entre planilha ("I Simpósio"), página (workshop) e loja (produto 68634, que mostra 24 h e está sem data). A página fala em 16 h. Risco de divergência para quem chega pela loja. | Confiança, conformidade | E (ficha e plano, P9) | Médio | UFAPE |
| 9 | Urgência real parcial: "Somente 30 vagas" aparece várias vezes e a data é fixa, mas não há contador de vagas restantes. Sem esse número, a peça não pode dizer "últimas vagas". | Urgência | E; H | Médio | SITE e UFAPE |
| 10 | O rótulo "Para quem decide olhando além do número" no lugar de "Para quem é" é criativo, mas atrasa o entendimento. | Clareza | E; H [SUPOSIÇÃO] | Baixo | SQUAD |

### Correções por prioridade

**O que a squad escreve**

1. Linha de resumo e botão no topo, depois do hero: "Garanta a sua vaga" com um subtítulo de decisão: "Escolha entre o workshop presencial completo e a opção só com a teoria, ao vivo e gravada. Veja o valor de cada uma logo abaixo." Texto do botão: "Ver ingressos". O preço fica no bloco de dado.
2. Bloco "Escolha o seu ingresso" (texto de apoio, sem valor): duas colunas, cada uma com "inclui" e "não inclui". Presencial: sexta teórica, sábado prático, certificado conforme presença. Transmitido e gravado: aulas teóricas de sexta-feira, ao vivo e gravadas. [CONFIRMAR: como a presença é medida e se o certificado vale para essa opção]
3. Bloco "Desconto para aluno e ex-aluno" com passo a passo: "1. Use o cupom na hora da compra. 2. Envie o comprovante de vínculo para a secretaria. 3. Confirme sua condição. [CONFIRMAR: ordem e prazo do passo 2]". O código SIMPNEUROMONIT é dado do evento (confirmado pela Ufape em 26/10/2026). Onde ele aparece na página é decisão do site.
4. FAQ extra (sem número): "O almoço está incluído?" [CONFIRMAR], "O que devo levar?" [CONFIRMAR], "Como chego à Unidade 2?" (com endereço do banco), "Posso pagar parcelado?" [CONFIRMAR], "Posso cancelar ou transferir?" [CONFIRMAR], "O que acontece se houver mudança no programa?" (a página já avisa que a distribuição de docentes segue em alinhamento).
5. O_que_levar: "Nenhum conhecimento prévio de EEG é exigido: a sexta-feira constrói a base" (afirmação da página); demais itens [CONFIRMAR].
6. Para quem (3 a 5 itens a partir de publico_alvo da ficha): anestesiologista que quer decidir com base em sinais além do clínico; intensivista que acompanha pacientes sob bloqueio neuromuscular; residente e pós-graduando que querem aprender a ler EEG e BIS; profissional que quer entender limites e artefatos dos monitores.
7. Resposta citável (40 a 60 palavras, sem número): "O workshop de Neuromonitorização Veterinária é um evento presencial, com um dia teórico e um dia prático, para médicos veterinários que querem interpretar EEG e índices como o BIS na anestesia e na UTI. A teoria também pode ser acompanhada online, ao vivo e gravada."
8. Texto de convite curto para a campanha, alinhado com a página de destino (peça de outro agente, não escrita aqui).

**Site ou plataforma nova**

1. Botão e preços acima da programação, com faixa fixa no celular ("Ver ingressos" visível ao rolar). [CONFIRMAR comportamento atual]
2. Programação em acordeão por dia (sexta e sábado) no celular, com resumo no topo.
3. Mostrar valor com desconto ao aplicar o cupom, e o cupom funcionando no checkout. Mostrar parcelamento.
4. Contador de vagas restantes, só se houver número real e atualizado pelo sistema de inscrições. [CONFIRMAR]
5. Ocultar os convidados "A definir" até a confirmação (regra do template: seção sem confirmação fica oculta).
6. Corrigir a carga horária do produto 68634 na loja (24 h contra 16 h) e dar a ele data.
7. Eventos no GA4: clique em "Ver ingressos", clique em cada ingresso, uso do cupom, início e conclusão do checkout. [CONFIRMAR ferramenta]
8. Mapa e como chegar (dado).

**Ufape**

- Forma de pagamento e parcelamento; política de cancelamento e reembolso; almoço e o que levar.
- Fluxo de comprovação do vínculo de aluno e ex-aluno, prazo e canal.
- Como a presença é medida no ingresso online e o texto de certificado de participação [CONFIRMAR].
- Autorização para uso dos nomes e imagens de docentes em peças.

### As 3 principais correções com teste

**Correção 1: botão e resumo de preços acima da programação (problema 1)**
- O que muda: texto do item 1 e a mudança de site do item 1 acima.
- Hipótese [SUPOSIÇÃO]: se o visitante do celular encontrar o botão e os dois ingressos sem rolar a programação, mais visitantes chegam ao checkout, porque hoje o preço fica depois de dezenas de blocos.
- Teste: A/B das duas ordens, ou antes e depois se o tráfego for pequeno. O evento acontece em 25 dias; um A/B só serve se o tráfego da campanha for alto. Métrica primária: cliques em "Ver ingressos" e inícios de checkout por visitante. Proteção: taxa de rejeição e vendas totais. [CONFIRMAR tráfego]

**Correção 2: cupom e preço com desconto visíveis, e pagamento claro (problemas 2 e 3)**
- O que muda: bloco "Desconto para aluno e ex-aluno", valor com desconto, parcelamento.
- Hipótese [SUPOSIÇÃO]: se o aluno e o ex-aluno virem o código e o valor final, mais deles concluem a compra, porque hoje o cupom não está na página e o público é o mais próximo da marca.
- Teste: antes e depois, medindo usos do cupom por visitante e compras do público de aluno e ex-aluno. Se as mensagens de WhatsApp e e-mail para a base levarem o código, o uso do cupom já mede esse público. [CONFIRMAR CRM]

**Correção 3: ingressos sem ambiguidade e FAQ prático (problemas 4, 5 e 6)**
- O que muda: lista "inclui e não inclui", FAQ com almoço, o que levar, como chegar, cancelamento, parcelamento; ocultar convidados "A definir".
- Hipótese [SUPOSIÇÃO]: se as dúvidas práticas e a diferença entre os ingressos forem respondidas, menos visitantes ficam em dúvida na hora de pagar e menos mensagens de "como funciona" chegam ao time.
- Teste: antes e depois. Métrica primária: compras por visitante. Métrica de apoio: perguntas repetidas no WhatsApp. [CONFIRMAR dados]

### Comparação com templates/pagina-da-turma.md (Workshop)

Ordem padrão: hero, sobre, para_quem, programacao, facilitadores, o_que_levar, investimento, local_e_datas, faq, formulario, cta_final.

| Seção do template | Na página do evento |
|---|---|
| hero | Existe, com três nomes e chips de resumo |
| sobre | Existe (abertura e "Neuromonitorização aplicada") |
| para_quem | Existe, com título criativo |
| programacao | Existe e é forte (por dia e horário) |
| facilitadores | Existe depois do preço (no template vem antes); quatro convidados "A definir" |
| o_que_levar | Ausente (só a resposta do FAQ sobre EEG prévio) |
| investimento | Existe, sem parcelamento e sem valor com desconto |
| local_e_datas | Existe no topo |
| faq | Existe, falta o prático |
| formulario | Ausente no texto copiado (bloco "Garanta a sua vaga" é o mais próximo) |
| cta_final | Existe um bloco de fechamento ("Do cérebro à analgesia..."), sem botão no texto copiado |

### Conformidade (lista, não reescrita)

- Certificado de participação: texto padrão aprovado [CONFIRMAR] (contexto/eventos.md). A página diz "Certificado UFAPE conforme presença". Não há referência ao MEC.
- "Apostila e material digital, se previsto": não prometer apostila em peça (alerta da ficha).
- Docentes: usar só os confirmados (decisão de 26/10/2026) e só com autorização registrada [CONFIRMAR autorização]. "A definir" na página pública.
- Nome do evento e da carga horária divergem entre planilha, página e loja (16 h na página; 24 h no produto 68634).
- Preço e parcelas: faltam parcelas e valor de cada uma. Cupom: regra, público elegível e prazo de validade precisam estar claros (a página não traz validade nem limite de uso).
- Urgência: "Somente 30 vagas" tem número real; "últimas vagas" só com número de vagas restantes, que não existe.
- Política de cancelamento, adiamento e reembolso: ausente. [CONFIRMAR]
- Formulário e checkout: finalidade dos dados e política de privacidade [CONFIRMAR no site].
- Campanha direta para esta página: a página de destino precisa mostrar o que o anúncio prometer (preço, data, vagas).

---

## Síntese: padrões que se repetem nas quatro páginas

1. **Um só caminho de ação, COMPRAR, sem segundo passo (E).** Nenhuma das quatro mostra no texto copiado WhatsApp, formulário de lead ou "receber o programa". O template exige "formulario". Hipótese [SUPOSIÇÃO]: visitante de ticket médio ou alto (573, evento) conversa antes de pagar; já no ticket baixo (411, grupos) o botão direto deve bastar, e o ganho vem da clareza.
2. **O preço do cartão aparece sem o total (E).** 573: R$ 3.030,00 contra R$ 2.350,00 à vista. 411: R$ 588,00 contra R$ 420,00. 713: R$ 880,00 contra R$ 734,00. O evento não mostra parcelamento. A regra da linha exige o total quando for diferente do à vista.
3. **Condições do produto escondidas ou contraditórias (E).** 573 com horários e formas de pagamento divergentes; 411 com prazo de acesso no fim e "Turma I" em curso contínuo; 713 com quatro descrições de período; evento com lista "inclui" ambígua. É o padrão mais forte: o visitante não consegue repetir o que está comprando.
4. **"Para quem" tarde ou ausente (E).** 573, 411 e 713 colocam o público no fim ou não colocam; o evento é a exceção.
5. **Falta prova de quem ensina (E).** Um docente sem bio (573 e 411), 20 nomes sem bio (713), docentes bem descritos mas sem autorização registrada e sem edição anterior (evento). Depoimentos e vídeos não aparecem em nenhuma.
6. **Política de turma, cancelamento e reembolso incompleta (E).** As pós têm aviso; os livres presenciais não. 713 diz "não reembolsável" sem contexto; o evento não diz nada.
7. **Entrada tardia e produto contínuo ou anual mal explicados (E).** 713 cobra valor integral com a maior parte das aulas já dadas; 411 não diz quando o prazo de acesso começa.
8. **Venda cruzada ausente (E).** Nenhuma página leva ao próximo degrau (online para presencial, grupo para pós, curso para pós). É a função de porta de entrada que o contexto da linha descreve.
9. **Sem frase de certificação ou de que curso livre não confere diploma (E).** Pendência P1. Em 713 há "Certificado" sem condição.
10. **Erros de texto e blocos vazios (E)** em todas, que enfraquecem a confiança de quem avalia um investimento [SUPOSIÇÃO].
11. **Template.** Faltam os tipos "grupo de estudos" e "curso online contínuo com regra de acesso". As seções que faltam em todas são faq (menos no evento), formulario, cta_final, depoimentos e certificacao.
12. **Ordem de preço e botão.** O evento é o caso extremo (preço só depois da programação), mas a mesma pergunta vale para 573: o botão aparece no topo; confirmar no celular se o preço fica visível sem rolagem. [CONFIRMAR no site]

### Ordem sugerida de trabalho (para o cmo e o backlog-de-otimizacao)

1. Decisões da Ufape que destravam a conversão: vagas e regra de adiamento do 573, formas de pagamento e e-mail corretos, produto para o entrante tardio no 713 e qual página fica (643 ou 713), pagamento e cancelamento do evento, regra do cupom, texto de certificado.
2. Mudanças de site de baixo custo: total do cartão em todas as páginas, botão do evento acima da programação, WhatsApp e formulário curto, correção de textos, remoção do link de login do 411, remoção de "A definir" no evento.
3. Texto da squad: hero, "Sobre", "Para quem", FAQ e blocos de acesso, na ordem das ondas: evento e 573 primeiro (campanhas ativas e data próxima), depois os contínuos.
4. Mapear eventos no GA4 e no CRM antes de qualquer teste. [CONFIRMAR ferramenta]

### Próximo agente sugerido

desenho-de-experimentos, para transformar as três correções de cada página em testes com amostra e duração, assim que houver dado de tráfego. Para o evento e para o 573, que acontecem em 25 e 19 dias, o desenho deve ser antes e depois, não A/B. Depois, backlog-de-otimizacao (etapa 1.33) e qa-de-marketing.

---

## Fatos (com fonte)

- 573: início 14/11/2026, 28 h, R$ 2.350,00 à vista ou 10x de R$ 303,00 no cartão, status aberto. Fonte: catálogo, seção 4, e ficha 573.
- 573: INVESTIMENTO cita "carta de crédito", boleto parcelado "6 x de 550 reais" a pedir por e-mail, e horários com duas versões de término no sábado (18h e 19h). Fonte: ficha 573.
- 573: 16 h de prática e 12 h de teoria gravada, disponível por 6 meses. Fonte: ficha 573.
- 573: a visão de campanhas mostra 29/11 e o catálogo 14/11. Fonte: plano do cmo, seção 3 (status da mídia) e P6.
- 411: 12 h, R$ 420,00 à vista ou 6x de R$ 98,00, acesso por 120 dias, "Turma I", link de login em LOCAL, um docente. Fonte: catálogo, seção 5, e ficha 411.
- 713: R$ 734,00 à vista ou 10x de R$ 88,00, ementa de 23 aulas (22 com data de 04/03/2026 a 23/12/2026 e uma "a definir"), 20 docentes, quatro deles marcados "(EUA)", desistência sem reembolso, gravações por 120 e 30 dias. Fonte: ficha 713 e catálogo, seção 7.
- 713: das 23 aulas, 17 tinham data até 14/10/2026 (anteriores a hoje). Conta feita sobre a ementa.
- 713: duplicidade com 643 (Anual 2025/2026). Fonte: catálogo, seção 7, e plano do cmo, P7.
- Evento: 20 e 21/11/2026, Av. Tiradentes, 960, 16 h (8 teóricas e 8 práticas), 30 vagas, R$ 1.250,00 presencial, R$ 450,00 transmitido e gravado, cupom SIMPNEUROMONIT com 20% para aluno e ex-aluno (confirmado pela Ufape em 26/10/2026), certificado conforme presença, docentes confirmados, quatro convidados "A definir". Fonte: ficha do evento e catálogo, seção 9.
- Evento: produto 68634 da loja mostra 24 h e está sem data. Fonte: ficha do evento e plano do cmo, P9.
- Faltam 19 dias para 14/11, 25 dias para 20/11. Conta a partir de 26/10/2026.
- 10 x 303 é igual a R$ 3.030,00; 6 x 550 é igual a R$ 3.300,00; 6 x 98 é igual a R$ 588,00; 10 x 88 é igual a R$ 880,00. Valores com 20% de desconto: R$ 1.000,00 e R$ 360,00. Contas.
- O template pagina-da-turma.md tem os tipos pos, livre, workshop e simposio, e seção obrigatória "formulario". Fonte: templates/pagina-da-turma.md.
- A frase de certificação ligada ao MEC não aparece nas quatro páginas analisadas. Fonte: fichas.

## Suposições

- [SUPOSIÇÃO] A maior parte dos candidatos chega pelo celular. Confirmar no GA4.
- [SUPOSIÇÃO] A primeira tela do celular mostra título, preço e botão, como a ordem do texto sugere, exceto no evento, onde preço e botão ficam depois da programação.
- [SUPOSIÇÃO] Visitante de curso presencial de ticket médio e alto conversa com o time antes de pagar; sem segundo caminho na página, parte sai.
- [SUPOSIÇÃO] O boleto parcelado por e-mail derruba a compra.
- [SUPOSIÇÃO] Em curso gravado de preço baixo, aula de amostra e texto de resultado aumentam a compra.
- [SUPOSIÇÃO] Total do cartão visível e regra de acesso clara reduzem desistência e reclamação.
- [SUPOSIÇÃO] Explicar o formato "grupo de estudo" amplia a conversão de quem nunca participou.
- [SUPOSIÇÃO] A venda cruzada entre os degraus (online, presencial, grupo e pós) aumenta a conversão. A decisão é da Ufape.
- [SUPOSIÇÃO] Mostrar o código do cupom e o valor final converte mais o público de aluno e ex-aluno.
- [SUPOSIÇÃO] Erros de digitação e "A definir" em página pública reduzem a confiança.
- [SUPOSIÇÃO] Os textos de hero e de "Sobre" propostos refletem a dor do clínico; validar com o WhatsApp de vendas anonimizado.

## Dados que faltam

- [CONFIRMAR] Tráfego, taxa de conversão por página, origem (celular e computador), eventos de GA4, gravações e mapas de calor, e dados do checkout (abandono, forma de pagamento).
- [CONFIRMAR] Se o site tem WhatsApp fixo, formulário de lead, depoimentos em imagem, vídeo, logos de parceiros e política de privacidade no checkout (o texto copiado não mostra).
- [CONFIRMAR NO CATÁLOGO] Vagas, turma mínima e regra de adiamento do 573; data certa (14/11 ou 29/11).
- [CONFIRMAR] Quais formas de pagamento valem no 573 (Pix, boleto parcelado, cartão), qual e-mail de secretaria vale e se o boleto parcelado sai direto no site.
- [CONFIRMAR] Horário final do sábado do 573 e dados de prática (alunos por equipamento e animais).
- [CONFIRMAR] Regras de acesso do 411 (início da contagem dos 120 dias) e se a "PRÁTICA DE ECOCARDIOGRAMA" é gravada.
- [CONFIRMAR] Período, frequência e nome corretos do 713; o que o entrante tardio recebe; qual página fica (643 ou 713); condição para o certificado; revisão jurídica da frase de não reembolso.
- [CONFIRMAR] Evento: parcelamento, cancelamento e reembolso, almoço, o que levar, fluxo e prazo de comprovação do vínculo de aluno e ex-aluno, validade e limite do cupom, medição de presença no ingresso online, vagas restantes.
- [CONFIRMAR] Texto de certificado de participação do evento e texto padrão de curso livre pela regulação.
- [CONFIRMAR autorização] Docentes, depoimentos, vídeo e imagem.
- [CONFIRMAR] Quem aprova páginas e preços, metas de conversão e verba.
