# QA de marketing: mídia paga da Pós refeita com a verba do CEO (versão 3)

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Arquivos revisados (não editados):**
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (versão 3: a seção 12 inteira, mais o corpo nos pontos em que a seção 12 manda valer sobre ele)
  - /home/user/marketing-ufape/saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 3)
- **Entradas lidas:**
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/contexto/ufape-geral.md
  - /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 17, com foco nas decisões 14 a 17)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 12 e 13, mais a seção 7 para P3 a P5)
  - /home/user/marketing-ufape/auditorias/11-midia-paga.md
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seções "Como usar", 2 e 3)
- **Método:** recálculo de toda conta das duas versões 3 contra o catálogo e as decisões do CEO (meta em reais, custo por matrícula, cenários, verba por canal, fase, semana e dia, datas de corte, dias de ciclo, semanas do calendário e limites de volume). Depois, conferência cruzada entre os dois arquivos e as duas auditorias, item por item.
- **Dados pessoais:** nenhum. Só contas sobre preços do catálogo e a verba e a meta do CEO.
- **Natureza do que foi revisado:** são planos, não peças. A conformidade foi aplicada às regras que os planos passam para as peças. Toda peça de março e abril passa de novo pelo qa-de-marketing antes de subir.

---

## 1. Tabela de vereditos

| # | O que foi conferido | gestor-de-midia-pos v3 | estrategia-de-midia-pos v3 |
|---|---|---|---|
| V1 | Meta em reais = 15 x total do catálogo, nas 20 turmas do recorte e nas 10 de maio | Certo (30 de 30) | Certo (20 de 20) |
| V2 | Custo máximo por matrícula R$ 2.000,00 / 15 = R$ 133,33 | Certo | Certo |
| V3 | Três cenários (inscrições, leads, custo por inscrição, CPL) | Certo | Certo |
| V4 | Verba por canal e fase (março 500/200/1.300; abril 500/1.500; Meta e Google) | Certo, soma R$ 2.000,00 | Certo, soma R$ 2.000,00 |
| V5 | Verba por semana e por dia (frio, remarketing, Google), diárias arredondadas para baixo | Não se aplica | Certo nas 14 turmas; nenhuma passa de R$ 2.000,00 |
| V6 | Datas de corte (30 dias antes do início), dias e semanas de ciclo, dia da semana dos marcos | Certo | Certo, exceto a leitura do rodízio de 657 e 341 (QM4) |
| V7 | Limites de volume (verba semanal x 3 maior ou igual a conceitos x 1,5 x CPL) | Contas certas, regra diferente da estratégia (QM3) | Certo |
| V8 | Coerência entre os dois arquivos | Corrigir (QM3) | Corrigir (QM3, QM4, QM5) |
| V9 | Toda taxa de conversão marcada [SUPOSIÇÃO] ou [CONFIRMAR] | Atende (recomendação R1) | Atende (recomendação R6) |
| V10 | Nenhum preço nem valor de inscrição em texto de peça | **Falha:** a encomenda proíbe só o valor da inscrição (QM2) | Atende |
| V11 | Provas de bolsa, YouTube e LinkedIn fora | Seção 12 atende; **o corpo ainda programa as três coisas** (QM1) | Atende |
| V12 | Toda ação no gerenciador é pedido de aprovação humana | Atende | Atende (recomendação R4) |
| V13 | auditorias/11-midia-paga.md | Corrigir (seção 4) | Pendências externas, sem falha do plano (seção 4) |
| V14 | auditorias/conformidade-educacional.md | Corrigir: item de preço (QM2) | Pendências externas, sem falha do plano (seção 5) |
| **Veredito** | | **CORRIGIR** | **CORRIGIR** |

