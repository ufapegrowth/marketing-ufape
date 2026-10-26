# QA de marketing: cinco saídas do departamento 03 (SEO e Busca por IA)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (pos e livres, com a parte de eventos coberta pelos arquivos de livres)
- Data: 26/10/2026
- Status: rascunho de QA. Nada foi publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md
  - contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seções 1 a 9)
  - auditorias/03-busca.md
  - auditorias/conformidade-educacional.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 4)
  - Revisados: saidas/03-seo-e-busca/lacunas-de-conteudo-pos-2026-10-26.md, lacunas-de-conteudo-livres-2026-10-26.md, links-e-autoridade-pos-2026-10-26.md, pesquisa-de-palavras-chave-pos-2026-10-26.md e pesquisa-de-palavras-chave-livres-2026-10-26.md (lidos inteiros)
- Não abri faculdade.ufape.com.br nem nenhuma página externa. As fichas de contexto/cursos/ não foram reabertas: o que os arquivos atribuem às fichas foi conferido só quanto à marcação [CONFIRMAR NO CATÁLOGO].

## Resumo dos vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| lacunas-de-conteudo-pos-2026-10-26.md | **corrigir** | Contagem de páginas de Clínica Cirúrgica diverge do catálogo; "presencial integral" e "100% presencial" sem base no catálogo; nomes "Pós em" em FAQ e títulos propostos; rótulo errado de 669 e 455 |
| lacunas-de-conteudo-livres-2026-10-26.md | **corrigir** | 616 (online no catálogo) e 573 e 560 (semipresenciais) agrupados como "presencial"; cluster de ventilação com uma palavra para duas páginas; carga horária de 202 dada como fato |
| links-e-autoridade-pos-2026-10-26.md | **corrigir** | Rascunho de imprensa diz "22 especialidades" (são 22 provas em 19 especialidades); texto de bolsa sem regra completa; âncora e título com "Pós em"; afirmações externas sem fonte |
| pesquisa-de-palavras-chave-pos-2026-10-26.md | **corrigir** | "Menor ticket da linha" falso; "21 especialidades abertas" errado; descrição de 698 promete prova de bolsa que não existe; "integral"; H2 com "Pós em"; títulos com barra vertical quebram as tabelas |
| pesquisa-de-palavras-chave-livres-2026-10-26.md | **corrigir** | Blocos citáveis sem total no cartão; bloco e FAQ de 573 sem a frase de curso livre; contagem "36 de 47" contínuos contradiz a própria seção 6; links para a Pós com "Pós em" |

Regra aplicada: qualquer item de auditorias/conformidade-educacional.md sem marcação bloqueia o arquivo, e o veredito é corrigir. Todos os cinco têm ao menos um item com falha. Nenhuma das falhas é de certificação ligada ao MEC, de dado pessoal, de travessão ou de "últimas vagas": nesses pontos os cinco estão limpos.

---

## 1. lacunas-de-conteudo-pos-2026-10-26.md

### 1.1 Auditoria 03-busca, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma única palavra-chave alvo por página prioritária | Atende | Pilar único por curso (T3); a palavra é definida na etapa 2.1 |
| 2 | Títulos e descrições únicos | Não se aplica | O arquivo não propõe título nem descrição de SEO; títulos de artigo são distintos |
| 3 | Nenhuma página importante bloqueada | Pendente de dado | Sem rastreamento; remete ao seo-tecnico. Não bloqueia |
| 4 | Nenhum link interno quebrado | Pendente de dado | Idem; propõe 301 de 670 para 68636 |
| 5 | Toda página aponta para o pilar | Atende | Seção 5, "Ligações internas" |
| 6 | Responde à principal pergunta | Atende | Perguntas de IA por área e FAQ padrão T2 |
| 7 | Correções escritas como chamados | Atende em parte | Seção 9 lista pendências com dono implícito; recomendo o formato do seo-tecnico (o que, onde, critério de pronto) |
| 8 | Encerrados redirecionados | Atende | 670, 654 e Internação por 301 |
| 9 | Dados de curso batem com o catálogo | **Falha** | Ver itens 1, 2 e 4 da lista de correções |
| 10 | Bloco citável, FAQ real e marcação | Atende | T2 e FAQ por área; marcação remete ao seo-tecnico |
| 11 | Conteúdo sem JavaScript | Pendente de dado | SEO-05 do seo-tecnico |
| 12 | Nenhum resultado de IA sem checagem | Atende | Tudo "conferir manualmente", roteiro na seção 8 |
| 13 | Nenhuma consulta com duas páginas disputando sem correção | Atende | T3 e 301 por código |

