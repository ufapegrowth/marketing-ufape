# QA de marketing: reconferência dos posicionamentos de Pós, Livres e Eventos (etapa 1.7, segunda rodada)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (pos, livres e eventos)
- Data: 26/10/2026
- Peças reconferidas (não editadas):
  - saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md (382 linhas)
  - saidas/02-estrategia-e-posicionamento/posicionamento-livres-2026-10-26.md (470 linhas)
  - saidas/02-estrategia-e-posicionamento/posicionamento-eventos-2026-10-26.md (374 linhas)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/catalogo-de-cursos.md (inteiro, seções 1 a 9)
  - auditorias/02-estrategia-e-posicionamento.md
  - auditorias/conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02b.md (P1 a P6, L1 a L6, E1 a E5, PA1 a PA7, LA1 a LA6, EA1 a EA5)
- Não reli nesta rodada contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md, as fichas e as saídas de inteligência: as citações dessas fontes foram conferidas no dep02b e aceitas como estão [SUPOSIÇÃO: transcrição fiel mantida].
- Números de linha: referem-se aos arquivos como estavam em 26/10/2026, nesta rodada.
- Dados pessoais: nenhum. Nenhum docente nomeado aqui.

---

## 1. Vereditos

| Arquivo | Bloqueantes do dep02b | Ajustes do dep02b | Achados novos | Veredito |
|---|---|---|---|---|
| posicionamento-pos | P1 a P6 resolvidos | PA1 a PA7 não resolvidos | N-P1 (bloqueante), N-P2 | **CORRIGIR** |
| posicionamento-livres | L1 a L6 resolvidos | LA1 a LA4 e LA6 não resolvidos; LA5 em parte | N-L1, N-L2 | **CORRIGIR** |
| posicionamento-eventos | E1 a E5 resolvidos | EA1 a EA5 não resolvidos | nenhum | **CORRIGIR** |

Os 17 bloqueantes da primeira rodada foram resolvidos, bem e sem efeito colateral. Os três arquivos voltam porque os ajustes PA, LA e EA ficaram para esta rodada e nenhum arquivo os aplicou (os três dizem no status ou na seção final que "não foram aplicados" ou "não foram pedidos nesta rodada"). Três desses ajustes (PA6, LA4, EA3) tocam o item de conformidade "não confere diploma e não equivale a graduação ou pós", e EA4 toca o item de modalidade; pela regra do QA, item de conformidade sem marcação bloqueia. A Pós tem ainda um dado novo errado (N-P1).

---

## 2. posicionamento-pos-2026-10-26.md

### 2.1 Reconferência dos bloqueantes

| Item | Situação | Onde e como |
|---|---|---|
| P1 | Resolvido | Linha 150: "pós-graduação em Medicina Veterinária, com 29 turmas abertas em São Paulo e em Goiânia (28 semipresenciais e 1 presencial, a 68632)". Nota da linha 152 e A1 (linha 83) explicam a 719. Contagem conferida no catálogo, seção 2: 30 abertas, 719 fora de Medicina Veterinária, 68632 presencial |
| P2 | Resolvido | Matrícula em todas as turmas com preço: linhas 105, 196 a 203, 211, 217. Valores conferidos (R$ 250,00; R$ 350,00 em 68629 e 586) |
| P3 | Resolvido | A9 (linha 91): modalidade de cada turma de Goiânia e local da prática [CONFIRMAR] |
| P4 | Resolvido | Coluna "Selo" na tabela 1.3 (legenda na linha 79); A4, A5, A8 com [CONFIRMAR NO CATÁLOGO]; prova 3 (linha 160) e objeção 3 (linha 251) marcadas; linha 150 com "[CONFIRMAR NO CATÁLOGO: 15 ou 20]" |
| P5 | Resolvido | Linha 276 com data, distribuição, nota de corte, regra e marcação; linha 277 sem afirmar 20; linha 106 com [CONFIRMAR NO CATÁLOGO] |
| P6 | Resolvido | 679 fora da tabela 3.2 (nota da linha 205) e na 3.5 (linha 237) com "concorrente sem fonte" |

