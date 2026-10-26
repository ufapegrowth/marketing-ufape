# QA de marketing: guia de marca da Ufape (estrategia-de-marca, etapa 1.6)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: geral (Graduação, Pós-graduação, Cursos Livres e Eventos)
- Data: 26/10/2026
- Peça revisada: saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md (não editada)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md, contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (seções 1 a 9, inteiro)
  - contexto/cursos/graduacao/editais-2027-1.md
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md
  - contexto/cursos/pos/68610-pos-graduacao-em-dermatologia-veterinaria.md
  - contexto/cursos/livres/68614-curso-livre-em-videotoscopia.md
  - contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
  - auditorias/02-estrategia-e-posicionamento.md
  - auditorias/conformidade-educacional.md
- Não conferi nas fontes primárias: fichas 573, 454, 68652, 700 e Pedagogia, e os arquivos de persona, concorrência, tendências e plano do cmo. As citações desses arquivos foram aceitas como estão [SUPOSIÇÃO: transcrição fiel].
- Dados pessoais: nenhum nesta revisão. Nenhum docente é nomeado aqui.

---

## 1. Veredito

**CORRIGIR.**

O guia é sólido na estrutura, na arquitetura de marca e nas regras proibitivas. Volta para o agente estrategia-de-marca porque falha em itens de auditorias/conformidade-educacional.md (preço e condições completos; bolsa e desconto com regra, público e validade; modalidade correta) e no item 9 da auditoria 02 (dados só da ficha sem marcação). Pela regra do QA, qualquer falha de conformidade bloqueia, sem exceção.

Problemas que bloqueiam: C1 a C5 (seção 4). Ajustes da mesma rodada: A1 a A11 (seção 5).

---

## 2. Auditoria 02-estrategia-e-posicionamento, item por item

| # | Item | Resultado do QA | Observação |
|---|---|---|---|
| 1 | O plano tem uma única meta principal | Não se aplica | Guia de marca não define meta; herda a do plano do cmo. Concordo com a seção 11 do guia |
| 2 | Persona e curso ou oferta estão nomeados | Atendido | Público por linha na seção 5; cursos citados por código (68610, 68614, 573, provas de 27/11/2026, workshop, Medicina Veterinária) |
| 3 | Os 8 canais foram avaliados; ativos cabem na capacidade; fora com justificativa | Atendido com ressalva | Seção 9 cobre os 8 canais. Capacidade do time [CONFIRMAR], como o próprio guia marca |
| 4 | O posicionamento nomeia a alternativa real | Parcial, corrigir (A7) | O guia nomeia concorrentes com hospital (Anclivepa, Qualittas), mas não registra as alternativas reais por linha que já estão documentadas: conteúdo gratuito e adiar (ufape-geral.md), curso livre em vez de pós e aprender na rotina com colega (pos-graduacao.md), Pedagogia EAD mais barata (graduacao.md). Uma linha por linha de negócio resolve |
| 5 | Todo pilar tem prova | Parcial, corrigir (C4, A6) | A prova "Goiânia presencial" está errada quanto à modalidade (C4). D3 usa o aprimoramento 641, com status "verificar", como exemplo de prova sem aviso de uso (A6) |
| 6 | As regras de voz da marca têm exemplos | Atendido com correções | 14 pares conferidos (4 + 5 + 5). Três "assim sim" precisam de correção (C1, C2, C3) e cinco precisam de marcação (C5) |
| 7 | O plano cabe no tempo e na verba informados | Não se aplica | Sem custo de mídia. Produção de imagem própria depende de capacidade [CONFIRMAR] |
| 8 | Nenhuma oferta, pilar ou resposta a objeção promete emprego, aprovação ou salário | Atendido | Promessa limitada ao que acontece no curso e à clareza das condições |
| 9 | Preços, bolsas e condições vêm do catálogo ou estão marcados [CONFIRMAR NO CATÁLOGO] | Falha, corrigir (C1, C3, C5) | Preços batem com o catálogo. Falham: regra de renovação do desconto da Graduação descrita de forma errada (C1); regras das bolsas vindas do contexto da linha sem marcação (C3); cinco "assim sim" com dado só da ficha sem a marcação que a regra 4 do próprio guia exige (C5) |

