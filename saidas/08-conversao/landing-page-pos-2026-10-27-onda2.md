# Páginas das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), encomenda F3 da onda 2

- **Agente:** landing-page (departamento 08, Conversão)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** F3 do plano do CMO em versão 2 (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md, seção 10, linha F3, e seções 2, 7 e 9). O plano previa o nome landing-page-pos-2026-11-13.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Formato:** templates/pagina-da-turma.md (versão 1), tipo pos, ordem padrão, uma seção por turma com o código no título.
- **Status:** rascunho para o qa-de-marketing (auditorias/03-busca.md, auditorias/08-conversao.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago a partir deste arquivo. Publicar as páginas e corrigir as páginas no ar são ações humanas (pedido OB1, no fim de cada seção).
- **Consumidores:** seo-on-page (F4: `titulo_seo`, `descricao_seo`, `resposta_citavel`, `entidades` e `descricao_schema`), otimizador-de-cta (F5), qa-de-marketing (F13) e a plataforma, que valida o formato. Fora da cadeia, depois da publicação e com dados reais, o próximo agente é analise-cro.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 14, 16, 18 e 20)
  - contexto/ufape-geral.md (voz da marca: técnica, próxima, confiante; de colega para colega)
  - contexto/pos-graduacao.md (inclusive "Padrão de nome")
  - contexto/catalogo-de-cursos.md (seção 2, linhas de 657, 341, 289, 68615 e 333; única fonte dos dados de curso)
  - Fichas inteiras: contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md, 341-pos-graduacao-em-medicina-interna-equina.md, 289-pos-graduacao-em-cardiologia-veterinaria.md, 68615-pos-graduacao-em-patologia-clinica.md, 333-pos-graduacao-em-citopatologia-veterinaria.md
  - templates/pagina-da-turma.md e .claude/commands/pagina-de-curso.md
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (versão 2, inteiro; pesam as seções 1, 2, 4, 8, 9 e 10)
  - F1: saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md (inteiro: palavra principal, divisão 68615 x 333, CP1)
  - F2: saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda2.md (inteiro; os textos das seções 1 a 7 são usados como estão)
  - auditorias/conformidade-educacional.md e auditorias/08-conversao.md
- **Não aberto:** saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2.md (as correções C1, C2, C7 e C14 chegam pelo plano em versão 2 e pela F2, que já as aplicou); saidas/08-conversao/landing-page-pos-2026-10-26.md (hub das provas, não serve a estas turmas); analise-cro-pos-2026-10-26.md; faculdade.ufape.com.br; nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum docente é nomeado no texto das páginas.
- **Marcadores:** [SUPOSIÇÃO] é escolha ou hipótese deste agente, com a origem. [CONFIRMAR] é dado que só a Ufape tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz.

---

## 0. Como ler este arquivo e regras aplicadas às 5 páginas

1. **Só o que a IA escreve.** Em cada turma, os blocos de texto da página são `hero`, `sobre`, `para_quem`, `investimento` (só a frase de apoio), `faq` (só as perguntas da IA), `formulario` e `cta_final`. Tudo o mais é dado do catálogo ou escolha humana e aparece só como chave, com a visibilidade proposta. O texto está em bloco de citação (">") ou aspas e é o que vai para a página. Notas internas, códigos, módulos citados por número e pendências ficam fora desses blocos e não vão para a página.
2. **Nenhum número, preço, data, local, vaga ou nome de docente no texto da página.** Nem algarismo, nem ordinal, nem número romano. O 3º módulo, a turma mínima e as datas aparecem só como dado da turma (OU14, A12), indicado pela chave.
3. **Mensagem da F2 sem reescrita.** A mensagem central, as provas, as respostas às objeções, a frase-ponte 68615 x 333 e as chamadas vêm da F2 como estão. Dois ajustes de forma, sem trocar palavra de sentido: (a) onde a mensagem central passa de 70 caracteres (título) ou 160 (subtítulo), a frase é dividida entre `hero.titulo` e `hero.subtitulo` (o que o título leva sai do subtítulo) e a frase inteira abre o `sobre`; (b) cada resposta vira par pergunta e resposta no `faq`, e eu escrevo só a pergunta.
4. **Ordem.** Ordem padrão do tipo pos nas 5 páginas, sem proposta de outra. A chave `objetivos` existe no catálogo do tipo mas não está na ordem padrão; por isso o objetivo da ficha (inclusive "reduzir complicações e mortalidade perioperatória", em 657) não aparece nas páginas. Se o editor propuser incluí-la, em 657 ela fica oculta até a revisão da regulação (pedido na seção 657).
5. **Seção de certificação oculta, sem frase.** `certificacao` com visivel nao nas 5, até a regulação aprovar o texto oficial (contexto/catalogo-de-cursos.md: [PREENCHER COM A REGULAÇÃO]). Nenhuma página escreve "MEC", "certificado", "reconhecida" nem variações.
6. **Sem bolsa.** Nenhuma pergunta ou resposta fala de bolsa, prova de bolsa, desconto ou promoção (decisão 14; 341 sem promoção, OU10). Pergunta sobre bolsa vai para a secretaria.
7. **Sem depoimento, nota, empregabilidade ou prova externa.** Não há depoimento autorizado em mãos: `depoimentos` fica oculta (escolha humana). A voz do candidato aparece nas perguntas do `faq`, todas [SUPOSIÇÃO] (hipóteses da persona e das objeções da F2) até chegarem conversas anonimizadas do WhatsApp de vendas.
8. **Chamada principal única por página:** "Quero me inscrever" (formulário). WhatsApp é chamada secundária, com o número da praça vindo do dado (Goiânia tem telefone próprio em 289).
9. **Ordem do que o candidato precisa ver até o fim:** topo (título, subtítulo, botão), proposta (`sobre`), para quem, conteúdo (`matriz`), quem ensina, condições (`investimento`, `local_e_datas`), dúvidas (`faq`), formulário, chamada final. É a ordem padrão do tipo, então problema, solução, rotina, provas, oferta, objeções e chamada final ficam todos cobertos: problema e solução no `sobre`, rotina e modalidade no `sobre` e no `faq`, provas no `sobre` e na `matriz` (dado), oferta no `investimento` (dado), objeções no `faq`.

---

## 1. Seção 657: Pós-graduação em Anestesiologia Avançada

### 1.1 Cabeçalho (template)

```
tipo: pos
curso: pos-graduacao-em-anestesiologia-avancada [SUPOSIÇÃO: slug derivado do nome do arquivo da ficha; o catálogo não traz slug]
turma_ou_edicao: [CONFIRMAR NO CATÁLOGO] (slug da turma do código 657; o catálogo não traz slug de turma)
palavra_chave_principal: pós-graduação em anestesiologia avançada veterinária
```

### 1.2 SEO (IA)

A cargo do F4 (seo-on-page), que lê este texto e o F1. Não escrito aqui. A página não promete "para quem" (U10): `resposta_citavel` da 657-Q1 sai sem a parte "para quem".

### 1.3 Ordem e visibilidade

```
ordem: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final
motivo_da_ordem: ordem padrão do tipo
```

| Chave | visivel | Origem e nota |
|---|---|---|
| hero | sim | IA e humano (imagem do acervo, escolha do editor) |
| numeros | sim | dado |
| sobre | sim | IA |
| para_quem | **nao** | oculta até U10: nenhuma peça diz quem pode entrar em 657. A ficha diz "exclusiva para médicos veterinários anestesistas já atuantes" e a Ufape ainda não respondeu |
| diferenciais | sim se o banco trouxer | dado, sem reescrita |
| matriz | sim | dado. Ver pedido OB1 sobre frases de resultado clínico no cronograma |
| docentes | sim | dado |
| certificacao | **nao** | oculta até a regulação; sem frase |
| video | nao | humano: o editor decide; o roteiro da F9 serve a Reels |
| depoimentos | nao | humano: sem depoimento autorizado em mãos |
| investimento | sim | dado e IA (frase de apoio) |
| local_e_datas | sim | dado |
| parceiros | nao | dado: o bloco da ficha está vazio; mostra só se o banco trouxer parceiros [CONFIRMAR] |
| faq | sim | dado e IA |
| formulario | sim | dado e IA |
| cta_final | sim | IA |