**Destino:** os dois arquivos voltam aos agentes que os produziram (gestor-de-midia: QM1, QM2 e QM3; estrategia-de-midia: QM4 e QM5, e conferir QM3 depois que o gestor fechar a regra). Ainda não seguem para a aprovação humana de PP15, PP16 e EM4, EM11 e EM13 a EM16. Depois das correções, basta uma nova conferência curta destes cinco pontos. As contas não precisam ser refeitas.

---

## 2. Correções obrigatórias

### QM1. gestor-de-midia-pos: corpo do arquivo ainda programa provas, YouTube, LinkedIn e a reserva P6

A seção 12 tira as provas (decisão 14), o YouTube, o LinkedIn e a P6. Mas só as seções 0, 4 e 7 ganharam o aviso da versão 3 (o próprio arquivo diz isso, linha 622). As seções 1, 3, 5, 6, 9 e 11 seguem como na versão 2, sem aviso. Quem executa no gerenciador lê primeiro o calendário (seção 6), e esse calendário manda subir as provas em 03/11, contra a decisão 14.

| Linha | O que está escrito | Correção |
|---|---|---|
| 59 a 63 (seção 1) | P1, P2, P5 e YouTube em P3 como frentes ativas | Pôr o aviso "Versão 3: P1 e P2 suspensas (decisão 14); P5, P6 e o YouTube fora (12.5 e 12.6)" no topo da seção, ou marcar cada linha |
| 200, 202 e 205 (seção 3) | YouTube e LinkedIn como "teste condicionado"; provas "Ativo" | Marcar YouTube e LinkedIn como "fora nesta verba (12.6)" e a coluna P1/P2 como "suspensa (decisão 14)" |
| 265 e 266 (seção 5) | Linhas de exemplo das provas (P1) | Trocar por uma turma de março ou apontar para a seção 2.4 da estrategia-de-midia-pos |
| 284 (seção 6) | "31/10 Teste de rastreio (D8)" | 30/10 (EA4 do cmo, seção 12.6, EVM1; a estratégia já usa 30/10, linha 372) |
| 285, 287, 288, 290 e 293 (seção 6) | Subida das provas em 03/11, revisões das provas, prova e pausa em 27/11, remarketing de bolsa P2 | Marcar como "suspenso (decisão 14)" ou retirar |
| 299 e 302 (seção 6) | Uso da reserva P6 em 04/01 e 18/01 | Retirar: P6 deixou de existir (12.5) |
| 301 (seção 6) | Decisão de LinkedIn e YouTube em 08/01 | Trocar por "PP13 e PP14 com recomendação fora; decisão do cmo" |
| 354 (PP7) | "até lá, a parte delas fica em P6" | "até lá, vale a regra de turma atrasada: as partes contam da data de subida" (estratégia, 3.1) |
| 365 | "Recomendação do gestor: aprovar PP2 e PP3; PP13 e PP14 só se as condições fecharem até 08/01" | Contradiz a linha 363 e a 12.7 (linha 599). Trocar por "PP3 e PP8 suspensos; PP13 e PP14: recomendação fora nesta verba; aprovar PP15 e PP16" |
| 383, 388, 391, 406 e 417 (seção 11) | Auditoria ainda cita PP13, PP14, Insight Tag e provas recebendo verba | Atualizar para Meta e Google só, sem provas |
| 667 a 669 (Suposições) | Divisão 30/5/35/15/5/10, fases das provas, canais com YouTube 10% | Marcar "versão 2, substituída pela seção 12" |

**Por que é obrigatória:** a decisão 14 diz que não sai peça nova das provas, e o pedido de revisão exige que provas, YouTube e LinkedIn tenham saído. Hoje, quem lê o arquivo encontra duas instruções que se contradizem.

### QM2. gestor-de-midia-pos, seção 12.8: a encomenda proíbe só o valor da inscrição, não o preço

