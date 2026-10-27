# QA de marketing: montagem das campanhas pagas da Graduação 2027/1 (Meta e Google)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 27/10/2026 (terça-feira)
- Workflow: /campanha-de-vestibular, conferência da montagem dos canais pagos (etapas de anuncios-meta e anuncios-google)
- Status: rascunho de QA. Nada é publicado, enviado ou pago a partir deste arquivo. Os arquivos revisados não foram editados.
- Arquivos revisados (inteiros):
  - A1 saidas/11-midia-paga/anuncios-meta-graduacao-2026-10-26.md (339 linhas)
  - A2 saidas/11-midia-paga/anuncios-google-graduacao-2026-10-26.md (638 linhas)
- Entradas lidas:
  - CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 17)
  - contexto/graduacao.md; contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 1); contexto/cursos/graduacao/editais-2027-1.md (fonte de todo dado do edital)
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md e graduacao-em-pedagogia.md (só para conferir disciplinas citadas)
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (G1 a G16; G10 menores)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12.7, D11 e D12; seção 13, conferida quanto a mídia)
  - saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (v3: seções 2.3 a 4.8) e estrategia-de-midia-graduacao-2026-10-26.md (v3: fases, semanas e calendário do Enem)
  - saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md (seções 2.1, 2.3, 2.6, 4.2 e 9)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-d.md (A-C1 a A-C5)
  - auditorias/11-midia-paga.md; auditorias/conformidade-educacional.md
- Script de recontagem: /tmp/claude-0/-home-user/266c34a1-9b23-5a3e-bf6a-85e9f1184970/scratchpad/qa-campanhas-grad/conta.py (lê as tabelas dos dois arquivos e conta caracteres com espaços, em NFC).

---

## 1. Vereditos

| Arquivo | Veredito | Correções obrigatórias | Motivo principal |
|---|---|---|---|
| A1 anuncios-meta | **CORRIGIR** | 5 (M-1 a M-5) | Conceitos com preço e desconto (v1-preco, v4-ato, p3-preco, p4-ato) podem subir sem a trava G7, ao contrário do Google e do criativos; limites de gasto por campanha não batem com as fases que cada campanha cobre; regra de divisão do noturno ambígua; regra de plataforma e datas do Enem sem marca |
| A2 anuncios-google | **APROVADO com ajustes** | 2 (G-1 e G-2) | Textos, contagens, fixações, verba, UTM e travas corretos. Ajustes: regras de plataforma sem marca (uma delas contradiz o próprio arquivo) e decisão sobre a faixa etária "desconhecida" fora do pedido de aprovação |

"APROVADO com ajustes": segue para a aprovação humana; os ajustes entram na próxima versão e o qa confere só esses itens antes da montagem (11 a 13/11). "CORRIGIR": volta ao anuncios-meta e passa por conferência só dos itens M-1 a M-5. Em ambos os casos, nada sobe sem MP1, MP2, MP4, MP10, G13, G14 e a aprovação humana.

---

## 2. Conferências pedidas

### 2.1 Recontagem do Google por script (item 1)

| Grupo | Itens | Limite | Maior | Divergência entre o declarado e o real | Acima do limite |
|---|---|---|---|---|---|
| Títulos dos 4 RSA (L218 a L310) | 60 | 30 | 30 ("Faculdade de Veterinária em SP", L271 e L297) | 0 | 0 |
| Descrições dos 4 RSA (L233 a L314) | 16 | 90 | 88 (L233, L259, L285, L311) | 0 | 0 |
| Ativos da fase 4 (L324 a L326) | 3 | 30 e 90 | 19 e 68 | 0 | 0 |
| Sitelinks, título (L350 a L354) | 5 | 25 | 25 ("Edital do Vestibular 2027", L351) | 0 | 0 |
| Sitelinks, descrições (L350 a L354) | 10 | 35 | 32 (L352, L354) | 0 | 0 |
| Frases de destaque (L367 a L372) | 6 | 25 | 23 (L369) | 0 | 0 |
| **Total** | **100** | | | **0** | **0** |

Meta (conferência extra, limite [SUPOSIÇÃO] do próprio arquivo de cerca de 40 e 30): 13 títulos de 20 a 35 caracteres e 13 descrições de 16 a 30. Nenhum acima.

