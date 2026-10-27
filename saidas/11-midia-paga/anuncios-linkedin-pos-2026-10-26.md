# Estrutura de LinkedIn Ads: teste condicionado de 657 (Pós)

- **Agente:** anuncios-linkedin (departamento 11 Mídia Paga)
- **Linha:** pos
- **Data:** 26/10/2026 (etapa 1.15 da camada 1)
- **Versão:** 2, corrigida após qa-de-marketing-geral-2026-10-26-loteD (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-loteD.md)
- **Curso:** 657, Pós-graduação em Anestesiologia Avançada, turma II, São Paulo, semipresencial, início 13/03/2027 (catálogo, seção 2)
- **Status deste arquivo:** rascunho para o qa-de-marketing e pedido de aprovação humana. Nada sobe, nada é pago. A montagem no Campaign Manager é feita por humano, depois da decisão do cmo em 08/01/2027 (PP14) e da aprovação de R6.
- **Entradas lidas:**
  - .claude/agents/anuncios-linkedin.md; .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - CLAUDE.md; docs/execucao-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12, em especial 12.4, 12.6, 12.7, 12.11 e 12.12)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-pos-2026-10-26.md (seção 4, linha 5, e ordem de verba parcial)
  - contexto/catalogo-de-cursos.md; contexto/pos-graduacao.md; contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md
  - saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (seções 3, 4.1, PP7, PP14, encomendas)
  - saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (seções 2, 3.5, 4.2, 4.3, 4.6, EM8 e EM10)
  - saidas/11-midia-paga/analise-de-midia-pos-2026-10-26.md (657 pausada, histórico prioritário)
  - saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-26.md (não há criativo de 657 nem de LinkedIn)
  - saidas/05-social-e-comunidade/estrategia-social-pos-2026-10-26.md (LinkedIn orgânico fora, seção 4.5; ES5)
  - auditorias/11-midia-paga.md

**Nota de referência.** O pedido desta etapa cita "D13" para a regra de P5 e "D14" para o padrão de nomes. Na seção 12 do plano do cmo, a regra "P5 só para o LinkedIn de 657" é o item **EM8** (12.6), a das 3 semanas é **EM10** com o pedido **R6** (12.11), e o padrão de nomes e UTM é **D11 e D12** (12.7). D13 é a frase do curso livre e D14 trata de posts duplicados. Este arquivo segue o conteúdo pedido, com as referências da seção 12.

---

## Mudanças desta versão

- **LI-Q1 (obrigatório antes da montagem):** grupo de campanha, campanhas e utm_campaign passam a usar a chave `pos_657`, sem a área curta, como manda D12: grupo `pos_657_linkedin_lead_202701`, campanhas `pos_657_linkedin_lead_anest_202701` e `pos_657_linkedin_lead_rmk30d_202701`, e o mesmo valor no utm_campaign (seções 3 e 5). O nome com área curta da estrategia-de-midia-pos fica citado só como forma superada, nos fatos.
- **LI-Q2:** a referência "D8" para o evento de lead e o rastreio saiu (na seção 12 do cmo, D8 é a janela de silêncio). Agora aponta para EM11 da estrategia-de-midia-pos e para o teste de rastreio de 31/10 (C4, C10, seção 3 e lista de dados que faltam).
- Nada mais mudou: condições, públicos, criativos, leitura e critério de parar seguem iguais.

---

## 1. Resumo da decisão

1. **LinkedIn entra só como teste condicionado de 657**, com uma campanha, 2 conceitos e leitura de 3 semanas (11/01 a 31/01/2027). É a última frente na ordem de uso da verba (estrategia-de-marketing-pos, seção 6.2) e a primeira a cortar.
2. **Não sobe sem as 3 semanas aprovadas juntas** (EM10, R6). Sem a 3ª semana, o teste não roda neste trimestre e os 5% de P5 voltam para P3 na Meta.
3. **Bloqueio próprio de 657:** o pré-requisito de quem pode cursar ainda não está escrito na página nem confirmado pela Ufape (U10, PP7). Enquanto ele não existir, nenhum anúncio de 657 sobe em nenhum canal, e o LinkedIn não tem como recortar o público certo.
4. **Modelo: enxuta** (skill estrutura-de-campanha-paga, passo 2). Motivo: verba pequena (parte de 5% da verba nova), conta sem histórico no canal e público de nicho. Um grupo de campanha (oferta do curso, resposta direta), uma campanha de público frio, remarketing só se o público chegar a mil pessoas.
5. **Nenhum número de público, CPC, CPM, CPL ou verba existe hoje.** Tudo isso é [CONFIRMAR] no gerenciador e no PP1.

