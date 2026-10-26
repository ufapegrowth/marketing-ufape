# Análise CRO: Pós-graduação e prova de bolsa (raio-x de uma página-modelo por tipo)

- **Agente:** analise-cro (departamento 08 Conversão), etapa 1.30 da camada 1
- **Linha:** pos
- **Data:** 26/10/2026
- **Skill usada:** .claude/skills/raio-x-de-pagina/SKILL.md
- **Status:** rascunho para o qa-de-marketing e para a aprovação da pessoa do marketing. Nada foi publicado, enviado ou pago.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/cursos-livres.md
  - contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seções 2 e 3, para conferir dados)
  - templates/pagina-da-turma.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1, 2 e 7, e as seções 3 e 4 para prazos e ondas)
  - auditorias/08-conversao.md e auditorias/conformidade-educacional.md
  - Fichas: contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md, contexto/cursos/pos/68610-pos-graduacao-em-dermatologia-veterinaria.md e contexto/cursos/pos/68639-prova-de-bolsa-de-estudos-para-anestesiologia-veterinaria.md (seção "Texto da página")

## Como ler este documento

- **Evidência (E):** está no texto copiado da página, na ficha ou no catálogo, ou é conta feita a partir desses dados (a conta aparece indicada).
- **Hipótese (H):** opinião do agente sobre o efeito na conversão. Toda hipótese leva [SUPOSIÇÃO].
- **Lado de quem resolve:** SQUAD (texto que a squad escreve), SITE (mudança no site atual ou na plataforma nova) e UFAPE (decisão ou confirmação da Ufape).
- **Impacto:** alto, médio ou baixo, avaliação do agente, não medida.

### Limites desta análise

- Não há dado de tráfego, GA4, mapa de calor, gravação de sessão nem taxa de conversão. Tudo que depende de número vira [CONFIRMAR].
- Não consegui abrir faculdade.ufape.com.br. O texto copiado não mostra layout, imagens, botões flutuantes, cabeçalho, rodapé nem o botão de WhatsApp. Por isso, o que digo sobre "primeira tela do celular" é inferido pela ordem do texto e é [SUPOSIÇÃO] até alguém abrir a página no celular. Se o site tem WhatsApp fixo, depoimentos em imagem ou formulário de lead que o texto copiado não traz, a conclusão correspondente muda. [CONFIRMAR no site, no celular]
- Que a maior parte dos candidatos chega pelo celular é [SUPOSIÇÃO] até confirmar no GA4.
- Teste A/B exige tráfego medido. Os testes abaixo são desenhos para o agente desenho-de-experimentos refinar, não testes aprovados.
- Pontos de conformidade (frase ligada ao MEC, urgência, bolsa, preço) vão para a lista de cada página. Não foram reescritos.

---

## Página 1: Pós com turma aberta, 707 Pós-graduação em Oftalmologia Veterinária (modelo de pós de ticket mais alto)

**Dados conferidos no catálogo (seção 2):** São Paulo, semipresencial, turma VII, início 30/10/2026 (planilha e site), 600 h, 24 módulos, 30x de R$ 1.590,00, total de R$ 47.700,00, matrícula de R$ 250,00, status aberto. A ficha confere com o catálogo. Faltam 4 dias para o início (conta a partir de 26/10/2026). Está na onda 1, com campanha ativa na visão de campanhas citada no plano do cmo.

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | Título "Pós-graduação em Oftalmologia Veterinária", turma VII, no topo (E) | Passa |
| Para quem? | "Médicos Veterinários" só aparece perto do fim, em PÚBLICO-ALVO. O parágrafo de abertura fala em "médicos-veterinários capacitados" como resultado, não como público (E) | Passa em parte |
| Qual modalidade? | SEMIPRESENCIAL no bloco de números. Quantos módulos presenciais e quantos online só se descobre lendo o cronograma inteiro (E) | Passa em parte |
| O que fazer agora? | Botão COMPRAR. Não há segundo caminho no texto (E) | Passa para quem já decidiu, falha para quem ainda compara [SUPOSIÇÃO] |

### O que já funciona (E)

