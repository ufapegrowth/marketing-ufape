# QA de marketing: departamento 01, lote b (personas de Pós, Livres e Eventos, e análise de tendências)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (o lote cobre pos, livres, eventos e geral)
- Data: 26/10/2026
- Status: rascunho de QA. Nada é publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md
  - contexto/eventos.md
  - contexto/graduacao.md (para conferir o bloco E da análise de tendências)
  - contexto/catalogo-de-cursos.md (inteiro, seções 1 a 9)
  - templates/persona.md
  - auditorias/01-qualidade-de-pesquisa.md
  - auditorias/conformidade-educacional.md
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-livres-2026-10-26.md
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-eventos-2026-10-26.md
  - saidas/01-inteligencia-de-mercado/analise-de-tendencias-geral-2026-10-26.md
  - saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-26.md (linhas 1 a 140, para conferir contradições)
  - saidas/01-inteligencia-de-mercado/inteligencia-concorrencia-pos-2026-10-26.md (linhas 1 a 120, para conferir contradições)
- Método: leitura integral dos quatro arquivos e conferência de cada código, nome, preço, parcela, total, matrícula, data, carga horária, turma e status contra o catálogo. Contas refeitas à mão (totais no cartão, descontos, dias até a data, contagens de turmas e provas, datas de calendário). A busca de travessão e meia-risca foi feita por leitura, sem ferramenta automática de busca nesta sessão [SUPOSIÇÃO: risco residual de caractere invisível; vale rodar a checagem automática antes da aprovação humana].

## Resumo dos vereditos

| Arquivo | Auditoria 01 | Conformidade educacional | Veredito |
|---|---|---|---|
| pesquisa-de-persona-pos-2026-10-26.md | 5 itens atendidos, 2 parciais, 1 não atendido (persona sem base real, pendência da Ufape) | 4 itens falham (dados do curso, superlativo, comparação com concorrente, preço sem matrícula) e 1 parcial (bolsa) | corrigir |
| pesquisa-de-persona-livres-2026-10-26.md | 6 atendidos, 1 parcial, 1 não atendido (persona sem base real) | 1 item parcial (dados do curso: contagens) | corrigir |
| pesquisa-de-persona-eventos-2026-10-26.md | 6 atendidos, 1 parcial, 1 não atendido (persona sem base real) | 2 itens falham (curso livre ou evento sem diploma; consentimento de WhatsApp) e 3 parciais | corrigir |
| analise-de-tendencias-geral-2026-10-26.md | 4 atendidos, 2 parciais, 2 não se aplicam | 1 item falha (dados do curso) e 2 parciais (bolsa; consentimento de WhatsApp) | corrigir |

Os quatro voltam para o agente que os produziu (pesquisa-de-persona e analise-de-tendencias). Nenhum segue agora para a aprovação humana.

Sobre o item "A persona é baseada em alunos e candidatos reais": nos três arquivos de persona ele está honestamente declarado como não atendido. O agente não consegue resolver isso sozinho, porque depende de a Ufape enviar conversas e dados agregados. Este item não entra na lista de correções do agente, mas impede que qualquer das três personas seja tratada como validada. Até lá, elas valem só como rascunho de hipóteses.

Verificações transversais (os quatro arquivos):
- Travessão ou meia-risca: nenhum encontrado na leitura.
- "Últimas vagas", "vagas limitadas": aparecem só em regra proibitiva. Ressalva em Eventos (ver E-R1).
- "Certificado pelo MEC", "reconhecida pelo MEC" ou nota MEC: nenhuma ocorrência fora de regra proibitiva. O ato da Graduação citado na análise de tendências (Portaria SERES/MEC nº 162, de 13/03/2025) bate com o catálogo.
- Dado pessoal de aluno, candidato ou lead: nenhum. Nenhum docente é nomeado.
- Citação de candidato apresentada como real: nenhuma. Toda fala em primeira pessoa está marcada [SUPOSIÇÃO] e rotulada "não é citação". Trechos de página estão rotulados como voz da página.
- Número de meta, verba, vagas restantes, leads ou matrículas inventado: nenhum.

---

## 1. pesquisa-de-persona-pos-2026-10-26.md

### 1.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação do QA |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | Parcial | S-P1 e S-P3 sem data própria (linhas 300 e 302) e tudo de resumo de busca. Aceitável em rascunho, desde que S-P1 a S-P5 não entrem em peça sem conferência na fonte primária (o próprio arquivo diz isso na linha 23) |
| As suposições estão marcadas com [SUPOSIÇÃO] | Atendido | Perfil, gatilhos, dores, resultados, canais e decisor estão marcados. Dois pontos são erro de fato, não suposição (ver P1 e P2) |
| As citações de candidatos e alunos são literais e anonimizadas | Atendido por ausência | 0 citações reais. Hipóteses de fala marcadas (linhas 61 a 70, 123 a 130, 175 a 182, 224 a 231) |
| Os dados de instituições concorrentes são públicos e datados | Atendido, com ressalva | Fonte: inteligencia-concorrencia-pos de 26/10/2026, por resumo de busca. A comparação de taxa com a Anclivepa vira resposta de peça sem conferência na fonte primária (ver P4) |
| Os números de mercado mostram faixa mínima e máxima | Parcial | A faixa de 154,9 mil a 188 mil mistura critérios e contradiz os outros arquivos (ver P5) |
| A persona é baseada em alunos e candidatos reais | Não atendido | Pendência da Ufape (ver nota no resumo). Declarado na linha 324 |
| As conclusões terminam em ações | Atendido | Seção 8 |
| A pesquisa cobre uma única linha de negócio | Atendido | Só pos. 719 tratado como exceção; cursos livres aparecem só como alternativa |

