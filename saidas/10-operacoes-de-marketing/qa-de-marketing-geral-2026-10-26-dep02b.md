# QA de marketing: posicionamento de Pós, Livres e Eventos (etapa 1.7)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (pos, livres e eventos)
- Data: 26/10/2026
- Peças revisadas (não editadas):
  - saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/posicionamento-livres-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/posicionamento-eventos-2026-10-26.md
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md, contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md
  - contexto/catalogo-de-cursos.md (inteiro, seções 1 a 9)
  - auditorias/02-estrategia-e-posicionamento.md
  - auditorias/conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02a.md (QA do guia de marca)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 e 2, para a meta e o recorte)
  - saidas/01-inteligencia-de-mercado/inteligencia-concorrencia-pos-2026-10-26.md (cabeçalho, seções 0 a 3, para conferir a fonte e a ressalva das afirmações sobre concorrentes)
- Não conferi nas fontes primárias: fichas de contexto/cursos/ (68610, 68614, 573, 623, 644, 454, 657, 698, 720, evento neuro-summit, 700, 202), os arquivos de persona, a pesquisa de mercado e a inteligencia-concorrencia de Livres. As citações dessas fontes foram aceitas como estão [SUPOSIÇÃO: transcrição fiel]. Como regra, todo dado que os arquivos dizem vir "da ficha" foi tratado como dado fora do catálogo.
- Dados pessoais: nenhum nesta revisão. Nenhum docente é nomeado aqui.
- Números de linha: referem-se aos arquivos revisados como estavam em 26/10/2026.

---

## 1. Vereditos

| Arquivo | Veredito | Bloqueantes | Ajustes |
|---|---|---|---|
| posicionamento-pos-2026-10-26.md | **CORRIGIR** | P1 a P6 | PA1 a PA7 |
| posicionamento-livres-2026-10-26.md | **CORRIGIR** | L1 a L6 | LA1 a LA6 |
| posicionamento-eventos-2026-10-26.md | **CORRIGIR** | E1 a E5 | EA1 a EA5 |

Os três arquivos são sólidos: nomeiam alternativas reais, removem atributos sem prova, não prometem emprego, renda ou aprovação, não usam frase de certificação nem nota do MEC e nunca tratam o hospital próprio como exclusivo. Voltam para o agente posicionamento porque cada um falha em pelo menos um item de auditorias/conformidade-educacional.md, e pela regra do QA qualquer falha de conformidade bloqueia, sem exceção. Vários bloqueantes repetem erros já apontados no QA do guia de marca (dep02a): ver seção 5.

---

## 2. posicionamento-pos-2026-10-26.md

### 2.1 Auditoria 02-estrategia-e-posicionamento, item por item

| # | Item | Resultado do QA | Observação |
|---|---|---|---|
| 1 | Uma única meta principal | Atendido (herdado) | Linha 282 cita a meta única do plano do cmo (turmas de Pós confirmadas com a turma mínima até o início), que confere com cmo-geral, seção 1. Quantidade-alvo [CONFIRMAR] |
| 2 | Persona e curso ou oferta nomeados | Atendido | P1 a P4 (seção 1.4); turmas e provas por código (seções 3.2 a 3.5) |
| 3 | 8 canais avaliados | Não se aplica (herdado) | Posicionamento não escolhe canal; vale o plano do cmo, seção 5 |
| 4 | Nomeia a alternativa real | Atendido | Oito alternativas (seção 1.2): Anclivepa-SP, Qualittas, Equalis, EAD e agregadores, residência, pós de universidades, cursos curtos (inclusive os livres da Ufape) e adiar. Fonte da inteligencia-concorrencia citada por linha. Ressalva de resumo de busca só no cabeçalho e nas fontes (PA1) |
| 5 | Todo pilar tem prova | Falha, corrigir (P3, P4) | As 3 provas da declaração existem, mas a prova 3 e o atributo A4 usam dado só da ficha sem marcação (P4). O atributo A9 tem rótulo errado de modalidade (P3). "Docentes da rotina" e "hospital nos módulos" foram rebaixados a [SUPOSIÇÃO], como deve ser |
| 6 | Regras de voz com exemplos | Atendido com correção (P5) | Quatro pares na seção 5; dois "assim sim" falham na conformidade (P5) |
| 7 | Cabe no tempo e na verba | Não se aplica | Sem custo de mídia |
| 8 | Sem promessa de emprego, aprovação ou salário | Atendido | Seções 1.4, 2.2, 4 e 5. "Especialize-se" na frase é o nome do produto (especialização), não promessa de título; a seção 5 já veta "torne-se especialista" como promessa |
| 9 | Preços, bolsas e condições do catálogo ou marcados | Falha, corrigir (P2, P4, P5) | Todos os preços conferem com o catálogo, seção 2 (conferi 68629, 333, 60, 699, 352, 359, 698, 341, 289, 68632, 68609, 68623, 657 e 719). Falham: matrícula omitida (P2); regras de bolsa e condições de turma da ficha ou do contexto sem [CONFIRMAR NO CATÁLOGO] em parte dos trechos (P4, P5) |

