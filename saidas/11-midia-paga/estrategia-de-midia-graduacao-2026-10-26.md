# Plano de mídia detalhado: Graduação 2027/1 (Medicina Veterinária e Pedagogia)

- Agente: estrategia-de-midia (departamento 11, Mídia Paga, por encomenda do gestor-de-midia)
- Linha: graduacao
- Data: 26/10/2026 (segunda-feira)
- Workflow: /campanha-de-vestibular, etapa 4 de 8 (plano detalhado por semana, encomendado na seção 6 do plano do gestor-de-midia)
- Liberações cobertas:
  - G1: Edital nº 002/2026 (Vestibular 2027) + Graduação em Medicina Veterinária, São Paulo. G1a integral; G1b noturno
  - G2: Edital nº 004/2026 (Processo Seletivo 2027.1 Goiânia) + Graduação em Pedagogia, Goiânia, noturno
- Status: rascunho para aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda ação em gerenciador de anúncios é feita por humano, depois da aprovação.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (seção 1, Graduação)
  - contexto/cursos/graduacao/editais-2027-1.md
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - .claude/skills/metas-de-custo/SKILL.md
  - saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (encomenda principal)
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md
  - auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md
- Regra de fonte: preço, turno, duração, modalidade e ato vêm do catálogo (seção 1); datas, vagas, turma mínima e regras de desconto vêm da ficha dos editais 2027/1. Não existe verba, meta acima do piso, histórico de CPL, exportação de plataforma nem número de CRM: tudo isso é [CONFIRMAR] ou [DADO NÃO FORNECIDO]. Nenhum benchmark de mercado é usado. Nenhum dado pessoal neste arquivo.
- Decisões do gestor-de-midia respeitadas sem alteração: canais ativos (Meta e Google Search; YouTube e TikTok condicionados só no integral; LinkedIn fora), bloqueio do noturno (G8 e MP4) e da Pedagogia (G6, MP4 e MP1), públicos só 18 anos ou mais, cenário conservador como meta oficial, percentuais por fase (seção 3.2 dele) e por canal (seção 3.3 dele), nomenclatura (4.2), UTM (4.6), protocolo de teste (4.7) e critérios (5).

---

## 0. Resumo em cinco linhas

1. Verba total da Graduação: **VT = [CONFIRMAR]** (MP2). Este plano entrega só percentuais de VT e fórmulas.
2. Divisão por curso proposta, proporcional ao teto de receita do 1º semestre de cada recorte: integral 52,5%, noturno 42,0%, Pedagogia 5,5% de VT [SUPOSIÇÃO de desenho, aprovação EM1].
3. Metas: CPL e custo por matrícula do cenário conservador, escritos como fórmula antes da subida; cada fase lê a etapa do funil que já dá para medir naquela fase (lead, inscrito, avaliado, matrícula).
4. Calendário: subida do integral em 16/11/2026 (dia seguinte ao 2º domingo do Enem), noturno e Pedagogia no dia seguinte ao desbloqueio, pesos semanais ligados à divulgação das notas do Enem e ao resultado do Sisu, pausa geral em 22/02/2027.
5. Realocação semanal só dentro da verba aprovada, com teto de 20% por semana por campanha e decisão do cmo quando mexe em recorte ou canal.

---

## 1. Funil reverso e metas de custo (skill metas-de-custo, cenário conservador)

### 1.1 Variáveis (as mesmas do gestor-de-midia, seção 2.1)

| Símbolo | O que é | Valor | Fonte |
|---|---|---|---|
| T1 | Receita do 1º semestre de 2027 com desconto, por matrícula | Integral R$ 30.000,00; noturno R$ 24.000,00; Pedagogia R$ 3.150,00 | Editais 003/2026 (aritmética: 6 x R$ 5.000,00; 6 x R$ 4.000,00; 6 x R$ 525,00) |
| k1c | Fração de T1 que de fato entra, versão conservadora | [CONFIRMAR] | financeiro |
| V | Custo variável por aluno no 1º semestre | [CONFIRMAR] | financeiro |
| Md | Margem desejada por matrícula | [CONFIRMAR] | diretoria |
| t1 a t5 | Passagens lead para inscrito, inscrito para avaliado, avaliado para aprovado, aprovado para matriculado, matriculado ativo em 22/02/2027 (conservadoras) | [CONFIRMAR] | CRM, números agregados |
| tc | t1 x t2 x t3 x t4 x t5 | [CONFIRMAR] | conta |
| M_r | Matrículas que a mídia paga precisa trazer no recorte r | [CONFIRMAR] (piso de 30 por turma menos base e orgânico) | cmo e CRM |
| B_r | Leads, inscritos, avaliados e aprovados que já estão na base desde 17/08/2026 | [CONFIRMAR] | CRM, agregado |

### 1.2 Metas oficiais (conservador, n = 0)

| Meta | Fórmula | Integral | Noturno | Pedagogia |
|---|---|---|---|---|
| Custo por matrícula máximo | CPMmax_r = T1_r x k1c menos V menos Md | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| CPL máximo | CPLmax_r = CPMmax_r x tc_r | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Teto absoluto do custo por matrícula (k1 = 1, V = 0, Md = 0; não é meta) | T1_r | R$ 30.000,00 | R$ 24.000,00 | R$ 3.150,00 |
| CPL teto a cada 1 ponto percentual de tc (não é meta) | T1_r x 0,01 | R$ 300,00 | R$ 240,00 | R$ 31,50 |
| Limite de revisão da campanha | 1,3 x CPLmax_r por 2 semanas seguidas, ou custo por matrícula acumulado acima de CPMmax_r a partir de C2 (04/01/2027) [regra prática, não meta] | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |

Regra: estes valores são preenchidos e aprovados (MP1) antes de qualquer subida com escala. Depois que a campanha sobe, não são reescritos para caber no resultado. Base e otimista servem só para saber até onde a verba poderia ir; nunca viram meta.

### 1.3 Funil reverso por recorte (conta de trás para frente)

| Etapa | Fórmula | Integral | Noturno | Pedagogia |
|---|---|---|---|---|
| Matrículas ativas da mídia | M_r | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Matrículas brutas | M_r / t5 | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Aprovados | matrículas brutas / t4, menos aprovados na base | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Avaliados (redação feita ou nota do Enem enviada) | aprovados / t3, menos avaliados na base | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Inscritos | avaliados / t2, menos inscritos na base | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Leads necessários | L_r = inscritos / t1 | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Leads por semana necessários | L_r / semanas ativas do recorte (14 no integral, de 16/11/2026 a 21/02/2027; menos no noturno e na Pedagogia, contadas do desbloqueio até a data de corte da seção 4.4) | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Verba teto do recorte | VerbaTeto_r = M_r x CPMmax_r | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] |
| Verba que o plano destina | VT x share_r (seção 2.1) | VT x 52,5% | VT x 42,0% | VT x 5,5% |
| A verba destinada cabe no teto? | VT x share_r menor ou igual a VerbaTeto_r | sim / não | sim / não | sim / não |
| A verba compra os leads necessários? | VT x share_r / CPLmax_r maior ou igual a L_r | sim / não | sim / não | sim / não |

Leitura:
- Se a verba destinada passar do teto, o excedente não é gasto e o gestor-de-midia avisa o cmo (a matrícula não paga a mídia no horizonte conservador).
- Se a verba não comprar os leads necessários, o plano não entrega a meta com essa verba: aviso ao cmo antes de subir. Pedido de verba extra, se houver, vai separado ao gestor-de-midia, marcado como pedido de aprovação (EM9).

### 1.4 Metas por fase (a mesma meta conservadora, lida na etapa que a fase já consegue medir)

