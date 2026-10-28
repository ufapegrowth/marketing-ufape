# Pacote de produção do UFAPE Cast para a janela da turma 68606 (Pós-graduação em Gastroenterologia Veterinária)

- **Agente:** podcast (departamento 12, Vídeo e Áudio)
- **Linha:** pos
- **Data:** 28/10/2026 (quarta-feira)
- **Curso e turma:** Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo, código 68606
- **Nome do podcast:** UFAPE Cast, **nome em aprovação** (decisão 21). Se mudar, troque o nome em títulos, capas, cartelas e na abertura falada. Nada mais muda.
- **Métrica que o pacote deve mover:** ouvintes que chegam ao fim (por episódio), visitas à página da 68606 com UTM do podcast, cortes publicados por episódio e seguidores novos. Só números exportados do YouTube, do Spotify e do analytics. Sem meta antes de 4 episódios de linha de base.
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada é gravado, publicado, enviado ou pago a partir deste arquivo.
- **Entradas lidas:**
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 18, 21 e 23)
  - /home/user/marketing-ufape/docs/insumos/ufape-podcast-proposta-2026-10-28.txt (formato, blocos, quadros, pacote, specs, checklist)
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha: módulos e docentes)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md (slides 12 a 14, e o resto para datas, UTM e regras)
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json (linha literal do catálogo)
  - /home/user/marketing-ufape/.claude/skills/conformidade-educacional/SKILL.md e /home/user/marketing-ufape/auditorias/conformidade-educacional.md
- **Não aberto:** faculdade.ufape.com.br e contexto/catalogo-de-cursos.md inteiro (os dados de curso vêm da linha literal do catálogo citada no JSON da 68606 e da ficha). Nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum aluno, tutor, paciente ou egresso é nomeado. Docentes só com nome e titulação como estão na ficha (maiúsculas normalizadas). Só a caixa muda (DR. para Dr.); nome e titulação como na ficha. Mesmo ajuste na apresentação.

---

## 0. Texto fixo reaproveitado em todo o pacote

Estes blocos são copiados sem alteração onde indicados. Mudou aqui, muda em toda peça.

**[CHAMADA-TURMA]** (obrigatória em toda chamada à turma depois de 07/11/2026, decisão 18, texto do pedido):

> A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.

**[LINK-TURMA]** (UTM do plano do cmo, slide 13; só o `utm_content` muda por episódio):

```
https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=<youtube|spotify|instagram>&utm_medium=organic_social&utm_campaign=pos_68606_202610&utm_content=ufapecast_ep01
```

- O `utm_campaign` é `pos_68606_202610` em todo episódio com chamada da turma (regra 11 do cmo-pos). Episódio sem chamada de turma usa `pos_conteudo_<AAAAMM>` [CONFIRMAR com o arquiteto-de-fluxos].
- Link testado antes de publicar. O tráfego do Spotify usa `utm_medium=organic_social` por seguir o plano do cmo [CONFIRMAR com o arquiteto-de-fluxos se áudio pede outro medium].

**[ABERTURA-FALADA]** (apresentador, da proposta): "Bem-vindo ao UFAPE Cast, o podcast da Faculdade UFAPE sobre conhecimento e prática em Medicina Veterinária." Assinatura fixa: "Um podcast da Faculdade UFAPE."

**[AVISO-OPINIÃO]** (descrição e fechamento de todo episódio): "As opiniões e experiências relatadas são dos convidados. Este conteúdo é educativo e não substitui a avaliação clínica de um caso."

**Regras de toda peça do pacote (valem para fala, tela, capa, legenda e descrição):**

1. Opinião é do convidado. A squad escreve só perguntas, temas e frases institucionais. Nenhuma frase deste arquivo é para ser dita pelo convidado.
2. Conteúdo clínico leva **[REVISÃO DOCENTE]**: a pauta, a edição final e a legenda do corte passam por revisão do próprio docente ou de um revisor docente [CONFIRMAR nome]. Dose, protocolo e conduta nunca saem em texto da squad.
3. Nenhum paciente, tutor, aluno ou clínica identificável: sem nome, foto, voz, prontuário, exame com identificação, placa, tela de sistema. Casos só anônimos, contados pelo convidado.
4. Sem promessa de emprego, renda, posição, aprovação ou resultado. Sem "garantia".
5. Sem frase de certificação e sem "MEC". O texto oficial ainda não existe.
6. Sem preço, parcela ou valor de inscrição nas peças do podcast (a página da turma traz a condição completa). Sem bolsa nem prova de bolsa.
7. Sem urgência falsa, contador, "últimas vagas". A data do 3º módulo só aparece dentro da [CHAMADA-TURMA] completa.
8. Sem afirmar ou insinuar característica pessoal de quem assiste (situação financeira, saúde, emprego, idade). Títulos e legendas são perguntas ou fatos da pauta.
9. O curso se chama sempre "Pós-graduação em Gastroenterologia Veterinária". A palavra "pós" sozinha só aparece como termo genérico em pergunta ("Como escolher minha pós?"), nunca como nome de curso.
10. Não usar "especialidade emergente e carente de profissionais" nem "coordenadores referências nacionais" (textos da página sem fonte). Não citar número de turma mínima.
11. Sem travessão nem meia-risca em nenhum texto, inclusive na tela e nas legendas.

---

## 1. Plano da série

| Item | Definição |
|---|---|
| Nome | UFAPE Cast (em aprovação), subtítulo "Conhecimento e prática em Medicina Veterinária" |
| Formato | episódio gravado, quinzenal, 35 a 45 minutos (decisão 21), vídeo e áudio |
| Plataformas | YouTube (episódio completo em playlist de podcast; Shorts e cortes em listas próprias) e Spotify (áudio; vídeo no Spotify é expansão opcional). Apple Podcasts: por RSS, só se a Ufape quiser [CONFIRMAR] |
| Janela | 5 episódios de 24/11/2026 a 19/01/2027, mais 1 reserva em 02/02/2027. Pausa de campanha da 68606 em 22/01/2027 |
| Frequência | 1 episódio a cada 14 dias, às terças, regra prática e não meta. Sessões de gravação com 2 episódios para caber na agenda dos docentes [SUPOSIÇÃO] |
| Quadros | "Formação em foco" (ep. 1 e reserva), "Ciência e prática" (ep. 2, 4 e 5), "Comunidade UFAPE" (ep. 3) |
| Público do pacote | médico veterinário formado que avalia especialização (terceiro grupo da proposta: "quem quer ir além") |
| Papel no funil | consideração: o episódio leva à página da turma com UTM; o time de vendas explica a regra do 3º módulo |
| Apresentador | [CONFIRMAR quem apresenta e quem grava, edita e publica, e quantas horas por semana] |

**Estrutura do roteiro de cada episódio (proposta, página 21):** gancho e abertura (0 a 2 min), história do convidado (2 a 10), conversa principal (10 a 28), pergunta da comunidade (28 a 35), vida na UFAPE (35 a 40), fechamento (40 a 45). Não é preciso preencher todos os tempos.

**Pacote por episódio (decisão 21):** episódio completo no YouTube, áudio no Spotify, miniatura horizontal (3840 x 2160) e capa quadrada (3000 x 3000), mais 3 cortes verticais com legenda (1080 x 1920), 3 capas verticais, 1 card 4:5 (1080 x 1350), 2 Stories (1080 x 1920) e 1 card do convidado (1080 x 1080). Tarjas de todos os participantes, legendas revisadas em SRT, créditos e capítulos.

