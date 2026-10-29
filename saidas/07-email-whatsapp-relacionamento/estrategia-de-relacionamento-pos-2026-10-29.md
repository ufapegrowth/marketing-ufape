# Estratégia de relacionamento por círculo e programa permanente da base: Pós-graduação em Gastroenterologia Veterinária (piloto e moldura)

- **Agente:** estrategia-de-relacionamento (departamento 07, E-mail, WhatsApp e Relacionamento)
- **Linha:** pos
- **Data:** 29/10/2026
- **Encomenda:** do cmo, na seção "Próximo passo e encomendas da cadeia" do plano saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-29-plano-estrategico-divulgacao-gastro.md. Pedido de origem do CEO em 29/10/2026.
- **Curso piloto:** Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo, código 68606 (catálogo, seção 2). A estratégia é do curso, não de uma turma (decisão 28).
- **Decisão 28 do CEO (29/10/2026), aplicada nesta revisão:** 20% de desconto para alunos e ex-alunos de Pós em Pós, simpósios e workshops; a base tem consentimento para contato sobre novas oportunidades e é trabalhada normalmente por mídia paga [CONFIRMAR a interpretação]; sem desconto para o indicado; parceiros saem como canal; a próxima turma abre normalmente 3 a 4 meses depois de uma turma confirmada [CONFIRMAR a interpretação]; grupos de estudo já existem e servem de comunidade.
- **Sem datas, sem textos de mensagem, sem peças.** Este arquivo só traz estratégia. Frequências são limites e durações de regra, nunca calendário.
- **Como ler:** cada seção traz dois blocos.
  - **[MOLDURA]**: vale para qualquer curso de Pós (com ajuste, para Livres e Eventos).
  - **[GASTRO]**: o preenchimento do piloto. É o que troca no próximo curso.
- **Status:** rascunho para o qa-de-marketing (auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago. A squad escreve regra; o CRM da Ufape executa, só para quem deu consentimento.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 26)
  - contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (seção 2, linha 68606, e seção 3 para a prova 68650; a seção 4 em diante só até onde o catálogo foi aberto, a parte final não foi relida)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-29-plano-estrategico-divulgacao-gastro.md (inteiro)
  - saidas/07-email-whatsapp-relacionamento/estrategia-de-relacionamento-pos-2026-10-26.md (seções 0 a 9.1; a parte final de 9.2 em diante não foi relida)
- **Não li:** cmo-geral-2026-10-26.md. As regras D16 e E1 a E4 entram como o plano de 29/10 e a decisão 17 as descrevem (teto por contato, engajamento, erro 131049 da Meta, descadastro em até 48 h, opt-in por canal e finalidade). Onde preciso do texto exato de E1 e E2, aponto para a seção 13 do cmo-geral e não repito número.
- **Não abri** faculdade.ufape.com.br. Nenhuma busca na web nesta rodada.
- **Dados pessoais:** nenhum. Segmentos e campos, nunca pessoas. Docentes não são nomeados.

---

## 0. Resumo para quem decide

1. **Seis segmentos de CRM** (C1 a C5 e C8) com critério de entrada, de saída, consentimento por canal (e-mail, WhatsApp, anúncio) e uma regra de prioridade em três camadas: saída e serviço vencem tudo; régua ativa de turma vence programa permanente; entre círculos vale o mais quente para a oferta, mas a regra que protege o contato vence a que vende (aluno em curso e Graduação nunca recebem oferta de compra da Pós).
2. **Três programas permanentes da base da área** (lista de espera, carta da área, convite ao T2), cada um com objetivo, quem entra, frequência máxima, o que mede e como sai. Os três dividem o mesmo teto D16 do contato, então o programa permanente cede a vez a qualquer régua de turma ou de prova.
3. **Proposta de regra de indicação (T1)** para a Ufape decidir: elegibilidade, gatilho (1ª mensalidade paga pelo indicado), atribuição, limites, privacidade do indicado e opções de benefício sem valor para quem indica; não há desconto para o indicado (decisão 28). Nada é prometido antes da decisão (regra C8 do plano do cmo e CDC).
4. **Consentimento separado por finalidade e por canal.** Participar de uma sessão ao vivo ou entrar na lista de espera nunca depende de aceitar campanha. Anúncio com lista de clientes fica liberado para a base com consentimento para novas oportunidades, que a Ufape já trabalha por mídia paga (decisão 28); o registro formal da base legal segue [CONFIRMAR] (L6, N12, UA4).
5. **Nenhum número de base, taxa ou meta existe.** Tudo que depende de tamanho de círculo, consentimento e linha de base é [CONFIRMAR]. As primeiras 4 semanas de leitura viram a linha de base.
6. **Trava de Gastro:** a próxima turma do curso ainda não está no catálogo; pela decisão 28 ela abre normalmente 3 a 4 meses depois de uma turma confirmada [CONFIRMAR a interpretação]. A lista de espera e a carta trabalham a base sem chamada de compra até a turma ter data.

---

## 1. Os segmentos de CRM (C1 a C5 e C8)

### 1.1 [MOLDURA] Regras comuns

**Conceitos.** Círculo é o segmento do contato pela relação dele com a Ufape e com a área. Consentimento é o registro de permissão por canal e por finalidade. Programa é o que o contato recebe. O contato só recebe campanha se o círculo permitir e o consentimento do canal existir.

**Consentimentos que o CRM precisa guardar por contato** (canal, finalidade, data, origem e texto aceito; nomes de campo [CONFIRMAR com o arquiteto-de-fluxos]):