Fixações:
- Desconto (RSA-M1 L218 e L233; RSA-G1 L270 e L285): título "Integral: 50% de Desconto" fixado na posição 1 e descrição 1 fixada na posição 1. Como a descrição da posição 1 sempre aparece, o percentual nunca sai sem valor cheio, valor com desconto, "/mês", validade (1º semestre 2027) e "Condições e validade no edital". Nenhum outro título cita preço ou desconto. **Garante.**
- Enem (RSA-M2 L244 e L259; RSA-G2 L296 e L311): título "Enem: Média Mínima 300 Pontos" fixado na posição 1 e descrição 1 fixada com "média mínima de 300 pontos, edições de 2010 em diante". O título solto "Enem de 2010 em Diante" (L251, L302) só aparece junto do título fixado. Os RSA de preço não têm Enem (L238, L290). **Garante.**
- Recursos sem Enem, sem preço e sem a palavra desconto (L344): conferido nos 5 sitelinks e nas 6 frases.

### 2.2 Verba e diárias (item 2)

| Conferência | A1 Meta | A2 Google | Fonte |
|---|---|---|---|
| Total da Medicina Veterinária | R$ 1.440,00 (L109) | R$ 560,00 (L116) | gestor 3.3; soma R$ 2.000,00 |
| Total da Pedagogia | R$ 2.000,00 (L109) | fora por verba | gestor 3.1 e 3.3 |
| Semanas S1 a S14 contra o gestor 3.3 | 14 de 14 iguais, nos dois cursos | 14 de 14 iguais | gestor 3.3 |
| Totais por fase | 450, 225, 525, 240; Pedagogia 600, 300, 700, 400 (L112) | 150, 75, 175, 160 (L96) | estrategia 2.4; gestor 3.2 |
| Diárias (semanal / 7) | todas conferidas (L95 a L108) | todas conferidas, arredondadas para baixo (L102 a L115); marca R$ 184,00 e genérica R$ 376,00 somam R$ 560,00 | gestor 3.3 |
| Leads base | 216 e 300 (L82, L109) | 84 (L125) | verba / R$ 6,67 |
| Nenhum curso acima de R$ 2.000,00 | ok na tabela; **trava de gasto falha** (M-2) | ok; data de término 21/02/2027 como segunda trava (L88) | decisão 15 |
| Pausa em 22/02/2027 | L110, L241, AM8 | L117, L88, AG10 | MP13 |

### 2.3 Dados do edital e conformidade (item 3)

Conferidos contra contexto/cursos/graduacao/editais-2027-1.md e o catálogo, seção 1: inscrição gratuita; redação online, eliminatória, nota mínima 5,0, feita depois da inscrição; Enem com média mínima de 300 pontos, edições de 2010 em diante; aulas em 22/02/2027; turma mínima de 30 com devolução da 1ª parcela; cancelamento com 80% até 2 dias antes das aulas; matrícula eletrônica a partir de 2 dias depois do resultado; documentos em até 30 dias; integral 4 anos e noturno 5 anos; Pedagogia noturno 4 anos; preços de/por e percentuais; "representante legal"; atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) e Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). **Todos corretos nos dois arquivos.** Disciplinas citadas (Anatomia, Práticas Hospitalares, Projeto Extensionista I; Prática Docente I a VIII, Projeto Integrador I a VII, estágio a partir do 6º) batem com as fichas, como no qa-d. Pedagogia sem carga horária (G5). Nenhum "últimas vagas", nota do MEC, frase de certificação ou promessa de emprego (busca no texto). Anúncio só 18+ nos conjuntos da Meta (L124); no Google, ver G-2. Desconto: sempre completo (valor cheio, valor com desconto, percentual, validade e "Condições e validade no edital", regra inteira nos blocos B-DESC ou no SL5) ou ausente.

### 2.4 UTM D11 e D12 (item 4)

| Parâmetro | Meta (L198 a L204) | Google (L435 a L452) | Criativos (seção 9) | D11 e D12 |
|---|---|---|---|---|
| utm_source / utm_medium | meta / paid_social | google / cpc | iguais | ok |
| utm_campaign | nome da campanha, prefixo grad_ | nome da campanha, prefixo grad_ | igual | ok |
| utm_content | conceito_formato_gancho_vN (a_v1) | conceito_formato_gancho_vN (a_v1); sitelinks sl-..._sitelink_a_v1 | conceito_formato_vN (sem bloco de gancho) | Meta e Google ok; criativos e gestor 4.2 e 4.6 ainda no padrão antigo (nota da seção 5) |
| utm_term | público | {keyword}; "sitelink" nos sitelinks | igual | não regulado por D11 e D12; ok |
| URL base | faculdade.ufape.com.br/graduacao e /graduacao/pedagogia, sem https:// | https://faculdade.ufape.com.br/graduacao | sem https:// | [CONFIRMAR, G13] nos três (recomendação R-M2) |

