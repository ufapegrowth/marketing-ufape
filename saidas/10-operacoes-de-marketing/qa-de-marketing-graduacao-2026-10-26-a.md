# QA de marketing: cadeia da Graduação 2027/1 (cinco planos de 26/10/2026)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 26/10/2026
- Status: rascunho de QA. Nada é publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 1)
  - contexto/cursos/graduacao/editais-2027-1.md
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md e graduacao-em-pedagogia.md (para conferir matriz, docentes e página)
  - templates/kit-de-lancamento-graduacao.md
  - auditorias/02-estrategia-e-posicionamento.md, 06-geracao-de-demanda.md, 11-midia-paga.md e conformidade-educacional.md
  - Arquivos revisados:
    - A1 saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md
    - A2 saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md
    - A3 saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md
    - A4 saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md
    - A5 saidas/11-midia-paga/estrategia-de-midia-graduacao-2026-10-26.md

## Como ler este QA

- Os cinco arquivos são planos e briefings, não peças finais. Cada um passa de novo no QA quando virar peça (criativo, post, mensagem), conforme o calendário do cmo (10/11/2026).
- Códigos dos itens: **OK** (cumpre); **NA** (não se aplica); **PE** (pendente externo: depende de resposta da Ufape, do site ou do jurídico; não bloqueia o plano, bloqueia a peça que depender dele); **FALHA** (o texto do arquivo precisa mudar).
- Regra do QA: qualquer FALHA leva o arquivo a "corrigir". Itens PE ficam listados como bloqueio de peça.
- Linhas citadas são as do arquivo revisado na leitura de 26/10/2026.

## Resumo dos vereditos

| Arquivo | Veredito | Correções obrigatórias |
|---|---|---|
| A1 cmo | **corrigir** | 3 (mais 2 de consistência de menor peso) |
| A2 estrategia-de-campanha | **corrigir** | 4 (mais 2 de menor peso) |
| A3 estrategia-de-oferta | **corrigir** | 5 (mais 1 de menor peso) |
| A4 gestor-de-midia | **corrigir** | 1 (mais 1 de consistência) |
| A5 estrategia-de-midia | **corrigir** | 3 (mais 2 de menor peso) |

Nenhum arquivo traz nota do MEC, frase de certificação, promessa de emprego, salário ou aprovação garantida, "últimas vagas", número de verba, meta ou taxa inventado, dado pessoal de aluno ou candidato, travessão ou meia-risca (conferência visual na leitura integral dos cinco arquivos). Todos usam público só 18+ nos anúncios e a LP da Graduação com UTM como destino. Os problemas são pontuais e estão listados abaixo.

## Conferência de dados (comum aos cinco arquivos)

| Dado | Fonte | A1 | A2 | A3 | A4 | A5 |
|---|---|---|---|---|---|---|
| Medicina Veterinária integral: de R$ 10.000,00 por R$ 5.000,00/mês (50%) | catálogo seção 1; Edital 003/2026 | OK | OK | OK | OK | OK |
| Medicina Veterinária noturno: de R$ 10.000,00 por R$ 4.000,00/mês (60%) | idem | OK | OK | OK | OK | OK |
| Pedagogia: de R$ 1.050,00 por R$ 525,00/mês (50%) | catálogo; Edital 003/2026 Goiânia | OK | OK | OK | OK | OK |
| Semestre cheio R$ 60.000,00 e R$ 6.300,00 em 6 parcelas | ficha dos editais | OK | OK | OK | NA | NA |
| Totais do 1º semestre com desconto R$ 30.000,00, R$ 24.000,00, R$ 3.150,00 (aritmética) | conta sobre os editais | NA | NA | OK | OK | OK |
| Validade: só 1º semestre de 2027; renovação semestral com comprovação; perda por atraso; sem acúmulo com programa governamental | Editais 003/2026 | OK | OK | OK | OK | OK |
| Vagas 45 + 45 e 80 | Editais 002 e 004/2026 | OK | OK | OK | OK | OK |
| Turma mínima 30 (com reembolso da 1ª parcela) | editais | OK | OK | OK | OK | OK |
| Inscrições gratuitas desde 17/08/2026 | editais | OK | OK | OK | OK | OK |
| Aulas em 22/02/2027 (segunda-feira) | editais; calendário conferido | OK | OK | OK | OK | OK |
| Enem média mínima 300, edições de 2010 em diante | editais | OK | OK (ver A2, item 3) | OK | NA | OK |
| Cancelamento com 80% até 2 dias antes (20/02/2027, pela conta) | editais | OK | OK | OK | OK | OK |
| Ato Medicina Veterinária: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) | catálogo | OK | OK | OK | OK | NA |
| Ato Pedagogia: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) | catálogo | OK | OK | OK | OK | NA |
| Credenciamento SP: Portaria MEC nº 176, de 27/02/2025 (D.O.U. 28/02/2025); Goiânia: Portaria MEC nº 871, de 10/11/2022, publicação [CONFIRMAR] | ufape-geral.md; ficha dos editais | OK | OK | OK | NA | NA |
| Carga horária Medicina Veterinária 4.195 h + 75 h | catálogo | OK | OK | OK | OK | NA |
| Carga horária Pedagogia só como divergente (3.440 h site x 3.640 h edital), fora das peças | catálogo | OK | OK | OK | OK | OK |
| Nota do MEC, frase de certificação | proibido | ausente | ausente | ausente | ausente | ausente |
| "Últimas vagas", "vagas limitadas", contagem regressiva | proibido | só como proibição | idem | idem | idem | idem |
| Números de verba, meta, taxa | [CONFIRMAR] | OK | OK | OK | OK (fórmulas; percentuais como [SUPOSIÇÃO de desenho] sobre verba [CONFIRMAR]) | OK (idem; ver A5, item 1 sobre datas do Enem) |
| Público de anúncio só 18+ | regra do cmo | OK | OK | OK | OK | OK |
| Destino único: LP da Graduação com UTM, URL [CONFIRMAR, G13] | kit e CLAUDE.md | OK | OK | OK | OK | OK |
| Cuidados com menor de idade | contexto/graduacao.md; Edital 002/2026 | OK | OK (ver item 6) | OK | OK | OK |
| Dado pessoal de aluno ou candidato | proibido | ausente | ausente | ausente | ausente | ausente |
| Travessão ou meia-risca | proibido | ausente | ausente | ausente | ausente | ausente |

