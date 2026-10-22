# CATÁLOGO DE CURSOS DA UFAPE

Fonte única de dados de curso para toda a squad. Nenhum agente pode divulgar curso, preço, carga horária, duração, modalidade ou ato regulatório que não esteja aqui. Se um dado faltar, o agente escreve [CONFIRMAR NO CATÁLOGO] e não segue com a peça final.

Responsável pela atualização: [nome, área]
Última atualização: [AAAA-MM-DD]

## Como preencher

- Uma linha por curso e modalidade (o mesmo curso em EAD e presencial são duas linhas).
- linha: graduacao, pos ou livres.
- ato_regulatorio: para Graduação, portaria de autorização ou reconhecimento (número e data). Para Pós, o texto de validade aprovado pela regulação. Para Livres, "curso livre, não confere diploma".
- preco_e_condicoes: valor da mensalidade ou total, número de parcelas, descontos com regras e validade.
- status: aberto, em breve, encerrado. Só cursos "aberto" podem ser divulgados com chamada para inscrição.
- Quando o catálogo crescer, ele pode sair deste arquivo e virar uma tabela no banco da plataforma; os agentes continuam lendo pela mesma regra.

## Cursos

| codigo | linha | curso | modalidade | carga_horaria | duracao | turno_ou_formato | ato_regulatorio | nota_mec_e_fonte | preco_e_condicoes | proxima_turma | pagina_oficial | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [GRAD-001] | graduacao | [Administração] | [EAD] | [3.000 h] | [8 semestres] | [aulas online + polo] | [Portaria nº X, de DD/MM/AAAA] | [nota, fonte e data, ou "não divulgar"] | [R$ X/mês; condições] | [2027.1] | [url] | [aberto] |
| [POS-001] | pos | [MBA em Gestão de Pessoas] | [EAD] | [360 h] | [12 meses] | [online] | [texto de validade aprovado] | [não se aplica] | [R$ X/mês em N parcelas] | [turma de MM/AAAA] | [url] | [aberto] |
| [LIV-001] | livres | [Excel para o Mercado] | [online] | [20 h] | [acesso por 6 meses] | [gravado] | [curso livre, não confere diploma] | [não se aplica] | [R$ X à vista ou N x R$ Y] | [imediato] | [url] | [aberto] |