- **Linhas 606 (anuncios-meta) e 608 (criativos-de-anuncio):** "nenhum texto com o valor da inscrição até U11" e "nenhuma peça cita o valor da inscrição (R$ 260,00 ou R$ 250,00) até U11".
- **Problema:** pelo contexto da linha (contexto/pos-graduacao.md, "Regras específicas"), toda peça com preço mostra parcelas, valor da parcela, total **e matrícula**. A matrícula é justamente o valor em dúvida (R$ 260,00 do CEO contra R$ 250,00 ou R$ 350,00 do site, U11). Com a encomenda do jeito que está, um criativo poderia mostrar "30x de R$ 1.180,00" sem a matrícula. Isso falha no item de preço da conformidade ("sem esconder taxa de matrícula").
- **Correção:** nas duas linhas, escrever o que a estratégia já diz (linha 283 e seção 7): "nenhuma peça mostra preço (parcela, total ou matrícula) nem valor de inscrição até U11; o investimento completo fica na página da turma".

### QM3. Coerência: duas regras diferentes para o limite de volume, o "frio sai" e a troca do rodízio

- **gestor, linhas 557 a 574 (tabela de 12.6), linha 580 (item 4) e linha 589 ("Só remarketing"):** o limite é calculado sobre a Meta inteira com 3 conceitos (por exemplo, 68615 na conversão: R$ 85,72; manutenção: R$ 33,33). A regra "o frio sai depois de 2 semanas acima do limite da tabela" usa esse número.
- **estratégia, linhas 233 a 249 (3.6), 144 (2.5) e 422 (6.3):** frio e remarketing são campanhas separadas (68615 na conversão: frio R$ 51,43; manutenção só remarketing com 2 peças: R$ 50,00). A mesma regra "frio sai" usa este número.
- **Efeito:** com o mesmo CPL observado (por exemplo, R$ 60,00 na Meta fria de 68615 na conversão), um arquivo manda tirar o frio e o outro não. A estratégia registra a diferença (linhas 249 e 471), mas a decisão continua com duas fontes.
- **Também:** a troca do rodízio está em "1,5 vez o CPL máximo gasto" no gestor (linha 587) e em R$ 27,00 (1,5 x R$ 18,00) na estratégia (linha 257). O gestor não diz de qual cenário é o CPL máximo; se for o de corte (R$ 4,00), o número cai para R$ 6,00.
- **Linha 557 do gestor:** cita "estrategia-de-midia-pos (seção 3.4)" com fatores de VN e YouTube da versão 2. Na versão 3, a seção 3.4 é a verba de abril e não existe mais VN nem YouTube.
- **Correção (no gestor, dono da regra):** declarar a tabela 3.6 da estrategia-de-midia-pos como a única fonte do limite de volume e do gatilho "frio sai", trocar o item 4 por "manutenção: só remarketing com 2 peças, limite de R$ 50,00", fixar a troca do rodízio em R$ 27,00 (1,5 x o maior CPL máximo, R$ 18,00) e tirar a referência à 3.4 da versão 2. Depois disso, a estratégia apaga as linhas 249 (segunda frase) e 471 da lista de diferenças.

### QM4. estrategia-de-midia-pos: 657 e 341 têm, sim, uma semana fechada antes da manutenção

- **Linha 259 (3.7, item 7):** "657 e 341 não têm semana fechada antes da manutenção: o gatilho é lido em 11/01".
- **Conferência:** 657 e 341 sobem na segunda-feira, 14/12 (linhas 183 e 378). A semana de 14 a 20/12 é inteira (segunda a domingo, 7 dias) e cobre toda a fase de aquecimento delas, com R$ 500,00 gastos (linha 212, S2). Ela pode ser lida na revisão 8, em 21/12, junto com 68615, 289 e 333.
- **Linhas 402 (revisão 7), 403 (revisão 8) e 406 (revisão 11):** acompanham o mesmo erro.
- **Correção:** ler o gatilho de 657 e 341 em 21/12 (semana de 14 a 20/12), com o rodízio valendo a partir de 04/01, como nas outras três. Se o agente preferir manter 11/01, ele precisa escrever o motivo como [SUPOSIÇÃO] (por exemplo, aprendizado da plataforma numa semana só), sem dizer que a semana não existe.

