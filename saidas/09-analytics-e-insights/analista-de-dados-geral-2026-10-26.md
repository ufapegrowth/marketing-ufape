# Análise de dados: distribuição da mídia paga por urgência, ticket, área e linha

- **Agente:** analista-de-dados (09 Analytics e Insights)
- **Linha:** geral (Pós-graduação, Cursos Livres e Eventos; Graduação não aparece na visão de campanhas)
- **Data:** 26/10/2026
- **Etapa:** 1.10 da camada 1 do plano do cmo
- **Versão:** 3 (26/10/2026), propaga as decisões 7 a 13 da Ufape e a seção 12 do cmo (saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md). Mudanças na seção "Mudanças desta versão", antes das listas finais.
- **Status:** rascunho, versão 2, corrigida após o veredito do qa-de-marketing (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep09-10.md, itens A1 a A4, R1 e R2). Nada é publicado, enviado ou pago.
- **Entradas lidas:**
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/contexto/ufape-geral.md
  - /home/user/marketing-ufape/contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (26/10/2026)
  - /home/user/marketing-ufape/docs/visao-de-campanhas-2026-10-26.md
  - /home/user/marketing-ufape/docs/auditoria-do-catalogo-2026-10-26.md
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 2, 3 e 7)
  - /home/user/marketing-ufape/.claude/skills/memorando-de-insight/SKILL.md e .claude/skills/arvore-de-metricas/SKILL.md
  - /home/user/marketing-ufape/auditorias/09-analytics.md
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep09-10.md (veredito, seção 1)

---

## 0. Antes de concluir: o que os dados são e o que não são

1. **Só existe um conjunto de dados:** a visão de campanhas (67 linhas, uma por curso ou turma, com status da mídia paga, formatos ativos, ângulos e dias até o início), cruzada com o catálogo (linha, tipo, preço, status, data). Não há leads, inscrições, matrículas, verba, gasto, cliques nem resultado de campanha. Por isso **nenhuma** conta de custo por lead, custo por matrícula, taxa de conversão lead para matrícula ou receita da linha é possível hoje. Todas ficam [CONFIRMAR] e não foram estimadas.
2. **"Campanha ativa" não é "verba".** A visão diz se a campanha está ligada, não quanto gasta. Quando este memorando fala em "onde a verba está", fala de onde há campanha ligada. O peso real de cada campanha é [CONFIRMAR].
3. **Ticket = preço de lista do site** (catálogo, 26/10/2026): para Pós, o total "no cartão ou boleto", sem a matrícula de R$ 250,00 ou R$ 350,00; para Livres e Eventos, o preço à vista. Não é receita nem margem.
4. **Dados bagunçados encontrados no cruzamento** (detalhe na seção 6): 7 linhas da visão não casam com um único código do catálogo; 10 linhas têm data diferente do catálogo, e em um caso (Ventilação Mecânica, 68618) as duas datas vêm da mesma planilha (18/12/2026 no catálogo e 22/05/2027 na visão).

### Como contei

- Numerei as 67 linhas da tabela da visão de campanhas na ordem do arquivo, de V1 (linha 9 do arquivo) a V67 (linha 75). Cada linha foi lida e classificada à mão (não há script nesta rodada). As contagens por status batem com o total escrito no topo da visão: 26 sem campanha, 22 pausadas, 19 ativas (26 + 22 + 19 = 67).
- Cada linha foi ligada a um código do catálogo pelo nome, local e data. A linha de negócio vem da seção do catálogo onde o código está (seção 2 = Pós; seções 4 a 8 = Livres; seção 9 = Eventos).
- **Datas e dias até o início vêm do catálogo** (que traz a data da planilha), não da visão. Onde a data do catálogo difere da visão (seção 6.4), vale a do catálogo e a da visão aparece entre parênteses. A coluna "Dias até o início" da visão só é usada quando o catálogo não tem data ou o código é [CONFIRMAR]. Conferi a coluna da visão por amostra (30/10/2026 = 4 dias; 28/11/2026 = 33 dias; 13/03/2027 = 138 dias: 5 + 30 + 31 + 31 + 28 + 13).
- Áreas A1 a A14 e a separação "recorte" e "fora do recorte" vêm das seções 2.2 a 2.4 e da tabela de status de mídia da seção 3 do plano do cmo, recontadas item a item.
- Percentuais arredondados a uma casa: parte dividida pelo total, vezes 100.

---

## 1. Memorando de insight

### Pergunta 1. Onde estão as campanhas ligadas em relação à urgência?

**Dados (visão de campanhas, contagem V1 a V67, dias pela data do catálogo):**

| Faixa de dias até o início (catálogo) | Linhas | Ativa | Pausada | Sem campanha |
|---|---|---|---|---|
| Já iniciada (dias negativos) | 32 | 6 | 9 | 17 |
| De 0 a 30 dias | 5 | 5 | 0 | 0 |
| De 31 a 60 dias | 6 | 5 | 1 (68618) | 0 |
| De 61 a 180 dias | 14 | 2 | 8 | 4 |
| Mais de 180 dias | 10 | 1 | 4 | 5 |
| **Total** | **67** | **19** | **22** | **26** |

Diferença para a leitura pela coluna da visão: 573 passa de 34 para 19 dias (entra na faixa de 0 a 30), 68614 passa de 53 para 33 dias (continua de 31 a 60) e 68618 passa de 208 para 53 dias (sai de "mais de 180" e entra de 31 a 60, pausada). Pela coluna da visão, a faixa de até 60 dias teria 10 linhas, todas ativas; pela data do catálogo, que é a que vale, são 11 linhas e 10 ativas (P6 do plano do cmo). As demais divergências da seção 6.4 não mudam de faixa (continuam como já iniciadas).

- Das 19 campanhas ativas, 6 (31,6%) estão em turma já iniciada, 10 (52,6%) em turma que começa em até 60 dias e 3 (15,8%) em turma a mais de 60 dias.
- Das 11 linhas com início em até 60 dias pelo catálogo, 10 estão com campanha ativa; a exceção é o Curso de Ventilação Mecânica Aplicada à Anestesia Veterinária (68618, 18/12/2026, 53 dias), pausado.
- Das 35 linhas ainda não iniciadas (V33 a V67): 13 ativas, 13 pausadas e 9 sem campanha.

