# Revisão de QA: apresentação do plano de marketing da Pós-graduação (exemplo 68606, com o UFAPE Cast)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 28/10/2026 (quarta-feira)
- **Peças revisadas:**
  - Os 20 slides publicados em /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/slides/, na ordem de deck.json: capa, indice, pracas, publico, curso, meta, verba, mensagem, canais, regua, docentes, podcast, episodio-funil, pauta, calendario, kit, decisoes, proximos, conclusao, anexo (texto visível e notas em aside).
  - O roteiro do cmo: /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md (inteiro, 582 linhas).
- **Entradas lidas (fontes primárias):**
  - /home/user/marketing-ufape/CLAUDE.md; /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 21 e regras)
  - /home/user/marketing-ufape/contexto/ufape-geral.md; /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha inteira, inclusive a lista "Participantes")
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (cabeçalho, regras e seção 2, linha 68606)
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json
  - /home/user/marketing-ufape/docs/insumos/tgh-plano-de-campanhas-cursos-tier1-v2.txt (26 slides)
  - /home/user/marketing-ufape/docs/insumos/ufape-podcast-proposta-2026-10-28.txt (26 páginas)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (seções 0 a 13, versão 7)
  - /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (seções 0, 1, 6A, 7 e 8)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (seções 0, 1, 6 e 7)
  - /home/user/marketing-ufape/saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md (seções 0, 6 e 11)
  - /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md (seções 0, 0.2, 0.3 e 6)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md (seções 0 a 8)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 13: 13.1 a 13.4 e listas)
  - /home/user/marketing-ufape/auditorias/02-estrategia-e-posicionamento.md; /home/user/marketing-ufape/auditorias/conformidade-educacional.md
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web. Nenhum slide e nenhuma linha do roteiro foram editados.
- **Dados pessoais:** nenhum. Docentes citados só com nome e titulação como estão na ficha.

---

## 1. Veredito

**CORRIGIR.**

A apresentação é fiel ao roteiro e às fontes na maior parte dos números, mas não passa em quatro itens de auditorias/conformidade-educacional.md (modalidade clara, preço com condições completas, urgência real e autorização de imagem) e, na passagem do roteiro para os slides, perdeu marcas e condições que mudam o sentido (teto da verba "se G = 0", nome do podcast "em aprovação", "com o ok dele" no card do convidado, teto de mensagens como "de mercado"). Pela regra do agente, qualquer item da conformidade sem marcação leva a CORRIGIR, sem exceção.

São 21 achados: 14 bloqueiam (B) e 7 são ajustes (A). Depois das correções, a apresentação volta ao qa só para os itens F1 a F21; o resto já está conferido nesta revisão.

---

## 2. O que foi conferido e bate com a fonte

### 2.1 Contas

| Conta | Valor no slide e no roteiro | Conferência | Resultado |
|---|---|---|---|
| Custo máximo por matrícula | R$ 133,33 (meta, conclusao) | R$ 2.000,00 / 15 = R$ 133,333 | Certo |
| Meta em reais | R$ 531.000,00 (meta) | 15 x R$ 35.400,00 = R$ 531.000,00 | Certo |
| Vezes a verba | 265,5 (slide) e 265,50 (roteiro) | R$ 531.000,00 / R$ 2.000,00 = 265,50 | Certo |
| Divisão por praça | R$ 600, R$ 500, R$ 400, R$ 280, R$ 220 (verba) | 30%, 25%, 20%, 14% e 11% de R$ 2.000,00; soma R$ 2.000,00; igual ao deck, slide 22 | Certo |
| Dias do ciclo | 87 dias (calendario) | 28/10/2026 a 22/01/2027: 4 + 30 + 31 + 22 = 87 | Certo |
| Dias de fim de ano | 14 (aside de verba) | 21/12 a 31/12 (11) + 01/01 a 03/01 (3) = 14 | Certo |
| Dias equivalentes | 80 | 87 menos 14 / 2 = 80 (gestor, 13.1) | Certo |
| Diária com G = 0 | R$ 25,00 (R$ 12,50 no fim de ano) | R$ 2.000,00 / 80 | Certo |
| Fase 1 | R$ 250,00 | 28/10 a 06/11 = 10 dias x R$ 25,00 | Certo |
| Fase 2 | R$ 1.750,00 | 07/11 a 22/01 = 77 dias; 63 x R$ 25,00 + 14 x R$ 12,50 = R$ 1.575,00 + R$ 175,00 | Certo |
| Fase 1 por praça | R$ 75,00; R$ 62,50; R$ 50,00; R$ 35,00; R$ 27,50 | percentuais x R$ 250,00; soma R$ 250,00 | Certo |
| Fase 2 por praça | R$ 525,00; R$ 437,50; R$ 350,00; R$ 245,00; R$ 192,50 | percentuais x R$ 1.750,00; soma R$ 1.750,00 | Certo |
| Fase 1 + fase 2 por praça | colunas | 75 + 525 = 600; 62,50 + 437,50 = 500; 50 + 350 = 400; 35 + 245 = 280; 27,50 + 192,50 = 220 | Certo |
| Diária por praça | R$ 2,75 a R$ 7,50 (aside de verba) | 11% e 30% de R$ 25,00 | Certo |
| Cenários do funil | 25/500/R$ 4,00; 20/200/R$ 10,00; 17/112/R$ 18,00 | iguais ao gestor, 12.3; no otimista, 112 leads x R$ 18,00 = R$ 2.016,00 (ver F14) | Certo, com ressalva F14 |
| Base da praça | 8.016 = 76,7% de 10.447; SP 5.151 = 49,3% | 2.900 + 2.251 + 947 + 1.099 + 819 = 8.016; 8.016 / 10.447 = 76,73%; Sul 386 + 371 + 342 = 1.099 | Certo |
| SP com 55% da verba | conclusao | 30% + 25% | Certo |
| Critério do AP-4 | R$ 3,86 por dia | 1,5 x R$ 18,00 = R$ 27,00 por semana / 7 = R$ 3,857 | Certo (ver F20 sobre a origem) |
| Contagem de titulação | 17 Dr./Dra., 12 MSc., 6 Esp., 3 Profa. (docentes) | contagem própria das 38 linhas da lista "Participantes" da ficha: 17 + 12 + 6 + 3 = 38 | Certo |