Meta e Google estão coerentes entre si. Nenhum dado pessoal em UTM.

### 2.5 Travas (item 5)

| Trava | A1 Meta | A2 Google |
|---|---|---|
| G6 Pedagogia | ok (L251, AM7) | não se aplica (Pedagogia fora) |
| G7 textos dos Editais 003/2026 | **ausente** (M-1) | ok (L465, L521, AG3) |
| G8 noturno | ok (L252, AM6) | ok (L463, AG11, negativas de turno) |
| G12 reajuste | ok no checklist (L224) e na tabela (L253) | ok (L464) |
| G13 URL, formulário, CRM | ok (L254) | ok (L467) |
| G14 aprovador | ok (L7, L255) | ok (L468, L530) |
| Datas do Enem | trava ok (L256); **data dada como fato em L233** (M-5) | ok, sempre com [CONFIRMAR no calendário oficial do Inep] (L87, L466) |

### 2.6 Aprovação humana e regras de plataforma (item 6)

- Ações: toda subida, troca, pausa, verba e limite está em AM1 a AM11 e AG1 a AG11, com o que, por que, quanto, efeito e como desfazer. Ok nos dois.
- Regras de plataforma sem fonte e sem marca: A1 L91 (M-4); A2 L67, L205 e L212 (G-1). As demais estão marcadas ([CONFIRMAR] ou [SUPOSIÇÃO]).

### 2.7 Travessão e meia-risca (item 7)

Busca de U+2014 e U+2013 (e de U+2012 e U+2015): **0 ocorrências** nos dois arquivos.

---

## 3. Correções obrigatórias

### A1 anuncios-meta (CORRIGIR)

| # | Onde | Problema | Correção |
|---|---|---|---|
| M-1 | L27 (resumo), L187 (6.4), L217 a L225 (checklist), L247 a L259 (travas), L268 e L269 (AM2 e AM3) | A trava G7 (correção dos Editais 003/2026 e aprovação do texto do desconto pela regulação) não aparece no arquivo. Com isso, v1-preco entra no primeiro teste em 16/11 e v4-ato, p3-preco e p4-ato também podem subir sem ela. O Google bloqueia os anúncios de preço por G7 (L465) e o criativos exige G7 para INT-V1 (criativos L815 e L895): a mesma regra de desconto ficaria liberada num canal e bloqueada no outro | Incluir G7 na tabela de travas (efeito: nenhum anúncio com preço ou desconto sobe), no checklist "Antes de montar", em AM2 e AM3 e no status de v1-preco, v4-ato, p3-preco e p4-ato. Escrever o teste alternativo da fase 1 se G7 ou G12 não estiverem respondidos em 13/11 (por exemplo, v3-entrada e v2-pratica, com o terceiro conceito entrando depois) |
| M-2 | L49, L91, L112, L225, L228, L240, L275 (AM9) | A trava de gasto não fecha com o mapa de campanhas. (a) L91 e L228 põem o limite de gasto da campanha "igual ao total da fase", mas _202611 cobre as fases 1 e 2 (L46) e pararia em R$ 450,00, sem os R$ 225,00 da fase 2. (b) L49 diz que _202701 é da fase 3 e L240 diz que ela segue em fevereiro; a fase 4 (R$ 240,00) não tem campanha ampla definida e só tem o remarketing, que depende de público mínimo. (c) L225 e AM9 põem o limite da conta da Meta em R$ 4.000,00, que inclui os R$ 560,00 do Google: a Meta da Medicina Veterinária poderia passar de R$ 1.440,00 e o curso de R$ 2.000,00; se a conta também tiver campanhas de Pós, o limite da conta nem serve como trava [CONFIRMAR] | Limite por campanha igual à soma das fases que ela cobre: _202611, R$ 675,00 (fases 1 e 2, menos o que for para o remarketing de 202612); _202701, R$ 525,00 ou R$ 765,00 se seguir na fase 4; dizer qual campanha recebe os R$ 240,00 da fase 4 quando não houver público de remarketing. Pedagogia na mesma lógica. Trocar "R$ 4.000,00" por "R$ 1.440,00 na Medicina Veterinária e R$ 2.000,00 na Pedagogia, somados por limite de campanha (R$ 3.440,00 na Meta)" |
| M-3 | L81, L83, L272 (AM6), contra L113 | L81 e AM6 dizem "metade da verba semanal do curso"; a verba semanal do curso inclui o Google (S1: R$ 200,00), e metade dela daria R$ 100,00 ao noturno na Meta, com a Meta acima de R$ 150,00. L83 e AM6 põem o noturno no ar "no dia seguinte a MP8", e L113 (e gestor 3.3) dividem a verba "a partir da semana seguinte": a semana do desbloqueio fica sem diária definida | Escrever "metade da verba semanal da Meta do curso (seção 4)" e fazer o noturno subir na segunda-feira seguinte a MP8, quando a divisão 50% e 50% começa; ou dizer de onde sai a diária dos dias anteriores, sem passar do total da semana |
| M-4 | L91 | "A Meta pode gastar até 25% a mais num dia" é regra de plataforma sem fonte e sem marca | Marcar [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda da Meta] e levar para a Lista 2 |
| M-5 | L233 | "Enem de 08 e 15/11" aparece como fato; a própria tabela de travas (L256), o Google (L87) e o estrategia (L315 e L318) tratam as datas como informadas e a confirmar | Escrever "08 e 15/11, datas informadas do Enem 2026 [CONFIRMAR no calendário oficial do Inep]" |

