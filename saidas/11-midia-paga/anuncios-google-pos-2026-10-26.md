# Estrutura de Google Ads da Pós-graduação: Busca por turma de março e de abril de 2027 (etapa 1.14, versão 3)

- **Agente:** anuncios-google (departamento 11 Mídia Paga, por encomenda do gestor-de-midia)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira); arquivo criado em 26/10/2026
- **Versão:** 3 (27/10/2026). Cumpre a encomenda da linha "anuncios-google" da seção 7 de saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 4), com prazos de 30/11/2026 (março) e 30/12/2026 (abril). A parte das provas de bolsa da versão 2 passa para a seção 18, "suspenso (decisão 14)", sem apagar. A parte de turmas da versão 2 foi substituída (os textos com preço e o título de matrícula saem, decisão 16).
- **Versões anteriores:** 2 (26/10/2026, provas e turmas, corrigida pelo qa-de-marketing-geral-2026-10-26-loteD); 1 (26/10/2026).
- **Etapa:** 1.14 da camada 1 do plano do cmo; encomenda do gestor-de-midia-pos (versão 5, seção 12.8) e da estrategia-de-midia-pos (versão 4, seção 7).
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda linha é pedido para um humano executar no Google Ads, depois da aprovação.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 17; valem nesta rodada 8, 10, 11, 12, 14, 15, 16 e 17)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12, com D11 e D12 na 12.7, EM8 a EM10 na 12.6, U10 na 12.12; seção 13, que trata do teto de mensagens e não afeta anúncio pago)
  - saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (versão 5; seções 9 e 12)
  - saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 4; seções 2, 3.1 a 3.8, 4.1 a 4.5, 6 e 7)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (seções 2 a 4, áreas A1 a A14)
  - saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (v2, aprovada; seções 0, 1 e 2)
  - saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md (v3, aprovada; seções 0 a 3, a ficha para peça de cada turma e as seções 17 a 19)
  - saidas/11-midia-paga/anuncios-google-pos-2026-10-26.md (versão 2, a base desta atualização)
  - auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - contexto/ufape-geral.md, contexto/pos-graduacao.md e contexto/catalogo-de-cursos.md (seção 2)
  - Fichas em contexto/cursos/pos/ (bloco "Dados principais") de 68615, 289, 333, 657, 341, 68635, 68636, 68617, 68628, 68609, 68632, 679, 366 e 662
