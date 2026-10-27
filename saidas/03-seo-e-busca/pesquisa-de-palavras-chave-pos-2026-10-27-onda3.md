# Pesquisa de palavras-chave e perguntas de IA das 8 turmas de abril de 2027 da Pós-graduação (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609), encomenda O1, lote A, da onda 3

- **Agente:** pesquisa-de-palavras-chave
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** O1 do plano do CMO (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md, versão 2, seção 10), lote A (abril de 2027). A turma 662 fica fora, em espera total (OU18); o registro está na seção 14. O lote B (maio) é outra entrega, em nova versão deste arquivo, sem mudar o nome.
- **Status:** rascunho para o qa-de-marketing (auditoria 03-busca e auditorias/conformidade-educacional.md). Nada é publicado, enviado ou pago. Nenhuma ação em site, anúncio ou CRM foi feita; todo pedido ao time do site e ao gestor-de-midia é sugestão para decisão humana.
- **Consumidores deste arquivo:** mensagens (O2), landing-page (O3, campo `palavra_chave_principal` do template), seo-on-page (O4) e otimizador-de-cta (O5). Para os guias de decisão e os artigos de apoio citados aqui, o próximo agente é **lacunas-de-conteudo**.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md (instruções do projeto, já carregadas no início da sessão)
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 10, 11, 12, 14, 16, 18 e 20)
  - contexto/ufape-geral.md e contexto/pos-graduacao.md (inclusive "Padrão de nome")
  - contexto/catalogo-de-cursos.md (inteiro; a seção 2, linhas das 8 turmas e das turmas antigas, é a única fonte dos dados de curso citados aqui)
  - Fichas inteiras em contexto/cursos/pos/: 679-pos-graduacao-em-infectologia-veterinaria.md, 68632-pos-graduacao-em-clinica-cirurgica-de-caes-e-gatos.md, 68635-pos-graduacao-em-clinica-medica-e-emergencia-de-pequenos-animais.md, 366-pos-graduacao-em-fisioterapia-fisiatria-e-reabilitacao-veterinaria.md, 68628-pos-graduacao-em-oncologia-veterinaria.md, 68617-pos-graduacao-em-endocrinologia-de-pequenos-animais.md, 68636-pos-graduacao-em-pneumologia-veterinaria.md, 68609-pos-graduacao-em-anestesiologia-veterinaria.md
  - Fichas das turmas antigas, só o bloco "Dados principais" e o cronograma até o 3º módulo: 535, 665, 663 e 68607; só o bloco "Dados principais": 670, 654 e 68605
  - templates/pagina-da-turma.md (tipo pos: regras do texto da IA e ordem padrão)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (linhas 1 a 420 e 820 a 1013: cabeçalho, seções 0 a 4, 7.5 a 7.7, 8 a 11 e as listas finais; as seções 5, 6 e 7.1 a 7.4 não foram lidas)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md (formato, escalas e a regra de vocabulário entre turmas)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (2.1, v3: seções 2 e 3 e as áreas A1, A2, A3, A4, A7, A10 e A14, reaproveitadas aqui com o ID de origem)
  - saidas/11-midia-paga/anuncios-google-pos-2026-10-26.md (v6, linhas 1 a 398: seções 0 a 8.2; sementes, negativas e janelas de extensão)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md (seções 1 a 3, Q1, Q55 e a seção 5)
  - .claude/skills/visibilidade-em-ia/SKILL.md (roteiro de perguntas e pontuação)
