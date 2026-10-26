# QA de marketing: kit da Graduação 2027/1, rodada d (Medicina Veterinária em São Paulo e Pedagogia em Goiânia)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 26/10/2026 (segunda-feira)
- Workflow: /campanha-de-vestibular, conferência do kit mínimo (templates/kit-de-lancamento-graduacao.md)
- Status: rascunho de QA. Nada é publicado, enviado ou pago a partir deste arquivo. Os arquivos revisados não foram editados.
- Entradas lidas:
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 17)
  - templates/kit-de-lancamento-graduacao.md
  - contexto/ufape-geral.md, contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 1)
  - contexto/cursos/graduacao/editais-2027-1.md (fonte de todo dado do edital)
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md e graduacao-em-pedagogia.md (matriz, para conferir disciplinas, semestres e horas citados)
  - auditorias/conformidade-educacional.md, 02-estrategia-e-posicionamento.md, 05-social.md, 06-geracao-de-demanda.md, 07-email-e-whatsapp.md, 11-midia-paga.md, 12-video-e-audio.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-a.md, -b.md e -c.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12, em especial D1, D5, D11 e D12)
- Arquivos revisados inteiros (todos em saidas/, de 26/10/2026):
  - O1 02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md (versão 2, reconferência dos itens do qa-b)
  - C1 11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md (versão corrigida depois do qa-b)
  - P1 05-social-e-comunidade/posts-sociais-graduacao-2026-10-26.md (versão 3)
  - N1 06-geracao-de-demanda/campanhas-de-nutricao-graduacao-2026-10-26.md (versão 2)
  - M1 07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md (novo)
  - T1 12-video-e-audio/tiktok-graduacao-2026-10-26.md (novo)
- Fora desta rodada, por pedido: gestor-de-midia-graduacao e estrategia-de-midia-graduacao (em atualização).
- Linhas citadas: as da leitura de 26/10/2026.

---

## 1. Vereditos

| Arquivo | Veredito | Correções obrigatórias | Motivo principal |
|---|---|---|---|
| O1 estrategia-de-oferta | **APROVADO com ajustes** | 0 | Itens 1 a 3 do qa-b resolvidos. Restam ajustes de forma: Enem sem a condição completa em textos internos, "regra clara de renovação", marca de autorização de docentes desatualizada e registro de versão |
| C1 criativos-de-anuncio | **APROVADO com ajustes** | 0 | C-1 a C-9 do qa-b resolvidos. Restam: utm_content sem o bloco de gancho pedido em D12, Enem sem "2010 em diante" em 3 textos curtos, notas desatualizadas |
| P1 posts-sociais | **CORRIGIR** | 2 | "vale para entrar" e "pode usá-la para entrar" no Enem (G1-02 e G2-02, insinua entrada garantida); ganchos alternativos de desconto sem o ano e sem valores |
| N1 campanhas-de-nutricao | **CORRIGIR** | 1 | Primeira linha B do L2 (G1 e G2): "Você pode entrar com a redação online ou com o Enem", sem a condição, no texto que aparece sozinho na notificação |
| M1 copy-de-mensagens | **APROVADO com ajustes** | 0 | Kit completo, sem desconto fora do KW4, sem prazo inventado. Ajustes: uma primeira linha de reserva sem a condição do Enem, CTAs que prometem ação que a LP pode não entregar, frase "Cada passo leva alguns dias" |
| T1 tiktok | **CORRIGIR** | 2 | utm_campaign fora do D12 (blocos "organico" e "goiania", que os posts já tiraram); horas do 1º semestre (300 h e 280 h) usadas como fato, dado de carga horária que não está no catálogo |

"APROVADO" e "APROVADO com ajustes" querem dizer: segue para a aprovação humana; os ajustes entram na próxima versão sem nova rodada de QA. "CORRIGIR": volta ao agente que produziu e passa por conferência só dos itens apontados. Em todos os casos, publicação e envio continuam bloqueados pelas pendências externas da seção 5 (G6, G7, G8, G10, G11, G12, G13, G14, templates da Meta, datas do Enem). A tabela de aprovadores de contexto/ufape-geral.md segue vazia (G14); peças com ato regulatório passam também pela regulação.

---

## 2. Conferência de dados do edital e do catálogo (todos os arquivos)

