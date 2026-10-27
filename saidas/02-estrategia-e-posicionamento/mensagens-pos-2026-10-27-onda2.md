# Mensagens das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), encomenda F2 da onda 2

- **Agente:** mensagens (departamento 02, Estratégia e Posicionamento)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1 (já com os ajustes C1, C2, C7 e C14 do plano da onda 2 em versão 2, ver "Ajustes antes da entrega")
- **Encomenda:** F2 do plano do CMO (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md, seção 10): mensagem central e respostas às objeções por turma, sem número, para a página da turma; 68615 (laboratório clínico) diferenciada de 333 (leitura de lâminas) sem comparação de valor. O plano previa o nome mensagens-pos-2026-11-10.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Consumidores:** landing-page (F3, blocos `hero`, `sobre`, `para_quem`, `faq`, `investimento` e `cta_final`), seo-on-page (F4, `resposta_citavel`), otimizador-de-cta (F5), copy-de-mensagens (F7, respostas do time), posts-sociais (F8) e tiktok (F9).
- **Status:** rascunho para o qa-de-marketing (auditorias/02-estrategia-e-posicionamento.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago a partir deste arquivo.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 14, 16 e 18)
  - contexto/ufape-geral.md (voz da marca: técnica, próxima, confiante; de colega para colega)
  - contexto/pos-graduacao.md
  - contexto/catalogo-de-cursos.md (seção 2, linhas de 657, 341, 289, 68615 e 333)
  - Fichas inteiras: contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md, 341-pos-graduacao-em-medicina-interna-equina.md, 289-pos-graduacao-em-cardiologia-veterinaria.md, 68615-pos-graduacao-em-patologia-clinica.md, 333-pos-graduacao-em-citopatologia-veterinaria.md
  - templates/pagina-da-turma.md (regras do texto da IA; tipo pos)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (lido na versão 1, inteiro; pesam as seções 1, 2, 4, 8 e 10, linha F2 e linha F3)
  - saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (v2: regras da seção 0, base da seção 1, A1, A2, A11 e A14 (15.4))
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md (F1, inteiro: palavra principal, perguntas para IA, seção 4 de divisão 68615 x 333, CP1)
  - Correções C1, C2, C7 e C14 da versão 2 do plano, recebidas do orquestrador durante a rodada (origem: saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2.md, que este agente não abriu)
- **Não aberto:** templates/casa-de-mensagens.md (o formato desta entrega foi fixado pela encomenda); a versão 2 do plano e o arquivo do qa citados acima; faculdade.ufape.com.br; nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum docente é nomeado no texto para a página (regra do template).
- **Marcadores:** [SUPOSIÇÃO] é hipótese ou escolha deste agente, com a origem. [CONFIRMAR] é dado que só a Ufape tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo e a ficha não trazem.

---

## 0. Regras desta entrega

1. **Texto para a página sem número.** Nenhum algarismo, número por extenso, ordinal, numeral romano, preço, parcela, data, vaga, carga horária, duração, local (cidade, bairro, endereço, hospital) nem nome de docente nos blocos marcados "Texto para a página". Esses fatos vêm como dado do catálogo (`numeros`, `investimento`, `local_e_datas`, `docentes`, `matriz`, `objetivos`). As notas internas de cada seção podem citar código, módulo, ID da F1 e pendência, e não vão para a página.
2. **Fonte.** Toda prova sai da ficha da turma (cronograma, apresentação, público-alvo, observações). O que a ficha não traz vira [CONFIRMAR].
3. **Proibido no texto:** "MEC", "certificado", "certificação", "reconhecido" e variações, prova ou título de especialista, superlativo da ficha ("referência nacional", "oportunidade única", "de excelência", "de ponta"), bolsa, prova de bolsa, desconto, promoção, urgência ("últimas vagas", "corra", "só até", contador), promessa de emprego, renda ou resultado clínico.
4. **Travas por turma:** 657 sem pré-requisito (U10) e sem nada sobre prova ou título de especialista (C14); 341 sem nada que dependa da promoção (OU10, C7) e sem local da prática (OU11); 333 sem "coordenação" (OU12), sem nada sobre entrada depois do início (OU3) e sem tratar todos os módulos presenciais como de leitura de lâminas (C1, C2); entrada até o 3º módulo nunca vira frase de urgência nem texto da IA (OU14: entra só como dado da turma no FAQ).
5. **Nome:** sempre "Pós-graduação em <área>" (341 e 333 aparecem como "Pós Graduação" no catálogo; o texto usa a forma padrão).
6. **Voz:** de colega para colega, frases curtas, termos técnicos corretos (contexto/ufape-geral.md). Não há citação real de candidato: toda fala de objeção está marcada [SUPOSIÇÃO] e deve ser trocada quando chegarem conversas anonimizadas do WhatsApp de vendas.
7. **Sem travessão nem meia-risca.** Conferido na escrita; a busca final é do orquestrador.

