# QA de marketing: guia de marca da Ufape, reconferência da versão 2 (estrategia-de-marca, etapa 1.6)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (Graduação, Pós-graduação, Cursos Livres e Eventos)
- Data: 26/10/2026
- Rodada: 2 (a rodada 1 está em saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02a.md)
- Peça revisada: saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md, versão 2, 509 linhas (não editada)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md, contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md
  - contexto/cursos/graduacao/editais-2027-1.md
  - contexto/catalogo-de-cursos.md (seções 1 a 9, inteiro)
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md (matriz do 1º semestre)
  - contexto/cursos/pos/68610-pos-graduacao-em-dermatologia-veterinaria.md
  - contexto/cursos/livres/68614-curso-livre-em-videotoscopia.md
  - contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
  - auditorias/02-estrategia-e-posicionamento.md
  - auditorias/conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02a.md
- Não conferi nas fontes primárias: fichas 573, 454, 68652, 700 e Pedagogia, e os arquivos de persona, concorrência, tendências e plano do cmo [SUPOSIÇÃO: transcrição fiel, como na rodada 1].
- Dados pessoais: nenhum nesta revisão. Nenhum docente é nomeado aqui.

---

## 1. Veredito

**CORRIGIR.**

A versão 2 resolveu os 16 itens da rodada 1 (C1 a C5 e A1 a A11). Volta para o agente estrategia-de-marca por um problema novo, que bloqueia pela conformidade (preço e condições completos; desconto com regra): o exemplo "assim sim" da Graduação para a família diz que o atraso perde só o desconto daquele mês, mas o Edital 003/2026 também lista o atraso de uma ou mais mensalidades como motivo de cancelamento do desconto (N1). A falha também é do QA: a redação proposta na rodada 1 (C1) omitiu essa cláusula, e o agente a seguiu ao pé da letra.

Problema que bloqueia: N1. Ajustes da mesma rodada, sem bloquear: N2 a N4.

---

## 2. Reconferência item a item da rodada 1