**Insight:** a mídia ligada segue o calendário de perto (10 de 11 turmas em até 60 dias estão ativas pela data do catálogo), mas um terço das campanhas ativas ainda roda em turma que já começou, e a única turma próxima sem campanha ligada (68618) pode estar pausada porque a aba de campanhas acha que ela é de maio de 2027.

**Ação:** gestor-de-midia leva à aprovação humana a decisão sobre as 6 ativas em turma iniciada (pedido A4 do plano), com gasto da semana de cada uma [CONFIRMAR], e pede à Ufape a data única da 68618 antes de qualquer decisão sobre ela.

**Ressalvas:** sem gasto por campanha, 6 ativas podem pesar muito ou quase nada. Não se sabe se essas turmas ainda aceitam entrada (política [CONFIRMAR]). As datas de 573, 68614 e 68618 são as da planilha (as do catálogo), que valem pela decisão 12 da Ufape (26/10/2026).

### Pergunta 2. A mídia ligada acompanha o ticket?

**Dados (Pós ainda não iniciadas na visão, preço total do catálogo, sem matrícula):**

| Status | Turmas | Mediana do ticket | Menor e maior |
|---|---|---|---|
| Ativa | 8 (707, 68604, 68606, 698, 68608, 68610, 289, 662) | R$ 35.400,00 | R$ 26.970,00 e R$ 47.700,00 |
| Pausada | 12 (657, 68615, 341, 333, 679 [CONFIRMAR], 68635, 366, 68617, 578, 382, 352, 60) | R$ 34.575,00 | R$ 28.050,00 e R$ 48.400,00 |
| Sem campanha | 7 (68628, 68632, 68609, 68616, 719, 68623, 699), fora a linha de Pneumologia (código [CONFIRMAR]) | R$ 33.000,00 | R$ 12.000,00 e R$ 38.940,00 |

Conta das medianas: valores ordenados de cada grupo. Ativa: 26.970; 30.000; 30.000; 35.400; 35.400; 35.400; 37.500; 47.700 (4º e 5º = 35.400). Pausada: 28.050; 29.700; 33.000; 33.000; 33.000; 33.750; 35.400; 36.000; 37.500; 43.500; 47.880; 48.400 (6º e 7º: (33.750 + 35.400) / 2 = 34.575). Sem campanha: 12.000; 32.450; 33.000; 33.000; 34.800; 35.772; 38.940 (4º = 33.000).

As 5 Pós de maior ticket ainda não iniciadas que aparecem na visão:

| Código | Curso | Ticket (site) | Dias | Status |
|---|---|---|---|---|
| 657 | Pós-graduação em Anestesiologia Avançada | R$ 48.400,00 | 138 | Pausada |
| 352 | Pós-graduação em Ventilação Mecânica | R$ 47.880,00 | 210 | Pausada |
| 707 | Pós-graduação em Oftalmologia Veterinária | R$ 47.700,00 | 4 | Ativa, só estático, sem 5 ângulos |
| 341 | Pós-graduação em Medicina Interna Equina | R$ 43.500,00 (promoção de 20% no site [CONFIRMAR regra, P16]) | 145 | Pausada |
| 68628 | Pós-graduação em Oncologia Veterinária | R$ 38.940,00 | 166 | Sem campanha |

**Insight:** o ticket não explica o status: as medianas dos três grupos ficam entre R$ 33.000,00 e R$ 35.400,00, e 3 das 4 maiores turmas futuras estão pausadas. Quem decide é a data, não o valor da turma.

**Ação:** o gestor-de-midia usa o ticket como peso explícito nas metas de custo (skill metas-de-custo) quando os números chegarem, começando por 657, 341 e 352.

**Ressalvas:** preço de lista não é receita (bolsas, descontos e inadimplência [CONFIRMAR]). O preço de 662 e 679 pode ser de outra turma (link trocado, auditoria de 26/10, seção 3).

### Pergunta 3. Há turmas que começam em até 30 dias sem campanha? E turmas iniciadas com campanha ativa?

**Em até 30 dias (até 25/11/2026), sem campanha:**

- Na visão: **nenhuma**. As 5 linhas da faixa pela data do catálogo (707, 68604, 68606, o Workshop Brasileiro de Neuromonitorização de 20/11 e 573, com 19 dias pelo catálogo) estão ativas.
- No catálogo, itens abertos com início em até 30 dias que **não constam** na visão (status de mídia desconhecido): Grupo de Estudos em Cardiologia e Ecocardiografia Veterinária (68665, 01/11/2026, 6 dias) e Grupo de Estudos em Clínica Médica e Emergência de Cães e Gatos (68666, 25/11/2026, 30 dias). Ticket de R$ 100,00 cada.
- Logo depois da janela, também sem status na visão: as 22 provas de bolsa de 27/11/2026 (32 dias) e o curso 68637 (28/11/2026, 33 dias, possível duplicado de 623).

**Turmas já iniciadas com campanha ativa (6, todas de Pós):**

| Linha da visão | Código | Curso | Dias | Formatos | Ângulos | Ticket (site) |
|---|---|---|---|---|---|---|
| V16 | 650 | Pós-graduação em Medicina de Felinos | -72 | Estático | Sem 5 | R$ 30.000,00 |
| V17 | 68662 | Pós-graduação em Odontologia Veterinária (link trocado) | -72 | Estático | Sem 5 | R$ 35.400,00 [CONFIRMAR] |
| V18 | 706 | Pós-graduação em Ultrassonografia de Pequenos Animais | -72 | Estático | Sem 5 | R$ 14.960,00 |
| V19 | 586 | Pós-graduação em Anestesiologia Veterinária (Direto ao ponto), EAD | -65 | Estático | Sem 5 | R$ 14.130,00 |
| V20 | 554 | Pós-graduação em Dor e Cuidados Paliativos na Veterinária | -65 | Estático e vídeo | Sem 5 | R$ 27.000,00 |
| V32 | 68612 | Pós-graduação em Nefrologia e Urologia Veterinária | -2 | Estático e vídeo | Com 5 | R$ 32.520,00 |

