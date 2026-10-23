---
name: schema-de-curso
description: Escreve a marcação estruturada (JSON-LD) das páginas de curso, da instituição, dos docentes e das perguntas frequentes, para buscadores e IAs entenderem cada página. Use em toda página de curso nova ou reescrita e quando a página nunca aparece como fonte.
---
# Marcação estruturada de curso

Propósito: dar aos buscadores e às IAs sinais claros do que é cada página e de quem está por trás dela. A squad escreve o código; quem aplica é o time do site (projeto ufape-site), depois da aprovação.

Entradas: texto ou URL da página, tipo da página (curso, área, artigo, perguntas frequentes), dados do curso em contexto/catalogo-de-cursos.md e dados da instituição em contexto/ufape-geral.md.

Passos:
1. Escolha os tipos do schema.org:
   - página de curso: Course, com provider apontando para a instituição e hasCourseInstance para cada turma (modalidade, início, carga horária) quando houver turma no catálogo
   - instituição: EducationalOrganization (ou CollegeOrUniversity para a Graduação), com nome, site, logotipo e perfis oficiais
   - docente ou coordenador citado: Person, com cargo e área
   - perguntas frequentes visíveis na página: FAQPage
   - artigo ou guia: Article, com autor e data de atualização
2. Escreva o JSON-LD pronto para colar, usando só dados do catálogo e do contexto. Campo sem dado fica fora do código, nunca preenchido por suposição.
3. Liste as entidades que o texto da página precisa citar (nome completo do curso, área, modalidade, instituição, coordenação) e onde.
4. Confira se a Ufape é descrita do mesmo jeito no site, nos perfis sociais e em portais externos (nome, cidade, modalidades, credenciamento). Aponte toda divergência.
5. Aponte qualquer trecho da página que contradiz outra página ou o catálogo.

Saída: JSON-LD por tipo, lista de entidades e onde citar, checagem de consistência da marca e divergências encontradas.

Verificações antes de terminar:
- Todo campo do JSON-LD tem fonte no catálogo ou no contexto
- Preço, nota do MEC e ato regulatório só aparecem se estiverem no catálogo
- Pós-graduação com "Pós-graduação em" no nome
- O FAQ marcado é o mesmo que está visível na página