**Como cada peça desta casa vira bloco da página (sugestão para a F3, [SUPOSIÇÃO]):** mensagem central serve de base para o `subtitulo` do `hero` (até 160 caracteres) e para a primeira frase de `sobre`; as 3 provas viram o resto de `sobre`; as respostas às objeções viram perguntas do `faq`; a chamada principal serve ao `cta_final`; as variações servem a posts, Stories, roteiros e mensagens (F7 a F9), cada uma em um estágio de consciência.

---

## 1. Respostas comuns às 5 turmas (texto para a página, sem número)

Valem como base do `faq` e da frase de apoio de `investimento` em todas as turmas. Cada seção abaixo traz só as objeções próprias da turma.

| Objeção [SUPOSIÇÃO, contexto da linha] | Texto para a página | Limite |
|---|---|---|
| "É caro. Quanto vou pagar no total?" | "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente." | Sem valor no texto (vem do dado). Nunca "cabe no bolso", "investimento que se paga", "ganhe mais", desconto, promoção ou bolsa. |
| "E se a turma não fechar?" | "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada." | Sem o número mínimo (A12). Frase de reembolso só em 657, 289 e 333, onde a ficha diz que o reembolso dos valores de inscrição é devido se a turma não for confirmada; em 341 o texto da ficha está truncado e contraditório [CONFIRMAR]; em 68615 a ficha não traz o aviso de passagem e hotel, e vale a regra da linha. |
| "Posso entrar depois que a turma começar?" | Nenhum texto da IA. A resposta entra como dado da turma no `faq` (OU14), com a regra completa da decisão 18. Até lá, resposta do time: "A Ufape aceita matrícula até o 3º módulo; eu te explico como ficam os módulos já dados." | Nunca como chamada, título ou frase de prazo. Em 333, bloqueada até OU3: resposta do time "vou confirmar com a secretaria como fica". |
| "Vou ter de largar a rotina?" | "A teoria é online e o presencial fica nos módulos de prática, com as datas publicadas no cronograma antes de começar. Dá para planejar a agenda da clínica com antecedência." | Nunca "flexível", "no seu ritmo", "estude quando quiser". Reposição de módulo perdido [CONFIRMAR OU3]. |

---

## 2. Seção 657: Pós-graduação em Anestesiologia Avançada

**Notas internas (não vão para a página).** Palavra principal (F1): "pós-graduação em anestesiologia avançada veterinária" (657-K0). Pergunta de IA que a mensagem central responde: 657-Q1, sem a parte "para quem" (U10). Termo da ficha que vira entidade: "anestesia de precisão" (657-K6). A palavra "exclusiva" e qualquer recorte de quem pode entrar ficam fora até U10. C14: o convite da ficha para a prova de especialista não entra em texto, chamada, FAQ nem resposta do time; e o item do "Objetivo do Programa" que fala de resultado clínico perioperatório não é repetido aqui: fica só na seção de dado `objetivos`.

### 2.1 Mensagem central (texto para a página)

> Da anestesia de protocolo à anestesia de precisão: fisiologia aplicada, decisão crítica em tempo real e prática presencial guiada nos módulos de técnica avançada.

### 2.2 Três provas de apoio (texto para a página; fonte: ficha de 657)

1. **Prática guiada nos módulos presenciais.** Bloqueios locorregionais com prática guiada e execução avançada; hemodinâmica avançada e ventilação mecânica com manipulação de ventiladores e monitores hemodinâmicos; TIVA e TCI em execução avançada; reanimação cardiorrespiratória com avaliação viscoelástica do coágulo. As aulas práticas não são transmitidas nem gravadas. *(Fonte: cronograma, módulos marcados PRESENCIAL, e observação da ficha.)*
2. **O paciente que o protocolo não resolve.** Hemodinâmica além da pressão arterial, com foco em débito cardíaco e perfusão tecidual; ventilação do paciente especial e proteção pulmonar; bloqueio neuromuscular e ventilação monopulmonar; distúrbios de coagulação e uso racional de hemoderivados; anestesia em cirurgias neurológicas e cardiotorácicas; dor e analgesia em felinos; pets não convencionais. *(Fonte: cronograma.)*
3. **Uma proposta escrita, não um slogan.** O programa foi estruturado para a transição da anestesia de protocolo para a anestesia de precisão, com base em fisiologia aplicada, tomada de decisão crítica e gestão de riscos, para conduzir pacientes de risco moderado a alto e antecipar crises anestésicas. *(Fonte: texto de apresentação e "Objetivo do Programa" da ficha, só os itens de conduta; sem resultado clínico, C14.)*

### 2.3 Respostas às 3 objeções principais (texto para a página)

