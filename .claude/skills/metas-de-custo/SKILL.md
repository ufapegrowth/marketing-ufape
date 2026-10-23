---
name: metas-de-custo
description: Calcula quanto a Ufape pode pagar por lead e por matrícula antes de uma campanha subir, com três cenários e o orçamento de teste.
---
# Calcular as metas de custo de uma captação

Propósito: Definir, antes de qualquer verba ser gasta, o custo por lead (CPL) máximo e o custo por matrícula máximo de um curso ou de uma linha. Sem essa meta escrita, nenhuma campanha pode ser chamada de boa ou ruim.

Passos:
1. Colete os dados do curso em contexto/catalogo-de-cursos.md ou no cadastro: valor da mensalidade, número de parcelas, duração do curso, taxa de matrícula e condições (bolsa, desconto). O que não estiver lá vira [CONFIRMAR NO CATÁLOGO].
2. Peça ao time os números do negócio, em uma mensagem só: custo variável por aluno (plataforma, polo, comissão, impostos), margem que a Ufape quer por matrícula, taxa de conversão de lead para matrícula e taxa de evasão da linha. Número que ninguém souber vira [SUPOSIÇÃO], com o valor conservador usado e o motivo.
3. Calcule a receita esperada por matrícula, mostrando a conta:
   - Receita bruta por matrícula = mensalidade x parcelas que o aluno realmente paga (descontando a evasão esperada) + taxa de matrícula, menos bolsas e descontos.
   - Margem de contribuição por matrícula = receita esperada por matrícula menos custos variáveis por aluno.
4. Calcule as metas, sempre com a conta aberta:
   - Custo por matrícula de equilíbrio = margem de contribuição por matrícula.
   - Custo por matrícula máximo = margem de contribuição menos a margem desejada.
   - CPL máximo = custo por matrícula máximo x taxa de conversão lead para matrícula.
   - Custo por conversa no WhatsApp máximo = custo por matrícula máximo x taxa de conversão conversa para matrícula (se a campanha for de mensagem).
   Avise o risco de caixa: a verba sai hoje e a receita entra mês a mês, ao longo do curso.
5. Monte três cenários lado a lado: conservador (conversão e permanência menores), base (números informados) e otimista (conversão e permanência maiores).
6. Defina o orçamento de teste:
   - Por conceito de criativo: algo entre 1,5 e 3 vezes o CPL máximo antes de julgar (regra prática, não meta).
   - Verba semanal dividida pelo CPL máximo dá os leads por semana. Se der volume baixo demais para o algoritmo aprender, recomende menos conjuntos ou otimizar para um evento mais acima no funil.
   - Verba diária sugerida = (leads desejados por semana x CPL máximo) dividido por 7.
7. Se a conta mostrar que a oferta não fecha (CPL máximo baixo demais para a linha), diga isso claramente e aponte as alavancas: melhorar a conversão lead para matrícula, revisar bolsa e desconto, reduzir a evasão, melhorar a página do curso.

Saída: as metas em destaque (custo por matrícula máximo, CPL máximo e, se houver, custo por conversa máximo), a conta passo a passo, a tabela dos três cenários, o orçamento de teste com os leads por semana esperados e uma frase pronta para explicar as metas à diretoria, sem jargão.

Verificações antes de terminar:
- Toda conta está aberta, com os números de origem e a fonte de cada um.
- Valores em reais, com duas casas decimais.
- Nenhuma faixa de referência foi apresentada como meta; regras práticas estão marcadas assim.
- Metas são limites de viabilidade, não previsão de resultado.
- A conta é de uma linha ou de um curso por vez; nada soma Graduação, Pós e Cursos Livres sem mostrar cada linha.
