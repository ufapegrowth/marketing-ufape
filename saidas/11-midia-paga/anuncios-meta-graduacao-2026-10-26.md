# Estrutura de Meta Ads: Graduação 2027/1 (Medicina Veterinária em São Paulo e Pedagogia em Goiânia)

- Agente: anuncios-meta (departamento 11, Mídia Paga, sob o gestor-de-midia)
- Linha: graduacao
- Data: 26/10/2026 (conforme a encomenda); versão 2 em 27/10/2026, prazo 06/11/2026
- Versão: 2, corrige o qa-de-marketing de 27/10/2026 (itens M-1 a M-5) e aplica as recomendações R-M1 a R-M6 que são deste arquivo
- Workflow: /campanha-de-vestibular, etapa 5 (estrutura do canal Meta)
- Status: rascunho para aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Quem monta, revisa e aprova é um humano; aprovador nomeado: [CONFIRMAR, G14].
- Entradas lidas:
  - CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 17)
  - contexto/ufape-geral.md; contexto/graduacao.md; contexto/catalogo-de-cursos.md (seção 1); contexto/cursos/graduacao/editais-2027-1.md
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (G1 a G16)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12.7, D11 e D12)
  - saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (v3) e estrategia-de-midia-graduacao-2026-10-26.md (v3)
  - saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-d.md e qa-de-marketing-graduacao-2026-10-27-campanhas.md
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md; auditorias/11-midia-paga.md; auditorias/conformidade-educacional.md
- Não lidas: as fichas por curso (matriz); os nomes de disciplinas vêm do criativos-de-anuncio, que os marca [CONFIRMAR NO CATÁLOGO].
- Regra de fonte: preço, turno, duração, modalidade, carga horária e ato vêm do catálogo (seção 1); datas, vagas, ingresso e regras do desconto vêm da ficha dos editais; verba e metas vêm do plano de mídia v3 (decisões 15 e 16). Não existe exportação de plataforma, histórico de CPL nem número de CRM: nenhum desempenho é citado.

---

## Mudanças desta versão

| # | O que mudou | Onde | Motivo |
|---|---|---|---|
| 1 | Trava G7 (correção dos Editais 003/2026 e aprovação do texto do desconto pela regulação) incluída: nenhum anúncio com preço ou desconto sobe sem ela (v1-preco, v4-ato, p3-preco, p4-ato). Teste alternativo da fase 1 escrito | 0, 6, 6.4, 8, 10, AM2, AM3 | qa M-1 |
| 2 | Limite de gasto por campanha igual à soma das fases que ela cobre; campanha da fase 4 definida; limites R$ 1.440,00 (Medicina Veterinária), R$ 2.000,00 (Pedagogia) e R$ 3.440,00 na Meta, sem o Google; limite da conta deixa de ser trava | 2, 4, 8, AM9 | qa M-2 |
| 3 | Noturno: "metade da verba semanal da Meta do curso", sobe na segunda-feira seguinte a MP8 | 2.2, 3, 4, AM6 | qa M-3 |
| 4 | Regra de 25% a mais por dia marcada [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda da Meta] | 4, Lista 2 | qa M-4 |
| 5 | Datas do Enem como "informadas" com [CONFIRMAR no calendário oficial do Inep] | 8, 10 | qa M-5 |
| 6 | Título de v3, NOT-v3 e p5 até a semana E: "Enem de 2010 em diante" (a Meta e o Google seguem a mesma regra sobre "sua nota"); decisão final do cmo em AM12 | 6, AM12 | qa R-M1 |
| 7 | URL base com https://; data de término 21/02/2027 em cada campanha como segunda trava | 7, 8 | qa R-M2 e R-M3 |
| 8 | Posicionamentos: Audience Network e Messenger fora [SUPOSIÇÃO] | 5 | qa R-M4 |
| 9 | "Aprendizado limitado" com a fonte (gestor 3.5) e o [CONFIRMAR] dele | 6.4 | qa R-M5 |
| 10 | Abertura da fase 3 com a condição completa do Enem ("média mínima de 300 pontos, de 2010 em diante") | 6.1 | qa R-M6 |
| 11 | Ato regulatório: lido como "quando citar, como no catálogo"; pergunta ao cmo em AM12 | 6, AM12 | qa R-M7 |

---

## 0. Resumo (5 linhas)

1. Modelo: lançamento por fases, enxuto. Uma campanha e um conjunto por curso e turno, público amplo 18+, orçamento na campanha, no máximo 3 conceitos ativos. Objetivo Cadastros na LP, evento Lead; matrícula é só leitura.
2. Verba Meta (plano v3): Medicina Veterinária R$ 1.440,00, Pedagogia R$ 2.000,00, R$ 3.440,00 na Meta (o Google, R$ 560,00, é do anuncios-google). Pausa em 22/02/2027.
3. Só o integral pode subir (montagem em pausa de 11 a 13/11, ativação em 16/11) com MP1, MP2, MP4, MP10 e G13. Anúncio com preço ou desconto também exige G7 e G12; sem eles, sobe o teste alternativo (seção 6.4).
4. Noturno espera G8 e MP8; Pedagogia espera G6, MP4, MP1 e MP9.
5. Travas abertas: G6, G7, G8, G12, G13, G14, datas do Enem, público mínimo de remarketing, listas de contatos (MP7).

---

## 1. Modelo escolhido e motivo

- Lançamento por fases (captação, aquecimento, inscrições abertas, reta final), porque as aulas começam em 22/02/2027 e a mensagem muda por fase. Dentro da fase a lógica é enxuta: R$ 142,86 por semana por curso, em média, não sustentam teste e escala em campanhas separadas.
- Pedagogia: local (Goiânia), enxuta, 1 campanha e 1 conjunto.
- Orçamento na campanha, nunca no conjunto: com 1 conjunto por campanha, o orçamento de campanha dá o mesmo controle com um nível a menos e permite o limite de gasto da campanha como trava.
- Conjunto único e amplo. A diversidade de criativos faz o papel dos interesses. Sem interesses, sem semelhantes, sem listas de contatos.
- Metas (plano v3, aprovação pendente em MP1): custo por matrícula máximo R$ 133,33; CPL máximo base R$ 6,67 (conservador R$ 2,67; otimista R$ 13,33), com taxas de conversão [SUPOSIÇÃO de cenário]. Se o formulário da LP for a inscrição (G13), a meta vira custo por inscrito: R$ 16,67 no base.

