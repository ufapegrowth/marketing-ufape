versao: 1

# PÁGINA DA TURMA OU EDIÇÃO

Formato de saída do workflow /pagina-de-curso (decisões P56, P71 a P74 do plano 03). A plataforma valida este formato antes de gravar: seção fora do catálogo do tipo, seção obrigatória ausente ou texto com número recusam a página. Seção nova só entra numa versão nova deste template (P72).

Quem escreve o quê:
- Dado: vem do banco na hora, no site. A squad não escreve nada nesses campos e não repete os valores no texto.
- IA: texto escrito pela squad e aprovado pelo editor.
- Humano: escolha do editor no app (imagens, depoimentos).

Regras do texto da IA:
- Nunca citar preço, parcelas, datas, vagas, carga horária, duração, local, nomes de docentes ou números de qualquer tipo. Esses fatos aparecem nas seções de dado.
- Nada inventado: o que não estiver na ficha congelada vira [CONFIRMAR] e a seção fica oculta até alguém confirmar.
- Nenhum dado pessoal. Depoimentos não passam pela IA.
- Português do Brasil, sem travessão.

## Cabeçalho

tipo: [pos | livre | workshop | simposio]
curso: [slug do curso, da ficha]
turma_ou_edicao: [slug da turma ou edição, da ficha]
palavra_chave_principal: [da etapa de pesquisa]

## SEO (IA)

titulo_seo: [até 60 caracteres, sem número]
descricao_seo: [até 155 caracteres, sem número]
resposta_citavel: [40 a 60 palavras que respondem "o que é e para quem é", sem número]
entidades: [termos, áreas e conceitos que a página deve nomear]

## Ordem proposta

Ordem padrão do tipo (abaixo). A IA pode propor outra, com uma linha de motivo; o editor aprova (P73).

ordem: [lista de chaves de seção]
motivo_da_ordem: [se diferente do padrão]

## Seções

Cada seção tem: chave, visivel (sim ou nao), e o conteúdo da IA quando houver.

### Comuns a todos os tipos

| Chave | Origem | O que a IA entrega | Obrigatória |
|---|---|---|---|
| hero | IA e humano | titulo (até 70 caracteres) e subtitulo (até 160); a imagem é escolha do editor no acervo | sim |
| numeros | dado | nada (carga horária, duração, módulos e vagas vêm do banco) | não |
| sobre | IA | 2 a 3 parágrafos sobre a proposta do curso | sim |
| para_quem | IA | 3 a 5 itens a partir de publico_alvo da ficha | não |
| investimento | dado e IA | só a frase de apoio (sem valor); total, parcelas e matrícula vêm do banco | sim |
| local_e_datas | dado | nada | sim |
| faq | dado e IA | perguntas e respostas sem número, depois das que já estão na turma | não |
| formulario | dado e IA | texto do botão e uma frase de apoio | sim |
| cta_final | IA | título curto e texto do botão | não |

### Pós-graduação

| Chave | Origem | O que a IA entrega |
|---|---|---|
| diferenciais | dado | nada (sem reescrita) |
| objetivos | dado | nada (sem reescrita) |
| matriz | dado | nada (módulos e disciplinas da turma) |
| docentes | dado | nada (nome, titulação, formação e bio curta da ficha) |
| certificacao | dado e IA | uma frase de apoio, sem citar ato regulatório que não esteja na ficha |
| video | humano | nada |
| depoimentos | humano | nada (escolha do editor, fora da IA) |
| parceiros | dado | nada |

Ordem padrão: hero, numeros, sobre, para_quem, diferenciais, matriz, docentes, certificacao, video, depoimentos, investimento, local_e_datas, parceiros, faq, formulario, cta_final.

### Cursos Livres

| Chave | Origem | O que a IA entrega |
|---|---|---|
| conteudo | dado | nada (módulos) |
| docentes | dado | nada |
| certificacao | dado e IA | uma frase de apoio |
| depoimentos | humano | nada |

Ordem padrão: hero, numeros, sobre, para_quem, conteudo, docentes, certificacao, depoimentos, investimento, local_e_datas, faq, formulario, cta_final.

### Workshop

| Chave | Origem | O que a IA entrega |
|---|---|---|
| programacao | dado | nada (agenda da edição) |
| facilitadores | dado | nada |
| o_que_levar | IA | itens ou pré-requisitos, sem número |

Ordem padrão: hero, sobre, para_quem, programacao, facilitadores, o_que_levar, investimento, local_e_datas, faq, formulario, cta_final.

### Simpósio

| Chave | Origem | O que a IA entrega |
|---|---|---|
| programacao_por_dia | dado | nada (agenda e cronograma da edição) |
| palestrantes | dado | nada |
| parceiros | dado | nada |
| certificacao_participacao | dado e IA | uma frase de apoio |

Ordem padrão: hero, numeros, sobre, para_quem, programacao_por_dia, palestrantes, parceiros, certificacao_participacao, investimento, local_e_datas, faq, formulario, cta_final.

## Marcação para buscadores e IA (JSON-LD)

A IA entrega só a parte textual (nome, descrição e perguntas do FAQ) seguindo a skill schema-de-curso. A plataforma monta o JSON-LD completo com os fatos do banco: Course, CourseInstance, offers, Person e FAQPage.

descricao_schema: [até 300 caracteres, sem número]

## Verificações antes de entregar

- Todas as seções obrigatórias do tipo estão presentes.
- Nenhuma chave fora do catálogo do tipo.
- Nenhum número, preço, data, vaga, local ou nome de docente no texto da IA.
- Toda afirmação sobre o curso tem origem na ficha; o resto está marcado [CONFIRMAR].
- auditorias/03-busca.md, auditorias/08-conversao.md e auditorias/conformidade-educacional.md rodadas.