### 2.2 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH, duração e turno batem com o catálogo | Falha (P1, P3) | Códigos, turmas, datas e CH conferidos (A6: 68606 IX, 68616 IX, 68608 VIII, 68636 VIII, 68609 VIII, 707 VII, 68615 VII, 68604 VI; em andamento 68605 XI, 666 XI, 68607 X; 750 h em 68635 e 68623; 600 h em 707). Contagens conferidas: 30 turmas abertas, 22 provas abertas, 24 das 30 entre 13/03 e 28/05/2027. Falham: linha 147 e A9 (linha 88) |
| Dados do curso | Status "aberto" ou sem chamada | Atendido | 677, 586, 650, 68607 e demais "verificar" ficam sem chamada de compra (linhas 182, 196, 212, 221) |
| Dados do curso | Modalidade clara e correta | Falha (P1, P3) | 68632 é presencial; 719 não é veterinária |
| Regulação | Graduação: ato do catálogo | Não se aplica | |
| Regulação | Pós lato sensu sem "reconhecida pelo MEC" | Atendido | Frases de MEC só na seção 5 como proibição. Linha 71 cita "certificado de especialização lato sensu" do contexto, já marcado como não utilizável em peça |
| Regulação | Curso livre sem diploma | Atendido com ajuste (PA6) | Linha 214; alinhar à redação da auditoria |
| Regulação | Nota MEC só com fonte e ano | Atendido | Nenhuma nota |
| Promessas | Sem promessa de emprego, salário, aprovação | Atendido | |
| Promessas | Empregabilidade com fonte | Não se aplica | |
| Promessas | Superlativos só com fonte | Atendido | Seção 5 veta; nenhum usado. Ver PA4 sobre "reta final" |
| Promessas | Comparação com concorrente objetiva e verificável | Atendido com ressalva (PA1, PA2) | Objetiva e não depreciativa; "onde a Ufape perde" é dito com honestidade. Fonte é resumo de busca (confiança A ou M na inteligencia-concorrencia); a ressalva precisa acompanhar as tabelas |
| Preço (CDC) | Valor, parcelas e condições completas, sem esconder matrícula | Falha (P2) | Matrícula omitida em várias turmas |
| Preço (CDC) | Bolsa e desconto com regra, público e validade | Falha (P5) | Exemplo da linha 270 e valor de P4 (linha 103) |
| Preço (CDC) | Urgência real | Atendido com ajuste (PA4) | "Últimas vagas" e "vagas limitadas" só como proibição |
| Preço (CDC) | Prouni, Fies, financiamento | Não se aplica | |
| Pessoas e dados | Autorização de depoimentos e imagens | Atendido | Nenhum docente nomeado; [CONFIRMAR autorização] em A5 e 2.2 |
| Pessoas e dados | Menores | Não se aplica | |
| Pessoas e dados | Formulários com finalidade | Não se aplica | |
| Pessoas e dados | WhatsApp e e-mail com consentimento | Não se aplica | |
| Pessoas e dados | Nenhum dado pessoal | Atendido | Linha 122 pede só lista agregada |
| Plataformas e anúncios | Todos os itens | Atendido ou não se aplica | Linha 214 (não mirar "pós EAD barata") está alinhada. Nenhuma característica pessoal; nenhuma urgência falsa |

**RESULTADO:** Aprovado ( )  Bloqueado (X). Itens bloqueados: nome e modalidade conforme o catálogo; modalidade correta; preço com matrícula; bolsa com regra, público e validade.

### 2.3 Problemas que bloqueiam

**P1. Seção 2.2, linha 147 (parágrafo do posicionamento).**
- Problema: "a Faculdade UFAPE oferece pós-graduação semipresencial em Medicina Veterinária, com 30 turmas abertas em 14 áreas". Das 30 turmas abertas, a 719 (Inteligência Artificial na Saúde) não é de Medicina Veterinária (o próprio arquivo a tira do posicionamento na linha 106) e a 68632 é presencial, não semipresencial (catálogo, seção 2). A frase vai virar texto de peça.
- Correção proposta: "a Faculdade UFAPE oferece pós-graduação em Medicina Veterinária, com 29 turmas abertas em São Paulo e em Goiânia (28 semipresenciais e 1 presencial, a 68632)". Ajustar também a nota da linha 149 e o atributo A1 (linha 80) para dizer que "30 turmas em 14 áreas" inclui a 719.

**P2. Preço sem matrícula: linha 102 (P3, "Prova a mostrar"), linhas 193 a 200 (seção 3.2) e linha 206 (seção 3.3).**
- Problema: 333, 60, 699, 352, 359, 698, 341, 289, 68632, 68609 e 68623 aparecem com parcelas e total, mas sem a matrícula de R$ 250,00 que está no catálogo. Só 68629 traz a matrícula (R$ 350,00). A regra da linha (contexto/pos-graduacao.md: "toda peça com preço mostra número de parcelas, valor da parcela, total e matrícula") e o item de CDC da conformidade exigem a matrícula. Essas tabelas são a fonte que o agente mensagens vai copiar.
- Correção proposta: acrescentar "matrícula R$ 250,00" em cada uma, por exemplo "333 Citopatologia (30x de R$ 935,00, R$ 28.050,00, matrícula R$ 250,00)". Valores conferidos no catálogo, seção 2.

**P3. Atributo A9, linha 88 ("Goiânia presencial"); repete o C4 do dep02a.**
- Problema: o rótulo diz "Goiânia presencial", mas só a 68632 é presencial; 289, 68609 e 68623 são semipresenciais (catálogo, seção 2). O uso permitido ("Pós-graduação com prática presencial em Goiânia") está correto, o rótulo não. Também falta dizer que o local da prática em Goiânia é [CONFIRMAR].
- Correção proposta: "A9. Goiânia: 4 turmas abertas (68632 presencial; 289, 68609 e 68623 semipresenciais, com módulos práticos presenciais) e 3 provas (68640, 68642, 68644). Local da prática [CONFIRMAR]".

**P4. Dado só da ficha ou do contexto sem [CONFIRMAR NO CATÁLOGO]: linhas 83 (A4), 84 (A5), 87 (A8), 157 (prova 3), 245 (objeção 3) e 2.2 (linha 147, "qual é a turma mínima e o que acontece se ela não fechar").**
- Problema: turma mínima de 20, orientação de passagem e hotel, reembolso da inscrição, 1ª mensalidade 30 dias antes, contagem de docentes por ficha e módulos de 3 dias em 666 e 707 vêm das fichas ou do contexto da linha, não do catálogo. Só A2 e A3 levam a marcação. A turma mínima ainda diverge (15 na página da prova, 20 nas páginas de curso). O arquivo de Livres usa um selo por atributo ("Prova no catálogo" ou "Só na ficha [CONFIRMAR NO CATÁLOGO]") e o de Pós não: falta de consistência e falha no item 9 da auditoria 02.
- Correção proposta: acrescentar à tabela 1.3 a mesma coluna de selo do arquivo de Livres e marcar A4, A5, A8, a prova 3 da seção 2.3 e a objeção 3 com "[CONFIRMAR NO CATÁLOGO]". Na linha 147, escrever "qual é a turma mínima [CONFIRMAR NO CATÁLOGO: 15 ou 20]".

