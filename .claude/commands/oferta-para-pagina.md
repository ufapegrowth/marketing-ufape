---
description: Rode quando houver uma oferta de curso nova ou reformulada. Cadeia: estrategia-de-oferta -> landing-page -> otimizador-de-cta -> qa-de-marketing
argument-hint: [linha] [curso ou tema]
---
Execute o workflow "Oferta para página".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha e curso deste pedido: $ARGUMENTS

1. Use o agente estrategia-de-oferta para produzir a ficha da oferta. Salve e passe o arquivo para a próxima etapa.
2. Use o agente landing-page para produzir o texto da página. Salve e passe o arquivo para a próxima etapa.
3. Use o agente otimizador-de-cta para produzir os CTAs. Salve e passe o arquivo para a próxima etapa.
4. Use o agente qa-de-marketing para produzir a revisão de qualidade. Salve e passe o arquivo para a próxima etapa.
5. Rode auditorias/08-conversao.md e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: texto da página aprovado para construção.
