# Formulário e CTA final das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), encomenda F5 da onda 2

- **Agente:** otimizador-de-cta (departamento 08, Conversão)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** F5 do plano do CMO em versão 2 (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md, seção 10, linha F5). O plano previa o nome otimizador-de-cta-pos-2026-11-17.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Formato:** campos `formulario` e `cta_final` de templates/pagina-da-turma.md (tipo pos), uma seção por turma com o código no título.
- **Status:** rascunho para o qa-de-marketing (auditorias/08-conversao.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago a partir deste arquivo. Publicar as páginas, ligar o formulário ao CRM e montar o teste são ações humanas ou da plataforma, depois da aprovação.
- **Consumidores:** qa-de-marketing (F13), editor e time do site (montagem do formulário e do teste), gestor-de-midia (conferência de 04/12), desenho-de-experimentos (próximo agente).
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 14, 16, 18 e 20)
  - contexto/ufape-geral.md (voz da marca, contatos oficiais; não traz o endereço da política de privacidade)
  - contexto/pos-graduacao.md
  - contexto/catalogo-de-cursos.md (linhas 1 a 180, que incluem a seção 2 com 657, 341, 289, 68615 e 333; única fonte dos dados de curso)
  - Fichas inteiras: contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md, 341-pos-graduacao-em-medicina-interna-equina.md, 289-pos-graduacao-em-cardiologia-veterinaria.md, 68615-pos-graduacao-em-patologia-clinica.md, 333-pos-graduacao-em-citopatologia-veterinaria.md (nenhuma traz política de privacidade)
  - templates/pagina-da-turma.md (campos `formulario` e `cta_final`; regra de texto sem número)
  - auditorias/conformidade-educacional.md e auditorias/08-conversao.md
  - .claude/skills/hipotese-de-teste/SKILL.md
  - F3: saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md (inteiro: botão provisório "Quero me inscrever", frase de apoio provisória, `cta_final` por turma, checklist de rastreamento)
  - F4: saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda2.md (inteiro; só confere que nada aqui entra em campo de SEO)
  - F2: saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda2.md (inteiro: chamada principal, variações e objeções por turma)
  - Plano do CMO: saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (inteiro)
- **Não aberto:** faculdade.ufape.com.br; as saídas do qa-de-marketing; .claude/commands; nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum docente é nomeado.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape ou a plataforma tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com a origem.

---

## 0. Como ler este arquivo e blocos comuns às 5 turmas

### 0.1 Regras aplicadas

1. **Texto da página sem número, preço, data, local nem nome de docente.** Vale para tudo o que está em bloco de citação (">") ou entre aspas: é o texto que vai para a página. Nenhum algarismo, ordinal, numeral romano ou número por extenso. Notas, contagens, datas do teste e códigos ficam fora desses blocos e não vão para a página.
2. **Fora de todo texto de página:** "MEC", certificado, certificação, reconhecida, bolsa, prova de bolsa, desconto, promoção, urgência ("últimas vagas", "só até", contador, "corra"), superlativo da ficha, promessa de emprego, renda ou resultado clínico, valor da inscrição (U11).
3. **Travas por turma:** 657 sem pré-requisito e sem prova ou título de Especialista (U10, C14); 341 sem promoção e sem local da prática (OU10, OU11); 289 sem cidade (CP1); 333 sem "coordenação" (OU12) e sem nada depois do início (OU3).
4. **Regra do 3º módulo e turma mínima:** só como dado da turma (OU14, A12). Nenhum botão, título ou apoio fala de prazo de entrada.
5. **Botão que diz a ação real.** O formulário não matricula nem cobra: ele pede um retorno do time de vendas. O texto recomendado diz isso. "Quero me inscrever" fica como variante de teste, não como texto recomendado, porque promete mais do que o clique entrega (auditorias/conformidade-educacional.md, item de página de destino que entrega o que a peça promete) [SUPOSIÇÃO: o formulário é só de contato, sem pagamento].
6. **Uma chamada principal por página** (auditorias/08-conversao.md): hero, formulário e `cta_final` pedem a mesma ação e usam o mesmo texto de botão em cada braço do teste. WhatsApp continua chamada secundária, com o número da praça vindo do dado (Goiânia em 289), como na F3.
7. **Nada inventado:** nenhuma prova nova. Ao redor do botão só entram provas que já estão na página (cronograma, FAQ, `docentes` como dado). Sem depoimento, nota, selo ou avaliação, porque nenhum existe autorizado em mãos.

### 0.2 Inventário de CTAs (método, passo 1)