### 1.2 Auditoria conformidade-educacional

| Item | Resultado | Observação do QA |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Não atendido | P1 e P2 |
| Status "aberto" (ou não chama para inscrição) | Atendido | Turmas em "verificar" marcadas como fora da divulgação (68607 na linha 245; 677 e 701 na linha 289) |
| Modalidade clara e correta | Atendido | 586 EAD, 68632 presencial, demais semipresencial, como no catálogo |
| Graduação: ato do catálogo | Não se aplica | - |
| Pós lato sensu: sem "reconhecida pelo MEC" | Atendido | Linha 87: texto oficial [PREENCHER COM A REGULAÇÃO] |
| Curso livre: não confere diploma | Não se aplica | Livres só como alternativa |
| Nota MEC só com fonte oficial | Atendido | Nenhuma nota |
| Sem promessa de emprego, salário ou aprovação | Atendido | Linhas 71 e 232 |
| Dados de empregabilidade com fonte, período e amostra | Atendido | Dados públicos da categoria, com amostra (S-P2, 360 clínicos de MG) e aviso de que não são do aluno da Ufape |
| Superlativos só com fonte | Não atendido | P2 |
| Comparação com concorrente objetiva e verificável | Não atendido | P4 |
| Preço com parcelas, total e matrícula | Não atendido | P3 |
| Bolsa e desconto com regra, público e prazo | Parcial | Regras citadas de contexto/pos-graduacao.md e contradições marcadas, mas o número de provas sem turma de destino está subestimado (P6) |
| Urgência real | Atendido | "Reta final" (linha 284) tem data real do catálogo (68606, 07/11/2026). Não usar como frase de peça sem a data |
| Prouni, Fies ou financiamento | Não se aplica | - |
| Autorização de depoimento e imagem | Atendido | Linha 391 |
| Menores de idade | Não se aplica | - |
| Formulários com finalidade e política | Não se aplica | - |
| WhatsApp e e-mail com consentimento | Não se aplica | Nenhum envio proposto |
| Nenhum dado pessoal | Atendido | - |
| Políticas de Meta e Google para educação | Não se aplica | Segmentação por origem (linha 197) é geográfica e depende de dado inexistente; não é discriminatória |
| Página de destino entrega o prometido | Não se aplica | - |
| Itens de ANÚNCIOS (6) | Não se aplica | Arquivo de pesquisa, sem anúncio |

### 1.3 Problemas e correções

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| P1 | Linha 84 (objeção 1 de P1) e linha 193 (objeção 1 de P2) | "Total de R$ 28.050,00 a R$ 48.400,00 nas turmas abertas de 500 h ou mais". O teto está errado: R$ 48.400,00 é a 657, que tem 360 h. Entre as abertas com 500 h ou mais, o maior total é o da 707 (600 h, R$ 47.700,00) | Escrever "R$ 28.050,00 (333) a R$ 47.700,00 (707) nas turmas abertas de 500 h ou mais" ou, se a ideia é cobrir todas as abertas, "R$ 12.000,00 (719) a R$ 48.400,00 (657)", sempre com o código |
| P2 | Linha 276 (5.1, A5) | "Menor ticket de pós da Ufape" para a 68629 (R$ 16.456,00). É falso: a 719 está aberta com total de R$ 12.000,00 (e a 586, em "verificar", tem R$ 14.130,00) | Trocar por "menor ticket entre as pós veterinárias abertas (a 719, de R$ 12.000,00, é de outro público)" |
| P3 | Linha 84 (333) e linha 244 (333 e 60) | Preço sem a matrícula de R$ 250,00, que o catálogo traz para as duas turmas. A regra da linha pede parcela, número de parcelas, total e matrícula; a resposta à objeção vai virar texto de mensagem | Acrescentar "matrícula de R$ 250,00" na 333 e na 60, como já está feito na 68604 e na 68629. Recomendado também na tabela 5.1 (341, 359, 657, 707, 289, 68632, 68609, 68623, 60, 352) |
| P4 | Linha 145 (objeção 1 de P4) | A resposta propõe peça com "R$ 100,00 contra R$ 350,00 da Anclivepa". A taxa do concorrente vem de resumo de busca, não do edital aberto, e comparação com concorrente exige o responsável indicado em contexto/ufape-geral.md (regra de aprovação ainda sem nome) | Marcar a taxa da Anclivepa como [CONFIRMAR no edital oficial] e acrescentar: "comparação só em peça aprovada pelo responsável de regulação, depois da conferência na fonte primária". Manter a ressalva já escrita de que a Anclivepa dá 50% e a Ufape só 2 bolsas de 50% por prova |
| P5 | Linhas 51, 300, 323 e 361 | Universo de veterinários "154,9 mil a 188 mil" registrados. Contradiz a pesquisa de mercado da Pós (154,9 mil a "180 mil ou mais"), a persona de Livres (154,9 mil a 182,3 mil "em atividade") e o número da pesquisa de mercado dos Livres ("quase 240 mil registrados", AviNews, 09/09/2025, citado na linha 54 da pesquisa de mercado da Pós) | Separar por critério e por data: registrados (154,9 mil em 2021, Forbes; "mais de 180 mil", blog de 2026; 188 mil, reportagem sem data; quase 240 mil, AviNews de 09/09/2025) e em atividade (182,3 mil, AviNews). Dizer que as fontes divergem e não usar nenhum desses números em peça |
| P6 | Linhas 147, 152, 340 e 385 | "Quatro provas sem turma futura aberta" (68652, 68649, 68653, 68655). Pelo catálogo, outras provas também não têm turma aberta do mesmo curso, na mesma cidade, que comece depois de 27/11/2026 (ver tabela 6.1 deste QA) | Trocar "quatro provas" por "pelo menos quatro provas sem turma aberta; outras oito com destino incerto pela data ou pela cidade", citar a tabela 6.1 e manter "destino de cada prova: [CONFIRMAR]". A objeção 3 de P4 não pode indicar turma de destino enquanto a Ufape não confirmar |