| Item | Resolvido? | Onde (linha da versão 2) | Observação do QA |
|---|---|---|---|
| C1. Desconto da Graduação (família) | Sim, com problema novo (N1) | 202; Lista 1, 456; regra 6, 279 | Renovação pedida pelo aluno a cada semestre com comprovação, perda no mês de pagamento atrasado, reajuste em dezembro e Edital 003/2026 estão presentes e batem com contexto/cursos/graduacao/editais-2027-1.md. Valores batem com o catálogo, seção 1 (R$ 10.000,00 por R$ 5.000,00, 50%). Falta a cláusula de cancelamento por atraso (N1) |
| C2. Cupom e produto 68634 (Eventos) | Sim | 215; D3, 87; 6.1, 246; Lista 3, 495 | [CONFIRMAR validade do cupom SIMPNEUROMONIT] e [CONFIRMAR status do produto 68634] presentes; o exemplo só vira peça depois das confirmações. Preços, 16 h e cupom de 20% batem com o catálogo, seção 9. "Comprovação do vínculo na secretaria" marcada [CONFIRMAR NO CATÁLOGO] |
| C3. Prova de bolsa | Sim, com ajuste (N2) | 212 | Data 27/11/2026 e inscrição de R$ 100,00 batem com o catálogo, seção 3. Público ("médicos veterinários formados"), 11 bolsas (2 de 50% em monitoria, 4 de 25%, 5 de 10%), nota 7,0, não acumulativa e intransferível batem com contexto/pos-graduacao.md, e tudo isso está marcado [CONFIRMAR NO CATÁLOGO] com a turma de destino. Falta o prazo de matrícula como elemento de validade (N2) |
| C4. Goiânia | Sim | 92; 6.2, 268; Lista 1, 459 | 68632 presencial; 289, 68609 e 68623 semipresenciais; provas 68640, 68642 e 68644. Confere com o catálogo, seções 2 e 3 |
| C5. Dados só de ficha sem marcação | Sim | 175 (Como ler); 188; 189; 190; 191; 200; 215; regra 4, 277; D1 e D2, 85 e 86; 2.2, 70 e 71; 6.2, 259 | Todos os cinco trechos apontados na rodada 1 estão marcados, e "Como ler" explica a regra. Restam três dados de condição sem marcação, fora dos exemplos de voz (N3) |
| A1. Traços de voz | Sim | 42; 3.1, 112 a 122; checklist, 349 | Traços apresentados como proposta [SUPOSIÇÃO] com equivalência a "técnica, próxima, confiante"; itens 5 e 6 não bloqueiam até a validação |
| A2. Opção "não se aplica" | Sim | 341 | Legenda "[x] cumpre; [n/a] não se aplica, com o motivo escrito; vazio bloqueia a peça" |
| A3. Duplicidades | Sim | 350 a 354; 370 a 372 | Item 7 remete a 14, 16, 17 e 18; item 5 só "precisa" e remete a 11, 19 e 20; item 6 só tom; item 9 com "igual à conformidade"; item 21 com autorização e titulação, item 23 com menor e dado pessoal |
| A4. Clareza do checklist | Sim | 344; 350; 361; 379; 380; 383 | Item 1 com "até a decisão da Ufape"; item 5 com "quando a peça fala do curso"; item 14 com "depois, só o texto aprovado"; item 28 com emoji em [SUPOSIÇÃO]; item 29 com [n/a] até o manual e selo proibido desde já; item 30 com [CONFIRMAR o arquivo do padrão de UTM] |
| A5. Ufape Clínica nos Livres | Sim | 168 | [CONFIRMAR por curso], com a nota sobre "hospital UFAPE" na ficha 68614 e os aprimoramentos 639, 640 e 641 em "verificar" (confere com o catálogo, seção 8) |
| A6. 641 e turmas numeradas | Sim | 87; 91 | 641 "não usar em peça enquanto o status for verificar"; 68605, 666 e 68607 (todas "verificar" no catálogo, seção 2) só como prova de tradição, uso [CONFIRMAR] |
| A7. Alternativa real por linha | Sim | 2.4, 95 a 104 | Uma linha por linha de negócio, com fonte e [SUPOSIÇÃO]. Fontes conferidas em contexto/graduacao.md, contexto/pos-graduacao.md, contexto/cursos-livres.md e contexto/ufape-geral.md |
| A8. Dado de 56% | Sim | 307; Lista 2, 479; Lista 3, 502 | Saiu da Lista 1; regra de não assumir leitor homem mantida sem o número |
| A9. Curso 488 | Sim | 129; 256 | Nome do catálogo, sem caixa alta, sem promessa de aprovação nem de título |
| A10. Frase do curso livre | Sim | 168; 213; 243; 362 | "não confere diploma nem equivale a graduação ou pós-graduação", igual à conformidade |
| A11. Contatos @intercursos.com.br | Sim | 157; 247; 265; 345 | A regra vale para o nome como marca; os endereços oficiais podem aparecer |

---

## 3. Conferência dos exemplos "assim sim" contra catálogo, editais e contextos

