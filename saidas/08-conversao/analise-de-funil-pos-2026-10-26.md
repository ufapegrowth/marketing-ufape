# Análise de funil: Pós-graduação e prova de bolsa (funil desenhado, sem números)

- **Agente:** analise-de-funil (departamento 08 Conversão), etapa 1.31 da camada 1
- **Linha:** pos
- **Data:** 26/10/2026
- **Status:** rascunho para o qa-de-marketing e para a aprovação da pessoa do marketing. Nada foi publicado, enviado ou pago.
- **Natureza desta entrega:** não existe nenhum número de funil (visitas, leads, inscrições, matrículas) [CONFIRMAR]. Por isso este arquivo desenha o funil como ele existe hoje, nomeia cada etapa e o evento que a mede, lista hipóteses de queda, propõe a instrumentação mínima e define as perguntas que os números precisam responder primeiro. Nenhuma taxa de conversão foi escrita nem estimada.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md (para a fronteira entre as linhas)
  - saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (seções 0, 4 e 5)
  - saidas/08-conversao/analise-cro-pos-2026-10-26.md
  - saidas/08-conversao/analise-cro-livres-2026-10-26.md (só a síntese, para comparar)
  - saidas/01-inteligencia-de-mercado/insights-de-alunos-pos-2026-10-26.md (seções 2, 4, 5 e 8)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1, 3 e 7)
- **Não reaberto nesta etapa:** contexto/catalogo-de-cursos.md e as fichas. Os dados de curso citados (código, início, turma mínima, regras da prova) vêm das saídas acima, que já os conferiram com o catálogo. Todo dado de curso que não esteja nelas aparece como [CONFIRMAR NO CATÁLOGO]. Não foi aberto faculdade.ufape.com.br.
- **Dado pessoal:** nenhum. Tudo que o funil pede é contagem somada por turma e semana.

---

## 0. Limites desta análise

1. Não há número de GA4, CRM, Chatwoot, loja, Meta Ads nem Google Ads. Tudo que depende de número é [CONFIRMAR].
2. As ferramentas de CRM, GA4 e atendimento não estão informadas (ufape-geral.md, seção Ferramentas). Os nomes de evento abaixo são proposta e valem para qualquer ferramenta [CONFIRMAR ferramenta].
3. Não se sabe o que o botão COMPRAR cobra na página da turma (matrícula de R$ 250,00, 1ª mensalidade ou os dois) [CONFIRMAR]. O funil trata o pagamento como uma etapa com tipo de pagamento registrado, para a pergunta ser respondida pelo dado.
4. A definição de lead, inscrito e matriculado ainda é a do CRM e não foi enviada [CONFIRMAR]. Até lá valem as definições provisórias da seção 1.3 [SUPOSIÇÃO].
5. Os sinais de atrito vêm de leitura de página e de contexto (E), não de comportamento medido. Toda ordem de prioridade abaixo é avaliação do agente e muda quando chegarem os números.

---

## 1. Funil por etapa

A Pós tem dois caminhos que terminam na mesma matrícula: a compra direta na página da turma (trilha A) e a prova de bolsa (trilha B, funil paralelo). O candidato pode usar os dois: ver a página, não comprar, fazer a prova e se matricular depois. Por isso cada etapa tem um identificador de turma e de origem, para não contar a mesma pessoa duas vezes na hora de somar matrículas por turma.

### 1.1 Trilha A: compra direta na página da turma

```
A1 anúncio ou busca (clique)
  > A2 visita à página da turma
    > A3 intenção: clique em COMPRAR, no WhatsApp (se existir) ou no link da prova de bolsa
      > A4 contato com o time de vendas (lead no CRM e conversa no WhatsApp)
        > A5 checkout iniciado
          > A6 pagamento (matrícula e/ou 1ª mensalidade) [CONFIRMAR o que COMPRAR cobra]
            > A7 matriculado (1ª mensalidade paga, definição do analista-de-dados)
              > A8 turma confirmada (mínimo de alunos atingido)
                > A9 início da turma e matrícula líquida (cancelamentos e desistências)
```