Observações sem bloqueio:
- Linha 86: "turma mínima de 20" das fichas está marcada [CONFIRMAR NO CATÁLOGO]; correto.
- As regras da bolsa (11 bolsas, 2 de 50%, 4 de 25%, 5 de 10%, nota 7,0, 2 dias úteis de recurso, 10 dias úteis de matrícula) batem com contexto/pos-graduacao.md. O preço de R$ 100,00 bate com a seção 3 do catálogo.
- Conferidos sem divergência: 30 turmas abertas, 22 provas abertas, 68656 fora do ar, 4 turmas e 3 provas em Goiânia, 0 EAD aberta; preços e parcelas de 68604, 333, 68629, 60, 341, 719, 359, 657, 707, 352, 586, 289, 68632, 68609, 68623; datas e cargas citadas na seção 5.

### 1.4 Veredito: corrigir

Volta para o agente pesquisa-de-persona com P1 a P6.

---

## 2. pesquisa-de-persona-livres-2026-10-26.md

### 2.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação do QA |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | Atendido, com ressalva | Catálogo e fichas de 26/10/2026; externos via 1.1 e 1.2, de resumo de busca |
| As suposições estão marcadas com [SUPOSIÇÃO] | Atendido | - |
| As citações de candidatos e alunos são literais e anonimizadas | Atendido por ausência | 0 citações (seção 5.1). Itálicos rotulados como formulação provável. Voz da página separada (5.2) |
| Os dados de concorrentes são públicos e datados | Atendido, com ressalva | Tabela da seção 4 com data |
| Os números de mercado mostram faixa mínima e máxima | Parcial | L5 |
| A persona é baseada em alunos e candidatos reais | Não atendido | Pendência da Ufape. Declarado na linha 306 |
| As conclusões terminam em ações | Atendido | Seção 6 |
| A pesquisa cobre uma única linha | Atendido, com ressalva | Ponte para a Pós só como hipótese |

### 2.2 Auditoria conformidade-educacional

| Item | Resultado | Observação do QA |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Parcial | L1 e L2 (contagens). Preços, parcelas, totais calculados, datas e cargas conferidos e corretos |
| Status "aberto" | Atendido | Itens "verificar" e "sem venda" ficam fora (A4, Lima, aprimoramentos) |
| Modalidade clara e correta | Atendido | Contradição da 616 marcada [CONFIRMAR NO CATÁLOGO]; 560 semipresencial |
| Graduação: ato do catálogo | Não se aplica | - |
| Pós lato sensu | Não se aplica | - |
| Curso livre: não confere diploma | Atendido | Linhas 21, 81, 84 |
| Nota MEC | Atendido | Linha 280: a frase da ficha de 68614 não é repetida |
| Sem promessa de emprego, salário ou aprovação | Atendido | Linhas 21 e 84. "Cobrar por isso" (linha 65) está marcado como inferência; não usar como promessa de renda em peça |
| Dados de empregabilidade | Não se aplica | - |
| Superlativos | Atendido | - |
| Comparação com concorrente | Atendido | Quadam e Langford só como referência, sem ataque |
| Preço completo | Atendido | À vista e total no cartão em todos os itens |
| Bolsa e desconto | Atendido, com ressalva | Condição de 720 com regra [CONFIRMAR NO CATÁLOGO] |
| Urgência real | Atendido | "Turma reduzida" vetada como escassez (linha 263); prazo de 29/10 da 68614 é conta correta (28/11 menos 30 dias) |
| Prouni, Fies | Não se aplica | - |
| Autorização de imagem e voz | Atendido | Docentes não nomeados |
| Menores | Não se aplica | - |
| Formulários | Não se aplica | Linha 152 propõe pergunta na prova de bolsa, já condicionada à aprovação humana |
| WhatsApp e e-mail com consentimento | Não se aplica | Nenhum envio proposto |
| Nenhum dado pessoal | Atendido | - |
| Políticas de plataforma e itens de ANÚNCIOS | Não se aplica | - |