### 1.2 Conformidade educacional, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH, duração e turno batem com o catálogo | **Falha** | "presencial integral" e "100% presencial" (68632) não constam no catálogo, que diz só "Presencial" |
| Dados do curso | Status aberto ou sem chamada | Atende | Turmas em "verificar" sem chamada de compra |
| Dados do curso | Modalidade clara e correta | **Falha** | Mesmo ponto do "integral" |
| Regulação | Graduação: ato do catálogo | Não se aplica | |
| Regulação | Pós não diz "reconhecida pelo MEC" | Atende | Nenhuma frase de certificação proposta; FAQ 8 bloqueada |
| Regulação | Curso livre sem diploma | Não se aplica | Livres só por link |
| Regulação | Nota MEC só com fonte | Atende | Nenhuma nota citada |
| Promessas | Sem promessa de emprego, salário ou aprovação | Atende | Vagas da Agrobase tratadas como sinal fraco, fora do argumento de venda |
| Promessas | Empregabilidade com fonte | Atende | Nenhum dado usado |
| Promessas | Superlativos só com fonte | Atende, com ressalva | "o mais alto do recorte entre as de 600 h" (linha 480) é vazio: 707 é a única de 600 h. Retirar |
| Promessas | Comparação com concorrente objetiva | Atende | A8.4 só por critérios, sem ranking |
| Preço | Valor, parcelas e condições completas | Atende | T8 exige parcelas, valor, total e matrícula |
| Preço | Bolsa com regra, público e prazo | Atende | Hub T1 bloqueado até resolver contradições |
| Preço | Urgência real | Atende | Nenhuma |
| Preço | Prouni, Fies | Atende | Não cita |
| Pessoas | Autorização de imagem e voz | Atende | Nenhum docente nomeado; currículos de terceiros marcados [CONFIRMAR] |
| Pessoas | Menores | Não se aplica | |
| Pessoas | Formulários com finalidade e política | Não se aplica | |
| Pessoas | Consentimento de WhatsApp e e-mail | Não se aplica | |
| Pessoas | Nenhum dado pessoal | Atende | |
| Plataformas e anúncios | 8 itens | Não se aplica | Arquivo sem anúncio nem página de destino |

### 1.3 Outras conferências pedidas

- Datas e prazos: 707, 68604 e 68606 em 4, 5 e 12 dias; 68610 em 33 dias. Conferem com o catálogo e com a data de hoje.
- Volume: só qualitativo, marcado [SUPOSIÇÃO]. Os números 952 e 996 são contagem de ofertas de agregador, com fonte, não volume. Atende.
- Fontes externas: aviso de páginas não abertas presente (linha 19). Várias afirmações sem URL nem "sem fonte" (item 5 abaixo).
- Docentes: nenhum nome. Atende. Travessão e meia-risca: nenhum encontrado na leitura completa. "Últimas vagas": nenhum.

### 1.4 Veredito: corrigir

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 262, 268 e 753 (A4.1, "O que a Ufape tem hoje", tabela consolidada) | "Quatro páginas de Clínica Cirúrgica" e "duas páginas de SP e duas de Goiânia". O catálogo tem três: 535 (Goiânia, verificar), 665 (São Paulo, verificar) e 68632 (Goiânia, aberto) | "Três páginas (uma em São Paulo e duas em Goiânia)". Se a quarta vier do seo-tecnico, citar o código e marcar [CONFIRMAR NO CATÁLOGO] |
| 2 | Linhas 277 e 288 (A4, lacuna e artigo 2) e linha 285 (FAQ 2) | "pós presencial integral em Goiânia" e "A Pós de Goiânia é 100% presencial?": "integral" e "100%" não estão no catálogo | Artigo: "Pós-graduação em Clínica Cirúrgica de Cães e Gatos em Goiânia (presencial): como funciona e quem consegue conciliar". FAQ: "A Pós-graduação em Clínica Cirúrgica de Cães e Gatos de Goiânia é presencial? (catálogo: presencial; frequência [CONFIRMAR NO CATÁLOGO])" |
| 3 | Linha 146 (FAQ 4 de A1), linha 193 (FAQ 4 de A2), linhas 460 e 470 (guia e artigo 1 de A8) | Nome fora do padrão em FAQ e título propostos: "A Pós em Anestesiologia (Direto ao ponto)", "a Pós em Cardiologia de SP", "Pós em dermatologia veterinária: EAD, semipresencial ou presencial" | "Pós-graduação em Anestesiologia Veterinária (Direto ao ponto)"; "Pós-graduação em Cardiologia Veterinária de São Paulo e a de Goiânia"; "Pós-graduação em Dermatologia Veterinária: EAD, semipresencial ou presencial, como decidir" |
| 4 | Linha 345 (A6, catálogo) | "grupos de estudos 669, 455 e 721": 669 e 455 são minicursos (seção 5 do catálogo); só 721 é grupo | "minicursos 669 e 455 e grupo de estudos 721". Na linha 391, 103, 104 e 542 são cursos online, não minicursos |
| 5 | Linhas 224, 270, 316, 361, 363, 454, 498, 588, 630, 632, 677 e 825 | Afirmações externas sem URL nem "sem fonte": UESC, Colégio Brasileiro de Cirurgia Veterinária, UFES e UFRGS, parceria com a UniAvan em currículos, ABRAGA, Equalis e lista de bolsa da Anclivepa "não oficial", CBOV e UFRRJ, UFPel e USP, currículos de Neurologia, Anhembi Morumbi, ISVPS | Acrescentar URL e data de consulta (26/10/2026) ou escrever "sem fonte" ao lado de cada uma |
| 6 | Linha 314 (A5) | Recomenda que a primeira frase da página repita "pós em diagnóstico por imagem veterinária" | Usar o nome padrão do catálogo e o termo sem "Pós em": "A Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária é uma especialização em diagnóstico por imagem veterinária..." |
| 7 | Linha 480 (A9) | Superlativo sem conteúdo ("o mais alto do recorte entre as de 600 h") | Retirar |