| Etapa | Nome | O que conta | Evento ou medida | Fonte | Existe hoje? |
|---|---|---|---|---|---|
| A1 | Clique no anúncio ou na busca | cliques com UTM e código da turma, por semana | clique no anúncio (plataforma) | Meta Ads, Google Ads | Existe nas plataformas; ligação com a turma só se o código estiver no nome da campanha ou no utm_campaign [CONFIRMAR] |
| A2 | Visita à página da turma | visitantes únicos da página da turma, por origem | visualizacao_pagina_turma (parâmetro codigo_turma) | GA4 | [CONFIRMAR ferramenta e se há tag nas páginas] |
| A3 | Intenção | visitantes que clicaram em COMPRAR, WhatsApp ou link da prova de bolsa | clique_comprar, clique_whatsapp, clique_prova_bolsa | GA4 | COMPRAR existe nas páginas (E); WhatsApp e link da prova só em parte das páginas (E, CRO); eventos de clique [CONFIRMAR] |
| A4 | Contato com o time | conversas novas por turma e leads novos no CRM, com origem | conversa_iniciada (Chatwoot) e lead_criado (CRM) | Chatwoot, CRM | [CONFIRMAR]; o site informou instabilidade no WhatsApp interno em 22/10/2026 (ufape-geral.md) |
| A4b | Tempo da primeira resposta | mediana por semana | primeira_resposta_em menos conversa_iniciada_em | Chatwoot | [CONFIRMAR] |
| A5 | Checkout iniciado | visitantes que abriram o checkout | inicio_checkout | loja, GA4 | [CONFIRMAR] |
| A6 | Pagamento | pedidos pagos, com tipo (matrícula, 1ª mensalidade) | compra_concluida (parâmetros tipo_pagamento e codigo_turma) | loja | [CONFIRMAR] |
| A7 | Matriculado | primeira mensalidade paga, por turma e semana | matricula_paga | CRM | [CONFIRMAR] |
| A8 | Turma confirmada | situação da turma: confirmada, em risco, cancelada, com a data da mudança | turma_confirmada (campo situacao_turma e data) | CRM ou planilha | [CONFIRMAR]; a data em que a turma é confirmada não consta nas fichas (insights, H-T2) |
| A9 | Início e matrícula líquida | presentes no módulo 1 e cancelamentos | cancelamento_registrado | CRM | [CONFIRMAR] |

Conversão entre etapas (a calcular quando houver números, nunca antes):

| De | Para | Conta | Valor |
|---|---|---|---|
| A1 | A2 | visitas da página ÷ cliques | [CONFIRMAR] |
| A2 | A3 | visitantes que clicaram ÷ visitantes únicos | [CONFIRMAR] |
| A3 | A4 | conversas e leads ÷ visitantes que clicaram | [CONFIRMAR] |
| A4 | A5 | checkouts ÷ leads | [CONFIRMAR] |
| A5 | A6 | pagamentos ÷ checkouts | [CONFIRMAR] |
| A4 | A7 | matriculados ÷ leads (taxa lead para matrícula, métrica da árvore do analista) | [CONFIRMAR] |
| A7 | A8 | matriculados da turma ÷ mínimo de alunos (20, contexto da linha) | [CONFIRMAR] |

Observação sobre A3 e A4: o candidato de ticket alto pode ir da página direto para o WhatsApp sem passar por COMPRAR, ou comprar sem falar com ninguém. As duas portas existem e a conta de A3 para A4 precisa separar as duas origens [SUPOSIÇÃO: o candidato de pós conversa antes de pagar, hipótese do CRO ainda não validada].

### 1.2 Trilha B: prova de bolsa (funil paralelo)

Regras lidas nas páginas das 22 provas de 27/11/2026 (iguais em todas, contexto/pos-graduacao.md): inscrição de R$ 100,00, prova presencial, nota de corte 7,0, 11 bolsas por prova (2 de 50%, 4 de 25% e 5 de 10%), 2 dias úteis para recurso, 10 dias úteis para a matrícula depois do resultado.

```
B1 visita à página da prova
  > B2 inscrição na prova (R$ 100,00 pagos)
    > B3 comparecimento à prova presencial (27/11/2026)
      > B4 resultado (nota de corte 7,0) e divulgação (WhatsApp ou e-mail)
        > B5 bolsa concedida, ou aprovado sem bolsa
          > B6 matrícula dentro de 10 dias úteis
            > B7 1ª mensalidade paga (matriculado)
              > B8 turma confirmada
```

