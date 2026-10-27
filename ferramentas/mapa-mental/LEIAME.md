# Gerador do mapa mental e dos JSON por curso

Gera, a partir de contexto/catalogo-de-cursos.md e das saídas aprovadas, um JSON por item no esquema versão 1 (saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md) e o mapa mental HTML que abre offline.

Como rodar, a partir da raiz do repositório:

    python3 -I ferramentas/mapa-mental/mapa_json.py --write
    python3 -I ferramentas/mapa-mental/mapa_html.py

Saídas: saidas/10-operacoes-de-marketing/cursos/*.json e saidas/02-estrategia-e-posicionamento/cmo-geral-AAAA-MM-DD.html (mude HOJE e o nome do arquivo no script a cada onda). A pasta saida/ guarda só o arquivo intermediário e a versão da página para publicação.

Regras: nenhum número é inventado; dado ausente vira "[CONFIRMAR]" ou null com pendência. Nada vai para o banco: é só arquivo.

De onde vem cada coisa (versão de 27/10/2026, com as correções B1 a B14 da revisão saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-mapa.md):

- Lidas das tabelas, a cada rodada: P3 a P17 (plano geral, seção 7); 2.1 itens 2, 3, 5 e 7 e a tabela 2.4 (recorte, turmas iniciadas com campanha ativa, grupos já iniciados, modalidade do workshop); A4 (seção 8); coluna "Bloqueio" das tabelas 1.1 e 1.2 do plano da onda 3; perguntas com turma citada da seção 8 dos planos das ondas 2 e 3; pedidos das seções 8 (onda 1) e 9 (ondas 2 e 3); seções 1 e 2 e os blocos das ondas de docs/pendencias-camada-1.md; pedidos G (plano da Graduação, seção 8) e MP (gestor-de-midia da Graduação, seção 7); travas da Graduação e saídas tiradas de uso, do diário (docs/andamento-planejamento.md).
- Escritos no script, cada um com o arquivo e a seção de origem num comentário: o que cada código bloqueia (BLOQ), as travas em texto corrido dos blocos da onda 2 e do lote A (TRAVAS), as pendências que vêm de texto corrido (ESPECIFICAS), o alvo dos pedidos da onda 3 (ALVO_ONDA3), o status do kit e as listas das ondas.
- Quando uma saída é aprovada ou uma pendência é respondida, atualize a fonte (plano, pendências ou diário) e rode de novo; só mexa no script quando a mudança estiver num dos dicionários acima.
