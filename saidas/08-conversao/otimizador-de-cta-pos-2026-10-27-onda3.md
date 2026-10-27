# Formulário e CTA final das 8 turmas de abril de 2027 da Pós-graduação (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609), encomenda O5, lote A, da onda 3

- **Agente:** otimizador-de-cta (departamento 08, Conversão)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1 (lote A). O lote B (maio) entra em nova versão deste arquivo, sem mudar o nome. A turma 662 fica fora, em espera total (OU18); o registro está na seção 9.
- **Encomenda:** O5 do plano do CMO em versão 2 (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md, seção 10, linha O5; regras E1 a E22, em especial E8 e E21). O plano previa a entrega em 16/11; este arquivo sai com a data real do dia, como manda a E10.
- **Formato:** campos `formulario` e `cta_final` de templates/pagina-da-turma.md (tipo pos), uma seção por turma com o código no título. Modelo de forma: saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md, já corrigido pelas Q56 a Q59 da revisão saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md.
- **Status:** rascunho para o qa-de-marketing (O18a; auditorias/08-conversao.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago a partir deste arquivo. Publicar as páginas, ligar o formulário ao CRM e montar o teste são ações humanas ou da plataforma, depois da aprovação.
- **Consumidores:** qa-de-marketing (O18a), editor e time do site (montagem do formulário e do teste), gestor-de-midia (conferência de 11/12 e reconferência de 04/01), landing-page (troca de linhas da seção 0.8, se aprovada), desenho-de-experimentos (próximo agente).
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md (orquestrador)
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 14, 16, 18 e 20)
  - contexto/ufape-geral.md (voz da marca, contatos oficiais; não traz o endereço da política de privacidade) e contexto/pos-graduacao.md
  - contexto/catalogo-de-cursos.md (linhas 1 a 180, que incluem a seção 2 com as 8 turmas; única fonte dos dados de curso)
  - Fichas em contexto/cursos/pos/: 679, 68632, 68635 e 366 inteiras; 68628, 68617, 68636 e 68609 até a linha 60 (dados principais e início do texto). O cronograma completo dessas quatro e as conferências módulo a módulo vêm da O3, que as leu inteiras. Nenhuma ficha traz política de privacidade.
  - templates/pagina-da-turma.md
  - auditorias/conformidade-educacional.md e auditorias/08-conversao.md
  - O3: saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md (inteiro: `formulario`, `cta_final`, visibilidade de `matriz`, travas e checklist 11.2)
  - O4: saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda3.md (linhas 1 a 120: regras e decisões; confere que nada deste arquivo entra em campo de SEO)
  - Plano do CMO: saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (linhas 1 a 200 e 770 a 940: cabeçalho, diagnóstico, regras E1 a E22, travas por turma, perguntas à Ufape, pedidos de aprovação e encomenda O5)
  - Onda 2: saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md (inteiro) e saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md (linhas 380 a 668: Q56 a Q59, seções 5 a 8)
- **Não aberto:** faculdade.ufape.com.br; as demais saídas da onda 3; .claude/skills/hipotese-de-teste/SKILL.md (o formato do cartão de hipótese vem do arquivo da onda 2, que o aplicou); nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum docente é nomeado.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape ou a plataforma tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com a origem.

---

## 0. Como ler este arquivo e blocos comuns às 8 turmas

### 0.1 Regras aplicadas

1. **Texto da página sem número, preço, data, local nem nome de docente (E1).** Vale para tudo o que está em bloco de citação (">") ou entre aspas: é o texto que vai para a página. Nenhum algarismo, ordinal, numeral romano ou número por extenso, e nenhum "um" ou "uma" que conte. Notas, contagens de caracteres, datas do teste e códigos ficam fora desses blocos e não vão para a página.
2. **Fora de todo texto de página:** "MEC", certificado, certificação, reconhecida, bolsa, prova de bolsa, desconto, promoção, urgência ("últimas vagas", "só até", contador, "corra"), superlativo da ficha (E14), promessa de emprego, renda ou resultado clínico, valor da inscrição (U11), prova ou título de Especialista (E13).
3. **Regra 8 em 68632 (OU3 aberta, E22):** nenhum texto deste arquivo, em 68632, fala de entrada depois do início, de matrícula até o 3º módulo ou do 3º módulo. O mesmo vale para a regra do 3º módulo nas outras sete turmas: ela é dado da turma (OU14), nunca botão, título, apoio, confirmação ou frase perto do botão (E6, E7, E18).
4. **Botão que diz a ação real (E8).** O formulário não matricula nem cobra: pede um retorno do time de vendas. O texto recomendado e controle é "Quero receber o retorno do time" (31 caracteres), igual ao do hero e do `cta_final` da O3. "Quero me inscrever" segue suspenso (Q58 e Q59).
5. **E21 e Q56:** quem não marca uma caixa de aceite recebe só o retorno pedido no formulário e não entra nas listas de campanha (S2 e S3) daquele canal. Nenhum texto diz "usamos seus dados só para esse contato".
6. **Q57:** a mensagem de erro manda ao time pelo WhatsApp da página (o de vendas da praça, vindo do dado), nunca à secretaria.
7. **Uma chamada principal por página** (auditorias/08-conversao.md): hero, formulário e `cta_final` pedem a mesma ação e usam o mesmo texto de botão em cada braço do teste. WhatsApp continua chamada secundária, com o número da praça vindo do dado (Goiânia em 68632 e 68609; São Paulo nas outras seis). O número nunca entra no texto.
8. **Nada inventado:** nenhuma prova nova. Ao redor do botão só entram provas que já estão na página (respostas do `faq`, `matriz` quando visível, `docentes` como dado). Sem depoimento, nota, selo ou avaliação, porque nenhum existe autorizado em mãos.
9. **Travas por turma** (seções 1 a 8): P3 e OU19 (679), OU3 e OU34 (68632), OU35 (68635), P4 e OU20 (366), P5 e OU30 (68628), P5, OU29 e URL "/v/" (68617), P3 e OU21 (68636), OU31 e E13 (68609). CP1: nenhuma cidade em texto de página.

### 0.2 Inventário de CTAs (método, passo 1)

| CTA | Onde | Texto atual | Ação que pede | Situação |
|---|---|---|---|---|
| Botão do hero | topo da página | "Quero receber o retorno do time" (campo `botao` do hero na O3, [CONFIRMAR com a plataforma]) | rolar até o formulário | trocar pelo texto do braço sorteado (seção 0.4) |
| Botão do formulário | `formulario` | "Quero receber o retorno do time" (O3) | enviar nome, WhatsApp e e-mail | refinado nas seções 1 a 8 |
| Botão do `cta_final` | fim da página | "Quero receber o retorno do time" (O3) | rolar ou abrir o formulário | refinado nas seções 1 a 8 |
| WhatsApp | botão fixo no celular e link | texto não definido pela O3 [CONFIRMAR] | abrir conversa com vendas da praça | secundário; sem mudança aqui |
| Política de privacidade | abaixo do botão | "política de privacidade" | abrir a política | endereço [CONFIRMAR] |
| Links do `faq` perto do botão | ao lado do formulário | perguntas por turma (O3) | rolar até a resposta | seções 1.5 a 8.5 |
| Link-ponte entre turmas | `faq` | nome da outra turma (O3, regra E19) | abrir a outra página | sem mudança; só vira link depois da página conferida |
| CTA nas páginas no ar hoje | fichas de 26/10/2026 | "COMPRAR" (as 8); "PROVA DE BOLSA: Clique aqui" (todas menos 679 e 366); "prova de Especialista: Clique aqui" (68609) | comprar direto; abrir prova | fora desta entrega: os dois últimos saem pelo OB1 (decisão 14 e E13); "COMPRAR" é decisão humana do OB1 (item "botão COMPRAR" da O3), e se ficar vira chamada secundária |