---

## 2. Mapa em árvore e limite de gasto por campanha

Regra: o limite de gasto de cada campanha é a soma das verbas das fases que ela cobre, descontada a parte que for para o remarketing. Proposta de divisão do remarketing: até 20% da verba da fase da campanha ampla [SUPOSIÇÃO de desenho, decide o gestor-de-midia em AM5]. Toda campanha tem data de término 21/02/2027 como segunda trava (pausa em 22/02/2027).

### 2.1 Medicina Veterinária integral (pode subir em 16/11/2026)

| Campanha | Fases que cobre | Limite de gasto | Observação |
|---|---|---|---|
| grad_medvet-integral_meta_cadastro_amplo18_202611 | 1 e 2 (16/11 a 03/01/2027) | R$ 675,00 (R$ 450,00 + R$ 225,00), menos até R$ 45,00 se o remarketing _202612 existir | Conjunto: ..._202611__amplo18. Anúncios: v1-preco, v2-pratica, v3-entrada |
| grad_medvet-integral_meta_cadastro_amplo18_202701 | 3 e 4 (04/01 a 21/02/2027) | R$ 765,00 (R$ 525,00 + R$ 240,00), menos a parte dos remarketings _202701 (até R$ 105,00) e _202702 (até R$ 48,00) se existirem | Sobe em 04/01 e substitui a _202611. É a campanha da fase 4 quando não houver público de remarketing. Se o CPL da fase 3 passou do máximo, o gestor propõe pausá-la em 31/01 e os R$ 240,00 da fase 4 vão só para o remarketing _202702, se houver público; sem público, viram economia |
| grad_medvet-integral_meta_cadastro_rmk-lp30d_202612, _202701, _202702 | 2, 3 e 4 | partes acima | Só com o público de visitantes no mínimo da Meta [CONFIRMAR o valor vigente no gerenciador]. Conjunto: ..._rmk-lp30d__rmk-lp30d |

Soma dos limites do integral: R$ 675,00 + R$ 765,00 = R$ 1.440,00 enquanto o noturno estiver bloqueado.

### 2.2 Medicina Veterinária noturno (BLOQUEADO: G8 e MP4, depois MP8)

- grad_medvet-noturno_meta_cadastro_amplo18_AAAAMM (AAAAMM do mês do desbloqueio); conjunto ..._AAAAMM__amplo18; anúncios v1-preco, v2-noite, v3-entrada (v4-ato entra na fase 2).
- Verba: metade da verba semanal da Meta do curso (coluna "Integral, semana" da seção 4), a partir da segunda-feira seguinte a MP8. Até essa segunda-feira, o integral mantém a diária cheia da semana. Limite de gasto do noturno = soma das metades das semanas restantes; o limite do integral cai na mesma medida, por humano, no mesmo dia (AM6). O total do curso na Meta não passa de R$ 1.440,00.
- Remarketing do noturno: mesma regra do integral.

### 2.3 Pedagogia (BLOQUEADO: G6, MP4 e MP1, depois MP9)

- grad_pedagogia_meta_cadastro_goiania18_AAAAMM; conjunto ..._AAAAMM__goiania18; limite de gasto R$ 2.000,00, menos a parte do remarketing (até 20% da verba da fase em que existir), com a regra de entrada tardia da seção 4.
- grad_pedagogia_meta_cadastro_rmk-lp30d_AAAAMM: só com público mínimo.
- Anúncios (com G7 resolvido): p1-noite, p3-preco, p4-ato; p2-pratica na rotação; p5-entrada como conceito novo da fase 2.

### 2.4 Limite total

- Meta: R$ 1.440,00 (Medicina Veterinária) e R$ 2.000,00 (Pedagogia), somados pelos limites de campanha: R$ 3.440,00. O Google (R$ 560,00) tem limite próprio no anuncios-google e não entra nessa soma.
- O limite de gasto da conta não vale como trava da Graduação: a conta pode ter campanhas de outras linhas [CONFIRMAR]. A trava é por campanha.

Regra dos 3 conceitos: nunca mais de 3 conceitos ativos por curso e turno. Conceito novo (v4-ato, p5-entrada) entra no lugar do de pior resultado, só depois de 2 semanas de leitura, e nunca se desligam todos os antigos ao mesmo tempo. Cada conceito pode ter até 2 anúncios (formato principal e versão 9:16), porque a UTM muda por formato.

---

## 3. Campanhas: objetivo, evento, verba e leads por semana

| Item | Integral | Noturno | Pedagogia |
|---|---|---|---|
| Objetivo na Meta | Cadastros (ou Leads, conforme o nome atual no gerenciador) | idem | idem |
| Destino | Site: LP da Graduação, sem formulário instantâneo | idem | idem |
| Evento de otimização | Lead (evento padrão do pixel, disparado no envio do formulário da LP) [SUPOSIÇÃO]. Se a LP não disparar Lead, pedir ao responsável da plataforma antes de subir [CONFIRMAR, G13, MP10] | idem | idem |
| Matrícula | Conversão personalizada separada, só para leitura, nunca evento de otimização (volume baixo demais para aprender). Lida no CRM por utm_campaign e utm_content. Envio de matrícula à Meta por API de Conversões só depois de base legal e tratamento de menores validados (MP7, G10) | idem | idem |
| Janela de atribuição | Padrão da conta (7 dias de clique) [CONFIRMAR] | idem | idem |
| Verba Meta no ciclo | R$ 1.440,00 no curso | metade da verba semanal da Meta do curso, dentro dos R$ 1.440,00 | R$ 2.000,00 |
| Leads pela verba (base, CPL R$ 6,67) | 216 no ciclo; conservador 539; otimista 108 | em metade | 300; conservador 750; otimista 150 |
| Sobe em | 16/11/2026 | segunda-feira seguinte a MP8 | dia seguinte a MP9 |

