# Análise de funil: Cursos Livres (funil desenhado, sem números)

- **Agente:** analise-de-funil (departamento 08 Conversão), etapa 1.31 da camada 1
- **Linha:** livres
- **Data:** 26/10/2026
- **Status:** rascunho para o qa-de-marketing e para a aprovação da pessoa do marketing. Nada foi publicado, enviado ou pago.
- **Natureza desta entrega:** não existe nenhum número de funil (visitas, leads, pedidos, vendas) [CONFIRMAR]. Este arquivo desenha o funil como ele existe hoje, nomeia cada etapa e o evento que a mede, lista hipóteses de queda, propõe a instrumentação mínima e define as perguntas que os números precisam responder primeiro. Nenhuma taxa de conversão foi escrita nem estimada.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/cursos-livres.md
  - contexto/pos-graduacao.md (para a venda cruzada e a fronteira entre as linhas)
  - saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (seções 0, 4 e 5)
  - saidas/08-conversao/analise-cro-livres-2026-10-26.md
  - saidas/08-conversao/analise-cro-pos-2026-10-26.md (só a síntese, para comparar)
  - saidas/01-inteligencia-de-mercado/insights-de-alunos-pos-2026-10-26.md (seções transversais)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1, 3 e 7)
- **Não reaberto nesta etapa:** contexto/catalogo-de-cursos.md e as fichas. Os dados de curso citados (código, data, preço, forma de pagamento) vêm das saídas acima, que já os conferiram com o catálogo. Todo dado de curso fora delas aparece como [CONFIRMAR NO CATÁLOGO]. Não foi aberto faculdade.ufape.com.br.
- **Fora desta entrega:** o workshop de Neuromonitorização (20 e 21/11/2026) é da linha Eventos. O analise-cro o incluiu no arquivo de Livres só por pedido da etapa. O funil dele pertence ao arquivo de eventos e usa as mesmas etapas L1 a L7 abaixo, com cupom (SIMPNEUROMONIT) e ingresso presencial ou transmitido.
- **Dado pessoal:** nenhum. Tudo que o funil pede é contagem somada por produto e semana.

---

## 0. Limites desta análise

1. Não há número de GA4, loja, CRM, Chatwoot, Meta Ads nem Google Ads. Tudo que depende de número é [CONFIRMAR].
2. As ferramentas de CRM, GA4 e atendimento não estão informadas (ufape-geral.md, seção Ferramentas). Os nomes de evento são proposta [CONFIRMAR ferramenta].
3. A linha tem seis formatos com ciclos de venda diferentes (contexto/cursos-livres.md). Um funil só, com variações por formato, evita seis desenhos, mas a leitura dos números tem de ser separada por formato. Somar presencial, online e grupo numa conversão única esconderia o problema.
4. Em Livres a compra costuma ser direta na loja, sem passar por vendedor. É [SUPOSIÇÃO]: se for verdade, o CRM não tem lead dessas compras e a conta de funil depende da loja e do GA4 [CONFIRMAR].
5. Os sinais de atrito vêm de leitura de página e de contexto (E), não de comportamento medido. A ordem de prioridade é avaliação do agente e muda quando chegarem os números.

---

## 1. Funil por etapa

### 1.1 Desenho único com variação por formato

```
L1 anúncio ou busca (clique)
  > L2 visita à página do produto
    > L3 intenção: clique em COMPRAR ou no WhatsApp de vendas (se existir)
      > L4 checkout iniciado
        > L5 forma de pagamento escolhida (Pix, boleto, cartão, boleto parcelado)
          > L6 pedido pago
            > L7 entrega: vaga confirmada e comparecimento (presencial), primeiro acesso (online e minicurso), entrada no grupo (grupo de estudos)
              > L8 depois da compra: venda cruzada (curso online para presencial, grupo para pós) [SUPOSIÇÃO]
```

Dois desvios do caminho principal precisam de evento próprio, porque são onde o dado costuma se perder:

- **Boleto parcelado pedido por e-mail à secretaria** (573, CRO página 1): é o único passo manual do funil. A pessoa sai do checkout, pede o boleto e a compra pode nunca voltar ao site. Sem registro, aparece como abandono de L5.
- **"Avise-me"** (turma sem venda): demanda por turma sem produto à venda. Não é etapa do funil, é sinal de demanda (analista, seção 4.5).

