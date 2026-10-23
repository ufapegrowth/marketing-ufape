# Guia de adaptação da squad para a Ufape

Este guia define como os arquivos de `referencia-original/` (material "The Claude Code Marketing Team 2026", em inglês) foram convertidos para a squad da Ufape. Use-o sempre que criar ou alterar um agente, skill, workflow, template ou auditoria.

## Regras de escrita (valem para todo arquivo)

1. Português do Brasil, linguagem simples e direta.
2. Nunca usar travessão (nem o longo nem o médio) como pontuação. Use vírgula, dois-pontos, parênteses ou ponto.
3. "ICP" vira "persona" (perfil de aluno ideal). "Customer" vira "aluno" ou "candidato" (antes da matrícula). "Offer" vira "oferta" ou "curso". "Lead magnet" vira "isca digital". "Sales" vira "comercial" ou "time de captação".
4. Nada de exemplos B2B de software. Os exemplos devem falar de cursos, candidatos, matrícula, captação, vestibular, rematrícula.
5. Mantenha a estrutura de cada arquivo original (mesmas seções, mesma ordem, mesmo número de passos). Adapte o conteúdo, não a forma.

## A Ufape em uma frase

A Ufape vende três linhas de produto, cada uma com público, ciclo de venda e ticket diferentes:

| Linha | Público típico | Ciclo | Arquivo de contexto |
|---|---|---|---|
| Graduação | Jovens saindo do ensino médio e adultos voltando a estudar | Captação semestral (vestibular) | `contexto/graduacao.md` |
| Pós-graduação | Profissionais formados buscando especialização ou MBA | Captação contínua, turmas abertas | `contexto/pos-graduacao.md` |
| Cursos Livres | Quem quer uma habilidade rápida, sem diploma | Compra rápida, alto volume | `contexto/cursos-livres.md` |

Todo agente trabalha para **uma linha por vez**. Se o pedido não disser a linha, o agente pergunta.

## Modelo de arquivo de agente

```
---
name: <slug-pt>
description: <o que faz>. Use quando <situação>.
tools: <mesmas ferramentas do original>
model: <sonnet | opus>
---
Você é o agente <slug-pt> da squad de marketing da Ufape (departamento <Nome do Departamento>).

Antes de qualquer coisa, leia contexto/ufape-geral.md e o contexto da linha de negócio do pedido (contexto/graduacao.md, contexto/pos-graduacao.md ou contexto/cursos-livres.md). Se o pedido não disser a linha, ou se faltar algo que você precisa, pergunte antes de começar.

Sua função: <função>.

Entradas: <entradas>.

Método:
1. ...
2. ...
3. ...
4. ...

Saída: <descrição da saída>. Salve em Markdown em saidas/<pasta-do-departamento>/ com o nome <slug-pt>-<linha>-AAAA-MM-DD.md (linha: graduacao, pos ou livres).

Regras:
- <regra específica do original, traduzida e adaptada>
- <regra específica da Ufape, quando fizer sentido>
- Dados de curso (nome, modalidade, carga horária, duração, preço, condições, atos regulatórios) só podem vir de contexto/catalogo-de-cursos.md. Se não estiver lá, escreva [CONFIRMAR NO CATÁLOGO].
- Marque toda suposição com [SUPOSIÇÃO] e liste as fontes no final.
- Apenas rascunho. Nada é publicado, enviado ou pago sem aprovação humana.

Ao terminar, informe o caminho do arquivo e sugira o próximo agente: <slug-pt do próximo>.
```

Escolha de modelo: `opus` para agentes de estratégia, posicionamento, análise e QA (estrategia-de-marketing, posicionamento, mensagens, estrategia-de-oferta, estrategia-de-marca, estrategia-de-campanha, estrategia-de-midia, analista-de-dados, backlog-de-otimizacao, qa-de-marketing). `sonnet` para todos os outros.

## Modelo de skill

```
---
name: <slug-pt>
description: <propósito>
---
# <Título em PT>

Propósito: <propósito>

Passos:
1. ...

Saída: <saída>

Verificações antes de terminar:
- ...
```

## Modelo de workflow (comando)

```
Execute o workflow "<Nome em PT>".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente <slug> para produzir <saída>. Salve e passe o arquivo para a próxima etapa.
...
N. Rode a auditoria do departamento e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: <critério>.
```

O comando começa com um bloco de frontmatter:

```
---
description: <quando rodar>. Cadeia: <slug> -> <slug> -> ...
argument-hint: [linha] [curso ou tema]
---
```

