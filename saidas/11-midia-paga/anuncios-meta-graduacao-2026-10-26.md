# Estrutura de Meta Ads: Graduação 2027/1 (Medicina Veterinária em São Paulo e Pedagogia em Goiânia)

- Agente: anuncios-meta (departamento 11, Mídia Paga, sob o gestor-de-midia)
- Linha: graduacao
- Data: 26/10/2026 (conforme a encomenda); entregue em 27/10/2026, prazo 06/11/2026
- Workflow: /campanha-de-vestibular, etapa 5 (estrutura do canal Meta)
- Status: rascunho para aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Quem monta, revisa e aprova é um humano; aprovador nomeado: [CONFIRMAR, G14].
- Entradas lidas:
  - CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 17)
  - contexto/ufape-geral.md; contexto/graduacao.md; contexto/catalogo-de-cursos.md (seção 1); contexto/cursos/graduacao/editais-2027-1.md
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (pedidos G1 a G16)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12.7, D11 e D12; seção 13 só até o início da D16, que trata de mensagens e não afeta anúncio)
  - saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (v3) e estrategia-de-midia-graduacao-2026-10-26.md (v3)
  - saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-d.md
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md; auditorias/11-midia-paga.md; auditorias/conformidade-educacional.md
- Não lidas nesta rodada: as fichas por curso (matriz); os nomes de disciplinas vêm do criativos-de-anuncio, que já os marca [CONFIRMAR NO CATÁLOGO].
- Regra de fonte: preço, turno, duração, modalidade, carga horária e ato vêm do catálogo (seção 1); datas, vagas, ingresso e regras do desconto vêm da ficha dos editais; verba e metas vêm do plano de mídia v3 (decisões 15 e 16). Não existe exportação de plataforma, histórico de CPL nem número de CRM: nenhum desempenho é citado.

---

## 0. Resumo (5 linhas)

1. Modelo: lançamento por fases, enxuto pela verba. 1 campanha e 1 conjunto por curso e turno, público amplo 18+, orçamento na campanha, no máximo 3 conceitos ativos.
2. Verba Meta: Medicina Veterinária R$ 1.440,00 (integral agora; noturno divide 50% e 50% depois de MP8); Pedagogia R$ 2.000,00 (bloqueada). Pausa geral em 22/02/2027.
3. Objetivo: Cadastros na LP da Graduação, evento de otimização Lead. Matrícula é leitura separada, nunca otimização.
4. Só o integral pode subir (montagem em pausa de 11 a 13/11, ativação em 16/11), e só com MP1, MP2, MP4, MP10 e G13 respondidos. Noturno espera G8 e MP8. Pedagogia espera G6, MP4, MP1 e MP9.
5. Travas abertas: G6, G8, G12, G13, G14, datas do Enem, tamanho mínimo do público de remarketing, listas de contatos (MP7).

---

## 1. Modelo escolhido e motivo

- Lançamento por fases (captação, aquecimento, inscrições abertas, reta final), porque as aulas começam em 22/02/2027 e a mensagem muda por fase. Dentro da fase, a lógica é enxuta: R$ 142,86 por semana por curso, em média, não sustentam teste e escala em campanhas separadas.
- Pedagogia: local (Goiânia), enxuta, 1 campanha e 1 conjunto.
- Orçamento na campanha, nunca no conjunto. Motivo: 1 conjunto por campanha, então o orçamento de campanha dá o mesmo controle com um nível a menos e permite o limite de gasto da campanha como trava.
- Conjunto único e amplo. A diversidade de criativos faz o papel dos interesses. Sem interesses, sem semelhantes, sem listas de contatos.
- Metas (do plano v3, aprovação pendente em MP1): custo por matrícula máximo R$ 133,33; CPL máximo base R$ 6,67 (conservador R$ 2,67; otimista R$ 13,33), todos [SUPOSIÇÃO de cenário] nas taxas de conversão. Se o formulário da LP for a inscrição (G13), a meta vira custo por inscrito: R$ 16,67 no base.

---

## 2. Mapa em árvore (campanha, conjunto, anúncio)

### 2.1 Medicina Veterinária integral (pode subir em 16/11/2026)

- grad_medvet-integral_meta_cadastro_amplo18_202611 (fase 1 e 2, até 03/01/2027)
  - conjunto: grad_medvet-integral_meta_cadastro_amplo18_202611__amplo18
    - anúncios: v1-preco, v2-pratica, v3-entrada (seção 5)
- grad_medvet-integral_meta_cadastro_amplo18_202701 (fase 3, 04/01 a 31/01/2027, escala só com conceitos validados)
  - conjunto: ..._202701__amplo18