- Preço completo e coerente: parcela, total e matrícula, com a forma de pagamento da matrícula. 30 x R$ 1.590,00 dá R$ 47.700,00 (confere). Atende a regra da linha de mostrar parcelas, valor da parcela, total e matrícula.
- Coordenação nomeada (três pessoas) e lista de docentes. Para a persona, docente é a principal prova de autoridade (contexto/pos-graduacao.md).
- Diferenciais concretos: um microscópio individual por aluno, supervisão constante, atendimentos clínicos reais em mutirões. Isso responde à objeção "quanta prática real" melhor que adjetivo.
- Cronograma completo com marcação "On-line" e "Presencial" em cada módulo, mais horários dos três dias.
- Transparência sobre turma mínima, reembolso só se a turma não for confirmada, e orientação para só comprar passagem e hotel com a turma fechada. Isso responde à objeção 3 da linha (medo de a turma não fechar).
- Aviso claro de que as aulas presenciais e práticas não são transmitidas nem gravadas.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | Só existe um caminho: COMPRAR, para um investimento de R$ 47.700,00 mais matrícula. Não há "falar com o time", "receber o programa" nem formulário de lead no texto copiado. | Chamada para ação | E (ausência no texto); H (efeito) [SUPOSIÇÃO: nesse ticket o candidato costuma conversar antes de pagar; validar com o WhatsApp de vendas] | Alto | SITE e SQUAD |
| 2 | As três objeções centrais (valor, tempo e viagem, turma que não fecha) estão enterradas: a política da turma e do reembolso fica em CONSIDERAÇÕES, no fim da página. Quantos módulos exigem viagem (10 presenciais e 14 online, conta feita sobre o cronograma; os módulos 11 e 22 têm rótulo misto) não aparece resumido em nenhum lugar. | Objeções sem resposta | E (posição no texto e contagem); H (efeito) | Alto | SITE (números) e SQUAD (texto) |
| 3 | Regra da 1ª mensalidade: "paga com 30 dias de antecedência da data de início". O início é daqui a 4 dias. A página não diz o que vale para quem entra agora. | Preço e condições | E (conflito entre a regra e a data); H (hesitação) | Alto | UFAPE (regra) e SQUAD (texto) |
| 4 | Pouca prova social: sem depoimento, sem vídeo, sem dado de egressos, sem uso explícito da tradição ("Turma VII" aparece só como rótulo). O bloco PATROCINADORES E PARCEIROS aparece vazio no texto copiado. | Prova e confiança | E (ausência no texto copiado); H (efeito) | Médio a alto | UFAPE (material e autorização) e SITE |
| 5 | Urgência real existe e não é usada: início em 4 dias é fato. A página não mostra data-limite de matrícula nem contagem para o início. | Urgência | E (data); H (efeito) | Médio | SQUAD e UFAPE (data-limite) |
| 6 | Erros no cronograma e no texto: "24, 25 e 25 de março de 2028", "Teórico/Prátrico/Presencial", "Palestrantes Convidados" repetido, "CONVIDADO: DR..." no meio da lista. | Confiança | E; H (efeito em quem examina o valor) | Médio | UFAPE (corrigir no site) |
| 7 | Duração em tempo (anos) não está no topo: só "600 horas" e "24 módulos". A duração de cerca de 2 anos é informação do contexto da linha, não do texto desta página. | Clareza da oferta | E (ausência); H (efeito) | Médio | SITE (campo de dado) e UFAPE (confirmar no catálogo) |
| 8 | Valor total com matrícula (R$ 47.950,00, conta feita: R$ 47.700,00 mais R$ 250,00) não aparece. A matrícula está separada do total. | Preço e condições | E (conta); H (efeito) | Baixo a médio | SITE |
| 9 | Seção de certificação sem texto aprovado (ver lista de conformidade). | Confiança | E | Médio | UFAPE (regulação) |
| 10 | Ufape Clínica (hospital veterinário próprio) não é citada na página, embora seja um diferencial a provar em ufape-geral.md. | Prova | E (ausência); [CONFIRMAR] se os mutirões acontecem lá | Baixo a médio | UFAPE |

### Correções por prioridade

**O que a squad escreve (texto, sem número, no formato do template)**

1. Hero. Título (até 70 caracteres): "Pós-graduação em Oftalmologia Veterinária". Subtítulo (até 160 caracteres): "Clínica e cirurgia oftalmológica para médicos veterinários, com teoria online ao vivo e prática presencial, com um microscópio para cada aluno." Motivo: coloca "para quem" e o diferencial mais forte na primeira tela. A imagem é escolha do editor.
2. Bloco "Como a turma é confirmada" perto do preço. Texto: "A turma começa quando atinge o mínimo de alunos informado nesta página. Por isso, compre passagem e hotel só depois da confirmação. Se a turma não for confirmada, a Ufape devolve os valores de inscrição. [CONFIRMAR: o que é devolvido, em quanto tempo e se inclui mensalidade]". Fonte: CONSIDERAÇÕES da ficha.
3. Frase de apoio do investimento: "Veja o valor de cada parcela, o total e a matrícula. Se tiver dúvida sobre pagamento ou rotina dos módulos, fale com o time de vendas antes de decidir."
4. Texto do botão secundário e frase de apoio do formulário: botão "Falar com o time no WhatsApp"; frase "Tire dúvidas sobre investimento, rotina de módulos e viagem. Respondemos em horário comercial. [CONFIRMAR horário e responsável]".
5. FAQ sem número, depois das perguntas que já existem na turma: "Preciso ir a São Paulo todo mês?" (resposta com os números do banco: [CONFIRMAR]); "O que acontece se a turma não fechar?"; "Posso entrar com a turma já em andamento?" ([CONFIRMAR com a Ufape]); "As aulas presenciais ficam gravadas?" (resposta na página: não).
6. Para quem (3 a 5 itens a partir de publico_alvo da ficha): médico veterinário que quer atuar em clínica e cirurgia oftalmológica; que quer treinar microcirurgia com acompanhamento; que quer discutir casos reais com especialistas. Sem inventar além da ficha.

**O que depende do site ou da plataforma nova**

1. Botão secundário de WhatsApp e formulário curto de lead ao lado do COMPRAR, com evento de clique e de envio no GA4. [CONFIRMAR ferramenta de medição e CRM]
2. Faixa de números gerada do banco: módulos online e presenciais, duração, turma, início. O banco precisa de um campo de módulos presenciais.
3. Valor total com matrícula calculado pelo site.
4. Cronograma recolhido em blocos (acordeão) no celular, com resumo no topo.
5. Corrigir os erros de digitação do cronograma na loja.
6. Rastreamento de rolagem até CRONOGRAMA, CONSIDERAÇÕES e botão. [CONFIRMAR]

**O que depende da Ufape**

- Regra da 1ª mensalidade para quem entra com o início próximo e data-limite de matrícula.
- Depoimentos e vídeo com autorização registrada, número de turmas já realizadas e se pode usar como prova.
- Texto de certificação aprovado pela regulação.

### As 3 principais correções com teste

