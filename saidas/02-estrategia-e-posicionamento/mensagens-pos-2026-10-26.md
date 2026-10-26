# Casa de mensagens da Pós-graduação por área de especialidade (A1 a A14)

- **Agente:** mensagens (departamento 02, Estratégia e Posicionamento), etapa 2.2 da camada 2
- **Linha:** pos
- **Data:** 26/10/2026
- **Escopo:** as 30 turmas de Pós do recorte (seção 2.3 do plano do cmo), agrupadas nas áreas A1 a A14. A14 vai por curso. As provas de bolsa ficam fora desta rodada (decisão 14 da Ufape): aparecem só como fato do catálogo, sem peça, sem chamada e sem regra de bolsa. A13 (Medicina felina) não tem turma de Pós aberta no recorte e recebe só uma nota.
- **Modelo:** templates/casa-de-mensagens.md, com o método do agente (mensagem central, 3 pilares, objeções, palavras) e os campos pedidos pelo plano do cmo para a camada 2 (público e momento de carreira, promessa, 3 pilares de prova, 3 objeções, palavras, títulos e chamadas, turmas da área).
- **Status:** rascunho para o qa-de-marketing (auditorias/02-estrategia-e-posicionamento.md e auditorias/conformidade-educacional.md) e para a aprovação da pessoa do marketing. Nada foi publicado, enviado ou pago.
- **Entradas lidas:**
  - .claude/agents/mensagens.md; templates/casa-de-mensagens.md
  - CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 14)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 2.3, 3, 4 e 12, inclusive D6, D7 e D13)
  - contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (seção 2)
  - fichas das 30 turmas em contexto/cursos/pos/: 657, 68609, 359, 289, 698, 68636, 352, 68635, 68623, 68632, 578, 662, 366, 68604, 68629, 68606, 68617, 68610, 707, 68628, 68608, 68615, 333, 68616, 679, 382, 699, 341, 60, 719 (dados principais, texto de apresentação, cronograma, condições e lista de docentes)
  - saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md (1.7)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md (1.8)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md (seção 6, palavras)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (2.1)
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md
  - saidas/01-inteligencia-de-mercado/insights-de-alunos-pos-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/mensagens-eventos-2026-10-26.md (só como referência de formato)
- Não abri faculdade.ufape.com.br. Nenhuma busca na web.
- **Dados pessoais:** nenhum de aluno, candidato ou lead. Docentes, coordenadores e convidados aparecem só com nome e titulação exatamente como estão na ficha (grafia e caixa da ficha), com autorização de imagem e citação registrada (decisões 8 e 10 da Ufape, 26/10/2026).

---

## 0. Regras desta casa (valem para todas as áreas)

1. **Fonte.** Nome, campus, modalidade, carga horária, turma, preço e condições vêm do catálogo (seção 2). Datas de início: a do catálogo, que segue a planilha (decisão 12). Módulos, docentes e condições da página (turma mínima, passagem, reembolso) vêm da ficha e levam [CONFIRMAR NO CATÁLOGO] quando a peça final depender deles.
2. **Voz do candidato.** Não há nenhuma citação real de candidato ou aluno (insights-de-alunos-pos e pesquisa-de-persona-pos). Toda frase "nas palavras do candidato" desta casa é hipótese das etapas 1.3 e 1.4, marcada [SUPOSIÇÃO]. Quando chegarem conversas anonimizadas do WhatsApp de vendas, estas frases devem ser trocadas.
3. **Preço.** Peça com preço usa o texto-padrão da estrategia-de-oferta-pos (seção 2.1), com a turma mínima corrigida para 15 (decisão 11): "[N]x de R$ [parcela] no cartão ou boleto (total de R$ [total]), mais matrícula de R$ [matrícula]. A 1ª mensalidade é paga até 30 dias antes do início. Turma mínima de 15 alunos: compre passagem e hotel só depois de a turma ser confirmada." Versão curta: "[N]x de R$ [parcela] no cartão ou boleto. Total de R$ [total] + matrícula de R$ [matrícula]." Sem as condições completas, a peça sai sem preço.
4. **1ª mensalidade vencida.** Em 707, 68604, 68606 e, a partir de 29/10/2026, 68610, 68608 e 698 (todas com início até 28/11/2026), a frase da 1ª mensalidade sai e o texto termina em "Fale com o time para saber como entrar na turma" [SUPOSIÇÃO de texto, regra 3 da estrategia-de-oferta-pos, a validar com o time de vendas].
5. **Descontos.** Nenhum desconto entra em peça: 341 (20% com regra cortada), 359 (12% para os 10 primeiros), 352 (10% para os 10 primeiros), aluno e ex-aluno (regra a preencher), crédito ou combo de curso livre (D7 do cmo). "10 primeiros" também não vira escassez.
6. **Certificação.** Nenhuma peça afirma certificação, reconhecimento ou selo do MEC, nem "dupla certificação" (68635 e 68623), nem "certificado de especialização", até a regulação aprovar o texto oficial. Pergunta sobre certificado ou título vai para a secretaria.
7. **Urgência.** Sem "últimas vagas", "vagas limitadas", "corra", "garanta já", contador. A data de início e a turma mínima são os únicos fatos de tempo.
8. **Nome.** Sempre "Pós-graduação em <área>" em título e peça, mesmo quando o catálogo grafa "Pós Graduação" (706, 68629, 341, 333) ou "Pós-Graduação" (719).
9. **Provas de bolsa.** Esta rodada não produz peça de prova (decisão 14). Cada área cita só que existe prova de bolsa no catálogo, com o código, como fato. Nenhuma linha desta casa liga prova a turma, cita bolsas, percentuais, nota de corte ou inscrição.
10. **Turmas que não entram.** Turmas em "verificar", "sem venda" ou "encerrado" (por exemplo 68605, 68607, 650, 666, 663, 677, 701, 586, 554, 68612, 670) não recebem chamada de compra e não aparecem nos exemplos.

---

## 1. Base comum da linha (o que todas as áreas herdam)

**Mensagem guarda-chuva (posicionamento-pos, seção 2.1, ajustada pela regra 5 da estrategia-de-oferta-pos):** Especialize-se sem parar de atender: prática presencial no cronograma e condições claras antes da matrícula.

**Versão de elevador da linha (três frases):** A Pós-graduação da Faculdade UFAPE junta teoria online e módulos práticos presenciais em fins de semana marcados no cronograma de cada turma. Antes da matrícula você vê quem ensina, o que se pratica em cada módulo presencial, quanto paga (parcelas, total e matrícula) e qual é a turma mínima (15 alunos). Há turmas em São Paulo e em Goiânia, com início entre outubro de 2026 e maio de 2027.

**Os três pilares da linha (cada área troca a prova pela da sua ficha):**

| Pilar | Afirmação | Prova (fonte) | Palavras do candidato [SUPOSIÇÃO, H-T e P1] |
|---|---|---|---|
| 1. Prática no calendário | A prática é presencial, com data e tema no cronograma | Cronograma de cada ficha; "Aulas Presenciais e Práticas não serão transmitidas" (fichas) | "Quero praticar de verdade, não só assistir." |
| 2. Quem ensina, com nome | O corpo docente está na página, com nome e titulação | Lista de docentes de cada ficha; autorização de imagem e citação (decisões 8 e 10) | "Quero saber com quem eu vou aprender." |
| 3. Condições claras | Parcelas, total, matrícula e turma mínima antes de pagar | Catálogo (preço); turma mínima de 15 (decisão 11); orientação de passagem (fichas) | "Pago antes de saber se a turma fecha?" |

**As 3 objeções do contexto da linha e a resposta-base (cada área adapta):**

| Objeção [SUPOSIÇÃO do contexto] | Resposta-base, na linguagem do candidato | Limite |
|---|---|---|
| Investimento alto | "O valor está inteiro na página: parcelas, total e matrícula. Você decide com a conta fechada, sem letra miúda." Mostrar o texto-padrão da turma. | Nunca "cabe no bolso", "investimento que se paga", "ganhe mais", comparação de preço com concorrente, desconto sem regra |
| Tempo (um fim de semana por mês, cerca de 2 anos) | "É um fim de semana por mês, com as datas publicadas antes de começar. A teoria é online; o presencial é só nos módulos práticos." | Dizer quando há módulo de 3 dias (707, 68616, 60). Nunca "flexível", "no seu ritmo", "estude quando quiser". Reposição de módulo [CONFIRMAR] |
| Medo de a turma não fechar | "A turma abre com no mínimo 15 alunos. A orientação é comprar passagem e hotel só depois de a turma ser confirmada." | Data em que a turma é confirmada [CONFIRMAR]; reembolso só com o texto da ficha e o que entra em "valores de inscrição" [CONFIRMAR]. Nunca "turma garantida" ou "turma confirmada" sem confirmação |

**Variação por estágio de consciência (vale para todas as áreas; a área troca o exemplo de caso e o módulo):**

| Estágio | Ângulo | Exemplo de linha [SUPOSIÇÃO de texto] |
|---|---|---|
| Inconsciente | O caso da rotina | "Aquele caso de [área] que você encaminha toda semana." |
| Consciente do problema | Por que estudar a área a fundo | "Resolver [tema] pede raciocínio clínico e prática supervisionada, não só um vídeo." |
| Consciente da solução | Como é a Pós da Ufape | "Teoria online, módulos práticos presenciais com data no cronograma e [N] docentes com nome na página." |
| Pronto para se matricular | Condições e data | "Início em [data da planilha], [campus]. [Texto-padrão de preço]." |