| Etapa | Nome | Evento ou medida | Fonte | Existe hoje? |
|---|---|---|---|---|
| B1 | Visita à página da prova | visualizacao_pagina_prova (codigo_prova, especialidade, praça) | GA4 | [CONFIRMAR] |
| B1b | Chegada vinda da página da turma | clique_prova_bolsa (de qual turma veio) | GA4 | exemplo: 68610 tem "Clique aqui" (E); clique medido [CONFIRMAR] |
| B2 | Inscrição paga | pedidos pagos da prova, por especialidade e praça | loja | [CONFIRMAR] |
| B3 | Comparecimento | presentes sobre inscritos | CRM ou lista de presença | [CONFIRMAR] (pedido do analista, seção 4.3) |
| B4 | Aprovação | notas acima da nota de corte, em contagem; recursos | CRM | [CONFIRMAR] |
| B5 | Bolsa | bolsas por faixa (50%, 25%, 10%) e aprovados sem bolsa | CRM | [CONFIRMAR]; a regra de distribuição e o que fazer com aprovado sem bolsa não estão publicadas (CRO, página 3) |
| B6 | Matrícula | matrículas feitas depois da prova, por prova | CRM | [CONFIRMAR] |
| B7 | 1ª mensalidade | matriculados vindos da prova | CRM | [CONFIRMAR] |
| B8 | Turma confirmada | igual à A8 | CRM | [CONFIRMAR] |

Conversão entre etapas: B1 para B2, B2 para B3, B3 para B4, B4 para B6 e B6 para B7. Todas [CONFIRMAR]. Não existe número hoje.

Três fatos do desenho que o funil precisa registrar, porque mudam a leitura:

1. A turma de destino de cada prova não aparece na página [CONFIRMAR]. Para Felinos, Endoscopia, Nefrologia e Odontologia não há turma futura aberta da mesma área no catálogo (cmo, seção 2.3). Sem destino, B6 não pode ser ligada a uma turma.
2. O mínimo para confirmar a turma é 15 na página da prova e 20 nas páginas das turmas [CONFIRMAR NO CATÁLOGO]. A8 e B8 mudam conforme o número que valer.
3. A prova de Dermatologia (68646) é em 27/11/2026 e a turma 68610 começa em 28/11/2026. O prazo de 10 dias úteis para a matrícula cai depois do início da turma, e a regra da 1ª mensalidade ("30 dias antes do início", E) não combina com esse calendário [CONFIRMAR regra para quem entra depois].

### 1.3 Definições provisórias de etapa [SUPOSIÇÃO]

Valem só até a Ufape enviar as definições do CRM (pedido do analista, seção 4.3). A régua tem de ser uma só para todas as contas.

| Termo | Definição provisória |
|---|---|
| Lead | pessoa que deixou contato (formulário, conversa no WhatsApp ou inscrição na prova) com código de turma |
| Inscrito | lead com matrícula (R$ 250,00) ou inscrição na prova (R$ 100,00) paga |
| Matriculado | 1ª mensalidade paga |
| Turma confirmada | matriculados da turma maiores ou iguais ao mínimo vigente |

---

## 2. Hipóteses de queda, por prioridade

Critério de ordem (avaliação do agente, [SUPOSIÇÃO]): quanto a evidência já lida aponta para a hipótese, quanto o ticket e o prazo agravam o efeito, e quanto o número que vai chegar consegue confirmar ou descartar. Todas são hipótese até haver número. As evidências (E) vêm dos arquivos lidos.