| CTA | Onde | Texto atual | Ação que pede | Situação |
|---|---|---|---|---|
| Botão do hero | topo da página | "Quero me inscrever" (provisório da F3) | rolar até o formulário | trocar pelo texto do braço do teste (ver 0.4) |
| Botão do formulário | `formulario` | "Quero me inscrever" (provisório da F3) | enviar nome, WhatsApp e e-mail | reescrito nas seções 1 a 5 |
| Botão do `cta_final` | fim da página | "Quero me inscrever" (provisório da F3) | rolar ou abrir o formulário | reescrito nas seções 1 a 5 |
| WhatsApp | botão fixo no celular e link | texto não definido pela F3 [CONFIRMAR] | abrir conversa com vendas da praça | secundário; sem mudança aqui |
| Política de privacidade | abaixo do botão | "política de privacidade" (F3) | abrir a política | endereço [CONFIRMAR] |
| Link-ponte 68615 e 333 | `faq` | nome da outra turma (F2) | abrir a outra página | sem mudança; ver 0.7 |
| CTA nas páginas no ar hoje | fichas de 26/10/2026 | "COMPRAR"; em 289 e 68615 "PROVA DE BOLSA: Clique aqui"; em 657 "prova de Especialista: Clique aqui" | comprar direto; abrir prova | fora desta entrega: os dois últimos saem pelo OB1 (decisão 14 e C14) |

### 0.3 Formulário: o que se pede e o que não se pede

**Campos (iguais nas 5 turmas):**

| Campo | Rótulo | Obrigatório | Por que é necessário | Mensagem de erro |
|---|---|---|---|---|
| Nome | Seu nome | sim | o time de vendas precisa saber como chamar o contato | Digite seu nome. |
| WhatsApp | WhatsApp com DDD | sim | canal do retorno do time de vendas [SUPOSIÇÃO: o retorno é por WhatsApp] | Confira o número do WhatsApp com DDD. |
| E-mail | E-mail (opcional) | não | só para quem quer receber mensagens por e-mail; sem ele o retorno acontece pelo WhatsApp [SUPOSIÇÃO: o CRM aceita lead sem e-mail, CONFIRMAR] | Confira o e-mail. |

Dica dentro do campo: só o WhatsApp leva "DDD e número". Os outros dois ficam sem exemplo, para a tela não carregar número.

**Caixas de aceite (opcionais, nunca pré-marcadas), uma por canal e finalidade (regra E4 do plano geral):**

> Quero receber mensagens sobre esta turma e sobre cursos da mesma área por WhatsApp.
>
> Quero receber mensagens sobre esta turma e sobre cursos da mesma área por e-mail.

A caixa de e-mail só aparece ou só vale se o campo de e-mail estiver preenchido. O retorno do time de vendas pedido no formulário não depende de nenhuma das duas caixas. Quem não marca uma caixa recebe só o retorno pedido e não entra nas listas de campanha (S2 e S3) daquele canal (encomenda F10).

**Campos de rastreamento (ocultos, sem dado pessoal):** código da turma, UTM (preservadas do clique ao CRM, regra 12 do plano) e `cta_variante` (c, v1 ou v2). Ver 0.5.

**Não se pede, por não ser necessário ao retorno:** CPF, data de nascimento, cidade e estado (o campus é dado da turma; em 289 a cidade não entra, CP1), CRMV, ano de formatura, especialidade atual, pergunta de elegibilidade (em 657 seria pré-requisito disfarçado, U10), interesse em bolsa (decisão 14), orçamento, "como conheceu" (vem da UTM). Quem decidir pedir qualquer um deles precisa justificar a necessidade antes.

**Mensagem de erro de envio (comum):**

> Não conseguimos enviar seus dados agora. Tente de novo ou fale com o time pelo WhatsApp desta página.

**Frase de risco abaixo do botão (comum):**

> Enviar seus dados não gera cobrança nem compromisso de inscrição.

[SUPOSIÇÃO: o formulário não dispara pagamento. O time do site confirma antes de publicar; se houver cobrança em alguma etapa, a frase sai.]

**Frase de finalidade e link da política de privacidade (LGPD, comum):**

> Usamos seus dados para o time de vendas da Faculdade Ufape retornar sobre esta turma e orientar sua inscrição. Se você marcar as opções acima, também enviamos mensagens sobre esta turma e sobre cursos da mesma área, e você pode sair quando quiser. Veja como tratamos seus dados na [política de privacidade]([CONFIRMAR: endereço da política de privacidade da Faculdade Ufape]).

O endereço da política não está em contexto/ufape-geral.md nem em nenhuma das 5 fichas: fica [CONFIRMAR]. Sem o endereço o formulário não passa em conformidade-educacional (item de finalidade e link). Base legal, retenção, compartilhamento com a ferramenta de CRM e de WhatsApp e contato do encarregado são da política, não da tela [CONFIRMAR com quem responde pela LGPD na Ufape].

### 0.4 Botão: o texto recomendado e as duas variantes de teste

| Braço | Texto do botão | Caracteres | Papel |
|---|---|---|---|
| C (recomendado e controle) | Quero receber o retorno do time | 31 | diz o que acontece depois do clique |
| V1 | Quero tirar minhas dúvidas | 26 | reduz o compromisso percebido |
| V2 | Quero me inscrever | 18 | suspenso: só entra no teste se o clique levar à inscrição de fato; com o formulário de contato, promete mais do que entrega (conformidade, página de destino) [CONFIRMAR com o time do site] |