### 2.2 Reconferência dos ajustes

| Item | Situação | O que ainda falta |
|---|---|---|
| PA1 | Não resolvido | Ressalva de resumo de busca segue só no cabeçalho (linha 23) e nas fontes (linha 381). Falta na legenda da tabela 1.2 (linha 62), da tabela 3.5 (linha 224) e no resumo da seção 0 (linha 32) |
| PA2 | Não resolvido | Linha 106, coluna "Prova a mostrar": "depois do fim das inscrições da Anclivepa-SP (07/11/2026)". Mover para uso interno de calendário (dado de confiança M, cópia não oficial do edital). Mesma lógica na linha 53 |
| PA3 | Não resolvido | "condições à vista antes da matrícula" segue nas linhas 38 e 144. Trocar por "condições claras" ou "condições na página", ou registrar o risco para o agente mensagens |
| PA4 | Não resolvido | "reta final" segue nas linhas 230 (68604) e 233 (707). Acrescentar: "na peça, só a data de início, sem 'reta final' nem 'últimos dias'" |
| PA5 | Não resolvido | A6 (linha 88): Unicruz 9ª edição e Qualittas desde 2014 sem fonte na célula. Citar inteligencia-concorrencia C-5 e C-2 |
| PA6 | Não resolvido | Linha 219: "curso livre não confere diploma nem equivale a pós-graduação". Trocar por "não confere diploma nem equivale a graduação ou pós-graduação" |
| PA7 | Não resolvido | Linha 271 remete ao guia de marca sem ressalva. Acrescentar que os exemplos herdados só valem depois da nova rodada do guia (dep02a em corrigir) |

### 2.3 Achados novos (regressão)

**N-P1 (bloqueante). "Menores totais" errado: linhas 249 (objeção 1, colunas "Resposta" e "Prova") e 330 (Lista 1), e a escolha das turmas em P3 (linha 105).**
- Problema: o arquivo diz que 68629, 333 e 60 são os menores totais de pós veterinária aberta. No catálogo, seção 2, a ordem é 68629 (R$ 16.456,00), **698 (R$ 26.970,00, 18x de R$ 1.498,33, matrícula R$ 250,00)**, 333 (R$ 28.050,00) e 60 (R$ 29.700,00). A 698 fica de fora e a 60 é a quarta, não a terceira. É afirmação comparativa de preço que o agente mensagens vai copiar.
- Correção: "68629, 698 e 333 como menores totais de pós veterinária aberta" (com parcelas, total e matrícula do catálogo), ou manter 68629, 333 e 60 sem a palavra "menores" ("exemplos de turmas de total mais baixo"). Na linha 105, se a 698 não servir à P3 (área específica, início em 28/11/2026), dizer por que ficou fora.

**N-P2 (ajuste). "Pós em" na linha 355 (Lista 2):** "contato com o público da Pós em Neurologia". Trocar por "Pós-graduação em Neurologia e Neurocirurgia Veterinária (68616)".

**Observação, sem bloqueio:** a categoria e a declaração interna (linhas 37, 134 e 146) dizem "pós-graduação veterinária semipresencial"; a 68632 é presencial. Aceitável como enquadramento da linha, mas a peça da 68632 não pode herdar "semipresencial".

### 2.4 Varredura de regressão