**Nomes de arquivo (proposta, página 23):** `UFAPECAST_EP01_YT_CAPA_v01.jpg`, `UFAPECAST_EP01_CORTE1_9x16_v01.mp4`. Matriz de áudio em WAV, publicação em MP3, vídeo MP4 1920 x 1080 a 30 quadros.

---

## 2. Episódio 1 completo

### 2.1 Ficha do episódio

- **Número e quadro:** Ep. 01, quadro "Formação em foco".
- **Pergunta central (de quem avalia uma pós):** como escolher a pós-graduação certa para a minha rotina?
- **Data de publicação:** terça, 24/11/2026 [SUPOSIÇÃO de calendário, depende do nome aprovado e da produção].
- **Convidados:**
  - Esp. Maria Carolina Pappalardo, coordenação da Pós-graduação em Gastroenterologia Veterinária (nome e titulação como na ficha). Autorização de imagem e citação: registrada (decisões 8 e 10).
  - Egresso de pós da Ufape: [CONFIRMAR nome, de qual pós, e autorização de imagem, voz e citação]. Sem a autorização registrada, o episódio sai só com a coordenação. Relato de egresso é depoimento: além do termo assinado de imagem, voz e citação, o episódio com egresso passa pela aprovação de "Peças com certificação, ato regulatório ou depoimento" de contexto/ufape-geral.md (responsável e regulação, hoje [CONFIRMAR]). Sem as duas coisas, o ep. 1 sai só com a coordenação, e a descrição, os títulos, o Story e o card tiram toda menção ao egresso.
- **Apresentador:** [CONFIRMAR].
- **O que o ep. 1 serve:** todas as turmas de Pós. A chamada aponta para a 68606.

### 2.2 Títulos

| Plataforma | Título (limite sugerido) | Observação |
|---|---|---|
| YouTube | Como escolher minha pós-graduação? Conversa com a coordenação e um egresso | UFAPE Cast #01 (a caber em 100 caracteres: "Como escolher minha pós-graduação? | UFAPE Cast #01") |
| YouTube (título final recomendado) | Como escolher minha pós-graduação? | UFAPE Cast #01 | 49 caracteres, pergunta que a pessoa busca |
| Spotify | #01 Como escolher minha pós-graduação? com Esp. Maria Carolina Pappalardo | número primeiro, para ordenar a lista |
| Miniatura YouTube (texto, 3 a 6 palavras) | Qual pós combina comigo? | foto real da coordenação (e do egresso, se autorizado); selo "UFAPE Cast Ep. 01" |
| Capa quadrada (Spotify e playlist) | UFAPE Cast | Ep. 01 | Como escolher minha pós? | subtítulo "Conhecimento e prática em Medicina Veterinária" |

### 2.3 Descrição do YouTube

```
Como escolher minha pós-graduação? Neste primeiro episódio do UFAPE Cast, o podcast da Faculdade UFAPE sobre conhecimento e prática em Medicina Veterinária, a coordenação da Pós-graduação em Gastroenterologia Veterinária e um egresso de pós da Ufape conversam sobre as perguntas de quem avalia uma especialização: o que comparar, como é a rotina de estudo, o que olhar no cronograma e quem ensina.

Conheça a Pós-graduação em Gastroenterologia Veterinária (turma IX, São Paulo):
https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=youtube&utm_medium=organic_social&utm_campaign=pos_68606_202610&utm_content=ufapecast_ep01

A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.

CAPÍTULOS
00:00 Abertura e pergunta do episódio
02:00 A história da coordenação: como chegou à especialidade
06:00 A história do egresso: como decidiu fazer uma pós
10:00 O que comparar antes de escolher uma pós
14:00 Rotina e formato: como conciliar o estudo com a clínica
18:00 Prática e quem ensina: o que conferir antes da matrícula
22:00 Pós, residência, curso curto ou aprender com um colega
25:00 Dúvidas antes de pagar
28:00 A pergunta da comunidade
35:00 Vida na UFAPE: como funciona um módulo
40:00 Fechamento e chamada

QUEM PARTICIPA
- Esp. Maria Carolina Pappalardo, coordenação da Pós-graduação em Gastroenterologia Veterinária.
- Egresso de pós da Ufape: [CONFIRMAR nome e autorização].
- Apresentação: [CONFIRMAR].

SOBRE ESTE EPISÓDIO
Perguntas abordadas: como comparar opções de especialização; o que observar no cronograma, nos módulos presenciais e no corpo docente; como funciona a rotina de módulos aos fins de semana; quando uma pós, uma residência, um curso curto ou a troca com um colega podem fazer sentido; que dúvidas levar ao time antes de pagar.
Informações do curso conferidas com a ficha da turma em 28/10/2026.

As opiniões e experiências relatadas são dos convidados. Este conteúdo é educativo e não substitui a avaliação clínica de um caso.

Transcrição revisada e legendas (SRT): [CONFIRMAR onde será publicada].
Siga o UFAPE Cast no YouTube e no Spotify.
Um podcast da Faculdade UFAPE.
Créditos: edição, trilha e licenças [CONFIRMAR].
```

Notas de produção da descrição: os tempos dos capítulos são [SUPOSIÇÃO] e serão ajustados à edição final (o YouTube exige o primeiro capítulo em 00:00, ao menos 3 capítulos e 10 segundos por capítulo). O bloco "Sobre este episódio" lista perguntas, não respostas, para não escrever opinião no lugar de ninguém.

### 2.4 Descrição do Spotify

```
Como escolher minha pós-graduação? A coordenação da Pós-graduação em Gastroenterologia Veterinária, Esp. Maria Carolina Pappalardo, e um egresso de pós da Ufape [CONFIRMAR] conversam sobre as dúvidas de quem avalia uma especialização: o que comparar, como é a rotina de módulos, o que olhar no cronograma e quem ensina.

Página da turma IX, São Paulo: https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=spotify&utm_medium=organic_social&utm_campaign=pos_68606_202610&utm_content=ufapecast_ep01

A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.

Capítulos: 00:00 Abertura | 02:00 A história da coordenação | 06:00 A história do egresso | 10:00 O que comparar | 14:00 Rotina e formato | 18:00 Prática e quem ensina | 22:00 Pós, residência, curso curto ou colega | 25:00 Dúvidas antes de pagar | 28:00 Pergunta da comunidade | 35:00 Vida na UFAPE | 40:00 Fechamento.

As opiniões e experiências relatadas são dos convidados. Este conteúdo é educativo e não substitui a avaliação clínica de um caso.
UFAPE Cast, um podcast da Faculdade UFAPE.
```

Áudio: o episódio precisa fazer sentido sem imagem. O apresentador fala nome e função de cada pessoa e explica o que aparece em tela.

### 2.5 Roteiro por bloco

Legenda: **FALA INSTITUCIONAL** é texto da Ufape e pode ser lido como está. **PERGUNTAS** são da squad, para o apresentador. **TRAZER** é o que se pede ao convidado que traga, sem escrever a resposta.

#### Bloco 1. Gancho e abertura (00:00 a 02:00)

