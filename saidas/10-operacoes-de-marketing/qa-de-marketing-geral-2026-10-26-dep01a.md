# QA de marketing: saídas do departamento 01 (pesquisa de mercado e insights de alunos, Pós e Livres)

- Agente: qa-de-marketing
- Linha: geral (revisão de quatro arquivos: dois da linha pos e dois da linha livres)
- Data: 26/10/2026
- Status: rascunho de QA. Nenhum arquivo revisado foi alterado. Nada é publicado, enviado ou pago sem aprovação humana.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md
  - contexto/catalogo-de-cursos.md (seções 1 a 9, inteiro)
  - auditorias/01-qualidade-de-pesquisa.md
  - auditorias/conformidade-educacional.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 4, para conferir o escopo da etapa 1.1 e 1.3)
  - Arquivos revisados (inteiros): saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-26.md, pesquisa-de-mercado-livres-2026-10-26.md, insights-de-alunos-pos-2026-10-26.md e insights-de-alunos-livres-2026-10-26.md
- Limite desta revisão: as fichas de contexto/cursos/ não foram abertas. Dados que os agentes atribuem às fichas foram conferidos só quanto à marcação ([CONFIRMAR NO CATÁLOGO] quando não estão no catálogo), não quanto ao conteúdo. A busca por travessão e meia-risca foi feita por leitura integral (sem ferramenta de busca de caractere) [SUPOSIÇÃO: nenhuma ocorrência escapou à leitura].
- Regra de leitura das auditorias: os quatro arquivos são documentos internos de pesquisa, não peças. Itens de conformidade que só existem em peça (formulário, anúncio, página de destino, envio) ficam como "não se aplica", com o motivo.

## Resumo dos vereditos

| Arquivo | Veredito | Problemas que exigem correção |
|---|---|---|
| pesquisa-de-mercado-pos-2026-10-26.md | CORRIGIR | 8 |
| pesquisa-de-mercado-livres-2026-10-26.md | CORRIGIR | 10 |
| insights-de-alunos-pos-2026-10-26.md | CORRIGIR | 2 |
| insights-de-alunos-livres-2026-10-26.md | APROVADO (com 3 ajustes recomendados, não bloqueantes) | 0 |

Achados gerais da busca pedida:
- Dado pessoal de aluno, candidato ou lead: nenhum nos quatro arquivos. Docentes não são nomeados. O único CEP citado (insights-pos, seção 6) é de endereço da Ufape, não de pessoa.
- Travessão ou meia-risca: nenhum encontrado.
- Frase de certificação ligada ao MEC escrita por extenso: aparece em pesquisa-pos (linhas 39 e 303) e pesquisa-livres (linha 106), sempre como problema a evitar, nunca como afirmação. O briefing manda nunca escrever a frase: corrigir (ver listas).
- "Últimas vagas", "vagas limitadas" ou urgência sem número: não usados como chamada. Os descontos "para os 10 primeiros" (359, 352) e as "vagas presenciais limitadas" (616) aparecem só como alerta, com a ressalva de que não viram escassez em peça. Correto.
- Número de meta ou verba inventado: nenhum. A conta de 590 a 600 matrículas (pesquisa-pos, seção 3) é aritmética sobre a turma mínima, declarada como "não é meta". Correto.

---

## 1. pesquisa-de-mercado-pos-2026-10-26.md

### 1.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | NÃO ATENDE | Fontes sem data de publicação ou com fonte primária não localizada sustentam conclusões: S9 (projeção de 6% e 3,5% ao ano, "fonte primária não localizada"), base da oportunidade 1 (linhas 29, 69, 265, 305); S12 (salários, "sem data"), base do risco 1 e da conta de esforço (linhas 37, 77, 78, 156, 461); S11 (reportagens de 2026 com "endereços exatos a confirmar", linhas 265 e 511); S6, S10, S18, S21, S24, S26 e S27 sem data de publicação na lista de fontes |
| Suposições marcadas com [SUPOSIÇÃO] | ATENDE | Lista 2 completa; leituras inferidas marcadas no texto |
| Citações de candidatos e alunos literais e anonimizadas | NÃO SE APLICA | Não há citação de candidato ou aluno |
| Dados de concorrentes públicos e datados | ATENDE COM RESSALVA | Anclivepa-SP, UFPA e Unicruz com edital e ano; valor da Unicruz com [CONFIRMAR] de edição (linha 145). Qualittas sem data (S18) entra no item 1 |
| Números de mercado com faixa mínima e máxima | ATENDE | Seção 3 traz mínimo e máximo; grupos sem fonte declarados como "sem fonte" |
| Persona baseada em alunos e candidatos reais | NÃO SE APLICA | O arquivo não constrói persona; grupos G1 a G6 são de dimensionamento |
| Conclusões terminam em ações | ATENDE | Seção 9 ("O que exige decisão agora", com quem e prazo) e seção 10 |
| Uma única linha de negócio | ATENDE | Só pos; Graduação aparece só como contexto (S15) e Livres e Eventos com "não somar" |