Resultado da auditoria 02: corrigir.

---

## 3. auditorias/conformidade-educacional.md, item por item

Aplicada ao guia como documento de regras e aos exemplos "assim sim" como se fossem peças.

**DADOS DO CURSO**

| Item | Resultado | Observação |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Falha (C4) | Nomes, cargas e turnos conferidos: 68610 (500 h, semipresencial, 28/11/2026), 68614 (12 h, presencial, 28/11/2026), 573 (28 h), Medicina Veterinária (integral 4 anos, noturno 5 anos), workshop (16 h). Falha: seção 2.3, linha 88, chama Goiânia de "presencial" para 4 turmas, mas só 68632 é presencial |
| Status "aberto" (ou sem chamada para inscrição) | Atendido com ressalva (A6, C2) | Exemplos com chamada usam cursos abertos. Ressalvas: 641 ("verificar") citado em D3; produto 68634 (modalidade transmitida do workshop) está "verificar" na seção 4 do catálogo, embora a linha do evento na seção 9 esteja "aberto" |
| Modalidade clara e correta | Falha (C4) | Mesmo problema de Goiânia |

**REGULAÇÃO (MEC)**

| Item | Resultado | Observação |
|---|---|---|
| Graduação: ato do catálogo, sem arredondar nem antecipar | Atendido | Portaria SERES/MEC nº 162, de 13/03/2025, bate com o catálogo, seção 1. Peça com ato regulatório passa pelo aprovador de contexto/ufape-geral.md, hoje vazio [CONFIRMAR] |
| Pós lato sensu: sem "reconhecida pelo MEC"; texto de validade aprovado | Atendido | As frases de MEC aparecem só em "assim não" (linhas 168 e 193), na lista proibitiva 6.2 (linha 232), na regra de caixa alta (linha 258) e nas notas para outros arquivos (linha 386). Texto aprovado ainda não existe e o guia não o inventa |
| Curso livre: não confere diploma e não equivale a graduação ou pós | Atendido com ajuste (A10) | Linha 193 e 6.1 dizem "não confere diploma nem equivale a pós-graduação". Recomendo alinhar à redação da auditoria |
| Nota MEC só com fonte oficial e ano | Atendido | Só no contraexemplo da linha 194 |

**PROMESSAS E PROVAS**

| Item | Resultado | Observação |
|---|---|---|
| Nenhuma promessa de emprego, salário, promoção, aprovação | Atendido | Seções 2.2, 3.2 e 6.2. Ver A9 sobre o nome do curso 488 |
| Empregabilidade ou satisfação com fonte, período e amostra | Não se aplica | Não há dado desse tipo. O dado de 56% de mulheres tem confiança baixa a média (A8) |
| Superlativos só com fonte | Atendido | 3.2 e 6.2 proíbem; nenhum "assim sim" usa superlativo |
| Comparação com concorrente objetiva e não depreciativa | Atendido com ressalva | Anclivepa e Qualittas aparecem como dado interno, sem depreciação, e o guia proíbe dizer "único". A fonte é resumo de busca: conferir na fonte primária antes de qualquer peça comparativa, que também passa pelo aprovador [CONFIRMAR] |

**PREÇO E CONDIÇÕES (CDC)**

| Item | Resultado | Observação |
|---|---|---|
| Preço com valor, parcelas e condições completas, sem esconder matrícula ou reajuste | Falha (C1) | Pós (linha 191), Livres (linha 193, conta 10 x R$ 175,00 = R$ 1.750,00 correta) e Eventos (linha 195) estão completos. O exemplo da Graduação para a família (linha 182) omite a regra de manutenção do desconto e o reajuste anual de dezembro (Edital 002/2026) |
| Bolsa e desconto com regra, público elegível e validade | Falha (C1, C2, C3) | Linha 182: regra de renovação errada. Linha 195: cupom SIMPNEUROMONIT sem validade. Linha 192: prova de bolsa sem data, sem público elegível e sem as regras de não acumulação e intransferência. O próprio checklist do guia (item 19) reprovaria esses três exemplos |
| Urgência real | Atendido | "Últimas vagas", "corra", "garanta já" só em "assim não" e na lista proibitiva |
| Prouni, Fies ou financiamento próprio | Não se aplica | Não citados |