Mais 9 iniciadas com campanha pausada (V11, V15, V23, V24, V25, V26, V29, V30, V31). As 6 ativas batem com a lista do plano do cmo (seção 2.1, item 2).

**Insight:** o risco de "campanha sem turma" está todo na Pós e em turmas de 2 a 72 dias atrás; o risco de "turma sem campanha registrada" está fora da visão, nos itens de ticket baixo e nas provas de bolsa.

**Ação:** ver ações 1 e 2 na seção 3.

**Ressalvas:** a política de entrada em turma iniciada é [CONFIRMAR]; 5 das 6 começaram há mais de 60 dias.

### Pergunta 4. Quantas campanhas estão sem os 5 ângulos ou só com estático?

**Dados (41 linhas com campanha, ativa ou pausada):**

| | Ativa (19) | Pausada (22) | Total (41) |
|---|---|---|---|
| Só estático | 13 | 17 | 30 (73,2%) |
| Estático e vídeo | 6 | 4 | 10 |
| Só vídeo | 0 | 1 | 1 |
| Com 5 ângulos | 9 | 6 | 15 |
| Sem 5 ângulos | 10 (1 é o Workshop de Neuromonitorização, onde a visão diz que a regra não se aplica) | 16 | 26 (63,4%) |
| Sem 5 ângulos **ou** só estático | 15 | 19 | 34 (82,9%) |
| Com 5 ângulos **e** vídeo | 4 (68612, 68606, 698, 68608) | 3 (68605, 659, 366) | 7 |

Cruzamento das 19 ativas:

| | Com 5 ângulos | Sem 5 ângulos |
|---|---|---|
| Só estático | 5 (68604, 68610, 573, 68614, 289) | 8 (650, 68662, 706, 586, 707, Workshop de Neuromonitorização, 623, Paciente Grave) |
| Estático e vídeo | 4 (68612, 68606, 698, 68608) | 2 (554, 662) |

**Insight:** das 13 ativas em turma ainda não iniciada, só 3 (68606, 698, 68608) têm vídeo e os 5 ângulos. A Pós com reta final mais curta e maior ticket entre as ativas (707, 4 dias, R$ 47.700,00) roda o pacote mais pobre: só estático e sem 5 ângulos.

**Ação:** criativos-de-anuncio prioriza o pacote completo onde ainda dá tempo (33 dias ou mais pela data do catálogo: 68610, 68614 e, no lugar da 623, a 68637, porque nenhuma campanha nova aponta para a 623 até a correção da página, decisão 13), e não onde faltam 4 ou 5 dias. A 573 fica fora da lista: começa em 19 dias pela data da planilha, que vale (decisão 12; 34 pela visão).

**Ressalvas:** a visão não diz quais ângulos existem nem o desempenho de cada formato. "Com 5 ângulos" não prova resultado melhor; é hipótese a testar quando houver números.

### Pergunta 5. Como as campanhas se concentram por área e por linha?

**Por linha (todas as 67 linhas da visão):**

| Linha | Linhas na visão | Ativa | Pausada | Sem campanha |
|---|---|---|---|---|
| Pós | 42 | 14 | 18 | 10 |
| Livres | 21 | 3 | 4 | 14 |
| Eventos | 4 | 2 | 0 | 2 |
| Graduação | 0 | - | - | - |
| **Total** | **67** | **19** | **22** | **26** |

A Pós tem 14 das 19 ativas (73,7%).

**Cobertura do recorte de 110 itens do plano pela visão:**

| Linha | Itens no recorte | Constam na visão | Ativa | Pausada | Sem campanha | Não constam |
|---|---|---|---|---|---|---|
| Pós (30 turmas e 22 provas) | 52 | 27 | 8 | 12 | 7 | 25 (22 provas, 68636, 68629, 359) |
| Livres | 55 | 4 | 3 (623, 573, 68614) | 1 (68618) | 0 | 51 |
| Eventos | 3 | 3 | 2 (Workshop de Neuromonitorização, 700 [CONFIRMAR]) | 0 | 1 (202 [CONFIRMAR]) | 0 |
| **Total** | **110** | **34 (30,9%)** | **13** | **13** | **8** | **76 (69,1%)** |

Conta: a tabela de status da seção 3 do plano lista 34 itens com status e 76 "não consta" (25 na onda 1, 46 na onda 2, 5 na onda 3). Bate com a visão: das 35 linhas não iniciadas, 34 caem no recorte e 1 (Pneumologia, ligada ao código 670 fora do ar) fica fora.

**Por área de especialidade (seção 2.3 do plano), só os 34 itens do recorte que constam na visão:**

| Área | Itens na área | Ativa | Pausada | Sem campanha | Não constam |
|---|---|---|---|---|---|
| A1 Anestesiologia e dor | 14 | 0 | 1 (657) | 1 (68609) | 12 |
| A2 Cardiorrespiratório | 13 | 3 (289, 698, 573) | 2 (352, 68618) | 0 | 8 |
| A3 Emergência, terapia intensiva e clínica médica | 13 | 1 (700 [CONFIRMAR]) | 1 (68635) | 1 (68623) | 10 |
| A4 Cirurgia, ortopedia e reabilitação | 8 | 1 (662) | 2 (578, 366) | 1 (68632) | 4 |
| A5 Diagnóstico por imagem e endoscopia | 9 | 3 (68604, 68614, 623) | 0 | 0 | 6 |
| A6 Gastroenterologia | 5 | 1 (68606) | 0 | 0 | 4 |
| A7 Endocrinologia e nefrologia | 10 | 0 | 1 (68617) | 0 | 9 |
| A8 Dermatologia | 3 | 1 (68610) | 0 | 0 | 2 |
| A9 Oftalmologia | 4 | 1 (707) | 0 | 0 | 3 |
| A10 Oncologia | 4 | 0 | 0 | 1 (68628) | 3 |
| A11 Laboratório | 8 | 1 (68608) | 2 (68615, 333) | 1 (202 [CONFIRMAR]) | 4 |
| A12 Neurologia | 4 | 1 (Workshop de Neuromonitorização) | 0 | 1 (68616) | 2 |
| A13 Medicina felina | 6 | 0 | 0 | 0 | 6 |
| A14 Outras especialidades | 9 | 0 | 4 (679 [CONFIRMAR], 382, 341, 60) | 2 (699, 719) | 3 |
| **Total** | **110** | **13** | **13** | **8** | **76** |

