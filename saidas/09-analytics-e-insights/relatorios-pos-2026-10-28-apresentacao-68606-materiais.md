# Roteiro dos blocos C e D da apresentação da Pós-graduação: materiais gerados e lacunas (modelo para os outros cursos, 68606 como primeiro preenchimento)

- **Agente:** relatorios (departamento 09, Analytics e Insights)
- **Linha:** pos
- **Data:** 28/10/2026 (versão 2, com o inventário completo pelo grep do orquestrador)
- **Para:** complementar o roteiro de 20 slides saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md. Os blocos A e B (insights e estratégia) são do cmo e não estão aqui.
- **Papel da apresentação (informação do CEO):** a apresentação é o MODELO para os outros cursos; a 68606 é o primeiro preenchimento. O deck da The Growth Hub e a proposta do podcast são só referência para tópicos sem resposta.
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada foi publicado, enviado, pausado ou pago.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - contexto/ufape-geral.md, contexto/pos-graduacao.md, conhecimento/INDICE.md
  - saidas/10-operacoes-de-marketing/cursos/pos-68606.json
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md (seções 0 a 4.3, 6 e 8) e cmo-pos-2026-10-28-apresentacao-68606.md
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (v5, seções 0, 1, 6A, 7 e 8) e copy-de-mensagens-pos-2026-10-26-reta-final.md (cabeçalho, seções 0.1 a 0.6 e dados da 68606, para a comparação de versões)
  - saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (seção 0, seção 7 A6)
  - saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md (seções 0 e 6, A6), autoridade-docente-pos-2026-10-26.md (seções 0 e 6, A6) e posts-sociais-pos-2026-10-26.md (linha 223)
  - saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (v7; seções 12 e 13) e cabeçalhos de criativos-de-anuncio-pos-2026-10-26.md, criativos-de-anuncio-pos-turmas-2026-10-26.md, criativos-de-anuncio-pos-2026-10-27-ext.md, anuncios-meta-pos-2026-10-26.md e anuncios-google-pos-2026-10-26.md
  - saidas/06-geracao-de-demanda/iscas-digitais-pos-2026-10-26.md (seção 8) e campanhas-de-nutricao-pos-2026-10-26.md (linha 159)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (resumo e seção A6)
  - saidas/04-conteudo/conteudo-longo-pos-2026-10-26.md (linha 107), estrategia-de-conteudo-pos-2026-10-26.md, newsletter-geral-2026-10-26.md, youtube-pos-2026-10-26.md (cabeçalhos e resumos)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-28-apresentacao.md (veredito final: APROVADO na reconferência de 28/10/2026)
  - docs/pendencias-camada-1.md, docs/execucao-2026-10-26.md (decisões 1 a 21), docs/insumos/ufape-podcast-proposta-2026-10-28.txt
- **Inventário por busca textual:** o orquestrador rodou `grep -rl 68606 saidas` e passou a lista com a linha de cada ocorrência; ela está incorporada. youtube-pos, anuncios-meta-pos e anuncios-google-pos não têm nada da 68606. Os arquivos grandes não foram lidos linha a linha: as passagens da 68606 foram lidas nas linhas indicadas.
- **Dados pessoais:** nenhum. Docentes só com nome e titulação como estão na ficha.
- **Troca de travessão no texto copiado:** nenhuma foi necessária; as peças copiadas não traziam travessão nem meia-risca.

---

## Convenções (valem para todos os slides)

- Cada slide traz: etiqueta, título-afirmação, subtítulo, conteúdo exato, rótulo de modelo, fonte por arquivo, visual sugerido e notas do apresentador.
- **Rótulo de modelo:** "MODELO: fixo da linha" (vale igual para toda turma de Pós) ou "MODELO: troca por turma" (com a lista dos campos variáveis e de onde cada um vem).
- **Origem dos campos variáveis (chaves para preencher outra turma):**
  - **catálogo:** contexto/catalogo-de-cursos.md, seção 2 (nome, campus, modalidade, carga, turma, início, preço, status)
  - **ficha:** contexto/cursos/pos/<código>-<slug>.md (módulos, datas dos módulos 1 a 3, 1º presencial, coordenação, docentes, endereço, texto da página)
  - **JSON:** saidas/10-operacoes-de-marketing/cursos/pos-<código>.json (kit, pendências, aprovações, metas, números agregados)
  - **casa de mensagens:** mensagens-pos, seção da área da turma (promessa, pilares, objeções)
  - **plano da onda:** cmo-pos da onda (datas de pausa, calendário, toques do OA9)
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape tem; [SUPOSIÇÃO] é escolha de agente; [DADO NÃO FORNECIDO] é número que não existe nos arquivos.
- **Mínimo do kit da Pós:** templates/kit-de-lancamento-pos.md; os mínimos usados abaixo são os registrados em pos-68606.json (kit.entregas).
- Situação no qa, só como consta nos arquivos: "qa aprovado e aguardando aprovação humana", "rascunho" ou "inventário pendente".

---

# BLOCO C. Materiais gerados para a 68606 (e para a área A6)

## Slide C1. Inventário do kit mínimo da turma

- **Etiqueta:** C · MATERIAIS · INVENTÁRIO
- **Título-afirmação:** Dos 9 itens do kit, 4 estão escritos e aprovados pelo qa; 5 seguem com inventário pendente.
- **Subtítulo:** Checklist que serve a qualquer turma de Pós: mínimo do kit, quantidade na 68606, agente, arquivo e situação.
- **Rótulo:** MODELO: fixo da linha (colunas e mínimos); troca por turma (quantidade, arquivo, situação, vindos do JSON da turma, campo kit.entregas).
- **Conteúdo (tabela):**

| Item do kit | Mínimo | Na 68606 | Agente | Arquivo | Situação |
|---|---|---|---|---|---|
| Página da turma | 1 | página oficial no ar, não conta como entregue | landing-page, seo-on-page | pos-68606.json (OA10) | inventário pendente |
| Plano dos 8 canais | 1 | 1 | cmo | cmo-pos-2026-10-26.md, seção 5 | qa aprovado e aguardando aprovação humana |
| Plano de mídia | 1 | 1 | gestor-de-midia | gestor-de-midia-pos-2026-10-26.md | qa aprovado e aguardando aprovação humana |
| Posts orgânicos | 6 | 0 | posts-sociais | sem arquivo | inventário pendente |
| Criativos de anúncio | 3 | 0 escritos pela squad; no ar [CONFIRMAR] | criativos-de-anuncio | sem arquivo | inventário pendente |
| Post por docente | 1 por docente autorizado (38 na ficha) | 1 rascunho (AD-A6-1) | autoridade-docente | autoridade-docente-pos-2026-10-26.md | rascunho |
| WhatsApp (mín. 4) e e-mail (mín. 2) | 4 e 2 | 4 e 2 | copy-de-mensagens | copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A | qa aprovado e aguardando aprovação humana (OA9) |
| Roteiro de vídeo curto | 1 | 0 | tiktok | sem arquivo | inventário pendente |

- **Fonte:** pos-68606.json (kit.entregas, kit.acrescimos, kit.inventario); templates/kit-de-lancamento-pos.md.
- **Visual:** tabela com semáforo (verde: qa aprovado; amarelo: rascunho; cinza: inventário pendente) e o contador "5 de 9 sem peça aprovada".
- **Notas do apresentador:**
  - O mínimo nunca diminui. O que não chega vira lacuna escrita no relatório final (OA8).
  - Acréscimos do kit da 68606: mensagens de reta final (mesmo arquivo dos WhatsApp, aprovadas pelo qa); inventário do kit (cmo, prazo 28/10, a fazer, depende da resposta OU5 da Ufape); pedido de pausa e relatório final (cmo e gestor-de-midia, a fazer, prazos 22/01, 25/01 e 22/02/2027); pacote do podcast (acréscimo da decisão 21, a fazer).
  - Posts orgânicos: o plano do cmo prevê 2 no feed e 4 em Stories de 03/11 a 20/01 (OA11), mas nenhum texto dos 6 existe em arquivo da squad. O arquivo posts-sociais-pos-2026-10-26.md é da campanha das provas (ver slide C18). Criativos: o cmo-pos diz que contam os que já estão no ar e aprovados; quantos são, a Ufape ainda não informou (OU5). Criativos-de-anuncio-pos-turmas-2026-10-26.md cobre 14 turmas de março e abril; o grep achou 2 ocorrências do código 68606 nele, mas o arquivo não tem criativo da 68606 (a turma não está entre as 14) [CONFIRMAR as 2 linhas].
  - Página: a página oficial está no ar com frase de certificação ligada ao órgão regulador, turma mínima de 20 e sem a regra do 3º módulo; por isso não conta como entregue (OA10, pendências p01, p02 e p04).
  - Post por docente: o kit pede 1 por docente autorizado; há 1 de 38, e a lacuna de 37 está registrada no OA8.
  - **Substituição de versão (mensagens):** o arquivo copy-de-mensagens-pos-2026-10-26-reta-final.md (73 ocorrências da 68606; 9 mensagens de reta final, véspera e pós-início de 707, 68604 e 68606, com envios da 68606 em 03/11, 06/11 e 11/11) é a versão anterior. O arquivo onda1 v5 é o vigente, e esta apresentação mostra só ele. Ver a comparação no slide C2.
  - Para outra turma: copie esta tabela, troque os arquivos pelos do JSON dessa turma e some a quantidade real.

---

## Slide C2. Materiais além do kit e o que serve à turma

- **Etiqueta:** C · MATERIAIS · ALÉM DO KIT
- **Título-afirmação:** A área A6 tem casa de mensagens, 10 ganchos, palavras-chave e 1 post de docente; a isca está especificada e não produzida.
- **Subtítulo:** O que serve à 68606, o que é da linha toda e o que não foi feito para ela.
- **Rótulo:** MODELO: troca por turma (a área A6 muda para a área da turma; os arquivos são os mesmos, com outra seção).
- **Conteúdo (tabela):**