---

## 2. lacunas-de-conteudo-livres-2026-10-26.md

### 2.1 Auditoria 03-busca, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma palavra-chave alvo por página | Atende em parte | Coluna de palavra por cluster; falha só em CD-VM (item 13) |
| 2 | Títulos e descrições únicos | Não se aplica | Títulos de trabalho de artigo, distintos |
| 3 | Página importante bloqueada | Pendente de dado | SEO-05 |
| 4 | Links internos quebrados | Pendente de dado | |
| 5 | Página aponta para o pilar | Atende | Seção 8.2 |
| 6 | Responde à principal pergunta | Atende | Q01 a Q25 e FAQ por formato |
| 7 | Correções como chamados | Atende | Pedidos H1 a H7 com o que, por que, custo, efeito e como desfazer |
| 8 | Encerrados redirecionados | Atende | 539, 592, 716, 68613 e 715 por 301 |
| 9 | Dados batem com o catálogo | **Falha** | Modalidade de 616, 573 e 560; carga horária de 202 |
| 10 | Bloco citável, FAQ e marcação | Atende | Seção 6.4 e seção 10 |
| 11 | Sem JavaScript | Pendente de dado | |
| 12 | IA sem checagem | Atende | |
| 13 | Duas páginas disputando sem correção | **Falha** | CD-VM: 507 e 68618 com a mesma palavra "curso de ventilação mecânica veterinária" |

### 2.2 Conformidade educacional, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH | **Falha** | 202 com "8 h" como fato (linhas 211 e 564); catálogo sem carga horária |
| Dados do curso | Status aberto ou sem chamada | Atende | Itens em "verificar" fora de cluster |
| Dados do curso | Modalidade clara e correta | **Falha** | 616 está na seção 5 do catálogo (modalidade "On-line"); 573 e 560 são semipresenciais; 68618 sem modalidade. Os quatro entram no grupo "Presencial hands-on" e no hub "cursos práticos presenciais" |
| Regulação | Graduação, Pós | Não se aplica | |
| Regulação | Curso livre sem diploma | Atende | Linha 30 e FAQ 10.1 item 11 |
| Regulação | Nota MEC | Atende | Frase de "selo do MEC" de 68614 tratada como pendência, não repetida |
| Promessas | Quatro itens | Atende | Nenhum tema promete resultado; SciELO citado com fonte |
| Preço | Valor, parcelas e condições | Atende, com ressalva | Linha 431: a tabela dos hubs mostra "à vista e total no cartão"; incluir também número e valor da parcela |
| Preço | Bolsa e desconto | Atende | Cupom SIMPNEUROMONIT com regra para aluno de pós [CONFIRMAR] |
| Preço | Urgência | Atende | Nenhuma; "PROMOÇÃO VÁLIDA POR TEMPO LIMITADO" de 202 não é repetida |
| Preço | Prouni, Fies | Atende | |
| Pessoas | Autorização | Atende | Docentes sem nome |
| Pessoas | Demais itens | Não se aplica ou atende | Nenhum dado pessoal |
| Plataformas e anúncios | 8 itens | Não se aplica | |

### 2.3 Outras conferências pedidas

- Datas e prazos: 573 em 19 dias, neuro-summit em 25, 623 e 68614 em 33, 68665 em 6 (catálogo), 68666 em 30. Conferem. Janela de cancelamento de 68614 em 29/10: cálculo correto.
- Contagens internas: 31 lacunas, 6 P1, 15 P2, 10 P3; 22 com revisão de docente e 5 com regulação. Conferem com a tabela da seção 12.
- Volume: qualitativo e marcado. Fontes externas: S1 a S36 com URL e data; falta o S35 na numeração (sem efeito). Aviso de páginas não abertas presente.
- "Diploma" só aparece em negação ("não confere diploma"). Atende. Travessão, meia-risca e "últimas vagas": nenhum.

### 2.4 Veredito: corrigir

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 64, 121, 405 e 593 (inventário, seção 5.1, CD-F1 e L06) | 616 (online no catálogo, local "Presencial e Online"), 573 e 560 (semipresencial) e 68618 (sem modalidade) classificados como "presencial hands-on" | Renomear o formato para "cursos práticos com data" e mostrar a modalidade do catálogo de cada item; 616 e 68618 só entram no hub depois de [CONFIRMAR NO CATÁLOGO] a modalidade |
| 2 | Linha 411 (CD-VM) | Uma palavra principal para duas páginas (507 e 68618) | Adotar a divisão da pesquisa-de-palavras-chave: 507 "curso online de ventilação mecânica veterinária"; 68618 "curso de ventilação mecânica na anestesia veterinária" |
| 3 | Linhas 211 e 564 (seção 5.6 e FAQ 10.5 item 8) | "202 (R$ 285,00, 8 h...)" e "202: 8 h, turma III" como fato; o catálogo não traz carga horária nem turma de 202 | Marcar "8 h e turma III [CONFIRMAR NO CATÁLOGO]" |
| 4 | Linha 431 (mapa de links, item 3) | Tabela dos hubs sem número e valor da parcela | "preço à vista, número de parcelas e valor da parcela, e total no cartão (cálculo marcado)" |