Contagem feita letra por letra, espaços inclusos. O mesmo texto vale para o botão do hero, do formulário e do `cta_final` em cada braço. A F3 deixou "Quero me inscrever" no hero: como este arquivo não altera o arquivo da F3, o editor troca o botão do hero pelo texto do braço sorteado (pedido no fim de cada seção) [SUPOSIÇÃO: meta de até 32 caracteres para caber em uma linha no celular, que é só uma meta de leitura, o template não fixa limite].

Por que o controle não é "Quero me inscrever": quem clica espera começar a inscrição e encontra um pedido de contato. O texto honesto reduz o clique enganado e a frustração do primeiro retorno. Se V2 vencer, a mensagem de confirmação abaixo já explica a etapa, para a promessa não ficar maior do que a entrega.

### 0.5 Regras comuns do teste de botão (skill hipotese-de-teste)

1. **Uma mudança por teste:** só o texto do botão, nas 3 posições da mesma página e em todas as 5 páginas. Nada mais muda.
2. **Sorteio por visitante,** com divisão igual entre C e V1 (V2 suspenso, seção 0.4), e o mesmo braço nas 5 páginas para quem visitar mais de uma. Isso importa em 68615 e 333, que disputam o mesmo segmento (A11) [SUPOSIÇÃO: a plataforma faz o sorteio por cookie, CONFIRMAR com o time do site].
3. **Métrica principal:** taxa de envio do formulário (leads dividido por visitantes da página). **Métrica de qualidade:** inscrição paga por lead, medida separada da matrícula paga, só números somados (decisão 16). A 1ª mensalidade paga não decide este teste: o ciclo dela é mais longo que a janela [SUPOSIÇÃO].
4. **Evento:** `generate_lead` com o parâmetro `cta_variante`, e o mesmo valor gravado no lead do CRM; `click_whatsapp` sem o parâmetro (a F3 sugere os nomes dos eventos [SUPOSIÇÃO]). Sem dado pessoal em nenhum parâmetro.
5. **Janela:** de segunda 04/01/2027 a domingo 07/02/2027, 5 semanas inteiras. Não atravessa o fim de ano sem campanha (21/12 a 03/01), o Carnaval (08 a 10/02) nem os cortes da 1ª mensalidade (11/02 em 657; 18/02 em 341, 289 e 68615; 25/02 em 333), todos do plano do CMO. De 07/12 a 03/01 as páginas rodam só com o controle, para formar a linha de base.
6. **Quantidade de leads:** não há CPL nem visita histórica. O plano estima CPL de R$ 4,00 a R$ 18,00 e verba de R$ 2.000,00 por turma, o que dá cerca de 111 a 500 leads por turma no ciclo inteiro, só da mídia paga e antes de dividir em 3 braços (conta deste agente, a partir do plano). Por isso o teste não se decide por turma: C contra V1 e C contra V2 são lidos com as 5 turmas somadas, e o resultado por turma vale só como direção. O desenho-de-experimentos fixa o mínimo de leads por braço antes de começar e decide se corta para 2 braços.
7. **Regra de decisão, escrita antes do teste** [SUPOSIÇÃO: limiares provisórios, o desenho-de-experimentos confirma ou troca]:
   - V vence se, nas 5 turmas somadas e com o mínimo de leads por braço atingido, a taxa de envio ficar pelo menos 20% acima da do controle (relativo) **e** a inscrição paga por lead não ficar mais de 10% abaixo da do controle (relativo).
   - Se vencer: vira o botão das 5 páginas e passa a ser o controle das turmas seguintes; o resultado é registrado.
   - Se empatar ou a amostra não chegar ao mínimo: fica o controle, e o registro diz "sem evidência".
   - Se perder: descartar e registrar o motivo.
   - Se um braço aumentar leads e derrubar a inscrição paga por lead, o ganho de volume não vale: fica o controle.
8. **O que não muda durante a janela:** texto da página, ordem das seções e criativos. A diária pode mudar na revisão de ritmo de 04/01 e 18/01; o gestor-de-midia avisa, e o teste lê só a taxa por visitante, que a diária não altera [SUPOSIÇÃO].
9. **Sem ferramenta de teste no site** [CONFIRMAR]: alternativa é trocar de braço por semana, o que é menos confiável e não separa o efeito do botão do efeito da semana.

### 0.6 Mensagem de confirmação (estrutura comum)

Título: "Recebemos seus dados." Depois, uma frase por turma sobre o que o time responde (nas seções 1 a 5), mais as linhas comuns abaixo.

Linhas comuns, depois da frase da turma:

> Nenhuma cobrança foi feita. Enquanto isso, você pode rever o cronograma e as condições nesta página. Se preferir falar agora, use o botão de WhatsApp desta página.

Linha extra só para quem marcou a caixa de WhatsApp:

> Você aceitou receber mensagens por WhatsApp. Para parar, responda SAIR a qualquer mensagem.

Linha extra só para quem marcou a caixa de e-mail:

> Você aceitou receber mensagens por e-mail. Para parar, use o link de descadastro no fim de cada e-mail.