| Conferência | Resultado |
|---|---|
| Dado novo errado | N-P1. Demais dados conferidos no catálogo: 30 abertas, 24 entre 13/03 e 28/05/2027, total de R$ 12.000,00 (719) a R$ 48.400,00 (657), preços de 699, 352, 359, 698, 333, 341, 289, 68632, 68609, 68623, 586, 68629 e 60, turmas numeradas de A6, CH de 750 h e 600 h |
| Frase de certificação ou nota do MEC fora de proibição | Nenhuma. Linha 72 cita "certificado de especialização lato sensu" do contexto, já marcado como não utilizável em peça (como no dep02b) |
| "Pós em" | N-P2 (linha 355) |
| Travessão ou meia-risca | Nenhum encontrado [SUPOSIÇÃO: leitura visual, sem busca por caractere] |

### 2.5 auditorias/02-estrategia-e-posicionamento.md, item por item

| # | Item | Resultado |
|---|---|---|
| 1 | Uma única meta principal | Atendido (herdado do cmo, linha 288) |
| 2 | Persona e curso nomeados | Atendido |
| 3 | 8 canais | Não se aplica (herdado) |
| 4 | Alternativa real | Atendido, com PA1 aberto |
| 5 | Todo pilar tem prova | Atendido (P3, P4 resolvidos), com PA5 aberto |
| 6 | Voz com exemplos | Atendido, com PA7 aberto |
| 7 | Tempo e verba | Não se aplica |
| 8 | Sem promessa de emprego, aprovação ou salário | Atendido |
| 9 | Preços e condições do catálogo ou marcados | **Falha (N-P1)** |

### 2.6 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, CH batem | Atendido (P1, P3 resolvidos) |
| Dados do curso | Status aberto ou sem chamada | Atendido |
| Dados do curso | Modalidade correta | Atendido |
| Regulação | Graduação | Não se aplica |
| Regulação | Pós sem "reconhecida pelo MEC" | Atendido |
| Regulação | Curso livre sem diploma e sem equivaler a graduação ou pós | **Falha (PA6)** |
| Regulação | Nota MEC | Atendido (nenhuma) |
| Promessas | Emprego, salário, aprovação | Atendido |
| Promessas | Empregabilidade com fonte | Não se aplica |
| Promessas | Superlativos | Atendido |
| Promessas | Comparação com concorrente objetiva e verificável | **Falha (PA1, PA2)**: dado de confiança M como prova a mostrar, ressalva fora das tabelas |
| Preço (CDC) | Valor, parcelas, matrícula | **Falha (N-P1)**: comparação de total errada |
| Preço (CDC) | Bolsa com regra, público, validade | Atendido (marcado) |
| Preço (CDC) | Urgência real | **Falha (PA4)**: "reta final" sem regra de uso |
| Preço (CDC) | Prouni, Fies | Não se aplica |
| Pessoas e dados | Autorização | Atendido |
| Pessoas e dados | Menores | Não se aplica |
| Pessoas e dados | Formulários | Não se aplica |
| Pessoas e dados | Consentimento WhatsApp e e-mail | Não se aplica |
| Pessoas e dados | Nenhum dado pessoal | Atendido |
| Plataformas e anúncios | Todos | Atendido ou não se aplica |

**RESULTADO:** Aprovado ( )  Bloqueado (X).

### 2.7 Veredito: CORRIGIR

O que falta: N-P1, N-P2, PA1, PA2, PA3, PA4, PA5, PA6, PA7.

---

## 3. posicionamento-livres-2026-10-26.md

### 3.1 Reconferência dos bloqueantes