**PESSOAS E DADOS (LGPD E DIREITO DE IMAGEM)**

| Item | Resultado | Observação |
|---|---|---|
| Autorização de uso de depoimentos, fotos e vídeos | Atendido | Seção 8.1 e D2; nenhum docente nomeado; currículos citados sem nome (linhas 123 e 125) |
| Menores só com autorização dos responsáveis | Atendido | Seções 5.4, 8.2 e 9 |
| Formulários com finalidade e política de privacidade | Não se aplica | O guia não tem formulário |
| WhatsApp e e-mail só com consentimento e saída fácil | Atendido | Seções 5.4 e 9 ("só com opt-in e forma fácil de sair") |
| Nenhum dado pessoal de aluno ou candidato | Atendido | Nenhum encontrado |

**PLATAFORMAS E ANÚNCIOS**

| Item | Resultado | Observação |
|---|---|---|
| Políticas da Meta e do Google, sem segmentação discriminatória | Atendido | Regra da seção 5.2 e item 9 do checklist |
| Página de destino entrega o que foi prometido | Não se aplica | Coberto pelo item 30 do checklist |
| Sem característica pessoal de quem vê | Atendido | 5.2 e 6.2; o "assim sim" de Eventos (linha 183) descreve uso, não característica |
| Sem urgência falsa, contador ou interface falsa | Atendido | |
| Sem pessoa pública ou parceria inexistente | Atendido | 8.1, regra 5; regra 4 impede transformar vínculo de docente em parceria |
| Sem caixa alta excessiva, pontuação repetida ou símbolos | Atendido | Regra 7 da seção 7 |
| Página carrega, sem domínio inesperado | Não se aplica | |
| Nenhuma sugestão para driblar a análise | Atendido | |

**RESULTADO:** Aprovado ( )  Bloqueado (X)
Itens bloqueados: preço e condições completos (C1); bolsa e desconto com regra, público e validade (C1, C2, C3); nome e modalidade conforme o catálogo e modalidade correta (C4).
Revisado por: agente qa-de-marketing; humano [CONFIRMAR aprovador, tabela de aprovação vazia em contexto/ufape-geral.md].
Data: 26/10/2026.

---

## 4. Problemas que bloqueiam (corrigir antes de nova revisão)

**C1. Seção 5.2, Graduação (família), linha 182.**
- Problema: "é renovado a cada semestre, conforme o edital" diz que a renovação é automática. O Edital 003/2026 diz que o aluno pede a renovação a cada semestre, com comprovação, e que o desconto se perde no mês em que a mensalidade for paga depois do vencimento. O exemplo também omite o reajuste anual em dezembro (Edital 002/2026). Falha nos itens de preço e de desconto da conformidade e no traço "transparente" do próprio guia.
- Correção proposta: "Para a família: no turno integral, a mensalidade do 1º semestre de 2027 cai de R$ 10.000,00 para R$ 5.000,00 (50% de desconto). Para manter o desconto, o aluno pede a renovação a cada semestre, com comprovação. Pagamento depois do vencimento perde o desconto daquele mês. As mensalidades têm reajuste em dezembro. Regras completas no Edital 003/2026." (fonte: catálogo, seção 1; editais 2027/1).