- **Não aberto:** faculdade.ufape.com.br. Nenhuma pesquisa na web para este conteúdo.
- **Dados pessoais:** nenhum. Nenhum docente é nomeado neste arquivo.
- **Marcadores:** [CONFIRMAR] é fato que a Ufape ou o time precisa informar; [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz; [SUPOSIÇÃO] é escolha de desenho ou hipótese deste agente, sempre com a origem; [DADO NÃO FORNECIDO] é número de mídia que não existe nos arquivos (volume, CPC, CTR, gasto, leads). Regra prática é regra de método, não meta. Verba (R$ 2.000,00 por turma) e meta (15 matrículas) vêm do CEO (decisões 15 e 16).
- **Limites de caracteres** (título 30, descrição 90, frase de destaque 25, sitelink 25, caminho 15) são referência de plataforma sem fonte nos arquivos [SUPOSIÇÃO; conferir no editor]. **Todas as contagens foram feitas à mão, em duas passagens, sem script**; as peças mais próximas do limite estão marcadas, e o editor do Google Ads é a conferência final (item S9 do checklist).

---

## 0. Resumo em cinco linhas

1. **O que é:** 14 campanhas de Busca, uma por turma (5 de março, 9 de abril), cada uma com 2 grupos (`__area`, com campus, e `__marca`, "Faculdade UFAPE"), 2 anúncios responsivos por grupo, palavras-chave sementes [SUPOSIÇÃO] sem volume nem CPC [DADO NÃO FORNECIDO], negativas gerais, cruzadas e de praça, e recursos sem preço.
2. **Verba:** só a parte Google da estratégia v4, por turma: março R$ 705,00 e abril R$ 675,00 (teto de R$ 9.600,00 nas 14 turmas), com as diárias em reais por fase da seção 4 (arredondadas para baixo; 289 e 662 recalculadas em 30/11 e 30/12).
3. **Conversão:** lead (cadastro ou início de checkout) é a única que otimiza; inscrição paga e 1ª mensalidade ficam como conversões separadas, só para leitura. UTM `google` e `cpc` no padrão D11 e D12.
4. **Fora:** lance em concorrente, Performance Max, Display, YouTube, preço, valor de inscrição, MEC, certificação, bolsa, prova de bolsa e urgência.
5. **Trava:** nada sobe antes do teste de rastreio de 30/10 e da aprovação; 679, 68636 e 662 (P3), 366 (P4), 657 (U10 e PP7), 341 (PP7) e 68617 (URL) têm trava própria (seção 11). Doze pedidos de aprovação (AGP12 a AGP23, seção 15).

---

## 1. Regras que valem para toda a montagem

| Regra | Valor | Fonte |
|---|---|---|
| Nome do curso | "Pós-graduação em <área>" como no catálogo, nas descrições. Em título (30 caracteres) nenhum nome completo cabe: o título leva a área como está no catálogo; onde nem ela cabe, forma curta marcada (68635, 68617, 68632, 366), sem mudar o sentido. A descrição fixada na posição 1 traz sempre o nome completo | catálogo, seção 2; contexto/pos-graduacao.md |
| Marca | "Faculdade UFAPE" em todo anúncio (homonímia com a universidade federal) | estrategia-de-midia-pos, 4.1 |
| Preço | Nenhum anúncio, recurso ou sitelink mostra parcela, total, matrícula ou valor de inscrição até a resposta de U11. Não entra a frase "Veja parcelas, total e matrícula" (a condição 4 do AP7 a limita ao remarketing) | decisão 16; criativos v3, 1.2 |
| Proibido no texto | MEC, certificação, título de especialista, bolsa, prova de bolsa, desconto, promoção (341 inclusive), "últimas vagas", "vagas limitadas", contagem regressiva, "inscrição", "inscreva-se", superlativo, nome de concorrente, travessão e meia-risca | conformidade-educacional; criativos v3, 1.1 |
| Turma | Número de turma fora das peças de 68628, 68617 e 662; turma mínima sem número | criativos v3, 1.1 |
| Data de início | Só a da planilha. Sem data em 679, 68636 e 366 até a trava (seção 11); em 662 só nome, campus e data | criativos v3, seções 15 a 17 |
| Modalidade | 68632 é presencial: nenhum texto diz "semipresencial" | catálogo; criativos v3 |
| Concorrente | Nenhum nome em anúncio; nenhum lance em marca de concorrente; o nome entra só como negativa | anuncios-google.md; gestor, 3 |
| Políticas | Sem ponto de exclamação no título, sem caixa alta para gritar (UFAPE é sigla), sem símbolos, sem característica de quem vê | conformidade-educacional [SUPOSIÇÃO de política do Google] |
| Rede | Só Rede de Pesquisa do Google; sem parceiros de pesquisa, sem Display, sem Performance Max, sem YouTube | estrategia-de-midia-pos, seção 7; gestor, 3 [SUPOSIÇÃO de desenho: parceiros sem leitura de qualidade] |
| Destino | Sempre a página da turma, nunca WhatsApp. Página com link trocado não recebe anúncio | estrategia-de-midia-pos, 4.1 |
| Nomes | Campanha `pos_<código>-<área curta>_google_lead_busca_<AAAAMM da subida>`; grupo = campanha + `__area` ou `__marca`; anúncio `rsa-<código>-<grupo>-<a ou b>_v1` | D12; estrategia-de-midia-pos, 4.2 |
| UTM | Marcação automática ligada e sufixo de URL final da seção 10, com `utm_source=google` e `utm_medium=cpc` | D11 e D12 |
| Execução | Só por humano, depois da aprovação | CLAUDE.md |

---

## 2. Modelo de estrutura, metas e conversão (skill estrutura-de-campanha-paga)

**Modelo: enxuta.** Verba de R$ 2.000,00 por turma no ciclo e Google com R$ 675,00 a R$ 705,00 dela: uma campanha de conversão por turma, com orçamento na campanha (a meta e a verba são por turma, e o código vai no nome), 2 grupos e 2 anúncios por grupo. Mais campanhas ou grupos espalhariam uma verba que já é pequena (gestor 12.6). Orçamento na campanha, nunca no grupo.

**Metas escritas antes de subir** (estrategia-de-midia-pos, 2.2 e 2.5; todas as taxas são [SUPOSIÇÃO ilustrativa] do gestor):

| Item | Valor |
|---|---|
| Meta da turma | 15 matrículas (1ª mensalidade paga); custo máximo por matrícula R$ 133,33 |
| CPL máximo | R$ 4,00 (conservador, meta de corte), R$ 10,00 (base), R$ 18,00 (otimista) |
| Custo máximo por inscrição paga | R$ 80,00, R$ 100,00 e R$ 120,00 |
| Aviso ao cmo | CPL acima de R$ 18,00 por 2 semanas fechadas, ou leads abaixo da curva do otimista no fim de uma fase |

**Conversão que cada campanha otimiza:** lead (cadastro, se a página tiver; senão início de checkout; EM11), a única na coluna "Conversões" usada para o lance. Inscrição paga e 1ª mensalidade paga entram como conversões **secundárias** (leitura, sem entrar no lance), porque 17 a 25 inscrições no ciclo inteiro não dão volume para o algoritmo (gestor 12.6). A página de cada turma e o evento que ela registra são [CONFIRMAR]; o teste de rastreio é de 30/10 (EA4).

**Estratégia de lance** [SUPOSIÇÃO de desenho, AGP15]: "Maximizar conversões" com a conversão de lead, sem CPA desejado, porque não há histórico de custo por clique na conta [DADO NÃO FORNECIDO]. Com diárias de R$ 7,14 a R$ 21,42 o volume é baixo; o risco está registrado na seção 12. Se o teste de rastreio de 30/10 falhar, a campanha não sobe.

**Protocolo de teste** (a regra da skill, aplicada ao plano): leitura só com 3 dias de dados e R$ 27,00 gastos na campanha; pausa de anúncio com R$ 36,00 gastos sem lead, nunca todos os anúncios de uma campanha ao mesmo tempo; uma mudança por campanha por semana (seção 12).

---

## 3. Mapa das 14 campanhas

Todas: Rede de Pesquisa, português, todos os dias, orçamento diário na campanha, sem data de término automática (a pausa é pedido no dia seguinte ao corte, EM16). Localização "presença ou interesse" (EM6, [SUPOSIÇÃO de desenho; origem: a persona secundária viaja para o módulo, e a procedência dos alunos não existe nos dados; ampliar só com a procedência do CRM, [CONFIRMAR]]).

| Turma | Campanha (= utm_campaign) | URL final (página da turma) | Localização | Sobe | Trava (seção 11) |
|---|---|---|---|---|---|
| 68615 | pos_68615-patclin_google_lead_busca_202612 | https://faculdade.ufape.com.br/produto/68615/pos-graduacao-patologia-clinica/sao-paulo | estado de SP | 07/12 | PP6 |
| 289 | pos_289-cardio-go_google_lead_busca_202612 | https://faculdade.ufape.com.br/produto/289/pos-graduacao-em-cardiologia-veterinaria | GO e DF | 07/12 | limite de R$ 500,00 e recálculo de 30/11 |
| 333 | pos_333-citopato_google_lead_busca_202612 | https://faculdade.ufape.com.br/produto/333/pos-graduacao-em-citopatologia-veterinaria | estado de SP | 07/12 | PP6 |
| 657 | pos_657-anest-avancada_google_lead_busca_202612 | https://faculdade.ufape.com.br/produto/657/pos-graduacao-em-anestesiologia-avancada | estado de SP | 14/12 | PP7 e U10 |
| 341 | pos_341-equina_google_lead_busca_202612 | https://faculdade.ufape.com.br/produto/341/pos-graduacao-em-medicina-interna-equina | estado de SP | 14/12 | PP7, PR7, local da prática |
| 68635 | pos_68635-clinmed-emerg_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68635/pos-graduacao-clinica-medica-e-emergencia-de-pequenos-animais/sao-paulo | estado de SP | 06/01 | página sem pendência |
| 68636 | pos_68636-pneumo_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68636/pos-graduacao-em-pneumologia-veterinaria | estado de SP | 06/01 | P3 e U6: data conferida na planilha |
| 68617 | pos_68617-endocrino_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68617/pos-graduacao-endocrinologia-de-pequenos-animais/v/sao-paulo | estado de SP | 06/01 | URL com final "/v/" (turma V) |
| 68628 | pos_68628-onco_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68628/pos-graduacao-oncologia-veterinaria/sao-paulo | estado de SP | 06/01 | sem número de turma (P5) |
| 68609 | pos_68609-anest-go_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68609/pos-graduacao-anestesiologia-veterinaria/goiania | GO e DF | 06/01 | nenhuma além das gerais |
| 68632 | pos_68632-cirurgia-go_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/68632/pos-graduacao-clinica-cirurgica-de-caes-e-gatos/goiania | GO e DF | 06/01 | nunca "semipresencial" |
| 679 | pos_679-infecto_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/679/pos-graduacao-em-infectologia-veterinaria | estado de SP | só com a trava resolvida | P3 (link trocado) |
| 366 | pos_366-fisio_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/366/pos-graduacao-fisioterapia-fisiatria-e-reabilitacao-veterinaria/sao-paulo | estado de SP | só com a data conferida | P4 (data diverge) |
| 662 | pos_662-orto_google_lead_busca_202701 | https://faculdade.ufape.com.br/produto/662/pos-graduacao-em-ortopedia-veterinaria | estado de SP | só com o link corrigido | P3 e limite de R$ 500,00 |

Notas: (a) o AAAAMM é o mês da subida (D12): 202612 em março e 202701 em abril; 679, 366, 662 e 68636, se subirem depois, trocam o AAAAMM do nome e da utm_campaign pelo mês real da subida (o nome do anúncio não muda). (b) 289 e 662 têm campanha no ar que não é renomeada (D12); a visão de campanhas não separa o canal, então, se houver busca ativa de 289 ou 662, ela não recebe as palavras-chave novas [CONFIRMAR na exportação, A1 da 1.12]. (c) Os URLs vêm das seções 4 a 17 do criativos v3; o URL de 662 é conferido em 28/10 (PP5). (d) 68632 e 68609 em GO e DF; as demais em SP.

---

## 4. Verba e diárias em reais, por fase

Só a parte Google da estratégia v4 (3.3 e 3.4), que vem do gestor 12.5: março 30% no aquecimento, 50% na manutenção e 35% na conversão; abril 30% no aquecimento e 35% na conversão. A verba não gasta numa fase passa para a seguinte da mesma turma; na última, a sobra não é gasta. Diária = total da fase dividido pelos dias da fase, **arredondada para baixo** em duas casas (diária vezes dias nunca passa do total). Nada passa de uma turma para outra sem nova decisão do CEO. Nenhum valor abaixo é aumento: são tetos.

### 4.1 Total por turma e por fase

| Grupo de turmas | Fase | Datas (dias) | Total da fase | Por semana | Diária |
|---|---|---|---|---|---|
| 68615, 289 (teto), 333 | Aquecimento | 07/12 a 20/12 (14) | R$ 150,00 | R$ 75,00 | R$ 10,71 |
| 657, 341 | Aquecimento | 14/12 a 20/12 (7) | R$ 150,00 | R$ 150,00 | R$ 21,42 |
| as 5 de março (289: teto) | Manutenção | 21/12 a 03/01 (14) | R$ 100,00 | R$ 50,00 | R$ 7,14 |
| 68615, 289, 341 | Conversão | 04/01 a 18/02 (46) | R$ 455,00 | R$ 69,24 | R$ 9,89 |
| 333 | Conversão | 04/01 a 25/02 (53) | R$ 455,00 | R$ 60,09 | R$ 8,58 |
| 657 | Conversão | 04/01 a 11/02 (39) | R$ 455,00 | R$ 81,67 | R$ 11,66 |
| as 9 de abril (662: teto) | Aquecimento | 06/01 a 24/01 (19) | R$ 150,00 | R$ 55,26 | R$ 7,89 |
| 679 | Conversão | 25/01 a 04/03 (39) | R$ 525,00 | R$ 94,23 | R$ 13,46 |
| 68632, 68635, 366, 68628 | Conversão | 25/01 a 11/03 (46) | R$ 525,00 | R$ 79,89 | R$ 11,41 |
| 68617, 68636 | Conversão | 25/01 a 18/03 (53) | R$ 525,00 | R$ 69,34 | R$ 9,90 |
| 68609, 662 | Conversão | 25/01 a 25/03 (60) | R$ 525,00 | R$ 61,25 | R$ 8,75 |

Totais por turma: março R$ 150,00 + R$ 100,00 + R$ 455,00 = **R$ 705,00**; abril R$ 150,00 + R$ 525,00 = **R$ 675,00**. Teto nas 14 turmas: 5 x R$ 705,00 + 9 x R$ 675,00 = R$ 3.525,00 + R$ 6.075,00 = **R$ 9.600,00**, dentro dos R$ 2.000,00 de cada turma (o restante é Meta, no arquivo do anuncios-meta). Turma que sobe atrasada (bloqueio): as partes são as mesmas, contadas da data de subida; se subir já na manutenção ou depois, o aquecimento vai para a conversão (estrategia-de-midia-pos, 3.1).

### 4.2 Calendário de diárias por turma (cada troca é pedido a humano)

| Turma | Sobe com | Troca de diária | Conversão | Pedido de pausa (EM16) |
|---|---|---|---|---|
| 68615 | R$ 10,71 (07/12) | R$ 7,14 em 21/12 | R$ 9,89 em 04/01 | 19/02 (corte 18/02) |
| 289 | teto de R$ 10,71, recalculada em 30/11 | teto de R$ 7,14 em 21/12, recalculada pelo saldo | R$ 9,89 em 04/01 | 19/02 |
| 333 | R$ 10,71 (07/12) | R$ 7,14 em 21/12 | R$ 8,58 em 04/01 | 26/02 (corte 25/02) |
| 657 | R$ 21,42 (14/12) | R$ 7,14 em 21/12 | R$ 11,66 em 04/01 | 12/02 (corte 11/02) |
| 341 | R$ 21,42 (14/12) | R$ 7,14 em 21/12 | R$ 9,89 em 04/01 | 19/02 |
| 68635, 68628, 68632, 366 | R$ 7,89 (06/01) | - | R$ 11,41 em 25/01 | 12/03 (corte 11/03) |
| 68617, 68636 | R$ 7,89 (06/01) | - | R$ 9,90 em 25/01 | 19/03 (corte 18/03) |
| 68609 | R$ 7,89 (06/01) | - | R$ 8,75 em 25/01 | 26/03 (corte 25/03) |
| 679 | R$ 7,89 (06/01, só com a trava) | - | R$ 13,46 em 25/01 | 05/03 (corte 04/03) |
| 662 | teto de R$ 7,89, recalculada em 30/12 | - | R$ 8,75 em 25/01 | 26/03 |

Datas de corte são [SUPOSIÇÃO] (1ª mensalidade 30 dias antes do início, por turma; [CONFIRMAR na ficha]); se o corte mudar, a diária e a pausa são recalculadas numa nova versão escrita antes da subida.

### 4.3 289 e 662 (o gasto que já roda conta nos R$ 2.000,00; regra 3.8 e EM15)

- A campanha atual (gasto até 06/12 em 289 e até 05/01 em 662) não passa de R$ 500,00, o aquecimento da turma. A parte Google da estrutura nova é 30% do aquecimento novo, dividida pelos dias da fase.
- **Fórmula:** aquecimento novo = R$ 500,00 menos o gasto da campanha atual até a véspera (se positivo). Google do aquecimento novo = 30% desse valor. Diária = esse valor dividido por 14 dias (289, 07/12 a 20/12) ou por 19 dias (662, 06/01 a 24/01), arredondada para baixo. O gasto até a véspera é informado pela analise-de-midia em 30/11 (289) e 30/12 (662): [DADO NÃO FORNECIDO].
- Se o aquecimento novo for zero, a estrutura de 289 sobe em 21/12 (já na manutenção) e a de 662 sobe em 25/01 (na conversão). A conversão (R$ 455,00 em 289; R$ 525,00 em 662) nunca é tocada pelo gasto anterior.
- 662: a URL é conferida em 28/10; se levar à página errada, vai o pedido de pausa (PP5). Estrutura nova de 662 só com o link corrigido.

### 4.4 Referência de leitura da parte Google (verba da fase dividida pelo CPL máximo de cada cenário)

É conta do plano, não resultado observado. O plano não fixa meta de leads por canal [SUPOSIÇÃO: a curva da seção 2.4 da estratégia v4 é da turma inteira; aqui só a parcela Google serve de régua para ler a busca]. Cenários com CPL máximo de R$ 4,00, R$ 10,00 e R$ 18,00 ([SUPOSIÇÃO ilustrativa] do gestor).

| Fase | Verba Google | Leads de referência (R$ 4,00 / R$ 10,00 / R$ 18,00) |
|---|---|---|
| Aquecimento (março e abril) | R$ 150,00 | 37,50 / 15,00 / 8,33 |
| Manutenção (março) | R$ 100,00 | 25,00 / 10,00 / 5,56 |
| Conversão de março | R$ 455,00 | 113,75 / 45,50 / 25,28 |
| Conversão de abril | R$ 525,00 | 131,25 / 52,50 / 29,17 |
| Ciclo de março | R$ 705,00 | 176,25 / 70,50 / 39,17 |
| Ciclo de abril | R$ 675,00 | 168,75 / 67,50 / 37,50 |

### 4.5 Condição de volume (tabela 3.6 da estratégia v4, fonte única)

Maior CPL que o Google da campanha aguenta, com 2 anúncios por grupo: igual à verba semanal do Google (2 x verba semanal / 2 conceitos). Os CPL máximos do CEO (R$ 4,00 a R$ 18,00) ficam abaixo de todos os limites, então a estrutura passa no papel.

| Turmas | Fase | Limite Google |
|---|---|---|
| 68615, 289, 333 | Aquecimento | R$ 75,00 |
| 657, 341 | Aquecimento | R$ 150,00 |
| as 5 de março | Manutenção | R$ 50,00 |
| 68615, 289, 341 | Conversão | R$ 69,24 |
| 333 | Conversão | R$ 60,09 |
| 657 | Conversão | R$ 81,67 |
| as 9 de abril | Aquecimento | R$ 55,26 |
| 679 | Conversão | R$ 94,23 |
| 68632, 68635, 366, 68628 | Conversão | R$ 79,89 |
| 68617, 68636 | Conversão | R$ 69,34 |
| 68609, 662 | Conversão | R$ 61,25 |

Escada: CPL da semana fechada acima do limite, o grupo fica com 1 anúncio responsivo (o limite dobra); só depois disso vai o pedido de tirar a busca. Para onde vai a verba da busca que sai: [CONFIRMAR com o gestor] (a regra da estratégia para o frio da Meta divide metade para remarketing e metade para busca; para a busca não há regra escrita).

---

## 5. Configurações comuns da campanha

| Campo | Valor |
|---|---|
| Tipo e objetivo | Pesquisa; meta "Leads" (cadastro) |
| Orçamento | Diário, na campanha, nos valores da seção 4; sem orçamento compartilhado |
| Lance | Maximizar conversões (lead), sem CPA desejado [SUPOSIÇÃO, AGP15]; troca para CPA desejado só com conversões registradas e com aprovação |
| Rede | Só Pesquisa; parceiros de pesquisa e Display desligados |
| Localização | "Presença ou interesse" nos locais da seção 3 [SUPOSIÇÃO, EM6]; sem exclusão de local |
| Idioma | Português |
| Programação | Todos os dias, sem ajuste de lance por horário ou dispositivo [SUPOSIÇÃO: sem dado para ajustar] |
| Rotação | Otimizar (padrão dos responsivos) |
| Público | Sem lista de contatos, sem segmento de público (sem dado pessoal; base legal [CONFIRMAR]); 18 anos ou mais no ajuste de demografia, sem exclusão por saúde, religião, orientação sexual, renda, emprego ou origem |
| Correspondência | Frase e exata no começo; ampla fora [SUPOSIÇÃO de desenho: verba pequena, termos amplos gastam fora da intenção] |
| Gasto diário | O Google pode gastar mais que a diária em um dia e compensar em outros, dentro de um teto mensal [SUPOSIÇÃO: regra de plataforma sem fonte nos arquivos, conferir]; por isso o gasto é lido toda segunda contra a seção 4 e vale o pedido de pausa de EM16 |

---

## 6. Palavras-chave sementes por turma [SUPOSIÇÃO]

Todas são sementes. **Volume e CPC de toda palavra-chave abaixo: [DADO NÃO FORNECIDO]** (consulta no Planejador de Palavras-chave, a fazer por humano antes da subida; a pesquisa-de-palavras-chave só traz volume qualitativo "estimado", que não é dado de ferramenta). Origem: K-ID é o termo da pesquisa (seção 4 do arquivo de SEO); "sec. A<n>" é termo secundário da área; "derivada" é o nome do catálogo com o campus. Os termos "pós em" e abreviações (como "pós em cardio vet") entram só como palavra-chave, nunca em texto visível. Cada turma tem 2 grupos: `__area` (área com campus; frase e exata) e `__marca` (frase e exata com "faculdade ufape").

| Turma | `__area` (correspondência) | `__marca` |
|---|---|---|
| 68615 | "pós-graduação em patologia clínica veterinária" (frase, K11.2); [pós-graduação em patologia clínica veterinária] (exata, K11.2); "pós em patologia clínica veterinária são paulo" (frase, sec. A11); "especialização em patologia clínica de cães e gatos" (frase, sec. A11) | "faculdade ufape patologia clínica" (frase, derivada); [faculdade ufape pós-graduação patologia clínica] (exata, derivada) |
| 289 | "pós-graduação em cardiologia veterinária" (frase, K2.2); "pós em cardiologia veterinária em goiânia" (frase, K2.3); [pós-graduação em cardiologia veterinária goiânia] (exata, derivada de K2.3); "especialização em cardiologia de cães e gatos" (frase, sec. A2) | "faculdade ufape cardiologia goiânia" (frase, derivada); [faculdade ufape pós-graduação cardiologia veterinária] (exata, derivada) |
| 333 | "pós-graduação em citopatologia veterinária" (frase, K11.3); [pós-graduação em citopatologia veterinária] (exata, K11.3); "pós em citologia veterinária" (frase, sec. A11); "especialização em citopatologia de cães e gatos" (frase, sec. A11) | "faculdade ufape citopatologia" (frase, derivada); [faculdade ufape pós-graduação citopatologia veterinária] (exata, derivada) |
| 657 | "pós-graduação em anestesiologia avançada veterinária" (frase, K1.3); [pós-graduação em anestesiologia avançada veterinária] (exata, K1.3); "pós em anestesiologia avançada" (frase, sec. A1); "anestesia avançada em cães e gatos pós" (frase, sec. A1) | "faculdade ufape anestesiologia avançada" (frase, derivada); [faculdade ufape pós-graduação anestesiologia avançada] (exata, derivada) |
| 341 | "pós-graduação em medicina interna equina" (frase, A14); [pós-graduação em medicina interna equina] (exata, A14); "pós em medicina equina" (frase, sec. A14); "especialização em clínica de equinos" (frase, sec. A14) | "faculdade ufape medicina equina" (frase, derivada); [faculdade ufape pós-graduação medicina interna equina] (exata, derivada) |
| 68635 | "pós-graduação em clínica médica e emergência de pequenos animais" (frase, A3); "pós em emergência veterinária" (frase, K3.4); "pós em clínica médica de pequenos animais" (frase, sec. A3); "especialização em clínica médica de cães e gatos" (frase, sec. A3) | "faculdade ufape clínica médica e emergência" (frase, derivada); [faculdade ufape pós-graduação clínica médica e emergência] (exata, derivada) |
| 68636 | "pós-graduação em pneumologia veterinária" (frase, K2.6); [pós-graduação em pneumologia veterinária] (exata, K2.6); "pós em pneumologia veterinária são paulo" (frase, sec. A2); "especialização em pneumologia de cães e gatos" (frase, sec. A2) | "faculdade ufape pneumologia" (frase, derivada); [faculdade ufape pós-graduação pneumologia veterinária] (exata, derivada) |
| 68617 | "pós-graduação em endocrinologia de pequenos animais" (frase, A7); "pós em endocrinologia veterinária" (frase, K7.1); "pós em endocrinologia de pequenos animais semipresencial" (frase, K7.2); "especialização em endocrinologia de cães e gatos" (frase, sec. A7) | "faculdade ufape endocrinologia" (frase, derivada); [faculdade ufape pós-graduação endocrinologia] (exata, derivada) |
| 68628 | "pós-graduação em oncologia veterinária" (frase, K10.1); [pós-graduação em oncologia veterinária] (exata, K10.1); "pós em oncologia veterinária são paulo" (frase, sec. A10); "especialização em oncologia de cães e gatos" (frase, sec. A10) | "faculdade ufape oncologia" (frase, derivada); [faculdade ufape pós-graduação oncologia veterinária] (exata, derivada) |
| 68609 | "pós-graduação em anestesiologia veterinária" (frase, K1.1); "pós em anestesiologia veterinária em goiânia" (frase, K1.2); [pós-graduação em anestesiologia veterinária goiânia] (exata, derivada de K1.2); "especialização em anestesiologia de cães e gatos" (frase, sec. A1) | "faculdade ufape anestesiologia goiânia" (frase, derivada); [faculdade ufape pós-graduação anestesiologia veterinária] (exata, derivada) |
| 68632 | "pós-graduação em clínica cirúrgica de cães e gatos" (frase, K4.1); "pós em clínica cirúrgica presencial em goiânia" (frase, K4.2); "pós presencial goiânia veterinária" (frase, KT17); "especialização em cirurgia de cães e gatos" (frase, sec. A4) | "faculdade ufape cirurgia goiânia" (frase, derivada); [faculdade ufape pós-graduação clínica cirúrgica] (exata, derivada) |
| 679 | "pós-graduação em infectologia veterinária" (frase, A14); [pós-graduação em infectologia veterinária] (exata, A14); "especialização em infectologia de cães e gatos" (frase, sec. A14); "pós em doenças infecciosas veterinária" (frase, sec. A14) | "faculdade ufape infectologia" (frase, derivada); [faculdade ufape pós-graduação infectologia veterinária] (exata, derivada) |
| 366 | "pós-graduação em fisioterapia veterinária" (frase, K4.6); "pós em reabilitação veterinária" (frase, K4.6); "pós em fisiatria veterinária" (frase, sec. A4); "pós em fisioterapia e reabilitação de cães e gatos" (frase, sec. A4) | "faculdade ufape fisioterapia veterinária" (frase, derivada); [faculdade ufape pós-graduação reabilitação veterinária] (exata, derivada) |
| 662 | "pós-graduação em ortopedia veterinária" (frase, K4.4); [pós-graduação em ortopedia veterinária] (exata, K4.4); "pós em ortopedia veterinária são paulo" (frase, sec. A4); "especialização em ortopedia de cães e gatos" (frase, sec. A4) | "faculdade ufape ortopedia" (frase, derivada); [faculdade ufape pós-graduação ortopedia veterinária] (exata, derivada) |

Notas: (a) K4.3 ("pós em cirurgia veterinária") e K3.3 ("pós-graduação em clínica médica de pequenos animais") são cabeças de termo de volume alto e disputa de agregadores; ficam fora das sementes de 68632 e 68635 [SUPOSIÇÃO de desenho: com R$ 7,89 a R$ 13,46 por dia, o gasto iria para termos de menor intenção]. (b) Nenhum termo traz marca de concorrente. (c) O relatório de termos de pesquisa é lido em toda revisão (seção 12); termo novo entra como semente só com aprovação.

---

## 7. Negativas [SUPOSIÇÃO, a validar pelo relatório de termos]

### 7.1 Lista geral (lista compartilhada, aplicada às 14 campanhas antes do primeiro dia)

| Tipo | Termos |
|---|---|
| Gratuito e material | grátis; gratuito; gratuita; pdf; apostila; download |
| Emprego e concurso | concurso; emprego; vaga de emprego; salário |
| Outros níveis | residência; mestrado; doutorado; enem; vestibular; sisu; curso livre; curso online gravado; [graduação em medicina veterinária] (exata) |
| EAD | ead; "100% online" [SUPOSIÇÃO; origem: a Ufape não tem turma EAD aberta, pesquisa de palavras-chave 2.2] |
| Homonímia (universidade federal) | universidade federal; pernambuco; agreste; garanhuns |
| Fora desta rodada (decisão 14) | prova de bolsa; bolsa de estudos; bolsa [SUPOSIÇÃO: nenhum anúncio fala de bolsa, e as provas estão suspensas] |
| Regulação (texto oficial vazio) | título de especialista; "reconhecida pelo mec" [SUPOSIÇÃO: o anúncio não pode afirmar nada sobre isso] |
| Concorrente (só como negativa, sem lance) | anclivepa [CONFIRMAR a lista de concorrentes; contexto/ufape-geral.md está vazio nesse item] |

**Cuidado:** não usar "graduação" em correspondência ampla: pode bloquear "pós graduação", porque o Google trata o hífen como separador [SUPOSIÇÃO de comportamento de plataforma; conferir]. Por isso a graduação entra como exata.

### 7.2 Negativas cruzadas e de praça por campanha (v4, 4.4 e 4.5, mais os acréscimos marcados)

| Turma | Negativas próprias da campanha |
|---|---|
| 68615 | citopatologia; hematologia; goiânia; goiás |
| 289 | ecocardiografia; pneumologia; são paulo |
| 333 | patologia clínica; hematologia; goiânia; goiás |
| 657 | locorregional; goiânia; goiás; exatas: [pós-graduação em anestesiologia veterinária], [pós em anestesiologia veterinária], [anestesiologia veterinária] (os termos sem "avançada" ficam para 68609 em Goiânia [SUPOSIÇÃO]) |
| 341 | pequenos animais; cães; gatos; goiânia; goiás |
| 68635 | terapia intensiva; goiânia; goiás |
| 68636 | cardiologia; ventilação mecânica; goiânia; goiás |
| 68617 | nefrologia; goiânia; goiás |
| 68628 | eletroquimioterapia (curso livre 560); goiânia; goiás |
| 68609 | avançada; locorregional; são paulo |
| 68632 | ortopedia; videocirurgia; são paulo; semipresencial [SUPOSIÇÃO: a turma é presencial e o anúncio não pode dizer "semipresencial"] |
| 679 | citopatologia; goiânia; goiás |
| 366 | ortopedia; fisioterapeuta [SUPOSIÇÃO: o público é de médicos veterinários, quem pode atuar é [CONFIRMAR]]; goiânia; goiás |
| 662 | videocirurgia; goiânia; goiás |

Regra de praça: campanha de São Paulo nega "goiânia" e "goiás"; campanha de Goiânia nega "são paulo". Termo de negativa novo que sair do relatório de termos não conta como mudança de estrutura [SUPOSIÇÃO de desenho].

---

## 8. Anúncios responsivos (2 por grupo)

### 8.1 Como são montados

Cada turma tem dois textos de anúncio, **A (turma e campus)** e **B (formato e prática)**, copiados nos dois grupos. São 4 anúncios por campanha, 56 no total:

| Anúncio (nome = utm_content) | Grupo | Texto | Fixações [SUPOSIÇÃO] |
|---|---|---|---|
| rsa-<código>-area-a_v1 | `__area` | A | título da área na posição 1; "Faculdade UFAPE" na posição 3; descrição 1 fixada (a do nome completo) |
| rsa-<código>-area-b_v1 | `__area` | B | igual |
| rsa-<código>-marca-a_v1 | `__marca` | A | "Faculdade UFAPE" na posição 1; título da área na posição 2; descrição 1 fixada |
| rsa-<código>-marca-b_v1 | `__marca` | B | igual |

Cada texto tem até 12 títulos e 4 descrições (o limite é 15 e 4). Quando o CPL da semana fechada passa do limite da seção 4.5, cada grupo fica só com o texto A [SUPOSIÇÃO de desenho: A é o texto de decisão, com campus e turma]. A descrição de nome completo fica fixada na posição 1 em todos: é ela que garante que "Pós-graduação em <área>" e o campus apareçam juntos.

### 8.2 Títulos que valem para várias turmas (até 30 caracteres)

| Código | Título | Caracteres | Uso |
|---|---|---|---|
| C1 | Faculdade UFAPE | 15 | todos |
| C2 | Pós-graduação veterinária | 25 | todos |
| C3 | Para médicos veterinários | 25 | todos, menos 657 e 662 |
| C3b | Para anestesistas já atuantes | 29 | só 657 (público da página; U10 aberta) |
| C4 | Veja a página da turma | 22 | todos |
| C5 | Veja o cronograma na página | 27 | todos |
| C6 | Calendário dos módulos | 22 | texto B, todos, menos 662 |
| C7 | Docentes listados na página | 27 | texto B, só 68615, 289, 657, 68635, 68636, 68617, 68609 e 366 (nas demais não há peça de autoridade docente, criativos v3) |
| C8 | Teoria online e prática | 23 | texto B, semipresenciais, menos 662 |
| C9 | Módulos presenciais | 19 | texto B, onde não há contagem (68615, 341, 68609) |
| C9b | Aulas presenciais | 17 | texto B, só 68632 |

### 8.3 Campos por turma (contados)

Fórmulas de contagem: "Início em dd/mm/aaaa" tem 20 caracteres; "Turma de março de 2027" e "Turma de abril de 2027" têm 22; "<CH> h de carga horária" tem 22 (500, 360 ou 750); "<N> módulos" tem 10; "<N> módulos presenciais" tem 21; "Campus São Paulo" tem 16 e "Campus Goiânia" tem 14; "Semipresencial" tem 14 e "Presencial" tem 10.

| Turma | Título da área (caracteres) | Título extra (caracteres) | Modalidade, CH, módulos | Início (título) | Turma do mês (título) | Contagem de presenciais (título) |
|---|---|---|---|---|---|---|
| 68615 | Patologia Clínica (17) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | não (a ficha não conta) |
| 289 | Cardiologia Veterinária (23) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 333 | Citopatologia Veterinária (25) | - | Semipresencial, 500 h, 24 | Início em 27/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 657 | Anestesiologia Avançada (23) | - | Semipresencial, 360 h, 18 | Início em 13/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 341 | Medicina Interna Equina (23) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | não (a ficha não conta) |
| 68635 | Clínica Médica e Emergência (27), forma curta por limite | Pequenos Animais (16) | Semipresencial, 750 h, 28 | Início em 10/04/2027 | Turma de abril de 2027 | 9 módulos presenciais |
| 68636 | Pneumologia Veterinária (23) | - | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 6 módulos presenciais |
| 68617 | Endocrinologia (14), forma curta por limite | Pequenos Animais (16) | Semipresencial, 500 h, 24 | Início em 17/04/2027 | Turma de abril de 2027 | 2 módulos presenciais |
| 68628 | Oncologia Veterinária (21) | - | Semipresencial, 500 h, 24 | Início em 10/04/2027 | Turma de abril de 2027 | 8 módulos presenciais |
| 68609 | Anestesiologia Veterinária (26) | - | Semipresencial, 500 h, 26 | Início em 24/04/2027 | Turma de abril de 2027 | não (muitos, fora de ordem na ficha) |
| 68632 | Clínica Cirúrgica (17), forma curta por limite | Cães e Gatos (12) | Presencial, 500 h, 24 | Início em 10/04/2027 | Turma de abril de 2027 | não (toda presencial) |
| 679 | Infectologia Veterinária (24) | - | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 3 módulos presenciais |
| 366 | Reabilitação Veterinária (24), forma curta por limite | Fisioterapia e Fisiatria (24) | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 9 módulos presenciais |
| 662 | Ortopedia Veterinária (21) | - | só nome, campus e data | Início em 24/04/2027 | Turma de abril de 2027 | não (662 só com nome, campus e data) |

Fontes: nome, campus, modalidade, CH, turma e data de início, catálogo seção 2 (68636 sem data da planilha; 366 e 662 com a divergência registrada); módulos e presenciais, fichas e criativos v3 (contagem nas fichas, seção 18 e Lista 1 de lá), a conferir na ficha no dia da montagem (S8). A forma curta de 68617 ("Endocrinologia"), 68635, 68632 e 366 só existe porque o nome do catálogo passa de 30 caracteres; o nome completo está na descrição fixada.

### 8.4 Texto A, turma e campus (12 títulos; semipresenciais com data)

Ordem dos títulos: 1 título da área (fixar na posição 1 em `__area`); 2 C1; 3 "Campus <praça>"; 4 C2; 5 "Semipresencial"; 6 "Início em dd/mm/aaaa"; 7 "Turma de <mês> de 2027"; 8 "<CH> h de carga horária"; 9 "<N> módulos"; 10 C3 (657: C3b); 11 C4; 12 título extra da turma (onde houver).

Exceções:
- **68636, 679 e 366 (sem data):** os títulos 6 e 7 saem; entram C5 e, em 68636 e 366, o título "<N> módulos presenciais" no lugar do 9 quando ele couber.
- **68632 (presencial):** o título 5 é "Presencial"; o título extra é "Cães e Gatos"; nenhum título diz "semipresencial".
- **662 (só nome, campus e data):** títulos 1, 2, 3, 4, 6, 7 e 11, e C5 no lugar dos demais. Nenhum título de modalidade, CH, módulos ou público.

**Descrições do texto A (até 90; 4 por anúncio):**

| # | Descrição | Caracteres | Uso |
|---|---|---|---|
| DS1 | nome completo e campus (tabela 8.6) | 59 a 86 | todos; fixada na posição 1 |
| DC | "Veja turma, campus e cronograma na página da Faculdade UFAPE." | 61 | todos, menos 657 e 662 |
| DC657 | "Para médicos veterinários anestesistas já atuantes. Veja a página da turma." | 75 | só 657 (U10 aberta) |
| DS2 | "Semipresencial, 500 h, 24 módulos. Veja o cronograma na página da turma." | 72 | semipresenciais, menos 662; troca CH e N de cada turma, sem mudar o tamanho |
| DS2p | "Presencial, 500 h, 24 módulos. Veja o cronograma na página da turma." | 68 | só 68632 |
| DT | "A turma pode não ser formada: compre passagem e hotel só depois de ela ser confirmada." | 86 | todos, menos 662; depende do AGP20 |

Montagem: A de 68615 usa DS1, DC, DS2 e DT; A de 657 usa DS1, DC657, DS2 e DT; A de 68632 usa DS1, DC, DS2p e DT; A de 662 usa DS1, D662b e D662c (3 descrições, tabela 8.5). Sem o AGP20, a descrição DT sai e o anúncio segue com 3 descrições.

### 8.5 Texto B, formato e prática (12 títulos)

Ordem dos títulos: 1 título da área; 2 C1; 3 "Campus <praça>"; 4 C8; 5 "<N> módulos presenciais" (onde a ficha conta; senão C9); 6 C6; 7 C5; 8 C7 (só onde permitido); 9 "<N> módulos"; 10 "<CH> h de carga horária"; 11 C3 (657: C3b); 12 "Semipresencial".

Exceções:
- **68632:** títulos 4 e 12 saem; entram C9b ("Aulas presenciais") e "Presencial"; "<N> módulos" fica.
- **662:** o texto B usa os mesmos 7 títulos permitidos do A, em outra ordem (1, 2, 3, 6 "Início em 24/04/2027", C5, C4, C2), sem C6, C7, C8, módulos, CH ou público. Por falta de conteúdo liberado, A e B de 662 se diferem pouco [SUPOSIÇÃO: 1 anúncio por grupo é aceitável até a ficha ser corrigida; a escolha é do qa].
- **333, 341, 68628, 679 e 662:** sem C7 (sem peça de autoridade docente).

**Descrições do texto B (até 90; 4 por anúncio):**

| # | Descrição | Caracteres | Uso |
|---|---|---|---|
| DS1 | nome completo e campus (tabela 8.6) | 59 a 86 | todos; fixada na posição 1 |
| DF | "Aulas online e módulos presenciais de prática. Cronograma na página da turma." | 77 | semipresenciais, menos 662 |
| DB2 | "Teoria online e prática presencial nos módulos. Veja o calendário na página da turma." | 85 | semipresenciais, menos 662 |
| DS2 | como no texto A | 72 | semipresenciais, menos 662 |
| DP1 | "Presencial em Goiânia, 24 módulos, um por mês. Veja o cronograma na página da turma." | 84 | só 68632 |
| DP2 | "Aulas presenciais não são transmitidas. Cronograma na página da turma." | 70 | só 68632 (a ficha traz a observação; as fichas de 68636 e 68609 não, e lá a frase não entra) |
| DS2p | como no texto A | 68 | só 68632 |
| D662b | "Faculdade UFAPE, campus São Paulo. Veja o cronograma na página da turma." | 72 | só 662 |
| D662c | "Turma com início em 24/04/2027 no campus São Paulo. Veja a página da turma." | 75 | só 662 |

Montagem: B das semipresenciais usa DS1, DF, DB2 e DS2; B de 68632 usa DS1, DP1, DP2 e DS2p; B de 662 usa DS1, D662b e D662c.

### 8.6 Descrição de nome completo (DS1) por turma

Fórmula: 17 caracteres de "Pós-graduação em " mais o nome mais ", campus <praça>." (19 em São Paulo, 17 em Goiânia) e, quando cabe, " Início em dd/mm/aaaa." (23).

| Turma | DS1 | Caracteres |
|---|---|---|
| 68615 | Pós-graduação em Patologia Clínica, campus São Paulo. Início em 20/03/2027. | 75 |
| 289 | Pós-graduação em Cardiologia Veterinária, campus Goiânia. Início em 20/03/2027. | 79 |
| 333 | Pós-graduação em Citopatologia Veterinária, campus São Paulo. Início em 27/03/2027. | 83 |
| 657 | Pós-graduação em Anestesiologia Avançada, campus São Paulo. Início em 13/03/2027. | 81 |
| 341 | Pós-graduação em Medicina Interna Equina, campus São Paulo. Início em 20/03/2027. | 81 |
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, campus São Paulo. | 83 |
| 68636 | Pós-graduação em Pneumologia Veterinária, campus São Paulo. | 59 |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais, campus São Paulo. | 70 |
| 68628 | Pós-graduação em Oncologia Veterinária, campus São Paulo. Início em 10/04/2027. | 79 |
| 68609 | Pós-graduação em Anestesiologia Veterinária, campus Goiânia. Início em 24/04/2027. | 82 |
| 68632 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, campus Goiânia. Início 10/04/2027. | 86 (perto do limite; recontar no editor) |
| 679 | Pós-graduação em Infectologia Veterinária, campus São Paulo. | 60 |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, campus São Paulo. | 86 (perto do limite; recontar no editor) |
| 662 | Pós-graduação em Ortopedia Veterinária, campus São Paulo. Início em 24/04/2027. | 79 |

Nomes completos conferidos no catálogo, seção 2: o catálogo escreve "Pós Graduação" em 333 e 341, e as peças usam "Pós-graduação em <área>" (contexto da linha). 68632 usa "Início" sem "em" para caber em 90.

### 8.7 Caminho de exibição

"pos-graduacao" (13) e a área sem acento, até 15: "patologia" (9), "cardiologia" (11), "citopatologia" (13), "anestesiologia" (14), "equina" (6), "clinica-medica" (14), "pneumologia" (11), "endocrinologia" (14), "oncologia" (9), "cirurgia" (8), "infectologia" (12), "reabilitacao" (12), "ortopedia" (9).

### 8.8 Checagem dos textos contra as regras

Nenhum texto traz preço, parcela, matrícula, inscrição, bolsa, desconto, MEC, certificado, "últimas vagas" ou concorrente. "Para médicos veterinários" e "Para anestesistas já atuantes" repetem o público-alvo da página (não descrevem quem vê o anúncio). A frase DT (passagem e hotel) é a de criativos v3 (1.2, r2) reescrita para caber em 90 caracteres, com o mesmo sentido; a versão aprovada tem 90 e ficaria no limite.

---

## 9. Recursos (extensões)

Nenhum recurso mostra preço, parcela, matrícula ou valor de inscrição (decisão 16).

| Recurso | Conteúdo | Condição |
|---|---|---|
| Frases de destaque (até 25) | "Faculdade UFAPE" (15); "Campus São Paulo" (16) ou "Campus Goiânia" (14); "Semipresencial" (14) ou "Presencial" (10); "Início em dd/mm/aaaa" (20, onde há data); "<CH> h de carga horária" (22, menos 662); "Módulos presenciais" (19, ou "Aulas presenciais" (17) em 68632); "Cronograma na página" (20); "Corpo docente na página" (23, só onde C7 vale) | todas as campanhas; 662 só com marca, campus, data e cronograma |
| Snippet estruturado | cabeçalho "Cursos" [SUPOSIÇÃO de cabeçalho disponível em português]; valores abaixo | só onde o programa está na ficha; nas demais, sem snippet [CONFIRMAR na ficha] |
| Sitelinks (até 25) | "Calendário dos módulos" (22); "Corpo docente" (13); "Como funciona" (13); "Todas as pós-graduações" (23) | só com URL distinta da página da turma e aceita pelo editor [CONFIRMAR]; sem URL própria, não sobe (o anúncio vale sem sitelink) |
| Chamada | não | atendimento instável em 22/10 e destino é a página, nunca WhatsApp |
| Formulário de lead | não | a coleta é na página da turma |
| Imagem e preço | não | decisão 16 |

Valores de snippet (até 25 caracteres, de 3 a 10 por conjunto; módulos da ficha como estão nas peças aprovadas do criativos v3):

| Turma | Valores (caracteres) |
|---|---|
| 68615 | Hemostasia (10); Hemoparasitoses (15); Mielograma (10); Automação do hemograma (22) |
| 289 | Eletrocardiograma (17); Taquiarritmias (14); Bradiarritmias (14); Ecocardiografia (15) |
| 333 | Citologia básica (16); Imunocitopatologia (18); Leitura de lâminas (18); Derrames cavitários (19); Mielograma (10) |
| 657 | Hemodinâmica avançada (21); Ventilação mecânica (19); Bloqueios locorregionais (24) |
| 68628 | Imunoterapia (12); Eletroquimioterapia (19); Biossegurança (13) |
| 68609 | Avaliação pré-anestésica (24); Monitoração (11); Anestesia inalatória (20) |
| 366 | Hidroterapia (12); Cinesioterapia (14); Recursos eletrofísicos (22); Terapias manuais (16) |
| 341, 68635, 68636, 68617, 68632, 679, 662 | sem snippet até o programa da ficha ser conferido [CONFIRMAR] |

---

## 10. UTM, rastreio e conversões

- **Marcação automática** (gclid) ligada na conta [CONFIRMAR].
- **Sufixo de URL final**, no nível do anúncio: `utm_source=google&utm_medium=cpc&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term={keyword}` (D11 e D12). Minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Nenhum dado pessoal em UTM.
- **Exemplo (68615, `__area`, texto A):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68615-patclin_google_lead_busca_202612&utm_content=rsa-68615-area-a_v1&utm_term={keyword}`.
- **Exemplo (68632, `__marca`, texto B):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68632-cirurgia-go_google_lead_busca_202701&utm_content=rsa-68632-marca-b_v1&utm_term={keyword}`.
- **Anúncios já no ar** (289 e 662, se tiverem busca) não são renomeados; a análise lê por tabela de correspondência (D12).
- **Conversões:**

| Conversão | Papel | Onde é medida | Observação |
|---|---|---|---|
| Lead (cadastro; ou início de checkout) | primária, entra no lance | tag do Google na página da turma | teste de 30/10 (EA4); evento que a página registra [CONFIRMAR] |
| Inscrição paga | secundária, só leitura | loja ou CRM | importação de conversão offline só com o padrão do arquiteto-de-fluxos (P15) e a base legal [CONFIRMAR]; valor da inscrição fora dos textos até U11 |
| 1ª mensalidade paga (matrícula de fato) | secundária, só leitura | CRM e financeiro | idem |

Os dois pagamentos são lidos por turma e somados no CRM (só números somados, nenhum dado pessoal).

---

## 11. Travas de subida (nada sobe com trava aberta)

| Turma | Trava | Quem resolve | O que fica valendo até lá |
|---|---|---|---|
| Todas | Teste de rastreio de 30/10 (lead disparando na página, UTM chegando ao CRM); aprovação de PP16, EM4, EM11 e EM13 a EM16 | Ufape e humano | nada sobe |
| 679 | **P3:** link da planilha trocado (a linha "Citopatologia 03/04" aponta para 679); sem data e sem preço em peça final | Ufape e cmo (pedido A12) | campanha pronta e pausada, sem data nos textos |
| 68636 | **P3:** data só no site (planilha sem data, U6); sem data e sem preço em peça final | Ufape e cmo (A12) | sem data nos textos |
| 662 | **P3:** a página mostra início em 15/08/2026, cronograma de 2026, turma IV e preço de outra turma; campanha atual com gasto limitado a R$ 500,00 até 05/01; URL conferida em 28/10 (PP5) | Ufape e cmo | só nome, campus e data da planilha (24/04/2027); nenhum texto de modalidade, CH, módulos, público ou docente |
| 366 | **P4:** data diverge (planilha 10/04/2027, site 24/04/2027); sobe só com a data conferida na página | Ufape | sem data nos textos |
| 657 | **U10:** pré-requisito formal ainda não escrito na página; **PP7:** desbloqueio de 657 e 341, data alvo 14/12 [SUPOSIÇÃO] | Ufape; pessoa do marketing e cmo | o texto usa só o público da ficha ("anestesistas já atuantes"); se U10 trouxer pré-requisito formal, o texto muda em nova versão |
| 341 | **PP7**; **PR7:** regra da promoção de 20% (nenhum texto cita promoção ou desconto); local da prática com cavalos [CONFIRMAR] | Ufape; pessoa do marketing e cmo | sem promoção, sem local da prática, sem contagem de presenciais |
| 68617 | **URL:** a ficha termina em "/v/" (turma V; planilha VII); conferir se o destino é a turma da planilha; sem número de turma em peça | Ufape | sem número de turma |
| 68628 | **P5:** turma diverge (planilha VI, site VII); sem número de turma em peça | Ufape | sem número de turma |
| 289 | Limite de R$ 500,00 da campanha atual até 06/12; diárias recalculadas em 30/11 | analise-de-midia e gestor | seção 4.3 |
| 68615 e 333 | **PP6:** motivo da pausa anterior conhecido, meta escrita, criativos aprovados e página sem pendência | gestor e qa | - |
| 68632 | Nunca "semipresencial" | - | texto e negativa já cuidam disso |
| Páginas com "CERTIFICADO PELO MEC" | **P2/A7:** o anúncio não repete a frase; a página ainda a publica (46 páginas); a conformidade do destino é pedido à Ufape (A7) | Ufape (regulação) | anúncio sem frase de certificação |

Também seguem [CONFIRMAR]: páginas que dizem turma mínima de 20 (a decisão 11 fixa 15; nenhum texto cita o número); política de privacidade e finalidade do formulário em cada página.

---

## 12. Protocolo de leitura e riscos

| Item | Regra |
|---|---|
| Leitura permitida | campanha com pelo menos 3 dias de dados e R$ 27,00 gastos (1,5 x R$ 18,00) [SUPOSIÇÃO de desenho do plano]; nenhuma tendência com os 2 últimos dias; antes disso, só direção |
| Relatório de termos de pesquisa | lido toda revisão de segunda (feriado passa para o dia útil seguinte, D15); termo irrelevante vira negativa |
| Pausa de anúncio | R$ 36,00 gastos sem lead [SUPOSIÇÃO de desenho do plano: 2 x R$ 18,00]; pedido de pausa do anúncio, nunca de todos da campanha |
| Meta de corte | CPL da semana fechada até R$ 4,00; custo por inscrição até R$ 80,00 |
| Alerta | CPL acima de R$ 4,00: ordem de checagem do gestor (verba gasta, tráfego, conversão, fadiga, página, rastreio); uma mudança por campanha por semana |
| Limite de volume | tabela da seção 4.5; escada de 2 para 1 anúncio por grupo |
| Aviso ao cmo | CPL acima de R$ 18,00 por 2 semanas fechadas |
| Teto da turma | gasto acumulado do ciclo da turma (Meta e Google) em R$ 2.000,00, ou dia seguinte ao corte: pedido de pausa de todas as campanhas da turma (EM16) |
| Lance | troca para CPA desejado só com conversões registradas e com aprovação |

**Riscos registrados (sem número observado):** (1) com diária de R$ 7,14 a R$ 21,42 e CPC [DADO NÃO FORNECIDO], a campanha pode entregar poucos cliques; 2 grupos com 2 anúncios cada fragmentam esse volume, e a escada da seção 4.5 é a resposta do plano. (2) A estratégia "Maximizar conversões" com poucos leads pode demorar a aprender [SUPOSIÇÃO]. (3) Termos genéricos de alta disputa (cabeças de termo) ficaram fora das sementes de propósito.

---

## 13. Calendário de execução humana (depois da aprovação)

| Data | O que | Turmas |
|---|---|---|
| 28/10 | Gasto do ciclo e URL de 662 conferidos (PP5, PP15) | 662 |
| 30/10 | Teste de rastreio (lead, inscrição paga e 1ª mensalidade como conversões separadas; UTM até o CRM) | todas |
| 30/11 | Estrutura de março pronta para aprovação; diárias de 289 recalculadas pelo saldo da fase | março; 289 |
| 07/12 | Sobem 68615, 289 e 333 (aquecimento) | março |
| 14/12 | Sobem 657 e 341, se PP7 desbloqueado | março |
| 21/12 | Manutenção: diária de R$ 7,14 nas 5 turmas | março |
| 30/12 | Estrutura de abril pronta para aprovação; diárias de 662 recalculadas | abril; 662 |
| 04/01 | Conversão de março: R$ 9,89 (68615, 289, 341), R$ 8,58 (333), R$ 11,66 (657) | março |
| 06/01 | Sobe abril, lote 1 (68635, 68636, 68617, 68628, 68609, 68632); lote 2 (679, 366, 662) só com a trava resolvida | abril |
| 25/01 | Conversão de abril (seção 4.2) | abril |
| 12/02 a 26/03 | Pedidos de pausa no dia seguinte ao corte (seção 4.2) | cada turma |

---

## 14. Checklist de montagem

| # | Item |
|---|---|
| S1 | Meta (CPL máximo e custo por matrícula) e verba em reais escritas, com aprovador (PP16; aprovador de "Anúncios e verba" em contexto/ufape-geral.md ainda vazio [CONFIRMAR]) |
| S2 | Tag do Google e conversão de lead disparando na página de destino; inscrição paga e 1ª mensalidade como conversões secundárias; marcação automática ligada (teste de 30/10) |
| S3 | Rede só de Pesquisa; parceiros, Display, Performance Max e YouTube fora |
| S4 | Localização "presença ou interesse" nos locais da seção 3; idioma português |
| S5 | Nomes de campanha, grupo e anúncio e sufixo de UTM como nas seções 3, 8 e 10 |
| S6 | Página de destino coerente e sem a trava da seção 11; URL de 68617 e de 662 conferidas |
| S7 | Orçamento diário nos valores da seção 4, arredondado para baixo; 289 e 662 com o saldo recalculado |
| S8 | Dados de curso conferidos na ficha no dia da montagem (data, campus, modalidade, CH, módulos, contagem de presenciais) |
| S9 | Títulos e descrições aprovados pelo qa (conformidade) e recontados no editor, em especial DS1 de 68632 e 366; fixações aplicadas |
| S10 | Negativas gerais, cruzadas e de praça aplicadas antes do primeiro dia; "graduação" só como exata |
| S11 | Recursos: frases de destaque; snippets só onde há programa; sitelinks só com URL própria; sem chamada, sem formulário, sem preço |
| S12 | Sem término automático; pedido de pausa no dia seguinte ao corte; exportação antes de qualquer pausa |
| S13 | Registro de quem montou, revisou e aprovou |

Pausa (todas): exportar a campanha (grupos, palavras-chave, anúncios, recursos); pausar, nunca remover; conferir gasto zero no dia seguinte; registrar data, hora e motivo; desfazer reativando.

---

## 15. Pedidos de aprovação humana (AGP12 a AGP23)

Os pedidos AGP1 a AGP11 da versão 2 seguem na seção 18 e ficam suspensos (decisão 14), salvo as partes gerais repetidas abaixo. Até a tabela de aprovação de contexto/ufape-geral.md ser preenchida, todos vão à pessoa do marketing que aprovou o plano do cmo; os que mudam canal ou distribuição vão também ao gestor e ao cmo.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AGP12 | Campanhas de Busca de março (68615, 289, 333, 657, 341), seções 3 a 10, com nomes e UTM D11 e D12 | encomenda da estratégia v4; PP16 | até R$ 705,00 por turma na Busca (R$ 3.525,00 nas 5), dentro dos R$ 2.000,00 de cada turma | leads de busca por turma, com origem lida até o CRM | pausar a campanha, com exportação prévia | 30/11 (subida em 07/12 e 14/12) |
| AGP13 | Campanhas de Busca de abril (68635, 68636, 68617, 68628, 68609, 68632, 679, 366, 662) | idem | até R$ 675,00 por turma na Busca (R$ 6.075,00 nas 9) | demanda de abril formada na busca | pausar, com exportação prévia | 30/12 (subida em 06/01) |
| AGP14 | Diárias por fase e datas de troca (21/12, 04/01, 25/01), arredondadas para baixo; 289 e 662 recalculadas em 30/11 e 30/12 pela fórmula da seção 4.3 | a verba é por turma e por fase | dentro dos valores da AGP12 e AGP13; sem aumento | gasto no ritmo do plano | voltar à diária anterior | 30/11; 30/12 |
| AGP15 | Lance "Maximizar conversões" (lead) sem CPA desejado | sem histórico de CPC na conta | sem verba nova | aprendizado sem teto errado | trocar a estratégia (reinicia o aprendizado) | 30/11 |
| AGP16 | Só Rede de Pesquisa, sem parceiros, sem Display, sem Performance Max e sem YouTube; sem lance em concorrente | controle de qualidade do tráfego; encomenda do gestor | sem verba nova | gasto só na busca | ligar parceiros (não recomendado) | 30/11 |
| AGP17 | Negativas gerais, cruzadas e de praça da seção 7, inclusive "prova de bolsa", "bolsa", "ead" e "título de especialista" | evitar disputa interna e termo que a peça não atende | sem verba | menos gasto fora da intenção | retirar a negativa | 30/11 |
| AGP18 | Fixações: título da área (posição 1 em `__area`), "Faculdade UFAPE" (posição 3 em `__area`; posição 1 em `__marca`) e a descrição de nome completo na posição 1 | nome completo do catálogo, campus e marca sempre visíveis | sem verba | conformidade de nome e homonímia | soltar as fixações | 30/11 |
| AGP19 | Conversões: lead primária; inscrição paga e 1ª mensalidade secundárias; importação offline do CRM só com P15 e base legal | EM11; funil de duas etapas medido por turma | sem verba | leitura do custo por inscrição e por matrícula | desativar a conversão secundária | 30/10 (teste) |
| AGP20 | Frase de transparência "A turma pode não ser formada: compre passagem e hotel só depois de ela ser confirmada" no texto A (menos 662) | regra da linha e pilar de condições claras; mesma aprovação do AP8 do criativos v3 | sem verba | transparência sem número de turma mínima | tirar a descrição DT | 30/11 |
| AGP21 | Recursos: frases de destaque e snippets onde há programa já; sitelinks só com URL própria; sem chamada, sem formulário, sem preço | URL distinta e atendimento instável | sem verba | anúncio mais completo sem destino falso | ativar depois | 30/11 |
| AGP22 | Liberar as turmas com trava só quando a trava da seção 11 estiver resolvida: 679, 68636 e 662 (P3), 366 (P4), 657 (U10 e PP7), 341 (PP7 e PR7) e 68617 (URL) | página que não entrega o que o anúncio promete bloqueia a peça (conformidade) | a mesma verba de cada turma, sem verba nova | nenhum clique pago para página errada | pausar a campanha | 30/11; 30/12 |
| AGP23 | Localização "presença ou interesse": estado de SP para as turmas de São Paulo; GO e DF para 289, 68609 e 68632 | EM6; sem dado de procedência | sem custo | menos gasto fora do público provável | ampliar a região | 30/11 |

**Os 3 primeiros:** AGP19 (rastreio, antes de 30/10), AGP12 (março, antes de 30/11) e AGP22 (travas, antes de cada subida).

---

## 16. Auditorias

### 16.1 auditorias/11-midia-paga.md

| Item | Resultado | Observação |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais ativados e fora justificados | Pendente externo | Só Busca nesta saída; Meta no arquivo do anuncios-meta; YouTube e LinkedIn fora (PP13 e PP14 ao cmo); aprovação em PP16 |
| Metas de CPL e custo por matrícula escritas antes de subir | Atendido em parte | Seção 2, com os números do plano; taxas i e k [SUPOSIÇÃO ilustrativa] |
| Verba dentro do valor aprovado, com aprovador registrado | Atendido em parte | Seção 4: nenhuma turma passa de R$ 2.000,00; aprovador [CONFIRMAR] |
| Nomenclatura padrão | Atendido no desenho | Seções 3 e 8 (D12) |
| UTMs completas e origem chegando ao CRM | Pendente externo | Seção 10 (D11); depende do teste de 30/10 |
| Pixel, API de Conversões e conversões do Google | Pendente externo | Seção 10; teste de 30/10; TikTok e LinkedIn fora |
| Criativos aprovados em conformidade-educacional | Pendente externo | Os anúncios desta saída passam pelo qa antes da subida |
| Anúncios dentro das políticas de cada plataforma | Atendido no desenho [SUPOSIÇÃO] | Sem característica pessoal, sem escassez, sem concorrente |
| Nenhum público com menores de 18 anos; no YouTube, conteúdo infantil excluído | Atendido no desenho | Busca com ajuste de 18 anos ou mais; YouTube fora |
| Post de docente promovido ou Spark Ad com autorização registrada | Não se aplica | Nenhum docente nomeado |
| Relatório semanal ao CMO | Pendente externo | Seção 12 |
| Sem segmentação discriminatória nem exclusão por atributo sensível | Atendido no desenho | Seção 5 |
| Públicos sem dados pessoais usados sem base legal | Atendido | Sem lista de contatos |
| Dados de curso conferidos no catálogo | Atendido | Seção 8.3; divergências marcadas (68636, 366, 662, 68617, 68628) |
| Destino de WhatsApp | Não se aplica | O destino é a página da turma |
| Números só das exportações | Atendido | Nenhum número de mídia observado; contas só com a verba e a meta do CEO e as taxas [SUPOSIÇÃO] do gestor |
| Nenhuma alteração feita na plataforma sem um humano executar e aprovar | Atendido | Seções 11, 13 e 15 escritas como pedido |

### 16.2 auditorias/conformidade-educacional.md

| Bloco | Resultado | Observação |
|---|---|---|
| Dados do curso batem com o catálogo | Atendido | Nome completo na descrição fixada; formas curtas só em título por limite; 68632 presencial |
| Status "aberto" | Atendido | As 14 estão "aberto"; 679, 68636 e 662 com trava de página |
| Pós sem "reconhecida pelo MEC" e sem certificação | Atendido | Nenhum texto; negativas cobrem a consulta |
| Sem promessa de emprego, salário, aprovação | Atendido | Seção 1 |
| Preço com condições completas | Atendido | Nenhum preço em anúncio ou recurso (U11) |
| Bolsa e desconto com regra | Atendido | Nenhum texto cita bolsa ou desconto; 341 sem promoção |
| Urgência real | Atendido | Só data de início da planilha e a informação de que a turma pode não ser formada |
| Autorização de imagem | Atendido | Nenhum docente nomeado; nenhuma imagem |
| Característica pessoal de quem vê | Atendido | O texto descreve o curso e o público da página |
| Formulários com finalidade e política de privacidade | Pendente externo | Conferir nas páginas antes de cada subida |
| Destino entrega o que o anúncio promete | Pendente externo | 679, 68636, 662, 366, 68617, 341, 657 (seção 11) |
| Sem caixa alta excessiva, sem travessão nem meia-risca | Atendido | Conferido por leitura do arquivo; caixa alta só em "UFAPE" |

**Resultado:** pronto para o qa-de-marketing e, depois, para a aprovação humana dos pedidos AGP12 a AGP23. Nenhuma campanha sobe antes disso.

---

## 17. Mudanças desta versão

**Versão 3 (27/10/2026)**, pela encomenda da estrategia-de-midia-pos v4 (seção 7) e pelas decisões 14, 15 e 16 do CEO:
- **Provas de bolsa (campanha das provas, grupos por área, anúncios, recursos, AGP1 a AGP11):** passam para a seção 18, "suspenso (decisão 14)", sem apagar. Nada daquela seção sobe, e nenhuma peça nova de prova é produzida até nova ordem.
- **Turmas (antiga seção 4):** substituída. Entram 14 campanhas, uma por turma, com as diárias em reais por fase da estratégia v4 (no lugar de percentuais de VN), sem preço (saem a descrição DT2 com parcelas e total e o título "Matrícula de R$ 250,00") e sem número de turma mínima.
- **Chave de campanha:** `pos_<código>-<área curta>` como na estratégia v4 (4.2); a versão 2 usava só `pos_<código>`.
- **Grupos:** `__area` (com campus) e `__marca`, 2 anúncios por grupo (texto A e texto B), com a escada para 1 anúncio pelo limite da tabela 3.6.
- **Turmas de abril (9) no lugar de 6:** entram 679, 366 e 662 (lote 2), com a trava própria; 68636 passa a subir só com a data conferida.
- **Nome do curso:** sempre o do catálogo na descrição fixada; forma curta só em título, por limite, nas 4 turmas marcadas.
- **Conversões:** lead primária; inscrição paga e 1ª mensalidade secundárias (decisão 16 e EM11); sai a conversão de compra da inscrição das provas.
- **Negativas:** entram "ead", "bolsa", "prova de bolsa", "título de especialista" e as cruzadas de 68632, 679, 366 e 662; sai a negativa temporária "prova de bolsa" só durante a campanha das provas (agora vale o ano inteiro, porque as provas estão suspensas).
- **Travas:** seção 11 com P3 (679, 68636, 662), P4 (366), U10 e PP7 (657), PP7 e PR7 (341), URL de 68617 e o teste de rastreio de 30/10.
- **Pedidos:** AGP12 a AGP23 no lugar de AGP7 a AGP9 para as turmas.
- Nenhuma conta de verba mudou: todos os valores vêm das seções 3.3 e 3.4 da estratégia v4.

---

## 18. Suspenso (decisão 14): campanha das provas de bolsa (conteúdo da versão 2, sem apagar)

**Situação:** suspenso por ordem do CEO (decisão 14, 26/10/2026): "Não produzir peças novas das provas de bolsa nem de Livres até nova ordem." Nada desta seção sobe, é montado ou é pago. O texto abaixo fica como registro para quando a ordem voltar; ele deve ser revisado contra as decisões 11 e 16 e contra a estratégia v4 antes de qualquer uso (por exemplo, o valor de R$ 100,00 da inscrição da prova é do catálogo, seção 3, e não se confunde com a inscrição da Pós em U11).

### 18.1 Mudanças da versão 2 (registro)

- **AGP-Q1 (obrigatório):** a descrição D4 ("Resultado por WhatsApp e/ou e-mail") passa a valer só nos grupos das 10 provas cuja ficha não se contradiz (68639, 68640, 68646, 68647, 68648, 68649, 68654, 68655, 68658, 68660). Nos grupos das outras 12 provas, entra a D5 até U1 ser respondida (seção 18.5).
- Títulos e descrições recontados por script depois da troca: nenhum título acima de 30 caracteres, nenhuma descrição acima de 90.
- O relatório do qa não trouxe outro ajuste para este arquivo.

### 18.2 Regras específicas das provas

| Regra | Valor | Fonte |
|---|---|---|
| Provas | Online, com o campus do grupo; sem endereço, sem "presencial"; 27/11/2026, das 9h às 13h | decisão 11; seção 12.9 |
| Distribuição das bolsas | Sempre visível com qualquer percentual: a descrição com a distribuição completa fica fixada na posição 1 da descrição (seção 18.5) | criativos-de-anuncio-pos, 3.2 e 5.4 |
| Turma mínima | 15, só onde a página da turma já disser 15 [CONFIRMAR por página] | decisão 11 |
| Estratégia de lance | "Maximizar conversões" com a conversão de compra, sem CPA desejado até haver conversões registradas [SUPOSIÇÃO de desenho, AGP3] | v2 |

### 18.3 Modelo de estrutura (v2)

P1 Provas: 1 campanha, orçamento na campanha compartilhado entre os grupos de área. Motivo: busca por "prova de bolsa" mais área tem volume desconhecido e provavelmente baixo por área [SUPOSIÇÃO]; um orçamento único deixa a verba ir para a área que é buscada.

### 18.4 Campanha, grupos, palavras-chave e negativas das provas (sobe em 03/11, pausa em 27/11, suspenso)

| Campo | Valor |
|---|---|
| Nome | pos_provas20261127_google_compra_busca_202611 |
| Objetivo e conversão | Vendas; conversão principal: compra da inscrição de R$ 100,00 (tag do Google na página de confirmação) testada em 30/10 |
| Orçamento | 3,60% de VN na fase 1 (03/11 a 09/11; diária 0,5143%), 3,15% na fase 2 (10/11 a 19/11; diária 0,3150%), 3,00% na fase 3 (20/11 a 26/11; diária 0,4286%); total 9,75% de VN (1.13, 3.1). Percentuais de VN superados pela decisão 15 |
| Localização | estado de São Paulo, Goiás e Distrito Federal, com "presença ou interesse" (EM6) [SUPOSIÇÃO de desenho] |
| Idioma | português |
| Programação | todos os dias; término em 26/11/2026 |
| Rotação | otimizar |

Grupos e palavras-chave sementes [SUPOSIÇÃO; volume e CPC: DADO NÃO FORNECIDO]. Um grupo por área liberada. Em 03/11: `__a12-neuro` (68654) e `__a11-patclin` (68658). Com decisão registrada sobre a página (E2): `__a2-pneumo` (68659), `__a3-clinmed` (68645), `__a5-ultra` (68661), `__a7-endocrino` (68648), `__a10-onco` (68657). Goiânia, só com a página dizendo online e campus Goiânia: `__a1-anest-go` (68640), `__a4-cirurgia-go` (68644); `__a2-cardio-go` (68642) e `__a2-cardio` (68641) só com os links corrigidos. Destino incerto (E5): só com A-C2. Sem grupo: 68649, 68653, 68652, 68655. Grupo geral só com a página única das provas (A-C9).

| Grupo | Palavra-chave | Correspondência |
|---|---|---|
| __a12-neuro | "prova de bolsa pós-graduação neurologia veterinária" | frase |
| | [prova de bolsa neurologia veterinária] | exata |
| | "bolsa pós-graduação neurologia veterinária" | frase |
| | "bolsa de estudos neurologia veterinária" | frase |
| | "faculdade ufape prova de bolsa neurologia" | frase (marca) |
| __a11-patclin | "prova de bolsa pós-graduação patologia clínica veterinária" | frase |
| | [prova de bolsa patologia clínica veterinária] | exata |
| | "bolsa pós-graduação patologia clínica" | frase |
| | "bolsa de estudos patologia clínica veterinária" | frase |
| | "faculdade ufape prova de bolsa patologia clínica" | frase (marca) |
| demais áreas | mesmo padrão, com o nome da especialidade da tabela 5.5 do criativos | frase e exata |

Correspondência ampla fora no começo [SUPOSIÇÃO de desenho]. O relatório de termos de pesquisa seria lido em 09/11, 16/11 e 23/11.

Negativas das provas [SUPOSIÇÃO, a validar pelo relatório de termos]:
- **Comuns (lista compartilhada da campanha):** grátis, gratuito, gratuita, pdf, apostila, download, concurso, emprego, vaga de emprego, residência, mestrado, doutorado, sisu, enem, vestibular, universidade federal, pernambuco, agreste, garanhuns, anclivepa (negativa evita aparecer para quem busca o concorrente; nenhum lance nele).
- **Cruzadas entre grupos:** cada grupo nega o nome das especialidades dos outros grupos ativos (ex.: `__a12-neuro` nega "patologia", "pneumologia", "oncologia"; `__a11-patclin` nega "citopatologia", "hematologia", "neurologia").
- **Entre praças:** grupos de São Paulo negam "goiânia"; grupos de Goiânia negam "são paulo".

### 18.5 Anúncio responsivo das provas `rsa-<área>_prova_v1` (um por grupo)

**Títulos compartilhados (13) e de área (2), até 30 caracteres:**

| # | Título | Observação |
|---|---|---|
| S1 | "Prova de bolsa veterinária" (26) | |
| S2 | "Inscrição de R$ 100,00" (22) | |
| S3 | "11 bolsas por prova" (19) | |
| S4 | "Bolsas de 10% a 50%" (19) | só com D2 fixada na descrição 1 |
| S5 | "Prova online em 27/11" (21) | substitui "Prova presencial em 27/11" (decisão 11) |
| S6 | "Prova das 9h às 13h" (19) | horário da ficha; U2 aberta |
| S7 | "Nota de corte 7,0" (17) | |
| S8 | "Faculdade UFAPE" (15) | fixar na posição 3 [SUPOSIÇÃO] |
| S9 | "Pós-graduação veterinária" (25) | |
| S10 | "Bolsas de 50%, 25% e 10%" (24) | só com D2 fixada |
| S11 | "Inscreva-se na prova" (20) | |
| S12 | "Desempate por currículo" (23) | |
| S13 | "Campus São Paulo" (16) | nos grupos de Goiânia: "Campus Goiânia" (14). Substitui "Prova em São Paulo ou Goiânia" |
| A1 | título de área 1 da tabela 5.5 do criativos (ex.: "Prova de bolsa: Neurologia" (26); "Prova 27/11: Patologia Clínica" (30)) | fixar na posição 1 [SUPOSIÇÃO] |
| A2 | título de área 2 (ex.: "Neurologia e Neurocirurgia" (26); "Bolsa em Patologia Clínica" (26)) | |

**Descrições (até 90), 4 por anúncio:**

| # | Descrição | Uso |
|---|---|---|
| D1 | "Prova de bolsa da Faculdade UFAPE: inscrição de R$ 100,00 e 11 bolsas por prova." (80) | todos |
| D2 | "2 bolsas de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0." (68) | todos; fixada na posição 1 da descrição |
| D3 | "Prova online em 27/11/2026, das 9h às 13h, campus São Paulo. Regras na página da prova." (87) | grupos de SP; em Goiânia: "Prova online em 27/11/2026, das 9h às 13h, campus Goiânia. Regras na página da prova." (85) |
| D4 | "Bolsa não acumulativa e intransferível. Resultado por WhatsApp e/ou e-mail." (75) | só nos grupos das 10 provas cuja ficha não se contradiz no canal do resultado: 68639, 68640, 68646, 68647, 68648, 68649, 68654, 68655, 68658 e 68660 (AGP-Q1). Dos grupos de 03/11, valem __a12-neuro (68654) e __a11-patclin (68658) |
| D5 | "Bolsa não acumulativa e intransferível. Inscrição: Pix, boleto ou 1x no cartão." (79) | no lugar de D4 em todos os demais grupos (68641, 68642, 68643, 68644, 68645, 68650, 68651, 68652, 68653, 68657, 68659, 68661), até U1 ser respondida |

Caminho de exibição: "prova-de-bolsa" (14) / nome da área sem acento, até 15. URL final: a página da prova da área (tabela 4.1 do criativos), com o sufixo de UTM da seção 10 deste arquivo (utm_campaign = pos_provas20261127_google_compra_busca_202611; utm_content = rsa-<área>_prova_v1).

### 18.6 Recursos das provas (v2, suspensos)

| Recurso | Conteúdo | Condição |
|---|---|---|
| Frases de destaque (até 25) | "Prova online" (12); "11 bolsas por prova" (19); "Inscrição de R$ 100,00" (22); "Nota de corte 7,0" (17); "Desempate por currículo" (23) | todos os grupos |
| Snippets estruturados | cabeçalho "Cursos" [SUPOSIÇÃO]; valores: especialidades com grupo ativo (ex.: "Neurologia" (10), "Patologia Clínica" (17)) | só especialidades liberadas |
| Sitelinks (até 25) | "Regras da prova" (15); "Como se inscrever" (17) | só com URLs próprias (FAQ ou página única, A-C8 e A-C9) [CONFIRMAR] |
| Chamada | números de vendas de São Paulo e de Goiânia do contexto geral | recomendação: não ativar (atendimento instável em 22/10) |
| Formulário de lead | não | coleta fora da página |
| Imagem | arte 1:1 de C1 ou C2 sem o quadro "presencial" [SUPOSIÇÃO] | só depois da troca das artes (AMP2 do anuncios-meta-pos) |

### 18.7 Protocolo de leitura das provas (v2, suspenso)

Leitura: custo por inscrito por grupo, com 3 dias e gasto de 1,5 x CPImax; relatório de termos em toda revisão. Pausa de anúncio: 1,5 a 2 x CPImax sem inscrição. Teste T8 do criativos: fixar S2 ou S3 na posição 2, dentro do mesmo grupo, de 03/11 a 16/11; leitura pelo relatório de recursos e custo por inscrito somado. Lance: troca para CPA desejado só com conversões registradas e com aprovação.

### 18.8 Pedidos AGP1 a AGP11 da versão 2 (suspensos)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AGP1 | Campanha das provas da seção 18.4, com nomes e UTM D11 e D12 | D12; provas ainda não subiram | 9,75% de VN [CONFIRMAR reais] | busca de prova por área com origem lida | trocar o sufixo | 30/10 (suspenso) |
| AGP2 | Títulos e descrições das provas com "online" e campus (S5, S13, D3) | decisão 11 | sem verba | anúncio coerente com a decisão | voltar ao texto anterior só se a decisão mudar | 30/10 (suspenso) |
| AGP3 | Lance "Maximizar conversões" sem CPA desejado no começo | sem histórico de CPC | sem verba nova | aprendizado sem teto errado | lance manual | 30/10 (suspenso) |
| AGP4 | Só Rede de Pesquisa, sem parceiros | controle de qualidade do tráfego | sem verba | gasto só no Google | ligar parceiros | 30/10 (vale hoje na AGP16) |
| AGP5 | Fixações: área na posição 1, "Faculdade UFAPE" na 3; D2 na descrição 1 (provas); DT2 na descrição 2 (turmas, substituída pela AGP18) | relevância, marca e preço sempre completo | sem verba | conformidade de preço e bolsa | soltar as fixações | 30/10 (suspenso) |
| AGP6 | Negativas comuns, cruzadas, de praça e "prova de bolsa" nas turmas | evitar disputa interna e termo errado | sem verba | menos gasto fora da intenção | retirar | 30/10 (provas, suspenso); turmas na AGP17 |
| AGP7 | Campanhas de março da seção 4 da versão 2 | P3 | 12,3375% de VN no Google em P3 | leads de busca por turma | pausar | substituído pela AGP12 |
| AGP8 | Campanhas de abril lote 1 da seção 4 da versão 2 | P4 | 0,75% de VN por turma (6 turmas) | demanda de abril | pausar | substituído pela AGP13 |
| AGP9 | Recursos: frases de destaque e snippets já; sitelinks só com URLs próprias; sem chamada e sem formulário | URL distinta e atendimento instável | sem verba | anúncio mais completo sem destino falso | ativar depois | substituído pela AGP21 |
| AGP10 | Grupos de Goiânia só com a página dizendo online e campus Goiânia; Cardiologia só com os links corrigidos | destino coerente | dentro de P1 | nenhum clique para página errada | pausar os grupos | 31/10 (suspenso) |
| AGP11 | Turma mínima de 15 em título e descrição só onde a página da turma já diz 15 | decisão 11; páginas com 20 | sem verba | transparência sem contradição | tirar o título | substituído: nenhum texto de turma cita o número |

### 18.9 Notas da versão 2 sobre arquivos de outros agentes (registro)

- **criativos-de-anuncio-pos, seção 5:** S5 "Prova presencial em 27/11", S13 "Prova em São Paulo ou Goiânia", D3 com "presencial", a frase de destaque "Prova presencial" e a UTM `utm_medium=pago` contrariam a decisão 11 e D11; trocas na seção 18.5 e 18.6 deste arquivo. A D2 do criativos ("Bolsas de 50% (monitoria), 25% e 10%") não mostra a quantidade de cada bolsa; a D2 deste arquivo traz a distribuição completa.
- **estrategia-de-midia-pos, 4.3:** exceção de UTM das provas superada por D12.

---

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 de mídia por turma de Pós; meta de pelo menos 15 matrículas por turma; inscrição de R$ 260,00 medida separada da 1ª mensalidade; nenhuma peça cita o valor da inscrição até U11; provas de bolsa e Livres fora desta rodada (docs/execucao-2026-10-26.md, decisões 14, 15 e 16).
- Parte Google por turma: março R$ 705,00 (aquecimento R$ 150,00, manutenção R$ 100,00, conversão R$ 455,00) e abril R$ 675,00 (aquecimento R$ 150,00, conversão R$ 525,00); fases, datas, dias e limites de volume (gestor-de-midia-pos 12.5 e 12.6; estrategia-de-midia-pos 3.1 a 3.6).
- Meta de custo: R$ 133,33 por matrícula; CPL máximo R$ 4,00, R$ 10,00 e R$ 18,00 nos três cenários [taxas SUPOSIÇÃO do gestor] (estrategia-de-midia-pos 2.2).
- Padrão D11 (utm_source google, utm_medium cpc) e D12 (chave pos_<código>, nome da campanha = utm_campaign, AAAAMM da subida) (cmo-geral, 12.7; estrategia-de-midia-pos 4.2 e 4.3).
- Áreas curtas, negativas cruzadas por turma, e que Performance Max, Display, YouTube e LinkedIn estão fora (estrategia-de-midia-pos 4.2, 4.4, 4.5 e 7; gestor 12.6).
- Nome, campus, modalidade, CH, turma e data de início das 14 turmas (catálogo, seção 2, 26/10/2026); módulos de cada ficha (contexto/cursos/pos/); 68636 com data só no site; 366 com data divergente; 662 com a página de outra turma (catálogo e fichas).
- Contagem de módulos presenciais nas fichas de 289, 333, 657, 68635, 68636, 68617, 68628, 679 e 366; observação "aulas presenciais não serão transmitidas" nas fichas de 68632 e de outras 10, e ausente em 68636 e 68609 (criativos-de-anuncio-pos-turmas v3, Lista 1).
- Bloqueios: 679, 68636 e 662 (P3), 366 (P4), 657 (U10, PP7), 341 (PP7, PR7), 68617 (URL com "/v/"), 68628 (turma) (criativos v3, seção 18; cmo-geral, seção 7 e 12.12).
- Termos de busca com área, campus e marca vêm da pesquisa-de-palavras-chave-pos (K1.1 a K11.3, KT17 e as listas "secundárias" de cada área); a Ufape não tem turma EAD aberta (mesmo arquivo, seção 2.2).
- Frase de transparência sobre passagem e hotel: regra da linha (contexto/pos-graduacao.md) e frase do r2 do criativos v3 (1.2).
- Calendário: 02/11/2026 feriado; 07/12/2026, 14/12/2026, 04/01/2027 e 25/01/2027 são segundas; 06/01/2027 é quarta; cortes em quintas-feiras (estrategia-de-midia-pos, Lista 1).

## Lista 2. Suposições

- [SUPOSIÇÃO] Todas as palavras-chave são sementes, sem volume nem CPC; as "derivadas" combinam o nome do catálogo com o campus ou a marca.
- [SUPOSIÇÃO] Limites de caracteres e recursos do Google (cabeçalho "Cursos", comportamento do hífen em negativa, gasto acima da diária em um dia), sem fonte nos arquivos.
- [SUPOSIÇÃO] Correspondência só de frase e exata no começo; Rede de Pesquisa sem parceiros; sem ajuste de lance por horário ou dispositivo.
- [SUPOSIÇÃO] Lance "Maximizar conversões" (lead) sem CPA desejado.
- [SUPOSIÇÃO] Fixações de título e descrição; texto A como o de decisão que fica quando o CPL passa do limite.
- [SUPOSIÇÃO] Localização "presença ou interesse" (EM6): a persona secundária viaja; a procedência dos alunos não existe nos dados.
- [SUPOSIÇÃO] Negativas "ead", "100% online", "bolsa", "prova de bolsa", "título de especialista", "reconhecida pelo mec", "salário", "semipresencial" (em 68632), "fisioterapeuta" (em 366) e as exatas de 657.
- [SUPOSIÇÃO] Datas de corte (1ª mensalidade 30 dias antes do início) e, por isso, as datas de pausa.
- [SUPOSIÇÃO] A parcela Google da curva de leads é régua de leitura; o plano não fixa meta de leads por canal.
- [SUPOSIÇÃO] Leitura permitida com R$ 27,00 e pausa de anúncio com R$ 36,00 sem lead (1,5 e 2 vezes o maior CPL máximo).
- [SUPOSIÇÃO] Frase DT reescrita para caber em 90 caracteres com o mesmo sentido da aprovada no criativos v3.
- [SUPOSIÇÃO] Ficar sem snippet nas turmas sem programa lido; 1 anúncio por grupo em 662 até a ficha ser corrigida.
- [SUPOSIÇÃO] Taxas de lead para inscrição e de inscrição para matrícula (5%, 10%, 15%; 60%, 75%, 90%), do gestor, só ilustrativas.

## Lista 3. Dados que faltam

- [DADO NÃO FORNECIDO] Volume de busca e CPC de toda palavra-chave (Planejador de Palavras-chave); CPL, CTR e gasto históricos da Pós; gasto de 289 até 30/11 e de 662 até 30/12 (analise-de-midia).
- [CONFIRMAR] Teste de rastreio de 30/10; evento que a página de cada turma registra; marcação automática ligada; importação de conversão do CRM (P15) e base legal.
- [CONFIRMAR U11] Valor da inscrição (R$ 260,00 do CEO contra R$ 250,00 e R$ 350,00 do site) e o rótulo da página; até lá nenhum texto cita preço.
- [CONFIRMAR U10] Pré-requisito formal de 657; [CONFIRMAR PR7] regra da promoção de 341 e local da prática com cavalos.
- [CONFIRMAR] Link e página de 679, 68636 e 662 (P3); data de 366 (P4) e de 68636 na planilha (U6); turma da URL de 68617 e número de turma de 68628, 68617 e 662.
- [CONFIRMAR] Datas de corte por turma; período exato do ciclo de cada turma (decisão 15); mínimo diário aceito pelo Google; para onde vai a verba da busca que sair.
- [CONFIRMAR] URLs próprias para sitelinks; programa de 341, 68635, 68636, 68617, 68632, 679 e 662 para snippets; contagem de presenciais de 68615, 341 e 68609.
- [CONFIRMAR] Lista de concorrentes para negativas; aprovador de "Anúncios e verba" em contexto/ufape-geral.md; política de privacidade e finalidade do formulário nas 14 páginas; páginas que ainda dizem turma mínima de 20.
- [CONFIRMAR] Campanhas de busca já ativas da Pós (exportação A1 da 1.12); aprovação de PP16 e de EM4, EM11 e EM13 a EM16.
- [CONFIRMAR NO CATÁLOGO] 68636 sem data da planilha; 341 com a promoção cortada no catálogo (fora de qualquer texto).

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma. Regras de plataforma sem fonte nos arquivos estão marcadas [SUPOSIÇÃO].

---

**Próximo agente sugerido:** qa-de-marketing (auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md; conferir as contagens de caracteres no editor); depois, aprovação humana dos pedidos AGP12 a AGP23 e execução por humano no Google Ads.