| Material | Agente | Arquivo | Serve à 68606? | Situação |
|---|---|---|---|---|
| Casa de mensagens A6 | mensagens | mensagens-pos-2026-10-26.md, seção 7 | sim | v2, corrigida após o qa |
| 10 ganchos A6 (3 recomendados) | criador-de-ganchos | criador-de-ganchos-pos-2026-10-26.md, seção 6 | sim | v2; cmo-pos cita camada 2 aprovada [CONFIRMAR, o cabeçalho diz "para nova conferência"] |
| Respostas do time (10) | copy-de-mensagens | copy-de-mensagens-pos-onda1-2026-10-26.md, seção 7 | sim | qa aprovado e aguardando aprovação humana |
| Palavras-chave K6.1 a K6.5 | pesquisa-de-palavras-chave | pesquisa-de-palavras-chave-pos-2026-10-26.md, seção A6 | sim (Google) | rascunho; sem RSA escrito |
| Isca da área A6 | iscas-digitais | iscas-digitais-pos-2026-10-26.md, seção 8 | especificada, produção reservada | rascunho |
| Nutrição NP3 (área sem turma aberta) | campanhas-de-nutricao | campanhas-de-nutricao-pos-2026-10-26.md, linha 159 | depois de 07/11 | rascunho |
| Conteúdo longo | conteudo-longo | conteudo-longo-pos-2026-10-26.md, linha 107 | só cita a 68606 numa tabela | rascunho |
| Material da prova 68650 | vários | ver slide C18 | relacionado, fora da prioridade | decisão 14 |

- **Fonte:** arquivos citados na tabela; pos-68606.json (arquivos_por_camada); cmo-pos-2026-10-26.md, seção 4.3.
- **Visual:** mapa em colunas "serve à turma" e "serve à linha" com os arquivos como etiquetas.
- **Notas do apresentador:**
  - **Comparação das duas versões das mensagens da 68606.** Vigente: copy-de-mensagens-pos-onda1-2026-10-26.md, versão 5, com 6 toques (T1 28/10, T2 29/10, W2 06/11, E2 02/12, W3 16/12, W4 12/01), regra completa do 3º módulo e nenhuma frase da 1ª mensalidade; é o arquivo que o mapa pos-68606.json e o plano do cmo citam. Anterior: copy-de-mensagens-pos-2026-10-26-reta-final.md, com 3 mensagens por turma (reta final em 03/11, véspera em 06/11 e pós-início em 11/11) e a frase CL1 ("a 1ª mensalidade é paga até 30 dias antes do início; esse prazo já passou"). Divergências: a frase da 1ª mensalidade (linha 46 do arquivo antigo) saiu das versões 3 a 5 do onda1, porque a decisão 18 (27/10) mudou a regra de entrada e a data de corte deixou de ser limite; o arquivo antigo depende de PR4, B2 e B5 (política de entrada e lista de interesse), que a decisão 18 respondeu. A substituição é inferência deste agente [SUPOSIÇÃO], pelos arquivos do mapa e do plano do cmo; o cabeçalho de nenhum dos dois arquivos declara a substituição [CONFIRMAR com o cmo].
  - Isca (especificação, não produzida): título "Gastroenterologia veterinária na Ufape: o que se pratica nos 3 módulos presenciais", subtítulo "Pós-graduação em Gastroenterologia Veterinária", PDF de 4 a 6 páginas, esforço 4 h. Motivo da reserva: a turma começa em 07/11/2026, a isca não estaria no ar a tempo, e depois dela a área fica sem turma aberta (NP3). Produzir só se a Ufape informar a regra de entrada tardia ou uma turma futura.
  - Nutrição: o segmento S10 inclui "A6 Gastroenterologia depois de 07/11 (68606 iniciada)", área sem turma aberta no catálogo; antes disso a 68606 tem régua com data.
  - Conteúdo longo: o artigo cita "Pós-graduação em Gastroenterologia Veterinária (turma IX)", 500 h, 24 módulos, 3 presenciais, em tabela de comparação de seis cursos. Não é peça da turma.
  - A estratégia de conteúdo diz que a venda de reta final é do kit, e o conteúdo editorial serve à próxima edição (estrategia-de-conteudo-pos, resumo, item 5). Newsletter e YouTube não citam a 68606 (YouTube: nada no grep).
  - Anúncios: anuncios-meta-pos e anuncios-google-pos cobrem março e abril e não têm a 68606 (grep).

---

## Slide C3. Casa de mensagens da área A6

- **Etiqueta:** C · MATERIAIS · MENSAGEM
- **Título-afirmação:** A promessa da área sai da ficha: Gastroenterologia de cães e gatos, do diagnóstico à prática.
- **Subtítulo:** Promessa, três pilares de prova e a chamada que a área usa.
- **Rótulo:** MODELO: troca por turma (promessa e pilares vêm da casa de mensagens da área; as provas, da ficha).
- **Conteúdo (texto literal):**
  - **Promessa central:** "Gastroenterologia de cães e gatos do diagnóstico à prática cirúrgica e endoscópica, com grupo de discussão de casos com a coordenação."
  - **Pilar 1, Docentes:** "Coordenação Esp. Maria Carolina Pappalardo; 38 professores listados, entre eles Dr. Rodolfo Oliveira Leal, DRA. VIVIANE DE MARCO, DR. Fabrizio Grandi e DRA. Maria Anete Lallo"
  - **Pilar 3, Formato e campus:** "Semipresencial, São Paulo"
  - **Chamada:** "Fale com o time para saber como entrar na turma."
- **Fonte:** saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md, seção 7 (versão 2). Situação: v2 corrigida após o qa; a chamada da casa foi atualizada pela regra 6 do plano do cmo (decisão 18) nas mensagens do arquivo onda1.
- **Visual:** a "casa" com a promessa no telhado e três pilares; ao lado, os 3 títulos de exemplo.
- **Notas do apresentador:**
  - Pilar 2, Módulos (texto literal): "24 módulos, 500 h; 3 módulos presenciais (6, 13 e 21) com anatomia prática, prática de cirurgia esofágica, gástrica, intestinal, pancreática e hepatobiliar, parasitologia ou transplante fecal e colocação de sondas. Diferenciais escritos na ficha: "Estágios com a cooperação em suas clínicas/hospitais" e grupo para discussão de casos entre alunos e coordenadores (regras do estágio [CONFIRMAR])".
  - Objeções e respostas (literal): "Ainda dá para entrar? A turma começa em 07/11." Resposta: "Fale com o time para saber como entrar na turma." Sem prazo inventado e sem "últimas vagas". "Tem prática de endoscopia e cirurgia ou é tudo online?" Resposta: "A teoria é online e há 3 módulos presenciais (6, 13 e 21) com prática de anatomia, cirurgia e parasitologia, além do estágio previsto na página." "São 38 professores. Vou ter acesso a alguém?" Resposta: "A página prevê um grupo para discussão de casos entre alunos e coordenadores." (formato e frequência [CONFIRMAR]).
  - Títulos de exemplo [SUPOSIÇÃO de texto]: "Pós-graduação em Gastroenterologia Veterinária: prática cirúrgica e discussão de casos com a coordenação"; "Turma de 07/11/2026 da Pós-graduação em Gastroenterologia Veterinária, em São Paulo".
  - Evitar: "especialidade emergente e carente de profissionais" e "coordenadores referências nacionais" (textos da página sem fonte). A prova de bolsa da área não é caminho para esta turma.
  - Para outra turma: troque a seção 7 (A6) pela seção da área da turma.

---

## Slide C4. WhatsApp T2: o convite de 29/10

- **Etiqueta:** C · MATERIAIS · WHATSAPP 1 DE 4
- **Título-afirmação:** O primeiro WhatsApp apresenta a turma e leva à página.
- **Subtítulo:** Qui 29/10, 10h, antes do início; só para quem tem opt-in de campanha (S2 e S3 da área A6).
- **Rótulo:** MODELO: troca por turma. Campos variáveis: nome do curso, turma (IX), início (07/11/2026), módulo e data do 1º presencial, carga e módulos (catálogo e ficha); link da página e UTM (ficha, campo página oficial); data do envio (plano da onda, tabela do OA9).
- **Conteúdo (balão de WhatsApp, texto literal):**

> Olá, [nome]. Aqui é a equipe da Pós-graduação da Faculdade UFAPE.
>
> A Pós-graduação em Gastroenterologia Veterinária (turma IX) começa em 07/11/2026 com o módulo 1 online; os módulos presenciais são na sede da Ufape, em São Paulo. O primeiro é o módulo 6, em 17 e 18/04/2027, com prática de cirurgia esofágica, gástrica e intestinal. São 500 h em 24 módulos.
>
> Parcelas, total e matrícula estão na página da turma:
> https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=whatsapp&utm_medium=crm&utm_campaign=pos_68606_202610&utm_content=t2-68606
>
> Para não receber mais mensagens, responda SAIR.

- **Agente:** copy-de-mensagens. **Arquivo:** saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.2 (versão 5, a vigente). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** mockup de balão de WhatsApp com o botão "Ver a turma" e o botão "Sair" embaixo.
- **Notas do apresentador:**
  - Primeira linha A (teste): "Olá, [nome]. Prática de cirurgia esofágica, gástrica e intestinal na Pós-graduação em Gastroenterologia." Primeira linha B (teste): "Olá, [nome]. A turma de Gastroenterologia começa em 07/11, em São Paulo."
  - Template Meta: pos_68606_reta_final_t2, variável {{1}} = primeiro nome; botões "Ver a turma" (URL estática com UTM) e "Sair" [CONFIRMAR U11a: se a Ufape usa a API oficial do WhatsApp].
  - Sem preço, bolsa, certificação ou "últimas vagas". Toda mensagem depende da página corrigida (OA10) e da decisão humana no OA9 [CONFIRMAR com a regulação se pode sair antes da troca da frase na página].
  - O envio de 29/10 está dentro do teto D16 [SUPOSIÇÃO do cmo].
  - Esta mensagem substitui a "reta final" de 03/11 do arquivo anterior (reta-final.md); ver slide C2.

---