| Código | Consentimento | O que libera | Observação |
|---|---|---|---|
| K1 | E-mail de campanha, por finalidade | carta da área, convite a sessão, aviso de turma | finalidades separadas (ver 1.2); descadastro em até 48 h (E3) |
| K2 | WhatsApp de campanha, por finalidade | convite curto, lembrete, aviso de turma | só com opt-in (E4); "responda SAIR" em toda mensagem; só em horário comercial e dia útil; contato que bloqueia ou denuncia sai (E2 e E3) |
| K3 | Serviço | confirmação, gravação prometida na inscrição, documento, lembrete de algo que o contato comprou ou pediu | não carrega campanha (L3); não conta no teto, mas respeita o horário do WhatsApp |
| K4 | Anúncio por engajamento | remarketing de quem visitou página ou viu conteúdo, sem lista de clientes | depende do aviso e do aceite de cookies e pixel no site [CONFIRMAR banner] |
| K5 | Anúncio com lista de clientes | público personalizado e semelhante a partir de lista | **liberado para a base com consentimento para novas oportunidades** (decisão 28), que a Ufape já trabalha por mídia paga; registro formal da base legal pelo encarregado de dados segue [CONFIRMAR] (L6, N12, UA4) |

**Teto D16 que vale para todos os programas:** até 2 WhatsApp e 2 e-mails de campanha por contato por semana, somando linhas e newsletter; no máximo 1 mensagem de campanha por dia, em qualquer canal. Contato em duas bases fica com o teto menor. Nenhum programa deste arquivo cria teto próprio acima disso.

**Regra de horário do WhatsApp.** Campanha e lembrete de WhatsApp só em dia útil, dentro do horário comercial da Ufape. Isso vale também para lembrete de sessão ao vivo que aconteça fora do horário comercial: o lembrete sai dentro do horário comercial anterior à sessão, nunca no horário da sessão. Única exceção: resposta a contato iniciado pelo próprio candidato ou aluno.

**Saída universal.** SAIR no WhatsApp ou descadastro no e-mail tira o contato de toda campanha de todas as linhas (regra da estratégia de relacionamento de 26/10/2026, seção 3.2, item 3). Serviço pode continuar, conforme a Ufape confirmar (R7 daquela estratégia, ainda aberto).

### 1.2 [MOLDURA] Finalidades de consentimento propostas

Duas finalidades de campanha, escritas na tela do consentimento em linguagem simples [texto a aprovar pela Ufape e pelo encarregado]:

- **F-A, conteúdo e convites da área:** alimenta a carta da área e os convites a sessões ao vivo.
- **F-B, aviso de próxima turma:** alimenta a lista de espera. Só aviso de abertura de turma e do que a turma exige para entrar.

Quem aceita uma não aceita a outra. O consentimento de F-A e F-B é sempre opcional: o ato principal (inscrever-se na sessão, perguntar sobre o curso) acontece sem ele. Caixa de aceite nunca vem marcada.

### 1.3 [MOLDURA] Tabela dos segmentos

| Círculo | Critério de entrada | Critério de saída | E-mail | WhatsApp | Anúncio |
|---|---|---|---|---|---|
| **C1. Ex-aluno do próprio curso** | concluiu turma anterior do mesmo curso (registro acadêmico) | pede SAIR; fica sem interação pelo prazo de higiene e não reconfirma; ou passa a ser aluno da turma em curso (vai para C3 enquanto durar) | K1 de F-A e F-B; campanha de curso só com K1 | K2 só se o opt-in existir e a interação for recente (E1) | K4 sim; K5 só com UA4 |
| **C2. Comprador da mesma área em Livres e Eventos** | comprou produto da área (mini curso, grupo de estudos, imersão), é formado e já passou a janela de silêncio do curso (regra D8 da estratégia de 26/10) | pede SAIR; matricula (vira aluno, C3); sem interação pelo prazo de higiene | K1; sem crédito, combo ou desconto da ponte Livres para Pós (D7) | igual a C1 | K4 sim; K5 só com UA4 |
| **C3. Aluno atual de outra Pós ou Livre** | matrícula ativa em outro curso, com opt-in | conclui (vai para C1 se for o mesmo curso, ou C4); cancela ou fica inadimplente (sem campanha; só serviço da secretaria e do financeiro) [SUPOSIÇÃO]; pede SAIR | K1 só para conteúdo da área e indicação. **Nunca oferta de compra de outra Pós** | só convite a sessão e a indicação, com opt-in; canal de serviço da secretaria nunca vende (L3) | K4 sim, sem oferta de compra; K5 não |
| **C4. Ex-aluno de outras Pós, Livres e Eventos** | concluiu outro curso e declarou interesse na área, ou clicou e consumiu conteúdo da área (interesse declarado, nunca suposto) | pede SAIR; sem interação pelo prazo de higiene | K1 de F-A; F-B só se pediu aviso | igual a C1 | K4 sim; K5 só com UA4 |
| **C5. Graduação em Medicina Veterinária** | aluno atual com 18 anos ou mais e opt-in de comunicação institucional | forma-se (sai de C5; entra em C4 com origem "egresso da Graduação", só se aceitar de novo); pede SAIR | só comunicação institucional (eventos, aulas abertas institucionais). **Nenhuma venda de Pós** | nenhuma campanha de Pós | nenhum anúncio de Pós; menor de 18 anos nunca |
| **C8. Indicação** | duas funções: **indicador** (contato de C1 a C4 com K1 ou K2 que recebeu e aceitou o convite a indicar; C6 e C7 só se a Ufape decidir, seção 3; C5 nunca) e **indicado** (pessoa nova que preenche o próprio formulário pelo link ou código) | indicador: pede SAIR, deixa o programa ou o programa encerra. Indicado: matricula, recusa, fica sem interação pelo prazo de higiene ou pede SAIR | indicador: K1 (convite a indicar é campanha). Indicado: só depois do próprio consentimento, nunca por dado passado pelo indicador | idem | indicado: K4 se aceitar cookies; K5 não |

**O indicado** é tratado como contato novo e frio (C9) até aceitar o próprio consentimento; a diferença é a origem "indicação", que fica registrada.

### 1.4 [MOLDURA] Prioridade quando o contato está em mais de um círculo

O CRM aplica as camadas nesta ordem. A primeira que se aplica decide.