**Palavras da linha (estrategia-de-marca-geral, seção 6):** usamos "Pós-graduação em <área>", semipresencial, módulo presencial, aula online, caso clínico, rotina, raciocínio clínico, turma mínima de 15 alunos, total, matrícula, médicas e médicos veterinários. Evitamos o que a regra 6 e a regra 7 da seção 0 proíbem, mais "o melhor", "a maior", "referência nacional", "única", "pioneira", "primeira do Brasil", "renomados", "maiores especialistas", "de ponta", "estrutura completa" sem lista, "Ufape Intercursos" como marca, "Pós em", "Pós Graduação", "Pós-Graduação".

---

## 2. A1. Anestesiologia e dor (turmas 657, 68609, 359)

**Público e momento de carreira.** Dois públicos na mesma área [SUPOSIÇÃO, persona 5.1]: (a) para 68609, a médica ou o médico veterinário que quer atuar na anestesiologia clínica (público da ficha: "Médicos Veterinários que querem atuar na anestesiologia veterinária clínica"), em geral clínico de 1 a 8 anos de formado, em Goiânia e entorno; (b) para 657 e 359, quem já é anestesista: 657 é "exclusiva para médicos veterinários anestesistas já atuantes" e 359 tem público "Médicos veterinários quais já possuem residência em Anestesiologia" (redação ambígua, H-A1.2 [CONFIRMAR]).

**Promessa central.** Da monitoração básica à anestesia de precisão: a trilha de anestesiologia da Ufape tem uma turma para cada momento, com a prática presencial marcada no cronograma.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 657: coordenação Dra. Mayara Travalini de Lima e Dr. Alessandro Martins; 17 professores listados, entre eles Prof. Stelio Pacca Loureiro Luna, Profa. Denise Fantoni, Prof. André Escobar (EUA), Profa. Marina Cayetano Evangelista (CANADÁ), Prof. Pablo Ezequiel Otero MV, PhD, DACVAA (ARGENTINA) e Prof. Francesco Staffieri (Itália). 68609: coordenação Dr. Alessandro Martins, Dr Rogério Viera Da Silva e Dra. Mayara Travalini de Lima; 14 professores listados, entre eles Profa. Denise Fantoni, Prof. Juan Carlos Duque e Prof. Stelio Pacca Loureiro Luna. 359: coordenação Dr. Alessandro Martins e Dra. Mayara Travalini de Lima; 11 professores listados, entre eles LV CertVA, DipECVAA, MRCVS. Luis Campoy (EUA), DVM, Dipl.ECVAA MRCVS. JAIME VISCASILLAS (ESPANHA) e DVM, MSc, DVSc. Flavio A. Freitag (CANADÁ) |
| Módulos | 68609 (26 módulos, 500 h): fisiologia, farmacologia, exames pré-operatórios, monitoração; módulo 5 presencial com prática hands-on de avaliação pré-anestésica, sedação e monitoração; módulo 8 presencial com intubação, indução e anestesia geral inalatória. 657 (18 módulos, 360 h): TIVA e TCI, locorregional avançada, hemodinâmica avançada, ventilação mecânica aplicada à anestesia, dor e analgesia em felinos; módulos presenciais de bloqueios locorregionais (prática guiada) e de hemodinâmica avançada e ventilação mecânica (prática aplicada). 359 (20 módulos, 360 h): técnicas locorregionais por região do corpo; prática com modelos anatômicos, sonoanatomia guiada por ultrassom, phantoms, eletroneuroestimuladores, fluoroscopia e pacientes vivos em aulas demonstrativas; aulas teóricas gravadas [CONFIRMAR NO CATÁLOGO] |
| Formato e campus | Semipresencial nas três. 68609 em Goiânia (endereço da ficha: "Ufape Goiânia"); 657 e 359 em São Paulo (sede da Av. 9 de Julho) |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Qual das pós de anestesia é para mim?" (H-A1.1) | "Depende de onde você está hoje. Se quer entrar na anestesiologia clínica, a Pós-graduação em Anestesiologia Veterinária em Goiânia começa pela fisiologia e pela monitoração. Se você já é anestesista, a Pós-graduação em Anestesiologia Avançada e a Pós-graduação em Anestesiologia Locorregional Veterinária aprofundam a técnica." Pré-requisito exato de 657 e 359 [CONFIRMAR] antes de dizer quem pode entrar. |
| "Por que a avançada e a locorregional custam mais?" (H-A1.4) | Não justificar preço com adjetivo. Mostrar o que a ficha traz: 360 h com módulos presenciais de prática guiada e o corpo docente listado, e o texto-padrão completo de cada turma. Nunca comparar com a pós geral como "vale mais". |
| "Vou praticar em paciente ou só em modelo?" (H-A1.3) | Para 359, a ficha diz: modelos anatômicos, phantoms, sonoanatomia, fluoroscopia e técnicas em pacientes vivos em aulas demonstrativas, além de hands-on. Para 68609, o módulo 5 é hands-on de sedação e monitoração. Número de alunos por estação [CONFIRMAR]. |

**Palavras e frases.** Usar: anestesia de precisão (texto da ficha 657), bloqueio locorregional guiado por ultrassom, monitoração, prática guiada, anestesista. Evitar: "título de especialista" (a ficha cita a prova de Especialista; sem texto oficial, não entra), "maiores nomes da anestesia regional do mundo" (texto da ficha 359, superlativo sem fonte), "10 primeiros", "12% de desconto".

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Anestesiologia Veterinária em Goiânia: do pré-anestésico à anestesia inalatória"
- Título: "Pós-graduação em Anestesiologia Avançada: para quem já anestesia e quer ir além do protocolo"
- Título: "Pós-graduação em Anestesiologia Locorregional Veterinária: bloqueios guiados por ultrassom, com prática presencial"
- Chamada: "Veja os módulos presenciais e o corpo docente da turma de 24/04/2027 em Goiânia."
- Chamada: "Confira o cronograma da turma de 13/03/2027 em São Paulo antes de decidir."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 657 | Pós-graduação em Anestesiologia Avançada | São Paulo | 13/03/2027 | II | 30x de R$ 1.613,33 no cartão ou boleto (total de R$ 48.400,00), mais matrícula de R$ 250,00 | liberada; pré-requisito [CONFIRMAR] |
| 68609 | Pós-graduação em Anestesiologia Veterinária | Goiânia | 24/04/2027 | VIII | 30x de R$ 1.081,67 no cartão ou boleto (total de R$ 32.450,00), mais matrícula de R$ 250,00 | liberada |
| 359 | Pós-graduação em Anestesiologia Locorregional Veterinária | São Paulo | 22/05/2027 (só no site, [CONFIRMAR com a planilha]) | I | 26x de R$ 1.673,08 no cartão ou boleto (total de R$ 43.500,00), mais matrícula de R$ 250,00 | liberada sem o desconto da ficha; pré-requisito [CONFIRMAR] |

Provas de bolsa da área no catálogo: 68639 (São Paulo) e 68640 (Goiânia). Sem peça nesta rodada (decisão 14).

---

## 3. A2. Cardiorrespiratório (turmas 289, 698, 68636, 352)

**Público e momento de carreira.** Clínico de pequenos animais que atende cardiopatas e pacientes respiratórios e quer fazer e interpretar o exame (P1). Para 698, quem quer a ecocardiografia sem a cardiologia inteira (pergunta de nível, H-A2.3). Para 352, quem já está na UTI ou no centro cirúrgico [SUPOSIÇÃO, persona 5.2]. Para 289, quem mora em Goiânia e entorno.

**Promessa central.** Do coração ao pulmão, uma pós para cada nível: cardiologia em Goiânia, ecocardiografia, pneumologia e ventilação mecânica em São Paulo, com prática presencial nos módulos marcados.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 289: coordenação Msc. Flavia Mazzo; 14 professores listados, entre eles Dr. Marlos Gonçalves Sousa, Profa. Denise Fantoni, Dr. Guillermo Veiga, DR. BRUNO DURANTE e PHD. Fabio Gava. 698: coordenação MSc Fernanda Fontalva Cordeiro; 5 professores listados (MSC. REBECCA PESSOA, DR. BRUNO DURANTE, Msc. Flavia Mazzo, MV. Vinícius Dayoub). 68636: coordenação Agata R. M. Esposito; 16 professores listados, entre eles Dr. Fausto Brandão (PORTUGAL), Prof. André Shih (EUA), Dr. Mauricio Veloso Brun e Dra. Sabrina Caruso Chate. 352: coordenação Dr. Alessandro Martins; 10 professores listados, entre eles Prof. João Henrique Neves Soares (EUA), Prof. Daniel Sakai (EUA), Prof. Francesco Staffieri (Itália) e Profa. Denise Fantoni |
| Módulos | 289 (24 módulos, 500 h): 6 módulos presenciais, com prática hands-on de ecocardiograma. 698 (12 módulos, 370 h): 5 módulos presenciais hands-on (ecocardiografia básica, hemodinâmica, DMVM, cardiomiopatias, congênitas) e TCC no módulo 12. 68636 (24 módulos, 500 h): práticas de anatomia e semiologia respiratória, ultrassonografia pulmonar, laringotraqueobroncoscopia, rinoscopia e intervenções emergenciais nos módulos presenciais. 352 (18 módulos, 360 h): 7 módulos presenciais (modalidades ventilatórias, ventilação protetora, assincronia e desmame, ventilação monopulmonar, ECMO) e grupo de estudo para discussão de casos e artigos [CONFIRMAR NO CATÁLOGO] |
| Formato e campus | Semipresencial nas quatro. 289 em Goiânia ("Ufape Goiânia", na ficha); 698, 68636 e 352 em São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Preciso da cardiologia completa ou posso fazer só ecocardiografia?" (H-A2.3) | "São caminhos diferentes. A Pós-graduação em Cardiologia Veterinária (500 h, Goiânia) cobre da fisiologia às cardiopatias, com ecocardiograma nos módulos práticos. A Pós-graduação em Ecocardiografia (370 h, São Paulo) é focada no exame, com 5 módulos práticos hands-on." Pré-requisito de 698 [CONFIRMAR NO CATÁLOGO]. |
| "Moro longe de São Paulo, vou ter de viajar todo mês?" | Para Goiânia: "A Pós-graduação em Cardiologia Veterinária tem turma em Goiânia." Para São Paulo: "A teoria é online; você viaja só nos módulos presenciais, com data no cronograma. Compre passagem só depois de a turma ser confirmada." |
| "Ventilação mecânica serve para quem não trabalha em UTI?" (Q2.7) | Responder com a ficha: o programa liga anestesia, sedação, monitoração e UTI. Público-alvo na ficha: "Médicos Veterinários". Indicação clínica por perfil fica para revisão docente [CONFIRMAR]. |