**C2. Seção 5.3, Eventos, linha 195.**
- Problema: o cupom SIMPNEUROMONIT aparece sem prazo de validade, que nenhuma fonte informa. O próprio item 19 do checklist e a conformidade exigem validade. A modalidade de R$ 450,00 é o produto 68634, com status "verificar" no catálogo (seção 4), sem data e com 24 h na loja.
- Correção proposta: acrescentar "[CONFIRMAR validade do cupom SIMPNEUROMONIT]" e "[CONFIRMAR status do produto 68634 antes de chamar para a compra da modalidade transmitida]". Manter o exemplo, mas avisar que ele só vira peça depois das duas confirmações.

**C3. Seção 5.3, Pós (prova de bolsa), linha 192.**
- Problema: o exemplo não informa a data da prova, o público elegível nem as regras (não acumulativa, intransferível). Os números de bolsas e a nota de corte vêm de contexto/pos-graduacao.md (páginas das provas), não do catálogo, que traz só o preço da inscrição. O catálogo e a página divergem sobre turma mínima (15 na prova, 20 no curso). A turma de destino de cada prova não está documentada.
- Correção proposta: "Prova de bolsa em 27/11/2026. Inscrição de R$ 100,00. Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. A bolsa não é acumulativa nem transferível. [CONFIRMAR NO CATÁLOGO: regras das bolsas, público elegível e turma de destino]".

**C4. Seção 2.3, linha 88 (provas complementares).**
- Problema: "Goiânia presencial (4 turmas abertas e 3 provas no catálogo...)". No catálogo, das 4 turmas abertas em Goiânia, só a 68632 (Clínica Cirúrgica de Cães e Gatos) é presencial. As turmas 289, 68609 e 68623 são semipresenciais. Falha no item de modalidade da conformidade.
- Correção proposta: "Goiânia: 4 turmas de Pós abertas no catálogo (68632 presencial; 289, 68609 e 68623 semipresenciais) e 3 provas de bolsa (68640, 68642, 68644); nenhum concorrente presencial achado em Goiânia (busca limitada)".

**C5. Exemplos "assim sim" com dado só da ficha e sem a marcação da regra 4 do próprio guia (seção 7).**
- Linha 168 (Pós, precisa): "coleta, citologia e atendimento de casos clínicos" vem do cronograma da ficha 68610, que a própria página diz que pode mudar.
- Linha 170 (Graduação, precisa): disciplinas do 1º semestre vêm da matriz na ficha. O contexto da linha confirma só "prática desde o 1º semestre".
- Linha 171 (Eventos, precisa): a programação de sexta e sábado vem da ficha do evento.
- Linha 180 (Livres, próxima): "um fim de semana" vem das datas 28 e 29/11 da ficha; o catálogo traz só 28/11/2026.
- Linha 195 (Eventos, transparente): "com comprovação do vínculo na secretaria" vem da ficha.
- Correção proposta: marcar cada trecho com [CONFIRMAR NO CATÁLOGO], como já foi feito nas linhas 83 e 169. A outra opção é acrescentar uma frase em "Como ler" (linha 155) dizendo que programação, cronograma e matriz vêm da ficha e seguem a regra 4. Sem isso, o guia contradiz a própria regra.

---

## 5. Ajustes da mesma rodada (não bloqueiam sozinhos, mas entram na correção)

**A1. Traços de voz x contexto/ufape-geral.md (seções 1, 3.1 e checklist item 5).** contexto/ufape-geral.md diz "técnica, próxima, confiante". O guia adota "precisa, próxima, transparente" e o item 5 do checklist já bloqueia peças por esses traços. O guia registra a troca como proposta, mas aplica a regra antes da validação. Correção: marcar o item 5 com [SUPOSIÇÃO: vale depois da validação da Ufape e da atualização de contexto/ufape-geral.md]. Até lá, "precisa" equivale a "técnica" e "transparente" se confere pelos itens 11, 19 e 20. A lista "Palavras que evitamos" do contexto geral está toda coberta pela seção 6.2: não há contradição.

**A2. Checklist sem opção "não se aplica" (linha 318).** "Item sem marcação bloqueia a peça", mas os itens 4, 15, 19, 20, 22 e 25 não valem para toda peça. Correção: legenda "[x] cumpre; [n/a] não se aplica, com motivo; vazio bloqueia".