### 2.2 Datas, dias da semana e dados de curso

- Catálogo, linha 68606: Pós-graduação em Gastroenterologia Veterinária, São Paulo, Semipresencial, 07/11/2026, turma IX, 500 h, 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00; aberto. Bate com curso.html, meta.html e com pos-68606.json.
- Ficha: 24 módulos; módulo 1 em 07 e 08/11/2026, 2 em 19 e 20/12/2026 e 3 em 23 e 24/01/2027, todos online; presenciais nos módulos 6 (17 e 18/04/2027), 13 (27 e 28/11/2027) e 21 (julho de 2028), com os temas citados; fim em 28 e 29/10/2028; temas de laboratório (módulo 3), imagem (5 e 8) e luto e burnout (24); coordenação Esp. Maria Carolina Pappalardo; 38 nomes. Tudo bate.
- Dias da semana conferidos a partir de qua 28/10/2026: qui 29/10, ter 03/11, qui 05/11, sex 06/11, sáb 07/11, ter 24/11, qua 02/12, ter 08/12, qua 16/12, sáb 19/12, ter 22/12, ter 05/01, ter 12/01, ter 19/01, sex 22/01, sáb 23/01, seg 25/01, ter 02/02, seg 22/02; revisões de segunda de 09/11 a 18/01. Todos certos.
- Docentes, com a grafia da ficha: Esp. Maria Carolina Pappalardo, Dr. Rodolfo Oliveira Leal, DRA. VIVIANE DE MARCO, DR. Fabrizio Grandi, DRA. Maria Anete Lallo, Dra. Cibele Figueira Carvalho; "Profa. Ísis Carvalho" e "ESP. Isis de Carvalho Rodrigues Santana Lemes" como possível duplicidade. Todos certos.
- Deck da The Growth Hub: cadastros, percentuais, CPA de R$ 210,51 na conta e R$ 168,50 na Imersão Cirurgia (GO), público base, idade mínima 20 e sugestão de 22 a 35, exemplo de SP com 4,7 a 5,5 milhões, criativo abreviado e as três colunas PRIORIZAR, TESTAR e CONECTAR. Todos certos.
- Proposta do podcast: nome recomendado UFAPE Cast e as outras cinco opções, subtítulo, assinatura, três públicos, objetivo, quadros, roteiro de 0 a 45 minutos, pacote por episódio, YouTube e Spotify, PodVet como referência editorial e as cores #056382, #6687A6 e #B6CADB. Todos certos.
- Saídas de 26/10: régua de 6 toques da 68606 (T1, T2, W2, E2, W3, W4, datas e assuntos), frase da regra, 10 respostas do time, ganchos A6-09, A6-03 e A6-02, promessa e pilares da área A6, AD-A6-1 em S3 (09 a 15/11), OA4, OA8 (37 em lacuna), OA9, OA10, R3 de 1,5 x CPL e 3 dias, 30 dias de maturação. Todos certos.

### 2.3 Regras do pedido

| Regra | Resultado | Onde |
|---|---|---|
| Nenhum travessão nem meia-risca | Atende na leitura integral dos 20 slides e do roteiro; nenhum encontrado. A conferência por busca dos caracteres U+2014 e U+2013 fica com o orquestrador, como diz o próprio roteiro | todos |
| Nunca "certificado/reconhecido pelo MEC" | Atende. O único uso é descritivo ("frase de certificação ligada ao MEC", como problema da página) | kit, decisoes |
| TGH nunca chamada de agência | Atende. Sempre "The Growth Hub" | todos |
| Nada de dado pessoal | Atende | todos |
| Preço só como uso interno | Falha em decisoes.html (F12); falta condição em curso.html (F3) | curso, decisoes |
| Nada de urgência sem número real | Falha no exemplo de remarketing (F1) | mensagem |
| Sempre "Pós-graduação em" no nome | Falha em notas de pauta.html e mensagem.html (F15) | pauta, mensagem |
| Nome exato do evento | Atende: "Workshop Brasileiro de Neuromonitorização" em regua.html e calendario.html; nenhum "simpósio" | regua, calendario |