| Item | Situação | Onde e como |
|---|---|---|
| L1 | Resolvido | 616 fora de F1 (nota na linha 90); entra em F2 como online com data, modalidade [CONFIRMAR NO CATÁLOGO] (linha 145); A1 (linha 330) e proibição (linha 314). Preço conferido: R$ 990,00 ou 5x de R$ 240,00 (R$ 1.200,00) |
| L2 | Resolvido | Parágrafo de F1 (linha 137) sem "os docentes atuam na rotina", com [CONFIRMAR NO CATÁLOGO por curso] e [CONFIRMAR autorização]; regra 9 (linha 41) |
| L3 | Resolvido | Declaração de F4 (linhas 244 e 245) sem "a cada 15 dias" nem "anual"; F4.1 restrito ao 644 (linha 228); nota da linha 247 |
| L4 | Resolvido | "6 a 8 horas, de R$ 185,00 a R$ 300,00" (linhas 209 e 210), alternativa sem a 669 (linha 212), "online [CONFIRMAR NO CATÁLOGO: gravado ou ao vivo]", frase sobre a Pós fora da declaração. Conferido: 669 com 6 h e R$ 300,00; 482 com 8 h e R$ 289,00; 461 com R$ 185,00 |
| L5 | Resolvido | F5.1 (linha 263), categoria (linha 269) e parágrafo (linha 273) com [SUPOSIÇÃO: docente e origem do conteúdo a confirmar] |
| L6 | Resolvido | Linha 249 e A2 (linha 331): sem peça da 68641 até a correção do link |

### 3.2 Reconferência dos ajustes

| Item | Situação | O que ainda falta |
|---|---|---|
| LA1 | Não resolvido | Linha 390: "Meta principal do plano do cmo: turmas de Pós confirmadas; para Livres, vendas por curso". Reescrever como "Meta única do plano do cmo: turmas de Pós confirmadas. Métrica de apoio desta linha: vendas por curso livre [CONFIRMAR]" |
| LA2 | Não resolvido | Categoria e declaração de F2 (linhas 174 e 177) seguem "aula gravada por tema" para os 22 itens; no catálogo, seção 5, a maioria tem modalidade "Online" (só 591 e 602 dizem "Gravação"). Marcar "gravado [CONFIRMAR NO CATÁLOGO]" ou trocar por "online" |
| LA3 | Não resolvido | A grafia "Semiprensecial" da 573 no catálogo não entrou nos pedidos da seção 6 |
| LA4 | Não resolvido | A frase segue "não confere diploma nem equivale a pós-graduação" nas linhas 35, 69, 137, 178, 210, 245, 273, 305 e 363. Acrescentar "graduação ou" |
| LA5 | Em parte | Seção 4 (linha 326) já diz "resumos de busca de 26/10/2026". Falta a ressalva na legenda da tabela 1.1 (linha 47) |
| LA6 | Não resolvido | Linha 395 remete ao guia de marca sem dizer que os exemplos herdados só valem depois da nova rodada do guia |

### 3.3 Achados novos (regressão)

**N-L1 (ajuste, carga horária). F2, linha 143, e F2.2, linha 163.** O degrau "ferramenta curta" lista 602, 104, 541, 106, 542 e 102, e o F2.2 o descreve como "ferramenta de 4 a 6 h". No catálogo, seção 5, a 542 tem 12 h e a 102 tem 9 h. Correção: "ferramenta de 4 a 6 h (602, 541, 107, 104, 106)" e passar 542 e 102 para o curso médio, ou mudar a faixa para "4 a 12 h". Item "Prova no catálogo" precisa bater com o catálogo.

**N-L2 (ajuste). "Pós em" na linha 331:** "Pós em Cardiologia da Anclivepa-SP". É de concorrente, mas o texto vai para as mensagens; usar "Pós-graduação em Cardiologia da Anclivepa-SP" para manter o padrão.

### 3.4 Varredura de regressão

| Conferência | Resultado |
|---|---|
| Dado novo errado | N-L1. Conferidos no catálogo: 616, 669, 482, 461, 454 (5x de R$ 59,00, R$ 295,00), 411, 103, 131 (12x de R$ 376,00, R$ 4.512,00), 13 minicursos, grupos de R$ 100,00 (68663; 68665 em 01/11/2026; 68666 em 25/11/2026) e de R$ 734,00 (10x de R$ 88,00), 347 e 501 |
| Frase de certificação ou nota do MEC fora de proibição | Nenhuma (só na seção 3, linha 306, como proibição) |
| "Pós em" | N-L2 (linha 331) |
| Travessão ou meia-risca | Nenhum encontrado [SUPOSIÇÃO: leitura visual] |