### 2.3 Problemas e correções

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| L1 | Linha 31 (tabela da seção 1) e linha 37 | "Tem 3 datas dentro da onda 1". São 2 datas (14/11 e 28/11) para 3 cursos e 4 códigos (573; 68614; 623 e 68637) | Escrever "3 cursos (4 códigos) com data em 14/11 e 28/11/2026" |
| L2 | Linha 32 e linha 105 | "22 contínuos" no formato gravado, mas a lista dos três degraus tem 21 itens; o 22º é o 95 (Auxiliar Veterinário), que a própria persona tira do recorte (linha 226) | Escrever "21 itens (o 95, de auxiliar, fica fora desta persona)" ou incluir o 95 na lista |
| L5 | Linha 305 (auditoria, item de faixa) | "154,9 mil a 182,3 mil em atividade" junta registrados de 2021 (154,9 mil) com em atividade de 2025 (182,3 mil) numa faixa só, e diverge da persona da Pós (154,9 mil a 188 mil) | Separar por critério e data, como em P5, e alinhar o texto com a persona da Pós |

Observações sem bloqueio (ajustar se der):
- Linha 90: o par 68614 e 623 (28/11/2026) com as pós 68604 (31/10/2026) e 68606 (07/11/2026) aponta para turmas que já terão começado na data do curso livre. Como ponte, vale a próxima turma, que não existe no catálogo [CONFIRMAR].
- Linha 93: 68638 (POCUS, São Paulo) foi ligado a 68623 (Goiânia). Em São Paulo, a pós aberta mais próxima do tema é 68635 (Clínica Médica e Emergência, 10/04/2027).
- Linha 179: a prova 68641 (Cardiologia, SP) não tem turma de Cardiologia aberta em São Paulo (ver 6.1).
- Linha 162: o início de 644 em março de 2026 vem da ficha; o catálogo não traz data para 644.

### 2.4 Veredito: corrigir

Volta para o agente pesquisa-de-persona com L1, L2 e L5 (correções pequenas).

---

## 3. pesquisa-de-persona-eventos-2026-10-26.md

### 3.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação do QA |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | Atendido, com ressalva | Ficha e catálogo de 26/10/2026; externos via 1.2 |
| As suposições estão marcadas com [SUPOSIÇÃO] | Atendido | - |
| As citações de candidatos e alunos são literais e anonimizadas | Atendido por ausência | 0 citações; itálicos rotulados; voz da página separada |
| Os dados de concorrentes são públicos e datados | Atendido, com ressalva | Datas de congressos de 2026 sem fonte, declarado |
| Os números de mercado mostram faixa mínima e máxima | Parcial | Declarado pelo agente: tamanho de público sem fonte. Aceitável |
| A persona é baseada em alunos e candidatos reais | Não atendido | Pendência da Ufape. Declarado na linha 271 |
| As conclusões terminam em ações | Atendido | Seção 6 |
| A pesquisa cobre uma única linha | Atendido, com ressalva | 700 e 202 seguem o plano do cmo; está declarado |

### 3.2 Auditoria conformidade-educacional

| Item | Resultado | Observação do QA |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Parcial | E3 e E4 |
| Status "aberto" | Parcial | E5 |
| Modalidade clara e correta | Atendido, com ressalva | Presencial e transmitido bem separados (2.6). No catálogo, a linha da 68634 diz modalidade "Presencial" para o produto transmitido: incluir no pedido à Ufape |
| Graduação: ato | Não se aplica | - |
| Pós lato sensu | Não se aplica | - |
| Curso livre (e evento): não confere diploma | Não atendido | E1 |
| Nota MEC | Atendido | "Certificado UFAPE conforme presença" é texto da página e não cita o MEC |
| Sem promessa | Atendido | Linha 83 (sem eficácia clínica), linha 99 (sem paciente vivo), linha 200 (sem caminho para a pós) |
| Dados de empregabilidade | Não se aplica | - |
| Superlativos | Atendido | Linha 58: ausência de concorrente não vira ineditismo |
| Comparação com concorrente | Atendido | Sem comparação de preço |
| Preço completo | Atendido, com ressalva | Parcelamento do presencial [CONFIRMAR NO CATÁLOGO]; valores com cupom marcados como cálculo e suposição. Contas conferidas: R$ 1.000,00 e R$ 360,00; 700 em 10x de R$ 98,00 = R$ 980,00; 202 em 6x de R$ 78,00 = R$ 468,00 |
| Bolsa e desconto com regra, público e prazo | Parcial | E6 |
| Urgência real | Atendido, com ressalva | E-R1 |
| Prouni, Fies | Não se aplica | - |
| Autorização de imagem e voz | Atendido | Docentes não nomeados; [CONFIRMAR autorização] |
| Menores | Não se aplica | - |
| Formulários com finalidade e política de privacidade | Parcial | E7 |
| WhatsApp e e-mail só com consentimento | Não atendido | E2 |
| Nenhum dado pessoal | Atendido | - |
| Políticas de plataforma e itens de ANÚNCIOS | Não se aplica | - |