| Dado | Fonte | O1 | C1 | P1 | N1 | M1 | T1 |
|---|---|---|---|---|---|---|---|
| Inscrição gratuita, abertas desde 17/08/2026 | Editais 002 e 004/2026 | ok | ok | ok | ok | ok | ok |
| Redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0 | idem | ok | ok | ok | ok | ok | ok |
| Enem: média mínima de 300 pontos, edições de 2010 em diante, com a condição de ingresso | idem | ajuste (textos internos) | ajuste (3 textos curtos sem "2010") | **falha** ("vale para entrar") | **falha** (L2, primeira linha B) | ok (1 linha de reserva sem condição) | ok |
| Aulas em 22/02/2027 | idem | ok | ok | ok | ok | ok | ok |
| Matrícula a partir de 2 dias depois do resultado | idem | ok | ok | ok | ok | ok | NA |
| Desconto com valor cheio, valor com desconto, percentual, validade (1º semestre de 2027), renovação com comprovação, perda no atraso, sem acúmulo, nome do programa | Editais 003/2026 | ok (0.2) | ok (B-DESC, cartões, RSA fixadas) | ok nos corpos; **falha** em 3 ganchos alternativos | ok (BP e LD) | ok (só KW4, bloco completo) | NA (sem preço) |
| Vencimento dia 10 e reajuste só na Medicina Veterinária | Edital 002/2026 | ok | ok (não cita) | ok | ok | ok (não cita) | NA |
| Cancelamento com 80% até 2 dias antes das aulas | editais | ok (cita 20/02/2027) | ok | ok | ok (cita 20/02/2027) | ok (sem a data, que é sábado) | NA |
| Turma mínima de 30, com devolução da 1ª parcela, nunca como pressão | editais | ok | ok | ok | ok | ok | NA |
| "representante legal" | Edital 002/2026 | ok | ok | ok | ok | ok | ok |
| Ato Medicina Veterinária: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) | catálogo | ok | ok (arte 1:1 sem D.O.U., ajuste) | ok | ok | ok | NA |
| Ato Pedagogia: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) | catálogo | ok | ok (arte 1:1 sem D.O.U., ajuste) | ok | ok | ok | ok |
| Nota do MEC, "reconhecido", certificação | proibido | ausente | ausente | ausente | ausente | ausente | ausente |
| "Últimas vagas", contagem, prazo de inscrição inventado | proibido | ausente | ausente | ausente | ausente | ausente | ausente |
| Carga horária: MV 4.195 h + 75 h; Pedagogia fora | catálogo | ok | ok | ok | ok | ok | ok no total; **falha** nas horas do semestre (T-2) |
| Matriz citada (disciplinas e semestres) | fichas, conferidas por este QA | ok | ok | ok | ok | ok | ok (7 disciplinas da Pedagogia e 3 da MV conferidas) |
| UTM para a LP: D11 (source e medium) | cmo-geral 12.7 | NA | ok (meta, google, tiktok; paid_social e cpc) | ok (organic_social) | ok (crm) | ok (crm) | ok no medium; tiktok como [SUPOSIÇÃO] |
| UTM: D12 (utm_campaign e utm_content) | cmo-geral 12.7 | NA | ok no campaign; ajuste no content (sem bloco de gancho) | ok (grad_..._202611) | ajuste (chave sem turno e mês do G2 divergem do M1) | ok | **falha** (blocos "organico" e "goiania") |
| U+2014 e U+2013 | regra da casa | nenhum | nenhum | nenhum | nenhum | nenhum | nenhum |

Observação sobre a última linha: este QA não tem ferramenta de busca automática nesta rodada; a conferência de U+2014 e U+2013 foi feita na leitura integral dos seis arquivos [SUPOSIÇÃO: conferência visual]. O M1 declara conferência automática própria. Recomendo uma busca automática pelo orquestrador antes da aprovação humana.

---

## 3. Detalhes por arquivo

### 3.1 O1 estrategia-de-oferta: APROVADO com ajustes

Reconferência dos itens do qa-b (veredito A3):

| Item do qa-b | Situação | Onde | Resultado |
|---|---|---|---|
| 1. Noturno "só escala" | "Anúncio pago do noturno bloqueado até G8 e MP4" | L154, L323, L326 | Resolvido |
| 2. V3 do G1 sem a condição do Enem | "(média mínima de 300 pontos, edições de 2010 em diante)" | L265 | Resolvido |
| 3. Desconto sem percentual ou sem "Condições e validade no edital" | Versões curtas da 0.2 | L184, L201, L228 | Resolvido |
| 4 (menor peso). "Enem" e "Enem antigo vale" | Sem mudança | L197, L223 | Continua (ajuste A-O1 abaixo) |

Auditoria 02, item por item: meta única (ok, serve à meta do cmo); persona e oferta nomeadas (ok, [SUPOSIÇÃO] marcada); 8 canais (ok, herdado do cmo); alternativa real (ok); todo pilar com prova (ok, hospital só com G11); voz com exemplos (pendente na Ufape, voz em [SUPOSIÇÃO]); cabe no tempo e na verba (pendente, G3); sem promessa de emprego, aprovação ou salário (ok); preços e condições do catálogo ou [CONFIRMAR] (ok).

Ajustes (não bloqueiam):