### QM5. estrategia-de-midia-pos: a regra de 289 e 662 contradiz o próprio limite

- **Linha 265 (3.8):** o gasto até 06/12 sai primeiro do aquecimento (R$ 500,00); "se passar de R$ 500,00, o que passar sai da Meta fria da conversão"; o pedido de redução da diária só vem acima de R$ 700,00, "para preservar os R$ 1.300,00 da conversão".
- **Linha 462 (EM15):** repete o limite de R$ 700,00.
- **Problema:** com gasto de R$ 600,00 até 06/12, R$ 100,00 saem da conversão e nenhum pedido é feito. Isso contradiz o motivo escrito (preservar a conversão). Além disso, as tabelas 3.3 e 3.5 mostram 289 com a diária cheia do aquecimento a partir de 07/12. Se o aquecimento já tiver sido gasto antes, a diária precisa cair. A regra está no rodapé da linha 189, mas não chega às encomendas da seção 7 nem ao calendário.
- **Correção (escolher uma):** (a) o pedido de redução sai quando o gasto previsto até 06/12 passar de R$ 500,00, e o que passar sai da manutenção; ou (b) manter R$ 700,00 e escrever que o que passar de R$ 500,00 sai da manutenção (R$ 200,00), não da conversão. Nos dois casos, juntar ao calendário de 30/11 (289) e de 30/12 (662) a linha "diárias da estrutura nova recalculadas pelo saldo da fase, informado pela analise-de-midia".

---

## 3. Recomendações (não bloqueiam)

| # | Arquivo e linha | O que | Sugestão |
|---|---|---|---|
| R1 | gestor, 39 e 458 | "CPL máximo, cenário base: R$ 10,00" em todas as turmas e "três cenários ilustrativos" sem marcador. A taxa de origem está marcada (12.3), mas o número derivado aparece sozinho | Pôr [SUPOSIÇÃO, taxas de 12.3] no título da coluna e na linha 39 |
| R2 | gestor, 456, 458 e 486 | O nome "Retorno sobre a verba" pode ser lido como projeção de ROI, mas é receita bruta de lista em 18 a 30 parcelas, sem evasão. A linha 486 diz "90 a 363 vezes" (contando maio, 719), e a linha 39 diz "202 a 363" (recorte). O teto "R$ 11.470,00 a R$ 19.609,96" é só de março e abril (a seção 2.4 vai até R$ 8.578,04 com 68629) | Trocar o nome por "meta em reais dividida pela verba" e dizer o recorte de cada faixa |
| R3 | gestor, 351 (PP4), e estratégia, 298 a 308 | PP4 usa `pos_<código>_<plataforma>...`; a estratégia usa `pos_<código>-<área curta>_<plataforma>...`. As duas começam por pos_<código>, como pede o D12 | O PP4 do gestor cita a seção 4.2 da estratégia como padrão final |
| R4 | estratégia, 256 a 258 (3.7, passos 4 e 5) | "o 3º é pausado", "o pior sai", escritos como ação direta | Escrever "pedido de pausa (humano no gerenciador)", como a seção 6.3 já faz |
| R5 | estratégia, 165 a 174, e gestor, 534 | A onda 1 roda até o início da turma (D9 e D18), mas o ciclo de março e abril termina no corte (1ª mensalidade 30 dias antes). As duas regras convivem sem explicação | Uma frase dizendo que a onda 1 segue D9 e D18 do memorando e que a entrada depois do vencimento da 1ª mensalidade é [CONFIRMAR] com a Ufape |
| R6 | estratégia, 116 e 117 | Linhas de leads (500, 200 e 112) e inscrições pagas (25, 20 e 17) sem marcador na tabela | Pôr [SUPOSIÇÃO, 2.2] nas duas linhas |

---

## 4. Contas recalculadas (resumo da conferência)