### 1.4 Texto da IA

**hero**

- titulo (63 caracteres): Pós-graduação em Anestesiologia Avançada: anestesia de precisão
- subtitulo (111 caracteres): Fisiologia aplicada, decisão crítica em tempo real e prática presencial guiada nos módulos de técnica avançada.

**sobre**

> Da anestesia de protocolo à anestesia de precisão: fisiologia aplicada, decisão crítica em tempo real e prática presencial guiada nos módulos de técnica avançada. A Faculdade Ufape oferece a pós-graduação em anestesiologia avançada veterinária em formato semipresencial.
>
> **Uma proposta escrita, não um slogan.** O programa foi estruturado para a transição da anestesia de protocolo para a anestesia de precisão, com base em fisiologia aplicada, tomada de decisão crítica e gestão de riscos, para conduzir pacientes de risco moderado a alto e antecipar crises anestésicas.
>
> **O paciente que o protocolo não resolve.** Hemodinâmica além da pressão arterial, com foco em débito cardíaco e perfusão tecidual; ventilação do paciente especial e proteção pulmonar; bloqueio neuromuscular e ventilação monopulmonar; distúrbios de coagulação e uso racional de hemoderivados; anestesia em cirurgias neurológicas e cardiotorácicas; dor e analgesia em felinos; pets não convencionais.
>
> **Prática guiada nos módulos presenciais.** Bloqueios locorregionais com prática guiada e execução avançada; hemodinâmica avançada e ventilação mecânica com manipulação de ventiladores e monitores hemodinâmicos; TIVA e TCI em execução avançada; reanimação cardiorrespiratória com avaliação viscoelástica do coágulo. As aulas práticas não são transmitidas nem gravadas.

**para_quem:** oculta (U10). Nenhum item escrito.

**investimento (frase de apoio, sem valor)**

> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.

**faq (perguntas da IA, depois das que já estão na turma)**

> **O que o curso traz além da rotina de anestesia?**
> O curso vai para onde o protocolo não chega: hemodinâmica além da pressão arterial, ventilação do paciente especial, bloqueio neuromuscular, coagulação no transoperatório e anestesia em cirurgias neurológicas e cardiotorácicas. Nos módulos presenciais, a prática é guiada, com ventiladores, monitores e bombas de infusão na mão.
>
> **Dá para encaixar o curso na escala do centro cirúrgico?**
> A teoria é online, em fins de semana com data marcada no cronograma. O presencial fica só nos módulos de prática, também com mês marcado, então dá para montar a escala antes de começar.
>
> **Quanto vou pagar no total?**
> O total, as parcelas e a matrícula estão nesta página, ao lado do cronograma de cada módulo presencial. Você vê o que paga e o que vai praticar antes de decidir.
>
> **E se a turma não fechar?**
> A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados.

- **Item de dado da turma, não escrito pela squad (OU14):** pergunta "Posso entrar depois que a turma começar?" com a regra da decisão 18 e a data do 3º módulo digitadas pelo editor como dado da turma. Depende de OU14, OU6 e OU3. Modelo para o editor: seção 7.1 deste arquivo.
- **Fora da página:** "Preciso ser anestesista ou já atuar na área?" e qualquer pergunta sobre prova ou título de especialista vão para a secretaria (U10, C14). Resposta do time: "Vou confirmar com a secretaria e te retorno."

**formulario**

- botao: Quero me inscrever
- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade.
- Finalidade e link da política de privacidade são refinados pelo F5 (otimizador-de-cta).

**cta_final**

- titulo: Veja o cronograma e os módulos de prática guiada antes de decidir.
- botao: Quero me inscrever
- apoio (opcional): Cronograma, quem ensina e condições estão nesta página. Ficou alguma dúvida? Fale com o time.

### 1.5 Travas aplicadas em 657

- U10: sem pré-requisito em nenhuma frase; `para_quem` oculta; a palavra "exclusiva" fora de título e descrição.
- C14: sem o convite da prova de Especialista nem qualquer frase de título; sem o item de resultado clínico do objetivo (fica só na chave de dado `objetivos`, fora da ordem).
- OU14: regra do 3º módulo só como dado.

### 1.6 OB1: o que corrigir na página de 657 que está no ar hoje (ficha de 26/10/2026)

1. Frase "CERTIFICADO PELO MEC" (bloco de certificação). Remover; a seção fica oculta até o texto da regulação.
2. "Vagas: Mínimo 20 alunos". Trocar para 15 (decisão 11, A12) ou deixar só o aviso de turma sem número.
3. Convite "Tem interesse em prestar a prova de Especialista em Anestesiologia? Clique aqui". Retirar ou passar pela regulação, porque título de especialista não entra em peça [CONFIRMAR com a regulação].
4. Público-alvo "exclusiva para médicos veterinários anestesistas já atuantes". A Ufape escreve o pré-requisito real (U10) ou retira a frase; até lá nenhuma peça repete.
5. Regra do 3º módulo: a página não diz que a matrícula vai até o 3º módulo. Incluir como dado da turma, com a data (decisão 18, OU14), com a redação final depois de OU6.
6. Para a regulação revisar (a ficha promete resultado clínico ou usa superlativo): objetivo "Reduzir complicações e mortalidade perioperatória", "com maestria" e "profissionais diferenciados"; módulo de reanimação com "elevando drasticamente as taxas de retorno à circulação espontânea"; módulo de casos com "a decisão do anestesista dita a sobrevivência"; "máxima segurança e previsibilidade". Se `objetivos` entrar na página, fica oculta até essa revisão.
7. "Prova de recuperação ... (Prova cobrada separadamente)" sem valor: preço e condições têm de ser completos (conformidade-educacional, CDC). A Ufape informa o valor ou a regra [CONFIRMAR].
8. Bloco "Documentos para matrícula (MEC e UFAPE)" cita o órgão: a regulação diz se o título fica [CONFIRMAR].
9. Docente listada duas vezes com grafias diferentes (Dra. Mayara Travalini de Lima e Profa. Mayara Travalini): uniformizar no dado.

---

## 2. Seção 341: Pós-graduação em Medicina Interna Equina

### 2.1 Cabeçalho (template)

```
tipo: pos
curso: pos-graduacao-em-medicina-interna-equina [SUPOSIÇÃO: slug derivado do nome do arquivo da ficha; o catálogo escreve "Pós Graduação" e o padrão de nome da linha é "Pós-graduação em"]
turma_ou_edicao: [CONFIRMAR NO CATÁLOGO] (slug da turma do código 341)
palavra_chave_principal: pós-graduação em medicina interna equina
```

### 2.2 SEO (IA)

A cargo do F4. Não escrito aqui.

### 2.3 Ordem e visibilidade

```
ordem: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final
motivo_da_ordem: ordem padrão do tipo
```