**P5. Seção 5, exemplos "assim sim" das linhas 270 e 271, e valor de P4 na linha 103; repete o C3 e o C5 do dep02a.**
- Problema: linha 270, "Inscrição de R$ 100,00. Cada prova tem 11 bolsas: 2 de 50%, 4 de 25% e 5 de 10%.", não traz a data da prova, o público elegível, a regra de não acumulação e intransferência nem a marcação de que as regras não estão no catálogo. É o mesmo exemplo que o dep02a bloqueou no guia de marca (C3). Linha 271, "A turma abre com no mínimo 20 alunos", afirma o número que o próprio arquivo marca como 15 ou 20 [CONFIRMAR]. Linha 103, "decide a matrícula depois do resultado, em até 10 dias úteis", usa regra da página da prova sem marcação.
- Correção proposta:
  - Linha 270: "Prova de bolsa em 27/11/2026, inscrição de R$ 100,00. Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. A bolsa não é acumulativa nem transferível. [CONFIRMAR NO CATÁLOGO: regras das bolsas, público elegível e turma de destino]".
  - Linha 271: "A turma só abre com o mínimo de alunos [CONFIRMAR NO CATÁLOGO: 15 ou 20]. Compre passagem só depois da confirmação."
  - Linha 103: acrescentar "[CONFIRMAR NO CATÁLOGO]" depois de "10 dias úteis".

**P6. Seção 3.2, linha 199 (679 Infectologia em "áreas em que a Ufape está quase sozinha").**
- Problema: a inteligencia-concorrencia-pos (resumo, item 3) lista as áreas "quase sozinhas" e a Infectologia (679) não está entre elas. A afirmação sobre ausência de concorrente fica sem fonte.
- Correção proposta: tirar a 679 da tabela 3.2 e levá-la para 3.5 com "concorrente: sem fonte", ou citar a seção da inteligencia-concorrencia que a sustenta.

### 2.4 Ajustes da mesma rodada

- **PA1. Ressalva de resumo de busca nas tabelas (linhas 31, 63 e 219).** A ressalva está só no cabeçalho (linha 22) e nas fontes (linha 372). Acrescentar na legenda das tabelas 1.2 e 3.5 e no resumo da seção 0: "dados de concorrentes: resumo de busca de 26/10/2026 (inteligencia-concorrencia-pos), conferir na fonte primária antes de qualquer peça; peça comparativa passa pelo aprovador de contexto/ufape-geral.md [CONFIRMAR aprovador]".
- **PA2. P4, linha 103 ("prova em 27/11/2026, depois do fim das inscrições da Anclivepa-SP (07/11/2026)").** Está na coluna "Prova a mostrar", o que convida a peça comparativa. A inteligencia-concorrencia diz que parte do calendário da Anclivepa vem de cópia não oficial do edital (confiança M). Mover para "uso interno de calendário", não prova de peça.
- **PA3. Frase da seção 2.1, linha 141 ("condições à vista antes da matrícula").** "À vista" é termo de pagamento em toda a linha (Pix ou boleto). Na peça, a frase pode ser lida como pagamento à vista. Sugestão: "condições claras antes da matrícula" ou "condições na página antes da matrícula". Decisão de redação do agente mensagens; registrar o risco.
- **PA4. Seção 3.5, linhas 225 e 228 ("reta final").** 68604 (31/10/2026) e 707 (30/10/2026) começam em dias. A data é real, mas "reta final" vira urgência fácil. Acrescentar: "na peça, só a data de início, sem 'reta final' nem 'últimos dias'".
- **PA5. A6, linha 85 (Unicruz 9ª edição; Qualittas desde 2014).** Citar a fonte na célula (inteligencia-concorrencia C-5 e C-2), como nas demais.
- **PA6. Linha 214 (frase do curso livre).** Alinhar à conformidade: "curso livre não confere diploma nem equivale a graduação ou pós-graduação".
- **PA7. Exemplos da seção 5 e guia de marca.** A linha 265 remete ao guia de marca, que está em "corrigir" (dep02a). Acrescentar que os exemplos herdados só valem depois da nova rodada do guia.

---

## 3. posicionamento-livres-2026-10-26.md

### 3.1 Auditoria 02-estrategia-e-posicionamento, item por item

| # | Item | Resultado do QA | Observação |
|---|---|---|---|
| 1 | Uma única meta principal | Atendido com ajuste (LA1) | Linha 378: "Meta principal do plano do cmo: turmas de Pós confirmadas; para Livres, vendas por curso". No cmo, "vendas por curso livre" é métrica de apoio, não meta. A redação sugere duas metas |
| 2 | Persona e curso nomeados | Atendido | P-L1 a P-L5; cursos por código |
| 3 | 8 canais avaliados | Não se aplica (herdado) | Linha 380 cita o plano do cmo, seção 5 |
| 4 | Nomeia a alternativa real | Atendido | Não estudar agora, Vetlove, Vetsapiens, Quadam, Animal Health Science Ecosystem, Anclivepa, Medvep, Fisio Care Pet, CBCV, grupos da UFPel e da UEL, treinamento do fabricante ([SUPOSIÇÃO]) e a Pós da própria Ufape. Fonte e data na tabela 1.1; ressalva de resumo de busca no cabeçalho (linha 21) e nas fontes (linha 446) |
| 5 | Todo pilar tem prova | Falha, corrigir (L2, L3, L5) | O sistema de selos é o melhor dos três arquivos. Falham: "os docentes atuam na rotina" no parágrafo de F1 (L2); "docentes brasileiros" em F5 (L5); "a cada 15 dias" generalizado para todos os grupos (L3) |
| 6 | Regras de voz com exemplos | Atendido por herança, com ressalva (LA6) | Remete ao guia de marca, que está em "corrigir" (dep02a). A seção 3 traz "usar no lugar" para cada proibição |
| 7 | Cabe no tempo e na verba | Não se aplica | |
| 8 | Sem promessa de emprego, aprovação ou salário | Atendido | 488 sem promessa de aprovação; "cobrar pelo serviço" vetado (linha 307) |
| 9 | Preços e condições do catálogo ou marcados | Atendido com correção (L4) | Conferi 573, 68614, 623, 68637, 616, 68618, 68638, 560, 602, 131, 411, 103, 461, 669, 454, grupos de R$ 100,00 e de R$ 734,00, 347 e 501: todos batem; totais no cartão marcados como cálculo e corretos. Falha a faixa do minicurso (L4) |