---

## 3. Achados

Legenda: **B** bloqueia (falha de conformidade, regra do pedido, marca [SUPOSIÇÃO] ou [CONFIRMAR] perdida, ou mudança de sentido); **A** ajuste (precisão ou clareza, sem mudar o sentido). Quando o mesmo erro está no roteiro, a correção vale para os dois arquivos.

### F1 (B) Exemplo de remarketing com a data do 3º módulo sem a regra completa
- **Slide:** mensagem.html, card "A partir de 07/11 · remarketing [SUPOSIÇÃO]".
- **Texto atual:** "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo; nesta turma, ele começa em 23/01/2027."
- **Problema:** a frase da regra (decisão 18; regra 6 do plano da onda 1; copy-de-mensagens, 1.4) vai sempre inteira, em bloco. O slide corta "Antes de pagar, o time explica como ficam os módulos que já aconteceram" (levada só para a nota) e troca "do curso" e "o 3º módulo" por "ele". Do jeito que está, a data do 3º módulo aparece sem a regra completa: falha o item "urgência é real" e o item de anúncios "sem urgência ou escassez falsa".
- **Correção exata:** trocar o texto do card por "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram." e apagar da nota a frase "O remarketing completa: "Antes de pagar, o time explica como ficam os módulos que já aconteceram."".

### F2 (B) Exemplo de anúncio até 06/11 sem modalidade e sem as condições
- **Slide:** mensagem.html, card "Até 06/11 · texto [SUPOSIÇÃO], passa pelo qa".
- **Texto atual:** "Pós-graduação em Gastroenterologia Veterinária para médicos veterinários formados. Turma IX em São Paulo, início em 07/11/2026, 3 módulos presenciais de prática."
- **Problema:** o resumo tirou "o módulo 1 online" e "Teoria online", então o anúncio fala só de presencial num curso semipresencial (falha o item "modalidade está clara e correta"); tirou também a data do 1º presencial e "Veja parcelas, total e matrícula na página da turma", que é a forma de citar condições sem preço (regra 7 do plano da onda 1). O roteiro tem o texto certo.
- **Correção exata:** "Pós-graduação em Gastroenterologia Veterinária para médicos veterinários formados. Turma IX em São Paulo, com início em 07/11/2026 e o módulo 1 online. Teoria online e 3 módulos presenciais de prática, o primeiro em 17 e 18/04/2027. Veja parcelas, total e matrícula na página da turma."

### F3 (B) Preço sem a condição completa
- **Slide:** curso.html, card "Investimento · uso interno".
- **Texto atual:** "30x de R$ 1.180,00 ou R$ 35.400,00; matrícula de R$ 250,00 no site. Inscrição de R$ 260,00 [CONFIRMAR U11]."
- **Problema:** o roteiro promete "preço com a condição completa" e o slide perdeu "no cartão ou boleto" (texto do catálogo) e a condição da 1ª mensalidade ("1ª mensalidade paga até 30 dias antes do início, segundo a página"), que a auditoria pede junto do preço (item "preço mostra valor, número de parcelas e condições completas") e que o gestor pede na conferência da página (M1 do qa onda2c). Também sumiu "nunca em peça até a U11" do texto visível.
- **Correção exata:** "30x de R$ 1.180,00 ou R$ 35.400,00 no cartão ou boleto, mais matrícula de R$ 250,00 no site; 1ª mensalidade paga até 30 dias antes do início, segundo a página. O CEO informou inscrição de R$ 260,00: a diferença é [CONFIRMAR U11]. Nunca em peça até a U11."

### F4 (B) Verba por fase apresentada como plano, sem "teto se G = 0" e sem [SUPOSIÇÃO]
- **Slide:** verba.html (título, cabeçalho da tabela e nota de rodapé).
- **Texto atual:** título "Mesma divisão do deck, com R$ 2.000,00 e duas fases."; colunas "Até 06/11" e "07/11 a 22/01".
- **Problema:** o roteiro diz "com a verba que sobrar do ciclo" e as colunas dizem "teto se G = 0". A 68606 já gasta desde antes da decisão 15 (G é [CONFIRMAR, PP15]); o slide faz parecer que os R$ 2.000,00 estão inteiros e que R$ 250,00 e R$ 1.750,00 são o plano. Perdeu também a marca do roteiro: "Valores por fase (...): conta do cmo sobre a fórmula do gestor, com G = 0; teto, não meta" está na lista [SUPOSIÇÃO], e o meio dia de 21/12 a 03/01 é [SUPOSIÇÃO de desenho] do gestor (13.1).
- **Correção exata:**
  - Título: "Mesma divisão do deck, com a verba que sobrar do ciclo."
  - Colunas: "Fase 1 (28/10 a 06/11), teto se G = 0" e "Fase 2 (07/11 a 22/01), teto se G = 0".
  - Rodapé da tabela: "Teto, não meta [SUPOSIÇÃO do cmo sobre a fórmula do gestor, 13.1; o meio dia de 21/12 a 03/01 é suposição de desenho do gestor]. Verba real de cada praça = (R$ 2.000,00 menos G) x o percentual. G, gasto já feito no ciclo: [CONFIRMAR PP15]."

