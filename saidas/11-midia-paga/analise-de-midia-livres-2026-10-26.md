# Revisão de mídia de Cursos Livres: diagnóstico estrutural das campanhas ativas e pausadas e roteiro de leitura para quando os números chegarem (etapa 1.12)

- **Agente:** analise-de-midia (departamento 11 Mídia Paga, reporta ao gestor-de-midia)
- **Linha:** livres
- **Data:** 26/10/2026 (segunda-feira)
- **Etapa:** 1.12 da camada 1 do plano do cmo (diagnostico-de-midia nas campanhas ativas e pausadas)
- **Status:** rascunho para o gestor-de-midia, para o qa-de-marketing (auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda ação em gerenciador de anúncios é feita por humano, depois da aprovação.
- **Natureza:** não existe nenhum número de desempenho nas fontes (gasto, impressões, cliques, CPM, CTR, visitas, inícios de checkout, pedidos pagos, custo por venda). A exportação pedida no memorando do gestor (seção 7.1) ainda não chegou. Este diagnóstico é estrutural: cruza a visão de campanhas (status, data, formatos, ângulos) com o catálogo e as fichas (status do produto, data na página, data na planilha, página duplicada, texto da página) e escreve, antes dos números, o roteiro de leitura (métricas, cortes, limiares e a decisão que cada resultado dispara). Todo número de desempenho aparece como [DADO NÃO FORNECIDO] ou [CONFIRMAR]. Nenhuma métrica foi inventada.
- **Entradas lidas:**
  - /home/user/marketing-ufape/.claude/agents/analise-de-midia.md
  - /home/user/marketing-ufape/.claude/skills/diagnostico-de-midia/SKILL.md e /home/user/marketing-ufape/.claude/skills/metas-de-custo/SKILL.md
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (briefing)
  - /home/user/marketing-ufape/docs/andamento-planejamento.md (conflitos entre saídas)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 3, com o status da mídia por item; seções 7 e 8)
  - /home/user/marketing-ufape/contexto/ufape-geral.md
  - /home/user/marketing-ufape/contexto/cursos-livres.md
  - /home/user/marketing-ufape/contexto/eventos.md (sobreposição de público com o workshop)
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seções 4, 5, 7 e 8)
  - Fichas de /home/user/marketing-ufape/contexto/cursos/livres/: 573, 68614, 623, 68637 e 68618 (data na página, texto de pagamento e de certificado, vagas)
  - /home/user/marketing-ufape/contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md (só para a sobreposição de público)
  - /home/user/marketing-ufape/docs/visao-de-campanhas-2026-10-26.md
  - /home/user/marketing-ufape/docs/auditoria-do-catalogo-2026-10-26.md (seções 4 e 7)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-livres-2026-10-26.md (1.11)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-geral-2026-10-26.md (memorando da onda 1, versão 2)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (só a seção 4.2, calendário das provas, para a sobreposição de público)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analise-de-campanha-livres-2026-10-26.md (1.32)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (1.10)
  - Referência só de formato e método (conteúdo não copiado): /home/user/marketing-ufape/saidas/11-midia-paga/analise-de-midia-pos-2026-10-26.md
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web. Nenhuma exportação de plataforma, de loja ou de CRM recebida.
- **Dados pessoais:** nenhum lido nem citado. Nenhum docente, aluno, candidato ou comprador aparece aqui.
- **Marcadores:** [DADO NÃO FORNECIDO] é número de desempenho que só a exportação traz. [CONFIRMAR] é fato que a Ufape precisa informar. [CONFIRMAR NO CATÁLOGO] é dado de curso que está só na ficha. [SUPOSIÇÃO] é hipótese deste agente, com a origem. "Regra prática" é regra de método da skill, não meta.
- **Unidade de julgamento em Livres:** o pedido pago na loja (e a vaga preenchida nos presenciais), não o lead (gestor 1.11, seção 2; analise-de-campanha, seção 0). Onde a skill diz CPL e custo por matrícula, aqui se lê custo por início de checkout (antecedente) e custo por venda (CPV).

---

## 0. Resumo em duas frases

As 3 campanhas ativas de Livres (573, 68614 e 623) têm, todas, um bloqueio que vem antes de qualquer número: em 573 e 68614 a visão de campanhas tem uma data diferente da que a planilha e a própria página mostram (14/11 e 28/11), e em 623 a página do produto mostra "01 e 02 de agosto de 2026" como início, uma data já passada, enquanto a página duplicada 68637 mostra 28 e 29/11. O gargalo principal hoje é o elo "chegada" (destino e data que o candidato vê), e só depois de corrigi-lo gasto, CTR, inícios de checkout e custo por venda passam a valer como evidência.

---

## 1. Regras de leitura aplicadas (escritas antes dos números)

1. **Sem número, sem decisão de desempenho** (memorando, regra 1; analise-de-campanha, R0). As decisões deste arquivo são de elegibilidade, conformidade e calendário. Nenhuma campanha é chamada de boa ou ruim.
2. **Dados suficientes** (skill, passo 2, regra prática): perdedor só depois de gastar de 1,5 a 2 vezes o CPVmax do produto sem venda; diferença entre anúncios com menos de 10 a 20 conversões de cada lado é ruído; janela mínima de 3 a 7 dias; os 2 últimos dias subcontam vendas (gestor 1.11, seção 8, item 7). Nos presenciais, o volume de compra quase nunca chega a isso: a leitura é de ritmo e de antecedentes (visita e início de checkout).
3. **Funil de cima para baixo:** entrega, atenção, interesse, chegada, conversão, venda (no lugar de matrícula), saturação. O primeiro elo fraco é a causa provável; o resto é consequência.
4. **Uma mudança por vez no mesmo conjunto,** no máximo uma por semana. Correção de conformidade é a única exceção (memorando, regra 3).
5. **Gerenciador, analytics e loja não batem: a decisão é INVESTIGAR,** e nenhuma decisão de desempenho vale até resolver.
6. **Não culpar o algoritmo antes de checar criativo, página e rastreamento** (instrução do agente).
7. **Julgar contra a meta escrita antes** (gestor 1.11, seção 8, item 9), nunca contra o resultado visto depois.
8. **Inscrição que volta não conta:** reembolso, cancelamento e turma que não abre saem do numerador (gestor 1.11, seção 8, item 4).

---

## 2. Metas contra realizado