### 0.3 Formulário: o que se pede e o que não se pede

**Campos (iguais nas 8 turmas):**

| Campo | Rótulo | Obrigatório | Por que é necessário | Mensagem de erro do campo |
|---|---|---|---|---|
| Nome | Seu nome | sim | o time de vendas precisa saber como chamar o contato | Digite seu nome. |
| WhatsApp | WhatsApp com DDD | sim | canal do retorno do time de vendas [SUPOSIÇÃO: o retorno é por WhatsApp, como na onda 2] | Confira o número do WhatsApp com DDD. |
| E-mail | E-mail (opcional) | não | só para quem quer receber mensagens por e-mail; sem ele o retorno acontece pelo WhatsApp [SUPOSIÇÃO: o CRM aceita lead sem e-mail, CONFIRMAR] | Confira o e-mail. |

Só o WhatsApp leva a dica "DDD e número"; os outros dois ficam sem exemplo, para a tela não carregar número.

**Caixas de aceite (opcionais, nunca pré-marcadas), uma por canal e finalidade (regras E4 e E21 do plano):**

> Quero receber mensagens sobre esta turma e sobre cursos da mesma área por WhatsApp.
>
> Quero receber mensagens sobre esta turma e sobre cursos da mesma área por e-mail.

A caixa de e-mail só aparece ou só vale se o campo de e-mail estiver preenchido. O retorno do time de vendas pedido no formulário não depende de nenhuma das duas caixas. **Quem não marca uma caixa recebe só o retorno pedido e não entra nas listas de campanha (S2 e S3) daquele canal** (Q56; encomenda O10 do plano, arquiteto-de-fluxos).

**Campos de rastreamento (ocultos, sem dado pessoal):** código da turma, UTM (preservadas do clique ao CRM, regra 12 do plano) e `cta_variante` (c, v1 ou v2). Ver 0.5.

**Não se pede, por não ser necessário ao retorno:** CPF, data de nascimento, cidade e estado (o campus é dado da turma; em 68632 e 68609 a cidade não entra no texto, CP1), CRMV, ano de formatura, especialidade atual, pergunta de elegibilidade ou de experiência prévia (em 68609 seria pré-requisito disfarçado; E13), interesse em bolsa (decisão 14), orçamento, "como conheceu" (vem da UTM). Quem decidir pedir qualquer um deles precisa justificar a necessidade antes. **Isto corrige a O3 em um ponto** (seção 0.8, linha 5): o checklist da O3 diz "mais a pergunta de interesse se necessária", e aqui não há pergunta de interesse.

**Mensagem de erro de envio (comum, Q57):**

> Não conseguimos enviar seus dados agora. Tente de novo ou fale com o time pelo WhatsApp desta página.

Em 68632 e 68609, o WhatsApp da página é o de vendas da praça de Goiânia, e em 679, 68635, 366, 68628, 68617 e 68636 é o de vendas de São Paulo, nos dois casos vindo do dado (contatos oficiais, contexto/ufape-geral.md). O texto não traz número.

**Frase de risco abaixo do botão (comum):**

> Enviar seus dados não gera cobrança nem compromisso de inscrição.

[SUPOSIÇÃO: o formulário não dispara pagamento. O time do site confirma antes de publicar; se houver cobrança em alguma etapa, a frase sai, e a linha "Enviar seus dados não gera cobrança" do `cta_final` e "Nenhuma cobrança foi feita" da confirmação saem junto.]

**Frase de finalidade e link da política de privacidade (LGPD, comum):**

> Usamos seus dados para o time de vendas da Faculdade Ufape retornar sobre esta turma e orientar sua inscrição. Se você marcar as opções acima, também enviamos mensagens sobre esta turma e sobre cursos da mesma área, e você pode sair quando quiser. Veja como tratamos seus dados na [política de privacidade]([CONFIRMAR: endereço da política de privacidade da Faculdade Ufape]).

O endereço da política não está em contexto/ufape-geral.md nem em nenhuma das 8 fichas: fica [CONFIRMAR]. Sem o endereço, o formulário não passa em conformidade-educacional (item de finalidade e link). Base legal, retenção, compartilhamento com a ferramenta de CRM e de WhatsApp e contato do encarregado são da política, não da tela [CONFIRMAR com quem responde pela LGPD na Ufape].

**Ordem na tela, de cima para baixo:** título, apoio, campos, caixas de aceite, botão, frase de risco, frase de finalidade com o link. O checklist 11.2 da O3 diz que a finalidade fica "ao lado do botão"; aqui ela fica abaixo (seção 0.8, linha 6).

### 0.4 Botão: o texto recomendado e as duas variantes de teste

| Braço | Texto do botão | Caracteres | Papel |
|---|---|---|---|
| C (recomendado e controle) | Quero receber o retorno do time | 31 | diz o que acontece depois do clique |
| V1 | Quero tirar minhas dúvidas | 26 | reduz o compromisso percebido |
| V2 | Quero me inscrever | 18 | suspenso: só entra no teste se o clique levar à inscrição de fato; com o formulário de contato, promete mais do que entrega (conformidade, página de destino) [CONFIRMAR com o time do site] |

Contagem feita letra por letra, espaços inclusos. "Quero receber o retorno do time": Quero (5), espaço (6), receber (13), espaço (14), o (15), espaço (16), retorno (23), espaço (24), do (26), espaço (27), time (31). "Quero tirar minhas dúvidas": Quero (5), espaço (6), tirar (11), espaço (12), minhas (18), espaço (19), dúvidas (26). "Quero me inscrever": Quero (5), espaço (6), me (8), espaço (9), inscrever (18). O qa reconta por script.

O mesmo texto vale para o botão do hero, do formulário e do `cta_final` em cada braço. Como este arquivo não altera a O3, o editor troca o botão do hero pelo texto do braço sorteado (pedido no fim de cada seção) [SUPOSIÇÃO: meta de até 32 caracteres para caber em uma linha no celular, que é só meta de leitura; o template não fixa limite].

Por que o controle não é "Quero me inscrever": quem clica espera começar a inscrição e encontra um pedido de contato. O texto honesto reduz o clique enganado e a frustração do primeiro retorno. Se V2 voltar ao teste e vencer, a mensagem de confirmação já explica a etapa, para a promessa não ficar maior do que a entrega.

### 0.5 Regras comuns do teste de botão, somando com a onda 2

**Um teste só, com 13 páginas.** O controle (C) e V1 são os mesmos braços da onda 2 (seção 0.4 do arquivo da onda 2). Entram no mesmo teste as 5 páginas de março de 2027 (657, 341, 289, 68615 e 333) e as 8 deste arquivo. A leitura principal é com as 13 somadas e a leitura de apoio é por lote (março e abril), por área e por turma, só como direção. Cartões: 10 da onda 2 e 16 deste arquivo (8 de V1 e 8 de V2 suspenso), 26 no total.