| Exemplo (linha) | Fonte conferida | Resultado |
|---|---|---|
| Pós, precisa (188) | Catálogo 68610: 500 h, semipresencial, 28/11/2026. Ficha 68610: módulo 5 presencial com "Técnicas de coleta", "Citopatologia" e "Atendimento de Casos Clínicos"; módulo 9 com casos clínicos | Dados do catálogo corretos; trecho da ficha marcado. Ajuste N4 ("citologia" x "citopatologia" e o plural "nos módulos presenciais") |
| Livres, precisa (189) | Ficha 68614: sábado de manhã teoria (anatomia, raciocínio diagnóstico), sábado à tarde demonstrativo em pacientes reais, domingo hands-on em modelo | Bate com a ficha; marcado [CONFIRMAR NO CATÁLOGO] |
| Graduação, precisa (190) | Ficha da graduação, matriz do 1º semestre: Anatomia, Práticas Hospitalares, Projeto Extensionista I; contexto/graduacao.md: prática desde o 1º semestre | Bate; marcado |
| Eventos, precisa (191) | Catálogo, seção 9: 16 h. Ficha do workshop: sexta com neuroanatomia, EEG, análises espectrais e BIS; sábado com instalação, qualidade do sinal e casos com bloqueio neuromuscular | Bate; marcado |
| Pós, próxima (199) | Ficha 68610: dermatopatias alérgicas e otoscopia no cronograma | Paráfrase plausível; marcada |
| Livres, próxima (200) | Catálogo 68614: 12 h, 28/11/2026. Ficha: 28 e 29/11 | Bate; "um fim de semana" marcado |
| Graduação jovem (201) | Catálogo, seção 1: integral 4 anos, noturno 5 anos, presencial, São Paulo | Bate. "Para quem trabalha durante o dia" vem da página e coincide com a persona do noturno em contexto/graduacao.md ([SUPOSIÇÃO] lá); é público, não dado de curso: sem ação |
| Graduação família (202) | Catálogo, seção 1; editais 2027/1 (Editais 002/2026 e 003/2026) | Valores, renovação, perda no mês e reajuste corretos. Falta o cancelamento por atraso: **N1, bloqueia** |
| Eventos, próxima (203) | Ficha do workshop: "Para quem decide olhando além do número" | Bate |
| Pós, transparente (211) | Catálogo 68610: 30x de R$ 1.000,00, R$ 30.000,00, matrícula R$ 250,00. Turma mínima de 20 e passagem e hotel: contexto/pos-graduacao.md e ficha 68610 | Preço completo e correto. Turma mínima sem marcação: N3 |
| Pós, prova de bolsa (212) | Catálogo, seção 3; contexto/pos-graduacao.md | Data, inscrição, público, bolsas, nota e regras corretos e marcados. N2 (prazo de matrícula) |
| Livres, transparente (213) | Catálogo 68614: R$ 1.250,00 ou 10x de R$ 175,00; conta 10 x 175,00 = R$ 1.750,00 correta | Bate; frase do curso livre conforme a conformidade |
| Graduação, transparente (214) | Editais 2027/1: inscrição gratuita, redação online ou Enem com mínimo de 300 pontos, aulas em 22/02/2027. Catálogo, seção 1: Portaria SERES/MEC nº 162, de 13/03/2025 | Bate. Ato regulatório exige o aprovador de contexto/ufape-geral.md, hoje vazio [CONFIRMAR] |
| Eventos, transparente (215) | Catálogo, seção 9: R$ 1.250,00 presencial (16 h), R$ 450,00 transmitido e gravado (só teoria), 20% com SIMPNEUROMONIT para aluno e ex-aluno. Datas 20 e 21/11/2026: briefing e ficha | Bate; validade do cupom, status do 68634 e comprovação do vínculo marcados |

Pontos pedidos no briefing desta rodada:
- Desconto da Graduação com renovação semestral, perda no atraso e reajuste em dezembro: presentes; falta o cancelamento por atraso (N1).
- Cupom SIMPNEUROMONIT com validade [CONFIRMAR]: presente (87, 215, 246, 495).
- Prova de bolsa com data, público e regras do contexto: presente e marcada (212); N2 para o prazo de matrícula.
- Goiânia por turma: correta (92, 268).
- [CONFIRMAR NO CATÁLOGO] no que vem só da ficha: presente em todos os exemplos de voz; três condições fora deles sem marcação (N3).

---

## 4. Auditoria 02-estrategia-e-posicionamento, item por item

| # | Item | Resultado | Observação |
|---|---|---|---|
| 1 | Uma única meta principal | Não se aplica | O guia herda a meta do plano do cmo (seção 11) |
| 2 | Persona e curso ou oferta nomeados | Atendido | Público por linha (177 a 180); cursos por código |
| 3 | 8 canais avaliados; ativos cabem na capacidade; fora com justificativa | Atendido com ressalva | Seção 9 cobre os 8. Capacidade do time [CONFIRMAR] |
| 4 | Posicionamento nomeia a alternativa real | Atendido | Seção 2.4 (A7 resolvido) |
| 5 | Todo pilar tem prova | Atendido | D1 a D4 com prova; Goiânia correta; itens em "verificar" só como prova |
| 6 | Regras de voz têm exemplos | Atendido com correção | 14 pares conferidos; um "assim sim" precisa de correção (N1) |
| 7 | Cabe no tempo e na verba | Não se aplica | Sem custo de mídia |
| 8 | Nada promete emprego, aprovação ou salário | Atendido | Inclui a regra do curso 488 |
| 9 | Preços, bolsas e condições do catálogo ou marcados | Atendido com ressalva (N3) | Preços batem com o catálogo; regras de bolsa, cupom e dados de ficha marcados. Turma mínima de 20, reembolso da inscrição e "11 bolsas" na seção 6.1 vêm do contexto ou da ficha sem a marcação da regra 4 do próprio guia. O briefing aceita a ficha como fonte consolidada, então não bloqueia, mas o guia fica incoerente com a própria regra |

Resultado da auditoria 02: atendida, com os ajustes N3 e N4.

---