| Etapa | Nome | O que conta | Evento ou medida | Fonte | Existe hoje? |
|---|---|---|---|---|---|
| L1 | Clique no anúncio ou na busca | cliques com UTM e código do produto, por semana | clique no anúncio (plataforma) | Meta Ads, Google Ads | Existe nas plataformas; o código no nome da campanha ou no utm_campaign [CONFIRMAR] |
| L2 | Visita à página do produto | visitantes únicos, por origem | visualizacao_pagina_produto (codigo_produto, formato) | GA4 | [CONFIRMAR ferramenta e tag] |
| L3 | Intenção | cliques em COMPRAR e no WhatsApp | clique_comprar, clique_whatsapp | GA4 | COMPRAR existe (E, CRO); WhatsApp na página não aparece no texto copiado; eventos [CONFIRMAR] |
| L3b | Contato com vendas | conversas novas por produto e tempo da primeira resposta | conversa_iniciada, primeira_resposta | Chatwoot | [CONFIRMAR] |
| L4 | Checkout iniciado | visitantes que abriram o checkout | inicio_checkout | loja, GA4 | [CONFIRMAR] |
| L5 | Forma de pagamento | contagem por forma (Pix, boleto, cartão, boleto parcelado) e carrinhos abandonados | forma_pagamento_escolhida, carrinho_abandonado | loja | [CONFIRMAR]; abandono total da loja está no pedido do analista (seção 4.5) |
| L5b | Boleto parcelado pedido por e-mail | pedidos manuais à secretaria, por semana | contagem manual ou etiqueta no atendimento | secretaria | não existe registro [CONFIRMAR] |
| L6 | Pedido pago | pedidos pagos por produto e semana, com cupom e UTM | compra_concluida (codigo_produto, forma_pagamento, cupom) | loja | [CONFIRMAR] |
| L7 | Entrega | presencial: vagas preenchidas e comparecimento; online: primeiro acesso e conclusão; grupo: entrada e presença | vaga_confirmada, comparecimento, primeiro_acesso | loja, plataforma de aulas, CRM | [CONFIRMAR]; vagas e turma mínima não constam nas páginas dos presenciais (CRO, página 1) |
| L8 | Venda cruzada | compradores de Livres que viram lead de Pós, somados | lead_pos_vindo_de_livres | CRM | [CONFIRMAR]; ligação a validar (analista, árvore 5.2) |

Conversão entre etapas (a calcular quando houver números):

| De | Para | Conta | Valor |
|---|---|---|---|
| L1 | L2 | visitas ÷ cliques | [CONFIRMAR] |
| L2 | L3 | visitantes que clicaram ÷ visitantes únicos | [CONFIRMAR] |
| L3 | L4 | checkouts ÷ cliques em COMPRAR | [CONFIRMAR] |
| L4 | L5 | checkouts que chegaram à forma de pagamento ÷ checkouts | [CONFIRMAR] |
| L5 | L6 | pedidos pagos ÷ formas escolhidas, separado por forma | [CONFIRMAR] |
| L2 | L6 | pedidos pagos ÷ visitantes únicos (conversão do produto) | [CONFIRMAR] |
| L6 | L7 | presentes ou primeiros acessos ÷ pedidos pagos | [CONFIRMAR] |

### 1.2 Variações por formato

| Formato | Produtos de referência (CRO) | O que muda no funil | Leitura própria |
|---|---|---|---|
| Presencial, 1 a 3 dias | 573 (início 14/11/2026 no catálogo; 29/11 na visão de campanhas), 623, 68614, 68637 | L7 depende de vaga e de turma confirmada; L5 inclui boleto parcelado por e-mail; o candidato viaja | vagas preenchidas por semana nas 4 a 8 semanas antes da data [SUPOSIÇÃO do contexto]; curva por dias até a data |
| Online gravado | 411 (o 616 é presencial e online, com início em 05/12/2026 no catálogo, e conta como item com data) | 411: sem data nem vaga; L7 é o primeiro acesso; prazo de acesso (120 dias) | conversão da página e do checkout; venda contínua por semana |
| Minicurso online de 8 h | 13 minicursos contínuos (recorte) | porta de entrada, ticket baixo; L8 mais importante | conversão e venda cruzada |
| Grupo de estudos | 68665 (01/11/2026), 68666 (25/11/2026), 713 (anual) | L7 é a entrada no grupo e a presença; entrada tardia pesa em 713 (17 de 23 aulas já dadas em 26/10/2026, conta do CRO) | conversão por data de entrada no ciclo |
| Espanhol | 347, 501 | revisão por falante nativo antes de medir [CONFIRMAR] | fora da primeira leitura |