| Objeção, nas palavras do candidato [SUPOSIÇÃO, H-A1.1 e persona] | Resposta |
|---|---|
| "Anestesia já faz parte da minha rotina. O que eu vou ver aqui que ainda não vi?" | "O curso vai para onde o protocolo não chega: hemodinâmica além da pressão arterial, ventilação do paciente especial, bloqueio neuromuscular, coagulação no transoperatório e anestesia em cirurgias neurológicas e cardiotorácicas. Nos módulos presenciais, a prática é guiada, com ventiladores, monitores e bombas de infusão na mão." |
| "É um dos valores mais altos que vi." (H-A1.4) | "O total, as parcelas e a matrícula estão nesta página, ao lado do cronograma de cada módulo presencial. Você vê o que paga e o que vai praticar antes de decidir." (Sem justificar com adjetivo nem comparar com outra pós.) |
| "Não consigo sair do centro cirúrgico com frequência." | "A teoria é online, em fins de semana com data marcada no cronograma. O presencial fica só nos módulos de prática, também com mês marcado, então dá para montar a escala antes de começar." |

**Fora da página até U10:** "Preciso ser anestesista ou já atuar na área?" (657-Q3). Resposta do time: "Vou confirmar com a secretaria quem pode entrar nesta turma e te retorno." Nenhuma peça diz quem pode entrar. Pergunta sobre prova ou título de especialista também vai para a secretaria, sem texto pronto (C14).

### 2.4 Chamada principal e 3 variações (texto para a página e peças)

- **Chamada principal:** "Veja o cronograma e os módulos de prática guiada antes de decidir."
- **Variação 1 (consciente do problema):** "Paciente de alto risco não cabe no protocolo. Veja como o curso trabalha hemodinâmica, ventilação e coagulação."
- **Variação 2 (consciente da solução):** "Teoria online e prática presencial guiada em bloqueios, hemodinâmica e ventilação mecânica. Confira os módulos."
- **Variação 3 (pronto para decidir):** "Cronograma, quem ensina e condições estão nesta página. Ficou alguma dúvida? Fale com o time."

---

## 3. Seção 341: Pós-graduação em Medicina Interna Equina

**Notas internas.** Palavra principal (F1): "pós-graduação em medicina interna equina" (341-K0); variação de corpo "médico veterinário de equinos" (341-K2, [SUPOSIÇÃO] da F1). Pergunta de IA: 341-Q1 e 341-Q5. Bloqueadas: 341-Q3 (local da prática e formato do módulo 3, OU11). C7: nenhum texto, chamada, resposta ou variação depende da promoção (OU10); a resposta de investimento é a mesma das outras turmas. Fica fora o texto da ficha que chama o recém-formado de "inseguro e sem nenhum diferencial competitivo", que ofende o público, e a frase da ficha sobre "descontos e bolsas de estudo". "Hospital veterinário" não entra no texto enquanto o local da prática estiver em aberto (OU11).

### 3.1 Mensagem central (texto para a página)

> Medicina interna equina sistema por sistema, do paciente crítico ao potro neonato, com teoria online e prática presencial em fins de semana marcados no cronograma.

### 3.2 Três provas de apoio (texto para a página; fonte: ficha de 341)

1. **A espécie inteira, por sistema.** Abordagem clínica do paciente equino e farmacologia; paciente crítico, choque e cuidados intensivos; preparação cirúrgica e manejo de feridas; cardiologia com eletrocardiograma e ecocardiograma; trato respiratório; sistema digestivo; sistema locomotor e diagnóstico de claudicação; neonatologia, UTI neonatal e potros críticos; podologia; odontologia equina; transtornos neurológicos; pele, olhos, sistema urinário e genital. *(Fonte: cronograma.)*
2. **Prática em quase todos os temas.** O curso prevê treinamentos práticos e demonstrativos na maioria dos temas, aulas teóricas online e práticas presenciais aos fins de semana, e termina com estágio obrigatório e atividades complementares. *(Fonte: texto de apresentação, objetivo e cronograma da ficha. Onde é a prática: [CONFIRMAR OU11], fora do texto.)*
3. **Evidência e leitura crítica.** Há um módulo de medicina equina baseada em evidências, os conteúdos teóricos combinam aula online e leitura crítica, e a avaliação inclui provas práticas, seminários e trabalho de conclusão quando escolhido com a coordenação do curso. *(Fonte: cronograma e "Avaliação e metodologia" da ficha.)*

### 3.3 Respostas às 3 objeções principais (texto para a página)

| Objeção [SUPOSIÇÃO, H-A14.1 e texto da ficha sobre pouca prática na graduação] | Resposta |
|---|---|
| "Na faculdade quase não pratiquei com cavalo. Vou dar conta?" | "O curso começa pela abordagem clínica do paciente equino e prevê treinamento prático e demonstrativo na maioria dos temas, do paciente crítico à podologia. A teoria vem antes da prática em cada sistema." |
| "Atendo a campo. Não dá para parar toda hora para viajar." | "A teoria é online. O presencial acontece em fins de semana, com as datas publicadas no cronograma antes de começar. Compre passagem e hotel só depois de a turma ser confirmada." |
| "É caro para quem está começando com equinos." | "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente." (Mesma resposta das outras turmas, sem nenhuma condição além do dado.) |