Leads por semana são o que a verba compra se o CPL ficar exatamente no máximo. Não são previsão de resultado.

---

## 4. Verba por semana (R$, por campanha de Meta)

Verba diária da campanha = semanal / 7. Trava: limite de gasto por campanha (seção 2). A Meta pode gastar até 25% a mais num dia, mantendo a média da semana [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda da Meta]; o limite de campanha impede que o total passe do aprovado.

| Sem. | Datas | Integral, semana | Integral, diária | Leads base | Pedagogia, semana | Pedagogia, diária |
|---|---|---|---|---|---|---|
| S1 | 16 a 22/11/2026 | 150,00 | 21,43 | 22,5 | 200,00 | 28,57 |
| S2 | 23 a 29/11 | 150,00 | 21,43 | 22,5 | 200,00 | 28,57 |
| S3 | 30/11 a 06/12 | 150,00 | 21,43 | 22,5 | 200,00 | 28,57 |
| S4 | 07 a 13/12 | 67,50 | 9,64 | 10,1 | 90,00 | 12,86 |
| S5 | 14 a 20/12 | 67,50 | 9,64 | 10,1 | 90,00 | 12,86 |
| S6 | 21 a 27/12 | 45,00 | 6,43 | 6,8 | 60,00 | 8,57 |
| S7 | 28/12 a 03/01/2027 | 45,00 | 6,43 | 6,8 | 60,00 | 8,57 |
| S8 | 04 a 10/01 | 131,25 | 18,75 | 19,7 | 175,00 | 25,00 |
| S9 | 11 a 17/01 | 131,25 | 18,75 | 19,7 | 175,00 | 25,00 |
| S10 | 18 a 24/01 | 131,25 | 18,75 | 19,7 | 175,00 | 25,00 |
| S11 | 25 a 31/01 | 131,25 | 18,75 | 19,7 | 175,00 | 25,00 |
| S12 | 01 a 07/02 | 96,00 | 13,71 | 14,4 | 160,00 | 22,86 |
| S13 | 08 a 14/02 | 72,00 | 10,29 | 10,8 | 120,00 | 17,14 |
| S14 | 15 a 21/02 | 72,00 | 10,29 | 10,8 | 120,00 | 17,14 |
| Total | | 1.440,00 | | 216 | 2.000,00 | 300 |
| 22/02/2027 | Início das aulas | pausa | | | pausa | |

- Totais por fase (integral, Meta): R$ 450,00, R$ 225,00, R$ 525,00 e R$ 240,00. Pedagogia: R$ 600,00, R$ 300,00, R$ 700,00 e R$ 400,00.
- Noturno depois de MP8: a coluna "Integral, semana" é dividida 50% e 50% entre as duas campanhas a partir da segunda-feira seguinte. O total do curso na Meta não muda.
- Pedagogia desbloqueada depois de 16/11: semanas sem anúncio não são recuperadas de uma vez. A parte não gasta da fase 1 se divide pelas 7 semanas das fases 3 e 4 (até R$ 85,71 a mais por semana) e só é gasta se a campanha passar no critério de escalar; o resto vira economia.
- Pesos de Enem e Sisu (semana E e semana S) só entram com as datas oficiais confirmadas. O Sisu não aparece em nenhum texto.
- Realocação entre semanas, canais, turnos ou cursos segue a seção 6.2 do estrategia-de-midia e vira pedido de aprovação.

---

## 5. Conjuntos: público, localização, posicionamentos e exclusões

| Item | amplo18 (integral e noturno) | goiania18 (Pedagogia) | rmk-lp30d |
|---|---|---|---|
| Idade | mínimo 18 anos, sem teto. Conferir no gerenciador que o 18 é limite fixo e não sugestão [CONFIRMAR] | idem | idem |
| Gênero | todos | todos | todos |
| Localização | Grande São Paulo [SUPOSIÇÃO, área a confirmar com o comercial de SP] | Goiânia e região metropolitana [SUPOSIÇÃO, raio a confirmar com o comercial de Goiânia]. Raio pequeno demais encarece a entrega | a mesma do curso |
| Interesses e comportamentos | nenhum | nenhum (nada de "professor" ou "trabalha em escola") | nenhum |
| Público | amplo; Advantage+ audience sem sugestões de segmentação | idem | visitantes da LP do curso nos últimos 30 dias, só por pixel; só com o mínimo da Meta |
| Posicionamentos | automáticos, com Audience Network e Messenger desligados [SUPOSIÇÃO: não há criativo nem destino pensados para eles; CONFIRMAR no gerenciador]. Ficam feed, Stories, Reels e Explorar do Instagram e do Facebook. Criativos em 1:1 e 9:16; 4:5 opcional | idem | idem |
| Exclusões | quem disparou Lead nos últimos 180 dias (evento do pixel, sem lista); no noturno, visitantes que chegaram por anúncio do integral e o inverso [SUPOSIÇÃO de desenho] | quem disparou Lead nos últimos 180 dias | quem disparou Lead; cruzada entre turnos |
| Listas de contatos, semelhantes e importações | proibidos até validação jurídica (MP7, G10): a base pode ter menores | idem | idem |
| Categoria especial de anúncio | Educação não está entre as categorias especiais da Meta [CONFIRMAR no gerenciador]. Se a conta pedir, seguir a exigência | idem | idem |

Regras fixas: nenhuma segmentação ou exclusão por idade (além do piso de 18), gênero, renda, saúde, religião, origem ou emprego. Nenhum menor como público. A mensagem fala com "você e sua família" e lembra o aceite do representante legal.

---

## 6. Anúncios