### F5 (B) Teto de mensagens chamado de "teto de mercado"
- **Slide:** regua.html, título. **Roteiro:** slide 10, título e primeiro item ("Teto (D16, decisão do cmo com referência de mercado)").
- **Texto atual:** "Seis mensagens até 12/01, dentro do teto de mercado."
- **Problema:** a seção 13 do plano geral diz o contrário: "Não existe referência publicada com um número de mensagens por semana" e o número do D16 é [SUPOSIÇÃO] do cmo, calibrado por limites de alerta com fonte (decisão 17). O título apaga a marca e afirma uma referência que não existe. A própria nota do slide diz "nenhuma fonte publica um número".
- **Correção exata:**
  - Título do slide: "Seis mensagens até 12/01, dentro do teto D16."
  - Abaixo de "2 + 2 por semana", acrescentar: "Número [SUPOSIÇÃO do cmo, D16], revisto pelos limites de alerta com fonte."
  - Roteiro, slide 10: trocar "Teto (D16, decisão do cmo com referência de mercado)" por "Teto (D16, decisão do cmo; número [SUPOSIÇÃO], calibrado pelos limites de alerta com fonte da seção 13.4)".

### F6 (A) Limites de alerta citados sem a regra exata
- **Slide:** regua.html, nota. **Roteiro:** slide 10, "Por que esse número".
- **Texto atual:** "spam no Gmail abaixo de 0,10%, descadastro acima de 0,17% por envio (média do Brasil)".
- **Problema:** na tabela 13.4 o alerta de descadastro é "acima de 0,17% (média do Brasil) em 2 envios seguidos da mesma régua" e o corte é "acima de 0,34% em 1 envio [SUPOSIÇÃO do fator 2]"; no Gmail, alerta com 0,10% ou mais e corte com 0,30% ou mais.
- **Correção exata:** "alerta com spam no Gmail de 0,10% ou mais (corte com 0,30%); alerta com descadastro acima de 0,17% (média do Brasil) em 2 envios seguidos da mesma régua (corte acima de 0,34% em 1 envio [SUPOSIÇÃO do fator 2]); qualidade do número do WhatsApp em amarelo (corte em vermelho)".

### F7 (B) "10 peças" e "todas levam à página da turma"
- **Slide:** episodio-funil.html, título e nota; anexo.html, nota do AP-2. **Roteiro:** slide 13 (título), slide 20 (AP-2) e lista [SUPOSIÇÃO] ("Contagem de cerca de 10 peças por episódio (pacote da decisão 21 mais episódio, áudio e link na newsletter)").
- **Texto atual:** "Um episódio vira 10 peças, e todas levam à página da turma."
- **Problema:** (1) "todas levam à página da turma" não é verdade no próprio plano: o episódio 3 sai "sem chamada de turma", o link na resposta 1 a 1 leva ao episódio e, depois de 22/01, o episódio aponta para a próxima turma ou para o conteúdo da Pós. (2) A conta não fecha com a origem dada no roteiro: o pacote da decisão 21 sozinho já soma 10 (3 cortes + 3 capas + 1 card 4:5 + 2 Stories + 1 card do convidado); com episódio, áudio e link na newsletter seriam 13.
- **Correção exata:**
  - Título: "Um episódio vira 10 peças de divulgação, e as chamadas de turma levam à página da turma."
  - Nota do slide e nota do AP-2: "Contagem: 10 peças = pacote da decisão 21 (3 cortes verticais, 3 capas verticais, 1 card 4:5, 2 Stories e 1 card do convidado); episódio, áudio e link na newsletter ficam fora da conta [SUPOSIÇÃO de contagem]. Em 5 episódios, cerca de 50 peças."
  - Roteiro, lista [SUPOSIÇÃO]: trocar o item por "Contagem de 10 peças por episódio: só o pacote da decisão 21 (3 + 3 + 1 + 2 + 1); episódio, áudio e newsletter fora da conta."

### F8 (B) Condições de aprovação perdidas na tabela do funil do podcast
- **Slide:** episodio-funil.html, tabela.
- **Texto atual e correção exata:**
  - Linha "1 card do convidado", coluna Regra: de "conta como post de docente" para "conta como post de docente, com o ok dele (checklist C1 a C8 da autoridade-docente-pos)". O roteiro tem "com o ok dele"; o slide perdeu a condição de autorização.
  - Linha "1 card 4:5", coluna Regra: de "troca uma peça, não soma" para "só com aprovação (AP-4): troca uma peça, não soma". O roteiro tem "só com aprovação".
  - Linha "Episódio completo", coluna Regra: de "notas com nome e titulação, UTM" para "notas com nome e titulação da ficha, link com UTM e transcrição revisada".