**Fora da página até a resposta da Ufape:** "Onde são as aulas práticas com os cavalos?" (OU11). Resposta do time: "Vou confirmar com a secretaria onde acontece cada módulo presencial e te retorno." Qualquer pergunta sobre condição de pagamento além do que a página mostra também vai para a secretaria, sem texto pronto.

### 3.4 Chamada principal e 3 variações

- **Chamada principal:** "Veja os sistemas, os módulos práticos e as condições da turma de medicina interna equina."
- **Variação 1 (consciente do problema):** "Claudicação, sistema digestivo, potro crítico: cada caso de equino pede raciocínio clínico por sistema."
- **Variação 2 (consciente da solução):** "Do paciente crítico ao potro neonato, com teoria online e prática presencial em fins de semana com data marcada."
- **Variação 3 (pronto para decidir):** "Cronograma, quem ensina e condições estão nesta página. Fale com o time antes de se matricular."

---

## 4. Seção 289: Pós-graduação em Cardiologia Veterinária

**Notas internas.** Palavra principal (F1): "pós-graduação em cardiologia veterinária" (289-K0); alvo de curto prazo é a cauda de cidade (289-K1), que **não entra no texto da IA** (template e CP1). A diferença real da turma é o campus; sem CP1 aprovada, ela aparece só no dado (`local_e_datas`) e no JSON-LD. Se a CP1 for aprovada, a cidade entra por variável do dado em `titulo_seo` e `resposta_citavel` (seo-on-page, F4), não por texto desta casa. "Ecocardiograma" aparece como conteúdo; "ecocardiografia" como palavra-alvo é da página de 698 (F1, seção 3). Bloco "PROVA DE BOLSA" da ficha: fora (decisão 14).

### 4.1 Mensagem central (texto para a página)

> Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância.

### 4.2 Três provas de apoio (texto para a página; fonte: ficha de 289)

1. **Ecocardiograma na prática.** A maior parte dos módulos presenciais é de prática hands-on de ecocardiograma, e o curso trata a interpretação crítica e a elaboração de laudos ecocardiográficos na rotina. *(Fonte: cronograma, módulos PRESENCIAL e módulo de laudos.)*
2. **Do exame físico à emergência.** Anatomia, fisiologia e semiologia circulatória; farmacologia cardiovascular e insuficiência cardíaca congestiva; radiografia; eletrocardiograma, taquiarritmias e bradiarritmias; ecocardiografia com Doppler e hemodinâmica; cardiopatias adquiridas de cães e de felinos; cardiopatias congênitas; hipertensão arterial sistêmica; síndrome cardiorrenal; cirurgia e intervencionismo; anestesia do paciente cardiopata; emergências cardíacas. *(Fonte: cronograma.)*
3. **Presencial só onde há prática.** Todas as aulas teóricas são acompanhadas a distância; apenas os módulos com aula prática são obrigatoriamente presenciais, e essas aulas não são transmitidas. *(Fonte: texto de apresentação e observação da ficha.)*

### 4.3 Respostas às 3 objeções principais (texto para a página)

| Objeção [SUPOSIÇÃO, persona secundária e H-A2.3] | Resposta |
|---|---|
| "Moro longe. Vou ter de viajar todo mês?" | "Não. A teoria é acompanhada a distância; só os módulos com aula prática são presenciais, e as datas estão no cronograma. Compre passagem e hotel só depois de a turma ser confirmada." |
| "Preciso da cardiologia completa ou só do exame?" | "Aqui o ecocardiograma faz parte de um percurso maior, que vai da fisiologia e do eletrocardiograma às cardiopatias e às emergências. Se o seu objetivo é só o exame, o guia de decisão da área mostra os dois caminhos lado a lado." (Sem dizer qual é melhor; o link vai para o guia A2, que liga a 698.) |
| "Sou clínico geral, não cardiologista. Serve para mim?" (289-Q5) | "O público da turma são médicas e médicos veterinários, e o curso começa pela anatomia, pela fisiologia e pela semiologia circulatória antes de chegar aos exames." Nível de entrada exigido [CONFIRMAR NO CATÁLOGO]. |

### 4.4 Chamada principal e 3 variações

- **Chamada principal:** "Veja o cronograma, do eletrocardiograma ao ecocardiograma na prática."
- **Variação 1 (consciente do problema):** "Fechar o caso cardiológico pede eletrocardiograma, imagem e raciocínio clínico juntos."
- **Variação 2 (consciente da solução):** "Teoria a distância e ecocardiograma hands-on na maior parte dos módulos presenciais."
- **Variação 3 (pronto para decidir):** "Cronograma, quem ensina e condições estão nesta página. O time de vendas tira suas dúvidas." (O telefone de vendas da praça entra como dado ou no formulário, não no texto.)