---

## 3. links-e-autoridade-pos-2026-10-26.md

### 3.1 Auditoria 03-busca, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma palavra-chave alvo por página | Atende | R1: todo link aponta para o pilar único |
| 2 | Títulos e descrições únicos | Não se aplica | |
| 3 | Página importante bloqueada | Pendente de dado | IA-6 e SEO-05 |
| 4 | Links internos quebrados | Atende em parte | Seções 3.4 e 3.5 com 301 e roteiro de medição |
| 5 | Página aponta para o pilar | Atende | Regras R2 a R4 e tabela 3.3 |
| 6 | Responde à principal pergunta | Atende | Seção 9.2 |
| 7 | Correções como chamados | Atende | Travas T-1 a T-8 com quem resolve e o que libera |
| 8 | Encerrados redirecionados | Atende | 670, 68656, provas antigas e turmas sem venda por 301 |
| 9 | Dados batem com o catálogo | **Falha** | "22 especialidades"; códigos 638 e 183 fora do catálogo sem fonte |
| 10 | Bloco citável, FAQ e marcação | Atende | IA-3, IA-4 e IA-8 |
| 11 | Sem JavaScript | Pendente de dado | IA-6 |
| 12 | IA sem checagem | Atende | Nenhuma taxa de citação |
| 13 | Canibalização | Atende | R1, R4 e R9 |

### 3.2 Conformidade educacional, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH | **Falha** | D-3 (assunto e corpo) e ideia 3 da seção 7: "22 especialidades". O catálogo tem 22 provas em 19 especialidades (Anestesiologia, Cardiologia e Clínica Cirúrgica têm prova em São Paulo e em Goiânia) |
| Dados do curso | Status aberto ou sem chamada | Atende | R5 |
| Dados do curso | Modalidade | Atende | IA-2 manda usar a modalidade do catálogo |
| Regulação | Pós sem "reconhecida pelo MEC" | Atende | Nenhuma; e-MEC não usado como prova de pós (O-1) |
| Regulação | Nota MEC | Atende | |
| Promessas | Quatro itens | Atende | "Sem promessa de aprovação"; nada de concorrente nos rascunhos |
| Preço | Valor e condições | Atende | Preço de 68610 com parcelas, total e matrícula |
| Preço | Bolsa com regra, público elegível e prazo | **Falha** | D-1 e D-3 citam 11 bolsas e percentuais sem dizer que a bolsa é não acumulativa e intransferível, sem prazo de matrícula e sem turma de destino. A trava T-3 segura o envio, mas o texto precisa trazer as regras ou remeter a elas |
| Preço | Urgência | Atende | "Nenhuma peça diz últimas vagas" |
| Pessoas | Autorização | Atende | Registro de autorização (5.1); nenhum nome |
| Pessoas | Dado pessoal | Atende | D-7 aponta nome de pessoa aprovada na página 694 sem repeti-lo; o telefone da Anclivepa é institucional |
| Pessoas | Consentimento de e-mail | Não se aplica | Contatos institucionais a redações e portais, só após aprovação |
| Plataformas e anúncios | 8 itens | Não se aplica | |

### 3.3 Outras conferências pedidas

- Prazo da prova: "faltam 32 dias" confere.
- Rascunhos de contato não citam certificação nem concorrente. Atende.
- Fontes externas com URL e data na Lista 1; aviso de páginas não abertas presente (linha 19). Faltam fonte em três pontos (item 4 abaixo).
- Travessão, meia-risca, "últimas vagas": nenhum.

### 3.4 Veredito: corrigir

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 284 e 288 (D-3) e 356 (seção 7, ideia 3) | "22 especialidades" | "22 provas de bolsa em 19 especialidades, em São Paulo e Goiânia" |
| 2 | Linhas 258 (D-1) e 288 (D-3) | Bolsa sem regra completa | Acrescentar: "bolsa não acumulativa e intransferível; regras, prazo de matrícula e turma de destino na página [URL do hub T1]". Só enviar depois de T-3 |
| 3 | Linha 144 (R7), linha 165 (guia e âncora de A8), linha 159 (primeira frase de A5) | Âncora, título de guia e frase de página com "pós em" | Âncoras visíveis: "Pós-graduação em Dermatologia Veterinária semipresencial em São Paulo"; guia: "Pós-graduação em Dermatologia Veterinária: EAD, semipresencial ou presencial"; frase de A5 como no item 6 da seção 1.4 |
| 4 | Linha 398 (IA-4), linha 400 (IA-6), linhas 75, 229, 231 e 235 (CBOV, ABRAGA, CBCV, ANFIVET) | "Course Info não gera mais destaque visual no Google desde 2025" e "muitos robôs de IA não executam JavaScript" sem fonte; entidades "sugeridas pela busca" sem URL | Fonte e data, ou "sem fonte" e [SUPOSIÇÃO] |
| 5 | Linhas 177 e 181 (seção 3.4) | Códigos 638 e 183 não existem no catálogo | Citar a origem (seo-tecnico) e marcar [CONFIRMAR NO CATÁLOGO] |
| 6 | Linhas 166 e 508 | 463, 669, 455 e 721 marcados [CONFIRMAR NO CATÁLOGO] | Já estão no catálogo (seções 5 e 7): 463 Mini Curso em Dermatologia na Clínica Médica de Pequenos Animais, aberto (contínuo), R$ 248,00 à vista ou 5x de R$ 59,52; 669 e 455 minicursos; 721 grupo de estudos. Substituir a marca pelo dado |

