---
name: visibilidade-em-ia
description: Verifica se a Ufape aparece quando candidatos perguntam a assistentes de IA (ChatGPT, Gemini, Perplexity, Claude e a visão geral com IA do Google) sobre os cursos dela, explica por que não aparece e prioriza as correções. Use antes de escrever ou reescrever páginas de curso e todo mês na saúde de busca.
---
# Visibilidade em respostas de IA

Propósito: fazer a Ufape ser citada e recomendada quando um candidato pergunta a uma IA qual curso fazer, sem inventar resultado de medição.

## Limite do que a squad consegue medir

A squad só tem o Claude e a busca na web. Ela não consegue perguntar ao ChatGPT, ao Gemini nem ao Perplexity. Por isso:
- O agente gera as perguntas, checa o que a busca na web mostra (fontes que aparecem, páginas da Ufape e de concorrentes) e analisa as páginas.
- Toda coluna que depende de rodar a pergunta num assistente fica "conferir manualmente", com o roteiro para a pessoa conferir.
- Resposta de IA varia de uma vez para outra: uma rodada é anedota. A pessoa roda cada pergunta de 3 a 5 vezes por assistente e registra a taxa ("citada 2 de 5").
- Nota geral de visibilidade só aparece se vier dessas checagens reais, com o tamanho da amostra. Sem checagem, não há nota.

## Passos

1. Escreva de 10 a 20 perguntas que um candidato faria a uma IA, do jeito que ele digita, separadas por linha (graduacao, pos ou livres) e por estágio:
   - problema: "vale a pena fazer pós em <área> depois de <situação>?"
   - solução: "qual a melhor pós EAD em <área>?", "faculdade de <curso> com nota do Enem em <cidade>"
   - comparação: "Ufape ou <concorrente> para <curso>?"
   - decisão: "quanto custa a <curso> da Ufape?", "a <curso> da Ufape é reconhecida pelo MEC?"
   Fique só com perguntas que mudam matrícula. Junte variações da mesma intenção numa pergunta principal.
2. Para cada pergunta, registre o que a busca na web mostra: fontes que aparecem, se há página da Ufape e qual, quais concorrentes aparecem. O resto da tabela fica "conferir manualmente".
3. Para cada pergunta em que a Ufape não aparece, diga o motivo provável: não existe página, página fraca, falta prova de terceiros (portais, guias, imprensa), formato errado ou dado inconsistente entre o site e outros perfis.
4. Faça a checagem de extração nas páginas prioritárias:
   - primeira frase responde à pergunta de forma direta
   - blocos de resposta de 40 a 60 palavras que fazem sentido sozinhos
   - tabela de comparação quando a pergunta compara
   - FAQ com perguntas reais de candidatos
   - marcação estruturada (skill schema-de-curso)
   - autor ou coordenador identificado
   - data de atualização visível
   - conteúdo visível sem depender de JavaScript
   - política de robôs de IA no robots.txt coerente com o objetivo (robôs de busca de IA liberados; decisão sobre robôs de treino tomada à parte)
5. Liste as fontes de terceiros que a IA usa para a pergunta e que citam concorrentes e não a Ufape. Elas viram a lista da skill mencoes-e-citacoes.
6. Dê a correção mais rápida por pergunta e o concorrente que vence cada uma.

## Pontuação de oportunidades de SEO e IA

Quando houver mais ideias que tempo, pontue cada ideia (palavra-chave, pergunta ou página) de 0 a 100:
- intenção de matrícula (0 a 30): quanto a pessoa está perto de se inscrever
- demanda (0 a 25): só com dado de ferramenta ou do Search Console fornecido; sem dado, pontue de forma qualitativa e marque [SUPOSIÇÃO]
- facilidade (0 a 25): chance real de a Ufape vencer
- lacuna em IA (0 a 20): a IA cita concorrentes e não a Ufape (só com checagem real)
O valor de uma matrícula vem da skill metas-de-custo (.claude/skills/metas-de-custo/SKILL.md). Escreva uma linha com o motivo de cada nota, ordene da maior para a menor e corte o que ficar abaixo de 40 (regra prática, não meta).

## O que não fazer

- Escrever versões de página "para IA" diferentes da página para pessoas.
- Picotar a página em pedaços pequenos para a IA: use parágrafos e intertítulos normais.
- Inventar citação, prêmio, avaliação, ranking ou nota do MEC.
- Esconder o conteúdo principal atrás de formulário ou de JavaScript.

Saída: tabela pergunta, linha, estágio, o que a busca mostrou, Ufape aparece (busca: sim ou não; assistentes: conferir manualmente ou taxa medida), motivo, concorrente que vence, correção mais rápida; checagem de extração por página; lista de fontes para mencoes-e-citacoes; roteiro de checagem manual; e, se pedida, a pontuação de oportunidades.

Verificações antes de terminar:
- Nenhum resultado de assistente de IA foi preenchido sem checagem real
- Toda nota de visibilidade mostra o tamanho da amostra
- As perguntas estão separadas por linha de negócio
- Dados de curso conferidos em contexto/catalogo-de-cursos.md ou marcados com [CONFIRMAR NO CATÁLOGO]