### A2 anuncios-google (APROVADO com ajustes)

| # | Onde | Problema | Correção |
|---|---|---|---|
| G-1 | L67, L205, L212 | Regras de plataforma sem fonte e sem marca: L67 "o Google só tem orçamento por campanha" (contradiz o orçamento compartilhado proposto em L124 e AG2); L205 "até 15 títulos e 4 descrições por anúncio"; L212 a "Força do anúncio" que fica em "Média" ou "Ruim" com fixações | L67: "orçamento por campanha (ou compartilhado, só no item de reserva do AG2)"; marcar L205 e L212 com [SUPOSIÇÃO, CONFIRMAR no editor] e acrescentar à Lista 2 |
| G-2 | L391 e L538 (AG5) | L391 diz "anúncio só para 18 anos ou mais" e, na mesma linha, "não excluir a faixa desconhecida", que pode incluir menores. A escolha fica fora do pedido AG5, que só fala em "idade 18 ou mais" | Levar a decisão para o AG5, com as duas opções (excluir ou não a faixa "desconhecida"), o efeito de cada uma no alcance e a validação do jurídico (G10). Até a resposta, valer a opção mais restrita (falha fechada) |

---

## 4. Recomendações (não bloqueiam)

| # | Arquivo e linha | Recomendação |
|---|---|---|
| R-M1 | A1 L154, L168, L181 (título "Use sua nota do Enem" no ar desde 16/11) | O Google proíbe "sua nota" até a semana E (L466, trava 5b) e a Meta usa no título desde a fase 1. O texto traz "de 2010 em diante" e o qa-d aprovou o conceito, mas a regra precisa ser uma só. Pedir ao cmo que decida; sugestão até a semana E: título "Enem de 2010 em diante" |
| R-M2 | A1 L199, L200, L202, L203 | Usar "https://" na URL base, como o Google (L441) |
| R-M3 | A1 seção 8 | Pôr data de término 21/02/2027 em cada campanha, como segunda trava (igual ao Google, L88) |
| R-M4 | A1 L129 | Posicionamentos automáticos podem incluir Audience Network e Messenger [SUPOSIÇÃO]; dizer se ficam ou saem |
| R-M5 | A1 L190 | "Aprendizado limitado" vem do gestor 3.5; citar a fonte e o [CONFIRMAR] dele |
| R-M6 | A1 L157 a L160 | A fase 3 do criativos (2.6) troca também a abertura, e ela traz Enem sem "2010 em diante" na linha visível (a arte e o complemento trazem). Escrever a abertura da fase 3 com a condição completa |
| R-M7 | A1 seção 6 | contexto/graduacao.md pede "citar sempre o ato regulatório"; hoje o ato só está em v4-ato e p4-ato. Lido como "quando citar, como no catálogo" [SUPOSIÇÃO de leitura]; se o cmo ler como "em toda peça", incluir B-ATO-INT ou B-ATO-PED no complemento de todos os anúncios |
| R-G1 | A2 L351, L354 | Sitelinks para PDF: conferir no item 14 do checklist se o PDF mostra contato e política de privacidade (conformidade, PLATAFORMAS); se não, destino na LP |
| R-G2 | A2 L522 | Dizer o valor do limite: R$ 560,00 nas duas campanhas (conta compartilhada com a Pós [CONFIRMAR]) |
| R-G3 | A2 L7 | "Etapa 4" aqui e "etapa 5" na Meta (L6); alinhar com o workflow |