**Palavras e frases.** Usar: ecocardiograma, ecodopplercardiografia, hands-on (sempre com o tema do módulo), cardiopata, paciente respiratório, ventilação protetora. Evitar: "curso inédito" e "melhores especialistas do mundo" (textos da ficha 352), "referência mundial", "10% para os 10 primeiros", "pós em cardio vet" no texto visível (termo só de anúncio, palavras-chave K2.7), comparar carga ou duração com concorrente.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Cardiologia Veterinária em Goiânia, com ecocardiograma nos módulos práticos"
- Título: "Pós-graduação em Ecocardiografia: 5 módulos hands-on em São Paulo"
- Título: "Pós-graduação em Pneumologia Veterinária: da radiologia à broncoscopia"
- Chamada: "Cardiologia ou ecocardiografia? Compare os cronogramas e escolha o seu nível."
- Chamada: "Veja os módulos presenciais da Pós-graduação em Ventilação Mecânica."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 289 | Pós-graduação em Cardiologia Veterinária | Goiânia | 20/03/2027 | II | 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00 | liberada |
| 698 | Pós-graduação em Ecocardiografia | São Paulo | 28/11/2026 | III | 18x de R$ 1.498,33 no cartão ou boleto (total de R$ 26.970,00), mais matrícula de R$ 250,00 | site mostra 2027 (pedido A6): sem anúncio novo até a correção; regra 4 da seção 0 |
| 68636 | Pós-graduação em Pneumologia Veterinária | São Paulo | 17/04/2027 (só no site, [CONFIRMAR com a planilha]) | VIII | 30x de R$ 1.265,00 no cartão ou boleto (total de R$ 37.950,00), mais matrícula de R$ 250,00 | liberada |
| 352 | Pós-graduação em Ventilação Mecânica | São Paulo | 24/05/2027 (site diz 24/04/2027) | I | 30x de R$ 1.596,00 no cartão ou boleto (total de R$ 47.880,00), mais matrícula de R$ 250,00 | liberada sem o desconto da ficha |

Provas de bolsa da área no catálogo: 68641, 68642 (Cardiologia, links invertidos, P3) e 68659 (Pneumologia). Sem peça nesta rodada.

---

## 4. A3. Emergência, terapia intensiva e clínica médica (turmas 68635, 68623)

**Público e momento de carreira.** Plantonista e clínico generalista que se sente inseguro com o paciente grave (H-A3.1) e tem escala de fim de semana (H-A3.4). Para 68635, o clínico que quer a base ampla de clínica médica com emergência; para 68623, quem quer terapia intensiva e emergência, com turma vinculada a Goiânia.

**Promessa central.** Para decidir com segurança no plantão: 750 horas de clínica, emergência e terapia intensiva, com os módulos práticos datados no cronograma.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 68635: coordenação Prof. Caio Cavalcanti Balençuela; 25 professores listados, entre eles DR. Roberto Fecchio, Dra. Angélica Safatle, Dr. Leo Londoño (EUA) e Prof. André Shih (EUA). 68623: coordenação Dr. Alessandro Martins e Dra. Denise Fantoni; 33 professores listados, entre eles PhD, DVM, DACVECC. Daniel Fletcher (EUA), Dr. Leo Londoño (EUA), Prof. Daniel Sakai (EUA) e DR. RONALD PAIVA M GONÇALVES (EUA) |
| Módulos | 68635 (28 módulos, 750 h): uma especialidade por mês (nefrologia, neurologia, pneumologia, gastro, infectologia, dermatologia, endocrinologia, oftalmologia, hematologia, oncologia, odontologia, felinos, imagem) e 9 módulos presenciais (semiologia, eletrocardiograma e hemogasometria, sondagem uretral, ambulatório clínico, A-fast e T-fast, triagem do paciente grave, RCP e trauma). 68623 (28 módulos, 750 h): A-fast, T-fast e Eco Fast, punção guiada, cateter central e arterial, hemodinâmica, ventilação mecânica, sepse, RCP, neurointensivismo, UTI móvel e queimados, com módulos presenciais de prática |
| Formato e campus | Semipresencial nas duas. 68635 em São Paulo. 68623 com localidade Goiânia no catálogo, mas a ficha diz "Aulas Práticas (Presenciais) - Unidade São Paulo" [CONFIRMAR onde são os módulos presenciais de 68623 antes de qualquer peça] |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Trabalho em plantão de fim de semana. Dá para fazer?" (Q3.3) | "As datas de todos os módulos estão no cronograma antes de começar, então dá para negociar a escala com meses de antecedência. A teoria é online; o presencial é só nos módulos práticos." Reposição de módulo [CONFIRMAR]. Nunca "flexível". |
| "Qual a diferença entre Clínica Médica e Emergência e Terapia Intensiva e Emergência, se as duas têm 750 h?" (H-A3.3) | "A Pós-graduação em Clínica Médica e Emergência de Pequenos Animais passa por uma especialidade clínica por mês e termina no paciente grave. A Pós-graduação em Terapia Intensiva e Emergência Veterinária fica no paciente crítico: hemodinâmica, ventilação, sepse, neurointensivismo." Sem dizer qual "vale mais". |
| "Tem pós EAD bem mais barata." | Não comparar preço. "Aqui a prática é presencial: A-fast, T-fast, punção guiada e RCP se aprendem com a mão no paciente e no equipamento." Mostrar o texto-padrão completo. |

**Palavras e frases.** Usar: paciente grave, plantão, triagem, A-fast e T-fast, RCP, hemodinâmica, sepse. Evitar: "dupla certificação", "2 certificações", "certificado de emergência 375 horas" (textos das fichas, regra 6), "Domine o conhecimento para salvar vidas" (promessa de resultado), "referência nacional", "salvar vidas" como promessa da pós.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Clínica Médica e Emergência de Pequenos Animais: 750 h, da semiologia ao paciente grave"
- Título: "Pós-graduação em Terapia Intensiva e Emergência Veterinária: hemodinâmica, ventilação e sepse com prática presencial"
- Título: "Plantonista: veja as datas dos módulos antes de montar sua escala"
- Chamada: "Confira o cronograma da turma de 10/04/2027 em São Paulo."
- Chamada: "Compare as duas pós de 750 h e escolha pelo seu plantão."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | São Paulo | 10/04/2027 | V | 30x de R$ 1.100,00 no cartão ou boleto (total de R$ 33.000,00), mais matrícula de R$ 250,00 | liberada |
| 68623 | Pós-graduação em Terapia Intensiva e Emergência Veterinária | Goiânia (catálogo) | 22/05/2027 | IV | 30x de R$ 1.160,00 no cartão ou boleto (total de R$ 34.800,00), mais matrícula de R$ 250,00 | só depois de confirmar o local da prática |

Provas de bolsa da área no catálogo: 68645 e 68660. Sem peça nesta rodada.

---

## 5. A4. Cirurgia, ortopedia e reabilitação (turmas 68632, 578, 662, 366)

**Público e momento de carreira.** Clínico que já opera ou quer operar com mais segurança (68632, 578, 662), e o veterinário que trabalha com reabilitação de pacientes ortopédicos, neurológicos e idosos (366). Para 68632, quem mora em Goiânia e pode estar na cidade todo mês (H-A4.1).