### 3.5 auditorias/02-estrategia-e-posicionamento.md, item por item

| # | Item | Resultado |
|---|---|---|
| 1 | Uma única meta principal | **Falha (LA1)**: a redação sugere duas metas |
| 2 | Persona e curso nomeados | Atendido |
| 3 | 8 canais | Não se aplica (herdado) |
| 4 | Alternativa real | Atendido, com LA5 em parte |
| 5 | Todo pilar tem prova | Atendido (L2, L3, L5 resolvidos), salvo N-L1 |
| 6 | Voz com exemplos | Atendido por herança, com LA6 aberto |
| 7 | Tempo e verba | Não se aplica |
| 8 | Sem promessa | Atendido |
| 9 | Preços e condições do catálogo ou marcados | Atendido |

### 3.6 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, CH batem | **Falha (N-L1)**: faixa de 4 a 6 h com cursos de 9 e 12 h |
| Dados do curso | Status aberto ou sem chamada | Atendido |
| Dados do curso | Modalidade correta | **Falha (LA2)**: "gravado" para itens que o catálogo diz "Online" (L1 resolvido) |
| Regulação | Pós sem MEC | Não se aplica |
| Regulação | Curso livre sem diploma e sem equivaler a graduação ou pós | **Falha (LA4)** |
| Regulação | Nota MEC | Atendido |
| Promessas | Todos | Atendido |
| Preço (CDC) | Valor, parcelas, condições | Atendido |
| Preço (CDC) | Desconto com regra | Atendido |
| Preço (CDC) | Urgência real | Atendido |
| Preço (CDC) | Prouni, Fies | Não se aplica |
| Pessoas e dados | Autorização | Atendido |
| Pessoas e dados | Formulários com finalidade | Atendido (linha 214) |
| Pessoas e dados | Nenhum dado pessoal | Atendido |
| Plataformas e anúncios | Todos | Atendido ou não se aplica |

**RESULTADO:** Aprovado ( )  Bloqueado (X).

### 3.7 Veredito: CORRIGIR

O que falta: LA1, LA2, LA3, LA4, LA5 (legenda da tabela 1.1), LA6, N-L1, N-L2.

---

## 4. posicionamento-eventos-2026-10-26.md

### 4.1 Reconferência dos bloqueantes

| Item | Situação | Onde e como |
|---|---|---|
| E1 | Resolvido | Regra 9 (linha 40); W9 (linha 107); oferta de E-W2 (linha 136) com status, modalidade "Presencial", local "Saiba Mais", 24 h e [CONFIRMAR NO CATÁLOGO]; declaração (linha 147) marcada. Conferido no catálogo, seção 4 |
| E2 | Resolvido | W1 (linha 99) e W8 (linha 106) separam catálogo e ficha; oferta de E-W1 (linhas 77 e 78) separada |
| E3 | Resolvido | Declaração (linha 126), ressalva (linha 128), EO1 (linha 272), regra 7 (linha 38) e seção 3 (linha 238) |
| E4 | Resolvido | Linha 126: "Pós-graduação em Anestesiologia Avançada da Ufape [CONFIRMAR autorização]" |
| E5 | Resolvido | Linha 130: pergunta opcional, finalidade, política de privacidade, aprovação humana, só números somados; pedido 8 (linha 296) |

### 4.2 Reconferência dos ajustes