Convenções:
- Nome do anúncio = utm_content, no padrão D12 com bloco de gancho (ajuste A-C1 do qa-d): `<conceito>_<formato>_<gancho>_vN`. Gancho a, b ou c (os ganchos B e C ficam em reserva no criativos, para iteração I1); N é a versão. Alinhar com o gestor-de-midia (AM10).
- Texto principal: o que aparece antes do "ver mais" (cerca de 125 caracteres) é a primeira frase; nos textos de preço ela já traz valor cheio, valor com desconto, percentual e validade. O complemento leva a regra completa. Limites: título cerca de 40 e descrição cerca de 30 caracteres [SUPOSIÇÃO do criativos, CONFIRMAR na plataforma]; o humano confere a contagem no gerenciador.
- Blocos (B-DESC-INT, B-ENTRADA, B-MENOR e os demais) estão na seção 2.1 do criativos-de-anuncio. A arte e o texto dentro do vídeo estão nas seções 2 e 3 do mesmo arquivo. Este arquivo não reescreve as peças.
- Entregável padrão: o texto principal, título, descrição e CTA aprovados no criativos são a versão A de cada conceito. As versões B e C (5 ângulos por conceito) ficam em reserva no criativos e entram só como iteração depois de um vencedor, por causa do limite de 3 conceitos e da verba.
- CTA: "Cadastre-se" nas campanhas de cadastro, porque o objetivo é cadastro; "Saiba mais" no remarketing e em v4-ato e p4-ato, porque quem já viu a página quer ler as condições.
- Ajustes do qa-d que entram na montagem: A-C3 (D.O.U. na arte 1:1 de v4-ato e p4-ato), A-C5 (R-I2, cena 1, linha "Média mínima de 300 pontos") e A-C2 (R-P1, cena 3, "de 2010 em diante"). São da peça e ficam com o criativos-de-anuncio; a montagem usa a arte já corrigida.
- Título do conceito de entrada (R-M1): até a semana E, "Enem de 2010 em diante" (22 caracteres) no lugar de "Use sua nota do Enem", porque o Google proíbe "sua nota" até a semana E e a regra deve ser uma só. O texto principal já traz "de 2010 em diante" e a média mínima. A decisão final é do cmo (AM12).
- Ato regulatório (R-M7): este arquivo lê "citar sempre o ato" como "quando citar, como no catálogo" [SUPOSIÇÃO de leitura]; hoje o ato vai em v4-ato e p4-ato. Se o cmo ler como "em toda peça", entra B-ATO-INT ou B-ATO-PED no complemento de todos os anúncios (AM12).
- Status por G7: v1-preco, v4-ato, p3-preco e p4-ato (e a troca de fase 2 com a regra do desconto) trazem preço ou desconto e ficam BLOQUEADOS até G7 (correção dos Editais 003/2026 e aprovação do texto pela regulação) e G12 (reajuste de dezembro). Os conceitos sem preço (v2, v3, p1, p2, p5) dependem das demais travas.

### 6.1 Integral (pronto para montagem depois do qa de 10/11 e da aprovação humana; preço só com G7)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| v1-preco (BLOQUEADO por G7 e G12) | v1-preco_feed-1x1_a_v1; v1-preco_stories-9x16_a_v1 | "De R$ 10.000,00 por R$ 5.000,00 por mês (50%) no 1º semestre de 2027: Medicina Veterinária integral na Faculdade UFAPE, em São Paulo." | B-DESC-INT, B-ENTRADA, B-MENOR; fecha com "Veja o edital e faça a inscrição gratuita pelo site." | 50% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| v2-pratica | v2-pratica_reels-9x16_a_v1 (vídeo R-I1); v2-pratica_feed-1x1_a_v1 | "No 1º semestre da matriz integral: Anatomia, Práticas Hospitalares e Projeto Extensionista I. Medicina Veterinária presencial na Faculdade UFAPE, em São Paulo." | "Integral, presencial, em 4 anos.", B-ENTRADA, B-MENOR. Sem preço | Prática desde o 1º semestre | Veterinária integral em SP | Cadastre-se |
| v3-entrada | v3-entrada_carrossel-1x1_a_v1; v3-entrada_stories-9x16_a_v1 (ou vídeo R-I2) | "Inscrição gratuita na Faculdade UFAPE. Use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Medicina Veterinária presencial em São Paulo. As aulas começam em 22/02/2027." | Enem de 2010 em diante | Média mínima de 300 pontos | Cadastre-se |
| v4-ato (fase 2; BLOQUEADO por G7 e G12) | v4-ato_carrossel-1x1_a_v1; v4-ato_stories-9x16_a_v1 | "Medicina Veterinária em São Paulo, na Faculdade UFAPE: veja o ato do curso, a inscrição gratuita, o desconto com regra e as condições de cancelamento." | B-ATO-INT, B-DESC-INT, B-COND, B-ENTRADA, B-MENOR | Antes de matricular, confira | Ato do curso e condições | Saiba mais |

Trocas de texto por fase (seção 2.6 do criativos; mesmo conceito, muda abertura, título e descrição; a regra completa fica no complemento):
- Fase 2, remarketing: abertura "A regra completa do desconto do 1º semestre de 2027."; título "Regras do desconto 2027/1"; descrição "Condições e validade no edital". Nome: v1-preco_feed-1x1_a_v2. Bloqueada por G7 e G12.
- Fase 3: abertura "Nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou redação online: veja como se inscrever." (R-M6, com a condição completa na linha visível); título "Nota do Enem ou redação"; descrição "Inscrição gratuita". A semana E ("Notas do Enem divulgadas...") só depois da data oficial confirmada.
- Fase 4: abertura "As aulas começam em 22/02/2027: veja os passos da matrícula."; título "Passos da matrícula"; complemento B-PASSOS, B-COND, B-MENOR. Sem contagem regressiva e sem "vagas".