| # | Onde | Problema | Correção |
|---|---|---|---|
| A-O1 | L109 ("Enem com 300 pontos"); L123 ("300 pontos, de 2010 em diante"); L167 e L211 ("Enem de 2010 em diante com 300 pontos"); L197 ("ou Enem"); L223 ("Enem antigo vale") | Condição do Enem incompleta em textos que alimentam peças | "nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)" em todos |
| A-O2 | L158 ("com regra clara de renovação"); L201 ("com regra clara") | A "comprovação" da renovação ainda é [CONFIRMAR] (P1): "clara" promete mais do que o edital define | "com a regra de renovação explicada antes da matrícula" |
| A-O3 | L41 (regra 10), L134, L317 | "[CONFIRMAR autorização]" de docentes não se aplica mais (decisões 8 e 10) | Manter só nome e titulação da ficha; a marca fica apenas para o hospital (G11) |
| A-O4 | L7, L326, L328 a L334, L382 | Registro de versão cita só o qa-a e diz "pronta para a rodada -b"; as correções do qa-b não estão registradas | Acrescentar "Versão 3, corrigida após o qa-b (itens 1 a 3)" e atualizar o próximo passo |
| A-O5 | L165 ("Campos de Atuação e Práticas Hospitalares"); L210 ("Fundamentos da Educação Infantil", "gestão escolar") | Nomes de componentes resumidos (mesmo ponto do P9 do qa-c) | Usar os nomes da ficha: "Campos de Atuação do Médico Veterinário e Práticas Hospitalares"; "Fundamentos Teóricos e Metodológicos da Educação Infantil"; "Princípios e Métodos de Gestão Escolar Integrada" |
| A-O6 | L57, L92, L125, L169, L213 ("até 20/02/2027") | 20/02/2027 é sábado; o M1 deixou de citar a data até a Ufape confirmar | Harmonizar com o M1 ("até 2 dias antes do início das aulas") até a resposta [CONFIRMAR] |

### 3.2 C1 criativos-de-anuncio: APROVADO com ajustes

Reconferência do veredito C1 do qa-b: C-1 (Enem com a condição em cartões, cenas e descrições: L269, L328, L416, L501, L636, L690, L707, L739, L751), C-2 (ganchos sem "vale para entrar", L343, L516, L541), C-3 (L829 e L846, "inclusive em teste"), C-4 (L543), C-5 (L571), C-6 (L174, L295), C-7 (L37), C-8 (L51) e C-9 (L970): todos resolvidos.

Auditoria 11, item por item: plano do gestor aprovado (pendente, fora desta rodada); metas antes de subir (pendente MP1, bloqueia toda subida, ok no texto); verba (pendente MP2); nomenclatura (ajuste A-C1); UTMs completas (ok, URL base em G13); pixel e conversões (pendente, [DADO NÃO FORNECIDO]); criativos na conformidade (ok, seção 4); políticas das plataformas (ok); nenhum público menor (ok); Spark Ad com autorização (ok, nenhuma pessoa); relatório semanal (não se aplica ainda); sem segmentação discriminatória (ok); públicos sem dado pessoal (ok); dados de curso (ok); destino de WhatsApp (não se aplica); números só das exportações (ok); nenhuma alteração sem humano (ok).

Ajustes (não bloqueiam):

| # | Onde | Problema | Correção |
|---|---|---|---|
| A-C1 | Seção 9, L919 e todos os destinos (ex.: L187, L215, L243) | D12 pede o nome do anúncio "<conceito>_<formato>_<gancho>_vN"; o arquivo codifica o gancho dentro do vN (v1 = A, v2 = B, v3 = C, v4 em diante = iteração), o que mistura gancho e iteração | utm_content e nome do anúncio com bloco de gancho: v1-preco_feed-1x1_a_v1, v1-preco_feed-1x1_b_v1. Alinhar com o gestor-de-midia na atualização em curso (seção 4.2 do plano dele) |
| A-C2 | RSA-INT-v1 descrição 2 (L690); RSA-PED-p1 descrição 2 (L751); R-P1 cena 3, fala e tela (L636) | Enem com a média mínima, mas sem "edições de 2010 em diante" | Descrições: "Use a nota do Enem 2010+ (média mínima de 300) ou faça a redação online." (conferir 90 caracteres no editor). R-P1: "...nota do Enem, com média mínima de 300 pontos, de 2010 em diante" |
| A-C3 | INT-V4 arte 1:1 (L267); NOT-V4 arte 1:1 (L382); P4 arte 1:1 (L499) | Ato sem a data do D.O.U. (os posts já trazem o D.O.U. na arte, P10 do qa-c) | Acrescentar "(D.O.U. 21/03/2025)" e "(D.O.U. 20/12/2022)" |
| A-C4 | P2, campo Status (L428); seção 8, primeira nota (L910) | Dizem que a oferta afirma "Projeto Integrador em todos os semestres"; a oferta já foi corrigida (L209) | Retirar as duas notas |
| A-C5 | R-I2 cena 1 (L593) e INT-V3 gancho A (L228) | "Sua nota do Enem pode ser a sua entrada" funciona porque a condição vem na mesma arte e na cena seguinte; no vídeo, os 3 primeiros segundos ficam sem a condição | Acrescentar na tela da cena 1 a linha "Média mínima de 300 pontos" (recomendado, não obrigatório) |

### 3.3 P1 posts-sociais (v3): CORRIGIR