## Pastas de saída por departamento

| Nº | Departamento | Pasta |
|---|---|---|
| 01 | Inteligência de Mercado | saidas/01-inteligencia-de-mercado/ |
| 02 | Estratégia e Posicionamento | saidas/02-estrategia-e-posicionamento/ |
| 03 | SEO e Busca | saidas/03-seo-e-busca/ |
| 04 | Conteúdo | saidas/04-conteudo/ |
| 05 | Social e Comunidade | saidas/05-social-e-comunidade/ |
| 06 | Geração de Demanda | saidas/06-geracao-de-demanda/ |
| 07 | E-mail, WhatsApp e Relacionamento | saidas/07-email-whatsapp-relacionamento/ |
| 08 | Conversão | saidas/08-conversao/ |
| 09 | Analytics e Insights | saidas/09-analytics-e-insights/ |
| 10 | Operações de Marketing | saidas/10-operacoes-de-marketing/ |
| 11 | Mídia Paga (novo, não existe no original) | saidas/11-midia-paga/ |

## Mapa de nomes (original -> Ufape)

### Agentes

| Dep. | Original | Ufape |
|---|---|---|
| 01 | market-research | pesquisa-de-mercado |
| 01 | icp-research | pesquisa-de-persona |
| 01 | competitor-intel | inteligencia-concorrencia |
| 01 | customer-insights | insights-de-alunos |
| 01 | trend-analysis | analise-de-tendencias |
| 02 | marketing-strategy | estrategia-de-marketing |
| 02 | positioning | posicionamento |
| 02 | messaging | mensagens |
| 02 | offer-strategy | estrategia-de-oferta |
| 02 | brand-strategy | estrategia-de-marca |
| 03 | keyword-research | pesquisa-de-palavras-chave |
| 03 | content-gap | lacunas-de-conteudo |
| 03 | onpage-seo | seo-on-page |
| 03 | technical-seo | seo-tecnico |
| 03 | link-building | links-e-autoridade |
| 04 | content-strategy | estrategia-de-conteudo |
| 04 | content-brief | briefing-de-conteudo |
| 04 | longform-content | conteudo-longo |
| 04 | content-editor | editor-de-conteudo |
| 04 | repurposing | reaproveitamento |
| 05 | social-strategy | estrategia-social |
| 05 | social-posts | posts-sociais |
| 05 | hook-creator | criador-de-ganchos |
| 05 | thought-leadership | autoridade-docente |
| 05 | social-repurposing | reaproveitamento-social |
| 06 | campaign-strategy | estrategia-de-campanha |
| 06 | lead-magnets | iscas-digitais |
| 06 | distribution | distribuicao |
| 06 | nurture-campaigns | campanhas-de-nutricao |
| 06 | audience-growth | crescimento-de-audiencia |
| 07 | email-strategy | estrategia-de-relacionamento |
| 07 | newsletter | newsletter |
| 07 | email-copy | copy-de-mensagens |
| 07 | lifecycle | jornada-do-aluno |
| 07 | email-optimisation | otimizacao-de-mensagens |
| 08 | landing-page | landing-page |
| 08 | cro-analysis | analise-cro |
| 08 | cta-optimiser | otimizador-de-cta |
| 08 | funnel-analysis | analise-de-funil |
| 08 | experiment-design | desenho-de-experimentos |
| 09 | data-analyst | analista-de-dados |
| 09 | campaign-analysis | analise-de-campanha |
| 09 | content-performance | desempenho-de-conteudo |
| 09 | reporting | relatorios |
| 09 | analysis-optimisation | backlog-de-otimizacao |
| 10 | workflow-architect | arquiteto-de-fluxos |
| 10 | systems-integration | integracao-de-sistemas (removido em outubro de 2026) |
| 10 | marketing-qa | qa-de-marketing |
| 10 | documentation | documentacao (removido em outubro de 2026) |
| 10 | marketing-systems | organizacao-de-sistemas (removido em outubro de 2026) |
| 11 | (novo) | estrategia-de-midia |
| 11 | (novo) | anuncios-meta |
| 11 | (novo) | anuncios-google |
| 11 | (novo) | criativos-de-anuncio |
| 11 | (novo) | analise-de-midia |

### Skills