1. **Uma mudança por teste:** só o texto do botão, nas 3 posições da mesma página e em todas as 13 páginas. Nada mais muda.
2. **Sorteio por visitante,** com divisão igual entre C e V1 (V2 suspenso, seção 0.4), e o mesmo braço nas 13 páginas para quem visitar mais de uma. Isso importa nos pares de mesma área: A1 (657 e 68609), A2 (289 e 68636), A4 (68632 e 366) e A11 (68615 e 333) [SUPOSIÇÃO: a plataforma faz o sorteio por cookie, CONFIRMAR com o time do site].
3. **Métrica principal:** taxa de envio do formulário (leads dividido por visitantes da página). **Métrica de qualidade:** inscrição paga por lead, medida separada da matrícula paga, só números somados (decisão 16). A 1ª mensalidade paga não decide este teste: o ciclo dela é mais longo que a janela [SUPOSIÇÃO].
4. **Evento:** `generate_lead` com o parâmetro `cta_variante`, e o mesmo valor gravado no lead do CRM; `click_whatsapp` sem o parâmetro (nomes sugeridos pela O3, 11.2 [SUPOSIÇÃO]). Sem dado pessoal em nenhum parâmetro.
5. **Janela:** a mesma da onda 2, de segunda 04/01/2027 a domingo 07/02/2027, 5 semanas inteiras [SUPOSIÇÃO: o desenho-de-experimentos confirma]. Para o lote A ela cabe antes de qualquer corte da 1ª mensalidade (04/03 a 25/03, plano do CMO, seção 1.1), do Carnaval (08 a 10/02) e do fim de ano sem campanha (21/12 a 03/01). As páginas de abril entram no ar em 10/12 (plano, seção 7.2): de 10/12 a 03/01 rodam só com o controle, para formar a linha de base, e a mídia de abril sobe em 06/01. O feriado de 25/01 (São Paulo) sem campanha não pausa o sorteio.
6. **Quantidade de leads:** não há CPL nem visita histórica. A conta da onda 2 (verba de R$ 2.000,00 por turma dividida por CPL de R$ 4,00 a R$ 18,00, cerca de 111 a 500 leads por turma no ciclo inteiro, antes de dividir em braços) é herdada e vale como ordem de grandeza também aqui [SUPOSIÇÃO herdada: o plano da onda 3 só confirma o teto de CPL de R$ 18,00, não o piso]. No lote A, 15% da verba (R$ 300,00 por turma) fica para a extensão depois do corte (plano, seção 1.2, citando o gestor), então menos leads caem dentro da janela. Por isso o teste não se decide por turma. O desenho-de-experimentos fixa o mínimo de leads por braço antes de começar e decide se corta para 2 braços (já é o caso, com V2 suspenso).
7. **Regra de decisão, escrita antes do teste** [SUPOSIÇÃO: limiares provisórios herdados da onda 2; o desenho-de-experimentos confirma ou troca]:
   - V1 vence se, nas 13 páginas somadas e com o mínimo de leads por braço atingido, a taxa de envio ficar pelo menos 20% acima da do controle (relativo) **e** a inscrição paga por lead não ficar mais de 10% abaixo da do controle (relativo).
   - Se vencer: vira o botão das 13 páginas e passa a ser o controle das turmas seguintes (lote B, em nova versão deste arquivo); o resultado é registrado.
   - Se empatar ou a amostra não chegar ao mínimo: fica o controle, e o registro diz "sem evidência".
   - Se perder: descartar e registrar o motivo.
   - Se um braço aumentar leads e derrubar a inscrição paga por lead, o ganho de volume não vale: fica o controle.
   - Se o braço só mover leads entre páginas da mesma área (por exemplo 68632 para 366, ou 68636 para 289) sem aumentar o total da área, não conta como vitória.
8. **O que não muda durante a janela:** texto da página, ordem das seções e criativos. A diária pode mudar nas revisões de ritmo do gestor; o teste lê só a taxa por visitante [SUPOSIÇÃO].
9. **Sem ferramenta de teste no site** [CONFIRMAR]: alternativa é trocar de braço por semana, menos confiável e sem separar o efeito do botão do efeito da semana.
10. **Condição de entrada de cada turma no teste:** a página precisa estar no ar já corrigida pelo OB1 (OC1-A, publicação até 10/12). 679, 366 e 68636 só entram com `local_e_datas` visível e a data confirmada (OU19, OU20, OU21). 68617 só entra com a URL "/v/" conferida (OU29). Turma que não estiver pronta em 04/01 fica fora do teste e entra no controle, sem recontar a janela dos outros.

### 0.6 Mensagem de confirmação (estrutura comum)

Título: "Recebemos seus dados." Depois, uma frase por turma sobre o que o time responde (seções 1 a 8), mais as linhas comuns abaixo.

Linhas comuns, depois da frase da turma, **variante A** (`matriz` visível: 679, 68632, 68635 e 366):

> Nenhuma cobrança foi feita. Enquanto isso, você pode rever o cronograma e as condições nesta página. Se preferir falar agora, use o botão de WhatsApp desta página.

**Variante B** (`matriz` oculta até a correção do dado: 68628, 68617, 68636 e 68609). Sem a `matriz`, "rever o cronograma" apontaria para um bloco que não aparece:

> Nenhuma cobrança foi feita. Enquanto isso, você pode rever as condições nesta página. Se preferir falar agora, use o botão de WhatsApp desta página.

Linha extra só para quem marcou a caixa de WhatsApp:

> Você aceitou receber mensagens por WhatsApp. Para parar, responda SAIR a qualquer mensagem.

Linha extra só para quem marcou a caixa de e-mail:

> Você aceitou receber mensagens por e-mail. Para parar, use o link de descadastro no fim de cada e-mail.

"Nenhuma cobrança foi feita" só vale com o time do site confirmando que o formulário não cobra (seção 0.3). O prazo do retorno não vai no texto: [CONFIRMAR prazo e horário de atendimento do time de vendas]. Se a Ufape confirmar, o editor acrescenta uma frase sobre o prazo, sem número, por exemplo "O retorno acontece em dia útil, no horário de atendimento". Uma confirmação automática por WhatsApp ou e-mail seria envio e só existe com o aceite da caixa e com o pedido OC2 do plano (nada é escrito aqui).

### 0.7 Posicionamento e prova ao redor do botão (método, passo 4), regras comuns

- **Posição:** o botão do hero rola até o formulário; o formulário fica depois do `faq`, na ordem padrão do tipo pos (O3); o `cta_final` fecha a página e leva de volta ao formulário. No celular, botão fixo do WhatsApp como secundário, nunca dois botões primários.
- **Embaixo do botão, nesta ordem:** frase de risco, frase de finalidade e link da política (0.3).
- **Prova que pode ficar perto:** links para a pergunta de formato ou de prática do `faq` de cada turma (seções 1.5 a 8.5), para "E se a turma não fechar?" (aviso de passagem e hotel, regra da linha em contexto/pos-graduacao.md) e, quando visível, para a `matriz`. `docentes` como dado, sem frase de autoridade nova.
- **Não pôr perto do botão:** selo ou frase de MEC e de certificação (seção `certificacao` oculta até a regulação), nota ou avaliação, depoimento (nenhum autorizado em mãos), contador de vagas, "últimas vagas", bolsa, desconto, valor da inscrição, a regra do 3º módulo (nunca como urgência, E6 e E7), prova ou título de Especialista.
- **Sem "sem compromisso" como selo:** a ideia aparece só na frase de risco, em linguagem simples, e só se o time do site confirmar que o formulário não cobra.
- **Turma mínima e reembolso:** só pelo `faq`. O alcance de "valores de inscrição" no reembolso é [CONFIRMAR com a secretaria] (O3); por isso nenhuma frase perto do botão promete reembolso.

### 0.8 Conferência com a O3: textos iguais e o que a O3 deve trocar

**Textos iguais.** O apoio do formulário e o apoio, o título e o botão do `cta_final` de cada turma, nas seções 1 a 8, são os que a O3 já usa, palavra por palavra (seções x.4 da O3). Nenhum foi reescrito. O que este arquivo acrescenta à O3 é só o que ela deixou ao O5: título do formulário, rótulos, caixas de aceite, frase de risco, finalidade com link, mensagem de confirmação, mensagem de erro e as variações de botão.

**O que a O3 deve trocar ou registrar** (linha a linha; nenhuma é troca de texto de página já escrito):