Reconferência do qa-c (P1 a P12): P2 a P12 resolvidos (representante legal, B-MENOR no G1 e no G2, promessa "por escrito" retirada, G1-02 e G2-02 bloqueados até as datas do Enem, G2 inteiro bloqueado até G6, G1-03 até G8, G1-04-alt escrito e conferido na matriz: Projeto Extensionista I a V no integral e I a VII no noturno, nomes da matriz no G2-06, D.O.U. no G1-05, datas fora do Carnaval, marcas de matriz). P1 resolvido nas chamadas, cartões e Stories quanto à média de 300 pontos, mas a troca dos ganchos manteve "vale para entrar" (P-1 abaixo).

Auditoria 05, item por item: frequência segue o plano (ok, dentro do D5; publicação só depois do QA e da aprovação); ideia clara (ok); ganchos cumpridos (**falha**, P-1 e P-2); histórias e números reais (ok, datas do Enem bloqueadas); formato para celular (ok); ações de comunidade (não se aplica ao rascunho); métricas de conversa e lead (ok); autorização de imagem (ok, artes tipográficas; foto só com G11); dados de curso batem com o catálogo (ok, salvo P-1).

Correções obrigatórias:

| # | Onde | Problema | Correção |
|---|---|---|---|
| P-1 | G1-02: gancho alternativo (L184), corpo (L191, "pode usá-la para entrar") e Stories tela 2 (L208); G2-02: gancho alternativo (L690), corpo (L697) e Stories tela 2 (L714) | "vale para entrar" e "pode usá-la para entrar" insinuam entrada garantida pela nota; a nota dá direito de concorrer (vagas de 45, 45 e 80). É o mesmo ponto do C-2 do qa-b, cortado nos criativos (L561) e proibido no M1 (regra 0.4.2) e no T1 (regra 0.3.2). Conformidade: promessa de aprovação | Gancho: "Enem de 2010 em diante, com média mínima de 300 pontos: a nota pode ser usada para concorrer." Corpo: "...pode usá-la para concorrer a uma vaga em Medicina Veterinária" (no G2, "em Pedagogia"). Stories tela 2: "Nota do Enem de 2010 em diante, com média mínima de 300 pontos, pode ser usada para concorrer." |
| P-2 | G1-07, gancho alternativo 2 (L435: "50% de desconto no 1º semestre: veja as condições antes de decidir."); G1-08, gancho alternativo 1 (L476: "...por R$ 4.000,00 por mês no 1º semestre."); G2-05, gancho alternativo 2 (L815: "50% de desconto no 1º semestre de Pedagogia: veja as condições.") | Desconto sem o ano (G1-07, G1-08, G2-05) e sem valores (G1-07, G2-05), contra a regra 4 do próprio arquivo e o C-6 do qa-b. Conformidade: desconto sem validade clara | G1-07: "De R$ 10.000,00 por R$ 5.000,00 (50%) no 1º semestre de 2027: veja as condições." G1-08: "...por R$ 4.000,00 por mês no 1º semestre de 2027." G2-05: "De R$ 1.050,00 por R$ 525,00 (50%) no 1º semestre de 2027: veja as condições." |

Ajustes:
- A-P1: auditoria 5.1 (L973) afirma que nenhum gancho promete aprovação; atualizar depois de P-1.
- A-P2: G2-05, corpo (L827): "nas condições do Edital 003/2026 Goiânia" pode ficar como "nas regras do Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026)", como a regra 3 da oferta.

### 3.4 N1 campanhas-de-nutricao (v2): CORRIGIR

Reconferência do qa-c (N1 a N16): N1 a N8 e N10 a N16 resolvidos (seis elementos do desconto em BP e LD; bloqueio G12 e G7 em toda mensagem com preço; Pedagogia sem dia 10 e sem reajuste; sem "por escrito"; representante legal; 13 versões -R por liberação escritas; bloqueio G6 e G8 com chamada alternativa; "a partir de 2 dias"; nome completo da disciplina; gancho do AT3; rodapé do G2; D.O.U.; resposta 4.2; UTM por mensagem; gancho do A6). N9 resolvido nas pré-visualizações e na primeira linha A, mas não na primeira linha B do L2 (N-1).

Auditoria 07, item por item: consentimento e descadastro (regras ok; registro e teste dependem do CRM e de G10, bloqueia envio); um objetivo por mensagem (ok); assuntos e primeiras linhas honestos (**falha**, N-1); segmentos por etapa (ok); regras de saída (ok, seção 5); resultados registrados (pendente até o primeiro envio); cliques e conversões medidos (ok no desenho, G13); horário, frequência e template Meta (horário e D1 ok; templates não submetidos, bloqueia envio).

Auditoria 06, item por item: briefing (ok); metas (pendente, G2 e G3); isca (não se aplica); nutrição depois da captura (ok); distribuição por peça (ok); comunidades (não se aplica); checagem (C0 em 30/10, ainda não feita); consentimento em todo formulário (pendente, G10 e G13); bolsas, descontos e prazos batem (ok).

Correção obrigatória:

| # | Onde | Problema | Correção |
|---|---|---|---|
| N-1 | G1-L2, primeira linha B (L416: "Você pode entrar com a redação online ou com o Enem."); G2-L2, primeira linha B (L1036, mesmo texto) | Enem sem a condição e "pode entrar com" no texto que aparece sozinho na notificação (mesmo ponto do N9 do qa-c e do C-2 do qa-b; a regra 4 do arquivo e a 0.4.2 do M1 proíbem) | "Oi, {primeiro_nome}, aqui é da Faculdade UFAPE. A inscrição é gratuita: redação online ou nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)." No G2, "...da Faculdade UFAPE de Goiânia..." |

Ajustes:

| # | Onde | Problema | Correção |
|---|---|---|---|
| A-N1 | 4.1, linha "Tem aula a distância?" (L1458) | "como a lei permite" (o mesmo trecho que o qa-a mandou trocar na oferta) | "conforme o edital, que cita o Decreto 14.256/2025" |
| A-N2 | G1-A3 (L757), G1-A3-R (L774), G2-A3 (L1211), G2-A3-R (L1379) | Variável {valor_primeira_mensalidade} não está na tabela 0.2 e traria valor fora do catálogo | Tirar a linha até a resposta da nota (1ª mensalidade com desconto) ou usar {mensalidade_desc} com a fonte do catálogo |
| A-N3 | 0.2, utm_campaign (L104) | Lead do G1 sem turno como grad_medvet_202611; posts e M1 usam grad_medvet-geral_202611. Pedagogia como grad_pedagogia_<AAAAMM do 1º envio depois de G6>; o M1 usa grad_pedagogia_202611 | Adotar grad_medvet-geral_202611 e uma só regra de mês para a Pedagogia nos dois arquivos (decisão do cmo, pedido já aberto em L1621) |
| A-N4 | Seção 1, tabela do kit mínimo (L246 a L259) | Diz que o kit são R2, AT2, L2, A2, M2, R1, A3, A6 e M5; o M1 entregou o kit como toques de calendário (KW1 a KW5, KE1 a KE3), com supressão para quem está em régua ativa. Duas contagens para o mesmo kit | Trocar a tabela por um apontamento ao M1, seção 0.1 (o kit é do copy-de-mensagens; a régua é por evento). O cmo confirma a leitura |
| A-N5 | Mensagens com "até 20/02/2027" (ex.: L479, L758, L818, L853, L933) | 20/02/2027 é sábado; o M1 usa só "até 2 dias antes do início das aulas" | Harmonizar com o M1 até a Ufape responder [CONFIRMAR] |

### 3.5 M1 copy-de-mensagens (novo): APROVADO com ajustes

Auditoria 07, item por item: consentimento e descadastro (regras ok; registro, G10 e teste do SAIR dependem do CRM, bloqueia envio); um objetivo (ok); assuntos e primeiras linhas honestos (ok nas escolhidas; ajuste A-M1 numa reserva); segmentos por etapa (ok, com supressão "fora de régua ativa" de 5 dias úteis); regras de saída (ok, inclusive "depois"); resultados registrados (pendente); cliques e conversões (ok no desenho, G13); horário, frequência e template (horário e D1 ok; nenhum template submetido, bloqueia envio).

Sem duplicar a régua: conferido. Cada toque do kit tem segmento que exclui quem recebeu ou vai receber toque da nutrição em 5 dias úteis, e cada mensagem aponta a mensagem da régua que cobre o mesmo assunto (KE1 x L1, KW1 x L2, KE2 e KW3 x R e AT, KW4 x A2, A3 e A6, KE3 e KW5 só para inscrito sem avaliação). O matriculado fica só com a régua M. A única divergência é de contagem, tratada em A-N4.

Ajustes (não bloqueiam):

| # | Onde | Problema | Correção |
|---|---|---|---|
| A-M1 | KW2, primeira linha 4 (L349: "Nota do Enem ou redação online: agora dá para escolher com a nota na mão.") | Reserva sem a condição, contra a regra 0.4.2 do próprio arquivo | Tirar da lista ou acrescentar "(média mínima de 300 pontos)" |
| A-M2 | Botões e links "Fazer minha avaliação" (L428, L453, L509, L524, L641, L663, L718, L733) e "Concluir a matrícula" (L570, L587) apontando para a LP | A avaliação e a matrícula acontecem na área do candidato e na plataforma de matrícula; se a LP não levar até lá, a página não entrega o que o botão promete (G13) | Até G13: "Ver como fazer a avaliação" e "Ver como concluir a matrícula"; ou trocar o destino com aprovação humana, como prevê L175 |
| A-M3 | KE2, G1 e G2 (L424, L449: "Cada passo leva alguns dias.") | Afirmação sem prazo confirmado (o prazo do resultado é [CONFIRMAR]); o próprio arquivo a marca como [SUPOSIÇÃO] (L858) | "Depois da avaliação ainda vêm o resultado, a matrícula (a partir de 2 dias depois do resultado) e os documentos." |
| A-M4 | 0.9, utm_campaign da Pedagogia (L155) | Mês 202611 para a Pedagogia, que só envia com link depois de G6; o N1 usa o mês do primeiro envio | Mesma regra nos dois arquivos (A-N3) |

### 3.6 T1 tiktok (novo): CORRIGIR