**Correção 1: caminho secundário "falar com o time" ao lado do COMPRAR (problema 1)**
- O que muda: botão de WhatsApp e/ou formulário curto, texto do item 4 acima.
- Hipótese [SUPOSIÇÃO]: se o visitante que ainda não decidiu tiver um segundo passo de baixo compromisso, mais visitantes viram conversas com o time, porque o investimento é alto e a objeção mais provável é de valor e de rotina.
- Teste: A/B com 50% do tráfego da página-modelo em cada versão, ou antes e depois se o tráfego for pequeno. Métrica primária: conversas iniciadas por visitante único. Métrica de proteção: cliques em COMPRAR e matrículas por visitante. Qualidade: matrículas por conversa [CONFIRMAR CRM].
- Viabilidade: a 707 fecha em 4 dias, então não há tempo de teste nela. Usar a página da próxima pós de maior ticket (por exemplo, a de março de 2027) e aplicar na 707 só com aprovação humana e sem teste.
- Linha de base: [CONFIRMAR]. Tamanho de amostra e duração: [CONFIRMAR] com o desenho-de-experimentos.

**Correção 2: responder as objeções antes do cronograma, com resumo de rotina e política da turma (problema 2)**
- O que muda: faixa de números (módulos online e presenciais, duração), bloco "Como a turma é confirmada" e as perguntas do FAQ.
- Hipótese [SUPOSIÇÃO]: se as objeções de tempo, viagem e turma mínima aparecerem antes do cronograma, mais visitantes chegam ao botão, porque hoje essas respostas ficam abaixo de um cronograma de 24 módulos.
- Teste: A/B ou antes e depois. Métrica primária: cliques em COMPRAR e no caminho secundário por visitante. Métrica de apoio: profundidade de rolagem e tempo até o primeiro clique. Proteção: perguntas repetidas no WhatsApp sobre viagem e turma (contagem manual por semana). [CONFIRMAR dados]

**Correção 3: regra de entrada com início próximo (problema 3) e urgência real (problema 5)**
- O que muda: a Ufape define o que vale para a 1ª mensalidade e a data-limite. A squad escreve uma frase simples: "Matrículas abertas até [CONFIRMAR data-limite]. O primeiro módulo é em [início do banco]." Sem "últimas vagas", porque não há número de vagas restantes.
- Hipótese [SUPOSIÇÃO]: se a condição de entrada for explícita, menos candidatos desistem por dúvida sobre o pagamento antecipado, porque a regra atual parece impossível de cumprir com o início próximo.
- Teste: sem A/B (janela curta). Antes e depois, comparando conversas e matrículas das duas últimas semanas com as anteriores. Métrica: matrículas e perguntas sobre a regra. [CONFIRMAR dados]. Replicar no desenho das pós de março, onde dá para testar.

### Comparação com templates/pagina-da-turma.md (Pós)

| Seção do template | Na página 707 (texto copiado) |
|---|---|
| hero | Existe, mas sem para quem e sem subtítulo |
| numeros | Existe (início, horas, módulos, modalidade, turma, local); falta resumo de online e presencial |
| sobre | Existe (objetivo) |
| para_quem | Só no fim (PÚBLICO-ALVO), uma linha |
| diferenciais | Existe, forte |
| matriz | Existe (cronograma), sem recolhimento |
| docentes | Existe (nomes e titulação; sem bio no texto) |
| certificacao | Cabeçalho "CERTIFICAÇÃO DO MEC" (ver conformidade) |
| video | Ausente |
| depoimentos | Ausente |
| investimento | Existe, sem frase de apoio e sem total com matrícula |
| local_e_datas | Existe |
| parceiros | Cabeçalho sem conteúdo no texto copiado |
| faq | Ausente |
| formulario | Ausente (só COMPRAR) |
| cta_final | Ausente |

### Conformidade (lista, não reescrita)

- Cabeçalho "CERTIFICAÇÃO DO MEC" e "Documentos para matrícula (MEC e UFAPE)". A ficha traz "Alertas: nenhum"; o alerta de certificação não foi registrado nesta ficha. Nota para o cmo. Frase de certificação ligada ao MEC: não repetir; texto aprovado [PREENCHER COM A REGULAÇÃO].
- "referências nacionais e internacionais", "altamente qualificado" e "infraestrutura completa e moderna": superlativos sem fonte na página. Exigem fonte verificável (auditoria de conformidade, item de superlativos).
- Regra da 1ª mensalidade versus início próximo: condição de pagamento sem explicação para quem entra tarde (CDC, clareza de condições).
- Política de reembolso e de força maior: está na página; manter, e revisar com a regulação se o texto atende às regras da instituição.
- Qualquer "últimas vagas" ou contagem regressiva: só com número real de vagas, que não existe hoje. Não usar.
- Depoimentos, fotos e vídeos de docentes: só com autorização registrada [CONFIRMAR autorização].
- Formulário e checkout: o texto copiado não mostra finalidade de uso dos dados nem link para política de privacidade. [CONFIRMAR no site]
- Página de destino de anúncio: a ficha mostra início e preço coerentes com o catálogo. A frase ligada ao MEC fica sinalizada no item "página de destino" (pedido A7 do plano do cmo).

---

## Página 2: Pós com turma aberta, 68610 Pós-graduação em Dermatologia Veterinária (modelo de pós de ticket médio, com link para prova de bolsa)

**Dados conferidos no catálogo (seção 2):** São Paulo, semipresencial, turma V, início 28/11/2026 (planilha e site), 500 h, 24 módulos, 30x de R$ 1.000,00, total de R$ 30.000,00, matrícula de R$ 250,00, status aberto. Faltam 33 dias (conta a partir de 26/10/2026). Está na onda 1, com campanha ativa. Existe prova de bolsa de Dermatologia (68646) em 27/11/2026, um dia antes do início.

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | Título e bloco de números claros (E) | Passa |
| Para quem? | O primeiro parágrafo é uma afirmação geral ("A pele é o maior órgão do corpo..."). "Médicos Veterinários" só em PÚBLICO-ALVO, no fim (E) | Falha [SUPOSIÇÃO: para quem não conhece a especialidade, o topo não diz o que ele vai conseguir fazer] |
| Qual modalidade? | SEMIPRESENCIAL no bloco de números (E) | Passa em parte |
| O que fazer agora? | COMPRAR; mais abaixo, "Tem interesse em prestar a prova de bolsa? Clique aqui" (E) | Passa em parte |