Aritmética conferida: 119 dias (17 semanas) de 26/10/2026 a 22/02/2027; 10 semanas desde 17/08/2026; dias da semana de 26/10, 08/11, 15/11, 16/11/2026 e 22/02/2027; shares 52,5%, 42,0% e 5,5% (30.000, 24.000 e 3.150 sobre 57.150); todas as tabelas de percentual por fase, canal e semana do A5 (seções 2.2 a 2.6); CPL teto por ponto de conversão (R$ 300,00, R$ 240,00, R$ 31,50) e 30 x T1 (R$ 900.000,00, R$ 720.000,00, R$ 94.500,00) do A4. Tudo bate, salvo o arredondamento indicado em A5, item 5.

---

## A1. cmo-graduacao-2026-10-26.md

### Auditoria 02 (estratégia e posicionamento)

| Item | Resultado | Nota |
|---|---|---|
| Uma única meta principal | OK | 3 turmas com pelo menos 30 matrículas confirmadas até 22/02/2027; alvo acima do piso [CONFIRMAR] |
| Persona e curso nomeados | OK | G1 e G2; personas marcadas [SUPOSIÇÃO] |
| 8 canais avaliados, ativos cabem na capacidade, fora justificados | OK / PE | Tabela da seção 4 completa; capacidade [CONFIRMAR] (G11) |
| Alternativa real nomeada | OK | outras faculdades e vestibulares públicos; Pedagogia EAD mais barata |
| Todo pilar tem prova | **FALHA** | L109: "atacar com 'prática e hospital desde o começo'". A existência do hospital está no contexto; o uso dele pela graduação, e desde o 1º semestre, não está provado (o próprio A3 bloqueia o pilar até G11). Ver correção 1 |
| Regras de voz com exemplos | PE | voz da marca ainda [SUPOSIÇÃO] em ufape-geral.md |
| Cabe no tempo e na verba | PE | verba [CONFIRMAR] (G3) |
| Nenhuma promessa de emprego, aprovação ou salário | OK | |
| Preços e condições do catálogo | OK | conferidos na tabela acima |

### Conformidade educacional

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | OK | Pedagogia sem carga horária até G5 |
| Status "aberto" | OK | os dois cursos |
| Modalidade clara | OK | presencial; até 30% a distância informado |
| Graduação: ato do catálogo, sem antecipar | OK | |
| Pós lato sensu | NA | |
| Curso livre | NA | |
| Nota MEC só com fonte | OK | nenhuma nota |
| Sem promessa de emprego, salário, concurso, sucesso | OK | |
| Empregabilidade com fonte | NA | nenhum dado |
| Superlativos com fonte | OK | nenhum |
| Comparação com concorrente objetiva | OK | EAD só por atributos verificáveis |
| Preço completo, sem esconder taxa ou reajuste | OK | modelo de linha L177; reajuste sinalizado (G12) |
| Desconto com regra, público e validade | OK | |
| Urgência real | OK | |
| Prouni, Fies, financiamento | OK | ausentes |
| Autorização de imagem e depoimento | PE | G11 |
| Menores só com autorização | OK | seção 4 e G10 |
| Formulário com finalidade e política de privacidade | PE | G13 |
| WhatsApp e e-mail só com consentimento | OK / PE | regra de opt-in escrita; consentimento de menor no CRM (G10) |
| Nenhum dado pessoal | OK | |
| Políticas Meta e Google, sem segmentação discriminatória | OK | |
| Página de destino entrega o prometido | PE | G6 (Pedagogia) e G8 (noturno) |
| Texto não afirma característica pessoal | OK | |
| Sem escassez falsa, contador, botão falso | OK | |
| Sem pessoa pública ou parceria inexistente | OK | |
| Sem caixa alta ou símbolos | NA | sem texto de anúncio |
| Página carrega, domínio, dados da Ufape, política | PE | G13 |
| Sem sugestão de driblar análise | OK | |