---

## 2. Hipóteses de queda, por prioridade

Critério de ordem (avaliação do agente, [SUPOSIÇÃO]): quanto a evidência já lida aponta para a hipótese, quanto ela afeta mais de um produto, e quanto o número que vai chegar consegue confirmar ou descartar. Todas são hipótese até haver número. As evidências (E) vêm dos arquivos lidos.

| # | Hipótese | Etapa onde a queda apareceria | Evidência (E) | Que dado confirma | Que dado descarta | Prioridade |
|---|---|---|---|---|---|---|
| 1 | **Pagamento confuso e passo manual.** No 573 o topo, o bloco INVESTIMENTO e o boleto parcelado dizem coisas diferentes; o boleto parcelado exige pedir por e-mail à secretaria; "carta de crédito" aparece no lugar de cartão; o e-mail citado difere do canal oficial. | L4 para L5 e L5 para L6 | CRO Livres, página 1, problema 1; síntese, itens 2 e 3 | carrinhos abandonados na etapa de pagamento; pedidos de boleto por e-mail que não viram pedido pago; queda maior em L5 para L6 no boleto | queda de L5 para L6 igual em todas as formas de pagamento | Alta |
| 2 | **Pagar antes de saber se a turma abre, sem vagas, turma mínima nem regra de adiamento.** As pós têm o aviso, o 573 não. Quem viaja teme perder passagem. | L3 para L4, L4 para L6 e L6 para L7 | CRO Livres, página 1, problema 2; síntese, item 6; insights H-T1 e H-T3 (por analogia com a Pós) | perguntas "tem vaga" e "e se não fechar" no atendimento; queda em presencial maior que em online do mesmo ticket | presencial com a mesma conversão que online | Alta nos presenciais |
| 3 | **Anúncio e página com datas diferentes.** 573: 14/11 no catálogo e 29/11 na visão; 68614: 28/11 e 18/12; 68618: 18/12/2026 e 22/05/2027. | L2 para L3 (quebra de expectativa) | CRO Livres, página 1, problema 10; plano do cmo, P6; analista, seção 6.4 | queda maior nos produtos com data divergente; cliques de anúncios que citam outra data | sem diferença entre produtos com e sem divergência | Alta nos produtos da onda 1 |
| 4 | **Caminho único de compra.** Só COMPRAR, sem "falar com o time", em ticket médio e alto (573). Em ticket baixo (411, grupos) o botão direto deve bastar. | L2 para L3 e L3 para L4 | CRO Livres, síntese, item 1 | poucos cliques e leads de WhatsApp vindos de fora da página nos presenciais; sem efeito nos online de ticket baixo | cliques altos no 573 apesar do caminho único | Média, só em presencial de ticket maior [SUPOSIÇÃO] |
| 5 | **Total do cartão não mostrado.** Cartão 10x no 573 soma bem mais que o à vista; 411 e 713 idem. O visitante descobre a diferença no checkout. | L4 para L5 e L5 para L6 | CRO Livres, síntese, item 2; analista, seção 0 (parcelado costuma ser mais caro que o à vista, contexto) | abandono no cartão maior que no Pix; forma de pagamento escolhida pelo parcelamento e desistência na etapa seguinte | sem diferença de abandono entre formas | Média |
| 6 | **Sem "sobre", sem "para quem" e sem prova.** 411 vai do preço direto para a lista de tópicos; 713 tem frase de abertura incompleta e não diz o que é grupo de estudo; sem aula de amostra nem depoimento. | L2 para L3 | CRO Livres, páginas 2 e 3 (problemas 1, 3 e 5); objeção 1 da linha ("vale pagar se há conteúdo gratuito?") | queda forte na página de online e minicurso, com tráfego bom; rolagem baixa | boa conversão de L2 para L3 mesmo sem esses blocos | Média a alta em online e grupos |
| 7 | **Entrada tardia em produto contínuo ou anual.** 713 cobra o valor integral com 17 das 23 aulas já realizadas; 411 não diz quando começam os 120 dias de acesso. | L3 para L4 em grupo anual; L6 para L7 e reclamações depois | CRO Livres, página 2 (problema 2) e página 3 (problema 2) | queda em 713 depois de março; pedidos de cancelamento nas primeiras semanas | conversão estável ao longo do ano | Média |
| 8 | **Prática real não explicada.** 573 promete 16 h de prática, mas não diz quantos alunos por aparelho nem se o aluno faz o exame. Objeção 3 da linha. | L2 para L3 | CRO Livres, página 1, problema 5 | perguntas sobre prática no atendimento; queda em presencial | sem pergunta recorrente sobre o tema | Média |
| 9 | **Vazamento no meio da página de venda.** O 411 tem link para a tela de login em outro domínio dentro da página de venda. | L2 para L3 | CRO Livres, página 2, problema 5 | cliques no link de login por visitante de venda; saídas para outro domínio | cliques desprezíveis nesse link | Baixa a média |
| 10 | **Duplicidades.** 623 e 68637 (endoscopia de 28/11), grupos 643 e 713, 642 e 712: o anúncio pode levar à versão errada e o visitante se divide entre duas páginas. | L1 para L2 e L2 para L3 | plano do cmo, P7; CRO Livres, página 3, problema 6 | tráfego e pedidos divididos entre as duas páginas | uma das duas sem visita | Média na onda 1 (623 e 68637) |
| 11 | **Falta de próximo passo.** Nenhuma página leva ao degrau seguinte, então L8 pode ser quase zero por desenho, não por falta de interesse. | L8 | CRO Livres, síntese, item 8 | compradores de Livres que viram lead de Pós, somados, perto de zero | venda cruzada acontece sem link | Baixa para a conversão da própria venda; média para o valor da linha |

