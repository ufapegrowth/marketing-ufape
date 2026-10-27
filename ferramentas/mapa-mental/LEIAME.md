# Gerador do mapa mental e dos JSON por curso

Gera, a partir de contexto/catalogo-de-cursos.md e das saídas aprovadas, um JSON por item no esquema versão 1 (saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md) e o mapa mental HTML que abre offline.

Como rodar, a partir da raiz do repositório:

    python3 -I ferramentas/mapa-mental/mapa_json.py --write
    python3 -I ferramentas/mapa-mental/mapa_html.py

Saídas: saidas/10-operacoes-de-marketing/cursos/*.json e saidas/02-estrategia-e-posicionamento/cmo-geral-AAAA-MM-DD.html (mude HOJE e o nome do arquivo no script a cada onda). A pasta saida/ guarda só o arquivo intermediário e a versão da página para publicação.

Regras: nenhum número é inventado; dado ausente vira "[CONFIRMAR]" ou null com pendência. Status do kit, pendências por turma e pedidos de aprovação estão escritos no próprio script e precisam ser atualizados quando uma saída é aprovada ou uma pendência é respondida. Nada vai para o banco: é só arquivo.