## Slide C5. WhatsApp W2: a véspera do início

- **Etiqueta:** C · MATERIAIS · WHATSAPP 2 DE 4
- **Título-afirmação:** Na véspera, o assunto é o módulo 1, online, no fim de semana.
- **Subtítulo:** Sex 06/11, 10h, antes do início.
- **Rótulo:** MODELO: troca por turma. Campos: início, tema do módulo 1 e data do 1º presencial (ficha); data da véspera (catálogo menos 1 dia); UTM (plano da onda).
- **Conteúdo (balão, texto literal):**

> Olá, [nome]. Aqui é a equipe da Pós-graduação da Faculdade UFAPE.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começa em 07/11/2026, sábado, com o módulo 1 online (semiologia e fisiologia gastrointestinal); os módulos presenciais são na sede da Ufape, em São Paulo. O primeiro é o módulo 6, em 17 e 18/04/2027.
>
> Parcelas, total e matrícula estão na página da turma:
> https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=whatsapp&utm_medium=crm&utm_campaign=pos_68606_202610&utm_content=w2-68606
>
> Para não receber mais mensagens, responda SAIR.

- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.3 (v5). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** balão de WhatsApp com a data em destaque; ao lado, o calendário de 06 a 08/11.
- **Notas do apresentador:** primeira linha A (teste): "Olá, [nome]. O módulo 1 de Gastroenterologia é em 07 e 08/11, online." Primeira linha B (teste): "Olá, [nome]. A turma de Gastroenterologia começa em 07/11, em São Paulo." Template pos_68606_reta_final_w2 [CONFIRMAR U11a]. Sexta é dia útil, e a régua das provas não envia nesta data (decisão 14). Coincide com a data da "véspera" do arquivo anterior (06/11, 10h), mas o texto vigente é este.

---

## Slide C6. WhatsApp W3: depois do início, com a regra completa

- **Etiqueta:** C · MATERIAIS · WHATSAPP 3 DE 4
- **Título-afirmação:** Depois do início, a mensagem diz a regra inteira do 3º módulo.
- **Subtítulo:** Qua 16/12, 10h. A chamada é falar com o time (responder TURMA).
- **Rótulo:** MODELO: troca por turma. Campos fixos da linha: a frase da regra (só as datas mudam). Campos variáveis: início e data do 3º módulo (ficha), carga, nome do curso, data do envio.
- **Conteúdo (balão, texto literal):**

> Olá, [nome]. Aqui é a equipe da Pós-graduação da Faculdade UFAPE.
>
> A Pós-graduação em Gastroenterologia Veterinária (turma IX, São Paulo) tem 500 h, com módulos presenciais de prática na sede da Ufape.
>
> A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.
>
> Para falar com o time, responda TURMA. O atendimento é em horário comercial.
>
> Para não receber mais mensagens, responda SAIR.

- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.4 (v5). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** balão de WhatsApp com a frase da regra em bloco, sem destaque na data.
- **Notas do apresentador:** a frase da regra vai sempre inteira e a data do 3º módulo nunca aparece sozinha nem com "corra" ou "últimas vagas" (decisão 18). Nenhuma mensagem promete reposição, gravação ou aula extra (OU3 aberta); a ficha da 68606 não cita gravação. A palavra TURMA é [SUPOSIÇÃO de texto]. Primeira linha A (teste): "Olá, [nome]. Prática de cirurgia e anatomia na Pós-graduação em Gastroenterologia Veterinária." Primeira linha B (teste): "Olá, [nome]. Dúvida sobre como entrar na turma de Gastroenterologia?" Se a Ufape responder OU6 (véspera ou 1º dia do 3º módulo), a frase é ajustada.

---

## Slide C7. WhatsApp W4: o último toque antes da pausa

- **Etiqueta:** C · MATERIAIS · WHATSAPP 4 DE 4
- **Título-afirmação:** O último toque é uma pergunta simples, com a mesma regra.
- **Subtítulo:** Ter 12/01, 10h, depois do período sem campanha (21/12 a 03/01); pausa em 22/01.
- **Rótulo:** MODELO: troca por turma (mesmos campos do slide C6).
- **Conteúdo (balão, texto literal):**

> Olá, [nome]. Aqui é a equipe da Pós-graduação da Faculdade UFAPE.
>
> Passando para saber se você ainda pensa na Pós-graduação em Gastroenterologia Veterinária (turma IX, São Paulo).
>
> A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.
>
> Se quiser conversar, responda TURMA e o time de vendas te atende em horário comercial.
>
> Para não receber mais mensagens, responda SAIR.

- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.4 (v5). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** balão de WhatsApp; ao lado, a linha do tempo com os 4 toques (29/10, 06/11, 16/12, 12/01).
- **Notas do apresentador:** primeira linha A (teste): "Olá, [nome]. Ainda pensa na Pós-graduação em Gastroenterologia Veterinária?" Primeira linha B (teste): "Olá, [nome]. Voltando ao assunto da turma de Gastroenterologia." Em 12/01 há empate com o toque de 68604 para quem está nas duas turmas; vence a de maior GUT do plano geral (seção 8.2 do arquivo, [SUPOSIÇÃO]). Quem pagou a 1ª mensalidade sai da lista no dia; depois de 22/01 a turma sai de toda lista.

---

## Slide C8. E-mail T1: a apresentação da turma

- **Etiqueta:** C · MATERIAIS · E-MAIL 1 DE 2
- **Título-afirmação:** O primeiro e-mail abre com uma pergunta de rotina e leva à página.
- **Subtítulo:** Qua 28/10, 9h. Teste A/B de assunto.
- **Rótulo:** MODELO: troca por turma. Campos: assunto, abertura (gancho da casa de mensagens da área), nome do curso, turma, início, 1º presencial, carga, bullets da ficha, coordenação, link e UTM.
- **Conteúdo (e-mail, resumo; texto inteiro nas notas):**
  - **Assunto A (teste):** "Prática de cirurgia esofágica, gástrica e intestinal, em São Paulo"
  - **Assunto B (teste):** "Pós-graduação em Gastroenterologia Veterinária: início em 07/11, em São Paulo"
  - **Pré-visualização:** "Turma IX começa em 07/11/2026. Veja o cronograma e as condições na página."
  - **Abertura:** "Quantos casos gastrointestinais você encaminha por mês?"
  - **Botão:** "Ver a turma e as condições"
- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.1 (v5). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** mockup de caixa de entrada com os dois assuntos lado a lado e, abaixo, o e-mail aberto.
- **Notas do apresentador (corpo inteiro, texto literal):**

> Olá, [nome],
>
> Quantos casos gastrointestinais você encaminha por mês?
>
> Fechar o diagnóstico de uma enteropatia, de uma hepatopatia ou de uma pancreatopatia na rotina pede raciocínio clínico e prática, não só aula teórica.
>
> A Pós-graduação em Gastroenterologia Veterinária da Faculdade UFAPE (turma IX) começa em 07/11/2026 com o módulo 1 online; os módulos presenciais são na sede da Ufape, em São Paulo. O primeiro presencial é o módulo 6, em 17 e 18/04/2027. São 500 horas em 24 módulos, semipresencial.
>
> O que está na página da turma:
> - módulos presenciais de prática, como o 6, com anatomia, cirurgia esofágica, gástrica e intestinal e parasitologia ou transplante fecal;
> - grupo para discussão de casos entre alunos e coordenadores;
> - coordenação da Esp. Maria Carolina Pappalardo, com 38 nomes listados, coordenação incluída.
>
> Parcelas, total e matrícula estão na página da turma, junto com o cronograma completo.
>
> [Botão: Ver a turma e as condições]
>
> A turma pode não ser formada. Compre passagem e hotel só depois de a turma ser confirmada.
>
> Equipe da Pós-graduação, Faculdade UFAPE
>
> [RODAPÉ PADRÃO DO E-MAIL]

  - Rodapé padrão (literal, inserido pelo CRM): "Você recebe este e-mail porque aceitou receber comunicações da Faculdade UFAPE. Descadastrar em um clique: [link de descadastro]. Política de privacidade: [link]. Faculdade UFAPE, Av. 9 de Julho, 3939, São Paulo, SP." O endereço da política de privacidade é [CONFIRMAR] (pendência p04).
  - Botão leva a https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria?utm_source=email&utm_medium=crm&utm_campaign=pos_68606_202610&utm_content=t1-68606.
  - Reservas de assunto: "Olá, aquele caso gastrointestinal que você ainda encaminha"; "Gastroenterologia com grupo de discussão de casos com a coordenação"; "Do módulo 1 online à primeira aula prática: o cronograma da turma IX".
  - O gancho é [SUPOSIÇÃO de texto, persona de A6]. O texto é fixo da linha no bloco "A turma pode não ser formada" e no rodapé.

---

## Slide C9. E-mail E2: como entrar na turma que já começou

- **Etiqueta:** C · MATERIAIS · E-MAIL 2 DE 2
- **Título-afirmação:** O segundo e-mail troca a compra por conversa com o time.
- **Subtítulo:** Qua 02/12, 9h, depois do início, com a regra completa.
- **Rótulo:** MODELO: troca por turma. Campos: assunto, quais módulos em curso são online e onde é o 1º presencial (ficha), frase da regra com as datas, link wa.me do WhatsApp de vendas (ufape-geral: vendas São Paulo; Goiânia tem outro número).
- **Conteúdo (e-mail, resumo; texto inteiro nas notas):**
  - **Assunto A (teste):** "Prática de cirurgia esofágica, gástrica e intestinal, em São Paulo"
  - **Assunto B (teste):** "Pós-graduação em Gastroenterologia Veterinária: como entrar na turma que já começou"
  - **Regra (literal):** "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram."
  - **Botão:** "Falar com o time de vendas"
- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A.4 (v5). **Situação:** qa aprovado e aguardando aprovação humana (OA9).
- **Visual:** mockup de e-mail com o botão para o WhatsApp de vendas.
- **Notas do apresentador (corpo inteiro, texto literal):**