---

## 2. Condições de entrada (todas precisam fechar até 08/01/2027)

| # | Condição | Fonte | Estado em 26/10/2026 | Quem confirma |
|---|---|---|---|---|
| C1 | Pré-requisito de 657 definido pela Ufape e escrito na página da turma | U10 (cmo 12.12); PP7 (gestor) | Aberto. A página diz só "exclusiva para médicos veterinários anestesistas já atuantes", sem dizer como isso é comprovado [CONFIRMAR U10] | Ufape; humano que edita o site |
| C2 | Verba de P5 aprovada (PP2) e a 3ª semana aprovada junto (R6), com a verba do trimestre seguinte | EM10, R6 | [CONFIRMAR] | pessoa do marketing; cmo |
| C3 | Condição de volume fechada: com 2 conceitos e 5% de VN em 2 semanas, VN mínima = 40 x CPLmax_h de 657 no canal; se os 5% forem espalhados em 3 semanas, VN mínima = 60 x CPLmax_h | estrategia-de-midia-pos, 3.5 | CPLmax_h de 657 depende de Mmid e c [CONFIRMAR PP1] | gestor-de-midia |
| C4 | Insight Tag instalada no domínio faculdade.ufape.com.br, com a conversão de 657 configurada e testada | PP14; skill, passo 8 | Pendente. Quem instala [CONFIRMAR]; evento que a página registra (cadastro, início de checkout ou compra) [CONFIRMAR, EM11 da estrategia-de-midia-pos e teste de rastreio de 31/10] | humano de site e rastreio; arquiteto-de-fluxos |
| C5 | Públicos de remarketing criados logo depois da instalação da tag, antes do lançamento (o LinkedIn só conta a partir da criação) | skill, passo 8; instrução do agente | Depende de C4 | humano no gerenciador |
| C6 | Página da Ufape no LinkedIn existente e conta de anúncios com forma de pagamento ativa | ES5 (estrategia-social-pos) | [CONFIRMAR se a página existe e quem administra]. Anúncio sem página da empresa: [SUPOSIÇÃO] de que o LinkedIn exige a página para anunciar | Ufape |
| C7 | Público frio com tamanho estimado pela plataforma de pelo menos 15 mil membros (faixa de referência: 50 mil a 300 mil) | instrução do agente; estrategia-de-midia-pos, 4.6 | [CONFIRMAR no gerenciador]. Abaixo de 15 mil, o teste não sobe | humano no gerenciador |
| C8 | Página de destino em conformidade: sem a frase de certificação que a squad não repete e com a turma mínima de 15 alunos (a página ainda diz 20) | contexto da linha; decisão 11; ficha de 657 (alertas) | Pendente. Se a página não for corrigida, a subida exige decisão registrada da pessoa do marketing, como nas provas em E2 | Ufape; pessoa do marketing |
| C9 | Criativos de 657 aprovados pelo qa-de-marketing e pela conformidade | auditorias/11-midia-paga.md | Não existem ainda (seção 6) | criativos-de-anuncio; qa-de-marketing |
| C10 | Rastreio da origem até o CRM (UTM chegando com o lead) | PP4; EM11 e teste de rastreio de 31/10 (estrategia-de-midia-pos) | Pendente externo | arquiteto-de-fluxos |

Se qualquer condição não fechar até 08/01, a recomendação é **não subir** e devolver P5 para P3 na Meta (gestor, 4.1).

---

## 3. Estrutura (para o Campaign Manager)

Mapa em árvore. Orçamento definido na campanha (nível onde fica o público no LinkedIn), não no grupo, porque só há uma campanha de verba e o controle por público é o que se quer ler.