As metas de Livres existem como fórmula no plano 1.11 (seções 2.2 a 2.5): custo por venda máximo (CPVmax = MC menos M), custo por início de checkout máximo (CPVmax x k) e CPC máximo (CPVmax x q), sem valor em reais, porque faltam fração à vista, taxas, devolução, custo variável, margem e conversões (LP1). Não recalculei nada com a skill metas-de-custo: a conta está pronta no 1.11 e este arquivo só a usa. O único limite em reais que existe é o teto absoluto (preço à vista, com taxa, custo e margem iguais a zero), que não é meta.

| Item | Meta (fonte) | Valor da meta | Teto absoluto (catálogo; não é meta) | Realizado |
|---|---|---|---|---|
| 573 Hands-On de Ecocardiografia Veterinária Básica | CPVmax conservador (1.11, 2.3) | [CONFIRMAR] (LP1) | R$ 2.350,00 | gasto, visitas, inícios de checkout, pedidos pagos [DADO NÃO FORNECIDO] |
| 68614 Curso Livre em Videotoscopia | CPVmax conservador; mínimo de 15 participantes (ficha) | [CONFIRMAR] | R$ 1.250,00 | [DADO NÃO FORNECIDO] |
| 623 (e 68637) Imersão em Endoscopia Digestiva | CPVmax conservador; mínimo de 15 (ficha) | [CONFIRMAR] | R$ 890,00 | [DADO NÃO FORNECIDO] |
| 68618 Ventilação Mecânica (pausada) | só leitura do histórico antes da pausa | [CONFIRMAR] | R$ 1.710,00 | histórico [DADO NÃO FORNECIDO] |
| 592, 99, 68668 (pausadas, turma passada ou sem venda) | sem meta: decisão por elegibilidade | não se aplica | não se aplica | histórico [DADO NÃO FORNECIDO] |

Conta de conferência dos tetos: R$ 2.350,00, R$ 1.250,00, R$ 890,00 e R$ 1.710,00 são os preços à vista do catálogo (seção 4). Em CPC, cada 1 ponto percentual de visita que vira pedido sobe o teto em R$ 23,50, R$ 12,50, R$ 8,90 e R$ 17,10, respectivamente (preço dividido por 100; 1.11, seção 2.4).

---

## 3. Retrato estrutural da mídia de Livres

### 3.1 Contagem (visão de campanhas de 26/10/2026)

| Situação | Linhas | Códigos |
|---|---|---|
| Campanha ativa | 3 | 623, 573, 68614 |
| Campanha pausada | 4 | 592, 99, 68668, 68618 |
| Sem campanha | 14 | 575, 605, 539, 500, 477, 621, 599, 617, 606, 718 ou 68622, 716, 717, 433, 625 |
| **Total** | **21** | |

Todas as 7 campanhas com status são só estáticas; 2 têm os 5 ângulos (573 e 68614) e 5 não têm (visão; analise-de-campanha, 1.4). Do recorte de 55 itens de Livres do plano do cmo, 51 não aparecem na visão (68637, 616, 68638, 560, 68665, 68666 e os 45 contínuos) [CONFIRMAR status de mídia].

### 3.2 As 3 ativas cruzadas com o catálogo e a página

Dias contados a partir de 26/10/2026.

| Código | Curso (catálogo) | Status no catálogo | Data na planilha (vale) | Data na página (ficha) | Data na visão | Dias (planilha) | Formatos e ângulos | O que bloqueia antes do número |
|---|---|---|---|---|---|---|---|---|
| 573 | Curso Hands-On de Ecocardiografia Veterinária Básica, São Paulo, semipresencial, 28 h, R$ 2.350,00 à vista ou 10x de R$ 303,00 | aberto | 14/11/2026 | 14 e 15/11/2026 | 29/11/2026 | 19 | estático, com 5 ângulos | (a) a visão está 15 dias depois da página e da planilha; (b) a página tem dois textos de pagamento ("6 x de 550 reais no boleto" pedido por e-mail e "carta de crédito"), U7 da 1.9; (c) a página usa "equipamentos de última geração" (superlativo sem fonte, vetado nas peças pelo 1.11, seção 7) |
| 68614 | Curso Livre em Videotoscopia, São Paulo, presencial, 12 h, R$ 1.250,00 à vista ou 10x de R$ 175,00 | aberto | 28/11/2026 | 28 e 29/11/2026 | 18/12/2026 | 33 | estático, com 5 ângulos | (a) a visão está 20 dias depois da página e da planilha; (b) a página traz frase de certificação ligada ao regulador (selo), que a squad não repete e que bloqueia verba nova (1.11, seção 8, item 10); (c) devolução total por cancelamento só até 29/10 (30 dias antes, ficha): depois disso nenhum anúncio cita a regra |
| 623 | III curso de imersão teórico e prático em endoscopia digestiva, São Paulo, presencial, 12 h, R$ 890,00 à vista ou 6x de R$ 205,00 | aberto | 28/11/2026 | **01 e 02 de agosto de 2026** | 28/11/2026 | 33 | estático, sem 5 ângulos; 3 criativos novos em 21/10/2026 | a página do produto mostra uma data já passada (ficha 623, alerta; auditoria do catálogo de 26/10, seção 4); a página duplicada 68637 (turma IV, só no site) mostra 28 e 29/11/2026 |

### 3.3 As 4 pausadas cruzadas com o catálogo

| Código | Curso | Status no catálogo | Data (planilha) | Data na visão | Leitura estrutural | Decisão |
|---|---|---|---|---|---|---|
| 68618 | Curso de Ventilação Mecânica Aplicada à Anestesia Veterinária, teórico-prático, 17 h, R$ 1.710,00 à vista ou 1x de R$ 1.800,00 | aberto | 18/12/2026 | 22/05/2027 | a página mostra "18, 19 e 20 de dezembro", "Turma I" e formato presencial; o catálogo deixa a modalidade em branco e o site está sem data de início no campo próprio (auditoria, seção 7). Se 18/12 valer, a campanha está pausada dentro da janela de 8 semanas, aberta em 23/10 | manter pausada até a LP6 do 1.11 (Ufape confirma 18/12/2026 até 13/11) |
| 592 | Curso Teórico/Prático de bloqueio locorregional guiado por ultrassonografia, São Paulo | sem venda (avise-me) | 01/08/2026 | 01/08/2026 | destino sem compra | manter pausada; se houver anúncio ativo apontando para a página, pausa imediata |
| 99 | Curso Prático de Imersão em Cirurgia Veterinária, Goiânia | verificar (turma já iniciada e com venda) | 26/09/2026 | 26/09/2026 | turma passada ainda à venda | manter pausada; reativar só com data nova confirmada |
| 68668 | Aprimoramento Terapia Intensiva Veterinária, 48 h, R$ 100,00 | verificar (turma já iniciada e com venda) | 19/10/2026 | 01/10/2026 | turma iniciada; teto absoluto de R$ 100,00 por venda | manter pausada |