### Kit mínimo

Kit G1 e kit G2 com todas as entregas do templates/kit-de-lancamento-graduacao.md nas quantidades mínimas (1, 1, 6, 4, 5, 3, 2), mais acréscimos. O mínimo não diminuiu. OK.

### Veredito A1: **corrigir**

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 2.4, L109 (cruzamentos do G1) e seção 5.1, L219 (post de captação "hospital próprio") | Pilar "hospital desde o começo" sem prova de uso pela graduação | Reescrever para "prática desde o 1º semestre (matriz) e hospital veterinário próprio (Ufape Clínica) [CONFIRMAR uso pela graduação e autorização, G11]" e condicionar o post de captação sobre o hospital a G11 |
| 2 | Seção 7, L300 a L306 | Caminhos e datas das etapas 2 a 4 (…-2026-10-28, -10-29, -10-30) não batem com os arquivos entregues (todos …-2026-10-26) | Atualizar a tabela com os caminhos reais, para a plataforma encadear as etapas sem erro |
| 3 | Seção 2.4, L109, e seção 9, L362 | Diz que o anúncio do noturno não "escala" antes de G8 (permite rodar em teste); o A4 (L73) bloqueia o noturno por inteiro até G8 e MP4 | Alinhar ao A4: "anúncio pago do noturno bloqueado até G8 e MP4" |
| 4 (menor peso) | Seção 3, L139 | "cerca de 8 a 10 vezes menor": pela aritmética do catálogo é de 7,6 (R$ 4.000,00 / R$ 525,00) a 9,5 vezes (R$ 5.000,00 / R$ 525,00) | Trocar por "cerca de 7,6 a 9,5 vezes" |
| 5 (menor peso) | Seção 3, L144 | Nome sugerido grad_pedagogia_meta_cadastro_goiania_202611 difere do padrão do A4 (goiania18, AAAAMM do mês de subida, porque a Pedagogia está bloqueada) | Adotar grad_pedagogia_meta_cadastro_goiania18_AAAAMM |

---

## A2. estrategia-de-campanha-graduacao-2026-10-26.md

### Auditoria 06 (geração de demanda)

| Item | Resultado | Nota |
|---|---|---|
| Toda campanha tem briefing escrito | OK | G1 e G2 no formato do template |
| Metas definidas antes do lançamento | **FALHA** | Valores [CONFIRMAR] são aceitos, mas L201 e a linha C0 (L207) permitem lançar "em teste com limite de gasto aprovado" sem metas numéricas. Isso contraria este item e o item 2 da auditoria 11. Ver correção 1 |
| Isca entrega a promessa do título | NA | sem isca; sugestão de guia fica para iscas-digitais |
| Toda captura tem nutrição em seguida | OK / PE | régua (06/11) e ativação da base (30/10); segmento no CRM [CONFIRMAR] |
| Plano de distribuição por peça | PE | por fase está feito; por peça fica com posts-sociais e gestor-de-midia |
| Regras das comunidades | NA | sem ação em grupos |
| Revisão no ponto de checagem | PE | C0 a C3 com data e regra; ainda não ocorreram |
| Consentimento em todo formulário | PE | G13 e G10; a squad não altera a LP |
| Bolsas, descontos e prazos batem com catálogo e ficha | OK | conferidos (tabela de dados) |