### 3.3 Problemas e correções

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| E1 | Linha 70 (outras dúvidas: certificado) e seção 0 | O arquivo orienta a resposta sobre certificado, mas não diz que o workshop e os gravados 700 e 202 não conferem diploma nem equivalem a pós. O catálogo lista esses produtos com os Livres, e o item de conformidade pede isso | Acrescentar na seção 0 e na linha 70: "o workshop e os gravados não conferem diploma nem equivalem a pós-graduação; certificado de participação conforme a página, texto oficial [PREENCHER COM A REGULAÇÃO]" |
| E2 | Linha 81 (E1a, onde está) e Lista B, item 8 | Propõe usar o WhatsApp do grupo pago 644 como canal de divulgação, "dependendo de a Ufape autorizar". A autorização que vale é o consentimento de cada pessoa para receber marketing, não a da Ufape | Reescrever: "mensagem de divulgação só para quem deu opt-in de marketing, com saída fácil; o grupo de estudo do 644 não é canal de venda". O mesmo vale para a base de participantes de 2025 do 700 (Lista B, item 8) e para a base de alunos e ex-alunos (linha 60) |
| E3 | Linhas 175, 185 e Lista A, item 5 | 202 com "8 h" e "turma III": o catálogo não traz carga horária nem turma para o 202 (seção 9). A própria regra do arquivo (linha 19) pede [CONFIRMAR NO CATÁLOGO] para dado só da ficha, como foi feito com a carga do 700 | Marcar "8 h e turma III (ficha) [CONFIRMAR NO CATÁLOGO]" |
| E4 | Linha 120 (E1c) | "30x de R$ 1.000,00 a R$ 1.600,00 ou mais". No catálogo, as pós abertas em 30x vão de R$ 935,00 (333) a R$ 1.613,33 (657) | Escrever "30x de R$ 935,00 a R$ 1.613,33, mais matrícula, nas pós abertas em 30 parcelas" |
| E5 | Linhas 17, 66 e 133 a 138 | O produto 68634 (transmitido e gravado, R$ 450,00) está com status "verificar" no catálogo (sem data no site, carga de 24 h). O arquivo aponta a divergência de carga, mas não o status | Acrescentar "68634 em 'verificar' no catálogo: peça de compra do transmitido só depois de a Ufape corrigir data e carga na loja [CONFIRMAR NO CATÁLOGO]" |
| E6 | Linhas 17, 66 e 128 | Cupom SIMPNEUROMONIT: regra (20%) e público (aluno e ex-aluno) estão escritos; falta o prazo de validade | Acrescentar "validade do cupom: [CONFIRMAR]" na Lista C, item 4 |
| E7 | Linhas 38 e 254 | Propõe coletar o perfil profissional no formulário de inscrição. Formulário precisa informar a finalidade e ter link para a política de privacidade | Acrescentar essa condição nas duas ações |

Observação sem bloqueio:
- E-R1, linhas 50 e 238: "vaga limitada (30)" no gatilho e "Somente 30 vagas, por ordem de inscrição" no banco de linguagem. O número 30 é real no catálogo, mas a frase empurra para escassez. Sugestão: "30 vagas no total (catálogo); vagas restantes [CONFIRMAR]", sem "somente".
- Conferidos sem divergência: 20 e 21/11/2026, 16 h, 30 vagas, Av. Tiradentes, 960, R$ 1.250,00 e R$ 450,00, cupom SIMPNEUROMONIT de 20% (catálogo, seção 9, e decisão 6 do briefing); faltam 25 dias; 5 turmas de anestesiologia abertas ou iniciadas (586, 68607, 657, 68609, 359); dados de 657, 359, 68609, 68607, 68623, 352, 68635, 68616, 68608, 68615 e das provas; prova seis dias depois do sábado prático.

### 3.4 Veredito: corrigir

Volta para o agente pesquisa-de-persona com E1 a E7.

---

## 4. analise-de-tendencias-geral-2026-10-26.md

### 4.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação do QA |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | Atendido, com ressalva | F1, F2 e F7 sem data própria; tudo de resumo de busca, declarado na linha 18 |
| As suposições estão marcadas com [SUPOSIÇÃO] | Parcial | Duas afirmações escritas como fato estão erradas (T1 e T2) |
| As citações de candidatos e alunos são literais e anonimizadas | Não se aplica | Nenhuma citação |
| Os dados de concorrentes são públicos e datados | Atendido, com ressalva | Anclivepa via pesquisa da Pós; uso condicionado a dado conferido (linha 269) |
| Os números de mercado mostram faixa mínima e máxima | Parcial | T5 e T6 |
| A persona é baseada em alunos e candidatos reais | Não se aplica | Não é persona |
| As conclusões terminam em ações | Atendido | Seções 8 e 9 |
| A pesquisa cobre uma única linha | Não se aplica (arquivo geral) | Cada tendência indica a linha, e a Graduação está separada no bloco E. Sem mistura de público |