### 3.4 Sem campanha e fora da visão (informativo)

- As 14 linhas sem campanha são de turmas passadas, sem data ou sem venda (575, 605, 539, 500, 477, 621, 599, 617, 606, 716, 717, 433, 625 e a linha de cardiointensivismo, que pode ser 718 ou 68622 [CONFIRMAR]; analista 1.10, seção 6.3). Nenhuma pede ação de mídia.
- 68637 (duplicado de 623), 616 (05/12/2026), 68638 (06/03/2027), 560 (22/05/2027), os grupos 68665 e 68666 e os 45 contínuos não aparecem na visão. A pergunta é se existe campanha que a planilha não registra (analise-de-campanha, 2.5). Grupos: sem mídia paga (memorando, D21). 616: campanha nova pela LP7 do 1.11 (10/11).

---

## 4. Gargalo do funil (diagnóstico estrutural, elo por elo)

Sem números, o que dá para ler é se cada elo tem condição de funcionar. O elo que falha primeiro invalida a leitura dos de baixo.

| Elo | O que a estrutura mostra hoje | Campanhas afetadas | Diagnóstico | Evidência |
|---|---|---|---|---|
| 0. Elegibilidade (o produto pode ser vendido?) | as 3 ativas estão "aberto"; as 3 pausadas antigas estão "verificar" ou "sem venda" | 592, 99, 68668 (pausadas) | elo bom nas ativas; nas pausadas, a pausa é a decisão certa | catálogo, seção 4 |
| 1. Entrega (CPM) | sem dado; três campanhas da linha disputam públicos de outras linhas a partir de 03/11 (seção 5, NL5) | 573 (cardio), 616 e 68618 quando subirem (anestesia) | [DADO NÃO FORNECIDO]. Risco estrutural de leilão mais caro por sobreposição com a Pós e as provas | gestor-de-midia-pos, 4.2; visão |
| 2. Atenção (retenção de 3 segundos) | as 7 campanhas com status são só estáticas | todas | não mensurável: sem vídeo não há retenção a ler | visão |
| 3. Interesse (CTR do link, CPC) | sem dado; ângulos rotulados só como "com" ou "sem 5" | todas | [DADO NÃO FORNECIDO]; sem rótulo por anúncio, não dá para dizer qual ângulo funciona | visão |
| 4. Chegada (visualizações da página por clique; o que a página mostra) | 623 leva (se a URL for a do produto 623) a uma página com início em 01/08/2026; 573 e 68614 têm página coerente com a planilha, mas a visão usada pela mídia diverge; 573 tem pagamento contraditório e 68614 tem frase de certificação ligada ao regulador | 623, 573, 68614 (as 3 ativas) | **primeiro elo fraco**: a página pode não entregar o que o anúncio promete (623) ou ter pendência de conformidade (573, 68614). CTR e conversão dessas campanhas não valem como evidência até a correção | fichas 573, 68614 e 623; auditoria do catálogo, seção 4 |
| 5. Conversão (taxa da página, custo por início de checkout) | evento de compra nas páginas de Livres no pixel e no Google não testado (LP3 do 1.11; D8 do memorando) | todas | [DADO NÃO FORNECIDO]. Sem saber o evento registrado, o custo por início de checkout de uma campanha não se compara com o de outra | 1.11, LP3 |
| 6. Venda (pedido pago, custo por venda, vagas) | código do catálogo no utm_campaign [CONFIRMAR]; em 573 parte do pagamento sai da loja (boleto parcelado pedido por e-mail à secretaria) | todas; 573 em especial | [DADO NÃO FORNECIDO]. Venda fora da loja não carrega UTM: o custo por venda de 573 tende a sair maior do que é [SUPOSIÇÃO, origem: texto da página] | ficha 573; 1.11, LP3 |
| 7. Saturação (frequência e CTR ao longo dos dias) | 623 recebeu 3 criativos em 21/10 (aprendizado em curso); 573 e 68614 com pacote único estático, data de criação [CONFIRMAR] | 573, 68614 | risco a medir, não fato | visão |
| Calendário | a visão põe 573 em 29/11 e 68614 em 18/12, mas planilha e página dizem 14/11 e 28/11 | 573, 68614 | se a mídia foi programada pela visão, a campanha pode estar com ritmo de quem tem mais tempo do que tem, e com data de término depois do curso [CONFIRMAR no gerenciador] | visão; fichas; catálogo |

**Conclusão do diagnóstico:** o primeiro elo fraco é a chegada, nas 3 ativas, e o segundo é o calendário de 573 e 68614. A ação certa nos dois é de conformidade e de calendário, não de desempenho. Parte já está pedida (memorando D12 e D19; 1.11 LP3, LP4 e LP5); o que é novo está na seção 5 e nas ações LA2 e LA3.

---

## 5. Achados novos deste diagnóstico (não estavam nas entradas de mídia)