- grad_medvet-integral_meta_cadastro_rmk-lp30d_202612, _202701 e _202702: só quando o público de visitantes da LP atingir o mínimo da Meta [CONFIRMAR o valor vigente no gerenciador]. A verba sai da campanha ampla, sem acréscimo. Proposta de divisão: até 20% da verba semanal da Meta do curso [SUPOSIÇÃO de desenho, decide o gestor-de-midia em AM5].
  - conjunto: ..._rmk-lp30d__rmk-lp30d (visitantes da LP nos últimos 30 dias, 18+, só por pixel)

### 2.2 Medicina Veterinária noturno (BLOQUEADO: G8 e MP4, depois MP8)

- grad_medvet-noturno_meta_cadastro_amplo18_AAAAMM (AAAAMM do mês do desbloqueio)
  - conjunto: ..._AAAAMM__amplo18
    - anúncios: v1-preco, v2-noite, v3-entrada (v4-ato entra na fase 2)
- Remarketing do noturno: mesma regra do integral.

### 2.3 Pedagogia (BLOQUEADO: G6, MP4 e MP1, depois MP9)

- grad_pedagogia_meta_cadastro_goiania18_AAAAMM
  - conjunto: ..._AAAAMM__goiania18
    - anúncios: p1-noite, p3-preco, p4-ato (p2-pratica entra na rotação; p5-entrada é o conceito novo da fase 2)
- grad_pedagogia_meta_cadastro_rmk-lp30d_AAAAMM: só com público mínimo.

Regra dos 3 conceitos: nunca mais de 3 conceitos ativos por curso e turno. Conceito novo (v4-ato, p5-entrada) entra no lugar do conceito de pior resultado, só depois de 2 semanas de leitura, e nunca se desligam todos os antigos ao mesmo tempo. Cada conceito pode ter até 2 anúncios (formato principal e versão 9:16 para Stories e Reels), porque a UTM muda por formato.

---

## 3. Campanhas: objetivo, evento, verba e leads por semana

| Item | Integral | Noturno | Pedagogia |
|---|---|---|---|
| Objetivo na Meta | Cadastros (ou Leads, conforme o nome atual no gerenciador) | idem | idem |
| Destino | Site: LP da Graduação, sem formulário instantâneo | idem | idem |
| Evento de otimização | Lead (evento padrão do pixel, disparado no envio do formulário da LP). Se a LP não disparar Lead, pedir ao responsável da plataforma antes de subir [CONFIRMAR, G13, MP10] | idem | idem |
| Matrícula | Conversão personalizada separada, só para leitura, nunca como evento de otimização (volume baixo demais para aprender). Pelo CRM, por utm_campaign e utm_content. Envio de matrícula à Meta por API de Conversões só depois de base legal e tratamento de menores validados (MP7, G10) | idem | idem |
| Janela de atribuição | Padrão da conta (7 dias de clique) [CONFIRMAR] | idem | idem |
| Verba Meta no ciclo | R$ 1.440,00 (dividida 50% e 50% com o noturno depois de MP8) | metade da verba semanal do curso | R$ 2.000,00 |
| Leads pela verba (base, CPL R$ 6,67) | 216 no ciclo; conservador 539; otimista 108 | idem, em metade | 300; conservador 750; otimista 150 |
| Sobe em | 16/11/2026 | dia seguinte a MP8 | dia seguinte a MP9 |

Leads por semana são o que a verba compra se o CPL ficar exatamente no máximo. Não são previsão de resultado.

---

## 4. Verba por semana (R$, por campanha de Meta)

Verba diária da campanha = semanal / 7. Trava: limite de gasto da campanha igual ao total da fase (a Meta pode gastar até 25% a mais num dia, e o limite impede que o total passe).

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
- Noturno depois de MP8: cada valor semanal da coluna do integral passa a ser dividido em duas campanhas, 50% e 50%, a partir da semana seguinte. O total do curso não muda.
- Pedagogia desbloqueada depois de 16/11: semanas sem anúncio não são recuperadas de uma vez. A parte não gasta da fase 1 se divide pelas 7 semanas das fases 3 e 4 (até R$ 85,71 a mais por semana) e só é gasta se a campanha passar no critério de escalar. O resto vira economia.
- Pesos de Enem e Sisu (semana E e semana S) só entram com as datas oficiais confirmadas. O Sisu não aparece em nenhum texto.
- Realocação entre semanas, canais, turnos ou cursos segue a seção 6.2 do estrategia-de-midia e vira pedido de aprovação.

---

## 5. Conjuntos: público, localização, posicionamentos e exclusões

