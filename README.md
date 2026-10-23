# Squad de Marketing da Ufape

Uma squad de marketing multiagente que roda no Claude Code. São 60 agentes em 12 departamentos, comandados pelo agente cmo, mais skills, workflows, templates, auditorias e receitas. Tudo foi adaptado para a realidade da Ufape: quatro linhas de produto (Graduação, Pós-graduação, Cursos Livres e Eventos), WhatsApp como canal principal, mídia paga e conformidade educacional (MEC, CDC, Conar e LGPD).

A base é o material "The Claude Code Marketing Team (2026)". Os arquivos originais, em inglês, estão em `referencia-original/` só para consulta. A forma como cada peça foi adaptada está em `docs/guia-de-adaptacao.md`.

A mídia paga e o planejamento foram reforçados com o kit "7 Skills Meta Ads" e com quatro frameworks de gestão (SWOT, matriz GUT, SIPOC e Balanced Scorecard), adaptados para a Ufape. Skills novas: `metas-de-custo`, `diagnostico-de-midia`, `matriz-gut` e `analise-swot`. A origem de cada uma está no guia de adaptação.

O departamento 03 virou "SEO e Busca por IA", com cinco skills novas (`visibilidade-em-ia`, `leitura-do-search-console`, `canibalizacao`, `schema-de-curso` e `mencoes-e-citacoes`), adaptadas de um pacote de 16 skills de SEO e da skill `ai-seo` de Corey Haines (MIT). O departamento 12, Vídeo e Áudio, traz os agentes `tiktok`, `youtube`, `podcast` e `x`. O departamento 10 ficou enxuto: saíram `organizacao-de-sistemas`, `documentacao` e `integracao-de-sistemas`, e o workflow `/semana-de-implantacao`.

A mídia paga virou uma squad de ads completa: o `gestor-de-midia` chefia o departamento 11, decide a divisão de verba entre Meta, Google e YouTube, TikTok e LinkedIn, roda a revisão semanal e reporta ao CMO. Entraram também `anuncios-tiktok` e `anuncios-linkedin` (foco em Pós) e o workflow `/plano-de-midia-da-turma`.

Canais: toda estratégia avalia os 8 canais (Instagram, Facebook, TikTok, X, LinkedIn, YouTube, podcast e WhatsApp) e ativa os que a capacidade de produção sustenta com qualidade, justificando os que ficam de fora.

## Como começar

1. Abra esta pasta no Claude Code.
2. Preencha `contexto/ufape-geral.md`, os três contextos de linha e `contexto/catalogo-de-cursos.md`. Sem isso, os agentes vão perguntar ou marcar [SUPOSIÇÃO].
3. Digite `/agents` para confirmar que os agentes carregaram.
4. Dê um objetivo ao Claude Code ou rode um workflow, por exemplo `/pagina-de-curso pos MBA em Gestão de Pessoas`.

## Estrutura

```
CLAUDE.md                      orquestrador
contexto/                      contexto geral, contexto por linha e catálogo de cursos
.claude/agents/                60 agentes
.claude/skills/                32 skills
.claude/commands/              28 workflows
templates/                     16 templates (inclui 4 kits de lançamento e a página da turma)
auditorias/                    12 auditorias de departamento + conformidade educacional
receitas.md                    10 receitas rápidas
conhecimento/                  índice e voz do aluno
saidas/                        entregas, uma pasta por departamento
docs/                          guia de adaptação
referencia-original/           material original, em inglês
```

## Comando e os 12 departamentos

| Nº | Departamento | Agentes |
|---|---|---|
| - | Comando | cmo (recebe a liberação, planeja os 8 canais, prioriza, distribui e revisa; o gestor-de-midia reporta a ele) |
| 01 | Inteligência de Mercado | pesquisa-de-mercado, pesquisa-de-persona, inteligencia-concorrencia, insights-de-alunos, analise-de-tendencias |
| 02 | Estratégia e Posicionamento | estrategia-de-marketing, posicionamento, mensagens, estrategia-de-oferta, estrategia-de-marca |
| 03 | SEO e Busca por IA | pesquisa-de-palavras-chave, lacunas-de-conteudo, seo-on-page, seo-tecnico, links-e-autoridade |
| 04 | Conteúdo | estrategia-de-conteudo, briefing-de-conteudo, conteudo-longo, editor-de-conteudo, reaproveitamento |
| 05 | Social e Comunidade | estrategia-social, posts-sociais, criador-de-ganchos, autoridade-docente, reaproveitamento-social |
| 06 | Geração de Demanda | estrategia-de-campanha, iscas-digitais, distribuicao, campanhas-de-nutricao, crescimento-de-audiencia |
| 07 | E-mail, WhatsApp e Relacionamento | estrategia-de-relacionamento, newsletter, copy-de-mensagens, jornada-do-aluno, otimizacao-de-mensagens |
| 08 | Conversão | landing-page, analise-cro, otimizador-de-cta, analise-de-funil, desenho-de-experimentos |
| 09 | Analytics e Insights | analista-de-dados, analise-de-campanha, desempenho-de-conteudo, relatorios, backlog-de-otimizacao |
| 10 | Operações de Marketing | arquiteto-de-fluxos, qa-de-marketing |
| 11 | Mídia Paga | gestor-de-midia, estrategia-de-midia, criativos-de-anuncio, anuncios-meta, anuncios-google, anuncios-tiktok, anuncios-linkedin, analise-de-midia |
| 12 | Vídeo e Áudio (novo) | tiktok, youtube, podcast, x |