**Promessa central.** Da técnica cirúrgica à reabilitação: cirurgia presencial em Goiânia, videocirurgia, ortopedia e fisioterapia em São Paulo, com prática em cada módulo marcado.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 68632: 6 professores listados (Dr. Jose Luiz Lopes, Dr. Artur Gouveia Rocha, Dra. Fabiana A. Voorwald, Dr. Luiz Artur Giuffrida, Dr. Marco Augusto Machado Silva, Dr. Fabrício Singaretti de Oliveira); coordenação não consta na ficha [CONFIRMAR]. 578: coordenação UFAPE; 3 professores listados (Dr. Marco Augusto Machado Silva, Dr. Mauricio Veloso Brun, DR. Marcos Carvallo). 662: coordenação Dra. Carolina Gonçalves Dias Lima; 12 professores listados, entre eles DR. Pablo Herthel de Carvalho e Dra Maíra Rezende Formenton [CONFIRMAR que a lista é desta turma: link trocado, P3]. 366: coordenação UFAPE; 8 professores listados, entre eles Dra Carolina Gonçalves Dias Lima, Profa. Mayara Travalini, Msc. Patricia Bonifácio Flôr e DRA. Laryssa Rosseto |
| Módulos | 68632 (24 módulos, 500 h): do princípio da cirurgia à neurocirurgia, cirurgias cardiovasculares e cuidados perioperatórios, um tema por mês. 578 (24 módulos, 500 h): treinamento em simuladores (nível básico, intermediário e avançado), ovariectomia, gastropexia, biópsias, colecistectomia, esplenectomia, adrenalectomia, nefrectomia nos módulos presenciais. 366 (24 módulos, 500 h): 9 módulos presenciais (hidroterapia, cinesioterapia, recursos eletrofísicos, reabilitação neurológica e ortopédica, bandagem taping, paciente a beira-leito). 662: aulas práticas em modelos e cadáveres, em pequenos grupos (texto da ficha) [CONFIRMAR, ficha de outra turma] |
| Formato e campus | 68632 é **presencial** em Goiânia ("Ufape Goiânia"), a única turma presencial do recorte. 578, 662 e 366 são semipresenciais em São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "A de Goiânia é toda presencial? Preciso ir todo mês?" (H-A4.1, Q4.2) | "Sim, a Pós-graduação em Clínica Cirúrgica de Cães e Gatos de Goiânia é presencial: um fim de semana por mês na Ufape Goiânia, com as datas no cronograma." Jornada e horários [CONFIRMAR NO CATÁLOGO]. Nunca chamar 68632 de semipresencial. |
| "Vou operar em animal vivo, em cadáver ou em modelo?" (H-A4.2) | Responder só com a ficha de cada turma: em 578, simuladores e procedimentos nos módulos presenciais; em 662, modelos e cadáveres em pequenos grupos [CONFIRMAR]. Em 68632, a ficha não descreve a prática: [CONFIRMAR] antes de responder. |
| "Fisioterapia veterinária é área do médico veterinário?" | Citar só o que a ficha de 366 traz: a Resolução nº 850, de 05/12/2006, citada na página, que trata da fisioterapia animal [CONFIRMAR NO CATÁLOGO e com a regulação antes de peça]. |

**Palavras e frases.** Usar: técnica cirúrgica, simulador, prática supervisionada, reabilitação, paciente a beira-leito. Evitar: "alternativa", "encantador mundo da ortopedia" (texto da ficha 662), "reconhecimento pelo MEC" (fichas 68632 e 578), "a única pós presencial de Goiânia", preço ou turma de 662 em peça.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, presencial em Goiânia"
- Título: "Pós-graduação em Videocirurgia Veterinária: do simulador ao procedimento"
- Título: "Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária: 9 módulos práticos em São Paulo"
- Chamada: "Veja os 24 temas da turma de 10/04/2027 em Goiânia."
- Chamada: "Confira o que se pratica em cada módulo presencial."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68632 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Goiânia (presencial) | 10/04/2027 | V | 30x de R$ 1.100,00 no cartão ou boleto (total de R$ 33.000,00), mais matrícula de R$ 250,00 | liberada |
| 578 | Pós-graduação em Videocirurgia Veterinária | São Paulo | 22/05/2027 | IV | 30x de R$ 1.250,00 no cartão ou boleto (total de R$ 37.500,00), mais matrícula de R$ 250,00 | liberada |
| 662 | Pós-graduação em Ortopedia Veterinária | São Paulo | 24/04/2027 | sem número (diverge) | sem preço em peça (link trocado, P3) | só nome, campus e data até a correção |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | São Paulo | 10/04/2027 (site diz 24/04/2027) | I | 30x de R$ 1.100,00 no cartão ou boleto (total de R$ 33.000,00), mais matrícula de R$ 250,00 | liberada |

Provas de bolsa da área no catálogo: 68643 e 68644. Sem peça nesta rodada.

---

## 6. A5. Diagnóstico por imagem e endoscopia (turmas 68604, 68629)

**Público e momento de carreira.** Clínico que quer laudar e discutir o achado com segurança (H-A5.2) e o recém-formado que quer começar pelo ultrassom (P3, persona 5.1). 68629 tem o menor total entre as pós veterinárias abertas.

**Promessa central.** Ver, interpretar e defender o achado: imagem completa ou ultrassonografia de pequenos animais, com prática presencial nos módulos marcados.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 68604: coordenação M.V. Carlos Fotin; 11 professores listados, entre eles Dra. Tilde Fróes, DRA. Cibele Figueira Carvalho e Dr. Antônio Carlos C. Lacreta Junior. 68629: coordenação MSC. Luciane Kanayama; 10 professores listados, entre eles DRA. Elaine Cristina Soares, DRA. Cibele Figueira Carvalho e DRA. Carolina de Oliveira Guirelli |
| Módulos | 68604 (24 módulos, 500 h): radiologia, ultrassonografia, tomografia e ressonância; 7 módulos presenciais de prática (anatomia, Rx e US por sistema, Doppler, ultrassom intervencionista e beira-leito). 68629 (18 módulos, 360 h): ultrassonografia por sistema, Doppler, procedimentos guiados, emergência (Afast, Tfast, Vetblue, POCUS); 4 módulos presenciais (Prática I a IV) e 2 mesas redondas online |
| Formato e campus | Semipresencial, São Paulo, nas duas |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Diagnóstico por imagem ou ultrassonografia: qual escolher?" (H-A5.4, Q5.2) | "A Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária (500 h) cobre radiologia, ultrassom, tomografia e ressonância. A Pós-graduação em Ultrassonografia de Pequenos Animais (360 h) é só ultrassom, do básico ao Doppler e aos procedimentos guiados." |
| "Preciso ter aparelho na clínica?" (H-A5.5) | "A prática é feita nos módulos presenciais, na Ufape." Requisito de equipamento próprio [CONFIRMAR]; não afirmar que não precisa. |
| "Vou praticar tomografia e ressonância?" (H-A5.1) | Responder com a ficha: tomografia e ressonância estão nos módulos finais, online. Não prometer prática nesses métodos. |

**Palavras e frases.** Usar: laudo, interpretação, achado, Doppler, procedimento guiado, POCUS (só como tema do módulo de 68629). Evitar: "custo relativamente baixo" (texto da ficha sobre o método, não sobre o curso), "a pós mais barata", "a partir de", "apenas", termos de EAD.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Ultrassonografia de Pequenos Animais: 4 módulos práticos em São Paulo"
- Título: "Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária: Rx, ultrassom, tomografia e ressonância"
- Chamada: "Veja o cronograma da turma de 22/05/2027 e as datas das práticas."
- Chamada (68604, turma de 31/10/2026): "Fale com o time para saber como entrar na turma."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68604 | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | São Paulo | 31/10/2026 | VI | 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00 | inventário e reta final (seção 4 do cmo); regra 4 da seção 0 |
| 68629 | Pós-graduação em Ultrassonografia de Pequenos Animais | São Paulo | 22/05/2027 (só no site, [CONFIRMAR com a planilha]) | III | 24x de R$ 685,67 no cartão ou boleto (total de R$ 16.456,00), mais matrícula de R$ 350,00 | liberada |

Provas de bolsa da área no catálogo: 68647, 68661 e 68649 (Endoscopia, sem turma de destino). Sem peça nesta rodada. Não há turma de Pós em endoscopia aberta: a área não fala de endoscopia em peça de Pós.

---

## 7. A6. Gastroenterologia (turma 68606)

**Público e momento de carreira.** Clínico de pequenos animais que atende muito caso gastrointestinal e quer ser referência local na área (H-A6.1). Turma começa em 07/11/2026: mensagem de reta final, sem urgência inventada.

**Promessa central.** Gastroenterologia de cães e gatos do diagnóstico à prática cirúrgica e endoscópica, com grupo de discussão de casos com a coordenação.

**Pilares de prova (ficha 68606):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação Esp. Maria Carolina Pappalardo; 38 professores listados, entre eles Dr. Rodolfo Oliveira Leal, DRA. VIVIANE DE MARCO, DR. Fabrizio Grandi e DRA. Maria Anete Lallo |
| Módulos | 24 módulos, 500 h; 3 módulos presenciais com anatomia prática, prática de cirurgia esofágica, gástrica, intestinal, pancreática e hepatobiliar, parasitologia ou transplante fecal e colocação de sondas. Diferenciais escritos na ficha: estágios com a cooperação nas clínicas e hospitais dos coordenadores e grupo para discussão de casos entre alunos e coordenadores (regras do estágio [CONFIRMAR]) |
| Formato e campus | Semipresencial, São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Ainda dá para entrar? A turma começa em 07/11." | "Fale com o time para saber como entrar na turma." Sem prazo inventado e sem "últimas vagas". Regra de entrada tardia [CONFIRMAR] (PR4). |
| "Tem prática de endoscopia e cirurgia ou é tudo online?" (H-A6.4, Q6.3) | "A teoria é online e há 3 módulos presenciais com prática de anatomia, cirurgia e parasitologia, além do estágio previsto na página." Endoscopia prática e regras do estágio [CONFIRMAR NO CATÁLOGO]. |
| "São 38 professores. Vou ter acesso a alguém?" | "A página prevê um grupo para discussão de casos entre alunos e coordenadores." Formato e frequência [CONFIRMAR]. |