### F9 (A) Suposição do card do convidado como post de docente: decisão do qa
- **Slide:** docentes.html. **Roteiro:** slide 11 e lista [SUPOSIÇÃO].
- **Texto atual:** "cada convidado ganha o card do convidado e um corte com o nome dele [SUPOSIÇÃO, a confirmar no qa]."
- **Decisão do qa:** aceito com condição. O kit pede 1 post por docente autorizado; o card do convidado e o corte com o nome contam juntos como **1** post de docente do kit, só para docente da ficha (egresso e convidado de fora não contam) e só quando seguem o checklist C1 a C8 da autoridade-docente-pos (texto inteiro aprovado por ele, nome e titulação da ficha, opinião dele, revisão clínica dele, chamada para a turma ou para a próxima da área com UTM, nenhum paciente identificável).
- **Correção exata:** "cada docente da ficha convidado ganha o card do convidado e um corte com o nome dele, que contam juntos como 1 post de docente do kit quando seguem o checklist C1 a C8 da autoridade-docente-pos (critério do qa, 28/10/2026)." No roteiro, tirar o item da lista [SUPOSIÇÃO] e citar esta revisão como fonte.

### F10 (B) Situação do kit: aprovação errada e plano dos 8 canais desatualizado
- **Slide:** kit.html, coluna "Escrito · qa aprovado" e coluna "Inventário pendente". **Roteiro:** slide 16.
- **Texto atual:** "Aguardam a aprovação humana (OA9)." e "Prazos de 03 a 05/11 (OA11)."
- **Problema:** (1) o OA9 aprova só envios de WhatsApp e e-mail; plano dos 8 canais e plano de mídia esperam a aprovação do plano da onda 1 (pos-68606.json: "aguardando_aprovacao"). (2) O plano dos 8 canais aprovado pelo qa é o da seção 5 do cmo-pos-2026-10-26, com podcast e YouTube "Fora"; a apresentação muda os dois para ativos (decisão 21), e essa mudança só passa pelo qa nesta revisão. (3) OA11 é só a publicação dos 6 posts; criativos e roteiro têm prazo em 05/11 e o post de docente em 29/10 (cmo-pos, 4.3). (4) Sumiu o acréscimo "inventário do kit, prazo 28/10 (OU5)" do roteiro.
- **Correção exata:**
  - Rodapé da coluna 1: "Plano dos 8 canais e plano de mídia aguardam a aprovação do plano da onda 1; WhatsApp e e-mails, o OA9. A versão do plano dos 8 canais aprovada pelo qa tem podcast e YouTube fora; a mudança da decisão 21 (slide 09) depende desta revisão e da aprovação humana."
  - Rodapé da coluna 2: "Prazos: posts em 03/11 (OA11); criativos e roteiro em 05/11; post de docente em 29/10."
  - Coluna 3: acrescentar o item "Inventário do kit (prazo 28/10, resposta da Ufape OU5)".

### F11 (B) Nome do podcast sem a marca "em aprovação" na tabela de canais
- **Slide:** canais.html, linha do podcast; linha do Instagram.
- **Texto atual:** "Podcast (UFAPE Cast)"; Instagram: "6 posts do kit, Stories de docente, anúncios Meta e cortes do podcast".
- **Problema:** pela decisão 21, UFAPE Cast é nome "ainda para aprovação", e o roteiro escreve "nome em aprovação". O slide perdeu a marca. No Instagram, perdeu "nos slots que a grade da Pós já tem", que é a condição de não passar o teto D5.
- **Correção exata:** "Podcast (UFAPE Cast, nome em aprovação)"; Instagram: "6 posts do kit, Stories de docente, anúncios Meta e cortes do podcast, nos slots que a grade da Pós já tem".

### F12 (B) Preço fora do slide interno sem a marca "uso interno"
- **Slide:** decisoes.html, item 5. **Roteiro:** cabeçalho (linha "Formato") e slide 17, item 5.
- **Texto atual:** "Valor da inscrição: R$ 260,00 ou R$ 250,00 (U11)"; no cabeçalho do roteiro, "preço aparece só no slide 5".
- **Problema:** valores aparecem também no slide 6 (marcado "uso interno", certo) e no slide 17 (sem marca). O cabeçalho do roteiro promete algo que o próprio roteiro não cumpre.
- **Correção exata:** slide 17, item 5: "Valor da inscrição: R$ 260,00 ou R$ 250,00 (U11) · uso interno". Roteiro, cabeçalho: "preço aparece nos slides 5 (condição completa), 6 (meta em reais) e 17 (U11), sempre com a marca "uso interno"".

### F13 (A) "9 dias do início"
- **Slide:** verba.html ("não abrir cinco campanhas a 9 dias do início") e anexo.html, nota do AP-1 ("9 dias até o início"). **Roteiro:** slides 7 e 20.
- **Problema:** de 28/10 a 07/11 são 10 dias, a mesma contagem do mapa da turma (dias_ate_inicio = 11 em 27/10) e da fase 1 (10 dias).
- **Correção exata:** "a 10 dias do início" e "10 dias até o início".