Motivo: a matrícula só acontece depois de inscrição, avaliação e resultado. Nas primeiras fases o custo por matrícula ainda não existe; a meta da fase é o custo máximo da etapa do funil derivado do mesmo CPMmax conservador. Nenhuma meta nova é criada: são frações da mesma conta.

| Fase | Datas | Indicador principal de custo | Fórmula da meta (conservador) | Indicador de qualidade |
|---|---|---|---|---|
| 1. Captação | 16/11 a 06/12/2026 | CPL | CPL observado menor ou igual a CPLmax_r = CPMmax_r x t1 x t2 x t3 x t4 x t5 | t1 observada (lead para inscrito) maior ou igual à t1 conservadora |
| 2. Aquecimento | 07/12/2026 a 03/01/2027 | Custo por inscrito | CPI observado menor ou igual a CPImax_r = CPMmax_r x t2 x t3 x t4 x t5 | t2 observada (inscrito para avaliado) |
| 3. Inscrições abertas (conversão) | 04/01 a 31/01/2027 | Custo por avaliado | CPAvmax_r = CPMmax_r x t3 x t4 x t5 | t3 e t4 observadas |
| 4. Reta final | 01/02 a 21/02/2027 | Custo por matrícula acumulado do recorte | gasto acumulado do recorte / matrículas atribuídas menor ou igual a CPMmax_r | t5 (sem cancelamento até 20/02/2027) |
| Todas | 16/11/2026 a 21/02/2027 | CPL | CPL menor ou igual a CPLmax_r em toda semana | tc mínima = CPL observado / CPMmax_r (fórmula 11 do gestor) |

Atribuição: o custo de cada etapa usa o gasto acumulado do recorte desde a subida dividido pelas etapas acumuladas com origem paga no CRM (utm_source meta, google ou tiktok). Origem sem UTM não entra na conta da mídia nem é retirada dela sem investigar (seção 6, linha "Investigar").

---

## 2. Divisão da verba por curso, canal e fase (percentual de VT)

### 2.1 Divisão por curso

| Recorte | Share de VT | Como foi calculado | Status |
|---|---|---|---|
| G1a Medicina Veterinária integral | 52,5% | T1 / soma dos T1 = 30.000 / 57.150 | Ativo, sobe 16/11/2026 |
| G1b Medicina Veterinária noturno | 42,0% | 24.000 / 57.150 | Bloqueado até G8 e MP4 (MP8) |
| G2 Pedagogia | 5,5% | 3.150 / 57.150 | Bloqueado até G6, MP4 e MP1 (MP9) |

[SUPOSIÇÃO de desenho, aprovação EM1] A proporção usa o teto de receita do 1º semestre com a mesma meta de 30 matrículas por turma (piso do edital) e a mesma k1, V e Md relativas. Quando MP1 trouxer os números, a divisão definitiva passa a ser share_r = VerbaTeto_r / soma das VerbaTeto, recalculada uma vez, antes da subida, e nunca depois para caber no resultado.

Verba de recorte bloqueado: fica reservada. Não é remanejada para outro recorte sem aprovação (MP2 do gestor). Se o recorte não for desbloqueado até a data de corte (seção 4.4), a reserva vira economia; só um humano pode decidir usá-la em outro recorte, com pedido de aprovação ao cmo.

### 2.2 Integral: percentual de VT por fase e canal

Fases (gestor 3.2): 30%, 15%, 35%, 20% da verba do recorte. Canais (gestor 3.3). Arredondamento em duas casas; a soma pode variar 0,01.

| Fase | % de VT na fase | Meta | Google Search | YouTube | TikTok |
|---|---|---|---|---|---|
| 1. Captação | 15,75% | 9,45% | 3,94% | 0,00% | 2,36% (só com MP5; sem MP5 vai para a Meta) |
| 2. Aquecimento | 7,88% | 4,33% | 1,58% | 1,18% (só com MP6; sem MP6 vai para a Meta) | 0,79% (só se o teste passou; se não, Meta) |
| 3. Conversão | 18,38% | 10,11% | 6,43% | 0,00% | 1,84% (só se o teste passou; se não, Meta) |
| 4. Reta final | 10,50% | 5,25% | 5,25% | 0,00% | 0,00% |
| Total integral | 52,50% | 29,14% | 17,20% | 1,18% | 4,99% |

### 2.3 Noturno: percentual de VT por fase e canal (Meta 60%, Google Search 40%)

| Fase | Se desbloqueado até 16/11 | Meta | Google Search | Se desbloqueado depois de 16/11 (parte da fase 1 vai para a fase 3) | Meta | Google Search |
|---|---|---|---|---|---|---|
| 1. Captação | 12,60% | 7,56% | 5,04% | 0,00% | 0,00% | 0,00% |
| 2. Aquecimento | 6,30% | 3,78% | 2,52% | 6,30% (só a partir da semana do desbloqueio) | 3,78% | 2,52% |
| 3. Conversão | 14,70% | 8,82% | 5,88% | 27,30% | 16,38% | 10,92% |
| 4. Reta final | 8,40% | 5,04% | 3,36% | 8,40% | 5,04% | 3,36% |
| Total | 42,00% | 25,20% | 16,80% | 42,00% | 25,20% | 16,80% |

Trava: a parte que vai da fase 1 para a fase 3 só é gasta se a campanha passar no critério de escala (seção 6); o que não couber no limite de 20% de aumento por semana não é forçado e vira economia. Semanas do aquecimento anteriores ao desbloqueio também viram economia, nunca gasto acumulado depois.

### 2.4 Pedagogia: percentual de VT por fase e canal (Meta 75%, Google Search 25% se a busca for aprovada; sem busca, 100% Meta)

| Fase | % de VT na fase | Meta | Google Search (condicionado) |
|---|---|---|---|
| 1. Captação | 1,65% | 1,24% | 0,41% |
| 2. Aquecimento | 0,83% | 0,62% | 0,21% |
| 3. Conversão | 1,93% | 1,44% | 0,48% |
| 4. Reta final | 1,10% | 0,83% | 0,28% |
| Total | 5,50% | 4,13% | 1,38% |

Mesma regra do noturno para desbloqueio depois de 16/11: a parte da fase 1 passa para a fase 3, com a mesma trava.

### 2.5 Peso de cada semana dentro da fase [SUPOSIÇÃO de desenho, aprovação EM3]

| Fase | Semana (segunda a domingo) | Peso na fase | Motivo |
|---|---|---|---|
| 1 | S1 16/11 a 22/11 | 33,3% | Primeira semana depois do 2º dia do Enem (15/11); aprendizado |
| 1 | S2 23/11 a 29/11 | 33,3% | Teste dos conceitos |
| 1 | S3 30/11 a 06/12 | 33,4% | C1 em 30/11 |
| 2 | S4 07/12 a 13/12 | 30% | Remarketing começa |
| 2 | S5 14/12 a 20/12 | 30% | Possível reajuste de dezembro [CONFIRMAR, G12] |
| 2 | S6 21/12 a 27/12 | 20% | Natal [SUPOSIÇÃO: menor atenção] |
| 2 | S7 28/12 a 03/01 | 20% | Ano-novo [SUPOSIÇÃO: menor atenção] |
| 3 | S8 04/01 a 10/01 | 25% (base) | C2 em 04/01 |
| 3 | S9 11/01 a 17/01 | 25% (base) | |
| 3 | S10 18/01 a 24/01 | 25% (base) | |
| 3 | S11 25/01 a 31/01 | 25% (base) | C3 em 25/01 |
| 4 | S12 01/02 a 07/02 | 40% | Primeira semana da reta final |
| 4 | S13 08/02 a 14/02 | 30% | Carnaval de 2027 nesta semana [SUPOSIÇÃO: confirmar no calendário] |
| 4 | S14 15/02 a 21/02 | 30% | Última semana antes das aulas |