**Palavras e frases.** Usar: caso gastrointestinal, enteropatia, hepatopatia, discussão de casos, estágio (com a regra quando existir). Evitar: "especialidade emergente e carente de profissionais" e "coordenadores referências nacionais" (textos da ficha, sem fonte), promessa de mercado, a prova de bolsa da área como caminho para esta turma.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Gastroenterologia Veterinária: prática cirúrgica e discussão de casos com a coordenação"
- Título: "Turma de 07/11/2026 da Pós-graduação em Gastroenterologia Veterinária, em São Paulo"
- Chamada: "Fale com o time para saber como entrar na turma."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68606 | Pós-graduação em Gastroenterologia Veterinária | São Paulo | 07/11/2026 | IX | 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00 | inventário e reta final; regra 4 da seção 0 |

Prova de bolsa da área no catálogo: 68650 (a turma começa antes da prova). Sem peça nesta rodada.

---

## 8. A7. Endocrinologia e nefrologia (turma 68617)

**Público e momento de carreira.** Clínico que atende diabético, Cushing, hipotireoidismo e doença renal crônica e quer fechar o caso sem encaminhar. Nefrologia não tem turma aberta no recorte (68612 em "verificar"): a área vende só endocrinologia.

**Promessa central.** Endocrinologia de pequenos animais da fisiologia hormonal à discussão de casos, com prática de atendimento endocrinológico.

**Pilares de prova (ficha 68617):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação DR. Eric Vieira Januário; 22 professores listados, entre eles Dr. Alan Poppl, Dra. Marilu Gioso, Dra. Priscila Viau e Dra. Ayne Hayashi |
| Módulos | 24 módulos, 500 h: fisiologia endócrina, Cushing, hipoadrenocorticismo, diabetes mellitus em cães e gatos, cetoacidose, insulinoma, distúrbios da calcemia, doença renal crônica e infecção urinária no endocrinopata, discussão de casos em vários módulos; módulo 12 presencial com atendimento endocrinológico, anatomia do sistema endócrino e discussão de casos |
| Formato e campus | Semipresencial, São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "O começo é muito teórico. Quando aplico na rotina?" (H-A7.2) | "Os primeiros módulos são fisiologia, porque o raciocínio endócrino depende dela; a partir do módulo 5 o curso entra em Cushing, e a discussão de casos aparece ao longo do cronograma." |
| "Tem prática presencial?" | "Sim: o módulo 12 é presencial, com atendimento endocrinológico." Número exato de módulos presenciais [CONFIRMAR NO CATÁLOGO]. Não exagerar a prática. |
| "Tem pós de nefrologia?" | "A turma aberta da área hoje é a Pós-graduação em Endocrinologia de Pequenos Animais, que trata doença renal crônica e proteinúria no paciente endócrino." Nunca oferecer 68612. |

**Palavras e frases.** Usar: endocrinopata, Cushing, diabetes mellitus, discussão de casos, atendimento endocrinológico. Evitar: "instituição reconhecida e respeitada", "profissionais renomados", "agrega valor ao seu currículo" (textos da ficha), número da turma.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Endocrinologia de Pequenos Animais: do Cushing ao diabético felino"
- Título: "Endocrinologia em São Paulo, com atendimento endocrinológico no módulo presencial"
- Chamada: "Veja o cronograma da turma de 17/04/2027."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais | São Paulo | 17/04/2027 | sem número (planilha VII, site V) | 30x de R$ 1.200,00 no cartão ou boleto (total de R$ 36.000,00), mais matrícula de R$ 250,00 | liberada, sem número de turma |

Provas de bolsa da área no catálogo: 68648 e 68653 (Nefrologia, sem turma de destino). Sem peça nesta rodada.

---

## 9. A8. Dermatologia (turma 68610)

**Público e momento de carreira.** Clínico com casos de pele e ouvido recorrentes, que encaminha alergias, otites e piodermites (H-A8.1). Turma começa em 28/11/2026.

**Promessa central.** Dermatologia de cães e gatos com atendimento de casos clínicos nos módulos presenciais, do tricograma à dermatohistopatologia.

**Pilares de prova (ficha 68610):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação UFAPE (sem nome na ficha [CONFIRMAR]); 18 professores listados, entre eles Dr. Alan Poppl, DR. Fabrizio Grandi, Dra. Andrea Barbosa, Dr. Claudio Nazaretian Rossi e DRA. Ana Amélia D. Gomes |
| Módulos | 24 módulos, 500 h; 7 módulos presenciais (5, 9, 14, 18, 21, 22 e 24), com atendimento de casos clínicos (módulos 5 e 9), testes alérgicos, otoscopia e videotoendoscopia, fotobiomodulação, crioterapia e dermatohistopatologia; plantões de dúvidas mensais e discussão de casos e artigos (texto da ficha) |
| Formato e campus | Semipresencial, sede da Ufape em São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "A turma começa em 28/11. Ainda dá para entrar?" | "Fale com o time para saber como entrar na turma." Sem prazo inventado. |
| "Tenho acesso aos professores fora das aulas?" (H-A8.2) | "A página prevê plantões de dúvidas mensais e discussão de casos e artigos." Horário e formato [CONFIRMAR]. |
| "Quanto tempo vou passar fora da clínica?" | "São 7 módulos presenciais em 24 meses, com as datas no cronograma; os outros 17 são online." |

**Palavras e frases.** Usar: alergia, otite, piodermite, dermatoscopia, citologia de pele, atendimento de casos clínicos. Evitar: "reconhecida pelo Ministério da Educação" (texto da ficha), "dermatozoonoses" no texto de peça (jargão da página), "pós em derma vet" no texto visível.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Dermatologia Veterinária: 7 módulos presenciais com atendimento de casos"
- Título: "Dermatologia em São Paulo: turma de 28/11/2026"
- Chamada: "Fale com o time para saber como entrar na turma."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68610 | Pós-graduação em Dermatologia Veterinária | São Paulo | 28/11/2026 | V | 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00 | liberada; regra 4 da seção 0 a partir de 29/10/2026 |

Prova de bolsa da área no catálogo: 68646 (27/11/2026, véspera do início). Sem peça nesta rodada.

---

## 10. A9. Oftalmologia (turma 707)

**Público e momento de carreira.** Clínico mais experiente, com renda e casos oftálmicos frequentes, que quer operar e microoperar (H-A9.1); objeção de preço mais forte do portfólio (persona 5.1). Turma começa em 30/10/2026.

**Promessa central.** Oftalmologia clínica e cirúrgica com microscópio individual nas aulas práticas e atendimentos supervisionados.

**Pilares de prova (ficha 707):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação Dra. Andrea Barbosa, Dra. Angélica Safatle e Dra. Juliana Jorge; 19 professores listados, entre eles DRA. Paula Diniz Galera, Dr. Eduardo Perlmann, PHD. Silvia Franco Andrade, Dr. Alexandre Lima de Andrade e o convidado DR. João A. T. Pigatto (autorização de convidados: decisão 10) |
| Módulos | 24 módulos, 600 h; módulos de 3 dias (sexta a domingo); 10 módulos presenciais na sede, com cirurgia e microcirurgia ocular, microscópio individual por aluno, supervisão de professores e monitores e atendimentos clínicos reais em mutirões supervisionados; conteúdos de relações interpessoais, postura ética e gestão financeira (texto da ficha) |
| Formato e campus | Semipresencial, São Paulo; teoria online ao vivo, com gravação na plataforma |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "É o valor mais alto que vi." (H-A9.2) | Sem justificar com adjetivo. "São 600 h, com microscópio individual nas aulas práticas. O valor está inteiro: [texto-padrão]." Não comparar com outra pós. |
| "Os módulos são de três dias. Como fico na clínica?" (H-A9.3) | "Sim, os módulos vão de sexta a domingo, e as datas estão no cronograma até 2028, então dá para planejar a agenda com antecedência." |
| "Ainda dá para entrar? A turma começa em 30/10." | "Fale com o time para saber como entrar na turma." |

**Palavras e frases.** Usar: microscópio individual, microcirurgia ocular, mutirão supervisionado, segmento anterior e posterior. Evitar: "infraestrutura completa e moderna" e "corpo docente altamente qualificado" (textos da ficha, sem lista), "referências nacionais e internacionais", prova de bolsa (68656 fora do ar).

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Oftalmologia Veterinária: microscópio individual nas aulas práticas"
- Título: "600 h de oftalmologia clínica e cirúrgica em São Paulo"
- Chamada: "Fale com o time para saber como entrar na turma de 30/10/2026."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 707 | Pós-graduação em Oftalmologia Veterinária | São Paulo | 30/10/2026 | VII | 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00 | inventário e reta final; regra 4 da seção 0 |

Prova de bolsa: não há prova de Oftalmologia ativa (68656 fora do ar).

---

## 11. A10. Oncologia (turma 68628)