### F14 (A) Slide de meta: arredondamento do otimista, marca e frase do risco
- **Slide:** meta.html.
- **Texto atual e correção exata:**
  - Etiqueta da tabela: de "Exemplo ilustrativo · taxas são suposição" para "[SUPOSIÇÃO ilustrativa] taxas sem histórico", no padrão visual do roteiro.
  - Nota: acrescentar "No otimista, a conta dá 111,11 leads (112 na prática, gestor 12.3); o CPL máximo de R$ 18,00 vem da conta exata (R$ 133,33 x 15% x 90%); com 112 leads inteiros, R$ 17,86."
  - Card "A conta fecha?": de "Com CPL acima de R$ 18,00 por 2 semanas, a meta não fecha só com mídia." para "Com CPL acima de R$ 18,00 por 2 semanas fechadas, a meta não fecha só com mídia em nenhum dos três cenários." e de "O que esse CPA mede: [CONFIRMAR]." para "O que esse CPA mede: [CONFIRMAR com a The Growth Hub]."

### F15 (B) Nome de curso fora do padrão "Pós-graduação em"
- **Slide:** pauta.html, nota; mensagem.html, nota (gancho A6-02). **Roteiro:** slide 14 (tabela e fonte) e slide 8 (A6-02).
- **Texto atual:** "na Pós de Diagnóstico por Imagem (68604)"; "na Pós de Patologia Clínica (68615)"; "Cirurgia esofágica, gástrica e intestinal na pós de Gastroenterologia? Veja o presencial".
- **Correção exata:** "na Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária (68604)"; "na Pós-graduação em Patologia Clínica (68615)"; "Cirurgia esofágica, gástrica e intestinal na Pós-graduação em Gastroenterologia Veterinária? Veja o presencial". Nota para o criador-de-ganchos (arquivo não editado): o A6-02 precisa da mesma troca antes de virar carrossel.

### F16 (B) Pauta sem a autorização do egresso e sem a regra do nome do evento
- **Slide:** pauta.html, rodapé da tabela e nota.
- **Texto atual:** "Datas [SUPOSIÇÃO]. Tema, agenda, egresso e convidados de fora [CONFIRMAR]."
- **Problema:** o roteiro marca "egresso de pós da Ufape [CONFIRMAR nome e autorização]"; a decisão 21 mantém autorização de imagem por episódio em [CONFIRMAR]. A nota também perdeu a regra "o evento de 20 e 21/11, se citado, é o "Workshop Brasileiro de Neuromonitorização"".
- **Correção exata:** rodapé: "Datas [SUPOSIÇÃO]. Tema e agenda de cada docente, nome do egresso e convidados de fora, com autorização de imagem por episódio: [CONFIRMAR] (decisão 21)." Nota, no fim das regras de pauta: "o evento de 20 e 21/11, se citado, é o "Workshop Brasileiro de Neuromonitorização"."

### F17 (B) Recomendação do deck apresentada como fato
- **Slide:** proximos.html, coluna "Conectar".
- **Texto atual:** "Dashboards da The Growth Hub cruzam tudo."
- **Problema:** no deck (slide 25) é "RECOMENDAÇÃO"; o roteiro escreve "Recomendação do deck" e marca as ferramentas da Ufape como [CONFIRMAR]. O slide afirma que o cruzamento já acontece.
- **Correção exata:** "Recomendação do deck: dashboards e sistemas da The Growth Hub para cruzar toda semana campanhas, CRM e comercial. Ferramentas de CRM e analytics da Ufape: [CONFIRMAR]."

### F18 (A) Calendário: fim de ano e módulo 1
- **Slide:** calendario.html.
- **Texto atual e correção exata:**
  - "21/12 a 03/01 · Sem mensagem · mídia pela metade" para "Sem mensagem de campanha · mídia só no remarketing, diária pela metade [SUPOSIÇÃO do gestor, 13.1]". Mensagem de serviço continua permitida (D16, regra de serviço).
  - "07 e 08/11 · Módulo 1 · início da turma" para "Módulo 1, online · início da turma".

### F19 (A) "Matrícula aceita até aqui" sem a pendência OU6
- **Slide:** curso.html, bandeira do módulo 3.
- **Texto atual:** "matrícula aceita até aqui".
- **Correção exata:** "matrícula até o 3º módulo (véspera ou 1º dia: [CONFIRMAR OU6])".

### F20 (B) Critério do AP-4 emprestado de outra turma sem marca
- **Slide:** anexo.html, nota do AP-4. **Roteiro:** slide 20, coluna Quanto do AP-4.
- **Texto atual:** "só se a diária da turma for de pelo menos R$ 3,86 (critério do gestor, 13.4)".
- **Problema:** a seção 13.4 do gestor é o critério do vídeo de 68610. Aplicar à 68606 é escolha do cmo e precisa da marca.
- **Correção exata:** "só se a diária da turma for de pelo menos R$ 3,86 (critério do gestor para o vídeo de 68610, 13.4, aplicado à 68606 por analogia [SUPOSIÇÃO do cmo])".