### Conformidade educacional

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno | OK | |
| Status "aberto" | OK | |
| Modalidade clara | OK | |
| Graduação: ato do catálogo | OK | |
| Pós lato sensu / curso livre | NA | |
| Nota MEC | OK | |
| Sem promessa de emprego, salário, aprovação | **FALHA** | L102 "entre com sua nota do Enem" e L259 "ou sua nota do Enem" sem a condição de média mínima de 300 pontos, edições de 2010 em diante: lida sozinha, insinua entrada com qualquer nota. Ver correção 3 |
| Empregabilidade com fonte | NA | |
| Superlativos | OK | |
| Comparação com concorrente | OK | EAD só por atributos verificáveis |
| Preço completo | **FALHA** | L108 mensagem central do noturno "com 60% de desconto no 1º semestre de 2027" sem valor cheio e valor com desconto; a regra do contexto e da ficha dos editais exige percentual, valor cheio, valor com desconto e validade juntos. Ver correção 2 |
| Desconto com regra, público e validade | OK | seção "Oferta" completa |
| Urgência real | OK | |
| Prouni, Fies | OK | |
| Autorização de imagem | PE | G11 |
| Menores | OK | L124 usa "responsável legal"; o edital diz "representante legal" (correção 6) |
| Formulário com finalidade e política | PE | G13 |
| WhatsApp e e-mail com consentimento | OK / PE | G10 |
| Nenhum dado pessoal | OK | |
| Políticas Meta e Google | OK | regra 6 |
| Página entrega o prometido | PE / **FALHA** | PE em G6 e G8. FALHA em L102 e L106: a mensagem do integral promete "prática ... já no 1º semestre, com hospital veterinário próprio" como se a prática do 1º semestre fosse no hospital, sem prova de uso pela graduação (o A3 bloqueia esse pilar). Ver correção 4 |
| Texto não afirma característica pessoal | OK | exemplos L35, L117 e L271 |
| Sem escassez falsa, contador, botão falso | OK | |
| Sem pessoa pública | OK | |
| Caixa alta | NA | |
| Página carrega e mostra política | PE | G13 |
| Sem drible de análise | OK | |

### Veredito A2: **corrigir**

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 1, L201; tabela de checagens, L207 (C0); repetido no G2, L333 | Permite subir mídia "em teste" sem metas numéricas de CPL e custo por matrícula | Trocar por: "Nenhuma campanha sobe, nem em teste, sem CPL máximo e custo por matrícula máximo numéricos (mesmo provisórios) e limite de gasto aprovados por humano (MP1 e MP2). Sem números em C0, a data de 16/11 é adiada e o cmo avisa a pessoa do marketing" |
| 2 | L108 (mensagem central do noturno) | Percentual sem valor cheio e valor com desconto | "Estude veterinária à noite, em São Paulo: de R$ 10.000,00 por R$ 4.000,00 por mês no 1º semestre de 2027 (60% de desconto). Condições e validade no edital." |
| 3 | L102 (ideia comum) e L259 (mensagem central G2) | Enem sem a condição de ingresso | Acrescentar "(média mínima de 300 pontos, edições de 2010 em diante)" sempre que a nota do Enem aparecer como forma de entrada; trocar "entre com sua nota" por "use sua nota" |
| 4 | L102 e L106 (mensagem do integral, coluna de provas) | Hospital usado como prova da prática do 1º semestre sem confirmação | Separar as duas provas: "prática desde o 1º semestre" (matriz, verificada) e "hospital veterinário próprio" com [CONFIRMAR uso pela graduação e autorização, G11]; peça com o hospital só depois de G11, como no A3 |
| 5 (menor peso) | L118 | "anúncio pago do noturno só escala depois da correção" difere do bloqueio total do A4 | Alinhar: "anúncio pago do noturno bloqueado até G8 e MP4" |
| 6 (menor peso) | L124 | "responsável legal" | Usar o termo do edital: "representante legal" |

---

## A3. estrategia-de-oferta-graduacao-2026-10-26.md

### Auditoria 02 (estratégia e posicionamento)

| Item | Resultado | Nota |
|---|---|---|
| Uma única meta principal | OK | serve à meta do cmo |
| Persona e curso ou oferta nomeados | OK | três segmentos, [SUPOSIÇÃO] marcada |
| 8 canais | OK | herdado do cmo, sem mudança |
| Alternativa real nomeada | OK | |
| Todo pilar tem prova | **FALHA** | (a) L207: "Prática Docente e Projeto Integrador em todos os semestres a partir do 1º"; pela ficha da Pedagogia, o Projeto Integrador vai do 1º ao 7º semestre (o 8º só tem Prática Docente VIII). (b) L111 e L139: proposta de valor e promessa do segmento A usam o hospital como pilar, contra a regra do próprio arquivo (L294: "Pilar hospital só entra em peça com essa confirmação") |
| Regras de voz com exemplos | PE | exemplos de frase permitida e bloqueada dados; voz da marca [SUPOSIÇÃO] |
| Cabe no tempo e na verba | PE | G3 |
| Nenhuma promessa de emprego, aprovação ou salário | OK | redação descrita como eliminatória |
| Preços e condições do catálogo ou [CONFIRMAR] | **FALHA** | L51 e L62 aplicam à Pedagogia ("idem") o vencimento no dia 10 e o reajuste de dezembro, cuja fonte é o Edital 002/2026 de São Paulo; a ficha dos editais não lista mensalidade nem reajuste entre as regras que o Edital 004/2026 repete. L84 repete o reajuste para a Pedagogia |