| Chave | visivel | Origem e nota |
|---|---|---|
| hero | sim | IA e humano |
| numeros | sim | dado |
| sobre | sim | IA |
| para_quem | sim | IA |
| diferenciais | **só depois da correção** | dado, sem reescrita. O texto da ficha traz "descontos e bolsas de estudo" e "corpo docente de excelência": a chave só aparece com o dado corrigido (OB1); até lá, oculta |
| matriz | sim | dado. O módulo marcado "ONLINE PRESENCIAL" e o estágio obrigatório vêm do dado (OU11) |
| docentes | sim | dado |
| certificacao | **nao** | oculta até a regulação; sem frase |
| video | nao | humano |
| depoimentos | nao | humano: sem depoimento autorizado em mãos |
| investimento | sim | dado e IA. **Sem promoção** (OU10): o dado de preço não pode carregar o texto da promoção cortado |
| local_e_datas | **só depois da correção** | dado, obrigatória. Não publicar com o segundo local sem explicação (OU11) nem com o texto do endereço quebrado: a página só sai com o dado corrigido |
| parceiros | nao | dado: bloco vazio na ficha [CONFIRMAR] |
| faq | sim | dado e IA |
| formulario | sim | dado e IA |
| cta_final | sim | IA |

### 2.4 Texto da IA

**hero**

- titulo (61 caracteres): Pós-graduação em Medicina Interna Equina: sistema por sistema
- subtitulo (118 caracteres): Do paciente crítico ao potro neonato, com teoria online e prática presencial em fins de semana marcados no cronograma.

**sobre**

> Medicina interna equina sistema por sistema, do paciente crítico ao potro neonato, com teoria online e prática presencial em fins de semana marcados no cronograma. A Faculdade Ufape oferece a pós-graduação em medicina interna equina em formato semipresencial, pensada para o médico veterinário de equinos que quer aprofundar o raciocínio clínico por sistema.
>
> **A espécie inteira, por sistema.** Abordagem clínica do paciente equino e farmacologia; paciente crítico, choque e cuidados intensivos; preparação cirúrgica e manejo de feridas; cardiologia com eletrocardiograma e ecocardiograma; trato respiratório; sistema digestivo; sistema locomotor e diagnóstico de claudicação; neonatologia, UTI neonatal e potros críticos; podologia; odontologia equina; transtornos neurológicos; pele, olhos, sistema urinário e genital.
>
> **Prática em quase todos os temas.** O curso prevê treinamentos práticos e demonstrativos na maioria dos temas, aulas teóricas online e práticas presenciais aos fins de semana, e termina com estágio obrigatório e atividades complementares. **Evidência e leitura crítica.** Há um módulo de medicina equina baseada em evidências, os conteúdos teóricos combinam aula online e leitura crítica, e a avaliação inclui provas práticas, seminários e trabalho de conclusão quando escolhido com a coordenação do curso.

**para_quem**

- Médicas e médicos veterinários interessados em medicina interna equina.
- Quem atende equinos, inclusive a campo, e precisa planejar as viagens das aulas presenciais com antecedência.
- Quem quer ampliar a prática com cavalos, do paciente crítico à podologia.
- Quem busca organizar o raciocínio clínico por sistema, com leitura crítica e medicina baseada em evidências.

**investimento (frase de apoio, sem valor)**

> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.

**faq (perguntas da IA)**

> **Pratiquei pouco com cavalos na faculdade. O curso ajuda?**
> O curso começa pela abordagem clínica do paciente equino e prevê treinamento prático e demonstrativo na maioria dos temas, do paciente crítico à podologia. A teoria vem antes da prática em cada sistema.
>
> **Atendo a campo. Dá para viajar para as aulas presenciais?**
> A teoria é online. O presencial acontece em fins de semana, com as datas publicadas no cronograma antes de começar. Compre passagem e hotel só depois de a turma ser confirmada.
>
> **Quanto vou pagar no total?**
> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.
>
> **E se a turma não fechar?**
> A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada.

- **Sem frase de reembolso em 341:** o texto da ficha está truncado e contraditório [CONFIRMAR].
- **Item de dado da turma, não escrito pela squad (OU14):** "Posso entrar depois que a turma começar?", com a regra e a data do 3º módulo. O módulo 3 da ficha está marcado "ONLINE PRESENCIAL": a frase só fecha com OU11. Modelo: seção 7.1.
- **Fora da página até OU11:** "Onde são as aulas práticas com os cavalos?". Resposta do time: "Vou confirmar com a secretaria onde acontece cada módulo presencial e te retorno." A palavra "hospital veterinário" não entra em texto nenhum.
- **Fora da página:** qualquer pergunta sobre condição de pagamento além do que a página mostra vai para a secretaria, sem texto pronto.

**formulario**

- botao: Quero me inscrever
- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade.

**cta_final**

- titulo: Veja os sistemas, os módulos práticos e as condições da turma de medicina interna equina.
- botao: Quero me inscrever
- apoio (opcional): Cronograma, quem ensina e condições estão nesta página. Fale com o time antes de se matricular.

### 2.5 Travas aplicadas em 341

- OU10 e C7: nenhuma frase, pergunta ou chamada depende da promoção; a resposta de investimento é a mesma das outras turmas. A ficha também diz "descontos e bolsas de estudo": fora (decisão 14).
- OU11: sem local da prática e sem "hospital veterinário"; formato do módulo 3 só como dado.
- Fora do texto: a frase da ficha que chama o recém-formado de "inseguro e sem nenhum diferencial competitivo", por ofender o público, e "corpo docente de excelência" (superlativo sem fonte).
- Sem termo de pequenos animais, cães ou gatos (negativas da Busca paga).

### 2.6 OB1: o que corrigir na página de 341 que está no ar hoje (ficha de 26/10/2026)

1. Frase "CERTIFICADO PELO MEC". Remover; a seção fica oculta até o texto da regulação.
2. "Vagas: Mínimo 20 alunos". Trocar para 15 (decisão 11, A12) ou deixar só o aviso sem número.
3. Promoção "20% DE DESCONTO EM TODO O CURSO", com a regra cortada ("A Medicina Equina é uma esp..."). A Ufape escreve a regra completa (quem, quando, até quando, se acumula) ou retira a promoção (OU10). O mesmo texto cortado está no campo de preço do catálogo.
4. Segundo local na ficha ("Pressa. Português: Ermênio de Oliveira Penteado... Indaiatuba") sem explicação e com o texto quebrado; e a frase "as aulas práticas serão realizadas no EQUIPAMENTO HOSPITAL VETERINÁRIO". A Ufape diz onde acontece cada módulo presencial (OU11).
5. Módulo 3 marcado "ONLINE PRESENCIAL": dizer se é online ou presencial (OU11).
6. "possibilidade de descontos e bolsas de estudo" no texto de diferenciais: retirar (decisão 14).
7. "veterinários formados com pouca experiência prática e, consequentemente, inseguros e sem nenhum diferencial competitivo": reescrever; ofende o público.
8. "corpo docente de excelência" e "conteúdo inovador" (superlativos sem fonte): retirar ou documentar.
9. Texto de reembolso truncado ("Solicitados, serão solicitados reembolsos de valores de inscrição, apenas se a turma for confirmada"): reescrever com a regra clara [CONFIRMAR].
10. Regra do 3º módulo: incluir como dado da turma, com a data (decisão 18, OU14, OU6). A data do 3º módulo cai em feriado nacional (OU17): a Ufape confirma.
11. Nome padrão: "Pós-graduação em Medicina Interna Equina" (a ficha traz "Pós Graduação" e "Pós-Graduação/Especialização").
12. Bloco "Documentos para matrícula (MEC e UFAPE)" cita o órgão: a regulação diz se o título fica [CONFIRMAR].

---

## 3. Seção 289: Pós-graduação em Cardiologia Veterinária

### 3.1 Cabeçalho (template)

```
tipo: pos
curso: pos-graduacao-em-cardiologia-veterinaria [SUPOSIÇÃO: slug derivado do nome do arquivo da ficha; o catálogo não traz slug]
turma_ou_edicao: [CONFIRMAR NO CATÁLOGO] (slug da turma do código 289; existe outra turma de Cardiologia no catálogo, em "verificar", então o slug de turma é o que separa as páginas)
palavra_chave_principal: pós-graduação em cardiologia veterinária
```

### 3.2 SEO (IA)