### 6.2 Noturno (BLOQUEADO)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| v1-preco (também G7 e G12) | v1-preco_feed-1x1_a_v1; v1-preco_reels-9x16_a_v1 (R-N2) | "De R$ 10.000,00 por R$ 4.000,00 por mês (60%) no 1º semestre de 2027: Medicina Veterinária noturno, 5 anos, na Faculdade UFAPE, em São Paulo." | B-DESC-NOT, B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | 60% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| v2-noite | v2-noite_reels-9x16_a_v1 (R-N1); v2-noite_feed-1x1_a_v1 | "Faculdade UFAPE: Medicina Veterinária no período noturno, presencial, em São Paulo. O curso dura 5 anos. Inscrição gratuita." | "No 1º semestre da matriz noturna: Práticas Hospitalares e Projeto Extensionista I.", B-ENTRADA, B-MENOR. Sem preço | Veterinária à noite em SP | Presencial, 5 anos | Cadastre-se |
| v3-entrada | v3-entrada_stories-9x16_a_v1; v3-entrada_carrossel-1x1_a_v1 | "Faculdade UFAPE, Medicina Veterinária noturno em São Paulo: use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Curso noturno de 5 anos. As aulas começam em 22/02/2027." | Enem de 2010 em diante | Média mínima de 300 pontos | Cadastre-se |
| v4-ato (fase 2; também G7 e G12) | v4-ato_stories-9x16_a_v1; v4-ato_carrossel-1x1_a_v1 | "Medicina Veterinária noturno na Faculdade UFAPE, em São Paulo: veja o ato do curso, a duração de 5 anos, o desconto com regra e as condições de cancelamento." | B-ATO-INT, B-DESC-NOT, B-COND, B-ENTRADA, B-MENOR | Noturno: ato e condições | Confira o edital | Saiba mais |

Não prometer "sem largar o trabalho", não falar de horário de prática e estágio ([CONFIRMAR NO CATÁLOGO]) e não usar "mudar de carreira".

### 6.3 Pedagogia (BLOQUEADO)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| p1-noite | p1-noite_reels-9x16_a_v1 (R-P1); p1-noite_feed-1x1_a_v1 | "Faculdade UFAPE em Goiânia: Pedagogia presencial, no período noturno, em 4 anos. Foco na docência na Educação Infantil e nos anos iniciais do Ensino Fundamental." | B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | Pedagogia à noite em Goiânia | Presencial, 4 anos | Cadastre-se |
| p3-preco (também G7 e G12) | p3-preco_feed-1x1_a_v1; p3-preco_stories-9x16_a_v1 | "De R$ 1.050,00 por R$ 525,00 por mês (50%) no 1º semestre de 2027: Pedagogia noturno na Faculdade UFAPE, em Goiânia." | B-DESC-PED, B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | 50% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| p4-ato (também G7 e G12) | p4-ato_stories-9x16_a_v1; p4-ato_carrossel-1x1_a_v1 | "Pedagogia na Faculdade UFAPE, em Goiânia: veja o ato do curso, a inscrição gratuita, o desconto com regra e as condições de cancelamento." | B-ATO-PED, B-DESC-PED, B-COND, B-ENTRADA, B-MENOR | Antes de matricular, confira | Ato do curso e condições | Saiba mais |
| p2-pratica (rotação) | p2-pratica_reels-9x16_a_v1 (R-P2); p2-pratica_carrossel-1x1_a_v1 | "Prática Docente em todos os semestres e Projeto Integrador do 1º ao 7º, com estágio supervisionado a partir do 6º. Pedagogia na Faculdade UFAPE, em Goiânia." | "Pedagogia presencial, à noite, em 4 anos.", B-ENTRADA, B-MENOR. Sem preço | Prática Docente desde o 1º semestre | Pedagogia em Goiânia | Cadastre-se |
| p5-entrada (fase 2) | p5-entrada_carrossel-1x1_a_v1 | "Faculdade UFAPE, Pedagogia em Goiânia: use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Pedagogia presencial, à noite. As aulas começam em 22/02/2027." | Enem de 2010 em diante | Média mínima de 300 pontos | Cadastre-se |

Pedagogia: sem carga horária (3.440 h no site, 3.640 h no edital: [CONFIRMAR NO CATÁLOGO]), sem coordenação, sem docentes, sem endereço, sem trechos de modelo da página, sem crianças em imagem, sem comparação com EAD.

### 6.4 Combinações para o primeiro teste (fase 1)

Cenário A, G7 e G12 respondidos até 13/11 (aprovação pelo humano em AM2):
- Integral: v3-entrada, v1-preco e v2-pratica juntos, todos gancho a, 3 semanas de teste. Primeiro v3 e v1, por atacarem o gargalo provável (inscrito que não faz a redação, [SUPOSIÇÃO do cmo]) e a objeção de preço.
- Noturno: v1-preco e v2-noite nas 2 primeiras semanas depois do desbloqueio, depois v3-entrada.
- Pedagogia: p1-noite e p3-preco primeiro (regra de volume), depois p4-ato; p2 e p5 depois.

Cenário B, G7 ou G12 sem resposta em 13/11 (teste alternativo, sem preço e sem desconto):
- Integral sobe em 16/11 só com v3-entrada e v2-pratica (2 conceitos). O terceiro conceito, v1-preco, entra no mesmo conjunto assim que G7 e G12 forem respondidos e o qa conferir o texto, sem nova campanha e sem desligar os dois que estão no ar. A verba semanal da seção 4 não muda.
- Noturno: v2-noite e v3-entrada; v1-preco entra depois.
- Pedagogia: p1-noite e p2-pratica; p3-preco e p4-ato entram depois.
- v4-ato e a troca de fase 2 com a regra do desconto só entram com G7 e G12. A fase 2 usa, no lugar, o conceito sem preço de melhor resultado.
- Leitura: a fase 1 vira teste de 2 conceitos; o aprendizado sobre preço (H1 do criativos) começa só quando v1-preco entrar.

Protocolo (regras práticas, não metas, do plano v3): teste de R$ 10,00 a R$ 20,00 por conceito antes de julgar; pausar anúncio com R$ 13,33 gastos sem lead depois de 3 dias no ar (proposta ao humano); promover com CPL até R$ 6,67 e passagem de lead para inscrito igual ou acima da média do curso; decisão só com 2 semanas seguidas; mudança de verba de escala no máximo 20% por semana; 1 conceito novo a cada 2 semanas a partir da fase 2. Com R$ 150,00 por semana, o conjunto tende a ficar em "aprendizado limitado" no cenário base (gestor-de-midia 3.5, que cita cerca de 50 eventos em 7 dias na Central de Ajuda da Meta [CONFIRMAR o número vigente]); não mexer em público por isso.

---

## 7. Nomenclatura e UTM (D11 e D12)