### Conformidade educacional

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno | OK | |
| Status "aberto" | OK | |
| Modalidade clara | OK | L93 "como a lei permite" (correção 6) |
| Graduação: ato do catálogo | OK | atos e credenciamentos exatos; publicação da Portaria nº 871/2022 omitida |
| Pós lato sensu / curso livre | NA | |
| Nota MEC | OK | |
| Sem promessa de emprego, salário, aprovação | OK | |
| Empregabilidade com fonte | NA | |
| Superlativos | OK | "maior desconto da linha" (L152) é comparação interna verdadeira (60% contra 50%) |
| Comparação com concorrente | OK | EAD sem preço de terceiros |
| Preço completo | **FALHA** | L111 (1.3) e L156 (2.3): propostas de valor com "50% de desconto" e "60% de desconto" sem valor cheio e valor com desconto. Pedagogia: reajuste e vencimento sem fonte (ver auditoria 02) |
| Desconto com regra, público e validade | OK | seção 0.2 e versões curtas corretas, com "1º semestre de 2027" e "Condições e validade no edital" |
| Urgência real | OK | P3 só com data e número reais |
| Prouni, Fies | OK | |
| Autorização de imagem e nome | PE / **FALHA** | PE em G11. FALHA em L132: além de nome e titulação, cita cargos (coordenadora de pós, Diretora Científica), o que a regra do briefing de execução não permite ("Docentes só com nome e titulação como estão na ficha") |
| Menores | OK | |
| Formulário com finalidade e política | PE | G13 |
| WhatsApp e e-mail com consentimento | PE | G10 |
| Nenhum dado pessoal | OK | docentes não são aluno nem candidato |
| Políticas Meta e Google | OK | P8 nunca vira segmentação por emprego |
| Página entrega o prometido | PE / **FALHA** | PE em G6 e G8. FALHA em L84: a resposta manda o candidato pedir "as regras de renovação por escrito", documento que o próprio arquivo diz não existir (P1) |
| Texto não afirma característica pessoal | OK | |
| Sem escassez falsa | OK | |
| Sem pessoa pública | OK | |
| Caixa alta | NA | |
| Página carrega e mostra política | PE | G13 |
| Sem drible de análise | OK | |

### Veredito A3: **corrigir**

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 3.4, L207 | Projeto Integrador não está em todos os semestres | "Prática Docente em todos os 8 semestres; Projeto Integrador do 1º ao 7º semestre; estágio supervisionado obrigatório a partir do 6º semestre" |
| 2 | Seção 1.5, L132 | Docentes com cargos, além de nome e titulação | Deixar só nome e titulação como na ficha (por exemplo "Dra. Sabrina Caruso Chate", "Profa. Dra. Mayara Travalini", "Profa. Dra. Denise Fantoni", "Dr. Alessandro Rodrigues de Carvalho Martins (coordenação)"), com [CONFIRMAR autorização]; o vínculo com as pós entra como fato geral ("professores que também dão aula nas pós da Ufape", contexto/graduacao.md), sem cargo individual |
| 3 | Seção 0.1, L51 e L62 (coluna Pedagogia "idem"); seção 0.3, L84 | Vencimento no dia 10 e reajuste de dezembro aplicados à Pedagogia sem fonte no Edital 004/2026 | Na coluna Pedagogia, trocar por "[CONFIRMAR com a Ufape: vencimento e reajuste no Edital 004/2026]"; na resposta 0.3, citar o reajuste só para a Medicina Veterinária até a confirmação |
| 4 | Seções 1.3 (L111), 1.6 (L139), 2.3 (L156) | Proposta de valor e promessa com hospital como pilar (contra L294) e com percentual sem valores | Tirar o hospital da proposta e da promessa até G11 (ou marcar [CONFIRMAR uso pela graduação, G11]); trocar "50% de desconto" e "60% de desconto" pelas versões curtas da seção 0.2 |
| 5 | Seção 0.3, L84 | Promete regras de renovação "por escrito" que ainda não existem | Trocar por "Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação." e manter [CONFIRMAR] até P1 ser aprovada |
| 6 (menor peso) | Seção 0.3, L93 | "como a lei permite" é afirmação jurídica genérica | "conforme o edital, que cita o Decreto 14.256/2025" |

---

## A4. gestor-de-midia-graduacao-2026-10-26.md

### Auditoria 11 (mídia paga)