**Meta em reais e razão sobre a verba (gestor 12.2; estratégia 2.3 e 3.2).** As 20 turmas do recorte, conferidas contra o total no cartão ou boleto do catálogo: 707 R$ 715.500,00; 68604 R$ 450.000,00; 68606 R$ 531.000,00; 698 R$ 404.550,00; 68610 R$ 450.000,00; 68608 R$ 531.000,00; 657 R$ 726.000,00; 341 R$ 652.500,00; 289 R$ 531.000,00; 68615 R$ 531.000,00; 333 R$ 420.750,00; 679, 68632, 68635 e 366 R$ 495.000,00; 68628 R$ 584.100,00; 68617 R$ 540.000,00; 68636 R$ 569.250,00; 68609 R$ 486.750,00; 662 R$ 562.500,00. As 10 de maio também estão certas (719 R$ 180.000,00 até 352 R$ 718.200,00). As razões sobre R$ 2.000,00 estão certas, com arredondamento em duas casas (por exemplo, 698: 202,275, escrito 202,28). As diferenças de centavos entre parcela x número de parcelas e total (657, 698 e 68609) estão bem apontadas.

**Custo por matrícula e cenários.** R$ 2.000,00 / 15 = R$ 133,33. Conservador: 15 / 0,60 = 25 inscrições; 25 / 0,05 = 500 leads; R$ 80,00 e R$ 4,00. Base: 20; 200; R$ 100,00 e R$ 10,00. Otimista: 16,67; 111,11; R$ 120,00 e R$ 18,00. A regra "1 ponto de i com k de 75% = R$ 1,00 de CPL" está certa. A receita de inscrição (15 x R$ 260,00 = R$ 3.900,00, ou 1,95 vez a verba) também.

**Verba por canal e fase.** Março: 25% R$ 500,00 (Meta R$ 350,00, Google R$ 150,00); 10% R$ 200,00 (R$ 100,00 e R$ 100,00); 65% R$ 1.300,00 (R$ 845,00 e R$ 455,00). Total: Meta R$ 1.295,00 e Google R$ 705,00. Abril: R$ 500,00 (R$ 350,00 e R$ 150,00) e R$ 1.500,00 (R$ 975,00 e R$ 525,00). Total: R$ 1.325,00 e R$ 675,00. Divisão frio e remarketing: março R$ 787,00 e R$ 508,00; abril R$ 865,00 e R$ 460,00. Tudo certo.

**Datas de corte e ciclos** (fevereiro de 2027 tem 28 dias): 657, de 13/03 para 11/02; 289, 68615 e 341, de 20/03 para 18/02; 333, de 27/03 para 25/02; 679, de 03/04 para 04/03; 10/04 para 11/03; 17/04 para 18/03; 24/04 para 25/03. Dias com os dois extremos: 74, 81, 60, 67, 58, 65, 72 e 79. Conversão: 46, 53 e 39 (março); 39, 46, 53 e 60 (abril). Aquecimento: 14, 7 e 19. Manutenção: 14. Todos certos, e os cortes caem mesmo em quintas-feiras.

**Semana e dia.** As 14 turmas fecham em R$ 2.000,00 exatos na tabela 3.5. Exemplos: 68615 = 250 + 250 + 100 + 100 + 6 x 197,83 (1.186,96) + 113,04; 333 = 500 + 200 + 7 x 171,70 (1.201,89) + 98,11; 657 = 500 + 200 + 5 x 233,33 (1.166,67) + 133,33; 679 = 500 + 5 x 269,23 (1.346,15) + 153,85; 68632 e grupo = 500 + 6 x 228,26 (1.369,57) + 130,43; 68617 e 68636 = 500 + 7 x 198,11 (1.386,79) + 113,21; 68609 e 662 = 500 + 8 x 175,00 + 100,00. Diárias arredondadas para baixo e conferidas (por exemplo, 657 remarketing na conversão: 338 / 39 = 8,6667, escrito 8,66; 333 frio: 507 / 53 = 9,566, escrito 9,56). Nenhuma diária x dias passa do total da fase.