- **Gancho (montado na edição):** um trecho curto do próprio convidado, escolhido depois da gravação, com o ok dele, mais o título na tela "Como escolher minha pós?". Trecho: [escolher na edição].
- **FALA INSTITUCIONAL:** [ABERTURA-FALADA] "Hoje a pergunta é: como escolher minha pós-graduação? Comigo, a Esp. Maria Carolina Pappalardo, coordenação da Pós-graduação em Gastroenterologia Veterinária, e um egresso de pós da Ufape." (nome do egresso [CONFIRMAR]).
- **PERGUNTA de abertura (para os dois):** o que vocês gostariam de saber antes de escolher uma pós?
- **Tela:** cartela do episódio (3 a 5 s), tarjas de nome e função na primeira fala.

#### Bloco 2. História do convidado (02:00 a 10:00)

- **PERGUNTAS para a coordenação (02:00 a 06:00):**
  1. Como foi o seu caminho até a especialidade?
  2. Quando você olha para trás, o que gostaria de ter perguntado antes de escolher uma formação?
  3. O que você mais ouve de quem está avaliando uma pós?
- **PERGUNTAS para o egresso (06:00 a 10:00):**
  1. Como foi a sua decisão de fazer uma pós?
  2. O que você comparou e como decidiu?
  3. Como foi conciliar o curso com a rotina?
  4. O que você perguntaria hoje a quem está nessa fase?
- **TRAZER:** uma situação vivida (sem nome de pessoa, tutor, paciente ou clínica) que mostre como a decisão foi tomada. O apresentador não pede, nem aceita, relato de ganho de renda, emprego ou posição. Se vier, o trecho sai na edição.

#### Bloco 3. Conversa principal (10:00 a 28:00)

- **3A. O que comparar (10:00 a 14:00)**
  1. Que critérios ajudam a comparar duas opções de pós?
  2. Quais perguntas vale levar ao time da instituição antes de decidir?
- **3B. Rotina e formato (14:00 a 18:00)**
  3. Como é, na prática, conciliar módulos de fim de semana com a rotina de clínica?
  4. Que cuidado de planejamento vocês recomendam a quem vem de outra cidade?
- **3C. Prática e quem ensina (18:00 a 22:00)**
  5. O que olhar no cronograma de uma pós antes de pagar?
  6. Por que o formato (online e presencial) e a data da prática entram na escolha?
  7. Onde um candidato pode conhecer quem vai ensinar antes da matrícula?
- **3D. Pós, residência, curso curto ou aprender com um colega (22:00 a 25:00)**
  8. Em que situações cada caminho faz sentido? (Sem comparar com instituição concorrente pelo nome e sem afirmar que um caminho é melhor.)
- **3E. Dúvidas antes de pagar (25:00 a 28:00)**
  9. Que dúvidas vale esclarecer com o time antes de pagar e de assinar qualquer contrato?
- **TRAZER:** exemplos anônimos da rotina do convidado. Termos técnicos explicados em uma frase para quem só escuta.
- **Para o apresentador:** estas perguntas alimentam os 3 cortes (seção 2.7). Pedir respostas completas e autocontidas nos trechos 3B, 3C e 3D, que são os trechos-alvo.
- **[REVISÃO DOCENTE]:** só se a conversa entrar em conduta clínica (não é o objetivo deste episódio).

#### Bloco 4. Pergunta da comunidade (28:00 a 35:00)

- **Como a pergunta chega:** caixa de perguntas nos Stories e formulário curto da Ufape, abertos de 09/11 a 17/11 [SUPOSIÇÃO de prazo]. A pergunta é lida sem nome, sem cidade e sem curso de quem enviou. Sem consentimento do remetente, nada identifica a pessoa. [CONFIRMAR formulário com política de privacidade (pendência p04)]. A caixa de perguntas do Instagram mostra o perfil de quem enviou: o perfil nunca vai para arquivo de trabalho, planilha ou chat da squad; a triagem copia só o texto da pergunta. O formulário só abre com finalidade escrita e link da política de privacidade. Sem isso até a véspera da abertura, o ep. 1 usa a pergunta de reserva e o bloco 4 não abre formulário.
- **Pergunta escolhida:** [CONFIRMAR, vem da comunidade].
- **Pergunta de reserva (se nenhuma chegar)** [SUPOSIÇÃO, não atribuir a ninguém, dizer "uma dúvida comum de quem avalia uma pós"]: "Dá para conciliar uma pós com a rotina de clínica?"
- **PERGUNTAS de aprofundamento:** o que você diria a quem tem essa dúvida? Que exemplo anônimo ilustra? Que informação a pessoa pode pedir ao time para decidir?
- **FALA INSTITUCIONAL:** "A pergunta veio da comunidade da Faculdade UFAPE."

#### Bloco 5. Vida na UFAPE (35:00 a 40:00)

- **FALA INSTITUCIONAL (somente dados da ficha, lidos pelo apresentador):** "A Pós-graduação em Gastroenterologia Veterinária, turma IX, em São Paulo, é semipresencial, com 500 horas e 24 módulos. O módulo 1 foi em 07 e 08 de novembro de 2026. Os módulos práticos presenciais acontecem nos módulos 6, 13 e 21." (fonte: ficha 68606; sem preço, sem frase de certificação).
- **PERGUNTAS para a coordenação:**
  1. Como é a rotina de um módulo online e a de um módulo presencial?
  2. O que o aluno encontra no grupo de discussão de casos descrito na página? (a descrição vem da página; a resposta é da coordenação)
  3. Como funciona a avaliação ao longo do curso?
- **TRAZER:** uma descrição de um módulo (tema, formato), sem relatar paciente.
- **Não perguntar nem afirmar:** regra de entrada depois do início (é fala do apresentador); reposição de módulos (OU3 em aberto), data final de matrícula além da regra oficial, número de vagas, turma mínima.

#### Bloco 6. Fechamento (40:00 a 45:00)

- **PERGUNTA final para os dois:** que conselho vocês dão a quem está comparando caminhos de formação? (a resposta é de cada um)
- **FALA INSTITUCIONAL (chamada, uma ação por momento):** "Se você quer conhecer a Pós-graduação em Gastroenterologia Veterinária, o link da página da turma está na descrição. A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram."
- **Cartela de encerramento (5 a 10 s):** "Siga o UFAPE Cast no YouTube e no Spotify. Um podcast da Faculdade UFAPE." (chamada de inscrição como segundo momento, depois da chamada da turma).
- **Tela final do YouTube (últimos 15 a 20 s):** espaço para o episódio 2, a playlist e a inscrição.
- **[AVISO-OPINIÃO]** em áudio, em uma frase, no fim.

### 2.6 Pergunta da comunidade (resumo operacional)

| Passo | O quê | Quando |
|---|---|---|
| 1 | Abrir caixa de perguntas nos Stories e formulário com política de privacidade | 09/11 a 17/11 [SUPOSIÇÃO] |
| 2 | Triagem: tirar qualquer dado pessoal, caso identificável e pedido de conduta clínica sobre caso real | 18/11 |
| 3 | Escolher 1 pergunta e avisar a coordenação | antes da gravação |
| 4 | Ler no ar sem nome | gravação |

### 2.7 Pacote do episódio 1

#### Os 3 cortes verticais (1080 x 1920, MP4, legenda queimada e SRT)

Em todo corte: começo compreensível, 45 a 60 segundos [SUPOSIÇÃO, regra prática], tarja com nome e função, legenda fiel à fala (revisada), assinatura discreta "UFAPE Cast", cartela final de 3 a 5 segundos com "Conversa completa no UFAPE Cast. Link na legenda." Cortes com a data do 3º módulo só se carregarem a [CHAMADA-TURMA] completa; por isso a data fica na legenda do post.