Leitura: as hipóteses 1, 2, 3 e 5 estão na compra de presenciais (e, em parte, na de grupos e online). As hipóteses 6, 8 e 9 estão na página. A hipótese 7 é de produto contínuo e anual. A 11 não derruba a venda de Livres, mas limita o valor da linha como porta de entrada para a Pós [SUPOSIÇÃO].

---

## 3. Instrumentação mínima (por produto e por semana)

Este bloco liga ao pedido de dados do analista-de-dados (saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md, seção 4). Não cria pedido novo: aponta o que deste funil cada linha do pedido destrava.

### 3.1 Regras que valem para tudo

1. **Chave de ligação:** o código do catálogo do produto vai no nome da campanha ou no utm_campaign, no parâmetro de evento do GA4 e no produto da loja.
2. **Corte de tempo:** uma linha por código e por semana (segunda a domingo), mais a coluna "dias até a data" nos presenciais. Nos contínuos, "semana do ano" para comparar com a semana equivalente do ano anterior.
3. **Janela:** a partir de 01/08/2026 (proposta do analista, [SUPOSIÇÃO]).
4. **Sem dado pessoal:** só contagens e somas, em CSV ou planilha.
5. **Separar por formato:** presencial, online, minicurso, grupo e espanhol nunca somados numa conversão única.

### 3.2 Eventos (nomes propostos)

| Evento | Quando dispara | Parâmetros mínimos | Etapa |
|---|---|---|---|
| visualizacao_pagina_produto | página do produto carregada | codigo_produto, formato, origem | L2 |
| clique_comprar | clique em COMPRAR | codigo_produto, posicao_na_pagina | L3 |
| clique_whatsapp | clique no botão de WhatsApp, quando existir | codigo_produto | L3 |
| clique_link_saida | clique em link para outro domínio na página de venda (ex.: login do 411) | codigo_produto, destino | hipótese 9 |
| rolagem_secao | rolagem até investimento, sobre, FAQ e botão | codigo_produto, secao | hipóteses 6 e 8 |
| inicio_checkout | checkout aberto | codigo_produto | L4 |
| forma_pagamento_escolhida | forma selecionada | codigo_produto, forma (pix, boleto, cartao, boleto_parcelado) | L5 |
| carrinho_abandonado | checkout sem pagamento depois de um tempo definido [CONFIRMAR] | codigo_produto, ultima_etapa | L5 |
| compra_concluida | pagamento aprovado | codigo_produto, forma, cupom, utm | L6 |
| conversa_iniciada e primeira_resposta | Chatwoot | codigo_produto (ou "sem_codigo") | L3b |
| vaga_confirmada e comparecimento | CRM ou lista de presença | codigo_produto | L7 |