| # | Onde na O3 | O que está | O que a O3 deve fazer |
|---|---|---|---|
| 1 | `formulario` de cada turma (seções 1.4 a 8.4) | só `botao` e "frase de apoio" | acrescentar o campo `titulo` com "Tire suas dúvidas sobre a Pós-graduação em <nome do catálogo>" (texto exato nas seções 1.1 a 8.1 deste arquivo). O template só prevê botão e frase de apoio: se a plataforma recusar o título, ele sai e nada mais muda [CONFIRMAR com a plataforma, mesma trava da onda 2] |
| 2 | `cta_final` de 68628, 68617, 68636 e 68609 (seções 5.4, 6.4, 7.4 e 8.4) | título e apoio dizem "Veja o cronograma" e "Viu o cronograma?" | registrar que esse texto só vale com a `matriz` visível. A O3 mantém `matriz` oculta nessas quatro até a correção do dado. Se a `matriz` ficar oculta no dia da publicação, trocar pelo texto de reserva das seções 5.3, 6.3, 7.3 e 8.3 deste arquivo |
| 3 | Notas 3.2 e 7.2 (SEO) e seções 3.4, 7.4 e 8.4 (`cta_final`) | a nota diz que "terapia intensiva", "cardiologia", "ventilação mecânica" e termos irmãos só aparecem no nome da outra pós-graduação, na frase-ponte; o apoio do `cta_final` de 68635 e 68636 e de 68609 também os nomeia ("Em dúvida entre ..., o time de vendas explica a diferença") | manter o texto (o apoio não diz qual é melhor, E11) e ajustar a nota para "só na frase-ponte e no apoio do `cta_final`", para o qa não ler como erro. O `cta_final` não é campo de SEO |
| 4 | Seção 0, item 8 | `botao` do hero com "[CONFIRMAR com a plataforma]" | sem troca. Registrar que o texto do hero muda pelo braço sorteado (seção 0.4 deste arquivo) |
| 5 | Checklist 11.2, "Formulário curto" | "nome, WhatsApp e e-mail (e-mail opcional), mais a pergunta de interesse se necessária" | tirar "mais a pergunta de interesse se necessária". O formulário só pede nome, WhatsApp e e-mail (seção 0.3) |
| 6 | Checklist 11.2, "Finalidade do uso dos dados e link da política ao lado do botão" | "ao lado do botão" | trocar por "abaixo do botão, depois da frase de risco" |
| 7 | `cta_final`, "apoio (opcional)" | frase de risco "Enviar seus dados não gera cobrança" condicionada ao time do site | sem troca. Mesma condição vale aqui para a confirmação ("Nenhuma cobrança foi feita") |

### 0.9 Correções da revisão da onda 2 que valem desde a primeira linha

| Item do qa | Como aparece aqui |
|---|---|
| Q56 | Seção 0.3: quem não marca uma caixa recebe só o retorno pedido e não entra em S2 e S3 daquele canal |
| Q57 | Seção 0.3: erro de envio manda ao time pelo WhatsApp da página, não à secretaria |
| Q58 | Seção 0.4: V2 suspenso; divisão igual só entre C e V1 (seção 0.5, item 2) |
| Q59 | Todo cartão de V2 traz "suspenso até a confirmação da seção 0.4" no título |

---

## 1. Seção 679: Pós-graduação em Infectologia Veterinária

### 1.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Infectologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, a prática de laboratório e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3 (Seu nome, WhatsApp com DDD, E-mail opcional; duas caixas desmarcadas).
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nenhuma data nem mês (P3, OU19); nada de "pequenos animais" nem "cães e gatos" (a ficha não restringe a espécie); nada sobre entrada depois do início.

### 1.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, a prática de laboratório e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da variante A (seção 0.6). Pergunta sobre a data de início: "Vou confirmar a data com a secretaria e te retorno com o link da turma" (O3, P3 e OU19).

### 1.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, do laboratório ao controle de infecção hospitalar.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre a prática de laboratório e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 1.4). A `matriz` de 679 é visível, então o "Viu o cronograma?" aponta para um bloco que existe.

### 1.4 Variações de botão e hipóteses

Regras comuns de janela, métrica, mínimo de leads e decisão: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio do formulário acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** a primeira pergunta do `faq` é "Infectologia já aparece na clínica geral. Preciso de pós-graduação nisso?" (O3, voz do candidato [SUPOSIÇÃO] da O2). Quem hesita nessa pergunta tende a aceitar "tirar dúvidas" mais do que "pedir retorno de vendas", porque o pedido parece menor [SUPOSIÇÃO]. Risco: com a data em divergência (P3), o time responde "vou confirmar a data com a secretaria" e o lead pode esfriar.
- **Tempo mínimo:** a janela comum (04/01 a 07/02/2027), só com a data de 679 confirmada e `local_e_datas` visível (seção 0.5, item 10).
- **Se ganhar / se perder:** regra da seção 0.5, item 7.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** a palavra de intenção filtra curiosos; quem busca a turma pelo nome já decidiu olhar [SUPOSIÇÃO; a leitura por tipo de tráfego usa a UTM, CONFIRMAR que o nome da campanha separa frio e remarketing].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5. Se ganhar, a confirmação da seção 1.2 já diz que o próximo passo é o retorno do time.

### 1.5 Posicionamento e prova ao redor (679)

- **Perto do botão:** links para "Vou ter prática ou é tudo online?" (O3: módulos presenciais de laboratório, zoonoses e controle de infecção) e para "E se a turma não fechar?" (aviso de passagem e hotel; a ficha não traz linha de reembolso, então a resposta de 679 não promete reembolso, O3). `matriz` visível.
- **Fora:** "única do mundo", "empregabilidade", "diferencial competitivo", "saúde pública", qualquer data ou mês, certificado, depoimento, nota, bolsa.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, superlativos, data de início confirmada).

---

## 2. Seção 68632: Pós-graduação em Clínica Cirúrgica de Cães e Gatos

### 2.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Clínica Cirúrgica de Cães e Gatos
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma presencial, as aulas teórico-práticas e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3; o WhatsApp da página é o de vendas de Goiânia, vindo do dado.
- **Não pedir nem dizer:** nada sobre entrada depois do início nem sobre o 3º módulo (regra 8, OU3, E22); nenhuma cidade em texto (CP1); nunca "online", "a distância" nem "semipresencial" (turma presencial); nada de "coordenação" (OU34); nada de "formar especialistas".

### 2.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma presencial, as aulas teórico-práticas e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da variante A (seção 0.6). A resposta do time a "Ainda dá tempo?" diz só a data de início (dado da turma) e o link, enquanto OU3 estiver aberta (E22; O3). Pergunta sobre experiência prévia: "O público da turma são médicas e médicos veterinários; experiência prévia, vou confirmar com a secretaria" (O3).

### 2.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma presencial de clínica cirúrgica, módulo a módulo.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre as aulas teórico-práticas e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 2.4). `matriz` visível.

### 2.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** a turma é presencial e a pergunta do `faq` é "É presencial. Como concilio com a clínica?" (O3 [SUPOSIÇÃO]). A conciliação da agenda se resolve em conversa, e "tirar dúvidas" nomeia essa conversa. Risco: perguntas de entrada depois do início e de reposição de módulo só têm a resposta "data de início e link" (E22), o que pode esfriar o lead.
- **Tempo mínimo:** a janela comum. Leitura de apoio com 366 na área A4, porque o candidato compara cirurgia e reabilitação (frase-ponte da O3).
- **Se ganhar / se perder:** regra da seção 0.5. Em 68632, se ganhar em volume e perder em inscrição paga por lead, fica o controle.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem escolhe um curso presencial já organiza a agenda para ir ao campus; a palavra de intenção pode alinhar o clique com essa decisão [SUPOSIÇÃO: persona secundária da linha].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 2.5 Posicionamento e prova ao redor (68632)

- **Perto do botão:** links para "É presencial. Como concilio com a clínica?" (cronograma e aviso de passagem e hotel) e para "E se a turma não fechar?" (aviso de passagem e hotel e reembolso dos valores de inscrição, O3). `matriz` visível.
- **Fora:** qualquer frase de entrada depois do início, "reconhecimento pelo Ministério da Educação", "referência nacional", "garante", "formar especialistas", bloco de prova de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, frases ligadas ao órgão regulador, bloco de bolsa). Se o item de "entrada depois do início" fosse incluído antes de OU3, ele quebraria a regra 8.