| Item | amplo18 (integral e noturno) | goiania18 (Pedagogia) | rmk-lp30d |
|---|---|---|---|
| Idade | mínimo 18 anos, sem teto. Conferir no gerenciador que o 18 é limite fixo e não sugestão [CONFIRMAR] | idem | idem |
| Gênero | todos | todos | todos |
| Localização | Grande São Paulo [SUPOSIÇÃO, área a confirmar com o comercial de SP], pessoas que moram ou estiveram recentemente | Goiânia e região metropolitana [SUPOSIÇÃO, raio a confirmar com o comercial de Goiânia]. Raio pequeno demais encarece a entrega | a mesma do curso |
| Interesses e comportamentos | nenhum | nenhum (nada de "professor" ou "trabalha em escola") | nenhum |
| Público | amplo; Advantage+ audience sem sugestões de segmentação | idem | visitantes da LP do curso nos últimos 30 dias, só por pixel; só com o mínimo da Meta |
| Posicionamentos | automáticos (feed, Stories, Reels, Explorar; Instagram e Facebook). Criativos nos formatos 1:1 e 9:16; 4:5 opcional | idem | idem |
| Exclusões | quem disparou Lead nos últimos 180 dias (evento do pixel, sem lista); no noturno, visitantes que chegaram por anúncio do integral e o inverso [SUPOSIÇÃO de desenho] | quem disparou Lead nos últimos 180 dias | quem disparou Lead; cruzada entre turnos |
| Listas de contatos, semelhantes e importações | proibidos até validação jurídica (MP7, G10): a base pode ter menores | idem | idem |
| Categoria especial de anúncio | Educação não está entre as categorias especiais da Meta [CONFIRMAR no gerenciador]. Se a conta pedir, seguir a exigência | idem | idem |

Regras fixas: nenhuma segmentação ou exclusão por idade (além do piso de 18), gênero, renda, saúde, religião, origem ou emprego. Nenhum menor como público. A mensagem fala com "você e sua família" e lembra o aceite do representante legal.

---

## 6. Anúncios

Convenções:
- Nome do anúncio = utm_content, no padrão D12 com bloco de gancho (ajuste A-C1 do qa-d): `<conceito>_<formato>_<gancho>_vN`. Gancho a, b ou c (os ganchos B e C ficam em reserva no criativos, para iteração I1); N é a versão. Alinhar com o gestor-de-midia (AM10).
- Texto principal: o que aparece antes do "ver mais" é a primeira frase; nos textos de preço ela já traz valor cheio, valor com desconto, percentual e validade. O complemento leva a regra completa. Limites: título cerca de 40 e descrição cerca de 30 caracteres [CONFIRMAR na plataforma, SUPOSIÇÃO do criativos]; o humano confere a contagem no gerenciador.
- Blocos (B-DESC-INT, B-ENTRADA, B-MENOR e os demais) estão na seção 2.1 do criativos-de-anuncio. A arte e o texto dentro do vídeo estão nas seções 2 e 3 do mesmo arquivo. Este arquivo não reescreve as peças.
- Padrão de entregável: o texto principal, título, descrição e CTA aprovados no criativos são a versão A de cada conceito. As versões B e C (5 ângulos por conceito) já estão em reserva no criativos e entram só como iteração depois de um vencedor. Esta é a diferença assumida em relação ao entregável padrão de 5 textos por criativo, por causa do limite de 3 conceitos e da verba.
- CTA: botão "Cadastre-se" nas campanhas de cadastro, porque o objetivo é cadastro; "Saiba mais" no remarketing e em v4-ato e p4-ato, porque quem já viu a página quer ler as condições.
- Ajustes do qa-d que entram na montagem: A-C3 (D.O.U. na arte 1:1 de v4-ato e p4-ato: "(D.O.U. 21/03/2025)" e "(D.O.U. 20/12/2022)"); A-C5 (R-I2, cena 1, linha "Média mínima de 300 pontos" na tela); A-C2 (R-P1, cena 3, "de 2010 em diante"). Esses ajustes são da peça e ficam com o criativos-de-anuncio; a montagem só usa a arte já corrigida.