| # | Hipótese | Etapa onde a queda apareceria | Evidência (E) | Que dado confirma | Que dado descarta | Prioridade |
|---|---|---|---|---|---|---|
| 1 | **Pagar antes de saber se a turma abre.** A 1ª mensalidade é paga até 30 dias antes do início e o reembolso só ocorre se a turma não for confirmada. A página não diz quando a turma é confirmada. | A4 para A5, A5 para A6, A6 para A7 | Insights H-T1 e H-T2; CRO 707, problemas 2 e 3, e correção 3; fichas lidas (turma mínima de 20, passagem e hotel só com a turma fechada) | motivo de perda "turma pode não abrir" ou "pagamento antecipado" entre os leads perdidos; quedas maiores entre A4 e A6 do que entre A2 e A3 | motivo de perda dominado por preço ou concorrente; leads de turmas já confirmadas com a mesma queda | Alta |
| 2 | **Caminho único de compra.** Só COMPRAR no texto copiado, para tickets altos; sem "falar com o time", sem formulário. | A2 para A3 e A3 para A4 | CRO páginas 707, 68610 e 68639 (problemas 1 e 2); síntese, item 1; o template exige a seção formulario e as páginas não a têm | muitos visitantes na página e poucos cliques; leads vindos de WhatsApp fora da página; queda grande de A2 para A3 | A2 para A3 em linha com as turmas que já têm WhatsApp na página | Alta |
| 3 | **Regra da 1ª mensalidade inviável perto do início.** 707 começa em 4 dias (prazo já vencido) e 68610 passa do prazo em 29/10. | A4 para A6 nas turmas com início próximo | CRO 707 (problema 3) e 68610 (problema 5) | perda de leads concentrada nos últimos 30 dias antes do início; perguntas repetidas ao time sobre "posso entrar agora" | leads convertendo igual dentro e fora da janela de 30 dias | Alta nas turmas da onda 1 |
| 4 | **Prova de bolsa pouco ligada à turma e regras contraditórias.** A página não diz a turma de destino nem o valor da mensalidade com bolsa; mínimo 15 contra 20; resultado e prazo descritos de formas diferentes. | B1 para B2, B4 para B6 | CRO 68639 (problemas 1, 2 e 5); insights H-PB5, H-PB7 e H-PB8; contexto da linha | muitas visitas à prova e poucas inscrições; muitos aprovados e poucas matrículas; perguntas sobre "para qual turma vale" | inscrição e matrícula altas mesmo nas provas sem destino claro | Alta (campanha única de 27/11, 32 dias) |
| 5 | **Atendimento: demora na primeira resposta e instabilidade do WhatsApp.** O WhatsApp de vendas é o canal principal; o site informou instabilidade em 22/10/2026. | A4 para A5 e A4 para A7 | ufape-geral.md (canais e ferramentas); cmo, seção 5 (WhatsApp como canal principal). Não há dado de tempo de resposta | conversão de lead para matrícula menor nas faixas de resposta mais lenta; conversas sem resposta no Chatwoot | tempo de resposta curto e estável com a mesma queda | Média, sobe para alta se a mediana for longa |
| 6 | **Turma mínima enterrada no fim da página.** O candidato descobre o risco de a turma não fechar tarde, depois de ler 24 módulos. | A2 para A3 e depois A4 para A6 | CRO 707 (problema 2); insights H-T1; rolagem até CONSIDERAÇÕES [CONFIRMAR] | profundidade de rolagem baixa até CONSIDERAÇÕES e perguntas sobre turma no WhatsApp | candidatos que leram CONSIDERAÇÕES e mesmo assim saem | Média |
| 7 | **Prática real e rotina de viagem não explicadas.** Quantos módulos exigem viagem, onde é a prática, quantos alunos por mesa ficam invisíveis. | A2 para A3 | CRO 707 e 68610 (problema 6); insights H-A4.2, H-A9.1 e H-A14.3 | perguntas sobre viagem e prática no WhatsApp; motivo de perda "deslocamento" | motivo de perda irrelevante nesse tema | Média |
| 8 | **Preço total alto e parcela no cartão.** Objeção 1 da linha. A bolsa deveria ser a resposta natural, mas está mal ligada à turma. | A5 para A6 e A3 para A4 | contexto/pos-graduacao.md (objeção 1, [SUPOSIÇÃO]); insights H-T10, H-A1.4 e H-A10.3 | motivo de perda "preço total" ou "limite do cartão"; queda maior nas turmas de maior ticket | queda igual em turmas de ticket baixo e alto | Média |
| 9 | **Divergência e erro de página reduzem a confiança.** Datas diferentes (698 em 2027 no site e 2026 na planilha), "??" no texto (68610), frase de certificação ligada ao MEC, cronograma com erros. | A2 para A3 | CRO 707 (problemas 6 e 9) e 68610 (problema 7); insights, seção 6 | queda maior nas turmas com divergência (698, 68610) do que nas sem | sem diferença entre turmas com e sem divergência | Média a baixa |
| 10 | **Qualidade do tráfego.** Seis campanhas ativas em turma já iniciada e 73,2% das campanhas com status só em estático (analista, perguntas 1 e 4) podem trazer visita que não é candidato. | A1 para A2 e A2 para A3 | analista-de-dados, perguntas 1 e 4; visão de campanhas | muitos cliques e queda forte logo na página; formato ou público com taxa de A2 para A3 diferente entre si | cliques de campanhas diferentes com o mesmo comportamento na página | Baixa a média |

Leitura: as hipóteses 1, 3 e 6 giram em torno de uma mesma ordem de eventos (pagar, depois saber se a turma abre). Se o motivo de perda confirmar uma delas, a correção é de regra da Ufape e de texto, não de anúncio. As hipóteses 2, 7 e 9 estão na página. As hipóteses 4 e 5 estão fora da página (prova e atendimento).

---

## 3. Instrumentação mínima (por turma e por semana)

Este bloco liga ao pedido de dados do analista-de-dados (saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md, seção 4). Não cria pedido novo: aponta o que deste funil cada linha do pedido destrava.

### 3.1 Regras que valem para tudo

