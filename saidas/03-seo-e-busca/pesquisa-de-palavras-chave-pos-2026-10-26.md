# Pesquisa de palavras-chave e perguntas de IA da Pós-graduação, por área de especialidade (A1 a A14)

- Agente: pesquisa-de-palavras-chave (etapa 2.1 da camada 2)
- Linha: pos
- Data: 26/10/2026
- Status: rascunho corrigido após o veredito do qa-de-marketing (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep03.md), para nova passagem pelo qa-de-marketing (auditoria 03-busca e auditorias/conformidade-educacional.md). Nada é publicado, enviado ou pago. Nenhuma ação em anúncio, CRM ou site foi feita.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md (inclusive a seção "Padrão de nome")
  - contexto/catalogo-de-cursos.md (seções 2 e 3 e o cabeçalho "Como usar"; é a única fonte de dado de curso deste arquivo)
  - .claude/skills/agrupar-palavras-chave/SKILL.md, .claude/skills/briefing-seo/SKILL.md e .claude/skills/visibilidade-em-ia/SKILL.md
  - saidas/03-seo-e-busca/lacunas-de-conteudo-pos-2026-10-26.md (entrada principal)
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 2.3, as 14 áreas, e seção 4, camada 2)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep03.md (veredito, seção 4)
- Pesquisa na web: 20 consultas com WebSearch em 26/10/2026 (fontes na seção "Fontes"). Nenhuma página de origem foi aberta. Não tentei abrir faculdade.ufape.com.br. Não li as fichas de contexto/cursos/ nem o template templates/pagina-da-turma.md nesta rodada: o esqueleto de H2 da seção 2.5 é proposta e o template prevalece.
- Dados pessoais: nenhum. Docentes não são nomeados.

---

## 1. Resumo para quem decide

1. **Escopo:** 14 áreas, 31 páginas de curso (turmas abertas do recorte, mais os pilares de Cardiologia, Anestesiologia e Clínica Cirúrgica, que juntam várias turmas), 22 provas de bolsa em 19 especialidades e a campanha das provas. Cada palavra-chave principal liga a uma única página. Cada área tem de 10 a 15 termos e de 5 a 7 perguntas para assistentes de IA, todos pontuados.
2. **O que a busca mostrou:** nas consultas de curso por área, os resultados são agregadores (Quero Bolsa, Guia da Carreira, EAD.com.br), blogs de faculdades, editais de concorrentes e currículos de terceiros. Nenhuma página de curso da Ufape apareceu entre os resultados de "pós-graduação em <área>". A única página da Ufape que apareceu foi o edital de aprimoramento em terapia intensiva (faculdade.ufape.com.br). A busca por "presencial" devolveu quase só oferta EAD: há espaço para "semipresencial e presencial" em dermatologia, oftalmologia e Goiânia [SUPOSIÇÃO]. O WebSearch não é uma página de resultados do Google: ausência é indício, não prova.
3. **Nichos com menos disputa visível** (a busca não trouxe pós brasileira lato sensu específica): ecocardiografia veterinária, gastroenterologia veterinária (resultados dominados por medicina humana), hematologia e citopatologia veterinárias, ortopedia veterinária [SUPOSIÇÃO]. São as melhores apostas de facilidade.
4. **Áreas de cabeça de termo caro:** dermatologia, oncologia, oftalmologia e clínica médica têm muita oferta EAD barata em agregador. A Ufape deve disputar por formato (semipresencial, módulos práticos) e por termos de cauda (cidade, prova de bolsa), não pelo termo curto.
5. **Termos que não podem virar peça agora:** título de especialista e certificado (texto oficial vazio, [PREENCHER COM A REGULAÇÃO]), EAD (a Ufape não tem turma EAD aberta; 586 está em "verificar"), turmas iniciadas em "verificar" (sem chamada de compra), Oftalmologia na prova de bolsa (68656 fora do ar) e as provas 68652, 68649, 68653 e 68655 até a Ufape informar a turma de destino.
6. **Prazo:** 707, 68604 e 68606 começam em 4, 5 e 12 dias. Página nova não ranqueia a tempo [SUPOSIÇÃO]. O ganho de 707, 68604 e 68606 está na próxima edição, na prova de 27/11 e na citação por IA. Para 698, 68610 e 68608 (28/11) e para a prova de 27/11, o que vale é anúncio de busca por termo de cauda e a página corrigida.
7. **Próximo agente:** lacunas-de-conteudo já rodou (entrada deste arquivo). Seguem o briefing-de-conteudo (etapa 2.7) e o mensagens (etapa 2.2), que reaproveitam os termos principais e as perguntas daqui.

---

## 2. Método, escalas e limites

### 2.1 O que foi feito

1. Para cada área, parti dos cursos e das provas do recorte (códigos do catálogo, seções 2 e 3) e das lacunas da entrada principal.
2. Consultei a web (20 consultas) para ver quem aparece, em que formato, e que termos os títulos e subtítulos dos resultados usam. Anotei só o que o resumo de busca mostrou.
3. Expandi cada tema nos padrões da seção 2.2 e nas sete intenções pedidas: comparar instituições, entender a especialização, preço e condições, prova de bolsa, carreira e título de especialista, EAD x presencial e Goiânia.
4. Classifiquei cada termo e cada pergunta pela intenção (aprender, comparar, matricular, resolver) e pontuei.
5. Escrevi as perguntas completas para assistentes de IA (ChatGPT, Gemini, Perplexity, Claude), do jeito que o candidato digita, no roteiro da skill visibilidade-em-ia: problema, solução, comparação e decisão.
6. Agrupei em pilar e apoio (skill agrupar-palavras-chave) e escrevi o briefing SEO resumido de cada página de curso.

### 2.2 Padrões de variação de termo

| Padrão | Exemplo | Uso |
|---|---|---|
| Nome completo | pós-graduação em dermatologia veterinária | termo principal da página de curso |
| Cidade | pós em dermatologia veterinária em São Paulo; pós em cardiologia veterinária em Goiânia | cauda de maior chance de matrícula |
| Modalidade | pós em dermatologia veterinária semipresencial, presencial, EAD | comparar |
| Especialização e espécie | especialização em dermatologia de cães e gatos | variação do termo principal |
| Preço | quanto custa; valor; mensalidade; parcelas | resolver |
| Prova de bolsa | prova de bolsa de dermatologia veterinária | resolver |
| Carreira | vale a pena; como se especializar; título de especialista | aprender e comparar |
| Nome popular | pós em cardio vet; especialização em felinos; pós em derma vet | só em lista de palavras-chave e em palavra de grupo de anúncio |

Regra de nome (contexto/pos-graduacao.md): título, H1, H2, anúncio, FAQ e qualquer texto visível ao candidato usam "Pós-graduação em <área>". "Pós em", "pós vet" e abreviações aparecem só em listas de palavras-chave e em palavras de grupo de anúncio (o que o candidato digita), nunca em texto visível. A marca nos títulos é "Faculdade UFAPE", para separar da Universidade Federal do Agreste de Pernambuco, que usa a mesma sigla e aparece na busca por "ufape" (lacunas, T9). Nas tabelas, título e marca vêm separados por vírgula para não quebrar a coluna; o título final pode usar a barra vertical como separador entre o nome do curso e a marca.

### 2.3 Pontuação (skill visibilidade-em-ia)

Pontuação = M + D + F, de 0 a 80. O componente "lacuna em IA" (0 a 20) fica de fora, porque só existe com checagem real em assistentes, que a squad não faz. Cada célula mostra "total (M/D/F)".

- M, intenção de matrícula (0 a 30): matricular de 26 a 30; resolver de 20 a 26; comparar de 14 a 20; aprender de 4 a 10.
- D, demanda (0 a 25): sem dado de ferramenta, qualitativa: Alto = 20, Médio = 14, Baixo = 8. Todo volume é [SUPOSIÇÃO], tirado de quantidade de ofertas em agregadores, de matérias de "mais procuradas" e do tipo de termo. Não há volume numérico em nenhuma linha.
- F, facilidade (0 a 25): chance real de a Ufape vencer. Cabeça de termo contra agregadores de 6 a 12; termo intermediário de 14 a 18; cauda com página própria e pouca concorrência visível de 18 a 24.
- Corte: abaixo de 32 (40 sobre 100, proporcional ao teto de 80) não vira página nem anúncio; fica como apoio ou descartado [SUPOSIÇÃO: regra prática da skill, não meta].
- Tipo: toda linha de "Palavras-chave" é busca; toda linha de "Perguntas para IA" é IA.
- A coluna "Ufape aparece em assistentes" fica "conferir manualmente" em todas as perguntas (roteiro na seção 8).

### 2.4 Prioridade

- P1: intenção de matricular ou resolver, com turma em março de 2027 ou antes, ou prova de 27/11/2026.
- P2: turma de abril e maio de 2027, ou página de apoio à decisão (guia, FAQ).
- P3: conteúdo informativo, termo bloqueado por regulação ou turma em "verificar".

### 2.5 Briefing SEO: esqueleto e bloco citável

Esqueleto de H2 para toda página de curso (proposta; o template templates/pagina-da-turma.md prevalece). Todo H2 que cita o curso usa "Pós-graduação em <área>":

1. Para quem é a Pós-graduação em <área>.
2. O que você vai estudar (módulos e cronograma da ficha).
3. Como funcionam as aulas (online e módulos presenciais).
4. Turmas, local e datas.
5. Investimento e formas de pagamento (parcelas, valor da parcela, total e matrícula, do catálogo).
6. Prova de bolsa de estudos da Pós-graduação em <área> (só quando houver prova da área no catálogo).
7. Coordenação e docentes [CONFIRMAR autorização].
8. Perguntas frequentes (bloco T2 da entrada principal, mais as da área).

Não existe H2 de certificação nem frase de certificação em nenhuma página: o texto oficial está vazio.

Bloco citável do topo (40 a 60 palavras), molde com campos do catálogo: "[Nome padrão do curso] é uma especialização para médicos veterinários da Faculdade UFAPE, em [local], na modalidade [modalidade do catálogo], com [carga horária] horas. A turma [número] começa em [data da planilha]. O pagamento é em [n] parcelas de [valor], mais matrícula de [valor]." O briefing-de-conteudo preenche cada campo a partir do catálogo e marca [CONFIRMAR NO CATÁLOGO] no que faltar.

Limite de caracteres: título até cerca de 60 e descrição até cerca de 155, para não cortar no resultado de busca.

### 2.6 Limites

- O WebSearch não devolve as sugestões do Google (preenchimento automático) nem a caixa "As pessoas também perguntam". As variações de termo e de pergunta deste arquivo vêm de: títulos e subtítulos dos resultados, nomes de cursos em agregadores, padrões do roteiro, nomes populares informados no pedido e a persona. A formulação exata é [SUPOSIÇÃO]. Antes de investir em anúncio, conferir as sugestões do Google e o Search Console (seção 8).
- Não há volume. Nenhuma exportação de ferramenta foi fornecida.
- Não consultei nenhum assistente de IA. Nenhuma taxa de citação foi inventada.
- Dados de curso (nome, modalidade, CH, local, início, turma, status) vêm só do catálogo. O que só existe nas fichas leva [CONFIRMAR NO CATÁLOGO].
- Perguntas de tutor ("meu gato está com...") ficam fora: o público é o médico veterinário.
- Linha Pós apenas. Cursos livres e o workshop de Neuromonitorização (linha Eventos) aparecem só como link, nunca no mesmo cluster.
- Nenhum termo com nota do MEC, "reconhecida pelo MEC" ou certificação.

---

## 3. Termos e perguntas transversais (valem para as 14 áreas)

Páginas de destino: T1 hub da prova de bolsa, T4 guia "Como escolher uma Pós-graduação em Medicina Veterinária", T5 "Pós-graduação, residência, aprimoramento e curso livre: qual a diferença", T6 explicador de título de especialista (bloqueado), T7 "Como funciona a Pós-graduação semipresencial da Faculdade UFAPE, mês a mês", T8 "Investimento e formas de pagamento" (códigos da entrada principal). Listagens por praça são proposta [SUPOSIÇÃO: o site pode já ter uma página de listagem; [CONFIRMAR]].

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| KT1 | Comparar instituições | pós-graduação em medicina veterinária | comparar | Alto | 40 (14/20/6) | Listagem das pós (categoria) | Cabeça de termo dominada por agregadores; usar como categoria e links internos, não como alvo de ranqueamento |
| KT2 | Comparar instituições | melhores pós-graduações em medicina veterinária; pós mais procuradas | comparar | Alto | 44 (14/20/10) | T4 | Matérias do Quero Bolsa e Pravaler ocupam o termo. Guia por critérios, sem ranking e sem nomear concorrente |
| KT3 | Comparar instituições | como escolher pós-graduação em medicina veterinária | comparar | Médio | 48 (16/14/18) | T4 | Critérios objetivos: carga prática, formato, parcelas, turma mínima |
| KT4 | Comparar instituições | prova de bolsa anclivepa; pós anclivepa | comparar | Médio | 36 (14/14/8) | Sem página própria | Termo de marca do concorrente. Não criar página nem anúncio sem decisão humana (risco de marca) [CONFIRMAR com jurídico]. Atender a dúvida no hub, sem nomear |
| KT5 | EAD x presencial | pós em medicina veterinária EAD | comparar | Alto | 40 (14/20/6) | T4 (seção EAD x semipresencial) | A Ufape não tem turma EAD aberta. Página honesta sobre o formato, sem prometer EAD |
| KT6 | EAD x presencial | pós em medicina veterinária semipresencial | comparar | Médio | 52 (20/14/18) | T7 | Descreve 1 módulo por mês, aulas online e módulos presenciais (contexto da linha) |
| KT7 | EAD x presencial | pós EAD ou presencial qual vale mais | comparar | Médio | 46 (14/14/18) | T4 e T7 | Resultados de busca trazem blogs de faculdades e a revista do Quero Bolsa. Sem afirmar equivalência de valor |
| KT8 | Entender | pós-graduação ou residência em medicina veterinária | comparar | Médio | 48 (16/14/18) | T5 | Alternativa nomeada pela persona P3. A busca mostrou fonte antiga sobre a residência como pós lato sensu; conferir [REVISÃO REGULAÇÃO] |
| KT9 | Entender | aprimoramento ou pós em medicina veterinária | comparar | Baixo | 40 (14/8/18) | T5 | Os aprimoramentos da Ufape estão em "verificar" ou "sem venda": só como exemplo de categoria |
| KT10 | Carreira e título | pós lato sensu dá título de especialista CFMV | aprender | Médio | 36 (10/14/12) | T6 (bloqueado) | A busca trouxe guias e CRMV que dizem que o certificado não é o título e que o título é registrado pelo CRMV. Nada sobre a Ufape até [PREENCHER COM A REGULAÇÃO] |
| KT11 | Carreira e título | como se tornar especialista em medicina veterinária | aprender | Médio | 34 (8/14/12) | T5 e T6 | Mesma trava |
| KT12 | Carreira e título | pós em medicina veterinária vale a pena | aprender | Médio | 38 (8/14/16) | T4 | Sem promessa de renda ou emprego |
| KT13 | Preço e condições | quanto custa pós em medicina veterinária | resolver | Alto | 56 (22/20/14) | T8 | Agregador mostra 952 ofertas de R$ 60,00 a R$ 2.235,84 (valores promocionais). A Ufape compete por prática e parcelas claras, sem comparar preço |
| KT14 | Preço e condições | pós em medicina veterinária parcelado; com bolsa | resolver | Médio | 52 (22/14/16) | T8 e T1 | Mostrar parcelas, valor, total e matrícula do catálogo |
| KT15 | Preço e condições | pós em medicina veterinária 2027 | matricular | Médio | 54 (24/14/16) | Listagem das pós | Turmas abertas de 2027 no catálogo; datas por curso |
| KT16 | Goiânia | pós em medicina veterinária Goiânia | matricular | Médio | 58 (28/14/16) | Listagem Goiânia [SUPOSIÇÃO] | O agregador mostra 996 ofertas para Goiânia, quase todas EAD; nenhuma pós presencial concorrente apareceu. Turmas Ufape em Goiânia: 289, 68632, 68609 e 68623 |
| KT17 | Goiânia | pós presencial Goiânia veterinária | matricular | Baixo | 54 (28/8/18) | 68632 (Clínica Cirúrgica, presencial) | Única turma com modalidade "presencial" no recorte (catálogo); frequência e jornada [CONFIRMAR NO CATÁLOGO] |
| KT18 | Prova de bolsa | prova de bolsa pós-graduação veterinária | resolver | Médio | 60 (28/14/18) | T1 (hub) | Concorrente de marca tem edital com taxa de R$ 350,00 e inscrição até 07/11/2026 (resumo de busca, [CONFIRMAR no edital]) |
| KT19 | Prova de bolsa | como funciona a prova de bolsa de pós veterinária | resolver | Médio | 56 (24/14/18) | T1 | Regras do contexto da linha, com contradições [CONFIRMAR NO CATÁLOGO] |
| KT20 | Marca | faculdade ufape pós-graduação; ufape intercursos | matricular | Baixo | 58 (26/8/24) | Página institucional e listagem | A busca por "Ufape Intercursos" devolveu o edital da Ufape e a universidade federal homônima. Marca precisa de página institucional (T9) |

### Perguntas transversais para assistentes de IA