**Insight:** A2 e A5 somam 6 das 13 ativas do recorte (46,2%), enquanto a maior área, A1 Anestesiologia e dor (14 itens), não tem nenhuma campanha ativa e tem a turma de maior ticket do recorte pausada (657, R$ 48.400,00). A1, A7, A10, A13 e A14 (43 itens somados: 14 + 10 + 4 + 6 + 9) estão com zero ativas.

**Ação:** o gestor-de-midia confere, na divisão de verba por área (etapa 1.11), se o zero em A1 é decisão ou lacuna, e a Ufape informa o motivo da pausa de 657.

**Ressalvas:**
- Área é agrupamento de mensagem do plano, não unidade de verba; uma área pode estar coberta por campanha institucional fora da visão [CONFIRMAR].
- A linha V67 (Paciente Grave, ativa) tem dois candidatos no catálogo (seção 6.3). As tabelas acima usam a hipótese do plano (produto 700). Se V67 for a linha da planilha de mesmo nome, sem página e sem código (catálogo, seção 9), ela sai do recorte e as contagens mudam: Eventos no recorte com 1 ativa e 2 itens na visão, A3 com 0 ativa, recorte com 12 ativas e 33 itens na visão (77 não constam). Nesse caso há uma campanha **ativa levando a um item sem página**, que falha no item "página de destino" da conformidade educacional.

---

## 2. Três insights não óbvios

1. **A planilha mede a mídia de um terço do que a squad vai vender.** 76 dos 110 itens do recorte (69,1%) não têm status na visão de campanhas, entre eles os 3 primeiros da matriz GUT: as 22 provas de bolsa (32 dias, porta de entrada da Pós) e os grupos 68665 e 68666 (6 e 30 dias). "Zero turmas em até 30 dias sem campanha" na visão é verdade só para o que a visão lista. Evidência: tabela de cobertura da pergunta 5 e tabela de status da seção 3 do plano.
2. **Há criativo completo parado em turma futura, enquanto turma com prazo curto roda o pacote mais pobre.** Três Pós ainda não iniciadas estão pausadas com os 5 ângulos prontos: 68615 (145 dias), 366 (166 dias, com vídeo) e 68617 (173 dias). Ao mesmo tempo, 707 (4 dias, R$ 47.700,00) roda só estático e sem 5 ângulos. Reativar o que já está pronto custa menos que produzir do zero. Evidência: V45, V53, V54 e V33 da visão; tabela da pergunta 4.
3. **O calendário da própria planilha não é único.** Em 10 das 67 linhas a data da visão difere da do catálogo, e o caso de Ventilação Mecânica (68618) muda a faixa de urgência: 53 dias pelo catálogo (18/12/2026, a data que vale) e 208 dias pela visão (22/05/2027), com a campanha pausada. Para 573 a diferença é de 19 dias (catálogo) para 34 (visão), e para 68614 de 33 (catálogo) para 53 (visão). Qualquer regra "ligar a campanha N dias antes" vai errar nesses itens até a Ufape fixar uma data. Evidência: tabela de divergências da seção 6.4.

## 3. Três ações (todas pedidos de aprovação humana)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| 1 | Gestor-de-midia leva à pessoa do marketing a decisão de pausar ou manter as 6 campanhas ativas em Pós já iniciadas (650, 68662, 706, 586, 554, 68612), com o gasto da última semana de cada uma | 31,6% das ativas estão em turma iniciada (pergunta 1) | gasto e diária [CONFIRMAR]; esta análise não propõe valor | liberar orçamento para onda 1 sem gastar em turma que talvez não aceite entrada | reativar no gerenciador de anúncios (ação humana) |
| 2 | Ufape inclui na visão de campanhas uma linha com código do catálogo e status de mídia para as 22 provas de bolsa, 68665, 68666, 68637, 616 e os contínuos, informa para onde leva a campanha ativa da V67 e envia o pacote de dados da seção 4 | 69,1% do recorte não tem status de mídia (insight 1); V67 pode levar a item sem página (pergunta 5) | sem custo de mídia | a squad passa a ver a mídia de todo o recorte, a começar pela onda 1 | não se aplica |
| 3 | Gestor-de-midia e criativos-de-anuncio avaliam reativar 68615, 366 e 68617 (criativos com 5 ângulos já prontos) na janela que as metas de custo indicarem, e direcionam a produção de vídeo e ângulos para itens com 33 dias ou mais pela data do catálogo (68610, 68614 e 68637, que substitui a 623 até a correção da página, decisão 13); 573 (19 dias pela data da planilha, que vale pela decisão 12) entra na reta curta | criativo pronto parado e pacote pobre na reta curta (insight 2, pergunta 4) | verba [CONFIRMAR] | mais cobertura de ângulos com menos produção nova | pausar de novo no gerenciador (ação humana) |

---

## 4. Pedido de dados para a Ufape

Regras para todos os envios:
- **Granularidade:** uma linha por código do catálogo (turma, edição ou produto) e por semana, de segunda a domingo, a partir de 01/08/2026 (para cobrir as turmas iniciadas com campanha ativa) [SUPOSIÇÃO: janela proposta pelo agente].
- **Chave de ligação:** o código do catálogo precisa estar no nome da campanha ou no utm_campaign. Sem ele, o dado não se liga à turma.
- **Sem dado pessoal:** só contagens e somas. Nenhum nome, telefone, CPF ou e-mail. Exportação em CSV ou planilha.
- **Definições escritas:** lead, inscrito e matriculado como o CRM conta (ver CRM abaixo).

### 4.1 Meta Ads