### 6.1 Integral (pronto para montagem depois do qa de 10/11 e da aprovação humana)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| v1-preco | v1-preco_feed-1x1_a_v1; v1-preco_stories-9x16_a_v1 | "De R$ 10.000,00 por R$ 5.000,00 por mês (50%) no 1º semestre de 2027: Medicina Veterinária integral na Faculdade UFAPE, em São Paulo." | B-DESC-INT, B-ENTRADA, B-MENOR; fecha com "Veja o edital e faça a inscrição gratuita pelo site." | 50% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| v2-pratica | v2-pratica_reels-9x16_a_v1 (vídeo R-I1); v2-pratica_feed-1x1_a_v1 | "No 1º semestre da matriz integral: Anatomia, Práticas Hospitalares e Projeto Extensionista I. Medicina Veterinária presencial na Faculdade UFAPE, em São Paulo." | "Integral, presencial, em 4 anos.", B-ENTRADA, B-MENOR. Sem preço | Prática desde o 1º semestre | Veterinária integral em SP | Cadastre-se |
| v3-entrada | v3-entrada_carrossel-1x1_a_v1; v3-entrada_stories-9x16_a_v1 (ou vídeo R-I2) | "Inscrição gratuita na Faculdade UFAPE. Use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Medicina Veterinária presencial em São Paulo. As aulas começam em 22/02/2027." | Use sua nota do Enem | Média mínima de 300 pontos | Cadastre-se |
| v4-ato (fase 2, entra no lugar do pior conceito) | v4-ato_carrossel-1x1_a_v1; v4-ato_stories-9x16_a_v1 | "Medicina Veterinária em São Paulo, na Faculdade UFAPE: veja o ato do curso, a inscrição gratuita, o desconto com regra e as condições de cancelamento." | B-ATO-INT, B-DESC-INT, B-COND, B-ENTRADA, B-MENOR | Antes de matricular, confira | Ato do curso e condições | Saiba mais |

Trocas de texto por fase (seção 2.6 do criativos, mesmo conceito, muda abertura, título e descrição; a regra completa fica no complemento):
- Fase 2, remarketing: abertura "A regra completa do desconto do 1º semestre de 2027."; título "Regras do desconto 2027/1"; descrição "Condições e validade no edital". Nomes: v1-preco_feed-1x1_a_v2 (versão 2 do mesmo gancho, para não confundir com gancho).
- Fase 3: título "Nota do Enem ou redação", descrição "Inscrição gratuita". A semana E ("Notas do Enem divulgadas...") só depois da data oficial confirmada.
- Fase 4: abertura "As aulas começam em 22/02/2027: veja os passos da matrícula."; título "Passos da matrícula"; complemento B-PASSOS, B-COND, B-MENOR. Sem contagem regressiva e sem "vagas".

### 6.2 Noturno (BLOQUEADO)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| v1-preco | v1-preco_feed-1x1_a_v1; v1-preco_reels-9x16_a_v1 (R-N2) | "De R$ 10.000,00 por R$ 4.000,00 por mês (60%) no 1º semestre de 2027: Medicina Veterinária noturno, 5 anos, na Faculdade UFAPE, em São Paulo." | B-DESC-NOT, B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | 60% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| v2-noite | v2-noite_reels-9x16_a_v1 (R-N1); v2-noite_feed-1x1_a_v1 | "Faculdade UFAPE: Medicina Veterinária no período noturno, presencial, em São Paulo. O curso dura 5 anos. Inscrição gratuita." | "No 1º semestre da matriz noturna: Práticas Hospitalares e Projeto Extensionista I.", B-ENTRADA, B-MENOR. Sem preço | Veterinária à noite em SP | Presencial, 5 anos | Cadastre-se |
| v3-entrada | v3-entrada_stories-9x16_a_v1; v3-entrada_carrossel-1x1_a_v1 | "Faculdade UFAPE, Medicina Veterinária noturno em São Paulo: use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Curso noturno de 5 anos. As aulas começam em 22/02/2027." | Use sua nota do Enem | Média mínima de 300 pontos | Cadastre-se |
| v4-ato (fase 2) | v4-ato_stories-9x16_a_v1; v4-ato_carrossel-1x1_a_v1 | "Medicina Veterinária noturno na Faculdade UFAPE, em São Paulo: veja o ato do curso, a duração de 5 anos, o desconto com regra e as condições de cancelamento." | B-ATO-INT, B-DESC-NOT, B-COND, B-ENTRADA, B-MENOR | Noturno: ato e condições | Confira o edital | Saiba mais |

Não prometer "sem largar o trabalho", não falar de horário de prática e estágio ([CONFIRMAR NO CATÁLOGO]) e não usar "mudar de carreira".

### 6.3 Pedagogia (BLOQUEADO)