1. **Chave de ligação:** o código do catálogo da turma vai em todo lugar (nome da campanha ou utm_campaign, parâmetro de evento do GA4, campo do lead no CRM, produto da loja). Sem ele o dado não se liga à turma.
2. **Corte de tempo:** uma linha por código e por semana (segunda a domingo), mais a coluna "dias até o início" no fim da semana. Essa coluna é o que permite comparar períodos equivalentes (seção 5).
3. **Janela:** a partir de 01/08/2026 (proposta do analista, [SUPOSIÇÃO]).
4. **Sem dado pessoal:** só contagens e somas, em CSV ou planilha.

### 3.2 Eventos (nomes propostos)

| Evento | Quando dispara | Parâmetros mínimos | Etapa |
|---|---|---|---|
| visualizacao_pagina_turma | página da turma carregada | codigo_turma, tipo_produto (pos), origem | A2 |
| clique_comprar | clique em COMPRAR | codigo_turma, posicao_na_pagina | A3 |
| clique_whatsapp | clique no botão de WhatsApp, quando existir | codigo_turma, posicao_na_pagina | A3 |
| clique_prova_bolsa | clique no link da prova a partir de uma turma | codigo_turma, codigo_prova | A3, B1b |
| rolagem_secao | rolagem até CRONOGRAMA, CONSIDERAÇÕES e o botão | codigo_turma, secao | hipóteses 6 e 7 |
| inicio_checkout | checkout aberto | codigo_turma | A5 |
| compra_concluida | pagamento aprovado | codigo_turma, tipo_pagamento (matricula, mensalidade, inscricao_prova), forma_pagamento | A6, B2 |
| visualizacao_pagina_prova | página da prova carregada | codigo_prova, especialidade, praca | B1 |
| conversa_iniciada | primeira mensagem do candidato no Chatwoot | codigo_turma (ou "sem_codigo"), canal | A4 |
| primeira_resposta | primeira mensagem do time | carimbo de tempo (para a mediana) | A4b |

Nada disso é marcação de pessoa. Os carimbos de tempo viram só a mediana por semana na saída para a squad.

### 3.3 UTM

Padrão proposto [SUPOSIÇÃO; conferir com o padrão de UTM da squad, que não foi aberto nesta etapa]:

| Parâmetro | Valor | Exemplo |
|---|---|---|
| utm_source | plataforma | meta, google, instagram, whatsapp, email |
| utm_medium | tipo de mídia | cpc, organico, disparo, bio |
| utm_campaign | código do catálogo e tipo | 707_pos, 68610_pos, prova_bolsa_20261127 |
| utm_content | formato e ângulo | estatico_a1, video_a3 |
| utm_term | termo (busca paga) | palavra-chave somada, sem dado pessoal |

Para a campanha única das provas de bolsa, o código da prova (68639, 68646 e os outros) vai em utm_content, para a variação por especialidade ser lida sem criar uma campanha por prova.

### 3.4 Campos no CRM

| Campo | Para quê |
|---|---|
| codigo_turma | ligar lead, inscrição e matrícula à turma |
| utm_source, utm_medium, utm_campaign, utm_content | custo por lead e por matrícula por origem |
| origem_do_contato | formulário, WhatsApp pela página, WhatsApp direto, prova de bolsa, indicação |
| etapa_do_funil e data de entrada em cada etapa | calcular conversão e tempo entre etapas |
| motivo_de_perda (lista fechada, ver abaixo) | explicar a queda depois do contato |
| primeira_resposta_em | tempo de primeira resposta |
| trilha | compra direta ou prova de bolsa (e, se as duas, qual veio primeiro) |
| prova: inscrito, presente, aprovado, faixa de bolsa, matriculado | trilha B |
| situacao_turma e data da mudança | A8 e B8 |
| meta_de_matriculas e turma_minima da turma | saber quanto falta |

Lista fechada de motivo de perda [SUPOSIÇÃO; a Ufape ajusta as categorias antes de usar]: preço total, parcela ou limite do cartão, turma pode não abrir, pagamento antecipado ou regra da 1ª mensalidade, data ou tempo, deslocamento, escolheu outra instituição, sem resposta do candidato, sem resposta do time, não passou na prova de bolsa, bolsa insuficiente, outro. O texto livre da conversa não sai do CRM.

### 3.5 Ligação com o pedido de dados do analista

| Seção do pedido | O que este funil usa dela |
|---|---|
| 4.1 Meta Ads e 4.2 Google Ads | cliques e leads por turma e semana (A1), formato e ângulo (hipótese 10) |
| 4.3 CRM | leads, inscritos, matriculados, cancelamentos, situação da turma, etapa e motivo de perda, tempo da primeira resposta, provas de bolsa (trilhas A e B) |
| 4.4 Planilha de datas | código em cada linha e data única de início (sem isso "dias até o início" não é confiável) |
| 4.5 Loja | pedidos pagos, carrinhos abandonados e UTM do pedido (A5, A6, B2) |
| Complementar: GA4 e Chatwoot | visitas por página e conversão do formulário (A2, A3); conversas e tempo de resposta (A4) |