---

## 4. pesquisa-de-palavras-chave-pos-2026-10-26.md

### 4.1 Auditoria 03-busca, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma palavra-chave alvo por página | Atende | Tabela consolidada, seção 6 |
| 2 | Títulos e descrições únicos | Atende, com defeito de forma | Títulos únicos por curso, mas a barra vertical dentro das células desloca as colunas (item 4 da lista) |
| 3 | Página importante bloqueada | Pendente de dado | |
| 4 | Links internos quebrados | Pendente de dado | |
| 5 | Página aponta para o pilar | Atende | "Pilar e apoio" por área |
| 6 | Responde à principal pergunta | Atende | Perguntas por área e bloco citável |
| 7 | Correções como chamados | Atende em parte | Seção 9 lista pendências sem dono nem critério de pronto |
| 8 | Encerrados redirecionados | Atende | 654 e 701 por 301; 68656 sem palavra |
| 9 | Dados batem com o catálogo | **Falha** | Itens 1 a 3, 5 e 7 da lista |
| 10 | Bloco citável, FAQ e marcação | Atende | Molde com campos do catálogo |
| 11 | Sem JavaScript | Pendente de dado | |
| 12 | IA sem checagem | Atende | |
| 13 | Canibalização | Atende | Página única e 301 ou canonical |

### 4.2 Conformidade educacional, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH | **Falha** | "Única pós presencial integral" (68632); "21 especialidades abertas" |
| Dados do curso | Status | Atende | 650, 653, 68612, 677 e Odontologia sem compra |
| Dados do curso | Modalidade | **Falha** | "integral" |
| Regulação | Pós sem "reconhecida pelo MEC" | Atende | Nenhum termo nem H2 de certificação |
| Regulação | Nota MEC | Atende | |
| Promessas | Superlativos só com fonte | **Falha** | "Menor ticket da linha" para 68629 (R$ 16.456,00) é falso: 719 custa R$ 12.000,00. Também em Q5.4 |
| Promessas | Demais itens | Atende | "Sem promessa de renda ou emprego" |
| Preço | Valor e condições | Atende | Parcelas, total e matrícula do catálogo |
| Preço | Bolsa com regra, público e prazo | Atende, com ressalva | Bloco citável do hub (linha 982) só sai depois de confirmar; acrescentar "não acumulativa e intransferível" e a turma de destino |
| Preço | Urgência | Atende | |
| Pessoas | Todos | Atende ou não se aplica | |
| Plataformas | Página de destino entrega o que promete | **Falha** | Descrição de 698 (linha 224) diz "Veja módulos, turma e prova de bolsa", mas não há prova de Ecocardiografia no catálogo |
| Anúncios | Estrutura do Google (seção 5.3) | Atende | Sem urgência falsa; termo de concorrente não ativado; negativas para separar da UFAPE de Pernambuco |

### 4.3 Outras conferências pedidas

- Códigos, datas, CH, preços e status das tabelas de recorte conferidos com o catálogo: batem (698 em 28/11/2026, 370 h; 289 em 20/03/2027; 68629 com matrícula de R$ 350,00; 68628 com R$ 38.940,00; 707 com R$ 47.700,00; 677 com o maior preço; Goiânia com 289, 68632, 68609 e 68623; 3 provas em Goiânia).
- Padrão de nome em título e H1: atende em todos os briefings, inclusive na correção de 333, 341, 68629 e 719. Exceção em H2 (item 6).
- Volume: "Volume (est.)" qualitativo; a nota D (20, 14, 8) é conversão declarada do sinal qualitativo e marcada [SUPOSIÇÃO]. Atende.
- Fontes externas com URL na seção "Fontes"; aviso de páginas não abertas presente (linha 17).
- Travessão, meia-risca, "últimas vagas": nenhum.