| Item | Situação | O que ainda falta |
|---|---|---|
| EA1 | Não resolvido | "programa hora a hora" e "programa por hora" para todos os eventos seguem nas linhas 63, 67 e 68. Para 700 e 202 só há grade por tema na ficha. Trocar por "o programa antes da inscrição" ou marcar [CONFIRMAR NO CATÁLOGO] para os gravados |
| EA2 | Não resolvido | Linha 312: "(precisa, próxima, transparente)" sem marcação. contexto/ufape-geral.md diz "técnica, próxima, confiante [SUPOSIÇÃO]". Marcar [SUPOSIÇÃO] |
| EA3 | Não resolvido | A frase segue "não confere diploma nem equivale a pós-graduação" nas linhas 37, 68, 126, 149, 176, 204, 226 e 281. Acrescentar "graduação ou" |
| EA4 | Não resolvido | 202 tem modalidade "Online" no catálogo (seção 9, local "Online"); "gravado" e "gravação" vêm da ficha e seguem sem marcação nas linhas 200, 203, 204 e 236; a linha 68 diz "simpósios gravados". Marcar "gravado [CONFIRMAR NO CATÁLOGO]". O 700 tem "Gravação" no nome do catálogo e está coberto |
| EA5 | Não resolvido | Tabela 1.1 e tabela de alternativas de E-W1 (linha 86) sem a ressalva de resumo de busca na legenda. A nota da linha 59 fala de limite da busca, não de resumo de busca a conferir na fonte primária |

### 4.3 Achados novos (regressão)

Nenhum. Datas e preços conferidos no catálogo: workshop (20/11/2026, 16 h, 30 vagas, R$ 1.250,00, R$ 450,00, cupom de 20%), 68634 (seção 4), 700 (10x de R$ 98,00, R$ 980,00 por cálculo), 202 (6x de R$ 78,00, R$ 468,00 por cálculo), 106 (6 h, R$ 159,00), 462 (8 h, R$ 216,00), Pós e provas da ponte (657, 68609, 359, 68623, 352, 68635, 68616, 68608, 68615; provas 68639, 68640, 68660, 68645, 68654, 68651, 68658).

### 4.4 Varredura de regressão

| Conferência | Resultado |
|---|---|
| Dado novo errado | Nenhum |
| Frase de certificação ou nota do MEC fora de proibição | Nenhuma |
| "Pós em" | Só como proibição (linha 239) |
| Travessão ou meia-risca | Nenhum encontrado [SUPOSIÇÃO: leitura visual] |

### 4.5 auditorias/02-estrategia-e-posicionamento.md, item por item

| # | Item | Resultado |
|---|---|---|
| 1 | Uma única meta principal | Atendido (herdado) |
| 2 | Persona e oferta nomeadas | Atendido |
| 3 | 8 canais | Não se aplica (herdado) |
| 4 | Alternativa real | Atendido, com EA5 aberto |
| 5 | Todo pilar tem prova | Atendido (E2 resolvido), com EA1 e EA4 abertos |
| 6 | Voz com exemplos | **Falha (EA2)**: traços não validados aplicados como regra |
| 7 | Tempo e verba | Não se aplica |
| 8 | Sem promessa | Atendido |
| 9 | Preços e condições do catálogo ou marcados | Atendido (E1, E3 resolvidos) |

### 4.6 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, CH batem | Atendido (E1, E2 resolvidos) |
| Dados do curso | Status aberto ou sem chamada | Atendido (68634 sem chamada) |
| Dados do curso | Modalidade correta | **Falha (EA4)**: 202 como gravado sem marcação |
| Regulação | Evento sem diploma e sem equivaler a graduação ou pós | **Falha (EA3)** |
| Regulação | Sem MEC, sem certificado | Atendido |
| Promessas | Todos | Atendido |
| Preço (CDC) | Valor, parcelas, condições | Atendido |
| Preço (CDC) | Desconto com regra, público e validade | Atendido (marcado) |
| Preço (CDC) | Urgência real | Atendido |
| Pessoas e dados | Autorização | Atendido |
| Pessoas e dados | Formulários com finalidade | Atendido (E5 resolvido) |
| Pessoas e dados | Nenhum dado pessoal | Atendido |
| Plataformas | Destino entrega o prometido | Atendido ("apenas teórico" obrigatório) |
| Anúncios | Demais itens | Atendido ou não se aplica |