### 3.2 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH batem com o catálogo | Falha (L1, L4) | Contagens conferidas: 22 gravados, 13 minicursos, 25 presenciais fora de venda, 7 grupos de R$ 734,00. Falham: 616 como presencial (L1); "8 horas" com a 669, de 6 h (L4) |
| Dados do curso | Status "aberto" ou sem chamada | Atendido | 718, 575, 605, 639, 640, 641 e os 25 presenciais em "verificar" ou "sem venda" ficam fora |
| Dados do curso | Modalidade clara e correta | Falha (L1, LA3) | 616 tem modalidade "On-line" no catálogo e entra em F1 "presencial hands-on"; o plano do cmo também a conta como "online com data" |
| Regulação | Pós lato sensu sem MEC | Não se aplica | |
| Regulação | Curso livre sem diploma | Atendido com ajuste (LA4) | Todas as declarações dizem "não confere diploma nem equivale a pós-graduação". Alinhar à redação da auditoria ("graduação ou pós-graduação"), como pedido no A10 do dep02a |
| Regulação | Nota MEC | Atendido | "Selo do MEC" da ficha 68614 e da página de 599 só na seção 3, como proibição |
| Promessas | Sem promessa de resultado | Atendido | |
| Promessas | Superlativos | Atendido | "Última geração", "de ponta", "100% prático" removidos |
| Promessas | Comparação com concorrente | Atendido com ressalva | Objetiva. A frase do parágrafo de F4 (linha 240), "diferente do grupo universitário, feito para estudantes e docentes", resume a fonte ("abertos à comunidade acadêmica"); manter a palavra da fonte. Comparação de preço com a Quadam só com câmbio datado (linha 259): correto |
| Preço (CDC) | Valor, parcelas e condições completas | Atendido | À vista, parcelas e total no cartão. Matrícula: nenhum livre aberto tem matrícula no catálogo, salvo 717 (fora) |
| Preço (CDC) | Bolsa e desconto com regra | Atendido | Desconto de 720 só na ficha e marcado; cupom e promoções não usados |
| Preço (CDC) | Urgência real | Atendido | "Turma reduzida" e "garanta sua vaga" de 573 vetados (linha 302). A janela de cancelamento de 68614 (29/10/2026, cálculo correto: 28/11 menos 30 dias) é usada para restringir, não para pressionar |
| Preço (CDC) | Prouni, Fies | Não se aplica | |
| Pessoas e dados | Autorização | Atendido | Docentes citados por papel; [CONFIRMAR autorização] |
| Pessoas e dados | Formulários com finalidade | Atendido | Linha 209 pede aviso de finalidade e aprovação humana para a pergunta na prova de bolsa |
| Pessoas e dados | Nenhum dado pessoal | Atendido | Linha 280 exige histórias anonimizadas; linha 368 pede só números somados |
| Plataformas e anúncios | Todos | Atendido ou não se aplica | |

**RESULTADO:** Aprovado ( )  Bloqueado (X). Itens bloqueados: nome, modalidade e CH conforme o catálogo; modalidade correta.

### 3.3 Problemas que bloqueiam

**L1. Seção 2.1, linha 84 (616 em F1 "presencial hands-on").**
- Problema: no catálogo (seção 5, online e gravados) a 616 tem modalidade "On-line" e local "Presencial e Online". O plano do cmo (seção 2.2) a conta como "online com data". O arquivo marca [CONFIRMAR NO CATÁLOGO], mas a põe na tabela de presenciais, no par "616 e 68618 e Pós 657" (linha 136) e na variação A1 como "prática de anestesia felina" (linha 321). Falha no item "EAD não aparece como presencial".
- Correção proposta: tirar a 616 da tabela F1 e criar uma linha à parte, "616 Imersão Avançada em Anestesia Felina, 05/12/2026, 12 h, R$ 990,00 ou 5x de R$ 240,00 (R$ 1.200,00 por cálculo). Modalidade [CONFIRMAR NO CATÁLOGO: online, presencial ou híbrida]. Sem posicionamento de prática até a confirmação". Na linha 321, trocar "prática de anestesia felina" por "imersão em anestesia felina, modalidade [CONFIRMAR NO CATÁLOGO]".

**L2. Parágrafo de F1, linha 134 ("Os docentes atuam na rotina e, em cursos como a Ecocardiografia Hands-On, quem ensina coordena a Pós da mesma área").**
- Problema: "os docentes atuam na rotina" não tem prova por docente. O arquivo de Pós (linha 84) e o contexto geral tratam isso como [SUPOSIÇÃO]. Aqui vira afirmação na declaração. O vínculo de 573 com a Pós 698 está nas fichas, mas só pode ir com autorização (F1.6). O mesmo parágrafo usa "demonstração em pacientes com indicação clínica" e "proporção por participante", que só existem na ficha 68614.
- Correção proposta: "O roteiro mostra teoria, demonstração e prática com o equipamento [CONFIRMAR NO CATÁLOGO por curso]. Em alguns cursos, quem ensina também coordena a Pós-graduação da mesma área [CONFIRMAR autorização]." Tirar "os docentes atuam na rotina".