```
Grupo de campanha: pos_657_linkedin_lead_202701
  Campanha F (frio): pos_657_linkedin_lead_anest_202701
    Público: anest (seção 4, opção escolhida no gerenciador)
    Anúncio L1: 657-l1-precisao_img_protocolo_v1
    Anúncio L2: 657-l2-coord_tla_caso_v1 (ou a alternativa L2b, seção 6)
  Campanha R (remarketing, só se o público chegar a 1.000): pos_657_linkedin_lead_rmk30d_202701
    Público: rmk30d (visitantes da página de 657 nos últimos 30 dias, pela Insight Tag)
    Anúncios: os mesmos L1 e L2
```

| Item | Valor | Origem |
|---|---|---|
| Objetivo | Conversões no site (lead na página de 657, sem formulário nativo) | estrategia-de-midia-pos, 4.6: sem formulário nativo, para não coletar dado fora da política de privacidade da página [SUPOSIÇÃO do plano] |
| Conversão otimizada | o evento de lead de 657 que a Insight Tag registrar (cadastro ou início de checkout) [CONFIRMAR, EM11 da estrategia-de-midia-pos e teste de rastreio de 31/10] | C4 |
| Exclusões | quem já converteu em 657 (conversão da Insight Tag); a campanha F exclui o público rmk30d quando a campanha R existir | estrategia-de-midia-pos, 4.6 |
| Expansão de público | desligada | instrução do agente |
| Rede de audiência do LinkedIn | desligada | instrução do agente |
| Lance | automático (entrega máxima) na semana 1; mudança para lance manual um pouco abaixo do custo médio observado só na revisão de 18/01, como uma mudança única e com pedido aprovado | instrução do agente (regra prática, não meta) |
| Verba | parte de P5: 5% de VN em 11/01 a 24/01 mais a 3ª semana (25/01 a 31/01) com verba do trimestre seguinte [CONFIRMAR valores] | gestor 4.1; EM10 |
| Leads por semana esperados | verba semanal da campanha dividida por CPLmax_h de 657 [CONFIRMAR: os dois números faltam] | skill, passo 4 |
| Datas | sobe em 11/01/2027; revisões em 18/01 e 25/01; termina em 31/01/2027 às 23h59; leitura final em 01/02/2027 | EM10; estrategia-de-midia-pos, calendário |
| Mensagem patrocinada | fora (sem formulário, sem regra de frequência aprovada) | instrução do agente |

**Por que não abrir outros grupos (remarketing amplo, conteúdo, prova):** a skill manda financiar um grupo antes de abrir o próximo. Com 3 semanas e parte de 5% da verba, só a oferta do curso tem chance de ler algo.

**Relação com a Meta de 657.** A Meta de 657 só sobe com PP7 (alvo 14/12). Visitantes vindos do LinkedIn entram no remarketing da Meta (pixel). Por isso a leitura do LinkedIn usa o lead com utm_source=linkedin no CRM, e não a soma dos canais [SUPOSIÇÃO de atribuição por último clique com UTM, a conferir pelo arquiteto-de-fluxos, P15].

---

## 4. Públicos por área profissional (tudo [SUPOSIÇÃO] até a consulta no gerenciador)

Público-alvo da página: médicos veterinários anestesistas já atuantes (ficha de 657). O recorte final depende do pré-requisito (C1, U10). Nenhuma segmentação por idade, gênero ou característica sensível; nenhuma lista de contatos enviada (sem base legal registrada). Localização: Brasil [SUPOSIÇÃO: a turma é em São Paulo, mas 12 dos 18 módulos são online e a persona secundária viaja para os presenciais; recortar só SP tende a encolher demais um público já pequeno]. Se a Ufape preferir só o estado de SP, vale a escolha dela.

| Opção | Critérios (nomes das opções como aparecem na plataforma: [CONFIRMAR]) | Quando usar | Tamanho estimado |
|---|---|---|---|
| A. Cargo | cargos ligados a anestesia veterinária (por exemplo, médico veterinário anestesista, anestesiologista veterinário), sem senioridade (cargo e senioridade não se combinam) | primeira escolha, se passar de 15 mil | [CONFIRMAR no gerenciador] |
| B. Competência e setor | competência "anestesiologia" ou "anestesia" mais setor de serviços veterinários | se A ficar abaixo de 15 mil | [CONFIRMAR no gerenciador] |
| C. Formação e competência | área de formação em medicina veterinária mais competência em anestesia | último recurso, se B ainda ficar pequeno | [CONFIRMAR no gerenciador] |
| R. Remarketing | visitantes da página de 657 nos últimos 30 dias (Insight Tag) | só com 1.000 pessoas ou mais | [CONFIRMAR] (depende da data de criação, C5) |