| ID | Pergunta (como o candidato digita) | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| QT1 | Pós-graduação em medicina veterinária ou residência: qual vale mais a pena para quem trabalha? | Comparação | comparar | 48 (16/14/18) | T5 | [REVISÃO REGULAÇÃO] |
| QT2 | Como funciona uma pós semipresencial em medicina veterinária? Preciso viajar todo mês? | Problema | resolver | 52 (22/14/16) | T7 | Cronograma e turma mínima do contexto; reposição de módulo [CONFIRMAR] |
| QT3 | Quanto custa uma pós em medicina veterinária na Ufape e como é o parcelamento? | Decisão | resolver | 56 (24/14/18) | T8 | Só dado do catálogo |
| QT4 | Como funciona a prova de bolsa da Ufape e quantas bolsas tem? | Decisão | resolver | 58 (26/14/18) | T1 | Regras com contradições entre fichas [CONFIRMAR NO CATÁLOGO] |
| QT5 | Pós lato sensu dá direito ao título de especialista do CFMV? | Problema | aprender | 36 (10/14/12) | T6 | Bloqueada. A página encaminha à secretaria |
| QT6 | Faculdade UFAPE é a mesma coisa que a UFAPE de Pernambuco? | Decisão | resolver | 44 (20/8/16) | Página institucional | Resposta com nome, CNPJ e sede do contexto geral; sem texto de credenciamento até a regulação |
| QT7 | Se a turma da pós não fechar, o que acontece com o meu dinheiro e a minha viagem? | Decisão | resolver | 52 (24/14/14) | FAQ T2 | Turma mínima e orientação de comprar passagem só com turma confirmada (contexto); regra de reembolso [CONFIRMAR] |
| QT8 | Existe pós em medicina veterinária presencial em Goiânia? | Solução | matricular | 54 (28/8/18) | Listagem Goiânia | 4 turmas no catálogo |
| QT9 | A pós da Ufape tem prova de bolsa? Qual é a inscrição? | Decisão | resolver | 56 (26/14/16) | T1 | Inscrição de R$ 100,00 (catálogo, seção 3) |

---

## 4. Seções por área (ordem de prioridade das lacunas)

Convenções de cada seção:
- Os códigos e os dados da tabela de páginas vêm do catálogo (26/10/2026). "Início" é o da planilha.
- Nome da página: nome padrão "Pós-graduação em <área>". Quando o nome do catálogo foge do padrão (por exemplo "Pós Graduação em Citopatologia Veterinária"), a página usa o padrão e a diferença vai para a observação.
- Endereço: /pos-graduacao/pos-graduacao-em-<área> [SUPOSIÇÃO: padrão do CMS, endereços novos dependem de SEO-04].
- Onde há duas turmas do mesmo curso, a palavra principal liga a uma única página (T3). Enquanto o site mantiver uma página por turma, a página que fica com o termo principal é a da turma aberta mais próxima e a outra recebe 301 ou canonical [CONFIRMAR com o time do site].
- O grupo "Goiânia" só aparece quando a área tem turma ou prova em Goiânia no catálogo. Sem turma, não existe termo local.
- Nenhuma tabela promete EAD: a Ufape não tem turma EAD aberta.
- Nas tabelas de briefing, a coluna "Título" mostra o nome do curso e a marca separados por vírgula.

---

### A2. Cardiorrespiratório (cardiologia, ecocardiografia, pneumologia, ventilação mecânica)

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 698 | Pós-graduação em Ecocardiografia | São Paulo, semipresencial, 370 h | 28/11/2026, III (o site mostra 2027, conflito P4) | aberto | pós-graduação em ecocardiografia veterinária | pós em ecocardiografia veterinária São Paulo; especialização em ecocardiografia de cães e gatos; pós em eco vet; ecocardiografia veterinária pós valor |
| 289 (e 68605) | Pós-graduação em Cardiologia Veterinária | Goiânia (289), semipresencial, 500 h; 68605 em São Paulo está em "verificar" | 289: 20/03/2027, II | aberto | pós-graduação em cardiologia veterinária | pós em cardiologia veterinária em Goiânia; especialização em cardiologia de cães e gatos; pós em cardio vet; prova de bolsa de cardiologia |
| 68636 | Pós-graduação em Pneumologia Veterinária | São Paulo, semipresencial, 500 h | 17/04/2027, VIII (data só no site, [CONFIRMAR NO CATÁLOGO]) | aberto | pós-graduação em pneumologia veterinária | especialização em pneumologia de cães e gatos; pós em pneumologia veterinária São Paulo; pós em pneumo vet |
| 352 | Pós-graduação em Ventilação Mecânica | São Paulo, semipresencial, 360 h | 24/05/2027, I (data diverge entre planilha e site, [CONFIRMAR NO CATÁLOGO]) | aberto | pós-graduação em ventilação mecânica veterinária | especialização em ventilação mecânica em cães e gatos; ventilação mecânica veterinária curso de especialização; pós em ventilação mecânica anestesia e UTI |
| 68641, 68642, 68659 | Provas de bolsa de Cardiologia (SP e Goiânia, links invertidos, P3) e de Pneumologia | SP e Goiânia, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de cardiologia veterinária (68641 e 68642); prova de bolsa de pneumologia veterinária (68659) | prova de bolsa pós cardiologia Goiânia; bolsa de estudos pós cardiologia veterinária |

Não há prova de bolsa de Ecocardiografia no catálogo: a página de 698 não cita prova. Se a prova de Cardiologia (68641 e 68642) valer para 698, [CONFIRMAR NO CATÁLOGO] antes de qualquer menção.

Fora do recorte, só por link: 68605 e 659 (verificar), 670 (encerrado, link fora do ar), livre 573 (Hands-On de Ecocardiografia, 14/11/2026) e 68618 (Ventilação Mecânica Aplicada à Anestesia, livre).

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K2.1 | Entender | pós-graduação em ecocardiografia veterinária | matricular | Médio | 62 (28/14/20) | Pilar Ecocardiografia (698) | A busca não trouxe pós brasileira específica; resultados de medicina humana e cursos no exterior. Melhor aposta da área. Data do site precisa de correção antes de anúncio novo |
| K2.2 | Entender | pós-graduação em cardiologia veterinária | matricular | Alto | 58 (28/20/10) | Pilar Cardiologia | Anclivepa-SP, agregadores e guias ocupam. Ufape não apareceu |
| K2.3 | Goiânia | pós em cardiologia veterinária em Goiânia | matricular | Baixo | 60 (30/8/22) | Pilar Cardiologia (289) | Cauda local, turma de março de 2027 |
| K2.4 | Entender | pós em ecocardiografia veterinária em São Paulo | matricular | Baixo | 60 (30/8/22) | Pilar Ecocardiografia | Turma de 28/11/2026 |
| K2.5 | Entender | pós-graduação em ventilação mecânica veterinária | matricular | Baixo | 56 (28/8/20) | Pilar Ventilação (352) | Ticket alto; público de UTI e anestesia [SUPOSIÇÃO] |
| K2.6 | Entender | pós-graduação em pneumologia veterinária | matricular | Baixo | 54 (28/8/18) | Pilar Pneumologia (68636) | 670 fora do ar; confirmar a página oficial |
| K2.7 | Nome popular | pós em cardio vet; especialização em cardio vet; pós em eco vet | matricular | Baixo | 52 (26/8/18) | Lista de palavras e grupo de anúncio | Não vai para título, H1, H2 nem texto visível |
| K2.8 | Preço e condições | quanto custa pós em cardiologia veterinária | resolver | Médio | 52 (22/14/16) | Seção de investimento do pilar e T8 | Parcelas, total e matrícula do catálogo |
| K2.9 | Prova de bolsa | prova de bolsa de cardiologia veterinária | resolver | Médio | 60 (26/14/20) | Provas 68641 e 68642 e hub T1 | Corrigir os links invertidos (P3) antes de anúncio |
| K2.10 | Comparar | cardiologia ou ecocardiografia veterinária: qual pós escolher | comparar | Baixo | 46 (16/8/22) | Guia A2 | Resolve a dúvida de nível (persona H-A2.3) |
| K2.11 | Comparar | pós em ecocardiografia ou curso hands-on de ecocardiografia | comparar | Baixo | 46 (16/8/22) | Guia A2, com link para o livre 573 | Livres entra só por link |
| K2.12 | EAD x presencial | pós em cardiologia veterinária EAD | comparar | Médio | 36 (14/14/8) | Guia A2 (resposta sobre formato) | Sem oferta EAD na área; não criar página de EAD |
| K2.13 | Carreira e título | título de especialista em cardiologia veterinária | aprender | Médio | 36 (10/14/12) | T6 (bloqueado) | [REVISÃO REGULAÇÃO] |
| K2.14 | Comparar instituições | pós em cardiologia veterinária Anclivepa | comparar | Médio | 36 (14/14/8) | Sem página própria | Edital de Cardiologia 2026 do concorrente apareceu; não nomear no conteúdo |
| K2.15 | Entender | o que faz um cardiologista veterinário | aprender | Médio | 32 (6/14/12) | Artigo de apoio | [REVISÃO DOCENTE]; no limite do corte |

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q2.1 | Existe pós só de ecocardiografia veterinária em São Paulo? Quanto tempo dura e quando começa? | Solução | matricular | 56 (28/8/20) | Topo do pilar Ecocardiografia | Dados: 370 h, semipresencial, início 28/11/2026 pela planilha (a página precisa trazer a data certa) |
| Q2.2 | Preciso fazer cardiologia veterinária antes de uma pós em ecocardiografia? | Decisão | resolver | 50 (24/8/18) | FAQ do pilar Ecocardiografia | Pré-requisito de 698 [CONFIRMAR NO CATÁLOGO] |
| Q2.3 | Qual a diferença entre pós em cardiologia veterinária e pós em ecocardiografia veterinária? | Comparação | comparar | 46 (16/8/22) | Guia A2 | Primeira frase responde sozinha |
| Q2.4 | Tem pós em cardiologia veterinária em Goiânia? Como são as aulas? | Solução | matricular | 54 (30/8/16) | Pilar Cardiologia | 289, semipresencial, 500 h |
| Q2.5 | Vale a pena fazer um curso hands-on de ecocardiografia ou a pós completa? | Comparação | comparar | 44 (16/8/20) | Guia A2 | Link para o livre 573 |
| Q2.6 | Como funciona a prova de bolsa de cardiologia da Ufape e quanto custa a inscrição? | Decisão | resolver | 56 (26/14/16) | Prova 68641 e 68642 e T1 | Inscrição de R$ 100,00 (catálogo) |
| Q2.7 | Pós em ventilação mecânica veterinária serve para quem não trabalha em UTI? | Problema | aprender | 40 (12/8/20) | FAQ do pilar Ventilação | [REVISÃO DOCENTE] |

**Pilar e apoio**

| Cluster | Pilar (uma palavra principal) | Apoio |
|---|---|---|
| Cardiologia | Pós-graduação em Cardiologia Veterinária | Guia A2; prova 68641 e 68642; FAQ da área; artigo "o que faz o cardiologista" (aprender) |
| Ecocardiografia | Pós-graduação em Ecocardiografia | Guia A2; link para o livre 573; FAQ de pré-requisito |
| Pneumologia | Pós-graduação em Pneumologia Veterinária | Prova 68659; ponte com Ventilação |
| Ventilação mecânica | Pós-graduação em Ventilação Mecânica | FAQ "serve para quem não é de UTI"; link para o livre 68618 |

Links: apoio liga para o pilar e para o guia; o pilar liga para o guia, para o FAQ e para o hub da prova. Intenção de aprender (artigos) fica em páginas separadas das de matricular.

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos (além do esqueleto) |
|---|---|---|---|---|
| Ecocardiografia (698) | Pós-graduação em Ecocardiografia, Faculdade UFAPE | Pós-graduação em Ecocardiografia para médicos veterinários, semipresencial, 370 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Ecocardiografia | Pós-graduação em Ecocardiografia, Cardiologia ou curso hands-on: por onde começar; Pré-requisitos da Pós-graduação em Ecocardiografia [CONFIRMAR NO CATÁLOGO]. Sem H2 de prova de bolsa (não há prova de Ecocardiografia) |
| Cardiologia (289) | Pós-graduação em Cardiologia Veterinária, Faculdade UFAPE | Pós-graduação em Cardiologia Veterinária, semipresencial, 500 h, turma em Goiânia. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Cardiologia Veterinária | Turma de Goiânia e turma de São Paulo da Pós-graduação em Cardiologia Veterinária [CONFIRMAR NO CATÁLOGO se a de SP entra] |
| Pneumologia (68636) | Pós-graduação em Pneumologia Veterinária, Faculdade UFAPE | Pós-graduação em Pneumologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Pneumologia Veterinária | Data de início da Pós-graduação em Pneumologia Veterinária [CONFIRMAR NO CATÁLOGO] |
| Ventilação Mecânica (352) | Pós-graduação em Ventilação Mecânica, Faculdade UFAPE | Pós-graduação em Ventilação Mecânica para médicos veterinários, semipresencial, 360 h, em São Paulo. Veja módulos e investimento. | Pós-graduação em Ventilação Mecânica | A Pós-graduação em Ventilação Mecânica serve só para quem trabalha em UTI? [REVISÃO DOCENTE] |

Entidades a citar: Faculdade UFAPE, nome completo do curso, modalidade, local, carga horária, termos técnicos da ementa da ficha. Prova que a página precisa: dado do catálogo, coordenação com autorização registrada [CONFIRMAR autorização]. Marcação da skill schema-de-curso.

---

### A8. Dermatologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68610 | Pós-graduação em Dermatologia Veterinária | São Paulo, semipresencial, 500 h | 28/11/2026, V | aberto | pós-graduação em dermatologia veterinária | pós em dermatologia veterinária presencial São Paulo; pós em dermatologia veterinária semipresencial; especialização em dermatologia de cães e gatos; pós em derma vet; pós em dermatologia veterinária duração e carga horária |
| 68646 | Prova de Bolsa de Estudos para Dermatologia Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de dermatologia veterinária | prova de bolsa pós dermatologia São Paulo; bolsa de estudos pós em dermatologia veterinária |