| # | Achado | Evidência | Fato ou hipótese | O que muda |
|---|---|---|---|---|
| NL1 | A página do produto 623 mostra início em "01 e 02 de agosto de 2026". A página 68637, com o mesmo curso e o mesmo preço, mostra "28 e 29 de novembro de 2026" e "Turma IV". O nome da 623 começa com "III curso" | fichas 623 e 68637; auditoria do catálogo de 26/10, seção 4 | a data na página é fato. A leitura de que 623 é a página da turma III (agosto, já realizada) e 68637 a da turma IV (novembro) é [SUPOSIÇÃO, origem: número romano no nome e data de cada página] | O memorando (D19) e o 1.11 tratam 623 e 68637 como duplicidade a decidir até 31/10. Se a suposição valer, a campanha ativa de 623, com 3 criativos novos desde 21/10, manda clique para uma página de turma passada. É o mesmo tipo de risco da 698 na Pós (D2). A conferência da URL vira prioridade de 28/10 (ação LA2) |
| NL2 | Em 573 e 68614 a página e a planilha concordam (14 e 15/11; 28 e 29/11). Só a visão de campanhas diverge (29/11; 18/12) | fichas 573 e 68614; catálogo; visão | fato | A pendência P6 do plano do cmo, nesses dois itens, é da planilha de mídia, não do produto. Riscos: (a) data de término programada no gerenciador pela visão, com gasto depois do curso; (b) ritmo de gasto de quem acha que tem 34 e 53 dias, quando tem 19 e 33. A regra D12 (anúncio sem data) continua certa até a Ufape confirmar (ação LA3) |
| NL3 | A página de 68618 diz "Primeira turma: 18, 19 e 20 de dezembro de 2026", formato presencial, e "turmas subsequentes com periodicidade bimestral". A visão marca 22/05/2027, dois dias antes da Pós 352 em Ventilação Mecânica (24/05/2027) | ficha 68618; visão; catálogo | os textos são fato; a leitura de que a linha da visão pode ter herdado a data de outra turma ou da Pós 352 é [SUPOSIÇÃO] | Reforça o pedido LP6 do 1.11 (confirmar 18/12 até 13/11). Se 18/12 valer, a pausa atual tira a campanha da janela de 8 semanas aberta em 23/10 |
| NL4 | Parte da venda de 573 pode acontecer fora da loja: "PARA PAGAMENTO EM BOLETO, SOLICITAR VIA E-MAIL" e "6 x de 550 reais no boleto" | ficha 573 | o texto é fato; o efeito na medição é [SUPOSIÇÃO] | Pedido pago por boleto via secretaria não carrega UTM. Na leitura, a venda de 573 soma loja e secretaria por código, e o custo por venda só é calculado com as duas fontes (portão G6) |
| NL5 | Sobreposição de público a partir de 03/11: 573 (cardio) roda junto com a Pós 698 (cardio, campanha ativa) e com as provas de Cardiologia 68641 e 68642 (03/11 a 26/11, pico de 03/11 a 09/11); 616 e 68618 (anestesia), quando subirem, rodam junto com as provas de Anestesiologia e com a mídia do Workshop Brasileiro de Neuromonitorização (frio e remarketing de 03/11 a 18/11) | gestor-de-midia-pos, 4.2 e PP3; gestor-de-midia-eventos, 1.6; 1.11 de Livres, seção 3 | as datas são fato; o efeito no leilão é [SUPOSIÇÃO, origem: conjuntos da mesma conta com públicos parecidos disputam a mesma entrega] | Na leitura, CPM subindo com CTR estável em 573 a partir de 03/11 é lido primeiro como disputa interna, não como fadiga nem como falha do criativo. As exclusões da LP10 do 1.11 cobrem só 20/11 a 27/11; de 03/11 a 19/11 vale observar a frequência somada (ação LA5 e seção 11) |

---

## 6. Divergências com a loja e o CRM

Não há exportação do gerenciador, da loja nem do CRM. A conciliação não pode ser feita. O que já se sabe que vai impedir ou distorcer a conciliação:

| Risco | Onde | Efeito na leitura | Como tratar quando os dados chegarem |
|---|---|---|---|
| Código do catálogo ausente no nome da campanha ou no utm_campaign [CONFIRMAR] | 573, 68614, 623 | pedido pago não se liga à campanha | medir o percentual de pedidos com UTM por código; abaixo de 100%, os sem UTM ficam "origem não atribuída", sem rateio por estimativa |
| Duas páginas para o mesmo curso | 623 e 68637 | pedidos se dividem entre dois códigos; a campanha pode levar a uma e a venda cair na outra | somar os pedidos dos dois códigos para a turma de 28/11 e registrar a URL final de cada anúncio |
| Venda fora da loja | 573 (boleto pedido por e-mail) | a loja subconta as vendas e o custo por venda sobe | pedir à secretaria a contagem de vendas por boleto, por produto e semana, somada |
| Reembolso e cancelamento | 68614 (devolução total até 29/10), 623 e 68637 (reembolso se a turma não for confirmada) | venda que volta infla o resultado | ler vendas líquidas (1.11, seção 8, item 4) |
| Evento de conversão diferente entre campanhas [CONFIRMAR] | todas | "resultado" no gerenciador pode ser visualização da página numa e compra noutra | comparar só campanhas com o mesmo evento |
| Data de término programada pela visão [CONFIRMAR] | 573, 68614 | gasto depois da data do curso aparece como gasto sem venda possível | separar o gasto posterior à data da planilha antes de calcular o custo por venda |

Regra: se gerenciador e loja diferirem acima da tolerância, a decisão do item é INVESTIGAR. A tolerância é [CONFIRMAR com o analista-de-dados]; não fixo número sem histórico.

---

## 7. Criativos cansados

Sem frequência, CTR e custo por início de checkout por anúncio ao longo das semanas, nenhum criativo pode ser chamado de cansado. Candidatos a olhar primeiro (hipótese, não fato):

| Campanha | Por que é candidata | O que confirma fadiga | O que derruba |
|---|---|---|---|
| 573 | pacote único estático; data de criação [CONFIRMAR]; se a campanha seguiu a janela da visão, roda desde o início de outubro [SUPOSIÇÃO] | frequência subindo e CTR do link caindo por 3 dias ou mais no mesmo anúncio, com custo por início de checkout subindo (skill, tabela de sintomas) | CTR estável; ou CPM subindo com CTR estável (aí é leilão, NL5) |
| 68614 | pacote único estático; mesma regra | mesma regra | idem |
| 623 | não é candidata hoje: 3 criativos entraram em 21/10 e ainda aprendem | leitura antes e depois de 21/10, peça por peça, com a ressalva de que criativo novo reinicia o aprendizado (analise-de-campanha, 2.3) | não se aplica |

Fadiga confirmada pede conceito novo, não só título novo. Exceção de calendário: em 573, se a data for 14/11, nenhum criativo novo entra depois de 07/11 (menos de 7 dias; memorando, 5.1, regra 1).

---

## 8. Roteiro de leitura quando a exportação chegar

Prazo: 2 dias úteis depois de receber a exportação (encomenda do 1.11, seção 7). Se ela chegar em 28/10 (quarta), a primeira versão numérica sai em 30/10 (sexta). Ordem fixa: portões, funil de cima para baixo, leitura por grupo, decisão.

### 8.1 Portões de qualidade do dado (antes de qualquer conta)