## 5. auditorias/conformidade-educacional.md, item por item

Aplicada ao guia como documento de regras e aos exemplos "assim sim" como se fossem peças.

**DADOS DO CURSO**

| Item | Resultado | Observação |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atendido | 68610, 68614, 573 (28 h), 68635 e 68623 (750 h), Medicina Veterinária (integral 4 anos, noturno 5 anos), workshop (16 h), Goiânia por turma |
| Status "aberto" (ou sem chamada) | Atendido | Exemplos com chamada usam cursos abertos; 641, 68605, 666, 68607 e 68634 com aviso de não chamar para compra |
| Modalidade clara e correta | Atendido | C4 resolvido; 6.2 proíbe chamar semipresencial de presencial |

**REGULAÇÃO (MEC)**

| Item | Resultado | Observação |
|---|---|---|
| Graduação: ato do catálogo, sem arredondar nem antecipar | Atendido | Portaria SERES/MEC nº 162, de 13/03/2025. Aprovador de peça com ato regulatório [CONFIRMAR] |
| Pós lato sensu: sem "reconhecida pelo MEC"; texto aprovado | Atendido | Frases de MEC só em "assim não" (188, 213, 214), na 6.2 (253, 254), na regra 7 (280), no checklist (361, 380) e nas notas (409). O guia não inventa texto de validade |
| Curso livre: não confere diploma nem equivale a graduação ou pós | Atendido | A10 resolvido |
| Nota MEC só com fonte oficial e ano | Atendido | Só no contraexemplo da linha 214 |

**PROMESSAS E PROVAS**

| Item | Resultado | Observação |
|---|---|---|
| Nenhuma promessa de emprego, salário, promoção, aprovação | Atendido | 73, 129, 256, 363 |
| Empregabilidade ou satisfação com fonte | Não se aplica | Não há dado desse tipo |
| Superlativos só com fonte | Atendido | Nenhum em "assim sim" |
| Comparação com concorrente objetiva | Atendido com ressalva | Anclivepa e Qualittas como dado interno, com conferência na fonte primária e aprovador [CONFIRMAR] (78) |

**PREÇO E CONDIÇÕES (CDC)**

| Item | Resultado | Observação |
|---|---|---|
| Preço com valor, parcelas e condições completas, sem esconder matrícula ou reajuste | **Falha (N1)** | Pós, Livres e Eventos completos. Graduação família omite que o atraso de uma ou mais mensalidades é motivo de cancelamento do desconto (Edital 003/2026) |
| Bolsa e desconto com regra, público elegível e validade | **Falha (N1)** | Mesmo exemplo: a regra do desconto da Graduação está incompleta. Prova de bolsa e cupom atendidos com marcação (N2 é ajuste) |
| Urgência real | Atendido | Só em "assim não" e listas proibitivas |
| Prouni, Fies ou financiamento | Não se aplica | Não citados |

**PESSOAS E DADOS (LGPD E DIREITO DE IMAGEM)**

| Item | Resultado | Observação |
|---|---|---|
| Autorização de depoimentos, fotos e vídeos | Atendido | Seção 8.1; nenhum docente nomeado |
| Menores só com autorização dos responsáveis | Atendido | 223, 308, 330, 372 |
| Formulários com finalidade e política de privacidade | Não se aplica | Sem formulário |
| WhatsApp e e-mail só com consentimento e saída fácil | Atendido | 223 e 328 |
| Nenhum dado pessoal de aluno ou candidato | Atendido | Nenhum encontrado |

**PLATAFORMAS E ANÚNCIOS**

| Item | Resultado | Observação |
|---|---|---|
| Políticas da Meta e do Google, sem segmentação discriminatória | Atendido | 195, 267, 354 |
| Página de destino entrega o prometido | Não se aplica | Coberto pelo item 30 do checklist |
| Sem característica pessoal de quem vê | Atendido | "Assim sim" descrevem uso |
| Sem urgência falsa, contador ou interface falsa | Atendido | |
| Sem pessoa pública ou parceria inexistente | Atendido | 8.1, regras 4 e 5 |
| Sem caixa alta excessiva, pontuação repetida ou símbolos | Atendido | Regra 7 |
| Página carrega, sem domínio inesperado | Não se aplica | |
| Nenhuma sugestão para driblar a análise | Atendido | |