> Olá, [nome],
>
> A Pós-graduação em Gastroenterologia Veterinária da Faculdade UFAPE (turma IX, São Paulo) está em andamento. Os módulos 1 a 5 são online; o primeiro presencial é o módulo 6, em 17 e 18/04/2027, na sede da Ufape.
>
> A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram.
>
> O que está na página da turma:
> - 500 horas em 24 módulos, com módulos presenciais de prática, o primeiro em 17 e 18/04/2027;
> - grupo para discussão de casos entre alunos e coordenadores;
> - coordenação da Esp. Maria Carolina Pappalardo.
>
> Fale com o time para entender como entrar na turma. Parcelas, total e matrícula você vê na página da turma.
>
> [Botão: Falar com o time de vendas]
>
> Equipe da Pós-graduação, Faculdade UFAPE
>
> [RODAPÉ PADRÃO DO E-MAIL]

  - Botão: https://wa.me/5511913669290 com a mensagem pré-preenchida "Olá, vim do e-mail da Pós-graduação em Gastroenterologia Veterinária (turma 68606) e quero entender como entrar na turma." UTM não rastreia wa.me: a atribuição vai pela mensagem [CONFIRMAR com o arquiteto-de-fluxos, P15].
  - Reservas de assunto: "Gastroenterologia: a Ufape aceita matrícula até o 3º módulo"; "Grupo de discussão de casos entre alunos e coordenadores"; "Fale com o time sobre os módulos que já aconteceram".
  - Condição de envio: turma "aberto" no catálogo depois do início (OU9); a exceção do contexto da linha cobre o status "verificar" por turma iniciada.

---

## Slide C10. Anúncios Meta: o que existe para a 68606

- **Etiqueta:** C · MATERIAIS · META ADS
- **Título-afirmação:** Não há arquivo de anúncio Meta da 68606; há dois textos de exemplo, e o resto está no ar.
- **Subtítulo:** Texto principal, título e botão: o que a squad escreveu, e o que falta.
- **Rótulo:** MODELO: troca por turma. Campos: nome do curso, turma, início, 1º presencial (ficha e catálogo); regra do 3º módulo (ficha); data de troca de fase (plano da onda).
- **Conteúdo (texto literal do exemplo, [SUPOSIÇÃO de texto]):**
  - **Até 06/11, título:** "Pós-graduação em Gastroenterologia Veterinária para médicos veterinários formados"
  - **Até 06/11, texto principal:** "Turma IX em São Paulo, com início em 07/11/2026 e o módulo 1 online. Teoria online e 3 módulos presenciais de prática, o primeiro em 17 e 18/04/2027. Veja parcelas, total e matrícula na página da turma."
  - **De 07/11 a 22/01, texto (remarketing):** "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram."
  - **Botão (CTA):** [DADO NÃO FORNECIDO]. **Título do remarketing:** [DADO NÃO FORNECIDO].
- **Agente:** cmo (exemplos no roteiro); criativos-de-anuncio fará a adaptação do texto pós-início (E10, prazo 05/11). **Arquivo:** saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md, slide 8; o texto foi corrigido nas correções F1 e F2 e conferido na reconferência do qa de 28/10/2026. **Situação:** exemplo de texto, rascunho; o anúncio no ar é [CONFIRMAR].
- **Visual:** dois mockups de anúncio no feed, "até 06/11" e "a partir de 07/11", com o título, o texto e a página de destino.
- **Notas do apresentador:**
  - A campanha da 68606 roda desde antes da decisão 15, com estático e vídeo e 5 ângulos, e é candidata a fadiga (D20, uma troca até 03/11) [analise-de-midia-pos 3.2, citada no plano do cmo]. Quais criativos estão no ar e quais passam na conformidade: [CONFIRMAR na exportação D6].
  - Os anúncios que citam a data de início saem em 07/11. Depois, só remarketing e busca (OA4).
  - Nada de preço, valor de inscrição, bolsa, certificação ou "últimas vagas" em anúncio.
  - Conferido por grep: anuncios-meta-pos-2026-10-26.md não tem a 68606. A estrutura Meta por turma (campanha fria, remarketing, nomes e UTM) existe só para as turmas de março e abril (v7); é o molde para as turmas novas.

---

## Slide C11. Google Ads: palavras-chave existem, anúncio responsivo não

- **Etiqueta:** C · MATERIAIS · GOOGLE ADS
- **Título-afirmação:** A 68606 tem cinco palavras-chave pesquisadas; os títulos e descrições do anúncio responsivo não foram escritos.
- **Subtítulo:** Busca dominada por medicina humana: espaço aberto para a Ufape [SUPOSIÇÃO].
- **Rótulo:** MODELO: troca por turma. Termos vêm da seção da área em pesquisa-de-palavras-chave-pos (K<área>.x); a estrutura da campanha vem de anuncios-google-pos-2026-10-26.md (grupos __area e __marca, 1 anúncio responsivo por grupo na extensão).
- **Conteúdo (palavras-chave, texto literal, com intenção e pontuação M/D/F):**

| ID | Termo | Pontuação |
|---|---|---|
| K6.1 | pós-graduação em gastroenterologia veterinária | 62 (28/14/20) |
| K6.2 | pós em gastroenterologia veterinária de pequenos animais em São Paulo | 60 (30/8/22) |
| K6.3 | especialização em gastroenterologia de cães e gatos | 54 (26/8/20) |
| K6.5 | quanto custa pós em gastroenterologia veterinária | 52 (22/14/16) |
| K6.4 | pós em gastro vet (só lista de palavras e grupo de anúncio, não vai para texto visível) | 50 (24/8/18) |

  - **Títulos e descrições do RSA da 68606:** [DADO NÃO FORNECIDO]. **Palavras-chave negativas da 68606:** [DADO NÃO FORNECIDO].
- **Agente:** pesquisa-de-palavras-chave. **Arquivo:** saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md, seção "A6. Gastroenterologia" (linhas 413 a 432) e resumo, item 3 (linha 28). **Situação:** rascunho (versão 3, corrigida após o qa); estrutura da campanha de Busca da 68606 em anuncios-google-pos: não tem (grep).
- **Visual:** mockup de resultado de busca com URL e descrição em cinza tracejado ([DADO NÃO FORNECIDO]) e, ao lado, a tabela dos termos.
- **Notas do apresentador:**
  - Volume é qualitativo e [SUPOSIÇÃO]: K6.1 e K6.5 médio; K6.2, K6.3 e K6.4 baixo. Observação do arquivo: "resultados dominados por medicina humana (Afya e outras): espaço aberto [SUPOSIÇÃO]". K6.2: "turma começa em 12 dias: serve à próxima edição". K6.5 aponta para a seção de investimento do pilar.
  - O plano da mídia diz que de 07/11 a 22/01, 23h59, só entram remarketing e busca de marca e de maior intenção (gestor, 12.6 e 13.2; OA4). A palavra de maior intenção do gestor é "pós-graduação em <área> veterinária", que coincide com K6.1.
  - Palavra-chave de preço (K6.5) só leva à página; nenhum anúncio cita valor até a U11.
  - Pelo padrão de nome, o texto visível usa "Pós-graduação em Gastroenterologia Veterinária".
  - A conferência da página de destino antes de qualquer subida segue pendente (OA10).

---

## Slide C12. Roteiros e conceitos de criativos

- **Etiqueta:** C · MATERIAIS · CRIATIVOS E VÍDEO
- **Título-afirmação:** Os conceitos da 68606 vêm dos 3 ganchos recomendados; o roteiro de vídeo curto ainda não foi escrito.
- **Subtítulo:** Pacote de criativos por turma e roteiro de Reel: situação.
- **Rótulo:** MODELO: troca por turma. Para outra turma de março ou abril, o pacote de 5 peças base (3 conceitos frios c1, c2, c3 e 2 de remarketing r1 e r2) está em criativos-de-anuncio-pos-turmas-2026-10-26.md.
- **Conteúdo (tabela):**

| Conceito | Origem | Formato | Situação |
|---|---|---|---|
| A6-09 "Do módulo online de fisiologia à cirurgia na prática: o primeiro presencial de Gastroenterologia." | criador-de-ganchos, A6 | Reel | recomendado, roteiro não escrito |
| A6-03 "3 práticas em um módulo: anatomia, cirurgia digestiva e parasitologia ou transplante fecal." | criador-de-ganchos, A6 | Reel | recomendado, roteiro não escrito |
| A6-02 "Cirurgia esofágica, gástrica e intestinal na Pós-graduação em Gastroenterologia Veterinária? Veja o presencial." | criador-de-ganchos, A6, com o nome ajustado | Carrossel | recomendado, ajuste a registrar no arquivo |
| Roteiro de vídeo curto (kit) | agente tiktok | Reel | inventário pendente, prazo 05/11 |

- **Fonte:** criador-de-ganchos-pos-2026-10-26.md, seção 6; correção F15 do qa; pos-68606.json (kit.entregas, roteiro_video).
- **Visual:** três cartões de conceito (Reel, Reel, carrossel) e um quarto cartão cinza "roteiro de vídeo curto: pendente".
- **Notas do apresentador:**
  - A6-02 no arquivo do criador-de-ganchos ainda traz "pós de Gastroenterologia" e precisa da mesma troca de nome antes de virar carrossel (observação do qa, seção 6). Aqui o texto já está no padrão.
  - O pacote criativos-de-anuncio-pos-2026-10-26.md é da campanha das provas de bolsa (suspensa, decisão 14) e o criativos-de-anuncio-pos-turmas cobre março e abril; nenhum tem criativo da 68606 (ver slide C18 para o material da prova 68650).
  - Fim de ano: nenhum conceito novo na extensão, só adaptação de texto (E10).

---

## Slide C13. Os 10 ganchos da área A6