### 3.6 Se só der para fazer cinco coisas primeiro

1. Código da turma em todo nome de campanha e UTM.
2. Eventos clique_comprar, clique_whatsapp e clique_prova_bolsa nas páginas das turmas da onda 1.
3. Definições de lead, inscrito e matriculado e o campo codigo_turma no CRM.
4. Motivo de perda em lista fechada e tempo da primeira resposta.
5. Trilha B: inscritos, presentes, aprovados e matriculados por prova, antes de 27/11/2026.

---

## 4. As 5 perguntas que os números precisam responder primeiro

| # | Pergunta | Números que respondem | Decisão que ela abre |
|---|---|---|---|
| 1 | Por turma, a maior queda está antes do contato (da visita à intenção, A2 para A3 ou A3 para A4) ou depois dele (do lead ao pagamento, A4 para A7)? | A2, A3, A4, A5, A6, A7 por turma e semana | escolher o cenário A (página) ou B (depois do contato) da seção 6 |
| 2 | Quantos matriculados cada turma da onda 1 tem hoje, quantos faltam para o mínimo e em quantos dias de campanha? (707, 68604, 68606, 698, 68610, 68608 e as turmas de março de 2027) | A7 e A8 por turma, meta e dias de campanha ativa | onde concentrar esforço e verba; quais turmas estão em risco de não abrir |
| 3 | Qual é a mediana do tempo da primeira resposta no WhatsApp e como a taxa de lead para matrícula muda por faixa de tempo? | A4b e A7 por faixa de tempo | decidir se o gargalo é de atendimento antes de mexer em página |
| 4 | Entre quem falou com o time e não pagou, quais motivos de perda dominam, por turma e por faixa de dias até o início? | motivo_de_perda somado por turma | qual correção vem primeiro: regra de pagamento e turma (hipóteses 1, 3 e 6), preço (8) ou prática e viagem (7) |
| 5 | Na prova de bolsa, qual é a passagem de inscritos para presentes, aprovados, matriculados e 1ª mensalidade, e que parte das matrículas da turma vem da prova e que parte da compra direta? | B2 a B7 por prova e A7 por turma | decidir se o bloco "o que esta bolsa vale" e a turma de destino são a correção de maior ganho, e se a prova canibaliza a compra direta |

Ordem de leitura: a pergunta 1 decide o cenário; a 2 decide o que é urgente; as 3 e 4 explicam a queda depois do contato; a 5 fecha o ramo da prova de bolsa.

---

## 5. Como comparar (períodos equivalentes)

Nunca meses soltos. Regras:

1. **Turma contra turma pela distância da data de início.** Comparar a mesma etapa nos mesmos dias até o início: a turma de março de 2027 a 150, 120, 90, 60, 30 e 7 dias do início contra a mesma especialidade no ano anterior, ou contra outra turma de ticket parecido, nos mesmos dias. É para isso que a coluna "dias até o início" existe.
2. **Prova contra prova.** A prova de 27/11/2026 contra a prova anterior mais próxima da mesma especialidade [CONFIRMAR se existe registro de inscritos, presentes e matrículas das provas antigas; há 13 provas antigas sem venda no catálogo].
3. **Sem benchmark externo.** Se não houver histórico equivalente, a comparação é entre turmas da mesma linha, de ticket e distância de início parecidos, dentro da Ufape. Nenhum número de mercado entra.
4. **Mesma definição.** Lead, inscrito e matriculado com a régua única do CRM.
5. **Datas divergentes.** Turmas cuja data difere entre catálogo e visão (analista, seção 6.4) ficam fora da comparação até haver uma data só.

---

## 6. Dois cenários de leitura (quando os números chegarem)

Nenhuma taxa de corte é proposta. "Queda" quer dizer que a etapa converte menos do que a mesma etapa em período equivalente (seção 5) ou do que turmas comparáveis. O limite que dispara ação é decisão da pessoa do marketing [CONFIRMAR]. Antes de qualquer cenário, conferir duas coisas: (a) se o evento da etapa dispara em todas as páginas (um evento quebrado parece queda) e (b) se a queda aparece só em turmas com divergência de data, de preço ou de link (analista, seção 6).

### Cenário A: a queda está na página (da visita à intenção e ao contato)

**Sinal:** muitos visitantes únicos e poucos cliques em COMPRAR, WhatsApp e prova de bolsa (A2 para A3 abaixo do comparável), ou poucos leads por clique (A3 para A4).