**RESULTADO:** Aprovado ( )  Bloqueado (X)
Itens bloqueados: preço e condições completos; bolsa e desconto com regra (N1).
Revisado por: agente qa-de-marketing; humano [CONFIRMAR aprovador, tabela de aprovação vazia em contexto/ufape-geral.md].
Data: 26/10/2026.

---

## 6. Conferências pedidas

| Conferência | Resultado |
|---|---|
| Travessão ou meia-risca | Nenhum encontrado na leitura integral das 509 linhas (leitura visual; não havia ferramenta de busca por caractere nesta revisão) |
| Dado pessoal | Nenhum. Nenhum docente nomeado; o nome do CEO de contexto/ufape-geral.md não aparece |
| Frase de certificação fora de regra proibitiva | Nenhuma. Todas as ocorrências estão em "assim não", na 6.2, na regra 7, no checklist ou nas notas para outros arquivos |
| "Últimas vagas", "vagas limitadas", "corra" fora de proibição | Nenhum |
| Promessa de emprego, renda, aprovação | Nenhuma |

---

## 7. Problema que bloqueia (corrigir antes de nova revisão)

**N1. Seção 5.2, Graduação (família), linha 202; repetir na Lista 1, linha 456.**
- Problema: "Pagamento depois do vencimento perde o desconto daquele mês" é só uma das regras do Edital 003/2026. O mesmo edital lista "atraso de uma ou mais mensalidades" entre os motivos de cancelamento do desconto (contexto/cursos/graduacao/editais-2027-1.md, linha 36). A peça apresenta a consequência mais branda como se fosse a única. "Para manter o desconto, o aluno pede a renovação" também pode soar como renovação garantida, e o edital só diz que o aluno pede, com comprovação. Origem: a redação proposta pelo QA na rodada 1 (C1) omitiu a cláusula.
- Correção proposta: "Para a família: no turno integral, a mensalidade do 1º semestre de 2027 cai de R$ 10.000,00 para R$ 5.000,00 (50% de desconto). Para continuar com o desconto, o aluno pede a renovação a cada semestre, com comprovação, conforme o edital. Pagamento depois do vencimento perde o desconto daquele mês, e o atraso de uma ou mais mensalidades está entre os motivos de cancelamento do desconto. As mensalidades têm reajuste em dezembro. Regras completas no Edital 003/2026." Acrescentar [CONFIRMAR com a Ufape como as duas regras de atraso do Edital 003/2026 se combinam] e levar a mesma pergunta para a Lista 3.

---

## 8. Ajustes da mesma rodada (não bloqueiam sozinhos, mas entram na correção)

**N2. Seção 5.3, prova de bolsa, linha 212.** O exemplo não traz o prazo de uso da bolsa. contexto/pos-graduacao.md informa 10 dias úteis para a matrícula (e 2 dias úteis para recurso). Acrescentar "Matrícula em até 10 dias úteis após o resultado" dentro do [CONFIRMAR NO CATÁLOGO] já existente, para o exemplo cumprir o item 19 do próprio checklist (validade). Registrar também a divergência de turma mínima (15 na prova, 20 no curso), que já está na Lista 3, junto do exemplo.

**N3. Condições só do contexto ou da ficha sem a marcação da regra 4 do próprio guia.**
- Linha 211 (Pós, transparente) e linha 238 (6.1): "turma mínima de 20 alunos" vem de contexto/pos-graduacao.md e da ficha 68610, não do catálogo. A fonte citada na 211 é "catálogo 68610; regra da linha".
- Linha 88 (D4): "reembolso da inscrição só se a turma não for confirmada; passagem e hotel só depois da confirmação" vem das considerações da ficha 68610.
- Linha 242 (6.1): "11 bolsas por prova" cita o catálogo como fonte, mas o número está só em contexto/pos-graduacao.md.
- Correção: marcar [CONFIRMAR NO CATÁLOGO] nesses trechos ou declarar em "Como ler" (175) e na regra 4 (277) que turma mínima e orientação de viagem da Pós são regra da linha em contexto/pos-graduacao.md e podem ir para a peça. O briefing aceita a ficha como fonte consolidada, por isso não bloqueia, mas o guia hoje contradiz a própria regra.

**N4. Seção 5.1, Pós, linha 188.** A ficha 68610 diz "Citopatologia" e "Técnicas de coleta", e não "citologia". Coleta e citopatologia estão só no módulo 5; casos clínicos nos módulos 5 e 9. Proposta: "No módulo presencial de março de 2027, técnicas de coleta, citopatologia e atendimento de casos clínicos", mantendo o [CONFIRMAR NO CATÁLOGO]. O traço "precisa" pede o termo técnico exato.