**Limites de volume.** As 33 células da tabela 3.6 da estratégia e as 12 linhas da tabela 12.6 do gestor estão certas dentro da regra de cada uma. O problema é ter duas regras (QM3), não a conta. Os fatores de VN da linha 557 do gestor também estão certos (R$ 28.571,43 / 285,71 = R$ 100,00), mas a referência é da versão 2.

**Calendário.** 07/12/2026, 04/01, 25/01 e 08/02/2027 caem em segundas-feiras; 06/01/2027 cai numa quarta. Carnaval em 08 e 09/02/2027 (Páscoa em 28/03/2027). Revisões em segundas, e as que caem em feriado passam para o dia útil seguinte (D15). Certo, exceto QM4.

---

## 5. auditorias/11-midia-paga.md, item por item

| Item | gestor v3 | estratégia v3 | Observação |
|---|---|---|---|
| Plano do gestor aprovado, com canais ativos e fora justificados | Corrigir | Atende no desenho | Meta e Google com motivo; no gestor, as seções 1 e 3 ainda mostram YouTube e LinkedIn como teste (QM1). Aprovação humana em PP16 pendente |
| Metas de CPL e custo por matrícula escritas antes de subir | Atende em parte | Atende em parte | R$ 133,33 e CPL em três cenários; taxas i e k [CONFIRMAR] |
| Verba dentro do valor aprovado, com aprovador registrado | Atende em parte | Atende em parte | R$ 2.000,00 por turma (decisão 15); nenhuma tabela passa disso; o aprovador do pagamento é [CONFIRMAR] (tabela de aprovação de ufape-geral.md vazia); gasto anterior em PP15 |
| Nomenclatura padrão | Pendente | Atende no desenho | R3 (harmonizar PP4 com a 4.2) |
| UTMs completas e origem no CRM | Pendente externo | Pendente externo | Teste de 30/10 (o gestor ainda diz 31/10, QM1) |
| Pixel, API de Conversões e conversões do Google nos canais ativos | Pendente externo | Pendente externo | EM11 e D8; TikTok e LinkedIn fora |
| Criativos aprovados na conformidade | Pendente externo | Pendente externo | Peças de março e abril ainda não existem; a encomenda do gestor precisa de QM2 |
| Anúncios dentro das políticas das plataformas | Atende no desenho | Atende no desenho | Sem atributo pessoal, sem escassez falsa, sem concorrente |
| Nenhum público com menores de 18 anos | Atende | Atende | 18+ em todo conjunto |
| Post de docente promovido ou Spark Ad com autorização | Não se aplica | Não se aplica | LinkedIn e TikTok fora; autorização de docentes registrada (decisões 8 e 10) |
| Relatório semanal ao CMO | Pendente externo | Pendente externo | Calendário da estratégia 6.2 certo |
| Sem segmentação discriminatória | Atende | Atende | Região por estado, sem atributo sensível |
| Públicos sem dados pessoais sem base legal | Atende | Atende | Sem lista de contatos até a base legal |
| Dados de curso conferidos no catálogo | Atende | Atende | Valores, parcelas, datas, praças, turmas e modalidade conferidos; divergências marcadas |
| Destino de WhatsApp oficial | Não se aplica | Não se aplica | A mídia leva à página da turma |
| Números da análise só das exportações | Atende | Atende | Nenhum número de mídia observado; taxas são [SUPOSIÇÃO] |
| Nenhuma alteração na plataforma sem humano | Atende | Atende | R4 para a redação do rodízio |

---

## 6. auditorias/conformidade-educacional.md, item por item (regras dos planos)