| # | Trecho-alvo (bloco e pergunta) | Título na tela (3 a 6 palavras) | Legenda do post | Dia sugerido |
|---|---|---|---|---|
| 1 | Bloco 3C, resposta à pergunta 5 ("O que olhar no cronograma de uma pós antes de pagar?"), cerca de 20:00 a 21:00 [SUPOSIÇÃO, ajustar à gravação] | O que olhar no cronograma? | "O que olhar no cronograma antes de pagar uma pós? A coordenação da Pós-graduação em Gastroenterologia Veterinária responde no UFAPE Cast, ep. 01. Episódio completo no YouTube e no Spotify (link na bio). Página da turma: [LINK-TURMA]. [CHAMADA-TURMA]. As opiniões são dos convidados." | ter 24/11 |
| 2 | Bloco 3C, resposta à pergunta 6 ("Por que o formato e a data da prática entram na escolha?"), cerca de 21:00 a 22:00 [SUPOSIÇÃO] | Prática presencial pesa na escolha? | "Prática presencial com data: pesa na escolha de uma pós? Trecho do UFAPE Cast, ep. 01. Episódio completo no YouTube e no Spotify. Página da turma: [LINK-TURMA]. [CHAMADA-TURMA]. As opiniões são dos convidados." | qui 26/11 |
| 3 | Bloco 3C, resposta à pergunta 7 ("Onde conhecer quem vai ensinar antes da matrícula?"), cerca de 22:00 a 23:00 [SUPOSIÇÃO] | Como conhecer quem ensina? | "Quem vai te ensinar: onde ver isso antes da matrícula? Trecho do UFAPE Cast, ep. 01, com a coordenação da Pós-graduação em Gastroenterologia Veterinária. Episódio completo no YouTube e no Spotify. Página da turma: [LINK-TURMA]. [CHAMADA-TURMA]. As opiniões são dos convidados." | ter 01/12 |

Os trechos-alvo são perguntas, não frases. O que o convidado responde é dele. Se a resposta gravada sair fraca, trocar pelo melhor trecho da mesma pergunta ou do bloco 3D, mantendo o título em forma de pergunta. [REVISÃO DOCENTE] se algum trecho tocar em conduta clínica.

#### As 3 capas verticais (uma por corte; 2160 x 3840 para Shorts, 1080 x 1920 para Reels)

Poucas palavras, marca legível, respiro ao redor, foto real autorizada (coordenação) na área de foto.

| Capa | Linha de cima | Texto central | Linha de baixo |
|---|---|---|---|
| 1 | UFAPE CAST | EP. 01 | O que olhar no cronograma? | Esp. Maria Carolina Pappalardo |
| 2 | UFAPE CAST | EP. 01 | Prática presencial pesa na escolha? | Esp. Maria Carolina Pappalardo |
| 3 | UFAPE CAST | EP. 01 | Como conhecer quem ensina? | Esp. Maria Carolina Pappalardo |

(O "|" separa linhas da arte, não é travessão.) Se o egresso aparecer no trecho, entra a segunda tarja só com a autorização registrada.

#### O card 4:5 (1080 x 1350)

- **Função:** anúncio do episódio com tema e dia, publicado como Story (C6, decisão D-G do qa), nunca no feed. Uso em remarketing Meta só com aprovação, trocando uma peça e não somando (AP-4 do plano do cmo).
- **Texto na arte:**
  - Topo: UFAPE CAST | EP. 01
  - Centro: Como escolher minha pós?
  - Subtítulo: Com Esp. Maria Carolina Pappalardo e um egresso de pós da Ufape [CONFIRMAR]
  - Faixa: No ar terça, 24/11, no YouTube e no Spotify
  - Rodapé pequeno: Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo. A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.
- **Legenda do post:** "Como escolher minha pós? Terça, 24/11, no UFAPE Cast, o podcast da Faculdade UFAPE. Conversa com a coordenação da Pós-graduação em Gastroenterologia Veterinária e um egresso de pós da Ufape. Página da turma: [LINK-TURMA]. [CHAMADA-TURMA]. As opiniões são dos convidados."
- **Dia sugerido:** ter 24/11, em formato de Story (C6); como anúncio de remarketing só pelo AP-4.

#### Os 2 Stories (1080 x 1920)

| Story | Texto na tela | Elementos | Dia |
|---|---|---|---|
| 1. Estreia | "No ar hoje: UFAPE Cast, ep. 01. Como escolher minha pós? Com Esp. Maria Carolina Pappalardo." | capa vertical 1, trecho de 6 a 10 s do corte 1 com legenda, figurinha de link para o YouTube, sem contador | ter 24/11 |
| 2. Link | "Ouça no Spotify ou veja no YouTube. Pós-graduação em Gastroenterologia Veterinária, turma IX. A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram." | figurinha de link para a página da turma com UTM `instagram`; texto da regra em corpo legível (pode ocupar duas telas curtas do mesmo Story) | qui 26/11 |

Cada Story tem uma ação só: o 1 leva ao episódio, o 2 leva à página da turma.

#### O card do convidado (1080 x 1080)

- **Texto na arte:** "Convidada do UFAPE Cast, ep. 01" | "Esp. Maria Carolina Pappalardo" | "Coordenação da Pós-graduação em Gastroenterologia Veterinária" | "Como escolher minha pós? No ar em 24/11."
- **Foto:** real, da coordenação, com autorização registrada (decisões 8 e 10). Foto escolhida: [CONFIRMAR].
- **Uso:** perfil da Ufape e, se ela quiser, o perfil pessoal dela (com o ok dela). Conta como 1 post de docente do kit junto com o corte com o nome dela, pelo checklist C1 a C8 da autoridade-docente (critério do qa de 28/10/2026).
- **Dia sugerido:** qua 25/11.
- **Egresso:** sem card próprio nesta versão. Se o egresso quiser e autorizar por escrito, entra um card só com "Egresso de pós da Ufape" e nome autorizado [CONFIRMAR].

#### Frases para posts (texto da Ufape, sem opinião de convidado)

- "Qual pós combina comigo? O ep. 01 do UFAPE Cast começa por essa pergunta."
- "Antes de pagar, leve perguntas ao time. O ep. 01 sugere por onde começar." Só publicar depois de conferir a frase com a edição final [REVISÃO].
- "Rotina de módulos, cronograma, prática e quem ensina: os temas do ep. 01."

#### Miniatura e capa quadrada

- **Miniatura YouTube (3840 x 2160, JPG até 2 MB):** foto real da coordenação, texto "Qual pós combina comigo?", selo UFAPE Cast, testada em tamanho pequeno.
- **Capa quadrada (3000 x 3000):** "UFAPE CAST | EP. 01 | Como escolher minha pós?"; subtítulo "Conhecimento e prática em Medicina Veterinária".

### 2.8 Conformidade do episódio 1 (skill conformidade-educacional, itens aplicáveis)