1. **Saída vence tudo.** SAIR, descadastro, bloqueio ou denúncia suspendem a campanha em todas as linhas.
2. **Serviço vence campanha.** Quem tem matrícula, inscrição ou pedido em andamento recebe o serviço antes de qualquer programa permanente.
3. **Régua ativa de turma ou de prova vence programa permanente.** Segue a fila D2 da estratégia de 26/10/2026 (seção 4): serviço, toque principal de campanha com data, follow-up, nutrição, reativação. Todo programa deste arquivo é "nutrição" e fica atrás das réguas com data. O que é suprimido não acumula para depois.
4. **Entre círculos, vale o mais quente para o tipo de oferta:** C1, depois C2, C3, C4, C5. O círculo mais quente define a trilha de mensagem e o campo "círculo de origem" no momento da matrícula.
5. **A regra de proteção vence a regra de oferta.** Se qualquer círculo do contato proíbe a oferta, ela não sai. Exemplos: contato em C2 e C3 (comprador da área que hoje é aluno de outra Pós) recebe a trilha de conteúdo e de indicação, nunca a oferta de compra; contato em C5 recebe só institucional, mesmo que tenha comprado um Livre.
6. **Indicação é uma camada, não um círculo.** O indicador continua no círculo dele e ganha a marca "indicador". Quando a matrícula chega com código de indicação, a origem registrada é "indicação" e o círculo do indicado vai num campo secundário. É assim que o T1 se mede sem esconder a origem real.
7. **Um contato, uma mensagem por dia, um programa por vez.** Quando dois programas permanentes disputam a mesma semana, vale a ordem: aviso de turma da lista de espera (só se houver turma no catálogo), convite à sessão, carta. A carta pode atrasar sem prejuízo.

### 1.5 [GASTRO] Preenchimento dos segmentos

| Círculo | Gastro | Particularidades e dados que faltam |
|---|---|---|
| C1 | ex-alunos das turmas I a VIII da Pós-graduação em Gastroenterologia Veterinária (a 68606 é a turma IX, catálogo e ficha) | tamanho e consentimento [CONFIRMAR, UN1]. Quem cursou e não concluiu só entra se a Ufape decidir [CONFIRMAR]. Uso de "tradição de turmas" como prova é [CONFIRMAR] (ufape-geral.md, seção Provas) |
| C2 | compradores de 721 (grupo de estudos), 455 e 669 (mini cursos), 291 (imersão online em gastroendoscopia), 68637 e 623 (imersões presenciais em endoscopia digestiva) | 455 aceita graduandos: sem campo "formado" confirmado, o contato entra em C2 sem oferta de Pós [CONFIRMAR campo]. Nenhuma peça ou link aponta para a página 623 até a correção do site (decisão 13); comprador de 623 pode estar em C2, mas o conteúdo não leva à página 623 |
| C3 | alunos de 68608 (Hematologia, a coordenação também ensina), 68635, 68623 e 68617, só quando cada turma começar (pelo catálogo, nenhuma das quatro começou); alunos das áreas vizinhas 653 (Endoscopia) e 564 (Nutrologia) | a turma atual do próprio curso (68606) é tratada como C3 enquanto dura, com as mesmas proteções. Regra da Ufape para comunicar com aluno em curso [CONFIRMAR] |
| C4 | ex-alunos de Clínica Médica, Endocrinologia, Nefrologia, Diagnóstico por Imagem, Felinos, Endoscopia e Nutrologia (áreas cujos módulos tocam Gastroenterologia, conforme o plano) | campo de interesse declarado por área [CONFIRMAR]. "Interesse" só por ação do contato (clique em conteúdo da área, pedido de aviso), nunca por dedução da squad |
| C5 | alunos da Graduação em Medicina Veterinária em São Paulo | se há egressos é [CONFIRMAR] (N11); pela data do ato, provavelmente ainda não [SUPOSIÇÃO] |
| C8 | indicadores vindos de C1 a C4 (e de C6 e C7 se a Ufape decidir, ver seção 3); indicados são clínicos de pequenos animais que atendem casos gastrointestinais | regra de elegibilidade na seção 3 |

---

## 2. Programa permanente da base da área

### 2.1 [MOLDURA] Desenho comum

A base da área é o conjunto de contatos com interesse declarado no curso e consentimento por canal (métrica "base da área" do plano). Três programas a alimentam e a leem:

| Programa | Papel | Canal principal | Finalidade de consentimento |
|---|---|---|---|
| Lista de espera da próxima turma (F10) | guardar quem quer saber da próxima turma | e-mail; WhatsApp só aviso curto com K2 | F-B |
| Carta da área (newsletter da especialidade) | manter a área viva entre turmas, com conteúdo clínico revisado | e-mail | F-A |
| Convite ao T2 (caso clínico ao vivo, F2) | gerar inscritos, presença, novos consentimentos e conversas | e-mail para convite; WhatsApp para lembrete curto com K2 | F-A |

Regras de convivência:

- Os três programas são "nutrição" na fila D2: cedem a vez a qualquer régua com data.
- Orçamento por contato: dentro do teto D16, o conjunto dos três programas ocupa no máximo 1 e-mail e 1 WhatsApp de campanha por semana, em dias diferentes [SUPOSIÇÃO: deixa a outra metade do teto para as réguas de turma e de prova].
- Um contato que está na lista de espera e na carta recebe uma mensagem por vez; o aviso de turma substitui a carta daquela semana.
- Toda mensagem leva saída simples. Todo envio em massa é pedido de aprovação humana (o que, por que, quantos contatos [CONFIRMAR], efeito esperado, como desfazer: pausar o programa no CRM).
- Nenhum programa cita promessa de vaga, de resultado, de emprego ou de desconto sem regra escrita. Preço só como o catálogo e o texto-padrão de preço da Ufape (parcelas, valor da parcela, total e inscrição).
- Conteúdo clínico passa por revisor docente antes do envio. A squad não escreve conduta nem dose.

