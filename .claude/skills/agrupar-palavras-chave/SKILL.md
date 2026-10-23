---
name: agrupar-palavras-chave
description: Transforma uma lista longa de palavras-chave em páginas pilar e páginas de apoio para os cursos da Ufape.
---
# Agrupar palavras-chave por tema

Propósito: transformar uma lista longa de palavras-chave em páginas pilar e páginas de apoio, separadas por linha de negócio (Graduação, Pós-graduação ou Cursos Livres).

Passos:
1. Remova duplicadas e termos fora do tema (ex.: buscas por cursos que a Ufape não oferece, termos de concurso público sem relação com o curso).
2. Agrupe por intenção e significado em comum (ex.: "pós em gestão de pessoas EAD" e "especialização em RH online" ficam juntas).
3. Dê nome a cada cluster e escolha a palavra-chave pilar (em geral, a da página do curso ou da área).
4. Distribua as palavras-chave de apoio entre as páginas (artigos, guias de carreira, perguntas frequentes).
5. Marque as páginas que já existem no site em cada cluster.
6. Monte o mapa por área (por exemplo, Medicina Veterinária, Educação, Gestão): os pilares da área, as páginas que uma instituição de referência teria em cada pilar e a situação de cada uma (existe, fraca ou falta).
7. Mostre quais páginas devem linkar para quais e ponha o mapa em ordem de construção, com as páginas de curso primeiro.

Saída: Tabela de clusters (cluster, pilar, palavras-chave de apoio, situação da página) e mapa por área com situação, links e ordem de construção.

Verificações antes de terminar:
- Uma palavra-chave principal por página
- Nenhum cluster mistura intenção de matrícula com intenção de aprender
- Nenhum cluster mistura linhas de negócio diferentes