**Público e momento de carreira.** Clínico que já atende paciente oncológico e quer conduzir o tratamento, com dúvida sobre segurança na quimioterapia (H-A10.2).

**Promessa central.** Oncologia de cães e gatos do diagnóstico ao cuidado paliativo, com quimioterapia, eletroquimioterapia e cirurgia oncológica nos módulos presenciais.

**Pilares de prova (ficha 68628):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação ESP. Juliana Vieira Cirillo; 36 professores listados, entre eles Dr. Jorge Luiz Costa Castro, Dra. Renata Afonso Sobral, Dr. Carlos Henrique Maciel Brunner, Dra. Sabrina Marin Rodigheri e PHD. Krishna Duro de Oliveira |
| Módulos | 24 módulos, 500 h; 8 módulos presenciais: quimioterapia antineoplásica com biossegurança, eletroquimioterapia e crioterapia, cirurgia oncológica e reconstrutiva, melanoma e sarcoma felino, radioterapia com visita, mastocitoma, neoplasias urinárias, nutrição do paciente oncológico; cuidado paliativo e dor em módulos online |
| Formato e campus | Semipresencial, São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "O que vou saber fazer no fim?" (H-A10.1) | Responder pelo cronograma, não pelo certificado: "Diagnóstico, quimioterapia, imunoterapia, eletroquimioterapia, cirurgia oncológica e cuidado paliativo, com 8 módulos práticos." Nunca prometer resultado clínico. |
| "Vou aprender a manipular quimioterápico com segurança?" (H-A10.2) | "O módulo 5 é presencial: quimioterapia antineoplásica e biossegurança." Estrutura exigida na clínica do aluno [CONFIRMAR, revisão docente]. |
| "Por que esta turma custa mais que a anterior?" (H-A10.3) | Não comparar com turma antiga. Mostrar só o texto-padrão desta turma. |

**Palavras e frases.** Usar: paciente oncológico, biossegurança, eletroquimioterapia, cirurgia oncológica, cuidado paliativo. Evitar: "reconhecimento pelo MEC" e "referência nacional em educação" (texto da ficha), número da turma, "cura".

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Oncologia Veterinária: 8 módulos presenciais, da quimioterapia à cirurgia oncológica"
- Título: "Quimioterapia com biossegurança: veja o módulo presencial da Pós-graduação em Oncologia Veterinária"
- Chamada: "Veja o cronograma da turma de 10/04/2027 em São Paulo."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68628 | Pós-graduação em Oncologia Veterinária | São Paulo | 10/04/2027 | sem número (planilha VI, site VII) | 30x de R$ 1.298,00 no cartão ou boleto (total de R$ 38.940,00), mais matrícula de R$ 250,00 | liberada, sem número de turma |

Prova de bolsa da área no catálogo: 68657. Sem peça nesta rodada.

---

## 12. A11. Laboratório: hematologia, patologia clínica e citopatologia (turmas 68608, 68615, 333)

**Público e momento de carreira.** Clínico que depende do laboratório externo para fechar o caso (H-A11.2) e veterinário que trabalha ou quer trabalhar em laboratório (68615 e 333). Dúvida central: "serve para clínico?" (H-A11.3).

**Promessa central.** Ler o exame com as próprias mãos: hematologia, patologia clínica e citopatologia com prática de lâmina, coleta e laudo nos módulos presenciais.

**Pilares de prova (fichas):**

| Pilar | Prova |
|---|---|
| Docentes | 68608: coordenação ESP. Mariana Aldemundo Pereira di Vincenzo; 14 professores listados, entre eles Dra Michele Andrade de Barros, DR. Nicole Hlavac e Dr. Paulo Tabanez. 68615: coordenação DRA. Sabrina Caruso Chate; 17 professores listados, entre eles Dra. Regina Kiomi Takahira, Dr. Paulo César Jark, DR. Fabrizio Grandi e Prof. André Shih (EUA). 333: coordenação UFAPE; 1 professora listada (Dra. Sabrina Caruso Chate) [CONFIRMAR corpo docente antes de peça de autoridade] |
| Módulos | 68608 (24 módulos, 500 h): mielograma, imunomediadas, coagulopatias, medicina transfusional; 3 módulos presenciais (coagulograma e coleta de mielograma; coleta e processamento de hemocomponentes; mais um). 68615 (24 módulos, 500 h): materiais biológicos, hemograma e sua automação, hemostasia, hemoparasitoses, mielograma, transfusão, bioquímica, urinálise, gestão do laboratório, com módulos presenciais de prática. 333 (24 módulos, 500 h): 6 módulos presenciais com leitura de lâminas e discussão de casos, coleta e coloração, citologia esplênica e linfoma, mielograma |
| Formato e campus | Semipresencial, São Paulo, nas três |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Serve para quem é clínico ou só para quem trabalha em laboratório?" (H-A11.3, Q11.1) | "O público das três é médico veterinário. A Pós-graduação em Hematologia Veterinária liga o exame ao paciente (anemias, coagulopatias, transfusão); a Pós-graduação em Patologia Clínica inclui como estruturar e administrar um laboratório." Recorte de perfil [CONFIRMAR NO CATÁLOGO]. |
| "Qual das três eu faço?" (Q11.2) | "Hematologia: sangue, medula e transfusão. Patologia clínica: o laboratório inteiro, do pré-analítico ao laudo. Citopatologia: células e tecidos ao microscópio." |
| "Quanto vou praticar?" | Citar os módulos presenciais da ficha de cada turma; em 333, "6 módulos presenciais com leitura de lâminas". Sem prometer volume de lâminas. |

**Palavras e frases.** Usar: lâmina, mielograma, laudo, coleta, hemocomponentes, correlação clínico-laboratorial. Evitar: "oportunidade única", "contribui para o avanço da ciência" (texto da ficha 333), "reconhecimento pelo MEC" (ficha 68615), autoridade docente de 333 até a correção.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Hematologia Veterinária: do hemograma à medicina transfusional"
- Título: "Pós-graduação em Patologia Clínica: o laboratório do pré-analítico ao laudo"
- Título: "Pós-graduação em Citopatologia Veterinária: 6 módulos de leitura de lâminas"
- Chamada: "Hematologia, patologia clínica ou citopatologia? Compare os cronogramas."

**Turmas da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68608 | Pós-graduação em Hematologia Veterinária | São Paulo | 28/11/2026 | VIII | 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00 | liberada; regra 4 da seção 0 a partir de 29/10/2026 |
| 68615 | Pós-graduação em Patologia Clínica | São Paulo | 20/03/2027 | VII | 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00 | liberada |
| 333 | Pós-graduação em Citopatologia Veterinária | São Paulo | 27/03/2027 | I | 30x de R$ 935,00 no cartão ou boleto (total de R$ 28.050,00), mais matrícula de R$ 250,00 | liberada; sem peça de autoridade docente |

Provas de bolsa da área no catálogo: 68651 e 68658. Sem peça nesta rodada.

---

## 13. A12. Neurologia (turma 68616)

**Público e momento de carreira.** Clínico inseguro no exame neurológico e na localização da lesão (H-A12.1). A ficha não traz público-alvo (H-A12.3 [CONFIRMAR]).

**Promessa central.** Do exame neurológico à neurocirurgia: localizar a lesão com raciocínio clínico, com avaliações e práticas presenciais em São Paulo.

**Pilares de prova (ficha 68616):**

| Pilar | Prova |
|---|---|
| Docentes | Coordenação Dra. Carolina Gonçalves Dias Lima; 15 professores listados, entre eles DIPECVN. Dakir Polidoro, DR. Pablo Herthel de Carvalho, Dr. Paulo Vinicius Tertuliano Marinho e MSc. Ricardo Martins de Azevedo Castro Guglielmi |
| Módulos | 24 módulos, 500 h: neuroanatomia, neurofisiologia, neuroimagem (US, Rx, TC e RM), coleta de LCE, semiologia e localização de lesões, afecções da coluna, epilepsia, neuro-otologia com video-otoscopia; módulos presenciais em São Paulo, alguns de sexta à tarde a domingo, com avaliações presenciais |
| Formato e campus | Semipresencial, São Paulo |

**Objeções e respostas:**

| Objeção [SUPOSIÇÃO] | Resposta |
|---|---|
| "Qual a diferença entre esta e a de neurocirurgia e neuro-oncologia?" (H-A12.2) | "A turma aberta é a Pós-graduação em Neurologia e Neurocirurgia Veterinária, que começa em 08/05/2027." Não citar 677 nem 701 (em "verificar"). |
| "Preciso ter experiência em neurologia?" (Q12.3) | A ficha não traz público-alvo: [CONFIRMAR NO CATÁLOGO] antes de responder. Até lá: "O curso começa pela neuroanatomia e pela neurofisiologia." |
| "Alguns módulos vão de sexta a domingo." | "Sim, e estão marcados no cronograma; a avaliação presencial é na sexta à tarde." |

**Palavras e frases.** Usar: exame neurológico, localização de lesão, neuroimagem, LCE, raciocínio clínico. Evitar: "reconhecimento pelo MEC" (texto da ficha), cupom do Workshop de Neuromonitorização (não vale para a Pós), "pós em neuro vet" no texto visível.

**Exemplos de título e chamada [SUPOSIÇÃO de texto]:**
- Título: "Pós-graduação em Neurologia e Neurocirurgia Veterinária: do exame neurológico à neurocirurgia"
- Título: "Localizar a lesão com segurança: veja o cronograma da turma de 08/05/2027"
- Chamada: "Confira os módulos presenciais e as datas de avaliação."