### 2.2 [MOLDURA] Lista de espera da próxima turma (F10)

| Item | Definição |
|---|---|
| Objetivo | Guardar com consentimento quem quer ser avisado quando houver nova turma do curso, e evitar que o interesse se perca entre turmas. Medida de sucesso: base da área e, depois, matrículas com origem "lista de espera" |
| Quem entra | (a) quem pediu "avise-me" na página da área ou da turma com K1 ou K2 de F-B; (b) lead que não fechou, **só depois** de encerrada a janela da turma em captação (a Ufape aceita matrícula até o 3º módulo, decisão 18) e só se aceitar F-B; (c) quem pediu aviso no atendimento de vendas, com o consentimento registrado na conversa; (d) quem se inscreveu numa sessão ao vivo e marcou F-B. Nunca entra por importação de lista, compra, raspagem ou grupo de WhatsApp (L4) |
| O que recebe | Confirmação de entrada (serviço, uma vez). Aviso de abertura da próxima turma e do que ela exige. Quando não houver turma no catálogo, no máximo um aviso de manutenção que pergunta se o contato quer continuar na lista, sem chamada de compra |
| Frequência máxima | Sem turma: no máximo 1 mensagem de manutenção por trimestre [SUPOSIÇÃO], por e-mail. Com turma aberta no catálogo: o aviso de turma entra na régua de turma (P5 da estratégia de 26/10) e segue o teto D16. WhatsApp só com K2 e uma vez por turma, curto, com SAIR |
| O que mede | Entradas por origem; consentimentos F-B ativos; SAIR, descadastros e bloqueios por envio; respostas; cliques no aviso; inscrições e matrículas com origem "lista de espera" na turma seguinte; taxa de fechamento da lista contra a do lead frio, mesma coorte. Sem meta antes da linha de base |
| Como sai | Matricula (vira aluno e C3, depois C1); pede SAIR ou descadastro; não reconfirma na mensagem de manutenção (sai de F-B; pode seguir na carta se tiver F-A); curso muda de status para encerrado no catálogo (a Ufape avisa uma vez e fecha a lista) |
| Cuidados | Texto do consentimento diz a finalidade ("avisar quando houver nova turma deste curso"). Nenhum aviso promete data, vaga ou condição que o catálogo não traga. Se o status da turma estiver "verificar", "sem venda" ou "encerrado", o aviso não sai com chamada de compra |

### 2.3 [MOLDURA] Carta da área (newsletter da especialidade)

| Item | Definição |
|---|---|
| Objetivo | Entregar conteúdo útil de uma especialidade a quem escolheu recebê-lo, manter a Ufape lembrada entre turmas, levar à sessão ao vivo e abastecer a lista de espera. Não vende turma por conta própria |
| Quem entra | Contatos com K1 de F-A e interesse na área: C1, C2, C4 de interesse declarado, lista de espera com F-A, C3 (só conteúdo), indicadores que quiserem. Inscritos em sessão ao vivo que marcaram F-A. C5 não recebe a carta de especialidade, só institucional. Frio (C9) entra pela isca da área ou pelo formulário, com finalidade e política de privacidade |
| Conteúdo | Um tema por edição, assinado ou revisado por docente; perguntas do clínico; aviso da sessão ao vivo; resumo do episódio do podcast; um bloco curto de "como funciona a Pós" fixo. A edição da carta e os textos são do agente newsletter |
| Frequência máxima | 1 e-mail por mês por área com volume suficiente [CONFIRMAR volume mínimo]. Nunca no mesmo dia de outra campanha ao contato. Só e-mail |
| O que mede | Cliques por bloco; respostas; descadastro e denúncia por envio; novos consentimentos vindos da carta; inscritos na sessão com origem carta; matrículas somadas com origem carta. Abertura é só diagnóstico de entrega |
| Como sai | Descadastro. Sem clique, resposta ou visita pelo prazo de higiene [SUPOSIÇÃO: o N=180 dias da estratégia de 26/10], o contato recebe uma reconfirmação; sem resposta, sai da carta e fica só com o que tiver K1 de outra finalidade |
| Cuidados | Revisor docente obrigatório. Caso clínico só como tema, sem paciente, tutor ou clínica identificável. Sem afirmação de certificação ligada ao MEC. Marca comercial de parceiro em conteúdo clínico só com revisão (C7 do plano) |

### 2.4 [MOLDURA] Convite ao T2 (caso clínico ao vivo)

| Item | Definição |
|---|---|
| Objetivo | Encher a sessão de quem tem interesse real na área, registrar novos consentimentos e abrir conversas com o time de vendas. A gravação abastece o podcast, os cortes e a busca, sempre com aprovação |
| Quem entra no convite | C1, C2 (formados), C4 de interesse declarado, lista de espera, carta, C3 (convite a sessão, sem oferta de compra), indicadores. Quem ainda não está na base chega pela mídia paga, pelos parceiros e pelo orgânico, com formulário próprio e finalidade escrita. A abertura da sessão a não alunos é decisão da Ufape (UD3) |
| O que recebe | Até 1 convite, 1 lembrete e 1 mensagem de pós-sessão por sessão, por contato, e no máximo um canal por dia. WhatsApp só para lembrete curto, com K2, no horário comercial; e-mail para convite, programação e pós-sessão |
| Frequência máxima | No máximo 1 sessão anunciada por mês por contato [SUPOSIÇÃO]; os três toques cabem no teto D16 e cedem a vez às réguas com data |
| O que mede | Inscritos, presentes, novos consentimentos (por finalidade e canal), conversas no WhatsApp de vendas com origem "evento", matrículas somadas com origem "evento", cortes produzidos, SAIR e descadastros por envio. A taxa de presença sobre inscritos é um número somado, nunca por pessoa |
| Como sai | Pós-sessão: quem não tem F-A nem F-B recebe só o que for serviço (a entrega da gravação, se foi prometida na inscrição). Quem tem F-A segue na carta, quem tem F-B segue na lista. Quem pede SAIR sai de tudo. Se a Ufape cancelar o formato, o convite deixa de ser enviado e quem já se inscreveu é avisado como serviço. |
| Cuidados | Inscrição na sessão nunca exige aceitar campanha. O aceite de F-A e de F-B é separado e desmarcado. Gravação só é publicada com aprovação e com a regra de gravação da Ufape (UD3). Presença de aluno ou de ex-aluno em imagem ou voz exige autorização registrada (L8). Nenhuma menção de conduta de caso sem revisão docente |