| Item da auditoria | Situação |
|---|---|
| Nome, modalidade, carga horária e turma batem com catálogo e ficha | Sim: Pós-graduação em Gastroenterologia Veterinária, semipresencial, 500 h, turma IX, São Paulo (linha literal do catálogo no JSON da 68606 e ficha) |
| Status "aberto" no catálogo e exceção do início | Sim: aplicada a decisão 18, com a regra completa em toda chamada |
| Frase de certificação, "MEC", nota | Nenhuma |
| Promessa de emprego, salário, resultado | Nenhuma; apresentador instruído a cortar relato de ganho |
| Preço, bolsa | Nenhum |
| Urgência | Só a data do 3º módulo, dentro da regra completa; sem contador, sem "últimas vagas" |
| Autorização de imagem e voz | Coordenação: registrada. Egresso: [CONFIRMAR] |
| Paciente, tutor, aluno identificável | Proibido na pauta e no checklist |
| Característica pessoal de quem assiste | Nenhuma; títulos em forma de pergunta |
| Formulário da pergunta da comunidade com política de privacidade | [CONFIRMAR] (p04) |
| Página de destino entrega o prometido | Pendente externo (OA10: a página ainda usa a frase ligada ao MEC e não traz a regra do 3º módulo); por isso a regra completa acompanha o link |

Veredito do agente podcast: reduz o risco, sujeito ao qa-de-marketing e à aprovação humana. Pede também revisão humana da regulação: o texto de certificação e a página de destino.

---

## 3. Episódios 2 a 5

Convenções: perguntas feitas pelo apresentador; as respostas são dos convidados. Todo episódio usa a estrutura de blocos da seção 1, com a pergunta da comunidade (28 a 35 min), a "Vida na UFAPE" (35 a 40) e o fechamento (40 a 45) no mesmo molde do ep. 1. O pacote por episódio é o da decisão 21 (3 cortes, 3 capas, 1 card 4:5, 2 Stories, 1 card do convidado). Os dias de publicação seguem o calendário da seção 4. **Convidados de fora e docentes: tema e agenda [CONFIRMAR] antes de qualquer convite.**

### Episódio 2. "Quando um caso gastrointestinal pede uma segunda opinião?"

- **Data:** ter 08/12/2026 [SUPOSIÇÃO]. **Quadro:** Ciência e prática.
- **Convidados:** Dr. Rodolfo Oliveira Leal, docente da ficha [CONFIRMAR agenda e tema]; veterinário clínico convidado [CONFIRMAR].
- **Objetivo:** mostrar, pela experiência dos convidados, como a discussão de casos entre colegas faz parte da rotina clínica e do estudo. Ponte com a pergunta de segunda opinião já prevista nos Stories da coordenação (AD-A6-1).
- **Perguntas (8):**
  1. Como vocês reconhecem, na rotina, o momento em que um caso pede outra opinião?
  2. Que informações o clínico costuma reunir antes de discutir o caso com um colega? [REVISÃO DOCENTE]
  3. O que muda na conversa quando o caso é discutido com quem atua na especialidade?
  4. Como comunicar ao tutor a decisão de pedir uma segunda opinião? (sem caso identificável)
  5. Que exemplo anônimo ilustra uma boa discussão de caso? [REVISÃO DOCENTE]
  6. Como um grupo de discussão de casos entre alunos e coordenação, citado na página da turma, entra na formação?
  7. Como registrar e organizar o que se aprende numa discussão de caso?
  8. Que conselho vocês dão a quem está começando a discutir casos com colegas?
- **Os 3 cortes (ideias):**
  1. "Quando pedir uma segunda opinião?" (resposta à pergunta 1)
  2. "O que reunir antes de discutir um caso?" (pergunta 2, [REVISÃO DOCENTE] obrigatória na legenda)
  3. "Como falar com o tutor sobre segunda opinião?" (pergunta 4)
- **Card do convidado:** Dr. Rodolfo Oliveira Leal, docente da Pós-graduação em Gastroenterologia Veterinária (titulação como na ficha).
- **Chamada:** [CHAMADA-TURMA] com [LINK-TURMA] (`utm_campaign=pos_68606_202610`, `utm_content=ufapecast_ep02`).
- **[REVISÃO DOCENTE]:** em toda a pauta, no roteiro final e nas legendas.

### Episódio 3. "Luto e burnout: como cuidar de quem cuida?"

- **Data:** ter 22/12/2026 [SUPOSIÇÃO]. **Quadro:** Comunidade UFAPE.
- **Convidados:** docente da ficha a indicar pela coordenação [CONFIRMAR]; segundo convidado [CONFIRMAR]. Tema vem do módulo 24 da ficha (Luto e Burnout).
- **Objetivo:** abrir uma conversa sobre o cuidado com a saúde mental de quem atua na veterinária, a partir da experiência dos convidados. Sem diagnóstico, sem conduta clínica, sem afirmar nada sobre quem assiste.
- **Perguntas (7):**
  1. Como o luto aparece na rotina da veterinária? [REVISÃO DOCENTE]
  2. Que diferença os convidados fazem entre cansaço, estresse e burnout? [REVISÃO DOCENTE: profissional de saúde mental deve validar a terminologia]
  3. Como uma equipe de clínica pode abrir esse assunto entre colegas?
  4. Como acolher um tutor em luto sem expor nenhum caso identificável?
  5. Por que esse tema aparece num curso técnico, como no módulo 24 da Pós-graduação em Gastroenterologia Veterinária?
  6. Que hábitos de rotina cada convidado adota? (relato pessoal, opcional)
  7. Onde buscar apoio profissional? (os convidados indicam serviços e profissionais; a Ufape confere cada indicação antes de publicar)
- **Os 3 cortes (ideias):**
  1. "Luto na veterinária: por onde começar a conversa?"
  2. "Como uma equipe pode falar sobre isso?"
  3. "Acolher o tutor em luto: o que considerar?"
- **Cuidados específicos:** linha fixa na descrição e no fim do episódio: "Em caso de necessidade de apoio, procure um profissional de saúde mental ou um serviço de saúde." [REVISÃO DOCENTE do texto]. Nenhum corte usa título que insinue que quem assiste está esgotado ou em sofrimento.
- **Chamada:** sem chamada de turma (decisão D-A do qa de 28/10/2026). O episódio sai em 22/12 só no YouTube e no Spotify. Chamada única: "Siga o UFAPE Cast e envie sua pergunta para o próximo episódio." Link: canal do UFAPE Cast; se o link for para o site, https://faculdade.ufape.com.br/?utm_source=<youtube|spotify|instagram>&utm_medium=organic_social&utm_campaign=pos_conteudo_202612&utm_content=ufapecast_ep03 [CONFIRMAR exceção com o arquiteto-de-fluxos]. Nenhuma peça do ep. 3 leva [CHAMADA-TURMA], link da 68606 ou data do 3º módulo.

### Episódio 4. "O que a imagem mostra num caso gastrointestinal?"

- **Data:** ter 05/01/2027 [SUPOSIÇÃO]. **Quadro:** Ciência e prática.
- **Convidados:** Dra. Cibele Figueira Carvalho, docente da ficha [CONFIRMAR agenda e tema; ela também está listada na Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, 68604]; segundo convidado [CONFIRMAR]. Temas da ficha: módulo 5 (radiologia e ultrassonografia aplicadas) e módulo 8 (ultrassonografia com doppler e microbolhas, tomografia do abdome).
- **Objetivo:** explicar, em linguagem acessível, o papel dos exames de imagem na investigação gastrointestinal, pelo olhar da convidada.
- **Perguntas (7):**
  1. Como a imagem entra na investigação de um caso gastrointestinal? [REVISÃO DOCENTE]
  2. O que a radiografia e a ultrassonografia mostram, e o que não mostram? [REVISÃO DOCENTE]
  3. Quando a tomografia é discutida? [REVISÃO DOCENTE]
  4. Como o clínico e quem faz o exame de imagem conversam sobre um caso?
  5. Que exemplo anônimo mostra o valor de repetir ou complementar um exame? Sem imagem de paciente real identificável. [REVISÃO DOCENTE]
  6. Como estudar imagem de forma prática durante uma pós?
  7. Que conselho para quem quer evoluir na leitura de imagem?