| Item | Resultado | Nota |
|---|---|---|
| Plano aprovado, canais ativados e fora justificados | PE | justificativas na seção 3.1; aprovação humana pendente |
| Metas de CPL e custo por matrícula escritas antes de subir | **FALHA** / PE | Fórmulas e conta pronta corretas; valores [CONFIRMAR] aceitos. Mas L375 ("sem números, a mídia sobe só em teste com limite de gasto aprovado e sem escala") e L423 ("Bloqueia a subida com escala") deixam subir sem meta numérica. Ver correção 1 |
| Verba dentro do aprovado, com aprovador | PE | MP2; tabela de aprovadores vazia (G14) |
| Nomenclatura padrão | OK | seção 4.2 |
| UTMs completas e origem no CRM | OK / PE | padrão e exemplos (4.6); URL e CRM em G13 e MP10 |
| Pixel, API, conversões configurados e testados | PE | checklist 4.8; estado [DADO NÃO FORNECIDO] |
| Criativos aprovados na conformidade | PE | QA de 10/11/2026 |
| Políticas das plataformas | OK | |
| Nenhum público com menores; YouTube sem conteúdo infantil | OK | 4.3, 4.5, 4.8 |
| Post de docente promovido ou Spark Ad com autorização | OK | Spark Ad só com autorização; LinkedIn fora |
| Relatório semanal ao cmo | PE | a partir de 23/11/2026 |
| Sem segmentação discriminatória | OK | 4.5 |
| Públicos sem dado pessoal sem base legal | OK | listas bloqueadas até MP7 |
| Dados de curso conferidos no catálogo | OK | |
| Destino de WhatsApp oficial | NA | sem campanha de mensagem; destino é a LP |
| Números só das exportações | OK | nenhum número de desempenho usado |
| Nenhuma alteração sem humano | OK | MP1 a MP14 |

### Conformidade educacional

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno | OK | |
| Status "aberto" | OK | |
| Modalidade clara | OK | |
| Graduação: ato do catálogo | OK | |
| Pós lato sensu / curso livre | NA | |
| Nota MEC | OK | |
| Sem promessa | OK | |
| Empregabilidade | NA | |
| Superlativos | OK | |
| Comparação com concorrente | OK | negativas de busca não citam concorrente |
| Preço completo | OK | usa o texto oficial do A3 (0.2) |
| Desconto com regra e validade | OK | |
| Urgência real | OK | reta final sem "últimas vagas" |
| Prouni, Fies | OK | |
| Autorização de imagem | PE | G11 |
| Menores | OK | 18+, listas bloqueadas, anúncio de busca visto por menor levado ao jurídico |
| Formulário com finalidade e política | PE | G13 |
| WhatsApp e e-mail | NA | fora da mídia paga |
| Nenhum dado pessoal | OK | |
| Políticas Meta e Google | OK | sem Performance Max; sem interesse por emprego |
| Página entrega o prometido | PE | noturno (G8) e Pedagogia (G6) bloqueados |
| Texto não afirma característica pessoal | OK | |
| Sem escassez falsa | OK | |
| Sem pessoa pública | OK | |
| Caixa alta | NA | |
| Página carrega e mostra política | PE | checklist 4.8 |
| Sem drible de análise | OK | |

### Veredito A4: **corrigir**

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 5, L375; seção 8, L423 e L465 | Exceção de C0 permite subir sem CPL e custo por matrícula numéricos | Escrever: "Nenhuma campanha sobe, nem em teste, sem CPLmax e CPMmax numéricos (mesmo provisórios, cenário conservador) aprovados em MP1 e verba aprovada em MP2. Sem isso, MP11 não é pedido e a subida de 16/11/2026 é adiada" |
| 2 (consistência) | Seção 1.2, L73 | Bloqueio total do noturno é mais rígido que o texto do A1 e do A2 ("não escala") | Manter o bloqueio do A4; a correção fica no A1 (item 3) e no A2 (item 5) |

---

## A5. estrategia-de-midia-graduacao-2026-10-26.md

### Auditoria 11 (mídia paga)

| Item | Resultado | Nota |
|---|---|---|
| Plano aprovado, canais justificados | PE | segue o A4 |
| Metas escritas antes de subir | **FALHA** / PE | Fórmulas, metas por fase e limite de revisão corretos; valores [CONFIRMAR]. L314 repete a exceção de C0 ("Sem números, a fase 1 sobe só em teste") |
| Verba dentro do aprovado | PE | tudo em percentual de VT [CONFIRMAR]; trava na 6.2 |
| Nomenclatura padrão | OK | |
| UTMs completas | OK / PE | exemplos por campanha; G13 |
| Pixel e conversões | PE | |
| Criativos aprovados na conformidade | PE | |
| Políticas das plataformas | OK | Sisu nunca associado à Ufape; termos com Sisu fora por padrão (EM6) |
| Nenhum público com menores | OK | 3.1 e 3.4 |
| Spark Ad com autorização | OK | |
| Relatório semanal | PE | |
| Sem segmentação discriminatória | OK / atenção | L280: palavra-chave "veterinária para quem trabalha" é intenção de busca, não texto; validar com anuncios-google (item 4) |
| Públicos sem dado pessoal | OK | exclusão só por evento do pixel (EM7) |
| Dados de curso conferidos | OK | |
| Destino de WhatsApp | NA | |
| Números só das exportações | OK / **FALHA** | Nenhum número de desempenho. Mas L497 registra "Datas do Enem 2026: 08 e 15/11/2026" como fato, com fonte "pedido do orquestrador", que não é fonte da squad. Ver correção 1 |
| Nenhuma alteração sem humano | OK | EM1 a EM9 |