---

## 9. Encaminhamento

- A peça **volta para o agente estrategia-de-marca** com N1 (bloqueante) e N2 a N4 (ajustes). Depois, nova rodada curta do qa-de-marketing, só sobre esses quatro pontos.
- Não segue para a aprovação humana nesta rodada. Quando seguir, o aprovador de peças com ato regulatório e comparação com concorrente precisa estar definido em contexto/ufape-geral.md [CONFIRMAR].
- Nada foi publicado, enviado ou pago. O arquivo revisado não foi editado.

---

## Lista 1. Fatos (com fonte)

- Edital 003/2026: desconto válido só para o 1º semestre de 2027; o aluno pede a renovação a cada semestre, com comprovação; o desconto se perde no mês em que a mensalidade for paga depois do vencimento; o atraso de uma ou mais mensalidades está entre os motivos de cancelamento do desconto (contexto/cursos/graduacao/editais-2027-1.md, linhas 35 e 36).
- Edital 002/2026: mensalidades com reajuste em dezembro de cada ano (mesmo arquivo, linha 27).
- Medicina Veterinária: integral de R$ 10.000,00 por R$ 5.000,00 (50%), noturno por R$ 4.000,00 (60%); Portaria SERES/MEC nº 162, de 13/03/2025 (catálogo, seção 1).
- Provas de bolsa de 27/11/2026: R$ 100,00 (catálogo, seção 3); 11 bolsas, nota 7,0, 10 dias úteis para a matrícula, não acumulativa, intransferível, turma mínima de 15 na página da prova (contexto/pos-graduacao.md).
- Goiânia: 68632 presencial; 289, 68609 e 68623 semipresenciais (catálogo, seção 2).
- Workshop: R$ 1.250,00, R$ 450,00, 16 h, 30 vagas, cupom SIMPNEUROMONIT de 20%, status aberto (catálogo, seção 9); 68634 em "verificar", 24 h na loja (catálogo, seção 4); comprovação do vínculo na secretaria (ficha do workshop).
- 68610: módulo 5 presencial com técnicas de coleta, citopatologia e atendimento de casos clínicos; turma mínima de 20; reembolso da inscrição só se a turma não for confirmada (ficha 68610).
- 68614: R$ 1.250,00 ou 10x de R$ 175,00, 12 h, presencial, 28/11/2026 (catálogo); 28 e 29/11, roteiro e proporção de 1 para 3 (ficha).

## Lista 2. Suposições

- [SUPOSIÇÃO] As citações das fichas 573, 454, 68652, 700 e Pedagogia e dos arquivos de persona, concorrência, tendências e plano do cmo continuam fiéis (não conferidas nesta rodada nem na anterior).
- [SUPOSIÇÃO] A ausência de travessão e meia-risca foi conferida por leitura visual, sem busca automática por caractere.
- [SUPOSIÇÃO] As duas regras de atraso do Edital 003/2026 (perda no mês e cancelamento) convivem; a leitura exata depende da Ufape.

## Lista 3. Dados que faltam

- [CONFIRMAR com a Ufape] Como se combinam, no Edital 003/2026, a perda do desconto no mês do atraso e o cancelamento do desconto por atraso de uma ou mais mensalidades.
- [CONFIRMAR] Validade do cupom SIMPNEUROMONIT; status do produto 68634 e carga horária na loja (24 h x 16 h).
- [CONFIRMAR NO CATÁLOGO] Regras das provas de bolsa, público elegível, prazo de matrícula, turma de destino e turma mínima (15 x 20).
- [CONFIRMAR NO CATÁLOGO] Turma mínima e orientação de viagem da Pós, se forem tratadas como dado de curso.
- [CONFIRMAR] Aprovador de peças com ato regulatório, comparação e depoimento (tabela vazia em contexto/ufape-geral.md).

## Fontes

docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/graduacao.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/eventos.md; contexto/catalogo-de-cursos.md; contexto/cursos/graduacao/editais-2027-1.md; contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md; contexto/cursos/pos/68610-pos-graduacao-em-dermatologia-veterinaria.md; contexto/cursos/livres/68614-curso-livre-em-videotoscopia.md; contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/conformidade-educacional.md; saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep02a.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md.