Regra da sazonalidade do Enem e do Sisu na fase 3 (substitui o peso base quando as datas forem confirmadas):
- E = semana da divulgação das notas do Enem 2026 [CONFIRMAR no calendário oficial do Inep; SUPOSIÇÃO: em ciclos anteriores as notas saíram em janeiro].
- S = semana do resultado da chamada regular do Sisu [CONFIRMAR no calendário oficial do MEC; SUPOSIÇÃO: janeiro ou início de fevereiro].
- Se E e S caem em semanas diferentes da fase 3: 30% para a semana E, 30% para a semana S, 20% para cada uma das outras duas.
- Se E e S caem na mesma semana: 35% nela, 25% na seguinte, 20% nas outras duas.
- Se S cair na fase 4: a semana S recebe 40% da fase 4 e as outras duas 30% cada.
- Se E cair antes de 04/01: o peso base da fase 3 se mantém e a semana E da fase 2 recebe 40% da fase 2, com as outras três divididas igualmente.
- A troca de pesos nunca muda o total da fase nem o total aprovado.

### 2.6 Integral: percentual de VT por semana e canal (pesos base; refazer com E e S confirmados)

| Semana | Total da semana | Meta | Google Search | YouTube | TikTok |
|---|---|---|---|---|---|
| S1 a S3 (cada) | 5,25% | 3,15% | 1,31% | 0,00% | 0,79% |
| S4 e S5 (cada) | 2,36% | 1,30% | 0,47% | 0,35% | 0,24% |
| S6 e S7 (cada) | 1,58% | 0,87% | 0,32% | 0,24% | 0,16% |
| S8 a S11 (cada) | 4,59% | 2,53% | 1,61% | 0,00% | 0,46% |
| S12 | 4,20% | 2,10% | 2,10% | 0,00% | 0,00% |
| S13 e S14 (cada) | 3,15% | 1,58% | 1,58% | 0,00% | 0,00% |

Fórmula geral, para qualquer recorte r, canal c e semana s: **Verba(r, c, s) = VT x share_r x fase% x canal% x peso_s**. Verba diária sugerida = Verba(r, c, s) / 7. Leads por semana que a verba compra = Verba(r, c, s) / CPLmax_r.

### 2.7 Condição de volume (regra prática do gestor, seção 2.5, não meta)

Um canal só fica ativo se, nas 3 semanas da fase 1, a verba dele cobrir pelo menos 1,5 x CPLmax por conceito ativo. Isso dá a VT mínima, em múltiplos do CPLmax do recorte, para cada canal fazer sentido:

| Recorte e canal | % de VT na fase 1 | Conceitos ativos | VT mínima para o canal |
|---|---|---|---|
| Integral, Meta | 9,45% | 3 | VT maior ou igual a 47,6 x CPLmax_integral |
| Integral, Google Search | 3,94% | 3 (um por conceito nos anúncios responsivos) | VT maior ou igual a 114,2 x CPLmax_integral |
| Integral, TikTok | 2,36% | 2 vídeos | VT maior ou igual a 127,1 x CPLmax_integral |
| Noturno, Meta | 7,56% | 3 | VT maior ou igual a 59,5 x CPLmax_noturno |
| Noturno, Google Search | 5,04% | 3 | VT maior ou igual a 89,3 x CPLmax_noturno |
| Pedagogia, Meta | 1,24% | 4 | VT maior ou igual a 483,9 x CPLmax_pedagogia |
| Pedagogia, Google Search | 0,41% | 2 | VT maior ou igual a 731,7 x CPLmax_pedagogia |

Conta: VT x % da fase 1 maior ou igual a conceitos x 1,5 x CPLmax. Se a condição não fechar: o canal sai e a verba dele vai para a Meta do mesmo recorte (integral e noturno); na Pedagogia, primeiro sai a busca; se nem a Meta fechar, sobe só com 2 conceitos (p1-noite e p3-preco) e a leitura fica com o orgânico e o WhatsApp, com aviso ao cmo. Recorte desbloqueado depois de 16/11 faz a mesma conta sobre as 3 primeiras semanas no ar.

---

## 3. Estrutura de campanhas por canal e fase

Modelos (gestor 4.1): integral e noturno em lançamento por fases com teste e escala; Pedagogia local e enxuta. Orçamento sempre na campanha, nunca no conjunto também. Nomes no padrão linha_curso_plataforma_objetivo_publico_AAAAMM; conjunto = campanha + "__" + público; anúncio = conceito_formato_versão (igual ao utm_content).

### 3.1 Regras de público e exclusão que valem para toda campanha

- Idade 18 anos ou mais em todo conjunto, grupo e público, em todas as plataformas. Nenhum público semelhante, de remarketing ou de vídeo configurado para menores.
- Sem interesses, sem segmentação ou exclusão por emprego, renda, saúde, religião, orientação sexual ou origem. Público amplo por região; o criativo seleciona.
- Sem listas de contatos (base de inscritos, matriculados ou semelhantes) até MP7. Exclusão de quem já converteu só por evento do pixel ou da tag (visitante que disparou o evento de cadastro), sem dado pessoal carregado na plataforma [SUPOSIÇÃO de desenho, aprovação EM7].
- Região: integral e noturno, Grande São Paulo [SUPOSIÇÃO, área a confirmar com o comercial]; Pedagogia, Goiânia e região metropolitana [SUPOSIÇÃO, raio a confirmar com o comercial de Goiânia; cuidado com raio pequeno demais].
- YouTube: conteúdo feito para crianças e canais infantis excluídos; categorias de conteúdo sensível excluídas.
- Texto de anúncio nunca afirma situação de quem vê. Sem "últimas vagas", "vagas limitadas", contagem regressiva ou "termina hoje". Sem nota do MEC e sem frase de certificação. Desconto sempre com valor cheio, valor com desconto, "1º semestre de 2027" e "Condições e validade no edital" (ficha de oferta, seção 0.2).
- Sisu: a Ufape não aparece em nenhum texto de anúncio associada ao Sisu, porque os editais não preveem ingresso pelo Sisu. O resultado do Sisu é só gatilho de calendário. A forma de ingresso anunciada é "nota do Enem, média mínima de 300 pontos, edições de 2010 em diante" (Edital 002/2026 e 004/2026).

### 3.2 Destino e UTM

URL base [CONFIRMAR, G13]: faculdade.ufape.com.br/graduacao (Medicina Veterinária, integral e noturno) e faculdade.ufape.com.br/graduacao/pedagogia. A squad nunca altera a LP.

| Canal | utm_source | utm_medium | utm_campaign | utm_content | utm_term |
|---|---|---|---|---|---|
| Meta | meta | paid_social | nome da campanha | nome do anúncio | público |
| Google Search | google | cpc | nome da campanha | nome do anúncio | {keyword} |
| YouTube | google | cpc | nome da campanha | nome do anúncio | público |
| TikTok | tiktok | paid_social | nome da campanha | nome do anúncio | público |

Modelo: `<URL base>?utm_source=<source>&utm_medium=<medium>&utm_campaign=<campanha>&utm_content=<anúncio>&utm_term=<público ou {keyword}>`

### 3.3 G1a Medicina Veterinária integral: Meta (Instagram e Facebook)