**L3. Declaração de F4, linhas 239 e 240 ("Um encontro marcado... a cada 15 dias"; "anual de R$ 734,00").**
- Problema: "a cada 15 dias" é dado só da ficha 644 e a declaração de uma linha o aplica a todos os grupos; a própria linha 242 reconhece que não vale para os outros. "Anual" está no nome de 644, 643, 713, 642 e 712, mas não de 721 e 720, que também custam R$ 734,00.
- Correção proposta: uma linha: "Um encontro marcado para discutir casos com quem é da área." Parágrafo: "Grupos com entrada de R$ 100,00 (68663, 68665, 68666; período coberto [CONFIRMAR NO CATÁLOGO]) e grupos de R$ 734,00 à vista ou 10x de R$ 88,00 (R$ 880,00 por cálculo). Frequência dos encontros [CONFIRMAR NO CATÁLOGO por grupo]".

**L4. Declaração de F3, linhas 204 e 205 ("8 horas... de R$ 185,00 a R$ 300,00"; "8 h gravadas").**
- Problema: o teto de R$ 300,00 é a 669, que tem 6 h (catálogo, seção 5). A frase mistura carga e preço que não batem. "Gravadas" não está no catálogo (modalidade "Online"). A última frase do parágrafo ("há cursos maiores e a Pós na mesma área") contradiz a regra 7 do próprio arquivo; a nota da linha 207 a manda tirar, mas ela continua na declaração.
- Correção proposta: "6 a 8 horas para ter por onde começar numa área da clínica, de R$ 185,00 a R$ 300,00 à vista" ou tirar a 669 e usar "8 horas, de R$ 185,00 a R$ 289,00 à vista". Trocar "gravadas" por "online [CONFIRMAR NO CATÁLOGO: gravado ou ao vivo]". Apagar a frase sobre a Pós da declaração.

**L5. F5, linhas 258, 264, 267 e 268 ("docente brasileiro", "vistos por docentes brasileiros").**
- Problema: a prova citada ("347 e 501 existem em espanhol") não prova a nacionalidade do docente; a própria célula marca "Que o docente é da Ufape: [CONFIRMAR]". A declaração afirma sem marcação. O formato está bloqueado, mas a declaração fica registrada como texto de referência.
- Correção proposta: marcar a declaração e a categoria com "[SUPOSIÇÃO: docente e origem do conteúdo a confirmar]" ou trocar por "cursos gravados da Faculdade UFAPE, em espanhol (347) e com legenda em espanhol (501)".

**L6. Seção 2.4, linha 244 (par 68665 e prova 68641).**
- Problema: o arquivo de Pós (linha 207) e o plano do cmo (P3) bloqueiam qualquer peça das provas 68641 e 68642 até a correção dos links trocados de Cardiologia SP e GO. O arquivo de Livres usa o par sem aviso.
- Correção proposta: acrescentar "68641 com link trocado (P3): sem peça até a correção".

### 3.4 Ajustes da mesma rodada

- **LA1. Linha 378 (meta).** Reescrever: "Meta única do plano do cmo: turmas de Pós confirmadas. Métrica de apoio desta linha: vendas por curso livre presencial e online [CONFIRMAR]."
- **LA2. Linha 172 (F2, "aula gravada por tema").** No catálogo, a modalidade dos 22 itens varia entre "Online", "On-line" e "Gravação". Marcar "gravado" [CONFIRMAR NO CATÁLOGO] nos que não dizem gravação (ex.: 137, 131).
- **LA3. Linha 81 (573 "semipresencial").** O catálogo grafa "Semiprensecial". A leitura como semipresencial está certa, mas registrar a correção de grafia na lista de pedidos ao catálogo.
- **LA4. Frase do curso livre (linhas 67, 134, 173, 205, 240, 268 e 300).** Alinhar a "não confere diploma nem equivale a graduação ou pós-graduação".
- **LA5. Tabela 1.1 e seção 4.** A ressalva de resumo de busca está no cabeçalho; repetir na legenda das tabelas de alternativas, que serão copiadas para as mensagens.
- **LA6. Linha 383 (voz).** Registrar que os exemplos herdados do guia de marca só valem depois da nova rodada do guia (dep02a em "corrigir").

---

## 4. posicionamento-eventos-2026-10-26.md

### 4.1 Auditoria 02-estrategia-e-posicionamento, item por item

| # | Item | Resultado do QA | Observação |
|---|---|---|---|
| 1 | Uma única meta principal | Atendido (herdado) | Linha 294 cita "inscrições do evento" como métrica de apoio, o que confere com o cmo |
| 2 | Persona e oferta nomeadas | Atendido | E1a a E1d, E2a e E2b; workshop, 68634, 700 e 202 |
| 3 | 8 canais avaliados | Não se aplica (herdado) | |
| 4 | Nomeia a alternativa real | Atendido | Animal Health Science Ecosystem, Congresso Brasileiro da Anclivepa, Medvep, CBCV, Vetlove, BEVA, WVC, Berna, não ir e produtos da própria Ufape. Ressalva de busca limitada na linha 57; resumo de busca no cabeçalho (linha 22) e nas fontes (linha 354) |
| 5 | Todo pilar tem prova | Falha, corrigir (E2) | W1 e W8 têm selo "Prova no catálogo" com parte do dado só na ficha |
| 6 | Regras de voz com exemplos | Atendido por herança, com ajuste (EA2) | Linha 299 aplica os traços "precisa, próxima, transparente" do guia, ainda não validados (A1 do dep02a) |
| 7 | Cabe no tempo e na verba | Não se aplica | |
| 8 | Sem promessa de emprego, aprovação ou salário | Atendido | |
| 9 | Preços e condições do catálogo ou marcados | Falha, corrigir (E1, E3) | Preços conferidos: R$ 1.250,00, R$ 450,00, cupom de 20%, 700 (R$ 780,00 ou 10x de R$ 98,00; R$ 980,00 por cálculo), 202 (R$ 285,00 ou 6x de R$ 78,00; R$ 468,00 por cálculo). Falham: status de 68634 (E1) e cupom sem validade na declaração (E3) |