| Campo | Granularidade | Para que serve |
|---|---|---|
| Semana (data de início) | semana | eixo de tempo de toda a análise |
| Código do catálogo (no nome da campanha ou UTM) | campanha | ligar gasto à turma |
| Nome e ID da campanha, do conjunto e do anúncio | anúncio | separar teste de criativo e de público |
| Status (ativa, pausada) e data da última mudança | campanha | conferir a visão de campanhas e achar campanha ligada em turma iniciada |
| Objetivo da campanha | campanha | comparar só campanhas de mesmo objetivo |
| Valor gasto (R$) | anúncio e semana | custo por lead e por matrícula; onde a verba está de fato |
| Orçamento diário ou vitalício | conjunto | ritmo de gasto até a data de início |
| Impressões, alcance e frequência | anúncio e semana | saturação de público em turma de campanha longa |
| Cliques no link, CTR e CPC | anúncio e semana | força do criativo e do ângulo |
| Leads (formulário instantâneo) e custo por resultado | anúncio e semana | custo por lead por turma |
| Conversões do pixel (Lead, InitiateCheckout, Purchase) e valor | anúncio e semana | ligar anúncio a compra na loja |
| Formato do anúncio (estático, vídeo, carrossel) | anúncio | testar se vídeo muda o resultado (pergunta 4) |
| Ângulo do anúncio (rótulo de 1 a 5, padrão da Ufape) | anúncio | testar se os 5 ângulos mudam o resultado |
| Visualizações de 3 segundos e ThruPlay | anúncio e semana | qualidade dos vídeos |
| Região (estado) | conjunto e semana | separar SP e Goiânia |

### 4.2 Google Ads

| Campo | Granularidade | Para que serve |
|---|---|---|
| Semana | semana | eixo de tempo |
| Código do catálogo (nome da campanha ou UTM) | campanha | ligar à turma |
| Tipo de campanha (Pesquisa, Performance Max, Display, YouTube) | campanha | comparar só tipos iguais |
| Status e data da última mudança | campanha | conferir a visão de campanhas |
| Custo (R$) | campanha e semana | custo por lead e por matrícula |
| Impressões, cliques, CTR e CPC | grupo de anúncios e semana | eficiência por turma |
| Conversões por ação (formulário, WhatsApp, compra) e valor | campanha e semana | ligar busca a lead e a compra |
| Parcela de impressões na pesquisa e perdida por orçamento e por classificação | campanha e semana | saber se falta verba ou falta relevância em turma urgente |
| Termos de pesquisa com mais custo (somados, sem dado pessoal) | campanha e mês | palavras-chave por área (camada 2) |

### 4.3 CRM

| Campo | Granularidade | Para que serve |
|---|---|---|
| Definição escrita de lead, inscrito e matriculado | uma vez | todas as contas usam a mesma régua |
| Leads novos por origem (utm_source, utm_medium, utm_campaign) | turma e semana | custo por lead por canal |
| Leads qualificados (critério da Ufape) | turma e semana | separar lead barato de lead que vira matrícula |
| Inscritos (ou matrícula de R$ 250,00 ou R$ 350,00 paga) | turma e semana | taxa lead para inscrito |
| Matriculados (primeira mensalidade paga) | turma e semana | taxa lead para matrícula e custo por matrícula |
| Cancelamentos e desistências | turma e semana | matrícula líquida |
| Meta de matrículas e turma mínima (20 na Pós) | turma | saber quanto falta para confirmar cada turma |
| Situação da turma (confirmada, em risco, cancelada) | turma e semana | prioridade de verba |
| Etapa do funil e motivo de perda (categorias somadas) | turma e mês | entender por que lead não vira matrícula |
| Tempo da primeira resposta (mediana) | linha e semana | indicador antecedente do atendimento |
| Provas de bolsa: inscritos, presentes, bolsas concedidas por faixa e matrículas resultantes | prova (por especialidade e praça) | conversão da prova em matrícula (meta de apoio do plano) |

### 4.4 Planilha "DATAS CURSOS E PÓS" (aba Visão de Campanhas)

| Campo | Granularidade | Para que serve |
|---|---|---|
| Código do catálogo em cada linha | turma | acabar com os casamentos por nome (seção 6) |
| Uma data de início única, igual nas abas | turma | dias até o início confiáveis |
| Data de fim das inscrições | turma | saber quando pausar sem precisar de pedido |
| Vagas totais e vagas restantes | turma e semana | urgência real; libera "últimas vagas" só com número |
| Histórico de status de mídia (ativa, pausada, sem) com data | turma | medir quantos dias cada turma teve campanha antes do início |
| Verba planejada | turma e mês | comparar planejado e gasto |
| Quais ângulos foram usados (nome de cada um) | turma | ir além de "com" ou "sem 5 ângulos" |
| Data de entrada de cada lote de criativo | turma | ler efeito de criativo novo (exemplo: V40, comentário de 21/10/26) |
| Página de destino de cada campanha | turma | conferir link trocado, item sem página (V67) e páginas com a frase de certificação |
| Linhas para provas de bolsa, grupos de estudos, contínuos e Graduação | item | cobrir os 76 itens do recorte que não constam |

### 4.5 Loja (site faculdade.ufape.com.br)

| Campo | Granularidade | Para que serve |
|---|---|---|
| Pedidos pagos | código do produto e semana | vendas de Livres, Eventos e provas de bolsa |
| Receita bruta e líquida (R$) | código do produto e semana | receita da linha |
| Cupons usados (código e quantidade, exemplo SIMPNEUROMONIT) | código do produto e semana | efeito do desconto de aluno e ex-aluno |
| Forma de pagamento (à vista ou parcelado, em contagem) | código do produto e mês | ticket efetivo |
| Reembolsos e cancelamentos | código do produto e semana | receita líquida |
| UTM do pedido (source, medium, campaign) | código do produto e semana | ligar venda ao anúncio sem depender do pixel |
| Carrinhos abandonados (contagem) | código do produto e semana | perda no checkout |
| Cadastros "avise-me" (contagem) | código do produto e semana | demanda por turma sem venda |
| Produtos à venda com turma já iniciada (lista) | semana | fechar a pendência P8 do plano |

Complementar, se existir: GA4 (visitas por página de turma e taxa de conversão do formulário) e Chatwoot (conversas por turma e tempo de primeira resposta, somados). Ferramentas [CONFIRMAR] (ufape-geral.md, seção Ferramentas, vazia).

---

## 5. Árvore de métricas por linha (só estrutura, sem valores)

Toda meta fica [CONFIRMAR] até o plano aprovado ou a skill metas-de-custo. Nenhuma métrica soma linhas.

### 5.1 Pós-graduação

