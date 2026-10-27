# Pesquisa de palavras-chave e perguntas de IA das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), encomenda F1 da onda 2

- **Agente:** pesquisa-de-palavras-chave
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** F1 do plano do CMO (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md, seção 10). O plano previa o nome pesquisa-de-palavras-chave-pos-2026-11-06.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Status:** rascunho para o qa-de-marketing (auditoria 03-busca e auditorias/conformidade-educacional.md). Nada é publicado, enviado ou pago. Nenhuma ação em site, anúncio ou CRM foi feita.
- **Consumidores deste arquivo:** mensagens (F2), landing-page (F3, campo `palavra_chave_principal` do template), seo-on-page (F4). Para os guias de decisão e artigos de apoio citados aqui, o próximo agente é lacunas-de-conteudo.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 10, 11, 14, 16, 18 e 20)
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md (inclusive "Padrão de nome")
  - contexto/catalogo-de-cursos.md (seção 2, linhas de 657, 341, 289, 68615 e 333; é a única fonte dos dados de curso citados aqui)
  - Fichas inteiras: contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md, 341-pos-graduacao-em-medicina-interna-equina.md, 289-pos-graduacao-em-cardiologia-veterinaria.md, 68615-pos-graduacao-em-patologia-clinica.md, 333-pos-graduacao-em-citopatologia-veterinaria.md
  - templates/pagina-da-turma.md (tipo pos: regras do texto da IA e ordem padrão)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (seções 1, 2, 4, 7, 8, 10 e 11)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (v3: seções 2, 3 e as áreas A1, A2, A11 e A14; reaproveitadas aqui com o ID de origem)
  - saidas/11-midia-paga/anuncios-google-pos-2026-10-26.md (v6: seções 1, 6, 7 e 8; sementes, negativas e textos da Busca paga das 5 turmas)
  - .claude/skills/visibilidade-em-ia/SKILL.md (roteiro de perguntas e pontuação)