| Fase | Campanha | Objetivo e evento | Conjunto e público | Exclusões | Anúncios | Exemplo de destino com UTM |
|---|---|---|---|---|---|---|
| 1 (16/11) | grad_medvet-integral_meta_cadastro_amplo18_202611 | Cadastros (evento de cadastro da LP; inscrição ou lead conforme G13) | __amplo18: 18+, Grande São Paulo, posicionamentos automáticos, sem interesses | Quem disparou o evento de cadastro nos últimos 180 dias (pixel) | v1-preco_feed-4x5_v1; v2-pratica_reels-9x16_v1; v3-entrada_stories-9x16_v1 (de 3 a 6, conceitos diferentes) | faculdade.ufape.com.br/graduacao?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_medvet-integral_meta_cadastro_amplo18_202611&utm_content=v2-pratica_reels-9x16_v1&utm_term=amplo18 |
| 2 (07/12) | a mesma campanha amplo18 continua (80% validados, 20% conceito novo) | Cadastros | __amplo18 | Idem | validados + 1 ou 2 conceitos novos (v4, v5 do criativos-de-anuncio) | idem, trocando utm_content |
| 2 (07/12) | grad_medvet-integral_meta_cadastro_rmk-lp30d_202612 | Cadastros | __rmk-lp30d: visitantes da LP nos últimos 30 dias, 18+ | Quem cadastrou (pixel); visitantes que chegaram por anúncio do noturno (URL contém medvet-noturno) [SUPOSIÇÃO de desenho, validar anuncios-meta] | v1-preco_feed-4x5 com regra completa na legenda; v3-entrada_stories-9x16 | ...utm_campaign=grad_medvet-integral_meta_cadastro_rmk-lp30d_202612&utm_content=v1-preco_feed-4x5_v2&utm_term=rmk-lp30d |
| 2 (07/12) | grad_medvet-integral_meta_engajamento_amplo18_202612 | Engajamento com vídeo (ThruPlay), para alimentar rmk-video50 | __amplo18 | Idem | v2-pratica_reels-9x16 (sem menor identificável, sem pessoa ou hospital sem autorização, G11) | ...utm_campaign=grad_medvet-integral_meta_engajamento_amplo18_202612&utm_content=v2-pratica_reels-9x16_v1&utm_term=amplo18 |
| 3 (04/01) | grad_medvet-integral_meta_cadastro_amplo18_202701 (escala) | Cadastros | __amplo18 | Idem | só conceitos validados; mensagem de redação online, nota do Enem e desconto com regra | ...utm_campaign=grad_medvet-integral_meta_cadastro_amplo18_202701&utm_content=v3-entrada_feed-4x5_v2&utm_term=amplo18 |
| 3 (04/01) | grad_medvet-integral_meta_cadastro_rmk-lp30d_202701 | Cadastros | __rmk-lp30d e __rmk-video50 (quem viu 50% do vídeo), 18+ | Quem cadastrou; cruzada com o noturno | validados + versão "sua nota do Enem pode ser a sua entrada" na semana E | ...utm_campaign=grad_medvet-integral_meta_cadastro_rmk-lp30d_202701&utm_content=v3-entrada_stories-9x16_v3&utm_term=rmk-video50 |
| 4 (01/02) | grad_medvet-integral_meta_cadastro_rmk-lp30d_202702 | Cadastros | __rmk-lp30d e __rmk-video50 | Quem cadastrou | passos da matrícula, aulas em 22/02/2027, documentos em até 30 dias; sem urgência sem número | ...utm_campaign=grad_medvet-integral_meta_cadastro_rmk-lp30d_202702&utm_content=v3-entrada_feed-4x5_v4&utm_term=rmk-lp30d |
| 4 (01/02) | campanha amplo18_202701 só segue se o CPL da fase 3 estiver até CPLmax; senão é pausada (proposta) e a verba vai para o remarketing e a busca da mesma fase | Cadastros | __amplo18 | Idem | validados | idem |

Pausas da Meta: amplo18_202611 em 03/01/2027 (substituída pela 202701); engajamento_202612 em 31/01/2027; rmk-lp30d_202612 em 03/01/2027; rmk-lp30d_202701 em 31/01/2027; todas em 22/02/2027 (MP13).

### 3.4 G1a integral: Google Search e YouTube

| Fase | Campanha | Objetivo e lance | Grupos e palavras (sementes, lista final pela pesquisa-de-palavras-chave e anuncios-google) | Exclusões | Anúncios | Exemplo de destino com UTM |
|---|---|---|---|---|---|---|
| 1 a 4 (16/11) | grad_medvet-integral_google_busca_marca_202611 | Conversões (cadastro); lance manual ou maximizar cliques até haver volume, depois por conversão [regra prática do gestor] | marca: "ufape veterinária", "faculdade ufape", "vestibular ufape" [SUPOSIÇÃO] | Faixa etária abaixo de 18 onde a plataforma permitir; negativas "noturno" e "pedagogia" (cruzadas) | v3-entrada_rsa_v1; v1-preco_rsa_v1 | faculdade.ufape.com.br/graduacao?utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_marca_202611&utm_content=v3-entrada_rsa_v1&utm_term={keyword} |
| 1 a 4 (16/11) | grad_medvet-integral_google_busca_generica_202611 | Conversões (cadastro) | faculdade de veterinária em SP; vestibular de veterinária 2027; veterinária com nota do Enem [SUPOSIÇÃO] | Negativas: "gratuita", "pública", "EAD", "concurso", "salário" [SUPOSIÇÃO do gestor]; "noturno" e "à noite" (vão para o noturno); "pedagogia" | v1-preco_rsa_v1; v2-pratica_rsa_v1; v3-entrada_rsa_v1 | ...utm_campaign=grad_medvet-integral_google_busca_generica_202611&utm_content=v2-pratica_rsa_v1&utm_term={keyword} |
| 3 (semana E e seguintes) | mesmo grupo "veterinária com nota do Enem", com verba da semana E | Conversões | termos com "nota do Enem" e "Enem 2026" + veterinária [SUPOSIÇÃO]. Termos com "Sisu" ficam fora por padrão (EM6) | Idem | v3-entrada_rsa_v2 com "Use sua nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)" | idem |
| 2 (07/12), só com MP6 | grad_medvet-integral_google_video_rmk-lp30d_202612 (YouTube) | Visualizações ou conversões em vídeo | rmk-lp30d (lista da tag), 18+ | Conteúdo feito para crianças, canais infantis, conteúdo sensível; quem converteu (tag) | v2-pratica_short-9x16_v1 (Shorts aprovados, G11) | faculdade.ufape.com.br/graduacao?utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_video_rmk-lp30d_202612&utm_content=v2-pratica_short-9x16_v1&utm_term=rmk-lp30d |

Sem Performance Max (gestor 3.1). YouTube pausado em 03/01/2027 (fim da fase 2).

### 3.5 G1a integral: TikTok (teste condicionado a MP5)

| Fase | Campanha | Objetivo | Grupo e público | Exclusões | Anúncios | Exemplo de destino com UTM |
|---|---|---|---|---|---|---|
| 1 (16/11) | grad_medvet-integral_tiktok_cadastro_amplo18_202611 | Conversões no site (evento de cadastro pelo pixel e API de eventos) | __amplo18: 18+, região de São Paulo, sem interesses | Quem converteu (pixel) | 2 vídeos dos roteiros do tiktok: v2-pratica_reels-9x16_v1 e v3-entrada_reels-9x16_v1. Spark Ad só com autorização registrada | faculdade.ufape.com.br/graduacao?utm_source=tiktok&utm_medium=paid_social&utm_campaign=grad_medvet-integral_tiktok_cadastro_amplo18_202611&utm_content=v2-pratica_reels-9x16_v1&utm_term=amplo18 |
| 2 e 3 | a mesma campanha, só se o teste passou em 07/12 | Conversões | idem | idem | vencedor + 1 novo | idem |

Critério do teste (gestor): em 3 semanas (até 06/12/2026), CPL até CPLmax_integral e tc mínima observada compatível (fórmula 11). Se não passar, a campanha é pausada em 07/12 (proposta ao humano) e os 0,79% e 1,84% de VT das fases 2 e 3 voltam para a Meta do integral.

### 3.6 G1b Medicina Veterinária noturno (bloqueado; sobe no dia seguinte a MP8)

Mesma estrutura da Meta e do Google do integral, trocando medvet-integral por medvet-noturno. Sem YouTube e sem TikTok. AAAAMM do mês em que subir.