### 1.2 Auditoria conformidade-educacional

| Item | Resultado | Observação |
|---|---|---|
| Nome, modalidade, carga, duração e turno batem com o catálogo | NÃO ATENDE | Afirmações erradas sobre o catálogo: linha 218 (menor ticket), linhas 303 e 447 (faixa de parcelas). Ver problemas 3 e 4 |
| Status "aberto" (ou sem chamada para inscrição) | ATENDE | Não há chamada; turmas "verificar" identificadas como tal |
| Modalidade clara e correta | ATENDE | 68632 presencial, 586 EAD em "verificar", demais semipresenciais, conforme catálogo. Recomendação: em "presencial integral" (linha 212) tirar "integral", que confunde com turno |
| Graduação: ato regulatório do catálogo | NÃO SE APLICA | Sem ato de graduação citado |
| Pós lato sensu: não diz "reconhecida pelo MEC" | ATENDE COM CORREÇÃO | Não afirma. Mas escreve por extenso a frase de certificação ligada ao MEC (linhas 39 e 303), proibida pelo briefing. Ver problema 5 |
| Curso livre: deixa claro que não confere diploma | NÃO SE APLICA | Linha pos |
| Nota MEC com fonte oficial | ATENDE | Nenhuma nota MEC citada |
| Nenhuma promessa de emprego, salário ou sucesso | ATENDE | Salários usados só para capacidade de pagamento |
| Empregabilidade ou satisfação com fonte, período e amostra | NÃO SE APLICA | Nenhum dado desse tipo |
| Superlativos só com fonte | ATENDE | "Referência mundial" da ficha 352 apontada como proibida em peça (linha 414) |
| Comparação com concorrente objetiva e não depreciativa | ATENDE | Comparação de taxa e preço com fonte; mas o lado Ufape (R$ 100,00) não vem do catálogo (problema 1) |
| Preço completo, sem esconder matrícula | ATENDE | Total, parcelas e matrícula citados juntos |
| Bolsa e desconto com regra, público e prazo | NÃO ATENDE | Diz que as regras da bolsa estão [PREENCHER] (linhas 153, 176, 304, 319, 485), mas contexto/pos-graduacao.md (atualizado em 26/10/2026) já traz as regras lidas nas 22 páginas. Descontos de 359 (12%) e 352 (10%) citados sem [CONFIRMAR NO CATÁLOGO] na linha 180. Ver problemas 2 e 8 |
| Urgência real | ATENDE | "10 primeiros" tratado como alerta (linha 180) |
| Prouni, Fies ou financiamento | NÃO SE APLICA | Não citados |
| Autorização de uso de depoimentos, fotos e vídeos | ATENDE | Docentes só em contagem, com [CONFIRMAR autorização] (linha 330) |
| Menores de idade | NÃO SE APLICA | |
| Formulários com finalidade e política de privacidade | NÃO SE APLICA | Sem formulário |
| WhatsApp e e-mail só com consentimento | NÃO SE APLICA | Sem envio |
| Nenhum dado pessoal | ATENDE | |
| Políticas de Meta e Google, página de destino, itens de anúncio | NÃO SE APLICA | Não é anúncio nem página |

### 1.3 Conferência com o catálogo

Conferidos e corretos: 30 turmas abertas (26 SP, 4 Goiânia: 289, 68632, 68609, 68623); 22 provas abertas e a distribuição por área (linha 177); 9 turmas I; distribuição de inícios (6, 5, 9 e 10, linha 164); preços, cargas, turmas e datas de todas as turmas citadas nas seções 8 e 10; 707 como terceiro maior valor aberto; 352 como segundo; quatro provas sem turma de destino (68652, 68649, 68653, 68655); contagem de dias (4, 12 e 33 dias).