---

## 3. Seção 68635: Pós-graduação em Clínica Médica e Emergência de Pequenos Animais

### 3.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Clínica Médica e Emergência de Pequenos Animais
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, os módulos presenciais e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nada de "duas certificações", "dupla certificação" nem certificado por parte da carga (OU35); nenhuma vaga com número (OU4); nada de "terapia intensiva" no formulário (termo de 68623).

### 3.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, os módulos presenciais e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da variante A (seção 0.6). Pergunta sobre certificados: "vou confirmar com a secretaria" (OU35), sem texto pronto.

### 3.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, da semiologia ao atendimento do paciente grave.
>
> **Apoio:** Viu o cronograma? Em dúvida entre clínica médica e terapia intensiva, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 3.4). `matriz` visível. A menção a terapia intensiva mantém a ponte A3 da O2 e não diz qual das duas é melhor (E11).

### 3.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** 68635 tem a maior carga horária do lote A (750 h, catálogo) e o `faq` traz "O curso é longo. Vale o tempo?" (O3 [SUPOSIÇÃO]). Quem pesa o tempo antes de pedir retorno de vendas pode preferir tirar a dúvida primeiro. Risco: o `cta_final` já prevê a conversa de comparação com terapia intensiva, e "tirar dúvidas" pode atrair mais comparadores do que decididos.
- **Tempo mínimo:** a janela comum. Leitura de apoio com a área A3 (68623 entra só no lote B, depois da janela).
- **Se ganhar / se perder:** regra da seção 0.5.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem procura "pós-graduação em clínica médica e emergência de pequenos animais" pelo nome (O1, palavra principal) já tem intenção alta; a palavra de intenção alinha o clique com essa decisão [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 3.5 Posicionamento e prova ao redor (68635)

- **Perto do botão:** links para "Faço plantão. Como encaixo os módulos presenciais?" (O3: o cronograma mostra o mês de cada módulo presencial) e para "E se a turma não fechar?". `matriz` visível.
- **Fora:** "duas certificações", certificados de carga parcial, "extremamente benéfico", "papel crucial", "ampla gama de condições", bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação e OU35, turma mínima, bloco de bolsa, aviso de passagem e hotel).

---

## 4. Seção 366: Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária

### 4.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, a prática presencial e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nenhuma data nem mês (P4, OU20); nada de "coordenação" (OU34); nada sobre atuação profissional depois do curso nem sobre quem não é médico veterinário (pergunta "Fisioterapeuta pode fazer?" vai ao time e à regulação, O3); nada de "primeira turma" nem "turma inaugural" (E1).

### 4.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, a prática presencial e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da variante A (seção 0.6). Pergunta sobre a data de início: "Vou confirmar a data com a secretaria e te retorno" (O3, P4 e OU20).

### 4.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, da avaliação da dor às terapias manuais.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre a prática presencial e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 4.4). `matriz` visível.

### 4.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** é turma de curso novo (turma I, catálogo), sem histórico para o visitante conferir, e o primeiro item do `faq` é "Quero oferecer reabilitação, mas não sei por onde começar" (O3 [SUPOSIÇÃO]). Um botão de dúvida acolhe quem ainda está entendendo a área. Risco: enquanto a data não for confirmada (OU20), o time só responde "vou confirmar a data com a secretaria", e as dúvidas de coordenação ficam sem texto (OU34).
- **Tempo mínimo:** a janela comum, só com a data de 366 e o CEP confirmados e `local_e_datas` visível (seção 0.5, item 10). Se a data de 24/04 valer em vez de 10/04, o corte da 1ª mensalidade muda de 11/03 para 25/03 (plano, seção 1.1) e a janela segue cabendo.
- **Se ganhar / se perder:** regra da seção 0.5. Leitura de apoio com 68632 na área A4.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem busca "pós-graduação em fisioterapia veterinária" (O1, palavra principal, forma digitada pelo candidato) tem intenção de especialização definida; a palavra de intenção pode filtrar curiosos [SUPOSIÇÃO]. Em curso novo, o risco de assustar quem ainda não conhece a oferta é maior.
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 4.5 Posicionamento e prova ao redor (366)

- **Perto do botão:** links para "Tem prática de verdade ou é só teoria?" (O3: módulos presenciais de prática por técnica) e para "E se a turma não fechar?". `matriz` visível.
- **Fora:** coordenação, "ganhando destaque no Brasil", a resolução de conselho de classe, "equipe formada por mestres e doutores", "novos profissionais especializados", data, CEP, bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, data confirmada, coordenação, CEP, frases sem fonte).

---

## 5. Seção 68628: Pós-graduação em Oncologia Veterinária

### 5.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Oncologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, os módulos presenciais e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nenhum número de turma, nem como pergunta (P5, OU30); nada de "presencial" como descrição da turma (ela é semipresencial); nada de "reconhecimento", "referência nacional" nem "garante".

### 5.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, os módulos presenciais e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da **variante B** (seção 0.6), enquanto a `matriz` estiver oculta; da variante A quando ela ficar visível. Pergunta sobre a turma: sem número (P5).

### 5.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, do diagnóstico do câncer à discussão de casos.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre os módulos presenciais e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 5.4). **Só vale com a `matriz` visível.** Na O3 a `matriz` de 68628 fica oculta até a correção do dado (módulo 24 com "Para definir" e módulos repetidos). Texto de reserva, para a `matriz` oculta (palavras tiradas do `sobre` da O3):

> **Título (reserva):** Veja os módulos presenciais, da quimioterapia à discussão de casos.
>
> **Apoio (reserva):** Viu os módulos presenciais? Deixe seus dados e o time de vendas responde suas dúvidas sobre o cronograma e as condições. Enviar seus dados não gera cobrança.
>
> **Botão (reserva):** Quero receber o retorno do time (31 caracteres)

### 5.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual ou um pouco menor.
- **Por quê:** 68628 tem o maior total do lote A (catálogo), e a primeira pergunta do `faq` é "Não tenho estrutura para quimioterapia na clínica. O que o curso traz sobre o tratamento?" (O3 [SUPOSIÇÃO]). Com total alto, um pedido de menor compromisso pode abrir mais conversas [SUPOSIÇÃO]. Risco: leads menos decididos e mais carga para o time, que não pode citar o número da turma (P5).
- **Tempo mínimo:** a janela comum, com a página corrigida pelo OB1 (`matriz` e turma, OU30).
- **Se ganhar / se perder:** regra da seção 0.5.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** menos envios no tráfego frio; igual ou mais no remarketing; inscrição paga por lead acima do controle.
- **Por quê:** com total alto, a palavra de intenção pode assustar no tráfego frio e filtrar bem quem já decidiu olhar [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 5.5 Posicionamento e prova ao redor (68628)

- **Perto do botão:** links para "Como funciona o semipresencial? Tenho de ir sempre?" (O3: a maior parte dos módulos é online, com o mês dos presenciais marcado no cronograma) e para "E se a turma não fechar?". `matriz` só depois da correção do dado: sem ela, o link do cronograma não existe.
- **Fora:** número da turma, "reconhecimento pelo Ministério da Educação", "referência nacional", "garante", bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, frases ligadas ao órgão, bloco de bolsa, turma VII ou VI, `matriz`).

---

## 6. Seção 68617: Pós-graduação em Endocrinologia de Pequenos Animais

### 6.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Endocrinologia de Pequenos Animais
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, as aulas práticas e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nenhum número de turma (P5, OU29); nada de TCC (a ficha traz o módulo "Como montar seu TCC" sem TCC na avaliação, OB1 da O3); nada de "reconhecida e respeitada", "renomados" nem "estará apto".