| Canal | Campanhas | Público | Exclusões específicas | Anúncios | Exemplo de destino com UTM |
|---|---|---|---|---|---|
| Meta | grad_medvet-noturno_meta_cadastro_amplo18_AAAAMM; depois rmk-lp30d e engajamento nas fases 2 a 4, como no integral | 18+, Grande São Paulo, amplo | Quem cadastrou (pixel); visitantes que chegaram por anúncio do integral (URL contém medvet-integral) | v1-preco, v2-pratica, v3-entrada com o ângulo do noturno ("Para quem quer estudar veterinária à noite"); sem "sem largar o trabalho" e sem horário de prática e estágio [CONFIRMAR NO CATÁLOGO] | faculdade.ufape.com.br/graduacao?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_medvet-noturno_meta_cadastro_amplo18_AAAAMM&utm_content=v1-preco_feed-4x5_v1&utm_term=amplo18 |
| Google Search | grad_medvet-noturno_google_busca_generica_AAAAMM (grupos: veterinária noturno SP; veterinária à noite; veterinária para quem trabalha [SUPOSIÇÃO; o termo é intenção de busca, o texto do anúncio não afirma emprego]); grad_medvet-noturno_google_busca_marca_AAAAMM só com "ufape veterinária noturno" | 18+ onde possível | Negativas cruzadas: termos genéricos sem "noturno" ou "à noite" ficam no integral; "pedagogia" | v1-preco_rsa, v2-pratica_rsa, v3-entrada_rsa | ...utm_campaign=grad_medvet-noturno_google_busca_generica_AAAAMM&utm_content=v1-preco_rsa_v1&utm_term={keyword} |

Regra de entrada tardia: as 2 primeiras semanas depois do desbloqueio são teste, qualquer que seja a fase do calendário; só depois disso a campanha entra na lógica de escala.

Nota ao gestor-de-midia (não altera o plano dele): o mapa 4.3 do gestor prevê busca de marca do noturno "igual trocando o curso". Para não pôr as campanhas da própria Ufape no mesmo leilão, este plano deixa os termos de marca gerais só no integral (a LP mostra os dois turnos) e o noturno só com termos de marca que tenham "noturno". Aprovação EM8.

### 3.7 G2 Pedagogia (bloqueada; sobe no dia seguinte a MP9)

| Canal | Campanha | Objetivo | Conjunto e público | Exclusões | Anúncios | Exemplo de destino com UTM |
|---|---|---|---|---|---|---|
| Meta | grad_pedagogia_meta_cadastro_goiania18_AAAAMM | Cadastros | __goiania18: 18+, Goiânia e região metropolitana, sem interesses, sem segmentação por emprego | Quem cadastrou (pixel) | p1-noite_feed-4x5_v1; p2-pratica_reels-9x16_v1; p3-preco_feed-4x5_v1; p4-ato_stories-9x16_v1. Sem carga horária, sem docentes, sem endereço até confirmação | faculdade.ufape.com.br/graduacao/pedagogia?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_pedagogia_meta_cadastro_goiania18_AAAAMM&utm_content=p1-noite_feed-4x5_v1&utm_term=goiania18 |
| Meta (fase 3 em diante, se houver público) | grad_pedagogia_meta_cadastro_rmk-lp30d_AAAAMM | Cadastros | visitantes da LP de Pedagogia, 18+, só quando o público atingir o tamanho mínimo exigido pela Meta | Quem cadastrou | p3-preco com regra completa; p1-noite | ...utm_campaign=grad_pedagogia_meta_cadastro_rmk-lp30d_AAAAMM&utm_content=p3-preco_feed-4x5_v2&utm_term=rmk-lp30d |
| Google Search (condicionado a volume, [DADO NÃO FORNECIDO]) | grad_pedagogia_google_busca_generica_AAAAMM | Conversões | pedagogia presencial em Goiânia; pedagogia noturno Goiânia; vestibular de pedagogia Goiânia [SUPOSIÇÃO] | Negativas: "EAD", "gratuita", "concurso", "salário", "veterinária" [SUPOSIÇÃO] | p1-noite_rsa_v1; p3-preco_rsa_v1 | faculdade.ufape.com.br/graduacao/pedagogia?utm_source=google&utm_medium=cpc&utm_campaign=grad_pedagogia_google_busca_generica_AAAAMM&utm_content=p1-noite_rsa_v1&utm_term={keyword} |

### 3.8 Tabela de leads por semana (preencher quando houver VT e CPLmax)

| Recorte | Canal | Semana | % de VT (seção 2) | Verba semanal (R$) = VT x % | CPLmax (R$) | Leads/semana = verba / CPLmax | Leads/semana necessários (1.3) | Passa na condição de volume (2.7)? |
|---|---|---|---|---|---|---|---|---|
| integral | meta | S1 | 3,15% | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | sim / não |
| integral | google | S1 | 1,31% | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | sim / não |
| integral | tiktok | S1 | 0,79% | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | [CONFIRMAR] | sim / não |
| ... | ... | S2 a S14 | seção 2.6 | ... | ... | ... | ... | ... |

Se a soma dos leads por semana do recorte ficar abaixo de L_r, o plano não entrega a meta com essa verba: aviso ao cmo antes de subir.

---

## 4. Calendário de subida e pausa

### 4.1 Preparação (nada no ar)

| Data | O que | Quem |
|---|---|---|
| 27/10 a 13/11/2026 | Nenhuma campanha paga de Graduação no ar. Inventário de campanhas fora da planilha (MP14) | humano |
| 30/10/2026 | C0: metas de custo (MP1) e verba (MP2). Sem números, a fase 1 sobe só em teste com limite de gasto aprovado e sem escala | cmo, gestor-de-midia, Ufape |
| 30/10 a 10/11/2026 | Criar públicos de remarketing (pixel e tag) para acumularem antes da subida; pixel, API de Conversões, tag do Google e pixel do TikTok testados (MP10) | humano |
| 04/11/2026 | Criativos (criativos-de-anuncio) e roteiros (tiktok) | agentes |
| 06/11/2026 | Estruturas de anuncios-meta, anuncios-google e anuncios-tiktok a partir deste plano | agentes |
| 08/11/2026 (domingo) | 1º dia do Enem 2026: sem anúncio pago no ar | - |
| 10/11/2026 | qa-de-marketing (auditoria 11 e conformidade-educacional) | qa |
| 11 a 13/11/2026 | Montagem da fase 1 do integral por humano, em pausa, depois do checklist 4.8 do gestor (MP11) | humano |
| 15/11/2026 (domingo) | 2º dia do Enem 2026: sem anúncio pago no ar | - |

### 4.2 Subidas e pausas