A cargo do F4. CP1 (cidade em `titulo_seo` e `resposta_citavel`): esta página não escreve a cidade em nenhum texto. A cidade aparece só no dado (`local_e_datas`) e no JSON-LD. Se a CP1 for aprovada, a cidade entra por variável do dado, pelo F4.

### 3.3 Ordem e visibilidade

```
ordem: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final
motivo_da_ordem: ordem padrão do tipo
```

| Chave | visivel | Origem e nota |
|---|---|---|
| hero | sim | IA e humano |
| numeros | sim | dado |
| sobre | sim | IA |
| para_quem | sim | IA |
| diferenciais | sim se o banco trouxer | dado, sem reescrita; se vier com "opções diagnósticas de ponta" ou "atendimento de excelência", corrigir antes (OB1) |
| matriz | sim | dado |
| docentes | sim | dado |
| certificacao | **nao** | oculta até a regulação; sem frase |
| video | nao | humano |
| depoimentos | nao | humano: sem depoimento autorizado em mãos |
| investimento | sim | dado e IA |
| local_e_datas | sim | dado, obrigatória (campus de Goiânia vem do dado) |
| parceiros | nao | dado: bloco vazio na ficha [CONFIRMAR] |
| faq | sim | dado e IA |
| formulario | sim | dado e IA |
| cta_final | sim | IA |

### 3.4 Texto da IA

**hero**

- titulo (64 caracteres): Pós-graduação em Cardiologia Veterinária: da fisiologia ao laudo
- subtitulo (150 caracteres): Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância.

**sobre**

> Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância. A Faculdade Ufape oferece a pós-graduação em cardiologia veterinária em formato semipresencial.
>
> **Do exame físico à emergência.** Anatomia, fisiologia e semiologia circulatória; farmacologia cardiovascular e insuficiência cardíaca congestiva; radiografia; eletrocardiograma, taquiarritmias e bradiarritmias; ecocardiografia com Doppler e hemodinâmica; cardiopatias adquiridas de cães e de felinos; cardiopatias congênitas; hipertensão arterial sistêmica; síndrome cardiorrenal; cirurgia e intervencionismo; anestesia do paciente cardiopata; emergências cardíacas.
>
> **Ecocardiograma na prática.** Os módulos presenciais são de prática hands-on de ecocardiograma, e o curso trata a interpretação crítica e a elaboração de laudos ecocardiográficos na rotina. **Presencial só onde há prática.** Todas as aulas teóricas são acompanhadas a distância; apenas os módulos com aula prática são obrigatoriamente presenciais, e essas aulas não são transmitidas.

**para_quem**

- Médicas e médicos veterinários interessados em cardiologia.
- Quem quer o percurso completo, da fisiologia e do eletrocardiograma às cardiopatias e às emergências, e não só o exame de ecocardiograma.
- Quem mora longe e prefere acompanhar a teoria a distância, com o presencial só nos módulos de prática.

**investimento (frase de apoio, sem valor)**

> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.

**faq (perguntas da IA)**

> **Moro longe. Vou ter de viajar todo mês?**
> Não. A teoria é acompanhada a distância; só os módulos com aula prática são presenciais, e as datas estão no cronograma. Compre passagem e hotel só depois de a turma ser confirmada.
>
> **Preciso da cardiologia completa ou só do exame?**
> Aqui o ecocardiograma faz parte de um percurso maior, que vai da fisiologia e do eletrocardiograma às cardiopatias e às emergências. Se o seu objetivo é só o exame, o guia de decisão da área mostra os dois caminhos lado a lado.
>
> **Sou clínico geral, não cardiologista. Serve para mim?**
> O público da turma são médicas e médicos veterinários, e o curso começa pela anatomia, pela fisiologia e pela semiologia circulatória antes de chegar aos exames.
>
> **Quanto vou pagar no total?**
> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.
>
> **E se a turma não fechar?**
> A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados.

- **A frase do guia** ("o guia de decisão da área mostra os dois caminhos lado a lado") só vai ao ar com o guia A2 publicado e com o link dele na resposta; sem o guia, a editora retira a última frase [CONFIRMAR]. O guia liga à turma de Ecocardiografia (onda 1) sem dizer qual é melhor.
- **Item de dado da turma, não escrito pela squad (OU14):** "Posso entrar depois que a turma começar?", com a regra e a data do 3º módulo. Modelo: seção 7.1.
- **Nível de entrada da pergunta de clínico geral** [CONFIRMAR NO CATÁLOGO]: a ficha diz só "Médicos Veterinários". A resposta não diz que o curso é "para iniciantes".

**formulario**

- botao: Quero me inscrever
- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade.
- O telefone de vendas de Goiânia vem do dado ou do formulário, nunca do texto.

**cta_final**

- titulo: Veja o cronograma, do eletrocardiograma ao ecocardiograma na prática.
- botao: Quero me inscrever
- apoio (opcional): Cronograma, quem ensina e condições estão nesta página. O time de vendas tira suas dúvidas.

### 3.5 Travas aplicadas em 289

- CP1: sem a cidade em nenhum texto.
- Sem bloco de prova de bolsa (decisão 14). O texto de apresentação da ficha não é repetido ("opções diagnósticas de ponta", "atendimento cardiológico de excelência").
- "Ecocardiograma" aparece como conteúdo dos módulos, sem tomar a palavra-alvo da página de Ecocardiografia (F1, seção 3).

### 3.6 OB1: o que corrigir na página de 289 que está no ar hoje (ficha de 26/10/2026)

1. Frase "CERTIFICADO PELO MEC". Remover; a seção fica oculta até o texto da regulação.
2. "Turma mínima de 20 alunos". Trocar para 15 (decisão 11, A12) ou deixar só o aviso sem número.
3. Bloco "PROVA DE BOLSA: Tem interesse em prestar a prova de bolsa? Clique aqui". Retirar (decisão 14).
4. Regra do 3º módulo: incluir como dado da turma, com a data (decisão 18, OU14, OU6).
5. Superlativos do texto de apresentação ("opções diagnósticas de ponta", "atendimento cardiológico de excelência"): retirar ou documentar.
6. Erros de digitação no cronograma ("Ecocargiograma", "Afeccções", aspas abertas no módulo 22): corrigir no dado.
7. Descrever o conteúdo de cardiologia equina e de pets não convencionais do cronograma (módulos 22 e 23) para a página poder decidir se "de cães e gatos" é fiel (F2 marca [CONFIRMAR NO CATÁLOGO]).
8. Bloco "Documentos para matrícula (MEC e UFAPE)" cita o órgão: a regulação diz se o título fica [CONFIRMAR].

---

## 4. Seção 68615: Pós-graduação em Patologia Clínica

### 4.1 Cabeçalho (template)

```
tipo: pos
curso: pos-graduacao-em-patologia-clinica [SUPOSIÇÃO: slug derivado do nome do arquivo da ficha; o catálogo não traz slug]
turma_ou_edicao: [CONFIRMAR NO CATÁLOGO] (slug da turma do código 68615)
palavra_chave_principal: pós-graduação em patologia clínica veterinária
```

### 4.2 SEO (IA)

A cargo do F4. O nome do catálogo não traz "veterinária": a palavra entra no corpo (`sobre`), como pede o F1.

### 4.3 Ordem e visibilidade

```
ordem: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final
motivo_da_ordem: ordem padrão do tipo
```