Regra: escolher uma opção para a campanha F (sem empilhar critérios que encolham o público). Se nenhuma passar de 15 mil, o teste não sobe e o motivo vai para a leitura de 08/01. O nome do bloco de público na UTM e no nome da campanha fica "anest" em qualquer das opções; a opção usada é registrada no pedido de subida.

---

## 5. Nomes e UTM (padrão D11 e D12 do cmo; estrategia-de-midia-pos, 4.2 e 4.3)

| Nível | Nome |
|---|---|
| Grupo de campanha | pos_657_linkedin_lead_202701 |
| Campanha frio | pos_657_linkedin_lead_anest_202701 |
| Campanha remarketing | pos_657_linkedin_lead_rmk30d_202701 |
| Anúncio L1 | 657-l1-precisao_img_protocolo_v1 |
| Anúncio L2 | 657-l2-coord_tla_caso_v1 |
| Anúncio L2b (alternativa) | 657-l2b-modulos_car_temas_v1 |

Formatos no nome: img (imagem única), tla (anúncio de líder de opinião), car (carrossel).

URL de destino com UTM (modelo, anúncio L1 na campanha frio):

`https://faculdade.ufape.com.br/produto/657/pos-graduacao-em-anestesiologia-avancada?utm_source=linkedin&utm_medium=paid_social&utm_campaign=pos_657_linkedin_lead_anest_202701&utm_content=657-l1-precisao_img_protocolo_v1&utm_term=anest`

- utm_source=linkedin; utm_medium=paid_social; utm_campaign = nome da campanha; utm_content = nome do anúncio; utm_term = público (anest ou rmk30d).
- Tudo em minúsculas, sem acento, sem dado pessoal.
- No anúncio de líder de opinião, o link com UTM precisa estar no próprio post do docente [SUPOSIÇÃO sobre como a plataforma trata o link do post promovido; conferir na montagem]. Se o post não aceitar o link com UTM, L2 sai e entra L2b.

---

## 6. Criativos ligados (não existem ainda: encomenda ao criativos-de-anuncio)

O pacote de criativos da Pós (criativos-de-anuncio-pos, 1.13) não tem peça de 657 nem de LinkedIn. Abaixo, o rascunho de direção e de texto para o criativos-de-anuncio fechar na camada 3, com o qa-de-marketing. Dados de curso só do catálogo e da ficha. Toda peça com preço mostra parcelas, valor da parcela, total e matrícula. Nenhuma frase de certificação. Nenhuma urgência. Nenhuma promessa de cargo, salário ou promoção. Nenhuma menção a 616, a crédito, combo ou desconto da ponte (D6 e D7).

### L1. Conteúdo patrocinado, imagem única (oferta do curso)

- **Ideia:** a passagem da "anestesia de protocolo" para a "anestesia de precisão", que é a proposta escrita na página de 657.
- **Introdução (rascunho):** "Da anestesia de protocolo à anestesia de precisão: fisiologia aplicada, decisão crítica e gestão de risco no paciente de alto risco. Pós-graduação em Anestesiologia Avançada, para médicos veterinários anestesistas que já atuam [texto do pré-requisito: CONFIRMAR U10]. Semipresencial em São Paulo, 360 h em 18 módulos, início em 13/03/2027. 30x de R$ 1.613,33 (total de R$ 48.400,00) e matrícula de R$ 250,00. Turma confirmada a partir de 15 alunos."
- **Título (rascunho):** "Pós-graduação em Anestesiologia Avançada: anestesia de precisão"
- **Texto na imagem:** "Anestesia de precisão" / "18 módulos, online e práticos em São Paulo" / "Início em 13/03/2027"
- **CTA:** Saiba mais
- **Nota:** a frase da turma mínima depende da correção da página (C8); se a página continuar com 20, a peça não cita número até a correção, para não divergir do destino.

### L2. Anúncio de líder de opinião (post da coordenação promovido)