### 4.2 Auditoria conformidade-educacional

| Item | Resultado | Observação do QA |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Não atendido | T1, T4 e T7. As datas por código foram tiradas do plano do cmo (linha 19); o QA conferiu todas no catálogo e elas batem |
| Status "aberto" | Atendido | 554, 699, 586 e 719 com status e ressalvas corretos |
| Modalidade | Atendido | Graduação presencial; Pós semipresencial; 586 EAD em "verificar" |
| Graduação: ato do catálogo | Atendido | Linha 259, Portaria SERES/MEC nº 162, de 13/03/2025, igual ao catálogo. Ver T3 sobre o decreto |
| Pós lato sensu | Atendido | Linha 27 |
| Curso livre: não confere diploma | Não se aplica | Ideias de pauta, sem resposta sobre certificado. A estrategia-de-conteudo deve incluir a frase nas peças de Livres |
| Nota MEC | Atendido | Nenhuma |
| Sem promessa | Atendido | Linhas 26, 95 e 168 |
| Dados de empregabilidade | Atendido | Vagas de plantão não viram promessa (linha 95) |
| Superlativos | Atendido | - |
| Comparação com concorrente | Atendido | Linha 269 condiciona a dado conferido |
| Preço completo | Atendido | Só faixas do catálogo (minicursos, grupos) |
| Bolsa e desconto | Parcial | T4 |
| Urgência real | Atendido | Linhas 272 e 285 sem "últimas vagas" |
| Prouni, Fies | Não se aplica | Não citados |
| Autorização de imagem e voz | Atendido | Linhas 89, 161, 193 e 200 |
| Menores | Atendido | Linhas 200, 253 e 326 |
| Formulários | Atendido, com ressalva | Linha 174: incluir finalidade e link da política de privacidade na pergunta de origem |
| WhatsApp e e-mail com consentimento | Parcial | T8 |
| Nenhum dado pessoal | Atendido | F5 traz no endereço o nome da autora de um TCC público. Não é aluno nem candidato; sugestão de citar pelo título, como fez a inteligencia-concorrencia com currículos |
| Políticas de plataforma e itens de ANÚNCIOS | Não se aplica | - |

### 4.3 Problemas e correções

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| T1 | Linha 53 (A.1) | "É a única área do recorte com prova de bolsa aberta (68652) e nenhuma turma de Pós aberta". Falso: Endoscopia (68649), Nefrologia (68653) e Odontologia (68655) também, como o próprio arquivo diz nas linhas 305 e 394, e outras provas têm destino incerto (tabela 6.1) | Trocar por "uma das áreas com prova de bolsa aberta e sem turma de Pós aberta (com 68649, 68653 e 68655)" |
| T2 | Linha 96 (A.4) | "O Workshop de Neuromonitorização é de anestesia e neurologia (A12), não de UTI." Contradiz a página do evento ("tanto no centro cirúrgico quanto na UTI", dois blocos de UTI na grade) e a persona de Eventos (E1b, intensivista) | Escrever "o workshop é de anestesia e neurologia, com dois blocos de UTI e sedação sob bloqueio neuromuscular (persona E1b)" |
| T3 | Linha 116 (B.1) contra linha 258 (E.2) | B.1 diz que o Decreto 12.456/2025 não inclui Medicina Veterinária entre as presenciais obrigatórias e que só o PL 2.559/25 propõe isso. E.2 resume os dois como "presencial obrigatório para Medicina Veterinária" | Corrigir E.2: "o decreto não lista Medicina Veterinária; o PL 2.559/25, ainda projeto, propõe graduação só presencial". Não comentar lei em peça (já dito na linha 259) |
| T4 | Linha 166 (C.2) | "Prova de bolsa de R$ 100,00 (regras no catálogo)". O catálogo traz só o preço (seção 3); as regras estão em contexto/pos-graduacao.md | Trocar por "preço no catálogo, seção 3; regras em contexto/pos-graduacao.md, a lançar no catálogo [CONFIRMAR NO CATÁLOGO]" |
| T5 | Linha 165 (C.2) e F11 | Média de R$ 4.607,16 (39 h). A pesquisa de mercado da Pós e a persona da Pós trazem R$ 4.670,73 para as mesmas 39 h (S12) | Conferir na fonte qual é o valor certo, ou registrar as duas fontes como divergentes. Continua proibido usar em peça |
| T6 | Linhas 46, 47 e F2 (A.1) | Gatos "30,8 e 33,3 milhões". A pesquisa de mercado da Pós registra "entre 30 e 33,6 milhões" (S9) | Registrar a faixa das três fontes (30 a 33,6 milhões) e dizer que divergem |
| T7 | Linha 251 (E.1) | "Matrícula 2 dias depois do resultado". O contexto da Graduação (editais 2027/1) diz "a partir de 2 dias depois do resultado" | Escrever "matrícula a partir de 2 dias depois do resultado" |
| T8 | Linha 57 (A.1, ideias) | "E-mail e WhatsApp para a base de felinos dos Livres" sem condicionar ao opt-in. A regra aparece só em D.4 (linha 212) | Acrescentar "só para quem deu opt-in de marketing, com saída fácil" |
| T9 | Linha 15 e Lista C, item 17 | O arquivo leu a pesquisa de mercado da Pós só até a linha 431 de 531 e deixou a conferência de contradição em aberto | Ler as linhas 432 a 531 e registrar o resultado antes de marcar como pronto |

