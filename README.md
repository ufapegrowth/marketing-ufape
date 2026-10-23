# Squad de Marketing da Ufape

Uma squad de marketing multiagente que roda no Claude Code. São 55 agentes em 11 departamentos, mais skills, workflows, templates, auditorias e receitas. Tudo foi adaptado para a realidade da Ufape: três linhas de produto (Graduação, Pós-graduação e Cursos Livres), WhatsApp como canal principal, mídia paga e conformidade educacional (MEC, CDC, Conar e LGPD).

A base é o material "The Claude Code Marketing Team (2026)". Os arquivos originais, em inglês, estão em `referencia-original/` só para consulta. A forma como cada peça foi adaptada está em `docs/guia-de-adaptacao.md`.

A mídia paga e o planejamento foram reforçados com o kit "7 Skills Meta Ads" e com quatro frameworks de gestão (SWOT, matriz GUT, SIPOC e Balanced Scorecard), adaptados para a Ufape. Skills novas: `metas-de-custo`, `diagnostico-de-midia`, `matriz-gut` e `analise-swot`. A origem de cada uma está no guia de adaptação.

## Como começar

1. Abra esta pasta no Claude Code.
2. Preencha `contexto/ufape-geral.md`, os três contextos de linha e `contexto/catalogo-de-cursos.md`. Sem isso, os agentes vão perguntar ou marcar [SUPOSIÇÃO].
3. Digite `/agents` para confirmar que os agentes carregaram.
4. Dê um objetivo ao Claude Code ou rode um workflow, por exemplo `/pagina-de-curso pos MBA em Gestão de Pessoas`.

## Estrutura

```
CLAUDE.md                      orquestrador
contexto/                      contexto geral, contexto por linha e catálogo de cursos
.claude/agents/                55 agentes
.claude/skills/                27 skills
.claude/commands/              26 workflows
templates/                     11 templates
auditorias/                    11 auditorias de departamento + conformidade educacional
receitas.md                    10 receitas rápidas
conhecimento/                  índice e voz do aluno
saidas/                        entregas, uma pasta por departamento
docs/                          guia de adaptação
referencia-original/           material original, em inglês
```

## Os 11 departamentos

| Nº | Departamento | Agentes |
|---|---|---|
| 01 | Inteligência de Mercado | pesquisa-de-mercado, pesquisa-de-persona, inteligencia-concorrencia, insights-de-alunos, analise-de-tendencias |
| 02 | Estratégia e Posicionamento | estrategia-de-marketing, posicionamento, mensagens, estrategia-de-oferta, estrategia-de-marca |
| 03 | SEO e Busca | pesquisa-de-palavras-chave, lacunas-de-conteudo, seo-on-page, seo-tecnico, links-e-autoridade |
| 04 | Conteúdo | estrategia-de-conteudo, briefing-de-conteudo, conteudo-longo, editor-de-conteudo, reaproveitamento |
| 05 | Social e Comunidade | estrategia-social, posts-sociais, criador-de-ganchos, autoridade-docente, reaproveitamento-social |
| 06 | Geração de Demanda | estrategia-de-campanha, iscas-digitais, distribuicao, campanhas-de-nutricao, crescimento-de-audiencia |
| 07 | E-mail, WhatsApp e Relacionamento | estrategia-de-relacionamento, newsletter, copy-de-mensagens, jornada-do-aluno, otimizacao-de-mensagens |
| 08 | Conversão | landing-page, analise-cro, otimizador-de-cta, analise-de-funil, desenho-de-experimentos |
| 09 | Analytics e Insights | analista-de-dados, analise-de-campanha, desempenho-de-conteudo, relatorios, backlog-de-otimizacao |
| 10 | Operações de Marketing | arquiteto-de-fluxos, integracao-de-sistemas, qa-de-marketing, documentacao, organizacao-de-sistemas |
| 11 | Mídia Paga (novo) | estrategia-de-midia, anuncios-meta, anuncios-google, criativos-de-anuncio, analise-de-midia |

## Workflows

| Workflow | Quando rodar |
|---|---|
| /campanha-de-vestibular | Captação semestral da Graduação |
| /lancamento-de-pos | Curso de Pós novo ou relançado |
| /pagina-de-curso | Página de curso nova ou reescrita |
| /lote-semanal-por-linha | Toda quinta-feira, uma vez por linha |
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
| /semana-de-implantacao | Primeira semana usando a squad |
| /arrumacao-mensal | Última sexta-feira do mês |

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
- Dia 5: `/semana-de-implantacao` para organizar pastas, fluxos e integrações.

## Próximo passo: plataforma de orquestração

Esta pasta é o "cérebro" da squad. A plataforma (painel com entrada de demandas, acompanhamento ao vivo e fila de aprovação) vai executar esses mesmos arquivos pelo Claude Agent SDK, com Supabase como banco e n8n para agendamentos e integrações.