| Original | Ufape |
|---|---|
| market-sizing | dimensionar-mercado |
| voice-of-customer | voz-do-aluno |
| positioning-canvas | canvas-de-posicionamento |
| ninety-day-plan | plano-de-90-dias |
| keyword-clustering | agrupar-palavras-chave |
| seo-page-brief | briefing-seo |
| content-calendar | calendario-de-conteudo |
| edit-pass | edicao-em-tres-passadas |
| hook-writing | ganchos-verdadeiros |
| post-formatting | formatar-post |
| lead-magnet-outline | estruturar-isca-digital |
| campaign-brief | briefing-de-campanha |
| subject-lines | assuntos-de-email |
| sequence-mapping | mapear-regua |
| page-teardown | raio-x-de-pagina |
| test-hypothesis | hipotese-de-teste |
| metric-tree | arvore-de-metricas (com o Balanced Scorecard, ver abaixo) |
| insight-memo | memorando-de-insight |
| workflow-mapping | mapear-fluxo |
| knowledge-index | indice-de-conhecimento |
| (novo) | conformidade-educacional |
| (novo) | estrutura-de-campanha-paga |
| (novo) | matriz-de-criativos |

### Workflows (comandos)

| Original | Ufape |
|---|---|
| market-to-icp-in-one-afternoon | mercado-a-persona |
| monthly-market-pulse | pulso-mensal-de-mercado |
| positioning-reset | reset-de-posicionamento |
| quarterly-plan | plano-trimestral |
| new-search-page | nova-pagina-de-busca |
| search-health-check | saude-de-busca |
| idea-to-published-article | ideia-a-artigo-publicado |
| content-refresh | atualizacao-de-conteudo |
| weekly-social-batch | lote-semanal-social |
| long-piece-to-social | conteudo-longo-para-social |
| lead-magnet-launch | lancamento-de-isca-digital |
| campaign-sprint | sprint-de-campanha |
| weekly-newsletter | newsletter-semanal |
| new-lifecycle-sequence | nova-regua-de-relacionamento |
| page-conversion-sprint | sprint-de-conversao |
| offer-to-page | oferta-para-pagina |
| monthly-reporting-cycle | ciclo-mensal-de-relatorios |
| post-campaign-review | revisao-pos-campanha |
| department-setup-week | semana-de-implantacao (removido em outubro de 2026) |
| monthly-ops-tidy | arrumacao-mensal |
| (novo) | campanha-de-midia-paga |
| (novo) | revisao-semanal-de-midia |
| (novo, Ufape) | campanha-de-vestibular |
| (novo, Ufape) | lancamento-de-pos |
| (novo, Ufape) | pagina-de-curso |
| (novo, Ufape) | lote-semanal-por-linha |

### Templates e auditorias

| Original | Ufape |
|---|---|
| templates/icp-profile.md | templates/persona.md |
| templates/messaging-house.md | templates/casa-de-mensagens.md |
| templates/seo-page-brief.md | templates/briefing-seo.md |
| templates/content-brief.md | templates/briefing-de-conteudo.md |
| templates/social-post.md | templates/post-social.md |
| templates/campaign-brief.md | templates/briefing-de-campanha.md |
| templates/email.md | templates/mensagem.md (e-mail ou WhatsApp) |
| templates/landing-page.md | templates/landing-page.md |
| templates/monthly-marketing-report.md | templates/relatorio-mensal.md |
| templates/workflow-doc.md | templates/documento-de-fluxo.md |
| (novo) | templates/briefing-de-midia.md |
| audits/research-quality-audit.md | auditorias/01-qualidade-de-pesquisa.md |
| audits/strategy-and-positioning-audit.md | auditorias/02-estrategia-e-posicionamento.md |
| audits/search-audit.md | auditorias/03-busca.md |
| audits/content-quality-audit.md | auditorias/04-qualidade-de-conteudo.md |
| audits/social-audit.md | auditorias/05-social.md |
| audits/demand-generation-audit.md | auditorias/06-geracao-de-demanda.md |
| audits/email-audit.md | auditorias/07-email-e-whatsapp.md |
| audits/conversion-audit.md | auditorias/08-conversao.md |
| audits/analytics-audit.md | auditorias/09-analytics.md |
| audits/marketing-ops-audit.md | auditorias/10-operacoes.md |
| (novo) | auditorias/11-midia-paga.md |
| (novo, Ufape) | auditorias/conformidade-educacional.md |

## Adaptações específicas por departamento