### 1.4 Problemas que exigem correção

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 30, 153, 175, 303, 310, 446 | Inscrição da prova de bolsa de R$ 100,00 tratada como dado de curso, mas não está no catálogo (seção 3 do catálogo não tem preço) | Manter o valor só com a marca [CONFIRMAR NO CATÁLOGO] e a fonte "contexto/pos-graduacao.md, site", até a Ufape incluir o preço da prova no catálogo |
| 2 | Linhas 153, 176, 304, 319, 485 | Afirma que as regras da bolsa estão vazias ([PREENCHER]); contexto/pos-graduacao.md, linha 17, já traz: 11 bolsas por prova (2 de 50% monitoria, 4 de 25%, 5 de 10%), nota de corte 7,0, não acumulativa, matrícula em 10 dias úteis e turma mínima de 15 na página da prova. Contradiz também insights-pos (seção 4) | Atualizar para "regras publicadas nas páginas das provas (contexto/pos-graduacao.md), ainda fora do catálogo [CONFIRMAR NO CATÁLOGO]"; manter [CONFIRMAR] só para a turma de destino. Na seção 3 (linha 119), registrar que, com mínimo de 15 (página da prova), a conta cairia para 450 [CONFIRMAR] |
| 3 | Linha 218 (A5) | "Ultrassonografia tem o menor ticket de pós da Ufape (R$ 14.960,00 a R$ 16.456,00)" está errado: 719 (R$ 12.000,00) e 586 (R$ 14.130,00) são menores, e o próprio arquivo diz isso na linha 369 | Trocar por "68629 (R$ 16.456,00) é o menor total entre as pós veterinárias abertas; só 719 (IA na Saúde, R$ 12.000,00) é menor". 706 (R$ 14.960,00) está em "verificar" |
| 4 | Linhas 303 e 447 contra a linha 151 | Faixa de parcelas começa em R$ 623,33 (706, status "verificar") na SWOT e na Lista 1, e em R$ 666,67 (719) na seção 5, que fala de turmas abertas | Usar "R$ 666,67 a R$ 1.673,08 nas turmas abertas" nas três linhas, ou deixar explícito "catálogo inteiro" quando incluir 706 |
| 5 | Linhas 39 e 303 | Frase de certificação ligada ao MEC escrita por extenso, em caixa alta. O briefing proíbe escrever a frase | Substituir por "frase de certificação ligada ao MEC" |
| 6 | Linhas 29, 69, 265, 305; 37, 77, 78, 156, 461; 265, 511; lista de fontes | Fontes sem data de publicação ou sem fonte primária sustentam a oportunidade 1 (Felinos) e o risco 1 (preço e renda) | Para S9, S11 e S12: incluir data de publicação e endereço, ou marcar o número como [SUPOSIÇÃO] e a conclusão como "a validar". Para S6, S10, S18, S21, S24, S26 e S27: incluir o ano de publicação na lista |
| 7 | Linhas 258, 260, 476 | O evento de 20/11/2026 é chamado de "simpósio"; no catálogo, no briefing e no plano do cmo o nome oficial é "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia" | Usar o nome do catálogo (ou "Workshop de Neuromonitorização") |
| 8 | Linhas 180 e 424 | Descontos de 359 (12%) e 352 (10%) e turma mínima de 15 da turma 60 citados só como "(ficha)", sem a marca exigida para dado fora do catálogo | Acrescentar [CONFIRMAR NO CATÁLOGO] nessas linhas (a Lista 3 já lista os descontos, mas a marca precisa estar no texto) |

Ajustes recomendados (não bloqueantes): nomes "Pós Graduação em" nos títulos das seções 341 e 333 (linhas 332 e 343) copiados do catálogo; em texto de trabalho, preferir o padrão "Pós-graduação em" de contexto/pos-graduacao.md. Harmonizar o universo de médicos veterinários com pesquisa-livres (ver seção 5, contradição C1).

### 1.5 Veredito

**CORRIGIR.** Falha no item 1 da auditoria 01 (fontes não datadas) e nos itens de dados do curso e de bolsa e desconto da conformidade. Volta para o agente pesquisa-de-mercado.

---

## 2. pesquisa-de-mercado-livres-2026-10-26.md

### 2.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | NÃO ATENDE | Afirmações sem endereço nem data na Lista A: agrolink (linha 303); Lusófona, 61 h (linha 227); congresso de endocrinologia em SP em 2026 (linha 229, tema que não aparece na seção 9); congresso da Anclivepa de silvestres em 2025 (linha 236); Emagister Colômbia (linha 167); Cuánto me Cuesta (linha 170); Startupi 2021 (linha 148); "agenda de terceiros" do Congresso Brasileiro da Anclivepa (linha 197); Guia da Carreira de Vitória (linha 142); série do Animal Health Science Ecosystem (só há o endereço do CINUV) |
| Suposições marcadas com [SUPOSIÇÃO] | ATENDE | Lista B completa |
| Citações de candidatos e alunos literais e anonimizadas | NÃO SE APLICA | Não há citação |
| Dados de concorrentes públicos e datados | NÃO ATENDE | Mesmos casos do item 1, mais superlativos sobre a Anclivepa sem fonte (linhas 139 e 197) |
| Números de mercado com faixa mínima e máxima | ATENDE | Seções 3.1 e 13 |
| Persona baseada em alunos e candidatos reais | NÃO SE APLICA | G1 a G6 marcados como [SUPOSIÇÃO], sem persona |
| Conclusões terminam em ações | ATENDE | Seções 14 ("O que exige decisão agora") e 15 |
| Uma única linha de negócio | ATENDE COM RESSALVA | Cobre Livres e Eventos (linha 4), com números separados. A etapa 1.1 do plano do cmo lista só pos e livres; a área A12 do plano já junta o evento. Recomendação: na próxima versão, levar as seções 8, 9 e 13.2 para um arquivo da linha eventos. Os dados de prova de bolsa (Pós) usados como "degrau" (linhas 210, 245, 293) precisam vir marcados como dado de outra linha |