| Chave | visivel | Origem e nota |
|---|---|---|
| hero | sim | IA e humano |
| numeros | sim | dado |
| sobre | sim | IA |
| para_quem | sim | IA |
| diferenciais | sim se o banco trouxer | dado, sem reescrita |
| matriz | sim | dado |
| docentes | sim | dado |
| certificacao | **nao** | oculta até a regulação; sem frase. A frase "tem reconhecimento pelo Ministério da Educação (MEC)" da ficha não entra |
| video | nao | humano |
| depoimentos | nao | humano: sem depoimento autorizado em mãos |
| investimento | sim | dado e IA |
| local_e_datas | **só depois da conferência** | dado, obrigatória. O CEP da ficha difere do das outras páginas de São Paulo (OU13): conferir antes de publicar |
| parceiros | nao | dado: bloco vazio na ficha [CONFIRMAR] |
| faq | sim | dado e IA |
| formulario | sim | dado e IA |
| cta_final | sim | IA |

### 4.4 Texto da IA

**hero**

- titulo (61 caracteres): Pós-graduação em Patologia Clínica: do pré-analítico ao laudo
- subtitulo (133 caracteres): O laboratório clínico veterinário: correlação clínico-laboratorial, prática presencial e como estruturar e administrar um laboratório.

**sobre**

> O laboratório clínico veterinário do pré-analítico ao laudo: correlação clínico-laboratorial, prática presencial e como estruturar e administrar um laboratório. A Faculdade Ufape oferece a pós-graduação em patologia clínica veterinária em formato semipresencial, com foco no laboratório clínico.
>
> **Um objetivo escrito para o laboratório.** Capacitar a médica e o médico veterinário a trabalhar em laboratórios clínicos, com correlação clínico-laboratorial, conhecimento de equipamentos e metodologias, técnicas de coleta e a estrutura e a administração de um laboratório.
>
> **O laboratório inteiro, fase por fase.** Materiais biológicos e erros pré-analíticos, analíticos e pós-analíticos; hemograma e sua automação; hemostasia; hemoparasitoses; avaliação bioquímica, função renal e urinálise; eletrólitos e hemogasometria; distúrbios endócrinos; exame coproparasitológico; citologia; líquidos cavitários e líquor; testes imunológicos e PCR; microbiologia; controle de qualidade e biossegurança no laboratório clínico veterinário.
>
> **Prática presencial com laudo.** Os módulos presenciais trazem automação e prática de hemograma, hemoparasitoses em hematoscopia, mielograma, hemocomponentes e transfusão, prática de bioquímica e urina, coleta e confecção de lâminas e técnicas básicas de microbiologia; a elaboração de laudos aparece ao longo do cronograma. As aulas presenciais não são transmitidas.

**para_quem**

- Médicas e médicos veterinários interessados em laboratório clínico.
- Quem trabalha ou quer trabalhar em laboratório clínico veterinário.
- Quem quer estruturar e administrar um laboratório, com controle de qualidade e biossegurança.
- Quem quer prática presencial de hemograma, bioquímica e urina.

**investimento (frase de apoio, sem valor)**

> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.

**faq (perguntas da IA)**

> **Serve para quem é clínico ou só para quem trabalha em laboratório?**
> O público da turma são médicas e médicos veterinários. O foco é o laboratório clínico, e a correlação clínico-laboratorial atravessa o curso: do pedido do exame à leitura do laudo.
>
> **Patologia clínica ou citopatologia: qual eu faço?**
> A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes. A [Pós-graduação em Citopatologia Veterinária](link para a página da turma 333) é centrada na leitura de lâminas: células e tecidos ao microscópio, com discussão de casos. A escolha depende do trabalho que você quer fazer na rotina.
>
> **Tem prática de verdade ou é tudo online?**
> A teoria é online e há módulos presenciais de prática: automação e prática de hemograma, bioquímica e urina, mielograma, coleta e confecção de lâminas e microbiologia. Essas aulas não são transmitidas.
>
> **O curso ensina a montar e administrar um laboratório?**
> Estruturar e administrar um laboratório está no objetivo do curso, junto com controle de qualidade, biossegurança e as boas práticas de laboratório em análises clínicas.
>
> **Quanto vou pagar no total?**
> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.
>
> **E se a turma não fechar?**
> A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados.

- **Pergunta-ponte (seção 5 da F2):** o texto é idêntico ao da página de 333; só muda o link (aqui, o nome "Pós-graduação em Citopatologia Veterinária" leva à página de 333). Sem comparação de valor, duração, carga, prática ou corpo docente, e sem dizer qual é melhor.
- **Reembolso em 68615:** a F2 limita a frase a 657, 289 e 333, mas a ficha de 68615 traz o mesmo texto de reembolso. Incluída aqui por ter fonte na ficha [CONFIRMAR com o qa e a secretaria]; o aviso de passagem e hotel que a ficha não traz vem da regra da linha.
- **Recorte de perfil** da primeira pergunta [CONFIRMAR NO CATÁLOGO]: a ficha diz só "Médicos Veterinários".
- **Item de dado da turma, não escrito pela squad (OU14):** "Posso entrar depois que a turma começar?", com a regra e a data do 3º módulo. Modelo: seção 7.1.

**formulario**

- botao: Quero me inscrever
- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade.

**cta_final**

- titulo: Veja o cronograma do laboratório clínico, do pré-analítico ao laudo.
- botao: Quero me inscrever
- apoio (opcional): Cronograma, quem ensina e condições estão nesta página. Em dúvida entre patologia clínica e citopatologia? O time explica a diferença.

### 4.5 Travas aplicadas em 68615

- Sem "reconhecimento pelo Ministério da Educação", sem "referência nacional em educação" e sem o bloco de prova de bolsa (decisão 14).
- Citologia aparece só como parte do curso, nunca como foco. Sem hematologia nem hemograma como foco (é da página de Hematologia, onda 1) e sem histopatologia, anatomia patológica ou necropsia.
- Sem a palavra "garante" da ficha ("o curso garante ... simulações de habilidades").

### 4.6 OB1: o que corrigir na página de 68615 que está no ar hoje (ficha de 26/10/2026)

1. Frase "Este curso de pós-graduação tem reconhecimento pelo Ministério da Educação (MEC) o que comprova a qualidade do ensino oferecido pela instituição que é referência nacional em educação". Retirar inteira: ato regulatório não confirmado na ficha, nexo de "comprova a qualidade" e superlativo sem fonte.
2. Frase "CERTIFICADO PELO MEC" (bloco de certificação). Remover; a seção fica oculta até o texto da regulação.
3. "Turma mínima de 20 alunos". Trocar para 15 (decisão 11, A12) ou deixar só o aviso sem número.
4. Bloco "PROVA DE BOLSA: Tem interesse em prestar a prova de bolsa? Clique aqui". Retirar (decisão 14).
5. Aviso de passagem e hotel ausente: a ficha de 68615 não traz a recomendação de comprar passagem e hotel só com a turma confirmada, que as outras páginas trazem. Incluir (regra da linha: ser transparente sobre a turma mínima).
6. CEP diferente do das demais páginas de São Paulo (01428-001 na ficha, 01407-100 nas outras): a Ufape confirma o correto (OU13).
7. "O curso garante além de embasamento teórico simulações de habilidades": retirar o verbo "garante".
8. Regra do 3º módulo: incluir como dado da turma, com a data (decisão 18, OU14, OU6).
9. Erros de digitação no cronograma ("regulameno", "sedmentoscopia"): corrigir no dado.
10. Bloco "Documentos para matrícula (MEC e UFAPE)" cita o órgão: a regulação diz se o título fica [CONFIRMAR].

---

## 5. Seção 333: Pós-graduação em Citopatologia Veterinária

### 5.1 Cabeçalho (template)

```
tipo: pos
curso: pos-graduacao-em-citopatologia-veterinaria [SUPOSIÇÃO: slug derivado do nome do arquivo da ficha; o catálogo escreve "Pós Graduação" e o padrão de nome da linha é "Pós-graduação em"]
turma_ou_edicao: [CONFIRMAR NO CATÁLOGO] (slug da turma do código 333)
palavra_chave_principal: pós-graduação em citopatologia veterinária
```

### 5.2 SEO (IA)