**Turma da área:**

| Código | Curso | Campus | Início (planilha) | Turma | Preço e condições (catálogo) | Para peça |
|---|---|---|---|---|---|---|
| 68616 | Pós-graduação em Neurologia e Neurocirurgia Veterinária | São Paulo | 08/05/2027 | IX | 30x de R$ 1.192,40 no cartão ou boleto (total de R$ 35.772,00), mais matrícula de R$ 250,00 | liberada |

Prova de bolsa da área no catálogo: 68654. Sem peça nesta rodada.

---

## 14. A13. Medicina felina (sem turma de Pós no recorte)

A área não tem turma de Pós aberta (650 em "verificar"). Segue o posicionamento-pos (seção 3.1): **sem casa de mensagens de venda de Pós em Felinos** até existir turma aberta. A prova de bolsa 68652 existe no catálogo, sem turma de destino [CONFIRMAR], e fica fora desta rodada (decisão 14). Conteúdo de felinos aparece como tema dentro de outras áreas, sempre pela ficha: dor e analgesia em felinos (657, módulo 5), dermatopatias em felinos (68610, módulo 12), geriatria felina (699, módulos 9 e 10), reabilitação em felinos (366). Nunca "cat friendly" como selo.

---

## 15. A14. Outras especialidades (por curso: 679, 382, 699, 341, 60, 719)

### 15.1 679. Pós-graduação em Infectologia Veterinária

- **Público e momento.** Clínico de pequenos animais que lida com doenças infecciosas, zoonoses e antibioticoterapia na rotina [SUPOSIÇÃO].
- **Promessa central.** Infectologia de cães e gatos da coleta da amostra à antibioticoterapia e ao controle de infecção hospitalar.
- **Pilares de prova (ficha):** docentes: coordenação Ricardo L. S. Gonzalez (titulação não consta na ficha); 6 professores listados, entre eles Dra Nadia Rossi de Almeida, Msc Thais M. Chucri e Dr. Paulo Tabanez. Módulos: 24 módulos, 500 h; 3 módulos presenciais (prática laboratorial de coleta e envio de amostras; zoonoses com coleta de material para exame de raiva; controle de infecção hospitalar). Formato: semipresencial, São Paulo.
- **Objeções:** (1) "É muito teórico?": "São 3 módulos presenciais de prática laboratorial e de controle de infecção, com as datas no cronograma; o resto é online." (2) "Preço": texto-padrão completo, sem comparação. (3) "Tempo": base comum da seção 1.
- **Usar:** zoonoses, antibioticoterapia, sepse, controle de infecção. **Evitar:** "única pós semipresencial em infectologia veterinária do mundo" (texto da ficha, sem fonte), "melhoria de sua empregabilidade" (texto da ficha, promessa).
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Infectologia Veterinária: de zoonoses à sepse"; "Veja o cronograma da turma de 03/04/2027."
- **Turma:** 679, São Paulo, início 03/04/2027, turma IV, 30x de R$ 1.100,00 no cartão ou boleto (total de R$ 33.000,00), mais matrícula de R$ 250,00. Link da planilha trocado na campanha (P3): conferir antes de anúncio.

### 15.2 382. Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos

- **Público e momento.** Clínico que atende reprodução, gestação e neonatos, e quem trabalha com canis e gatis [SUPOSIÇÃO, persona 5.2].
- **Promessa central.** Reprodução de cães e gatos do exame ginecológico e andrológico à neonatologia, com prática presencial em cada etapa.
- **Pilares de prova (ficha):** docentes: coordenação ESP. Patricia Salla e Dra. Marilu Martins Gioso.; 6 professores listados, entre eles DR. JULIO KEN NAGASHIMA, DRA. Rafaela Beatriz Pintor Torrecilha e DR. Tarso Felipe Teixeira. Módulos: 24 módulos, 500 h; 8 módulos presenciais (exame ginecológico e inseminação, exame andrológico e criopreservação de sêmen, ultrassonografia reprodutiva, cirurgias do aparelho reprodutivo, obstetrícia, neonatologia, manejo de canis e gatis, inseminação intrauterina cirúrgica). Formato: semipresencial, São Paulo.
- **Objeções:** (1) "É para clínico ou para criador?": a ficha não traz público-alvo [CONFIRMAR NO CATÁLOGO]. (2) "Preço": texto-padrão. (3) "Viagem": 8 módulos presenciais com mês marcado; compre passagem só com a turma confirmada.
- **Usar:** obstetrícia, neonatologia, inseminação, exame andrológico. **Evitar:** "criador" como público sem confirmação, promessa de resultado reprodutivo.
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos: 8 módulos práticos"; "Veja a primeira turma, com início em 22/05/2027."
- **Turma:** 382, São Paulo, início 22/05/2027, turma I, 30x de R$ 1.125,00 no cartão ou boleto (total de R$ 33.750,00), mais matrícula de R$ 250,00.

### 15.3 699. Pós-graduação em Geriatria Veterinária

- **Público e momento.** Clínico que atende cada vez mais cães e gatos idosos [SUPOSIÇÃO]. A ficha amplia o público para estudantes a partir do último ano: contradição com o ingresso por diploma [CONFIRMAR antes de qualquer peça].
- **Promessa central.** Cuidar do paciente idoso de forma integrada: farmacologia, dor, cognição, felinos e comunicação com o tutor, numa especialização dedicada à geriatria.
- **Pilares de prova (ficha):** docentes: coordenação Prof. Caio Cavalcanti Balençuela; 32 professores listados, entre eles Dra. Ayne Hayashi, Profa. Denise Fantoni, Dra. Angélica Safatle e Msc. Christian Jordan (Palestrante internacional - Lima, Peru). Módulos: 20 módulos, 500 h; polifarmácia e desprescrição, comunicação de más notícias, síndrome da disfunção cognitiva, geriatria felina; 2 módulos presenciais (um deles com acupuntura, fisioterapia e avaliação funcional). Formato: semipresencial, São Paulo. Turma: mínimo 15 e máximo 40 (ficha).
- **Objeções:** (1) "Geriatria não é só clínica médica?": "É o paciente idoso por inteiro: farmacologia, cognição, dor, felinos e comunicação com a família, num programa só." (2) "Quase tudo é online": "Sim, 2 módulos presenciais; o restante é online." (3) "Preço": texto-padrão.
- **Usar:** paciente idoso, polifarmácia, disfunção cognitiva, comunicação com o tutor. **Evitar:** "única", "pioneira", "primeira pós de geriatria", estudante como público.
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Geriatria Veterinária: o cão e o gato idosos por inteiro"; "Veja o cronograma da primeira turma."
- **Turma:** 699, São Paulo, início 22/05/2027, turma I, 24x de R$ 1.375,00 no cartão ou boleto (total de R$ 33.000,00), mais matrícula de R$ 250,00. Peça só depois de corrigir a ficha (público e ordem do cronograma).

### 15.4 341. Pós-graduação em Medicina Interna Equina

- **Público e momento.** Veterinário de equinos, que atende a campo, com pouca prática hospitalar na graduação (texto da ficha; H-A14.1) [SUPOSIÇÃO de perfil]. Não é o público de pequenos animais.
- **Promessa central.** Medicina interna equina com prática: do paciente crítico ao potro neonato, com aulas práticas em hospital veterinário.
- **Pilares de prova (ficha):** docentes: coordenação Esp. Maria Augusta Berlingieri; 9 professores listados, entre eles Dra. Patrícia Brossi, Dr. Marlos Gonçalves Sousa, Dra. Roberta Basile e Dr.Júlio Spagnolo. Módulos: 24 módulos, 500 h; paciente crítico, cardiologia, trato respiratório e digestivo, claudicação, neonatologia e UTI neonatal, podologia; vários módulos com parte presencial [CONFIRMAR quantos]. Local: a ficha lista a sede em São Paulo e um endereço em Indaiatuba (SP) e diz que as aulas práticas são em hospital veterinário [CONFIRMAR onde é a prática com cavalos].
- **Objeções:** (1) "Onde é a prática com cavalos?" (H-A14.3): só responder depois da confirmação do local. (2) "A promoção de 20% vale para mim?" (H-A14.2): não citar até a regra completa; "Fale com o time sobre condições." (3) "Preço": texto-padrão sem desconto.
- **Usar:** equino, paciente crítico, claudicação, neonato, prática hospitalar (com o local confirmado). **Evitar:** "20% de desconto", "aproveite", "bolsa" (não há prova de equinos), "inseguros e sem nenhum diferencial competitivo" (texto da ficha, ofende o público).
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Medicina Interna Equina: do paciente crítico ao potro"; "Veja os módulos da primeira turma, com início em 20/03/2027."
- **Turma:** 341, São Paulo, início 20/03/2027, turma I, 30x de R$ 1.450,00 no cartão ou boleto (total de R$ 43.500,00), mais matrícula de R$ 250,00 (sem a promoção em peça).

### 15.5 60. Pós-graduação em Medicina de Silvestres