Auditoria 12, item por item: gancho de 3 s sem som e cumprido (ok, todos com texto na tela; a resposta da cena 2 do TK-G1-01 depende de T-2); legenda revisada (pendente, depois da edição); autorização de imagem e voz (docente coberto pelas decisões 8 e 10, com aceite do texto pelo próprio docente, como pede 12.9 do cmo; voz da locução [CONFIRMAR]); título, capa e descrição (ok); sem promessa e sem urgência falsa (ok; "45 vagas" é total do edital, sem pressão); dados de curso batem com o catálogo (**falha**, T-2); cadência cabe na capacidade (pendente, G11); métricas de retenção, conversa e clique (ok).

Correções obrigatórias:

| # | Onde | Problema | Correção |
|---|---|---|---|
| T-1 | 0.5 (L98) e destinos de TK-G1-01 (L181), TK-G1-02 (L240), TK-G2-01 (L307) e TK-G2-02 (L369) | utm_campaign grad_medvet-integral_organico_202611, grad_medvet-geral_organico_202611 e grad_pedagogia_organico_goiania_202611 fora da forma de D12 (chave + _AAAAMM). Os posts já tiraram "organico" e "goiania" na v3; o orgânico da linha deixaria de ser lido junto | grad_medvet-integral_202611, grad_medvet-geral_202611 e grad_pedagogia_202611, como nos posts. utm_medium=organic_social fica; utm_source=tiktok segue como [SUPOSIÇÃO] até o cmo confirmar |
| T-2 | TK-G1-01: gancho B (L141), gancho C (L142), cena 2 (L151), nota (L156), legenda (L163 e L165); Lista 1 (L433) | "300 horas práticas e 280 teóricas" e "mais horas de prática que de teoria" são carga horária por semestre: dado que só pode vir do catálogo, que traz apenas o total (4.195 h + 75 h). A ficha vem de leitura automática com colunas falhando por disciplina (o próprio C1 recusou usar horas, L913). A soma confere (280 + 300 = 580), mas não é dado de catálogo | Cena 2 responde com as disciplinas do 1º semestre (Anatomia, Práticas Hospitalares, Projeto Extensionista I, Campos de Atuação do Médico Veterinário e Práticas Hospitalares), sem horas; gancho A mantido; ganchos B e C saem; legenda sem a linha das horas. As horas só voltam se o acadêmico incluir a matriz no catálogo [CONFIRMAR NO CATÁLOGO] |

Ajustes:
- A-T1: L418 diz que os posts ainda usam "aceite do responsável" e Enem sem a condição; desatualizado depois da v3. Retirar a nota.
- A-T2: L98 e L420 atribuem o bloco "organico" aos posts; atualizar junto com T-1.
- A-T3: TK-G1-01, docente na câmera (L132): manter "Doutor em Anestesiologia (FM-USP)" exatamente como na ficha e registrar o aceite do texto pelo docente antes da gravação.

---

## 4. Auditoria de conformidade educacional, item por item

Legenda: ok; F = falha (bloqueia); PE = pendente externo (bloqueia a publicação ou o envio, não o arquivo); NA = não se aplica.

| Item | O1 | C1 | P1 | N1 | M1 | T1 |
|---|---|---|---|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | ok | ok | ok | ok | ok | **F** (T-2) |
| Status "aberto" no catálogo | ok | ok | ok | ok | ok | ok |
| Modalidade clara | ok | ok | ok | ok | ok | ok |
| Graduação: ato do catálogo, sem arredondar nem antecipar | ok | ok (PE regulação) | ok (PE regulação) | ok (PE regulação) | ok (PE regulação) | ok (PE regulação) |
| Pós lato sensu | NA | NA | NA | NA | NA | NA |
| Curso livre | NA | NA | NA | NA | NA | NA |
| Nota MEC só com fonte | ok (nenhuma) | ok | ok | ok | ok | ok |
| Sem promessa de emprego, salário, aprovação, concurso | ok | ok | **F** (P-1) | **F** (N-1) | ok | ok |
| Empregabilidade com fonte | NA | NA | NA | NA | NA | NA |
| Superlativos com fonte | ok | ok | ok | ok | ok | ok |
| Comparação com concorrente | ok | ok | ok | ok (EAD por atributo) | ok | ok |
| Preço com condições completas | ok | ok (PE G12, G7) | ok nos corpos (PE G12, G7) | ok (PE G12, G7) | ok (PE G12, G7) | NA |
| Desconto com regra, público e validade | ok | ok | **F** (P-2) | ok | ok | NA |
| Urgência real | ok | ok | ok | ok | ok | ok |
| Prouni, Fies, financiamento | ok | ok | ok | ok | ok | ok |
| Depoimento, foto e vídeo com autorização | PE (G11, hospital) | ok | ok (PE G11 para foto) | ok | ok | ok (docente autorizado; PE voz) |
| Menores só com autorização dos responsáveis | ok | ok | ok | ok (PE G10) | ok (PE G10) | ok |
| Formulários com finalidade e política de privacidade | PE G13 | PE G13 | PE G13 | PE G13 | PE G13 | PE G13 |
| WhatsApp e e-mail só com consentimento, saída fácil | PE G10 | NA | NA | PE (CRM, G10) | PE (CRM, G10) | NA |
| Nenhum dado pessoal | ok | ok | ok | ok | ok | ok |
| Políticas Meta e Google, sem segmentação discriminatória | ok | ok | ok | ok | ok | ok |
| Página de destino entrega o prometido | PE G6, G8 | PE G13, G6, G8 | PE G6, G8 | PE G6, G8 | PE G13, G6, G8 (ajuste A-M2) | PE G6, G8 |
| Texto não afirma característica de quem vê | ok | ok | ok | ok | ok | ok |
| Sem escassez falsa, contador, botão falso | ok | ok | ok | ok | ok | ok |
| Sem pessoa pública ou parceria inexistente | ok | ok | ok | ok | ok | ok |
| Sem caixa alta excessiva ou símbolos | ok | ok | ok | ok | ok | ok |
| Sem sugestão de driblar análise | ok | ok | ok | ok | ok | ok |
| **Resultado** | Aprovado | Aprovado | Bloqueado | Bloqueado | Aprovado | Bloqueado |