- **Os 3 cortes (ideias):**
  1. "O que a imagem mostra num caso?"
  2. "Radiografia ou ultrassom: o que cada um mostra?"
  3. "Como o clínico conversa com quem faz a imagem?"
- **Cuidado de imagem:** qualquer imagem de exame mostrada vem de acervo autorizado, sem nome, data, clínica ou código que identifique, com crédito. Sem imagem, o apresentador descreve o que a tela mostra (áudio autossuficiente).
- **Chamada:** [CHAMADA-TURMA] com [LINK-TURMA] (`utm_campaign=pos_68606_202610`, `utm_content=ufapecast_ep04`).

### Episódio 5. "Do exame de laboratório ao diagnóstico: o que pedir e como ler?"

- **Data:** ter 19/01/2027 [SUPOSIÇÃO], último episódio antes da pausa da 68606 em 22/01. **Quadro:** Ciência e prática.
- **Convidados:** Dr. Fabrizio Grandi, docente da ficha [CONFIRMAR agenda e tema; ele também está listado na Pós-graduação em Patologia Clínica, 68615]; segundo convidado [CONFIRMAR]. Tema da ficha: módulo 3 (laboratório clínico aplicado à gastroenterologia, fluidoterapia e hemogasometria), que acontece em 23 e 24/01/2027.
- **Objetivo:** apresentar como os exames laboratoriais entram na construção do raciocínio diagnóstico, pelo olhar do convidado. A pauta não diz o que pedir nem como ler: a resposta é dele.
- **Perguntas (8):**
  1. Como o laboratório participa do raciocínio diagnóstico em gastroenterologia? [REVISÃO DOCENTE]
  2. Como o clínico escolhe o que solicitar? [REVISÃO DOCENTE]
  3. Que cuidados de coleta e de comunicação com o laboratório fazem diferença?
  4. Como o convidado orienta a leitura de um resultado sem fechar diagnóstico só com um exame? [REVISÃO DOCENTE]
  5. Que papel têm a fluidoterapia e a hemogasometria na discussão do módulo 3 da Pós-graduação em Gastroenterologia Veterinária? (tema da ficha; resposta do convidado) [REVISÃO DOCENTE]
  6. Que exemplo anônimo ilustra a diferença entre pedir um exame e interpretar o conjunto? [REVISÃO DOCENTE]
  7. Como um aluno pode estudar a interpretação de exames de forma prática?
  8. Que conselho para quem quer evoluir nessa leitura?
- **Os 3 cortes (ideias):**
  1. "Como o laboratório entra no diagnóstico?"
  2. "O que considerar ao ler um resultado?"
  3. "Como estudar exames na prática?"
- **Chamada:** [CHAMADA-TURMA] com [LINK-TURMA] (`utm_campaign=pos_68606_202610`, `utm_content=ufapecast_ep05`). Dado que o episódio sai a 4 dias do 3º módulo, a regra completa é obrigatória e nenhuma peça sugere "corra" ou "última chance".
- **Cuidados do ep. 5:** ninguém fala a data do módulo 3 nem "neste fim de semana" fora da [CHAMADA-TURMA]; na pauta, a pergunta 5 cita só "o módulo 3 da Pós-graduação em Gastroenterologia Veterinária", sem data.

### Reserva em 02/02/2027. "Pós, residência, curso curto ou aprender com um colega?"

- Quadro "Formação em foco". Convidado: Esp. Maria Carolina Pappalardo ou outro docente da ficha [CONFIRMAR]. Depois de 22/01 a 68606 sai das chamadas; o episódio aponta para a próxima turma da área [CONFIRMAR OU4] ou para o conteúdo da Pós. Pauta completa só se a Ufape aprovar a reserva.

---

## 4. Calendário de gravação e publicação

Todas as datas são [SUPOSIÇÃO] até a Ufape aprovar o nome do podcast, os convidados e a equipe de produção. Dia da semana conferido a partir de 28/10/2026 (quarta-feira). Regra prática, não meta.

| Data | Marco | Quem |
|---|---|---|
| ter 03/11 | Aprovação do nome do podcast e checagem de perfis (YouTube e Spotify) até 06/11 | Ufape |
| até 06/11 | Convites enviados à coordenação e aos docentes dos ep. 2 a 5; busca de egresso para o ep. 1; pedido de autorização registrada ao egresso | produção, Ufape |
| 09/11 a 17/11 | Caixa de perguntas da comunidade (Stories) e formulário | posts-sociais, com aprovação |
| seg 16/11 a sex 20/11 | Preparação, teste de áudio e câmeras; **sessão de gravação 1: ep. 1 e ep. 2** (ex.: ter 17/11) | produção |
| 20 e 21/11 | Workshop Brasileiro de Neuromonitorização: sem campanha da Pós; sem postagem do podcast | - |
| seg 23/11 | Edição final do ep. 1, revisão docente, legendas SRT, miniatura, capa quadrada; conformidade e qa; aprovação humana | editor, designer, qa |
| **ter 24/11** | **Ep. 1 no ar** (YouTube e Spotify); corte 1; Story de estreia; card 4:5 em formato de Story (C6) | responsável pelos canais |
| qua 25/11 | Card da convidada (Esp. Maria Carolina Pappalardo) | posts-sociais |
| qui 26/11 | Corte 2 em Story (C7); Story de link | posts-sociais |
| ter 01/12 | Corte 3 do ep. 1; **sessão de gravação 2: ep. 3 e ep. 4** | produção |
| qua 02/12 | E-mail E2 da régua (já contado no teto D16); o link do ep. 1 pode ir na newsletter do mês, que já conta no teto | humano no CRM |
| **ter 08/12** | **Ep. 2 no ar**; corte 1 do ep. 2; Story de estreia | produção |
| qua 09/12 | Card do convidado do ep. 2 | posts-sociais |
| qui 10/12 | Corte 2 em Story (C7) e Story de link do ep. 2 | posts-sociais |
| ter 15/12 | Corte 3 do ep. 2; **sessão de gravação 3: ep. 5** (e reserva, se aprovada) | produção |
| sáb 19 e dom 20/12 | Módulo 2 da 68606 (online) | Ufape |
| 21/12 a 03/01 | Sem mensagem de campanha e sem nenhuma peça derivada do podcast (decisão D-A do qa); só o ep. 3 em 22/12, no YouTube e no Spotify. | - |
| **ter 22/12** | **Ep. 3 no ar** só no YouTube e no Spotify (sem chamada de turma, `utm_campaign=pos_conteudo_202612`); nenhuma peça derivada de 21/12 a 03/01 (D-A) | produção |
| **ter 05/01** | **Ep. 4 no ar**; corte 1; Story de estreia | produção |
| qua 06/01 | Card da convidada do ep. 4 | posts-sociais |
| qui 07/01 | Corte 2 em Story (C7) e Story de link do ep. 4 | posts-sociais |
| ter 12/01 | Corte 3 do ep. 4; WhatsApp W4 da régua (último toque antes da pausa); o link do ep. 5 ainda não existe | humano no CRM |
| **ter 19/01** | **Ep. 5 no ar**; corte 1; Story de estreia | produção |
| qua 20/01 | Card do convidado do ep. 5 | posts-sociais |
| qui 21/01 | Corte 2 em Story (C7) e Story de link do ep. 5 | posts-sociais |
| sex 22/01, 23h59 | Pausa das campanhas da 68606. Peças com [CHAMADA-TURMA] saem do ar ou são trocadas | humano no gerenciador |
| sáb 23 e dom 24/01 | Módulo 3 da 68606 (online): fim da janela de matrícula | Ufape |
| seg 25/01 | Primeira leitura de métricas do podcast (ouvintes até o fim, visitas com UTM, cortes publicados) | analista |
| ter 26/01 | Corte 3 do ep. 5, sem chamada de matrícula da 68606 (a janela fechou): chamada para o conteúdo da Pós ou para a próxima turma da área [CONFIRMAR OU4] | posts-sociais |
| qua 27/01 | Corte 1 e Story 1 do ep. 3, sem chamada de turma [SUPOSIÇÃO de data] | posts-sociais |
| qui 28/01 | Story 2 do ep. 3 (link para o episódio), sem chamada de turma [SUPOSIÇÃO de data] | posts-sociais |
| ter 02/02 | Reserva, se aprovada | produção |
| qua 03/02 | Card do convidado do ep. 3, sem chamada de turma [SUPOSIÇÃO de data] | posts-sociais |
| qui 04/02 | Corte 2 do ep. 3, sem chamada de turma [SUPOSIÇÃO de data] | posts-sociais |
| qua 17/02 | Corte 3 do ep. 3, sem chamada de turma [SUPOSIÇÃO de data: depois da pausa de 22/01, fora da semana de Carnaval e sem outro post de feed da Pós no mesmo dia; o posts-sociais confere com as turmas de março] | posts-sociais |