A cargo do F4. Sem a palavra "coordenação" em nenhum campo (OU12).

### 5.3 Ordem e visibilidade

```
ordem: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final
motivo_da_ordem: ordem padrão do tipo
```

| Chave | visivel | Origem e nota |
|---|---|---|
| hero | sim | IA e humano |
| numeros | sim | dado |
| sobre | sim | IA |
| para_quem | sim | IA |
| diferenciais | sim se o banco trouxer | dado, sem reescrita |
| matriz | sim | dado, com os módulos presenciais como estão na ficha |
| docentes | **sim, com ressalva** | dado. Sem o rótulo "Coordenação: UFAPE" (OU12). Se a plataforma não conseguir esconder o rótulo, a chave fica oculta até a Ufape responder |
| certificacao | **nao** | oculta até a regulação; sem frase |
| video | nao | humano |
| depoimentos | nao | humano: sem depoimento autorizado em mãos |
| investimento | sim | dado e IA |
| local_e_datas | sim | dado, obrigatória. A data do módulo presencial inicial cai em Sábado de Aleluia e Páscoa (OU17): a Ufape confirma |
| parceiros | nao | dado: bloco vazio na ficha [CONFIRMAR] |
| faq | sim | dado e IA |
| formulario | sim | dado e IA |
| cta_final | sim | IA |

### 5.4 Texto da IA

**hero**

- titulo (62 caracteres): Pós-graduação em Citopatologia Veterinária: leitura de lâminas
- subtitulo (139 caracteres): Citopatologia veterinária centrada na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema.

**sobre**

> Citopatologia veterinária centrada na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema. A Faculdade Ufape oferece a pós-graduação em citopatologia veterinária em formato semipresencial.
>
> **Começa pelo material.** O curso abre com um módulo presencial de manejo de materiais biológicos (coleta, armazenamento, acondicionamento e transporte de amostras, técnicas de coloração e microscopia) e segue para citologia básica, critérios de malignidade e gestão da qualidade aplicada à citopatologia. **Lesão por lesão, sistema por sistema.** Processos inflamatórios e enfermidades infecciosas, derrames cavitários, líquidos biológicos, trato respiratório, neoplasias de células redondas, sangue periférico, neoplasias glandulares e mesenquimais, trato gastrointestinal, aparelho urinário, citopatologia reprodutiva, oftalmológica e auditiva, com atualizações em imunocitopatologia, automação citopatológica e citoinclusão.
>
> **Leitura de lâminas no presencial.** O cronograma tem módulos presenciais de leitura de lâminas e discussão de casos, chamados de experiências práticas citopatológicas. Os demais módulos presenciais tratam de manejo do material, de citologia esplênica e linfoma e de mielograma. As aulas presenciais não são transmitidas.

**para_quem**

- Médicas e médicos veterinários interessados em citopatologia.
- Quem quer treinar leitura de lâminas e discutir casos ao microscópio.
- Quem prefere partir do manejo do material, da coloração e da microscopia antes de entrar nos sistemas.

**investimento (frase de apoio, sem valor)**

> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.

**faq (perguntas da IA)**

> **Citopatologia ou patologia clínica: qual eu faço?**
> A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes. A Pós-graduação em Citopatologia Veterinária é centrada na leitura de lâminas: células e tecidos ao microscópio, com discussão de casos. A escolha depende do trabalho que você quer fazer na rotina.
>
> **Vou treinar leitura de lâmina de verdade?**
> Sim. O cronograma tem módulos presenciais de leitura de lâminas de citopatologia e discussão de casos. Outros módulos presenciais trabalham o manejo do material, a citologia esplênica e o linfoma e o mielograma.
>
> **Preciso já trabalhar em laboratório para acompanhar?**
> O público da turma são médicas e médicos veterinários. O curso abre com o manejo do material, a coloração e a microscopia, e passa pela citologia básica antes de entrar nos sistemas.
>
> **Vou ter de largar a rotina?**
> A teoria é online e o presencial fica nos módulos de prática, com as datas publicadas no cronograma antes de começar. Dá para planejar a agenda da clínica com antecedência.
>
> **Quanto vou pagar no total?**
> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.
>
> **E se a turma não fechar?**
> A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados.

- **Pergunta-ponte (seção 5 da F2):** texto idêntico ao da página de 68615; aqui, o nome "Pós-graduação em Patologia Clínica" leva à página de 68615. No arquivo de entrega, o link vai no nome, como na seção 4.4.
- **Sem item de dado sobre entrada depois do início:** bloqueado até OU3 (reposição do módulo presencial inicial). Sem OU3, nenhuma pergunta, resposta ou chamada trata de entrar depois do início. Resposta do time: "Vou confirmar com a secretaria como fica e te retorno."
- **Fora da página:** "Quem ensina?". Sem texto: a chave `docentes` mostra o dado da ficha (OU12). Nunca "coordenação".
- **Recorte de perfil e microscópio próprio** na pergunta de laboratório [CONFIRMAR NO CATÁLOGO].

**formulario**

- botao: Quero me inscrever
- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade.

**cta_final**

- titulo: Veja o cronograma de leitura de lâminas, sistema por sistema.
- botao: Quero me inscrever
- apoio (opcional): Cronograma e condições estão nesta página. Em dúvida entre citopatologia e patologia clínica? O time explica a diferença.

### 5.5 Travas aplicadas em 333

- OU12: nenhuma palavra sobre coordenação nem sobre quem ensina.
- C1 e C2: o texto não soma os módulos presenciais e não trata todos como de leitura de lâminas. Diz "módulos presenciais de leitura de lâminas e discussão de casos" e nomeia os outros presenciais pelo tema (manejo do material, citologia esplênica e linfoma, mielograma). A contagem fica fora da página: na ficha são 6 presenciais, dos quais 3 de leitura de lâminas (módulos 5, 10 e 20).
- OU3: nada sobre entrada depois do início.
- Ficam fora: "oportunidade única", "contribui para o avanço da ciência", "o que há de mais recente" e "oportunidade valiosa para quem busca se destacar" (texto da ficha). O ticket menor que o de 68615 não entra em texto nenhum.

### 5.6 OB1: o que corrigir na página de 333 que está no ar hoje (ficha de 26/10/2026)

1. Frase "CERTIFICADO PELO MEC". Remover; a seção fica oculta até o texto da regulação.
2. "Turma mínima de 20 alunos". Trocar para 15 (decisão 11, A12) ou deixar só o aviso sem número.
3. Coordenação "UFAPE" e uma só professora listada: a Ufape informa a coordenação e o corpo docente reais (OU12). Até lá, `docentes` sem o rótulo de coordenação.
4. Superlativos e promessas do texto de apresentação: "oportunidade única", "eleva o nível de excelência", "contribui para o avanço da ciência", "o que há de mais recente nas descobertas científicas", "oportunidade valiosa para quem busca se destacar". Retirar ou documentar.
5. Módulo 1 presencial sem reposição conhecida: a Ufape diz como o aluno repõe o módulo presencial inicial se entrar depois do início (OU3) e confirma as datas (Sábado de Aleluia e Páscoa, OU17). Sem OU3, nenhuma peça fala de entrar depois do início.
6. Regra do 3º módulo: incluir como dado da turma, com a data, só depois de OU3 (decisão 18, OU14, OU6).
7. Erros de digitação no cronograma ("masculine", "Experiência práticas citopatológicas"): corrigir no dado.
8. Nome padrão: "Pós-graduação em Citopatologia Veterinária" (a ficha traz "Pós Graduação").
9. Bloco "Documentos para matrícula (MEC e UFAPE)" cita o órgão: a regulação diz se o título fica [CONFIRMAR].

---

## 6. Pedido OB1 para a aprovação humana (as 5 páginas no ar hoje)