- **01 Inteligência de Mercado:** concorrentes são outras instituições de ensino (presenciais e EAD). `insights-de-alunos` usa conversas de atendimento (WhatsApp, Chatwoot), avaliações do Google e Reclame Aqui, pesquisas com alunos e anotações do time de captação. Remover nomes, telefones, CPF e e-mails antes de analisar.
- **02 Estratégia e Posicionamento:** a "alternativa real" inclui não estudar agora, estudar em outra instituição, EAD barato e cursos gratuitos. `estrategia-de-oferta` trabalha com bolsas, descontos, condições de pagamento e bônus, sempre dentro das regras de conformidade (sem garantia de emprego ou salário).
- **03 SEO e Busca por IA:** páginas de curso são as páginas de dinheiro. Palavras-chave típicas: "<curso> EAD", "pós em <área>", "faculdade de <curso> em <cidade>", "curso de <tema> com certificado".
- **04 Conteúdo:** blog, guias de carreira e conteúdo de apoio à decisão (como escolher uma pós, diferença entre MBA e especialização, quanto tempo dura o curso). Professores e coordenadores são fonte de autoridade.
- **05 Social e Comunidade:** canais prioritários Instagram, TikTok, YouTube Shorts e LinkedIn (este principalmente para Pós). `autoridade-docente` entrevista coordenadores e professores, não um fundador.
- **06 Geração de Demanda:** iscas digitais típicas: teste vocacional, simulado do vestibular, aula experimental, e-book de carreira, webinar com coordenador. Nutrição pode ser por e-mail e por WhatsApp.
- **07 E-mail, WhatsApp e Relacionamento:** o original só fala de e-mail. Na Ufape, WhatsApp é o canal principal de captação e relacionamento. Todo agente deste departamento cobre os dois canais e respeita opt-in, horário comercial e frequência humana no WhatsApp. `jornada-do-aluno` cobre: lead, inscrito, matriculado, calouro, aluno ativo, rematrícula, evasão e ex-aluno (para nova venda, como pós após a graduação).
- **08 Conversão:** foco em landing pages de curso e formulários de inscrição. O funil típico é: visita, lead, contato do time de captação, inscrição, matrícula, pagamento da primeira mensalidade.
- **09 Analytics e Insights:** métricas de negócio são custo por lead, custo por matrícula, taxa de conversão lead para matrícula e receita por linha. Dados vêm de GA4, Meta Ads, Google Ads, CRM e Chatwoot.
- **10 Operações de Marketing:** `qa-de-marketing` sempre roda também `auditorias/conformidade-educacional.md`. `arquiteto-de-fluxos` desenha os workflows que a plataforma roda (formato de `.claude/commands`).
- **11 Mídia Paga (novo):** cobre Meta Ads e Google Ads (Search, Performance Max e YouTube), estrutura de campanha por linha e por curso, públicos, criativos e leitura de resultados. Nunca sobe, altera ou pausa campanha: entrega plano e arquivos para um humano executar.

## Reforço de mídia paga e planejamento (outubro de 2026)

Duas fontes externas foram adaptadas para a Ufape, seguindo as mesmas regras de escrita deste guia. Os textos originais não foram copiados para o repositório; ficou só a versão adaptada.

### Kit "7 Skills Meta Ads" (material para gestores de tráfego)

| Skill do kit | Onde entrou na squad | Adaptação |
|---|---|---|
| Calculadora de Metas | skill nova metas-de-custo; usada por estrategia-de-midia e analise-de-midia | "Venda" virou matrícula; a receita vem de mensalidade, parcelas pagas, evasão, taxa de matrícula, bolsas e descontos |
| Diagnóstico de Campanha | skill nova diagnostico-de-midia; usada por analise-de-midia | Funil estendido até a matrícula no CRM; sintoma novo "lead barato e matrícula cara" |
| Estrategista de Criativos | skill matriz-de-criativos (reescrita) | As 5 dimensões de diversidade com personas da Ufape; "uma variável por vez" ficou só para iterações de um vencedor |
| Arquiteto de Estrutura | skill estrutura-de-campanha-paga (reforçada) | Modelos enxuta, teste e escala, lançamento por fases (vestibular e turma de Pós) e local; nomenclatura da Ufape mantida |
| Copy de Anúncio | agente anuncios-meta (reforçado) | Anatomia do anúncio, estruturas de texto e entregável padrão |
| Auditor de Políticas | skill conformidade-educacional e auditorias/conformidade-educacional.md (bloco de anúncios) | Junto da auditoria de MEC, CDC, Conar e LGPD, sem criar outra auditoria |
| Relatório para Cliente | agente relatorios (reforçado) | O leitor é a diretoria da Ufape; versão curta para WhatsApp e roteiro de reunião |