## Workflows

| Workflow | Quando rodar |
|---|---|
| /campanha-de-vestibular | Edital e curso da Graduação liberados para o marketing (começa pelo cmo) |
| /lancamento-de-pos | Turma de Pós liberada (começa pelo cmo) |
| /lancamento-de-turma-livre | Turma de Curso Livre liberada (começa pelo cmo) |
| /lancamento-de-evento | Edição de workshop ou simpósio liberada (começa pelo cmo) |
| /pagina-de-curso | Página da turma ou edição no formato de templates/pagina-da-turma.md |
| /lote-semanal-por-linha | Toda quinta-feira, uma vez por linha |
| /plano-de-midia-da-turma | Turma liberada para o marketing com verba de mídia |
| /campanha-de-midia-paga | Nova campanha com verba aprovada |
| /revisao-semanal-de-midia | Toda segunda-feira |
| /mercado-a-persona | Curso novo ou mercado novo |
| /pulso-mensal-de-mercado | Primeira segunda-feira do mês |
| /reset-de-posicionamento | Mensagem genérica ou queda de conversão |
| /plano-trimestral | Duas semanas antes do trimestre |
| /nova-pagina-de-busca | Palavra-chave prioritária sem página |
| /saude-de-busca | Mensal |
| /ideia-a-artigo-publicado | Tema aprovado no calendário |
| /atualizacao-de-conteudo | Mensal |
| /lote-semanal-social | Toda sexta-feira |
| /conteudo-longo-para-social | Artigo, vídeo ou webinar novo |
| /lancamento-de-isca-digital | Isca digital aprovada |
| /sprint-de-campanha | Data de lançamento ou promoção |
| /newsletter-semanal | Toda terça-feira |
| /nova-regua-de-relacionamento | Etapa da jornada sem régua |
| /sprint-de-conversao | Página importante abaixo da meta |
| /oferta-para-pagina | Oferta nova ou reformulada |
| /ciclo-mensal-de-relatorios | Último dia útil do mês |
| /revisao-pos-campanha | Fim ou checkpoint de campanha |
| /arrumacao-mensal | Última sexta-feira do mês (checagem de qualidade e correção dos workflows) |

## Regras de ouro

1. **O Claude rascunha, um humano decide.** Nada é publicado, enviado ou pago sem aprovação.
2. **Nada inventado.** Dados de curso só vêm do catálogo; números e provas precisam de fonte.
3. **Conformidade sempre.** Toda peça passa por `auditorias/conformidade-educacional.md`.
4. **Dados protegidos.** Nada de dados pessoais de alunos nas saídas, nem chaves de API em arquivos.
5. **Escrita humana.** Português simples, com a voz da Ufape.

## Primeira semana sugerida

- Dia 1: preencher os contextos e o catálogo; rodar `/mercado-a-persona` para a linha prioritária.
- Dia 2: `/reset-de-posicionamento` para ter a casa de mensagens.
- Dia 3: `/plano-trimestral` e aprovar o plano de 90 dias.
- Dia 4: `/lote-semanal-por-linha` e `/pagina-de-curso` para um curso prioritário.
- Dia 5: `/saude-de-busca` para ver a busca no Google e nas respostas de IA.

## Próximo passo: plataforma de orquestração

Esta pasta é o "cérebro" da squad. A plataforma (painel com entrada de demandas, acompanhamento ao vivo e fila de aprovação) vai executar esses mesmos arquivos pelo Claude Agent SDK, com Supabase como banco e n8n para agendamentos e integrações.