Mesmo pedido do plano (seção 9, OB1), com as listas por turma nas seções 1.6, 2.6, 3.6, 4.6 e 5.6.

| Campo | Conteúdo |
|---|---|
| O que | Publicar as 5 páginas deste arquivo (depois do qa e do F4 e F5) e corrigir no site o que as listas por turma apontam. Os itens comuns às 5: frase "CERTIFICADO PELO MEC"; turma mínima de 20; regra do 3º módulo ausente; bloco de prova de bolsa em 289 e 68615; frase de reconhecimento pelo órgão em 68615; convite da prova de Especialista em 657 |
| Por quê | Nenhuma das 5 páginas passa hoje em conformidade-educacional, e a mídia de 07/12 aponta para elas. Página fora da regra não conta como entregue |
| Quanto | Sem custo de mídia. Custo de quem edita o site: [CONFIRMAR] |
| Efeito esperado | A página entrega o que a peça promete e passa nas auditorias de conformidade e de conversão |
| Como desfazer | Voltar à versão anterior da página, exportada antes da troca |
| Prazo | 03/12/2026 (plano, seção 7.2); nenhum envio nem publicação sai para página com frase ligada ao órgão regulador antes da troca, salvo decisão humana registrada (regra 13 do plano) |
| Quem aprova | A pessoa do marketing; itens de certificação e de ato regulatório passam também pela regulação [CONFIRMAR quem] |
| Dependências | U10 (657), OU3 e OU12 (333), OU10 e OU11 (341), OU13 (68615), OU14, OU6 e OU17 |

Nada é publicado, enviado ou pago por este arquivo.

---

## 7. Modelos e checklists

### 7.1 Modelo do item de dado "Posso entrar depois que a turma começar?" (para o editor, não é texto da IA)

Não passa pelo validador do texto da IA, porque é dado da turma (OU14). Quem escreve é o editor, com a data do banco. Redação proposta, para a aprovação humana [SUPOSIÇÃO]:

> A Ufape aceita matrícula até o 3º módulo do curso, que nesta turma começa em [data do 3º módulo, do catálogo]. O time explica como ficam os módulos já dados.

Regras: nunca como título, chamada, contador ou "corra" (regra 7 do plano); a frase de reposição só entra com OU3 resolvida; em 333 o item não existe até OU3; em 341, a frase só fecha com OU11. As datas do 3º módulo, pela ficha: 657, 22 e 23/05/2027; 341, 01 e 02/05/2027; 289, 15 e 16/05/2027; 68615, 22 e 23/05/2027; 333, 29 e 30/05/2027.

### 7.2 Checklist de design e rastreamento (construção, por humano ou plataforma)

Design e conversão (auditorias/08-conversao.md):
- [ ] Topo passa no teste dos 5 segundos no celular: título com o nome do curso, subtítulo, botão "Quero me inscrever" visível sem rolar.
- [ ] Uma chamada principal por página ("Quero me inscrever", rola até o formulário); WhatsApp é chamada secundária, com botão fixo no celular e o número da praça vindo do dado (Goiânia em 289).
- [ ] Formulário curto: nome, WhatsApp e e-mail, mais a pergunta de interesse se necessária. Nada além do que o contato precisa.
- [ ] Finalidade do uso dos dados e link da política de privacidade ao lado do botão (conformidade-educacional); F5 refina.
- [ ] Dados do curso conferidos com contexto/catalogo-de-cursos.md: nome, modalidade, carga horária, preço, parcelas, matrícula, datas e local aparecem nas chaves de dado, nunca digitados no texto.
- [ ] `certificacao`, `depoimentos` e `parceiros` ocultas; `video` só com vídeo aprovado; `para_quem` de 657 oculta.
- [ ] Imagens do acervo, sem foto de docente sem autorização registrada (decisões 8 e 10) e sem pessoa pública.
- [ ] Página carrega rápido no celular e mostra os contatos oficiais da Ufape.

Rastreamento:
- [ ] GA4: evento de lead no envio do formulário (por exemplo `generate_lead`) e evento de clique no WhatsApp (por exemplo `click_whatsapp`); evento de inscrição quando o candidato chega ao pagamento da matrícula (nome do evento a combinar com quem monta o GA4) [SUPOSIÇÃO: nomes sugeridos].
- [ ] Pixel da Meta: evento de lead no envio e evento de inscrição na etapa de matrícula.
- [ ] Tag do Google Ads: conversão de lead e de inscrição, com a mesma definição do GA4, sem duplicar contagem.
- [ ] UTM preservadas do clique ao formulário e ao CRM (regra 12 do plano): pago `pos_<código>-<área curta>_<plataforma>_...`; CRM `utm_medium=crm`, `pos_<código>_<AAAAMM>`; orgânico `utm_medium=organic_social`. O lead chega ao CRM com a UTM.
- [ ] Teste de ponta a ponta antes da subida de 07/12 (conferência de 04/12): destino, UTM, política de privacidade e lead no CRM.
- [ ] Conversão de inscrição medida separada da matrícula paga (decisão 16: inscrição paga e depois primeira mensalidade paga), por turma, só números somados.

---

## 8. Autochecagem (template, auditorias/08-conversao.md e auditorias/conformidade-educacional.md)

| Item | Situação |
|---|---|
| Todas as seções obrigatórias do tipo presentes (hero, sobre, investimento, local_e_datas, formulario) | Sim, nas 5 páginas |
| Nenhuma chave fora do catálogo do tipo pos | Sim; só chaves comuns e as do tipo pos |
| Nenhum número, preço, data, vaga, local ou nome de docente no texto da IA | Sim nos blocos da página (sem algarismo, ordinal ou numeral romano); "um", "uma" e "uma das partes" aparecem como artigo nos textos da F2, e o qa confirma se o validador os ignora |
| Seção de certificação oculta, sem frase | Sim, nas 5 |
| FAQ sem bolsa e com a pergunta-ponte 68615 x 333 | Sim; a ponte está em 68615 e em 333, com o mesmo texto |
| 341 sem promoção, sem local da prática, sem "hospital veterinário" | Sim |
| 333 sem "coordenação", sem tratar todos os presenciais como de leitura de lâminas, sem pós-início | Sim |
| 657 sem pré-requisito, sem o convite da prova de Especialista, sem o item de resultado clínico | Sim; `para_quem` oculta; `objetivos` fora da ordem |
| Regra do 3º módulo só como dado da turma, nunca como urgência | Sim (modelo na seção 7.1) |
| 289 sem a cidade no texto (CP1) | Sim |
| Sem promessa de emprego, salário, renda, aprovação ou resultado clínico | Sim |
| Sem superlativo da ficha | Sim ("referência nacional", "oportunidade única", "excelência", "de ponta" fora) |
| Nome "Pós-graduação em <área>" | Sim |
| Uma chamada principal por página | Sim |
| Objeções respondidas na página | Sim, no `faq`, com as respostas da F2 |
| Provas reais e autorizadas | Sim; só o conteúdo da ficha; nenhum depoimento, nota ou número externo |
| Formulário com finalidade e política de privacidade | Pendente externo: F5 e conferência em 04/12 |
| Página de destino entrega o que a peça promete | Pendente externo até OB1 |
| Nenhum dado pessoal | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; a busca final é do orquestrador |