### 2.2 Auditoria conformidade-educacional

| Item | Resultado | Observação |
|---|---|---|
| Nome, modalidade, carga, duração e turno batem com o catálogo | NÃO ATENDE | Faixas e máximos errados (linhas 103, 224, 248) e modalidade divergente (problema 3) |
| Status "aberto" (ou sem chamada) | ATENDE | Itens em "verificar" identificados |
| Modalidade clara e correta | NÃO ATENDE | 573 e 560 são "Semipresencial" no catálogo e entram como "Presencial hands-on" (linhas 80, 95, 232, 295); 68618 tem modalidade em branco no catálogo e é tratado como presencial |
| Graduação: ato regulatório | NÃO SE APLICA | |
| Pós lato sensu: não diz "reconhecida pelo MEC" | ATENDE COM CORREÇÃO | Linha 106 escreve por extenso a frase de certificação ligada ao MEC (como alerta). Ver problema 9 |
| Curso livre: deixa claro que não confere diploma | NÃO ATENDE | A SWOT (linha 311) põe o credenciamento institucional (portarias do MEC) como força dos Cursos Livres, o que induz a ligar curso livre à regulação de graduação e pós |
| Nota MEC com fonte oficial | ATENDE | Nenhuma nota |
| Sem promessa de emprego ou sucesso | ATENDE | |
| Empregabilidade ou satisfação com fonte | NÃO SE APLICA | |
| Superlativos só com fonte | NÃO ATENDE | "Dona do maior congresso do segmento" (linha 139) e "Congresso do maior evento da categoria" (linha 197), sem fonte |
| Comparação com concorrente objetiva | ATENDE COM CORREÇÃO | Objetiva, mas o lado Ufape (R$ 100,00 da prova) é atribuído ao catálogo sem estar nele |
| Preço completo | ATENDE | À vista e parcelado mostrados; 461 com a diferença de 20% apontada |
| Bolsa e desconto com regra | ATENDE COM RESSALVA | Usa a prova de bolsa (Pós) sem as regras; ver problema 1 |
| Urgência real | ATENDE | "30 vagas" do workshop é número do catálogo |
| Prouni, Fies ou financiamento | NÃO SE APLICA | |
| Autorização de uso de imagem e voz | ATENDE | Docentes do workshop com [CONFIRMAR autorização] |
| Menores de idade | NÃO SE APLICA | |
| Formulários com finalidade | ATENDE COM RECOMENDAÇÃO | A proposta de "pergunta de origem" na prova de bolsa (linha 253) já pede aprovação humana; acrescentar que o formulário precisa informar a finalidade e ter link para a política de privacidade |
| WhatsApp e e-mail com consentimento | NÃO SE APLICA | |
| Nenhum dado pessoal | ATENDE | |
| Plataformas e anúncios | NÃO SE APLICA | |

### 2.3 Conferência com o catálogo

Conferidos e corretos: 7 presenciais abertos com data de 32 e 20 em "verificar"; 22 online contínuos, 13 minicursos, 10 grupos (2 com data, 8 contínuos); faixas de 96,00 a 4.060,80, 185,00 a 300,00, 100,00 a 734,00 e 250,00 a 1.000,00; preços e cargas de 573, 68614, 623, 68637, 68618, 68638, 560, 347, 340, 501, 602, 575, 605, 95, 488, 131, 137, 641; dados do workshop de 20/11/2026 (16 h, 30 vagas, R$ 1.250,00, R$ 450,00, cupom SIMPNEUROMONIT); 700 e 202.