---

## 5. Notas para arquivos de outros donos (não alterados)

- criativos-de-anuncio-graduacao: utm_content e nomes ainda sem bloco de gancho (A-C1); abertura da fase 3 sem "2010 em diante" na linha visível (R-M6).
- gestor-de-midia-graduacao: 4.2 e 4.6 ainda com conceito_formato_versão (sem bloco de gancho; AM10 e conflito 2 do Google pedem a troca); 4.8 com limite de conta de R$ 4.000,00 (mesmo ponto de M-2); confirmar a divisão 30% e 70% (40% e 60%) entre marca e genérica proposta no Google.

---

## 6. Auditorias

### 6.1 auditorias/11-midia-paga.md

| Item | A1 Meta | A2 Google |
|---|---|---|
| Plano do gestor aprovado, canais justificados | pendente (MP1 a MP4), fora deste QA | idem |
| Metas de CPL e custo por matrícula antes de subir | ok no texto (L38); aprovação MP1 | ok (seção 12) |
| Verba dentro do aprovado, com aprovador | **falha** na trava de gasto (M-2); aprovador G14 | ok na soma; aprovador G14 |
| Nomenclatura padrão | ok (D12 com gancho) | ok |
| UTMs completas e origem no CRM | ok; URL e CRM em G13 | ok; URL e CRM em G13 |
| Pixel, API de Conversões e conversões do Google | pendente, [DADO NÃO FORNECIDO] | pendente, [DADO NÃO FORNECIDO] |
| Criativos aprovados na conformidade | ok (qa-d), mas preço sem G7 (M-1) | ok |
| Políticas de anúncio da plataforma | ok | ok |
| Nenhum público com menores de 18 | ok | ajuste (G-2) |
| Docente promovido ou Spark Ad | não se aplica | não se aplica |
| Relatório semanal ao CMO | a partir de 23/11 | a partir de 23/11 |
| Sem segmentação discriminatória | ok | ok |
| Públicos sem dado pessoal sem base legal | ok (listas bloqueadas, MP7) | ok (importação só por gclid, depois do jurídico) |
| Dados de curso do catálogo | ok | ok |
| Destino de WhatsApp oficial | não se aplica | não se aplica (sem chamada) |
| Números só das fontes | ok | ok |
| Nenhuma alteração sem humano | ok | ok |

### 6.2 auditorias/conformidade-educacional.md

| Item | A1 Meta | A2 Google |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | ok (Pedagogia sem CH, G5) | ok |
| Status "aberto" | ok (2 abertos) | ok |
| Modalidade presencial clara | ok | ok |
| Ato de Graduação como no catálogo | ok | ok |
| Pós lato sensu e curso livre | não se aplica | não se aplica |
| Nota MEC | ausente, ok | ausente, ok |
| Sem promessa de emprego, salário ou aprovação | ok | ok (termos também negativados) |
| Empregabilidade e superlativos | não há | não há |
| Comparação com concorrente | não há | não há (sem lance em concorrente) |
| Preço com valor, parcelas e condições | ok no texto; **liberação sem G7** (M-1) | ok; bloqueado por G7 e G12 |
| Desconto com regra, público e validade | ok (blocos B-DESC) | ok (D1 fixada, D2, SL5) |
| Urgência real | ok | ok |
| Prouni, Fies, financiamento | não aparecem | não aparecem |
| Autorização de imagem | sem pessoas; docentes com autorização (decisões 8 e 10) | não se aplica |
| Menores só com autorização | sem imagem de menor | não se aplica |
| Formulário com finalidade e privacidade | [CONFIRMAR, G13] | [CONFIRMAR, G13] |
| Consentimento de WhatsApp e e-mail | não se aplica | não se aplica |
| Nenhum dado pessoal | ok | ok |
| Políticas de Meta e Google, sem segmentação discriminatória | ok | ok |
| Página entrega o que o anúncio promete | [CONFIRMAR, G13]; noturno G8 e Pedagogia G6 travados | [CONFIRMAR, G13]; PDFs em R-G1 |
| Sem característica pessoal de quem vê | ok | ok |
| Sem urgência falsa ou elemento falso | ok | ok |
| Sem pessoa pública ou parceria falsa | ok | ok |
| Sem caixa alta excessiva ou símbolos | ok (Google em iniciais maiúsculas, sem exclamação) | ok |
| Página de destino carrega e mostra dados da Ufape | conferência humana no checklist | conferência humana (item 14) |
| Sem sugestão para driblar a análise | ok | ok (recursos automáticos desligados) |