Para o boleto parcelado pedido por e-mail (L5b), enquanto o site não fechar a compra sozinho: a secretaria registra a contagem semanal por produto, sem nome nem e-mail do candidato. É uma medida provisória [SUPOSIÇÃO].

### 3.3 UTM

Padrão proposto [SUPOSIÇÃO; conferir com o padrão de UTM da squad, que não foi aberto nesta etapa]:

| Parâmetro | Valor | Exemplo |
|---|---|---|
| utm_source | plataforma | meta, google, instagram, whatsapp, email |
| utm_medium | tipo de mídia | cpc, organico, disparo, remarketing |
| utm_campaign | código do catálogo e formato | 573_livre_presencial, 411_livre_online |
| utm_content | formato do criativo e ângulo | estatico_a1, video_a3 |
| utm_term | termo (busca paga) | palavra-chave somada |

No anúncio de presencial, a data anunciada vai no utm_content ou no nome da campanha (ex.: d20261114). Assim, quando catálogo e visão divergirem (hipótese 3), dá para ver qual data o clique prometeu.

### 3.4 Campos nos sistemas

| Onde | Campo | Para quê |
|---|---|---|
| Loja | pedidos pagos e receita por código de produto e semana; forma de pagamento; cupom; UTM do pedido; carrinhos abandonados; reembolsos; avise-me | L4 a L6 e hipóteses 1, 2 e 5 |
| Loja ou planilha | vagas totais, vagas restantes e turma mínima por presencial | hipótese 2 e L7 |
| CRM | codigo_produto, utm, origem do contato, motivo de perda (lista fechada abaixo), situação da turma presencial | L3b, L8 |
| CRM | lead de Pós com marca "veio de Livres" (somado, sem dado pessoal) | L8 |
| Planilha de datas | data única de início por produto | evitar o problema da hipótese 3 |

Lista fechada de motivo de perda para quem falou com o time [SUPOSIÇÃO; a Ufape ajusta]: preço, forma de pagamento (boleto ou cartão), sem vaga ou turma incerta, data ou deslocamento, prática não clara, escolheu conteúdo gratuito, escolheu outro curso, sem resposta do candidato, sem resposta do time, outro.

### 3.5 Ligação com o pedido de dados do analista

| Seção do pedido | O que este funil usa dela |
|---|---|
| 4.1 Meta Ads e 4.2 Google Ads | cliques, leads e conversões por produto e semana (L1), formato e ângulo |
| 4.3 CRM | leads, tempo da primeira resposta, etapa e motivo de perda, origem por UTM (L3b, L8) |
| 4.4 Planilha de datas | código em cada linha e data única (hipótese 3); linhas para os Livres que não constam na visão (51 dos 55 do recorte, cobertura de 4 itens segundo o analista) |
| 4.5 Loja | pedidos pagos, receita, cupons, forma de pagamento, reembolsos, UTM do pedido, carrinhos abandonados, avise-me, produtos à venda com turma iniciada (L4 a L6) |
| Complementar: GA4 e Chatwoot | visitas por página de produto e conversão; conversas por produto e tempo da primeira resposta |

### 3.6 Se só der para fazer cinco coisas primeiro

1. Código do produto em todo nome de campanha e UTM, com a data anunciada nos presenciais.
2. Eventos de clique_comprar, inicio_checkout, forma_pagamento_escolhida e compra_concluida nos produtos da onda 1 (573, 623, 68614, 68637, 68665, 68666).
3. Carrinhos abandonados e forma de pagamento por produto, direto da loja.
4. Vagas totais e restantes e turma mínima dos presenciais.
5. Contagem semanal dos boletos parcelados pedidos por e-mail.

---

## 4. As 5 perguntas que os números precisam responder primeiro