### 2.4 Problemas que exigem correção

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 139, 210, 245, 293 | "Taxa da prova de bolsa da Ufape é R$ 100,00 (catálogo, seção 3)": a seção 3 do catálogo não tem preço. Atribuição de fonte falsa, e o dado é da linha Pós | Corrigir a fonte para "contexto/pos-graduacao.md, site" com [CONFIRMAR NO CATÁLOGO] e indicar que é dado da linha pos |
| 2 | Linha 103 | Faixa "curso médio de 12 a 54 h (R$ 420,00 a R$ 1.440,00)" não bate com o catálogo: 542 tem 12 h e custa R$ 165,00; 103 tem 48 h e custa R$ 1.488,00 | Refazer a faixa a partir do catálogo (por exemplo, de R$ 165,00 a R$ 1.488,00 para 8 a 54 h) ou listar os códigos usados |
| 3 | Linhas 80, 95, 232, 295 | 573 e 560 classificados como presencial; no catálogo são "Semipresencial" (573 com a grafia "Semiprensecial"). 68618 sem modalidade no catálogo | Separar "presencial" e "semipresencial com módulos presenciais"; 68618 com [CONFIRMAR NO CATÁLOGO] na modalidade. O próprio insights-livres (L-T10) já trata 573 e 560 como semipresenciais |
| 4 | Linha 248 | "Turmas abertas do catálogo (de R$ 12.000,00 a R$ 48.780,00)": o máximo aberto é R$ 48.400,00 (657); R$ 48.780,00 é 677, em "verificar". A conta "de 2 a 100 vezes" também está errada (R$ 12.000,00 / R$ 5.220,00 é cerca de 2,3; R$ 48.400,00 / R$ 96,00 é cerca de 504) | Usar R$ 12.000,00 a R$ 48.400,00 e corrigir a razão para "de cerca de 2 a cerca de 500 vezes", ou retirar a conta |
| 5 | Linha 224 (A2) | "Hands-on é a oferta de maior ticket entre os abertos com data": 560 (R$ 2.950,00) é maior que 573 (R$ 2.350,00) | Trocar por "573 é o maior ticket entre os itens com data da área A2" |
| 6 | Linhas 139 e 197 | Superlativos sobre a Anclivepa ("maior congresso do segmento", "maior evento da categoria") sem fonte | Incluir fonte com data ou retirar o superlativo |
| 7 | Linhas 142, 148, 167, 170, 197, 227, 229, 236, 303 e seção 9 | Afirmações externas sem endereço nem data na Lista A (ver 2.1, item 1) | Incluir endereço e data de cada uma na Lista A, ou marcar a afirmação como [SUPOSIÇÃO]. Para o congresso de endocrinologia (linha 229), conferir: o tema não aparece na lista da seção 9 |
| 8 | Linha 311 | Credenciamento institucional pelas portarias citado como força dos Cursos Livres | Retirar da SWOT de Livres, ou acrescentar que curso livre não confere diploma nem equivale a graduação ou pós e que o credenciamento não se aplica a ele |
| 9 | Linha 106 | Frase de certificação ligada ao MEC escrita por extenso | Substituir por "frase de certificação ligada ao MEC" |
| 10 | Linhas 15, 40, 41, 266 contra pesquisa-pos (linhas 51 a 53, 110) | Universo de médicos veterinários diferente entre os dois arquivos da mesma etapa (ver contradição C1) | Harmonizar com pesquisa-pos: mesma tabela de fontes, com o critério de cada número (registrados, em atividade) |

Ajustes recomendados (não bloqueantes): linha 98, o parêntese inclui "sem venda", que não é status "verificar"; linha 110, 669 não tem "na Clínica Médica" no nome; 616 (aberto, 05/12/2026) não aparece na contagem por formato da seção 4; linha 96, a data de 22/10/2026 da Langford já passou; Lista A item 9 diz que a taxa de R$ 350,00 vale também para a pós em Cardiologia 2026, o que pesquisa-pos não afirma (conferir no edital S22).

### 2.5 Veredito

**CORRIGIR.** Falha nos itens 1 e 4 da auditoria 01 e nos itens de dados do curso, modalidade, curso livre e superlativos da conformidade. Volta para o agente pesquisa-de-mercado.

---

## 3. insights-de-alunos-pos-2026-10-26.md

### 3.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | ATENDE | Cada hipótese aponta a ficha e o campo; catálogo de 26/10/2026 |
| Suposições marcadas com [SUPOSIÇÃO] | ATENDE | Todas as hipóteses marcadas, uma a uma |
| Citações literais e anonimizadas | ATENDE COM RECOMENDAÇÃO | Não há voz real, e o arquivo diz isso. Trechos entre aspas vêm de duas origens: texto literal das fichas e perguntas formuladas pelo agente (por exemplo H-T2, "Pago antes de saber se fecha?"). Recomendação: distinguir as formulações do agente (por exemplo, prefixo "pergunta provável:") para que a etapa de mensagens não as trate como voz do cliente |
| Dados de concorrentes públicos e datados | NÃO SE APLICA | |
| Números de mercado com faixa | NÃO SE APLICA | |
| Persona baseada em alunos reais | NÃO SE APLICA | Não constrói persona; declara que não há voz real |
| Conclusões terminam em ações | ATENDE | Seção 10 e pedido de dados (seção 8) |
| Uma única linha | ATENDE | pos; referências a Livres (720, 560, 603, 590, 604) só como fronteira |