| Conceito | Anúncio (utm_content) | Texto principal (primeira frase) | Complemento | Título | Descrição | CTA |
|---|---|---|---|---|---|---|
| p1-noite | p1-noite_reels-9x16_a_v1 (R-P1); p1-noite_feed-1x1_a_v1 | "Faculdade UFAPE em Goiânia: Pedagogia presencial, no período noturno, em 4 anos. Foco na docência na Educação Infantil e nos anos iniciais do Ensino Fundamental." | B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | Pedagogia à noite em Goiânia | Presencial, 4 anos | Cadastre-se |
| p3-preco | p3-preco_feed-1x1_a_v1; p3-preco_stories-9x16_a_v1 | "De R$ 1.050,00 por R$ 525,00 por mês (50%) no 1º semestre de 2027: Pedagogia noturno na Faculdade UFAPE, em Goiânia." | B-DESC-PED, B-ENTRADA, B-MENOR; fecha com a chamada à inscrição | 50% no 1º semestre de 2027 | Condições e validade no edital | Cadastre-se |
| p4-ato | p4-ato_stories-9x16_a_v1; p4-ato_carrossel-1x1_a_v1 | "Pedagogia na Faculdade UFAPE, em Goiânia: veja o ato do curso, a inscrição gratuita, o desconto com regra e as condições de cancelamento." | B-ATO-PED, B-DESC-PED, B-COND, B-ENTRADA, B-MENOR | Antes de matricular, confira | Ato do curso e condições | Saiba mais |
| p2-pratica (rotação) | p2-pratica_reels-9x16_a_v1 (R-P2); p2-pratica_carrossel-1x1_a_v1 | "Prática Docente em todos os semestres e Projeto Integrador do 1º ao 7º, com estágio supervisionado a partir do 6º. Pedagogia na Faculdade UFAPE, em Goiânia." | "Pedagogia presencial, à noite, em 4 anos.", B-ENTRADA, B-MENOR. Sem preço | Prática Docente desde o 1º semestre | Pedagogia em Goiânia | Cadastre-se |
| p5-entrada (fase 2) | p5-entrada_carrossel-1x1_a_v1 | "Faculdade UFAPE, Pedagogia em Goiânia: use a nota do Enem (média mínima de 300 pontos, de 2010 em diante) ou faça a redação online." | B-ENTRADA, B-MENOR, "Pedagogia presencial, à noite. As aulas começam em 22/02/2027." | Use sua nota do Enem | Média mínima de 300 pontos | Cadastre-se |

Pedagogia: sem carga horária (3.440 h no site, 3.640 h no edital: [CONFIRMAR NO CATÁLOGO]), sem coordenação, sem docentes, sem endereço, sem trechos de modelo da página, sem crianças em imagem, sem comparação com EAD.

### 6.4 Combinações para o primeiro teste (fase 1)

- Integral: v3-entrada, v1-preco e v2-pratica juntos, todos gancho a, 3 semanas de teste. Primeiro v3 e v1, por atacarem o gargalo provável (inscrito que não faz a redação, [SUPOSIÇÃO do cmo]) e a objeção de preço.
- Noturno: v1-preco e v2-noite nas 2 primeiras semanas depois do desbloqueio, depois v3-entrada.
- Pedagogia: p1-noite e p3-preco primeiro (regra de volume), depois p4-ato; p2 e p5 depois.
- Protocolo (regras práticas, não metas, do plano v3): teste de R$ 10,00 a R$ 20,00 por conceito antes de julgar; pausar anúncio com R$ 13,33 gastos sem lead depois de 3 dias no ar (proposta ao humano); promover com CPL até R$ 6,67 e passagem de lead para inscrito igual ou acima da média do curso; decisão só com 2 semanas seguidas; mudança de verba de escala no máximo 20% por semana; 1 conceito novo a cada 2 semanas a partir da fase 2. A Meta tende a ficar em "aprendizado limitado" no base; não mexer em público por isso.

---

## 7. Nomenclatura e UTM (D11 e D12)

- Campanha: linha_curso_plataforma_objetivo_publico_AAAAMM, com prefixo grad_ (curso: medvet-integral, medvet-noturno, pedagogia; público: amplo18, goiania18, rmk-lp30d).
- Conjunto: nome da campanha + "__" + público. Anúncio: ver seção 6. Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Nenhum dado pessoal em UTM.
- URL: `<BASE>?utm_source=meta&utm_medium=paid_social&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term=<público>`
  - BASE integral e noturno: faculdade.ufape.com.br/graduacao [CONFIRMAR, G13]
  - BASE Pedagogia: faculdade.ufape.com.br/graduacao/pedagogia [CONFIRMAR, G13]
- utm_source é sempre meta (D11); a plataforma pode separar instagram e facebook pelo posicionamento no relatório, sem mudar a UTM.
- Exemplo completo (integral, v3, fase 1): faculdade.ufape.com.br/graduacao?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_medvet-integral_meta_cadastro_amplo18_202611&utm_content=v3-entrada_carrossel-1x1_a_v1&utm_term=amplo18
- Exemplo (Pedagogia, p3): faculdade.ufape.com.br/graduacao/pedagogia?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_pedagogia_meta_cadastro_goiania18_AAAAMM&utm_content=p3-preco_feed-1x1_a_v1&utm_term=goiania18
- Os demais anúncios usam o mesmo modelo, trocando só utm_content (tabelas da seção 6) e utm_campaign (campanha da fase). Remarketing: utm_term=rmk-lp30d.
- Origem no CRM: utm_campaign e utm_content precisam chegar ao CRM com o lead (G13, MP10). Sem isso a matrícula não é lida por campanha.