### 4.4 Veredito: corrigir

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 305 (K5.3), 326 (Q5.4) e 1118 (top 10, item 6) | "Menor ticket da linha" | "Menor ticket da área A5" (68629, 24x de R$ 685,67, R$ 16.456,00, matrícula de R$ 350,00) |
| 2 | Linha 1015 (G3) e linha 1124 | "21 especialidades abertas" e "60 em 12 especialidades" | 22 provas em 19 especialidades; sem as 4 sem destino, 18 provas em 15 especialidades. Recontar ou retirar o número da linha 1124 |
| 3 | Linha 224 (briefing de 698) | Descrição promete prova de bolsa que não existe para Ecocardiografia | "Veja módulos, turma e investimento". Se a prova de Cardiologia (68641 e 68642) valer para 698, [CONFIRMAR NO CATÁLOGO] antes |
| 4 | Linhas 224 a 227, 283, 342 e 343, 402 a 404, 459, 518 a 520, 575 e 576, 636 a 639, 693, 749, 802, 854 e 855, 954 a 959 e 978 | Título "Pós-graduação em X \| Faculdade UFAPE" dentro de célula de tabela: a barra vertical cria uma coluna a mais e empurra a descrição para a coluna H1 | Escapar a barra ("\|") ou trocar por vírgula no texto da tabela, com nota de que o título final usa a barra |
| 5 | Linhas 130 (KT17), 599 (K4.2) e 627 | "Única pós presencial integral do recorte" e artigo "pós presencial integral em Goiânia" | "Única pós com modalidade presencial no recorte (catálogo)"; frequência e jornada [CONFIRMAR NO CATÁLOGO] |
| 6 | Linha 693 (H2 de Oncologia) e linha 58 (regra 2.2) | H2 "Pós em oncologia ou curso de eletroquimioterapia"; a regra 2.2 libera "Pós em" em texto corrido e FAQ, o que contraria contexto/pos-graduacao.md ("Nunca 'Pós em'" em títulos, peças, anúncios e páginas) | H2: "Pós-graduação em Oncologia Veterinária ou curso de eletroquimioterapia". Regra: "Pós em" só em listas de palavras-chave e em palavras de grupo de anúncio, nunca em texto visível |
| 7 | Linha 598 (K4.1) | "Hoje 4 páginas de mesmo nome" | Três no catálogo (535, 665 e 68632), como no item 1 da seção 1.4 |
| 8 | Linhas 417 e 453 (A6) | "grupos de estudos 669, 455 e 721" | "minicursos 669 e 455 e grupo de estudos 721" |
| 9 | Linhas 489 (K1.10), 610 (K4.13), 776 (K12.9), 879 e 880 (K9.7 e K9.8) | UFF, USP, CBCV, ABNV, UFRRJ e CBOV sem URL | Fonte e data, ou "sem fonte" |
| 10 | Linha 24 | "Cada área tem de 11 a 14 termos": A9, A12 e A13 têm 10 | "de 10 a 15 termos" |

---

## 5. pesquisa-de-palavras-chave-livres-2026-10-26.md

### 5.1 Auditoria 03-busca, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma palavra-chave alvo por página | Atende | Seção 10 e decisões de canibalização (8.2) |
| 2 | Títulos e descrições únicos | Atende | Seção 9, com contagem de caracteres |
| 3 | Página importante bloqueada | Pendente de dado | |
| 4 | Links internos quebrados | Pendente de dado | |
| 5 | Página aponta para o pilar | Atende | Seção 8.3 |
| 6 | Responde à principal pergunta | Atende | 67 perguntas e FAQ por página |
| 7 | Correções como chamados | Atende | Pedidos H1 a H9 |
| 8 | Encerrados redirecionados | Atende | Remete às duplicatas e 301 do arquivo de lacunas |
| 9 | Dados batem com o catálogo | **Falha** | Grupo "curso prático em São Paulo" com 616 e 573 (item 4 da lista); contagem de contínuos |
| 10 | Bloco citável, FAQ e marcação | Atende | Seção 9 |
| 11 | Sem JavaScript | Pendente de dado | |
| 12 | IA sem checagem | Atende | |
| 13 | Canibalização | Atende | CD-VM resolvido com duas palavras |

### 5.2 Conformidade educacional, item por item

| Bloco | Item | Resultado | Observação |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH | Atende, com ressalva | 202 e 616 corretamente marcados [CONFIRMAR NO CATÁLOGO] |
| Dados do curso | Status | Atende | 68634 só depois da correção da loja |
| Dados do curso | Modalidade | **Falha** | Linha 212: grupo "curso prático em São Paulo" inclui 616 (online no catálogo) e 573 (semipresencial) como presenciais |
| Regulação | Curso livre sem diploma | **Falha** | Blocos de 68614 e 623 trazem "não confere diploma", mas o de 573 (linha 618) e os de 68665 e 68666 (linhas 684 e 700) não, e a FAQ de 573 (linha 619) não tem a pergunta de certificado |
| Regulação | Nota MEC | Atende | IA47 bloqueada; selo do MEC de 68614 não repetido |
| Promessas | Quatro itens | Atende | 488 "não prometer aprovação nem título" |
| Preço | Valor, parcelas e condições completas | **Falha** | Blocos citáveis de 573 (linha 618), 68614 (linha 635) e 623 (linha 652) mostram à vista e parcela, sem o total no cartão, que contexto/cursos-livres.md exige quando é diferente (R$ 3.030,00; R$ 1.750,00; R$ 1.230,00) |
| Preço | Bolsa e desconto | Atende | Cupom com regra a confirmar |
| Preço | Urgência | Atende | "30 vagas" é o total do catálogo, sem escassez |
| Pessoas | Autorização e dados | Atende | Nenhum docente nomeado; nenhum dado pessoal |
| Plataformas e anúncios | 8 itens | Não se aplica | |