### 2.5 [GASTRO] Preenchimento dos três programas

| Programa | Gastro |
|---|---|
| Lista de espera | A próxima turma de Gastroenterologia não está no catálogo; pela decisão 28 ela abre normalmente 3 a 4 meses depois de uma turma confirmada [CONFIRMAR data, número da turma e a interpretação] e o destino da prova de bolsa 68650 não está informado [CONFIRMAR]. Por isso a lista existe sem data e sem chamada de compra. Enquanto a turma em captação aceitar matrícula (até o 3º módulo, decisão 18), quem não fechou fica no P2 da estratégia de 26/10 e **não** entra na lista. A página da área com "avise-me" é a porta principal e ainda não existe (UD5, canal 2 do plano). Até lá, a entrada é pelo atendimento de vendas e pelas sessões ao vivo |
| Carta da área | Carta de Gastroenterologia Veterinária. Nome da carta a decidir [CONFIRMAR], sem inventar marca. Temas candidatos vêm do cronograma e do grupo de estudos 721 (vômito e diarreia crônica, hepatopatias, pancreatite, colangites felinas, enteropatias, conforme o plano). Revisor docente nomeado [CONFIRMAR, N9]. A coordenação é a voz principal; professores de áreas cruzadas (imagem, endocrinologia, nutrição, oncologia) ampliam a pauta |
| Convite ao T2 | Sessão com a Esp. Maria Carolina Pappalardo (coordenação, ficha 68606), tema de um módulo do cronograma. Depende de UD3 (o que são as "aulas abertas" 8, 15 e 19 e se aceitam não alunos, N4). Horas da coordenação [CONFIRMAR, PA3] |

---

## 3. Proposta de regra do programa de indicação (T1)

**Rascunho para a Ufape decidir. Nada aqui está aprovado, nada vai ao ar e nenhum benefício é prometido.** O benefício fica como opção a decidir, sem valor. Os trechos jurídicos são leitura de bom senso e precisam de conferência do jurídico da Ufape [CONFIRMAR].

### 3.1 [MOLDURA] Princípios, amarrados às regras do plano

| Regra do plano | Como a proposta a cumpre |
|---|---|
| D16 (teto) | O convite a indicar é campanha: entra no teto, sai só para quem tem K1 ou K2, no horário e na frequência permitidos |
| E1 a E4 | Só base com opt-in recebe o convite (E4). Convite vai a quem está engajado, para não gerar rejeição nem o erro 131049 da Meta (E1 e E2; texto exato na seção 13 do cmo-geral). SAIR ou descadastro encerra o convite em até 48 h (E3) |
| L5 (indicação) | Quem indica manda o link ou o código. A Ufape nunca recebe telefone, e-mail ou nome de terceiro por meio do indicador, nem importa lista de contatos dele |
| Sem promessa não aprovada | Nenhuma peça, mensagem ou resposta do time cita benefício antes da aprovação formal da regra (regra C8 do plano do cmo de 29/10/2026 e auditorias/conformidade-educacional.md, preço e condições) |
| CDC | A oferta e a publicidade do programa são claras, completas e verdadeiras. O que for anunciado vincula a Ufape; não há "condição escondida". O direito de arrependimento do indicado continua valendo e a regra diz o que acontece com o benefício nesse caso [CONFIRMAR com jurídico] |

### 3.2 [MOLDURA] Regra proposta (texto-base para a Ufape editar)

**1. Quem pode indicar (indicador).**
- Contato de C1, C2, C3 ou C4, maior de 18 anos, com cadastro ativo, com K1 ou K2, que aceitou o convite a indicar.
- Aluno em curso pode indicar (é o mais engajado), mas não recebe oferta de compra de outro curso por isso.
- Não podem indicar, salvo decisão da Ufape: colaboradores da Ufape, do time de vendas e docentes (conflito de interesse) [CONFIRMAR]. Quem não é indicador por regra pode seguir compartilhando conteúdo normalmente.

**2. Quem pode ser indicado.**
- Médico veterinário formado (público da Pós, contexto/pos-graduacao.md), que nunca se matriculou na turma ou no curso indicado.
- Não é aluno atual da própria turma e não tem contato aberto com o time de vendas há mais do que um prazo de carência [CONFIRMAR prazo]. Lead que já está em negociação não vira indicação para efeito de benefício.
- O indicado se cadastra no próprio formulário, com finalidade e política de privacidade, ou fala com o time de vendas dizendo o código. Sem esse ato dele, a Ufape não conhece o indicado.

**3. Como indicar.**
- Link ou código pessoal por indicador, gerado pelo CRM com UTM no padrão do cmo (`utm_content=indicacao-<código>`).
- É proibido: disparo em massa pelo indicador, lista de contatos enviada à Ufape, postagem em grupo de WhatsApp ou comunidade contra a regra do grupo, divulgação de preço, condição ou benefício diferente do texto da regra publicada pela Ufape, uso de perfil falso ou de dado de terceiro. Descumprimento suspende o indicador e a Ufape pode negar o benefício [texto jurídico a revisar].