**A3. Duplicidades no checklist de 30 itens.**
- Item 7 (lista "Evitamos") repete 14 (MEC), 16 (promessa), 17 (superlativo) e 18 (urgência), que também estão na 6.2. Proposta: "7. Nenhum outro termo da 6.2 além dos já conferidos nos itens 14, 16, 17 e 18".
- Itens 5 e 6 se sobrepõem ("próxima, na linha certa" e "tom da linha certo"). Proposta: o item 5 fica só com "precisa" e "transparente" e o 6 fica com o tom.
- O item 5, na parte "transparente (condição inteira)", repete 11, 19 e 20. Proposta: "quando a peça tem oferta, ver 11, 19 e 20".
- O item 9 repete o primeiro item de ANÚNCIOS da conformidade. Pode ficar, com a nota "igual à conformidade".
- Os itens 21 e 23 dividem "dado pessoal" e "autorização". Proposta: o 21 fica com autorização e titulação e o 23 com menor e dado pessoal (já está quase assim; tirar "nenhum dado pessoal" do 23 ou do 21, não dos dois).

**A4. Clareza de itens do checklist.**
- Item 1: "grafia combinada (Ufape ou UFAPE)" ainda não foi combinada. Proposta: "até a decisão da Ufape, Ufape no texto corrido (seção 4.2)".
- Item 5: "quantas horas" bloqueia post orgânico de caso clínico sem oferta, o que contradiz a seção 5.4 ("um conceito por peça"). Proposta: "carga horária quando a peça fala do curso".
- Item 14: quando a regulação aprovar o texto de validade, o item passaria a contradizer a conformidade ("usa o texto de validade aprovado"). Proposta: "até a regulação aprovar o texto; depois, só o texto aprovado".
- Item 28: a regra de emoji é [SUPOSIÇÃO] e não deveria bloquear. Marcar como tal.
- Item 29: "conforme manual, quando chegar" não se verifica hoje. Proposta: "[n/a] até o manual; nenhum selo do MEC ou de terceiro na arte vale desde já".
- Item 30: "UTM no padrão da squad" não aponta o padrão. Indicar o arquivo ou marcar [CONFIRMAR padrão de UTM].

**A5. Seção 4.2, Cursos Livres (linha 148).** "Ufape Clínica nos práticos e no aprimoramento" não leva [CONFIRMAR por curso], como a Pós (linha 147). A ficha 68614 fala em "hospital UFAPE", no endereço da sede, e não usa "Ufape Clínica". Os três aprimoramentos (639, 640, 641) estão "verificar". Correção: "[CONFIRMAR por curso se a prática é na Ufape Clínica]".

**A6. D3, linha 85.** Cita o aprimoramento 641 ("verificar") como prova de continuidade. Correção: acrescentar "não usar em peça enquanto o status for verificar". Vale o mesmo para as turmas numeradas da linha 88 (68605, 666, 68607, todas "verificar"): servem como prova de tradição, nunca com chamada de compra, e o uso como prova continua [CONFIRMAR].

**A7. Auditoria 02, item 4.** Acrescentar à seção 2.3 ou 3 as alternativas reais por linha, com fonte: adiar ou aprender por conteúdo gratuito (ufape-geral.md, [SUPOSIÇÃO]); curso livre ou congresso em vez da pós, e aprender na rotina com colega (pos-graduacao.md, [SUPOSIÇÃO]); conteúdo gratuito em redes e YouTube (cursos-livres.md, [SUPOSIÇÃO]); outras faculdades e Pedagogia EAD mais barata (graduacao.md, [SUPOSIÇÃO]).

**A8. Lista 1, linha 419.** O dado "56% dos médicos veterinários são mulheres" tem confiança baixa a média e vem de reportagem. Passar para a Lista 2 ou acrescentar [CONFIRMAR na fonte primária do CFMV]. A regra de não assumir leitor homem (8.2) continua válida sem o número.