| Data | Sobe | Pausa | Observação de sazonalidade |
|---|---|---|---|
| 16/11/2026 (S1) | Integral: Meta amplo18_202611; Google marca e genérica; TikTok amplo18_202611 (só com MP5) | - | Dia seguinte ao 2º dia do Enem. As notas do Enem 2026 ainda não saíram: a mensagem é "faça a redação online quando quiser" e "já fez o Enem em outro ano? sua nota pode ser a sua entrada"; nunca sugerir que a nota de 2026 já pode ser usada |
| 23/11/2026 | - | - | 1ª leitura semanal (parcial, sem tendência declarada com os últimos dias) |
| 30/11/2026 | - | - | C1 |
| 07/12/2026 (S4) | Integral: Meta rmk-lp30d_202612 e engajamento_202612; YouTube rmk-lp30d_202612 (só com MP6) | TikTok se o teste não passou (proposta) | Reajuste de dezembro [CONFIRMAR, G12]: se mudar valores de 2027/1, criativos com preço passam por ciclo extra antes de seguir no ar |
| 21/12/2026 a 03/01/2027 | - | - | Festas: peso menor (seção 2.5) |
| 04/01/2027 (S8) | Integral: Meta amplo18_202701 (escala) e rmk-lp30d_202701 | Meta amplo18_202611, rmk-lp30d_202612; YouTube | C2; reavaliação do LinkedIn para o noturno só se o cmo pedir (fora da encomenda) |
| Semana E [CONFIRMAR] | Versões "use sua nota do Enem" (Meta e busca); peso da fase 3 conforme 2.5 | - | Divulgação das notas do Enem 2026 |
| Semana S [CONFIRMAR] | Peso conforme 2.5; mesma mensagem de nota do Enem, sem citar Sisu | - | Resultado da chamada regular do Sisu: candidatos não selecionados em instituições públicas podem buscar alternativas [SUPOSIÇÃO] |
| 25/01/2027 | - | - | C3: projeção de matrículas por turno |
| 01/02/2027 (S12) | Integral: Meta rmk-lp30d_202702 | Meta engajamento_202612 e rmk-lp30d_202701; amplo18_202701 se o CPL da fase 3 passou do CPLmax (proposta) | Reta final: passos da matrícula, sem urgência sem número |
| Data de corte de prospecção [CONFIRMAR] | - | Campanhas de público amplo (Meta amplo18, TikTok) | Ver 4.4 |
| 08 a 14/02/2027 (S13) | - | - | Carnaval nesta semana [SUPOSIÇÃO: confirmar no calendário] |
| 20/02/2027 | - | - | Último dia de pedido de cancelamento com devolução de 80% |
| 22/02/2027 | - | Todas as campanhas da Graduação 2027/1 (MP13) | Início das aulas |
| até 05/03/2027 | - | - | Relatório final contra as metas por recorte |

Noturno: sobe no dia seguinte a MP8, na fase do calendário em que estiver, com as 2 primeiras semanas como teste. Pedagogia: idem, no dia seguinte a MP9. Ambos pausam em 22/02/2027.

### 4.3 Checagem semanal

Toda segunda-feira, de 23/11/2026 a 22/02/2027, com os dados da semana anterior (segunda a domingo). O analise-de-midia monta o relatório (fatos, hipóteses, dados que faltam, até 200 palavras ao cmo); o gestor-de-midia decide dentro do plano; o humano executa.

### 4.4 Data de corte de prospecção

Lead que entra tarde demais não chega à matrícula até 20/02/2027. Fórmula: **data de corte = 20/02/2027 menos o tempo médio de lead para matrícula (CRM) [CONFIRMAR]**. Depois dela, ficam só remarketing e busca (marca e genérica), e a verba de público amplo da semana vai para o remarketing do mesmo recorte. Se a Ufape informar data-limite interna de inscrição ou matrícula (G4), as fases 3 e 4 são puxadas para terminar nela, num ciclo extra deste plano. Aprovação EM5.

---

## 5. Indicadores de leitura semanal

Leitura por recorte (integral, noturno, Pedagogia), nunca somada; depois por canal; depois por conceito. Os últimos dias sempre subcontam conversões.

| Indicador | Fórmula | Fonte | Meta ou referência | Uso |
|---|---|---|---|---|
| Verba gasta x planejada | gasto da semana / Verba(r, c, s) | plataforma | entre 90% e 110% [regra prática] | Primeira checagem: sem verba entregue não há leitura |
| Gasto acumulado x VT aprovada | soma do gasto / VT | plataforma | nunca acima de 100% | Trava de verba |
| CPM, CPC, CTR | da plataforma | plataforma | sem meta; comparação da conta com ela mesma a partir da S2 | Diagnóstico de tráfego e fadiga |
| CPL | gasto / leads (cadastros) | plataforma e CRM | até CPLmax_r | Todas as fases |
| Diferença de leads entre fontes | leads plataforma x analytics x CRM | três fontes | até 15% [regra prática do gestor] | Acima disso, investigar antes de decidir |
| t1 lead para inscrito | inscritos / leads | CRM agregado | maior ou igual à t1 conservadora | Qualidade do lead (fase 1) |
| Custo por inscrito | gasto acumulado / inscritos com origem paga | CRM | até CPImax_r | Fase 2 |
| t2 inscrito para avaliado | avaliados / inscritos | sistema de inscrição | maior ou igual à t2 conservadora | Gargalo provável da redação [SUPOSIÇÃO do cmo] |
| Custo por avaliado | gasto acumulado / avaliados com origem paga | sistema de inscrição | até CPAvmax_r | Fase 3 |
| t3, t4, t5 | aprovados / avaliados; matriculados / aprovados; ativos / matriculados | sistema e financeiro | maiores ou iguais às conservadoras | Fases 3 e 4 |
| Custo por matrícula acumulado | gasto acumulado do recorte / matrículas com origem paga | CRM e financeiro | até CPMmax_r | Fase 4 e C2 em diante |
| tc mínima | CPL observado / CPMmax_r | conta | tc observada maior ou igual | Diz se um CPL acima do esperado ainda cabe |
| Ritmo contra a curva | etapas acumuladas / etapas necessárias pela conta 1.3, por semana | CRM | maior ou igual a 100% da curva | Curva do piso de 30 por turma |
| Frequência e fadiga | frequência e queda de CTR do conceito | plataforma | sem meta; troca de criativo quando o CTR cai 2 semanas seguidas [regra prática] | Cadência de criativos |
| Gasto sem lead por anúncio | gasto do anúncio sem cadastro | plataforma | 2 x CPLmax_r [regra prática] | Pausa de anúncio |

---

## 6. Critérios de decisão e regra de realocação semanal

### 6.1 Escalar, manter, ajustar, pausar

Ordem da revisão, parando na primeira causa real: verba entregue; tráfego; conversão; fadiga; página; rastreamento.

| Decisão | Quando (regras práticas, não metas) | Ação | Quem decide |
|---|---|---|---|
| Investigar | Diferença de leads entre fontes acima de 15%, evento de conversão parado ou UTM ausente | Nenhuma decisão de desempenho até resolver | gestor-de-midia |
| Escalar | CPL até 0,8 x CPLmax_r por 2 semanas seguidas e t1 igual ou acima da média do recorte (a partir da fase 2, também custo da etapa da fase dentro da meta 1.4) | Aumento de até 20% por semana na campanha de escala, dentro da verba do recorte e da fase | proposta ao humano; acima da verba aprovada vai ao gestor-de-midia e ao cmo como pedido de aprovação |
| Manter | CPL até CPLmax_r e passagens estáveis | Nada muda; teste de conceito novo segue nos 20% | gestor-de-midia |
| Ajustar | CPL entre 1 e 1,3 x CPLmax_r por 2 semanas, ou tc observada abaixo da tc mínima, ou etapa da fase acima da meta 1.4 | Trocar criativo antes de mexer em público; conferir página e rastreamento; uma mudança por vez | gestor-de-midia, dentro do plano |
| Pausar anúncio | Gasto de 2 x CPLmax_r sem nenhum lead | Pausa do anúncio; nunca todos os antigos ao mesmo tempo | proposta ao humano |
| Pausar campanha (revisão) | CPL acima de 1,3 x CPLmax_r por 2 semanas depois de um ajuste, ou custo por matrícula acumulado acima de CPMmax_r a partir de C2 | Pausa e revisão do recorte com o cmo | proposta ao humano, decisão do cmo |
| Bloqueio mantido | Página do noturno ou da Pedagogia sem correção | Recorte segue fora do ar; verba reservada | cmo |

### 6.2 Regra de realocação semanal (sempre dentro da verba aprovada) [aprovação EM2]