**4. Gatilho e atribuição.**
- O evento que conta é a **matrícula do indicado, isto é, a 1ª mensalidade paga** (decisões 25 e 26), na turma elegível. Inscrição paga não basta.
- Atribuição pelo primeiro registro válido do código no cadastro do indicado, dentro de uma janela de atribuição [CONFIRMAR duração]. O CRM registra a origem "indicação".
- Se mais de um indicador reivindicar o mesmo indicado, vale o primeiro registro. Se o indicado exerceu o direito de arrependimento ou desistiu antes de concluir o pagamento, o benefício não é concedido ou é revertido na forma da regra [CONFIRMAR com jurídico].

**5. Elegibilidade da turma e do curso.**
- Só turmas com status "aberto" no catálogo, no curso e na praça definidos pela Ufape. Turma "verificar", "sem venda" ou "encerrado" não entra.
- Interação com bolsa e com o desconto de aluno e ex-aluno (20% em Pós, simpósios e workshops, decisão 28): a ficha da prova diz que a bolsa não é acumulativa; a Ufape decide se o benefício de quem indica acumula, não acumula ou substitui [CONFIRMAR, UD1]. O indicado não tem desconto próprio (decisão 28) e usa as condições normais, inclusive os 20% se for aluno ou ex-aluno de Pós.

**6. Benefício (opções a decidir; nenhum valor sugerido).**

| Opção | O que é | Prós | Riscos |
|---|---|---|---|
| A. Reconhecimento sem valor | agradecimento, acesso a conteúdo da área ou à sessão ao vivo, sem custo para a Ufape | baixo custo, simples, sem implicação de preço | pode não motivar; o conteúdo oferecido precisa existir de verdade |
| B. Benefício ao indicador | condição ou item definido pela Ufape, com regra escrita | motiva quem tem rede | custo por matrícula; precisa caber no teto de custo por matrícula do cmo; risco de indicação por interesse financeiro |
| C. Benefício ao indicado | fora: a Ufape não tem desconto para o indicado (decisão 28) | não se aplica | o indicado usa as condições normais, inclusive os 20% de aluno ou ex-aluno de Pós |
| D. Benefício aos dois | combinação de B e C | maior estímulo | maior custo e maior risco de regra confusa |

A Ufape decide: se há benefício, qual opção, quem paga, qual o valor e a forma [CONFIRMAR], (sem condição ao indicado, decisão 28). O benefício nunca é sorteio nem prêmio de resultado incerto, para não criar outra obrigação regulatória [CONFIRMAR com jurídico]. Qualquer benefício com valor vira regra com público, prazo, validade e condição escritos antes de ser anunciado.

**7. Prazo, limites e encerramento.**
- Vigência e limite de indicações por indicador, por turma e por ano: a Ufape define [CONFIRMAR]. A regra escrita traz prazo e validade do benefício.
- Encerramento: por comunicado, com antecedência combinada, honrando os benefícios já concedidos dentro da regra. Sem retroatividade.

**8. Privacidade (LGPD e L5).**
- O indicador só vê que o benefício foi concedido ou não. A Ufape não informa nome, contato ou situação de matrícula do indicado sem o consentimento dele.
- Dados do indicador e do indicado ficam no CRM; a squad só lê números somados (L1).
- O convite a indicar vai só a quem tem K1 ou K2; o indicado que pede SAIR sai de tudo e o indicador não é avisado.
- O indicado não precisa saber quem o indicou para se cadastrar, e pode recusar sem consequência.

**9. Anti-abuso e conflito.**
- Autoindicação, indicação cruzada em troca de benefício e indicação de quem já era lead são vetadas por regra de atribuição.
- Time de vendas registra "como conheceu" e o código, sem comissão por indicação ao indicador [CONFIRMAR se há comissão ao vendedor].

**10. Comunicação do programa.**
- Nenhum texto sai antes da aprovação humana da regra e do benefício. Todo texto de convite carrega saída simples e remete à regra completa.
- A regra completa fica publicada na página do programa e é a única fonte do que o time pode dizer.

### 3.3 [MOLDURA] O que o T1 mede e como desfaz

- **Mede (somado, sem meta antes da linha de base):** convites enviados, cliques no link ou código, cadastros de indicados, inscrições e matrículas com origem "indicação", taxa de fechamento do indicado contra a do lead pago na mesma turma, SAIR, descadastros e bloqueios por convite, indicadores ativos.
- **Desfaz:** encerrar por comunicado, honrando benefícios dentro da regra (como no plano, PA2).

### 3.4 [GASTRO] Preenchimento para o piloto

- **Quem indica no piloto:** ex-alunos das turmas I a VIII (C1) e alunos de áreas onde a coordenação também ensina (C3, por exemplo 68608, quando a turma começar). Indicados: clínicos de pequenos animais que atendem casos gastrointestinais. Tamanho de cada grupo e consentimento: [CONFIRMAR, UN1].
- **Turma elegível:** a 68606, enquanto a Ufape aceitar matrícula (até o 3º módulo, decisão 18), e as próximas turmas do curso quando existirem no catálogo.
- **Benefício:** nenhuma opção está pré-escolhida. O benefício, se houver, precisa conviver com a regra "bolsa não acumulativa" das provas e com o desconto de 20% de ex-aluno (decisão 28) [CONFIRMAR, UD1].
- **Não aplicar** a indicação a produtos de Livres ou a provas de bolsa neste piloto, salvo decisão da Ufape.
- **Hipótese a testar (SUPOSIÇÃO):** o indicado fecha mais do que o lead frio (T1 do plano). O teste só tem leitura se o campo "origem" e a UTM de indicação existirem antes do primeiro convite (M-A e M-B do plano).

---

## 4. Métricas e ritual

### 4.1 [MOLDURA]