**Próximo passo da cadeia /pagina-de-curso:** F4 seo-on-page (16/11), depois F5 otimizador-de-cta (17/11) e o qa em 19/11. Depois da publicação e com dados reais de visita, lead e inscrição, o próximo agente é **analise-cro**.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início, preço e status "aberto" das 5 turmas: contexto/catalogo-de-cursos.md, seção 2. Nenhum desses valores está no texto das páginas; entram como dado.
- 657: transição da anestesia de protocolo para a de precisão; objetivo de conduzir pacientes de risco moderado a alto e antecipar crises; módulos presenciais de bloqueios locorregionais, hemodinâmica avançada e ventilação mecânica, reanimação com avaliação viscoelástica, TIVA e TCI, cirurgia cardiotorácica e pets não convencionais; aulas práticas não transmitidas; público-alvo "exclusiva para médicos veterinários anestesistas já atuantes"; convite da prova de Especialista; "Prova cobrada separadamente": ficha de 657.
- 341: temas por sistema, de abordagem clínica a odontologia equina; treinamentos práticos e demonstrativos na maioria dos temas; teoria online e práticas presenciais aos fins de semana; estágio obrigatório e atividades complementares; módulo de medicina equina baseada em evidências; avaliação com provas práticas, seminários e trabalho de conclusão opcional; promoção com texto cortado; segundo local em Indaiatuba; módulo 3 "ONLINE PRESENCIAL"; "descontos e bolsas de estudo"; texto de reembolso truncado: ficha de 341.
- 289: módulos presenciais de prática hands-on de ecocardiograma; laudos ecocardiográficos; percurso da anatomia às emergências; teoria acompanhada a distância e só módulos práticos presenciais; bloco "PROVA DE BOLSA"; cardiologia equina e de pets não convencionais no cronograma: ficha de 289.
- 68615: objetivo de trabalhar em laboratórios clínicos, correlação clínico-laboratorial, estruturar e administrar um laboratório; módulos de pré-analítico a controle de qualidade e biossegurança; módulos presenciais de hemograma, hemoparasitoses, mielograma, hemocomponentes, bioquímica e urina, citologia com confecção de lâminas, líquidos cavitários e microbiologia; frase de reconhecimento pelo órgão e "referência nacional"; CEP diferente; ficha sem o aviso de passagem e hotel; ficha com o texto de reembolso: ficha de 68615.
- 333: módulos presenciais 1, 5, 10, 12, 13 e 20, dos quais 5, 10 e 20 de leitura de lâminas e discussão de casos; módulo inicial presencial de manejo de materiais, coloração e microscopia; coordenação "UFAPE" e uma professora listada: ficha de 333; contagem confirmada pelas correções C1 e C2 do plano em versão 2.
- Palavras principais, divisão de vocabulário 68615 x 333, regra de âncora cruzada e CP1: F1, seções 1, 4, 5 a 9 e 12.
- Mensagens centrais, provas, respostas às objeções, frase-ponte e chamadas: F2, seções 1 a 7.
- Regras do texto da IA, chaves do tipo pos e ordem padrão: templates/pagina-da-turma.md.
- Decisões 8, 10 e 11 (docentes autorizados, turma mínima de 15), 14 (sem bolsa), 16 (funil de inscrição e matrícula) e 18 (matrícula até o 3º módulo): docs/execucao-2026-10-26.md.
- Datas do 3º módulo e prazo de 03/12 para publicar: plano do CMO, seções 1, 7.2 e 9.
- Travas U10, OU3, OU6, OU10, OU11, OU12, OU13, OU14, OU17, CP1, A12 e A13: plano do CMO, seções 8, 9 e 10, e F1 e F2.
- Texto de certificação aprovado ainda não existe: contexto/catalogo-de-cursos.md ("Como usar") e contexto/pos-graduacao.md.

## [SUPOSIÇÃO]

- Todas as perguntas do `faq` na voz do candidato: hipóteses da persona e das objeções da F2 (H-A1.1, H-A1.4, H-A2.3, H-A14.1, H-A11.3, Q11.1, Q11.2), sem voz real.
- Os slugs de curso (derivados do nome do arquivo da ficha, no padrão "pos-graduacao-em-").
- A divisão da mensagem central entre `hero.titulo` e `hero.subtitulo` (limites de 70 e 160 caracteres do template), com a frase inteira abrindo o `sobre`; as contagens de caracteres foram feitas à mão e o qa confere.
- A frase "A Faculdade Ufape oferece a pós-graduação em <área> veterinária em formato semipresencial" que abre o `sobre` de cada turma, para levar a palavra principal e "veterinária" ao corpo (F1); "semipresencial" é permitido pela F1 mesmo sendo dado.
- A expressão "o médico veterinário de equinos" em 341, herdada como variação de corpo da F1 (341-K2, [SUPOSIÇÃO] da F1).
- Os itens de `para_quem` além de "Médicas e médicos veterinários interessados em <área>", que derivam das objeções da F2 e da persona (a ficha só diz "Médicos Veterinários"). Escritos como interesse, nunca como pré-requisito.
- A frase de reembolso ("os valores de inscrição pagos podem ser reembolsados") em 657, 289, 68615 e 333: redação deste agente a partir do texto da ficha ("só serão devidos caso a turma não seja confirmada").
- A frase "ao lado do cronograma de cada módulo presencial" da F2 (657) supõe esse arranjo na tela; a ordem padrão põe `matriz` antes de `investimento`, e o editor confere ou troca.
- Texto do botão "Quero me inscrever" e da frase de apoio do formulário; refinados pelo F5.
- Modelo do item de dado da regra do 3º módulo (seção 7.1) e nomes de eventos do GA4 e do Pixel.
- `diferenciais`, `parceiros` e `docentes` como "visíveis só se o dado vier correto", sem o texto do banco à vista.
- Que o validador do template ignora "um" e "uma" como artigo.

## [CONFIRMAR]

- **U10:** pré-requisito de 657 (`para_quem` oculta; nenhuma frase de quem pode entrar).
- **OU3:** reposição do módulo presencial inicial de 333 e de módulos perdidos em geral (bloqueia o item de dado de 333 e qualquer peça de 333 depois do início).
- **OU6:** se "até o 3º módulo" inclui o dia do módulo ou termina na véspera (redação final do item de dado).
- **OU10:** regra completa da promoção de 341 ou retirada; também o texto cortado no campo de preço do catálogo.
- **OU11:** segundo local de 341 (Indaiatuba), "hospital veterinário" da ficha e formato do módulo 3.
- **OU12:** coordenação e corpo docente de 333.
- **OU13:** CEP de 68615.
- **OU14:** se a regra do 3º módulo pode entrar como dado da turma no `faq`.
- **OU17:** datas do módulo inicial de 333 (Sábado de Aleluia e Páscoa) e do módulo 3 de 341 (feriado nacional).
- **CP1:** cidade em `titulo_seo` e `resposta_citavel` (pesa em 289).
- **A12:** correção da turma mínima de 20 para 15 nas 5 páginas, para o número poder aparecer como dado.
- **Certificação:** texto oficial da regulação; até lá a seção fica oculta.
- **Slug de turma** das 5 turmas e slugs de curso (o catálogo não traz).
- **[CONFIRMAR NO CATÁLOGO]:** recorte de perfil e nível de entrada de 289, 68615 e 333; necessidade de microscópio próprio em 333; se 289 pode ser descrita como "de cães e gatos" (a ficha também traz cardiologia equina e de pets não convencionais).
- **Reembolso:** redação final por turma (341 truncado e contraditório) e se a frase vale também para 68615, que a F2 não incluíra.
- **Prova de recuperação de 657 cobrada separadamente:** valor ou regra, para o preço mostrar a condição completa.
- **Guia de decisão A2 (289):** publicado, com link, antes de a resposta citar o guia.
- **Parceiros:** os blocos "Parceiros e patrocinadores" das fichas estão vazios.
- **Revisão docente:** conferência técnica de provas e respostas de 657, 341, 289, 68615 e 333 antes da publicação.
- **Quem edita o site** e quem aprova a regulação para os itens de certificação e de ato regulatório (A9 do plano); custo de edição do site.
- **U11:** valor da inscrição; até a resposta nenhuma peça cita valor de inscrição.
- **Voz real:** conversas anonimizadas do WhatsApp de vendas para trocar as falas [SUPOSIÇÃO] por falas de candidatos.