### 3.2 Auditoria conformidade-educacional

| Item | Resultado | Observação |
|---|---|---|
| Dados do curso batem com o catálogo | ATENDE COM CORREÇÃO | Preços, cargas, turmas e datas conferidos (H-T10, H-A1.1, H-A1.4, H-A2.3, H-A3.3, H-A4.3, H-A5.4, H-A9.2, H-A10.3, H-A12.2). Problema só na atribuição do R$ 100,00 (problema 1) |
| Status "aberto" | ATENDE | Sem chamada |
| Modalidade clara | ATENDE | H-T7 aponta a variação de grafia |
| Graduação: ato regulatório | NÃO SE APLICA | |
| Pós lato sensu: não diz "reconhecida pelo MEC" | ATENDE | Usa sempre "frase de certificação ligada ao MEC" |
| Curso livre | NÃO SE APLICA | |
| Nota MEC | ATENDE | Nenhuma |
| Promessas | ATENDE | Roteiro proíbe prometer resultado e afirmar validade |
| Empregabilidade ou satisfação | NÃO SE APLICA | |
| Superlativos | ATENDE | |
| Comparação com concorrente | NÃO SE APLICA | |
| Preço completo | ATENDE | H-T10 com parcelas, total e matrícula |
| Bolsa e desconto com regra | NÃO ATENDE | H-PB8 e a observação da linha 232 dizem que o contexto mantém as regras da bolsa como [PREENCHER]; contexto/pos-graduacao.md (26/10/2026) já traz as regras. Problema 2 |
| Urgência real | ATENDE | H-A1.5 recusa escassez sem número |
| Prouni, Fies | NÃO SE APLICA | |
| Autorização de depoimentos | ATENDE | Seção 7.1: citação só vira peça com autorização registrada |
| Menores de idade | NÃO SE APLICA | |
| Formulários com finalidade | ATENDE | Roteiro com consentimento [CONFIRMAR] com o encarregado de dados |
| WhatsApp e e-mail com consentimento | ATENDE | Nada enviado; pedido de dados com anonimização antes do envio |
| Nenhum dado pessoal | ATENDE | Regra de anonimização detalhada (7.3) |
| Plataformas e anúncios | NÃO SE APLICA | |

### 3.3 Problemas que exigem correção

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 4, linha 219; H-PB2 e H-PB3 (linhas 224 e 225) | "Preço e data vêm de contexto/pos-graduacao.md e do catálogo (inscrição de R$ 100,00 no site)": o catálogo não traz o preço da prova | Fonte: "contexto/pos-graduacao.md, site", com [CONFIRMAR NO CATÁLOGO] |
| 2 | H-PB8 (linha 230) e observação da linha 232 | Diz que o contexto da linha mantém as regras da bolsa vazias; contexto/pos-graduacao.md, linha 17, traz as regras (iguais nas 22 páginas, lidas em 26/10/2026) | Atualizar para "as regras estão no contexto da linha (lidas nas páginas), ainda fora do catálogo [CONFIRMAR NO CATÁLOGO]"; manter a pendência de turma de destino |

Ajustes recomendados (não bloqueantes): H-A3.3 compara 666 com 663 (status "verificar"); a turma aberta equivalente é 68635 (750 h, R$ 33.000,00). Marcar as perguntas formuladas pelo agente (ver 3.1, item 3).

### 3.4 Veredito

**CORRIGIR.** Dois ajustes pontuais de fonte e de regra de bolsa. Volta para o agente insights-de-alunos.

---

## 4. insights-de-alunos-livres-2026-10-26.md

### 4.1 Auditoria 01-qualidade-de-pesquisa

| Item | Resultado | Observação |
|---|---|---|
| Toda afirmação aponta para uma fonte datada | ATENDE | Ficha e campo em cada hipótese; catálogo de 26/10/2026 |
| Suposições marcadas | ATENDE | Todas as hipóteses marcadas |
| Citações literais e anonimizadas | ATENDE COM RECOMENDAÇÃO | Sem voz real; mesma recomendação de insights-pos sobre perguntas formuladas pelo agente entre aspas (por exemplo L-T2) |
| Concorrentes | NÃO SE APLICA | |
| Números de mercado | NÃO SE APLICA | |
| Persona | NÃO SE APLICA | |
| Conclusões terminam em ações | ATENDE | Seção 9 e pedido de dados |
| Uma única linha | ATENDE | livres; Pós só como venda cruzada |