- **Quem:** coordenação como na ficha: Dra. Mayara Travalini de Lima ou Dr. Alessandro Martins. Autorização de imagem e de citação registrada (decisões 8 e 10). Texto em primeira pessoa precisa do ok do próprio docente, porque é a voz dele (cmo, 12.9).
- **Condição:** existir um post da pessoa no LinkedIn, de preferência um que já tenha ido bem no orgânico [CONFIRMAR se existe]; a squad não escreve post em nome de docente sem o ok dele.
- **Pauta sugerida (para o docente escrever ou aprovar):** um tema do cronograma da página, por exemplo ler o estado cardiovascular além da pressão arterial (módulo 3, hemodinâmica avançada), com uma pergunta de caso e o convite para conhecer a turma. Conteúdo clínico passa pela revisão do próprio docente (revisor nomeado [CONFIRMAR]).
- **Link:** página de 657 com a UTM de L2.

### L2b. Alternativa a L2: carrossel de temas do programa

- Usar só se L2 não tiver post ou não aceitar o link com UTM.
- 5 cartões com temas reais do cronograma da ficha: anestesia total intravenosa (TIVA e TCI); bloqueios locorregionais guiados por ultrassom; hemodinâmica avançada; ventilação mecânica aplicada à anestesia; anestesia para cirurgias cardiotorácicas e neurológicas. Último cartão com início, praça, modalidade e condições completas, como em L1.
- CTA: Saiba mais.

**Anúncio de documento e formulário de lead:** fora deste teste. O plano decidiu destino na página, sem formulário nativo (estrategia-de-midia-pos, 4.6). Se a Ufape quiser formulário nativo no futuro, ele precisa do aviso de privacidade da Ufape e só dos campos do atendimento [CONFIRMAR texto da política].

---

## 7. Leitura de 3 semanas

Sem meta numérica antes da linha de base; os limites dependem de CPLmax_h de 657 [CONFIRMAR PP1].

| Semana | Datas | O que se lê | Decisão possível (sempre pedido a humano) |
|---|---|---|---|
| 1 | 11/01 a 17/01 | entrega (gasto contra o planejado), cliques para a página de destino (não a taxa de cliques que inclui curtidas), conversão registrada pela Insight Tag, lead com utm_source=linkedin no CRM | só correção de rastreio ou de destino; nenhuma mudança por desempenho |
| 2 | 18/01 a 24/01 | o mesmo, mais custo por clique na página e por lead contra CPLmax_h, frequência e penetração do público (alcançados divididos pelo tamanho do público) | uma mudança única: pausar o anúncio que gastou 1,5 a 2 x CPLmax_h sem lead, ou passar o lance a manual |
| 3 | 25/01 a 31/01 | o mesmo, mais qualificação dos leads no CRM (somados, se cumprem o pré-requisito de 657) | nenhuma mudança; a campanha termina em 31/01 |
| Leitura final | 01/02/2027 | CPL do canal contra CPLmax_h; proporção de leads qualificados; penetração; comparação com o CPL da Meta de 657 no mesmo período, se houver | recomendação ao cmo: repetir no próximo trimestre (com 359 e 352, de maio), ajustar público ou deixar o canal fora |

Os números entram só a partir das exportações do Campaign Manager e do CRM, somados por campanha e semana. Nenhum dado pessoal de lead.

---

## 8. Critério de parar

| Gatilho | Ação pedida | Como desfazer |
|---|---|---|
| Qualquer condição de C1 a C10 aberta em 08/01 | não subir; P5 volta para P3 na Meta | subir em outro trimestre com as condições fechadas |
| 3ª semana não aprovada (R6) | não subir neste trimestre | idem |
| Público frio abaixo de 15 mil nas opções A, B e C | não subir | rever o recorte com a Ufape |
| Insight Tag sem registrar conversão em 48 h de veiculação | pausar a campanha e corrigir o rastreio | reativar depois do teste de rastreio |
| Página de 657 fora do ar, com preço, data ou status diferente do catálogo, ou status da turma diferente de "aberto" | pausar a campanha no mesmo dia | reativar depois da correção |
| Anúncio com gasto de 1,5 a 2 x CPLmax_h sem lead | pausar o anúncio (nunca os dois ao mesmo tempo) | reativar o anúncio |
| Fim do teste | encerrar em 31/01/2027, 23h59, sem prorrogar sem nova aprovação | nova aprovação para outro período |