### 5.3 Outras conferências pedidas

- Datas, preços e CH da seção 9 conferidos: 573 (R$ 2.350,00 ou 10x de R$ 303,00; 28 h; 14/11/2026), 68614 (R$ 1.250,00 ou 10x de R$ 175,00; 12 h; presencial; 28/11/2026), 623 (R$ 890,00 ou 6x de R$ 205,00; 12 h), neuro-summit (16 h, 30 vagas, R$ 1.250,00 e R$ 450,00, cupom de 20%, Av. Tiradentes, 960), 68665 e 68666 (R$ 100,00). Batem.
- Volume qualitativo e marcado; fontes W01 a W24 com URL e data; aviso de páginas não abertas presente (linha 8).
- Travessão, meia-risca, "últimas vagas": nenhum.

### 5.4 Veredito: corrigir

| # | Linha ou seção | Problema | Correção proposta |
|---|---|---|---|
| 1 | Linhas 618, 635 e 652 | Bloco citável sem total no cartão | Acrescentar "(total de R$ 3.030,00 no cartão)", "(R$ 1.750,00)" e "(R$ 1.230,00)", marcados como cálculo |
| 2 | Linhas 618 e 619 (573); 684 e 700 (68665 e 68666) | Sem a frase de curso livre | Acrescentar "Curso livre: não confere diploma nem equivale a pós-graduação." ao bloco ou à FAQ de cada página |
| 3 | Linhas 399 e 414 | "47 contínuos, dos quais 36 têm palavra; 11 restantes", com 641 como exemplo. A seção 6 dá palavra aos 47 (contagem por área: 8, 3, 7, 2, 1, 3, 7, 4, 1, 3, 1, 5 e 2), e 641 não está entre os contínuos | "Os 47 contínuos têm palavra nesta seção"; retirar o exemplo de 641 ou mover a regra 6.17 para itens novos |
| 4 | Linha 212 (seção 5.1, grupo 2) | 616 e 573 tratados como presenciais | Mostrar a modalidade do catálogo; 616 [CONFIRMAR NO CATÁLOGO] (o próprio arquivo já aponta a contradição na linha 276) |
| 5 | Linhas 621, 638, 655 e 671 | Links de "próximo passo" com "Pós em Ecocardiografia", "Pós em Dermatologia Veterinária", "Pós em Gastroenterologia Veterinária", "Pós em Anestesiologia Avançada" | Nome padrão: "Pós-graduação em Ecocardiografia", "Pós-graduação em Dermatologia Veterinária", "Pós-graduação em Gastroenterologia Veterinária", "Pós-graduação em Anestesiologia Avançada", "Pós-graduação em Neurologia e Neurocirurgia Veterinária" |

---

## 6. Consistência entre os cinco arquivos e com o plano do cmo

| # | Tema | O que está consistente | O que diverge | Correção |
|---|---|---|---|---|
| 1 | Áreas A1 a A14 | Os cinco usam as 14 áreas e os itens da seção 2.3 do plano (provas por área, 616 em A1, 68665 e 68618 em A2, 68638 e 700 em A3, 202 em A11, neuro-summit em A12, 541, 95 e 68655 em A14) | Nada | |
| 2 | Onda 1 | Pós 707, 68604, 68606, 698, 68610 e 68608; Livres 573, 68614, 623 e 68637; grupos 68665 e 68666; workshop de 20 e 21/11; 22 provas. 68634 entra só com a correção da loja, como no item 7 da seção 2.1 do plano | Nada | |
| 3 | Prazos | 4, 5, 6, 12, 19, 25, 30, 32 e 33 dias, iguais em todos e ao plano | Nada | |
| 4 | Provas sem destino e 68656 | 68652, 68649, 68653 e 68655 sem destino; 68656 fora do ar | Nada | |
| 5 | Contagem de páginas de Clínica Cirúrgica | | lacunas-pos (4) e palavras-chave-pos (4) contra o catálogo (3) | Item 1 da seção 1.4 e item 7 da seção 4.4 |
| 6 | Contagem de especialidades das provas | | links (22) e palavras-chave-pos (21) contra o catálogo (19) | Item 1 da seção 3.4 e item 2 da seção 4.4 |
| 7 | "Presencial integral" de 68632 | | lacunas-pos e palavras-chave-pos afirmam; catálogo diz "Presencial" | Itens 2 (1.4) e 5 (4.4) |
| 8 | Rótulo de 669 e 455 | palavras-chave-livres acerta (minicursos) | lacunas-pos e palavras-chave-pos chamam de grupos | Itens 4 (1.4) e 8 (4.4) |
| 9 | Ventilação mecânica | palavras-chave-livres separa 507 e 68618 | lacunas-livres usa uma palavra para as duas | Item 2 (2.4) |
| 10 | Carga horária de 202 | palavras-chave-livres marca [CONFIRMAR NO CATÁLOGO] | lacunas-livres dá "8 h" como fato | Item 3 (2.4) |
| 11 | Padrão "Pós-graduação em" | Títulos e H1 de palavras-chave-pos atendem | palavras-chave-pos (regra 2.2) libera "Pós em" em texto e FAQ; os outros quatro têm FAQ, H2, âncora ou link com "Pós em" | Padronizar: "Pós em" só em lista de palavra-chave e em palavra de grupo de anúncio |
| 12 | Ordem das áreas | lacunas-pos e palavras-chave-pos usam a mesma ordem (A2, A8, A5, A11, A6, A1...) | O plano lista A1 a A13 e depois A14, sem ordem interna obrigatória | Sem correção; registrar que a ordem é do departamento 03 |
| 13 | Palavras de hubs e de L08 | palavras-chave-livres registra os ajustes na seção 8.4 | lacunas-livres ainda traz as palavras anteriores | Reconciliar lacunas-livres com a seção 8.4, como o próprio arquivo de palavras propõe |