| Programa ou círculo | Principais números somados | Fonte |
|---|---|---|
| Segmentos C1 a C5 | base com consentimento por canal e finalidade; envios por círculo; cliques, respostas, SAIR, descadastros e bloqueios por envio | CRM, ferramenta de e-mail e de WhatsApp |
| Lista de espera | entradas por origem; consentimentos F-B ativos; matrículas com origem "lista" | CRM |
| Carta da área | cliques por bloco, respostas, descadastro e denúncia por envio, novos consentimentos | ferramenta de e-mail |
| Convite ao T2 | inscritos, presentes, novos consentimentos, conversas de venda com origem "evento" | plataforma de transmissão, CRM |
| Indicação (T1) | convites, cadastros de indicados, matrículas com origem "indicação" | CRM, UTM |
| Resultado | matrículas por círculo de origem; taxa de fechamento por círculo, mesma coorte | CRM |

Regras de leitura: matrícula antes de lead; abertura só como diagnóstico; nenhuma decisão com menos de 2 envios do mesmo programa; as 4 primeiras semanas de leitura viram a linha de base; nenhuma meta de taxa antes disso [CONFIRMAR].

Regras de parada (valem desde o primeiro envio): SAIR, bloqueios e denúncias acima do dobro da média das 4 semanas anteriores pausam o programa [SUPOSIÇÃO]; queda de entrega de e-mail para o programa e roda a higiene; rebaixamento de qualidade de template ou de número na Meta pausa o WhatsApp de campanha (se houver API) [regra da plataforma, conferir a política vigente].

### 4.2 [MOLDURA] Ritual

Estes programas entram na **revisão mensal já existente** da estratégia de relacionamento de 26/10/2026 (seção 7.3). Nenhuma data nova. Perguntas adicionais: qual círculo trouxe matrícula e qual só trouxe SAIR; algum contato passou do teto D16 por causa dos programas permanentes; a lista de espera está crescendo com consentimento válido; qual edição da carta gerou conversa; o T2 trouxe base nova; o T1 trouxe fechamento maior que o do lead frio.

### 4.3 [GASTRO]

- Primeira leitura útil: participação de cada círculo nas matrículas da 68606 (pede o campo "origem" preenchido desde já).
- O T2 e a carta de Gastroenterologia só têm leitura de resultado depois de existir alguma turma de destino no catálogo. Antes disso, medem base e conversa.

---

## 5. O que precisamos da Ufape

### 5.1 Decisões

| # | Decisão | Trava |
|---|---|---|
| UD1 | Benefício da indicação: se há, qual opção, valor, quem paga, vigência, limite e acúmulo com bolsa e com ex-aluno | T1 inteiro |
| UD2 | Regra de desconto de aluno e ex-aluno de Pós: respondida pela decisão 28 (20% em Pós, simpósios e workshops) | (respondido) |
| UD3 | Abrir sessão ao vivo a não alunos; regra de gravação | T2 |
| UD5 | Página da área com "avise-me" | lista de espera |
| UD8 | Quem aprova envio em massa e depoimentos (tabela vazia em ufape-geral.md) | tudo |
| D-N1 | Textos e caixas de consentimento das finalidades F-A e F-B, aprovados pelo encarregado de dados | todos os programas |
| D-N2 | Se quem cursou e não concluiu, o inadimplente e o cancelado podem receber campanha | C1 e C3 |
| D-N3 | Colaboradores, vendedores e docentes podem indicar? Há comissão de venda por indicação? | T1 |
| D-N4 | Prazo de carência para lead em negociação não virar indicação; janela de atribuição | T1 |
| D-N5 | Prazo de higiene da base (SUPOSIÇÃO de 180 dias da estratégia de 26/10) | todos |
| D-N6 | Nome da carta da área; revisor docente nomeado | carta |
| D-N7 | Confirmar com o jurídico a leitura de CDC deste arquivo (oferta, arrependimento, benefício) | T1 |

### 5.2 Dados (só números somados)

- UN1. Tamanho de C1 a C5 e quantos têm K1 e K2, por finalidade.
- UN2. Origem das matrículas das turmas anteriores do curso.
- UN3. Data e número da próxima turma (abre normalmente 3 a 4 meses depois de uma turma confirmada, decisão 28); destino da prova 68650.
- UN6. Se a Graduação já tem egressos (N11).
- UN8 (código novo desta estratégia; o UN5 do plano é regra do estágio e do grupo de casos). Quantos contatos hoje têm campo de interesse por área.

### 5.3 Acessos e configurações (pela própria Ufape, sem chave no chat)

- UA1. CRM, ferramenta de e-mail e ferramenta de WhatsApp (API ou aplicativo); campos de consentimento por canal e finalidade; campo "círculo", "origem" e "indicador"; geração de código de indicação com UTM.
- UA6 (código novo desta estratégia; o UA2 do plano é leitura de Search Console, analytics, Meta Business e Google Ads). Templates aprovados pela Meta, se a Ufape usa a API (convite curto, lembrete, aviso de turma), com "responda SAIR".
- UA4. Base legal registrada pelo encarregado de dados para marketing à base de ex-alunos e para listas em plataformas de anúncio (N12). Em parte respondido pela decisão 28: a base tem consentimento e já é trabalhada por mídia paga, então K5 fica liberado para essa base; o registro formal segue [CONFIRMAR].
- UA5 (código novo desta estratégia, ligado à decisão UD4 do plano). Uso dos grupos de estudo que já existem (decisão 28), como o 721, como comunidade de ex-alunos, sem expor telefone (L7).

### 5.4 Aprovação humana pedida (nada roda antes)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AR1 | Aprovar os segmentos C1 a C5 e C8 e a regra de prioridade (seção 1) | base para toda campanha da área | sem custo | cada contato recebe uma coisa por vez | voltar à segmentação anterior |
| AR2 | Aprovar o desenho dos três programas (seção 2) | mantém a base viva entre turmas | horas do time [CONFIRMAR] | base da área com consentimento | pausar o programa no CRM |
| AR3 | Decidir o benefício e a regra do T1 (seção 3) | sem regra aprovada, não há programa | benefício [UD1] | indicações medidas | encerrar por comunicado, honrando o já concedido |
| AR4 | Autorizar os pedidos UN1, UN2, UN3, UN6 e UN8 e UA1, UA4, UA5 e UA6 | sem eles não há medição por círculo | sem custo direto | linha de base em 4 semanas | não se aplica |