Nada disso é feito pela squad: cada linha é um pedido para humano executar no gerenciador.

---

## 9. Pedidos de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| LI1 | Aprovar este desenho do teste de 657 (seções 3 a 8) para a decisão do cmo em 08/01/2027 | PP14; EM10 | parte de P5 [CONFIRMAR] | primeira leitura do canal na Pós | não subir |
| LI2 | Aprovar as 3 semanas juntas (11/01 a 31/01/2027), com a 3ª semana na verba do trimestre seguinte | R6 | 5% de VN mais a 3ª semana [CONFIRMAR] | leitura que decide o canal | P5 volta para a Meta de P3 |
| LI3 | Ufape definir o pré-requisito de 657 e escrevê-lo na página | U10; PP7 | sem custo de mídia | anúncio e público coerentes com quem pode se matricular | não se aplica |
| LI4 | Instalar a Insight Tag, configurar e testar a conversão de 657 e criar o público rmk30d logo em seguida (dezembro, se possível) | C4 e C5 | sem custo de mídia | remarketing com público acumulado antes de 11/01 | remover a tag |
| LI5 | Confirmar a página da Ufape no LinkedIn, o administrador e a forma de pagamento da conta de anúncios | C6; ES5 | sem custo | conta pronta para montar | não se aplica |
| LI6 | Corrigir a página de 657 (frase de certificação e turma mínima de 15) ou registrar a decisão de subir com a página como está | C8; contexto da linha | sem custo de mídia | destino em conformidade | não se aplica |
| LI7 | Encomendar L1 e L2 (ou L2b) ao criativos-de-anuncio, com o ok do docente para o post em primeira pessoa | C9; cmo 12.9 | sem custo de mídia | criativos prontos para o qa até 04/01 | não usar o conceito |

---

## 10. Checklist de montagem (para o humano, no dia da subida)

- [ ] C1 a C10 fechadas e registradas.
- [ ] Insight Tag recebendo eventos no domínio; conversão de 657 testada.
- [ ] Público rmk30d criado antes do lançamento.
- [ ] Opção de público escolhida, com tamanho estimado anotado; expansão de público e rede de audiência desligadas.
- [ ] Objetivo de conversões no site; conversão certa selecionada; exclusão de quem já converteu.
- [ ] Nomes de grupo, campanha e anúncios como na seção 5.
- [ ] UTM completa em cada anúncio, conferida com um clique de teste chegando ao CRM com origem.
- [ ] Criativos aprovados pelo qa-de-marketing e pela conformidade (sem certificação, sem urgência, preço completo, nome "Pós-graduação em Anestesiologia Avançada").
- [ ] Datas de início e fim (11/01 e 31/01/2027) e verba aprovadas configuradas.
- [ ] Exportação inicial guardada, para desfazer.

---

## 11. Auditorias aplicadas

- auditorias/11-midia-paga.md: Insight Tag e públicos antes do lançamento (C4, C5); post de docente com autorização registrada (decisões 8 e 10) e ok do docente para texto em primeira pessoa; nenhuma ação na plataforma pela squad.
- auditorias/conformidade-educacional.md: nenhuma frase de certificação; nenhuma urgência; preço com parcelas, valor da parcela, total e matrícula; nome no padrão "Pós-graduação em"; nenhum dado pessoal; destino com pendência de conformidade sinalizado (C8).

Próximo agente sugerido: qa-de-marketing.

---

## Fatos (com fonte)