### F21 (A) Pilar 3 sem a prova da turma mínima
- **Slide:** mensagem.html, "Pilar 3 · Condições claras".
- **Texto atual:** "Parcelas, total e matrícula na página, sem preço no anúncio."
- **Correção exata:** "Parcelas, total e matrícula na página da turma, e a turma pode não ser formada; sem preço no anúncio." (casa de mensagens, pilar 3, e roteiro, slide 8).

---

## 4. auditorias/02-estrategia-e-posicionamento.md (aplicada à apresentação e ao roteiro)

| Item | Resultado | Observação |
|---|---|---|
| O plano tem uma única meta principal | Atende | pelo menos 15 matrículas (1ª mensalidade paga) na 68606 (decisão 16) |
| Persona e curso ou oferta estão nomeados | Atende | Pós-graduação em Gastroenterologia Veterinária (68606); público base do deck; persona da linha [SUPOSIÇÃO] |
| Os 8 canais avaliados; ativos cabem na capacidade; os de fora com justificativa | Atende com correção | F10 e F11; capacidade de produção do podcast segue [CONFIRMAR] |
| O posicionamento nomeia a alternativa real | Não atende (pendente) | herdado da casa de mensagens; o posicionamento da linha em ufape-geral.md está em branco; a alternativa só aparece no episódio reserva |
| Todo pilar tem prova | Atende com ajuste | F21 |
| Regras de voz com exemplos | Não atende (pendente na Ufape) | voz em ufape-geral.md ainda é [SUPOSIÇÃO] |
| Cabe no tempo e na verba | Atende com correção | F4: a verba real depende de G [CONFIRMAR PP15]; produção do podcast fora da verba, custo [CONFIRMAR] |
| Nenhuma promessa de emprego, aprovação ou salário | Atende | |
| Preços e condições do catálogo ou [CONFIRMAR NO CATÁLOGO] | Atende com correção | valores batem com o catálogo; F3 e F12 |

---

## 5. auditorias/conformidade-educacional.md, item por item

A apresentação é interna, mas traz exemplos de peças (anúncio, remarketing, Stories, cortes) que vão a público depois. Os itens valem para esses exemplos e para os dados citados.

| Bloco | Item | Resultado | Onde e por quê |
|---|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atende | 500 h, semipresencial, turma IX, 07/11/2026, 24 módulos até 28 e 29/10/2028 |
| Dados do curso | Status "aberto" no catálogo (ou não chama para inscrição) | Atende | "aberto"; depois do início, exceção do contexto da linha, que exige a regra completa (ver F1) |
| Dados do curso | Modalidade clara e correta | **Não atende** | F2: o exemplo de anúncio fala só dos presenciais |
| Regulação | Graduação: ato do catálogo | Não se aplica | linha pos |
| Regulação | Pós lato sensu sem "reconhecida pelo MEC"; texto de validade aprovado | Atende | nenhuma frase de certificação; o texto oficial não existe e nada é afirmado |
| Regulação | Curso livre sem diploma | Não se aplica | |
| Regulação | Nota MEC só com fonte oficial | Atende | nenhuma nota |
| Promessas e provas | Sem promessa de emprego, salário, aprovação ou sucesso | Atende | |
| Promessas e provas | Empregabilidade e satisfação com fonte | Não se aplica | nenhum dado desse tipo |
| Promessas e provas | Superlativos só com fonte | Atende | "especialidade emergente" e "referências nacionais" ficam fora |
| Promessas e provas | Comparação com concorrente | Não se aplica | nenhuma |
| Preço e condições | Valor, parcelas e condições completas | **Não atende** | F3 (sem "no cartão ou boleto" e sem a condição da 1ª mensalidade); F12 (valor sem "uso interno") |
| Preço e condições | Bolsa e desconto com regra | Atende | nenhuma bolsa, prova ou desconto |
| Preço e condições | Urgência real | **Não atende** | F1: data do 3º módulo sem a regra completa |
| Preço e condições | Prouni, Fies ou financiamento | Não se aplica | |
| Pessoas e dados | Autorização de uso de imagem de alunos e professores | **Não atende** | docentes atendem (decisões 8 e 10); F8 (card do convidado sem "com o ok dele") e F16 (egresso sem autorização marcada) |
| Pessoas e dados | Menores de idade | Não se aplica | Pós, público formado |
| Pessoas e dados | Formulários com finalidade e política de privacidade | **Não atende (pendente externo)** | p04 do mapa da 68606; bloqueia as peças, não a leitura interna |
| Pessoas e dados | WhatsApp e e-mail só com consentimento e saída fácil | Atende | opt-in por canal, SAIR e descadastro em um clique; o podcast não cria toque novo |
| Pessoas e dados | Nenhum dado pessoal | Atende | |
| Plataformas | Políticas da Meta e do Google, sem segmentação discriminatória | Atende no desenho | público por formação e cargo; idade como faixa de partida, sem atributo sensível |
| Plataformas | Página de destino entrega o que a peça promete | **Não atende (pendente externo)** | OA10: a página tem "CERTIFICADO PELO MEC", turma mínima de 20 e não traz a regra do 3º módulo |
| Anúncios | Sem característica pessoal de quem vê | Atende | "para médicos veterinários formados" descreve o público do curso |
| Anúncios | Sem urgência falsa, contador ou imitação da interface | **Não atende** | mesmo motivo de F1 |
| Anúncios | Sem pessoa pública ou parceria inexistente | Atende | |
| Anúncios | Sem caixa alta excessiva ou símbolos | Atende | caixa alta só em nomes, como estão na ficha, nas notas |
| Anúncios | Página carrega, domínio esperado, dados da Ufape, contato e privacidade | **Não atende (pendente externo)** | p04 e OA10 |
| Anúncios | Sem sugestão para driblar a análise das plataformas | Atende | |

