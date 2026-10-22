---
description: Toda segunda-feira, para revisar a mídia paga da semana anterior. Cadeia: analise-de-midia -> criativos-de-anuncio -> estrategia-de-midia
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Revisão semanal de mídia".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente analise-de-midia para produzir a revisão de mídia a partir das exportações da Meta, do Google e do CRM. Salve e passe o arquivo para a próxima etapa.
2. Use o agente criativos-de-anuncio para produzir as variações que substituem os criativos cansados. Salve e passe o arquivo para a próxima etapa.
3. Use o agente estrategia-de-midia para produzir o ajuste do plano e da divisão de verba, dentro da verba aprovada. Salve e passe o arquivo para a próxima etapa.
4. Rode auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: lista escalar, ajustar ou pausar aprovada e entregue para um humano executar, com criativos novos prontos para os cansados.