- 657 é a Pós-graduação em Anestesiologia Avançada, turma II, São Paulo, semipresencial, 360 h, 18 módulos, início 13/03/2027, 30x de R$ 1.613,33, total de R$ 48.400,00, matrícula de R$ 250,00, status aberto (catálogo, seção 2; ficha de 657).
- A página de 657 diz que a Pós é exclusiva para médicos veterinários anestesistas já atuantes, mostra "Mínimo 20 alunos" e traz a frase de certificação que a squad não repete (ficha de 657, alertas).
- Turma mínima de 15 alunos também na Pós (decisão 11 de 26/10/2026, docs/execucao-2026-10-26.md).
- LinkedIn é teste condicionado só para 657 no bloco 3 (gestor-de-midia-pos, seção 3; PP14); P5 só para o LinkedIn de 657 (cmo, 12.6, EM8); sobe só com as 3 semanas de 11/01 a 31/01/2027 aprovadas juntas (cmo, 12.6, EM10, e 12.11, R6).
- Decisão do cmo sobre o LinkedIn em 08/01/2027 (gestor-de-midia-pos; estrategia-social-pos, S11).
- Campanha planejada na estrategia-de-midia-pos como pos_657-anest-avancada_linkedin_lead_anest_202701 (forma com área curta, superada por D12; aqui pos_657_linkedin_lead_anest_202701), com destino na página e sem formulário nativo (estrategia-de-midia-pos, 4.6); UTM linkedin e paid_social (estrategia-de-midia-pos, 4.3; cmo, D11 e D12).
- Condição de volume: VN mínima = 40 x CPLmax_h com 2 semanas, ou 60 x CPLmax_h com os 5% em 3 semanas (estrategia-de-midia-pos, 3.5).
- 657 está pausada e bloqueada até o pré-requisito estar na página (PP7; analise-de-midia-pos).
- Pré-requisito de 657 é a pergunta U10 à Ufape (cmo, 12.12); o par 616 para 657 só cita o pré-requisito depois de confirmado (cmo, 12.4).
- LinkedIn orgânico fora neste trimestre; existência da página da Ufape no LinkedIn a confirmar (estrategia-social-pos, 1.3, 4.5 e ES5).
- Coordenação de 657: Dra. Mayara Travalini de Lima e Dr. Alessandro Martins (ficha de 657); autorização de imagem e de citação registrada para todos os docentes (decisões 8 e 10).

## Suposições ([SUPOSIÇÃO])

- [SUPOSIÇÃO] Localização Brasil, e não só SP, para não encolher o público (12 dos 18 módulos são online).
- [SUPOSIÇÃO] Opções de público A, B e C e os nomes de cargo, competência, setor e formação; nomes exatos como aparecem na plataforma a conferir.
- [SUPOSIÇÃO] O LinkedIn exige página da empresa para anunciar; o link com UTM do post promovido segue o que estiver no post.
- [SUPOSIÇÃO] Atribuição do lead ao LinkedIn pelo último clique com UTM, mesmo com a Meta de 657 rodando no mesmo período.
- [SUPOSIÇÃO] Regras práticas do agente e da skill (público frio de 50 mil a 300 mil e nunca abaixo de 15 mil; remarketing a partir de mil; pausa com gasto de 1,5 a 2 x CPLmax_h sem lead; lance automático na semana 1). São referências de trabalho, não regras confirmadas das políticas da plataforma.
- [SUPOSIÇÃO do plano] Sem formulário nativo, para não coletar dado fora da política de privacidade da página.
- [SUPOSIÇÃO de desenho] Modelo enxuta, com uma campanha de frio e remarketing condicionado.

## Dados que faltam ([CONFIRMAR])

- [CONFIRMAR U10] Pré-requisito de 657 e o texto que vai na página e no anúncio.
- [CONFIRMAR] Verba de P5 e da 3ª semana (R6); verba nova total (PP2).
- [CONFIRMAR] CPLmax_h de 657 (Mmid, c e demais variáveis do PP1); leads por semana esperados.
- [CONFIRMAR] Tamanho dos públicos A, B, C e rmk30d no gerenciador; CPC, CPM e CPL do canal: [DADO NÃO FORNECIDO].
- [CONFIRMAR] Quem instala a Insight Tag e qual evento de lead a página de 657 registra (EM11; teste de rastreio de 31/10).
- [CONFIRMAR] Existência da página da Ufape no LinkedIn, administrador e forma de pagamento da conta de anúncios (ES5).
- [CONFIRMAR] Correção da página de 657 (frase de certificação e turma mínima de 15) ou decisão registrada.
- [CONFIRMAR] Existência de post da coordenação no LinkedIn e ok do docente para texto em primeira pessoa; nome do revisor docente do conteúdo clínico.
- [CONFIRMAR] Ferramenta que leva a UTM ao CRM (P15).