- **Etiqueta:** C · MATERIAIS · GANCHOS
- **Título-afirmação:** Dez ganchos de Gastroenterologia, três recomendados e um bloqueado até a U11.
- **Subtítulo:** Cada gancho vem da ficha; nenhum cita preço, bolsa ou certificação.
- **Rótulo:** MODELO: troca por turma (seção da área na tabela de ganchos; a lista de tipos e as regras G1 a G9 são fixas da linha).
- **Conteúdo (texto literal; formato entre parênteses):**
  - A6-09 (Reel, recomendado): "Do módulo online de fisiologia à cirurgia na prática: o primeiro presencial de Gastroenterologia."
  - A6-03 (Reel, recomendado): "3 práticas em um módulo: anatomia, cirurgia digestiva e parasitologia ou transplante fecal."
  - A6-02 (carrossel, recomendado): "Cirurgia esofágica, gástrica e intestinal na Pós-graduação em Gastroenterologia Veterinária? Veja o presencial." (nome ajustado ao padrão)
  - A6-07 (Reel): "24 módulos em dois anos: só 3 pedem você na sala."
  - A6-01 (carrossel): "38 professores listados: quem ensina Gastroenterologia Veterinária."
  - A6-04 (WhatsApp): "Gastroenterologia começa em 07/11. Fale com o time sobre a entrada."
- **Fonte:** criador-de-ganchos-pos-2026-10-26.md, seção 6 (v2). **Situação:** v2 corrigida após o qa; o plano do cmo trata a camada 2 como aprovada [CONFIRMAR, o cabeçalho ainda diz "para nova conferência"].
- **Visual:** seis cartões de gancho com o ícone do formato; os três recomendados em azul-petróleo.
- **Notas do apresentador (os 4 restantes, texto literal):**
  - A6-05 (carrossel): "Grupo de discussão de casos com a coordenação: o que a página prevê." Formato e frequência [CONFIRMAR].
  - A6-06 (anúncio): "Quanto custa a Pós-graduação em Gastroenterologia Veterinária? A conta inteira." BLOQUEADO até a U11; usar a versão sem valor.
  - A6-08 (carrossel): "O que a página diz sobre o estágio da pós de Gastroenterologia?" Regras, carga e local do estágio [CONFIRMAR].
  - A6-10 (WhatsApp): "Cronograma completo da Gastroenterologia, com as datas dos 3 módulos presenciais?"
  - Registro de grafia: no A6-08, a forma "pós de Gastroenterologia" do arquivo-fonte fica como está acima e deve virar "Pós-graduação em Gastroenterologia Veterinária" antes de ir ao ar; o A6-02 já foi trocado pela correção F15 do qa. Nenhum outro gancho citado nesta nota tinha o nome fora do padrão.
  - Restrições da área: sem "especialidade emergente e carente de profissionais", sem "coordenadores referências nacionais"; volume de prática de endoscopia não prometido; a prova de bolsa 68650 fica fora.

---

## Slide C14. Post de docente e Stories (AD-A6-1)

- **Etiqueta:** C · MATERIAIS · SOCIAL
- **Título-afirmação:** Um post de docente pronto: a coordenação em 3 Stories, na semana de 09 a 15/11.
- **Subtítulo:** Sai só com o ok e a revisão clínica da própria docente. Os 6 posts do kit ainda não foram escritos.
- **Rótulo:** MODELO: troca por turma. Campos: nome e titulação do docente (ficha, campo Coordenação ou Participantes); texto da tela 2 (ficha e casa de mensagens); semana e UTM (plano da onda). O checklist C1 a C8 e a regra "um post cita só o seu autor" são fixos da linha.
- **Conteúdo (Stories, texto literal):**
  - **Gancho (tela 1):** "Quando um caso gastrointestinal pede uma segunda opinião?"
  - **Tela 2:** "Sou Esp. Maria Carolina Pappalardo e coordeno a Pós-graduação em Gastroenterologia Veterinária da Faculdade UFAPE, em São Paulo. São 24 módulos e 500 horas, com 3 módulos presenciais, entre eles endoscopia e videocirurgia, e um grupo para discussão de casos entre alunos e coordenadores."
  - **Tela 3:** [PONTO DE VISTA A CONFIRMAR COM O DOCENTE] e "Fale com o time para saber como entrar na turma."
- **Agente:** autoridade-docente. **Arquivo:** saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md, seção 6 (v2). **Situação:** rascunho para a revisão da docente; pedido OA12.
- **Visual:** três quadros de Stories 9:16 em sequência, com a silhueta da docente (sem foto até ela aprovar).
- **Notas do apresentador:**
  - UTM: utm_campaign=pos_68606_202611; utm_content=docente-pappalardo. Encaixe: Stories da S3 (09 a 15/11).
  - Aprovar além do checklist: que a frase do grupo de discussão reflete o que ela conduz (formato e frequência [CONFIRMAR]); que o texto não cita o estágio.
  - A squad não escreve opinião clínica na voz do docente. Revisor docente do conteúdo clínico da Pós: [CONFIRMAR nome].
  - Os 6 posts orgânicos do kit (2 no feed e 4 em Stories, de 03/11 a 20/01, fora de 21/12 a 03/01; OA11) ainda não têm texto: inventário pendente. O posts-sociais-pos-2026-10-26.md cita a área A6 só como destino de campanha das provas (linha 223, item 7: "Pós-graduação em Gastroenterologia Veterinária (São Paulo)").
  - Lacuna de docentes: 37 dos 38 nomes sem post (OA8). O podcast pode fechar parte dela (card do convidado e corte contam como 1 post de docente, checklist C1 a C8; critério do qa de 28/10).

---

## Slide C15. Página da turma: a recomendação

- **Etiqueta:** C · MATERIAIS · PÁGINA
- **Título-afirmação:** A squad não cria página nova para a 68606: a correção é da página oficial.
- **Subtítulo:** Quatro correções no site destravam a página como entregue.
- **Rótulo:** MODELO: troca por turma. Campos: link da página (ficha); quais correções valem (cada turma tem seus erros: ficha e conformidade).
- **Conteúdo:**
  - **A7:** retirar a frase de certificação ligada ao órgão regulador
  - **A12:** turma mínima de 20 para 15
  - **A13:** escrever a regra "matrícula até o 3º módulo", com a data do 3º módulo (23/01/2027) e o que vale para os módulos perdidos (OU3)
  - **p04:** endereço da política de privacidade do formulário [CONFIRMAR]
- **Agente:** cmo, pedido OA10 ao site da Ufape. **Arquivo:** cmo-pos-2026-10-26.md, seção 8.1 (OA10); pos-68606.json (p01, p02, p04). **Situação:** pedido pendente; a página não conta como entregue.
- **Visual:** captura da página oficial com quatro marcas numeradas nos trechos a corrigir; rótulo "pedido à Ufape".
- **Notas do apresentador:**
  - Não há /pagina-de-curso para a 68606: a página oficial está no ar e a correção é da Ufape (roteiro do cmo, "Próximo passo"). A LP da Graduação é página separada e a squad nunca a altera.
  - O hub de prova de bolsa de landing-page-pos-2026-10-26.md é das provas (suspensas; ver C18).
  - Para as turmas de março e abril, as páginas novas estão em saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md e onda3.md, no formato de templates/pagina-da-turma.md; são o molde.
  - A página também mostra "1ª mensalidade paga até 30 dias antes do início" (ficha); como isso convive com a regra do 3º módulo é a OU8.

---

## Slide C16. Isca, conteúdo longo, nutrição, newsletter e YouTube

- **Etiqueta:** C · MATERIAIS · CONTEÚDO
- **Título-afirmação:** A isca da área A6 está especificada e reservada; não há artigo, nutrição nem vídeo próprios da 68606.
- **Subtítulo:** O que existe na linha, o que serve à área e o que ficou de fora, com o motivo.
- **Rótulo:** MODELO: fixo da linha (regras e estrutura); troca por turma (a isca da área, quando houver turma futura aberta).
- **Conteúdo (tabela):**

| Peça | Situação para a área A6 | Arquivo |
|---|---|---|
| Isca: "Gastroenterologia veterinária na Ufape: o que se pratica nos 3 módulos presenciais" | especificada, produção reservada: a turma começa em 07/11 e não há turma futura aberta | iscas-digitais-pos-2026-10-26.md, seção 8 |
| Artigos C03, C08 e C09 | da linha; a 68606 só aparece numa tabela de contraste | conteudo-longo-pos-2026-10-26.md, linha 107 |
| Nutrição NP3 | S10: área sem turma aberta depois de 07/11 | campanhas-de-nutricao-pos-2026-10-26.md, linha 159 |
| Newsletter geral | sem a 68606 no grep | newsletter-geral-2026-10-26.md |
| YouTube | nada da 68606 (grep); orgânico como casa do podcast | youtube-pos-2026-10-26.md |

- **Fonte:** arquivos da tabela.
- **Visual:** cinco ícones de formato; os que servem à área em azul-petróleo, os reservados em cinza.
- **Notas do apresentador:**
  - Isca, especificação: PDF de 4 a 6 páginas, ênfase no que se pratica; promessa "Veja o que a página oficial lista nos 3 módulos presenciais da Pós-graduação em Gastroenterologia Veterinária e como funciona o grupo de discussão de casos."; ponte para a 68606 com "Fale com o time para saber como entrar na turma."; revisor sugerido Esp. Maria Carolina Pappalardo [CONFIRMAR aceite]; esforço 4 h. Produzir só se a Ufape informar a regra de entrada tardia ou uma turma futura.
  - A estratégia de conteúdo diz que "a venda de reta final dessas turmas é do kit (WhatsApp de reta final), não deste plano". Nova isca ou artigo da A6 é novo pedido [CONFIRMAR OU4: há nova turma da área?]. O podcast (decisão 21) entra como nova fonte de conteúdo e substitui a avaliação "podcast fora".

---

## Slide C17. Respostas prontas do time de vendas