Revisado por: qa-de-marketing (agente). Revisão humana: pendente. Data: 26/10/2026.

---

## 5. Conferência do kit mínimo, item a item (templates/kit-de-lancamento-graduacao.md)

| Entrega | Mínimo | G1 Medicina Veterinária | G2 Pedagogia | Situação |
|---|---|---|---|---|
| Plano dos 8 canais | 1 | cmo-graduacao (aprovado no qa-b) | idem | Coberto; não revisado nesta rodada |
| Plano de mídia | 1 | gestor-de-midia-graduacao | idem | Coberto; em atualização, fora desta rodada |
| Posts orgânicos | 6 | 6 no kit (G1-01, G1-04 ou G1-04-alt, G1-06, G1-07, G1-08, G1-10), mais 2 para famílias e 3 extras | 6 (G2-01, G2-03 a G2-07), mais 1 extra | Coberto em quantidade; volta por P-1 e P-2. Publicação: G1-07, G1-08, G1-09 e G2-05 até G12 e G7; G1-03 e G1-08 até G8; todo o G2 até G6 |
| Criativos de anúncio com UTM para a LP | 4 | 8 conceitos (4 integral, 4 noturno), mais 6 RSA | 5 conceitos, mais 2 RSA | Coberto; noturno bloqueado (G8, MP4, MP8) e Pedagogia (G6, MP4, MP1, MP9); nada sobe sem MP1, MP2, MP4 e EM1 |
| WhatsApp ligados aos prazos do edital | 5 | KW1 a KW5 do M1, com -R | KW1 a KW5 do M1, com -R | Coberto pelo M1; a régua do N1 cobre os mesmos assuntos por evento, sem envio duplicado ao mesmo contato (supressão M1 0.3.2). Contagem a unificar (A-N4) |
| E-mails ligados aos prazos do edital | 3 | KE1 a KE3 do M1, com -R | KE1 a KE3 do M1, com -R | Coberto; idem |
| Roteiros de vídeo curto | 2 | TK-G1-01 e TK-G1-02 (orgânicos), mais R-I1, R-I2, R-N1, R-N2 (pagos, C1) | TK-G2-01 e TK-G2-02, mais R-P1, R-P2 | Coberto em quantidade; T1 volta por T-1 e T-2 |

O mínimo não diminuiu em nenhuma liberação. Toda peça aponta para a LP da Graduação com UTM; nenhuma propõe alterar a LP.

---

## 6. Encaminhamento

- O1 estrategia-de-oferta: **segue para a aprovação humana**, com os ajustes A-O1 a A-O6 na próxima versão.
- C1 criativos-de-anuncio: **segue para a aprovação humana**, com A-C1 (alinhado à atualização do gestor-de-midia) a A-C5.
- M1 copy-de-mensagens: **segue para a aprovação humana**, com A-M1 a A-M4.
- P1 posts-sociais: **volta para o posts-sociais**, com P-1 e P-2 (e A-P1, A-P2).
- N1 campanhas-de-nutricao: **volta para o campanhas-de-nutricao**, com N-1 (e A-N1 a A-N5).
- T1 tiktok: **volta para o tiktok**, com T-1 e T-2 (e A-T1 a A-T3).
- Depois das correções, conferência só dos itens apontados (rodada e). Mesmo aprovadas, nenhuma peça é publicada, enviada ou paga antes das pendências externas e da aprovação humana.

---

## Lista 1. Fatos (com fonte)