---

## 5. Diferença entre 68615 e 333 (frase-ponte única)

As duas turmas têm o mesmo segmento (A11) e começam com uma semana de diferença. A regra da F1 (seção 4) é pelo vocabulário: 68615 fica com laboratório clínico e patologia clínica; 333 fica com citopatologia, citologia e leitura de lâminas. A mesma frase vai para o `faq` das duas páginas, para o guia de decisão A11 e para a resposta do time, para que assistentes de IA citem uma resposta só (F1, observação 2 de 68615; perguntas 68615-Q3 e 333-Q3).

**Texto para a página (igual nas duas):**

> "A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes. A Pós-graduação em Citopatologia Veterinária é centrada na leitura de lâminas: células e tecidos ao microscópio, com discussão de casos. A escolha depende do trabalho que você quer fazer na rotina."

- Na página de 68615, o nome "Pós-graduação em Citopatologia Veterinária" é o link para 333; na página de 333, "Pós-graduação em Patologia Clínica" é o link para 68615 (regra de âncora da F1).
- Sem comparação de valor, de duração, de carga, de quantidade de prática ou de corpo docente. Nenhuma das duas é chamada de "mais completa", "mais prática" ou "mais acessível".
- Fica fora: hematologia e hemograma como foco (página de 68608), histopatologia, anatomia patológica e necropsia (nenhuma das duas cobre).

---

## 6. Seção 68615: Pós-graduação em Patologia Clínica (laboratório clínico)

**Notas internas.** Palavra principal (F1): "pós-graduação em patologia clínica veterinária" (68615-K0); o nome do catálogo não traz "veterinária", então a palavra entra no corpo ("laboratório clínico veterinário" na mensagem central). Perguntas de IA: 68615-Q1, Q3, Q4 e Q5. Ficam fora as frases da ficha ligadas ao órgão regulador, "referência nacional em educação" e o bloco "PROVA DE BOLSA". Citologia aparece só como parte do curso, nunca como foco.

### 6.1 Mensagem central (texto para a página)

> O laboratório clínico veterinário do pré-analítico ao laudo: correlação clínico-laboratorial, prática presencial e como estruturar e administrar um laboratório.

### 6.2 Três provas de apoio (texto para a página; fonte: ficha de 68615)

1. **Um objetivo escrito para o laboratório.** Capacitar a médica e o médico veterinário a trabalhar em laboratórios clínicos, com correlação clínico-laboratorial, conhecimento de equipamentos e metodologias, técnicas de coleta e a estrutura e a administração de um laboratório. *(Fonte: texto de apresentação da ficha.)*
2. **O laboratório inteiro, fase por fase.** Materiais biológicos e erros pré-analíticos, analíticos e pós-analíticos; hemograma e sua automação; hemostasia; hemoparasitoses; avaliação bioquímica, função renal e urinálise; eletrólitos e hemogasometria; distúrbios endócrinos; exame coproparasitológico; citologia; líquidos cavitários e líquor; testes imunológicos e PCR; microbiologia; controle de qualidade e biossegurança no laboratório clínico veterinário. *(Fonte: cronograma.)*
3. **Prática presencial com laudo.** Os módulos presenciais trazem automação e prática de hemograma, hemoparasitoses em hematoscopia, mielograma, hemocomponentes e transfusão, prática de bioquímica e urina, coleta e confecção de lâminas e técnicas básicas de microbiologia; a elaboração de laudos aparece ao longo do cronograma. As aulas presenciais não são transmitidas. *(Fonte: cronograma, módulos marcados Presencial, e observação da ficha.)*

### 6.3 Respostas às 3 objeções principais (texto para a página)

| Objeção [SUPOSIÇÃO, H-A11.3 e Q11.1] | Resposta |
|---|---|
| "Serve para quem é clínico ou só para quem trabalha em laboratório?" | "O público da turma são médicas e médicos veterinários. O foco é o laboratório clínico, e a correlação clínico-laboratorial atravessa o curso: do pedido do exame à leitura do laudo." Recorte de perfil [CONFIRMAR NO CATÁLOGO]. |
| "Patologia clínica ou citopatologia: qual eu faço?" (68615-Q3) | Frase-ponte da seção 5, sem mudança. |
| "Tem prática de verdade ou é tudo online?" (68615-Q4) | "A teoria é online e há módulos presenciais de prática: automação e prática de hemograma, bioquímica e urina, mielograma, coleta e confecção de lâminas e microbiologia. Essas aulas não são transmitidas." |

**Apoio para o FAQ (68615-Q5):** "O curso ensina a montar e administrar um laboratório?" Resposta: "Estruturar e administrar um laboratório está no objetivo do curso, junto com controle de qualidade, biossegurança e as boas práticas de laboratório em análises clínicas." Sem prometer resultado de negócio nem renda.