1. **Teto absoluto:** o gasto acumulado nunca passa da VT aprovada, nem a verba do recorte passa da VerbaTeto_r. Limite de gasto da conta igual à VT aprovada (checklist do gestor).
2. **Dentro da campanha (teste e escala):** a partir da fase 2, 20% da verba semanal do canal para conceito novo e 80% para validados. Conceito promovido muda de lugar sem mudar o total. Decide o gestor-de-midia.
3. **Entre canais do mesmo recorte e da mesma fase:** proposta do analise-de-midia, decisão do cmo (gestor, seção 5). Só move verba do canal com CPL pior em relação ao CPLmax_r para o canal com CPL melhor, se o canal que recebe passou no critério de escalar; no máximo 20% da verba semanal do canal que recebe [regra prática]. Já aprovado pelo gestor: TikTok e YouTube que não sobem ou não passam no teste devolvem a verba para a Meta do integral.
4. **Entre recortes:** só com pedido de aprovação ao cmo e à pessoa do marketing. Verba de recorte bloqueado não se move sozinha.
5. **Entre semanas:** verba não entregue numa semana pode passar para a semana seguinte do mesmo recorte e canal, respeitando o limite de 20% de aumento por semana; o que não couber vira economia, nunca gasto acumulado no fim.
6. **Entre fases:** só a regra do gestor (fase 1 de recorte desbloqueado depois de 16/11 vai para a fase 3, com a trava da seção 2.3). Fora disso, o total de cada fase não muda.
7. **Registro:** toda realocação vai no relatório semanal com o que, por que, quanto, efeito esperado e como desfazer. Nenhuma realocação muda as metas.

### 6.3 Protocolo de teste (gestor 4.7, aplicado)

- De 1,5 a 3 x CPLmax_r por conceito antes de julgar; pausa com 2 x CPLmax_r sem lead.
- Promoção à escala: CPL até CPLmax_r e t1 igual ou acima da média do recorte.
- Cadência: de 1 a 2 conceitos novos por recorte a cada 2 semanas a partir da fase 2 [SUPOSIÇÃO, depende da capacidade do criativos-de-anuncio].
- Mudança de verba em campanha de escala: até 20% por semana [regra prática].

---

## 7. Pedidos de aprovação humana

Valem os pedidos MP1 a MP14 do gestor-de-midia. Este plano acrescenta:

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| EM1 | Aprovar a divisão por curso: integral 52,5%, noturno 42,0%, Pedagogia 5,5% de VT, até MP1 permitir a divisão por VerbaTeto | Proporção ao teto de receita do 1º semestre; evita que a Pedagogia gaste acima do que a matrícula paga | percentuais sobre VT (MP2) | Verba por recorte fechada antes de 16/11/2026 | Nova versão aprovada pelo cmo antes da subida |
| EM2 | Aprovar a regra de realocação semanal (6.2) | Dá limite e dono para cada movimento de verba | sem custo adicional; dentro de VT | Ajustes semanais sem passar da verba | Voltar à divisão fixa da seção 2 |
| EM3 | Aprovar os pesos semanais (2.5) e a regra de Enem e Sisu | Concentrar verba nas semanas de maior intenção provável | redistribuição dentro de cada fase | Mais verba quando saem as notas e o resultado do Sisu | Pesos iguais por semana |
| EM4 | Aprovar as metas por fase (1.4) como leitura da meta conservadora | Permite julgar a campanha antes de existir matrícula | sem custo | Decisão semanal com meta escrita | Ler só CPL em todas as fases |
| EM5 | Informar o tempo médio de lead para matrícula e aprovar a data de corte de prospecção (4.4) | Evita gastar com lead que não chega à matrícula | sem custo | Verba final concentrada em quem já conhece a Ufape | Manter público amplo até 21/02 |
| EM6 | Decidir sobre termos de busca com "Sisu" (padrão: fora) | Os editais não preveem ingresso pelo Sisu; risco de expectativa errada | se aprovado, sai da verba da busca genérica | Alcance de quem busca alternativa depois do resultado | Negativar "sisu" |
| EM7 | Aprovar a exclusão de quem já converteu por evento do pixel e da tag (sem lista de contatos) | Menos gasto com quem já se cadastrou, sem dado pessoal carregado | sem custo | Verba em quem ainda não se cadastrou | Remover a exclusão no gerenciador |
| EM8 | Aprovar os termos de marca gerais só no integral e negativas cruzadas entre integral, noturno e Pedagogia | Evita a Ufape disputar o próprio leilão | sem custo | CPC de marca menor [SUPOSIÇÃO] e leitura limpa | Duplicar a marca no noturno, como no mapa do gestor |
| EM9 | Se a conta 1.3 mostrar que a VT não compra os leads necessários: pedido de verba extra ao gestor-de-midia, separado deste plano | Regra: nunca propor gasto acima do aprovado | [CONFIRMAR], só depois de MP1 e MP2 | Decisão informada da Ufape | Manter a VT aprovada e rever a meta antes da subida |

Nenhuma campanha sobe, muda, pausa ou recebe verba pela squad. Todo item acima é executado por humano depois da aprovação.

Canais fora da encomenda: nenhuma sugestão nova. LinkedIn segue fora, com reavaliação só se o cmo pedir em 04/01/2027.

---

## 8. Auditorias deste plano

**auditorias/11-midia-paga.md**
- [ ] Plano do gestor-de-midia aprovado, com canais ativados e fora justificados: canais e justificativas vêm do gestor (3.1); aprovação humana pendente.
- [ ] Metas de CPL e custo por matrícula escritas antes de subir: fórmulas, metas por fase e limite de revisão escritos (seção 1); valores [CONFIRMAR] (MP1). Bloqueia subida com escala.
- [ ] Verba dentro do valor aprovado, com aprovador: tudo em percentual de VT; VT e aprovador [CONFIRMAR] (MP2). Trava de verba na 6.2.
- [x] Nomenclatura padrão em campanhas, conjuntos e anúncios (seção 3).
- [ ] UTMs completas e origem no CRM: padrão e exemplos por campanha (3.2 a 3.7); URL base e chegada ao CRM [CONFIRMAR] (G13, MP10).
- [ ] Pixel, API de Conversões, conversões do Google, pixel e API de eventos do TikTok: no calendário 4.1; estado atual [DADO NÃO FORNECIDO]. Insight Tag do LinkedIn não se aplica (canal fora).
- [ ] Criativos aprovados na conformidade: dependem do qa de 10/11/2026.
- [x] Anúncios dentro das políticas das plataformas: regras de público, texto, destino e Sisu na 3.1; cada anúncio passa de novo no qa.
- [x] Nenhum público com menores de 18; YouTube com conteúdo infantil excluído (3.1, 3.4).
- [x] Spark Ad só com autorização registrada (3.5); post de docente promovido no LinkedIn não se aplica.
- [ ] Relatório semanal ao cmo: começa em 23/11/2026 (4.3).
- [x] Sem segmentação discriminatória nem exclusão por atributo sensível (3.1).
- [x] Públicos sem dados pessoais sem base legal: sem listas de contatos (MP7); exclusão só por evento do pixel (EM7).
- [x] Dados de curso conferidos no catálogo (seção 1) e na ficha dos editais; carga horária da Pedagogia fora.
- [x] Destino de WhatsApp: não há campanha de WhatsApp; destino é a LP.
- [x] Números só das exportações fornecidas: nenhuma exportação foi fornecida; nenhum número de desempenho nem benchmark usado. Percentuais são desenho do plano; valores em reais só os dos editais.
- [x] Nenhuma alteração feita na plataforma sem humano: todo passo é pedido de aprovação (seção 7).