## 7. Próximo passo

Os cinco arquivos voltam aos agentes que os produziram (lacunas-de-conteudo, links-e-autoridade e pesquisa-de-palavras-chave) com as listas das seções 1.4, 2.4, 3.4, 4.4 e 5.4. Depois da correção, passam de novo por este QA e só então seguem para a aprovação humana. A tabela de aprovação de contexto/ufape-geral.md está sem nome em todas as linhas: quem aprova cada tipo de peça é [CONFIRMAR]. Os rascunhos de contato (D-1 a D-5) e a estrutura de Google Search continuam dependendo de aprovação humana, mesmo depois de corrigidos.

Resultado: Aprovado ( )  Bloqueado (X) para os cinco arquivos.
Revisado por: qa-de-marketing (agente); humano: [CONFIRMAR].
Data: 26/10/2026.

---

## Lista 1. Fatos (com fonte)

- 22 provas de bolsa abertas em 27/11/2026, em 19 especialidades; Anestesiologia (68639 e 68640), Cardiologia (68641 e 68642) e Clínica Cirúrgica (68643 e 68644) têm prova em São Paulo e Goiânia; 68656 encerrado. Fonte: contexto/catalogo-de-cursos.md, seção 3.
- Clínica Cirúrgica de Cães e Gatos tem três turmas no catálogo: 535 (Goiânia, presencial, verificar), 665 (São Paulo, semipresencial, verificar) e 68632 (Goiânia, presencial, aberto). Fonte: catálogo, seção 2.
- 719 Pós-Graduação Inteligência Artificial na Saúde: R$ 12.000,00, o menor total entre as Pós abertas; 68629: R$ 16.456,00. Fonte: catálogo, seção 2.
- 616 está na seção 5 (online e gravados), modalidade "On-line", local "Presencial e Online"; 573 "Semiprensecial"; 560 "Semipresencial"; 68618 sem modalidade. Fonte: catálogo, seções 4 e 5.
- 669 e 455 são minicursos; 721 é grupo de estudos; 463 é Mini Curso em Dermatologia, aberto (contínuo), R$ 248,00 à vista ou 5x de R$ 59,52. Fonte: catálogo, seções 5 e 7.
- 202 não tem carga horária no catálogo. Fonte: catálogo, seção 9.
- Padrão de nome "Pós-graduação em <área>", nunca "Pós em", em títulos, peças, anúncios e páginas. Fonte: contexto/pos-graduacao.md, "Padrão de nome".
- Curso livre: mostrar à vista, parcelado e total no cartão quando diferente; deixar claro que não confere diploma. Fonte: contexto/cursos-livres.md, "Regras específicas de comunicação".
- Áreas, itens e ondas do recorte. Fonte: saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seções 2.3 e 3, e docs/execucao-2026-10-26.md.

## Lista 2. Suposições

- [SUPOSIÇÃO] A quarta página de Clínica Cirúrgica citada pelos arquivos pode vir do seo-tecnico (por exemplo, uma página fora do catálogo); não encontrei o código.
- [SUPOSIÇÃO] Os códigos 638 e 183 citados pelo links-e-autoridade vêm da auditoria do seo-tecnico, que não reli nesta revisão.
- [SUPOSIÇÃO] A ausência de travessão e meia-risca foi conferida por leitura completa dos cinco arquivos, sem ferramenta de busca de caracteres.
- [SUPOSIÇÃO] Os itens marcados "Pendente de dado" na auditoria 03-busca (bloqueio de indexação, links quebrados, conteúdo sem JavaScript) não bloqueiam arquivos de planejamento, porque dependem de rastreamento que a squad não tem; voltam a valer quando houver página.

## Lista 3. Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Se a prova de Cardiologia (68641 e 68642) vale para a Pós-graduação em Ecocardiografia (698).
- [CONFIRMAR NO CATÁLOGO] Modalidade de 616 e de 68618; carga horária e turma de 202; frequência e jornada de 68632.
- [CONFIRMAR] Turma de destino de todas as provas (o contexto da linha diz que nenhuma página informa) e regras únicas da prova.
- [CONFIRMAR] Nome ou cargo de quem aprova cada tipo de peça (tabela vazia em contexto/ufape-geral.md).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação da Pós, do curso livre e do evento.
- [CONFIRMAR autorização] Docentes citados nas fichas, antes de qualquer peça com nome.