**Checagens antes de agir:**
1. A origem do tráfego: a queda é igual em todas as campanhas ou só em formatos, ângulos ou públicos específicos (hipótese 10)?
2. A queda é igual no celular e no computador? [SUPOSIÇÃO: a maior parte vem do celular, confirmar no GA4]
3. A queda está nas turmas com página mais fraca (sem prática explicada, com divergência de data)?

**O que fazer (pedidos de aprovação humana, nada é publicado pela squad):**

| Ação | Quem faz | Efeito esperado | Como medir | Como desfazer |
|---|---|---|---|---|
| Caminho secundário "falar com o time" ao lado do COMPRAR | SITE e SQUAD (texto do analise-cro) | mais conversas por visitante | A2 para A3 e A3 para A4 antes e depois | remover o botão |
| Resposta às objeções antes do cronograma (turma mínima, viagem, prática) | SQUAD escreve, SITE publica | menos saída antes do botão | rolagem até o botão e clique em COMPRAR | voltar à ordem anterior |
| Bloco da prova de bolsa ligado à turma de destino | SITE e UFAPE | mais inscrições na prova | B1 para B2 | voltar ao link atual |
| Troca de formato ou ângulo do anúncio, se a queda for de tráfego | gestor-de-midia, com aprovação | visita mais qualificada | A1 para A2 e A2 para A3 por formato | reativar a versão anterior |

**Próximo agente:** desenho-de-experimentos, para transformar cada ação em teste ou em antes e depois, com a amostra possível. Em turma com início em poucos dias (707, 68604) não há tempo de teste: a correção vale como aprovação direta e a leitura é antes e depois.

### Cenário B: a queda está depois do contato (do lead ao pagamento e à matrícula)

**Sinal:** a página entrega visitantes e leads, mas a passagem de lead para checkout, pagamento ou matrícula (A4 para A5, A5 para A6, A4 para A7, B4 para B6) é menor que a comparável.

**Checagens antes de agir:**
1. Tempo da primeira resposta e conversas sem resposta (pergunta 3).
2. Motivo de perda dominante (pergunta 4).
3. A queda concentra-se nos últimos 30 dias antes do início (hipótese 3) ou aparece desde o começo da campanha?
4. Na trilha B: a perda está entre aprovação e matrícula (hipótese 4)?

**O que fazer (pedidos de aprovação humana):**

| Se o dado mostrar | Ação | Quem decide e quem faz | Como medir |
|---|---|---|---|
| resposta lenta ou conversas sem resposta | ajustar escala, roteiro e horário do time; mensagem automática de recebimento | Ufape (atendimento); copy-de-mensagens escreve o texto | tempo da primeira resposta e A4 para A7 |
| motivo "turma pode não abrir" ou "pagamento antecipado" | definir e comunicar quando a turma é confirmada e o que vale para a 1ª mensalidade; texto claro para o time e para a página | Ufape (regra); SQUAD (texto) | queda por motivo e A5 para A6 |
| motivo "regra da 1ª mensalidade" perto do início | regra de entrada para quem decide tarde e data-limite de matrícula | Ufape | A4 para A7 nos últimos 30 dias |
| motivo "preço total" ou "limite do cartão" | levar a prova de bolsa como alternativa no atendimento; deixar parcela, total e matrícula claros | Ufape e estrategia-de-oferta | A4 para A7 e inscrições na prova |
| perda entre aprovação e matrícula na prova | definir turma de destino, regra de quem passa sem bolsa e mensagem de resultado com prazo | Ufape; copy-de-mensagens | B4 para B6 |
| motivo "deslocamento" ou "prática" | resumo de módulos presenciais e de prática no atendimento e na página | SQUAD e Ufape | perguntas repetidas e A4 para A7 |

**Próximo agente:** desenho-de-experimentos para as mudanças de mensagem e de ordem de contato, e copy-de-mensagens para o roteiro do WhatsApp. Toda mensagem em massa só sai com aprovação humana e opt-in.

### Se a queda aparecer nos dois lugares

Tratar primeiro o que estiver mais perto do pagamento: um lead perdido por regra de pagamento custa mais que um visitante perdido na página (avaliação do agente, [SUPOSIÇÃO]). A decisão de ordem fica com a pessoa do marketing, apoiada pelo backlog-de-otimizacao (matriz GUT, etapa 1.33).

---

## 7. Próximo agente sugerido