- Campanha: linha_curso_plataforma_objetivo_publico_AAAAMM, com prefixo grad_ (curso: medvet-integral, medvet-noturno, pedagogia; público: amplo18, goiania18, rmk-lp30d).
- Conjunto: nome da campanha + "__" + público. Anúncio: ver seção 6. Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Nenhum dado pessoal em UTM.
- URL: `<BASE>?utm_source=meta&utm_medium=paid_social&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term=<público>`
  - BASE integral e noturno: https://faculdade.ufape.com.br/graduacao [CONFIRMAR, G13]
  - BASE Pedagogia: https://faculdade.ufape.com.br/graduacao/pedagogia [CONFIRMAR, G13]
- utm_source é sempre meta (D11); instagram e facebook se separam pelo posicionamento no relatório, sem mudar a UTM.
- Exemplo (integral, v3, fase 1): https://faculdade.ufape.com.br/graduacao?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_medvet-integral_meta_cadastro_amplo18_202611&utm_content=v3-entrada_carrossel-1x1_a_v1&utm_term=amplo18
- Exemplo (Pedagogia, p1): https://faculdade.ufape.com.br/graduacao/pedagogia?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_pedagogia_meta_cadastro_goiania18_AAAAMM&utm_content=p1-noite_reels-9x16_a_v1&utm_term=goiania18
- Os demais anúncios usam o mesmo modelo, trocando só utm_content (seção 6) e utm_campaign (campanha da fase). Remarketing: utm_term=rmk-lp30d.
- Origem no CRM: utm_campaign e utm_content precisam chegar ao CRM com o lead (G13, MP10). Sem isso a matrícula não é lida por campanha.

### Formulário e mensagem inicial

- Sem formulário instantâneo e sem campanha de mensagem. Destino único: LP da Graduação, que a squad nunca altera. Perguntas do formulário e política de privacidade são da LP [CONFIRMAR, G13]. Pedido à plataforma, não alteração da squad: o formulário deve informar a finalidade do uso dos dados e ter link para a política de privacidade.
- WhatsApp: nenhum anúncio leva a WhatsApp. Se um dia levar, só ao número oficial da Ufape, com o horário informado (secretaria: segunda a sexta, 9h às 18h).

---

## 8. Checklist de subida (humano executa; gestor-de-midia confere)

Antes de montar:
- [ ] MP1 (metas) e MP2 (verba e aprovador nomeado, G14) aprovados; sem isso nada sobe, nem em teste
- [ ] MP4 (públicos 18+) aprovado; MP15 respondido (leitura de "valor do curso", meta de 15 e turma mínima de 30)
- [ ] G7: Editais 003/2026 corrigidos e texto do desconto aprovado pela regulação; G12: efeito do reajuste de dezembro. Sem os dois, usar o cenário B da seção 6.4 (nenhum anúncio com preço ou desconto)
- [ ] G13: URL que recebe a UTM; formulário é inscrição ou captura; origem no CRM; política de privacidade
- [ ] MP10: pixel e API de Conversões recebendo o evento Lead; domínio verificado; evento testado no gerenciador de eventos
- [ ] Públicos de remarketing por pixel criados antes da fase 1, para acumular
- [ ] MP14: nenhuma campanha de Graduação rodando fora da planilha (se houver, o gasto entra nos R$ 2.000,00 do curso)
- [ ] Criativos aprovados pelo qa-de-marketing (10/11), com artes ajustadas (A-C2, A-C3, A-C5)
- [ ] Forma de pagamento ativa; limite de gasto por campanha conforme a seção 2 (R$ 3.440,00 na Meta, sem o Google); limite da conta não conta como trava

Montagem (11 a 13/11/2026, tudo em pausa):
- [ ] Campanha com objetivo Cadastros, orçamento diário da semana S1, limite de gasto da seção 2 e data de término 21/02/2027
- [ ] 1 conjunto: idade mínima 18, localização, sem interesses, posicionamentos da seção 5, exclusão por evento Lead
- [ ] Anúncios com nome, texto, título, descrição, CTA e UTM da seção 6; pré-visualização em feed, Stories e Reels
- [ ] Conferência de texto: nenhum "últimas vagas", nenhuma nota do MEC, nenhum "vale para entrar", Enem sempre com média mínima de 300 pontos e "2010 em diante", "representante legal", desconto só com valor cheio, valor com desconto, percentual, validade e "Condições e validade no edital"
- [ ] Teste de clique: a UTM chega à LP e ao CRM
- [ ] Ativação em 16/11/2026, segunda-feira. Datas informadas do Enem 2026, 08 e 15/11 (domingos) [CONFIRMAR no calendário oficial do Inep]: sem anúncio no ar nesses dias. Nenhuma mensagem sugere que a nota do Enem 2026 já pode ser usada

Trocas de fase (AM4): 07/12 (remarketing, se houver público), 04/01 (campanha _202701 sobe, _202611 pausa), 01/02 (remarketing _202702, se houver público; sem público, a _202701 segue).

## 9. Checklist de pausa

- [ ] 03/01/2027: pausar amplo18_202611 e rmk-lp30d_202612 (substituídas)
- [ ] 31/01/2027: pausar rmk-lp30d_202701; amplo18_202701 só se o CPL da fase 3 passou do máximo (proposta)
- [ ] 22/02/2027: pausar todas as campanhas da Graduação 2027/1 (MP13); conferir que nenhuma ficou ativa e que o gasto acumulado não passou de R$ 1.440,00 (Medicina Veterinária) e R$ 2.000,00 (Pedagogia) na Meta
- [ ] Antes: anúncio com R$ 13,33 sem lead depois de 3 dias; CPL acima de R$ 8,67 por 2 semanas depois de um ajuste; custo por matrícula acumulado acima de R$ 133,33 a partir de 04/01/2027; diferença acima de 15% entre plataforma, analytics e CRM (investigar antes de decidir). Cada pausa vai como proposta ao humano, com o que, por que, quanto, efeito e como desfazer
- [ ] Relatório final contra as metas até 05/03/2027

---

## 10. Travas

