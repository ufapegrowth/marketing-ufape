---
description: Rode na primeira segunda-feira do mês. Cadeia: analise-de-tendencias -> inteligencia-concorrencia -> insights-de-alunos -> estrategia-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Pulso mensal de mercado".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente analise-de-tendencias para produzir o radar de tendências. Salve e passe o arquivo para a próxima etapa.
2. Use o agente inteligencia-concorrencia para produzir o que mudou nos concorrentes (cursos, preços, bolsas, campanhas). Salve e passe o arquivo para a próxima etapa.
3. Use o agente insights-de-alunos para produzir os novos temas de feedback de candidatos e alunos. Salve e passe o arquivo para a próxima etapa.
4. Use o agente estrategia-de-marketing para produzir os ajustes no plano de captação. Salve e passe o arquivo para a próxima etapa.
5. Rode as auditorias dos departamentos (auditorias/01-qualidade-de-pesquisa.md e auditorias/02-estrategia-e-posicionamento.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: uma nota de pulso de uma página com 3 ajustes.