| # | Pergunta | Números que respondem | Decisão que ela abre |
|---|---|---|---|
| 1 | Por formato e produto, a maior queda está na página (L2 para L3) ou no checkout e no pagamento (L3 para L6)? | L2, L3, L4, L5, L6 por produto e semana | escolher o cenário A (página) ou B (depois do contato e do clique) da seção 6 |
| 2 | No checkout, quantos abandonam em cada forma de pagamento (Pix, cartão, boleto, boleto parcelado), e quantos pedidos de boleto por e-mail viram pedido pago? | L5, L5b e L6 por forma | priorizar a correção de pagamento (hipóteses 1 e 5) e dizer se o checkout precisa fechar o boleto parcelado sozinho |
| 3 | Nos presenciais, quantos pedidos pagos por semana, a partir de quantos dias antes da data, contra as vagas? (573, 623, 68614, 68637) | L6 e vagas por semana e dias até a data | saber se a venda acontece cedo ou só na reta final; se falta vaga ou falta demanda; se a regra de turma e adiamento pesa (hipótese 2) |
| 4 | Quanto das vendas passa por conversa no WhatsApp e quanto é compra direta, e qual é a mediana do tempo da primeira resposta? | L3b, L6 por origem e tempo da primeira resposta (L3b) | decidir se o atendimento é gargalo em Livres e se o caminho único da página (hipótese 4) importa em ticket médio |
| 5 | Nos contínuos, quais produtos vendem sem anúncio, qual é a conversão por tipo (online, minicurso, grupo) e quantos compradores de Livres viram lead de Pós? | L2 a L6 por produto e tipo; L8 somado | decidir onde o kit sempre ligado (remarketing) e a venda cruzada valem o esforço |

Ordem de leitura: a 1 decide o cenário; a 2 e a 3 explicam os presenciais da onda 1; a 4 mede o atendimento; a 5 organiza os contínuos da onda 2.

---

## 5. Como comparar (períodos equivalentes)

Nunca meses soltos. Regras:

1. **Presenciais:** comparar pela distância até a data. O 573 a 40, 30, 21, 14 e 7 dias da data, contra a edição anterior do mesmo curso nos mesmos dias [CONFIRMAR se existe edição anterior e seu registro], ou contra outro presencial de ticket e duração parecidos. A campanha de 4 a 8 semanas é [SUPOSIÇÃO] do contexto.
2. **Contínuos (online, minicursos, grupos):** a mesma semana do ano anterior, ou as semanas imediatamente anteriores de produtos do mesmo tipo e faixa de preço. Para o grupo anual 713, comparar pelo mês de entrada no ciclo, porque o valor é o mesmo e o conteúdo entregue cai ao longo do ano (hipótese 7).
3. **Mesmo formato.** Presencial com presencial, online com online, grupo com grupo.
4. **Sem benchmark externo.** Se não houver histórico, a comparação é entre produtos da linha Livres. Nenhum número de mercado entra.
5. **Datas divergentes.** 573, 68614 e 68618 (analista, seção 6.4) ficam fora da comparação até haver data única.
6. **Duplicidades.** 623 com 68637 e 643 com 713 são lidos juntos até a Ufape dizer qual página fica à venda.

---

## 6. Dois cenários de leitura (quando os números chegarem)

Nenhuma taxa de corte é proposta. "Queda" quer dizer que a etapa converte menos do que a mesma etapa em período equivalente (seção 5) ou do que produtos comparáveis do mesmo formato. O limite que dispara ação é decisão da pessoa do marketing [CONFIRMAR]. Antes de qualquer cenário, conferir (a) se o evento da etapa dispara em todas as páginas (evento quebrado parece queda) e (b) se a queda aparece só em produtos com data, preço ou link divergentes.

### Cenário A: a queda está na página (visita para intenção)

**Sinal:** muitos visitantes únicos e poucos cliques em COMPRAR ou WhatsApp (L2 para L3 abaixo do comparável).

**Checagens antes de agir:**
1. A origem do tráfego: a queda é igual em todas as campanhas ou só em formatos e públicos específicos?
2. A data ou o preço do anúncio batem com os da página (hipótese 3)?
3. A queda é igual no celular e no computador? [SUPOSIÇÃO: a maior parte vem do celular, confirmar no GA4]
4. A queda está nos produtos sem "sobre" nem prova (411, 713) ou também nos que têm (573)?

**O que fazer (pedidos de aprovação humana, nada é publicado pela squad):**

| Ação | Quem faz | Efeito esperado | Como medir | Como desfazer |
|---|---|---|---|---|
| Alinhar data e preço do anúncio com a página (fixar uma data) | Ufape (data); gestor-de-midia (anúncio, com aprovação) | menos quebra de expectativa | L2 para L3 por produto | voltar ao criativo anterior |
| Hero, "Sobre" e "Para quem" no topo; bloco "Por que pagar se há conteúdo gratuito" | SQUAD escreve (analise-cro), SITE publica | mais cliques por visitante nos online e grupos | L2 para L3 e rolagem | voltar à página atual |
| Bloco "Como é a prática" e dados de vagas no 573 | SQUAD e UFAPE | menos saída por dúvida sobre prática | L2 para L3 no presencial | remover o bloco |
| Remover o link de login do fluxo de compra do 411 | SITE | menos saída da página de venda | clique_link_saida e L2 para L3 | recolocar o link |
| Resolver duplicidades (623 e 68637, 643 e 713) | Ufape | tráfego e vendas numa só página | tráfego por página | reativar a página |