### 4.2 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH batem | Falha (E1, E2) | Data 20/11/2026, local Av. Tiradentes, 960 (Unidade 2), 16 h e 30 vagas conferem com o catálogo, seção 9; 21/11/2026 confere com o briefing (decisão 6). Falham: 68634 (E1) e o selo de W1 (E2) |
| Dados do curso | Status "aberto" ou sem chamada | Falha (E1) | 68634 está "verificar" no catálogo, seção 4 |
| Dados do curso | Modalidade clara | Falha (E1) | 68634 aparece no catálogo como "Presencial" e local "Saiba Mais"; o arquivo o trata como transmitido e gravado sem marcar a divergência |
| Regulação | Evento sem diploma | Atendido com ajuste (EA3) | Todas as declarações dizem "não confere diploma nem equivale a pós-graduação" |
| Regulação | Sem MEC, sem certificado | Atendido | "Certificado UFAPE" removido (linha 103, linha 218) |
| Promessas | Sem promessa de resultado | Atendido | EO4 não promete eficácia do BIS |
| Promessas | Superlativos | Atendido | "Primeiro", "único", "inédito" vetados. "De ponta a ponta" (linha 195) já leva [CONFIRMAR] |
| Promessas | Comparação com concorrente | Atendido | Objetiva; possível colisão de data com congressos marcada como [CONFIRMAR] |
| Preço (CDC) | Valor, parcelas e condições completas | Atendido com ressalva | Parcelamento do presencial marcado [CONFIRMAR NO CATÁLOGO]; valores com cupom marcados como cálculo e [SUPOSIÇÃO] |
| Preço (CDC) | Desconto com regra, público e validade | Falha (E3) | Cupom SIMPNEUROMONIT sem validade no parágrafo de E-W1 (linha 120) e em EO1 |
| Preço (CDC) | Urgência real | Atendido | "Somente 30 vagas" e "Garanta a sua vaga" da página vetados; "PROMOÇÃO VÁLIDA POR TEMPO LIMITADO" do 202 vetada |
| Pessoas e dados | Autorização | Atendido | Ninguém nomeado; convidados "a definir" fora |
| Pessoas e dados | Formulários com finalidade | Falha (E5) | Linha 124 propõe guardar no CRM o perfil declarado de cada inscrito, sem finalidade, aviso no formulário nem aprovação humana |
| Pessoas e dados | Nenhum dado pessoal | Atendido | Cruzamento só em números somados |
| Plataformas | Destino entrega o que o anúncio promete | Atendido | Campanhas para a página neuro-summit; "apenas teórico" obrigatório para 68634 |
| Anúncios | Demais itens | Atendido ou não se aplica | |

**RESULTADO:** Aprovado ( )  Bloqueado (X). Itens bloqueados: dados e status do curso; modalidade; desconto com validade; formulário com finalidade.

### 4.3 Problemas que bloqueiam

**E1. Seção 2.2, linhas 128 e 140 (E-W2, produto 68634); repete o C2 do dep02a.**
- Problema: o 68634 tem status "verificar (sem data no site...)" no catálogo, seção 4, com modalidade "Presencial" e 24 h. O arquivo registra só a divergência de carga horária e escreve a declaração com chamada de compra ("por R$ 450,00"). O dep02a já pediu "[CONFIRMAR status do produto 68634 antes de chamar para a compra da modalidade transmitida]". A linha do evento na seção 9 está "aberto" e cita o R$ 450,00, mas a página de compra do produto é a do 68634.
- Correção proposta: acrescentar na oferta de E-W2: "Status do produto 68634 no catálogo: verificar; modalidade cadastrada como Presencial e 24 h na loja. [CONFIRMAR NO CATÁLOGO: status, modalidade e carga horária] antes de qualquer peça com chamada para a compra da modalidade transmitida". Na declaração, manter o texto, mas com a mesma marcação.

**E2. Selos de W1 e W8 (linhas 93 e 100) e a oferta de E-W1 (linha 74); repete o C5 do dep02a.**
- Problema: W1 diz "16 h, 8 teóricas e 8 práticas" com selo "Prova no catálogo", mas o catálogo traz só "teórico e prático, 16 h"; a divisão 8 e 8, "sexta teórica e sábado prático" e "das 08h às 18h" vêm da ficha. W8 diz "vínculo comprovado na secretaria" com selo "Prova no catálogo", mas esse trecho é da ficha (o dep02a já o apontou no guia). A oferta da linha 74 mistura catálogo e ficha sem separar.
- Correção proposta: W1: "16 h, teórico e prático (catálogo). Divisão 8 h e 8 h, sexta e sábado, 08h às 18h: só na ficha [CONFIRMAR NO CATÁLOGO]". W8: "20% com SIMPNEUROMONIT para aluno e ex-aluno (catálogo). Comprovação do vínculo na secretaria: só na ficha [CONFIRMAR NO CATÁLOGO]". Separar a linha 74 do mesmo jeito.

**E3. Parágrafo de E-W1, linha 120, e EO1, linha 261 (cupom sem validade); repete o C2 do dep02a.**
- Problema: "aluno e ex-aluno Ufape com 20% pelo cupom SIMPNEUROMONIT" aparece na declaração sem validade nem regra para ex-aluno de curso livre. O W8 marca o prazo como [CONFIRMAR], mas a declaração não.
- Correção proposta: acrescentar na declaração "[CONFIRMAR validade do cupom e quem conta como ex-aluno]" e na ressalva da linha 122: "o cupom só vai para peça com validade e público elegível confirmados".

**E4. Parágrafo de E-W1, linha 120 ("a coordenação científica é a mesma da Pós em Anestesiologia Avançada da Ufape").**
- Problema: o padrão de nome da linha (contexto/pos-graduacao.md) proíbe "Pós em" em peças; a declaração é texto de referência para as mensagens. A frase também depende de autorização (já ressalvada na linha 122).
- Correção proposta: "a coordenação científica é a mesma da Pós-graduação em Anestesiologia Avançada da Ufape [CONFIRMAR autorização]".

**E5. Ponte para a Pós, linha 124 ("guardar no CRM o perfil declarado de cada inscrito").**
- Problema: coleta de dado de inscrito sem finalidade informada no formulário, sem link de política de privacidade e sem aprovação humana. O arquivo de Livres (linha 209) já exige isso para a pergunta equivalente.
- Correção proposta: "Pergunta opcional de perfil (anestesia, UTI, residente, pós-graduando) no formulário de inscrição, com finalidade informada e link para a política de privacidade, só depois de aprovação humana. Análise só em números somados."