### 6.4 Chamada principal e 3 variações

- **Chamada principal:** "Veja o cronograma do laboratório clínico, do pré-analítico ao laudo."
- **Variação 1 (consciente do problema):** "Erro de exame começa antes do equipamento: na coleta, no armazenamento e no envio da amostra."
- **Variação 2 (consciente da solução):** "Hemograma, bioquímica, urinálise, citologia e microbiologia, com prática presencial e gestão do laboratório no mesmo curso."
- **Variação 3 (pronto para decidir):** "Cronograma, quem ensina e condições estão nesta página. Em dúvida entre patologia clínica e citopatologia? O time explica a diferença."

---

## 7. Seção 333: Pós-graduação em Citopatologia Veterinária (leitura de lâminas)

**Notas internas.** Palavra principal (F1): "pós-graduação em citopatologia veterinária" (333-K0); diferencial de vocabulário "leitura de lâminas" (333-K3). Perguntas de IA: 333-Q1, Q2, Q3 e Q4. Bloqueadas: 333-Q5 e 333-QC2 (OU3). Nenhuma palavra sobre coordenação nem sobre quem ensina (OU12); a seção `docentes` é dado. Ficam fora "oportunidade única", "contribui para o avanço da ciência" e "o que há de mais recente" (textos da ficha). O ticket menor que o de 68615 não entra em texto nenhum. **C1 e C2 (contagem pela ficha, só para conferência interna):** são 6 módulos presenciais (1, 5, 10, 12, 13 e 20); só 3 deles (5, 10 e 20, "Experiências práticas citopatológicas") são de leitura de lâminas e discussão de casos; os outros são manejo de materiais biológicos (1), citologia esplênica e linfoma (12) e mielograma (13). O texto para a página nunca soma os presenciais nem trata todos como de leitura: diz "módulos presenciais de leitura de lâminas e discussão de casos" e nomeia os outros presenciais pelo tema.

### 7.1 Mensagem central (texto para a página)

> Citopatologia veterinária centrada na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema.

### 7.2 Três provas de apoio (texto para a página; fonte: ficha de 333)

1. **Leitura de lâminas no presencial.** O cronograma tem módulos presenciais de leitura de lâminas e discussão de casos, chamados de experiências práticas citopatológicas. Os demais módulos presenciais tratam de manejo do material, de citologia esplênica e linfoma e de mielograma. As aulas presenciais não são transmitidas. *(Fonte: cronograma e observação da ficha; contagem nas notas internas, C1 e C2.)*
2. **Começa pelo material.** O curso abre com um módulo presencial de manejo de materiais biológicos (coleta, armazenamento, acondicionamento e transporte de amostras, técnicas de coloração e microscopia) e segue para citologia básica, critérios de malignidade e gestão da qualidade aplicada à citopatologia. *(Fonte: cronograma. Fato de formato, sem tom de prazo.)*
3. **Lesão por lesão, sistema por sistema.** Processos inflamatórios e enfermidades infecciosas, derrames cavitários, líquidos biológicos, trato respiratório, neoplasias de células redondas, sangue periférico, neoplasias glandulares e mesenquimais, trato gastrointestinal, aparelho urinário, citopatologia reprodutiva, oftalmológica e auditiva, com atualizações em imunocitopatologia, automação citopatológica e citoinclusão. *(Fonte: cronograma.)*

### 7.3 Respostas às 3 objeções principais (texto para a página)

| Objeção [SUPOSIÇÃO, Q11.2 e 333-Q2] | Resposta |
|---|---|
| "Citopatologia ou patologia clínica: qual eu faço?" (333-Q3) | Frase-ponte da seção 5, sem mudança. |
| "Vou treinar leitura de lâmina de verdade?" | "Sim. O cronograma tem módulos presenciais de leitura de lâminas de citopatologia e discussão de casos. Outros módulos presenciais trabalham o manejo do material, a citologia esplênica e o linfoma e o mielograma." Sem prometer volume de lâminas. |
| "Preciso já trabalhar em laboratório para acompanhar?" | "O público da turma são médicas e médicos veterinários. O curso abre com o manejo do material, a coloração e a microscopia, e passa pela citologia básica antes de entrar nos sistemas." Recorte de perfil e necessidade de microscópio próprio [CONFIRMAR NO CATÁLOGO]. |

**Fora da página até a resposta da Ufape:**
- "Se eu entrar depois do início, como recupero o módulo presencial?" (OU3). Resposta do time: "Vou confirmar com a secretaria como fica e te retorno." Nenhuma peça depois do início.
- "Quem ensina?" (OU12). Sem resposta de texto; a seção `docentes` mostra o dado da ficha. Nunca "coordenação".

### 7.4 Chamada principal e 3 variações