---

## 6. Auditorias aplicadas

**auditorias/07-email-e-whatsapp.md**
- [x] Consentimento e descadastro no desenho (K1 a K5, finalidades F-A e F-B, saída universal). Funcionamento real [CONFIRMAR].
- [x] Cada programa tem um objetivo, regra de saída e frequência máxima.
- [x] Segmentos recebem mensagem relevante à etapa (seção 1).
- [x] Métricas por clique, resposta, conversão, SAIR e bloqueio; abertura só como diagnóstico.
- [x] WhatsApp só em horário comercial, com regra explícita para lembrete de sessão fora do horário; frequência humana; template Meta quando houver API.
- [ ] Registro real dos resultados de cada envio: depende do CRM [CONFIRMAR].

**auditorias/conformidade-educacional.md**
- [x] Dados de curso só do catálogo (68606: Pós-graduação em Gastroenterologia Veterinária, São Paulo, semipresencial, turma IX). Nenhum preço citado; quando citado, vai pelo texto-padrão.
- [x] Nenhuma frase de certificação ligada ao MEC.
- [x] Nenhum benefício, desconto ou bolsa afirmado além do desconto de 20% de aluno e ex-aluno de Pós (decisão 28); o resto como opção a decidir, com público, prazo e validade a escrever; sem desconto para o indicado.
- [x] Sem urgência falsa; nenhuma data neste arquivo.
- [x] LGPD: só números somados; consentimento por canal e finalidade; sem lista comprada ou importada; L5 e L6 respeitados.
- [ ] Revisão jurídica do trecho de CDC (seção 3): pendente (D-N7).
- [x] Sem travessão nem meia-risca (conferido na escrita; a busca dos caracteres é do qa).
- [x] The Growth Hub não é citada como "agência".

**Resultado:** pronto para o qa-de-marketing e para a aprovação humana. Próximo agente: newsletter.

---

## Fatos (com fonte)

- 68606: Pós-graduação em Gastroenterologia Veterinária, São Paulo, semipresencial, turma IX, aberto (catálogo, seção 2). Preço e condições (30x de R$ 1.180,00; R$ 35.400,00; inscrição de R$ 250,00) estão no catálogo e na decisão 23, e não são usados em regra nenhuma deste arquivo.
- Matrícula é a 1ª mensalidade paga; inscrição é o valor de R$ 250,00 (decisões 23, 25 e 26).
- A Ufape aceita matrícula até o 3º módulo (decisão 18); turma mínima de 15 (decisões 11 e 16).
- Nenhuma campanha nova aponta para a página 623 até a correção (decisão 13).
- A prova 68650 é de Gastroenterologia, São Paulo, e não tem turma de destino informada (catálogo, seção 3; contexto/pos-graduacao.md).
- Teto D16 e regras E1 a E4 (decisão 17 e plano do cmo de 29/10/2026).
- L1 a L8, círculos C1 a C9, F1, F2, F10, T1 e T2, UD1 a UD8, UN1 a UN7, UA1 a UA4 (plano do cmo de 29/10/2026).
- A bolsa das provas é não acumulativa e intransferível (contexto/pos-graduacao.md, regras das fichas).

## [SUPOSIÇÃO]

- Orçamento do programa permanente de no máximo 1 e-mail e 1 WhatsApp por semana por contato, para deixar espaço às réguas de turma.
- 1 mensagem de manutenção por trimestre na lista de espera sem turma; 1 sessão ao vivo anunciada por mês por contato; 1 carta por mês.
- Prazo de higiene de 180 dias, herdado do N=180 da estratégia de 26/10/2026.
- Cancelado e inadimplente sem campanha, só serviço.
- Quem cursou e não concluiu fora de C1 por padrão.
- A Graduação em Medicina Veterinária ainda sem egressos (N11).
- O indicado fechar mais do que o lead frio (hipótese do T1).
- Gatilho de parada: SAIR, bloqueios e denúncias acima do dobro da média das 4 semanas anteriores.

## [CONFIRMAR]

- Tamanho de cada círculo e consentimento por canal e finalidade (UN1); origem das matrículas anteriores (UN2).
- Data e número da próxima turma de Gastroenterologia; destino da prova 68650 (UN3).
- Campos do CRM para consentimento, círculo, origem, indicador e interesse por área; ferramentas de CRM, e-mail e WhatsApp; se há API da Meta (UA1, UA6).
- Registro formal da base legal (UA4); o consentimento para novas oportunidades existe (decisão 28).
- Textos de consentimento F-A e F-B; aprovadores; revisor docente; nome da carta.
- Benefício de quem indica, vigência, limite e acúmulo com bolsa e com os 20% de ex-aluno (UD1); desconto de ex-aluno respondido pela decisão 28.
- Abertura da sessão ao vivo a não alunos e regra de gravação (UD3); horas da coordenação.
- Se colaboradores, vendedores e docentes podem indicar; se há comissão de venda.
- Leitura jurídica do CDC (oferta, arrependimento, benefício) e se o benefício pode ser sorteio ou prêmio (a proposta o veta).
- Texto exato de E1 e E2 (seção 13 do cmo-geral), que não reabri.

## Fontes

- cmo-pos-2026-10-29-plano-estrategico-divulgacao-gastro.md (seções 3, 4, 6, 7, 8 e 9; encomendas da cadeia).
- estrategia-de-relacionamento-pos-2026-10-26.md (seções 0 a 7: papéis, regras de consentimento, segmentos S1 a S12, fila D2, limites, métricas e ritual).
- docs/execucao-2026-10-26.md (decisões 11, 13, 16, 17, 18, 23, 25 e 26).
- contexto/ufape-geral.md, contexto/pos-graduacao.md, contexto/catalogo-de-cursos.md.