### O que já funciona (E)

- Preço completo e coerente. 30 x R$ 1.000,00 dá R$ 30.000,00 (confere).
- Existe caminho para a prova de bolsa dentro da página. Para um ticket de R$ 30.000,00, é a resposta natural à objeção de valor. As outras duas páginas de pós não têm isso no texto.
- Cronograma com 24 módulos, marcação online e presencial, e tópicos bem específicos (dermatoscopia, microagulhamento, otoscopia, fotobiomodulação), que mostram conteúdo concreto.
- Avaliação, documentos de matrícula e política de turma mínima e de reembolso estão informadas.
- A ficha marca o alerta de certificação corretamente.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | O link da prova de bolsa é um "Clique aqui" sem data, valor, bolsas previstas nem turma. E a prova (27/11) acontece um dia antes do início da turma (28/11), com matrícula em até 10 dias úteis depois do resultado (regra da página da prova de Anestesiologia, 68639, que serve de modelo). A página não diz a qual turma a bolsa se aplica. | Preço, bolsa e condições | E (datas); H (efeito: o caminho que deveria baixar a objeção de valor fica confuso) [SUPOSIÇÃO]. Destino da prova: [CONFIRMAR] | Alto | UFAPE (turma de destino) e SITE (link e bloco) |
| 2 | Só COMPRAR para R$ 30.000,00, sem "falar com o time" no texto copiado. | Chamada para ação | E (ausência); H (efeito) [SUPOSIÇÃO] | Alto | SITE e SQUAD |
| 3 | Topo sem para quem e sem resultado esperado. O objetivo ("capacitar os profissionais a ampliar o raciocínio crítico...") só aparece no 3º parágrafo e se repete quase igual em JUSTIFICATIVA. | Clareza da oferta | E (posição e repetição); H (efeito) | Alto | SQUAD |
| 4 | Coordenação marcada só como "UFAPE" e docentes (18) listados apenas com titulação, sem bio no texto. A página 707 nomeia coordenadores; esta não. | Prova e confiança | E; H (efeito) | Médio a alto | UFAPE e SITE |
| 5 | Primeira mensalidade "com 30 dias de antecedência": para a turma de 28/11, esse prazo cai em 29/10 (conta: 28/11 menos 30 dias), 3 dias depois de hoje. A página não diz o que vale para quem decidir depois disso. | Preço e condições, urgência | E (conta); [CONFIRMAR regra] | Médio a alto | UFAPE |
| 6 | Falta o bloco de HORÁRIOS (a página 707 tem). Falta resumo de rotina: apenas 7 dos 24 módulos são presenciais, e o primeiro presencial é o módulo 5, em março de 2027 (contagem sobre o cronograma). Isso é argumento a favor para quem mora longe e não está dito. | Objeções sem resposta | E (ausência e contagem); H (efeito) | Médio | SITE e SQUAD |
| 7 | Defeitos de texto: "avisados ??com antecedência" (caractere quebrado), "Dermatopatia alergica II", "Módulo 15 -" quebrado, bloco CONSIDERAÇÕES repetido duas vezes, PARCEIROS E PATROCINADORES sem conteúdo no texto copiado. | Confiança | E; H (efeito) | Médio | UFAPE |
| 8 | Sem depoimento, sem vídeo, sem uso da tradição ("Turma V"). | Prova | E (ausência); H | Médio | UFAPE |
| 9 | Sem FAQ, sem formulário de lead, sem CTA final. | Chamada para ação | E | Médio | SITE e SQUAD |

### Correções por prioridade

**O que a squad escreve**

1. Hero. Título: "Pós-graduação em Dermatologia Veterinária". Subtítulo (até 160 caracteres): "Diagnóstico e tratamento das principais dermatopatias de cães e gatos, com teoria online ao vivo e gravada e prática presencial, para médicos veterinários." Os fatos vêm da ficha (descrição, modalidade, público). Motivo: coloca para quem e resultado no topo e tira o texto genérico do primeiro parágrafo.
2. Bloco da prova de bolsa, logo abaixo do investimento. Título: "Quer tentar uma bolsa antes de decidir?" Texto: "Veja na página da prova de bolsa a data, as regras e as bolsas previstas para esta especialidade. A prova é feita antes da matrícula e o resultado define se você segue com bolsa. [CONFIRMAR a turma em que a bolsa vale]". Botão: "Ver a prova de bolsa de Dermatologia". Sem percentual (o percentual desta prova não foi lido; [CONFIRMAR NO CATÁLOGO]).
3. Frase de apoio do investimento e botão secundário, no mesmo formato da 707 (item 3 e 4 da página 1).
4. FAQ: "Preciso ir a São Paulo todo mês?" (resposta com número do banco), "A prova de bolsa vale para esta turma?" ([CONFIRMAR]), "O que acontece se a turma não fechar?", "Posso entrar depois da primeira mensalidade?" ([CONFIRMAR]).
5. Para quem: médico veterinário que atende dermatopatias na rotina e quer método de diagnóstico; que quer dominar exames como citologia e dermatoscopia; que quer discutir casos clínicos. Só com base na ficha.
6. Remover do texto da IA qualquer frase de certificação. A seção de certificação fica oculta até haver texto aprovado.

**Site ou plataforma nova**

1. Bloco de bolsa ligado à prova certa (68646) e à turma de destino, mostrando data, valor da inscrição e bolsas previstas vindos do banco.
2. Faixa de números: módulos presenciais e online e mês do primeiro presencial (do banco).
3. WhatsApp e formulário de lead; remover o bloco CONSIDERAÇÕES duplicado; corrigir o caractere quebrado e a grafia.
4. Coordenação e docentes com bio curta da ficha, onde existir. [CONFIRMAR autorização]
5. Eventos de clique no link da prova, no COMPRAR e no WhatsApp. [CONFIRMAR ferramenta]