### 4.4 Ajustes da mesma rodada

- **EA1. Declaração da linha, linhas 65 e 66 ("cada evento mostra o programa por hora").** Vale para o workshop; para 700 e 202 o arquivo só tem grade por tema e tópicos, na ficha. Trocar por "o programa antes da inscrição" ou marcar [CONFIRMAR NO CATÁLOGO] para os gravados.
- **EA2. Linha 299 (traços de voz).** Os traços "precisa, próxima, transparente" ainda não estão validados; contexto/ufape-geral.md diz "técnica, próxima, confiante". Marcar [SUPOSIÇÃO], como pedido no A1 do dep02a.
- **EA3. Frase de evento (linhas 66, 120, 140, 167, 195, 217).** Alinhar a "evento não confere diploma nem equivale a graduação ou pós-graduação".
- **EA4. E-S1, linha 175 e declaração da linha 194 ("simpósio gravado").** O catálogo traz só "Online"; "gravado" e a data da edição vêm da ficha. Marcar [CONFIRMAR NO CATÁLOGO].
- **EA5. Tabela 1.1 e tabela de alternativas de E-W1.** Repetir a ressalva de resumo de busca na legenda das tabelas.

---

## 5. Consistência entre os três arquivos e com o guia de marca

### 5.1 O posicionamento repete erros do QA do guia de marca (dep02a)?

| Erro do dep02a | Pós | Livres | Eventos |
|---|---|---|---|
| C2: cupom SIMPNEUROMONIT sem validade e 68634 em "verificar" | Não se aplica | Não se aplica | **Repete** (E1, E3) |
| C3: exemplo da prova de bolsa sem data, público e regras | **Repete** (P5, linha 270) | Não se aplica | Não se aplica |
| C4: Goiânia chamada de presencial | **Repete em parte** (P3, rótulo de A9) | Não se aplica | Não se aplica |
| C5: dado só da ficha sem [CONFIRMAR NO CATÁLOGO] | **Repete** (P4, P5) | Evitado, salvo L2 e L3 | **Repete** (E2) |
| A1: traços de voz não validados aplicados como regra | Não repete | Não repete | **Repete** (EA2) |
| A5: Ufape Clínica sem [CONFIRMAR por curso] | Evitado (A7) | Evitado (F1.1) | Evitado (linha 103) |
| A10: frase do curso livre sem "graduação" | **Repete** (PA6) | **Repete** (LA4) | **Repete** (EA3) |

### 5.2 Divergências entre os arquivos

| # | Tema | Divergência | Correção |
|---|---|---|---|
| K1 | Docentes "que atuam na rotina" | Pós: [SUPOSIÇÃO] (linha 84). Livres: afirmação na declaração de F1 (linha 134) | Livres segue a Pós (L2) |
| K2 | Selos de prova | Livres usa "Prova no catálogo" ou "Só na ficha [CONFIRMAR NO CATÁLOGO]" em todo atributo. Pós não usa. Eventos usa, com dois selos errados | Padronizar pelo modelo de Livres (P4, E2) |
| K3 | Provas 68641 e 68642 | Pós bloqueia peça até a correção dos links (P3 do cmo). Livres usa 68641 como par do grupo 68665 sem aviso | L6 |
| K4 | Coleta de dado para medir a ponte com a Pós | Livres exige finalidade e aprovação humana; Eventos não | E5 |
| K5 | Meta | Pós e Eventos citam a meta única e a métrica de apoio do cmo; Livres dá a impressão de duas metas | LA1 |
| K6 | Turma mínima | Pós afirma 20 no exemplo (linha 271) e marca 15 ou 20 nas pendências | P5 |
| K7 | Nome da Pós | Eventos usa "Pós em Anestesiologia Avançada" em declaração; Livres e Pós usam "Pós-graduação em" | E4 |
| K8 | Hospital próprio | Os três tratam como não exclusivo, citam Anclivepa e Qualittas e pedem confirmação do local por curso. Consistente | Nada |
| K9 | Certificação, MEC, "últimas vagas", promessa | Os três só usam essas expressões em listas de proibição. Consistente | Nada |
| K10 | Workshop e Pós de Neurologia | Pós (linha 231) e Eventos (linha 124) tratam a ponte como [SUPOSIÇÃO]. Consistente | Nada |
| K11 | Categoria e frase | As três categorias são de uso (quando e como se estuda), com "roteiro, horas e preço à mostra" em Livres e "programa antes da inscrição" em Eventos, ao lado de "prática presencial no cronograma e condições antes da matrícula" na Pós. Família coerente de transparência, sem conflito. A Pós usa "à vista" em sentido de "visível" e Livres usa "à vista" como forma de pagamento (PA3) | PA3 |

### 5.3 Conferências pedidas no briefing

| Conferência | Pós | Livres | Eventos |
|---|---|---|---|
| Frase de certificação ou nota do MEC fora de proibição | Nenhuma | Nenhuma | Nenhuma |
| "Últimas vagas", "vagas limitadas" fora de proibição | Nenhuma ("reta final" em PA4) | Nenhuma | Nenhuma ("30 vagas" como capacidade do catálogo) |
| Promessa de emprego, renda ou aprovação | Nenhuma | Nenhuma | Nenhuma |
| "Hospital próprio" como exclusivo | Nunca | Nunca | Nunca (evento é na Unidade 2) |
| Curso livre ou evento sem diploma | Não se aplica | Dito em toda declaração (ajuste LA4) | Dito em toda declaração (ajuste EA3) |
| Concorrente com fonte da inteligência de concorrência | Sim, por linha | Sim, por linha | Sim, por linha |
| Ressalva de resumo de busca | Só no cabeçalho e nas fontes (PA1) | Só no cabeçalho e nas fontes (LA5) | Cabeçalho, linha 57 e fontes (EA5) |
| Dado pessoal | Nenhum | Nenhum | Nenhum |
| Travessão ou meia-risca | Nenhum encontrado | Nenhum encontrado | Nenhum encontrado |