### Formulário e mensagem inicial

- Sem formulário instantâneo e sem campanha de mensagem. Destino único: LP da Graduação, que a squad nunca altera. As perguntas do formulário e a política de privacidade são da LP [CONFIRMAR, G13]. Pedido à plataforma, não alteração da squad: o formulário deve informar a finalidade do uso dos dados e ter link para a política de privacidade.
- WhatsApp: nenhum anúncio leva a WhatsApp. Se um dia levar, só ao número oficial da Ufape com horário informado (secretaria: segunda a sexta, 9h às 18h; vendas SP e Goiânia: números do contexto geral).

---

## 8. Checklist de subida (humano executa; gestor-de-midia confere)

Antes de montar:
- [ ] MP1 (metas) e MP2 (verba e aprovador nomeado, G14) aprovados; sem isso nada sobe, nem em teste
- [ ] MP4 (públicos 18+) aprovado; MP15 respondido (leitura de "valor do curso", meta de 15 e turma mínima de 30)
- [ ] G13: URL que recebe a UTM; formulário é inscrição ou captura; origem no CRM; política de privacidade
- [ ] MP10: pixel e API de Conversões recebendo o evento Lead; domínio verificado; evento testado no gerenciador de eventos
- [ ] Públicos de remarketing por pixel criados antes da fase 1, para acumular
- [ ] MP14: nenhuma campanha de Graduação rodando fora da planilha (se houver, o gasto entra nos R$ 2.000,00 do curso)
- [ ] Criativos aprovados pelo qa-de-marketing (10/11) e artes com os ajustes A-C2, A-C3 e A-C5
- [ ] Preço e desconto aprovados por marketing e regulação; G12 (reajuste de dezembro) respondido, ou ciclo extra se mudar valor
- [ ] Forma de pagamento ativa e limite de gasto da conta igual à verba aprovada (R$ 2.000,00 por curso, R$ 4.000,00 na Graduação)

Montagem (11 a 13/11/2026, tudo em pausa):
- [ ] Campanha com objetivo Cadastros, orçamento de campanha diário da semana S1 e limite de gasto da fase
- [ ] 1 conjunto: idade mínima 18, localização, sem interesses, posicionamentos automáticos, exclusão por evento Lead
- [ ] Anúncios com nome, texto, título, descrição, CTA e UTM da seção 6; pré-visualização em feed, Stories e Reels
- [ ] Conferência de texto: nenhum "últimas vagas", nenhuma nota do MEC, nenhum "vale para entrar", Enem sempre com média mínima de 300 pontos e "2010 em diante", "representante legal", desconto só com valor cheio, valor com desconto, percentual, validade e "Condições e validade no edital"
- [ ] Teste de clique: a UTM chega à LP e ao CRM
- [ ] Ativação em 16/11/2026 (Enem de 08 e 15/11 sem anúncio no ar); nenhuma mensagem sugere que a nota do Enem 2026 já pode ser usada

Trocas de fase (pedido AM4): 07/12 (remarketing, se houver público), 04/01 (campanha _202701 sobe, _202611 pausa), 01/02 (remarketing _202702).

## 9. Checklist de pausa

- [ ] 03/01/2027: pausar amplo18_202611 e rmk-lp30d_202612 (substituídas)
- [ ] 31/01/2027: pausar rmk-lp30d_202701; amplo18_202701 só se o CPL da fase 3 passou do máximo (proposta)
- [ ] 22/02/2027: pausar todas as campanhas da Graduação 2027/1 (MP13); conferir que nenhuma ficou ativa e que o gasto acumulado não passou de R$ 2.000,00 por curso
- [ ] Antes: anúncio com R$ 13,33 sem lead depois de 3 dias; CPL acima de R$ 8,67 por 2 semanas depois de um ajuste; custo por matrícula acumulado acima de R$ 133,33 a partir de 04/01/2027; diferença acima de 15% entre plataforma, analytics e CRM (investigar antes de decidir). Cada pausa vai como proposta ao humano, com o que, por que, quanto, efeito e como desfazer
- [ ] Relatório final contra as metas até 05/03/2027

---

## 10. Travas