### Conformidade educacional

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno | OK | |
| Status "aberto" | OK | |
| Modalidade clara | OK | |
| Graduação: ato do catálogo | OK | |
| Pós lato sensu / curso livre | NA | |
| Nota MEC | OK | |
| Sem promessa | OK | L327 proíbe sugerir que a nota de 2026 já pode ser usada |
| Empregabilidade | NA | |
| Superlativos | OK | |
| Comparação com concorrente | OK | |
| Preço completo | OK | 3.1 exige valor cheio, valor com desconto, "1º semestre de 2027" e "Condições e validade no edital" |
| Desconto com regra e validade | OK | |
| Urgência real | OK | |
| Prouni, Fies | OK | |
| Autorização de imagem | PE | G11 |
| Menores | OK | |
| Formulário com finalidade e política | PE | G13 |
| WhatsApp e e-mail | NA | |
| Nenhum dado pessoal | OK | |
| Políticas Meta e Google | OK | |
| Página entrega o prometido | PE | G6 e G8 |
| Texto não afirma característica pessoal | OK | |
| Sem escassez falsa | OK | |
| Sem pessoa pública | OK | |
| Caixa alta | OK | |
| Página carrega e mostra política | PE | |
| Sem drible de análise | OK | |

### Veredito A5: **corrigir**

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 9, L497 (fato); dependentes em L34, L156, L318, L321, L327 | Datas do Enem 2026 (08 e 15/11/2026) tratadas como fato sem fonte da squad; A1 e A2 marcam as datas do Enem 2026 como [CONFIRMAR] | Mover para "Dados que faltam" como "[CONFIRMAR no calendário oficial do Inep] datas informadas pelo orquestrador: 08 e 15/11/2026"; nas seções 0, 2.5 e 4.1, escrever as datas com esse marcador. A data de subida (16/11) continua valendo como data interna do cmo |
| 2 | Seção 4.1, L314 | Exceção de C0 permite subir sem metas numéricas | Mesmo texto da correção 1 do A4 |
| 3 | Seção 8, L487 | Diz que as datas de notas do Enem e do Sisu "seguem [CONFIRMAR] no contexto/graduacao.md", mas o contexto não traz essas datas | Trocar por "seguem [CONFIRMAR] neste arquivo (seção 11) e nos pedidos ao cmo" |
| 4 (menor peso) | Seção 3.6, L280 | Grupo "veterinária para quem trabalha" encosta em situação de emprego | Manter só se o anuncios-google confirmar que a política de anúncios personalizados do Google permite; o texto do anúncio continua sem afirmar emprego |
| 5 (menor peso) | Seção 2.7, L204 e L205 | Mínimos da Pedagogia calculados com percentuais arredondados (1,24% e 0,41%) | Usar os exatos (1,2375% e 0,4125%): 484,8 x CPLmax e 727,3 x CPLmax |

---

## Consistência entre os cinco arquivos