**auditorias/conformidade-educacional.md** (aplicada ao plano; cada anúncio passa de novo no qa)
- [x] Nome, modalidade, duração e turno batem com o catálogo; carga horária da Pedagogia fora de toda peça.
- [x] Os dois cursos estão "aberto" no catálogo.
- [x] Modalidade presencial clara.
- [x] Atos só como no catálogo, sem antecipar reconhecimento.
- [x] Pós lato sensu e curso livre: não se aplica.
- [x] Nenhuma nota do MEC e nenhuma frase de certificação.
- [x] Nenhuma promessa de emprego, salário, aprovação ou concurso; redação descrita como eliminatória onde aparece.
- [x] Sem dado de empregabilidade nem superlativo sem fonte.
- [x] Sem comparação com concorrente em anúncio; Sisu não associado à Ufape.
- [x] Preço com valor cheio, desconto, "1º semestre de 2027" e "Condições e validade no edital"; reajuste sinalizado [CONFIRMAR].
- [x] Desconto com regra, público elegível e validade (ficha de oferta 0.2).
- [x] Sem urgência falsa: reta final fala de passos e datas do edital; sem "últimas vagas".
- [x] Prouni, Fies e financiamento fora.
- [ ] Autorização de uso de imagem de docentes e do hospital: [CONFIRMAR] (G11). Bloqueia vídeo e criativo com pessoa ou hospital.
- [x] Menores: anúncio só 18+, sem menor identificável, sem listas.
- [ ] Formulário da LP com finalidade e política de privacidade: [CONFIRMAR] (G13).
- [x] WhatsApp e e-mail: fora do escopo deste plano.
- [x] Nenhum dado pessoal neste arquivo.
- [x] Políticas da Meta e do Google para educação, sem segmentação discriminatória.
- [ ] Página de destino entrega o que o anúncio promete: noturno bloqueado até G8; Pedagogia bloqueada até G6.
- [x] Texto de anúncio não afirma característica pessoal de quem vê; termo de busca "para quem trabalha" é só intenção, nunca texto.
- [x] Sem escassez falsa, contador, botão falso, pessoa pública, caixa alta excessiva ou tentativa de driblar a análise.
- [ ] Página carrega, sem redirecionamento inesperado, com dados da Ufape e política de privacidade: [CONFIRMAR] (checklist 4.8 do gestor).

**Resultado:** Aprovado como rascunho para seguir à etapa 5 (criativos-de-anuncio). Bloqueados até resposta: subida com escala (MP1, MP2, EM1), noturno (G8, MP4, MP8), Pedagogia (G6, MP4, MP1, MP9), TikTok (G11, MP5), YouTube (MP6), listas de contatos (MP7), criativos com pessoa ou hospital (G11), termos com Sisu (EM6). Revisado por: estrategia-de-midia (agente). Revisão do qa-de-marketing e humana: pendente. Data: 26/10/2026.

**Notas para arquivos de outros donos (não alterados por este agente):**
- O gestor-de-midia pediu este arquivo para 30/10/2026; a entrega saiu em 26/10/2026.
- Mapa 4.3 do gestor: proposta de não duplicar termos de marca gerais no noturno (EM8).
- A sazonalidade do Enem (08 e 15/11/2026) e do resultado do Sisu foi incluída por pedido do orquestrador; as datas de notas e do Sisu seguem [CONFIRMAR] no contexto/graduacao.md.

---

## 9. Fatos (com fonte)

- Receita do 1º semestre de 2027 com desconto por matrícula: R$ 30.000,00 (integral), R$ 24.000,00 (noturno), R$ 3.150,00 (Pedagogia) (Editais 003/2026; ficha de oferta 0.1; gestor 2.1).
- Vagas 45, 45 e 80; turma mínima de 30; inscrições gratuitas desde 17/08/2026; redação online a qualquer momento, eliminatória, nota mínima 5,0; Enem com média mínima de 300 pontos, edições de 2010 em diante; matrícula a partir de 2 dias após o resultado; documentos em até 30 dias; cancelamento com devolução de 80% até 2 dias antes das aulas; aulas em 22/02/2027 (Editais 002 e 004/2026, ficha dos editais).
- Os editais não preveem ingresso pelo Sisu e não trazem data-limite de inscrição nem nota do MEC (ficha dos editais).
- Os dois cursos estão com status "aberto" (catálogo, resumo e seção 1).
- Datas do Enem 2026: 08 e 15/11/2026 (pedido do orquestrador desta etapa).
- Canais ativos, bloqueios, públicos 18+, cenário conservador, percentuais por fase e canal, nomenclatura, UTM, protocolo de teste e critérios de decisão (gestor-de-midia-graduacao-2026-10-26.md).
- Fases e checagens C0 a C3 (estrategia-de-campanha-graduacao-2026-10-26.md).
- Conceitos v1-preco, v2-pratica, v3-entrada e p1 a p4; texto oficial do desconto (estrategia-de-oferta-graduacao-2026-10-26.md, seções 0.2 e 5).

## 10. Suposições

- [SUPOSIÇÃO de desenho] Divisão por curso proporcional a T1 (52,5%, 42,0%, 5,5%), com a mesma meta de 30 por turma.
- [SUPOSIÇÃO de desenho] Pesos semanais dentro das fases e regra de Enem e Sisu (2.5).
- [SUPOSIÇÃO de desenho] Metas por fase como custo por etapa do funil (1.4).
- [SUPOSIÇÃO de desenho] Exclusão cruzada de visitantes por URL entre integral e noturno; exclusão de convertidos por evento do pixel.
- [SUPOSIÇÃO de desenho] Marca geral só no integral e negativas cruzadas.
- [SUPOSIÇÃO] Notas do Enem 2026 e resultado do Sisu em janeiro ou início de fevereiro de 2027; Carnaval de 2027 na semana de 08 a 14/02.
- [SUPOSIÇÃO] Menor atenção nas festas; candidatos não selecionados no Sisu buscam alternativas.
- [SUPOSIÇÃO] Palavras-chave sementes e negativas; regiões de entrega.
- Regras práticas, não metas: 1,5 a 3 x CPLmax por conceito; pausa com 2 x CPLmax sem lead; escalar com 0,8 x CPLmax por 2 semanas; revisão acima de 1,3 x CPLmax; até 20% de mudança por semana; 15% de diferença entre fontes; verba entregue entre 90% e 110%; troca de criativo com CTR em queda por 2 semanas.

## 11. Dados que faltam

- [CONFIRMAR] VT (verba total da Graduação) e aprovador (MP2).
- [CONFIRMAR] k1c, V, Md, t1 a t5, M por recorte e números da base desde 17/08/2026 (MP1; G2 do cmo).
- [CONFIRMAR] Tempo médio de lead para matrícula, para a data de corte (EM5); data-limite interna de inscrição e matrícula (G4).
- [CONFIRMAR] Data de divulgação das notas do Enem 2026 e do resultado do Sisu 2027; data do gabarito oficial.
- [CONFIRMAR] Se o formulário da LP é a inscrição; URL que recebe a UTM; origem no CRM; política de privacidade (G13).
- [DADO NÃO FORNECIDO] Estado do pixel, da API de Conversões, da tag do Google e do pixel do TikTok; histórico de CPL; volume de busca dos termos (inclusive Pedagogia em Goiânia).
- [CONFIRMAR] Correção das páginas (G6, G8); perfis e produção de TikTok e YouTube e autorizações de imagem (G11); efeito do reajuste de dezembro (G12).
- [CONFIRMAR] Área geográfica de entrega com o comercial de São Paulo e de Goiânia.
- [CONFIRMAR NO CATÁLOGO] Carga horária da Pedagogia; horário de prática e estágio do noturno.

---

## Próximo passo

Próximo agente: **criativos-de-anuncio** (etapa 5, 04/11/2026), com as seções 3.1 a 3.7 deste plano (nomes de anúncio, formatos, versão "use sua nota do Enem" para a semana E, regra do Sisu). Em paralelo, anuncios-meta, anuncios-google e anuncios-tiktok montam as estruturas (06/11/2026). Antes de qualquer subida: MP1, MP2, MP4 e EM1 respondidos pela Ufape.