- **Pesquisa na web:** 6 consultas com WebSearch em 27/10/2026 (fontes na seção 11). Nenhuma página foi aberta. Não tentei abrir faculdade.ufape.com.br: o texto das páginas está nas fichas.
- **Dados pessoais:** nenhum. Docentes não são nomeados neste arquivo.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape tem; [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz; [SUPOSIÇÃO] é hipótese ou escolha deste agente, sempre com o critério.

---

## 1. Resumo para quem decide

1. **Uma palavra-chave principal por turma, ligada a uma única página** (campo `palavra_chave_principal` do template), igual à semente principal da Busca paga da mesma turma, para que orgânico e pago contem a mesma história e cheguem à mesma página:

| Turma | `palavra_chave_principal` | Origem |
|---|---|---|
| 657 | pós-graduação em anestesiologia avançada veterinária | K1.3 da pesquisa de 26/10 |
| 341 | pós-graduação em medicina interna equina | A14 da pesquisa de 26/10 |
| 289 | pós-graduação em cardiologia veterinária | K2.2 da pesquisa de 26/10 (alvo realista de curto prazo: a cauda de Goiânia, K2.3) |
| 68615 | pós-graduação em patologia clínica veterinária | K11.2 da pesquisa de 26/10 |
| 333 | pós-graduação em citopatologia veterinária | K11.3 da pesquisa de 26/10 |

2. **68615 e 333 não competem se cada uma ficar com o seu vocabulário** (seção 4): 68615 é laboratório clínico (patologia clínica, análises clínicas, rotina e gestão do laboratório); 333 é leitura de lâminas (citopatologia, citologia, citodiagnóstico). Termo que mistura os dois ("citologia" com "patologia clínica") vai para a página cujo nome o candidato digitou primeiro; termo que nenhuma das duas cobre (histopatologia, anatomia patológica, necropsia) não é alvo de nenhuma.
3. **O que a busca na web mostrou:** nos 5 nichos, os resultados são agregadores (Quero Bolsa, Guia da Carreira), blogs de faculdades, editais de concorrentes e matrizes de terceiros. Nenhuma página da Ufape apareceu. Não surgiu pós brasileira com os nomes "anestesiologia avançada" nem "medicina interna equina"; surgiram pós de patologia clínica e de cardiologia (concorrentes) e oferta de citopatologia em agregadores. O WebSearch não é a página de resultados do Google: ausência é indício, não prova.
4. **Duas travas do template pesam nas palavras-chave:** o texto da IA não pode ter local, número, data nem nome de docente. Termos de cidade (Goiânia em 289, São Paulo nas demais) só chegam à página pelos blocos de dado e pelo JSON-LD, a menos que a Ufape autorize a cidade em `titulo_seo` e `resposta_citavel` (CP1, seção 12).
5. **Três turmas têm pergunta bloqueada por resposta da Ufape:** 657 (quem pode entrar, U10), 341 (onde é a prática e o formato do módulo 3, OU11, e a promoção, OU10) e 333 (como se repõe o módulo 1 presencial, OU3). As perguntas marcadas "bloqueada" não viram FAQ nem texto até a resposta.
6. **Nenhum volume de busca foi inventado.** Volume é qualitativo (Alto, Médio, Baixo) e [SUPOSIÇÃO], pelo critério da seção 2.2.

---

## 2. Método, escalas e limites

### 2.1 O que foi feito

1. Reaproveitei da pesquisa de 26/10 (v3) os termos e as perguntas de A1 (657), A2 (289), A11 (68615 e 333) e A14 (341), com o ID de origem na coluna "Origem". O que é novo está marcado "nova".
2. Li as 5 fichas e extraí os termos que a própria página usa (módulos, objetivos, público-alvo) para as secundárias e as entidades.
3. Cruzei com as sementes e as negativas da Busca paga (anuncios-google-pos v6, seções 6 e 7) para não haver conflito entre orgânico e pago (seção 3).
4. Fiz 6 consultas na web (uma por turma e uma de apoio sobre citologia) e anotei só o que o resumo da busca mostrou.
5. Escrevi as perguntas como o candidato digita a um assistente (ChatGPT, Gemini, Perplexity, Claude), nos estágios problema, solução, comparação e decisão do roteiro da skill visibilidade-em-ia. Cada turma tem 8: 5 específicas e 3 comuns (preço e parcelas, entrada depois do início, turma que não fecha).

### 2.2 Pontuação

Mesma escala da pesquisa de 26/10 (skill visibilidade-em-ia, sem o componente "lacuna em IA", que só existe com checagem real em assistentes): pontuação = M + D + F, de 0 a 80, mostrada como "total (M/D/F)".

- M, intenção de matrícula: matricular de 26 a 30; resolver de 20 a 26; comparar de 14 a 20; aprender de 4 a 10.
- D, demanda: sem exportação de ferramenta, qualitativa: Alto = 20, Médio = 14, Baixo = 8. [SUPOSIÇÃO: critério é quantidade de ofertas em agregadores e tipo do termo; nenhum volume numérico existe neste arquivo.]
- F, facilidade: chance real de a Ufape vencer. Cabeça de termo contra agregadores de 6 a 12; termo intermediário de 14 a 18; cauda com página própria e pouca concorrência visível de 18 a 24.
- Corte: abaixo de 32 não vira alvo; fica como apoio. [SUPOSIÇÃO: regra prática da skill, não meta.]
- Nota nova (marcada "nova") é [SUPOSIÇÃO] do agente pelo mesmo critério. Nota reaproveitada mantém o valor da pesquisa de 26/10.
- Tipo: toda linha de "Palavras-chave" é busca; toda linha de "Perguntas para IA" é IA.
- A coluna "Ufape aparece em assistentes" fica "conferir manualmente" em todas as perguntas. Roteiro: a pessoa roda cada pergunta de 3 a 5 vezes por assistente e registra a taxa ("citada 2 de 5"). Sem checagem, não há nota de visibilidade.

### 2.3 Tipos de página usados na coluna "Atende"

- **Página da turma (tipo pos, template pagina-da-turma.md):** a página de dinheiro. A coluna diz o bloco que responde: `hero`, `sobre`, `para_quem`, `matriz` (dado), `local_e_datas` (dado), `investimento` (dado e frase de apoio), `faq`, `resposta_citavel` e `entidades` (campos de SEO).
- **Guia de decisão:** página de apoio de comparação (guias de A1, A2, A11 e 341 do iscas-digitais-pos). Liga para a página da turma.
- **Artigo de apoio:** conteúdo de intenção "aprender", em página separada da de matrícula (encomenda para lacunas-de-conteudo e briefing-de-conteudo).
- **Sem página:** termo que a Ufape não deve mirar (regulação, bolsa, concorrente, EAD).

### 2.4 Limites

- O WebSearch não devolve o preenchimento automático do Google nem "As pessoas também perguntam". As variações vêm das fichas, dos títulos dos resultados, do roteiro e da persona; a formulação exata é [SUPOSIÇÃO]. Antes de investir em anúncio novo, conferir as sugestões do Google e o Search Console.
- Nenhum assistente de IA foi consultado. Nenhuma taxa de citação foi inventada.
- Dados de curso (nome, modalidade, local, carga horária, turma, início) vêm só do catálogo, seção 2. O que só existe na ficha leva [CONFIRMAR NO CATÁLOGO].
- Nenhum termo de certificação, título de especialista, bolsa ou nota de órgão regulador é alvo. Nenhuma pergunta promete esses itens.
- Nome do curso em texto visível: "Pós-graduação em <área>" (contexto da linha). "Pós em", "pós vet" e abreviações aparecem só em listas de palavras-chave e em grupos de anúncio, nunca em título, H1 ou FAQ. O catálogo escreve "Pós Graduação" em 333 e 341; as peças usam a forma padrão.
- Nome do curso na página x palavra digitada: o catálogo chama 68615 de "Pós-graduação em Patologia Clínica" e 289 de "Pós-graduação em Cardiologia Veterinária". Quem busca digita "veterinária"; por isso as principais levam "veterinária" e a página precisa trazer "veterinária" no corpo (`sobre`, `resposta_citavel`, `entidades`), sem trocar o nome do catálogo.

---

## 3. Como orgânico e pago não entram em conflito

Fonte: anuncios-google-pos v6 (seções 6 e 7). A palavra principal orgânica de cada turma é a mesma semente `__area` da Busca paga: as duas levam à mesma página, então não há disputa de destino. O que pode gerar conflito é o orgânico mirar, na página da turma, termos que o pago nega de propósito ou que são de outra página.

| Turma | Sementes pagas (`__area`, resumo) | Negativas pagas próprias | Regra para o orgânico |
|---|---|---|---|
| 657 | pós-graduação em anestesiologia avançada veterinária; pós em anestesiologia avançada; anestesia avançada em cães e gatos pós | locorregional; goiânia; goiás; exatas: [pós-graduação em anestesiologia veterinária], [pós em anestesiologia veterinária], [anestesiologia veterinária] | O termo genérico "pós-graduação em anestesiologia veterinária" é da página de 68609 (Goiânia, pilar de Anestesiologia), não de 657. Locorregional é de 359. |
| 341 | pós-graduação em medicina interna equina; pós em medicina equina; especialização em clínica de equinos | pequenos animais; cães; gatos; goiânia; goiás | Nenhum termo de pequenos animais na página. |
| 289 | pós-graduação em cardiologia veterinária; pós em cardiologia veterinária em goiânia; especialização em cardiologia de cães e gatos | ecocardiografia; pneumologia; são paulo | Ecocardiografia é da página de 698 (onda 1); pneumologia é de 68636. A página de 289 pode citar ecocardiograma só como conteúdo dos módulos, sem tomar a palavra. |
| 68615 | pós-graduação em patologia clínica veterinária; pós em patologia clínica veterinária são paulo; especialização em patologia clínica de cães e gatos | citopatologia; hematologia; goiânia; goiás | Citopatologia é de 333; hematologia e hemograma são de 68608 (onda 1). |
| 333 | pós-graduação em citopatologia veterinária; pós em citologia veterinária; especialização em citopatologia de cães e gatos | patologia clínica; hematologia; goiânia; goiás | Patologia clínica é de 68615; hematologia é de 68608. |

**Negativas gerais da Busca paga (valem para as 5):** grátis, pdf, concurso, emprego, salário, residência, mestrado, doutorado, curso livre, ead, "100% online", universidade federal, pernambuco, agreste, garanhuns, prova de bolsa, bolsa, título de especialista, "reconhecida pelo mec", anclivepa. Consequência para o orgânico, igual à pesquisa de 26/10: os termos de EAD, residência, título e concorrente não são alvo da página da turma. Quando a dúvida do candidato é essa, a resposta mora num guia de decisão ou artigo de apoio, nunca na página de dinheiro. Bolsa e prova de bolsa estão fora desta onda (decisão 14): pergunta sobre bolsa vai para a secretaria e não vira FAQ.

**Sugestões ao gestor-de-midia, sem editar o arquivo dele** (são [SUPOSIÇÃO]; a decisão é do gestor e do qa):
1. Em 333 e em 68615, avaliar negativas de histopatologia, anatomopatologia e necropsia, que nenhuma das duas turmas cobre e que o candidato pode digitar junto de "patologia" ou "citologia". A lista atual não tem esses termos.
2. Em 289, avaliar "ecocardiograma" como negativa exata se o relatório de termos de busca mostrar gasto nele (a negativa atual é só "ecocardiografia").

---

## 4. Quem fica com cada termo: 68615 (laboratório clínico) x 333 (leitura de lâminas)

As duas turmas começam com uma semana de diferença, têm o mesmo campus e disputam o mesmo segmento (A11). A ficha de 68615 tem 3 módulos de citologia dentro de um curso maior de laboratório; a ficha de 333 é inteira de citologia, com módulos presenciais de leitura de lâminas e discussão de casos. A regra é pelo vocabulário que o candidato digita.

| Termo ou tema | Página | Motivo |
|---|---|---|
| patologia clínica veterinária; pós em patologia clínica; análises clínicas veterinárias; laboratório clínico veterinário | 68615 | Nome do curso e objetivo da ficha ("trabalhar em laboratórios clínicos"). |
| bioquímica clínica, urinálise, hemostasia, coproparasitologia, controle de qualidade e biossegurança do laboratório | 68615 (matriz e apoio) | Módulos da ficha de 68615 que não existem em 333. |
| montar e administrar laboratório veterinário | 68615 | Objetivo da ficha ("estruturar e administrar um laboratório"). 333 tem só "gestão da qualidade aplicada à citopatologia", que não é alvo. |
| citopatologia veterinária; citologia veterinária; citodiagnóstico; leitura de lâminas; leitura de lâminas de citopatologia | 333 | Nome do curso e módulos presenciais de leitura de lâminas. |
| citologia de linfonodos, derrames cavitários, neoplasias de células redondas, linfoma (consulta clínica de rotina) | 333 como apoio (artigos) | Módulos da ficha de 333. A ficha de 68615 tem "Citologia I a III", mas a palavra não é alvo dela. |
| "patologia clínica" junto de "citologia" na mesma consulta | 68615 | O candidato nomeou primeiro o curso de laboratório. A página de 68615 liga para 333 no FAQ de comparação. |
| "citopatologia" ou "citologia" sozinhas | 333 | Idem, o inverso. A página de 333 liga para 68615. |
| mielograma | nenhuma das duas | Está na ficha das duas e é tema de hematologia. Sem alvo próprio para não canibalizar; apoio em artigo ligado a 68608 (onda 1). |
| hemograma, hematologia | 68608 (onda 1), não 68615 nem 333 | A paga já nega "hematologia" nas duas. |
| histopatologia, anatomia patológica, necropsia, patologia veterinária (geral) | nenhuma | O público de citologia e de laboratório clínico é outro. Não prometer nem ranquear; ver sugestão 1 da seção 3. |
| diferença entre as duas turmas | Guia de decisão A11 (iscas-digitais v2) e FAQ das duas páginas | Pergunta de comparação nas duas listas de perguntas (seções 8 e 9), com resposta escrita pela mensagem F2 (sem comparar valor). |

Regra de link interno: 68615 liga para 333 pela âncora "Pós-graduação em Citopatologia Veterinária" e 333 liga para 68615 pela âncora "Pós-graduação em Patologia Clínica". Nenhuma das duas usa a âncora principal da outra como termo de si mesma.

---

## 5. Seção 657: Pós-graduação em Anestesiologia Avançada (turma II)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 360 h, início 13/03/2027, turma II, status aberto. **Ficha:** público-alvo "exclusiva para médicos veterinários anestesistas já atuantes" [CONFIRMAR U10]; 6 módulos presenciais; temas: anestesia total intravenosa, locorregional, hemodinâmica avançada, ventilação mecânica aplicada à anestesia, dor em felinos, bloqueio neuromuscular, coagulação, reanimação, anestesia neurológica e cardiotorácica, pets não convencionais.

**O que a busca na web mostrou (27/10):** nenhuma pós brasileira com o nome "anestesiologia avançada" apareceu. Surgiram o projeto pedagógico de uma pós brasileira de Anestesiologia Veterinária de 2026 (UNAR), a página de pós de Anestesiologia do Quero Bolsa (a maior parte das ofertas indisponível na consulta) e cursos internacionais de anestesia avançada para enfermeiros veterinários, que são outra intenção. Sinal de espaço aberto para o termo "avançada" [SUPOSIÇÃO].

**Palavra principal:** pós-graduação em anestesiologia avançada veterinária. **Página:** a página da turma 657. **Tipo de página:** página da turma (tipo pos).

### 5.1 Palavras-chave

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 657-K0 | pós-graduação em anestesiologia avançada veterinária | matricular | Baixo | 58 (28/8/22) | K1.3 | Página da turma 657 (`hero`, `sobre`, `resposta_citavel`) | Principal. |
| 657-K1 | pós em anestesiologia avançada | matricular | Baixo | 52 (26/8/18) | sec. A1 | Página da turma 657 | Nome popular: só lista de palavras e grupo de anúncio, nunca texto visível. |
| 657-K2 | anestesia avançada em cães e gatos pós | matricular | Baixo | 52 (26/8/18) | sec. A1 | Página da turma 657 | A ficha não diz que o foco é cães e gatos (cita felinos e pets não convencionais); usar só em anúncio e lista [CONFIRMAR NO CATÁLOGO]. |
| 657-K3 | pós-graduação em anestesiologia avançada semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 657 (`faq`, `sobre`) | A modalidade vem do dado; no texto a IA pode dizer "semipresencial". |
| 657-K4 | pós-graduação em anestesiologia avançada São Paulo | matricular | Baixo | 54 (28/8/18) | nova | Página da turma 657 (blocos de dado e JSON-LD) | O texto da IA não cita local (template): ver CP1. |
| 657-K5 | quanto custa pós em anestesiologia avançada | resolver | Baixo | 50 (22/8/20) | nova (de K1.6 e Q1.7) | Página da turma 657 (`investimento`, dado) | O valor vem do banco; a IA escreve só a frase de apoio, sem número. |
| 657-K6 | anestesia de precisão veterinária | aprender | Baixo | 38 (8/8/22) | nova (termo da ficha) | Página da turma 657 (`sobre`, `entidades`) | A ficha usa "anestesia de precisão" como conceito; serve a entidades e citação, não a anúncio. |
| 657-K7 | hemodinâmica avançada em anestesia veterinária | aprender | Baixo | 36 (8/8/20) | nova (módulos 3 e 8) | Página da turma 657 (`matriz`) e artigo de apoio [REVISÃO DOCENTE] | Apoio. |
| 657-K8 | pós para anestesista veterinário já atuante | comparar | Baixo | 44 (16/8/20) | nova | Página da turma 657 (`para_quem`) | **Bloqueada até U10**: não escrever quem pode entrar. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| pós-graduação em anestesiologia veterinária (genérico); pós em anestesiologia veterinária em Goiânia | página de 68609 (Goiânia, pilar de Anestesiologia) | A Busca paga de 657 nega o termo exato; é da outra turma. |
| anestesiologia locorregional; bloqueios guiados por ultrassom | página de 359 | A paga de 657 nega "locorregional". |
| ventilação mecânica aplicada à anestesia (curso) | linha Livres (68618) e página de 352 | Não misturar linhas; a ficha de 657 tem o módulo, mas o termo não é alvo. |
| anestesia em pets não convencionais; reanimação cardiorrespiratória | linha Livres e apoio | Idem. |
| pós em anestesiologia EAD; residência em anestesiologia; título ou prova de especialista em anestesiologia | sem página (ou guia A1) | A ficha de 657 traz um convite para "a prova de Especialista em Anestesiologia": é tema de título, bloqueado (T6). Não entra na página. |
| prova de bolsa de anestesiologia | sem página nesta onda | Decisão 14. |

### 5.2 Perguntas que o candidato faz a assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 657-Q1 | Existe pós em anestesiologia avançada para veterinário que já é anestesista? Para quem é e como funciona? | Solução | matricular | 56 (28/8/20) | nova (de Q1.1) | Página da turma 657: `resposta_citavel` e `para_quem` | Resposta de 40 a 60 palavras sem número, local nem data. A parte "para quem" depende de U10. |
| 657-Q2 | Qual a diferença entre pós em anestesiologia veterinária e pós em anestesiologia avançada? | Comparação | comparar | 46 (16/8/22) | Q1.5 | Guia de decisão A1; `faq` da página de 657 liga ao guia | Tabela de comparação no guia; sem dizer qual é melhor. |
| 657-Q3 | Preciso ser anestesista e já atuar na área para fazer uma pós em anestesiologia avançada? | Decisão | resolver | 50 (24/8/18) | Q1.4 | `para_quem` e `faq` de 657 | **Bloqueada até U10.** Até lá, resposta do time: "vou confirmar com a secretaria". |
| 657-Q4 | O que se estuda numa pós em anestesiologia avançada: hemodinâmica, ventilação mecânica, TIVA? | Problema | aprender | 38 (8/8/22) | nova | `sobre` e `matriz` (dado) de 657 | Os módulos vêm da ficha, nunca da IA; o texto cita os temas sem número. |
| 657-Q5 | Como funciona a pós semipresencial em anestesiologia avançada? Tenho que ir a São Paulo todo mês? | Problema | resolver | 46 (22/8/16) | nova (de QT2) | `faq` e `local_e_datas` (dado) de 657 | Teoria online e módulos presenciais pela ficha. Reposição de módulo perdido [CONFIRMAR OU3]. |
| 657-QC1 | Quanto custa a pós em anestesiologia avançada da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | Q1.7 | `investimento` (dado) | Número só do dado. Sem preço em peça de mídia até U11. |
| 657-QC2 | Dá para entrar na pós em anestesiologia avançada depois que a turma já começou? | Decisão | resolver | 54 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18: matrícula até o 3º módulo, com explicação dos módulos já dados [CONFIRMAR OU3]. Sem "corra" nem contador. |
| 657-QC3 | E se a turma da pós em anestesiologia avançada não fechar, o que acontece com a viagem e o dinheiro? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` de 657 | Turma mínima sem número até a página trazer 15; passagem e hotel só depois da turma confirmada (ficha). |

**Observações de 657:** (1) sem U10 nenhuma peça diz quem pode entrar; a palavra "exclusiva" da ficha não vai para título nem descrição. (2) A pergunta 657-Q2 é o ponto de entrada de quem digita o termo genérico: o guia A1 serve de ponte para a página de 657 sem tomar o termo de 68609.

---

## 6. Seção 341: Pós-graduação em Medicina Interna Equina (turma I)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, início 20/03/2027, turma I, status aberto. **Ficha:** público-alvo "Médico Veterinários"; 24 módulos; temas: abordagem clínica do paciente equino, paciente crítico, preparação cirúrgica, cardiologia, respiratório, digestivo, locomotor, neonatologia, UTI neonatal, potros críticos, podologia, odontologia equina, medicina baseada em evidências; segundo local na ficha (Indaiatuba) e módulo 3 marcado "ONLINE PRESENCIAL" [CONFIRMAR OU11]; promoção de 20% com texto cortado [CONFIRMAR OU10].

**O que a busca na web mostrou (27/10):** nenhum programa brasileiro de medicina interna equina apareceu; surgiram residências e colégios europeus (ECEIM), uma especialização em medicina esportiva equina da Argentina, módulo de pós da África do Sul e a Pós-Graduação em Clínica de Equinos de Portugal (Universidade Lusófona). Para o Brasil, a busca trouxe só especializações em diagnóstico e cirurgia ou ortopedia equina. Sinal de espaço aberto para "medicina interna equina" [SUPOSIÇÃO]. Atenção: o termo "pós-graduação em clínica de equinos" é ocupado por oferta de Portugal (outro país); por isso a principal fica com "medicina interna equina", que é o nome da turma.

**Palavra principal:** pós-graduação em medicina interna equina. **Página:** a página da turma 341. **Tipo de página:** página da turma (tipo pos), com guia de decisão de 341 (iscas-digitais v2) de apoio.

### 6.1 Palavras-chave

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 341-K0 | pós-graduação em medicina interna equina | matricular | Baixo | 56 (28/8/20) | A14 | Página da turma 341 (`hero`, `sobre`, `resposta_citavel`) | Principal. |
| 341-K1 | pós em medicina equina | matricular | Baixo | 52 (26/8/18) | sec. A14 | Página da turma 341 | Nome curto: lista e grupo de anúncio. |
| 341-K2 | especialização em clínica de equinos | matricular | Baixo | 52 (26/8/18) | sec. A14 | Página da turma 341 (`sobre`) | Grafia disputada por oferta de Portugal; usar também "médico veterinário de equinos" no corpo [SUPOSIÇÃO]. |
| 341-K3 | pós em medicina interna equina São Paulo | matricular | Baixo | 56 (28/8/20) | sec. A14 | Página da turma 341 (dado e JSON-LD) | Local fora do texto da IA (CP1). |
| 341-K4 | pós-graduação em medicina interna equina semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 341 (`faq`) | A ficha diz que a teoria é online e a prática presencial aos fins de semana; o módulo 3 está em aberto (OU11). |
| 341-K5 | pós em cavalos veterinária; pós em equinos vet | matricular | Baixo | 48 (24/8/16) | sec. A14 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 341-K6 | quanto custa pós em medicina interna equina | resolver | Baixo | 46 (22/8/16) | nova | Página da turma 341 (`investimento`, dado) | **Sem promoção** em qualquer texto até OU10. |
| 341-K7 | neonatologia e UTI de potros: especialização | aprender | Baixo | 34 (6/8/20) | nova (módulos da ficha) | Artigo de apoio [REVISÃO DOCENTE] e `matriz` | Conteúdo de autoridade; no limite do corte. |
| 341-K8 | como se especializar em medicina equina | aprender | Baixo | 32 (6/8/18) | nova | Artigo de apoio (guia de 341) | [REVISÃO REGULAÇÃO] no trecho de título; no limite do corte. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| qualquer termo de pequenos animais, cães e gatos | outras turmas | A paga de 341 nega "pequenos animais", "cães" e "gatos". |
| pós em ortopedia ou cirurgia equina | sem página | Não há turma de ortopedia equina no catálogo. |
| medicina esportiva equina; "aptidão esportiva" | sem alvo | A ficha tem um tema do módulo 8 sobre aptidão esportiva, mas não é o foco do curso. |
| residência ou título de especialista em medicina interna equina (colégio europeu) | sem página | Bloqueado (T6); residências não são pós lato sensu. |
| promoção, desconto, bolsas | sem página | A ficha de 341 tem a promoção com texto cortado e cita "bolsas de estudo" no texto; decisão 14 e OU10. |

### 6.2 Perguntas que o candidato faz a assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 341-Q1 | Existe pós em medicina interna equina no Brasil? Qual é e onde fazer? | Solução | matricular | 56 (28/8/20) | nova (de A14) | `resposta_citavel` e `sobre` de 341 | Resposta sem número, local nem data. A busca não trouxe oferta brasileira concorrente. |
| 341-Q2 | Quem pode fazer a pós em medicina interna equina? Preciso já trabalhar com cavalos? | Problema | resolver | 46 (22/8/16) | nova | `para_quem` de 341 | A ficha diz só "Médico Veterinários"; experiência prévia não está escrita [CONFIRMAR NO CATÁLOGO]. |
| 341-Q3 | Onde são as aulas práticas com cavalos na pós em medicina interna equina de São Paulo? | Decisão | resolver | 46 (24/8/14) | Q14.2 | `local_e_datas` (dado) e `faq` | **Bloqueada até OU11** (segundo local da ficha e formato do módulo 3). Resposta do time: "vou confirmar com a secretaria". |
| 341-Q4 | Medicina interna equina, clínica de equinos ou ortopedia equina: qual pós escolher? | Comparação | comparar | 44 (16/8/20) | nova | Guia de decisão de 341 | Sem comparar valor nem citar concorrente. |
| 341-Q5 | O que se estuda numa pós em medicina interna equina? Tem sistema digestivo, neonatologia e potros críticos? | Problema | aprender | 38 (8/8/22) | nova | `sobre` e `matriz` (dado) | Os módulos da ficha, em ordem do dado. |
| 341-QC1 | Quanto custa a pós em medicina interna equina e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Sem promoção; número só do dado. |
| 341-QC2 | Dá para entrar na pós em medicina interna equina depois que a turma já começou? | Decisão | resolver | 54 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18; módulo 3 em aberto (OU11) pode mudar a frase. |
| 341-QC3 | E se a turma da pós em medicina interna equina não fechar, o que acontece com a viagem e o dinheiro? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Persona de equinos viaja mais [SUPOSIÇÃO]; passagem e hotel só depois da turma confirmada. |

**Observações de 341:** o alcance do @ufapevet no público de equinos é menor [SUPOSIÇÃO do plano do CMO]; por isso a busca (paga e orgânica) e o WhatsApp carregam mais peso nesta turma. O termo "medicina interna equina" tem pouca concorrência visível, mas também pouco volume provável: tratar como nicho de cauda.

---

## 7. Seção 289: Pós-graduação em Cardiologia Veterinária, Goiânia (turma II)

**Dados de apoio (catálogo, seção 2):** Goiânia, semipresencial, 500 h, início 20/03/2027, turma II, status aberto. **Ficha:** público-alvo "Médicos Veterinários"; 24 módulos, 6 presenciais, 4 deles de prática de ecocardiograma (módulos 9, 13, 16 e 19), o 24 de aula prática e prova final e o 6 sem conteúdo no cronograma; temas: anatomia e fisiologia, semiologia circulatória, radiografia, ECG, taquiarritmias e bradiarritmias, ecocardiografia, cardiopatias de cães, de felinos e congênitas, emergências cardíacas; a ficha traz o bloco "PROVA DE BOLSA" (sem peça, decisão 14).

**O que a busca na web mostrou (27/10):** o Anclivepa-SP publicou o edital da Pós-graduação em Cardiologia Veterinária de 2026; o Pravaler tem guia sobre a especialidade; o Guia da Carreira lista pós em medicina veterinária em Goiânia quase só em EAD, sem cardiologia semipresencial. Nenhuma pós de cardiologia semipresencial em Goiânia apareceu: sinal de espaço aberto para a cauda local [SUPOSIÇÃO]. A cabeça de termo ("pós-graduação em cardiologia veterinária") é disputada por agregadores e concorrentes (F baixo).

**Palavra principal:** pós-graduação em cardiologia veterinária. **Alvo realista de curto prazo:** pós em cardiologia veterinária em Goiânia (289-K1). **Página:** a página da turma 289 (única turma aberta de Cardiologia; 68605, em São Paulo, está em "verificar" e não recebe alvo; quando reabrir, decidir canonical ou 301 pela regra T3). **Tipo de página:** página da turma (tipo pos), com guia de decisão A2 de apoio.

### 7.1 Palavras-chave

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 289-K0 | pós-graduação em cardiologia veterinária | matricular | Alto | 58 (28/20/10) | K2.2 | Página da turma 289 (`hero`, `sobre`, `resposta_citavel`) | Principal; cabeça de termo. |
| 289-K1 | pós em cardiologia veterinária em Goiânia | matricular | Baixo | 60 (30/8/22) | K2.3 | Página da turma 289 (dado e JSON-LD) | Melhor aposta da turma. Local fora do texto da IA (CP1). |
| 289-K2 | pós-graduação em cardiologia veterinária Goiânia | matricular | Baixo | 60 (30/8/22) | K2.3 (exata derivada) | Página da turma 289 | Mesma página de 289-K1. |
| 289-K3 | especialização em cardiologia de cães e gatos | matricular | Baixo | 54 (26/8/20) | sec. A2 | Página da turma 289 (`sobre`) | A ficha cita cardiopatias de cães e de felinos. |
| 289-K4 | pós-graduação em cardiologia veterinária semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 289 (`faq`) | A ficha: aulas teóricas à distância, só os módulos práticos são presenciais. |
| 289-K5 | pós em cardio vet; especialização em cardio vet | matricular | Baixo | 52 (26/8/18) | K2.7 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 289-K6 | quanto custa pós em cardiologia veterinária | resolver | Médio | 52 (22/14/16) | K2.8 | Página da turma 289 (`investimento`, dado) | Número só do dado. |
| 289-K7 | pós em cardiologia veterinária quanto tempo dura | resolver | Baixo | 48 (22/8/18) | nova | Página da turma 289 (`numeros`, dado) | A duração vem do dado; a IA não escreve número. |
| 289-K8 | eletrocardiograma e arritmias em cães e gatos: especialização | aprender | Baixo | 34 (6/8/20) | nova (módulos 4, 5 e 7) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Apoio. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| pós em ecocardiografia (veterinária) | página de 698 (onda 1) | A paga de 289 nega "ecocardiografia". A página de 289 cita o hands-on de ecocardiograma como conteúdo, sem tomar a palavra, e liga para 698 no guia A2. |
| pneumologia; ventilação mecânica | páginas de 68636 e 352 | A paga nega "pneumologia". |
| pós em cardiologia veterinária São Paulo | sem alvo nesta página | A paga nega "são paulo"; 68605 está em "verificar". |
| prova de bolsa de cardiologia | sem página nesta onda | Decisão 14; o bloco "PROVA DE BOLSA" da ficha é corrigido no OB1. |
| pós em cardiologia veterinária Anclivepa; edital de concorrente | sem página | Termo de marca do concorrente; atender a dúvida no guia por critérios, sem nomear. |
| pós em cardiologia veterinária EAD; título de especialista em cardiologia veterinária | sem página (ou guia A2) | Pago nega EAD; título é T6 (bloqueado). |

### 7.2 Perguntas que o candidato faz a assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 289-Q1 | Tem pós em cardiologia veterinária em Goiânia? Como são as aulas? | Solução | matricular | 54 (30/8/16) | Q2.4 | `resposta_citavel` e `faq` de 289; `local_e_datas` (dado) | O texto da IA não cita Goiânia (CP1); o local aparece no dado e no JSON-LD. Resposta de 40 a 60 palavras. |
| 289-Q2 | Moro fora de Goiás: a pós semipresencial em cardiologia veterinária exige ir a Goiânia todo mês? | Problema | resolver | 48 (22/8/18) | nova (persona secundária) | `faq` de 289 | Pela ficha, só os módulos práticos são presenciais; frequência exata e hospedagem [CONFIRMAR NO CATÁLOGO]. |
| 289-Q3 | Qual a diferença entre pós em cardiologia veterinária e pós em ecocardiografia veterinária? | Comparação | comparar | 46 (16/8/22) | Q2.3 | Guia de decisão A2; `faq` de 289 liga a 698 | Sem dizer qual é melhor. |
| 289-Q4 | A pós em cardiologia veterinária tem ecocardiograma na prática, com hands-on? | Decisão | resolver | 50 (24/8/18) | nova | `matriz` (dado) e `faq` | A ficha lista módulos práticos de ecocardiograma. A pergunta cita "ecocardiograma" como conteúdo, sem tomar a palavra de 698. |
| 289-Q5 | Pós em cardiologia veterinária serve para clínico geral que não é cardiologista? | Problema | comparar | 44 (14/8/22) | nova (modelo Q11.1) | `para_quem` | A ficha diz só "Médicos Veterinários"; nível de entrada [CONFIRMAR NO CATÁLOGO]. |
| 289-QC1 | Quanto custa a pós em cardiologia veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 289-QC2 | Dá para entrar na pós em cardiologia veterinária depois que a turma já começou? | Decisão | resolver | 54 (26/8/22) | nova | `faq` (dado da turma, OU14) | Decisão 18 e OU3. |
| 289-QC3 | E se a turma da pós em cardiologia veterinária de Goiânia não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número até a página trazer 15. |

**Observações de 289:** (1) CP1 pesa mais aqui: a diferença da turma é o campus. Sem autorização da cidade em `titulo_seo` e `resposta_citavel`, o termo "Goiânia" depende do dado e do JSON-LD. (2) Atendimento de vendas de Goiânia tem telefone próprio (contexto geral); não é palavra-chave. (3) A campanha paga atual de 289 está ativa (PP9); este arquivo não altera nada nela.

---

## 8. Seção 68615: Pós-graduação em Patologia Clínica (turma VII), laboratório clínico

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, início 20/03/2027, turma VII, status aberto. **Ficha:** público-alvo "Médicos Veterinários"; 24 módulos; objetivo "capacitar o médico veterinário a trabalhar em laboratórios clínicos", correlação clínico-laboratorial, "estruturar e administrar um laboratório", equipamentos, técnicas de coleta; temas: pré-analítico, hematologia (módulos iniciais), hemostasia, hemoparasitoses, mielograma, hemocomponentes, bioquímica e urinálise, eletrólitos e hemogasometria, felinos, dermatologia, endócrino, coproparasitologia, Citologia I a III, líquidos cavitários, imunológicos e PCR, microbiologia, controle de qualidade e biossegurança. A ficha traz frases ligadas ao MEC e a "referência nacional" que não entram em nenhuma peça (OB1).

**O que a busca na web mostrou (27/10):** o Guia da Carreira lista pós em patologia clínica veterinária, com grande presença de EAD; o Pravaler descreve o conteúdo típico (hematologia, bioquímica clínica e citopatologia); uma vaga de patologista clínico veterinário em Valinhos (SP) cita a pós como requisito (sinal fraco de procura, sem promessa de emprego); a UNIFAA tem matriz de pós em Patologia Clínica Veterinária (2022) com módulo de citopatologia e mielograma, o que mostra que concorrentes de patologia clínica também incluem citologia. Nenhuma página da Ufape apareceu.

**Palavra principal:** pós-graduação em patologia clínica veterinária. **Página:** a página da turma 68615. **Tipo de página:** página da turma (tipo pos), com guia de decisão A11 de apoio.

### 8.1 Palavras-chave

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68615-K0 | pós-graduação em patologia clínica veterinária | matricular | Alto | 60 (28/20/12) | K11.2 | Página da turma 68615 (`hero`, `sobre`, `resposta_citavel`) | Principal. "Veterinária" vai no corpo; o nome do catálogo não a traz. |
| 68615-K1 | especialização em patologia clínica de cães e gatos | matricular | Baixo | 52 (26/8/18) | sec. A11 | Página da turma 68615 (`sobre`) | |
| 68615-K2 | pós em patologia clínica veterinária São Paulo | matricular | Baixo | 54 (28/8/18) | sec. A11 | Página da turma 68615 (dado e JSON-LD) | Local fora do texto da IA (CP1). |
| 68615-K3 | pós em análises clínicas veterinárias | matricular | Médio | 50 (24/14/12) | K11.4 | Página da turma 68615 (`sobre`, `faq`) | [SUPOSIÇÃO] de que atrai o mesmo público; o termo aparece em EAD de faculdades. |
| 68615-K4 | pós em laboratório clínico veterinário | matricular | Baixo | 50 (24/8/18) | nova (termo da ficha) | Página da turma 68615 (`sobre`, `entidades`) | A ficha usa "laboratórios clínicos" e "laboratório clínico veterinário" (módulo 24). |
| 68615-K5 | pós-graduação em patologia clínica veterinária semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 68615 (`faq`) | Os agregadores mostram a área sobretudo em EAD: espaço para semipresencial [SUPOSIÇÃO]. |
| 68615-K6 | pós em patologia clínica vet | matricular | Baixo | 50 (24/8/18) | K11.5 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68615-K7 | quanto custa pós em patologia clínica veterinária | resolver | Médio | 52 (22/14/16) | K11.6 | Página da turma 68615 (`investimento`, dado) | Número só do dado. |
| 68615-K8 | como montar e administrar um laboratório clínico veterinário | aprender | Baixo | 34 (6/8/20) | nova (objetivo da ficha) | Artigo de apoio ligado a 68615 [REVISÃO DOCENTE] | Cobre a dor de quem quer abrir laboratório. |
| 68615-K9 | controle de qualidade em laboratório clínico veterinário | aprender | Baixo | 32 (6/8/18) | nova (módulo 24) | `matriz` e artigo de apoio | No limite do corte. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| pós em citopatologia ou citologia veterinária; leitura de lâminas | página de 333 | Seção 4. A paga de 68615 nega "citopatologia". |
| hematologia, hemograma, interpretação de hemograma | página de 68608 (onda 1) e artigo de apoio | A paga nega "hematologia". A página de 68615 tem módulos de hematologia, mas a palavra não é alvo. |
| mielograma | nenhuma das duas | Seção 4. |
| histopatologia, anatomopatologia, necropsia | sem página | Fora do curso (ver sugestão 1, seção 3). |
| pós em patologia clínica EAD; título de especialista em patologia clínica | sem página (ou guia A11) | Pago nega EAD; título é T6. |
| prova de bolsa de patologia clínica | sem página nesta onda | Decisão 14; o bloco "PROVA DE BOLSA" da ficha sai no OB1. |
| "referência nacional", "reconhecimento pelo Ministério da Educação" | nenhum termo | Frases da ficha que a página nova não repete. |

### 8.2 Perguntas que o candidato faz a assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68615-Q1 | Pós em patologia clínica veterinária serve para clínico geral ou só para quem trabalha em laboratório? | Problema | comparar | 44 (14/8/22) | Q11.1 | `para_quem` e `faq` de 68615 | A ficha diz "Médicos Veterinários"; foco em laboratório clínico pelo objetivo. |
| 68615-Q2 | Qual a diferença entre hematologia, patologia clínica e citopatologia veterinária na pós? | Comparação | comparar | 46 (16/8/22) | Q11.2 | Guia de decisão A11; `faq` de 68615 liga a 68608 e a 333 | Resposta de mensagens F2 sem comparar valor. |
| 68615-Q3 | Quero trabalhar com citologia: faço pós em patologia clínica veterinária ou em citopatologia veterinária? | Comparação | comparar | 48 (18/8/22) | nova | `faq` de 68615 e `faq` de 333 (mesma resposta, âncoras cruzadas); Guia A11 | **Pergunta que separa as duas páginas.** Primeira frase: 68615 é o curso de laboratório clínico, com a citologia como parte; 333 é o curso centrado na leitura de lâminas. |
| 68615-Q4 | O que se estuda na pós em patologia clínica veterinária? Tem prática de laboratório, como hemograma e urinálise? | Decisão | resolver | 48 (22/8/18) | nova | `sobre`, `matriz` (dado) e `faq` | A ficha cita aulas práticas e módulos presenciais de hemograma e de bioquímica e urina. |
| 68615-Q5 | A pós em patologia clínica veterinária ensina a montar e administrar um laboratório? | Decisão | resolver | 50 (22/8/20) | nova | `sobre` (objetivo da ficha) e `faq` | Sem prometer resultado de negócio nem renda. |
| 68615-QC1 | Quanto custa a pós em patologia clínica veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | Q11.5 | `investimento` (dado) | Número só do dado. |
| 68615-QC2 | Dá para entrar na pós em patologia clínica veterinária depois que a turma já começou? | Decisão | resolver | 54 (26/8/22) | nova | `faq` (dado da turma, OU14) | Decisão 18 e OU3. |
| 68615-QC3 | E se a turma da pós em patologia clínica veterinária não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número. A ficha de 68615 não traz o aviso de passagem e hotel que as outras trazem; a regra da linha vale. |

**Observações de 68615:** (1) O CEP da ficha difere do das demais páginas de São Paulo (OU13): não afeta termo, afeta o dado de local no schema. (2) O Guia A11 e as duas páginas devem repetir a mesma frase de diferença (68615-Q3) para a IA citar uma resposta só.

---

## 9. Seção 333: Pós-graduação em Citopatologia Veterinária (turma I), leitura de lâminas

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, início 27/03/2027, turma I, status aberto. **Ficha:** público-alvo "Médicos veterinários"; 24 módulos; 6 presenciais (módulo 1 em 27 e 28/03/2027 com manejo de materiais biológicos, coleta, coloração e microscopia; "Experiências práticas citopatológicas I, II e III" com leitura de lâminas e discussão de casos; citologia esplênica e linfoma; mielograma); temas: citologia básica, critérios de malignidade, gestão da qualidade, imunocitopatologia, automação, citoinclusão, inflamatórios e infecciosos, derrames cavitários, líquidos biológicos, trato respiratório, neoplasias de células redondas, leucemias, sangue periférico, glandulares, mesenquimais, trato gastrointestinal, urinário, reprodutivo, oftálmica e auditiva. A ficha traz coordenação "UFAPE" e uma só professora listada (OU12).

**O que a busca na web mostrou (27/10):** Guia da Carreira e Quero Bolsa têm páginas de "Citopatologia Veterinária" com oferta de especialização, em grande parte EAD e algumas semipresenciais ou presenciais em São Paulo; as ementas de universidades públicas (UFES, UnB) tratam citologia em disciplina de pós stricto sensu, não em especialização lato sensu; a UNIFAA inclui citopatologia dentro de patologia clínica. Não apareceu especialização lato sensu em citopatologia com leitura de lâminas como foco principal: sinal de espaço aberto para o posicionamento "leitura de lâminas" [SUPOSIÇÃO].

**Palavra principal:** pós-graduação em citopatologia veterinária. **Página:** a página da turma 333. **Tipo de página:** página da turma (tipo pos), com guia de decisão A11 de apoio.

### 9.1 Palavras-chave (termos próprios de citopatologia)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 333-K0 | pós-graduação em citopatologia veterinária | matricular | Baixo | 58 (28/8/22) | K11.3 | Página da turma 333 (`hero`, `sobre`, `resposta_citavel`) | Principal. Curso novo (turma I). |
| 333-K1 | pós em citologia veterinária | matricular | Baixo | 52 (26/8/18) | sec. A11 | Página da turma 333 | Semente paga de 333; "citologia" sozinha é de 333 (seção 4). |
| 333-K2 | especialização em citopatologia de cães e gatos | matricular | Baixo | 52 (26/8/18) | sec. A11 | Página da turma 333 (`sobre`) | A ficha não restringe a cães e gatos; usar só em anúncio e lista [CONFIRMAR NO CATÁLOGO]. |
| 333-K3 | especialização em citologia veterinária com leitura de lâminas | matricular | Baixo | 54 (26/8/20) | nova (módulos presenciais da ficha) | Página da turma 333 (`sobre`, `matriz`) | Diferencial de vocabulário frente a 68615. |
| 333-K4 | pós-graduação em citopatologia veterinária semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 333 (`faq`) | Teoria online e módulos de leitura presenciais. |
| 333-K5 | pós-graduação em citopatologia veterinária São Paulo | matricular | Baixo | 54 (28/8/18) | nova | Página da turma 333 (dado e JSON-LD) | O Quero Bolsa tem página "Citopatologia Veterinária em São Paulo". Local fora do texto da IA (CP1). |
| 333-K6 | citodiagnóstico veterinário pós | matricular | Baixo | 50 (26/8/16) | nova | Lista de palavras e grupo de anúncio | Termo usado em ementa universitária (UFES); [SUPOSIÇÃO] de que o candidato digita. |
| 333-K7 | quanto custa pós em citopatologia veterinária | resolver | Baixo | 50 (22/8/20) | nova | Página da turma 333 (`investimento`, dado) | Número só do dado. |
| 333-K8 | citologia de linfonodos, derrames cavitários e neoplasias de células redondas em cães e gatos | aprender | Médio | 34 (6/14/14) | nova (módulos da ficha) | Artigos de apoio [REVISÃO DOCENTE] | Consulta clínica de rotina; serve de conteúdo de autoridade, não de matrícula. No limite do corte. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| patologia clínica, análises clínicas, laboratório clínico veterinário | página de 68615 | Seção 4; a paga de 333 nega "patologia clínica". |
| hematologia, hemograma, leucemias (como curso) | página de 68608 | A paga de 333 nega "hematologia". |
| mielograma | nenhuma | Seção 4. |
| histopatologia, anatomia patológica, necropsia, patologia veterinária | sem página | Fora do curso. |
| curso de citologia veterinária (livre, de poucos dias) | sem página nesta página; guia A11 | É intenção de Cursos Livres; não misturar linhas. |
| "coordenação" e nome de coordenador | nenhum termo | A ficha traz "UFAPE" como coordenação (OU12). |
| pós em citopatologia EAD; título de especialista | sem página (ou guia A11) | Pago nega EAD; título é T6. |

### 9.2 Perguntas que o candidato faz a assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 333-Q1 | Existe pós em citopatologia veterinária? Quando começa a primeira turma? | Solução | matricular | 56 (28/8/20) | Q11.4 | `resposta_citavel` e `faq` de 333; `local_e_datas` (dado) | A data vem do dado, nunca do texto da IA. |
| 333-Q2 | O que se aprende numa pós em citopatologia veterinária? Vou treinar leitura de lâminas? | Problema | resolver | 52 (22/8/22) | nova | `sobre`, `matriz` (dado) e `faq` | Módulos de "Experiências práticas citopatológicas" e microscopia da ficha. Sem promessa de resultado. |
| 333-Q3 | Qual a diferença entre pós em citopatologia veterinária e pós em patologia clínica veterinária? | Comparação | comparar | 48 (18/8/22) | nova (de Q11.2 e 68615-Q3) | `faq` de 333 e `faq` de 68615 (mesma resposta); Guia A11 | Primeira frase: 333 é o curso centrado na leitura de lâminas; 68615 é o de laboratório clínico. Sem comparar valor. |
| 333-Q4 | Como funciona a pós em citopatologia semipresencial? Quais módulos são presenciais? | Problema | resolver | 50 (22/8/20) | nova | `faq` e `local_e_datas` (dado) | Pela ficha, são 6 módulos presenciais; a lista exata vem do dado. |
| 333-Q5 | Se eu entrar depois do primeiro módulo presencial da pós em citopatologia, como recupero a prática? | Decisão | resolver | 44 (24/8/12) | nova | `faq` (dado da turma, OU14) | **Bloqueada até OU3** (reposição do módulo 1 presencial). Sem OU3, nenhuma peça depois do início; resposta do time: "vou confirmar com a secretaria como fica". |
| 333-QC1 | Quanto custa a pós em citopatologia veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 333-QC2 | Dá para entrar na pós em citopatologia veterinária depois que a turma já começou? | Decisão | resolver | 54 (26/8/22) | nova | `faq` (dado da turma, OU14) | **Depende de OU3**, por causa do módulo 1 presencial. |
| 333-QC3 | E se a turma da pós em citopatologia veterinária não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número. |

**Observações de 333:** (1) A ficha tem uma só professora listada e coordenação "UFAPE" (OU12): nenhuma pergunta ou termo cita coordenação. (2) 333 e 68615 se complementam; a mensagem F2 e as respostas do time seguem a seção 4. (3) Curso de menor ticket das cinco (catálogo); isso não entra em palavra-chave nem em comparação.

---

## 10. As 10 palavras-chave e perguntas mais perto da matrícula (das 5 turmas)

Critério: intenção matricular ou resolver, maior M e maior F. Perguntas e termos com trava de resposta da Ufape (U10, OU3, OU10, OU11) só entram quando a trava atinge a mídia ou uma parte da resposta, e isso está na coluna "Trava".

| # | ID | Termo ou pergunta | Tipo | Intenção | Pontuação | Página-alvo | Trava |
|---|---|---|---|---|---|---|---|
| 1 | 289-K1 | pós em cardiologia veterinária em Goiânia | busca | matricular | 60 (30/8/22) | 289 | CP1 (cidade no texto) |
| 2 | 68615-K0 | pós-graduação em patologia clínica veterinária | busca | matricular | 60 (28/20/12) | 68615 | nenhuma |
| 3 | 333-K0 | pós-graduação em citopatologia veterinária | busca | matricular | 58 (28/8/22) | 333 | OU3 só para peça depois do início |
| 4 | 657-K0 | pós-graduação em anestesiologia avançada veterinária | busca | matricular | 58 (28/8/22) | 657 | PP7 e U10 para a mídia, não para o texto |
| 5 | 341-K0 | pós-graduação em medicina interna equina | busca | matricular | 56 (28/8/20) | 341 | OU10 (sem promoção) |
| 6 | 333-Q1 | Existe pós em citopatologia veterinária? Quando começa a primeira turma? | IA | matricular | 56 (28/8/20) | 333 | nenhuma |
| 7 | 289-Q1 | Tem pós em cardiologia veterinária em Goiânia? Como são as aulas? | IA | matricular | 54 (30/8/16) | 289 | CP1 |
| 8 | 657-Q1 | Existe pós em anestesiologia avançada para veterinário que já é anestesista? | IA | matricular | 56 (28/8/20) | 657 | a parte "para quem" depende de U10 |
| 9 | 341-Q1 | Existe pós em medicina interna equina no Brasil? | IA | matricular | 56 (28/8/20) | 341 | nenhuma |
| 10 | QC2 nas 5 turmas | Dá para entrar na pós depois que a turma já começou? | IA | resolver | 54 (26/8/22) | as 5 | OU3, OU14 |

---

## 11. Fontes consultadas na web (27/10/2026, WebSearch; nenhuma página aberta; resumos de busca)

- Anestesiologia: Quero Bolsa, Faculdades de Anestesiologia Veterinária (https://querobolsa.com.br/cursos-e-faculdades/anestesiologia-veterinaria/bolsas); UNAR, projeto pedagógico de pós em Anestesiologia Veterinária 2026 (https://www.unar.edu.br/wp-content/uploads/2026/04/PPC%20Pós%20Med%20Vet%20Anestesio%202026.pdf); Improve International, formação avançada em anestesia para enfermeiros veterinários (https://improveinternational.com/pt/coursedate/nadvcertanestesiaonline/).
- Equinos: European College of Equine Internal Medicine (https://www.ebvs.eu/colleges/european-college-equine-internal-medicine); Universidade Lusófona, Pós-Graduação em Clínica de Equinos, Portugal (https://www.ulusofona.pt/lisboa/pos-graduacoes/clinica-de-equinos); Universidad de Buenos Aires, Especialización en Medicina Deportiva del Equino (https://www.fvet.uba.ar/archivos/postgrado/2024/fichaMDdE.pdf).
- Cardiologia: Anclivepa-SP, edital de Cardiologia Veterinária 2026 (https://portal.anclivepa-sp.org.br/wp-content/uploads/2026/01/Edital-Cardiologia-veterinaria-2026-.pdf); Pravaler, cardiologia veterinária (https://www.pravaler.com.br/blog/profissoes/cardiologia-veterinaria/); Guia da Carreira, medicina veterinária em Goiânia (https://guiadacarreira.com.br/cursos-e-faculdades/goias--goiania/medicina-veterinaria).
- Patologia clínica: Guia da Carreira (https://www.guiadacarreira.com.br/cursos-e-faculdades/patologia-clinica-veterinaria/pos-graduacao); Pravaler, patologia veterinária (https://www.pravaler.com.br/blog/profissoes/patologia-veterinaria/); Agrobase, vaga de patologista clínico veterinário (https://www.agrobase.com.br/oportunidades/2026/05/patologista-clinico-veterinario-valinhos-sp/); UNIFAA, matriz de Patologia Clínica Veterinária de 2022 (https://www.unifaa.edu.br/pdfs/2022/02/matriz-patologia-clinica-veterinaria.pdf).
- Citopatologia: Guia da Carreira (https://www.guiadacarreira.com.br/cursos-e-faculdades/citopatologia-veterinaria/cursos); Quero Bolsa, Citopatologia Veterinária em São Paulo (https://querobolsa.com.br/cursos-e-faculdades/citopatologia-veterinaria/todos); UnB, ementa de Citopatologia Veterinária (https://saudeanimal.unb.br/images/EMENTAS/Citopatologia_Veterinria.pdf); UFES, ementa de Citodiagnóstico em Patologia Animal (https://cienciasveterinarias.ufes.br/sites/cienciasveterinarias.ufes.br/files/field/anexo/ppgcv_-_1012_-_citodiagnostico_em_patologia_animal.pdf).

---

## 12. Decisões pendentes que mudam este arquivo (resumo)

- **CP1 (template x termos de cidade):** o template proíbe local no texto da IA. Decidir com o cmo e a pessoa do marketing se `titulo_seo` e `resposta_citavel` podem receber a cidade por variável do dado (para 289, a cidade é o diferencial). Sem isso, a cauda de cidade depende do dado, do JSON-LD e dos guias.
- **CP2 (guias e artigos de apoio):** os guias de A1, A2, A11 e 341 existem em iscas-digitais v2; os artigos de apoio marcados "[REVISÃO DOCENTE]" são encomenda de lacunas-de-conteudo e briefing-de-conteudo, fora do kit mínimo.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início e status das 5 turmas: catálogo, seção 2. Módulos, presenciais, público-alvo, objetivos, coordenação, docentes listados, frases ligadas ao MEC, promoção de 341, segundo local de 341, bloco "PROVA DE BOLSA" de 289 e de 68615, CEP de 68615 e coordenação "UFAPE" de 333: fichas em contexto/cursos/pos/.
- Padrão de nome "Pós-graduação em <área>", turma mínima de 15, matrícula até o 3º módulo (decisão 18), prova de bolsa fora desta onda (decisão 14) e proibição de frase de certificação: contexto/pos-graduacao.md e docs/execucao-2026-10-26.md.
- Regras do texto da IA (sem número, preço, data, vaga, local nem nome de docente) e campo `palavra_chave_principal`: templates/pagina-da-turma.md.
- Sementes, negativas gerais e negativas por turma da Busca paga: anuncios-google-pos-2026-10-26.md (v6), seções 6 e 7.
- Termos, notas e IDs reaproveitados (K1.3, K1.6, K2.2, K2.3, K2.7, K2.8, K11.2 a K11.6, A14, Q1.1, Q1.4, Q1.5, Q1.7, Q2.3, Q2.4, Q11.1, Q11.2, Q11.4, Q14.2, QT2, QT3, QT7): pesquisa-de-palavras-chave-pos-2026-10-26.md (v3).
- Resultados da busca na web (agregadores, editais, matrizes e ausência de oferta brasileira com os nomes "anestesiologia avançada" e "medicina interna equina" nos resumos): seção 11.
- 333 e 68615 têm vocabulário próprio: leitura de lâminas (módulos presenciais de citologia na ficha de 333) e laboratório clínico (objetivo da ficha de 68615).

## [SUPOSIÇÃO]

- Todo volume de busca (Alto, Médio, Baixo) é qualitativo, pelo critério da seção 2.2: quantidade de ofertas em agregadores e tipo do termo. Nenhuma exportação de ferramenta foi fornecida.
- Toda nota marcada "nova" é do agente pelo critério da seção 2.2; as reaproveitadas mantêm a nota de 26/10.
- A formulação exata das perguntas de IA e dos termos novos (o WebSearch não traz o preenchimento automático do Google).
- A ausência de oferta brasileira concorrente em "anestesiologia avançada", "medicina interna equina" e "citopatologia com leitura de lâminas" indica espaço aberto (a busca na web não é a página de resultados do Google).
- A cauda local de 289 (Goiânia) é a melhor chance da turma; a cabeça de termo é disputada.
- "Médico veterinário de equinos" como variação de corpo de texto em 341.
- "Análises clínicas veterinárias" atrai o mesmo público de patologia clínica (K11.4, herdada).
- O candidato digita "citodiagnóstico" (333-K6).
- Sugestões de negativas (histopatologia, anatomopatologia, necropsia; ecocardiograma exata em 289) ao gestor-de-midia.
- "Citologia" sozinha é de 333 e "patologia clínica" junto de "citologia" é de 68615 (regra de desempate da seção 4).
- Corte de 32 pontos para virar alvo (regra prática da skill, não meta).

## [CONFIRMAR]

- **U10:** pré-requisito de 657 (a ficha diz "exclusiva para médicos veterinários anestesistas já atuantes"). Bloqueia 657-K8, 657-Q3 e a parte "para quem" de 657-Q1.
- **OU3:** como se repõe módulo perdido, em especial o módulo 1 presencial de 333. Bloqueia 333-Q5 e 333-QC2 e qualquer peça de 333 depois do início.
- **OU10 e OU11:** regra da promoção de 341 e segundo local e formato do módulo 3. Bloqueiam 341-Q3 e a frase de 341-QC2.
- **OU12:** coordenação e corpo docente de 333.
- **OU13:** CEP de 68615.
- **OU14:** se a regra do 3º módulo pode entrar como dado da turma no FAQ (as perguntas QC2 das 5 turmas dependem disso).
- **CP1:** se `titulo_seo` e `resposta_citavel` podem receber a cidade por variável do dado (o template proíbe local no texto da IA).
- **Catálogo e ficha:** se 657-K2, 333-K2 e 289-K3 podem citar "cães e gatos" (as fichas de 657 e 333 não restringem a espécie); nível de entrada e experiência prévia de 289, 341 e 68615; frequência exata dos módulos presenciais e hospedagem; equipamento (microscópio) em 333.
- **Volume de busca:** exportação do Planejador de Palavras-chave ou do Search Console, a pedir a quem executa a Busca paga (anuncios-google-pos, seção 6, já marca "volume e CPC [DADO NÃO FORNECIDO]").
- **Checagem em assistentes:** rodar as 40 perguntas (8 por turma) de 3 a 5 vezes por assistente e registrar a taxa (roteiro da seção 2.2); sem isso não há nota de visibilidade.
- **Sugestões de negativas pagas:** decisão do gestor-de-midia e do qa (seção 3).
- **Guias e artigos de apoio:** quem escreve e revisa o que está marcado "[REVISÃO DOCENTE]" e "[REVISÃO REGULAÇÃO]" (lacunas-de-conteudo e briefing-de-conteudo).
- **U11:** valor da inscrição; até a resposta nenhuma peça cita valor de inscrição.