### 4.2 Auditoria conformidade-educacional

| Item | Resultado | Observação |
|---|---|---|
| Dados do curso batem com o catálogo | ATENDE | Conferidos: L-T5 (totais 3.030,00, 1.750,00, 1.230,00, 3.540,00, 1.200,00), L-T11, L-A1.3, L-A1.6, L-A2.4, L-A3.3, L-A4.3 (2.940,00), L-A7.5 (1.599,96), L-A8.2, L-A11.2, L-A13.1, L-A14.3. Dados só de ficha com [CONFIRMAR NO CATÁLOGO] (versão só online de 616, prazos de acesso, vagas) |
| Status "aberto" | ATENDE | 625 e 99 declarados fora do recorte (linha 64) |
| Modalidade clara | ATENDE COM RECOMENDAÇÃO | 616 classificado como "híbrido", termo que não existe no catálogo (modalidade "On-line", local "Presencial e Online"); a divergência já está em L-T10. Recomendação: [CONFIRMAR NO CATÁLOGO] no rótulo |
| Graduação e Pós | NÃO SE APLICA | |
| Curso livre: não confere diploma | ATENDE | L-T16 e roteiro (pergunta 9) |
| Nota MEC | ATENDE | Nenhuma |
| Promessas | ATENDE | L-A14.2: "a squad não promete emprego" |
| Superlativos | ATENDE | |
| Preço completo | ATENDE | |
| Bolsa e desconto | ATENDE | Desconto de 720 e 641 com [CONFIRMAR NO CATÁLOGO] |
| Urgência real | ATENDE | L-A1.4 recusa escassez sem número do catálogo |
| Autorização de depoimentos | ATENDE | Seção 6.1 |
| Formulários com finalidade | ATENDE | Roteiro com consentimento [CONFIRMAR] |
| WhatsApp e e-mail com consentimento | ATENDE | Nada enviado |
| Nenhum dado pessoal | ATENDE | |
| Itens de Prouni, menores, plataformas e anúncios | NÃO SE APLICA | |

### 4.3 Ajustes recomendados (não bloqueantes)

1. Marcar as perguntas formuladas pelo agente entre aspas (por exemplo L-T2, L-T13, L-A1.3) como "pergunta provável", separadas de texto literal das fichas.
2. Rótulo "híbrido" de 616: acrescentar [CONFIRMAR NO CATÁLOGO].
3. Seção 6.2, valor "híbrido" no campo Formato: mesma observação.

### 4.4 Veredito

**APROVADO** para seguir à aprovação humana, com os três ajustes recomendados registrados.

---

## 5. Contradições entre os arquivos

| # | Arquivos | Contradição | Como resolver |
|---|---|---|---|
| C1 | pesquisa-pos (linhas 51 a 53, 110) e pesquisa-livres (linhas 15, 40, 41, 266) | Pós: teto de 154,9 mil a "180 mil ou mais" e "número oficial de 2025 sem fonte". Livres: 182,3 mil em atividade e quase 240 mil registrados (AviNews, 09/09/2025) | Uma tabela única de universo para as duas linhas, com critério e data de cada número |
| C2 | pesquisa-pos (linha 56) e pesquisa-livres (linha 46) | 536 cursos e mais de 107 mil vagas (2023) contra mais de 87 mil vagas presenciais (2025) | Não são o mesmo indicador: rotular "vagas totais 2023" e "vagas presenciais 2025" nos dois |
| C3 | pesquisa-pos (linhas 153, 176) e insights-pos (seção 4) | Pesquisa diz regras de bolsa vazias; insights traz números das fichas; o contexto já tem as regras | Problema 2 de pesquisa-pos e problema 2 de insights-pos |
| C4 | pesquisa-pos (linhas 30, 446) e pesquisa-livres (linha 139) | R$ 100,00 atribuído ao "site" num arquivo e ao "catálogo, seção 3" no outro | Fonte única: contexto/pos-graduacao.md (site), com [CONFIRMAR NO CATÁLOGO] |
| C5 | pesquisa-pos (linha 25) e pesquisa-livres (linha 248) | Máximo das turmas abertas: R$ 48.400,00 num, R$ 48.780,00 no outro | R$ 48.400,00 (657) para turmas abertas |
| C6 | pesquisa-livres (linhas 80, 95) e insights-livres (L-T10) | 573 e 560 como presenciais num arquivo e semipresenciais no outro | Seguir o catálogo: semipresencial |
| C7 | pesquisa-pos (linhas 258, 476) e pesquisa-livres (linha 181) | "Simpósio de 20/11" contra o nome oficial de workshop | Nome do catálogo |
| C8 | pesquisa-pos (linha 119) e insights-pos (H-PB5) | Turma mínima de 20 na conta contra mínimo de 15 na página da prova | Registrar as duas e [CONFIRMAR] (já pendente no contexto da linha) |