| # | Portão | Passa quando | Se não passar |
|---|---|---|---|
| G1 | Exportação sem dado pessoal | só contagens e somas | devolver; não abrir |
| G2 | Campos mínimos do memorando (7.1) mais URL final, data de criação, formato e ângulo por anúncio e data de término programada | todos presentes para 573, 68614, 623 e 68618 | ler o que existe e marcar o resto [DADO NÃO FORNECIDO] |
| G3 | Janela e granularidade | uma linha por campanha, anúncio e semana, desde a criação até a exportação | só acumulado: sem tendência nem fadiga; pedir de novo |
| G4 | Ligação com o produto | código do catálogo no nome ou no utm_campaign | campanha sem código vai para "não atribuída" (LP3) |
| G5 | Contexto do período | o que mudou (criativos de 21/10 em 623, verba, URL, pausa de 68618 e motivo) | mudança sem causa registrada vira hipótese |
| G6 | Conciliação | pedidos pagos da loja por código e UTM, mais vendas por boleto da secretaria (573), contra os resultados do gerenciador | diferença acima da tolerância [CONFIRMAR]: INVESTIGAR |

### 8.2 Funil de cima para baixo: métrica, corte, limiar e decisão disparada

Limiares de custo são [CONFIRMAR] até a LP1 do 1.11. Limiares de tendência são regras práticas da skill. A referência é a própria conta, nunca benchmark externo.

| Etapa | Métrica e conta | Cortes | Limiar | Decisão que dispara |
|---|---|---|---|---|
| Ritmo de gasto | gasto da semana dividido por (diária x 7) | campanha, semana | abaixo do orçamento com poucas impressões | entrega travada: AJUSTAR orçamento, lance ou público, um por vez |
| Entrega | CPM = gasto / impressões x 1.000 | plataforma, campanha, semana | CPM subindo contra a linha de base, com CTR estável | leilão mais caro; em 573 a partir de 03/11, ler NL5 antes; renovar criativo ou ampliar público, sem mexer em verba |
| Interesse | CTR do link = cliques no link / impressões; CPC = gasto / cliques no link | anúncio, ângulo (573, 68614), peça antes e depois de 21/10 (623) | CTR abaixo da mediana dos anúncios da mesma campanha com 3 a 7 dias de dados | AJUSTAR: trocar ângulo; menos que isso, "ainda é ruído" |
| Chegada | visualizações da página / cliques no link; URL final | campanha, URL | queda contra a linha de base; URL que abre página com data diferente da planilha | INVESTIGAR página e rastreio antes de mexer no anúncio; URL errada: AJUSTAR o destino (exceção de conformidade) |
| Conversão | taxa da página = inícios de checkout / visualizações; custo por início de checkout = gasto / inícios | campanha, evento de otimização | custo por início de checkout acima de CPVmax x k depois de gastar de 1,5 a 2 vezes esse valor | com CTR bom: problema depois do clique (página, pagamento, checkout); pedir analise-cro. Com CTR ruim: voltar ao interesse |
| Conversão mínima | q mínima = CPC observado / CPVmax (1.11, fórmula 7) | produto | q mínima maior que a taxa de pedido por visita da loja [CONFIRMAR] | o CPC não cabe na meta com a conversão que a loja tem: AJUSTAR criativo, público ou página |
| Venda | pedidos pagos líquidos; custo por venda = gasto / pedidos pagos líquidos | produto, origem (UTM), semana | lido com 2 semanas fechadas e janela de 7 dias depois do clique (1.11, seção 8, item 3) | acima do CPVmax com volume: AJUSTAR um elo; abaixo e com volume: ESCALAR em passos de até 20% da diária, dentro da verba e das vagas |
| Ritmo de vagas | ritmo necessário = (mínimo ou meta menos vendidos) / semanas até a data de confirmação da turma | presencial | ritmo real abaixo do necessário em 2 leituras | reforço pela reserva L7 (LP8 do 1.11), decisão do cmo |
| Saturação | frequência e CTR do link por anúncio, dia a dia | anúncio | frequência subindo e CTR caindo por 3 dias ou mais | AJUSTAR: conceito novo, um anúncio por vez, nunca a menos de 7 dias da data |
| Queda súbita | queda de entrega ou de conversão de um dia para outro | campanha | qualquer | pagamento recusado, anúncio reprovado, página fora do ar, pixel parado: INVESTIGAR no mesmo dia |

Decisões possíveis (skill, passo 5): ESCALAR, MANTER, AJUSTAR, PAUSAR (gastou o suficiente e está fora da meta por 2 semanas depois de um ajuste, R6; nos presenciais com menos de 2 semanas até a data, vale a pausa na data ou ao lotar) e INVESTIGAR.

### 8.3 Leitura por grupo

| Grupo | Itens | O que ler | Para que serve | Decisão possível |
|---|---|---|---|---|
| Presencial de 14/11 (se a data valer) | 573 | gasto desde a criação; data de término programada; pedidos pagos (loja e secretaria); vagas [CONFIRMAR] | ritmo até 13/11 e revisão pós-curso em 21/11 | MANTER sem data no anúncio (D12); sem criativo novo depois de 07/11; pausa no fim do dia útil anterior à data (LP5) |
| Presenciais de 28/11 | 68614, 623 (e 68637) | URL final de cada anúncio; pedidos por código (623 e 68637 somados); mínimo de 15 [CONFIRMAR NO CATÁLOGO]; peças antes e depois de 21/10 em 623 | ritmo até a data de confirmação da turma [CONFIRMAR]; leitura dos criativos de 21/10 | 623: ver LA2; 68614: MANTER sem verba nova até a página sair da pendência |
| Pausada com data a confirmar | 68618 | motivo e data da pausa; gasto, cliques e pedidos do período ativo; URL | linha de base para a reativação de 19/11 (LP6) | manter pausada até a LP6 |
| Pausadas antigas | 592, 99, 68668 | confirmar status pausado e ausência de anúncio ativo; histórico | linha de base por área (cirurgia, anestesia, terapia intensiva) | manter pausadas |
| Itens sem status na visão | 68637, 616, contínuos | existe campanha fora da planilha? | descoberta (analise-de-campanha, 2.5) | se existir, entrar no grupo certo acima |

### 8.4 Contas que a leitura vai mostrar (fórmulas; valores [DADO NÃO FORNECIDO])

- CPM = gasto / impressões x 1.000
- CTR do link = cliques no link / impressões
- CPC do link = gasto / cliques no link
- Taxa de chegada = visualizações da página / cliques no link
- Taxa da página = inícios de checkout / visualizações da página
- Custo por início de checkout = gasto / inícios de checkout
- Custo por venda = gasto / pedidos pagos líquidos (loja mais secretaria, por código)
- q mínima = CPC observado / CPVmax (1.11, fórmula 7)
- Gasto mínimo para julgar um anúncio = 1,5 x CPVmax (ou 1,5 x custo por início de checkout máximo, se a campanha otimiza para checkout) (regra prática)
- Ritmo necessário = (mínimo ou meta menos vendidos) / semanas até a data de confirmação da turma