**Ufape**

- Qual turma recebe os aprovados da prova de 27/11 (a de 28/11 ou a seguinte) e como funciona a matrícula de quem passa depois do início.
- Regra da 1ª mensalidade perto do início.
- Coordenador nomeado, docentes e material de prova social autorizados.

### As 3 principais correções com teste

**Correção 1: bloco de prova de bolsa claro, ligado à turma de destino (problema 1)**
- O que muda: bloco de texto e botão do item 2, mais o bloco dinâmico do site.
- Hipótese [SUPOSIÇÃO]: se a prova de bolsa aparecer como alternativa visível, com data e destino, mais visitantes sensíveis a preço entram na prova em vez de sair da página, porque hoje o caminho é um "Clique aqui" sem informação.
- Teste: A/B (link atual versus bloco novo). Métrica primária: cliques para a página da prova por visitante e inscrições na prova (R$ 100,00) por visitante. Métrica de proteção: cliques em COMPRAR e matrículas diretas (para ver se a prova canibaliza a compra). Métrica de longo prazo: matrículas vindas da prova. [CONFIRMAR dados e CRM]
- Viabilidade: a prova é em 32 dias e a turma em 33; só dá para medir inscrições na prova até o dia 27/11. Janela curta, [CONFIRMAR tráfego].

**Correção 2: topo com para quem e resultado, mais caminho "falar com o time" (problemas 2 e 3)**
- O que muda: hero do item 1, botão secundário e frase de apoio.
- Hipótese [SUPOSIÇÃO]: se o topo disser para quem é e o que o aluno consegue fazer, e houver um segundo passo de baixo compromisso, mais visitantes avançam, porque hoje a oferta só fica clara no 3º parágrafo.
- Teste: A/B de hero (versão atual versus nova) com o botão secundário nas duas versões, para isolar o efeito do texto. Métrica primária: cliques em COMPRAR, WhatsApp ou prova de bolsa por visitante. Métrica de apoio: rolagem até o cronograma. [CONFIRMAR tráfego]

**Correção 3: rotina e custo de viagem no topo, e condição de entrada perto do início (problemas 5 e 6)**
- O que muda: faixa de números com módulos presenciais e online, FAQ sobre viagem e frase de data-limite (depende da Ufape).
- Hipótese [SUPOSIÇÃO]: se a página mostrar que são poucos os módulos presenciais e quando o primeiro acontece, a objeção de tempo e deslocamento diminui.
- Teste: antes e depois nas pós de março de 2027, onde há tempo de medir. Métrica: perguntas sobre viagem no WhatsApp (contagem por semana) e conversão do visitante em conversa. [CONFIRMAR dados]

### Comparação com templates/pagina-da-turma.md (Pós)

| Seção do template | Na página 68610 |
|---|---|
| hero | Existe, sem subtítulo de resultado |
| numeros | Existe |
| sobre | Existe (3 parágrafos, repetidos em JUSTIFICATIVA) |
| para_quem | Só no fim |
| diferenciais | Ausente (a 707 tem) |
| matriz | Existe |
| docentes | Existe, coordenação genérica |
| certificacao | Frase "reconhecida pelo MEC" e cabeçalho "CERTIFICADO PELO MEC" (ver conformidade) |
| video, depoimentos | Ausentes |
| investimento | Existe |
| local_e_datas | Existe; falta bloco de horários |
| parceiros | Cabeçalho sem conteúdo |
| faq | Ausente |
| formulario | Ausente; existe o link da prova de bolsa |
| cta_final | Ausente |

### Conformidade (lista, não reescrita)

- "A Pós-graduação em Dermatologia Veterinária é reconhecida pelo Ministério da Educação (MEC)" e o cabeçalho "CERTIFICADO PELO MEC". Proibido repetir; o texto aprovado é [PREENCHER COM A REGULAÇÃO]. Item P2 do plano do cmo.
- Anúncio que leve a esta página deve ser sinalizado no item "página de destino" da conformidade.
- Bolsa: regra, público elegível e prazo de validade precisam estar claros. O link atual não traz nenhum dos três.
- Regra da 1ª mensalidade (prazo de 29/10 pela conta acima): condição de pagamento a esclarecer.
- Docentes e fotos: só com autorização registrada.
- Formulário e checkout: finalidade dos dados e política de privacidade [CONFIRMAR no site].

---

## Página 3: Prova de bolsa, 68639 Prova de Bolsa de Estudos para Anestesiologia Veterinária (São Paulo)

**Dados conferidos no catálogo (seção 3) e na ficha:** São Paulo, 27/11/2026, status aberto; inscrição (ficha) de R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão. Faltam 32 dias. A ficha traz horário (9 às 13h), prova presencial, nota de corte, prazos, composição, local e bolsas previstas. A campanha das 22 provas é única (decisão 3 do briefing), com variação por especialidade. Não existe tipo "prova de bolsa" no template da página da turma.

### Teste dos 5 segundos (no celular, inferido pela ordem do texto)

| Pergunta | Resposta pelo texto copiado | Resultado |
|---|---|---|
| Que curso é este? | "Prova de Bolsa de Estudos para Anestesiologia Veterinária" (E) | Passa |
| Para quem? | Não há público nem requisito (por exemplo, médico veterinário formado). A página não diz para qual pós a bolsa vale (E) | Falha |
| Qual modalidade? | "PROVA PRESENCIAL", São Paulo, 9 às 13h, 27 de novembro de 2026 (E) | Passa |
| O que fazer agora? | Botão COMPRAR, o mesmo rótulo de um produto, para uma inscrição (E) | Passa em parte [SUPOSIÇÃO: rótulo "Inscrever-me na prova" é mais claro] |

### O que já funciona (E)