Observações de calendário:

- No máximo 1 post de feed da Pós por dia e 3 por semana, somando o kit da turma, os posts de docente e o podcast. O card 4:5 de todo episódio vira Story (ou anúncio de remarketing só pelo AP-4, nunca feed) e o corte 2 de cada episódio vira Story (C6 e C7). Story com link da turma leva a [CHAMADA-TURMA] inteira; a conferência slot a slot é do posts-sociais antes da aprovação. O P4 do posts-sociais fica em 03/12, sem a opção de 01/12.

- Nos cortes que sobram depois de 22/01, trocar a legenda: a [CHAMADA-TURMA] sai e entra um link para o conteúdo da Pós [CONFIRMAR OU4]. Nenhuma peça publicada fica com a regra do 3º módulo depois de 24/01.
- O teto de mensagens D16 não é alterado: o podcast só entra no WhatsApp em respostas 1 a 1 do time de vendas, dentro da janela de 24 h aberta pelo candidato, e na newsletter que já conta no teto.
- Se uma gravação atrasar, o episódio atrasa. Regra prática: parar a série depois de 2 episódios atrasados seguidos (AP-2 do cmo).

---

## 5. Checklist de autorização por episódio

### 5.1 Checklist base (marcar antes de gravar, antes de editar e antes de publicar)

**Antes de gravar**
- [ ] Autorização registrada de uso de imagem, voz e citação de cada pessoa que aparece (docentes: decisões 8 e 10, conferir o registro de cada nome; egresso e convidado de fora: termo assinado [CONFIRMAR modelo e guarda do termo])
- [ ] Nome e titulação conferidos com a ficha da turma (docentes) ou com o convidado (egresso e outros)
- [ ] Convidado sabe que a opinião é dele, sabe que haverá cortes e que o trecho vai a YouTube, Spotify, Instagram e, se aplicável, anúncio de remarketing
- [ ] Convidado informado de que pode pedir para retirar um trecho antes da publicação [SUPOSIÇÃO de procedimento]
- [ ] Menor de idade: não participa
- [ ] Local de gravação sem paciente, tutor, aluno, prontuário, tela de sistema ou placa que identifique
- [ ] Imagens de apoio (exame, foto clínica) vêm de acervo autorizado, sem identificação, com crédito
- [ ] Trilha, vinheta e grafismos com licença guardada
- [ ] Revisor docente do conteúdo clínico definido [CONFIRMAR nome]

**Antes de publicar**
- [ ] Conteúdo clínico revisado pelo docente ([REVISÃO DOCENTE]) e trechos de conduta removidos
- [ ] Nenhum trecho com promessa de emprego, renda, aprovação ou resultado; nenhuma frase de certificação ou "MEC"
- [ ] Nenhum preço, parcela ou bolsa em fala, tela, capa ou legenda
- [ ] [CHAMADA-TURMA] igual ao texto oficial, em toda peça com chamada à turma, e só até 22/01
- [ ] Nenhuma opinião escrita no lugar do convidado em legenda, card ou descrição
- [ ] Legendas SRT revisadas, tarjas sem cobrir o rosto, créditos completos
- [ ] Links e UTM testados, capa certa em cada plataforma
- [ ] Skill conformidade-educacional aplicada (fala, tela, legenda, descrição, página de destino)
- [ ] qa-de-marketing aprovou; pessoa da Ufape aprovou a publicação
- [ ] Docente viu e aprovou o card e os cortes em que aparece

### 5.2 Matriz por episódio

| Episódio | Pessoa | Autorização de imagem, voz e citação | Revisão de conteúdo | Observação |
|---|---|---|---|---|
| 1 | Esp. Maria Carolina Pappalardo | Registrada (decisões 8 e 10); conferir o registro nominal | Docente (conteúdo é de escolha de pós; clínico só se surgir) | Card do convidado e corte contam como 1 post de docente |
| 1 | Egresso de pós da Ufape | [CONFIRMAR: termo assinado, nome, pós de origem] | Ufape (relato de ganho é cortado) | Sem autorização, o episódio sai sem ele |
| 1 | Apresentador | [CONFIRMAR] | - | Quem fala a [CHAMADA-TURMA] |
| 1 | Autor da pergunta da comunidade | Sem identificação; pergunta lida sem nome | Triagem de dado pessoal | Formulário com política de privacidade [CONFIRMAR p04] |
| 2 | Dr. Rodolfo Oliveira Leal | Registrada (docente da ficha) | [REVISÃO DOCENTE] obrigatória | Agenda e tema [CONFIRMAR] |
| 2 | Veterinário clínico convidado | [CONFIRMAR: termo assinado] | [REVISÃO DOCENTE] | Sem clínica ou caso identificável |
| 3 | Docente a indicar | Registrada se da ficha; conferir | [REVISÃO DOCENTE] e revisão de profissional de saúde mental [SUPOSIÇÃO] | Tema sensível; sem insinuar condição de quem assiste |
| 3 | Segundo convidado | [CONFIRMAR: termo assinado] | idem | Indicação de serviços de apoio conferida pela Ufape |
| 4 | Dra. Cibele Figueira Carvalho | Registrada (docente da ficha) | [REVISÃO DOCENTE] obrigatória | Imagens de exame sem identificação; ela também consta na 68604 |
| 4 | Segundo convidado | [CONFIRMAR: termo assinado] | [REVISÃO DOCENTE] | - |
| 5 | Dr. Fabrizio Grandi | Registrada (docente da ficha) | [REVISÃO DOCENTE] obrigatória | Ele também consta na 68615 |
| 5 | Segundo convidado | [CONFIRMAR: termo assinado] | [REVISÃO DOCENTE] | - |