Toda conta aparece com os números usados, para o gestor conferir.

### 8.5 Calendário de leitura

| Data | Leitura |
|---|---|
| 28/10 (quarta) | URL final dos anúncios de 623, 573 e 68614; data de término programada; prazo da exportação (D6) |
| 29/10 (quinta) | último dia da devolução total da 68614 para a turma de 28/11; conferir que nenhum anúncio cita a regra depois disso |
| 30/10 (sexta) | primeira versão numérica deste diagnóstico, se a exportação chegar em 28/10 |
| 03/11 (terça) | revisão semanal 1 (02/11 é feriado) |
| 09/11 | revisão 2: ritmo de 573 |
| 13/11 (sexta) | pausa de 573, se a data for 14/11 (sábado) |
| 16/11 | revisão 3: ritmo de 68614 e da página de endoscopia escolhida |
| 21/11 | revisão pós-curso de 573, se a data for 14/11 (7 dias depois) |
| 23/11 | revisão 4: pausa dos presenciais de 28/11 na data ou ao lotar |
| 27/11 (sexta) | pausa de 68614 e da endoscopia, se quem executa não trabalhar no sábado 28/11 [CONFIRMAR] |
| 05/12 | revisão pós-curso de 68614 e da endoscopia |

---

## 9. Tabela de decisão (estrutural, hoje)

"Hoje" vale sem número. A coluna "Muda quando" diz o que tiraria o item da decisão atual.

| Item | Métrica-chave quando houver número | Diagnóstico hoje | Decisão hoje | Referência | Muda quando |
|---|---|---|---|---|---|
| 573 | ritmo de pedidos pagos até 13/11; custo por venda (loja e secretaria) | página e planilha em 14/11, visão em 29/11; pagamento contraditório na página | MANTER sem data no anúncio e sem aumento; INVESTIGAR a data de término programada | memorando D12; 1.11 LP5; ação LA3 | Ufape confirma a data e o texto único de pagamento |
| 68614 | ritmo contra o mínimo de 15; custo por venda | página e planilha em 28/11, visão em 18/12; frase de certificação ligada ao regulador na página | MANTER sem data no anúncio, sem verba nova até a página sair da pendência | D12; 1.11, seção 8, item 10; ação LA4 | página corrigida |
| 623 | URL final; CTR das peças de 21/10; pedidos (623 mais 68637) | página do produto com início em 01/08/2026 | INVESTIGAR a URL em 28/10; AJUSTAR o destino se for a página com data passada; PAUSAR se não houver página coerente até 30/10 | NL1; D19; ação LA2 | Ufape corrige a data da 623 ou escolhe a 68637 |
| 68637 | existência de campanha | duplicado de 623, página com 28 e 29/11 | não criar campanha; conferir se existe alguma | D19 | escolha da Ufape |
| 68618 | histórico antes da pausa | data divergente; pausada dentro da janela se 18/12 valer | manter pausada | 1.11 LP6; NL3 | Ufape confirma 18/12/2026 até 13/11 |
| 592 | anúncio ativo apontando para a página | sem venda | manter pausada | analise-de-campanha, 2.4 | não muda |
| 99 | idem | turma passada | manter pausada | idem | data nova confirmada |
| 68668 | idem | turma iniciada; R$ 100,00 | manter pausada | idem | regra de entrada e meta escrita |
| 68665, 68666 | não se aplica | ticket de R$ 100,00 | sem mídia paga | memorando D21 | decisão do cmo sobre 68666 |
| 616 | não se aplica (sem campanha) | data em 05/12; modalidade a confirmar | sem campanha até a LP7 (10/11) | 1.11 LP7 | aprovação da LP7 |

Nenhuma decisão de ESCALAR é possível nesta rodada: não há meta em reais nem volume lido.

---

## 10. Até 5 ações em ordem de impacto (pedidos de aprovação humana)

Executa: humano no gerenciador ou na Ufape. Aprovador: a pessoa do marketing que aprovou o plano do cmo, até a tabela de aprovação de contexto/ufape-geral.md ser preenchida. Ordem pelo impacto na leitura e no gasto.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| LA1 | Enviar a exportação do memorando (7.1) para 573, 68614, 623 e 68618, com cinco campos a mais por anúncio: URL final, data de criação, data de término programada, formato e ângulo; e, da loja e da secretaria, pedidos pagos e reembolsos por código e semana, somados, com e sem UTM | sem ela nenhum elo de entrega, interesse, conversão ou venda pode ser lido; os campos a mais fecham NL1, NL2 e NL4 | sem custo de mídia | primeira versão numérica deste diagnóstico em 2 dias úteis | não se aplica | 28/10 (D6) |
| LA2 | 623: um humano confere em 28/10 a URL final dos anúncios. Se for a página do produto 623 (início em 01/08/2026), a Ufape corrige a data dessa página ou escolhe a 68637 até 30/10 (sexta), e o humano ajusta a URL no mesmo dia (correção de conformidade, fora da regra de uma mudança por semana). Sem nenhuma das duas até o fim de 30/10, pausar a campanha 623, com exportação prévia, nunca excluir | a página mostra uma data já passada para um curso de 28/11 (NL1); o prazo de D19 (31/10) cai num sábado | diária atual [CONFIRMAR], sem aumento | nenhum clique pago leva a página com data errada; a leitura dos criativos de 21/10 passa a valer | voltar a URL anterior ou reativar a campanha com as configurações exportadas | conferência 28/10; correção ou pausa até o fim de 30/10 |
| LA3 | 573 e 68614: a Ufape confirma as datas que a planilha e a página já mostram (14/11 e 28/11) e corrige a visão de campanhas; um humano confere a data de término programada das duas campanhas e, se ela seguir a visão, ajusta para o dia útil anterior à data do curso | a divergência é só da planilha de mídia (NL2); gasto depois do curso seria gasto sem venda possível | sem custo de mídia | pausa no dia certo; ritmo lido contra o prazo real | voltar a data de término anterior | 28/10 |
| LA4 | Ufape corrige as páginas de destino das ativas: 68614 sem a frase de certificação ligada ao regulador; 573 com um texto único de pagamento (U7 da 1.9). Até a correção, nenhuma verba nova nas duas e a leitura de conversão delas fica marcada "página com pendência" | a página é o elo "chegada" das duas campanhas; conformidade educacional (destino entrega o que o anúncio promete) | sem custo de mídia | destino coerente com o catálogo e com a regra de certificação | não se aplica | 30/10 |
| LA5 | Congelar mudanças por desempenho em 573, 68614 e 623 até a primeira leitura com 3 a 7 dias de dados e metas da LP1; só valem as ações de conformidade e calendário (D12, D19, LA2 a LA4, LP5). De 03/11 a 19/11, registrar CPM e frequência de 573 lado a lado com a 698 e as provas de Cardiologia, e de 616 com o workshop e as provas de Anestesiologia, quando subirem | mudança antes da linha de base apaga a comparação e pode reabrir o aprendizado (623 aprende desde 21/10); CPM subindo nessa janela pode ser disputa interna (NL5) | sem custo de mídia | linha de base limpa para a 1.13 e para a revisão de 09/11 | liberar ajustes na revisão seguinte, com pedido | a partir de hoje até a primeira leitura numérica |