Livre contínuo 463: só por link.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K8.1 | Entender | pós-graduação em dermatologia veterinária | matricular | Alto | 58 (28/20/10) | Pilar Dermatologia (68610) | Agregadores EAD, PUCPR e outras ocupam. Disputar por formato |
| K8.2 | EAD x presencial | pós em dermatologia veterinária presencial São Paulo; semipresencial | matricular | Médio | 62 (30/14/18) | Pilar Dermatologia | A busca por "presencial" devolveu quase só EAD: espaço aberto [SUPOSIÇÃO] |
| K8.3 | Entender | especialização em dermatologia de cães e gatos | matricular | Médio | 54 (26/14/14) | Pilar Dermatologia | Variação da cabeça de termo |
| K8.4 | Nome popular | pós em derma vet; pós em dermato vet | matricular | Baixo | 52 (26/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K8.5 | Preço e condições | quanto custa pós em dermatologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | Concorrência de preço EAD forte: mostrar prática e parcelas, sem comparar |
| K8.6 | Preço e condições | pós em dermatologia veterinária duração e carga horária | resolver | Baixo | 50 (20/8/22) | Pilar | 500 h, semipresencial (catálogo) |
| K8.7 | Prova de bolsa | prova de bolsa de dermatologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68646 e T1 | Prova em 27/11/2026, inscrição de R$ 100,00 |
| K8.8 | EAD x presencial | pós em dermatologia veterinária EAD | comparar | Alto | 40 (14/20/6) | Guia de formato (T4) | A Ufape não oferece EAD aberto; resposta honesta |
| K8.9 | Comparar | dermatologia veterinária EAD ou presencial: qual vale mais | comparar | Médio | 50 (16/14/20) | Guia "Pós-graduação em Dermatologia Veterinária: EAD, semipresencial ou presencial" | P1 da entrada principal |
| K8.10 | Comparar instituições | pós em dermatologia veterinária Ufape ou Anclivepa | comparar | Baixo | 30 (14/8/8) | Sem página própria | Abaixo do corte; atender no guia por critérios, sem nomear |
| K8.11 | Carreira e título | pós em dermatologia veterinária vale a pena | aprender | Médio | 38 (10/14/14) | Artigo de apoio | Sem promessa de renda |
| K8.12 | Carreira e título | título de especialista em dermatologia veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte e bloqueado |
| K8.13 | Entender | o que faz um dermatologista veterinário | aprender | Médio | 32 (6/14/12) | Artigo de apoio | [REVISÃO DOCENTE] |

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q8.1 | Qual a melhor pós em dermatologia veterinária presencial ou semipresencial em São Paulo? | Solução | matricular | 56 (28/14/14) | Topo do pilar | Sem superlativo na página; dados do catálogo |
| Q8.2 | Pós em dermatologia veterinária EAD ou semipresencial: qual vale mais a pena? | Comparação | comparar | 50 (16/14/20) | Guia de formato | Tabela de comparação por critério |
| Q8.3 | Vale a pena especializar em dermatologia veterinária sendo clínico geral? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | [REVISÃO DOCENTE] |
| Q8.4 | Quanto custa a pós em dermatologia veterinária da Ufape e como parcela? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | Parcelas, total e matrícula do catálogo |
| Q8.5 | Como funciona a prova de bolsa de dermatologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68646 e T1 | Regras com contradições [CONFIRMAR NO CATÁLOGO] |
| Q8.6 | A pós em dermatologia veterinária tem atendimento prático supervisionado? | Decisão | resolver | 46 (24/8/14) | FAQ do pilar | [CONFIRMAR NO CATÁLOGO, ficha] [REVISÃO DOCENTE] |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Dermatologia | Pós-graduação em Dermatologia Veterinária | Guia "Pós-graduação em Dermatologia Veterinária: EAD, semipresencial ou presencial"; prova 68646; FAQ; artigo "como se especializar"; link para o livre contínuo 463 e para A11 (citologia) |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Dermatologia (68610) | Pós-graduação em Dermatologia Veterinária, Faculdade UFAPE | Pós-graduação em Dermatologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e prova de bolsa. | Pós-graduação em Dermatologia Veterinária | Pós-graduação em Dermatologia Veterinária semipresencial, presencial ou EAD: como decidir; Alergia e dermatologia felina na ementa da Pós-graduação em Dermatologia Veterinária [REVISÃO DOCENTE] |

---

### A5. Diagnóstico por imagem e endoscopia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68604 (e 68611) | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | São Paulo, semipresencial, 500 h | 68604: 31/10/2026, VI; 68611 sem data (verificar) | aberto (68604) | pós-graduação em diagnóstico por imagem veterinária | pós em diagnóstico por imagem veterinário semipresencial São Paulo; especialização em radiologia veterinária; pós em imagem vet; pós em diagnóstico por imagem duração |
| 68629 (e 706) | Pós-graduação em Ultrassonografia de Pequenos Animais | São Paulo, semipresencial, 360 h | 68629: 22/05/2027, III; 706 iniciada (verificar) | aberto (68629) | pós-graduação em ultrassonografia veterinária | pós em ultrassonografia de pequenos animais; pós em ultrassom veterinário; pós em ultrassonografia de cães e gatos; pós em USG vet |
| 68647, 68661, 68649 | Provas de bolsa de Diagnóstico por Imagem, Ultrassonografia em Pequenos Animais e Endoscopia | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de diagnóstico por imagem veterinário (68647); prova de bolsa de ultrassonografia veterinária (68661); prova de bolsa de endoscopia veterinária (68649, sem destino) | bolsa de estudos pós imagem veterinária |

Observações: o nome do catálogo da pós de imagem é longo e dilui o termo de busca. A primeira frase da página usa o nome padrão do catálogo e o termo: "A Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária é uma especialização em diagnóstico por imagem veterinária...". Usar nome curto no título depende da Ufape [CONFIRMAR NO CATÁLOGO]. 68629 aparece no catálogo como "Pós Graduação em Ultrassonografia", fora do padrão. 653 (Endoscopia) está em "verificar": página sem chamada de compra. Livres relacionados por link: 68614, 623 e 68637.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K5.1 | Entender | pós-graduação em diagnóstico por imagem veterinária | matricular | Alto | 60 (28/20/12) | Pilar Imagem (68604) | Poucas pós lato sensu na primeira página; a busca trouxe disciplinas stricto sensu e residência |
| K5.2 | EAD x presencial | pós em diagnóstico por imagem veterinário semipresencial em São Paulo | matricular | Médio | 62 (30/14/18) | Pilar Imagem | Concorrente EAD de preço baixo e pós da PUCPR com prática em Curitiba (persona) |
| K5.3 | Entender | pós-graduação em ultrassonografia veterinária | matricular | Alto | 62 (28/20/14) | Pilar Ultrassonografia (68629) | Menor ticket da área A5 (68629: 24x de R$ 685,67, total de R$ 16.456,00, matrícula de R$ 350,00); o menor total da linha é o de 719 (R$ 12.000,00). Vagas de emprego pedem pós ou residência (sinal fraco) |
| K5.4 | Entender | especialização em radiologia veterinária | matricular | Médio | 54 (26/14/14) | Pilar Imagem | Radiologia aparece entre as pós mais procuradas (Quero Bolsa) [SUPOSIÇÃO de equivalência]; a página cita radiografia |
| K5.5 | Nome popular | pós em imagem vet; pós em USG vet | matricular | Baixo | 52 (26/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K5.6 | Entender | pós em endoscopia veterinária | matricular | Baixo | 40 (18/8/14) | Pilar Endoscopia (653, sem compra) | Turma em "verificar": só conteúdo e a prova |
| K5.7 | Preço e condições | quanto custa pós em ultrassonografia veterinária | resolver | Médio | 54 (22/14/18) | Investimento do pilar e T8 | Parcelas, total e matrícula de R$ 350,00 do catálogo |
| K5.8 | Prova de bolsa | prova de bolsa de diagnóstico por imagem veterinário | resolver | Médio | 60 (26/14/20) | Prova 68647 e T1 | |
| K5.9 | Prova de bolsa | prova de bolsa de ultrassonografia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68661 e T1 | |
| K5.10 | Comparar | diagnóstico por imagem ou ultrassonografia: qual pós escolher | comparar | Baixo | 46 (16/8/22) | Guia A5 | P1 da entrada principal |
| K5.11 | Comparar | preciso de pós para fazer ultrassom na minha clínica veterinária | resolver | Médio | 40 (12/14/14) | Artigo de apoio | [REVISÃO DOCENTE] e [REVISÃO REGULAÇÃO] |
| K5.12 | EAD x presencial | pós em diagnóstico por imagem veterinária EAD | comparar | Alto | 40 (14/20/6) | Guia A5 (formato) | Sem oferta EAD da Ufape |
| K5.13 | Carreira e título | título de especialista em diagnóstico por imagem veterinário | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |

Goiânia: sem turma nesta área no catálogo. Sem termo local.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q5.1 | Pós em diagnóstico por imagem veterinário presencial ou semipresencial em São Paulo, qual existe? | Solução | matricular | 56 (28/14/14) | Topo do pilar Imagem | 68604 (início 31/10/2026) |
| Q5.2 | Qual a diferença entre pós em diagnóstico por imagem e pós em ultrassonografia veterinária? | Comparação | comparar | 46 (16/8/22) | Guia A5 | Sem resposta na Ufape hoje (lacunas) |
| Q5.3 | Vale a pena a pós em ultrassonografia de pequenos animais para quem é clínico geral? | Problema | aprender | 38 (10/8/20) | FAQ do pilar Ultrassonografia | [REVISÃO DOCENTE] |
| Q5.4 | Quanto custa a pós em ultrassonografia veterinária da Ufape e qual o menor investimento da área de imagem? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | Menor ticket da área A5, só catálogo; sem comparar com concorrente |
| Q5.5 | Endoscopia veterinária: faço pós ou curso livre? | Comparação | comparar | 38 (14/8/16) | Guia A5, com link para 623 e 68637 | Livres por link |
| Q5.6 | Como funciona a prova de bolsa de diagnóstico por imagem da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68647 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Imagem | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | Guia A5; prova 68647; FAQ de prática [CONFIRMAR NO CATÁLOGO]; link para 68614 |
| Ultrassonografia | Pós-graduação em Ultrassonografia de Pequenos Animais | Guia A5; prova 68661; artigo "ultrassom na própria clínica" [REVISÃO DOCENTE] |
| Endoscopia | Pós-graduação em Endoscopia Veterinária (653, sem compra) | Prova 68649 (só com destino); links para os livres 623 e 68637 |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Imagem (68604) | Pós-graduação em Diagnóstico por Imagem Veterinária, Faculdade UFAPE (nome curto: [CONFIRMAR NO CATÁLOGO]; senão usar o nome completo) | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos e turma. | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | Radiografia e ultrassonografia na ementa da Pós-graduação em Diagnóstico por Imagem; Pós-graduação em Diagnóstico por Imagem ou em Ultrassonografia: qual escolher |
| Ultrassonografia (68629) | Pós-graduação em Ultrassonografia de Pequenos Animais, Faculdade UFAPE | Pós-graduação em Ultrassonografia de Pequenos Animais, semipresencial, 360 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Ultrassonografia de Pequenos Animais | Equipamento e horas de prática da Pós-graduação em Ultrassonografia de Pequenos Animais [CONFIRMAR NO CATÁLOGO] |

---

### A11. Laboratório (hematologia, patologia clínica, citopatologia)

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68608 | Pós-graduação em Hematologia Veterinária | São Paulo, semipresencial, 500 h | 28/11/2026, VIII | aberto | pós-graduação em hematologia veterinária | especialização em hematologia de cães e gatos; pós em hematologia veterinária São Paulo; pós em hemato vet; pós em análises clínicas veterinárias |
| 68615 | Pós-graduação em Patologia Clínica | São Paulo, semipresencial, 500 h | 20/03/2027, VII | aberto | pós-graduação em patologia clínica veterinária | especialização em patologia clínica de cães e gatos; pós em patologia clínica veterinária São Paulo; pós em patologia clínica vet |
| 333 | Pós-graduação em Citopatologia Veterinária (catálogo: "Pós Graduação em Citopatologia Veterinária") | São Paulo, semipresencial, 500 h | 27/03/2027, I | aberto | pós-graduação em citopatologia veterinária | pós em citologia veterinária; especialização em citopatologia de cães e gatos |
| 68651, 68658 | Provas de bolsa de Hematologia e de Patologia Clínica Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de hematologia veterinária (68651); prova de bolsa de patologia clínica veterinária (68658) | bolsa de estudos pós hematologia; bolsa de estudos pós patologia clínica |

Livres e evento relacionados, por link: 462, 106 e evento 202 (linha Eventos).

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K11.1 | Entender | pós-graduação em hematologia veterinária | matricular | Médio | 60 (28/14/18) | Pilar Hematologia (68608) | A busca trouxe sobretudo stricto sensu e disciplinas; quase nenhuma pós lato sensu na primeira página |
| K11.2 | Entender | pós-graduação em patologia clínica veterinária | matricular | Alto | 60 (28/20/12) | Pilar Patologia Clínica (68615) | Pravaler a cita entre as mais procuradas |
| K11.3 | Entender | pós-graduação em citopatologia veterinária | matricular | Baixo | 58 (28/8/22) | Pilar Citopatologia (333) | Curso novo (turma I) |
| K11.4 | Entender | pós em análises clínicas veterinárias | matricular | Médio | 50 (24/14/12) | Pilar Patologia Clínica | O termo aparece em EAD de faculdades; [SUPOSIÇÃO] de que atrai o mesmo público |
| K11.5 | Nome popular | pós em hemato vet; pós em patologia clínica vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K11.6 | Preço e condições | quanto custa pós em patologia clínica veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K11.7 | Prova de bolsa | prova de bolsa de hematologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68651 e T1 | |
| K11.8 | Prova de bolsa | prova de bolsa de patologia clínica veterinária | resolver | Médio | 60 (26/14/20) | Prova 68658 e T1 | |
| K11.9 | Comparar | hematologia, patologia clínica ou citopatologia: qual pós escolher | comparar | Baixo | 46 (16/8/22) | Guia A11 | P1 da entrada principal |
| K11.10 | Comparar | pós em patologia clínica veterinária serve para clínico ou só para laboratório | comparar | Baixo | 44 (14/8/22) | FAQ e Guia A11 | Público de 68608 não está na ficha [CONFIRMAR] |
| K11.11 | Carreira e título | título de especialista em patologia clínica veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |
| K11.12 | Entender | interpretação de hemograma veterinário | aprender | Alto | 32 (4/20/8) | Artigo de apoio com link para 68608 | Conteúdo de autoridade; [REVISÃO DOCENTE]; no limite do corte |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q11.1 | Pós em patologia clínica veterinária serve para clínico geral ou só para quem trabalha em laboratório? | Problema | comparar | 44 (14/8/22) | FAQ do pilar Patologia Clínica | [CONFIRMAR NO CATÁLOGO] |
| Q11.2 | Qual a diferença entre hematologia, patologia clínica e citopatologia veterinária na pós? | Comparação | comparar | 46 (16/8/22) | Guia A11 | |
| Q11.3 | Pós em hematologia veterinária presencial ou semipresencial em São Paulo, existe? | Solução | matricular | 56 (28/14/14) | Pilar Hematologia | 68608, 28/11/2026 |
| Q11.4 | Existe pós em citopatologia veterinária? Quando começa a primeira turma? | Solução | matricular | 56 (28/8/20) | Pilar Citopatologia | 333, turma I, 27/03/2027 |
| Q11.5 | Quanto custa a pós em patologia clínica veterinária da Ufape? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | Catálogo |
| Q11.6 | Como funciona a prova de bolsa de hematologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68651 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Hematologia | Pós-graduação em Hematologia Veterinária | Guia A11; prova 68651; FAQ de público e rotina |
| Patologia clínica | Pós-graduação em Patologia Clínica | Guia A11; prova 68658; artigo "hemograma e esfregaço" |
| Citopatologia | Pós-graduação em Citopatologia Veterinária | Guia A11; artigo "citologia no consultório" com link para A8 |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Hematologia (68608) | Pós-graduação em Hematologia Veterinária, Faculdade UFAPE | Pós-graduação em Hematologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e prova de bolsa. | Pós-graduação em Hematologia Veterinária | Para clínico ou para laboratório: quem faz a Pós-graduação em Hematologia Veterinária [CONFIRMAR NO CATÁLOGO] |
| Patologia Clínica (68615) | Pós-graduação em Patologia Clínica, Faculdade UFAPE | Pós-graduação em Patologia Clínica, semipresencial, 500 h, em São Paulo. Veja módulos, turma e prova de bolsa. | Pós-graduação em Patologia Clínica | Pós-graduação em Hematologia, em Patologia Clínica ou em Citopatologia: qual escolher |
| Citopatologia (333) | Pós-graduação em Citopatologia Veterinária, Faculdade UFAPE | Pós-graduação em Citopatologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Citopatologia Veterinária | Corpo docente da ficha da Pós-graduação em Citopatologia Veterinária: confirmar coordenação [CONFIRMAR] |

---

### A6. Gastroenterologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68606 | Pós-graduação em Gastroenterologia Veterinária | São Paulo, semipresencial, 500 h | 07/11/2026, IX | aberto | pós-graduação em gastroenterologia veterinária | pós em gastroenterologia veterinária de pequenos animais; especialização em gastroenterologia de cães e gatos; pós em gastro vet; pós em gastroenterologia veterinária São Paulo; pós em gastroenterologia veterinária endoscopia |
| 68650 | Prova de Bolsa de Estudos para Gastroenterologia Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de gastroenterologia veterinária | bolsa de estudos pós gastroenterologia veterinária |

Por link: minicursos 669 e 455 e grupo de estudos 721.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K6.1 | Entender | pós-graduação em gastroenterologia veterinária | matricular | Médio | 62 (28/14/20) | Pilar Gastroenterologia (68606) | Resultados dominados por medicina humana (Afya e outras): espaço aberto [SUPOSIÇÃO] |
| K6.2 | Entender | pós em gastroenterologia veterinária de pequenos animais em São Paulo | matricular | Baixo | 60 (30/8/22) | Pilar | Turma começa em 12 dias: serve à próxima edição |
| K6.3 | Entender | especialização em gastroenterologia de cães e gatos | matricular | Baixo | 54 (26/8/20) | Pilar | |
| K6.4 | Nome popular | pós em gastro vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K6.5 | Preço e condições | quanto custa pós em gastroenterologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K6.6 | Entender | pós em gastroenterologia veterinária tem endoscopia e aulas práticas | resolver | Baixo | 48 (22/8/18) | FAQ do pilar | A ficha lista aulas práticas e estágios [CONFIRMAR NO CATÁLOGO] |
| K6.7 | Prova de bolsa | prova de bolsa de gastroenterologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68650 e T1 | |
| K6.8 | EAD x presencial | pós em gastroenterologia veterinária EAD ou presencial | comparar | Médio | 48 (16/14/18) | Guia de formato (T4) | Sem EAD da Ufape |
| K6.9 | Comparar | gastroenterologia ou clínica médica: qual pós escolher | comparar | Baixo | 44 (16/8/20) | Guia (ponte com A3) | |
| K6.10 | Carreira e título | como se especializar em gastroenterologia veterinária | aprender | Médio | 36 (8/14/14) | Artigo de apoio | [REVISÃO REGULAÇÃO] no trecho de título. A página atual afirma "especialidade emergente e carente de profissionais" sem fonte: não repetir |
| K6.11 | Entender | doença inflamatória intestinal e pancreatite em cães e gatos | aprender | Médio | 30 (4/14/12) | Artigo de apoio | Abaixo do corte como alvo de matrícula; manter como conteúdo de autoridade [REVISÃO DOCENTE] |
| K6.12 | Carreira e título | título de especialista em gastroenterologia veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Entidade de área sem fonte nesta rodada; conferir na fonte oficial |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q6.1 | Qual pós em gastroenterologia veterinária de pequenos animais existe em São Paulo? | Solução | matricular | 58 (28/14/16) | Topo do pilar | 68606 |
| Q6.2 | Gastroenterologia veterinária vale a pena como especialização? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | Sem afirmação de mercado sem fonte |
| Q6.3 | A pós em gastroenterologia da Ufape tem endoscopia e aulas práticas? | Decisão | resolver | 50 (24/8/18) | FAQ do pilar | [CONFIRMAR NO CATÁLOGO] |
| Q6.4 | Como funciona o grupo de discussão de casos da pós em gastroenterologia? | Decisão | resolver | 40 (20/8/12) | FAQ do pilar | Uma linha na ficha |
| Q6.5 | Quanto custa a pós em gastroenterologia veterinária da Ufape? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | |
| Q6.6 | Como funciona a prova de bolsa de gastroenterologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68650 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Gastroenterologia | Pós-graduação em Gastroenterologia Veterinária | Prova 68650; FAQ; artigo "como se especializar"; ponte com A5 (endoscopia e ultrassom); link para os minicursos 669 e 455 e para o grupo de estudos 721 |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Gastroenterologia (68606) | Pós-graduação em Gastroenterologia Veterinária, Faculdade UFAPE | Pós-graduação em Gastroenterologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e prova de bolsa. | Pós-graduação em Gastroenterologia Veterinária | Endoscopia e aulas práticas da Pós-graduação em Gastroenterologia Veterinária [CONFIRMAR NO CATÁLOGO]; Grupo de discussão de casos |

---

### A1. Anestesiologia e dor

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68609 (e 68607, 664) | Pós-graduação em Anestesiologia Veterinária | Goiânia, semipresencial, 500 h (68607 em São Paulo está em "verificar", 664 sem venda) | 68609: 24/04/2027, VIII | aberto | pós-graduação em anestesiologia veterinária | pós em anestesiologia veterinária em Goiânia; especialização em anestesiologia de cães e gatos; pós em anestesio vet; anestesiologia veterinária duração e carga horária; pós em anestesiologia veterinária presencial |
| 657 | Pós-graduação em Anestesiologia Avançada | São Paulo, semipresencial, 360 h | 13/03/2027, II | aberto | pós-graduação em anestesiologia avançada veterinária | pós em anestesiologia avançada; anestesia avançada em cães e gatos pós |
| 359 | Pós-graduação em Anestesiologia Locorregional Veterinária | São Paulo, semipresencial, 360 h | 22/05/2027, I (só no site) | aberto | pós-graduação em anestesiologia locorregional veterinária | bloqueios locorregionais guiados por ultrassom pós; pós em anestesia locorregional em cães e gatos |
| 68639, 68640 | Provas de bolsa de Anestesiologia Veterinária (SP e Goiânia) | SP e Goiânia, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de anestesiologia veterinária | prova de bolsa pós anestesiologia Goiânia; prova de bolsa pós anestesiologia São Paulo |

Fora do recorte, sem chamada de compra: 586 (Anestesiologia Direto ao ponto, EAD, verificar), 554 (Dor e Cuidados Paliativos, verificar). A turma de São Paulo de Anestesiologia (68607) está iniciada: não existe turma aberta de SP para esse termo; o termo local de SP fica para quando abrir [CONFIRMAR NO CATÁLOGO].

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K1.1 | Entender | pós-graduação em anestesiologia veterinária | matricular | Alto | 58 (28/20/10) | Pilar Anestesiologia | Quero Bolsa, UNAR (2026) e outros ocupam. Hoje há 3 páginas com o mesmo nome (C1) |
| K1.2 | Goiânia | pós em anestesiologia veterinária em Goiânia | matricular | Baixo | 60 (30/8/22) | Pilar Anestesiologia (68609) | Cauda local; turma de abril de 2027 |
| K1.3 | Entender | pós-graduação em anestesiologia avançada veterinária | matricular | Baixo | 58 (28/8/22) | Pilar Avançada (657) | Público já anestesista [SUPOSIÇÃO]; turma de março de 2027 |
| K1.4 | Entender | pós-graduação em anestesiologia locorregional veterinária | matricular | Baixo | 56 (28/8/20) | Pilar Locorregional (359) | Mercado pequeno e ticket alto |
| K1.5 | Nome popular | pós em anestesio vet; pós em anestesia veterinária | matricular | Baixo | 52 (26/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K1.6 | Preço e condições | quanto custa pós em anestesiologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K1.7 | Prova de bolsa | prova de bolsa de anestesiologia veterinária | resolver | Médio | 60 (26/14/20) | Provas 68639 e 68640 e T1 | Prova em SP e em Goiânia |
| K1.8 | Comparar | anestesiologia ou anestesiologia avançada: qual pós escolher | comparar | Baixo | 46 (16/8/22) | Guia A1 | P1 da entrada principal |
| K1.9 | EAD x presencial | pós em anestesiologia veterinária EAD | comparar | Alto | 40 (14/20/6) | Guia A1 (formato) | 586 está em "verificar": sem chamada de compra |
| K1.10 | Carreira e título | residência em anestesiologia veterinária | comparar | Médio | 38 (14/14/10) | T5 | A busca citou residência em anestesiologia na UFF e especialização na USP (resumo de busca de 26/10/2026, sem URL; conferir na fonte); [REVISÃO REGULAÇÃO] |
| K1.11 | Carreira e título | título de especialista em anestesiologia veterinária | aprender | Médio | 36 (10/14/12) | T6 (bloqueado) | Curso livre 488 prepara para a prova de título (link, linha Livres) |
| K1.12 | Entender | avaliação e tratamento da dor em cães e gatos pós-graduação | aprender | Médio | 32 (6/14/12) | Artigo e link para 554 (sem compra) | [REVISÃO DOCENTE]; no limite do corte |

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q1.1 | Qual a melhor pós em anestesiologia veterinária semipresencial? Tem em Goiânia? | Solução | matricular | 56 (28/14/14) | Topo do pilar | 68609, Goiânia, 500 h |
| Q1.2 | Pós em anestesiologia veterinária EAD ou presencial: qual escolher? | Comparação | comparar | 46 (16/14/16) | Guia A1 | |
| Q1.3 | Vale a pena fazer pós em anestesiologia sendo clínico geral? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | [REVISÃO DOCENTE] |
| Q1.4 | Anestesiologia avançada e locorregional exigem residência ou pós anterior? | Decisão | resolver | 50 (24/8/18) | FAQ de 657 e 359 | A ficha de 359 tem ambiguidade; 657 [CONFIRMAR NO CATÁLOGO] |
| Q1.5 | Qual a diferença entre pós em anestesiologia, anestesiologia avançada e locorregional? | Comparação | comparar | 46 (16/8/22) | Guia A1 | |
| Q1.6 | Como funciona a prova de bolsa da Ufape para anestesiologia e quanto custa a inscrição? | Decisão | resolver | 56 (26/14/16) | Provas 68639 e 68640 e T1 | R$ 100,00 (catálogo) |
| Q1.7 | Quanto custa a pós em anestesiologia avançada da Ufape e como parcela? | Decisão | resolver | 54 (24/8/22) | Investimento de 657 | Catálogo; ticket alto |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Anestesiologia | Pós-graduação em Anestesiologia Veterinária (página única, T3) | Guia A1 (os 5 cursos); provas 68639 e 68640; FAQ de pré-requisito; T5 e T6 |
| Anestesiologia avançada | Pós-graduação em Anestesiologia Avançada | Guia A1; FAQ de nível |
| Locorregional | Pós-graduação em Anestesiologia Locorregional Veterinária | Artigo "anestesia locorregional guiada por ultrassom" [REVISÃO DOCENTE] |
| Dor | Pós-graduação em Dor e Cuidados Paliativos na Veterinária (554, sem compra) | Artigo de dor; ponte com A14 (geriatria) |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Anestesiologia (68609) | Pós-graduação em Anestesiologia Veterinária, Faculdade UFAPE | Pós-graduação em Anestesiologia Veterinária, semipresencial, 500 h, turma em Goiânia. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Anestesiologia Veterinária | Pós-graduação em Anestesiologia Veterinária, Anestesiologia Avançada e Anestesiologia Locorregional: qual escolher; Turma de São Paulo da Pós-graduação em Anestesiologia Veterinária [CONFIRMAR NO CATÁLOGO] |
| Anestesiologia Avançada (657) | Pós-graduação em Anestesiologia Avançada, Faculdade UFAPE | Pós-graduação em Anestesiologia Avançada, semipresencial, 360 h, em São Paulo. Veja módulos, pré-requisitos e investimento. | Pós-graduação em Anestesiologia Avançada | Pré-requisitos da Pós-graduação em Anestesiologia Avançada [CONFIRMAR NO CATÁLOGO] |
| Locorregional (359) | Pós-graduação em Anestesiologia Locorregional Veterinária, Faculdade UFAPE | Pós-graduação em Anestesiologia Locorregional Veterinária, semipresencial, 360 h, em São Paulo. Veja módulos e investimento. | Pós-graduação em Anestesiologia Locorregional Veterinária | Bloqueios guiados por ultrassom na Pós-graduação em Anestesiologia Locorregional Veterinária [REVISÃO DOCENTE]; Pré-requisitos [CONFIRMAR NO CATÁLOGO] |

---

### A3. Emergência, terapia intensiva e clínica médica

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68635 (e 663) | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | São Paulo, semipresencial, 750 h (663 iniciada, verificar) | 68635: 10/04/2027, V | aberto | pós-graduação em clínica médica e emergência de pequenos animais | pós em clínica médica de pequenos animais semipresencial; especialização em clínica médica de cães e gatos; pós em emergência veterinária; pós de 750 horas |
| 68623 (e 666) | Pós-graduação em Terapia Intensiva e Emergência Veterinária | Goiânia, semipresencial, 750 h (666 em São Paulo, iniciada, verificar) | 68623: 22/05/2027, IV | aberto | pós-graduação em terapia intensiva veterinária | pós em terapia intensiva veterinária em Goiânia; pós em terapia intensiva e emergência veterinária; pós em UTI veterinária; pós em TI vet |
| 68645, 68660 | Provas de bolsa de Clínica Médica e Emergência e de Terapia Intensiva Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de terapia intensiva veterinária (68660); prova de bolsa de clínica médica e emergência veterinária (68645) | bolsa de estudos pós terapia intensiva; bolsa de estudos pós clínica médica |

Sem chamada de compra: Internação Veterinária (610, 614, 615, sem venda) e os aprimoramentos da Ufape Clínica. Livre por link: POCUS (68638).

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K3.1 | Entender | pós-graduação em terapia intensiva veterinária | matricular | Médio | 58 (28/14/16) | Pilar Terapia Intensiva (68623) | Uninter EAD e outros; 2 páginas de nome repetido (666 e 68623) |
| K3.2 | Goiânia | pós em terapia intensiva veterinária em Goiânia | matricular | Baixo | 60 (30/8/22) | Pilar Terapia Intensiva (68623) | Turma de maio de 2027 |
| K3.3 | Entender | pós-graduação em clínica médica de pequenos animais | matricular | Alto | 56 (28/20/8) | Pilar Clínica Médica e Emergência (68635) | Agregadores com EAD de parcela baixa: disputar por prática e carga horária |
| K3.4 | Entender | pós em emergência veterinária | matricular | Médio | 54 (26/14/14) | Pilar Clínica Médica e Emergência | |
| K3.5 | Nome popular | pós em UTI veterinária; pós em TI vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K3.6 | Preço e condições | quanto custa pós em terapia intensiva veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K3.7 | Preço e condições | pós de 750 horas vale a pena | resolver | Baixo | 42 (16/8/18) | FAQ "por que 750 h" | Distribuição de horas na ficha [CONFIRMAR NO CATÁLOGO] |
| K3.8 | Prova de bolsa | prova de bolsa de terapia intensiva veterinária | resolver | Médio | 60 (26/14/20) | Prova 68660 e T1 | |
| K3.9 | Comparar | clínica médica e emergência ou terapia intensiva: qual pós escolher | comparar | Médio | 50 (16/14/20) | Guia A3 | P1 da entrada principal |
| K3.10 | Comparar | aprimoramento, residência ou pós em terapia intensiva veterinária | comparar | Médio | 42 (14/14/14) | T5 | Aprimoramentos da Ufape em "verificar": só exemplo de categoria; [REVISÃO REGULAÇÃO] |
| K3.11 | EAD x presencial | pós em clínica médica de pequenos animais EAD | comparar | Alto | 40 (14/20/6) | Guia A3 (formato) | Concorrência de preço |
| K3.12 | Carreira e título | título de especialista em terapia intensiva veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q3.1 | Qual a diferença entre pós em clínica médica e emergência e pós em terapia intensiva veterinária? | Comparação | comparar | 46 (16/8/22) | Guia A3 | |
| Q3.2 | Aprimoramento, residência ou pós em terapia intensiva veterinária: qual escolher? | Comparação | comparar | 42 (14/14/14) | T5 | |
| Q3.3 | Dá para fazer pós em emergência veterinária trabalhando em plantão? | Problema | resolver | 48 (22/14/12) | FAQ de escala e módulos | Módulos de 3 dias em 666 (ficha); reposição [CONFIRMAR] |
| Q3.4 | Pós em terapia intensiva veterinária semipresencial em Goiânia: existe? | Solução | matricular | 56 (30/8/18) | Pilar Terapia Intensiva | 68623 |
| Q3.5 | Vale a pena uma pós de 750 horas? | Decisão | resolver | 42 (16/8/18) | FAQ do pilar | |
| Q3.6 | Como funciona a prova de bolsa de terapia intensiva da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68660 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Clínica médica e emergência | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | Guia A3; prova 68645; FAQ de plantão; link para POCUS (68638) |
| Terapia intensiva | Pós-graduação em Terapia Intensiva e Emergência Veterinária | Guia A3; T5; prova 68660; artigo "POCUS em emergência" [REVISÃO DOCENTE] |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Clínica Médica e Emergência (68635) | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, Faculdade UFAPE | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, semipresencial, 750 h, em São Paulo. Veja módulos e prova de bolsa. | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | Pós-graduação em Clínica Médica e Emergência ou em Terapia Intensiva: qual escolher; Por que 750 horas na Pós-graduação em Clínica Médica e Emergência de Pequenos Animais [CONFIRMAR NO CATÁLOGO] |
| Terapia Intensiva (68623) | Pós-graduação em Terapia Intensiva e Emergência Veterinária, Faculdade UFAPE | Pós-graduação em Terapia Intensiva e Emergência Veterinária, semipresencial, 750 h, turma em Goiânia. Veja módulos e prova de bolsa. | Pós-graduação em Terapia Intensiva e Emergência Veterinária | Pós-graduação em Terapia Intensiva e Emergência Veterinária, aprimoramento e residência; Plantão e escala dos módulos da Pós-graduação em Terapia Intensiva e Emergência Veterinária [CONFIRMAR] |

---

### A4. Cirurgia, ortopedia e reabilitação

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68632 (e 535, 665) | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Goiânia, presencial, 500 h (535 em Goiânia e 665 em São Paulo estão em "verificar") | 68632: 10/04/2027, V | aberto | pós-graduação em clínica cirúrgica de cães e gatos | pós em cirurgia veterinária; pós em clínica cirúrgica presencial em Goiânia; especialização em cirurgia de cães e gatos; pós em clínica cirúrgica vet |
| 578 | Pós-graduação em Videocirurgia Veterinária | São Paulo, semipresencial, 500 h | 22/05/2027, IV | aberto | pós-graduação em videocirurgia veterinária | especialização em videocirurgia de cães e gatos; videocirurgia veterinária pós ou curso prático |
| 662 | Pós-graduação em Ortopedia Veterinária | São Paulo, semipresencial, 500 h | 24/04/2027, IV (link trocado com Odontologia, P3: preço e turma podem ser de outra turma) | aberto | pós-graduação em ortopedia veterinária | especialização em ortopedia de cães e gatos; pós em ortopedia veterinária São Paulo |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | São Paulo, semipresencial, 500 h | 10/04/2027, I (data diverge entre planilha e site) | aberto | pós-graduação em fisioterapia veterinária | pós em reabilitação veterinária; pós em fisiatria veterinária; pós em fisioterapia e reabilitação de cães e gatos |
| 68643, 68644 | Provas de bolsa de Clínica Cirúrgica de Cães e Gatos (SP e Goiânia) | SP e Goiânia, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de clínica cirúrgica de cães e gatos | prova de bolsa pós cirurgia veterinária Goiânia; bolsa de estudos pós clínica cirúrgica |

Sem chamada de compra: 535 e 665 (verificar). Não há turma aberta de Clínica Cirúrgica em São Paulo no recorte. Livres por link: 99 e 433 (imersão em cirurgia veterinária, ambos em "verificar").

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K4.1 | Entender | pós-graduação em clínica cirúrgica de cães e gatos | matricular | Alto | 58 (28/20/10) | Pilar Clínica Cirúrgica (68632) | Hoje há 3 páginas no catálogo (535, 665 e 68632), todas com o mesmo nome (C1). UNIME e UNAR (2026) aparecem na busca |
| K4.2 | Goiânia | pós em clínica cirúrgica presencial em Goiânia | matricular | Baixo | 60 (30/8/22) | Pilar Clínica Cirúrgica (68632) | Única turma com modalidade "presencial" no recorte (catálogo); frequência e jornada [CONFIRMAR NO CATÁLOGO] |
| K4.3 | Entender | pós em cirurgia veterinária | matricular | Alto | 54 (26/20/8) | Pilar Clínica Cirúrgica | Cabeça de termo |
| K4.4 | Entender | pós-graduação em ortopedia veterinária | matricular | Médio | 56 (26/14/16) | Pilar Ortopedia (662) | A busca achou poucas pós lato sensu de ortopedia: espaço aberto [SUPOSIÇÃO]. Não anunciar antes de corrigir o link trocado |
| K4.5 | Entender | pós-graduação em videocirurgia veterinária | matricular | Baixo | 56 (28/8/20) | Pilar Videocirurgia (578) | Concorrente: UFPA com FADESP em endoscopia e videocirurgia (persona) |
| K4.6 | Entender | pós-graduação em fisioterapia veterinária; reabilitação | matricular | Médio | 52 (26/14/12) | Pilar Reabilitação (366) | Curso novo (turma I); Qualittas aparece com Fisiatria; data diverge |
| K4.7 | Nome popular | pós em cirurgia vet; pós em ortopedia vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K4.8 | Preço e condições | quanto custa pós em clínica cirúrgica de cães e gatos | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K4.9 | Prova de bolsa | prova de bolsa de clínica cirúrgica de cães e gatos | resolver | Médio | 60 (26/14/20) | Provas 68643 e 68644 e T1 | |
| K4.10 | Comparar | clínica cirúrgica, ortopedia ou videocirurgia: qual pós escolher | comparar | Baixo | 46 (16/8/22) | Guia A4 | |
| K4.11 | Comparar | videocirurgia veterinária: pós ou curso prático | comparar | Baixo | 44 (16/8/20) | Guia A4, link para 99 e 433 | Livres por link |
| K4.12 | EAD x presencial | pós em cirurgia veterinária presencial ou EAD | comparar | Médio | 46 (14/14/18) | Guia A4 (formato) | Cirurgia pede prática presencial: argumento do formato [REVISÃO DOCENTE] |
| K4.13 | Carreira e título | título de especialista em cirurgia veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | A busca citou o Colégio Brasileiro de Cirurgia Veterinária (resumo de busca de 26/10/2026, sem URL); conferir a regra na fonte |

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q4.1 | Qual a melhor pós em clínica cirúrgica de cães e gatos? Tem presencial em Goiânia? | Solução | matricular | 56 (30/8/18) | Topo do pilar | 68632 |
| Q4.2 | Pós em clínica cirúrgica presencial em Goiânia: como funciona e preciso morar na cidade? | Problema | resolver | 52 (26/8/18) | FAQ de Goiânia | Frequência, jornada e hospedagem [CONFIRMAR NO CATÁLOGO] |
| Q4.3 | Existe pós em ortopedia veterinária em São Paulo? | Solução | matricular | 54 (28/8/18) | Pilar Ortopedia | Após corrigir dados de 662 |
| Q4.4 | Pós em videocirurgia veterinária vale a pena ou faço só o curso prático? | Comparação | comparar | 44 (16/8/20) | Guia A4 | |
| Q4.5 | Existe pós de fisioterapia e reabilitação veterinária? Quem pode fazer? | Solução | matricular | 52 (26/8/18) | Pilar Reabilitação | Público [CONFIRMAR]; [REVISÃO REGULAÇÃO] |
| Q4.6 | Como funciona a prova de bolsa de clínica cirúrgica da Ufape em Goiânia e em São Paulo? | Decisão | resolver | 56 (26/14/16) | Provas 68643 e 68644 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Clínica cirúrgica | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Guia A4; provas 68643 e 68644; FAQ de Goiânia; artigo "Pós-graduação em Clínica Cirúrgica de Cães e Gatos em Goiânia (presencial): como funciona e quem consegue conciliar" |
| Videocirurgia | Pós-graduação em Videocirurgia Veterinária | Guia A4; link para 99 e 433 |
| Ortopedia | Pós-graduação em Ortopedia Veterinária | Guia A4 (depois de corrigir 662) |
| Reabilitação | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | Artigo "reabilitação e fisioterapia" [REVISÃO DOCENTE] |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Clínica Cirúrgica (68632) | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, Faculdade UFAPE | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, presencial, 500 h, turma em Goiânia. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Turma presencial de Goiânia da Pós-graduação em Clínica Cirúrgica de Cães e Gatos: quem consegue conciliar [CONFIRMAR NO CATÁLOGO frequência e jornada]; Turma de São Paulo [CONFIRMAR NO CATÁLOGO] |
| Videocirurgia (578) | Pós-graduação em Videocirurgia Veterinária, Faculdade UFAPE | Pós-graduação em Videocirurgia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Videocirurgia Veterinária | Pós-graduação em Videocirurgia Veterinária ou curso prático de cirurgia |
| Ortopedia (662) | Pós-graduação em Ortopedia Veterinária, Faculdade UFAPE | Pós-graduação em Ortopedia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Ortopedia Veterinária | Só publicar depois de corrigir preço e turma da Pós-graduação em Ortopedia Veterinária [CONFIRMAR NO CATÁLOGO] |
| Reabilitação (366) | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, Faculdade UFAPE | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos e turma. | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | Público e quem pode atuar após a Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária [CONFIRMAR]; [REVISÃO REGULAÇÃO] |

---

### A10. Oncologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68628 (e 654) | Pós-graduação em Oncologia Veterinária | São Paulo, semipresencial, 500 h (654 sem venda) | 10/04/2027, VII (turma diverge entre planilha e site, P5) | aberto | pós-graduação em oncologia veterinária | pós em oncologia veterinária de pequenos animais; especialização em oncologia de cães e gatos; pós em onco vet; pós em oncologia veterinária São Paulo; pós em oncologia veterinária presencial |
| 68657 | Prova de Bolsa de Estudos para Oncologia Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de oncologia veterinária | bolsa de estudos pós oncologia veterinária |

Livre por link: 560 (Curso de Eletroquimioterapia, 22/05/2027) e contínuo 465.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K10.1 | Entender | pós-graduação em oncologia veterinária | matricular | Alto | 58 (28/20/10) | Pilar Oncologia (68628) | Agregadores EAD de R$ 60 a R$ 200 por mês (promocionais), PUCPR e Anclivepa |
| K10.2 | Entender | pós em oncologia veterinária de pequenos animais presencial em São Paulo | matricular | Médio | 60 (30/14/16) | Pilar Oncologia | Semipresencial com módulos presenciais |
| K10.3 | Nome popular | pós em onco vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K10.4 | Preço e condições | quanto custa pós em oncologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | Ticket de R$ 38.940,00 no catálogo: a objeção é forte; mostrar parcelas e estrutura |
| K10.5 | Prova de bolsa | prova de bolsa de oncologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68657 e T1 | |
| K10.6 | Comparar | pós em oncologia ou curso de eletroquimioterapia | comparar | Baixo | 44 (16/8/20) | Guia A10, link para 560 | Livres por link |
| K10.7 | EAD x presencial | pós em oncologia veterinária EAD | comparar | Alto | 40 (14/20/6) | Guia de formato | Sem EAD da Ufape |
| K10.8 | Comparar | pós em oncologia veterinária duração e carga horária | resolver | Médio | 50 (20/14/16) | Pilar | 500 h; agregador cita de 400 a 600 h e de 12 a 24 meses como faixa de mercado |
| K10.9 | Carreira e título | título de especialista em oncologia veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |
| K10.10 | Entender | biossegurança em quimioterapia veterinária | aprender | Médio | 32 (6/14/12) | Artigo de apoio | Dúvida da persona (H-A10.2); [REVISÃO DOCENTE] |
| K10.11 | Entender | oncologia veterinária vale a pena como especialização | aprender | Médio | 38 (10/14/14) | Artigo de apoio | |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q10.1 | Pós em oncologia veterinária de pequenos animais presencial ou semipresencial em São Paulo | Solução | matricular | 56 (30/14/12) | Topo do pilar | 68628 |
| Q10.2 | Preciso de estrutura especial na clínica para fazer quimioterapia depois da pós? | Problema | aprender | 36 (10/8/18) | FAQ do pilar | [REVISÃO DOCENTE] |
| Q10.3 | Oncologia veterinária vale a pena como especialização? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | |
| Q10.4 | Pós em oncologia ou curso de eletroquimioterapia: qual faço primeiro? | Comparação | comparar | 44 (16/8/20) | Guia A10 | |
| Q10.5 | Quanto custa a pós em oncologia veterinária da Ufape e dá para parcelar? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | |
| Q10.6 | Como funciona a prova de bolsa de oncologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68657 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Oncologia | Pós-graduação em Oncologia Veterinária (página única; 654 recebe 301) | Guia A10; prova 68657; FAQ com biossegurança [REVISÃO DOCENTE]; link para 560 |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Oncologia (68628) | Pós-graduação em Oncologia Veterinária, Faculdade UFAPE | Pós-graduação em Oncologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Oncologia Veterinária | Biossegurança na quimioterapia na Pós-graduação em Oncologia Veterinária [REVISÃO DOCENTE]; Pós-graduação em Oncologia Veterinária ou curso de eletroquimioterapia |

---

### A7. Endocrinologia e nefrologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais | São Paulo, semipresencial, 500 h | 17/04/2027, V (turma diverge entre planilha e site, P5) | aberto | pós-graduação em endocrinologia de pequenos animais | pós em endocrinologia veterinária; especialização em endocrinologia de cães e gatos; pós em endócrino vet; diabetes e tireoide em cães e gatos pós |
| 68648, 68653 | Provas de bolsa de Endocrinologia de Pequenos Animais e de Nefrologia e Urologia Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de endocrinologia de pequenos animais (68648); prova de bolsa de nefrologia e urologia veterinária (68653, sem destino) | bolsa de estudos pós endocrinologia veterinária |

Sem chamada de compra: 68612 (Nefrologia e Urologia Veterinária, VIII, iniciada, verificar). Livres e grupos de estudos relacionados por link: 103, 104, 542, 458, 454, 642 e 712.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K7.1 | Entender | pós-graduação em endocrinologia veterinária | matricular | Médio | 56 (28/14/14) | Pilar Endocrinologia (68617) | Guia da Carreira e Quero Bolsa listam, quase todas EAD; IBMR aparece |
| K7.2 | Entender | pós em endocrinologia de pequenos animais semipresencial | matricular | Baixo | 58 (30/8/20) | Pilar Endocrinologia | |
| K7.3 | Nome popular | pós em endócrino vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K7.4 | Entender | pós em nefrologia e urologia veterinária | matricular | Médio | 36 (14/14/8) | Pilar Nefrologia (68612, sem compra) | Turma iniciada: só conteúdo e prova; Módulo e FSG aparecem na busca |
| K7.5 | Preço e condições | quanto custa pós em endocrinologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K7.6 | Prova de bolsa | prova de bolsa de endocrinologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68648 e T1 | |
| K7.7 | Prova de bolsa | prova de bolsa de nefrologia veterinária | resolver | Baixo | 40 (18/8/14) | Prova 68653 e T1 | Sem turma de destino: não anunciar até a Ufape decidir |
| K7.8 | Comparar | endocrinologia, nefrologia ou geriatria: qual pós escolher | comparar | Baixo | 44 (14/8/22) | Guia A7, ponte com A14 | |
| K7.9 | EAD x presencial | pós em endocrinologia veterinária EAD | comparar | Alto | 40 (14/20/6) | Guia de formato | Sem EAD da Ufape |
| K7.10 | Entender | endocrinologia veterinária vale a pena para clínico geral | aprender | Médio | 38 (10/14/14) | Artigo de apoio | |
| K7.11 | Carreira e título | título de especialista em endocrinologia veterinária | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |
| K7.12 | Entender | doença renal crônica em cães e gatos; diabetes mellitus em cães e gatos | aprender | Alto | 32 (4/20/8) | Artigos de apoio | [REVISÃO DOCENTE]; no limite do corte |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q7.1 | Pós em endocrinologia de pequenos animais semipresencial em São Paulo, existe? | Solução | matricular | 56 (30/8/18) | Topo do pilar | 68617 |
| Q7.2 | Pós em nefrologia e urologia veterinária: onde fazer e como funciona? | Solução | matricular | 40 (24/8/8) | Pilar Nefrologia (sem compra) | Só resposta de conteúdo |
| Q7.3 | Endocrinologia veterinária vale a pena para clínico geral? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | |
| Q7.4 | Fiz a prova de bolsa de nefrologia: para qual turma vale a bolsa? | Decisão | resolver | 40 (22/8/10) | FAQ do hub T1 | Destino de 68653 [CONFIRMAR] |
| Q7.5 | Como funciona a prova de bolsa de endocrinologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68648 e T1 | |
| Q7.6 | Quanto custa a pós em endocrinologia de pequenos animais da Ufape? | Decisão | resolver | 56 (24/14/18) | Investimento do pilar | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Endocrinologia | Pós-graduação em Endocrinologia de Pequenos Animais | Guia A7; prova 68648; FAQ de público; artigos clínicos [REVISÃO DOCENTE] |
| Nefrologia | Pós-graduação em Nefrologia e Urologia Veterinária (68612, sem compra) | Prova 68653 (só com destino); ponte com A14 (geriatria) |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Endocrinologia (68617) | Pós-graduação em Endocrinologia de Pequenos Animais, Faculdade UFAPE | Pós-graduação em Endocrinologia de Pequenos Animais, semipresencial, 500 h, em São Paulo. Veja módulos, investimento e prova de bolsa. | Pós-graduação em Endocrinologia de Pequenos Animais | Público e nível de entrada da Pós-graduação em Endocrinologia de Pequenos Animais [CONFIRMAR NO CATÁLOGO]; Turma [CONFIRMAR NO CATÁLOGO] (P5) |

---

### A12. Neurologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 68616 (e 701) | Pós-graduação em Neurologia e Neurocirurgia Veterinária | São Paulo, semipresencial, 500 h (701 iniciada, verificar) | 68616: 08/05/2027, IX | aberto | pós-graduação em neurologia e neurocirurgia veterinária | pós em neurologia veterinária; especialização em neurologia de cães e gatos; pós em neuro vet; pós em neurologia veterinária São Paulo |
| 68654 | Prova de Bolsa de Estudos para Neurologia e Neurocirurgia Veterinária | São Paulo, 27/11/2026 | 27/11/2026 | aberto | prova de bolsa de neurologia veterinária | bolsa de estudos pós neurologia e neurocirurgia |

Sem chamada de compra: 677 (Neurocirurgia e Neuro-oncologia, verificar) e 701. Por link, na linha Eventos: Workshop de Neuromonitorização (20 e 21/11/2026); não entra neste cluster.

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K12.1 | Entender | pós-graduação em neurologia veterinária | matricular | Médio | 56 (28/14/14) | Pilar Neurologia e Neurocirurgia (68616) | Anclivepa-SP e Módulo aparecem; a busca trouxe currículos que citam a pós da Ufape Intercursos (prova social a confirmar) |
| K12.2 | Entender | pós em neurologia e neurocirurgia veterinária em São Paulo | matricular | Baixo | 60 (30/8/22) | Pilar | Turma de maio de 2027 |
| K12.3 | Nome popular | pós em neuro vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K12.4 | Entender | pós em neurocirurgia veterinária | matricular | Baixo | 36 (14/8/14) | Pilar Neurocirurgia e Neuro-oncologia (677, sem compra) | Turma em "verificar" e preço mais alto do catálogo |
| K12.5 | Preço e condições | quanto custa pós em neurologia veterinária | resolver | Médio | 52 (22/14/16) | Investimento do pilar e T8 | |
| K12.6 | Prova de bolsa | prova de bolsa de neurologia veterinária | resolver | Médio | 60 (26/14/20) | Prova 68654 e T1 | |
| K12.7 | Comparar | neurologia ou neurocirurgia veterinária: qual pós escolher | comparar | Baixo | 44 (16/8/20) | Guia A12 | |
| K12.8 | EAD x presencial | pós em neurologia veterinária EAD | comparar | Médio | 36 (14/14/8) | Guia de formato | Sem EAD da Ufape |
| K12.9 | Carreira e título | como se especializar em neurologia veterinária; título de especialista | aprender | Médio | 34 (8/14/12) | Artigo de apoio e T6 | A busca citou a ABNV como entidade (resumo de busca de 26/10/2026, sem URL); conferir na fonte; [REVISÃO REGULAÇÃO] |
| K12.10 | Entender | exame neurológico em cães e gatos; hérnia de disco | aprender | Alto | 32 (4/20/8) | Artigos de apoio | [REVISÃO DOCENTE]; no limite do corte |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q12.1 | Pós em neurologia e neurocirurgia veterinária em São Paulo: qual existe e quando começa? | Solução | matricular | 56 (30/8/18) | Topo do pilar | 68616, 08/05/2027 |
| Q12.2 | Qual a diferença entre pós em neurologia e pós em neurocirurgia e neuro-oncologia? | Comparação | comparar | 44 (16/8/20) | Guia A12 | |
| Q12.3 | Para quem é a pós em neurologia veterinária? Preciso ter experiência? | Problema | resolver | 46 (24/8/14) | FAQ do pilar | A ficha não traz público-alvo [CONFIRMAR NO CATÁLOGO] |
| Q12.4 | Vale fazer pós em neurologia veterinária? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | |
| Q12.5 | Como funciona a prova de bolsa de neurologia da Ufape? | Decisão | resolver | 56 (26/14/16) | Prova 68654 e T1 | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Neurologia | Pós-graduação em Neurologia e Neurocirurgia Veterinária (página única; 701 recebe 301) | Guia A12; prova 68654; FAQ de nível de entrada; link para o evento de Neuromonitorização (linha Eventos) |
| Neurocirurgia | Pós-graduação em Neurocirurgia e Neuro-oncologia Veterinária (677, sem compra) | Guia A12 |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Neurologia (68616) | Pós-graduação em Neurologia e Neurocirurgia Veterinária, Faculdade UFAPE | Pós-graduação em Neurologia e Neurocirurgia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e prova de bolsa. | Pós-graduação em Neurologia e Neurocirurgia Veterinária | Nível de entrada da Pós-graduação em Neurologia e Neurocirurgia Veterinária [CONFIRMAR NO CATÁLOGO]; Neuroimagem e prática cirúrgica na Pós-graduação em Neurologia e Neurocirurgia Veterinária [REVISÃO DOCENTE] |

---

### A13. Medicina felina

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 650 | Pós-graduação em Medicina de Felinos | São Paulo, semipresencial, 500 h | 15/08/2026, VI (iniciada) | verificar: sem chamada de compra | pós-graduação em medicina de felinos | especialização em felinos; pós em medicina felina em São Paulo; pós em clínica médica de gatos; pós em felinos |
| 68652 | Prova de Bolsa de Estudos para Medicina de Felinos | São Paulo, 27/11/2026 | 27/11/2026 | aberto; turma de destino [CONFIRMAR] | prova de bolsa de medicina de felinos | o que cai na prova de bolsa de medicina felina; bibliografia da prova de bolsa de medicina de felinos; bolsa de estudos pós medicina felina |

A área não tem pós aberta. A página da prova (68652) é a mais completa do conjunto (conteúdo e bibliografia). Ela repete uma frase de reconhecimento ligada ao MEC e traz regras contraditórias (lacunas, seção 9): não copiar. Livres por link: 105, 340, 157, 459 e 347 (espanhol).

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K13.1 | Prova de bolsa | prova de bolsa de medicina de felinos | resolver | Médio | 56 (26/14/16) | Prova 68652 e T1 | Só subir campanha depois de definir o destino da prova |
| K13.2 | Prova de bolsa | o que cai na prova de bolsa de medicina felina; bibliografia | resolver | Baixo | 54 (24/8/22) | Artigo-guia da prova (a partir só da ficha) | P1 de A13 na entrada principal |
| K13.3 | Entender | pós-graduação em medicina de felinos | aprender | Médio | 40 (14/14/12) | Pilar Medicina de Felinos (650, sem compra) | Concorrência: Qualittas, Unyleya EAD, Equalis (persona) |
| K13.4 | Nome popular | especialização em felinos; pós em felinos; pós em gato | aprender | Médio | 38 (12/14/12) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K13.5 | Entender | pós em medicina felina em São Paulo | aprender | Baixo | 36 (14/8/14) | Pilar | Sem turma aberta |
| K13.6 | Comparar | pós em medicina de felinos ou clínica médica de pequenos animais | comparar | Baixo | 40 (14/8/18) | Guia ou FAQ | |
| K13.7 | EAD x presencial | pós em medicina felina EAD ou presencial | comparar | Médio | 36 (14/14/8) | FAQ | Unyleya EAD aparece na busca; Ufape sem EAD |
| K13.8 | Entender | cat friendly o que é; manejo do gato na consulta | aprender | Médio | 32 (6/14/12) | Artigo de apoio | Tendência forte (analise-de-tendencias); [REVISÃO DOCENTE]; não usar número de gatos (fontes divergem) |
| K13.9 | Carreira e título | vale a pena se especializar em medicina felina | aprender | Médio | 36 (8/14/14) | Artigo de apoio | |
| K13.10 | Carreira e título | título de especialista em medicina felina | aprender | Baixo | 30 (10/8/12) | T6 (bloqueado) | Abaixo do corte |

Goiânia: sem turma nem prova de felinos em Goiânia no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q13.1 | O que cai na prova de bolsa de medicina de felinos da Ufape e qual a bibliografia? | Decisão | resolver | 54 (24/8/22) | Artigo-guia e prova 68652 | Resposta já existe na página da prova; falta linguagem de busca |
| Q13.2 | Se eu passar na prova de bolsa de felinos, qual turma eu faço? | Decisão | resolver | 40 (24/8/8) | FAQ do hub T1 | Destino [CONFIRMAR]. Sem resposta, risco de reclamação |
| Q13.3 | Pós em medicina felina em São Paulo: quando abre a próxima turma? | Solução | matricular | 36 (24/8/4) | Pilar 650 | [CONFIRMAR] data da próxima turma; sem urgência inventada |
| Q13.4 | Vale a pena especializar em medicina de felinos? | Problema | aprender | 38 (10/14/14) | Artigo de apoio | |
| Q13.5 | Pós em medicina felina presencial ou EAD: qual escolher? | Comparação | comparar | 36 (14/14/8) | FAQ | |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Medicina felina | Pós-graduação em Medicina de Felinos (650, sem compra) | Artigo-guia da prova 68652; T1; links para os livres 105, 340, 157 e 459; artigo "por onde começar" [REVISÃO REGULAÇÃO] |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Medicina de Felinos (650) | Pós-graduação em Medicina de Felinos, Faculdade UFAPE | Pós-graduação em Medicina de Felinos, semipresencial, 500 h, em São Paulo. Veja o conteúdo e como funciona a prova de bolsa. | Pós-graduação em Medicina de Felinos | Sem H2 de compra enquanto estiver em "verificar"; Próxima turma da Pós-graduação em Medicina de Felinos [CONFIRMAR] |
| Prova de Medicina de Felinos (68652) | Prova de Bolsa de Estudos para Medicina de Felinos, Faculdade UFAPE | Prova de bolsa de medicina de felinos em 27/11/2026, em São Paulo. Veja conteúdo, bibliografia e regras. | Prova de Bolsa de Estudos para Medicina de Felinos | Conteúdo da prova de bolsa para a Pós-graduação em Medicina de Felinos; Bibliografia sugerida; Regras (depois de resolvidas as contradições) |

---

### A9. Oftalmologia

**Recorte e páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Status | Palavra principal | Secundárias |
|---|---|---|---|---|---|---|
| 707 | Pós-graduação em Oftalmologia Veterinária | São Paulo, semipresencial, 600 h | 30/10/2026, VII | aberto | pós-graduação em oftalmologia veterinária | pós em oftalmologia veterinária presencial São Paulo; pós em oftalmologia clínica veterinária; especialização em oftalmologia de cães e gatos; pós em oftalmo vet; pós em oftalmologia veterinária 600 horas |

Prova de bolsa: 68656 está fora do ar. Não existe prova de Oftalmologia em 27/11. Livres por link: contínuos 627, 482 e 720 e cursos de microcirurgia e imagem oftálmica sem data (589, 576, 590, 603, 604, 606).

**Palavras-chave**

| ID | Grupo | Termo | Intenção | Volume (est.) | Pontuação (M/D/F) | Página-alvo | Observação |
|---|---|---|---|---|---|---|---|
| K9.1 | Entender | pós-graduação em oftalmologia veterinária | matricular | Médio | 56 (28/14/14) | Pilar Oftalmologia (707) | Guia da Carreira e Quero Bolsa mostram quase só EAD |
| K9.2 | EAD x presencial | pós em oftalmologia veterinária presencial em São Paulo | matricular | Médio | 62 (30/14/18) | Pilar Oftalmologia | A busca não confirmou pós presencial em São Paulo além de registro antigo de concorrente: espaço aberto [SUPOSIÇÃO] |
| K9.3 | Entender | pós em oftalmologia clínica veterinária | matricular | Médio | 54 (26/14/14) | Pilar Oftalmologia | Nome usado por agregadores |
| K9.4 | Nome popular | pós em oftalmo vet | matricular | Baixo | 50 (24/8/18) | Lista de palavras e grupo de anúncio | Não vai para texto visível |
| K9.5 | Preço e condições | quanto custa pós em oftalmologia veterinária | resolver | Alto | 56 (24/20/12) | Investimento do pilar | Objeção principal: ticket de R$ 47.700,00 contra EAD de R$ 60 a R$ 500 por mês. Responder com estrutura (microscópio individual e horas, da ficha [CONFIRMAR NO CATÁLOGO]) sem comparar preço |
| K9.6 | Comparar | pós em oftalmologia veterinária ou curso de microcirurgia ocular | comparar | Baixo | 44 (16/8/20) | Guia A9, link para os livres | Livres sem data: sem chamada de compra |
| K9.7 | Comparar | pós ou residência em oftalmologia veterinária | comparar | Médio | 40 (14/14/12) | T5 | A busca citou a UFRRJ e a Anclivepa como residência e pós (resumo de busca de 26/10/2026, sem URL; conferir na fonte); [REVISÃO REGULAÇÃO] |
| K9.8 | Carreira e título | título de especialista em oftalmologia veterinária (CBOV) | aprender | Médio | 36 (10/14/12) | T6 (bloqueado) | A busca citou o CBOV como entidade que concede o título (resumo de busca de 26/10/2026, sem URL); conferir a regra na fonte |
| K9.9 | Entender | oftalmologia na clínica de pequenos animais: o que resolver e o que encaminhar | aprender | Médio | 32 (6/14/12) | Artigo de apoio | [REVISÃO DOCENTE] |
| K9.10 | Prova de bolsa | prova de bolsa de oftalmologia veterinária | resolver | Baixo | 24 (20/8/-4) | Nenhuma | Não existe prova aberta: não mirar o termo e remover o bloco "prova de bolsa" da página de 707 [CONFIRMAR]. A coluna F fica negativa porque a página prometeria o que não existe |

Goiânia: sem turma nesta área no catálogo.

**Perguntas para assistentes de IA**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q9.1 | Pós em oftalmologia veterinária presencial em São Paulo: qual existe e como são os módulos? | Solução | matricular | 58 (30/14/14) | Topo do pilar | 707, 600 h, semipresencial; módulos de 3 dias na ficha [CONFIRMAR NO CATÁLOGO] |
| Q9.2 | Pós em oftalmologia ou só curso de microcirurgia ocular, qual faço? | Comparação | comparar | 44 (16/8/20) | Guia A9 | |
| Q9.3 | Quanto custa a pós em oftalmologia veterinária da Ufape e por que o valor é esse? | Decisão | resolver | 56 (24/14/18) | FAQ "por que o investimento é esse" | Só dados da ficha e do catálogo |
| Q9.4 | Preciso de pós ou de residência para ser oftalmologista veterinário? | Problema | aprender | 36 (10/14/12) | T5 e T6 | [REVISÃO REGULAÇÃO] |
| Q9.5 | Cada aluno opera com microscópio na pós em oftalmologia da Ufape? | Decisão | resolver | 46 (24/8/14) | FAQ do pilar | A ficha cita microscópio individual por aluno [CONFIRMAR NO CATÁLOGO] |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Oftalmologia | Pós-graduação em Oftalmologia Veterinária | FAQ de investimento; guia "Pós-graduação em Oftalmologia Veterinária ou curso de microcirurgia" com link para os livres; T5 e T6; artigo "como se especializar" [REVISÃO REGULAÇÃO] |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Oftalmologia (707) | Pós-graduação em Oftalmologia Veterinária, Faculdade UFAPE | Pós-graduação em Oftalmologia Veterinária, semipresencial, 600 h, em São Paulo. Veja módulos, investimento e como funcionam as aulas. | Pós-graduação em Oftalmologia Veterinária | Por que o investimento na Pós-graduação em Oftalmologia Veterinária é esse (estrutura e horas da ficha); Pós-graduação em Oftalmologia Veterinária ou curso de microcirurgia; Prova de bolsa da Pós-graduação em Oftalmologia Veterinária: bloco só se houver destino válido |

---

### A14. Outras especialidades (por curso)

Tratada por curso, como manda o plano do cmo. Odontologia e Nutrologia estão em "verificar" ou sem turma aberta no recorte.

**Páginas de curso**

| Código | Página | Local, modalidade, CH | Início e turma | Palavra principal | Secundárias | Intenção | Volume (est.) | Pontuação (M/D/F) | Observação |
|---|---|---|---|---|---|---|---|---|---|
| 341 | Pós-graduação em Medicina Interna Equina (catálogo: "Pós Graduação em Medicina Interna Equina") | São Paulo, semipresencial, 500 h | 20/03/2027, I | pós-graduação em medicina interna equina | pós em medicina equina; especialização em clínica de equinos; pós em cavalos veterinária; pós em equinos vet; pós em medicina interna equina São Paulo | matricular | Baixo | 56 (28/8/20) | Público de equinos viaja mais [SUPOSIÇÃO]. A ficha cita um segundo local: onde é a prática [CONFIRMAR NO CATÁLOGO]. Promoção de 20% com texto cortado: não citar [CONFIRMAR NO CATÁLOGO] |
| 679 | Pós-graduação em Infectologia Veterinária | São Paulo, semipresencial, 500 h | 03/04/2027, IV | pós-graduação em infectologia veterinária | especialização em infectologia de cães e gatos; pós em doenças infecciosas veterinária; pós em infecto vet | matricular | Baixo | 54 (28/8/18) | Link da planilha (linha "Citopatologia 03/04") aponta para esta página: confirmar [CONFIRMAR NO CATÁLOGO] |
| 382 | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos | São Paulo, semipresencial, 500 h | 22/05/2027, I | pós-graduação em reprodução de cães e gatos | pós em obstetrícia veterinária; pós em neonatologia veterinária; especialização em reprodução animal de pequenos animais; pós em reprodução vet | matricular | Médio | 52 (26/14/12) | Curso novo; público inclui criadores [SUPOSIÇÃO]. Nome do catálogo é longo: título usa o nome completo |
| 699 | Pós-graduação em Geriatria Veterinária | São Paulo, semipresencial, 500 h | 22/05/2027, I | pós-graduação em geriatria veterinária | especialização em geriatria de cães e gatos; pós em cuidados paliativos veterinária; pós em geriatria vet; paciente geriátrico cães e gatos pós | matricular | Médio | 58 (28/14/16) | Sinal de tendência forte (longevidade); a busca não trouxe pós brasileira específica [SUPOSIÇÃO de espaço aberto]. Ficha com contradições de público, cronograma e lotação: corrigir antes de qualquer peça [CONFIRMAR NO CATÁLOGO] |
| 60 | Pós-graduação em Medicina de Silvestres | São Paulo, semipresencial, 360 h | 28/05/2027, I | pós-graduação em medicina de silvestres | pós em animais silvestres e exóticos; especialização em animais silvestres veterinária; pós em exóticos vet; pós em medicina de animais exóticos | matricular | Baixo | 54 (28/8/18) | Quero Bolsa tem matéria sobre a especialização. A página repete número de mercado sem conferir: não copiar. Turma mínima de 15 na ficha, não 20 [CONFIRMAR NO CATÁLOGO] |
| 719 | Pós-graduação em Inteligência Artificial na Saúde (catálogo: "Pós-Graduação Inteligência Artificial na Saúde") | São Paulo, semipresencial, 360 h | 08/05/2027, I | pós-graduação em inteligência artificial na saúde | pós em IA na saúde; especialização em inteligência artificial para saúde; pós em IA para médicos | matricular | Médio | 40 (20/14/6) | Menor total da linha (18x de R$ 666,67, R$ 12.000,00, matrícula de R$ 250,00). Público de saúde humana e TI, não de veterinários: persona e canal próprios [CONFIRMAR público]. Termo de cabeça muito disputado. Não ligar ao cluster de imagem veterinária |
| 68662, 678 (verificar), prova 68655 | Pós-graduação em Odontologia Veterinária | São Paulo, semipresencial, 500 h | verificar (iniciada, data diverge) | pós-graduação em odontologia veterinária | especialização em odontologia de cães e gatos; pós em odonto vet; prova de bolsa de odontologia veterinária | matricular | Médio | 36 (14/14/8) | Sem chamada de compra; prova sem turma de destino [CONFIRMAR]. Uma página única e o destino da prova são as lacunas P1 |

**Perguntas para assistentes de IA (A14)**

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| Q14.1 | Existe pós em geriatria veterinária no Brasil? Quando começa a primeira turma da Ufape? | Solução | matricular | 56 (28/14/14) | Topo do pilar 699 | Só depois de corrigir a ficha |
| Q14.2 | Pós em medicina interna equina em São Paulo: onde são as aulas práticas com cavalos? | Decisão | resolver | 46 (24/8/14) | FAQ do pilar 341 | [CONFIRMAR NO CATÁLOGO] |
| Q14.3 | Pós em medicina de silvestres e exóticos vale a pena para quem atende pets não convencionais? | Problema | aprender | 36 (10/8/18) | FAQ do pilar 60 | [REVISÃO DOCENTE] |
| Q14.4 | Pós em reprodução de cães e gatos para veterinário: o que a Ufape oferece? | Solução | matricular | 52 (26/8/18) | Topo do pilar 382 | |
| Q14.5 | Existe pós em infectologia veterinária em São Paulo? | Solução | matricular | 52 (28/8/16) | Topo do pilar 679 | |
| Q14.6 | Pós em inteligência artificial na saúde serve para veterinário? | Problema | resolver | 36 (20/8/8) | FAQ do pilar 719 | Público [CONFIRMAR]; sem resposta até a decisão |
| Q14.7 | Pós em odontologia veterinária em São Paulo | Solução | matricular | 40 (24/8/8) | Pilar Odontologia | Sem compra enquanto "verificar" |

**Pilar e apoio**

| Cluster | Pilar | Apoio |
|---|---|---|
| Geriatria | Pós-graduação em Geriatria Veterinária | Série "paciente geriátrico" [REVISÃO DOCENTE]; ponte com A1 (dor) e A7 |
| Equinos | Pós-graduação em Medicina Interna Equina | FAQ "onde é a prática com cavalos"; prova: não há |
| Silvestres | Pós-graduação em Medicina de Silvestres | Artigo de entrada em exóticos [REVISÃO DOCENTE] |
| Reprodução | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos | FAQ de público |
| Infectologia | Pós-graduação em Infectologia Veterinária | FAQ e guia "infectologia na clínica" [REVISÃO DOCENTE] |
| IA na Saúde | Pós-graduação em Inteligência Artificial na Saúde | Só depois da decisão de público |
| Odontologia | Pós-graduação em Odontologia Veterinária | Prova 68655 (só com destino) |

**Briefing SEO resumido**

| Página | Título | Descrição | H1 | H2 específicos |
|---|---|---|---|---|
| Medicina Interna Equina (341) | Pós-graduação em Medicina Interna Equina, Faculdade UFAPE | Pós-graduação em Medicina Interna Equina, semipresencial, 500 h, em São Paulo. Veja módulos, local da prática e investimento. | Pós-graduação em Medicina Interna Equina | Onde são as aulas práticas da Pós-graduação em Medicina Interna Equina [CONFIRMAR NO CATÁLOGO] |
| Infectologia (679) | Pós-graduação em Infectologia Veterinária, Faculdade UFAPE | Pós-graduação em Infectologia Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Infectologia Veterinária | Infectologia na rotina clínica e a Pós-graduação em Infectologia Veterinária [REVISÃO DOCENTE] |
| Reprodução (382) | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos, Faculdade UFAPE | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos, semipresencial, 500 h, em São Paulo. Veja módulos. | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos | Para quem é a Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução: clínicos e criadores [CONFIRMAR NO CATÁLOGO] |
| Geriatria (699) | Pós-graduação em Geriatria Veterinária, Faculdade UFAPE | Pós-graduação em Geriatria Veterinária, semipresencial, 500 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Geriatria Veterinária | Público, cronograma e lotação da Pós-graduação em Geriatria Veterinária: só depois de corrigir a ficha [CONFIRMAR NO CATÁLOGO] |
| Silvestres (60) | Pós-graduação em Medicina de Silvestres, Faculdade UFAPE | Pós-graduação em Medicina de Silvestres, semipresencial, 360 h, em São Paulo. Veja módulos, turma e investimento. | Pós-graduação em Medicina de Silvestres | Silvestres e exóticos: por onde começar a Pós-graduação em Medicina de Silvestres [REVISÃO DOCENTE] |
| IA na Saúde (719) | Pós-graduação em Inteligência Artificial na Saúde, Faculdade UFAPE | Pós-graduação em Inteligência Artificial na Saúde, semipresencial, 360 h, em São Paulo. Veja módulos, turma e requisitos. | Pós-graduação em Inteligência Artificial na Saúde | Público e requisitos de equipamento da Pós-graduação em Inteligência Artificial na Saúde [CONFIRMAR NO CATÁLOGO]; ato regulatório [CONFIRMAR NO CATÁLOGO] |

---

## 5. Campanha das provas de bolsa de 27/11/2026

Base: catálogo, seção 3 (22 provas abertas em 19 especialidades, inscrição de R$ 100,00 à vista, Pix ou boleto, ou 1x no cartão, prova em 27/11/2026 em São Paulo e em Goiânia; Anestesiologia, Cardiologia e Clínica Cirúrgica têm prova nas duas cidades) e regras do contexto da linha (11 bolsas por prova: 2 de 50%, 4 de 25% e 5 de 10%; nota de corte 7,0; resultado por WhatsApp ou e-mail; recurso em 2 dias úteis; matrícula em 10 dias úteis; bolsa não acumulativa e intransferível). As fichas se contradizem em partes (canal do resultado, prazo de matrícula de 10 ou 7 dias, turma mínima de 15 ou 20): [CONFIRMAR NO CATÁLOGO] antes de peça. Data de encerramento das inscrições: [CONFIRMAR NO CATÁLOGO]. Turma de destino de cada prova: [CONFIRMAR].

### 5.1 Hub da prova de bolsa (T1)

| Item | Proposta |
|---|---|
| Palavra principal | prova de bolsa pós-graduação veterinária |
| Secundárias | prova de bolsa pós-graduação medicina veterinária; como funciona a prova de bolsa de pós veterinária; prova de bolsa Ufape; prova de bolsa 27 de novembro; bolsa de estudos pós em medicina veterinária; prova de bolsa pós em Goiânia; prova de bolsa pós em São Paulo; quanto custa a inscrição da prova de bolsa; quantas bolsas tem a prova |
| Intenção | resolver (a pessoa já considera a pós e quer reduzir o preço) |
| Volume (est.) | Médio [SUPOSIÇÃO]; o concorrente de marca tem edital com inscrições abertas até 07/11/2026 (sinal de interesse na época) |
| Pontuação | 60 (28/14/18) |
| Página-alvo | Hub "Prova de bolsa de estudos" (nova), ligado a cada página de prova |
| URL | [CONFIRMAR]; sugestão /pos-graduacao/prova-de-bolsa [SUPOSIÇÃO] |
| Título proposto | Prova de Bolsa de Estudos da Pós-graduação, Faculdade UFAPE |
| Descrição proposta | Prova de bolsa para a pós-graduação da Faculdade UFAPE em 27/11/2026, em São Paulo e Goiânia. Veja especialidades, regras e como se inscrever. |
| H1 | Prova de bolsa de estudos da Pós-graduação |
| H2 | Como funciona a prova de bolsa da Pós-graduação; Quantas bolsas e quais percentuais; Datas, local e inscrição; Especialidades com prova (um bloco por Pós-graduação em <área>); Resultado, recurso e matrícula; O que acontece com a bolsa depois da aprovação; Perguntas frequentes |
| Bloco citável | "A prova de bolsa da Faculdade UFAPE acontece em 27/11/2026, em São Paulo e Goiânia, com inscrição de R$ 100,00. Cada prova tem 11 bolsas: 2 de 50%, 4 de 25% e 5 de 10%. A nota de corte é 7,0. A bolsa não é acumulativa nem intransferível para outra pessoa, e o candidato pode fazer recurso em 2 dias úteis." Só publicar depois de [CONFIRMAR NO CATÁLOGO] as regras e a turma de destino |

Regra: sem "últimas vagas", sem urgência sem número real, sem promessa de bolsa e sem frase de certificação.

### 5.2 Páginas de cada prova (uma palavra principal por página)

Padrão: palavra principal "prova de bolsa de <especialidade> veterinária"; título "Prova de Bolsa de Estudos para <especialidade>, Faculdade UFAPE" (nome do catálogo, com a marca separada por vírgula ou por barra vertical no título final); um link para o hub e um link para a pós da área.

| Área | Provas (código) | Palavra principal | Estado |
|---|---|---|---|
| A1 | 68639 (SP), 68640 (Goiânia) | prova de bolsa de anestesiologia veterinária | pronta para campanha |
| A2 | 68641, 68642 (links invertidos, P3), 68659 | prova de bolsa de cardiologia veterinária; prova de bolsa de pneumologia veterinária | corrigir links antes |
| A3 | 68645, 68660 | prova de bolsa de clínica médica e emergência veterinária; prova de bolsa de terapia intensiva veterinária | pronta |
| A4 | 68643 (SP), 68644 (Goiânia) | prova de bolsa de clínica cirúrgica de cães e gatos | pronta |
| A5 | 68647, 68661, 68649 | prova de bolsa de diagnóstico por imagem veterinário; de ultrassonografia veterinária; de endoscopia veterinária | 68649 sem destino |
| A6 | 68650 | prova de bolsa de gastroenterologia veterinária | pronta |
| A7 | 68648, 68653 | prova de bolsa de endocrinologia de pequenos animais; de nefrologia e urologia veterinária | 68653 sem destino |
| A8 | 68646 | prova de bolsa de dermatologia veterinária | pronta |
| A10 | 68657 | prova de bolsa de oncologia veterinária | pronta |
| A11 | 68651, 68658 | prova de bolsa de hematologia veterinária; de patologia clínica veterinária | pronta |
| A12 | 68654 | prova de bolsa de neurologia veterinária | pronta |
| A13 | 68652 | prova de bolsa de medicina de felinos | sem destino |
| A14 | 68655 | prova de bolsa de odontologia veterinária | sem destino |
| A9 | 68656 | (nenhuma) | fora do ar: não mirar |

Não há prova de Ecocardiografia no catálogo.

### 5.3 Estrutura sugerida para o Google Search (proposta para aprovação humana)

Nada foi criado no gerenciador. Quem aprova: pessoa do marketing (verba e anúncio), com o gestor-de-midia. O que: estrutura de grupos de anúncio. Por que: a busca por "prova de bolsa" tem intenção alta e janela curta (até 27/11/2026). Quanto: [CONFIRMAR] (verba não informada). Efeito esperado: inscrições na prova (sem número, não há linha de base). Como desfazer: pausar as campanhas pelo gerenciador, feito por humano.

| Grupo | Palavras (tema) | Tipo de correspondência sugerida [SUPOSIÇÃO] | Página de destino | Observação |
|---|---|---|---|---|
| G1 Marca | prova de bolsa ufape; faculdade ufape prova de bolsa; ufape intercursos pós | exata e frase | Hub | Proteger a marca; negativar "universidade federal", "pernambuco", "agreste" |
| G2 Genérico | prova de bolsa pós-graduação veterinária; prova de bolsa pós medicina veterinária; bolsa de estudos pós veterinária | frase | Hub | Termo de maior volume e mais disputado por concorrente e agregador |
| G3 Por especialidade | prova de bolsa de <especialidade> veterinária (22 provas abertas em 19 especialidades; sem as 4 provas sem destino, 18 provas em 15 especialidades; uma por grupo ou por tema) | frase e exata | Página da prova | Fora: 68656 (Oftalmologia, sem prova); 68652, 68649, 68653 e 68655 só com destino definido |
| G4 Regras | como funciona prova de bolsa pós veterinária; quantas bolsas tem a prova; quanto custa a inscrição da prova de bolsa | frase | Hub (seção de regras) | Resposta curta no anúncio sem prometer bolsa |
| G5 Praça | prova de bolsa pós em Goiânia; prova de bolsa pós em São Paulo; prova de bolsa pós cardiologia Goiânia | frase | Provas de Goiânia (68640, 68642 e 68644) e hub | Só 3 provas em Goiânia |
| G6 Concorrente | prova de bolsa anclivepa; provão anclivepa | não ativar | - | Decisão humana: risco de marca e de comparação sem fonte [CONFIRMAR com jurídico]. Sugestão: não ativar |

Palavras negativas sugeridas [SUPOSIÇÃO]: grátis, gratuita, concurso, residência, mestrado, doutorado, stricto sensu, enem, prouni, fies, universidade federal, ufape pernambuco, agreste, medicina humana, enfermagem.

Calendário de leilão: o gestor-de-midia decide início e fim. Janela útil: do pedido de aprovação até 27/11/2026 [CONFIRMAR data de encerramento das inscrições].

### 5.4 Perguntas das provas para assistentes de IA

| ID | Pergunta | Estágio | Intenção | Pontuação (M/D/F) | Bloco citável e página | Observação |
|---|---|---|---|---|---|---|
| QP1 | Como funciona a prova de bolsa da Ufape e quantas bolsas tem cada especialidade? | Decisão | resolver | 58 (26/14/18) | Hub | Regras com contradições [CONFIRMAR NO CATÁLOGO] |
| QP2 | Quanto custa a inscrição da prova de bolsa da Ufape e quando é a prova? | Decisão | resolver | 56 (26/14/16) | Hub | R$ 100,00; 27/11/2026 (catálogo) |
| QP3 | A prova de bolsa da Ufape é presencial? Onde fazer? | Decisão | resolver | 52 (24/14/14) | Hub | São Paulo e Goiânia; local exato [CONFIRMAR] |
| QP4 | O que cai na prova de bolsa de pós em medicina veterinária da Ufape? | Problema | resolver | 46 (22/8/16) | Hub e artigo-guia | Só felinos tem conteúdo e bibliografia na ficha |
| QP5 | Se eu passar na prova de bolsa, em quanto tempo preciso me matricular e a bolsa vale para qual turma? | Decisão | resolver | 50 (26/8/16) | Hub (FAQ) | 10 dias úteis (contexto) ou 7 (ficha): [CONFIRMAR]; destino [CONFIRMAR] |
| QP6 | Prova de bolsa de pós veterinária: Ufape ou Anclivepa, qual vale mais a pena? | Comparação | comparar | 38 (14/8/16) | Hub (critérios, sem nomear) | Comparar só com critérios e dado conferido de cada lado; sem ranking |
| QP7 | Posso acumular a bolsa com outro desconto da Ufape? | Decisão | resolver | 40 (22/8/10) | Hub (FAQ) | Bolsa não acumulativa (contexto); acumulação com descontos de 341, 359 e 352 [CONFIRMAR] |

---

## 6. Tabela consolidada

Prioridade (seção 2.4). Uma palavra principal por página. A coluna "Página de destino" usa o nome padrão e o código do catálogo.

| Área | Palavra principal | Intenção | Prioridade | Página de destino |
|---|---|---|---|---|
| Transversal | prova de bolsa pós-graduação veterinária | resolver | P1 | Hub da prova de bolsa (T1) |
| Transversal | pós em medicina veterinária Goiânia | matricular | P1 | Listagem de Goiânia [SUPOSIÇÃO] |
| Transversal | quanto custa pós em medicina veterinária | resolver | P1 | T8 Investimento e formas de pagamento |
| Transversal | como escolher pós-graduação em medicina veterinária | comparar | P2 | T4 Guia de escolha |
| Transversal | pós-graduação ou residência em medicina veterinária | comparar | P2 | T5 |
| Transversal | pós em medicina veterinária semipresencial | comparar | P2 | T7 Como funciona a Pós-graduação semipresencial |
| Transversal | pós lato sensu dá título de especialista CFMV | aprender | P3 (bloqueado) | T6 |
| Transversal | faculdade ufape pós-graduação | matricular | P2 | Página institucional (T9) |
| A2 | pós-graduação em ecocardiografia veterinária | matricular | P1 | Pós-graduação em Ecocardiografia (698) |
| A2 | pós-graduação em cardiologia veterinária | matricular | P1 | Pós-graduação em Cardiologia Veterinária (289 e 68605) |
| A2 | pós-graduação em pneumologia veterinária | matricular | P2 | Pós-graduação em Pneumologia Veterinária (68636) |
| A2 | pós-graduação em ventilação mecânica veterinária | matricular | P2 | Pós-graduação em Ventilação Mecânica (352) |
| A2 | cardiologia ou ecocardiografia veterinária: qual pós escolher | comparar | P2 | Guia A2 |
| A2 | prova de bolsa de cardiologia veterinária; de pneumologia | resolver | P1 | Provas 68641, 68642 e 68659 |
| A8 | pós-graduação em dermatologia veterinária | matricular | P1 | Pós-graduação em Dermatologia Veterinária (68610) |
| A8 | dermatologia veterinária EAD ou presencial: qual vale mais | comparar | P1 | Guia de formato de A8 |
| A8 | prova de bolsa de dermatologia veterinária | resolver | P1 | Prova 68646 |
| A5 | pós-graduação em diagnóstico por imagem veterinária | matricular | P1 | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária (68604) |
| A5 | pós-graduação em ultrassonografia veterinária | matricular | P2 | Pós-graduação em Ultrassonografia de Pequenos Animais (68629) |
| A5 | diagnóstico por imagem ou ultrassonografia: qual pós escolher | comparar | P2 | Guia A5 |
| A5 | prova de bolsa de diagnóstico por imagem veterinário; de ultrassonografia | resolver | P1 | Provas 68647 e 68661 |
| A5 | pós em endoscopia veterinária | aprender | P3 | Pós-graduação em Endoscopia Veterinária (653, sem compra); prova 68649 só com destino |
| A11 | pós-graduação em hematologia veterinária | matricular | P1 | Pós-graduação em Hematologia Veterinária (68608) |
| A11 | pós-graduação em patologia clínica veterinária | matricular | P1 | Pós-graduação em Patologia Clínica (68615) |
| A11 | pós-graduação em citopatologia veterinária | matricular | P2 | Pós-graduação em Citopatologia Veterinária (333) |
| A11 | hematologia, patologia clínica ou citopatologia: qual pós escolher | comparar | P1 | Guia A11 |
| A11 | prova de bolsa de hematologia veterinária; de patologia clínica | resolver | P1 | Provas 68651 e 68658 |
| A6 | pós-graduação em gastroenterologia veterinária | matricular | P1 | Pós-graduação em Gastroenterologia Veterinária (68606) |
| A6 | prova de bolsa de gastroenterologia veterinária | resolver | P1 | Prova 68650 |
| A1 | pós-graduação em anestesiologia veterinária | matricular | P1 | Pós-graduação em Anestesiologia Veterinária (68609, página única) |
| A1 | pós-graduação em anestesiologia avançada veterinária | matricular | P1 | Pós-graduação em Anestesiologia Avançada (657) |
| A1 | pós-graduação em anestesiologia locorregional veterinária | matricular | P2 | Pós-graduação em Anestesiologia Locorregional Veterinária (359) |
| A1 | anestesiologia ou anestesiologia avançada: qual pós escolher | comparar | P1 | Guia A1 |
| A1 | prova de bolsa de anestesiologia veterinária | resolver | P1 | Provas 68639 e 68640 |
| A3 | pós-graduação em terapia intensiva veterinária | matricular | P2 | Pós-graduação em Terapia Intensiva e Emergência Veterinária (68623) |
| A3 | pós-graduação em clínica médica e emergência de pequenos animais | matricular | P2 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais (68635) |
| A3 | clínica médica e emergência ou terapia intensiva: qual pós escolher | comparar | P1 | Guia A3 |
| A3 | prova de bolsa de terapia intensiva veterinária; de clínica médica e emergência | resolver | P1 | Provas 68660 e 68645 |
| A4 | pós-graduação em clínica cirúrgica de cães e gatos | matricular | P2 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos (68632) |
| A4 | pós-graduação em videocirurgia veterinária | matricular | P2 | Pós-graduação em Videocirurgia Veterinária (578) |
| A4 | pós-graduação em ortopedia veterinária | matricular | P2 | Pós-graduação em Ortopedia Veterinária (662, após corrigir dados) |
| A4 | pós-graduação em fisioterapia veterinária | matricular | P2 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária (366) |
| A4 | prova de bolsa de clínica cirúrgica de cães e gatos | resolver | P1 | Provas 68643 e 68644 |
| A10 | pós-graduação em oncologia veterinária | matricular | P2 | Pós-graduação em Oncologia Veterinária (68628) |
| A10 | prova de bolsa de oncologia veterinária | resolver | P1 | Prova 68657 |
| A7 | pós-graduação em endocrinologia de pequenos animais | matricular | P2 | Pós-graduação em Endocrinologia de Pequenos Animais (68617) |
| A7 | prova de bolsa de endocrinologia de pequenos animais | resolver | P1 | Prova 68648 |
| A7 | prova de bolsa de nefrologia e urologia veterinária | resolver | P3 (sem destino) | Prova 68653 |
| A12 | pós-graduação em neurologia e neurocirurgia veterinária | matricular | P2 | Pós-graduação em Neurologia e Neurocirurgia Veterinária (68616) |
| A12 | prova de bolsa de neurologia veterinária | resolver | P1 | Prova 68654 |
| A13 | prova de bolsa de medicina de felinos | resolver | P1 (após definir destino) | Prova 68652 e artigo-guia |
| A13 | pós-graduação em medicina de felinos | aprender | P3 (turma iniciada) | Pós-graduação em Medicina de Felinos (650, sem compra) |
| A9 | pós-graduação em oftalmologia veterinária | matricular | P1 (reta final e próxima edição) | Pós-graduação em Oftalmologia Veterinária (707) |
| A14 | pós-graduação em medicina interna equina | matricular | P2 | Pós-graduação em Medicina Interna Equina (341) |
| A14 | pós-graduação em infectologia veterinária | matricular | P2 | Pós-graduação em Infectologia Veterinária (679) |
| A14 | pós-graduação em reprodução de cães e gatos | matricular | P2 | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos (382) |
| A14 | pós-graduação em geriatria veterinária | matricular | P1 (corrigir ficha) e P2 | Pós-graduação em Geriatria Veterinária (699) |
| A14 | pós-graduação em medicina de silvestres | matricular | P2 | Pós-graduação em Medicina de Silvestres (60) |
| A14 | pós-graduação em inteligência artificial na saúde | matricular | P3 (público a decidir) | Pós-graduação em Inteligência Artificial na Saúde (719) |
| A14 | pós-graduação em odontologia veterinária | matricular | P3 (sem turma aberta) | Pós-graduação em Odontologia Veterinária (678 e 68662); prova 68655 só com destino |

---

## 7. As 10 palavras mais perto da matrícula

Critério: intenção de matricular ou resolver, turma ou prova em 2026 ou março de 2027, pontuação alta e sem bloqueio de regulação. Prazo: anúncio de busca por termo de cauda e página corrigida valem agora; ranqueamento orgânico de página nova leva semanas [SUPOSIÇÃO].

| # | Termo | Página | Pontuação | Por que está perto da matrícula |
|---|---|---|---|---|
| 1 | prova de bolsa pós-graduação veterinária | Hub (T1) | 60 | Porta de entrada; prova em 27/11/2026, inscrição de R$ 100,00 |
| 2 | pós-graduação em ecocardiografia veterinária | Ecocardiografia (698) | 62 | Início em 28/11/2026; pouca concorrência visível; corrigir data do site antes |
| 3 | pós em dermatologia veterinária presencial em São Paulo (semipresencial) | Dermatologia (68610) | 62 | Início em 28/11/2026; a busca por presencial devolve quase só EAD |
| 4 | pós-graduação em gastroenterologia veterinária | Gastroenterologia (68606) | 62 | Início em 07/11/2026; resultados dominados por medicina humana |
| 5 | pós em diagnóstico por imagem veterinário semipresencial em São Paulo | Imagem (68604) | 62 | Início em 31/10/2026; serve também à prova de imagem |
| 6 | pós-graduação em ultrassonografia veterinária | Ultrassonografia (68629) | 62 | Menor ticket da área A5 (R$ 16.456,00 no total); turma aberta de maio de 2027 |
| 7 | pós em oftalmologia veterinária presencial em São Paulo | Oftalmologia (707) | 62 | Início em 30/10/2026; espaço de formato presencial |
| 8 | pós-graduação em hematologia veterinária | Hematologia (68608) | 60 | Início em 28/11/2026; prova de hematologia no mesmo mês |
| 9 | pós em cardiologia veterinária em Goiânia | Cardiologia (289) | 60 | Cauda local; turma de 20/03/2027 e prova de Goiânia |
| 10 | pós em terapia intensiva veterinária em Goiânia | Terapia Intensiva (68623) | 60 | Cauda local; turma de maio de 2027 e prova de terapia intensiva |

Também de alta pontuação e perto da matrícula, fora do top 10 por prazo ou bloqueio: pós em clínica cirúrgica presencial em Goiânia (60, turma de 10/04/2027), prova de bolsa por especialidade (60 em 13 especialidades com destino definido: anestesiologia, cardiologia, clínica cirúrgica, dermatologia, diagnóstico por imagem, endocrinologia, gastroenterologia, hematologia, neurologia, oncologia, patologia clínica, terapia intensiva e ultrassonografia), pós-graduação em anestesiologia avançada (58, turma de 13/03/2027), pós-graduação em patologia clínica veterinária (60, turma de 20/03/2027).

---

## 8. Roteiro de checagem manual e próximos passos de pesquisa

1. **Sugestões do Google e "As pessoas também perguntam":** pessoa do marketing digita os 14 termos principais e os termos da seção 5.1 no Google, sem login, e registra as sugestões do preenchimento automático e as perguntas relacionadas. Acrescentar ao arquivo o que aparecer; descartar o que não existir.
2. **Search Console:** pedir exportação de consultas e páginas dos últimos 16 meses (já pedida na entrada principal). Com ela, trocar "Volume (est.)" por impressões e cliques reais e medir canibalização entre as páginas duplicadas (C1).
3. **Planejador de palavras-chave ou ferramenta de volume:** se a Ufape fornecer exportação, recalcular D (demanda) das linhas com número real.
4. **Assistentes de IA:** para cada pergunta das seções 3, 4 e 5.4 (cerca de 100), abrir ChatGPT, Gemini, Perplexity, Claude e a visão geral com IA do Google em janela nova, sem histórico. Rodar de 3 a 5 vezes por assistente em dias diferentes. Registrar: a Ufape foi citada (sim ou não), qual página, quais concorrentes e portais, quais fontes. Escrever como "citada 2 de 5" com o tamanho da amostra. Começar pelas perguntas de estágio "decisão" e "solução" das áreas A2, A8, A5, A11, A6 e A1. Nenhuma nota de visibilidade existe antes disso.
5. **Fontes de terceiros que a busca mostrou** para as áreas e que viram lista inicial de menções (links-e-autoridade): Quero Bolsa, Guia da Carreira, EAD.com.br, Educa Mais Brasil, Pravaler, blog da Anhanguera, Petlove (dicas), páginas de entidades de área (conferir endereços e regras nas fontes oficiais).

---

## 9. Pendências para o qa-de-marketing e para a Ufape

1. **Datas e dados conflitantes que travam página e anúncio:** 698 (site em 2027), 352, 366, 662 (link trocado), 68662, 68636 (data), 68628, 68617 e 662 (turma), 68641 e 68642 (links invertidos).
2. **Provas sem destino:** 68652, 68649, 68653 e 68655. Prova 68656 fora do ar e bloco "prova de bolsa" da página de 707 sem destino. Não há prova de Ecocardiografia; se a de Cardiologia valer para 698, confirmar.
3. **Regras da prova** com contradições entre fichas (canal do resultado, 10 ou 7 dias, turma mínima de 15 ou 20).
4. **Páginas de nome repetido** (C1): decisão do site sobre página única por curso (SEO-04).
5. **Certificação:** nenhum termo de certificação foi proposto. A página da prova de felinos repete frase de reconhecimento ligada ao MEC: não copiar.
6. **Nome curto da pós de imagem** e nomes fora do padrão do catálogo (Citopatologia, Ultrassonografia, Medicina Interna Equina, IA na Saúde): decidir se o catálogo muda ou se a página usa o padrão.
7. **Termo de marca do concorrente:** decisão humana e do jurídico sobre qualquer uso (seção 5.3, G6).
8. **Público de 719** (veterinários ou saúde humana e TI) antes de qualquer anúncio de busca.
9. **Aprovação** de verba e de grupos de anúncio: pessoa do marketing. Nada foi criado.
10. **Frequência e jornada de 68632** (presencial no catálogo): confirmar antes de qualquer texto sobre rotina.

---

## Lista 1. Fatos com fonte

Dados da Ufape (contexto/catalogo-de-cursos.md, 26/10/2026, seções 2 e 3):
- Código, nome, local, modalidade, início, turma, carga horária e status de cada curso e prova citados; inscrição de R$ 100,00 das 22 provas abertas em 27/11/2026, em 19 especialidades; 68656 encerrado.
- 719 tem o menor total entre as pós abertas (R$ 12.000,00); 68629 tem R$ 16.456,00, o menor da área A5.
- Clínica Cirúrgica de Cães e Gatos tem três páginas no catálogo: 535, 665 e 68632. 68632 é "Presencial" no catálogo.
- Não há prova de bolsa de Ecocardiografia no catálogo.
- Contexto da linha (contexto/pos-graduacao.md): formato semipresencial com 1 módulo por mês; turma mínima de 20; regras da prova de bolsa lidas nas páginas das provas em 26/10/2026; regra de nome "Pós-graduação em <área>".
- Contexto geral (contexto/ufape-geral.md): nome Faculdade UFAPE, CNPJ e sede; "certificado pelo MEC" não é usado.
- Recorte, áreas e ondas: saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md. Pendências P3 a P5 e provas sem destino: mesmo arquivo.
- Lacunas T1 a T10, áreas e perguntas de base: saidas/03-seo-e-busca/lacunas-de-conteudo-pos-2026-10-26.md. Objeções e hipóteses da persona (H-A2.3, H-A10.2): saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md.
- Veredito do qa: saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep03.md.

Dados da busca na web (WebSearch, 26/10/2026, resumo de resultado; páginas não abertas):
- Nenhuma página de curso da Ufape apareceu nas consultas de curso por área. A busca por "Ufape pós-graduação veterinária prova de bolsa" devolveu o edital de aprimoramento em terapia intensiva da Ufape (julho de 2026) e editais de outras instituições.
- Agregadores (Guia da Carreira, Quero Bolsa, EAD.com.br) mostram quase só ofertas EAD de dermatologia e oftalmologia; um agregador lista 996 ofertas de pós em medicina veterinária para Goiânia, de R$ 60,00 a R$ 1.248,21.
- A Anclivepa-SP tem edital de prova de bolsa para ingresso em fevereiro e agosto de 2027, e edital de Cardiologia Veterinária 2026 (inscrições de outubro de 2025 a janeiro de 2026).
- Guias e o CRMV-ES informam que a pós lato sensu gera certificado de conclusão e que o título de especialista é registrado pelo CRMV após aprovação do CFMV; a Resolução CFMV 935/2009 aparece marcada como revogada em manual do CFMV e a norma que a substituiu não foi confirmada.
- A busca por ecocardiografia veterinária não trouxe pós brasileira específica (apareceram cursos no exterior e especialização ampla em cardiologia).
- Currículos públicos citam pós de Neurologia e Neurocirurgia e de Nefrologia pela Ufape (terceiros, sem verificação).
- Sem URL guardada (resumo de busca, conferir na fonte): UFF, USP, UFRRJ, Colégio Brasileiro de Cirurgia Veterinária, ABNV e CBOV, citados em K1.10, K4.13, K9.7, K9.8 e K12.9.

## Lista 2. Suposições

- [SUPOSIÇÃO] Todo "Volume (est.)" (Alto, Médio, Baixo): sinal qualitativo a partir de ofertas em agregadores, matérias de "mais procuradas" e tipo de termo. Não há volume numérico em nenhuma linha.
- [SUPOSIÇÃO] A formulação de cada termo e de cada pergunta de IA vem de títulos de resultados, padrões do roteiro, nomes populares do pedido e da persona; o WebSearch não devolve preenchimento automático nem "As pessoas também perguntam".
- [SUPOSIÇÃO] Pesos D (Alto 20, Médio 14, Baixo 8), faixas de M e F, o teto de 80 e o corte em 32 (regra prática da skill, adaptada).
- [SUPOSIÇÃO] A ausência da Ufape nos resultados do WebSearch indica baixa visibilidade; o WebSearch não é uma página de resultados do Google.
- [SUPOSIÇÃO] Espaço aberto em ecocardiografia, gastroenterologia, hematologia, citopatologia, ortopedia e geriatria; e em "presencial ou semipresencial" para dermatologia, oftalmologia e imagem.
- [SUPOSIÇÃO] Os endereços novos seguem /pos-graduacao/pos-graduacao-em-<área> e a página única por curso (SEO-04) será implementada; o hub da prova e as listagens por praça são proposta.
- [SUPOSIÇÃO] Página nova leva semanas para ranquear; 707, 68604 e 68606 não se beneficiam do conteúdo novo a tempo.
- [SUPOSIÇÃO] Nomes populares ("pós em cardio vet", "especialização em felinos") são usados por candidatos; só entram em lista de palavras-chave e em grupo de anúncio.
- [SUPOSIÇÃO] Tipos de correspondência, palavras negativas e a estrutura de grupos do Google Search (seção 5.3).
- [SUPOSIÇÃO] Público de equinos viaja mais; público de reprodução inclui criadores; público de anestesiologia avançada já é anestesista; "radiologia veterinária" e "análises clínicas veterinárias" atraem o mesmo público das pós de imagem e de patologia clínica.

## Lista 3. Dados que faltam

- Search Console (16 meses), Google Trends e ferramenta de palavras-chave: sem eles não há volume real nem canibalização.
- Sugestões do Google e "As pessoas também perguntam" (seção 8, item 1).
- Rodada manual nos assistentes de IA (seção 8, item 4): sem ela não há taxa de citação.
- [CONFIRMAR NO CATÁLOGO] Datas de 698, 352, 366, 662, 68662 e 68636; turma de 68628, 68617 e 662; link trocado de 662 e 68662; links invertidos de 68641 e 68642.
- [CONFIRMAR NO CATÁLOGO] Destino das provas 68652, 68649, 68653 e 68655; situação de 68656; se a prova de Cardiologia vale para 698; data de encerramento das inscrições da prova; regras da prova (canal do resultado, prazo de matrícula, turma mínima).
- [CONFIRMAR NO CATÁLOGO] Pré-requisitos por turma (657, 359, 698, 352, 699); público de 68616, 68608, 366 e 719; ato regulatório de 719; promoção de 341; ficha de 699; frequência e jornada de 68632.
- [CONFIRMAR NO CATÁLOGO] Se a pós de imagem pode usar nome curto no título; se haverá turma de São Paulo de Anestesiologia e de Clínica Cirúrgica de novo.
- [CONFIRMAR] Página de listagem das pós e página institucional já existentes no site; lista de artigos do blog; URL do hub da prova.
- [CONFIRMAR] Verba e metas por linha (para o gestor-de-midia); data de encerramento das campanhas; decisão sobre termos de marca do concorrente.
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação, regra do EAD lato sensu e leitura da norma vigente do CFMV sobre título de especialista.
- [CONFIRMAR autorização] Docentes e coordenação em qualquer página ou peça.
- [CONFIRMAR] Parceria citada em currículos públicos (Gastroenterologia) e uso desses perfis como prova social.

## Fontes (consultadas em 26/10/2026, por resumo de busca)

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md; .claude/skills/agrupar-palavras-chave/SKILL.md; .claude/skills/briefing-seo/SKILL.md; .claude/skills/visibilidade-em-ia/SKILL.md; saidas/03-seo-e-busca/lacunas-de-conteudo-pos-2026-10-26.md; saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md; saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep03.md.

Externas (resumo de busca; conferir na fonte antes de ir para peça):
- Anestesiologia: [Quero Bolsa, anestesiologia veterinária](https://querobolsa.com.br/cursos-e-faculdades/anestesiologia-veterinaria/bolsas); [UNAR, PPC de pós em anestesiologia 2026](https://www.unar.edu.br/wp-content/uploads/2026/04/PPC%20Pós%20Med%20Vet%20Anestesio%202026.pdf); [blog Anhanguera, anestesiologia veterinária](https://blog.anhanguera.com/anestesiologia-veterinaria/)
- Cardiologia e ecocardiografia: [Anclivepa-SP, edital de Cardiologia 2026](https://portal.anclivepa-sp.org.br/wp-content/uploads/2025/11/Edital-Cardiologia-veterinaria-2026-.pdf); [Petlove, curso de cardiologia veterinária em São Paulo](https://www.petlove.com.br/dicas/curso-de-especializacao-em-cardiologia-veterinaria-sao-paulo-2); [Agrobase, vaga de cardiologista em Ribeirão Preto](https://www.agrobase.com.br/oportunidades/2026/04/medicoa-veterinarioa-especialista-cardiologista-ribeirao-preto-sp/)
- Dermatologia: [Guia da Carreira, pós em dermatologia veterinária](https://www.guiadacarreira.com.br/cursos-e-faculdades/dermatologia-veterinaria/pos-graduacao); [EAD.com.br, pós em dermatologia veterinária](https://www.ead.com.br/cursos-e-faculdades/dermatologia-veterinaria/pos-graduacao); [Quero Bolsa, pós em dermatologia veterinária](https://querobolsa.com.br/cursos-e-faculdades/dermatologia-veterinaria/pos-graduacao)
- Imagem: [Quero Bolsa, pós mais procuradas no Dia do Médico Veterinário](https://querobolsa.com.br/revista/dia-do-medico-veterinario-pos-graduacoes); [Agrobase, vaga de ultrassonografia](https://www.agrobase.com.br/oportunidades/2025/09/medicoa-veterinarioa-especialista-ultrassonografia-sao-jose-dos-campos-sp/)
- Goiânia: [Guia da Carreira, medicina veterinária em Goiânia](https://guiadacarreira.com.br/cursos-e-faculdades/goias--goiania/medicina-veterinaria)
- Prova de bolsa e concorrente: [Anclivepa-SP, edital de prova de bolsa de fevereiro de 2027](https://portal.anclivepa-sp.org.br/wp-content/uploads/2026/08/Edital-Prova-de-bolsa-Fevereiro-de-2027-1.pdf); [Quero Bolsa, 10 pós mais procuradas em medicina veterinária](https://querobolsa.com.br/revista/10-pos-graduacoes-mais-procuradas-em-medicina-veterinaria)
- Título de especialista: [Guia da Carreira, tudo sobre especialização em medicina veterinária](https://www.guiadacarreira.com.br/blog/tudo-sobre-especializacao-em-medicina-veterinaria); [CFMV, Resolução 935 (marcada como revogada no manual)](https://manual.cfmv.gov.br/arquivos/resolucao/935.pdf); [CRMV-ES, informativo](https://www.crmves.org.br/wp-content/uploads/2021/09/CRMV-ES-01-07-2021-a-01-08-2021.pdf)
- EAD x presencial: [Quero Bolsa, pós EAD x presencial](https://querobolsa.com.br/revista/pos-ead-x-presencial-qual-pesa-mais-no-curriculo); [blog Anhanguera, veterinária EAD](https://blog.anhanguera.com/veterinaria-ead/)
- Terapia intensiva e cirurgia: [Uninter, Medicina Veterinária Intensiva](https://www.uninter.com/pos-graduacao/a-distancia/medicina-veterinaria-intensiva-diagnostico-urgencia-e-cuidados-criticos/); [UNIME, pós em clínica médica e cirúrgica](https://www.educamaisbrasil.com.br/unime/noticias/participe-da-pos-em-clinica-medica-e-cirurgica-de-animais-de-companhia); [UNAR, PPC de cirurgia 2026](https://www.unar.edu.br/wp-content/uploads/2026/04/PPC%20Pós%20Med%20Vet%20Cirurgia%202026.pdf)
- Oncologia, felinos, endocrinologia e nefrologia, neurologia e oftalmologia: [Guia da Carreira, oncologia veterinária](https://www.guiadacarreira.com.br/cursos-e-faculdades/oncologia-veterinaria-de-pequenos-animais/cursos); [Quero Bolsa, clínica médica de gatos](https://querobolsa.com.br/cursos-e-faculdades/clinica-medica-de-gatos); [Guia da Carreira, nefrologia e urologia na Universidade Módulo](https://www.guiadacarreira.com.br/faculdades/universidade-modulo/cursos/nefrologia-e-urologia-de-animais-de-companhia); [Quero Bolsa, neurologista veterinário](https://querobolsa.com.br/carreiras-e-profissoes/neurologista-veterinario); [Guia da Carreira, pós em oftalmologia clínica veterinária](https://www.guiadacarreira.com.br/cursos-e-faculdades/oftalmologia-clinica-veterinaria/pos-graduacao)
- Gastroenterologia e laboratório: [blog Anhanguera, gastroenterologia veterinária](https://blog.anhanguera.com/gastroenterologia-veterinaria); [Pravaler, patologia veterinária](https://www.pravaler.com.br/blog/profissoes/patologia-veterinaria/)
- Marca: [edital de aprimoramento em terapia intensiva da Ufape (julho de 2026)](https://faculdade.ufape.com.br/uploads/arquivo/edital-programa-de-aprimoramento-em-terapia-intensiva-veterinaria_julho2026.docx.pdf)

---

## Próximo passo

Próximo agente sugerido: mensagens (etapa 2.2, usa os termos e as perguntas por área) e briefing-de-conteudo (etapa 2.7, usa os briefings da seção 4 e os blocos citáveis). Em paralelo, a pessoa do marketing roda a checagem da seção 8 (sugestões do Google e assistentes de IA). Antes de qualquer peça, o arquivo passa de novo pelo qa-de-marketing com a auditoria 03-busca e com auditorias/conformidade-educacional.md. A aprovação de verba e de grupos de anúncio é da pessoa do marketing.