| Bloco | Item | gestor v3 | estratégia v3 | Observação |
|---|---|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atende | Atende | "Pós-graduação em" nas peças; 333 e 341 com nota |
| Dados do curso | Status "aberto" (ou sem chamada para inscrição) | Atende | Atende | Só turmas "aberto" recebem verba nova; as 6 "verificar" seguem em pausa |
| Dados do curso | Modalidade clara e correta | Atende | Atende | 68632 presencial, sem "semipresencial" no anúncio |
| Regulação | Graduação: ato regulatório do catálogo | Não se aplica | Não se aplica | Linha pos |
| Regulação | Pós sem "reconhecida pelo MEC"; texto aprovado | Atende | Atende | Sem frase de certificação; texto oficial [CONFIRMAR] |
| Regulação | Curso livre sem diploma | Não se aplica | Não se aplica | |
| Regulação | Nota MEC só com fonte | Atende | Atende | Nenhuma nota |
| Promessas | Sem promessa de emprego, salário ou sucesso | Atende | Atende | |
| Promessas | Empregabilidade e satisfação com fonte | Não se aplica | Não se aplica | |
| Promessas | Superlativos só com fonte | Atende | Atende | |
| Promessas | Comparação com concorrente objetiva | Atende | Atende | Sem lance em concorrente; negativas só por homonímia |
| Preço (CDC) | Valor, parcelas e condições completas, sem esconder matrícula | **Falha (QM2)** | Atende | A estratégia proíbe preço até U11; o gestor só proíbe o valor da inscrição |
| Preço (CDC) | Bolsa e desconto com regra, público e prazo | Atende | Atende | Sem bolsa nos anúncios de turma; 341 sem promoção até PR7 |
| Preço (CDC) | Urgência real | Atende | Atende | Turma mínima de 15 só como informação |
| Preço (CDC) | Prouni, Fies ou financiamento | Não se aplica | Não se aplica | |
| Pessoas e dados | Autorização de imagem e voz | Atende | Atende | Decisões 8 e 10; nenhum aluno |
| Pessoas e dados | Menores só com autorização | Atende | Atende | 18+ |
| Pessoas e dados | Formulários com finalidade e política de privacidade | Pendente externo | Pendente externo | Conferir nas páginas antes de cada subida |
| Pessoas e dados | WhatsApp e e-mail só com consentimento | Atende | Atende | A mídia não leva ao WhatsApp; inscrição paga segue o teto D16 (decisão 17) |
| Pessoas e dados | Nenhum dado pessoal | Atende | Atende | Só números somados |
| Plataformas | Políticas da Meta e do Google, sem segmentação discriminatória | Atende no desenho | Atende no desenho | |
| Plataformas | Destino entrega o que o anúncio promete | Pendente externo | Pendente externo | 662 e 679 (link), 366 e 68636 (data) bloqueados até a correção |
| Anúncios | Sem característica pessoal de quem vê | Atende no desenho | Atende no desenho | |
| Anúncios | Sem urgência falsa nem imitação da interface | Atende | Atende | |
| Anúncios | Sem pessoa pública nem parceria inexistente | Atende | Atende | |
| Anúncios | Sem caixa alta excessiva nem símbolos | Atende no desenho | Atende no desenho | Conferir nas peças |
| Anúncios | Página de destino carrega, com dados da Ufape e política | Pendente externo | Pendente externo | |
| Anúncios | Sem sugestão para driblar a análise | Atende | Atende | |
| Texto | Sem travessão nem meia-risca | Atende | Atende | Nenhum encontrado na leitura completa dos dois arquivos (leitura visual, sem busca automática nesta revisão) |

**Resultado da conformidade:** gestor **bloqueado** (item de preço, QM2). Estratégia sem falha própria. Os itens "pendente externo" bloqueiam a subida de cada campanha, não o plano [SUPOSIÇÃO de método, a mesma das revisões anteriores do lote].

Revisado por: qa-de-marketing (agente). Revisão humana: [CONFIRMAR, tabela de aprovação de ufape-geral.md vazia; até lá, pessoa do marketing].
Data: 26/10/2026.