---

## 11. O que observar a seguir

| Métrica | Onde | Confirma o diagnóstico | Derruba o diagnóstico |
|---|---|---|---|
| URL final dos anúncios de 623 | gerenciador | abre a página com início em 01/08/2026: o elo "chegada" é o gargalo de 623 | abre a 68637 ou uma página com 28/11: 623 entra na leitura normal |
| Data de término programada de 573 e 68614 | gerenciador | 29/11 e 18/12 (ou sem término): a mídia foi planejada pela visão | término no dia da planilha: a divergência ficou só na planilha |
| Percentual de pedidos pagos de Livres com UTM e código | loja e secretaria | abaixo de 100% [valor DADO NÃO FORNECIDO]: o custo por venda não fecha por produto e a LP3 é urgente | 100%: leitura por produto já é possível |
| CPM de 573 de 03/11 a 09/11 contra a semana anterior, com CTR | gerenciador | CPM sobe e CTR fica estável: disputa de leilão com a Pós e as provas de cardio (NL5) | CPM estável: a sobreposição não pesa |

---

## 12. Notas sobre arquivos de outros agentes (não alterados)

- gestor-de-midia-livres-2026-10-26.md (1.11), seção 7: a encomenda pedia o diagnóstico "com a exportação do memorando". A exportação não chegou; este arquivo entrega a parte estrutural e o roteiro, e a versão numérica sai 2 dias úteis depois da exportação. A "leitura de 623 antes e depois de 21/10" só vale depois de LA2.
- gestor-de-midia-livres-2026-10-26.md, seções 4.2 e 9 (LP4): trata 573 e 68614 como "datas a confirmar" (P6). Pelas fichas, página e planilha já concordam; a divergência é da visão (NL2). Sugestão para a próxima versão: P6 nesses dois itens vira "corrigir a visão" e não "confirmar a data do curso".
- gestor-de-midia-geral-2026-10-26.md (memorando), D19, e gestor de Livres, seção 6: o prazo de 31/10 para a página única de endoscopia e para o teste de rastreio cai num sábado (26/10/2026 é segunda). Este arquivo usa 30/10 (sexta) em LA2.
- gestor-de-midia-geral-2026-10-26.md, seção 5.2, linha 623: "não mexer até 28/10" continua certo para criativos; a URL é exceção de conformidade (LA2).
- analise-de-campanha-livres-2026-10-26.md, seção 2.3 (623): o critério pede para "resolver a duplicidade"; NL1 sugere que pode não ser duplicidade, e sim duas turmas (III em agosto, IV em novembro). Fica para a Ufape confirmar.
- gestor-de-midia-livres-2026-10-26.md, seção 3 e LP10: as exclusões de público começam em 20/11, mas a sobreposição com as provas e com o workshop começa em 03/11 (NL5). Não peço exclusão nova (o memorando, 4.4, prefere controlar frequência a excluir públicos entre campanhas); peço só a leitura lado a lado (LA5).
- Conflito já registrado em docs/andamento-planejamento.md (relatório de 02/11 na analise-de-campanha-livres): este arquivo segue 03/11.

---

## 13. Auditorias

### 13.1 auditorias/11-midia-paga.md (aplicada a este diagnóstico)

| Item | Resultado | Observação |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais justificados | Pendente externo | 1.11 de Livres aguarda LP1, LP2 e LP14 |
| Metas de custo escritas antes de subir | Pendente externo | fórmulas no 1.11; valores em LP1 |
| Verba dentro do valor aprovado, com aprovador | Pendente externo | verba e aprovador [CONFIRMAR] |
| Nomenclatura padrão | Pendente externo | código do catálogo no nome e na UTM (LP3) |
| UTMs completas e origem chegando à loja e ao CRM | Pendente externo | seção 6; portões G4 e G6 |
| Pixel, API de Conversões, conversões do Google | Pendente externo | LP3 do 1.11; elo 5 da seção 4 |
| Criativos em conformidade educacional | Pendente externo | este arquivo não cria criativo |
| Anúncios dentro das políticas | Não se aplica | nenhum anúncio criado aqui |
| Nenhum público com menores de 18 anos | Não se aplica | nenhum público criado aqui |
| Post de docente promovido com autorização | Não se aplica | nenhum post |
| Relatório semanal ao cmo | Atendido no desenho | calendário na seção 8.5, sem feriado |
| Sem segmentação discriminatória | Não se aplica | |
| Públicos sem dados pessoais sem base legal | Atendido | nenhum público, nenhum dado pessoal |
| Dados de curso conferidos no catálogo | Atendido | datas, preços e status do catálogo; textos de página só das fichas, marcados como tal |
| Destino de WhatsApp oficial | Não se aplica | a mídia de Livres não leva ao WhatsApp |
| Números da análise só das exportações fornecidas | Atendido | nenhum número de desempenho; as únicas contas são dias até a data, prazos e tetos de preço do catálogo |
| Nenhuma alteração sem humano executar e aprovar | Atendido | toda ação está na seção 10 com o que, por que, quanto, efeito e como desfazer |

### 13.2 auditorias/conformidade-educacional.md (pontos que este arquivo toca)