**RESULTADO:** Aprovado ( )  Bloqueado (X).

### 4.7 Veredito: CORRIGIR

O que falta: EA1, EA2, EA3, EA4, EA5. São trocas de texto curtas, sem dependência da Ufape.

---

## 5. Encaminhamento

- Os três arquivos **voltam para o agente posicionamento**. Não seguem para a aprovação humana nesta rodada.
- Prioridade: Eventos primeiro (workshop em 20/11/2026, onda 1); só faltam EA1 a EA5. Depois Pós (N-P1 antes de qualquer mensagem com preço).
- Nota para o orquestrador: o status do arquivo de Pós (linha 6) diz que os ajustes PA1 a PA7 "não foram pedidos nesta rodada", e Livres e Eventos dizem o mesmo dos seus. Na próxima devolução, deixar explícito ao agente que os ajustes são obrigatórios.
- O agente mensagens (etapa 2.2) não deve partir destes arquivos antes da terceira rodada do qa.
- Peças com comparação com concorrente seguem dependendo do aprovador de contexto/ufape-geral.md (tabela vazia) [CONFIRMAR].
- Nada foi publicado, enviado ou pago. Os arquivos revisados não foram editados.

---

## Lista 1. Fatos (com fonte)

- 30 turmas de Pós abertas; 29 de Medicina Veterinária (719 fora), 28 semipresenciais e 1 presencial (68632) (catálogo, seção 2).
- Totais das Pós veterinárias abertas, do menor: 68629 R$ 16.456,00; 698 R$ 26.970,00; 333 R$ 28.050,00; 60 R$ 29.700,00 (catálogo, seção 2).
- 542 com 12 h e 102 com 9 h; 602 com 4 h; 541 e 107 com 5 h; 104 e 106 com 6 h (catálogo, seção 5).
- Modalidade "Gravação" só em 591 e 602 na seção 5; os demais online dizem "Online" ou "On-line" (catálogo, seção 5).
- 202: local "Online", sem "gravação" no nome; 700: "Gravação" no nome (catálogo, seção 9).
- 573 com modalidade grafada "Semiprensecial" (catálogo, seção 4).
- Voz da marca: "técnica, próxima, confiante [SUPOSIÇÃO]" (contexto/ufape-geral.md).
- Ajustes PA, LA e EA e seus textos de correção: qa-de-marketing-geral-2026-10-26-dep02b.md, seções 2.4, 3.4 e 4.4.

## Lista 2. Suposições

- [SUPOSIÇÃO] As citações de fichas, contextos de linha e saídas de inteligência seguem fiéis, como no dep02b (não reconferidas nesta rodada).
- [SUPOSIÇÃO] Ausência de travessão e meia-risca conferida por leitura visual, sem busca por caractere.
- [SUPOSIÇÃO] A redação final das correções é do agente posicionamento; as propostas aqui respeitam o catálogo.

## Lista 3. Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Se os cursos online e os minicursos são gravados ou ao vivo; se o 202 é gravação.
- [CONFIRMAR NO CATÁLOGO] Status, modalidade e carga horária do 68634; validade do cupom SIMPNEUROMONIT e público elegível.
- [CONFIRMAR NO CATÁLOGO] Regras das provas de bolsa, turma mínima (15 ou 20) e condições de turma das Pós.
- [CONFIRMAR] Aprovador de peças com comparação com concorrente (contexto/ufape-geral.md).
- [CONFIRMAR] Validação dos traços de voz e nova rodada do guia de marca (dep02a).

## Fontes

docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/catalogo-de-cursos.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/conformidade-educacional.md; saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02b.md; saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/posicionamento-livres-2026-10-26.md; saidas/02-estrategia-e-posicionamento/posicionamento-eventos-2026-10-26.md.