- Regras do dia muito claras: data, horário, local, documento, proibição de celular e relógio, nota de corte (7,0, equivalente a 70% de acerto), prazo de recurso e prazo de matrícula depois do resultado.
- Tabela de bolsas previstas: 2 bolsas de 50% (monitoria), 4 de 25% e 5 de 10% (11 no total, conta). Isso é concreto e raro. Correção do QA de 26/10: contexto/pos-graduacao.md e a pendência P10 do plano já registram esses percentuais (iguais nas 22 provas), e a peça pode citá-los como estão lá.
- Critério de desempate declarado (análise de currículo) e canal do resultado (WhatsApp e/ou e-mail).
- Ticket baixo (R$ 100,00), que reduz o atrito de decisão.

### O que impede o visitante de comprar ou falar com o time (ordenado pelo impacto provável)

| # | Problema | Categoria | Tipo | Impacto | Quem resolve |
|---|---|---|---|---|---|
| 1 | A página não diz para qual pós a bolsa vale, nem mostra o valor da mensalidade. Quem lê "25%" não sabe o que isso representa em reais. Em Anestesiologia há mais de uma turma aberta no catálogo (657, 68609 e 359) e uma já iniciada (68607). Qual é a de destino é [CONFIRMAR]. | Preço, bolsa e condições | E (ausência); H (efeito alto, pois é a pergunta que decide a inscrição) [SUPOSIÇÃO] | Alto | UFAPE (destino) e SITE (bloco com a pós e o valor) |
| 2 | Regra de distribuição incompleta: quem passa na nota de corte mas fica sem bolsa, pode se matricular sem bolsa? Como são ordenadas as 11 bolsas? Em que consiste a "monitoria" da bolsa de 50%? | Objeções sem resposta | E (ausência); H | Alto | UFAPE e SQUAD |
| 3 | A página não diz o que a prova cobra: sem temas, sem material de estudo, sem exemplo. Só "múltipla escolha e dissertativas". | Informação que falta | E (ausência); H (insegurança de quem teme reprovar) | Médio a alto | UFAPE e SQUAD |
| 4 | Sem prazo para se inscrever na prova (até que dia o botão funciona?) e sem política para ausência ou desistência dos R$ 100,00. | Preço e condições, urgência | E (ausência) [CONFIRMAR] | Médio | UFAPE |
| 5 | Divergência de número mínimo: esta página diz "Número mínimo de alunos para a confirmação da turma: 15". As páginas das turmas dizem 20 (contexto da linha e fichas 707 e 68610). | Confiança | E | Médio | UFAPE (qual número vale e para qual turma) |
| 6 | Para quem vem de fora: prova presencial só em São Paulo, resultado "via telefone" sem data prevista, prazo de 10 dias úteis para matricular. A página não traz data do resultado. | Objeções (deslocamento) | E (ausência); [CONFIRMAR] | Médio | UFAPE |
| 7 | Erros e repetição: "intrasferível", regras de celular e documento repetidas duas vezes (no corpo e em CONSIDERAÇÕES), "Valor" como rótulo de uma inscrição. | Confiança | E | Baixo a médio | UFAPE |
| 8 | Urgência real não explorada: a data (27/11) e as bolsas previstas (11) são fatos da página, mas não aparecem como motivo para agir. Não existe contagem de inscritos nem vagas restantes. | Urgência | E; H | Médio | SQUAD e UFAPE |

### Correções por prioridade

**O que a squad escreve**

1. Bloco "Como funciona a prova de bolsa" no topo, em passos curtos: "1. Inscreva-se. 2. Faça a prova presencial no dia indicado nesta página. 3. Receba o resultado pelos canais informados. 4. Se for aprovado, matricule-se dentro do prazo desta página." Os números ficam nos campos de dado da página (data, prazo), não no texto, para seguir a regra da plataforma.
2. FAQ de bolsa (perguntas escritas pela squad, respostas só depois da confirmação da Ufape): "Para qual turma a bolsa vale?", "O que acontece se eu passar e não receber bolsa?", "O que é a bolsa de monitoria?", "Como as bolsas são distribuídas?", "O que cai na prova?", "Posso fazer a prova e me matricular numa turma de outra cidade?", "E se eu não puder comparecer?". Cada resposta fica [CONFIRMAR] até a Ufape responder.
3. Texto do botão e frase de apoio: botão "Inscrever-me na prova de bolsa", frase "Inscrição na prova. O valor e as formas de pagamento estão ao lado. [CONFIRMAR prazo de inscrição]".
4. Frase de apoio de urgência com fato: "A prova acontece na data indicada nesta página. As bolsas previstas estão na tabela abaixo." Só fatos, sem "últimas vagas".
5. Orientação para quem vem de outra cidade: "A prova é presencial. Se você mora fora, planeje a viagem com antecedência e só reserve passagem depois de se inscrever. [CONFIRMAR se há opção em outra data ou local]".

**Site ou plataforma nova**

1. Bloco dinâmico "O que esta bolsa vale": pós de destino (link para a turma), mensalidade do banco e valor da mensalidade com 50%, 25% e 10% de desconto, calculado pelo site. Depende do cadastro do destino de cada prova.
2. Criar o tipo "prova_de_bolsa" no template (hoje não existe; seção nova só entra com versão nova do template, decisão P72) e um tipo "grupo_de_estudos".
3. Eventos de inscrição na prova e de clique no link da pós de destino. [CONFIRMAR ferramenta]
4. Rótulo do botão trocado de COMPRAR para o texto do item 3.
5. Lembrete automático por WhatsApp e e-mail para quem se inscreveu (véspera e dia) pelo CRM, só com consentimento. A squad escreve o texto; o CRM envia.

**Ufape**

- Pós de destino de cada prova, regra de distribuição das bolsas, o que a monitoria exige, conteúdo da prova, prazo de inscrição, política de ausência, número mínimo correto (15 ou 20), data do resultado.