---

## Resultado consolidado da conformidade (formato do checklist)

- pesquisa-de-mercado-pos: Aprovado ( ) Bloqueado (X). Itens bloqueados: dados do curso, bolsa e desconto (problemas 1 a 4 e 8); frase ligada ao MEC (problema 5).
- pesquisa-de-mercado-livres: Aprovado ( ) Bloqueado (X). Itens bloqueados: dados do curso e modalidade (problemas 2 a 5), curso livre (problema 8), superlativos (problema 6), frase ligada ao MEC (problema 9).
- insights-de-alunos-pos: Aprovado ( ) Bloqueado (X). Item bloqueado: bolsa e desconto e fonte do preço da prova (problemas 1 e 2).
- insights-de-alunos-livres: Aprovado (X) Bloqueado ( ).
- Revisado por: qa-de-marketing (agente). Revisão humana: [pendente, pessoa do marketing].
- Data: 26/10/2026.

## Próximo passo

- pesquisa-de-mercado-pos e pesquisa-de-mercado-livres voltam para o agente pesquisa-de-mercado.
- insights-de-alunos-pos volta para o agente insights-de-alunos.
- insights-de-alunos-livres segue para a aprovação humana.
- Depois da correção, os três arquivos voltam a este QA. Nenhum arquivo revisado foi editado.

---

## Lista 1. Fatos (com fonte)

- 30 turmas de pós abertas (26 SP, 4 Goiânia), 22 provas de bolsa abertas em 27/11/2026 e 9 turmas I: contexto/catalogo-de-cursos.md, seções 2 e 3 (26/10/2026).
- Maior total entre turmas de pós abertas: R$ 48.400,00 (657); maior do catálogo: R$ 48.780,00 (677, "verificar"); menor: R$ 12.000,00 (719): catálogo, seção 2.
- Menor total entre pós veterinárias abertas: R$ 16.456,00 (68629): catálogo, seção 2.
- Menor parcela entre turmas abertas: R$ 666,67 (719, 18x); R$ 623,33 é de 706, em "verificar": catálogo, seção 2.
- 573 e 560 têm modalidade semipresencial; 68618 sem modalidade: catálogo, seções 4.
- 542 (12 h, R$ 165,00) e 103 (48 h, R$ 1.488,00): catálogo, seção 5.
- O catálogo não traz o preço da inscrição da prova de bolsa; o valor de R$ 100,00 está em contexto/pos-graduacao.md (site) e no plano do cmo (seção 2.2).
- Regras da prova de bolsa (11 bolsas, 2 de 50%, 4 de 25%, 5 de 10%, nota de corte 7,0, mínimo de 15 na página da prova): contexto/pos-graduacao.md, linha 17, atualizado em 26/10/2026.
- Nome oficial do evento de 20/11/2026: Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia: catálogo, seção 9, e plano do cmo, seção 2.1.
- A etapa 1.1 do plano do cmo cobre as linhas pos e livres: saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 4.
- O briefing proíbe escrever a frase de certificação ligada ao MEC: docs/execucao-2026-10-26.md.

## Lista 2. Suposições

- [SUPOSIÇÃO] A leitura integral dos quatro arquivos encontrou todas as ocorrências de travessão e meia-risca (não houve busca automática por caractere).
- [SUPOSIÇÃO] Os dados atribuídos às fichas (lotação, descontos, prazos de acesso, regras das provas) estão corretos nas fichas; esta revisão não abriu as fichas.
- [SUPOSIÇÃO] A diferença de regras de bolsa entre os arquivos vem de o contexto ter sido atualizado depois da leitura feita pelos agentes, no mesmo dia.

## Lista 3. Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Preço da inscrição da prova de bolsa (R$ 100,00) e regras das bolsas.
- [CONFIRMAR] Turma de destino das provas 68652, 68649, 68653 e 68655; turma mínima (15 ou 20).
- [CONFIRMAR NO CATÁLOGO] Modalidade de 68618 e de 616; carga horária de 68638.
- [CONFIRMAR] Data de publicação e endereço das fontes externas listadas nos problemas 6 (pesquisa-pos) e 7 (pesquisa-livres).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação para pós e para curso livre.
- [PREENCHER] Responsável pela aprovação de peças em contexto/ufape-geral.md (tabela "Regras de aprovação" vazia).

## Fontes desta revisão

docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/catalogo-de-cursos.md; auditorias/01-qualidade-de-pesquisa.md; auditorias/conformidade-educacional.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 4); os quatro arquivos revisados em saidas/01-inteligencia-de-mercado/.