| Trava | Efeito | Quem resolve |
|---|---|---|
| G6: página de Pedagogia com texto de modelo, egresso copiado e docentes de outro curso | Pedagogia não sobe | Equipe do site |
| G8: campo turno do noturno mostra "INTEGRAL" | Noturno não sobe | Equipe do site |
| G12: reajuste de dezembro pode mudar os valores de 2027/1 | Todo criativo com preço passa por ciclo extra se mudar | Financeiro e marketing |
| G13: URL, formulário, CRM e privacidade | Nenhum destino é final; nenhuma subida | Plataforma |
| G14: aprovador não nomeado | Ninguém aprova verba, anúncio ou peça com ato | Ufape |
| Datas do Enem 2026 e das notas | Semana E e pesos de verba só com data confirmada; sem anúncio no ar em 08 e 15/11 | Marketing |
| MP7 e G10: listas de contatos e menores | Sem semelhantes, sem exclusão por lista, sem API de Conversões com matrícula | Jurídico |
| MP15: meta de 15 contra turma mínima de 30 | Meta em reais não fechada; não muda o custo máximo | CEO |
| Tamanho mínimo do remarketing | Sem campanha de remarketing até atingir o mínimo | Gestor-de-midia |

---

## 11. Pedidos de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AM1 | Aprovar esta estrutura (1 campanha e 1 conjunto por curso e turno, público amplo 18+, orçamento na campanha, 3 conceitos) | Verba baixa não suporta mais campanhas; leitura limpa | sem custo | Montagem possível a partir de 11/11 | Nova versão do arquivo |
| AM2 | Montar o integral em pausa entre 11 e 13/11/2026, só depois de MP1, MP2, MP4, MP10 e G13 | Montagem é feita por humano e precisa de revisão antes do ar | R$ 0 até a ativação | Campanha pronta para 16/11 | Excluir o rascunho no gerenciador |
| AM3 | Ativar o integral em 16/11/2026 | Início da captação de 14 semanas | R$ 150,00 por semana na Meta nas 3 primeiras semanas (R$ 450,00 na fase 1) | Cerca de 22 leads por semana se o CPL ficar em R$ 6,67; sem promessa | Pausar a campanha, por humano |
| AM4 | Trocas de fase em 07/12, 04/01 e 01/02 | Cada fase muda mensagem e verba | R$ 225,00, R$ 525,00 e R$ 240,00 | Transição no prazo | Manter a campanha anterior |
| AM5 | Criar campanha de remarketing quando o público atingir o mínimo, com até 20% da verba semanal da campanha ampla [SUPOSIÇÃO] | Remarketing só com público suficiente | dentro da verba do curso | Lembrar quem viu a LP | Pausar e devolver a verba à ampla |
| AM6 | Montar e ativar o noturno quando G8 e MP4 estiverem resolvidos (MP8) | Página precisa mostrar o turno certo | metade da verba semanal do curso, dentro dos R$ 1.440,00 | Noturno no ar no dia seguinte | Pausar; a verba volta ao integral |
| AM7 | Montar e ativar a Pedagogia quando G6, MP4 e MP1 estiverem resolvidos (MP9) | Página com texto de modelo | R$ 2.000,00 no ciclo, conforme a seção 4 | Pedagogia no ar com meta escrita | Pausar a campanha |
| AM8 | Pausar todas as campanhas da Graduação em 22/02/2027 | Fim do ciclo | encerra o gasto | Relatório final até 05/03/2027 | Reativar no gerenciador |
| AM9 | Definir o limite de gasto da conta e das campanhas conforme a seção 4 | Travar a verba aprovada | R$ 4.000,00 na Graduação | Gasto nunca passa do aprovado | Alterar o limite, por humano |
| AM10 | Adotar o nome de anúncio com bloco de gancho (a, b, c) em vez de codificar o gancho no vN | Ajuste A-C1 do qa-d; D12 pede o gancho | sem custo | Atribuição limpa de gancho e iteração | Voltar ao padrão do plano v3 |
| AM11 | Verba extra, se a Meta não entregar os leads necessários depois de 2 semanas de dados | Regra: nunca gastar acima do aprovado | [CONFIRMAR]: 15 x custo por matrícula observado, menos o já gasto | Decisão informada | Manter os R$ 2.000,00 e aceitar a meta parcial |

---

## 12. Auditoria

auditorias/11-midia-paga.md
- [ ] Plano aprovado: pendente (aprovação humana)
- [x] Metas de CPL e custo por matrícula escritas antes de subir (seção 1); aprovação pendente (MP1)
- [ ] Verba e aprovador: pendente (MP2, G14)
- [x] Nomenclatura padrão em campanha, conjunto e anúncio (seções 2, 6 e 7)
- [ ] UTMs completas e origem no CRM: UTM definida; URL e chegada ao CRM pendentes (G13)
- [ ] Pixel e API de Conversões: [DADO NÃO FORNECIDO]
- [ ] Criativos aprovados em conformidade-educacional: dependem do qa de 10/11 (o qa-d aprovou o pacote com ajustes)
- [x] Políticas da Meta: sem atributo pessoal, sem urgência falsa, sem caixa alta
- [x] Nenhum público com menores de 18
- [x] Sem segmentação discriminatória; sem listas de contatos
- [x] Dados de curso do catálogo e dos editais
- [x] Destino de WhatsApp: não se aplica
- [x] Números só das fontes fornecidas; nenhum desempenho citado
- [x] Nada foi subido, alterado, pausado ou gasto