Observações sem bloqueio:
- Linhas 45 e 150: "5 origens independentes" (A.1) conta a própria pesquisa da squad como origem, e "4 origens independentes" (C.1) lista 5 itens. Ajustar a contagem para manter a régua de sinal forte coerente.
- C.1 (linha 151) cita 87,78% e 74,17% do estudo da Revista CFMV; a persona da Pós cita 68,33% de insatisfação do mesmo estudo. Não é contradição (são indicadores diferentes), mas vale dizer isso nos dois arquivos.
- Contas conferidas e corretas: Black Friday em 27/11/2026; 20/11/2026 é sexta e 21/11 sábado; Carnaval em 09/02/2027, Sexta-feira Santa em 26/03 e Páscoa em 28/03/2027; último sábado de abril de 2027 em 24/04; janela de 11 a 25/02/2027; 24 das 30 turmas entre 13/03 e 28/05/2027; 9 turmas em abril; 10 turmas em maio; 7 presenciais abertos nos Livres; 13 minicursos de R$ 185,00 a R$ 300,00.

### 4.4 Veredito: corrigir

Volta para o agente analise-de-tendencias com T1 a T9.

---

## 5. Contradições entre os arquivos e com as pesquisas de mercado e a concorrência

| # | Tema | Onde diverge | Encaminhamento |
|---|---|---|---|
| X1 | Universo de médicos veterinários | Persona Pós: 154,9 mil a 188 mil registrados. Persona Livres: 154,9 mil a 182,3 mil em atividade. Pesquisa de mercado da Pós: 154,9 mil a "180 mil ou mais". Pesquisa de mercado dos Livres (citada pela da Pós): 182,3 mil em atividade e quase 240 mil registrados | P5 e L5 |
| X2 | Renda média CLT de 39 h | R$ 4.670,73 (pesquisa da Pós e persona da Pós) contra R$ 4.607,16 (tendências) | T5 |
| X3 | Número de gatos | 30 a 33,6 milhões (pesquisa da Pós) contra 30,8 e 33,3 milhões (tendências) | T6 |
| X4 | Workshop e UTI | Tendências A.4 diz "não é de UTI"; persona de Eventos e página do evento dizem o contrário | T2 |
| X5 | Felinos como única área sem turma | Tendências A.1 contra a própria seção 8, a persona da Pós e a concorrência (quatro provas sem turma) | T1 |
| X6 | Provas sem turma de destino | Os quatro arquivos e a concorrência falam em quatro provas; o catálogo mostra mais casos de destino incerto | P6 e tabela 6.1 |
| X7 | Fonte das regras da bolsa | Tendências diz "catálogo"; as regras estão em contexto/pos-graduacao.md | T4 |

Sem contradição: dados da Anclivepa (taxa de R$ 350,00, bolsa de 50% acima de 75%, inscrições até 07/11/2026, prova em 14/11 por cópia não oficial) e da UFPA com FADESP (R$ 1.920,00 por 18 meses, oferta até 04/05/2026) batem entre a persona da Pós e a inteligencia-concorrencia-pos.

## 6. Apoio às correções

### 6.1 Provas de bolsa de 27/11/2026 e turma aberta do mesmo curso e cidade (catálogo, 26/10/2026)

[SUPOSIÇÃO] A leitura abaixo supõe que o destino natural de cada prova é a turma aberta do mesmo curso, na mesma cidade, que começa depois da prova. A página da prova não diz o destino.

| Prova | Turma aberta compatível | Situação |
|---|---|---|
| 68652 Felinos, 68649 Endoscopia, 68653 Nefrologia, 68655 Odontologia | nenhuma | sem destino (já apontado nos arquivos) |
| 68650 Gastroenterologia (SP) | 68606 começa em 07/11/2026, antes da prova | destino incerto |
| 68647 Diagnóstico por Imagem (SP) | 68604 começa em 31/10/2026, antes da prova; 68611 em "verificar" e sem data | destino incerto |
| 68641 Cardiologia (SP) | nenhuma Cardiologia aberta em SP (68605 em "verificar"; 289 é de Goiânia; 698 é Ecocardiografia) | destino incerto |
| 68643 Clínica Cirúrgica (SP) | nenhuma aberta em SP (665 em "verificar"; 68632 é de Goiânia) | destino incerto |
| 68639 Anestesiologia (SP) | nenhuma Anestesiologia Veterinária aberta em SP (68607 em "verificar"; 657 e 359 são outros cursos, e a 359 exige residência ou pós na área) | destino incerto |
| 68660 Terapia Intensiva (SP) | só 68623, em Goiânia (666 em "verificar") | destino incerto |
| 68646 Dermatologia e 68651 Hematologia (SP) | 68610 e 68608 começam em 28/11/2026, um dia depois da prova, com 10 dias úteis para matrícula e 1ª mensalidade 30 dias antes do início | destino incerto pela data |
| Demais (68640, 68642, 68644, 68645, 68648, 68654, 68657, 68658, 68659, 68661) | 68609, 289, 68632, 68635, 68617, 68616, 68628, 68615, 68636, 68629 | turma aberta depois da prova |