Resultado: A1 **Bloqueado** até M-1 a M-5. A2 **Aprovado com ajustes** G-1 e G-2, conferidos antes da montagem. Revisado por: qa-de-marketing (agente). Revisão humana: pendente (G14). Data: 27/10/2026.

---

## Lista 1. Fatos (com fonte)

- Inscrição gratuita; redação online eliminatória, nota mínima 5,0; Enem com média mínima de 300 pontos, edições de 2010 em diante; aulas em 22/02/2027; turma mínima de 30 com devolução da 1ª parcela; devolução de 80% até 2 dias antes das aulas; menor precisa do aceite do representante legal (contexto/cursos/graduacao/editais-2027-1.md).
- Preços, percentuais, turnos, durações e atos da Medicina Veterinária e da Pedagogia (contexto/catalogo-de-cursos.md, seção 1).
- Verba R$ 2.000,00 por curso (decisão 15); Medicina Veterinária R$ 1.440,00 na Meta e R$ 560,00 no Google; Pedagogia R$ 2.000,00 na Meta; semanas S1 a S14 e fases (gestor-de-midia v3, 3.2 e 3.3).
- D11 (meta e paid_social; google e cpc) e D12 (prefixo grad_; conceito_formato_gancho_vN) (cmo-geral, 12.7).
- G7 bloqueia preço e desconto no criativos (L815, L895) e no Google (L465).
- Recontagem do Google: 100 itens, 0 divergências, 0 acima do limite (script citado no cabeçalho).
- 0 ocorrências de U+2014 e U+2013 nos dois arquivos.
- 16/11/2026 e 22/02/2027 são segundas-feiras; 08 e 15/11/2026 são domingos (calendário).

## Lista 2. Suposições

- [SUPOSIÇÃO] A conta da Meta e a do Google podem ter campanhas de outras linhas, o que tira o valor do limite de gasto da conta como trava da Graduação.
- [SUPOSIÇÃO de leitura] "Citar sempre o ato" (contexto/graduacao.md) lido como "quando citar, como no catálogo" (R-M7).
- [SUPOSIÇÃO] Posicionamentos automáticos da Meta incluem Audience Network e Messenger (R-M4).
- [SUPOSIÇÃO] O limite de cerca de 40 e 30 caracteres da Meta, usado só como referência na recontagem extra.

## Lista 3. Dados que faltam

- [CONFIRMAR] G7, G12, G13, G14, MP1, MP2, MP4, MP10 e MP15 antes de qualquer subida.
- [CONFIRMAR] Datas do Enem 2026 e da divulgação das notas no calendário oficial do Inep.
- [CONFIRMAR] Com o jurídico (G10): faixa etária "desconhecida" no Google e anúncio de busca visto por menor.
- [CONFIRMAR] Se as contas de anúncio são só da Graduação ou compartilhadas com a Pós.
- [CONFIRMAR] Com o cmo: uso de "sua nota do Enem" antes da semana E (R-M1).
- [DADO NÃO FORNECIDO] Estado do pixel, da API de Conversões e das conversões do Google; volume e CPC das palavras.

---

## Próximo passo

A1 volta ao **anuncios-meta** para M-1 a M-5 (conferência só desses itens). A2 segue para a **aprovação humana** (AG1 a AG11), com G-1 e G-2 entrando na próxima versão e conferidos pelo qa antes da montagem de 11 a 13/11/2026. Nada é publicado, enviado ou pago sem aprovação humana.