**Resultado:** Bloqueado. Itens que precisam mudar: modalidade (F2), preço (F3, F12), urgência (F1), autorização (F8, F16). Pendentes externos que seguem bloqueando as peças, não a apresentação: política de privacidade (p04) e página de destino (OA10).
**Revisado por:** qa-de-marketing (agente). Revisão humana: pendente.
**Data:** 28/10/2026.

---

## 6. Observações para outros arquivos (não editados)

- **pos-68606.json:** o campo "canais" ainda traz podcast "fora", YouTube "ativo" sem a condição de orgânico e LinkedIn "teste". Pela decisão 21 e pelo slide 09, o mapa precisa de uma nova revisão pelo orquestrador (podcast ativo como motor de conteúdo; YouTube só orgânico; LinkedIn fora). Até lá, o mapa e a apresentação divergem.
- **Rodapé:** o roteiro define o rodapé "UFAPE · Plano de marketing da Pós-graduação · Exemplo: Pós-graduação em Gastroenterologia Veterinária, turma IX"; os slides usam "Exemplo: turma 68606". Não bloqueia; vale alinhar ao roteiro se houver espaço.
- **Capa:** "Squad de marketing da Ufape, sobre o plano de campanhas da The Growth Hub" saiu do texto visível e foi para a nota. Não bloqueia.
- **criador-de-ganchos-pos:** A6-02 com "pós de Gastroenterologia" (F15).

---

## 7. Próximo passo

A apresentação **volta para o agente que a produziu** (cmo, com o orquestrador que montou os slides) para aplicar F1 a F21 nos slides e, onde indicado, no roteiro. Depois, nova conferência do qa só desses itens. Ela não segue para a aprovação humana nesta versão. Nada foi publicado, enviado ou pago.

---

## Fatos (com fonte)

- Linha 68606 do catálogo: São Paulo, semipresencial, 07/11/2026, turma IX, 500 h, 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00; aberto (contexto/catalogo-de-cursos.md, seção 2).
- Cronograma, docentes (38, com 17 Dr. ou Dra., 12 MSc., 6 Esp. e 3 Profa.), endereço, turma mínima de 20 na página e "CERTIFICADO PELO MEC" na página; 1ª mensalidade até 30 dias antes do início (ficha 68606).
- R$ 133,33, R$ 531.000,00, 265,50 vezes, cenários de R$ 4,00, R$ 10,00 e R$ 18,00 (112 leads na prática no otimista), 80 dias equivalentes e R$ 25,00 por dia com G = 0, R3 de 1,5 x CPL e 3 dias, R$ 3,86 no critério de 68610 (gestor-de-midia-pos, seções 8, 12.2, 12.3, 13.1 e 13.4).
- D16 sem referência de frequência publicada; limites de 13.4 (cmo-geral, seção 13).
- Cadastros, percentuais, CPA, público base, criativo abreviado e recomendação de dashboards (deck da The Growth Hub, slides 3 a 9, 12, 21, 22, 25 e 26).
- Nome recomendado, pacote por episódio, formato, quadros e roteiro (proposta do podcast; decisão 21).
- Régua, frase da regra e respostas do time (copy-de-mensagens-pos-onda1, seções 0.2, 1.4, 6A e 7).

## [SUPOSIÇÃO]

- [SUPOSIÇÃO do qa] O card do convidado e o corte com o nome contam juntos como 1 post de docente do kit, só para docente da ficha e só com o checklist C1 a C8 (F9).
- [SUPOSIÇÃO do qa] Contagem de "dias até o início" pela mesma regra do mapa da turma (F13).

## [CONFIRMAR]

- G, gasto acumulado do ciclo da 68606 (PP15).
- U11 (R$ 260,00 contra R$ 250,00), OU3, OU4, OU6 e OU8.
- Política de privacidade do formulário (p04) e correção da página (OA10).
- Podcast: nome e perfis, canal do YouTube, quem produz, custo, convidados, egresso e autorização por episódio.
- O que o CPA do deck mede e Mmid.

## Fontes

- /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/docs/insumos/tgh-plano-de-campanhas-cursos-tier1-v2.txt
- /home/user/marketing-ufape/docs/insumos/ufape-podcast-proposta-2026-10-28.txt
- /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md
- /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/deck.json e slides/*.html
- /home/user/marketing-ufape/auditorias/02-estrategia-e-posicionamento.md; /home/user/marketing-ufape/auditorias/conformidade-educacional.md