---

## Lista 1. Fatos (com fonte)

- 30 turmas de Pós abertas, 22 provas de bolsa abertas a R$ 100,00 em 27/11/2026, 68656 fora do ar, 0 turma EAD aberta (586 em "verificar"): contexto/catalogo-de-cursos.md, seções 2 e 3 (26/10/2026).
- 657 tem 360 h e total de R$ 48.400,00; 707 tem 600 h e total de R$ 47.700,00; 333 tem total de R$ 28.050,00; 719 tem total de R$ 12.000,00; matrícula de R$ 250,00 em 333 e 60: catálogo, seção 2.
- 202 e 700 não têm carga horária nem turma no catálogo; 68634 está em "verificar", com 24 h e modalidade "Presencial" na loja: catálogo, seções 4 e 9.
- Regras da bolsa (11 bolsas, percentuais, nota 7,0, prazos, mínimo de 15 na página da prova): contexto/pos-graduacao.md (26/10/2026).
- Matrícula da Graduação "a partir de 2 dias depois do resultado": contexto/graduacao.md (editais 2027/1).
- Curso livre não confere diploma nem equivale a pós: contexto/cursos-livres.md.
- Workshop com blocos de UTI e "tanto no centro cirúrgico quanto na UTI": ficha do evento, citada na persona de Eventos (26/10/2026).
- Universo de veterinários e renda: pesquisa-de-mercado-pos-2026-10-26.md, seções 1.1 e 1.3 (S1, S2, S12) e citação da pesquisa dos Livres (AviNews, 09/09/2025).
- Dados da Anclivepa e da UFPA com FADESP: inteligencia-concorrencia-pos-2026-10-26.md, seções 0, 1 e 3 (resumo de busca de 26/10/2026).
- Regra de aprovação: peças com comparação com concorrente passam pelo responsável de contexto/ufape-geral.md (nome ainda não preenchido).

## Lista 2. Suposições

- [SUPOSIÇÃO] O destino natural de cada prova é a turma aberta do mesmo curso e cidade que começa depois de 27/11/2026 (tabela 6.1).
- [SUPOSIÇÃO] Não há travessão nem meia-risca invisível nos quatro arquivos (conferência feita por leitura, sem busca automática).
- [SUPOSIÇÃO] Os produtos 700 e 202 e o workshop seguem a regra do curso livre sobre diploma, porque o catálogo os lista com os Livres e contexto/eventos.md não tem regra própria de certificação.
- [SUPOSIÇÃO] As partes das pesquisas de mercado e da concorrência que o QA não leu (pesquisa da Pós depois da linha 140; concorrência da Pós depois da linha 120; arquivos de Livres) não trazem outra contradição com os quatro arquivos.

## Lista 3. Dados que faltam

- [CONFIRMAR] Turma de destino de cada uma das 22 provas, inclusive os casos de data e cidade da tabela 6.1.
- [CONFIRMAR NO CATÁLOGO] Regras da prova de bolsa no catálogo (hoje só em contexto/pos-graduacao.md); turma mínima (15 ou 20).
- [CONFIRMAR NO CATÁLOGO] Carga horária e turma de 202 e de 700; status, data, carga e modalidade de 68634.
- [CONFIRMAR] Validade do cupom SIMPNEUROMONIT e se vale para aluno de pós e ex-aluno de curso livre.
- [CONFIRMAR no edital oficial] Taxa de R$ 350,00 e datas da prova da Anclivepa-SP, antes de qualquer comparação em peça.
- [CONFIRMAR] Valor certo da média CLT de 39 h (R$ 4.670,73 ou R$ 4.607,16) e número oficial de médicos veterinários por critério (registrados e em atividade).
- [PREENCHER] Responsável pela aprovação de peças com comparação com concorrente, certificação, ato regulatório ou depoimento (contexto/ufape-geral.md, regras de aprovação).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação de Pós, curso livre e evento.
- [CONFIRMAR] Conversas, avaliações e dados agregados de alunos e candidatos, para que as personas deixem de ser hipótese (item 6 da auditoria 01 nos três arquivos de persona).

## Fontes

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/eventos.md; contexto/graduacao.md; contexto/catalogo-de-cursos.md; templates/persona.md; auditorias/01-qualidade-de-pesquisa.md; auditorias/conformidade-educacional.md; os quatro arquivos revisados; saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-26.md (linhas 1 a 140); saidas/01-inteligencia-de-mercado/inteligencia-concorrencia-pos-2026-10-26.md (linhas 1 a 120). Nenhuma fonte externa nova foi consultada pelo QA.