- **Etiqueta:** C · MATERIAIS · VENDAS
- **Título-afirmação:** Dez respostas prontas, com "vou confirmar" onde a Ufape ainda não decidiu.
- **Subtítulo:** Conversa 1 a 1 no WhatsApp de vendas, dentro da janela de 24 h aberta pelo candidato.
- **Rótulo:** MODELO: fixo da linha (as 10 respostas); troca por turma: os campos [início], [data do 3º módulo] e [link da turma], da tabela 7.2 do arquivo (ficha e catálogo).
- **Conteúdo (perguntas literais e, para a 68606, a resposta da R1):**
  - R1 "Ainda dá tempo de me matricular?" R2 "A página diz que a 1ª mensalidade é paga 30 dias antes do início. Já passou, ainda consigo entrar?" R3 "A turma já começou (ou começa em breve). Posso entrar depois do início?" R4 "Perdi o módulo 1 (ou o 2). Como reponho?" R5 "Se eu entrar agora, quando e como pago a 1ª mensalidade?" R6 "Tem vaga? A turma está confirmada?" R7 "Se a turma não fechar, perco o que paguei?" R8 "Tem bolsa ou desconto para entrar agora?" R9 "Posso esperar a próxima turma?" R10 "Qual o valor?"
  - **R1, resposta literal:** "Sim. [Frase-base com início e 3º módulo da tabela 7.2.] Se quiser, te ajudo a finalizar: [link da turma]. Parcelas, total e matrícula estão lá."
  - **Dados da 68606 (tabela 7.2):** início 07/11/2026; 2º módulo 19 e 20/12/2026, online; 3º módulo 23 e 24/01/2027, online; 1º presencial módulo 6, 17 e 18/04/2027; gravação: não consta na ficha.
- **Agente:** copy-de-mensagens. **Arquivo:** copy-de-mensagens-pos-onda1-2026-10-26.md, seção 7 (v5). **Situação:** qa aprovado e aguardando aprovação humana.
- **Visual:** lista de 10 perguntas em balões à esquerda e, à direita, a resposta da R1 e as marcas "vou confirmar" nas R2, R4, R5, R6.
- **Notas do apresentador (respostas literais, para a 68606):**
  - Frase-base: "A turma [começa em / começou em] [início]. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em [data do 3º módulo, tabela 7.2]. Antes de pagar, o time explica como ficam os módulos que já aconteceram."
  - R1, se perguntarem se vale no 1º dia do 3º módulo: "Vou confirmar com a secretaria e te respondo por aqui." [OU6]
  - R2: "A página traz essa orientação, e a Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em [data do 3º módulo]. Como fica o pagamento da 1ª mensalidade para quem entra agora, vou confirmar com o financeiro e te respondo por aqui." [OU8] Não dizer a data do corte nem "perdeu o prazo".
  - R3, depois do início: "Pode. A turma começou em [início]. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em [data do 3º módulo]. Antes de pagar, te explico como ficam os módulos que já aconteceram." Antes do início: "A turma começa em [início]. A Ufape aceita matrícula até o 3º módulo do curso, que nesta turma começa em [data do 3º módulo]. Você pode começar desde o módulo 1: [link da turma]."
  - R4: "Antes de você pagar, te explico como ficam os módulos que já aconteceram. Como é a reposição, vou confirmar com a coordenação e te respondo por aqui. Hoje não consigo te prometer gravação nem aula extra." [OU3] Para a 68606, não dizer que as aulas online ficam gravadas (a ficha não cita).
  - R5: "Vou confirmar com o financeiro como fica para quem entra depois do início e te respondo por aqui. Parcelas, total e matrícula estão na página da turma: [link da turma]." [OU8]
  - R6: "Vou confirmar com a secretaria e te respondo por aqui." Depois da resposta da Ufape: "Segundo a secretaria em [data], a turma [nº] [está confirmada / ainda não foi confirmada]." [OU4] Antes do início: "A página informa que a turma pode não ser formada; por isso a orientação é comprar passagem e hotel só depois de a turma ser confirmada." Nunca "últimas vagas" nem número de vagas sem dado da Ufape.
  - R7: "A página da turma informa que pedidos de reembolso dos valores de inscrição só são devidos caso a turma não seja confirmada. Sobre passagem e hospedagem, a página diz que a Ufape não se responsabiliza pelo ressarcimento em caso de adiamento das aulas presenciais por força maior. Por isso, compre passagem e hotel só depois de a turma ser confirmada."
  - R8: "Para esta turma, não tenho bolsa nem desconto confirmados para te oferecer. As condições estão na página da turma: [link da turma]." Se citarem o bloco de prova de bolsa da página da 68606: "Não consigo confirmar bolsa para esta turma [CONFIRMAR A-C2]; vou perguntar à Ufape e te respondo por aqui."
  - R9: "Hoje não tenho data de nova turma de [área] para te passar [CONFIRMAR OU4]. A Ufape aceita matrícula nesta turma até o 3º módulo, que começa em [data do 3º módulo]. Se quiser, te explico como ficam os módulos que já aconteceram."
  - R10: "Parcelas, total e matrícula da turma [nº] estão na página da turma: [link da turma]. Se quiser, te explico como funciona o pagamento." Sem valores em texto até a U11.
  - Regras do time: registrar no CRM cada pergunta de R1 a R9 por turma, só como contagem; dúvida acadêmica ou de certificado vai à secretaria; pedido de saída vira SAIR no CRM no mesmo dia.

---

## Slide C18. Material relacionado: a prova de bolsa de Gastroenterologia (68650)

- **Etiqueta:** C · MATERIAIS · RELACIONADO
- **Título-afirmação:** Existe material da prova de bolsa de Gastroenterologia, mas está fora da prioridade e com correção pendente.
- **Subtítulo:** Não serve como peça vigente da 68606.
- **Rótulo:** MODELO: troca por turma (cada área tem a sua prova, quando existe; código vem do catálogo, seção 3).
- **Conteúdo:**
  - **Prova:** 68650, Prova de Bolsa de Estudos para Gastroenterologia Veterinária, São Paulo, 27/11/2026 (palavras-chave da área).
  - **Onde há material:** criativos-de-anuncio-pos-2026-10-26.md (linha 566), landing-page-pos-2026-10-26.md (linha 912), posts-sociais-pos-2026-10-26.md (linha 671).
  - **Situação:** campanha das provas parada pela decisão 14; correção pendente pela decisão 20: os textos tratam a prova como "online", e ela é presencial, em São Paulo e em Goiânia.
  - **Uso:** nenhuma peça da 68606 cita a prova de bolsa como caminho para a turma.
- **Fonte:** decisões 14 e 20 (docs/execucao-2026-10-26.md); arquivos citados (linhas indicadas pelo grep do orquestrador). O texto desses arquivos não foi copiado, porque não é vigente.
- **Visual:** cartão cinza "fora da prioridade" com o selo "correção pendente (decisão 20)".
- **Notas do apresentador:** o plano do cmo e a casa de mensagens mandam a prova de bolsa da área ficar fora das peças da turma. Local da prova de Goiânia: [CONFIRMAR] (fichas 68640, 68642 e 68644 mostram endereço de São Paulo). Turma de destino da 68650: a página não informa [CONFIRMAR].

---

## Slide C19. O painel de todas as peças

- **Etiqueta:** C · MATERIAIS · PAINEL
- **Título-afirmação:** Todas as peças de todos os cursos estão no painel.
- **Subtítulo:** A 68606 é o primeiro preenchimento; as demais turmas seguem o mesmo molde.
- **Rótulo:** MODELO: fixo da linha.
- **Conteúdo:**
  - **Link do painel:** https://claude.ai/artifact/9RJcf5McdsLPewFA6kqy8z
  - **Frase do slide:** "Todas as peças de todos os cursos estão no painel."
- **Fonte:** informação do pedido do CEO (link do painel). O conteúdo do painel não foi aberto nesta sessão: [CONFIRMAR se o painel está atualizado com as versões citadas aqui].
- **Visual:** captura do painel com destaque para o filtro por curso e o link impresso.
- **Notas do apresentador:** o painel é a consulta; os arquivos citados em cada slide são a fonte. Para outra turma, o caminho é o JSON pos-<código>.json e as seções da área.

---

# BLOCO D. O que não temos e o que está em dúvida

Duas partes: **Parte 1, lacunas da linha** (resolvem-se uma vez só e valem para toda turma de Pós) e **Parte 2, lacunas por turma** (repetem-se em cada turma). Em cada slide: "não temos" separado de "temos, mas em dúvida". Quando há referência possível no deck da The Growth Hub (arquivo docs/insumos/tgh-plano-de-campanhas-cursos-tier1-v2.txt) ou na proposta do podcast (docs/insumos/ufape-podcast-proposta-2026-10-28.txt), aparece como "referência disponível"; a resposta continua [CONFIRMAR]. Prazo só quando a fonte tem um.

## PARTE 1. Lacunas da linha (resolvem uma vez, valem para toda turma)

## Slide D1. Entrada depois do início e reposição de módulos

- **Etiqueta:** D · LINHA · REGRAS DE ENTRADA
- **Título-afirmação:** A regra de entrada existe; faltam a reposição, o pagamento e o dia limite.
- **Subtítulo:** Uma resposta da Ufape vale para toda turma de Pós.
- **Rótulo:** resolve uma vez; vale para toda a linha.
- **Conteúdo (tabela):**

| Item | O que falta | Quem responde | O que trava | Prazo |
|---|---|---|---|---|
| NÃO TEMOS: OU3, reposição | como o aluno repõe os módulos perdidos; gravação; o módulo presencial | Ufape (coordenação) | nenhuma peça promete reposição; time diz "vou confirmar" | 30/10 |
| NÃO TEMOS: OU8, pagamento | quando e como paga a 1ª mensalidade quem entra depois do início; ajuste de parcelas | Ufape (financeiro) | respostas R2, R5, R8 ficam em "vou confirmar" | 30/10 |
| EM DÚVIDA: OU6 | "até o 3º módulo" é até a véspera ou inclui o 1º dia? | Ufape | data de pausa; a mídia usa a véspera | 30/10 |
| NÃO TEMOS: OU9 | catálogo marcar turma iniciada como "aberto" | orquestrador, com a Ufape | não trava, pela exceção da decisão 18 | - |