### As 3 principais correções com teste

**Correção 1: bloco "O que esta bolsa vale" com a pós de destino e o valor da mensalidade (problema 1)**
- O que muda: bloco dinâmico do site, depende do destino cadastrado.
- Hipótese [SUPOSIÇÃO]: se o candidato enxergar a economia em reais na pós de destino, mais visitantes se inscrevem na prova, porque hoje a página não mostra o valor da bolsa.
- Teste: antes e depois, como as 22 provas são uma campanha única; ou A/B por especialidade (algumas provas com o bloco, outras sem) se houver tráfego suficiente. Métrica primária: inscrições na prova por visitante da página. Proteção: matrículas por inscrito na prova. [CONFIRMAR dados]

**Correção 2: FAQ e regras completas de bolsa (problemas 2, 3 e 5)**
- O que muda: respostas da Ufape às perguntas do item 2 e correção do número mínimo.
- Hipótese [SUPOSIÇÃO]: se as dúvidas sobre o que acontece depois da prova forem respondidas, menos inscritos faltam à prova e mais aprovados se matriculam, porque hoje o aprovado sem bolsa não sabe o que fazer.
- Teste: antes e depois. Métricas: comparecimento à prova (inscritos contra presentes) e matrículas por aprovado, e perguntas repetidas ao WhatsApp. [CONFIRMAR dados; a Ufape precisa registrar presença e matrícula por prova]

**Correção 3: "Como funciona" no topo, rótulo do botão e prazo de inscrição (problemas 4 e 8)**
- O que muda: bloco de passos, botão "Inscrever-me na prova de bolsa" e, se existir, o prazo de inscrição.
- Hipótese [SUPOSIÇÃO]: se o rótulo e o passo seguinte forem claros, mais visitantes concluem a inscrição de R$ 100,00, porque hoje o botão fala em comprar.
- Teste: A/B simples do rótulo do botão e do bloco de passos. Métrica primária: cliques no botão e inscrições concluídas por visitante. Proteção: taxa de abandono no checkout. [CONFIRMAR tráfego e checkout]

### Comparação com templates/pagina-da-turma.md

- Não existe tipo "prova_de_bolsa" nas seções do template (tipos: pos, livre, workshop, simposio). A página, como está, tem: dados, regras, composição, local e tabela de bolsas. Faltam hero com resultado, para quem, FAQ, formulário de lead e CTA final do template comum.
- Recomendação ao cmo: criar o tipo com as chaves sugeridas "como_funciona", "bolsas_previstas" (dado), "regras" (dado), "faq_bolsa" e "turma_de_destino" (dado). Como seção nova só entra em versão nova do template, o pedido vai ao cmo.

### Conformidade (lista, não reescrita)

- Bolsa: regra, público elegível e prazo de validade precisam estar claros. Falta o prazo de validade da bolsa e a turma elegível.
- Percentuais de bolsa: estão na ficha e, desde 26/10, em contexto/pos-graduacao.md (P10 resolvida); a peça pode usá-los como estão no contexto. [CONFIRMAR NO CATÁLOGO]
- Número mínimo de alunos: 15 nesta página contra 20 nas turmas.
- Texto "a bolsa de estudo não é acumulativa e é intrasferível": manter, corrigir a grafia no site.
- Urgência: "últimas bolsas" ou contagem só com número real de bolsas restantes, que não existe.
- Prova em dia útil e presencial: a peça de anúncio não pode prometer aprovação ou bolsa garantida.
- Dados pessoais de inscritos (resultado por telefone): tratamento no CRM, nunca em análise da squad.

---

## Síntese: padrões que se repetem nas três páginas

1. **Um só caminho de ação, COMPRAR, mesmo no ticket mais alto (E).** Nenhuma das três mostra no texto copiado um segundo passo (WhatsApp, formulário, receber o programa). O template prevê "formulario" como seção obrigatória; as páginas atuais não têm. Hipótese [SUPOSIÇÃO]: o candidato de pós conversa antes de pagar; confirmar com o histórico do WhatsApp de vendas.
2. **Objeções críticas no fim da página (E).** Turma mínima, reembolso, viagem e passagens estão em CONSIDERAÇÕES, depois de um cronograma de 24 módulos. As respostas existem; falta posição e resumo.
3. **Falta "para quem" e "o que você consegue fazer" no topo (E).** Em 707 e 68610 o público só aparece perto do fim. Em 68639 não aparece.
4. **Pouca prova social e pouco uso de autoridade (E).** Sem depoimento, vídeo, número de turmas ou parceiros visíveis no texto copiado. Docentes só por nome e titulação.
5. **Regra da 1ª mensalidade com 30 dias de antecedência (E)** não combina com início próximo. A 707 já passou do prazo; a 68610 passa em 29/10.
6. **Prova de bolsa pouco ligada à turma (E).** A 68610 manda para a prova com um "Clique aqui"; a prova não diz para qual pós vale; e as datas (27/11 e 28/11) são coladas. Resolve-se com um bloco ligado pelo banco.
7. **Erros de digitação e duplicações (E)** em todas, que enfraquecem a confiança de quem avalia um investimento alto [SUPOSIÇÃO].
8. **Frase de certificação ligada ao MEC (E)** em 707 e 68610. Vai para a lista de conformidade.
9. **Urgência real subutilizada (E/H).** Há datas reais (início, prova, bolsas previstas). Não há número de vagas restantes; sem ele, nenhuma peça usa "últimas vagas".
10. **Mapa para o template.** Seções que faltam em todas: faq, formulario, cta_final, depoimentos e video. O tipo "prova de bolsa" não existe no template.

### Ordem sugerida de trabalho (para o cmo e o backlog-de-otimizacao)