As faixas numéricas do kit (por exemplo, gastar de 1,5 a 2 vezes o CPL máximo antes de pausar) entraram como "regra prática, não meta". Os emojis de risco do kit foram retirados.

### Frameworks de gestão (SWOT, GUT, SIPOC e Balanced Scorecard)

| Framework | Onde entrou | Quem usa |
|---|---|---|
| SWOT | skill nova analise-swot | pesquisa-de-mercado, inteligencia-concorrencia, posicionamento |
| Matriz GUT | skill nova matriz-gut | backlog-de-otimizacao, workflows plano-trimestral e revisao-pos-campanha |
| SIPOC | skill mapear-fluxo (reforçada) | arquiteto-de-fluxos |
| Balanced Scorecard | skill arvore-de-metricas (reforçada) | estrategia-de-marketing, workflow plano-trimestral |

As notas da matriz GUT e os itens da SWOT são avaliação do agente, não medida, e precisam citar a fonte de cada dado.

## Onda 2, primeiro bloco: SEO e Busca por IA, canais e Vídeo e Áudio (outubro de 2026)

Decisões do CEO de 23/10/2026 (P9 a P12). Os textos originais não foram copiados; ficou só a versão adaptada.

### SEO e Busca por IA

Fontes: pacote de 16 skills de SEO enviado pelo CEO e a skill `ai-seo` de coreyhaines31/marketingskills (licença MIT).

| Skill de origem | Onde entrou na squad |
|---|---|
| ai-visibility-audit e ai-seo | skill nova visibilidade-em-ia. A squad só tem o Claude e a busca na web: resultado de assistente de IA fica "conferir manualmente" e nota só com checagem real |
| opportunity-scoring | seção "Pontuação de oportunidades" da visibilidade-em-ia; valor da matrícula vem da metas-de-custo; corte abaixo de 40 é regra prática |
| keyword-prompt-research | agente pesquisa-de-palavras-chave passa a listar perguntas feitas a assistentes de IA |
| brief-writer | skill briefing-seo e templates/briefing-seo.md: bloco de resposta citável, entidades, FAQ e prova |
| entity-schema | skill nova schema-de-curso (Course, EducationalOrganization, Person, FAQPage, Article); o código é aplicado no ufape-site |
| gsc-analyst | skill nova leitura-do-search-console, só com exportação colada |
| cannibalization-check | skill nova canibalizacao |
| citation-gap-hunter e mention-outreach | skill nova mencoes-e-citacoes, usada por links-e-autoridade; todo contato espera aprovação |
| topical-map | skill agrupar-palavras-chave (mapa por área) e agente lacunas-de-conteudo |
| internal-linking | agente links-e-autoridade |
| technical-audit | agente seo-tecnico (conteúdo sem JavaScript, robôs de IA, ordem por dano) |
| content-refresh | workflow atualizacao-de-conteudo |
| weekly-report, rank-citation-tracker | não trazidas (relatorios já cobre; rastreio sem fonte de dados inventaria resultado) |

### Canais

As regras "no máximo 3 canais" e "1 ou 2 plataformas" saíram de estrategia-de-marketing, plano-de-90-dias, estrategia-social e da auditoria 02. Agora todo plano avalia os 8 canais e ativa por prioridade e capacidade, justificando os de fora.

### Departamento 10 enxuto

Saíram organizacao-de-sistemas, documentacao e integracao-de-sistemas: dentro da plataforma, pastas e documentos ficam no pedido e integrações são projeto do admin. arquiteto-de-fluxos passou a desenhar os workflows da plataforma. Workflows ajustados: arrumacao-mensal (qa-de-marketing e arquiteto-de-fluxos), revisao-pos-campanha (aprendizados com relatorios), nova-regua-de-relacionamento (gatilhos listados pela jornada-do-aluno). semana-de-implantacao foi removido.

### Departamento 12, Vídeo e Áudio

Agentes novos tiktok, youtube, podcast e x, mais auditorias/12-video-e-audio.md e saidas/12-video-e-audio/. Fontes de método: reels-scripting, hook-generator e youtube-thumbnail de charlie947/social-media-skills (MIT) e social e video de coreyhaines31/marketingskills (MIT). Nada de ferramenta externa (Apify, Gemini) foi trazido: os agentes só planejam e roteirizam.