### 6.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, as aulas práticas e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da **variante B** (seção 0.6), enquanto a `matriz` estiver oculta; da variante A quando ela ficar visível. Pergunta sobre TCC: "vou confirmar com a secretaria" (O3), sem texto pronto.

### 6.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, da fisiologia hormonal às emergências endócrinas.
>
> **Apoio:** Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre as aulas práticas e as condições. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 6.4). **Só vale com a `matriz` visível.** Na O3 ela fica oculta até a correção do dado (módulo 17 com a data do 11). Texto de reserva, para a `matriz` oculta (palavras tiradas do `sobre` da O3):

> **Título (reserva):** Veja as aulas práticas presenciais e a discussão de casos clínicos.
>
> **Apoio (reserva):** Viu as aulas práticas? Deixe seus dados e o time de vendas responde suas dúvidas sobre o cronograma e as condições. Enviar seus dados não gera cobrança.
>
> **Botão (reserva):** Quero receber o retorno do time (31 caracteres)

### 6.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual.
- **Por quê:** o `faq` abre com "Sou clínico geral. Endocrinologia é para mim?" e traz "Pós-graduação ou curso online mais curto?" (O3 [SUPOSIÇÃO]). As duas perguntas se resolvem em conversa, e "tirar dúvidas" nomeia essa conversa. Só dois módulos são presenciais (O3), o que reduz a barreira de logística e pode deixar a dúvida de formato como a principal.
- **Tempo mínimo:** a janela comum, com a URL "/v/" conferida (OU29) e a página corrigida.
- **Se ganhar / se perder:** regra da seção 0.5.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem já comparou com curso online mais curto e voltou pela busca de marca tende a ter decidido pela pós-graduação; a palavra de intenção alinha o clique com isso [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 6.5 Posicionamento e prova ao redor (68617)

- **Perto do botão:** links para "Quanto do curso é presencial?" (O3: a maior parte é online, e os módulos presenciais são de aula prática) e para "E se a turma não fechar?". `matriz` só depois da correção do dado.
- **Fora:** número da turma, TCC, "instituição reconhecida", "profissionais renomados", "você estará apto", nome de marca (Palladia), bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, superlativos, turma V ou VII, URL "/v/", `matriz`).

---

## 7. Seção 68636: Pós-graduação em Pneumologia Veterinária

### 7.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Pneumologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, as aulas práticas presenciais e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3.
- **Não pedir nem dizer:** nenhuma data nem mês (P3, OU21); nada de "especialidade", "escassez" nem "vácuo" (E14); nenhuma promessa de hands-on nem de volume de procedimentos (a ficha não diz).

### 7.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, as aulas práticas presenciais e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da **variante B** (seção 0.6), enquanto a `matriz` estiver oculta; da variante A quando ela ficar visível. Pergunta sobre a data de início: "Vou confirmar a data com a secretaria e te retorno" (O3, OU21). Pergunta sobre a diferença para ecocardiografia (698): resposta do time, sem comparar valor (O3).

### 7.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, da fisiologia respiratória às intervenções emergenciais.
>
> **Apoio:** Viu o cronograma? Em dúvida entre pneumologia, cardiologia e ventilação mecânica, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 7.4). **Só vale com a `matriz` visível.** Na O3 ela fica oculta até a correção do dado (módulos 16 e 24 com data fora da sequência). Texto de reserva, para a `matriz` oculta (palavras tiradas do hero da O3):

> **Título (reserva):** Veja as aulas práticas presenciais de imagem e endoscopia respiratória.
>
> **Apoio (reserva):** Viu as aulas práticas? Em dúvida entre pneumologia, cardiologia e ventilação mecânica, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão (reserva):** Quero receber o retorno do time (31 caracteres)