| Tema | Resultado | Nota |
|---|---|---|
| Meta principal | OK | piso de 30 por turma, alvo [CONFIRMAR] até 45, 45 e 80, em A1 a A5 |
| Fases e datas | OK | captação 16/11 a 06/12/2026; aquecimento 07/12/2026 a 03/01/2027; conversão 04/01 a 31/01/2027; reta final 01/02 a 21/02/2027; pausa 22/02/2027; relatório até 05/03/2027 |
| Checagens | OK | C0 30/10, C1 30/11, C2 04/01, C3 25/01; revisões às segundas |
| Regra de C0 | **inconsistente** | A1 não permite subir sem metas; A2, A4 e A5 permitem subir em teste sem números. Corrigir A2, A4 e A5 (ver acima) |
| Canais | OK com uma ressalva | Instagram, Facebook e WhatsApp ativos; YouTube leve e TikTok em teste só no integral; LinkedIn, X e podcast fora; busca paga a critério do gestor. Ressalva: noturno "não escala" (A1, A2) x "bloqueado" (A4, A5) |
| Bloqueios | OK | Pedagogia até G6 (A4 e A5 acrescentam MP4 e MP1, mais rígidos e coerentes); TikTok até G11 e MP5; listas até MP7 |
| Datas do Enem 2026 | **inconsistente** | [CONFIRMAR] em A1 (L105, L394) e A2 (L163) x fato em A5 (L497) |
| Hospital como pilar | **inconsistente** | A3 bloqueia até G11 (L294); A1 (L109) e A2 (L102, L106) usam sem marcador; A3 também usa em 1.3 e 1.6 |
| Pedidos de aprovação | OK | G1 a G16 (cmo), MP1 a MP14 (gestor), EM1 a EM9 (estrategia-de-midia), P1 a P12 (propostas, não divulgáveis); referências cruzadas corretas |
| Nomenclatura | menor | goiania (A1, A2) x goiania18 (A4, A5); A4 registrou a divergência |
| Nomes e datas dos arquivos | menor | A1 seção 7 aponta datas futuras; A2 a A5 registram a diferença |
| Kit mínimo | OK | não diminuiu em nenhum arquivo |

## Regra de aprovação humana (contexto/ufape-geral.md)

A tabela de aprovadores está vazia em contexto/ufape-geral.md. Todos os arquivos pedem a nomeação (G14 do cmo). Peças com ato regulatório (todas as que citam portaria) passam também pela regulação da Ufape, conforme a auditoria de conformidade. Até a nomeação, nenhum dos cinco planos pode ser marcado como aprovado por humano.

## Encaminhamento

Os cinco arquivos **voltam para os agentes que os produziram** (cmo, estrategia-de-campanha, estrategia-de-oferta, gestor-de-midia e estrategia-de-midia), com as correções listadas. Depois da correção, nova rodada deste QA (arquivo …-b) e então aprovação humana. A cadeia pode seguir a etapa 5 (criativos-de-anuncio) só usando as versões curtas da seção 0.2 do A3, sem o pilar hospital e com a condição do Enem completa.

---

## Fatos (com fonte)

- Preços, percentuais, validade, vagas, turma mínima, datas de inscrição e de aulas, Enem mínimo e atos conferidos e corretos nos cinco arquivos (catálogo seção 1; contexto/cursos/graduacao/editais-2027-1.md).
- Pedagogia: Projeto Integrador do 1º ao 7º semestre; Prática Docente do 1º ao 8º; estágio a partir do 6º (contexto/cursos/graduacao/graduacao-em-pedagogia.md, matriz).
- Medicina Veterinária: Práticas Hospitalares e Projeto Extensionista I no 1º semestre; estágio no 7º e 8º (integral) e 9º e 10º (noturno); página do noturno com "INTEGRAL" no campo turno (ficha da Medicina Veterinária).
- Docentes da página da Medicina Veterinária e títulos usados pelo A3 (ficha da Medicina Veterinária).
- Vencimento no dia 10 e reajuste de dezembro constam do Edital 002/2026 (SP); a ficha não os lista para o Edital 004/2026 (ficha dos editais).
- Tabela de aprovadores vazia (contexto/ufape-geral.md).

## Suposições

- [SUPOSIÇÃO] A conferência de travessão e meia-risca foi visual, na leitura integral dos cinco arquivos; não encontrei nenhum.
- [SUPOSIÇÃO] Carnaval de 2027 em 08 e 09/02 (pela Páscoa de 28/03/2027), o que bate com a semana S13 do A5; continua [CONFIRMAR] no calendário oficial.
- [SUPOSIÇÃO] A frase "entre com sua nota do Enem" seria lida pelo público como entrada garantida; por isso pedi a condição completa.

## Dados que faltam

- [CONFIRMAR] Datas do Enem 2026, da divulgação das notas e do resultado do Sisu (calendários oficiais do Inep e do MEC).
- [CONFIRMAR] Vencimento e reajuste da Pedagogia no Edital 004/2026.
- [CONFIRMAR] Uso da Ufape Clínica pela graduação e autorização de imagem de docentes e do hospital (G11).
- [CONFIRMAR] Metas numéricas (CPLmax, CPMmax), verba e aprovador (MP1, MP2, G3), antes de qualquer subida.
- [CONFIRMAR] URL da LP com UTM, formulário com finalidade e política de privacidade, origem no CRM (G13); consentimento de candidato menor (G10).
- [CONFIRMAR] Correção das páginas (G6, G8), dos Editais 003/2026 (G7) e carga horária da Pedagogia (G5).
- [CONFIRMAR] Aprovadores por tipo de peça (G14).
- [CONFIRMAR NO CATÁLOGO] Horário de prática e estágio do noturno; coordenação e corpo docente da Pedagogia.