**Próximo agente:** desenho-de-experimentos. Em produtos com data próxima (573, em 19 dias pelo catálogo) não há tempo de teste: a leitura é antes e depois. Nos contínuos (411, minicursos) há tráfego contínuo e dá para testar topo, vídeo de amostra e bloco de acesso, se o tráfego medido sustentar.

### Cenário B: a queda está depois do clique (checkout, pagamento, contato ou entrega)

**Sinal:** a página entrega cliques em COMPRAR (L3), mas a passagem para checkout, forma de pagamento e pedido pago (L3 para L4, L4 para L5, L5 para L6) é menor que a comparável, ou há muitas conversas que não viram pedido.

**Checagens antes de agir:**
1. Em que forma de pagamento a queda se concentra (pergunta 2)? Boleto parcelado por e-mail é suspeito número um.
2. A queda é maior nos presenciais que nos online do mesmo ticket (hipótese 2)?
3. Tempo da primeira resposta e conversas sem resposta (pergunta 4).
4. Motivo de perda dominante entre quem falou com o time.

**O que fazer (pedidos de aprovação humana):**

| Se o dado mostrar | Ação | Quem decide e quem faz | Como medir |
|---|---|---|---|
| abandono concentrado no boleto parcelado ou no cartão | checkout que feche Pix, cartão e boleto parcelado sem e-mail; total de cada opção na página; corrigir "carta de crédito" e o e-mail citado | Ufape e SITE | L5 para L6 por forma e contagem de boletos pedidos por e-mail |
| queda maior em presencial, perguntas sobre vaga e adiamento | publicar vagas, turma mínima e regra de adiamento; mostrar "vagas restantes" só com número real | Ufape (regra e número); SQUAD (texto) | L3 para L6 e perguntas "tem vaga" |
| resposta lenta ou conversas sem resposta | ajustar escala e roteiro do WhatsApp de vendas; mensagem automática de recebimento | Ufape; copy-de-mensagens escreve o texto | tempo da primeira resposta e conversas que viram pedido |
| entrada tardia (713) com queda ou cancelamento | definir o que recebe quem entra com o ciclo em andamento e o preço dessa entrada | Ufape (decisão comercial); SQUAD (texto) | L3 para L6 por mês de entrada e cancelamentos |
| compradores sem comparecimento ou primeiro acesso | lembretes por WhatsApp e e-mail de véspera e de acesso, só com consentimento | CRM envia; copy-de-mensagens escreve | L6 para L7 |
| muitos pedidos sem venda cruzada | link para o degrau seguinte (online para presencial, grupo para pós), se a Ufape aprovar | Ufape e SITE | L8 somado |

**Próximo agente:** desenho-de-experimentos (antes e depois do checkout e do bloco de vagas), copy-de-mensagens (roteiro do WhatsApp e lembretes) e jornada-do-aluno (Livres para Pós). Toda mensagem em massa só sai com aprovação humana e opt-in.

### Se a queda aparecer nos dois lugares

Tratar primeiro o que está mais perto do pagamento (pagamento e vaga), porque é onde o visitante já decidiu e saiu mesmo assim (avaliação do agente, [SUPOSIÇÃO]). A decisão de ordem fica com a pessoa do marketing, apoiada pelo backlog-de-otimizacao (matriz GUT, etapa 1.33).

---

## 7. Próximo agente sugerido

desenho-de-experimentos, depois que a Ufape enviar o pedido de dados (analista, seção 4) e a instrumentação da seção 3 estiver no ar para a onda 1 de Livres. Antes dos números, o agente pode desenhar o plano de medição das correções do analise-cro (antes e depois para o 573 e os grupos 68665 e 68666; teste só nos contínuos com tráfego). Depois: backlog-de-otimizacao (1.33) e qa-de-marketing.

---

## Fatos (com fonte)