O prazo do retorno não vai no texto: [CONFIRMAR prazo e horário de atendimento do time de vendas]. Se a Ufape confirmar, o editor acrescenta uma frase sobre o prazo, sem número no texto, por exemplo "O retorno acontece em dia útil, no horário de atendimento". Uma confirmação automática por WhatsApp ou e-mail seria envio e só existe com o aceite da caixa e com o pedido OB2 do plano (nada é escrito aqui).

### 0.7 Posicionamento e prova ao redor do botão (método, passo 4), regras comuns

- **Posição:** o botão do hero rola até o formulário; o formulário fica depois de `faq`; o `cta_final` fecha a página e leva de volta ao formulário. No celular, botão fixo do WhatsApp como secundário (F3), nunca dois botões primários.
- **Embaixo do botão, nesta ordem:** frase de risco, frase de finalidade e link da política (0.3).
- **Prova que pode ficar perto:** o link para a pergunta "E se a turma não fechar?" do `faq` (fonte: ficha, aviso de passagem e hotel e reembolso da inscrição), o cronograma (`matriz`) e a seção `docentes` como dado. Em 341 e 333 o link vai só para o aviso de passagem e hotel, porque o texto de reembolso de 341 está truncado e 333 não pode falar de docentes até a OU12 (ver seções).
- **Não pôr perto do botão:** selo ou frase de MEC e de certificação (seção `certificacao` oculta até a regulação), nota ou avaliação, depoimento (nenhum autorizado em mãos), contador de vagas, "últimas vagas", bolsa, desconto, valor da inscrição.
- **Sem "sem compromisso" como selo:** a ideia aparece só na frase de risco, em linguagem simples, e só se o time do site confirmar que o formulário não cobra.

---

## 1. Seção 657: Pós-graduação em Anestesiologia Avançada

### 1.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Anestesiologia Avançada
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, os módulos de prática guiada e as condições da turma, e orientar a inscrição.

- **Campos:** Seu nome (obrigatório); WhatsApp com DDD (obrigatório); E-mail (opcional). Duas caixas de aceite opcionais, desmarcadas (texto na seção 0.3).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Não pedir:** nada que pergunte se a pessoa é anestesista ou atua na área (U10).

### 1.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, os módulos de prática guiada e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da seção 0.6. Pergunta sobre quem pode entrar vai para a secretaria; resposta do time: "Vou confirmar com a secretaria quem pode entrar nesta turma e te retorno" (F2).

### 1.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma e os módulos de prática guiada antes de decidir.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre os módulos de prática guiada e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

O título é a chamada principal da F2, sem mudança. O apoio faz a ponte entre o "veja" e o botão.

### 1.4 Variações de botão e hipóteses (hipotese-de-teste)

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** 657 tem o maior total das 5 turmas (catálogo) e a página não diz quem pode entrar (U10, `para_quem` oculta). Quem hesita em "pedir retorno de vendas" tende a aceitar "tirar dúvidas", porque o pedido parece menor [SUPOSIÇÃO]. Risco: leads menos decididos e mais carga para o time.
- **Tempo mínimo:** a janela comum (04/01 a 07/02/2027). A mídia de 657 só sobe em 14/12 e com PP7, então a janela cobre toda a fase de conversão até o corte de 11/02.
- **Se ganhar / se perder:** regra da seção 0.5, item 7. Em 657, se ganhar em volume e perder em inscrição paga por lead, fica o controle.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever", o texto provisório da F3. Nada mais muda.
- **Efeito previsto:** menos envios no tráfego frio e igual ou mais no remarketing e na busca de marca; inscrição paga por lead acima do controle.
- **Por quê:** quem volta pelo remarketing ou busca a turma pelo nome já decidiu olhar; a palavra de intenção filtra curiosos e pode alinhar o clique com a inscrição. No tráfego frio, com um total alto, pode assustar [SUPOSIÇÃO; a leitura por tipo de tráfego usa a UTM, CONFIRMAR que o nome da campanha separa frio e remarketing].
- **Tempo mínimo:** a janela comum.
- **Se ganhar / se perder:** regra da seção 0.5. Se ganhar, a confirmação da seção 1.2 já diz que o próximo passo é o retorno do time, para o texto não prometer mais do que entrega.

### 1.5 Posicionamento e prova ao redor (657)

- Perto do botão: link para a pergunta "E se a turma não fechar?" (ficha: aviso de passagem e hotel; reembolso da inscrição se a turma não for confirmada), e a seção de módulos de prática guiada (`matriz`).
- Fora: qualquer frase de quem pode entrar, "prova de Especialista", "exclusiva", resultado clínico do objetivo da ficha, depoimento, nota.
- Pedido ao editor: trocar o botão do hero pelo texto do braço sorteado.
- A página só vale com a OB1 feita (certificação, turma mínima, convite da prova de Especialista, pré-requisito).

---

## 2. Seção 341: Pós-graduação em Medicina Interna Equina

### 2.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Medicina Interna Equina
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre os sistemas, os módulos práticos e as condições da turma, e orientar a inscrição.