```
Topo: turmas confirmadas (turma mínima de 20) e receita da linha por turma  [meta: CONFIRMAR]
  Matrículas por turma (CRM)
    Leads da turma (CRM, Meta Ads, Google Ads)
      Verba por turma e semana (Meta Ads, Google Ads)
      Impressões, CTR e CPC por formato e ângulo (Meta Ads, Google Ads)
      Visitas à página da turma e conversão do formulário (GA4)
    Taxa lead para matrícula (CRM)
      Tempo de primeira resposta no WhatsApp (Chatwoot)
      Leads qualificados sobre leads (CRM)
      Motivos de perda (CRM)
    Ramo das provas de bolsa
      Inscritos na prova (loja) > presentes (CRM) > bolsas concedidas (CRM) > matrículas (CRM)
  Custo por lead = verba / leads (Meta Ads, Google Ads, CRM)
  Custo por matrícula = verba / matrículas (Meta Ads, Google Ads, CRM)
  Antecedentes de mídia: dias de campanha ativa antes do início; % de campanhas com vídeo e 5 ângulos (planilha)
```

| Perspectiva | Objetivo | Indicador | Meta | Iniciativa | Fonte |
|---|---|---|---|---|---|
| Financeira | turmas confirmadas com custo controlado | custo por matrícula por turma | [CONFIRMAR] | metas de custo em três cenários (gestor-de-midia) | Meta Ads, Google Ads, CRM |
| Aluno e mercado | lead que vira matrícula | taxa lead para matrícula por turma | [CONFIRMAR] | campanha única das provas de bolsa | CRM |
| Processos internos | rastreio completo até o CRM | % de leads com código da turma e UTM | [CONFIRMAR] | código do catálogo no nome de toda campanha | CRM, planilha |
| Aprendizado e crescimento | saber se vídeo e 5 ângulos funcionam | testes concluídos por mês | [CONFIRMAR] | teste de formato e ângulo em 2 turmas | Meta Ads, planilha |

5 da semana: matrículas por turma; custo por matrícula; leads por turma; tempo de primeira resposta; dias de campanha ativa antes do início.

### 5.2 Cursos Livres

```
Topo: vagas preenchidas por turma presencial, vendas semanais dos contínuos e receita da linha  [meta: CONFIRMAR]
  Pedidos pagos por produto (loja)
    Visitas à página do produto e conversão do checkout (GA4, loja)
    Carrinhos abandonados (loja)
    Verba e cliques por produto (Meta Ads, Google Ads)
  Custo por venda = verba / pedidos pagos (Meta Ads, Google Ads, loja)
  Venda cruzada para a Pós: compradores de Livres que viram lead de Pós, somados (CRM)  [SUPOSIÇÃO: ligação a validar]
```

| Perspectiva | Objetivo | Indicador | Meta | Iniciativa | Fonte |
|---|---|---|---|---|---|
| Financeira | receita por turma presencial | receita líquida por turma | [CONFIRMAR] | metas de custo por formato | loja |
| Aluno e mercado | turma presencial cheia | vagas preenchidas sobre vagas | [CONFIRMAR] | campanha de 4 a 8 semanas [SUPOSIÇÃO do contexto] | loja, planilha |
| Processos internos | só vender turma com data certa | produtos à venda com turma iniciada ou sem data | [CONFIRMAR] | correção das pendências P3 a P8 | loja, planilha |
| Aprendizado e crescimento | saber qual contínuo responde a remarketing | testes de remarketing concluídos | [CONFIRMAR] | kit sempre ligado por área | Meta Ads |

5 da semana: pedidos pagos por turma presencial; custo por venda; receita líquida; conversão do checkout; carrinhos abandonados.

### 5.3 Eventos

```
Topo: inscrições e receita por edição  [meta: CONFIRMAR]
  Inscrições presenciais (vagas do catálogo) e transmitidas (loja)
    Uso de cupom de aluno e ex-aluno (loja)
    Verba e cliques por edição (Meta Ads, Google Ads)
    Visitas à página do evento (GA4)
  Custo por inscrição = verba / inscrições (Meta Ads, Google Ads, loja)
  Gravados contínuos (700, 202): vendas por semana (loja)
```

| Perspectiva | Objetivo | Indicador | Meta | Iniciativa | Fonte |
|---|---|---|---|---|---|
| Financeira | receita por edição | receita líquida por edição | [CONFIRMAR] | metas de custo da edição | loja |
| Aluno e mercado | presencial cheio | inscrições presenciais sobre vagas | [CONFIRMAR] | kit do evento | loja, catálogo |
| Processos internos | mensagens de véspera e dia no prazo | mensagens aprovadas antes da data | [CONFIRMAR] | calendário do kit | planilha |
| Aprendizado e crescimento | saber o peso do cupom | inscrições com cupom sobre total | [CONFIRMAR] | leitura pós-evento | loja |

5 da semana: inscrições presenciais; inscrições transmitidas; custo por inscrição; uso de cupom; visitas à página.

### 5.4 Graduação (ramo à parte, cadeia do /campanha-de-vestibular)

```
Topo: matriculados por curso e praça (turma mínima de 30, catálogo)  [meta: CONFIRMAR]
  Inscritos no vestibular (CRM) > aprovados (CRM) > matriculados (CRM)
  Visitas à LP da Graduação com UTM (GA4)
  Custo por inscrito e por matriculado (Meta Ads, Google Ads, CRM)
```

Quadro e 5 da semana ficam com a cadeia da Graduação; a Graduação não aparece na visão de campanhas.

---

## 6. Tabelas de apoio

### 6.1 As 19 campanhas ativas

Dias pela data do catálogo; entre parênteses, a da visão quando diverge.