- **Chamada principal:** "Veja o cronograma de leitura de lâminas, sistema por sistema."
- **Variação 1 (consciente do problema):** "A lâmina chega e a dúvida fica: processo inflamatório ou neoplásico?"
- **Variação 2 (consciente da solução):** "Módulos presenciais de leitura de lâminas e discussão de casos, com a teoria online entre eles."
- **Variação 3 (pronto para decidir):** "Cronograma e condições estão nesta página. Em dúvida entre citopatologia e patologia clínica? O time explica a diferença."

---

## 8. Autochecagem (auditorias/02-estrategia-e-posicionamento.md e auditorias/conformidade-educacional.md)

| Item | Situação |
|---|---|
| Texto para a página sem número, preço, data, vaga, carga, duração, local e nome de docente | Sim, nas 5 seções (ordinais, numerais romanos e números por extenso evitados; "módulo 1", "Citologia I a III" e "Experiências práticas I a III" reescritos sem número) |
| Toda prova com origem na ficha | Sim, com a fonte ao lado; o que a ficha não traz está [CONFIRMAR] |
| Sem frase ligada ao órgão regulador, sem certificação | Sim |
| 657 sem prova ou título de especialista e sem o item de resultado clínico do objetivo (C14) | Sim; o item fica só no dado `objetivos` |
| Sem superlativo da ficha | Sim ("referência nacional", "oportunidade única", "de excelência", "de ponta" fora) |
| Sem urgência; regra do 3º módulo só como dado (OU14) | Sim |
| Sem bolsa, prova de bolsa, desconto ou promoção; 341 sem nada que dependa da promoção (OU10, C7) | Sim |
| 657 sem pré-requisito (U10) | Sim; pergunta vai para a secretaria |
| 333 sem "coordenação" (OU12) e sem pós-início (OU3) | Sim |
| 333 sem somar presenciais e sem tratar todos como de leitura de lâminas (C1, C2) | Sim; provas e objeção reescritas |
| 68615 x 333 diferenciadas sem comparação de valor | Sim, frase-ponte única (seção 5) |
| Sem promessa de emprego, renda, aprovação ou resultado clínico | Sim |
| Voz do candidato marcada | Sim, todas as falas de objeção [SUPOSIÇÃO] |
| Nome "Pós-graduação em <área>" | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; busca final pelo orquestrador |

**Próximo passo da cadeia:** F3 landing-page (texto das 5 páginas, 13/11), depois F4 seo-on-page e F5 otimizador-de-cta. Fora da cadeia /pagina-de-curso, o próximo agente sugerido para estas mensagens é estrategia-de-conteudo.

---

## Ajustes antes da entrega (plano da onda 2, versão 2)

- **C1 e C2 (333):** a prova 1 e a resposta "Vou treinar leitura de lâmina de verdade?" deixaram de tratar todos os módulos presenciais como de leitura de lâminas; os presenciais de manejo do material, citologia esplênica e linfoma e mielograma são nomeados à parte. A contagem (6 presenciais, 3 de leitura) fica só nas notas internas.
- **C14 (657):** nada sobre prova ou título de especialista; o item de resultado clínico do objetivo da ficha deixou de ser citado nesta casa e fica só na seção de dado `objetivos`.
- **C7 (341):** saiu a pergunta pronta sobre a promoção; a resposta de investimento é a mesma das outras turmas, e qualquer pergunta sobre condição de pagamento vai para a secretaria sem texto pronto.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início e status "aberto" das 5 turmas: contexto/catalogo-de-cursos.md, seção 2. Nenhum desses valores está no texto para a página.
- 657: transição de "anestesias de protocolo" para "anestesia de precisão", fisiologia aplicada, decisão crítica e gestão de riscos; objetivo de conduzir pacientes de risco moderado a alto e antecipar crises; módulos presenciais de bloqueios locorregionais, hemodinâmica avançada e ventilação mecânica, reanimação com avaliação viscoelástica, TIVA e TCI, cirurgia cardiotorácica e pets não convencionais; aulas práticas não transmitidas; público-alvo "exclusiva para médicos veterinários anestesistas já atuantes": ficha de 657.
- 341: temas por sistema, de abordagem clínica a odontologia equina; treinamentos práticos e demonstrativos na maioria dos temas; teoria online e práticas presenciais aos fins de semana; estágio obrigatório e atividades complementares; módulo de medicina baseada em evidências; avaliação com provas práticas, seminários e TCC opcional; segundo local em Indaiatuba; texto de reembolso truncado: ficha de 341.
- 289: 4 dos 6 módulos presenciais de prática hands-on de ecocardiograma (correção do orquestrador em 27/10/2026, ficha de 289: módulos 9, 13, 16 e 19); laudos ecocardiográficos; percurso da anatomia às emergências cardíacas; teoria acompanhada a distância e só módulos práticos obrigatoriamente presenciais; público "Médicos Veterinários"; bloco "PROVA DE BOLSA": ficha de 289.
- 68615: objetivo de trabalhar em laboratórios clínicos, correlação clínico-laboratorial, estruturar e administrar um laboratório, equipamentos, metodologias e coleta; módulos de pré-analítico a controle de qualidade e biossegurança; módulos presenciais de hemograma, hemoparasitoses, mielograma, hemocomponentes, bioquímica e urina, citologia com confecção de lâminas, líquidos cavitários e microbiologia; ficha sem o aviso de passagem e hotel: ficha de 68615.
- 333: 6 módulos presenciais (1, 5, 10, 12, 13 e 20), dos quais 3 (5, 10 e 20) de leitura de lâminas e discussão de casos; módulo inicial presencial de manejo de materiais biológicos, coloração e microscopia; percurso por lesão e sistema; coordenação "UFAPE" e uma professora listada: ficha de 333, confirmado pelas correções C1 e C2 do plano em versão 2.
- Reembolso dos valores de inscrição devido se a turma não for confirmada: fichas de 657, 289, 68615 e 333.
- Regras do texto da IA (sem número, preço, data, vaga, local e nome de docente) e blocos do tipo pos: templates/pagina-da-turma.md.
- Palavras principais, IDs de perguntas, divisão de vocabulário 68615 x 333, regra de âncora e CP1: saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md, seções 1, 4 e 5 a 9.
- Travas U10, OU3, OU10, OU11, OU12 e OU14: plano do CMO da onda 2, seções 2, 8 e 10 (F2 e F3); C1, C2, C7 e C14: versão 2 do plano, pelo orquestrador.
- Matrícula até o 3º módulo (decisão 18), turma mínima de 15 sem número em peça até a correção das páginas (decisão 11 e A12), sem peça de bolsa (decisão 14), sem valor de inscrição até a U11 (decisão 16): docs/execucao-2026-10-26.md.
- Voz da marca técnica, próxima e confiante, de colega para colega: contexto/ufape-geral.md (ela mesma marcada [SUPOSIÇÃO] lá).