- **Campos:** Seu nome (obrigatório); WhatsApp com DDD (obrigatório); E-mail (opcional). Duas caixas de aceite opcionais, desmarcadas (seção 0.3).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Não pedir nem dizer:** nada de promoção, desconto ou bolsa; nada sobre onde são as aulas práticas (OU11).

### 2.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre os sistemas, os módulos práticos e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da seção 0.6. Pergunta sobre local da prática ou formato de módulo: "Vou confirmar com a secretaria onde acontece cada módulo presencial e te retorno" (F2). Pergunta sobre condição de pagamento além da página vai para a secretaria, sem texto pronto.

### 2.3 CTA final (`cta_final`)

> **Título:** Veja os sistemas, os módulos práticos e as condições da turma de medicina interna equina.
>
> **Apoio:** Viu os sistemas e os módulos práticos? Deixe seus dados e o time de vendas responde suas dúvidas e orienta a inscrição. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

O título é a chamada principal da F2, sem mudança. Nenhuma frase depende da promoção (OU10, C7).

### 2.4 Variações de botão e hipóteses

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual ou menor.
- **Por quê:** o público de equinos é menor e alcançado com menos força pelo @ufapevet [SUPOSIÇÃO do plano], então cada visita vale mais. Sem a promoção, a página não tem gatilho de ação; um botão de dúvida convida quem ainda compara. Risco: dúvidas de local da prática e módulo 3 (OU11) que o time só responde com "vou confirmar com a secretaria".
- **Tempo mínimo:** a janela comum. O teste só começa se a página corrigida (OB1: promoção resolvida e segundo local explicado) estiver no ar; se OU10 não estiver resolvida até 11/12, os toques de 341 passam para janeiro (plano, regra 10) e o teste entra com a linha de base mais curta, mantendo o início em 04/01.
- **Se ganhar / se perder:** regra da seção 0.5. Em 341 o volume é o menor, então a leitura por turma não decide: vale o resultado somado.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem procura "pós-graduação em medicina interna equina" pelo nome já tem intenção alta (F1: palavra principal da turma), e a palavra de intenção alinha o clique com essa decisão. Sem promoção para empurrar, o texto não pode depender de gatilho externo [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, com a mesma condição de página corrigida.
- **Se ganhar / se perder:** regra da seção 0.5.

### 2.5 Posicionamento e prova ao redor (341)

- Perto do botão: link para "Compre passagem e hotel só depois de a turma ser confirmada" (resposta do `faq`), sem frase de reembolso (ficha truncada e contraditória), e o cronograma por sistema.
- Fora: promoção, "descontos e bolsas de estudo" da ficha, "hospital veterinário", segundo local, "corpo docente de excelência", depoimento, nota.
- Pedido ao editor: trocar o botão do hero pelo texto do braço sorteado.
- A página só vale com a OB1 feita (certificação, turma mínima, promoção, segundo local, módulo 3, datas de OU17).

---

## 3. Seção 289: Pós-graduação em Cardiologia Veterinária

### 3.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Cardiologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, a teoria a distância, os módulos práticos e as condições da turma, e orientar a inscrição.

- **Campos:** Seu nome (obrigatório); WhatsApp com DDD (obrigatório); E-mail (opcional). Duas caixas de aceite opcionais, desmarcadas (seção 0.3).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Não pedir nem dizer:** nenhuma cidade ou estado, nem como pergunta nem como texto (CP1). O telefone de vendas de Goiânia vem do dado ou do botão de WhatsApp, nunca do texto.

### 3.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, a teoria a distância, os módulos práticos e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da seção 0.6. O botão de WhatsApp citado nas linhas comuns usa o número de vendas da praça de 289, que vem do dado.

### 3.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, do eletrocardiograma ao ecocardiograma na prática.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre a teoria a distância e os módulos práticos. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

O título é a chamada principal da F2, sem mudança.

### 3.4 Variações de botão e hipóteses

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual.
- **Por quê:** a objeção central da turma é a distância ("Moro longe. Vou ter de viajar todo mês?", F2) e a de entrada ("Sou clínico geral. Serve para mim?"). Ambas se resolvem melhor em conversa, e "tirar dúvidas" nomeia essa conversa [SUPOSIÇÃO: falas de objeção são hipóteses da F2].
- **Tempo mínimo:** a janela comum. 289 é a única turma com campanha ativa hoje (limitada a R$ 500,00 até 06/12, PP9), mas o tráfego atual vai para a página antiga e não serve de linha de base.
- **Se ganhar / se perder:** regra da seção 0.5.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** a palavra de intenção filtra quem só está olhando e atrai quem já decidiu a praça; o candidato de outra cidade que já organizou a viagem tende a responder bem a um texto de decisão [SUPOSIÇÃO: persona secundária da linha].
- **Tempo mínimo:** a janela comum.
- **Se ganhar / se perder:** regra da seção 0.5.

### 3.5 Posicionamento e prova ao redor (289)

- Perto do botão: link para a resposta "Moro longe. Vou ter de viajar todo mês?" (fonte: ficha, teoria acompanhada a distância e só os módulos práticos presenciais; aviso de passagem e hotel) e para a pergunta "E se a turma não fechar?" (fonte: ficha, reembolso da inscrição).
- Fora: cidade em qualquer texto, "opções diagnósticas de ponta", "atendimento de excelência", bloco de prova de bolsa, depoimento, nota.
- Pedido ao editor: trocar o botão do hero pelo texto do braço sorteado.
- A página só vale com a OB1 feita (certificação, turma mínima, bloco de prova de bolsa).

---

## 4. Seção 68615: Pós-graduação em Patologia Clínica

### 4.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Patologia Clínica
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma do laboratório clínico e as condições da turma, e orientar a inscrição.

- **Campos:** Seu nome (obrigatório); WhatsApp com DDD (obrigatório); E-mail (opcional). Duas caixas de aceite opcionais, desmarcadas (seção 0.3).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Não pedir nem dizer:** nada que compare valor, duração ou prática com 333; nada que diga qual das duas é melhor.

### 4.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma do laboratório clínico e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da seção 0.6. Se a pessoa perguntar a diferença para a citopatologia, vale a frase-ponte única da F2 (seção 5), sem dizer qual é melhor.

### 4.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma do laboratório clínico, do pré-analítico ao laudo.
>
> **Apoio:** Viu o cronograma? Em dúvida entre patologia clínica e citopatologia, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

O título é a chamada principal da F2, sem mudança. A menção à citopatologia mantém a ponte da F2 e da F3 (variação 3 da F2).

### 4.4 Variações de botão e hipóteses

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual.
- **Por quê:** a pergunta que mais trava esta turma é "Patologia clínica ou citopatologia: qual eu faço?" (F2, F1). Ela se resolve conversando, e o apoio do `cta_final` já promete a explicação do time. Risco: o lead dividido entre 68615 e 333 (mesmo segmento, início com uma semana de diferença).
- **Tempo mínimo:** a janela comum. Para ler o efeito sem enganar, o desenho-de-experimentos soma os leads de 68615 e 333 (área A11) antes de comparar os braços.
- **Se ganhar / se perder:** regra da seção 0.5. Se o braço só mover leads de 333 para 68615 sem aumentar o total da área, não conta como vitória.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem já entendeu que quer o laboratório clínico (palavra principal da página) não precisa de conversa de dúvida; a palavra de intenção pode filtrar quem ainda compara as duas turmas [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, com o sorteio por visitante nas 5 páginas, para quem visita 68615 e 333 ver o mesmo braço.
- **Se ganhar / se perder:** regra da seção 0.5.

### 4.5 Posicionamento e prova ao redor (68615)

- Perto do botão: link para a pergunta-ponte do `faq` ("Patologia clínica ou citopatologia: qual eu faço?"), que também liga à página de 333, e para a pergunta sobre prática ("Tem prática de verdade ou é tudo online?", fonte: ficha, módulos presenciais).
- Fora: "tem reconhecimento pelo Ministério da Educação", "referência nacional em educação", "o curso garante", bloco de prova de bolsa, depoimento, nota.
- Pedido ao editor: trocar o botão do hero pelo texto do braço sorteado.
- A página só vale com a OB1 feita (frase do órgão regulador, certificação, turma mínima, aviso de passagem e hotel, CEP de OU13).

---

## 5. Seção 333: Pós-graduação em Citopatologia Veterinária

### 5.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Citopatologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma de leitura de lâminas e as condições da turma, e orientar a inscrição.

- **Campos:** Seu nome (obrigatório); WhatsApp com DDD (obrigatório); E-mail (opcional). Duas caixas de aceite opcionais, desmarcadas (seção 0.3).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Não pedir nem dizer:** nada de "coordenação" (OU12); nada sobre entrar depois do início ou sobre repor módulo (OU3); nada que trate todos os módulos presenciais como de leitura de lâminas (C1, C2).

### 5.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma de leitura de lâminas e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da seção 0.6. Pergunta sobre entrar depois do início ou sobre quem ensina: "Vou confirmar com a secretaria como fica e te retorno" (F2), até OU3 e OU12.

### 5.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma de leitura de lâminas, sistema por sistema.
>
> **Apoio:** Viu o cronograma? Em dúvida entre citopatologia e patologia clínica, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

O título é a chamada principal da F2, sem mudança.

### 5.4 Variações de botão e hipóteses

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual.
- **Por quê:** a página tem pouca prova de quem ensina (uma só professora listada na ficha, OU12) e nenhuma de depoimento, então parte dos visitantes precisa de reasseguramento. Um botão de dúvida acolhe essa conversa. Risco: o time só responde "vou confirmar com a secretaria" a perguntas de docentes e de reposição de módulo, e isso pode esfriar o lead.
- **Tempo mínimo:** a janela comum. O teste cabe inteiro antes do corte de 25/02 e da pausa da mídia de 333 em 26/03 (sexta-feira da Paixão, enquanto OU3 estiver aberta). Os leads de 333 se somam aos de 68615 na leitura da área A11.
- **Se ganhar / se perder:** regra da seção 0.5.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** 333 tem o menor total das 5 turmas (catálogo), o que baixa a barreira de decisão; uma palavra de intenção pode alinhar o clique com quem já escolheu "leitura de lâminas" como foco [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum.
- **Se ganhar / se perder:** regra da seção 0.5.

### 5.5 Posicionamento e prova ao redor (333)

- Perto do botão: link para a pergunta "Vou treinar leitura de lâmina de verdade?" (fonte: ficha, módulos presenciais de leitura de lâminas e discussão de casos, e os outros presenciais nomeados pelo tema) e para o aviso de passagem e hotel.
- Fora: "coordenação", seção `docentes` com o rótulo "Coordenação: UFAPE" (OU12), "oportunidade única", "o que há de mais recente", qualquer frase de entrada depois do início, depoimento, nota.
- Pedido ao editor: trocar o botão do hero pelo texto do braço sorteado.
- A página só vale com a OB1 feita (certificação, turma mínima, coordenação e docentes, datas de OU17).

---

## 6. Autochecagem (auditorias/08-conversao.md e auditorias/conformidade-educacional.md)

| Item | Situação |
|---|---|
| Uma chamada principal por página | Sim: hero, formulário e `cta_final` pedem a mesma ação; WhatsApp é secundário |
| Formulário pede só o necessário | Sim: nome e WhatsApp obrigatórios; e-mail opcional; lista do que não se pede na seção 0.3 |
| Finalidade do uso dos dados e link da política | Texto pronto; **endereço da política [CONFIRMAR]**, que bloqueia a publicação do formulário |
| WhatsApp e e-mail só com aceite e saída fácil | Sim: caixas separadas, desmarcadas, SAIR no WhatsApp e link de descadastro no e-mail |
| Texto de botão que não engana | Sim: o controle diz "receber o retorno do time"; "Quero me inscrever" fica só como variante, com a confirmação explicando a etapa |
| Urgência real | Nenhuma urgência, escassez ou prazo em botão, título ou apoio |
| Sem MEC, certificado, bolsa, desconto, promoção | Sim, nas 5 turmas |
| Travas por turma (U10 e C14 em 657; OU10 e OU11 em 341; CP1 em 289; OU3 e OU12 em 333) | Sim |
| Sem número, preço, data, local nem nome de docente no texto da página | Sim nos blocos de citação (conferido na escrita; o qa confirma se o validador ignora "um" e "uma" como artigo) |
| Dados do curso conferidos com o catálogo | Sim: nenhum dado de curso digitado; só nomes padrão e comparações de total citadas na análise, com fonte |
| Provas reais e autorizadas | Sim: só o que já está na página; sem depoimento, nota ou selo |
| Objeções respondidas perto do botão | Sim: links para as respostas do `faq` por turma |
| Testes com hipótese escrita e regra de decisão antes do início | Sim: 10 cartões (2 por turma) e regra comum na seção 0.5 |
| Resultados registrados, vencedores e perdedores | Prevista na regra de decisão; registro é do desenho-de-experimentos e da analise-cro |
| Eventos de lead e inscrição rastreados | Previsto na seção 0.5, item 4; conferência de ponta a ponta em 04/12 |
| Nenhum dado pessoal | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; a busca final é do orquestrador |

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início, preço total e status "aberto" das 5 turmas: contexto/catalogo-de-cursos.md, seção 2. Nenhum desses valores está no texto da página. Os totais citados só na análise (657 maior, 333 menor): mesmo catálogo.
- `formulario` e `cta_final` como seções do tipo pos (texto do botão e uma frase de apoio; título curto e botão): templates/pagina-da-turma.md. Regra de texto sem número: mesmo template.
- Botão provisório "Quero me inscrever" e frase de apoio provisória do formulário, `cta_final` por turma, hero e checklist de rastreamento: F3 (saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md).
- Chamada principal, variações e frase-ponte 68615 e 333: F2 (saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda2.md), seções 2 a 7.
- Contatos oficiais da secretaria e de vendas, razão social e voz da marca: contexto/ufape-geral.md. O endereço da política de privacidade não consta ali nem nas 5 fichas.
- Reembolso da inscrição se a turma não for confirmada e aviso de passagem e hotel: fichas de 657, 289, 68615 (reembolso) e 333; em 341 o texto de reembolso está truncado.
- Toque de WhatsApp e e-mail com opt-in por canal e finalidade, descadastro em um clique e SAIR (regras E1 a E4): plano do CMO, regra 11 e encomenda F7.
- CPL de R$ 4,00 a R$ 18,00, verba de R$ 2.000,00 por turma, meta de 15 matrículas, cortes da 1ª mensalidade, pausa de fim de ano, Carnaval, pausa de 333 em 26/03 e revisões de ritmo de 04/01 e 18/01: plano do CMO e gestor-de-midia-pos citado nele (seções 1, 2, 7.3 e 7.4).
- Decisões 8 e 10 (docentes autorizados), 11 (turma mínima 15), 14 (sem bolsa), 16 (inscrição paga e depois 1ª mensalidade; sem valor da inscrição até U11) e 18 (matrícula até o 3º módulo): docs/execucao-2026-10-26.md.
- Itens de conformidade (finalidade e link da política, consentimento por canal, página que entrega o que a peça promete, urgência real) e de conversão (uma chamada principal, formulário curto, testes com hipótese): auditorias/conformidade-educacional.md e auditorias/08-conversao.md.
- Os 5 passos do cartão de hipótese e as duas verificações (uma mudança por teste; regra de decisão escrita antes): .claude/skills/hipotese-de-teste/SKILL.md.

## [SUPOSIÇÃO]

- Que o formulário é só de contato e não cobra nem inicia pagamento (base da frase de risco "não gera cobrança nem compromisso de inscrição").
- Que o retorno do time de vendas acontece por WhatsApp (canal principal de venda da Pós, plano do CMO); por isso o WhatsApp é obrigatório e o e-mail é opcional.
- Que o CRM aceita lead sem e-mail e que e-mail opcional não prejudica o fluxo.
- Os rótulos, as duas caixas de aceite (uma por canal) e todo o texto do formulário, da confirmação e do `cta_final`: redação deste agente, a validar pela pessoa do marketing e por quem responde pela LGPD.
- Que "Quero receber o retorno do time" é o melhor controle, e que "Quero tirar minhas dúvidas" reduz o compromisso e "Quero me inscrever" filtra por intenção: hipóteses, sem dado de conversão (não existe linha de base).
- A meta de até 32 caracteres para o botão caber em uma linha no celular.
- Os limiares provisórios de decisão (20% relativos na taxa de envio e queda máxima de 10% relativos na inscrição paga por lead), que o desenho-de-experimentos confirma ou troca.
- Que a plataforma sorteia por visitante, mantém o braço nas 5 páginas e suporta o parâmetro `cta_variante` no evento de lead e no CRM; que a UTM do nome da campanha separa tráfego frio de remarketing.
- Que a inscrição paga por lead é mensurável por turma e braço, e que a 1ª mensalidade paga não decide o teste por causa do ciclo mais longo.
- Que a diária da mídia, quando mexida na revisão de ritmo, não altera a taxa por visitante.
- As hipóteses de persona por turma (distância em 289, comparação entre 68615 e 333, nicho em 341, alto total em 657, menor total em 333) e o @ufapevet alcançar menos o público de equinos (esta última, do plano do CMO).
- Que o número de leads por turma no ciclo vai de cerca de 111 a 500 (conta deste agente: R$ 2.000,00 divididos pelo CPL de R$ 4,00 a R$ 18,00 do plano).
- Os nomes dos eventos de rastreamento (herdados da F3).

## [CONFIRMAR]

- **Endereço da política de privacidade da Faculdade Ufape** (não está no ufape-geral nem nas fichas). Sem ele o formulário não passa na conformidade.
- **Texto da finalidade, base legal, retenção, compartilhamento com CRM e provedor de WhatsApp e contato do encarregado:** quem responde pela LGPD na Ufape revisa a frase da seção 0.3 e a política.
- **Pixel da Meta, tag do Google Ads e GA4 no evento de lead:** se há aviso de cookies e como o aceite se aplica a eles.
- **Canal, prazo e horário do retorno do time de vendas** (para a frase da confirmação).
- **Se o formulário não cobra nem gera obrigação** (frase de risco).
- **Se o CRM aceita lead sem e-mail** e a identificação do contato (por WhatsApp).
- **Ferramenta de teste no site:** sorteio por visitante, braço comum às 5 páginas, parâmetro no evento e no CRM.
- **Texto e número do botão de WhatsApp secundário** de cada praça (a F3 não definiu o texto).
- **Mínimo de leads por braço, limiares e se o teste corta para 2 braços:** desenho-de-experimentos.
- **Visitas e leads reais por turma** (nenhum número existe hoje; sem eles não há linha de base).
- **U10, OU3, OU10, OU11, OU12, OU13, OU14, OU17, A12 e CP1:** perguntas já abertas no plano; seguem valendo as travas por turma.
- **OB1:** nenhuma das 5 páginas vale enquanto a frase de certificação, a turma mínima de 20 e os demais itens das listas da F3 não forem corrigidos. O formulário e o `cta_final` deste arquivo só entram junto com a página corrigida.
- **U11:** valor da inscrição; até a resposta nenhum texto cita valor.
- **Revisão docente:** conferência técnica dos termos de cada turma nas frases de apoio antes da publicação.

## Próximo agente

**desenho-de-experimentos**: transformar os 10 cartões e a regra comum da seção 0.5 em plano de teste (mínimo de leads por braço, sorteio, janela de 04/01 a 07/02/2027, leitura somada das 5 turmas e da área A11, corte para 2 braços se a amostra não bastar). Antes disso, o qa-de-marketing (F13) revisa este arquivo com as auditorias 08 e de conformidade educacional. Depois da publicação e com dados reais, analise-cro.