### 7.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual.
- **Por quê:** a pergunta que mais trava a turma é "Pneumologia, cardiologia ou ventilação mecânica: qual eu faço?" (O3, ponte A2 [SUPOSIÇÃO]), e o apoio do `cta_final` já promete a explicação do time. Ela se resolve conversando, e "tirar dúvidas" nomeia essa conversa. Risco: o lead dividido com 289 (onda 2, área A2, janela comum); a data só existe no site (OU21), então o time responde "vou confirmar a data com a secretaria".
- **Tempo mínimo:** a janela comum, só com a data confirmada e `local_e_datas` visível. Para ler o efeito sem enganar, o desenho-de-experimentos soma os leads de 68636 e 289 (área A2) antes de comparar os braços.
- **Se ganhar / se perder:** regra da seção 0.5. Se o braço só mover leads de 289 para 68636 sem aumentar o total da área, não conta como vitória.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** quem já decidiu que quer o sistema respiratório (palavra principal da página) não precisa de conversa de dúvida; a palavra de intenção pode filtrar quem ainda compara as três turmas da área [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, com sorteio por visitante nas 13 páginas, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 7.5 Posicionamento e prova ao redor (68636)

- **Perto do botão:** links para "Vou ver endoscopia e imagem na prática?" (O3: ultrassonografia pulmonar, laringotraqueobroncoscopia e rinoscopia entre os módulos presenciais) e para "E se a turma não fechar?" (a ficha de 68636 já diz que a compra de passagem e hotel é só depois da confirmação da turma). `matriz` só depois da correção do dado.
- **Fora:** data, "especialidade", "escassez de especialistas", "à altura desse desafio", "não é uma extensão da clínica geral", a frase de aulas não transmitidas (a ficha de 68636 não a traz), bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (certificação, turma mínima, superlativos, data confirmada, `matriz`).

---

## 8. Seção 68609: Pós-graduação em Anestesiologia Veterinária

### 8.1 Formulário (`formulario`)

> **Título:** Tire suas dúvidas sobre a Pós-graduação em Anestesiologia Veterinária
>
> **Apoio:** Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, a prática presencial e as condições da turma, e orientar a inscrição.

- **Rótulos, campos e caixas de aceite:** seção 0.3.
- **Botão (controle):** Quero receber o retorno do time (31 caracteres).
- **Frase de risco, finalidade e link da política:** textos da seção 0.3 (link [CONFIRMAR]).
- **Mensagem de erro de envio:** seção 0.3; o WhatsApp da página é o de vendas de Goiânia, vindo do dado.
- **Não pedir nem dizer:** nada de prova ou título de Especialista (E13, OU31); nenhuma pergunta de experiência prévia (a ficha traz só o público "Médicos Veterinários que querem atuar na anestesiologia veterinária clínica"); nome do curso no singular, nunca "Anestesiologias Veterinárias"; nenhuma cidade em texto (CP1).

### 8.2 Mensagem de confirmação

> **Recebemos seus dados.**
>
> O time de vendas da Faculdade Ufape retorna pelo WhatsApp informado para responder suas dúvidas sobre o cronograma, a prática presencial e as condições da turma, e para orientar a inscrição.

Mais as linhas comuns da **variante B** (seção 0.6), enquanto a `matriz` estiver oculta; da variante A quando ela ficar visível. Pergunta sobre a prova de Especialista: secretaria, sem texto (E13, OU31).

### 8.3 CTA final (`cta_final`)

> **Título:** Veja o cronograma, da avaliação pré-anestésica aos pacientes especiais.
>
> **Apoio:** Viu o cronograma? Em dúvida entre as pós-graduações de anestesiologia, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão:** Quero receber o retorno do time (31 caracteres)

Igual à O3 (seção 8.4). **Só vale com a `matriz` visível.** Na O3 ela fica oculta até a correção do dado (frase de carreira no módulo 1 e módulo 17 em data anterior à do 16). Texto de reserva, para a `matriz` oculta (palavras tiradas do `sobre` da O3):

> **Título (reserva):** Veja a prática presencial, do pré-anestésico à reanimação.
>
> **Apoio (reserva):** Viu a prática presencial? Em dúvida entre as pós-graduações de anestesiologia, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança.
>
> **Botão (reserva):** Quero receber o retorno do time (31 caracteres)

### 8.4 Variações de botão e hipóteses

Regras comuns: seção 0.5.

**V1: "Quero tirar minhas dúvidas" (26 caracteres)**

- **Mudança:** o botão do hero, do formulário e do `cta_final` passa de "Quero receber o retorno do time" para "Quero tirar minhas dúvidas". Nada mais muda.
- **Efeito previsto:** taxa de envio acima do controle; inscrição paga por lead igual.
- **Por quê:** o `faq` abre com "Quero entrar na anestesia. Preciso já ser anestesista?" (O3 [SUPOSIÇÃO]) e traz "Anestesiologia, avançada ou locorregional: qual eu faço?". São dúvidas de entrada e de comparação, que o botão de dúvida acolhe melhor do que o pedido de retorno de vendas. Risco: a pergunta de experiência prévia só tem a resposta do público da ficha, e o time de Goiânia precisa estar pronto para a diferença entre as turmas da área (O7, plano).
- **Tempo mínimo:** a janela comum, com a página corrigida (OB1) e sem o convite da prova de Especialista. Leitura de apoio com 657 (onda 2, área A1), cujos leads somam com os de 68609 antes de comparar os braços; 359 entra só no lote B.
- **Se ganhar / se perder:** regra da seção 0.5. Se o braço só mover leads de 657 para 68609 sem aumentar o total da área, não conta como vitória.

**V2: "Quero me inscrever" (18 caracteres), suspenso até a confirmação da seção 0.4**

- **Mudança:** o botão passa para "Quero me inscrever". Nada mais muda.
- **Efeito previsto:** igual ou menos envios; inscrição paga por lead acima do controle.
- **Por quê:** 68609 tem o menor total do lote A (catálogo), o que baixa a barreira de decisão; uma palavra de intenção pode alinhar o clique com quem já escolheu a anestesiologia clínica [SUPOSIÇÃO].
- **Tempo mínimo:** a janela comum, se o braço for liberado.
- **Se ganhar / se perder:** regra da seção 0.5.

### 8.5 Posicionamento e prova ao redor (68609)

- **Perto do botão:** links para "Vou praticar ou só assistir?" (O3: hands-on e prática presencial entre os módulos, com acompanhamento individualizado no presencial, como na ficha) e para "E se a turma não fechar?". `matriz` só depois da correção do dado.
- **Fora:** prova ou título de Especialista, "extrema importância", "alto grau de informações", "formar veterinários capazes", "do anestesista volante ao chefe de setor", marcas de terceiros (RECOVER, ROTEM, Xlung, VetPain), bloco de bolsa, certificado, depoimento, nota.
- **Pedido ao editor:** trocar o botão do hero pelo texto do braço sorteado.
- **A página só vale com a OB1 feita** (título no singular, convite da prova de Especialista retirado, certificação, turma mínima, superlativos, `matriz`).

---

## 9. 662: registro de espera (OU18)

Nenhum formulário nem `cta_final` foi escrito para 662, porque a O3 não escreveu a página (espera total até a Ufape responder OU18: 24/04/2027 é turma nova de Ortopedia ou o módulo 9 da turma IV, e qual é a ficha de 2027). Quando a resposta chegar, o plano prevê ciclo extra com a página de 662 em nova versão da O3 e, a seguir, nova versão deste arquivo com a seção de 662, no mesmo formato e com os mesmos blocos comuns da seção 0. O teste de botão só inclui 662 se a página estiver no ar antes de 04/01.

---

## 10. Autochecagem (auditorias/08-conversao.md e auditorias/conformidade-educacional.md)

| Item | Situação |
|---|---|
| Uma chamada principal por página | Sim: hero, formulário e `cta_final` pedem a mesma ação; WhatsApp é secundário |
| Formulário pede só o necessário | Sim: nome e WhatsApp obrigatórios; e-mail opcional; lista do que não se pede na seção 0.3; a pergunta de interesse do checklist da O3 sai (seção 0.8, linha 5) |
| Finalidade do uso dos dados e link da política | Texto pronto; **endereço da política [CONFIRMAR]**, que bloqueia a publicação do formulário |
| WhatsApp e e-mail só com aceite e saída fácil | Sim: caixas separadas, desmarcadas, SAIR no WhatsApp e link de descadastro no e-mail |
| Quem não marca a caixa recebe só o retorno e não entra em S2 e S3 (E21, Q56) | Sim, seção 0.3 |
| Mensagem de erro manda ao time, não à secretaria (Q57) | Sim, seção 0.3 |
| Texto de botão que não engana | Sim: o controle diz "receber o retorno do time"; "Quero me inscrever" fica suspenso (Q58 e Q59) |
| Contagem de cada botão escrita | Sim: 31, 26 e 18, com a soma letra por letra na seção 0.4 e a contagem junto de cada botão |
| Urgência real | Nenhuma urgência, escassez ou prazo em botão, título, apoio ou confirmação; regra do 3º módulo fora de todo texto deste arquivo |
| Sem MEC, certificado, bolsa, desconto, promoção, prova de Especialista | Sim, nas 8 turmas |
| Travas por turma (P3 e OU19 em 679; regra 8, OU3 e OU34 em 68632; OU35 em 68635; P4 e OU20 em 366; P5 em 68628 e 68617; P3 e OU21 em 68636; E13 e OU31 em 68609) | Sim |
| Regra 8 em 68632: nada sobre entrada depois do início | Sim: nenhuma menção em formulário, confirmação, `cta_final` ou resposta pronta |
| Sem número, preço, data, local nem nome de docente no texto da página | Sim nos blocos de citação (conferido na escrita; "um" e "uma" não aparecem; o qa confirma por script) |
| Textos de apoio do formulário e do `cta_final` iguais aos da O3 | Sim: palavra por palavra; trocas pedidas à O3 na seção 0.8 |
| `cta_final` sem apontar para bloco oculto | Sim, com texto de reserva nas quatro turmas com `matriz` oculta (seções 5.3, 6.3, 7.3 e 8.3) e confirmação em variante B |
| Dados do curso conferidos com o catálogo | Sim: nenhum dado de curso digitado em texto de página; só nomes padrão do catálogo e comparações de total e de carga horária citadas na análise, com fonte |
| Provas reais e autorizadas | Sim: só o que já está na página; sem depoimento, nota ou selo |
| Objeções respondidas perto do botão | Sim: links para as respostas do `faq` por turma (O3) |
| Testes com hipótese escrita e regra de decisão antes do início | Sim: 16 cartões (2 por turma) e regra comum na seção 0.5, somada com os 10 da onda 2 |
| Resultados registrados, vencedores e perdedores | Prevista na regra de decisão; registro é do desenho-de-experimentos e da analise-cro |
| Eventos de lead e inscrição rastreados | Previsto na seção 0.5, item 4; conferência de ponta a ponta em 11/12 e reconferência em 04/01 (plano) |
| Nenhum dado pessoal | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; a busca final é do orquestrador |

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início, preço total e status "aberto" das 8 turmas: contexto/catalogo-de-cursos.md, seção 2, linhas 79 a 87. Nenhum desses valores está no texto de página. Os comparativos citados só na análise (68628 com o maior total do lote A, R$ 38.940,00; 68609 com o menor, R$ 32.450,00; 68635 com a maior carga horária, 750 h; 366 turma I): mesmo catálogo.
- `formulario` e `cta_final` como seções do tipo pos (texto do botão e uma frase de apoio; título curto e botão) e regra de texto sem número: templates/pagina-da-turma.md.
- Apoio do formulário, título, apoio e botão do `cta_final`, visibilidade de `matriz`, travas por turma, `faq` e checklist de rastreamento das 8 turmas: O3 (saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md), seções 1 a 8, 11.2 e 12.
- Sem linha de reembolso de inscrição na ficha de 679; passagem e hotel "somente após a confirmação oficial" na de 68636; módulo 1 presencial e regra 8 em 68632; 68609 e 68632 em Goiânia: fichas e plano do CMO (seções 1.1 e 2.1).
- Formato dos blocos comuns (campos, caixas, frases de risco e de finalidade, confirmação, mensagem de erro, cartões de hipótese e regra de decisão): arquivo da onda 2 (saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md), com as correções Q56 a Q59 da revisão onda2a.
- Regras E1 a E22, E8, E21, travas por turma, corte da 1ª mensalidade das 8 turmas, páginas no ar em 10/12, mídia de abril em 06/01, conferência de 11/12 e reconferência de 04/01, perguntas OU3, OU4, OU19 a OU21, OU25, OU29 a OU31, OU34 e OU35 e encomenda O5: plano do CMO (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md).
- Decisões 8 (docentes autorizados), 11 (turma mínima 15), 14 (sem bolsa), 16 (inscrição paga e depois 1ª mensalidade; sem valor da inscrição até U11), 18 (matrícula até o 3º módulo) e 20: docs/execucao-2026-10-26.md.
- Contatos oficiais de vendas por praça e razão social: contexto/ufape-geral.md. O endereço da política de privacidade não consta ali nem nas fichas.
- Itens de conformidade (finalidade e link da política, consentimento por canal, página que entrega o que a peça promete, urgência real) e de conversão (uma chamada principal, formulário curto, testes com hipótese): auditorias/conformidade-educacional.md e auditorias/08-conversao.md.

## [SUPOSIÇÃO]

- Que o formulário é só de contato e não cobra nem inicia pagamento (base da frase de risco, de "Nenhuma cobrança foi feita" e de "Enviar seus dados não gera cobrança").
- Que o retorno do time de vendas acontece por WhatsApp (canal principal de venda da Pós, plano do CMO); por isso o WhatsApp é obrigatório e o e-mail é opcional.
- Que o CRM aceita lead sem e-mail e que e-mail opcional não prejudica o fluxo.
- Rótulos, caixas de aceite, título do formulário, texto da confirmação e textos de reserva do `cta_final`: redação deste agente, a validar pela pessoa do marketing e por quem responde pela LGPD. Os textos de reserva usam só palavras do `sobre` e do hero da O3.
- Que "Quero receber o retorno do time" é o melhor controle, e que "Quero tirar minhas dúvidas" reduz o compromisso e "Quero me inscrever" filtra por intenção: hipóteses, sem dado de conversão (não existe linha de base).
- A meta de até 32 caracteres para o botão caber em uma linha no celular.
- Os limiares provisórios de decisão (20% relativos na taxa de envio e queda máxima de 10% relativos na inscrição paga por lead), herdados da onda 2, que o desenho-de-experimentos confirma ou troca.
- Que a janela de 04/01 a 07/02/2027 da onda 2 serve também ao lote A (corta antes de todos os cortes da 1ª mensalidade de abril, 04/03 a 25/03).
- Que a plataforma sorteia por visitante, mantém o braço nas 13 páginas e suporta o parâmetro `cta_variante` no evento de lead e no CRM; que a UTM do nome da campanha separa tráfego frio de remarketing.
- Que a inscrição paga por lead é mensurável por turma e braço, e que a 1ª mensalidade paga não decide o teste por causa do ciclo mais longo.
- Que a diária da mídia, quando mexida na revisão de ritmo, e o feriado de 25/01 sem campanha não alteram a taxa por visitante.
- A ordem de grandeza de 111 a 500 leads por turma (conta da onda 2, herdada; o piso de CPL de R$ 4,00 não aparece no plano da onda 3).
- As hipóteses de persona por turma nos cartões (conciliar agenda em 68632, comparação entre turmas da área em 68635, 68636 e 68609, nicho de curso novo em 366, total alto em 68628, dúvida de formato em 68617 e 679), todas derivadas das perguntas [SUPOSIÇÃO] do `faq` da O3.
- Os nomes dos eventos de rastreamento (herdados da O3).

## [CONFIRMAR]

- **Endereço da política de privacidade da Faculdade Ufape** (não está no ufape-geral nem nas fichas). Sem ele o formulário não passa na conformidade. Pendência já aberta no plano ("endereço da política de privacidade").
- **Texto da finalidade, base legal, retenção, compartilhamento com CRM e provedor de WhatsApp e contato do encarregado:** quem responde pela LGPD na Ufape revisa a frase da seção 0.3 e a política.
- **Pixel da Meta, tag do Google Ads e GA4 no evento de lead:** se há aviso de cookies e como o aceite se aplica a eles.
- **Canal, prazo e horário do retorno do time de vendas** (para a frase da confirmação).
- **Se o formulário não cobra nem gera obrigação** (frase de risco, `cta_final` e confirmação).
- **Se o CRM aceita lead sem e-mail** e a identificação do contato (por WhatsApp).
- **Plataforma:** se aceita o campo `titulo` no formulário, o campo de apoio no `cta_final` e o `botao` no hero (O3 e seção 0.8, linha 1).
- **Ferramenta de teste no site:** sorteio por visitante, braço comum às 13 páginas, parâmetro no evento e no CRM.
- **Texto e número do botão de WhatsApp secundário** de cada praça (a O3 não definiu o texto).
- **Mínimo de leads por braço, limiares, janela para o lote A e leitura somada por área (A1, A2, A4, A11):** desenho-de-experimentos.
- **Visitas e leads reais por turma** (nenhum número existe hoje; sem eles não há linha de base).
- **OU19, OU20 e OU21 (datas de 679, 366 e 68636), P5, OU29 e OU30 (turma e URL de 68617 e 68628), OU31 (68609), OU3 e OU34 (68632), OU35 (68635), OU25, OU14 e OU6:** perguntas já abertas no plano; seguem valendo as travas por turma.
- **OB1:** nenhuma das 8 páginas vale enquanto a frase de certificação, a turma mínima de 20 e os demais itens das listas da O3 (seções 1.6 a 8.6) não forem corrigidos. O formulário e o `cta_final` deste arquivo só entram junto com a página corrigida.
- **Visibilidade da `matriz` de 68628, 68617, 68636 e 68609** no dia da publicação (define se vale o texto da O3 ou o de reserva, e a variante A ou B da confirmação).
- **U11:** valor da inscrição contra a matrícula do site; até a resposta nenhum texto cita valor.
- **Alcance de "valores de inscrição" no reembolso** (matrícula, 1ª mensalidade antecipada), em todas as turmas menos 679.
- **Revisão docente:** conferência técnica dos termos de cada turma nas frases de apoio antes da publicação.
- **Quem aprova** formulário, texto de consentimento e peças com ato regulatório (A9 do plano): [CONFIRMAR quem].

## Próximo agente

**desenho-de-experimentos**: transformar os 16 cartões deste arquivo, mais os 10 da onda 2, e a regra comum da seção 0.5 em um plano único de teste de botão (mínimo de leads por braço, sorteio por visitante nas 13 páginas, janela de 04/01 a 07/02/2027, leitura somada e por área, corte para 2 braços já com V2 suspenso). Antes disso, o qa-de-marketing (O18a, 18/11) revisa este arquivo com as auditorias 08 e de conformidade educacional. Depois da publicação (10/12) e com dados reais, analise-cro.

## Fontes

- /home/user/marketing-ufape/CLAUDE.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/contexto/ufape-geral.md, /home/user/marketing-ufape/contexto/pos-graduacao.md, /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/ (fichas de 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609)
- /home/user/marketing-ufape/templates/pagina-da-turma.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md e /home/user/marketing-ufape/auditorias/08-conversao.md
- /home/user/marketing-ufape/saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md