| Linha da visão | Código | Linha | Dias | Formatos | Ângulos | Ticket (site) |
|---|---|---|---|---|---|---|
| V16 | 650 | Pós | -72 | Estático | Sem 5 | R$ 30.000,00 |
| V17 | 68662 | Pós | -72 | Estático | Sem 5 | R$ 35.400,00 [CONFIRMAR] |
| V18 | 706 | Pós | -72 | Estático | Sem 5 | R$ 14.960,00 |
| V19 | 586 | Pós | -65 | Estático | Sem 5 | R$ 14.130,00 |
| V20 | 554 | Pós | -65 | Estático e vídeo | Sem 5 | R$ 27.000,00 |
| V32 | 68612 | Pós | -2 | Estático e vídeo | Com 5 | R$ 32.520,00 |
| V33 | 707 | Pós | 4 | Estático | Sem 5 | R$ 47.700,00 |
| V34 | 68604 | Pós | 5 | Estático | Com 5 | R$ 30.000,00 |
| V35 | 68606 | Pós | 12 | Estático e vídeo | Com 5 | R$ 35.400,00 |
| V36 | Workshop Brasileiro de Neuromonitorização de 20/11 (a visão usa outro nome) | Eventos | 25 | Estático | não se aplica | R$ 1.250,00 presencial; R$ 450,00 transmitido |
| V37 | 698 | Pós | 33 | Estático e vídeo | Com 5 | R$ 26.970,00 |
| V38 | 68608 | Pós | 33 | Estático e vídeo | Com 5 | R$ 35.400,00 |
| V39 | 68610 | Pós | 33 | Estático | Com 5 | R$ 30.000,00 |
| V40 | 623 | Livres | 33 | Estático | Sem 5 | R$ 890,00 |
| V41 | 573 | Livres | 19 (visão: 34) | Estático | Com 5 | R$ 2.350,00 |
| V42 | 68614 | Livres | 33 (visão: 53) | Estático | Com 5 | R$ 1.250,00 |
| V44 | 289 | Pós | 145 | Estático | Com 5 | R$ 35.400,00 |
| V55 | 662 | Pós | 180 | Estático e vídeo | Sem 5 | R$ 37.500,00 [CONFIRMAR, link trocado] |
| V67 | 700 ou linha "Paciente Grave" sem página [CONFIRMAR] | Eventos | 385 (visão; o catálogo não tem data) | Estático | Sem 5 | R$ 780,00 se for 700; sem preço se for a linha sem página |

### 6.2 As 22 campanhas pausadas

| Linha da visão | Código | Linha | Dias | Formatos | Ângulos |
|---|---|---|---|---|---|
| V11 | 592 (sem venda) | Livres | -86 | Estático | Sem 5 |
| V15 | 653 | Pós | -72 | Estático e vídeo | Sem 5 |
| V23 | 665 | Pós | -37 | Estático | Sem 5 |
| V24 | 666 | Pós | -37 | Estático | Com 5 |
| V25 | 99 | Livres | -30 | Estático | Sem 5 |
| V26 | 68668 | Livres | -7 (visão: -25) | Estático | Sem 5 |
| V29 | 68605 | Pós | -9 | Estático e vídeo | Com 5 |
| V30 | 659 | Pós | -9 | Estático e vídeo | Com 5 |
| V31 | 68607 | Pós | -2 | Vídeo | Sem 5 |
| V43 | 657 | Pós | 138 | Estático | Sem 5 |
| V45 | 68615 | Pós | 145 | Estático | Com 5 |
| V46 | 341 | Pós | 145 | Estático | Sem 5 |
| V47 | 333 | Pós | 152 | Estático | Sem 5 |
| V48 | 679 [CONFIRMAR] (linha "Citopatologia 03/04") | Pós | 159 | Estático | Sem 5 |
| V52 | 68635 | Pós | 166 | Estático | Sem 5 |
| V53 | 366 | Pós | 166 | Estático e vídeo | Com 5 |
| V54 | 68617 | Pós | 173 | Estático | Com 5 |
| V59 | 578 | Pós | 208 | Estático | Sem 5 |
| V60 | 382 | Pós | 208 | Estático | Sem 5 |
| V63 | 68618 | Livres | 53 (visão: 208) | Estático | Sem 5 |
| V64 | 352 | Pós | 210 | Estático | Sem 5 |
| V65 | 60 | Pós | 214 | Estático | Sem 5 |

Conta de V26: de 19/10/2026 (catálogo) a 26/10/2026 = 7 dias já passados. Continua na faixa "já iniciada".

### 6.3 Linhas da visão que não casam com um único código

| Linha da visão | Nome na visão | Candidato no catálogo | Problema |
|---|---|---|---|
| V13 | Curso de aprimoramento em cardiointensivismo veterinário (01/08/2026, UF "-") | 718 (29/08/2026) ou 68622 (sem data) | data e código [CONFIRMAR] |
| V14 | Prático de ultrassonografia point of care (01/08/2026) | 716 (05/09/2026, sem venda) | data diverge |
| V22 | Curso Prático de Imersão em Cirurgia Veterinária, SP (05/09/2026) | 433 (03/10/2026) | data diverge |
| V48 | Pós Graduação em Citopatologia Veterinária (03/04/2027) | 679 Infectologia, segundo o plano | link trocado |
| V50 | Pós-graduação em Pneumologia Veterinária (10/04/2027) | 670 (fora do ar) ou 68636 (17/04/2027) | código [CONFIRMAR] |
| V66 | Internacional de Coagulação (15/11/2027) | 202 (contínuo, sem data) | ligação [CONFIRMAR] |
| V67 | Paciente Grave Multidiciplinar Foco em casos Clinicos (15/11/2027, ONLINE, **campanha ativa**) | Hipótese 1 (a do plano): 700, Congresso Internacional do Paciente Grave Multidisciplinar, gravação, aberto (contínuo), R$ 780,00. Hipótese 2: a linha de **mesmo nome** do catálogo, seção 9, ONLINE, sem código, status "sem página", "só na planilha" | ligação [CONFIRMAR]. Na hipótese 2, há campanha ativa levando a um item sem página: risco de anúncio sem destino válido ou com destino que não entrega o que promete (item "página de destino" da conformidade educacional) e mudança nas contagens do recorte (ressalvas da pergunta 5) |

### 6.4 Datas diferentes entre visão e catálogo (10)

Vale a data do catálogo (planilha "DATAS CURSOS E PÓS", conforme a regra de fonte).