| Item | Resultado | Observação |
|---|---|---|
| Dados de curso iguais ao catálogo | Atendido | seção 3; divergências marcadas (573, 68614, 623, 68618) |
| Produto "verificar" ou "sem venda" sem chamada para compra | Atendido | 592, 99 e 68668 seguem pausadas |
| Curso livre não confere diploma; sem frase de certificação ligada ao regulador | Atendido | a frase da página de 68614 é citada só como pendência (LA4), nunca como afirmação |
| Bolsa e desconto com regra | Atendido | nenhum desconto citado; regra de devolução da 68614 sai das peças depois de 29/10 |
| Urgência real | Atendido | nenhuma urgência sem número; mínimos de turma só para planejamento |
| Destino entrega o que o anúncio promete | Pendente externo | 623 (LA2), 573 e 68614 (LA3, LA4) |
| Nenhum dado pessoal | Atendido | |
| Texto sem travessão nem meia-risca | Atendido | conferido por busca dos caracteres no arquivo |

**Resultado:** pronto para o gestor-de-midia e para o qa-de-marketing. Não libera nenhuma mudança no gerenciador; as ações da seção 10 esperam aprovação humana.

---

## Fatos (com fonte)

- 21 linhas de Livres na visão: 3 ativas (623, 573, 68614), 4 pausadas (592, 99, 68668, 68618), 14 sem campanha; todas as 7 com status são só estáticas; 573 e 68614 com 5 ângulos; 623 com 3 criativos novos em 21/10/2026 (visão de campanhas; analise-de-campanha-livres, 1.1 e 1.4).
- Datas da planilha (catálogo): 573 em 14/11/2026, 68614 e 623 em 28/11/2026, 68618 em 18/12/2026; na visão: 29/11/2026, 18/12/2026, 28/11/2026 e 22/05/2027 (catálogo, seção 4; visão).
- Páginas: 573 diz "14 e 15/11/2026"; 68614 diz "28 e 29 de novembro de 2026"; 623 diz "01 e 02 de agosto de 2026"; 68637 diz "28 e 29 de novembro de 2026", turma IV; 68618 diz "18, 19 e 20 de dezembro de 2026", turma I, presencial, turmas seguintes bimestrais (fichas).
- 573: página com "6 x de 550 reais no boleto", boleto pedido por e-mail à secretaria e "carta de crédito"; 68614: página com frase de certificação ligada ao regulador (selo); 68614: mínimo de 15 e máximo de 30, devolução total até 30 dias antes; 623 e 68637: mínimo de 15 (fichas).
- Preços à vista e parcelas de 573, 68614, 623, 68637, 68618, 68668 e 99; status "aberto", "verificar" e "sem venda" (catálogo, seção 4).
- Decisões e pedidos D12, D19, D21 (memorando); LP1 a LP14 (1.11 de Livres); provas de 03/11 a 26/11 com pico de 03/11 a 09/11 (gestor-de-midia-pos, 4.2 e PP3); mídia do workshop de 03/11 a 18/11 (gestor-de-midia-eventos, 1.6).
- 26/10/2026 é segunda-feira; 31/10, 14/11 e 28/11 são sábados; 02/11 e 20/11 são feriados (calendário).
- Regras práticas de dados suficientes e tabela de sintomas (skill diagnostico-de-midia).

## Suposições

- [SUPOSIÇÃO] 623 é a página da turma III (agosto de 2026) e 68637 a da turma IV (novembro de 2026), e não uma duplicidade (NL1). Origem: número romano no nome e data de cada página.
- [SUPOSIÇÃO] A data da visão para 68618 pode ter vindo de outra turma ou da Pós 352 (NL3). Origem: 22/05/2027 fica a 2 dias de 24/05/2027.
- [SUPOSIÇÃO] Venda por boleto via secretaria não carrega UTM, e o custo por venda de 573 sai maior do que é (NL4). Origem: texto da página.
- [SUPOSIÇÃO] Conjuntos da mesma conta com públicos parecidos (cardio; anestesia) disputam a entrega de 03/11 a 19/11 (NL5). Origem: calendários dos planos de Pós e Eventos.
- [SUPOSIÇÃO] 573 e 68614 rodam desde o início de outubro, se seguiram a janela da visão (candidatos a fadiga). Origem: janela de 4 a 8 semanas do contexto da linha aplicada às datas da visão.
- Usadas como estão, das entradas: N = 2 semanas em R6, escala em passos de até 20% da diária, janela de atribuição de 7 dias, otimização para compra ou início de checkout conforme o rastreio (todas [SUPOSIÇÃO] do 1.11 e da 1.32).

## Dados que faltam

- [CONFIRMAR] Exportação agregada de Meta e Google de 573, 68614, 623 e 68618 por campanha, anúncio e semana, com URL final, data de criação, data de término programada, formato e ângulo (LA1).
- [CONFIRMAR] URL final dos anúncios de 623 e a escolha da Ufape entre a correção da página 623 e a 68637 (LA2).
- [CONFIRMAR] Datas de 573 e 68614 confirmadas pela Ufape e visão corrigida (LA3); data de 68618 (LP6).
- [CONFIRMAR] Correção das páginas de 68614 (frase de certificação) e de 573 (texto de pagamento) (LA4).
- [CONFIRMAR] Pedidos pagos e reembolsos por código e semana, na loja e na secretaria (boleto de 573), com e sem UTM.
- [CONFIRMAR] Metas em reais (LP1): fração à vista, taxas, devolução, custo variável, margem, q e k por produto.
- [CONFIRMAR] Vagas totais e restantes e data de confirmação de cada presencial.
- [CONFIRMAR] Motivo da pausa de 68618; status de mídia de 68637, 616 e dos 45 contínuos.
- [CONFIRMAR] Evento de otimização de cada campanha; status do pixel e das conversões do Google nas páginas de Livres (LP3).
- [CONFIRMAR] Quem executa no gerenciador e se trabalha no sábado (pausas de 14/11 e 28/11).
- [CONFIRMAR] Tolerância de diferença entre gerenciador e loja (com o analista-de-dados).
- [CONFIRMAR NO CATÁLOGO] Mínimos, máximos e regras de cancelamento dos presenciais; modalidade de 68618.
- [DADO NÃO FORNECIDO] Gasto, impressões, alcance, frequência, cliques, CTR, CPC, CPM, visitas, inícios de checkout, pedidos pagos e custo por venda de qualquer campanha.

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma.

---

**Próximo agente sugerido:** criativos-de-anuncio (conferir se algum criativo ativo de 573, 68614 ou 623 cita data, regra de devolução depois de 29/10 ou superlativo da página, e rotular formato e ângulo no nome dos anúncios novos). Antes, o gestor-de-midia leva LA1 a LA5 à aprovação humana e o qa-de-marketing revisa este arquivo.