**A9. Seções 3.2 e 6.2 x curso 488.** O nome oficial no catálogo é "CURSO PREPARATÓRIO PARA PROVA DE TITULO DE ESPECIALISTA EM ANESTESIOLOGIA VETERINÁRIA". Esclarecer que o nome do catálogo pode aparecer, sem caixa alta, e que a peça não promete aprovação nem título.

**A10. Linhas 193 e 223 (frase do curso livre).** Alinhar à conformidade: "Curso livre: não confere diploma nem equivale a graduação ou pós-graduação."

**A11. Item 2 do checklist x contatos oficiais.** contexto/ufape-geral.md manda usar nas peças os e-mails @intercursos.com.br. Esclarecer que o endereço de contato com o domínio intercursos.com.br pode aparecer e que a regra vale para o nome "Ufape Intercursos" como marca.

---

## 6. Conferências pedidas no briefing

| Conferência | Resultado |
|---|---|
| Travessão ou meia-risca no arquivo | Nenhum encontrado na leitura integral das 454 linhas (leitura visual, sem busca automática) |
| Frase de certificação ligada ao MEC fora de regra proibitiva | Nenhuma. Todas as ocorrências estão em "assim não", na 6.2, na regra 7 ou nas notas para outros arquivos |
| "Últimas vagas", "vagas limitadas", "corra" fora de proibição | Nenhum |
| Promessa de emprego, renda, aprovação | Nenhuma |
| Dado de curso fora do catálogo | Preços batem. Dados só da ficha sem marcação: C5. Regras de bolsa do contexto da linha sem marcação: C3. Regra do desconto da Graduação descrita errada: C1. Modalidade de Goiânia errada: C4 |
| Docente só com autorização | Atendido. Nenhum docente nomeado; currículos citados sem nome; regra 8.1 exige registro |
| Arquitetura de marca só com nomes das fichas | Atendido. Conferi "Faculdade UFAPE" e "CEO Faculdade UFAPE" (ficha da graduação), "UFAPE Intercursos" e "UFAPE Excelência Veterinária" (currículos na ficha da graduação), "Ufape Intercursos" (considerações da ficha 68610), "Faculdade Ufape, Unidade 2" e "Certificado UFAPE" (ficha do workshop), "Faculdade UFAPE" (ficha 68614). "Neuro Summit" é só o endereço da página e o guia não o adota. "Realização: Faculdade UFAPE" e "Faculdade UFAPE Goiânia" são propostas, cobertas pelo "tudo [CONFIRMAR]" da linha 129 e pelo [CONFIRMAR] da linha 146. O que não está documentado (relação entre Ufape Clínica e UFAPE Excelência Veterinária, emissor do certificado, grafia) está marcado [CONFIRMAR] ou [SUPOSIÇÃO] |
| Checklist de 30 itens: duplicidade e clareza | 30 itens contados. Duplicidades e itens pouco claros em A2, A3 e A4 |
| Dado pessoal | Nenhum |
| Contradições com contexto/ufape-geral.md | Traços de voz (A1). Palavras que evitamos: sem contradição. Regra de escrita sem travessão: sem contradição. Aprovadores: tabela vazia em ufape-geral.md, já listada pelo guia (linha 447) |

---

## 7. Encaminhamento

- A peça **volta para o agente estrategia-de-marca** com C1 a C5 (bloqueantes) e A1 a A11 (ajustes). Depois, nova rodada do qa-de-marketing.
- Não segue para aprovação humana nesta rodada. Quando seguir, o aprovador de peças com ato regulatório e comparação com concorrente precisa estar definido em contexto/ufape-geral.md [CONFIRMAR].
- Nada foi publicado, enviado ou pago. O arquivo revisado não foi editado.

---

## Lista 1. Fatos (com fonte)