- **Fonte:** cmo-pos-2026-10-26.md, seção 3 (OU3, OU6, OU8, OU9); decisão 18; contexto/pos-graduacao.md.
- **Visual:** quatro cartões com a trava e a pergunta; selo "uma vez só".
- **Notas do apresentador:** sem resposta, nenhuma peça usa urgência com a data do 3º módulo sem a frase completa. Referência disponível: nenhuma no deck nem na proposta do podcast.

---

## Slide D2. Preço, inscrição e texto de certificação

- **Etiqueta:** D · LINHA · PREÇO E REGULAÇÃO
- **Título-afirmação:** Sem a resposta sobre a inscrição e o texto oficial, nenhuma peça cita preço ou certificação.
- **Subtítulo:** Dois temas da linha toda.
- **Rótulo:** resolve uma vez; vale para toda a linha.
- **Conteúdo (tabela):**

| Item | O que falta | Quem responde | O que trava | Prazo |
|---|---|---|---|---|
| EM DÚVIDA: U11, valor da inscrição | R$ 260,00 (CEO) ou R$ 250,00 (site; R$ 350,00 em 3 cursos)? | CEO ou Ufape | nenhuma peça cita valor; a regra da linha exige parcelas, total e matrícula juntos | 30/10 |
| NÃO TEMOS: texto oficial de certificação | texto aprovado pela regulação | Ufape (regulação) | nenhuma peça afirma certificação; p01 | [DADO NÃO FORNECIDO] |
| NÃO TEMOS: API do WhatsApp (U11a) | se a Ufape usa a API oficial ou o aplicativo | Ufape | nomes de template valem só com a API | sem prazo na fonte |
| EM DÚVIDA: regra de desconto de aluno e ex-aluno | regra a preencher | Ufape | nenhum desconto entra em peça | sem prazo na fonte |

- **Fonte:** pendencias-camada-1.md (U11, U11a); contexto/pos-graduacao.md; pos-68606.json (p01, p03); mensagens-pos, regra 3 e regra 5.
- **Visual:** quatro cartões com cadeado.
- **Notas do apresentador:** o site usa uma frase de certificação ligada ao órgão regulador que a squad não repete. Referência disponível: nenhuma.

---

## Slide D3. Podcast

- **Etiqueta:** D · LINHA · PODCAST
- **Título-afirmação:** O podcast tem proposta e decisão do CEO; falta quem produz, quanto custa e se o nome está livre.
- **Subtítulo:** Sem estas respostas o episódio 1 não sai em 24/11 [SUPOSIÇÃO de calendário].
- **Rótulo:** resolve uma vez; vale para toda a linha.
- **Conteúdo (tabela):**

| Item | O que falta | Quem responde | O que trava | Referência disponível (proposta do podcast) |
|---|---|---|---|---|
| EM DÚVIDA: nome | aprovar UFAPE Cast ou outro; disponibilidade do nome e dos perfis | CEO e Ufape | identidade e canais | recomenda UFAPE Cast e lista 5 alternativas; "disponibilidade ainda não verificada" |
| NÃO TEMOS: equipe | quem grava, edita e publica; horas por semana | Ufape | calendário quinzenal | etapas e papéis do modelo de produção, com "pessoa de aprovação final" a definir |
| NÃO TEMOS: custo e local | custo de produção; local de gravação | Ufape e CEO | fora dos R$ 2.000,00 de mídia | a quantidade por episódio "pode acompanhar a capacidade da equipe" |
| NÃO TEMOS: convidados e autorização | convidados, egresso, autorização de imagem por episódio, canal do YouTube | Ufape | pauta de cada episódio | pauta sugerida "Como escolher minha pós?" (professor e egresso) |

- **Fonte:** cmo-pos-2026-10-28-apresentacao-68606.md, slides 12 e 17; decisão 21; ufape-podcast-proposta-2026-10-28.txt.
- **Visual:** quatro cartões com a referência ao lado.
- **Notas do apresentador:** prazo sugerido para o nome e os perfis: 06/11 [SUPOSIÇÃO de prazo do cmo]. A identidade visual da proposta foi adaptada do site público, não de um manual de marca: manual da marca [CONFIRMAR]. Os temas clínicos dos episódios passam por [REVISÃO DOCENTE]; revisor nomeado [CONFIRMAR].

---

## Slide D4. Ferramentas, medição e aprovação

- **Etiqueta:** D · LINHA · FERRAMENTAS E DADOS
- **Título-afirmação:** Sem CRM, analytics e aprovador definidos, a leitura semanal fica manual.
- **Subtítulo:** O que a Ufape ainda não informou sobre as ferramentas.
- **Rótulo:** resolve uma vez; vale para toda a linha.
- **Conteúdo (tabela):**

| Item | O que falta | Quem responde | O que trava | Referência disponível |
|---|---|---|---|---|
| NÃO TEMOS: CRM e funil | ferramenta e estrutura | Ufape | leitura de leads, inscrições e matrículas | deck TGH, slide 25: dashboards para cruzar campanhas, CRM e comercial |
| NÃO TEMOS: analytics | GA4, Meta e Google Ads exportados | Ufape | custo por lead e por matrícula | deck TGH, slide 25 (recomendação, não fato) |
| NÃO TEMOS: quem executa | quem opera gerenciador e CRM | Ufape | toda ação humana | - |
| NÃO TEMOS: quem aprova | tabela de aprovação em ufape-geral.md | Ufape | quem aprova verba, envio, página | - |
| NÃO TEMOS: posicionamento e voz | posicionamento em uma linha; exemplos de voz | Ufape | pendente das auditorias | - |

- **Fonte:** contexto/ufape-geral.md (seções Ferramentas e Regras de aprovação); cmo-pos-2026-10-26.md, seção 8 (quem executa [CONFIRMAR]); qa-de-marketing-pos-2026-10-28-apresentacao.md, F17.
- **Visual:** cinco cartões com a referência em cinza.
- **Notas do apresentador:** a ferramenta do deck da The Growth Hub é recomendação; a decisão de adotar é do CEO. Estas lacunas são preenchidas uma vez e servem a todas as turmas e linhas.

---

## Slide D5. Metas de custo e dúvidas de interpretação da linha

- **Etiqueta:** D · LINHA · INTERPRETAÇÃO
- **Título-afirmação:** Três dúvidas de interpretação mudam a leitura da meta de R$ 133,33 por matrícula.
- **Subtítulo:** Existem, mas estão em dúvida; resolvem uma vez.
- **Rótulo:** resolve uma vez; vale para toda a linha.
- **Conteúdo (tabela):**

| Item | A dúvida | Quem responde | O que trava | Referência disponível |
|---|---|---|---|---|
| CPA do deck | mede cadastro, inscrição ou matrícula? (R$ 210,51 na conta, R$ 168,50 na Imersão Cirurgia, GO) | The Growth Hub | se for custo por matrícula, já passa do teto de R$ 133,33 | deck TGH, slide 6 |
| Mmid | quantas das 15 matrículas vêm de fora da mídia | Ufape (comercial) | CPL máximo e verba | sem referência |
| Metas de custo | CPL máximo, custo por matrícula máximo, histórico de conversão, evasão, desconto | Ufape (financeiro) | o gestor usa 3 cenários [SUPOSIÇÃO] | fórmulas do gestor (12.2 a 12.4) |
| Taxas do funil | 5%, 10%, 15% e 60%, 75%, 90% | Ufape (histórico) | são ilustrativas | sem referência |

- **Fonte:** cmo-pos-2026-10-28-apresentacao-68606.md, slides 6 e 17; gestor-de-midia-pos-2026-10-26.md, seções 12.2 a 12.4; decisões 15 e 16. Prazo sugerido: 03/11 (CPA e Mmid, roteiro do cmo).
- **Visual:** quatro cartões; o CPA em destaque.
- **Notas do apresentador:** o teto de verba da fase 1 (R$ 250,00) e da fase 2 (R$ 1.750,00) é "teto se G = 0", conta do cmo sobre a fórmula do gestor, não meta. O teto D16 de mensagens (2 + 2 por semana, 1 por dia) é [SUPOSIÇÃO do cmo], sem referência publicada de frequência.

---

## PARTE 2. Lacunas que se repetem em cada turma

## Slide D6. Dados de funil e verba da turma

- **Etiqueta:** D · TURMA · FUNIL E VERBA
- **Título-afirmação:** Nenhum número real da 68606 chegou: gasto, leads, inscrições e matrículas são [CONFIRMAR].
- **Subtítulo:** Os mesmos campos se repetem em cada turma.
- **Rótulo:** repete em cada turma. Origem do campo: JSON da turma (numeros_agregados e metas), exportações do gerenciador (D6 do gestor) e CRM.
- **Conteúdo (tabela):**

| Item | Situação | Quem responde | O que trava | Prazo |
|---|---|---|---|---|
| NÃO TEMOS: G, gasto acumulado do ciclo (PP15, OA1) | [CONFIRMAR] | Ufape (quem opera o gerenciador) | diária e divisão por praça | 28/10 |
| NÃO TEMOS: leads antes e depois do início | [DADO NÃO FORNECIDO] | Ufape | custo por lead | toda segunda-feira |
| NÃO TEMOS: inscrições pagas e 1ª mensalidade paga | só somadas | Ufape (comercial) | leitura contra a meta de 15 | toda segunda-feira |
| NÃO TEMOS: vagas totais e restantes (OU4, p06) | [CONFIRMAR] | Ufape (secretaria) | texto de turma confirmada | toda segunda-feira |
| NÃO TEMOS: criativos no ar e aprovados (OU5) | [CONFIRMAR] | Ufape | kit, lacuna OA8 | 28/10 |
| EM DÚVIDA: Goiás + DF com 20% numa turma de São Paulo | manter como teste ou passar parte para SP | Ufape (aprovação humana) | divisão da verba | 03/11 |

- **Fonte:** pos-68606.json (metas, numeros_agregados, p05, p06); cmo-pos-2026-10-26.md, seção 3 (OU4, OU5) e OA1; gestor-de-midia-pos-2026-10-26.md, 12.7 (PP15); roteiro do cmo, slides 7 e 17.
- **Visual:** tabela com campos em cinza tracejado ([CONFIRMAR]).
- **Notas do apresentador:** referência disponível: o deck da The Growth Hub traz a divisão por praça (30%, 25%, 20%, 14%, 11%) e a lógica de testar Goiás + DF; o plano da onda 1 usa essa divisão como limite de leitura na 68606.