## [SUPOSIÇÃO]

- Todas as falas de objeção "nas palavras do candidato": hipóteses de insights-de-alunos-pos e pesquisa-de-persona-pos (H-A1.1, H-A1.4, H-A2.3, H-A11.3, H-A14.1, Q11.1, Q11.2), sem voz real.
- Escolha das 3 objeções principais de cada turma e da ordem das provas.
- Todo o texto proposto (mensagens centrais, provas redigidas, respostas, chamadas e variações) é deste agente, a validar pela pessoa do marketing.
- Mapa de uso dos textos nos blocos da página (seção 0) e o uso da mensagem central como subtítulo do `hero`.
- Atribuição de estágio de consciência a cada variação.
- Que a frase-ponte única em 68615 e 333 ajuda assistentes de IA a citar uma resposta só (herdada da F1).
- Que "módulos de técnica avançada" (657) e "sistema por sistema" (341 e 333) descrevem bem o cronograma sem exagero; a revisão docente pode ajustar.

## [CONFIRMAR]

- **U10:** pré-requisito de 657. Até lá, nenhuma peça diz quem pode entrar.
- **OU3:** como se repõem módulos perdidos, em especial o módulo inicial presencial de 333. Bloqueia 333-Q5, 333-QC2 e qualquer peça de 333 depois do início.
- **OU10:** regra da promoção de 341 ou retirada da página.
- **OU11:** onde é a prática de 341 (sede, Indaiatuba ou "hospital veterinário" da ficha) e formato do módulo 3.
- **OU12:** coordenação e corpo docente de 333.
- **OU14:** se a regra do 3º módulo entra como dado da turma no `faq`.
- **CP1:** se `titulo_seo` e `resposta_citavel` podem receber a cidade por variável do dado (pesa mais em 289).
- **A12:** correção da turma mínima de 20 para 15 nas 5 páginas, para o número poder aparecer como dado.
- **Reembolso em 341:** o texto da ficha está truncado e contraditório ("apenas se a turma for confirmada").
- **[CONFIRMAR NO CATÁLOGO]:** recorte de perfil e nível de entrada de 289, 341, 68615 e 333; necessidade de microscópio próprio em 333; se 289 pode ser descrita como "de cães e gatos" (a ficha também traz cardiologia equina e de pets não convencionais).
- **U11:** valor da inscrição; até lá nenhuma peça cita valor.
- **Voz real:** conversas anonimizadas do WhatsApp de vendas para trocar as falas [SUPOSIÇÃO].
- **Revisão docente:** conferência técnica das provas e das variações de 657, 341, 289, 68615 e 333 antes da publicação.
- **Plano em versão 2:** este agente leu a versão 1 do plano e aplicou só C1, C2, C7 e C14, como chegaram do orquestrador; se a versão 2 mudar mais algum ponto da F2, a casa precisa de nova rodada.