---

## 6. Itens ainda sem resposta que travam a produção

| # | O que falta | Trava o quê |
|---|---|---|
| 1 | Nome do podcast aprovado e perfis no YouTube e no Spotify | todas as artes, títulos e a abertura falada |
| 2 | Quem apresenta, grava, edita e publica; horas por semana; local; custo de produção (fora dos R$ 2.000,00 de mídia) | calendário inteiro |
| 3 | Egresso do ep. 1 e termo de autorização | ep. 1 completo |
| 4 | Convidados, temas e agendas dos ep. 2 a 5 | pautas 2 a 5 |
| 5 | Revisor docente do conteúdo clínico | publicação dos ep. 2, 4 e 5 e de todo corte clínico |
| 6 | Texto de certificação da regulação | nenhuma peça usa; só destrava páginas e descrições se a Ufape quiser |
| 7 | Correção da página da 68606 (A7, A12, A13) | página de destino entrega o que a peça promete |
| 8 | Formulário da pergunta da comunidade com política de privacidade | bloco 4 de todo episódio |
| 9 | OU3 (reposição dos módulos perdidos) e OU6 (véspera ou 1º dia) | só afeta respostas do time; a pauta não promete reposição |
| 10 | Exceção de UTM `pos_conteudo_<AAAAMM>` e medium do Spotify | rastreio |

---

## 7. Podcasts de terceiros

Não faz parte deste pedido. A lista de podcasts de terceiros com o ângulo de cada convite não foi feita aqui. Pode ser feita num segundo pacote, sempre em rascunho e com aprovação.

---

## Aprovações humanas pedidas (nada foi feito)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AP-2 (do cmo) | aprovar o nome UFAPE Cast (ou outro), o pacote por episódio e o calendário quinzenal | decisão 21 | custo de produção [CONFIRMAR], fora da verba de mídia | 5 episódios e cerca de 50 peças derivadas até a pausa | parar a série depois de 2 episódios atrasados |
| AP-3 (do cmo) | publicar episódios e cortes em YouTube, Spotify e Instagram, cada um com o ok do convidado | nada se publica sem aprovação | sem custo de mídia | visitas à página da turma com UTM do podcast | despublicar ou arquivar |
| AP-4 (do cmo, condicional) | usar o card 4:5 ou um corte no remarketing da 68606, trocando uma peça | só com diária suficiente | dentro dos R$ 2.000,00 | prova de autoridade no remarketing | voltar à peça anterior |

- A série só vai à aprovação de produção (AP-2) com equipe, horas por semana e custo informados pela Ufape. Até lá, o pacote é plano, não calendário.
- Os ep. 1, 2, 4 e 5 e seus pacotes com [CHAMADA-TURMA] ou [LINK-TURMA] só saem com a A13 publicada na página da 68606 e conferida pelo qa, mais a troca da frase ligada ao MEC (A7) e da turma mínima (A12) ou a decisão registrada da regulação (E1 do qa de 28/10/2026).

---

## Fatos (com fonte)

- 68606: Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo, semipresencial, 500 h, 24 módulos, início em 07/11/2026 (planilha), status aberto; coordenação Esp. Maria Carolina Pappalardo; docentes e módulos como na ficha (ficha 68606; linha literal do catálogo em pos-68606.json). Módulo 1 em 07 e 08/11/2026, módulo 2 em 19 e 20/12/2026, módulo 3 em 23 e 24/01/2027, online; presenciais nos módulos 6, 13 e 21.
- Temas dos módulos usados nas pautas: módulo 3 (laboratório clínico, fluidoterapia, hemogasometria), módulos 5 e 8 (imagem), módulo 24 (luto e burnout) (ficha 68606).
- A Ufape aceita matrícula até o 3º módulo do curso, nesta turma em 23/01/2027 (decisão 18, 27/10/2026); a regra completa vai em toda chamada (pedido de 28/10/2026).
- Inscrição de R$ 250,00 como no site (decisão 23); nenhuma peça deste pacote cita valor.
- Podcast no plano: nome recomendado UFAPE Cast, em aprovação; YouTube e Spotify; quinzenal; 35 a 45 minutos; blocos, quadros e pacote por episódio (decisão 21 e proposta de 28/10/2026).
- Docentes têm autorização de imagem e citação (decisões 8 e 10).
- Datas de episódios, convidados sugeridos e UTM: cmo-pos-2026-10-28-apresentacao-68606.md, slides 13 e 14.
- Especificações de arte e arquivos: proposta, páginas 12 a 15 e 23.

## [SUPOSIÇÃO]

- Calendário de gravação e publicação, incluindo os dias de corte, Stories e cards, as três sessões de gravação e a aprovação do nome até 06/11.
- Tempos dos capítulos e dos trechos-alvo dos cortes, ajustáveis à edição final.
- Duração de 45 a 60 segundos por corte.
- Prazo de 09/11 a 17/11 para a caixa de perguntas, a pergunta de reserva do ep. 1 e a triagem de 18/11.
- Possibilidade de o convidado pedir a retirada de um trecho antes da publicação.
- Revisão por profissional de saúde mental no ep. 3.
- Sessões de gravação com 2 episódios.
- Frases para posts do ep. 1 (sujeitas a conferir com a edição final).

## [CONFIRMAR]

- Nome do podcast; perfis e canal do YouTube; Apple Podcasts por RSS.
- Apresentador, produção, edição, publicação, horas por semana, local, custo.
- Egresso do ep. 1 (nome, pós de origem, termo de autorização).
- Convidados, temas e agendas dos ep. 2 a 5; docente do ep. 3.
- Revisor docente do conteúdo clínico (nome).
- Formulário da pergunta da comunidade com política de privacidade (p04).
- Onde ficam a transcrição revisada e as legendas.
- Créditos, trilha e licenças.
- Exceção de UTM de conteúdo e medium do Spotify.
- Conteúdo do episódio reserva de 02/02 (a chamada do ep. 3 foi decidida pela D-A).
- Próxima turma da área para as chamadas depois de 22/01 (OU4).
- Reposição dos módulos perdidos (OU3) e data limite de matrícula (OU6).
- Correção da página da 68606 e texto de certificação.
- Se "Profa. Ísis Carvalho" e "ESP. Isis de Carvalho Rodrigues Santana Lemes" são a mesma pessoa (não afeta este pacote).

## Fontes

- /home/user/marketing-ufape/CLAUDE.md
- /home/user/marketing-ufape/contexto/ufape-geral.md
- /home/user/marketing-ufape/contexto/pos-graduacao.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/docs/insumos/ufape-podcast-proposta-2026-10-28.txt
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json
- /home/user/marketing-ufape/.claude/skills/conformidade-educacional/SKILL.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md

## Próximo agente

qa-de-marketing (auditoria do departamento 12 e conformidade-educacional), antes da aprovação humana.
- 28/10/2026: correções E1, E2, E5, E6, E20 a E26 do qa-de-marketing (qa-de-marketing-pos-2026-10-28-enxoval-68606.md) aplicadas pelo orquestrador.
- 28/10/2026: ajustes R7, R8 e R9 da reconferência do qa-de-marketing aplicados pelo orquestrador.