- Medicina Veterinária: ato Portaria SERES/MEC nº 162, de 13/03/2025; integral de R$ 10.000,00 por R$ 5.000,00, noturno por R$ 4.000,00 (catálogo, seção 1).
- O desconto da Medicina Veterinária vale só para o 1º semestre de 2027. A renovação é pedida pelo aluno a cada semestre, com comprovação, e o desconto se perde no mês de pagamento atrasado (contexto/cursos/graduacao/editais-2027-1.md, Edital 003/2026). As mensalidades têm reajuste em dezembro (mesmo arquivo, Edital 002/2026).
- Turmas de Pós abertas em Goiânia: 289 (semipresencial), 68632 (presencial), 68609 (semipresencial), 68623 (semipresencial). Provas de bolsa em Goiânia: 68640, 68642, 68644 (catálogo, seções 2 e 3).
- 68634 (modalidade transmitida do workshop): status "verificar", sem data, 24 h na loja (catálogo, seção 4). Linha do workshop na seção 9: aberto, 16 h, R$ 1.250,00 e R$ 450,00, cupom SIMPNEUROMONIT de 20%.
- O cupom não tem prazo de validade informado (catálogo, seção 9; ficha do workshop).
- Regras das provas de bolsa (11 bolsas, nota 7,0, não acumulativa, intransferível): contexto/pos-graduacao.md. O catálogo, seção 3, traz só a inscrição de R$ 100,00.
- 68614: R$ 1.250,00 à vista ou 10x de R$ 175,00 (catálogo). Datas 28 e 29/11, roteiro, proporção 1 para 3 e "hospital UFAPE" só na ficha.
- 68610: módulo 5 presencial com coleta, citopatologia e atendimento de casos clínicos (ficha); "Ufape Intercursos" nas considerações (ficha).
- Nomes "UFAPE Excelência Veterinária", "UFAPE Intercursos" e "CEO Faculdade UFAPE" aparecem na ficha da graduação em Medicina Veterinária.
- Traços de voz em contexto/ufape-geral.md: técnica, próxima, confiante [SUPOSIÇÃO no próprio contexto].

## Lista 2. Suposições

- [SUPOSIÇÃO] As citações das fichas 573, 454, 68652, 700 e Pedagogia e dos arquivos de persona, concorrência, tendências e plano do cmo foram transcritas com fidelidade pelo agente estrategia-de-marca (não conferidas nesta revisão).
- [SUPOSIÇÃO] A ausência de travessão e meia-risca foi conferida por leitura visual, sem busca automática por caractere.
- [SUPOSIÇÃO] As correções propostas em C1 a C4 respeitam as regras dos editais e do catálogo. A redação final é do agente estrategia-de-marca.

## Lista 3. Dados que faltam

- [CONFIRMAR] Validade do cupom SIMPNEUROMONIT.
- [CONFIRMAR] Status do produto 68634 (verificar x aberto) e carga horária na loja (24 h x 16 h).
- [CONFIRMAR NO CATÁLOGO] Regras das provas de bolsa, público elegível, turma de destino e turma mínima (15 x 20).
- [CONFIRMAR NO CATÁLOGO] Cronograma da 68610, matriz do 1º semestre da Medicina Veterinária, programação do workshop, datas de dois dias da 68614.
- [CONFIRMAR] Se a prática dos Cursos Livres acontece na Ufape Clínica, curso a curso.
- [CONFIRMAR] Validação dos traços de voz e atualização de contexto/ufape-geral.md.
- [CONFIRMAR] Padrão de UTM da squad (item 30 do checklist).
- [CONFIRMAR] Aprovador de peças com ato regulatório, comparação e depoimento (tabela vazia em contexto/ufape-geral.md).
- [CONFIRMAR] Dado do CFMV sobre a proporção de mulheres, na fonte primária.

## Fontes

docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/graduacao.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/eventos.md; contexto/catalogo-de-cursos.md; contexto/cursos/graduacao/editais-2027-1.md; contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md; contexto/cursos/pos/68610-pos-graduacao-em-dermatologia-veterinaria.md; contexto/cursos/livres/68614-curso-livre-em-videotoscopia.md; contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/conformidade-educacional.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md.