1. Decisões da Ufape que destravam a conversão: turma de destino de cada prova, regra da 1ª mensalidade, regras de distribuição das bolsas, número mínimo (15 ou 20).
2. Mudanças de site de baixo custo: caminho secundário de WhatsApp e formulário, rótulo do botão da prova, correção de erros, bloco de bolsa ligado à turma.
3. Texto da squad: hero, FAQ, blocos de confirmação da turma e de passos da prova (itens deste documento), na ordem das ondas.
4. Mapear eventos no GA4 (clique em COMPRAR, WhatsApp, prova, formulário) antes de qualquer teste. [CONFIRMAR ferramenta]

### Próximo agente sugerido

desenho-de-experimentos, para transformar as três correções de cada página em testes com amostra e duração, assim que houver dado de tráfego. Depois, backlog-de-otimizacao (etapa 1.33) e qa-de-marketing.

---

## Fatos (com fonte)

- 707: início 30/10/2026, turma VII, 600 h, 24 módulos, 30x de R$ 1.590,00, total de R$ 47.700,00, matrícula de R$ 250,00, status aberto. Fonte: catálogo, seção 2, e ficha 707.
- 707: 10 módulos presenciais e 14 online, contados no cronograma da ficha 707 (módulos 11 e 22 com rótulo misto). Fonte: ficha 707.
- 707: política de turma mínima de 20, reembolso só se a turma não for confirmada, aulas presenciais não gravadas. Fonte: ficha 707.
- 68610: início 28/11/2026, turma V, 500 h, 24 módulos, 30x de R$ 1.000,00, total de R$ 30.000,00, matrícula de R$ 250,00, coordenação registrada como "UFAPE", 7 módulos presenciais e 17 online (contagem), primeiro presencial no módulo 5 (20 e 21 de março de 2027). Fonte: catálogo e ficha 68610.
- 68610: contém a frase "reconhecida pelo Ministério da Educação (MEC)" e o cabeçalho "CERTIFICADO PELO MEC". Fonte: ficha 68610.
- 68610: contém o link "Tem interesse em prestar a prova de bolsa? Clique aqui". Fonte: ficha 68610.
- 68639: prova em 27/11/2026, 9 às 13h, presencial, São Paulo, R$ 100,00, nota de corte 7,0 (70%), prazo de matrícula de 10 dias úteis, recurso em 2 dias úteis, número mínimo 15, 2 bolsas de 50% (monitoria), 4 de 25% e 5 de 10%. Fonte: ficha 68639 e catálogo, seção 3 (data, preço e status).
- Faltam 4 dias para 30/10, 33 para 28/11 e 32 para 27/11 (conta a partir de 26/10/2026). 30 dias antes de 28/11 é 29/10.
- 47.700 mais 250 é igual a 47.950 (conta). 2 mais 4 mais 5 é igual a 11 bolsas (conta).
- O template pagina-da-turma.md só tem os tipos pos, livre, workshop e simposio, e obriga a seção "formulario". Fonte: templates/pagina-da-turma.md.
- A frase ligada ao MEC está em 46 páginas do site. Fonte: plano do cmo, pendência P2.
- Percentuais de bolsa constam na ficha 68639 e em contexto/pos-graduacao.md (2 de 50%, 4 de 25%, 5 de 10%, iguais nas 22 provas). Fonte: ficha 68639, contexto/pos-graduacao.md.

## Suposições

- [SUPOSIÇÃO] A maior parte dos candidatos chega pelo celular. Confirmar no GA4.
- [SUPOSIÇÃO] A primeira tela do celular mostra título, preço e COMPRAR, como a ordem do texto sugere.
- [SUPOSIÇÃO] O candidato de pós conversa com o time antes de pagar um ticket desse tamanho; sem segundo caminho na página, parte dos visitantes sai.
- [SUPOSIÇÃO] Respostas às objeções antes do cronograma aumentam o avanço até o botão.
- [SUPOSIÇÃO] A prova de bolsa mais clara aumenta inscrições e matrículas, e o valor em reais da bolsa é o que decide o candidato sensível a preço.
- [SUPOSIÇÃO] Erros de digitação e blocos vazios reduzem confiança em quem avalia um investimento alto.
- [SUPOSIÇÃO] O rótulo "Inscrever-me na prova de bolsa" converte melhor que COMPRAR.
- [SUPOSIÇÃO] Vir de outra cidade para a prova pesa na decisão.
- A prova de bolsa de Dermatologia (68646) segue as mesmas regras da 68639: contexto/pos-graduacao.md registra que as regras são iguais nas 22 provas.

## Dados que faltam

- [CONFIRMAR] Tráfego, taxa de conversão por página, origem (celular e computador), eventos no GA4, gravações e mapas de calor.
- [CONFIRMAR] Se o site tem WhatsApp fixo, formulário de lead, depoimentos em imagem, vídeo, logos de parceiros e política de privacidade no checkout (o texto copiado não mostra).
- [CONFIRMAR] Regra da 1ª mensalidade para quem entra perto do início e data-limite de matrícula de 707 e 68610.
- [CONFIRMAR] Turma de destino de cada prova de bolsa e se a bolsa vale para a turma que começa um dia depois da prova.
- [CONFIRMAR] Distribuição das bolsas, o que a monitoria exige, conteúdo da prova, prazo de inscrição, política de ausência e data do resultado.
- [CONFIRMAR] Número mínimo da turma (15 na página da prova, 20 nas páginas de curso).
- [CONFIRMAR] Duração do curso em anos, para o campo do banco.
- [CONFIRMAR] Texto de certificação aprovado pela regulação.
- [CONFIRMAR autorização] Depoimentos, vídeo e imagem de docentes.
- [CONFIRMAR] Se os mutirões de Oftalmologia acontecem na Ufape Clínica.
- [CONFIRMAR] Quem aprova páginas e preços, metas de conversão e verba.