desenho-de-experimentos, depois que a Ufape enviar o pedido de dados (analista, seção 4) e a instrumentação da seção 3 estiver no ar para a onda 1. Antes dos números, o agente pode desenhar só o plano de medição das correções do analise-cro (antes e depois para 707 e 68604; teste só nas turmas de março de 2027). Depois: backlog-de-otimizacao (1.33) e qa-de-marketing.

---

## Fatos (com fonte)

- Não existe número de funil hoje (briefing do pedido; analista-de-dados, seção 0).
- A turma mínima da Pós é 20 nas páginas das turmas e 15 na página da prova de bolsa (contexto/pos-graduacao.md).
- A prova de bolsa tem inscrição de R$ 100,00, prova presencial em 27/11/2026, nota de corte 7,0, 11 bolsas por prova (2 de 50%, 4 de 25% e 5 de 10%), 2 dias úteis de recurso e 10 dias úteis para matrícula (contexto/pos-graduacao.md).
- A matrícula é de R$ 250,00 e a 1ª mensalidade é paga, na maioria das páginas, 30 dias antes do início (contexto/pos-graduacao.md).
- As páginas 707, 68610 e 68639 têm COMPRAR como único caminho de ação no texto copiado (analise-cro-pos, síntese, item 1).
- 707 começa em 30/10/2026 (4 dias); 68610 em 28/11/2026 (33 dias); as provas são em 27/11/2026 (32 dias) (analise-cro-pos).
- A prova de Dermatologia (68646) é um dia antes do início da turma 68610 (analise-cro-pos, página 2).
- A página de 68610 traz o link "Tem interesse em prestar a prova de bolsa? Clique aqui" sem data, valor nem turma (analise-cro-pos).
- A visão de campanhas tem 19 ativas, 22 pausadas e 26 sem campanha; 6 ativas estão em turmas já iniciadas; 73,2% das campanhas com status são só estáticas (analista-de-dados, perguntas 1 e 4).
- O site informou instabilidade no WhatsApp interno em 22/10/2026 (contexto/ufape-geral.md).
- Ferramentas de CRM, GA4 e atendimento não estão informadas (contexto/ufape-geral.md, seção Ferramentas).
- Para Felinos, Endoscopia, Nefrologia e Odontologia não há turma futura aberta da mesma área no catálogo (cmo, seção 2.3).

## Suposições

- [SUPOSIÇÃO] O candidato de pós conversa com o time antes de pagar, e por isso o caminho único prejudica (hipótese do analise-cro, não validada).
- [SUPOSIÇÃO] A maior parte dos candidatos chega pelo celular.
- [SUPOSIÇÃO] As definições provisórias de lead, inscrito, matriculado e turma confirmada da seção 1.3.
- [SUPOSIÇÃO] Os nomes de evento, o padrão de UTM e a lista de motivos de perda são propostas, a validar com a Ufape e com o padrão de UTM da squad.
- [SUPOSIÇÃO] A janela de dados a partir de 01/08/2026 (proposta do analista).
- [SUPOSIÇÃO] A ordem de prioridade das hipóteses e a regra de tratar primeiro a etapa mais próxima do pagamento são avaliação do agente.
- [SUPOSIÇÃO] O candidato pode usar a trilha A e a trilha B ao mesmo tempo, e a compra direta pode vir sem lead no CRM (compra pela loja sem conversa).

## Dados que faltam

- [CONFIRMAR] Todos os contadores das etapas A1 a A9 e B1 a B8, por turma e por semana (Meta Ads, Google Ads, GA4, loja, CRM, Chatwoot).
- [CONFIRMAR] O que o botão COMPRAR cobra (matrícula, 1ª mensalidade ou os dois).
- [CONFIRMAR] Quando a turma é confirmada e quem decide; qual mínimo vale (15 ou 20).
- [CONFIRMAR] Definições do CRM de lead, inscrito, matriculado e cancelamento.
- [CONFIRMAR] Ferramenta de CRM, GA4 e atendimento; se as páginas têm tag e eventos de clique; se existe botão de WhatsApp e formulário nas páginas.
- [CONFIRMAR] Tempo da primeira resposta e horário de atendimento do time.
- [CONFIRMAR] Turma de destino de cada prova, regra de distribuição das bolsas, data do resultado e regra para quem passa sem bolsa.
- [CONFIRMAR] Regra da 1ª mensalidade para quem entra com o início próximo e data-limite de matrícula.
- [CONFIRMAR] Histórico de provas e turmas equivalentes (inscritos, presentes, matrículas) para comparar períodos.
- [CONFIRMAR] Código do catálogo no nome das campanhas e uma data única de início para os itens com datas divergentes.
- [CONFIRMAR] Quem aprova metas, páginas e preços, mensagens em massa e verba (ufape-geral.md, tabela vazia).