| Trava | Efeito | Quem resolve |
|---|---|---|
| G6: página de Pedagogia com texto de modelo, egresso copiado e docentes de outro curso | Pedagogia não sobe | Equipe do site |
| G7: textos dos Editais 003/2026 (preâmbulo e data de assinatura de SP; item 3.5 de Goiânia) | Nenhum anúncio com preço ou desconto sobe (v1-preco, v4-ato, p3-preco, p4-ato, troca de fase 2); vale o cenário B | Regulação |
| G8: campo turno do noturno mostra "INTEGRAL" | Noturno não sobe | Equipe do site |
| G12: reajuste de dezembro pode mudar os valores de 2027/1 | Todo anúncio com preço passa por ciclo extra se mudar | Financeiro e marketing |
| G13: URL, formulário, CRM e privacidade | Nenhum destino é final; nenhuma subida | Plataforma |
| G14: aprovador não nomeado | Ninguém aprova verba, anúncio ou peça com ato | Ufape |
| Datas do Enem 2026 (08 e 15/11, informadas) e das notas | Semana E e pesos de verba só com data confirmada [CONFIRMAR no calendário oficial do Inep]; sem anúncio no ar em 08 e 15/11 | Marketing |
| MP7 e G10: listas de contatos e menores | Sem semelhantes, sem exclusão por lista, sem API de Conversões com matrícula | Jurídico |
| MP15: meta de 15 contra turma mínima de 30 | Meta em reais não fechada; não muda o custo máximo | CEO |
| Tamanho mínimo do remarketing | Sem campanha de remarketing até atingir o mínimo | Gestor-de-midia |

---

## 11. Pedidos de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AM1 | Aprovar esta estrutura (1 campanha e 1 conjunto por curso e turno, público amplo 18+, orçamento na campanha, 3 conceitos, limites por campanha da seção 2, posicionamentos sem Audience Network e Messenger) | Verba baixa não suporta mais campanhas; leitura limpa | sem custo | Montagem possível a partir de 11/11 | Nova versão do arquivo |
| AM2 | Montar o integral em pausa entre 11 e 13/11/2026, só depois de MP1, MP2, MP4, MP10 e G13. Com G7 e G12 respondidos, montar v1-preco; sem eles, montar só v2-pratica e v3-entrada (cenário B) | Montagem é feita por humano e precisa de revisão antes do ar; preço sem G7 contraria a regra do Google e do criativos | R$ 0 até a ativação | Campanha pronta para 16/11 | Excluir o rascunho no gerenciador |
| AM3 | Ativar o integral em 16/11/2026, com os conceitos liberados pelo cenário A ou B | Início da captação de 14 semanas | R$ 150,00 por semana na Meta nas 3 primeiras semanas (R$ 450,00 na fase 1) | Cerca de 22 leads por semana se o CPL ficar em R$ 6,67; sem promessa | Pausar a campanha, por humano |
| AM4 | Trocas de fase em 07/12, 04/01 e 01/02; os anúncios com preço só com G7 e G12 | Cada fase muda mensagem e verba | R$ 225,00, R$ 525,00 e R$ 240,00 | Transição no prazo | Manter a campanha anterior |
| AM5 | Criar campanha de remarketing quando o público atingir o mínimo, com até 20% da verba da fase [SUPOSIÇÃO] | Remarketing só com público suficiente | dentro da verba do curso | Lembrar quem viu a LP | Pausar e devolver a verba à ampla |
| AM6 | Montar e ativar o noturno depois de G8 e MP4 (MP8), na segunda-feira seguinte, com metade da verba semanal da Meta do curso; anúncios com preço também exigem G7 e G12 | Página precisa mostrar o turno certo | metade da verba semanal da Meta do curso, dentro dos R$ 1.440,00 | Noturno no ar sem passar do total do curso | Pausar; a verba volta ao integral |
| AM7 | Montar e ativar a Pedagogia depois de G6, MP4 e MP1 (MP9); anúncios com preço também exigem G7 e G12 | Página com texto de modelo | R$ 2.000,00 no ciclo, conforme a seção 4 | Pedagogia no ar com meta escrita | Pausar a campanha |
| AM8 | Pausar todas as campanhas da Graduação em 22/02/2027 | Fim do ciclo | encerra o gasto | Relatório final até 05/03/2027 | Reativar no gerenciador |
| AM9 | Definir o limite de gasto por campanha (seção 2): R$ 1.440,00 na Medicina Veterinária e R$ 2.000,00 na Pedagogia, R$ 3.440,00 na Meta, sem o Google; data de término 21/02/2027 | Travar a verba aprovada sem depender do limite da conta, que pode ser compartilhado | R$ 3.440,00 na Meta | Gasto da Graduação nunca passa do aprovado | Alterar o limite, por humano |
| AM10 | Adotar o nome de anúncio com bloco de gancho (a, b, c) em vez de codificar o gancho no vN | Ajuste A-C1 do qa-d; D12 pede o gancho | sem custo | Atribuição limpa de gancho e iteração | Voltar ao padrão do plano v3 |
| AM11 | Verba extra, se a Meta não entregar os leads necessários depois de 2 semanas de dados | Regra: nunca gastar acima do aprovado | [CONFIRMAR]: 15 x custo por matrícula observado, menos o já gasto | Decisão informada | Manter os R$ 2.000,00 e aceitar a meta parcial |
| AM12 | Ao cmo: (a) usar "Enem de 2010 em diante" no título até a semana E e decidir a regra única para Meta e Google (R-M1); (b) ler "citar sempre o ato" como "quando citar" ou como "em toda peça" (R-M7) | Uma regra só nos dois canais e conformidade com contexto/graduacao.md | sem custo | Textos iguais nos canais | Voltar ao título "Use sua nota do Enem" depois da semana E |

---

## 12. Auditoria