- Inscrição gratuita desde 17/08/2026; redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0; Enem com média aritmética mínima de 300 pontos, edições de 2010 em diante; matrícula eletrônica a partir de 2 dias depois do resultado; documentos em até 30 dias; aulas em 22/02/2027; turma mínima de 30 com reembolso da 1ª parcela; devolução de 80% se o cancelamento for pedido até 2 dias antes das aulas; candidato menor precisa do aceite do representante legal na inscrição e na matrícula (contexto/cursos/graduacao/editais-2027-1.md).
- Vagas: 45 integral, 45 noturno, 80 Pedagogia (idem). Os editais não trazem data-limite de inscrição, data de prova, vagas restantes nem nota do MEC (idem).
- Desconto: integral de R$ 10.000,00 por R$ 5.000,00 (50%), noturno por R$ 4.000,00 (60%), Pedagogia de R$ 1.050,00 por R$ 525,00 (50%), só no 1º semestre de 2027, renovação semestral com comprovação, perda no mês pago com atraso, sem acúmulo com programa governamental (catálogo, seção 1; Editais 003/2026). Vencimento no dia 10 e reajuste de dezembro só no Edital 002/2026.
- Atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025); Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). Carga horária no catálogo: 4.195 h + 75 h (Medicina Veterinária); Pedagogia em [CONFIRMAR] (catálogo, seção 1).
- Matriz do 1º semestre do integral na ficha: subtotal de 280 h teóricas, 300 h práticas e 580 h, com colunas por disciplina incompletas na leitura automática; disciplinas Anatomia, Citologia, Comportamento, Genética, Campos de Atuação do Médico Veterinário e Práticas Hospitalares, Educação Ambiental, Projeto Extensionista I e Práticas Hospitalares. Projeto Extensionista I a V (integral) e I a VII (noturno); estágio no 7º e 8º (integral) e 9º e 10º (noturno) (contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md, conferido por este QA).
- 1º semestre da Pedagogia: História da Educação; Formação Docente para a Diversidade; Didática: Organização do Trabalho Pedagógico; Língua Portuguesa: da oralidade à escrita; Ética, Filosofia e Direitos Humanos; Prática Docente I; Projeto Integrador I (contexto/cursos/graduacao/graduacao-em-pedagogia.md, conferido por este QA).
- D11: CRM com utm_medium=crm; orgânico com organic_social; pago na Meta e no TikTok com paid_social; Google com cpc. D12: utm_campaign = chave + _AAAAMM no CRM e no orgânico; Graduação com prefixo grad_; anúncio "<conceito>_<formato>_<gancho>_vN" (cmo-geral-2026-10-26.md, seção 12.7).
- Autorização de imagem e de citação para todos os docentes, palestrantes e convidados (docs/execucao-2026-10-26.md, decisões 8 e 10).
- 20/02/2027 é sábado; 22/02/2027 é segunda-feira (calendário).

## Lista 2. Suposições

- [SUPOSIÇÃO] A conferência de U+2014 e U+2013 nos seis arquivos foi visual, na leitura integral, sem busca automática (ferramenta indisponível nesta rodada); nenhum caractere foi encontrado.
- [SUPOSIÇÃO] "vale para entrar", "pode usá-la para entrar" e "pode entrar com o Enem" são lidos pelo público como entrada garantida, como nos qa-a, qa-b e qa-c.
- [SUPOSIÇÃO] "Sua nota do Enem pode ser a sua entrada", com a média mínima na mesma peça, não sugere entrada garantida; por isso ficou como recomendação (A-C5), não como falha.
- [SUPOSIÇÃO] A diferença de utm_content no C1 (gancho dentro do vN) é ajuste de nomenclatura, a resolver com o gestor-de-midia na atualização em curso, e não falha de conformidade.
- [SUPOSIÇÃO] utm_source=tiktok para o orgânico, até o cmo confirmar.

## Lista 3. Dados que faltam

- [CONFIRMAR] Datas oficiais do Enem 2026 e da divulgação das notas; se a nota de 2026 pode ser enviada assim que divulgada (G1-02, G2-02, KW2, semana E dos criativos).
- [CONFIRMAR] Efeito do reajuste de dezembro sobre 2027/1 (G12) e correção dos Editais 003/2026 (G7).
- [CONFIRMAR] Correção das páginas de Pedagogia (G6) e do turno do noturno (G8); URL que recebe a UTM, se a LP leva à área do candidato e à matrícula, origem no CRM e política de privacidade (G13).
- [CONFIRMAR] Consentimento de candidato menor no CRM e campos de idade e representante legal (G10); opt-in registrado; templates da Meta aprovados.
- [CONFIRMAR] Se o cancelamento com 80% pode ser pedido em 20/02/2027, que é sábado.
- [CONFIRMAR] Vencimento e reajuste da Pedagogia no Edital 004/2026; se a 1ª mensalidade já sai com o desconto.
- [CONFIRMAR NO CATÁLOGO] Carga horária por semestre e nomes das disciplinas como dado de catálogo; carga horária da Pedagogia (G5); horário das práticas e do estágio do noturno.
- [CONFIRMAR] Com o cmo: chave sem turno (grad_medvet-geral), mês do utm_campaign da Pedagogia, utm_source do TikTok orgânico, contagem única do kit de mensagens (M1 x N1) e bloco de gancho no nome do anúncio (D12).
- [CONFIRMAR] Uso da Ufape Clínica pela graduação e autorização de imagem do hospital (G11); perfil de TikTok e quem grava.
- [CONFIRMAR] Aprovadores por tipo de peça (G14).