| Código | Catálogo (vale) | Visão |
|---|---|---|
| 599 | 20/06/2026 | 21/06/2026 |
| 717 | 01/08/2026 | 29/08/2026 |
| 718 [CONFIRMAR ligação] | 29/08/2026 | 01/08/2026 |
| 716 | 05/09/2026 | 01/08/2026 |
| 433 | 03/10/2026 | 05/09/2026 |
| 625 | 01/10/2026 | 03/10/2026 |
| 68668 | 19/10/2026 | 01/10/2026 |
| 573 | 14/11/2026 | 29/11/2026 |
| 68614 | 28/11/2026 | 18/12/2026 |
| 68618 | 18/12/2026 | 22/05/2027 |

As 3 últimas mudam os dias até o início de itens do recorte (já listadas como P6 no plano do cmo); 573 e 68618 mudam também de faixa (pergunta 1).

---

## 7. Auditoria de analytics (auditorias/09-analytics.md), conferência do próprio agente

- [x] Árvore de métricas existe (esboço por linha, seção 5).
- [x] Toda métrica tem uma fonte nomeada.
- [ ] Relatórios comparam com as metas: não se aplica nesta rodada, porque não há metas (P11 do plano) [CONFIRMAR].
- [ ] Metas não batidas mostradas: não se aplica nesta rodada, porque não há metas.
- [x] Insights terminam com uma ação.
- [x] Lacunas de dados sinalizadas (seções 0 e 4, V67 na seção 6.3).
- [ ] Backlog revisado todo mês: não se aplica a este agente; fica com o backlog-de-otimizacao (etapa 1.33).
- [ ] Custo por lead, custo por matrícula, conversão e receita por linha: não se aplica nesta rodada, porque não há números; estrutura pronta na seção 5, separada por linha, e nada foi estimado.
- [x] Nenhum dado pessoal.

O qa-de-marketing confere de novo com esta auditoria e com auditorias/conformidade-educacional.md antes de marcar como pronto.

---

## Mudanças desta versão

- Seções 1 e 6: o evento de 20/11 passa a ser chamado de Workshop Brasileiro de Neuromonitorização (decisão 7); sai "simpósio".
- Seções 1 e 3 e listas: datas pela planilha, inclusive 573, 68614, 68618, 68662 e 662 (decisão 12); saem os [CONFIRMAR] de data (P6).
- Seções 1 e 3: a produção de criativos que ia para a 623 vai para a 68637 até a correção da 623 (decisão 13).

## Fatos (com fonte)

- A visão de campanhas tem 67 linhas: 19 ativas, 22 pausadas e 26 sem campanha (docs/visao-de-campanhas-2026-10-26.md, contagem V1 a V67).
- Por linha: Pós 42 (14 ativas), Livres 21 (3 ativas), Eventos 4 (2 ativas), Graduação 0 (visão cruzada com contexto/catalogo-de-cursos.md).
- 6 ativas estão em Pós já iniciadas: 650, 68662, 706, 586, 554 e 68612 (visão; plano do cmo, seção 2.1).
- Pela data do catálogo, 10 das 11 linhas com início em até 60 dias estão ativas; a exceção é 68618, pausada a 53 dias (catálogo, seção 4; visão, V63).
- 573 começa em 14/11/2026 pelo catálogo (19 dias) e em 29/11/2026 pela visão (catálogo, seção 4; visão, V41). Vale a data da planilha, a do catálogo (decisão 12 da Ufape, 26/10/2026).
- 30 das 41 campanhas com status são só estáticas; 26 não têm os 5 ângulos (visão).
- 34 dos 110 itens do recorte constam na visão; 76 não constam, inclusive as 22 provas de bolsa (plano do cmo, seção 3).
- A1 Anestesiologia e dor, com 14 itens, não tem campanha ativa; A1, A7, A10, A13 e A14 somam 43 itens sem campanha ativa (plano do cmo, seção 2.3, cruzado com a visão).
- O catálogo tem uma linha "Paciente Grave Multidiciplinar Foco em casos Clinicos", ONLINE, "sem página", "só na planilha", com o mesmo nome da V67, que está ativa (catálogo, seção 9; visão, V67).
- Preços citados são os do site em 26/10/2026 (catálogo); a turma mínima da Pós é 20 (contexto/pos-graduacao.md).
- 10 datas diferem entre a visão e o catálogo (seção 6.4).

## Suposições

- [SUPOSIÇÃO] "Campanha ativa" é usada como indicador de onde a verba está; o gasto real pode ser muito diferente entre campanhas.
- [SUPOSIÇÃO] As ligações V48 = 679, V66 = 202 e V67 = 700 seguem o plano do cmo e não foram confirmadas pela Ufape; para V67 há uma segunda hipótese (seção 6.3).
- [SUPOSIÇÃO] Janela de dados a partir de 01/08/2026, proposta pelo agente.
- [SUPOSIÇÃO] Venda cruzada de Livres para Pós como ramo da árvore (contexto de Cursos Livres, ainda não validado).
- [SUPOSIÇÃO] Campanha de 4 a 8 semanas para Livres presenciais (contexto de Cursos Livres).

## Dados que faltam

- [CONFIRMAR] Gasto, orçamento, impressões, cliques e leads por campanha, turma e semana (Meta Ads, Google Ads).
- [CONFIRMAR] Leads, inscritos, matriculados e cancelamentos por turma e semana, com as definições do CRM.
- [CONFIRMAR] Pedidos pagos, receita, cupons e reembolsos por produto e semana (loja).
- [CONFIRMAR] Metas de matrícula, verba por linha e vagas restantes por turma.
- [CONFIRMAR] Status de mídia das 22 provas de bolsa, 68665, 68666, 68637, 616, 68636, 68629, 359, 68638, 560 e dos contínuos.
- [CONFIRMAR] Para onde leva a campanha ativa da linha V67 da visão: produto 700 ou a linha "Paciente Grave" sem página.
- [CONFIRMAR] Código do catálogo nas linhas V13, V14, V22, V48, V50, V66 e V67, As datas dos 10 itens da seção 6.4 seguem a planilha (decisão 12), inclusive 573, 68614, 68618, 68662 e 662.
- [CONFIRMAR] Política de entrada em turma já iniciada e motivo da pausa de 657, 341 e 352.
- [CONFIRMAR] Regra e validade da promoção de 20% da 341 (P16 do plano).
- [CONFIRMAR] Ferramentas de CRM, GA4 e atendimento (ufape-geral.md, seção Ferramentas).