---

## Slide D7. Regras da turma

- **Etiqueta:** D · TURMA · REGRAS
- **Título-afirmação:** Faltam o fim das inscrições, o estágio, o grupo de casos e a confirmação da turma.
- **Subtítulo:** Dados da ficha que a squad não pode afirmar sozinha.
- **Rótulo:** repete em cada turma. Origem do campo: ficha da turma e catálogo; [CONFIRMAR NO CATÁLOGO] quando só a ficha traz.
- **Conteúdo (tabela):**

| Item | Situação | Quem responde | O que trava |
|---|---|---|---|
| NÃO TEMOS: fim das inscrições (p08) | não consta no catálogo nem na ficha; com a decisão 18, passa a ser a véspera do 3º módulo [CONFIRMAR OU6] | Ufape | data do pedido de pausa |
| NÃO TEMOS: regras do estágio | a ficha cita "Estágios com a cooperação em suas clínicas/hospitais" sem regras | Ufape | nenhuma peça cita estágio |
| EM DÚVIDA: grupo de discussão de casos | formato e frequência | Ufape (coordenação) | texto do pilar |
| EM DÚVIDA: turma confirmada e turma mínima | mínimo 15 (decisão 11); a página diz 20 | Ufape | frase "pode não ser formada" sem número |
| NÃO TEMOS: turma de destino da prova de bolsa 68650 | não aparece na página | Ufape | a prova fica fora das peças |
| NÃO TEMOS: kit, prazos de cada entrega (p09) | prazo não lançado no JSON | cmo | calendário do kit |

- **Fonte:** pos-68606.json (p06, p08, p09); mensagens-pos, seção 7; contexto/pos-graduacao.md; decisão 11.
- **Visual:** tabela com selo "da ficha".
- **Notas do apresentador:** referência disponível: nenhuma no deck nem na proposta do podcast. Prazo: o pedido de pausa da 68606 é 22/01, 23h59, [SUPOSIÇÃO: véspera do 3º módulo].

---

## Slide D8. Página e formulário

- **Etiqueta:** D · TURMA · PÁGINA E FORMULÁRIO
- **Título-afirmação:** A página oficial não passa na conformidade e o formulário não tem política de privacidade.
- **Subtítulo:** Cada turma tem a sua lista de correções.
- **Rótulo:** repete em cada turma. Origem do campo: ficha (texto da página) e conformidade-educacional.
- **Conteúdo (tabela):**

| Item | Situação | Quem responde | O que trava |
|---|---|---|---|
| NÃO TEMOS: A7, frase de certificação retirada | na página | Ufape (site) | página não conta como entregue |
| NÃO TEMOS: A12, turma mínima 15 | página diz 20 | Ufape (site) | idem |
| NÃO TEMOS: A13, regra do 3º módulo | ausente | Ufape (site) | a página não confirma o que a mensagem diz |
| NÃO TEMOS: p04, política de privacidade | endereço [CONFIRMAR] | Ufape (jurídico) | formulário e peças |
| EM DÚVIDA: envio antes da troca da frase | se a regulação permite | Ufape (regulação) | OA9 |

- **Fonte:** cmo-pos-2026-10-26.md, OA10 e regra 9; pos-68606.json (p02, p04); otimizador-de-cta-pos-2026-10-27-onda2.md (OB1); pendencias-camada-1.md, seção 3.
- **Visual:** quatro marcas sobre a captura da página.
- **Notas do apresentador:** prazo: "o quanto antes" (roteiro do cmo). Referência disponível: nenhuma. Os pedidos A4, A8 e A9 do plano do cmo-geral não foram lidos e não se aplicam à 68606 pelos arquivos desta sessão [CONFIRMAR].

---

## Slide D9. Docentes e autorizações

- **Etiqueta:** D · TURMA · DOCENTES
- **Título-afirmação:** A autorização dos docentes está decidida; falta a contagem no mapa, o revisor e os convidados de fora.
- **Subtítulo:** Docentes só com nome e titulação da ficha.
- **Rótulo:** repete em cada turma. Origem do campo: ficha (coordenação e Participantes) e decisões 8 e 10.
- **Conteúdo (tabela):**

| Item | Situação | Quem responde | O que trava |
|---|---|---|---|
| EM DÚVIDA: duplicidade de nome | "Profa. Ísis Carvalho" e "ESP. Isis de Carvalho Rodrigues Santana Lemes" podem ser a mesma pessoa | Ufape | contagem dos 38 |
| NÃO TEMOS: contagem no mapa (p07) | autorização registrada para todos (decisões 8 e 10); falta lançar as contagens | cmo | campo equipe do JSON |
| NÃO TEMOS: revisor docente do conteúdo clínico | nome | Ufape | posts e episódios clínicos |
| NÃO TEMOS: ok de cada docente | texto inteiro de cada post | cada docente | AD-A6-1 e os outros 37 |
| NÃO TEMOS: egresso e convidados de fora | nome e autorização por episódio | Ufape | podcast |

- **Fonte:** pos-68606.json (p07); autoridade-docente-pos-2026-10-26.md, seção 0; roteiro do cmo, slide 11 e slide 14; decisões 8, 10 e 21.
- **Visual:** mosaico dos 38 cartões cinza com o contador.
- **Notas do apresentador:** referência disponível na proposta do podcast: a etapa "Preparação" cita "convite, roteiro, nomes, funções e fotos autorizadas" e o checklist de revisão cita "convidado e uso de imagem alinhados".

---

## Slide D10. Dúvidas de interpretação da apresentação

- **Etiqueta:** D · TURMA · O QUE QUER DIZER
- **Título-afirmação:** Cinco números e frases da apresentação têm mais de uma leitura possível.
- **Subtítulo:** Existem, mas é preciso confirmar o que significam.
- **Rótulo:** repete em cada turma (o número muda; a pergunta é a mesma).
- **Conteúdo (tabela):**

| Item | Leitura em dúvida | Quem responde |
|---|---|---|
| R$ 133,33 por matrícula | média máxima do ciclo, com G = 0 como teto, não meta | CEO |
| "Matrícula" | 1ª mensalidade paga; a inscrição paga conta na meta, medida à parte (decisão 16) | CEO |
| Dias até o início | 10 dias de 28/10 a 07/11, mesma contagem do mapa | cmo |
| 3 presenciais | datas do módulo 21 só como "julho de 2028", sem dia | Ufape |
| Canais no mapa | pos-68606.json ainda traz podcast "fora" e LinkedIn "teste"; a decisão 21 e o qa dizem outra coisa | orquestrador |

- **Fonte:** decisões 15, 16 e 21; qa-de-marketing-pos-2026-10-28-apresentacao.md, seções 6 e 8.3; pos-68606.json (canais); ficha da 68606.
- **Visual:** cinco cartões "o slide diz" e "pode querer dizer".
- **Notas do apresentador:** o qa registrou que o JSON precisa de nova revisão dos canais pelo orquestrador; a A6-02 no arquivo do criador-de-ganchos também espera revisão. Nada disso bloqueia a apresentação, que é interna.

---

## Fatos (com fonte)

- 4 WhatsApp (T2, W2, W3, W4) e 2 e-mails (T1, E2) da 68606: copy-de-mensagens-pos-onda1-2026-10-26.md, seção 6A (v5); qa aprovado, aguardando aprovação humana (pos-68606.json).
- Planos de 8 canais e de mídia: qa aprovado e aguardando aprovação humana (pos-68606.json).
- Posts, criativos, post por docente (além do AD-A6-1), roteiro de vídeo e página: inventário pendente (pos-68606.json).
- 10 respostas do time: copy-de-mensagens-pos-onda1-2026-10-26.md, seção 7.
- Ganchos e AD-A6-1: criador-de-ganchos-pos e autoridade-docente-pos, versão 2. Palavras-chave K6.1 a K6.5: pesquisa-de-palavras-chave-pos, seção A6. Isca A6: iscas-digitais-pos, seção 8.
- Pendências p01 a p09 e OA1, OA4, OA8 a OA12: pos-68606.json.
- Decisões 1 a 21: docs/execucao-2026-10-26.md.

## [SUPOSIÇÃO]

- Textos de exemplo de anúncio (slide C10): [SUPOSIÇÃO de texto] do cmo.
- Calendário do podcast e prazo de 06/11: [SUPOSIÇÃO] do cmo.
- Teto D16 de mensagens, taxas do funil e divisão de verba por fase: [SUPOSIÇÃO] do cmo e do gestor.
- Ganchos de e-mail e palavra TURMA: [SUPOSIÇÃO de texto] do copy-de-mensagens.
- Volume das palavras-chave: [SUPOSIÇÃO] do agente de pesquisa.
- Substituição do arquivo reta-final pelo onda1 v5: inferência deste agente, pelo mapa e pelo plano do cmo.
- Papel de modelo: o rótulo "fixo" ou "troca por turma" e as origens dos campos são classificação deste agente, a validar com o cmo.

## [CONFIRMAR]

- Criativos no ar da 68606, título e botão dos anúncios, RSA e palavras-chave negativas do Google.
- As 2 ocorrências da 68606 em criativos-de-anuncio-pos-turmas-2026-10-26.md.
- Se o cmo declara a substituição do arquivo reta-final.
- Conteúdo atual do painel do artifact.
- Lacunas dos slides D1 a D10.

## Fontes

- Todos os arquivos listados em "Entradas lidas", no cabeçalho.
- Painel de peças: https://claude.ai/artifact/9RJcf5McdsLPewFA6kqy8z (informado no pedido; não aberto).

## Contagem e próximo agente

- Bloco C: 19 slides (C1 a C19). Bloco D: 10 slides (D1 a D10), em duas partes: D1 a D5 (linha) e D6 a D10 (turma).
- Próximo agente sugerido: backlog-de-otimizacao.