auditorias/11-midia-paga.md
- [ ] Plano aprovado: pendente (aprovação humana)
- [x] Metas de CPL e custo por matrícula escritas antes de subir (seção 1); aprovação pendente (MP1)
- [ ] Verba e aprovador: limites por campanha fecham com as fases (R$ 1.440,00, R$ 2.000,00, R$ 3.440,00 na Meta); aprovação e aprovador pendentes (MP2, G14)
- [x] Nomenclatura padrão em campanha, conjunto e anúncio (seções 2, 6 e 7)
- [ ] UTMs completas e origem no CRM: UTM definida; URL e chegada ao CRM pendentes (G13)
- [ ] Pixel e API de Conversões: [DADO NÃO FORNECIDO]
- [ ] Criativos aprovados em conformidade-educacional: dependem do qa de 10/11 (o qa-d aprovou o pacote com ajustes); preço só com G7
- [x] Políticas da Meta: sem atributo pessoal, sem urgência falsa, sem caixa alta
- [x] Nenhum público com menores de 18
- [x] Sem segmentação discriminatória; sem listas de contatos
- [x] Dados de curso do catálogo e dos editais
- [x] Destino de WhatsApp: não se aplica
- [x] Números só das fontes fornecidas; nenhum desempenho citado
- [x] Nada foi subido, alterado, pausado ou gasto

Conformidade educacional: texto de cada anúncio vem do pacote aprovado com ajustes no qa-d; Enem com a média mínima e "2010 em diante"; desconto com valor cheio, valor com desconto, percentual, validade e regra, e só com G7 e G12 resolvidos; ato só como no catálogo; nenhuma nota do MEC; Pedagogia sem carga horária. Pendentes externos: página (G6, G8), formulário e privacidade (G13), editais (G7), preço e ato (regulação). Resultado: rascunho pronto para nova conferência do qa nos itens M-1 a M-5.

---

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 por curso e meta de 15 matrículas por curso (decisões 15 e 16, docs/execucao-2026-10-26.md). Meta Medicina Veterinária R$ 1.440,00, Pedagogia R$ 2.000,00; distribuição semanal (gestor-de-midia v3, seção 3.3).
- Custo por matrícula máximo R$ 133,33 e CPL base R$ 6,67 (gestor-de-midia v3, seção 2).
- Integral de R$ 10.000,00 por R$ 5.000,00 (50%); noturno por R$ 4.000,00 (60%); Pedagogia de R$ 1.050,00 por R$ 525,00 (50%); só no 1º semestre de 2027 (catálogo, seção 1; editais 003/2026).
- Inscrição gratuita; redação online eliminatória, nota mínima 5,0; Enem com média mínima de 300 pontos, de 2010 em diante; aulas em 22/02/2027; turma mínima de 30; devolução de 80% até 2 dias antes das aulas; menor precisa do aceite do representante legal (editais 002 e 004/2026).
- Atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025); Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) (catálogo).
- Anúncio só para 18 anos ou mais (cmo-graduacao, G10).
- UTM: utm_medium=paid_social e utm_source=meta no pago da Meta; prefixo grad_ (cmo-geral, D11 e D12).
- G7 bloqueia preço e desconto no criativos e no Google (qa de 27/10/2026).
- 16/11/2026 e 22/02/2027 são segundas-feiras; 08 e 15/11/2026 são domingos (calendário).
- qa-d: criativos aprovados com ajustes A-C1 a A-C5.

## Lista 2. Suposições

- [SUPOSIÇÃO de cenário] Taxas de conversão do funil (20%, 40%, 50% e 10%, 12,5%, 20%), do gestor-de-midia, que dão os três CPLs.
- [SUPOSIÇÃO] Grande São Paulo e Goiânia com região metropolitana como área de entrega.
- [SUPOSIÇÃO de desenho] Divisão 50% e 50% entre turnos; exclusão cruzada entre turnos; até 20% da verba da fase para remarketing; exclusão de convertidos por evento do pixel.
- [SUPOSIÇÃO] Evento Lead disparado pelo formulário da LP; janela de atribuição padrão.
- [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda da Meta] A Meta pode gastar até 25% a mais num dia, mantendo a média da semana.
- [SUPOSIÇÃO] Audience Network e Messenger fazem parte dos posicionamentos automáticos e ficam fora desta estrutura.
- [SUPOSIÇÃO] Limites de 40 caracteres no título e 30 na descrição.
- [SUPOSIÇÃO de leitura] "Citar sempre o ato" (contexto/graduacao.md) lido como "quando citar, como no catálogo".
- [SUPOSIÇÃO do cmo] O gargalo do funil é o inscrito que não faz a redação.
- [SUPOSIÇÃO] Educação não é categoria especial de anúncio na Meta.
- [SUPOSIÇÃO] A conta de anúncios pode ter campanhas de outras linhas, por isso o limite da conta não serve de trava.

## Lista 3. Dados que faltam

- [CONFIRMAR] MP1, MP2, MP4, MP15 e aprovador nomeado (G14).
- [CONFIRMAR] G7 e G12 até 13/11 (senão vale o cenário B); G13 (URL, formulário, CRM, privacidade); G6; G8; G10 e MP7.
- [DADO NÃO FORNECIDO] Estado do pixel e da API de Conversões; histórico de CPL; número de inscritos e matrículas.
- [CONFIRMAR no calendário oficial do Inep] Datas do Enem 2026 (08 e 15/11, informadas) e das notas; data-limite interna de inscrição (G4).
- [CONFIRMAR NO CATÁLOGO] Carga horária da Pedagogia; nomes das disciplinas do 1º semestre; horário de prática e estágio do noturno.
- [CONFIRMAR] No gerenciador: tamanho mínimo do público de remarketing, limite de idade fixo no Advantage+ audience, limites de caracteres, categoria de anúncio, posicionamentos. Se a conta de anúncios é só da Graduação.
- [CONFIRMAR] Campanhas de Graduação rodando fora da planilha (MP14); período exato do ciclo (decisão 15); decisões do cmo em AM12.
- Nota para o gestor-de-midia (arquivo de outro dono, não alterado): a seção 4.8 do plano v3 fala em limite de conta de R$ 4.000,00, que inclui o Google; este arquivo usa limite por campanha.

---

## Próximo passo

Conferência do qa-de-marketing só nos itens M-1 a M-5 e nas recomendações aplicadas. Depois, aprovação humana (AM1 a AM12) antes da montagem de 11 a 13/11/2026. O anuncios-google segue em paralelo com G-1 e G-2. Nada é publicado, enviado ou pago sem aprovação humana.