A conferência de travessão e meia-risca foi feita por leitura integral, sem busca automática por caractere [SUPOSIÇÃO: leitura visual].

---

## 6. Encaminhamento

- Os três arquivos **voltam para o agente posicionamento** com os bloqueantes P1 a P6, L1 a L6 e E1 a E5 e os ajustes PA1 a PA7, LA1 a LA6 e EA1 a EA5. Depois, nova rodada do qa-de-marketing.
- Não seguem para a aprovação humana nesta rodada.
- Prioridade: Eventos primeiro (o workshop é em 20/11/2026 e está na onda 1). As correções E1 a E5 são curtas e não dependem da Ufape, salvo as confirmações que ficam marcadas.
- O agente mensagens (etapa 2.2) não deve partir destes arquivos antes da nova rodada; se a pessoa do marketing decidir adiantar o workshop, que use o arquivo de Eventos com E1 a E5 aplicados.
- Quando seguirem para aprovação humana, peças com comparação com concorrente precisam do aprovador definido em contexto/ufape-geral.md (tabela vazia) [CONFIRMAR].
- Nada foi publicado, enviado ou pago. Os arquivos revisados não foram editados.

---

## Lista 1. Fatos (com fonte)

- 30 turmas de Pós abertas, uma delas (719) de Inteligência Artificial na Saúde; 68632 é presencial; 289, 68609 e 68623 são semipresenciais (catálogo, seção 2).
- Matrícula de R$ 250,00 em todas as Pós abertas citadas, salvo 68629 (R$ 350,00) (catálogo, seção 2).
- 22 provas de bolsa abertas em 27/11/2026, R$ 100,00; o catálogo não traz as regras das bolsas (catálogo, seção 3). Regras e divergência de turma mínima (15 ou 20) em contexto/pos-graduacao.md.
- 616: modalidade "On-line", local "Presencial e Online", 05/12/2026, 12 h, R$ 990,00 ou 5x de R$ 240,00 (catálogo, seção 5); contada como "online com data" no plano do cmo, seção 2.2.
- 669: 6 h, R$ 300,00; 482: 8 h, R$ 289,00; 461: 8 h, R$ 185,00 (catálogo, seção 5).
- Grupos de R$ 734,00: 644, 643, 713, 642, 712 (com "Anual" no nome), 721 e 720 (sem "Anual") (catálogo, seção 7).
- 68634: status "verificar", modalidade "Presencial", local "Saiba Mais", 24 h (catálogo, seção 4). Workshop: aberto, 16 h, 30 vagas, R$ 1.250,00 e R$ 450,00, cupom de 20% (catálogo, seção 9).
- Meta única do plano: turmas de Pós confirmadas; vendas de livres e inscrições do evento são métricas de apoio (cmo-geral, seção 1).
- Áreas "quase sozinhas" da inteligencia-concorrencia-pos (resumo, item 3): 699, 352, 359, 657, 677, 698, 333, 68606, 341. Sem a 679.
- Dados de concorrentes da Pós vêm de resumo de busca de 26/10/2026, com confiança A, M ou B; parte do calendário da Anclivepa vem de cópia não oficial do edital (inteligencia-concorrencia-pos, cabeçalho e seção 0).
- Padrão de nome: "Pós-graduação em", nunca "Pós em" (contexto/pos-graduacao.md).
- Erros C2 a C5, A1, A5 e A10 do guia de marca (qa-de-marketing-geral-2026-10-26-dep02a.md).

## Lista 2. Suposições

- [SUPOSIÇÃO] As citações das fichas e dos arquivos de persona, pesquisa de mercado e concorrência de Livres foram transcritas com fidelidade pelo agente posicionamento (não conferidas nesta revisão).
- [SUPOSIÇÃO] Ausência de travessão e meia-risca conferida por leitura visual.
- [SUPOSIÇÃO] As correções propostas respeitam o catálogo e os contextos; a redação final é do agente posicionamento.
- [SUPOSIÇÃO] "À vista" na frase da Pós pode ser lido como forma de pagamento (risco de redação, não erro de dado).

## Lista 3. Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Regras das provas de bolsa, público elegível, turma de destino e turma mínima (15 ou 20).
- [CONFIRMAR NO CATÁLOGO] Condições de turma das Pós (reembolso, passagem, 1ª mensalidade), módulos de 3 dias e contagem de docentes, hoje só nas fichas.
- [CONFIRMAR NO CATÁLOGO] Modalidade da 616; modalidade, status e carga horária do 68634; "gravado" para os online que não dizem gravação e para o 202.
- [CONFIRMAR NO CATÁLOGO] Frequência e período coberto de cada grupo de estudos.
- [CONFIRMAR NO CATÁLOGO] Divisão 8 h e 8 h e horários do workshop; comprovação de vínculo do cupom.
- [CONFIRMAR] Validade do cupom SIMPNEUROMONIT e se vale para ex-aluno de curso livre.
- [CONFIRMAR] Local da prática das Pós em Goiânia.
- [CONFIRMAR] Docente e origem do conteúdo dos cursos em espanhol.
- [CONFIRMAR] Fonte para incluir a 679 entre as áreas sem concorrente nomeado.
- [CONFIRMAR] Correção dos links de 68641 e 68642 (P3 do cmo).
- [CONFIRMAR] Aprovador de peças com comparação com concorrente (tabela vazia em contexto/ufape-geral.md).
- [CONFIRMAR] Validação dos traços de voz e nova rodada do guia de marca.

## Fontes

docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/eventos.md; contexto/catalogo-de-cursos.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/conformidade-educacional.md; saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02a.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 e 2); saidas/01-inteligencia-de-mercado/inteligencia-concorrencia-pos-2026-10-26.md (cabeçalho e seções 0 a 3); saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/posicionamento-livres-2026-10-26.md; saidas/02-estrategia-e-posicionamento/posicionamento-eventos-2026-10-26.md.