- **Público e momento.** Veterinário que atende pets não convencionais, silvestres e exóticos, público menor e disperso [SUPOSIÇÃO].
- **Promessa central.** Peixes, anfíbios, répteis, aves e mamíferos silvestres numa especialização só, com módulos práticos presenciais.
- **Pilares de prova (ficha):** docentes: coordenação Carolina Nery (titulação não consta na ficha); 10 professores listados, entre eles ESP. SORAYA MALAGA, Mestre Laura Crispim Reisfeld, MSC. ANDRÉ GRESPAN e Dra Fernanda Passos Nunes. Módulos: 18 módulos, 360 h, por grupo animal; 4 módulos presenciais de aula prática; horários de sexta das 14h às 20h, sábado das 8h às 18h e domingo das 8h às 13h. Formato: semipresencial, São Paulo. Turma mínima de 15 alunos (ficha).
- **Objeções:** (1) "Módulos de sexta a domingo": "Sim, com os horários na página; planeje a agenda com as datas do cronograma." (2) "Preço": texto-padrão. (3) "Vale para quem atende só pets não convencionais?": revisão docente [CONFIRMAR].
- **Usar:** pets não convencionais, silvestres, exóticos, manejo, anestesia de silvestres. **Evitar:** o número de mercado da página (R$ 77,3 bilhões) e os números de espécies, sem fonte conferida.
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Medicina de Silvestres: de peixes a mamíferos, com 4 módulos práticos"; "Veja os horários e o cronograma da primeira turma."
- **Turma:** 60, São Paulo, início 28/05/2027, turma I, 24x de R$ 1.237,50 no cartão ou boleto (total de R$ 29.700,00), mais matrícula de R$ 250,00.

### 15.6 719. Pós-graduação em Inteligência Artificial na Saúde

- **Público e momento.** Fora das personas veterinárias: público da ficha "Médicos, Enfermeiros, Gestores de Saúde, Profissionais de TI e Engenheiros Clínicos". Persona própria [CONFIRMAR] (persona 5.1).
- **Promessa central.** IA aplicada à saúde com prática de prompts e agentes, respeitando LGPD e ética no tratamento de dados sensíveis.
- **Pilares de prova (ficha):** docentes: coordenação Prof. Ricardo Bontempo; 3 professores listados (João Carlos Bombardelli, Claudiney Sanches Junior, Paulo Alberto Simões; titulação não consta). Módulos: 15 módulos, 360 h; Machine Learning e Deep Learning, engenharia de prompts para LLMs, agentes de atendimento e suporte à decisão, LGPD; 3 módulos presenciais; metodologia PBL e ensino híbrido. Formato: semipresencial, São Paulo; exige notebook com processador i3, Windows e 8 GB de RAM (ficha).
- **Objeções:** (1) "Serve para veterinário?" (H-A14.4): a ficha não cita veterinária; não anunciar para o público veterinário sem decisão [CONFIRMAR]. (2) "Uso Mac" (H-A14.5): dizer o requisito como está na ficha. (3) "Preço": texto-padrão.
- **Usar:** IA na saúde, LGPD, prompts, agentes. **Evitar:** "alinhando-se às normas do Ministério da Educação" (texto da ficha), promessa de liderança ou cargo, chamar de "Pós-Graduação".
- **Títulos e chamadas [SUPOSIÇÃO de texto]:** "Pós-graduação em Inteligência Artificial na Saúde: prompts, agentes e LGPD"; "Veja o requisito de notebook e o cronograma antes de se inscrever."
- **Turma:** 719, São Paulo, início 08/05/2027, turma I, 18x de R$ 666,67 no cartão ou boleto (total de R$ 12.000,00), mais matrícula de R$ 250,00. Ato regulatório para saúde humana [CONFIRMAR NO CATÁLOGO].

Prova de bolsa da área no catálogo: 68655 (Odontologia, sem turma de destino). Sem peça nesta rodada.

---

## 16. Auditorias aplicadas (autochecagem, antes do qa-de-marketing)

| Item (auditorias/02 e conformidade-educacional) | Situação |
|---|---|
| Dado de curso só do catálogo ou da ficha | Sim; preço copiado do catálogo sem arredondar; datas da planilha pelo catálogo |
| Sem certificação, MEC, título | Sim; frases das fichas listadas em "evitar" |
| Sem urgência falsa, sem "últimas vagas" | Sim; reta final só com data e "fale com o time" |
| Preço só com condições completas | Sim; 662 sem preço; descontos fora |
| Sem promessa de emprego, renda, aprovação | Sim |
| Docentes com nome e titulação da ficha | Sim, grafia da ficha; autorização pelas decisões 8 e 10 |
| Turma mínima de 15 | Sim (decisão 11) |
| Voz do candidato marcada | Sim, tudo [SUPOSIÇÃO] |
| Provas de bolsa sem peça | Sim (decisão 14) |
| Nome "Pós-graduação em <área>" | Sim |
| Sem travessão nem meia-risca | Conferido por busca de U+2014 e U+2013 |

**Próximo agente sugerido:** criador-de-ganchos (2.3), depois criativos-de-anuncio (2.4) e autoridade-docente (2.5). Para A14 e as turmas da onda 1, a camada 3 reaproveita estas seções.

---

## Lista 1. Fatos (com fonte)

- Preço, parcelas, matrícula, campus, modalidade, carga horária, turma e status das 30 turmas: contexto/catalogo-de-cursos.md, seção 2 (site, 26/10/2026).
- Datas de início pela planilha, inclusive 698 em 28/11/2026, 352 em 24/05/2027, 366 em 10/04/2027 e 662 em 24/04/2027: catálogo e decisão 12 da Ufape.
- Turma mínima de 15 alunos na Pós: decisão 11 da Ufape (26/10/2026); contexto/pos-graduacao.md.
- Autorização de imagem e citação de docentes, coordenadores e convidados: decisões 8 e 10 da Ufape.
- Coordenação, professores listados, módulos, módulos presenciais e textos citados de cada turma: fichas em contexto/cursos/pos/ (26/10/2026).
- 68632 é a única turma presencial do recorte; as demais são semipresenciais: catálogo.
- 68623: localidade Goiânia no catálogo e na ficha ("Ufape Goiânia"), com o texto "Aulas Práticas (Presenciais)- Unidade São Paulo" na mesma ficha.
- Descontos de 341, 359 e 352 só nas fichas ou com texto cortado: estrategia-de-oferta-pos, seção 1.3.
- Texto-padrão de preço e regra da 1ª mensalidade vencida: estrategia-de-oferta-pos, seção 2.1.
- Provas de bolsa por área (códigos): plano do cmo, seção 2.3; catálogo, seção 3.
- Proibição de peças de provas de bolsa nesta rodada: decisão 14 da Ufape.

## Lista 2. Suposições

- [SUPOSIÇÃO] Todas as frases "nas palavras do candidato" e todas as objeções por área: hipóteses de insights-de-alunos-pos e pesquisa-de-persona-pos, sem voz real.
- [SUPOSIÇÃO] Público e momento de carreira de cada área (persona P1 e variações da seção 5 da pesquisa de persona).
- [SUPOSIÇÃO] Todos os exemplos de título, chamada e linha por estágio são texto proposto por este agente.
- [SUPOSIÇÃO] Texto "Fale com o time para saber como entrar na turma" para turmas com a 1ª mensalidade vencida (regra 3 da estrategia-de-oferta-pos).
- [SUPOSIÇÃO] Aplicar a regra da 1ª mensalidade vencida também a 698 (mesmo início de 68610 e 68608).

## Lista 3. Dados que faltam ([CONFIRMAR])

- [CONFIRMAR] Local dos módulos presenciais de 68623 (Goiânia ou São Paulo).
- [CONFIRMAR] Local da prática com cavalos de 341 (São Paulo, Indaiatuba ou hospital veterinário citado) e quantidade de módulos presenciais.
- [CONFIRMAR] Regra completa da promoção de 341 e dos descontos de 359 e 352 (fora de peça até lá).
- [CONFIRMAR] Pré-requisito de 657, 359 e 698; público-alvo de 68616 e 382; público de 699 (estudante do último ano) e ordem do cronograma.
- [CONFIRMAR] Dados de 662 (link trocado, P3): preço, turma, cronograma e docentes desta turma.
- [CONFIRMAR] Número da turma de 68617 e 68628 (planilha e site divergem).
- [CONFIRMAR com a planilha] Datas de 68636, 68629 e 359 (só no site).
- [CONFIRMAR] Correção da data de 698 no site (pedido A6) antes de anúncio novo.
- [CONFIRMAR] Coordenação de 68632; coordenação nomeada de 68610, 578, 366 e 333; corpo docente de 333.
- [CONFIRMAR] Regra de entrada tardia para 707, 68604, 68606, 68610, 68608 e 698 (PR4).
- [CONFIRMAR] Data em que cada turma é confirmada e o que entra em "valores de inscrição" no reembolso.
- [CONFIRMAR] Regra de reposição de módulo presencial.
- [CONFIRMAR] Regras do estágio e do grupo de discussão de 68606; formato dos plantões de dúvidas de 68610; prática de endoscopia em 68606.
- [CONFIRMAR] Requisito de equipamento próprio em 68604 e 68629; número de alunos por estação nas práticas.
- [CONFIRMAR] Persona e canal de 719 e ato regulatório para saúde humana; se 719 entra em peça para veterinários.
- [CONFIRMAR] Resolução citada na ficha de 366, com a regulação, antes de peça.
- [CONFIRMAR] Número de módulos presenciais de 68617, 68615, 68623 e 68616.
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação da Pós.