Conformidade educacional: texto de cada anúncio vem do pacote aprovado com ajustes no qa-d; Enem com a média mínima e "2010 em diante"; desconto com valor cheio, valor com desconto, percentual, validade e regra; ato só como no catálogo; nenhuma nota do MEC; Pedagogia sem carga horária. Pendentes externos: página (G6, G8), formulário e privacidade (G13), preço e ato (regulação). Resultado: rascunho pronto para o qa de 10/11.

---

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 por curso e meta de 15 matrículas por curso (decisões 15 e 16, docs/execucao-2026-10-26.md). Meta Medicina Veterinária R$ 1.440,00, Pedagogia R$ 2.000,00; distribuição semanal (gestor-de-midia v3, seção 3.3).
- Custo por matrícula máximo R$ 133,33 e CPL base R$ 6,67 (gestor-de-midia v3, seção 2).
- Integral de R$ 10.000,00 por R$ 5.000,00 (50%); noturno por R$ 4.000,00 (60%); Pedagogia de R$ 1.050,00 por R$ 525,00 (50%); só no 1º semestre de 2027 (catálogo, seção 1; editais 003/2026).
- Inscrição gratuita; redação online eliminatória, nota mínima 5,0; Enem com média mínima de 300 pontos, de 2010 em diante; aulas em 22/02/2027; turma mínima de 30; devolução de 80% até 2 dias antes das aulas; menor precisa do aceite do representante legal (editais 002 e 004/2026).
- Atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025); Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) (catálogo).
- Anúncio só para 18 anos ou mais (cmo-graduacao, G10).
- UTM: utm_medium=paid_social e utm_source=meta no pago da Meta; utm_campaign com prefixo grad_ (cmo-geral, D11 e D12).
- qa-d: criativos aprovados com ajustes A-C1 a A-C5.

## Lista 2. Suposições

- [SUPOSIÇÃO de cenário] Taxas de conversão do funil (20%, 40%, 50% e 10%, 12,5%, 20%), do gestor-de-midia, que dão os três CPLs.
- [SUPOSIÇÃO] Grande São Paulo e Goiânia com região metropolitana como área de entrega.
- [SUPOSIÇÃO de desenho] Divisão 50% e 50% entre turnos; exclusão cruzada entre turnos; até 20% da verba para remarketing; exclusão de convertidos por evento do pixel.
- [SUPOSIÇÃO] Evento Lead disparado pelo formulário da LP; janela de atribuição padrão.
- [SUPOSIÇÃO] Limites de 40 caracteres no título e 30 na descrição.
- [SUPOSIÇÃO do cmo] O gargalo do funil é o inscrito que não faz a redação.
- [SUPOSIÇÃO] Educação não é categoria especial de anúncio na Meta.

## Lista 3. Dados que faltam

- [CONFIRMAR] MP1, MP2, MP4, MP15 e aprovador nomeado (G14).
- [CONFIRMAR] G13: URL que recebe a UTM, se o formulário é inscrição, origem no CRM, política de privacidade.
- [DADO NÃO FORNECIDO] Estado do pixel e da API de Conversões; histórico de CPL; número de inscritos e matrículas.
- [CONFIRMAR] G6 (Pedagogia), G8 (turno do noturno), G12 (reajuste de dezembro), G10 e MP7 (menores e listas).
- [CONFIRMAR] Datas do Enem 2026 e das notas; data-limite interna de inscrição (G4).
- [CONFIRMAR NO CATÁLOGO] Carga horária da Pedagogia; nomes das disciplinas do 1º semestre; horário de prática e estágio do noturno.
- [CONFIRMAR] Tamanho mínimo do público de remarketing, limite de idade fixo no Advantage+ audience, limites de caracteres e categoria de anúncio, todos no gerenciador.
- [CONFIRMAR] Campanhas de Graduação rodando fora da planilha (MP14); período exato do ciclo (decisão 15).

---

## Próximo passo

Próximo agente: **anuncios-google** (busca de marca e genérica da Medicina Veterinária, R$ 560,00, com os RSA da seção 4 do criativos). Depois, qa-de-marketing em 10/11/2026 e aprovação humana antes de qualquer montagem.