- Não existe número de funil hoje (briefing do pedido; analista-de-dados, seção 0).
- A linha Livres tem seis formatos com ciclos diferentes: presencial por data, online e minicurso contínuos, grupos anuais ou por encontro, aprimoramento, espanhol; simpósios e congressos foram para Eventos em 23/10/2026 (contexto/cursos-livres.md).
- O 573 mostra, na página, o pagamento de três formas diferentes, pede o boleto parcelado por e-mail à secretaria e cita um e-mail diferente do canal oficial (analise-cro-livres, página 1, problema 1).
- O 573 não traz vagas, turma mínima nem regra de adiamento (analise-cro-livres, página 1, problema 2).
- O 573 tem início em 14/11/2026 no catálogo e 29/11/2026 na visão de campanhas; 68614 tem 28/11 contra 18/12; 68618 tem 18/12/2026 contra 22/05/2027 (analise-cro-livres; analista-de-dados, seção 6.4).
- O 411 não tem texto de apresentação, mostra o prazo de acesso (120 dias) só no fim e tem link para a tela de login em outro domínio (analise-cro-livres, página 2).
- O 713 tem quatro descrições de período; 17 das 23 aulas já tinham data até 14/10/2026 (conta do CRO sobre a ementa); existe duplicidade com 643 (analise-cro-livres, página 3).
- 623 e 68637 parecem duplicados; 643 e 713, 642 e 712 também (plano do cmo, P7).
- Das 55 entradas de Livres no recorte, só 4 constam na visão de campanhas (analista-de-dados, pergunta 5).
- Nenhuma das quatro páginas analisadas leva ao degrau seguinte da jornada (analise-cro-livres, síntese, item 8).
- O preço mediano da linha é de cerca de R$ 720 (contexto/cursos-livres.md).
- Ferramentas de CRM, GA4 e atendimento não estão informadas (contexto/ufape-geral.md, seção Ferramentas).

## Suposições

- [SUPOSIÇÃO] A compra de Livres é, em grande parte, direta na loja, sem lead no CRM.
- [SUPOSIÇÃO] A campanha dos presenciais dura de 4 a 8 semanas (contexto/cursos-livres.md).
- [SUPOSIÇÃO] Em ticket médio e alto (presencial) o visitante conversa antes de pagar; em ticket baixo o botão direto basta (hipótese do analise-cro).
- [SUPOSIÇÃO] A maior parte dos candidatos chega pelo celular.
- [SUPOSIÇÃO] A venda cruzada entre os degraus (online, presencial, grupo e pós) aumenta o valor da linha; a ligação ainda não foi validada.
- [SUPOSIÇÃO] Os nomes de evento, o padrão de UTM, a lista de motivos de perda e o registro manual de boletos por e-mail são propostas.
- [SUPOSIÇÃO] A janela de dados a partir de 01/08/2026 (proposta do analista).
- [SUPOSIÇÃO] A ordem de prioridade das hipóteses e a regra de tratar primeiro a etapa mais próxima do pagamento são avaliação do agente.

## Dados que faltam

- [CONFIRMAR] Todos os contadores das etapas L1 a L8, por produto e por semana (Meta Ads, Google Ads, GA4, loja, CRM, Chatwoot).
- [CONFIRMAR] Se a compra direta gera lead no CRM e se existe lead de Livres que vira lead de Pós.
- [CONFIRMAR] Vagas totais, vagas restantes, turma mínima e regra de adiamento dos presenciais.
- [CONFIRMAR] Quais formas de pagamento valem de fato no 573 e se o boleto parcelado fecha no site.
- [CONFIRMAR] Data única de início do 573, 68614 e 68618, e qual página fica à venda entre 623 e 68637, e entre 643 e 713.
- [CONFIRMAR] Regras de acesso do 411 (início da contagem dos 120 dias) e o que recebe quem entra tarde no 713.
- [CONFIRMAR] Ferramenta de CRM, GA4 e atendimento; se as páginas têm tag e eventos de clique; se existe botão de WhatsApp nas páginas de Livres.
- [CONFIRMAR] Tempo da primeira resposta e horário de atendimento do time.
- [CONFIRMAR] Histórico de edições anteriores dos presenciais e vendas por semana dos contínuos, para comparar períodos.
- [CONFIRMAR] Código do catálogo no nome das campanhas dos Livres (51 dos 55 itens do recorte não constam na visão de campanhas).
- [CONFIRMAR] Quem aprova metas, páginas e preços, mensagens em massa e verba (ufape-geral.md, tabela vazia).