---

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 por turma de Pós no ciclo; meta de pelo menos 15 matrículas; meta em reais de 15 vezes o valor do curso; inscrição de R$ 260,00 medida à parte da 1ª mensalidade; nenhuma peça cita o valor da inscrição até U11; provas de bolsa e Livres sem peça nova até nova ordem (docs/execucao-2026-10-26.md, decisões 14, 15 e 16).
- Teto de mensagens da Pós: 2 WhatsApp e 2 e-mails de campanha por semana, 1 por dia (decisão 17; plano do cmo, 13.3, D16).
- Totais, parcelas, matrícula de R$ 250,00 (R$ 350,00 em 706, 586 e 68629), datas de início, praça, modalidade e status das turmas citadas (catálogo, seção 2, 26/10/2026).
- Toda peça com preço mostra parcelas, valor da parcela, total e matrícula; 1ª mensalidade 30 dias antes do início na maioria das páginas; turma mínima de 15 (contexto/pos-graduacao.md).
- EA4 (teste de rastreio em 30/10), D11 e D12 (UTM e nomes), D15 (feriado na segunda) (plano do cmo, 12.6 a 12.8).
- Calendário: 26/10/2026 é segunda-feira; fevereiro de 2027 tem 28 dias; Páscoa de 2027 em 28/03 e Carnaval em 08 e 09/02.
- Tabela de aprovação de ufape-geral.md sem nomes (contexto/ufape-geral.md, "Regras de aprovação").

## Lista 2. Suposições

- [SUPOSIÇÃO] Itens "pendente externo" bloqueiam a subida de cada campanha, não o plano; o veredito de corrigir vem das falhas próprias (QM1 a QM5).
- [SUPOSIÇÃO] A semana de 14 a 20/12 conta como semana fechada para 657 e 341 porque a subida é numa segunda-feira e a semana do plano vai de segunda a domingo (estratégia, 3.5).
- [SUPOSIÇÃO] O CPL máximo da troca do rodízio no gestor (linha 587) é o mesmo da estratégia (R$ 18,00); o gestor não diz de qual cenário é.
- As taxas i e k (5%, 10% e 15%; 60%, 75% e 90%) são [SUPOSIÇÃO ilustrativa] dos próprios arquivos revisados; esta revisão só conferiu a aritmética.

## Lista 3. Dados que faltam

- [CONFIRMAR U11] Valor da inscrição da Pós (R$ 260,00 do CEO contra R$ 250,00 e R$ 350,00 do site).
- [CONFIRMAR] Período exato do ciclo e data de corte da 1ª mensalidade por ficha de turma.
- [CONFIRMAR] Taxas reais de lead para inscrição e de inscrição para matrícula, e Mmid por turma.
- [CONFIRMAR] Gasto acumulado do ciclo das 6 turmas da onda 1, de 289 e de 662 (PP15).
- [CONFIRMAR] Quem aprova anúncios e verba (tabela de ufape-geral.md).
- [CONFIRMAR] Mínimo diário aceito pela Meta e pelo Google para diárias de R$ 3,68 a R$ 10,00.
- [CONFIRMAR] Link de 662 e 679, data de 366 e 68636, turma de 68617 e 68628, pré-requisito de 657 (U10), promoção de 341 (PR7).
- [CONFIRMAR] Se a turma da onda 1 aceita matrícula depois do vencimento da 1ª mensalidade (R5).
- [CONFIRMAR] Texto oficial de certificação da Pós.

## Fontes

Internas: os arquivos listados no cabeçalho. Externas: nenhuma.

---

**Próximo passo:** volta ao gestor-de-midia (QM1, QM2 e QM3) e depois à estrategia-de-midia (QM4, QM5 e o ajuste de QM3). Em seguida, uma nova conferência do qa-de-marketing só desses pontos. Aprovado, segue para a aprovação humana de PP15, PP16 e EM4, EM11 e EM13 a EM16. Nada sobe, muda ou gasta antes disso.