- **Pesquisa na web:** 8 consultas com WebSearch em 27/10/2026, uma por turma (fontes na seção 16). Nenhuma página foi aberta. Não tentei abrir faculdade.ufape.com.br: o texto das páginas está nas fichas.
- **Dados pessoais:** nenhum. Docentes não são nomeados neste arquivo.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape ou o time do site tem; [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo e a ficha não trazem; [SUPOSIÇÃO] é hipótese ou escolha deste agente, sempre com o critério.

---

## 1. Resumo para quem decide

1. **Uma palavra-chave principal por turma, ligada a uma única página** (campo `palavra_chave_principal` do template), igual à primeira semente `__area` da Busca paga da mesma turma (anuncios-google-pos v6, seção 6), para que orgânico e pago contem a mesma história e cheguem à mesma página:

| Turma | `palavra_chave_principal` | Origem | Alvo realista de curto prazo |
|---|---|---|---|
| 679 | pós-graduação em infectologia veterinária | A14 da pesquisa de 26/10 | o mesmo termo (nicho de cauda) |
| 68632 | pós-graduação em clínica cirúrgica de cães e gatos | K4.1 da pesquisa de 26/10 | pós em clínica cirúrgica presencial em Goiânia (68632-K1) |
| 68635 | pós-graduação em clínica médica e emergência de pequenos animais | nome do catálogo, primeira semente paga | o mesmo termo |
| 366 | pós-graduação em fisioterapia veterinária | K4.6 da pesquisa de 26/10 | pós em reabilitação veterinária (366-K1) |
| 68628 | pós-graduação em oncologia veterinária | K10.1 da pesquisa de 26/10 | pós em oncologia veterinária de pequenos animais presencial em São Paulo (68628-K1) |
| 68617 | pós-graduação em endocrinologia de pequenos animais | nome do catálogo, primeira semente paga | pós em endocrinologia de pequenos animais semipresencial (68617-K1) |
| 68636 | pós-graduação em pneumologia veterinária | K2.6 da pesquisa de 26/10 | o mesmo termo |
| 68609 | pós-graduação em anestesiologia veterinária | K1.1 da pesquisa de 26/10 | pós em anestesiologia veterinária em Goiânia (68609-K1) |

2. **Vocabulário separado entre turmas da mesma área (E11)** na seção 4: A1 (68609, com 657 e 359), A2 (68636, com 289 e 352), A3 (68635, com 68623) e A4 (68632 e 366, com 578 e 662). Cada página fica com o seu termo; o termo que mistura duas turmas vai para a página cujo nome o candidato digitou primeiro. Cada seção de turma traz a tabela "termos que não são desta página".
3. **Disputa com turma antiga à venda (E20), seção 5.** Há 4 pares pedidos pelo plano (535 e 665 com 68632, 663 com 68635, 68607 com 68609) e 3 que as fichas mostram (654 com 68628, 670 com 68636 e 664 com 68609), mais 586 (produto diferente). A regra proposta separa dois casos: mesma oferta em outra data (535, 663, 664, 654 e 670) e mesmo nome em outro campus ou modalidade (665 e 68607). O pedido de canonical ou 301 ao time do site está na seção 5 e continua [CONFIRMAR]. Uma constatação que muda o prazo: pelo cronograma das fichas, o 3º módulo de 535 e de 663 foi em 26 e 27/09/2026, já passou; se as duas páginas ainda vendem, vendem fora da regra da decisão 18 [CONFIRMAR].
4. **O que a busca na web mostrou (27/10):** nas 8 áreas, os resultados são agregadores (Quero Bolsa, Guia da Carreira, EAD.com.br), páginas de faculdades de outras praças e perfis acadêmicos. Nenhuma página da Ufape apareceu. Não surgiu pós semipresencial de anestesiologia veterinária em Goiânia, nem pós presencial de clínica cirúrgica de cães e gatos em Goiânia, nem pós de oncologia veterinária semipresencial de instituição de São Paulo: sinal de espaço aberto para a cauda de cidade e de formato [SUPOSIÇÃO]. O WebSearch não é a página de resultados do Google: ausência é indício, não prova.
5. **Três turmas têm a data como [CONFIRMAR]** (679, OU19; 366, OU20; 68636, OU21). Nenhuma palavra-chave desta lista depende de data; só o `local_e_datas` (dado) e as perguntas sobre entrada depois do início dependem.
6. **Uma turma tem pergunta bloqueada por resposta da Ufape: 68632** (módulo 1 presencial, OU3). A pergunta sobre entrada depois do início fica sem resposta de página; a resposta do time é "vou confirmar com a secretaria" (E22). 679, 68635 e 366 só falam da entrada depois do início sem o mês do 3º módulo (E18).
7. **Nenhum volume de busca foi inventado.** Volume é qualitativo (Alto, Médio, Baixo) e [SUPOSIÇÃO], pelo critério da seção 2.2.
8. **Conta do arquivo:** 8 palavras principais e 72 secundárias (80 termos) e 64 perguntas a assistentes de IA (8 por turma).

---

## 2. Método, escalas e limites

### 2.1 O que foi feito

1. Reaproveitei da pesquisa de 26/10 (v3) os termos e as perguntas de A1, A2, A3, A4, A7, A10 e A14 que tocam as 8 turmas, com o ID de origem na coluna "Origem". O que é novo está marcado "nova".
2. Li as 8 fichas inteiras e conferi, módulo a módulo, o que cada uma diz de formato (online ou presencial) antes de escrever qualquer termo ou pergunta que fale de prática (E4 e E5).
3. Cruzei com as sementes e as negativas da Busca paga (anuncios-google-pos v6, seções 6 e 7) para não haver conflito entre orgânico e pago (seção 3).
4. Fiz 8 consultas na web (uma por turma) e anotei só o que o resumo da busca mostrou.
5. Escrevi as perguntas como o candidato digita a um assistente (ChatGPT, Gemini, Perplexity, Claude), nos estágios problema, solução, comparação e decisão do roteiro da skill visibilidade-em-ia. Cada turma tem 8: 5 específicas e 3 comuns (preço e parcelas, entrada depois do início, turma que não fecha).

### 2.2 Pontuação

Mesma escala das pesquisas de 26/10 e da onda 2 (skill visibilidade-em-ia, sem o componente "lacuna em IA", que só existe com checagem real em assistentes): pontuação = M + D + F, de 0 a 80, mostrada como "total (M/D/F)".

- M, intenção de matrícula: matricular de 26 a 30; resolver de 20 a 26; comparar de 14 a 20; aprender de 4 a 10.
- D, demanda: sem exportação de ferramenta, qualitativa: Alto = 20, Médio = 14, Baixo = 8. [SUPOSIÇÃO: critério é quantidade de ofertas em agregadores e tipo do termo; nenhum volume numérico existe neste arquivo.]
- F, facilidade: chance real de a Ufape vencer. Cabeça de termo contra agregadores de 6 a 12; termo intermediário de 14 a 18; cauda com página própria e pouca concorrência visível de 18 a 24.
- Corte: abaixo de 32 não vira alvo; fica como apoio. [SUPOSIÇÃO: regra prática da skill, não meta.]
- Nota nova (marcada "nova") é [SUPOSIÇÃO] do agente pelo mesmo critério. Nota reaproveitada mantém o valor da pesquisa de 26/10.
- Tipo: toda linha de "Palavras-chave" é **busca**; toda linha de "Perguntas para IA" é **IA**.
- A coluna "Ufape aparece em assistentes" fica "conferir manualmente" em todas as perguntas. Roteiro: a pessoa roda cada pergunta de 3 a 5 vezes por assistente e registra a taxa ("citada 2 de 5"). Sem checagem, não há nota de visibilidade.
- **Correção de conta:** a pergunta "Dá para entrar na pós depois que a turma já começou?" (QC2) aparece na onda 2 como "54 (26/8/22)"; 26 + 8 + 22 dá 56. Aqui uso 56 quando a resposta está liberada. Sugiro ao orquestrador corrigir a onda 2 [CONFIRMAR]; não editei o arquivo dela.

### 2.3 Tipos de página usados na coluna "Atende"

- **Página da turma (tipo pos, template pagina-da-turma.md):** a página de dinheiro. A coluna diz o bloco que responde: `hero`, `sobre`, `para_quem`, `matriz` (dado), `local_e_datas` (dado), `investimento` (dado e frase de apoio), `numeros` (dado), `faq`, `resposta_citavel` e `entidades` (campos de SEO).
- **Guia de decisão:** página de apoio de comparação (iscas-digitais-pos v2: A1, A2, A3, A4, A7, A10 e A14 têm guia, segundo o plano da onda 3, seção 3). Liga para a página da turma.
- **Artigo de apoio:** conteúdo de intenção "aprender", em página separada da de matrícula (encomenda para lacunas-de-conteudo e briefing-de-conteudo).
- **Sem página:** termo que a Ufape não deve mirar (regulação, bolsa, concorrente, EAD, outra linha).

### 2.4 Limites

- O WebSearch não devolve o preenchimento automático do Google nem "As pessoas também perguntam". As variações vêm das fichas, dos títulos dos resultados, do roteiro e da persona; a formulação exata é [SUPOSIÇÃO]. Antes de investir em anúncio novo, conferir as sugestões do Google e o Search Console.
- Nenhum assistente de IA foi consultado. Nenhuma taxa de citação foi inventada.
- Dados de curso (nome, modalidade, local, carga horária, turma, início) vêm só do catálogo, seção 2. O que só existe na ficha (módulos, formato por módulo, público-alvo) é citado como "ficha"; o que nem a ficha traz leva [CONFIRMAR NO CATÁLOGO].
- Nenhum termo de certificação, título de especialista, bolsa ou nota de órgão regulador é alvo. Nenhuma pergunta promete esses itens. Os superlativos e promessas das fichas (E14) ficam só no dado e no pedido OC1 do plano.
- Nome do curso em texto visível: "Pós-graduação em <área>" (contexto da linha). "Pós em", "pós vet" e abreviações aparecem só em listas de palavras-chave e em grupos de anúncio, nunca em título, H1 ou FAQ.
- Número em termo de busca ("pós de 750 horas") não entra em texto de página (E1); o termo é atendido pelo bloco de dado `numeros` e por guia.
- Nome do curso na página x palavra digitada: o nome do catálogo não muda (E2). Onde o candidato digita uma forma mais curta ou mais comum (fisioterapia veterinária em 366, oncologia veterinária de pequenos animais em 68628, endocrinologia e metabologia em 68617), a forma digitada é termo de busca e de lista, nunca o nome da página.

---

## 3. Como orgânico e pago não entram em conflito

Fonte: anuncios-google-pos v6 (seções 6 e 7). A palavra principal orgânica de cada turma é a primeira semente `__area` da Busca paga: as duas levam à mesma página, então não há disputa de destino. O que pode gerar conflito é o orgânico mirar, na página da turma, termos que o pago nega de propósito ou que são de outra página.

| Turma | Sementes pagas (`__area`, resumo) | Negativas pagas próprias | Regra para o orgânico |
|---|---|---|---|
| 679 | pós-graduação em infectologia veterinária (frase e exata); especialização em infectologia de cães e gatos; pós em doenças infecciosas veterinária | citopatologia; goiânia; goiás | Citopatologia é da página de 333 (onda 2). A linha "Citopatologia 03/04" da visão de campanhas aponta para esta página (P3, OU19): isso não é termo, é link a corrigir. |
| 68632 | pós-graduação em clínica cirúrgica de cães e gatos; pós em clínica cirúrgica presencial em goiânia; pós presencial goiânia veterinária; especialização em cirurgia de cães e gatos | ortopedia; videocirurgia; são paulo; semipresencial | A turma é presencial: nenhum termo ou texto diz "semipresencial". Ortopedia é de 662 (em espera) e videocirurgia é de 578 (maio). "São Paulo" é da turma antiga 665. |
| 68635 | pós-graduação em clínica médica e emergência de pequenos animais; pós em emergência veterinária; pós em clínica médica de pequenos animais; especialização em clínica médica de cães e gatos | terapia intensiva; goiânia; goiás | Terapia intensiva é de 68623 (maio). A cabeça de termo "pós-graduação em clínica médica de pequenos animais" (K3.3) fica fora das sementes pagas por desenho; o orgânico pode mirá-la. |
| 366 | pós-graduação em fisioterapia veterinária; pós em reabilitação veterinária; pós em fisiatria veterinária; pós em fisioterapia e reabilitação de cães e gatos | ortopedia; fisioterapeuta; goiânia; goiás | Ortopedia é de 662. "Fisioterapeuta" é negativa porque a ficha traz público de médicos veterinários; o orgânico não mira quem busca como fisioterapeuta. |
| 68628 | pós-graduação em oncologia veterinária (frase e exata); pós em oncologia veterinária são paulo; especialização em oncologia de cães e gatos | [curso de eletroquimioterapia] e [eletroquimioterapia curso] (exatas); goiânia; goiás | O curso livre de eletroquimioterapia é de Cursos Livres (560). O módulo de eletroquimioterapia da pós continua no texto como conteúdo, sem tomar o termo de curso. |
| 68617 | pós-graduação em endocrinologia de pequenos animais; pós em endocrinologia veterinária; pós em endocrinologia de pequenos animais semipresencial; especialização em endocrinologia de cães e gatos | nefrologia; goiânia; goiás | Nefrologia é de 68612 e da prova 68653; os módulos de função renal da ficha são conteúdo. |
| 68636 | pós-graduação em pneumologia veterinária (frase e exata); pós em pneumologia veterinária são paulo; especialização em pneumologia de cães e gatos | cardiologia; ventilação mecânica; goiânia; goiás | Cardiologia é de 289 (onda 2); ventilação mecânica é de 352 (maio). O módulo de ventilação mecânica da ficha é conteúdo. |
| 68609 | pós-graduação em anestesiologia veterinária; pós em anestesiologia veterinária em goiânia; especialização em anestesiologia de cães e gatos | avançada; locorregional; são paulo | O termo genérico e "Goiânia" são desta página; "avançada" é de 657 e "locorregional" é de 359. A Busca paga de 657 já nega o termo genérico. |

**Negativas gerais da Busca paga (valem para as 8):** grátis, gratuito, pdf, apostila, download, concurso, emprego, salário, residência, mestrado, doutorado, enem, vestibular, curso livre, curso online gravado, graduação em medicina veterinária (exata), ead, "100% online", universidade federal, pernambuco, agreste, garanhuns, prova de bolsa, bolsa de estudos, bolsa, título de especialista, "reconhecida pelo mec", anclivepa. Consequência para o orgânico: EAD, residência, título e concorrente não são alvo da página da turma; a dúvida do candidato é respondida em guia ou artigo de apoio, nunca na página de dinheiro. Bolsa e prova de bolsa estão fora desta onda (decisão 14).

**Conflitos encontrados e resolvidos nesta pesquisa:** nenhum termo secundário das 8 turmas usa uma negativa própria da mesma turma. Dois pontos pedem cuidado e estão marcados nas seções: (a) 68628-K1 e 68609-K10 trazem a palavra "presencial", que a Busca paga não nega, mas que não descreve a turma (as duas são semipresenciais); o termo é de lista e grupo de anúncio, e a página diz semipresencial; (b) "especialização em ... de cães e gatos" é semente paga em 679, 68635, 366, 68628, 68617, 68636 e 68609, e a ficha não restringe a espécie nessas turmas (E3); o termo fica em lista e anúncio, nunca em texto de página, [CONFIRMAR NO CATÁLOGO] se a Ufape quiser o recorte.

**Sugestões ao gestor-de-midia, sem editar o arquivo dele** (são [SUPOSIÇÃO]; a decisão é do gestor e do qa):
1. Avaliar negativas de "mini curso", "aprimoramento", "grupo de estudos" e "congresso" nas 8 campanhas. Os Cursos Livres contínuos de mesma área (465 em oncologia, 483 em anestesiologia, 458 em endocrinologia, 137 em clínica médica, 541 em antibioticoterapia, 644 e 68666 em grupos de estudo) podem casar com as sementes pagas e a lista geral só nega "curso livre" e "curso online gravado".
2. Em 68636, avaliar "medicina humana" e "pneumologista" como negativas: os resultados da web para pneumologia são dominados por medicina humana.
3. Em 366, avaliar "crefito" e "fisioterapia humana" junto de "fisioterapeuta": a ficha cita o conselho de fisioterapia e o termo atrai o público de fisioterapia humana.
4. Em 679, avaliar "saúde pública", "vigilância sanitária" e "vigilância epidemiológica": a ficha cita atuação em saúde pública, mas o público do curso é clínico e a paga já nega "concurso".

---

## 4. Quem fica com cada termo entre turmas da mesma área (E11)

Regra: pelo vocabulário que o candidato digita. O nome do módulo na ficha é conteúdo da página, não palavra-chave. Frase-ponte de página diz em que cada turma é centrada, nunca que uma cobre ou contém a outra (E11); a redação é do agente mensagens (O2).

| Área e turmas | Termo ou tema | Página | Motivo |
|---|---|---|---|
| A1: 68609, 657 (março) e 359 (maio) | pós em anestesiologia veterinária (genérico), "Goiânia" | 68609 | Nome do curso e campus. A paga de 657 nega o termo genérico. |
| | anestesiologia avançada | 657 | A paga de 68609 nega "avançada". |
| | anestesiologia locorregional, bloqueios guiados por ultrassom | 359 | A paga de 68609 nega "locorregional"; os módulos de bloqueio da ficha de 68609 são conteúdo. |
| | prova ou curso preparatório de título de especialista | sem página (Livres 488 por link) | Título é T6 bloqueado; convite da ficha de 68609 fica fora (E13). |
| A2: 68636, 289 (março) e 352 (maio) | pneumologia veterinária | 68636 | Nome do curso. |
| | cardiologia veterinária, ecocardiografia | 289 e 698 | A paga de 68636 nega "cardiologia". |
| | ventilação mecânica (como pós) | 352 | A paga de 68636 nega "ventilação mecânica"; o curso livre de ventilação mecânica (68618, 507) é de Cursos Livres. |
| A3: 68635 e 68623 (maio) | clínica médica e emergência de pequenos animais; pós em clínica médica de pequenos animais; pós em emergência veterinária | 68635 | Nome do curso e semente paga. |
| | terapia intensiva, UTI veterinária, "terapia intensiva e emergência veterinária" (nome completo) | 68623 | A paga de 68635 nega "terapia intensiva". |
| | internação veterinária (610, 614 e 615, sem venda) | sem alvo | Sem turma aberta. |
| A4: 68632, 366, 578 (maio) e 662 (espera) | clínica cirúrgica, pós em cirurgia veterinária (cabeça), cirurgia presencial em Goiânia | 68632 | Nome do curso e campus. |
| | fisioterapia, fisiatria, reabilitação veterinária | 366 | Nome do curso. |
| | videocirurgia | 578 | A paga de 68632 nega "videocirurgia". |
| | ortopedia veterinária, osteossíntese | 662 (em espera, OU18) | A paga de 68632 e a de 366 negam "ortopedia". Fica reservado: nem 68632 nem 366 tomam o termo, mesmo com módulo de ortopedia na ficha. |
| A10, A7, A14 (por curso) | oncologia veterinária | 68628 | Nome do curso. |
| | citologia e citopatologia | 333 (onda 2) | Módulos de citologia da ficha de 68628 não existem como termo. |
| | endocrinologia | 68617 | Nome do curso. |
| | nefrologia e urologia | 68612 e prova 68653 | A paga de 68617 nega "nefrologia". |
| | infectologia, doenças infecciosas | 679 | Nome do curso. Antibioticoterapia (curso) é de Cursos Livres (541). |

---

## 5. Disputa de busca com turma antiga à venda (E20) e regra de canonical ou 301

O catálogo marca as turmas antigas como "verificar (turma já iniciada e com venda)", e a decisão 18 permite vender até o 3º módulo. Nesse intervalo, duas páginas com o mesmo nome disputam a mesma consulta (Q55 da revisão da onda 2). As datas das turmas antigas abaixo vêm das fichas e são **nota interna para o pedido ao time do site; nunca entram em peça** (E6).

### 5.1 Os pares

| Turma nova | Turma antiga | O que têm em comum | O que difere | Estado no catálogo (26/10) | 3º módulo da antiga (cronograma da ficha, nota interna) | Termos em disputa |
|---|---|---|---|---|---|---|
| 68632 (Goiânia, presencial, V, 10/04/2027) | 535 (Goiânia, presencial, IV, 25/07/2026) | nome, campus, modalidade e carga horária: mesma oferta em outra data | turma e início | verificar (iniciada e com venda) | 26 e 27/09/2026: **já passou** | todos, inclusive "pós em clínica cirúrgica presencial em Goiânia" |
| 68632 | 665 (São Paulo, semipresencial, VIII, 19/09/2026) | nome e carga horária | campus e modalidade; a ficha de 665 traz público "Graduandos e Médicos Veterinários" e coordenação "UFAPE", a de 68632 traz só "Médicos Veterinários" e nenhuma coordenação | verificar (iniciada e com venda) | 21 e 22/11/2026 | "pós-graduação em clínica cirúrgica de cães e gatos" (nome igual); "são paulo" e "semipresencial" são da 665 |
| 68635 (São Paulo, semipresencial, 750 h, V, 10/04/2027) | 663 (São Paulo, semipresencial, 750 h, IV, 25/07/2026) | nome, campus, modalidade e carga horária: mesma oferta em outra data | turma e início | verificar (iniciada e com venda) | 26 e 27/09/2026: **já passou** | todos |
| 68609 (Goiânia, semipresencial, VIII, 24/04/2027) | 68607 (São Paulo, semipresencial, X, 24/10/2026) | nome e modalidade | campus; a ficha de 68607 abre com "Nível Básico a Intermediário", frase de nível que a ficha de 68609 não tem e que não passa para 68609 | verificar (iniciada e com venda) | 19 e 20/12/2026 | "pós-graduação em anestesiologia veterinária" (nome igual) |
| 68609 | 664 (Goiânia, semipresencial, VII, 11/04/2026) | nome, campus e modalidade: mesma oferta em outra data | turma e início | sem venda (avise-me) | fora da regra (sem venda) | todos; a página não vende, mas indexa |
| 68609 | 586 (Online, EAD, "Direto ao ponto", I, 360 h, 22/08/2026) | área | produto diferente (EAD, carga horária e nome com complemento) | verificar (iniciada e com venda) | não se aplica | "anestesiologia veterinária EAD" é da 586; a paga de 68609 nega EAD |
| 68628 (São Paulo, semipresencial, 10/04/2027) | 654 (São Paulo, semipresencial, VI, 11/04/2026) | nome, campus, modalidade e carga horária: mesma oferta em outra data | início e valor | sem venda (avise-me) | fora da regra (sem venda) | todos; a pesquisa de 26/10 já previa 301 de 654 |
| 68636 (São Paulo, semipresencial, VIII, 17/04/2027) | 670 (SP, VII, 10/04/2027 na planilha) | nome e campus | a página de 670 mostra "O produto requisitado não está mais disponível" | encerrado (link fora do ar) | não se aplica | todos; a data de 10/04/2027 da planilha está na linha de 670, não na de 68636 (OU21) |
| 679, 68617 e 366 | nenhuma | sem turma antiga do mesmo curso no catálogo | | | | |

Há ainda as páginas de prova de bolsa da mesma área (68639 e 68640 em anestesiologia; 68643 e 68644 em clínica cirúrgica; 68645 em clínica médica e emergência; 68648 em endocrinologia; 68657 em oncologia; 68659 em pneumologia). O nome delas começa por "Prova de Bolsa de Estudos para <área>" e compete com a página da turma pela consulta da área. Pela decisão 14 não há peça de bolsa nesta onda: nenhum termo desta lista mira "bolsa", e o link interno entre prova e turma fica com a onda das provas [CONFIRMAR]. Os pares do lote B (701 com 68616, 706 com 68629 e 666 com 68623) saem na entrega de maio.

### 5.2 Regra proposta (para decisão do time do site e da pessoa do marketing)

1. **Uma palavra principal, uma página.** Toda palavra-chave desta lista é da página da turma nova. A página antiga não recebe palavra-chave alvo, anúncio, link interno novo nem entra em guia.
2. **Mesma oferta em outra data** (535, 663, 664, 654 e 670): a antiga é a mesma página de curso em outra turma. Proposta: canonical da página antiga para a página da turma nova enquanto a antiga ainda vende, e 301 no dia seguinte à data limite da antiga (3º módulo da ficha; leitura "até a véspera" ou "inclui o dia" em OU6). [SUPOSIÇÃO: concentra a autoridade na página que a Ufape quer vender; o custo é perder a busca da antiga nos dias finais de venda.] Alternativa: canonical próprio na antiga até a data limite e só então 301. Para as que estão sem venda (664 e 654) e a que saiu do ar (670), o 301 já pode ser feito. Para 535 e 663, a data limite do cronograma já passou: confirmar se a venda terminou e, se terminou, fazer o 301 agora.
3. **Mesmo nome, outro campus ou modalidade** (665 e 68607): são ofertas diferentes, não são duplicatas. Cada página mantém canonical próprio. A diferença real é a cidade e a modalidade: com a CP1 aprovada, a cidade entra no título e na descrição das duas (proposta do qa na Q55 da onda 2); sem a CP1, a cidade e a modalidade só aparecem nos blocos de dado e no JSON-LD. Depois da data limite da antiga, ela sai de venda e recebe 301 para a página do curso ou para a próxima turma do **mesmo campus**; nunca para a página de outro campus (um candidato de São Paulo cairia numa turma de Goiânia). Sem destino do mesmo campus, a página fica sem venda, com o aviso de próxima turma, e sem 301 [CONFIRMAR].
4. **Produto diferente com nome parecido** (586, EAD): sem canonical nem 301. A dúvida "EAD ou semipresencial" é respondida no guia de decisão da área, não nas duas páginas de venda.
5. **Execução:** nada disso é feito pela squad. Cada mudança é pedido ao time do site, com a versão anterior exportada antes (como desfazer), 301 só depois de a página nova estar no ar e conferência no Search Console depois da troca [CONFIRMAR quem executa].

### 5.3 Pedidos ao time do site (todos [CONFIRMAR])

| # | Pedido | Turma |
|---|---|---|
| S1 | Canonical da 535 para a 68632 e 301 depois da data limite; confirmar se a venda da 535 já terminou | 68632, 535 |
| S2 | Canonical da 663 para a 68635 e 301 depois da data limite; confirmar se a venda da 663 já terminou | 68635, 663 |
| S3 | Canonical próprio em 665 e 68607, cidade e modalidade no título se a CP1 for aprovada; depois da data limite, 301 para a página do curso ou para a próxima turma do mesmo campus | 68632, 665, 68609, 68607 |
| S4 | 301 de 664 para a 68609, de 654 para a 68628 e de 670 para a 68636 (links de turmas sem venda ou fora do ar) | 68609, 68628, 68636 |
| S5 | Endereço no padrão "pos-graduacao-em-<área>" (o CMS aplica a regra ao salvar): hoje 6 das 8 páginas estão sem o "em" (68632, 68635, 366, 68628, 68617 e 68609); a URL antiga recebe 301 para a nova | 6 turmas |
| S6 | 68617: a URL termina em "/v/" (turma V); se existirem duas URLs com o mesmo conteúdo, canonical para a URL final (OU29) | 68617 |
| S7 | Corrigir a linha "Citopatologia 03/04" da visão de campanhas, que aponta para a página de 679 (P3, OU19) | 679 |

---

## 6. Seção 679: Pós-graduação em Infectologia Veterinária (turma IV)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, turma IV, status aberto, início 03/04/2027 [CONFIRMAR OU19: a data da planilha e a do site coincidem, mas a linha "Citopatologia 03/04" da visão de campanhas aponta para esta página, P3]. Dia do 3º módulo [CONFIRMAR NO CATÁLOGO] (E18).

**Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 24 módulos; 3 presenciais, nada além: módulo 3 "Prática laboratorial (coleta de amostras, armazenamento, envio)", módulo 13 "Zoonoses", sábado teórica e domingo com prática laboratorial (coleta de material para exame de raiva), e módulo 22 "Controle de infecção hospitalar", com prática no domingo. Os outros 21 são online. Temas dos módulos: introdução à infectologia clínica e imunologia, diagnóstico de doenças infecciosas, helmintos e protozoários, virologia, micologia, bacteriologia, doenças infecciosas de importância na medicina felina (viroses; bactérias e protozoários), antibioticoterapia, sepse, infecções intra-abdominais, doenças infecciosas por sistema (hematológica, gastrointestinal, cardiovascular e respiratória, renal, oftálmica, neurológica, neonatologia e reprodução, ortopédica), infectologia na UTI e vacinação. O objetivo da ficha cita prevenção e controle de zoonoses, diagnóstico e tratamento de doenças infecciosas e parasitárias, e a atuação do profissional da clínica médica de pequenos animais. A ficha não traz o aviso de passagem e hotel nem a linha de reembolso de inscrição (só a de não ressarcimento por adiamento): vale a regra da linha; reembolso [CONFIRMAR]. O superlativo do título e a promessa de empregabilidade ficam só no dado (E14).

**O que a busca na web mostrou (27/10):** o Quero Bolsa tem páginas "Doenças Parasitárias e Infectologia em Cães e Gatos", em EAD e ao vivo, com preços muito variados; as pós amplas de clínica médica de pequenos animais incluem parte infecciosa; nenhuma pós semipresencial com o nome "Infectologia Veterinária" apareceu e nenhuma página da Ufape. Sinal de espaço aberto para o termo, com pouca demanda provável [SUPOSIÇÃO]. Nicho de cauda.

**Palavra principal:** pós-graduação em infectologia veterinária. **Página:** a página da turma 679. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A14 de 679 (iscas-digitais v2) de apoio.

### 6.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 679-K0 | pós-graduação em infectologia veterinária | matricular | Baixo | 54 (28/8/18) | A14 | Página da turma 679 (`hero`, `sobre`, `resposta_citavel`) | Principal. Igual à semente paga (frase e exata). |
| 679-K1 | pós em infectologia veterinária São Paulo | matricular | Baixo | 54 (28/8/18) | nova | Página da turma 679 (dado e JSON-LD) | Local fora do texto da IA (CP1). |
| 679-K2 | pós em infectologia veterinária semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 679 (`faq`, `sobre`) | A modalidade vem do dado; no texto a IA pode dizer "semipresencial". |
| 679-K3 | especialização em infectologia de cães e gatos | matricular | Baixo | 50 (26/8/16) | sec. A14 | Lista de palavras e grupo de anúncio | A ficha fala em pequenos animais e traz módulos de medicina felina, sem restringir a espécie: nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 679-K4 | pós em doenças infecciosas veterinária | matricular | Baixo | 48 (24/8/16) | sec. A14 | Lista de palavras e grupo de anúncio | Grafia como o candidato digita; não vai para texto visível. |
| 679-K5 | pós em doenças infecciosas e parasitárias veterinária | matricular | Baixo | 48 (24/8/16) | nova (objetivo da ficha) | Página da turma 679 (`sobre`) | Termo da ficha ("doenças infecciosas e parasitárias") e do nome de agregador. |
| 679-K6 | pós em infecto vet | matricular | Baixo | 48 (24/8/16) | sec. A14 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 679-K7 | quanto custa pós em infectologia veterinária | resolver | Baixo | 46 (22/8/16) | nova | Página da turma 679 (`investimento`, dado) | O valor vem do banco; a IA escreve só a frase de apoio, sem número. |
| 679-K8 | zoonoses na clínica de pequenos animais: especialização | aprender | Baixo | 34 (6/8/20) | nova (módulo 13) | Artigo de apoio [REVISÃO DOCENTE] e `matriz` | Conteúdo de autoridade; no limite do corte. Sem promessa de carreira em saúde pública. |
| 679-K9 | controle de infecção hospitalar veterinária | aprender | Baixo | 32 (6/8/18) | nova (módulo 22) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | No limite do corte. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| citopatologia, citologia veterinária | página de 333 (onda 2) | A paga de 679 nega "citopatologia". |
| hematologia, hemograma | página de 68608 (onda 1) | O módulo de doenças infecciosas de importância hematológica é conteúdo. |
| curso de antibioticoterapia, atualização em antibioticoterapia | linha Cursos Livres (541), só por link | O módulo de antibioticoterapia da ficha é conteúdo; não misturar linhas. |
| sepse, terapia intensiva, UTI veterinária | página de 68623 (maio) | Módulos de sepse e de UTI são conteúdo. |
| clínica médica de pequenos animais (pós) | página de 68635 | A ficha cita o profissional da clínica médica no `sobre`, sem tomar o termo. |
| pós em medicina de felinos | sem alvo (650 em verificar) | Os módulos de medicina felina são conteúdo. |
| pós em parasitologia veterinária | sem alvo | A ficha tem um módulo de helmintos e protozoários, não um curso de parasitologia [SUPOSIÇÃO]. |
| saúde pública, vigilância sanitária, concurso | sem página | A ficha cita capacidade de atuação em saúde pública; promessa de carreira fica fora (E14). |
| pós em infectologia EAD; título de especialista; prova de bolsa | sem página (ou guia A14) | Pago nega EAD, título e bolsa; decisão 14. |

**Disputa E20:** nenhuma turma antiga do mesmo curso no catálogo. O único risco de destino é o P3 (link da visão de campanhas, pedido S7).

### 6.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 679-Q1 | Existe pós em infectologia veterinária em São Paulo? Como são as aulas? | Solução | matricular | 52 (28/8/16) | Q14.5 | `resposta_citavel` e `faq` de 679 | Resposta de 40 a 60 palavras sem número, local nem data. |
| 679-Q2 | O que se estuda numa pós em infectologia veterinária? Tem virologia, micologia e antibioticoterapia? | Problema | aprender | 38 (8/8/22) | nova | `sobre` e `matriz` (dado) de 679 | Os módulos vêm da ficha, nunca da IA. |
| 679-Q3 | Quais módulos da pós em infectologia veterinária são presenciais e o que se faz neles? | Decisão | resolver | 50 (22/8/20) | nova | `faq` e `local_e_datas` (dado) | Pela ficha são três, todos de laboratório ou de zoonoses e controle de infecção, com prática no módulo 3 e nos domingos dos módulos 13 e 22. Lista só dos três, sem generalizar "todas as aulas presenciais são práticas" (E5). |
| 679-Q4 | Pós em infectologia veterinária serve para clínico geral de pequenos animais? | Problema | comparar | 44 (14/8/22) | nova | `para_quem` e `faq` | A ficha diz só "Médicos Veterinários"; nível de entrada [CONFIRMAR NO CATÁLOGO]. |
| 679-Q5 | Infectologia veterinária ou clínica médica de pequenos animais: qual pós escolher? | Comparação | comparar | 44 (16/8/20) | nova | Guia de decisão A14 de 679; `faq` liga ao guia | Diz em que cada uma é centrada, sem dizer qual é melhor (E11). |
| 679-QC1 | Quanto custa a pós em infectologia veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 679-QC2 | Dá para entrar na pós em infectologia veterinária depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; sem o mês e sem a data do 3º módulo (E6 e E18); depois do início só com o dia [CONFIRMAR OU25]. |
| 679-QC3 | E se a turma da pós em infectologia veterinária não fechar, o que acontece com a viagem e o dinheiro? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; passagem e hotel só depois da turma confirmada (regra da linha). A ficha de 679 não traz reembolso: [CONFIRMAR]. |

---

## 7. Seção 68632: Pós-graduação em Clínica Cirúrgica de Cães e Gatos (turma V), Goiânia, presencial

**Dados de apoio (catálogo, seção 2):** Goiânia, **presencial**, 500 h, turma V, status aberto, início 10/04/2027. **Ficha:** público-alvo "Médicos Veterinários"; 24 módulos; turma presencial, sem formato marcado por módulo (E5: nada de "aulas online" nem de "semipresencial"); sem coordenação (OU34); módulo 1 presencial (OU3 aberta); temas: princípios da cirurgia e acessos, infecções e complicações cirúrgicas, trato urinário, trato gastrointestinal, paratopias e herniorrafias, olhos, trato reprodutor, exame ortopédico e neurológico, cirurgia oncológica e reconstrutiva, cirurgias torácicas, videocirurgia e endoscopia, ortopedia, otológicas, endócrino e hemolinfático, articulações, odontologia e cavidade oral, neurocirurgia, cardiovasculares, perioperatório e terapia intensiva do paciente cirúrgico, felinos, emergência e comunicação. A ficha traz o aviso de passagem e hotel e a linha de reembolso. O texto "referência nacional", "garante" e "reconhecimento pelo Ministério da Educação" fica no pedido OC1 (E14).

**O que a busca na web mostrou (27/10):** nenhum curso presencial de clínica e cirurgia de cães e gatos em Goiânia apareceu; surgiram o projeto pedagógico de uma pós de cirurgia veterinária da UNAR (2026), uma especialização em clínica médica e cirúrgica de uma faculdade do Paraná, a PUCPR e agregadores (Quero Bolsa, EducaMais Brasil). Sinal de espaço aberto para "presencial em Goiânia" [SUPOSIÇÃO]. A cabeça de termo é disputada por agregadores.

**Palavra principal:** pós-graduação em clínica cirúrgica de cães e gatos. **Alvo realista de curto prazo:** pós em clínica cirúrgica presencial em Goiânia (68632-K1). **Página:** a página da turma 68632. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A4 (iscas-digitais v2) de apoio.

### 7.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68632-K0 | pós-graduação em clínica cirúrgica de cães e gatos | matricular | Alto | 58 (28/20/10) | K4.1 | Página da turma 68632 (`hero`, `sobre`, `resposta_citavel`) | Principal; cabeça de termo. Hoje 3 páginas do catálogo têm o mesmo nome (535, 665 e 68632): seção 5. |
| 68632-K1 | pós em clínica cirúrgica presencial em Goiânia | matricular | Baixo | 60 (30/8/22) | K4.2 | Página da turma 68632 (dado e JSON-LD) | Melhor aposta da turma. Cidade fora do texto da IA (CP1). Frequência e jornada [CONFIRMAR NO CATÁLOGO]. |
| 68632-K2 | pós-graduação em clínica cirúrgica de cães e gatos Goiânia | matricular | Baixo | 60 (30/8/22) | K4.2 (exata derivada) | Página da turma 68632 | Mesma página de 68632-K1. |
| 68632-K3 | pós presencial goiânia veterinária | matricular | Baixo | 54 (28/8/18) | KT17 | Página da turma 68632 | A turma é a única presencial do recorte. |
| 68632-K4 | especialização em cirurgia de cães e gatos | matricular | Baixo | 52 (26/8/18) | sec. A4 | Página da turma 68632 (`sobre`) | |
| 68632-K5 | pós em cirurgia veterinária | matricular | Alto | 54 (26/20/8) | K4.3 | Página da turma 68632 (`sobre`) | Cabeça de termo; fora das sementes pagas por desenho. |
| 68632-K6 | pós em clínica cirúrgica vet | matricular | Baixo | 50 (24/8/18) | K4.7 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68632-K7 | quanto custa pós em clínica cirúrgica de cães e gatos | resolver | Médio | 52 (22/14/16) | K4.8 | Página da turma 68632 (`investimento`, dado) | Número só do dado. |
| 68632-K8 | pós em cirurgia veterinária presencial | comparar | Médio | 46 (14/14/18) | K4.12 | Guia de decisão A4 (formato) | A resposta honesta é "presencial em Goiânia"; nunca "semipresencial". |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| pós em clínica cirúrgica semipresencial; pós em clínica cirúrgica São Paulo | sem alvo nesta página (665 está à venda) | A paga de 68632 nega "semipresencial" e "são paulo"; seção 5. |
| ortopedia veterinária, osteossíntese | 662 (em espera, OU18) | A paga nega "ortopedia"; o módulo de ortopedia da ficha é conteúdo. |
| videocirurgia | página de 578 (maio) | A paga nega "videocirurgia"; o módulo de videocirurgia e endoscopia é conteúdo. |
| neurocirurgia | página de 68616 (maio) | O módulo de neurocirurgia é conteúdo. |
| fisioterapia, reabilitação | página de 366 | Seção 4. |
| anestesia, analgesia perioperatória | páginas de 68609, 657 e 359 | "Cuidados perioperatórios" é conteúdo. |
| imersão em cirurgia veterinária (inclusive a de Goiânia), castração de cães e gatos, mini curso de cirurgia | Cursos Livres (99, 433, 625 e 469), só por link | Não misturar linhas. |
| título de especialista em cirurgia; pós EAD; residência | sem página (ou guia A4) | Pago nega EAD e residência; título é T6. |
| prova de bolsa de clínica cirúrgica (68643 e 68644) | sem página nesta onda | Decisão 14; o bloco "PROVA DE BOLSA" da ficha sai no OC1. |

**Disputa E20:** 535 (mesma oferta) e 665 (outro campus e outra modalidade). Regra na seção 5.

### 7.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68632-Q1 | Tem pós presencial em clínica cirúrgica de cães e gatos em Goiânia? Como funciona? | Solução | matricular | 56 (30/8/18) | Q4.1 | `resposta_citavel` e `faq` de 68632; `local_e_datas` (dado) | O texto da IA não cita Goiânia (CP1); o campus aparece no dado e no JSON-LD. Resposta de 40 a 60 palavras. |
| 68632-Q2 | Pós em clínica cirúrgica presencial em Goiânia: preciso morar na cidade? Quantos fins de semana por mês? | Problema | resolver | 52 (26/8/18) | Q4.2 | `faq` e `local_e_datas` (dado) | Frequência, jornada e hospedagem [CONFIRMAR NO CATÁLOGO]. O cronograma da ficha traz um módulo por mês, em dois dias; horário não consta. |
| 68632-Q3 | Que cirurgias a pós em clínica cirúrgica de cães e gatos ensina? Tem neurocirurgia, cirurgia cardiovascular e videocirurgia? | Problema | aprender | 38 (8/8/22) | nova | `sobre` e `matriz` (dado) | Lista de temas com "entre eles" (E4); os módulos vêm da ficha. A pergunta cita videocirurgia e neurocirurgia como conteúdo, sem tomar o termo de 578 e de 68616. |
| 68632-Q4 | Pós em clínica cirúrgica: presencial em Goiânia ou semipresencial em São Paulo? Qual a diferença? | Comparação | comparar | 46 (16/8/22) | nova | Guia de decisão A4; `faq` de 68632 liga ao guia | Responde só pela turma aberta (presencial, Goiânia). Sem turma aberta em São Paulo no catálogo: a parte de São Paulo vai para "vou confirmar com o time" [CONFIRMAR]. Sem comparar valor nem nomear concorrente. |
| 68632-Q5 | Quem pode fazer a pós em clínica cirúrgica de cães e gatos? Preciso já operar? | Problema | resolver | 46 (22/8/16) | nova | `para_quem` e `faq` | A ficha diz só "Médicos Veterinários" (a de 665 diz outro público e não vale para 68632); experiência prévia não está escrita [CONFIRMAR NO CATÁLOGO]. |
| 68632-QC1 | Quanto custa a pós em clínica cirúrgica de cães e gatos da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 68632-QC2 | Dá para entrar na pós em clínica cirúrgica de cães e gatos depois que a turma já começou? | Decisão | resolver | 46 (26/8/12) | nova | `faq` (dado da turma, OU14) | **Bloqueada até OU3** (módulo 1 presencial; F baixo porque a página não pode responder). Enquanto isso, a resposta "Ainda dá tempo?" diz só a data de início e o link, sem a regra e sem a data do 3º módulo (E22). |
| 68632-QC3 | E se a turma da pós em clínica cirúrgica de cães e gatos não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel e a regra de reembolso de inscrição. |

---

## 8. Seção 68635: Pós-graduação em Clínica Médica e Emergência de Pequenos Animais (turma V)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 750 h, turma V, status aberto, início 10/04/2027. Dia do 3º módulo [CONFIRMAR NO CATÁLOGO] (E18). **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 28 módulos; sem campo de vagas; 9 presenciais: módulo 3 (semiologia e patologia clínica), 6 (anatomia cardiovascular, interpretação do eletrocardiograma, análise de hemogasometria), 10 (semiologia neurológica e respiratória, sondagem uretral de macho e fêmea), 14 (raspado de pele e análise, testes alergênicos), 18 (ambulatório clínico), 21 (exame clínico oral e odontógramas, tratamento periodontal), 24 (triagem e monitoração do paciente grave), 25 (A-FAST e T-FAST, atendimento de felinos) e 28 (reanimação cardiopulmonar, trauma, atendimento clínico). Os 19 demais são online. Os módulos cobrem sistemas (cardiovascular, nefrologia, neurologia, pneumologia, gastroenterologia, infectologia, dermatologia, endocrinologia, oftalmologia, hematologia, oncologia, odontologia, felinos, imagem) e emergência (urgência, UTI e internação). A ficha divide a carga em dois certificados de metade da carga horária cada e fala em "duas certificações aprovadas pelo MEC": nada disso entra em termo ou pergunta (OU35, OC1).

**O que a busca na web mostrou (27/10):** as páginas de "Clínica Médica de Pequenos Animais" do Guia da Carreira (várias faculdades), com duração de até 18 meses, e o guia do Pravaler; nenhum resultado confirmou pós semipresencial que junte clínica médica e emergência. Sinal fraco de espaço aberto [SUPOSIÇÃO]. A cabeça "clínica médica de pequenos animais" tem muita oferta de agregador.

**Palavra principal:** pós-graduação em clínica médica e emergência de pequenos animais. **Página:** a página da turma 68635. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A3 (iscas-digitais v2) de apoio.

### 8.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68635-K0 | pós-graduação em clínica médica e emergência de pequenos animais | matricular | Baixo | 58 (28/8/22) | nova (nome do catálogo) | Página da turma 68635 (`hero`, `sobre`, `resposta_citavel`) | Principal. Igual à primeira semente paga. |
| 68635-K1 | pós em clínica médica de pequenos animais | matricular | Alto | 56 (28/20/8) | K3.3 | Página da turma 68635 (`sobre`) | Cabeça de termo; agregadores com EAD de parcela baixa. Fora das sementes pagas por desenho; o orgânico disputa por prática e carga horária. |
| 68635-K2 | pós em emergência veterinária | matricular | Médio | 54 (26/14/14) | K3.4 | Página da turma 68635 | Semente paga de 68635. O nome completo de terapia intensiva e emergência é de 68623 (seção 4). |
| 68635-K3 | pós em clínica médica de pequenos animais semipresencial | matricular | Baixo | 56 (28/8/20) | sec. A3 | Página da turma 68635 (`faq`, `sobre`) | A modalidade vem do dado. |
| 68635-K4 | pós em clínica médica e emergência São Paulo | matricular | Baixo | 54 (28/8/18) | nova | Página da turma 68635 (dado e JSON-LD) | Cidade fora do texto da IA (CP1). |
| 68635-K5 | especialização em clínica médica de cães e gatos | matricular | Baixo | 50 (26/8/16) | sec. A3 | Lista de palavras e grupo de anúncio | A ficha fala em pequenos animais e em medicina felina sem restringir a espécie: nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 68635-K6 | pós em clínica médica e emergência vet | matricular | Baixo | 48 (24/8/16) | nova (nome popular) | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68635-K7 | quanto custa pós em clínica médica e emergência de pequenos animais | resolver | Médio | 52 (22/14/16) | K3.6 (adaptada) | Página da turma 68635 (`investimento`, dado) | Número só do dado. |
| 68635-K8 | pós de 750 horas vale a pena | resolver | Baixo | 42 (16/8/18) | K3.7 | Bloco `numeros` (dado) e guia A3 | O número não entra em texto de página (E1); a distribuição de horas por área [CONFIRMAR NO CATÁLOGO]. |
| 68635-K9 | A-FAST e T-FAST em cães e gatos | aprender | Baixo | 34 (6/8/20) | nova (módulo 25) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Conteúdo de autoridade; no limite do corte. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| terapia intensiva, UTI veterinária, pós em terapia intensiva e emergência veterinária | página de 68623 (maio) | A paga de 68635 nega "terapia intensiva". Os módulos de UTI e internação são conteúdo. |
| pós em Goiânia | 68623 e 289 | A paga nega "goiânia" e "goiás". |
| pós em cardiologia, neurologia, nefrologia, dermatologia, oncologia, endocrinologia, hematologia, infectologia, odontologia, oftalmologia | páginas de cada área | Cada sistema é módulo da ficha; nenhum entra em título nem em palavra-chave de 68635. |
| medicina de felinos (pós) | sem alvo (650 em verificar) | Módulos de medicina felina e de atendimento de felinos são conteúdo. |
| ultrassom point-of-care, urgência e emergência (curso) | Cursos Livres (68638 e 539), só por link | Não misturar linhas. |
| grupo de estudos em clínica médica e emergência (68666); aprimoramento em clínica médica (137) | Cursos Livres, só por link | Idem. |
| internação veterinária (610, 614 e 615) | sem alvo | Sem venda. |
| "dupla certificação", certificação por área, título de especialista | sem página | OU35 e OC1; E rules. |
| pós EAD; prova de bolsa de clínica médica e emergência (68645) | sem página | Pago nega EAD; decisão 14. |

**Disputa E20:** 663 (mesma oferta em outra data). Regra na seção 5.

### 8.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68635-Q1 | Existe pós semipresencial em clínica médica e emergência de pequenos animais em São Paulo? Como funciona? | Solução | matricular | 56 (28/8/20) | nova | `resposta_citavel` e `faq` de 68635; `local_e_datas` (dado) | Resposta sem número, local nem data. |
| 68635-Q2 | Dá para fazer a pós em clínica médica e emergência de pequenos animais trabalhando em plantão? | Problema | resolver | 48 (22/14/12) | Q3.3 (adaptada) | `faq` e `local_e_datas` (dado) | Reposição de módulo perdido [CONFIRMAR OU3]. |
| 68635-Q3 | Qual a diferença entre pós em clínica médica e emergência e pós em terapia intensiva veterinária? | Comparação | comparar | 46 (16/8/22) | Q3.1 | Guia de decisão A3; `faq` de 68635 liga ao guia | Diz em que cada uma é centrada, sem dizer qual é melhor (E11). |
| 68635-Q4 | A pós em clínica médica e emergência de pequenos animais tem prática de eletrocardiograma, A-FAST e T-FAST? | Decisão | resolver | 50 (24/8/18) | nova | `matriz` (dado) e `faq` | A ficha põe a interpretação do eletrocardiograma no módulo 6 e o A-FAST e T-FAST no módulo 25, os dois presenciais. Não generalizar para os 9 presenciais (E5). |
| 68635-Q5 | Vale a pena uma pós de 750 horas? Por que ela tem mais módulos que as outras? | Decisão | resolver | 42 (16/8/18) | Q3.5 | Bloco `numeros` (dado) e `faq` | Sem número no texto (E1). Distribuição de horas [CONFIRMAR NO CATÁLOGO]. |
| 68635-QC1 | Quanto custa a pós em clínica médica e emergência de pequenos animais da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 68635-QC2 | Dá para entrar na pós em clínica médica e emergência de pequenos animais depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; sem o mês do 3º módulo (E18); depois do início só com o dia [CONFIRMAR OU25]. |
| 68635-QC3 | E se a turma da pós em clínica médica e emergência de pequenos animais não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número (a ficha não traz campo de vagas); a ficha traz o aviso de passagem e hotel. |

---

## 9. Seção 366: Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária (turma I)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, turma I, status aberto, início 10/04/2027 pela planilha; o site e o cronograma da ficha mostram 24/04/2027 [CONFIRMAR OU20, P4]. Dia do 3º módulo [CONFIRMAR NO CATÁLOGO] (E18). **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 24 módulos; coordenação "UFAPE" (OU34: nenhum termo cita coordenação); 9 presenciais: módulo 3 (biomecânica aplicada a lesões locomotoras, órteses e próteses), 6 (prática de hidroterapia, cinesioterapia e avaliação de dor), 9 (prática de recursos eletrofísicos), 12 (prática de avaliação e reabilitação neurológica), 15 (prática de avaliação e reabilitação ortopédica), 18 (prática de bandagem taping e reabilitação em felinos e silvestres), 20 (avaliação respiratória e avaliação fisiátrica do paciente à beira-leito), 21 (prática de terapias manuais e paciente à beira-leito) e 24 (prática de atendimento clínico). **Os módulos 3 e 20 não dizem "prática" na ficha**: nenhum termo ou pergunta afirma que todos os presenciais são práticas (E5). Os 15 demais são online. O texto da ficha fala em animais de grande e pequeno porte, e os módulos trazem felinos, silvestres e cavalo atleta: "de cães e gatos" não está na ficha. O CEP da ficha (01428-001) difere do das outras páginas de São Paulo (OU20). A ficha cita uma resolução de conselho de classe sobre fisioterapia animal e a atuação com o conselho de fisioterapia: afirmação normativa que vai para a regulação, não vira termo nem pergunta de página [REVISÃO REGULAÇÃO].

**O que a busca na web mostrou (27/10):** o Quero Bolsa tem página "Fisioterapia Veterinária"; o EAD.com.br lista "Reabilitação e Fisioterapia de Cães e Gatos" com oferta indisponível na consulta; um site de cursos descreve a pós de fisioterapia veterinária com acesso por graduação em medicina veterinária ou área da saúde correlata; o resto são perfis acadêmicos. Nenhuma especialização lato sensu presencial ou semipresencial em destaque, nenhuma página da Ufape. Sinal de espaço aberto em reabilitação [SUPOSIÇÃO]. Curso novo (turma I), com a data em divergência.

**Palavra principal:** pós-graduação em fisioterapia veterinária. **Alvo realista de curto prazo:** pós em reabilitação veterinária (366-K1). O nome da página não muda (E2). **Página:** a página da turma 366. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A4 (iscas-digitais v2) de apoio.

### 9.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 366-K0 | pós-graduação em fisioterapia veterinária | matricular | Médio | 52 (26/14/12) | K4.6 | Página da turma 366 (`hero`, `sobre`, `resposta_citavel`) | Principal. Igual à primeira semente paga. |
| 366-K1 | pós em reabilitação veterinária | matricular | Médio | 52 (26/14/12) | K4.6 | Página da turma 366 (`sobre`) | Semente paga. |
| 366-K2 | pós em fisiatria veterinária | matricular | Baixo | 50 (26/8/16) | sec. A4 | Página da turma 366 (`sobre`) | Semente paga; a palavra faz parte do nome do curso. |
| 366-K3 | pós-graduação em fisioterapia, fisiatria e reabilitação veterinária semipresencial | matricular | Baixo | 52 (26/8/18) | nova | Página da turma 366 (`faq`) | Nome completo do catálogo com a modalidade. |
| 366-K4 | pós em fisioterapia veterinária São Paulo | matricular | Baixo | 52 (28/8/16) | nova | Página da turma 366 (dado e JSON-LD) | Cidade fora do texto da IA (CP1). |
| 366-K5 | pós em fisioterapia e reabilitação de cães e gatos | matricular | Baixo | 48 (24/8/16) | sec. A4 | Lista de palavras e grupo de anúncio | A ficha cita animais de grande e pequeno porte: nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 366-K6 | pós em fisioterapia animal | matricular | Médio | 46 (22/14/10) | nova | Lista de palavras e grupo de anúncio | Forma que a própria ficha usa ao falar da resolução; atrai também o público de fisioterapia humana. |
| 366-K7 | pós em fisio vet | matricular | Baixo | 46 (22/8/16) | nova (nome popular) | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 366-K8 | quanto custa pós em fisioterapia veterinária | resolver | Baixo | 48 (22/8/18) | nova | Página da turma 366 (`investimento`, dado) | Número só do dado. |
| 366-K9 | hidroterapia e cinesioterapia em cães: especialização | aprender | Baixo | 34 (6/8/20) | nova (módulos 5 e 6) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Apoio; no limite do corte. |
| 366-K10 | reabilitação neurológica e ortopédica em pequenos animais | aprender | Baixo | 36 (10/8/18) | nova (módulos 11 a 15) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Sem promessa de resultado clínico. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| ortopedia veterinária; osteossíntese; pós em ortopedia | 662 (em espera, OU18) | A paga de 366 nega "ortopedia"; os módulos de afecções ortopédicas e de reabilitação ortopédica são conteúdo. O termo fica reservado a 662. |
| clínica cirúrgica, cirurgia veterinária | página de 68632 | Seção 4. |
| videocirurgia | página de 578 (maio) | |
| neurologia veterinária (pós) | página de 68616 (maio) | Os módulos de neurologia e de reabilitação neurológica são conteúdo. |
| fisioterapeuta, fisioterapia humana, pós em fisioterapia para fisioterapeutas | sem página | A paga nega "fisioterapeuta"; o público da ficha é de médicos veterinários. Quem pode atuar depois do curso [REVISÃO REGULAÇÃO]; pergunta vai para o time. |
| resolução de conselho, registro profissional, "a área pertence à Medicina Veterinária" | nenhum termo | Frase normativa da ficha; vai à regulação (OC1). |
| medicina integrativa, acupuntura, cuidados paliativos (pós) | sem alvo | Os módulos 22 e 23 são conteúdo; 554 (Dor e Cuidados Paliativos) está em verificar. |
| reabilitação de cavalo atleta, fisioterapia equina | sem alvo | O módulo 17 cita o cavalo atleta como conteúdo; a pós equina é 341. |
| pós EAD; título de especialista; prova de bolsa | sem página | Pago nega EAD, título e bolsa. |

**Disputa E20:** nenhuma turma antiga de 366 (turma I).

### 9.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 366-Q1 | Existe pós de fisioterapia e reabilitação veterinária para médico veterinário? Quando começa a turma? | Solução | matricular | 52 (26/8/18) | Q4.5 | `resposta_citavel` e `faq` de 366; `local_e_datas` (dado) | A data vem do dado, nunca do texto da IA, e está em divergência [CONFIRMAR OU20]. [REVISÃO REGULAÇÃO] no trecho de atuação profissional. |
| 366-Q2 | Fisioterapeuta pode fazer a pós em reabilitação veterinária ou é só para médico veterinário? | Decisão | resolver | 46 (22/8/16) | nova | `para_quem` e `faq` | Pela ficha o público é de médicos veterinários. A resposta não fala de quem pode atuar depois; essa parte vai ao time e à regulação. Filtra o candidato que a paga já nega. |
| 366-Q3 | O que se estuda numa pós em fisioterapia veterinária? Tem hidroterapia, recursos eletrofísicos e terapias manuais? | Decisão | resolver | 50 (24/8/18) | nova | `sobre` e `matriz` (dado) | Os módulos 5, 6, 7 a 9, 19 e 21 da ficha. Temas com "entre eles" (E4); nenhum "todos os presenciais são práticos" (E5). |
| 366-Q4 | Pós em reabilitação veterinária é mais para ortopedia ou para neurologia? | Problema | aprender | 38 (8/8/22) | nova | `sobre` | A ficha tem reabilitação neurológica, ortopédica e respiratória; a pergunta não toma o termo de ortopedia (662). |
| 366-Q5 | Qual a diferença entre pós em fisioterapia e reabilitação veterinária, pós em ortopedia e pós em clínica cirúrgica? | Comparação | comparar | 44 (16/8/20) | nova | Guia de decisão A4; `faq` de 366 liga ao guia | Diz em que cada uma é centrada (E11); 662 só pelo nome, sem peça enquanto OU18 estiver aberta. |
| 366-QC1 | Quanto custa a pós em fisioterapia, fisiatria e reabilitação veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 366-QC2 | Dá para entrar na pós em fisioterapia e reabilitação veterinária depois que a turma já começou? | Decisão | resolver | 46 (26/8/12) | nova | `faq` (dado da turma, OU14) | **Bloqueada até OU20 e OU25** (data de início em divergência e 3º módulo sem dia): depois do início nenhuma peça sai sem o dia (E18). |
| 366-QC3 | E se a turma da pós em fisioterapia e reabilitação veterinária não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel. |

---

## 10. Seção 68628: Pós-graduação em Oncologia Veterinária (sem número de turma, P5)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, status aberto, início 10/04/2027. O número da turma diverge entre planilha e site (P5): nenhuma peça o cita. **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 24 módulos; 8 presenciais: módulo 5 (quimioterapia anti-neoplásica e conhecimento de biossegurança), 7 (eletroquimioterapia e crioterapia), 9 (cirurgia oncológica e reconstrutiva), 12 (melanoma e sarcoma felino; neoplasias cutâneas II), 15 (radioterapia com visita e discussão de casos clínicos), 17 (mastocitoma e discussão de casos clínicos), 20 (neoplasias do sistema urinário e discussão de casos clínicos) e 24 (nutrição do paciente oncológico, medicina integrativa e um item "Para definir - presencial"). Os 16 demais são online. Os módulos 21 e 22 repetem o mesmo conteúdo e o módulo 24 tem item "para definir" [CONFIRMAR NO CATÁLOGO antes de a `matriz` ficar visível]. A ficha não restringe a espécie (o módulo 23 trata de animais exóticos): "de pequenos animais" e "de cães e gatos" não estão na ficha. Coordenação e 36 professores listados; a coordenadora também aparece com outra grafia (OU30), sem uso aqui.

**O que a busca na web mostrou (27/10):** a PUCPR tem especialização semipresencial de oncologia veterinária em Curitiba; a Faculeste (MG) tem oncologia veterinária de pequenos animais em EAD; o Quero Bolsa tem página de oncologia veterinária; uma vaga de doutorado direto da USP apareceu (stricto sensu, outra intenção). Nenhuma oferta semipresencial de instituição sediada em São Paulo e nenhuma página da Ufape apareceram. Espaço aberto para "São Paulo" e "semipresencial" [SUPOSIÇÃO]; a cabeça de termo é disputada por EAD barato de agregador.

**Palavra principal:** pós-graduação em oncologia veterinária. **Alvo realista de curto prazo:** pós em oncologia veterinária de pequenos animais presencial em São Paulo (68628-K1), com a ressalva da modalidade. **Página:** a página da turma 68628. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A10 (iscas-digitais v2) de apoio.

### 10.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68628-K0 | pós-graduação em oncologia veterinária | matricular | Alto | 58 (28/20/10) | K10.1 | Página da turma 68628 (`hero`, `sobre`, `resposta_citavel`) | Principal; cabeça de termo. Igual à semente paga (frase e exata). |
| 68628-K1 | pós em oncologia veterinária de pequenos animais presencial em São Paulo | matricular | Médio | 60 (30/14/16) | K10.2 | Página da turma 68628 (dado e JSON-LD) | A turma é semipresencial: "presencial" só como o candidato digita, em lista e anúncio; a página diz semipresencial. "De pequenos animais" não está na ficha [CONFIRMAR NO CATÁLOGO]. |
| 68628-K2 | pós em oncologia veterinária São Paulo | matricular | Médio | 56 (28/14/14) | sec. A10 | Página da turma 68628 (dado e JSON-LD) | Semente paga; cidade fora do texto da IA (CP1). |
| 68628-K3 | pós em oncologia veterinária semipresencial | matricular | Médio | 56 (28/14/14) | nova | Página da turma 68628 (`faq`, `sobre`) | Os agregadores mostram a área sobretudo em EAD; espaço para semipresencial [SUPOSIÇÃO]. |
| 68628-K4 | especialização em oncologia de cães e gatos | matricular | Baixo | 52 (26/8/18) | sec. A10 | Lista de palavras e grupo de anúncio | Semente paga; nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 68628-K5 | pós em onco vet | matricular | Baixo | 50 (24/8/18) | K10.3 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68628-K6 | quanto custa pós em oncologia veterinária | resolver | Médio | 52 (22/14/16) | K10.4 | Página da turma 68628 (`investimento`, dado) | Número só do dado; a objeção de preço é forte, a frase de apoio não compara valor. |
| 68628-K7 | pós em oncologia veterinária duração e carga horária | resolver | Médio | 50 (20/14/16) | K10.8 | Bloco `numeros` (dado) | A duração e a carga vêm do dado; a IA não escreve número. |
| 68628-K8 | biossegurança em quimioterapia veterinária | aprender | Médio | 32 (6/14/12) | K10.10 | Artigo de apoio [REVISÃO DOCENTE] e `matriz` | Dúvida da persona; no limite do corte. O módulo 5 trata de biossegurança. |
| 68628-K9 | oncologia veterinária vale a pena como especialização | aprender | Médio | 38 (10/14/14) | K10.11 | Artigo de apoio | Sem promessa de renda ou emprego. |
| 68628-K10 | imunoterapia e terapia alvo em oncologia veterinária | aprender | Baixo | 34 (6/8/20) | nova (módulo 6) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Conteúdo de autoridade. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| curso de eletroquimioterapia | Cursos Livres (560), só por link | A paga nega as duas exatas; o módulo 7 da ficha fica como conteúdo. |
| mini curso em oncologia na clínica médica (465) | Cursos Livres, só por link | Não misturar linhas. |
| citologia, citopatologia | página de 333 (onda 2) | |
| hematologia, linfomas e leucemias como curso | página de 68608 (onda 1) | Os módulos 13 e 14 são conteúdo. |
| cirurgia oncológica (pós) | página de 68632 (cabeça "cirurgia") | O módulo 9 é conteúdo. |
| radioterapia veterinária (centro ou curso) | sem página | O módulo 15 cita a visita; sem promessa. |
| cuidados paliativos, dor (pós) | sem alvo (554 em verificar) | Os módulos 21 e 22 são conteúdo. |
| pós em oncologia EAD; residência; mestrado e doutorado | sem página | Pago nega EAD, residência, mestrado e doutorado. |
| prova de bolsa de oncologia (68657); título de especialista | sem página nesta onda | Decisão 14; título é T6. |

**Disputa E20:** 654 (mesma oferta em outra data, sem venda). Regra na seção 5.

### 10.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68628-Q1 | Existe pós em oncologia veterinária semipresencial em São Paulo? Como funcionam os módulos presenciais? | Solução | matricular | 56 (30/14/12) | Q10.1 | `resposta_citavel` e `faq` de 68628; `local_e_datas` (dado) | Resposta sem número, local nem data. A página diz semipresencial. |
| 68628-Q2 | Preciso de estrutura especial na clínica para fazer quimioterapia depois da pós? | Problema | aprender | 36 (10/8/18) | Q10.2 | Artigo de apoio [REVISÃO DOCENTE] | O módulo 5 trata de quimioterapia e biossegurança; a pergunta não vira promessa de "montar serviço". |
| 68628-Q3 | Pós em oncologia ou curso de eletroquimioterapia: qual faço primeiro? | Comparação | comparar | 44 (16/8/20) | Q10.4 | Guia de decisão A10, com link para o curso livre 560 | Livres entra só por link; diz em que cada um é centrado, sem dizer qual é melhor. |
| 68628-Q4 | O que se estuda numa pós em oncologia veterinária? Tem quimioterapia, cirurgia oncológica e radioterapia na prática? | Decisão | resolver | 50 (24/8/18) | nova | `sobre` e `matriz` (dado) | Quimioterapia (módulo 5) e cirurgia oncológica (módulo 9) são presenciais; radioterapia aparece no módulo 15 como "visita" com discussão de casos. Não generalizar os 8 presenciais (E5). |
| 68628-Q5 | Pós em oncologia veterinária serve para clínico geral ou só para quem já atua em oncologia? | Problema | comparar | 44 (14/8/22) | nova | `para_quem` e `faq` | A ficha diz só "Médicos Veterinários"; nível de entrada [CONFIRMAR NO CATÁLOGO]. |
| 68628-QC1 | Quanto custa a pós em oncologia veterinária da Ufape e dá para parcelar? | Decisão | resolver | 56 (24/14/18) | Q10.5 | `investimento` (dado) | Número só do dado. |
| 68628-QC2 | Dá para entrar na pós em oncologia veterinária depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; o dia do 3º módulo está na ficha (módulo 3 online), liberado como dado da turma depois de OU14. |
| 68628-QC3 | E se a turma da pós em oncologia veterinária não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel e o reembolso de inscrição. |

---

## 11. Seção 68617: Pós-graduação em Endocrinologia de Pequenos Animais (sem número de turma, P5)

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, status aberto, início 17/04/2027. O número da turma diverge entre planilha e site (P5): nenhuma peça o cita. **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 24 módulos; **só 2 presenciais**: módulo 12 (aula prática de atendimento endocrinológico, aula prática de anatomia do sistema endócrino e discussão de casos clínicos) e módulo 23 (aulas práticas de atendimento endócrino, ultrassonografia abdominal e cirurgia do sistema endócrino, e discussão de casos dos alunos). Os 22 demais são online: nenhum termo, pergunta ou frase-ponte descreve a turma como "com muita prática presencial" ou "presencial". Temas: fisiologia endócrina, síndrome de Cushing em cães, hipoadrenocorticismo, diabetes mellitus em cães e gatos e cetoacidose, hipotireoidismo canino e hipertireoidismo e hipotireoidismo felinos, distúrbios da calcemia, insulinoma, neoplasias adrenais, alopecia X, dislipidemias, doença renal crônica e função renal, emergências endócrinas, dosagens hormonais, imagem (ressonância, tomografia, cintilografia, ultrassonografia). O módulo 5 traz o item "Como montar seu TCC", mas a avaliação da ficha cita prova mensal e prova de recuperação, sem trabalho de conclusão: [CONFIRMAR NO CATÁLOGO] antes de qualquer peça falar de TCC. O módulo 17 aparece com data de fevereiro de 2028, fora da ordem (OU29). A URL da página termina em "/v/" (turma V).

**O que a busca na web mostrou (27/10):** os agregadores (Quero Bolsa, Guia da Carreira) listam, em várias faculdades (IBMR, Anhembi Morumbi, UniSul, FADERGS, UnP), a oferta com o nome **"Endocrinologia e Metabologia de Pequenos Animais"**; o resumo não trouxe a modalidade nem a carga. Esse é o nome de agregador, não o nome da turma da Ufape (E2): vira termo de lista e de anúncio. Nenhuma página da Ufape apareceu. Espaço aberto para "semipresencial" [SUPOSIÇÃO].

**Palavra principal:** pós-graduação em endocrinologia de pequenos animais. **Alvo realista de curto prazo:** pós em endocrinologia de pequenos animais semipresencial (68617-K1). **Página:** a página da turma 68617. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A7 (iscas-digitais v2) de apoio.

### 11.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68617-K0 | pós-graduação em endocrinologia de pequenos animais | matricular | Baixo | 56 (28/8/20) | nova (nome do catálogo) | Página da turma 68617 (`hero`, `sobre`, `resposta_citavel`) | Principal. Igual à primeira semente paga. |
| 68617-K1 | pós em endocrinologia de pequenos animais semipresencial | matricular | Baixo | 58 (30/8/20) | K7.2 | Página da turma 68617 (`faq`, `sobre`) | Semente paga. A modalidade vem do dado. |
| 68617-K2 | pós em endocrinologia veterinária | matricular | Médio | 56 (28/14/14) | K7.1 | Página da turma 68617 (`sobre`) | Semente paga; agregadores quase todos EAD. |
| 68617-K3 | especialização em endocrinologia de cães e gatos | matricular | Baixo | 50 (26/8/16) | sec. A7 | Lista de palavras e grupo de anúncio | Semente paga; a ficha cita cães e gatos nos módulos de diabetes e tireoide, mas não restringe a espécie: nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 68617-K4 | pós em endocrinologia e metabologia de pequenos animais | matricular | Médio | 50 (24/14/12) | nova (nome de agregador, web) | Lista de palavras e grupo de anúncio | Não é o nome do curso (E2); só lista e anúncio. |
| 68617-K5 | pós em endócrino vet | matricular | Baixo | 50 (24/8/18) | K7.3 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68617-K6 | quanto custa pós em endocrinologia veterinária | resolver | Médio | 52 (22/14/16) | K7.5 | Página da turma 68617 (`investimento`, dado) | Número só do dado. |
| 68617-K7 | diabetes e tireoide em cães e gatos pós | matricular | Baixo | 48 (26/8/14) | sec. A7 | Página da turma 68617 (`matriz`) e artigo de apoio | Termos de módulo da ficha; atende a quem digita pela doença. |
| 68617-K8 | endocrinologia veterinária vale a pena para clínico geral | aprender | Médio | 38 (10/14/14) | K7.10 | Artigo de apoio | Sem promessa de renda. |
| 68617-K9 | doença renal crônica e diabetes mellitus em cães e gatos | aprender | Alto | 32 (4/20/8) | K7.12 | Artigos de apoio [REVISÃO DOCENTE] | No limite do corte; "doença renal crônica" é conteúdo, não toma o termo de nefrologia. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| nefrologia e urologia (pós) | 68612 (em verificar) e prova 68653 | A paga de 68617 nega "nefrologia"; os módulos de função renal e doença renal crônica são conteúdo. |
| geriatria veterinária | 699 (maio) | Sem alvo aqui. |
| dermatologia veterinária | página de 68610 (onda 1) | O módulo de alterações dermatológicas do endocrinopata é conteúdo. |
| nutrologia | 564 (em verificar) | O módulo de nutrição do paciente endocrinopata é conteúdo. |
| ultrassonografia, tomografia, ressonância (pós) | páginas de 68629 e 68604 | São módulos de apoio ao diagnóstico. |
| curso de diabetes, mini curso de endocrinologia, emergência endócrina (curso) | Cursos Livres (542, 458, 103 e 104), só por link | Não misturar linhas. |
| endocrinologia de silvestres | sem alvo | O módulo 22 cita o tema; sem página. |
| trabalho de conclusão, TCC de pós | sem alvo | Ver [CONFIRMAR] acima. |
| pós EAD; prova de bolsa de endocrinologia (68648); título de especialista | sem página | Pago nega EAD, bolsa e título; decisão 14. |

**Disputa E20:** nenhuma turma antiga de 68617 à venda. A pendência é a URL com "/v/" (pedido S6).

### 11.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68617-Q1 | Pós em endocrinologia de pequenos animais semipresencial em São Paulo, existe? | Solução | matricular | 56 (30/8/18) | Q7.1 | `resposta_citavel` e `faq` de 68617; `local_e_datas` (dado) | Resposta sem número, local nem data. |
| 68617-Q2 | Como funciona a pós em endocrinologia de pequenos animais: o que é online e o que é presencial? | Problema | resolver | 50 (24/8/18) | nova | `faq` e `local_e_datas` (dado) | A ficha tem 2 módulos presenciais, de atendimento, anatomia, ultrassonografia abdominal e cirurgia do sistema endócrino. A resposta não generaliza a prática. |
| 68617-Q3 | O que se estuda na pós em endocrinologia veterinária? Tem síndrome de Cushing, diabetes e tireoide? | Problema | aprender | 38 (8/8/22) | nova | `sobre` e `matriz` (dado) | Os módulos vêm da ficha. |
| 68617-Q4 | Endocrinologia veterinária vale a pena para clínico geral? | Problema | aprender | 38 (10/14/14) | Q7.3 | Artigo de apoio | Sem promessa de renda. |
| 68617-Q5 | Vale a pena a pós em endocrinologia veterinária ou um curso online mais curto? | Comparação | comparar | 44 (16/8/20) | nova | Guia de decisão A7, com link para os cursos livres 103 e 458 | Livres entra só por link; diz em que cada um é centrado, sem dizer qual é melhor. |
| 68617-QC1 | Quanto custa a pós em endocrinologia de pequenos animais da Ufape e como é o parcelamento? | Decisão | resolver | 56 (24/14/18) | Q7.6 | `investimento` (dado) | Número só do dado. |
| 68617-QC2 | Dá para entrar na pós em endocrinologia de pequenos animais depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; o dia do 3º módulo está na ficha; URL conferida antes do primeiro envio (OU29). |
| 68617-QC3 | E se a turma da pós em endocrinologia de pequenos animais não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel e o reembolso de inscrição. |

---

## 12. Seção 68636: Pós-graduação em Pneumologia Veterinária (turma VIII), data só no site

**Dados de apoio (catálogo, seção 2):** São Paulo, semipresencial, 500 h, turma VIII, status aberto, início 17/04/2027 **só no site** (fonte "só no site" no catálogo) [CONFIRMAR OU21, P3]. **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários"; 24 módulos; 6 presenciais, que a ficha define na legenda como "aulas práticas em São Paulo": módulo 4 (práticas em anatomia e semiologia do sistema respiratório), 7 (ultrassonografia pulmonar), 13 (laringotraqueobroncoscopia), 16 (rinoscopia), 19 (intervenções emergenciais no paciente respiratório) e 24 (atividades práticas). Os 18 demais são online (aulas teóricas a distância). Temas online: fisiologia respiratória, semiologia e farmacologia, radiologia, hemogasometria, síndrome do braquicefálico, interpretação de exames, doenças infecciosas, dirofilariose e circulação pulmonar, patologias em felinos e em cães, tomografia, ventilação mecânica, oncologia do trato respiratório, toracoscopia, doenças pleurais, tromboembolismo pulmonar, discussão de casos e sedação do pneumopata. A ficha não traz a frase de aulas presenciais "não transmitidas" (as outras fichas trazem): nenhuma peça a usa. O módulo 16 aparece com "julho de 2027", o 24 com "março de 2028" e o 11 com um caractere solto, fora da ordem (CC do OC1). O texto da página fala em "vácuo", "escassez de especialistas" e "não é uma extensão da clínica geral. É uma especialidade": superlativo e comparação da ficha ficam fora (E14).

**O que a busca na web mostrou (27/10):** poucos resultados específicos de pneumologia veterinária; a maioria é de medicina humana (guias de pneumologia médica e programas de residência); um perfil acadêmico cita especialização em pneumologia veterinária em andamento por um instituto privado; a PUCPR tem pós de imagem veterinária (outra área). Nenhuma página da Ufape. Espaço aberto para o termo, com a ressalva de que a busca por "pneumologia" traz medicina humana [SUPOSIÇÃO].

**Palavra principal:** pós-graduação em pneumologia veterinária. **Página:** a página da turma 68636. **Tipo de página:** página da turma (tipo pos), com o guia de decisão A2 (iscas-digitais v2) de apoio, lado a lado com 289 e 352 (E11).

### 12.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68636-K0 | pós-graduação em pneumologia veterinária | matricular | Baixo | 54 (28/8/18) | K2.6 | Página da turma 68636 (`hero`, `sobre`, `resposta_citavel`) | Principal. Igual à semente paga (frase e exata). A página antiga 670 está fora do ar (seção 5). |
| 68636-K1 | pós em pneumologia veterinária São Paulo | matricular | Baixo | 54 (28/8/18) | sec. A2 | Página da turma 68636 (dado e JSON-LD) | Semente paga; cidade fora do texto da IA (CP1). |
| 68636-K2 | especialização em pneumologia de cães e gatos | matricular | Baixo | 50 (26/8/16) | sec. A2 | Lista de palavras e grupo de anúncio | Semente paga; a ficha traz patologias respiratórias em felinos e em cães, sem restringir a espécie: nunca em texto de página [CONFIRMAR NO CATÁLOGO]. |
| 68636-K3 | pós em pneumo vet | matricular | Baixo | 48 (24/8/16) | sec. A2 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68636-K4 | pós-graduação em pneumologia veterinária semipresencial | matricular | Baixo | 52 (26/8/18) | nova | Página da turma 68636 (`faq`, `sobre`) | A modalidade vem do dado. |
| 68636-K5 | quanto custa pós em pneumologia veterinária | resolver | Baixo | 48 (22/8/18) | nova | Página da turma 68636 (`investimento`, dado) | Número só do dado. |
| 68636-K6 | laringotraqueobroncoscopia e rinoscopia em cães e gatos | aprender | Baixo | 34 (6/8/20) | nova (módulos 13 e 16) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Conteúdo de autoridade; no limite do corte. |
| 68636-K7 | síndrome do braquicefálico: o que o clínico precisa saber | aprender | Médio | 36 (6/14/16) | nova (módulo 6) | Artigo de apoio [REVISÃO DOCENTE] | [SUPOSIÇÃO: tema frequente na clínica de pequenos animais; sem dado de volume]. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| cardiologia veterinária, ecocardiografia | páginas de 289 (onda 2) e 698 (onda 1) | A paga de 68636 nega "cardiologia". |
| ventilação mecânica (pós) | página de 352 (maio) | A paga nega "ventilação mecânica"; o módulo 15 é conteúdo. O curso livre (68618, 507) é de Cursos Livres. |
| terapia intensiva, emergência (pós) | páginas de 68623 e 68635 | O módulo de intervenções emergenciais é conteúdo. |
| diagnóstico por imagem, ultrassonografia, tomografia (pós) | páginas de 68604 e 68629 | Os módulos de radiologia, ultrassonografia pulmonar e tomografia são conteúdo. |
| hemogasometria (curso) | Cursos Livres (655 e 107), só por link | O módulo 5 é conteúdo. |
| pneumologia humana, pneumologista, residência em pneumologia | sem página | Resultados de medicina humana dominam a busca; ver sugestão 2 da seção 3. |
| "escassez de especialistas", "é uma especialidade", "vácuo" | nenhum termo | Superlativos e comparações da ficha (E14). |
| pós EAD; prova de bolsa de pneumologia (68659); título de especialista | sem página | Pago nega EAD, bolsa e título; decisão 14. |

**Disputa E20:** 670 (mesma oferta, encerrada). A planilha traz a data de 10/04/2027 na linha de 670 e nenhuma data na de 68636 [SUPOSIÇÃO: pode ser a mesma oferta renumerada; OU21]. Regra na seção 5.

### 12.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68636-Q1 | Existe pós em pneumologia veterinária em São Paulo? Quando começa a turma? | Solução | matricular | 54 (28/8/18) | nova (de K2.6) | `resposta_citavel` e `faq` de 68636; `local_e_datas` (dado) | A data vem do dado, nunca do texto da IA, e é [CONFIRMAR OU21]. |
| 68636-Q2 | O que se estuda numa pós em pneumologia veterinária? Tem broncoscopia, hemogasometria e ultrassom de pulmão? | Decisão | resolver | 50 (24/8/18) | nova | `sobre` e `matriz` (dado) | Laringotraqueobroncoscopia (módulo 13) e ultrassonografia pulmonar (módulo 7) são presenciais; hemogasometria (módulo 5) é online. Não generalizar os 6 presenciais (E5). |
| 68636-Q3 | Pneumologia veterinária é só para quem trabalha com UTI ou serve para clínico geral? | Problema | comparar | 44 (14/8/22) | nova | `para_quem` e `faq` | A ficha diz só "Médicos Veterinários"; nível de entrada [CONFIRMAR NO CATÁLOGO]. |
| 68636-Q4 | Qual a diferença entre pós em pneumologia veterinária, pós em cardiologia e pós em ventilação mecânica? | Comparação | comparar | 46 (16/8/22) | nova | Guia de decisão A2; `faq` de 68636 liga ao guia | Diz em que cada uma é centrada, sem dizer qual é melhor nem que uma cobre a outra (E11). |
| 68636-Q5 | Como funciona a pós em pneumologia veterinária semipresencial? Quais aulas são práticas? | Problema | resolver | 48 (22/8/18) | nova | `faq` e `local_e_datas` (dado) | A ficha define o presencial como "aulas práticas em São Paulo" e o online como teórico; o local aparece só no dado (CP1). |
| 68636-QC1 | Quanto custa a pós em pneumologia veterinária da Ufape e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 68636-QC2 | Dá para entrar na pós em pneumologia veterinária depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; o dia do 3º módulo está na ficha, mas a data de início só vale depois de OU21. |
| 68636-QC3 | E se a turma da pós em pneumologia veterinária não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel e o reembolso de inscrição. |

---

## 13. Seção 68609: Pós-graduação em Anestesiologia Veterinária (turma VIII), Goiânia

**Dados de apoio (catálogo, seção 2):** Goiânia, semipresencial, 500 h, turma VIII, status aberto, início 24/04/2027. **Ficha, conferida módulo a módulo:** público-alvo "Médicos Veterinários que querem atuar na anestesiologia veterinária clínica"; "26 módulos" nos dados principais, mas o cronograma lista 24 [CONFIRMAR NO CATÁLOGO]; 10 presenciais: módulo 5 (monitoração, avaliação pré-anestésica, medicação pré-anestésica, cálculos e manuseio de equipamentos, com hands-on de sedação), 8 (tira-dúvidas, intubação, manipulação de equipamentos, indução e anestesia geral inalatória), 11 (prática demonstrativa e hands-on de TIVA e anestesia alvo-controlada, ventilação mecânica aplicada, entre outros), 14 (prática de bloqueios locorregionais I e II, em modelos anatômicos), **16 e 17 (campanha de castração)**, **20 (anestesia em laparotomias e em procedimentos de imagem e videocirurgias; a ficha traz "aula prática demonstrativa em casos de rotina - online" e uma gravação liberada: parte online)**, 21 (reanimação cardiorrespiratória, procedimentos emergenciais, vias aéreas difíceis, acessos emergenciais e cuidados pós-parada), 23 (anestesia em exóticos e em felinos, prática demonstrativa e hands-on) e 24 (anestesia em pacientes especiais). Os demais são online, alguns "EAD síncrono" e alguns marcados "gravada" (módulos 1, 3 e 6, itens específicos): "gravada" vale só para os itens marcados (E3). O módulo 17 aparece com "fevereiro de 2028", fora da ordem [CONFIRMAR]. A ficha não traz a frase de aulas presenciais "não transmitidas" (as outras fichas trazem): nenhuma peça a usa. O H1 da página traz o plural "Anestesiologia Veterinárias" (OC1). A ficha cita "anestesia ... seja ele um cão, gata, cavalo, coelho, tartaruga": a turma não é de cães e gatos. O convite da prova de Especialista fica fora (E13).

**O que a busca na web mostrou (27/10):** nenhuma pós de anestesiologia veterinária semipresencial em Goiânia apareceu; surgiram o projeto pedagógico de uma pós semipresencial da UNAR (Araras, SP, 2026), páginas do Guia da Carreira sobre medicina veterinária em Goiânia (EAD e graduação) e o Quero Bolsa (oferta indisponível na consulta). Espaço aberto para a cauda de Goiânia [SUPOSIÇÃO]; a cabeça de termo é disputada por agregadores.

**Palavra principal:** pós-graduação em anestesiologia veterinária. **Alvo realista de curto prazo:** pós em anestesiologia veterinária em Goiânia (68609-K1). **Página:** a página da turma 68609, pilar de Anestesiologia (T3 da pesquisa de 26/10). **Tipo de página:** página da turma (tipo pos), com o guia de decisão A1 (iscas-digitais v2) de apoio, lado a lado com 657 e 359 (E11); o guia não diz quem pode entrar em 359.

### 13.1 Palavras-chave (tipo busca)

| ID | Termo | Intenção | Volume (qualit.) | Pontuação (M/D/F) | Origem | Atende | Observação |
|---|---|---|---|---|---|---|---|
| 68609-K0 | pós-graduação em anestesiologia veterinária | matricular | Alto | 58 (28/20/10) | K1.1 | Página da turma 68609 (`hero`, `sobre`, `resposta_citavel`) | Principal; cabeça de termo. Igual à semente paga. Três páginas do catálogo têm o mesmo nome (68607, 68609 e 664): seção 5. |
| 68609-K1 | pós em anestesiologia veterinária em Goiânia | matricular | Baixo | 60 (30/8/22) | K1.2 | Página da turma 68609 (dado e JSON-LD) | Melhor aposta da turma. Cidade fora do texto da IA (CP1). |
| 68609-K2 | pós-graduação em anestesiologia veterinária Goiânia | matricular | Baixo | 60 (30/8/22) | K1.2 (exata derivada) | Página da turma 68609 | Mesma página de 68609-K1. |
| 68609-K3 | especialização em anestesiologia de cães e gatos | matricular | Baixo | 52 (26/8/18) | sec. A1 | Lista de palavras e grupo de anúncio | Semente paga. **A ficha não restringe a espécie**: nunca em texto de página (E3) [CONFIRMAR NO CATÁLOGO]. |
| 68609-K4 | pós em anestesiologia veterinária semipresencial | matricular | Baixo | 54 (26/8/20) | nova | Página da turma 68609 (`faq`, `sobre`) | A modalidade vem do dado. |
| 68609-K5 | pós em anestesio vet; pós em anestesia veterinária | matricular | Baixo | 52 (26/8/18) | K1.5 | Lista de palavras e grupo de anúncio | Nunca em texto visível. |
| 68609-K6 | quanto custa pós em anestesiologia veterinária | resolver | Médio | 52 (22/14/16) | K1.6 | Página da turma 68609 (`investimento`, dado) | Número só do dado. |
| 68609-K7 | pós em anestesiologia veterinária duração e carga horária | resolver | Baixo | 50 (22/8/20) | sec. A1 | Bloco `numeros` (dado) | A duração e a carga vêm do dado; a IA não escreve número. |
| 68609-K8 | anestesia em felinos e animais exóticos: especialização | aprender | Baixo | 34 (6/8/20) | nova (módulos 22 e 23) | `matriz` e artigo de apoio [REVISÃO DOCENTE] | Conteúdo de autoridade. A pós de Cursos Livres sobre anestesia felina é 616 (só link). |
| 68609-K9 | avaliação e tratamento da dor em cães e gatos pós-graduação | aprender | Médio | 32 (6/14/12) | K1.12 | Artigo de apoio e link para 554 (sem compra) | No limite do corte; o módulo 7 trata de analgesia multimodal e escalas de dor. |
| 68609-K10 | pós em anestesiologia veterinária presencial em Goiânia | matricular | Baixo | 50 (26/8/16) | sec. A1 | Lista de palavras e grupo de anúncio | A turma é semipresencial (10 presenciais): a página diz semipresencial e nunca promete aulas todas presenciais. |

**Termos que não são desta página:**

| Termo | Fica com | Motivo |
|---|---|---|
| anestesiologia avançada | página de 657 (onda 2) | A paga de 68609 nega "avançada". |
| anestesiologia locorregional, bloqueios guiados por ultrassom | página de 359 (maio) | A paga nega "locorregional"; os módulos 12 a 14 da ficha são conteúdo. |
| pós em anestesiologia veterinária São Paulo | sem alvo nesta página (68607 à venda) | A paga nega "são paulo"; seção 5. |
| anestesiologia EAD, "Direto ao ponto" | sem página (586 em verificar) | Pago nega EAD; seção 5. |
| curso preparatório e prova de título de especialista em anestesiologia | Cursos Livres (488), só por link; título é T6 | O convite da ficha fica fora (E13). |
| grupo de estudo em anestesiologia (644), aprimoramento em anestesiologia (131), mini curso de anestesiologia na clínica médica (483), imersão em anestesia felina (616), cálculo de medicamentos em bolus (602) | Cursos Livres, só por link | Não misturar linhas. |
| ventilação mecânica aplicada à anestesia (curso) | Cursos Livres (68618, 507) e página de 352 | Os módulos 10 e 11 são conteúdo. |
| residência em anestesiologia | sem página | Pago nega residência; T5. |
| RECOVER, ROTEM, Xlung, VetPain | nenhum termo | Marcas e protocolos de terceiros dentro dos módulos: só no dado, nunca em termo, título ou pergunta. |
| prova de bolsa de anestesiologia (68639 e 68640) | sem página nesta onda | Decisão 14; o bloco "PROVA DE BOLSA" da ficha sai no OC1. |

**Disputa E20:** 68607 (outro campus), 664 (mesma oferta, sem venda) e 586 (produto diferente). Regra na seção 5.

### 13.2 Perguntas que o candidato faz a assistentes de IA (tipo IA)

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Origem | Atende (bloco) | Observação |
|---|---|---|---|---|---|---|---|
| 68609-Q1 | Qual pós em anestesiologia veterinária tem em Goiânia? É semipresencial? | Solução | matricular | 56 (28/14/14) | Q1.1 (sem "melhor") | `resposta_citavel` e `faq` de 68609; `local_e_datas` (dado) | O texto da IA não cita Goiânia (CP1); o campus aparece no dado e no JSON-LD. Resposta de 40 a 60 palavras. |
| 68609-Q2 | Preciso já ser anestesista para fazer a pós em anestesiologia veterinária ou serve para quem quer começar? | Decisão | resolver | 50 (24/8/18) | Q1.4 (adaptada) | `para_quem` e `faq` | A ficha diz "Médicos Veterinários que querem atuar na anestesiologia veterinária clínica", o que pode ser citado; experiência prévia exigida não está escrita [CONFIRMAR NO CATÁLOGO]. Não confundir com o pré-requisito de 359. |
| 68609-Q3 | Qual a diferença entre pós em anestesiologia veterinária, anestesiologia avançada e anestesiologia locorregional? | Comparação | comparar | 46 (16/8/22) | Q1.5 | Guia de decisão A1; `faq` de 68609 liga ao guia | Diz em que cada uma é centrada, sem dizer qual é melhor nem quem pode entrar em 359 (E11). |
| 68609-Q4 | O que se estuda na pós em anestesiologia veterinária? Tem hands-on, bloqueios e reanimação cardiorrespiratória? | Decisão | resolver | 50 (24/8/18) | nova | `sobre` e `matriz` (dado) | Hands-on nos módulos 5, 11 e 23; bloqueios no módulo 14 (modelos anatômicos); reanimação no módulo 21, todos presenciais. A pergunta cita bloqueios como conteúdo, sem tomar o termo de 359. |
| 68609-Q5 | Como funciona a pós semipresencial em anestesiologia veterinária em Goiânia? Quais módulos são presenciais? | Problema | resolver | 50 (22/8/20) | nova | `faq` e `local_e_datas` (dado) | Pela ficha são 10 presenciais, 2 deles de campanha de castração e 1 com parte online; a lista exata vem do dado. Itens "gravada" só os marcados. Reposição de módulo perdido [CONFIRMAR OU3]. |
| 68609-QC1 | Quanto custa a pós em anestesiologia veterinária da Ufape em Goiânia e como é o parcelamento? | Decisão | resolver | 50 (24/8/18) | nova (de QT3) | `investimento` (dado) | Número só do dado. |
| 68609-QC2 | Dá para entrar na pós em anestesiologia veterinária depois que a turma já começou? | Decisão | resolver | 56 (26/8/22) | nova | `faq` (dado da turma, OU14) | Regra da decisão 18 com a frase E7; o dia do 3º módulo está na ficha. |
| 68609-QC3 | E se a turma da pós em anestesiologia veterinária de Goiânia não fechar? | Decisão | resolver | 48 (22/8/18) | QT7 | `faq` | Turma mínima sem número; a ficha traz o aviso de passagem e hotel e o reembolso de inscrição. |

---

## 14. 662: registro de espera (OU18)

662 fica fora desta entrega: espera total até a Ufape responder OU18 (24/04/2027 é turma nova de Ortopedia ou o módulo 9 da turma IV, e qual é a ficha de 2027). Nenhuma palavra-chave nova foi escrita com a ficha de 2026. Dois efeitos neste arquivo: (a) o termo "ortopedia veterinária" fica **reservado** a 662; nem 68632 nem 366 o tomam, mesmo com módulos de ortopedia nas fichas (seção 4); (b) o guia A4 cita 662 só pelo nome. Quando OU18 chegar, o plano prevê ciclo extra; este agente entrega uma seção 662 em nova versão do arquivo.

---

## 15. As 10 palavras-chave e perguntas mais perto da matrícula (das 8 turmas)

Critério: intenção matricular ou resolver; ordem por pontuação, depois por M, depois por F; um item por conjunto de termos que levam à mesma página e à mesma intenção (K1 e K2 de 68632 e de 68609 contam juntos). Trava é o que impede ou limita o uso.

| # | ID | Termo ou pergunta | Tipo | Intenção | Pontuação | Página-alvo | Trava |
|---|---|---|---|---|---|---|---|
| 1 | 68632-K1 e K2 | pós em clínica cirúrgica presencial em Goiânia | busca | matricular | 60 (30/8/22) | 68632 | CP1 (cidade no texto); OU3 só para peça depois do início |
| 2 | 68609-K1 e K2 | pós em anestesiologia veterinária em Goiânia | busca | matricular | 60 (30/8/22) | 68609 | CP1 |
| 3 | 68628-K1 | pós em oncologia veterinária de pequenos animais presencial em São Paulo | busca | matricular | 60 (30/14/16) | 68628 | modalidade (a turma é semipresencial) e recorte de espécie [CONFIRMAR NO CATÁLOGO]: só lista e anúncio |
| 4 | 68617-K1 | pós em endocrinologia de pequenos animais semipresencial | busca | matricular | 58 (30/8/20) | 68617 | URL "/v/" (OU29) |
| 5 | 68635-K0 | pós-graduação em clínica médica e emergência de pequenos animais | busca | matricular | 58 (28/8/22) | 68635 | OU35 (frase de certificação da página no ar) |
| 6 | 68632-Q1 | Tem pós presencial em clínica cirúrgica de cães e gatos em Goiânia? Como funciona? | IA | matricular | 56 (30/8/18) | 68632 | CP1 |
| 7 | 68617-Q1 | Pós em endocrinologia de pequenos animais semipresencial em São Paulo, existe? | IA | matricular | 56 (30/8/18) | 68617 | nenhuma |
| 8 | 68628-Q1 | Existe pós em oncologia veterinária semipresencial em São Paulo? | IA | matricular | 56 (30/14/12) | 68628 | nenhuma |
| 9 | 68635-Q1 | Existe pós semipresencial em clínica médica e emergência de pequenos animais em São Paulo? | IA | matricular | 56 (28/8/20) | 68635 | nenhuma |
| 10 | 68609-Q1 | Qual pós em anestesiologia veterinária tem em Goiânia? É semipresencial? | IA | matricular | 56 (28/14/14) | 68609 | CP1 |

**Fora do top 10 por regra de desempate, mas de maior efeito na conversão depois do início:** "Dá para entrar na pós depois que a turma já começou?" (QC2), 56 (26/8/22) nas turmas em que a resposta está liberada (679, 68635, 68628, 68617, 68636 e 68609); em 68632 e 366 está bloqueada (OU3; OU20 e OU25). **679, 366 e 68636 ficam fora do top 10** por pontuação (a principal de cada uma é de cauda de nicho) e por trava de data (OU19, OU20 e OU21), não por falta de intenção.

---

## 16. Fontes consultadas na web (27/10/2026, WebSearch; nenhuma página aberta; resumos de busca)

- Infectologia: Quero Bolsa, Doenças Parasitárias e Infectologia em Cães e Gatos (https://querobolsa.com.br/cursos-e-faculdades/doencas-parasitarias-e-infectologia-em-caes-e-gatos/todos e https://querobolsa.com.br/cursos-e-faculdades/doencas-parasitarias-e-infectologia-em-caes-e-gatos/bolsas); Quero Bolsa, 9 especializações em medicina veterinária para fazer em 2025 (https://querobolsa.com.br/revista/9-especializacoes-em-medicina-veterinaria-para-fazer-em-2025); Guia da Carreira, tudo sobre especialização em medicina veterinária (https://www.guiadacarreira.com.br/blog/tudo-sobre-especializacao-em-medicina-veterinaria).
- Clínica cirúrgica: UNAR, projeto pedagógico de pós em cirurgia veterinária 2026 (https://www.unar.edu.br/wp-content/uploads/2026/04/PPC%20Pós%20Med%20Vet%20Cirurgia%202026.pdf); EducaMais Brasil, pós-graduação em clínica médica e cirúrgica (https://www.educamaisbrasil.com.br/cursos-e-faculdades/pos-graduacao-clinica-medica-e-cirurgica); Quero Bolsa, Clínica e Cirurgia de Pequenos Animais (https://querobolsa.com.br/cursos-e-faculdades/clinica-e-cirurgia-de-pequenos-animais); FAG, especialização em clínica médica e cirúrgica de cães e gatos (https://www.fag.edu.br/upload/arquivo/1759840833.pdf).
- Clínica médica e emergência: Guia da Carreira, Clínica Médica de Pequenos Animais (https://www.guiadacarreira.com.br/faculdades/anhembi-morumbi/cursos/clinica-medica-de-pequenos-animais e outras faculdades da mesma série); Pravaler, clínica de pequenos animais (https://www.pravaler.com.br/blog/profissoes/clinica-de-pequenos-animais/).
- Fisioterapia e reabilitação: Quero Bolsa, Fisioterapia Veterinária (https://querobolsa.com.br/cursos-e-faculdades/fisioterapia-veterinaria); EAD.com.br, Reabilitação e Fisioterapia de Cães e Gatos (https://www.ead.com.br/cursos-e-faculdades/reabilitacao-e-fisioterapia-de-caes-e-gatos/cursos).
- Oncologia: Quero Bolsa, Oncologia Veterinária (https://querobolsa.com.br/cursos-e-faculdades/oncologia-veterinaria); PUCPR, especialização em oncologia veterinária (https://estudenapuc.pucpr.br/pos-graduacao/wp-content/uploads/pdfs/pdf_502159.pdf); Faculeste, Oncologia Veterinária de Pequenos Animais (https://www.ead.com.br/faculdades/faculeste/cursos/oncologia-veterinaria-de-pequenos-animais/c0d0e46d-93d2-4c97-9d74-d2b4f1978ddd); Agência FAPESP, doutorado direto em oncologia veterinária na USP (https://agencia.fapesp.br/doutorado-direto-em-oncologia-veterinaria-na-usp-de-pirassununga/52497).
- Endocrinologia: Quero Bolsa, Endocrinologia e Metabologia de Pequenos Animais (https://querobolsa.com.br/cursos-e-faculdades/endocrinologia-e-metabologia-de-pequenos-animais); Guia da Carreira, UAM (https://www.guiadacarreira.com.br/faculdades/anhembi-morumbi/cursos/endocrinologia-e-metabologia-de-pequenos-animais) e UNISUL (https://www.guiadacarreira.com.br/faculdades/unisul-universidade-do-sul-de-santa-catarina/cursos/endocrinologia-e-metabologia-de-pequenos-animais); Quero Bolsa, IBMR (https://querobolsa.com.br/ibmr/cursos/endocrinologia-e-metabologia-de-pequenos-animais).
- Pneumologia: Quero Bolsa, Pneumologia e Ventilação Mecânica (https://querobolsa.com.br/cursos-e-faculdades/pneumologia-e-ventilcao-mecanica/bolsas); PUCPR, pós de diagnóstico por imagem (https://estudenapuc.pucpr.br/pos-graduacao/wp-content/uploads/pdfs/pdf_5525.pdf); Guia da Carreira, tudo sobre especialização em medicina veterinária (link acima).
- Anestesiologia: UNAR, projeto pedagógico de pós em Anestesiologia Veterinária 2026 (https://www.unar.edu.br/wp-content/uploads/2026/04/PPC%20Pós%20Med%20Vet%20Anestesio%202026.pdf); Quero Bolsa, Faculdades de Anestesiologia Veterinária (https://querobolsa.com.br/cursos-e-faculdades/anestesiologia-veterinaria/bolsas); Guia da Carreira, medicina veterinária em Goiânia (https://guiadacarreira.com.br/cursos-e-faculdades/goias--goiania/medicina-veterinaria).

---

## 17. Decisões pendentes que mudam este arquivo (resumo)

- **CP1 (template x termos de cidade):** o template proíbe local no texto da IA. Decidir com o cmo e a pessoa do marketing se `titulo_seo` e `resposta_citavel` podem receber a cidade por variável do dado. Para 68632 e 68609 (Goiânia) a cidade é o diferencial e, nos pares com 665 e 68607, é a única diferença real entre páginas de mesmo nome. Sem a CP1, a cauda de cidade depende do dado, do JSON-LD e dos guias.
- **CP2 (guias e artigos de apoio):** os guias de A1, A2, A3, A4, A7, A10 e A14 existem em iscas-digitais v2; os artigos de apoio marcados "[REVISÃO DOCENTE]" são encomenda de lacunas-de-conteudo e briefing-de-conteudo, fora do kit mínimo.
- **CP3 (regra de canonical e 301):** decisão do time do site e da pessoa do marketing sobre a seção 5, em especial para 535 e 663, cuja data limite já passou.
- **Próximo agente:** **lacunas-de-conteudo**, com as 8 turmas de abril, os artigos de apoio das seções 6 a 13 e os guias de decisão por área.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início e status das 8 turmas e das turmas antigas (535, 665, 663, 68607, 664, 586, 654, 670): contexto/catalogo-de-cursos.md, seção 2.
- Módulos, formato por módulo, presenciais, público-alvo, coordenação, avisos de passagem e hotel, reembolso, frases ligadas ao MEC e superlativos das 8 fichas, e o cronograma das turmas antigas até o 3º módulo: contexto/cursos/pos/ (fichas listadas no cabeçalho). Datas do 3º módulo das turmas antigas: 535 e 663 em 26 e 27/09/2026, 665 em 21 e 22/11/2026, 68607 em 19 e 20/12/2026.
- Padrão de nome "Pós-graduação em <área>", turma mínima de 15, matrícula até o 3º módulo (decisão 18), prova de bolsa fora desta onda (decisão 14) e proibição de frase de certificação: contexto/pos-graduacao.md e docs/execucao-2026-10-26.md.
- Regras E1 a E22, travas por turma, OU3, OU19 a OU21, OU25, OU29 a OU31, OU34 e OU35, e a lista de turmas antigas em disputa: saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md.
- Regras do texto da IA (sem número, preço, data, vaga, local nem nome de docente) e campo `palavra_chave_principal`: templates/pagina-da-turma.md.
- Sementes, negativas gerais, negativas por turma e janelas de extensão da Busca paga: saidas/11-midia-paga/anuncios-google-pos-2026-10-26.md (v6), seções 3, 6 e 7.
- Termos, notas e IDs reaproveitados (A14, K1.1, K1.2, K1.5, K1.6, K1.12, K2.6, K3.3, K3.4, K3.6, K3.7, K4.1, K4.2, K4.3, K4.6, K4.7, K4.8, K4.12, K7.1, K7.2, K7.3, K7.5, K7.10, K7.12, K10.1 a K10.4, K10.8, K10.10, K10.11, KT17, Q1.1, Q1.4, Q1.5, Q3.1, Q3.3, Q3.5, Q4.1, Q4.2, Q4.5, Q7.1, Q7.3, Q7.6, Q10.1, Q10.2, Q10.4, Q10.5, Q14.5, QT3, QT7): saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (v3).
- Formato, escalas e regra de vocabulário entre turmas: saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md; Q1 e Q55 da revisão: saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md.
- Resultados da busca na web (agregadores, projetos pedagógicos, ausência de oferta com os formatos citados nos resumos): seção 16.
- A ficha de 68609 e a de 68636 não trazem a frase de aulas presenciais "não transmitidas"; a ficha de 679 não traz o aviso de passagem e hotel nem a linha de reembolso; a ficha de 68617 traz o item "Como montar seu TCC" sem trabalho de conclusão na avaliação; a ficha de 68609 dá 26 módulos nos dados e lista 24 no cronograma: fichas em contexto/cursos/pos/.
- A conta 26 + 8 + 22 = 56 (QC2) contra "54" na onda 2: aritmética simples, seção 2.2.

## [SUPOSIÇÃO]

- Todo volume de busca (Alto, Médio, Baixo) é qualitativo, pelo critério da seção 2.2: quantidade de ofertas em agregadores e tipo do termo. Nenhuma exportação de ferramenta foi fornecida.
- Toda nota marcada "nova" é do agente pelo critério da seção 2.2; as reaproveitadas mantêm a nota de 26/10.
- A formulação exata das perguntas de IA e dos termos novos (o WebSearch não traz o preenchimento automático do Google).
- Espaço aberto para "presencial em Goiânia" (cirurgia), "semipresencial em Goiânia" (anestesiologia), "semipresencial em São Paulo" (oncologia), "semipresencial" (endocrinologia e pneumologia) e reabilitação (fisioterapia): a busca na web não é a página de resultados do Google e os resumos não trazem a modalidade de todas as ofertas.
- Demanda média para "síndrome do braquicefálico" (68636-K7), para "fisioterapia animal" (366-K6) e para "endocrinologia e metabologia" (68617-K4).
- A turma 670 pode ser a mesma oferta de 68636 renumerada (a data de 10/04/2027 está na linha de 670 na planilha).
- A proposta de canonical da página antiga para a nova enquanto a antiga vende (seção 5.2, regra 2) concentra autoridade na página que a Ufape quer vender; o custo é perder a busca da antiga nos dias finais.
- "Pós em parasitologia veterinária" não é curso da Ufape (a ficha de 679 tem um módulo de helmintos e protozoários).
- Sugestões de negativas ao gestor-de-midia (seção 3): mini curso, aprimoramento, grupo de estudos, congresso, medicina humana, pneumologista, crefito, fisioterapia humana, saúde pública, vigilância sanitária e vigilância epidemiológica.
- Corte de 32 pontos para virar alvo (regra prática da skill, não meta).
- "Pós em clínica médica e emergência" divide a palavra "emergência" com 68623: o termo genérico "pós em emergência veterinária" fica com 68635 por ser semente paga dela.

## [CONFIRMAR]

- **OU19:** data de 679 (03/04/2027) e correção da linha "Citopatologia 03/04" da visão de campanhas, que aponta para esta página (P3).
- **OU20:** início de 366 (10/04/2027 na planilha, 24/04/2027 no site e no cronograma) e coordenação ("UFAPE"); CEP.
- **OU21:** data de 68636 na planilha (só no site, 17/04/2027) e se a data de 10/04/2027 da linha de 670 é a mesma oferta.
- **OU3:** como se repõe o módulo 1 presencial de 68632. Bloqueia 68632-QC2 e qualquer peça de 68632 depois do início.
- **OU25 e OU14:** dia do 3º módulo de 679, 68635 e 366 (E18) e se a regra do 3º módulo pode entrar como dado da turma no FAQ (as perguntas QC2 dependem disso). **OU6:** leitura de "até o 3º módulo" (véspera ou dia).
- **OU29 e OU30:** turma e URL de 68617 ("/v/"); turma e coordenadora de 68628. **P5:** número de turma fora de peça.
- **OU31 e OU34:** "Dr. Rogério Vieira" e o convite da prova de Especialista de 68609; quem representa 68632 e 366.
- **OU35:** texto da regulação sobre a "dupla certificação" de 68635.
- **CP1:** se `titulo_seo` e `resposta_citavel` podem receber a cidade por variável do dado.
- **Regra de canonical e 301 (seção 5):** decisão do time do site e da pessoa do marketing; confirmar se a venda de 535 e de 663 terminou (3º módulo da ficha já passou); quem executa; destino de 665 e 68607 depois da data limite (página do curso ou próxima turma do mesmo campus).
- **Catálogo e ficha:** se "de cães e gatos" e "de pequenos animais" podem aparecer em texto de página nas turmas em que a ficha não restringe a espécie (679, 68635, 366, 68628, 68617, 68636 e 68609); nível de entrada e experiência prévia (679, 68635, 68628, 68636, 68609 e 68632); frequência, jornada e hospedagem de 68632; distribuição de horas de 68635; 26 ou 24 módulos de 68609 e a ordem do módulo 17; "TCC" em 68617; módulos 21, 22 e 24 de 68628; reembolso de 679.
- **Regulação:** quem pode atuar depois da pós de 366 e a frase normativa da ficha sobre o conselho de classe.
- **Volume de busca:** exportação do Planejador de Palavras-chave ou do Search Console, a pedir a quem executa a Busca paga (anuncios-google-pos, seção 6, já marca "volume e CPC [DADO NÃO FORNECIDO]").
- **Checagem em assistentes:** rodar as 64 perguntas (8 por turma) de 3 a 5 vezes por assistente e registrar a taxa (roteiro da seção 2.2); sem isso não há nota de visibilidade.
- **Sugestões de negativas pagas:** decisão do gestor-de-midia e do qa (seção 3).
- **Guias e artigos de apoio:** quem escreve e revisa o que está marcado "[REVISÃO DOCENTE]" (lacunas-de-conteudo e briefing-de-conteudo).
- **Onda 2:** corrigir a nota de QC2 (54 para 56) no arquivo da onda 2, se o orquestrador concordar.
- **U11 e OU4:** valor da inscrição (nenhuma peça cita) e vagas totais.
- **662 (OU18):** ficha de 2027 e se 24/04/2027 é turma nova.
