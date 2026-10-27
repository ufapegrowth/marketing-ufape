# QA de marketing: páginas das 8 turmas de abril de 2027 da Pós-graduação (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609), cadeia /pagina-de-curso O1 a O5, onda 3, revisão a

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Encomenda:** O18 (a) do plano saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (versão 2), seção 10.
- **Arquivos revisados (não editados):**
  - O1 /home/user/marketing-ufape/saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda3.md (726 linhas, inteiro)
  - O2 /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda3.md (440 linhas, inteiro)
  - O3 /home/user/marketing-ufape/saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md (1317 linhas, inteiro)
  - O4 /home/user/marketing-ufape/saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda3.md (1369 linhas, inteiro)
  - O5 /home/user/marketing-ufape/saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda3.md (808 linhas, inteiro, com a seção 0.8)
- **Entradas lidas:**
  - /home/user/marketing-ufape/CLAUDE.md e /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 20)
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 2 inteira)
  - Fichas inteiras em /home/user/marketing-ufape/contexto/cursos/pos/: 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609
  - /home/user/marketing-ufape/templates/pagina-da-turma.md
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md, 02-estrategia-e-posicionamento.md, 03-busca.md e 08-conversao.md
  - Plano da onda 3, versão 2: linhas 1 a 409 e 780 a 1013 (regras E1 a E22, travas da seção 2.3, kit por turma 4.1 a 4.9, perguntas, pedidos e encomendas)
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md (inteiro)
- **Não refeito (conferido por script pelo orquestrador):** dígitos no texto visível da O3; contagens de títulos e subtítulos da O3; as 32 contagens do O4; botões do O5 (31, 26 e 18); travessão e meia-risca; frases proibidas da E3. As contagens dos campos que esta revisão manda trocar foram feitas à mão e pedem nova conferência por script (lista na seção 9).
- **Não aberto:** faculdade.ufape.com.br; nenhuma busca na web; fichas das turmas antigas (535, 665, 663, 68607, 664, 654, 670, 586), cujas datas foram aceitas como estão na O1 (nota interna, fora de peça).
- **Dados pessoais:** nenhum nos 5 arquivos nem nesta revisão. Docentes só como dado da ficha.
- **Marcadores:** [SUPOSIÇÃO] é leitura ou escolha deste agente; [CONFIRMAR] é dado que só a Ufape, a plataforma ou o time do site tem; [CONFIRMAR NO CATÁLOGO] é dado de curso fora do catálogo e da ficha.

---

## 1. Vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| O1 pesquisa-de-palavras-chave | **APROVADO COM RESSALVAS** | arquivo de trabalho, sem texto de página; alvo realista de 68628 com "presencial" e recorte de espécie que a página não pode usar (A1, A2), uma afirmação errada sobre turma de São Paulo em 68632 (A4), uma frase de 366 que contradiz o bloqueio da pergunta QC2 (A3) e "pós de Cursos Livres" (A5). Nenhuma ressalva bloqueia a página |
| O2 mensagens | **CORRIGIR** | listas de presenciais incompletas sem "entre eles" ou "entre elas" (E4) em 679, 366, 68628, 68617, 68636 e 68609; "prática de laboratório" generalizada para os três presenciais de 679 (E5); "Pós-operatório" em 366, que a ficha não traz (E3); "ou só a tireoide" sem curso que sustente o guia; "o paciente inteiro" e "alopecia X" já tirados pela O3 e ainda na casa que alimenta O7 a O9; "pós" abreviado |
| O3 landing-page | **CORRIGIR** | herda E4 e E5 da O2 no hero e no `sobre` de 679, 68628 e 68636 e no FAQ de 679; nota interna dentro do bloco de página em 679 e 366; páginas de 68628, 68617, 68636 e 68609 chamam para o cronograma com a `matriz` oculta (página entrega o que promete); `numeros` de 68609 visível com o número de módulos em conflito; link para 366 antes da data confirmada; tabela de contagens desatualizada; pedidos 1, 2, 3, 5 e 6 do O5 (seção 0.8) |
| O4 seo-on-page | **CORRIGIR** | FAQPage precisa das gêmeas das correções de FAQ (679 e a regra da `matriz` oculta); `descricao_schema` de 68636 com lista de presenciais incompleta (E4); nota com "ou só a tireoide"; plural citado errado; fonte da data de 679 descrita errada. Decisões D1, D2 e D3 aceitas (seção 2) |
| O5 otimizador-de-cta | **CORRIGIR** | título de reserva de 68636 com lista de presenciais incompleta (E4); reserva do `cta_final` não cobre as respostas do FAQ que também citam o cronograma; referência de regra trocada; plural citado errado. Formulário com finalidade, aceite por canal desmarcado, E21, Q56, Q57 e Q58 atendidos; link da política segue como trava |

**Destino:** os 5 arquivos voltam ao orquestrador para aplicar A1 a A52 com o texto exato da seção 4 (os agentes donos podem aplicar, se o orquestrador preferir). Aplicadas com o texto exato e com a recontagem por script dos campos da seção 9, as 8 páginas **não precisam de nova rodada deste agente** e seguem para a aprovação humana do OB1 (OC1-A), que continua presa às travas da seção 6. Nada é publicado, enviado ou pago a partir destes arquivos.

---

## 2. Decisões do qa nesta revisão (pedidas pelos agentes)

1. **D1 do O4 (títulos de 68635 e 366 sem o prefixo):** aceita. Com o prefixo, os nomes do catálogo têm 64 e 67 caracteres e não cabem em `titulo_seo` (60). O título sem o prefixo não tira nem acrescenta palavra ao nome da área (E2) e não usa nenhuma das formas proibidas ("Pós em", "Pós Graduação"); o prefixo e o nome completo ficam no H1 (`hero.titulo` da O3), na `descricao_seo`, na `resposta_citavel` e na `descricao_schema`. A alternativa de 366 com a forma digitada ("Pós-graduação em Fisioterapia Veterinária | Ufape") fica recusada: troca o nome da página (E2). Observação sem troca [SUPOSIÇÃO]: "Clínica Médica e Emergência de Pequenos Animais | Ufape" pode ser lido como o hospital Ufape Clínica; a pessoa do marketing decide no OB1 se aceita esse risco.
2. **D2 do O4 (68632 sem "presencial" no título):** aceita. O nome completo do catálogo com a marca ocupa 58 caracteres; "presencial" está na `descricao_seo`, na `resposta_citavel`, na `descricao_schema` e no `hero.titulo` da O3.
3. **D3 do O4 (`resposta_citavel` sem frase de público):** aceita, pela Q42 da onda 2a. O público da ficha aparece só no FAQ.
4. **Ponte opcional 679 x 68635 (O2, 2.5; O3, linha 134; O4, linha 193):** entra no `faq` de 679 e no FAQPage. Responde 679-Q5 da O1, diz em que cada curso é centrado e não insinua que um contém o outro. O link para 68635 segue a E19. A nota de "item opcional" sai de dentro do bloco de página (A17).
5. **"Locorregionais" no `sobre` de 68609 (O4, seção 10, item 3):** fica como conteúdo. É o tema do módulo 14 da ficha ("Prática: Bloqueio locorregional I e II"); nenhum campo de SEO usa o termo, e o nome "Anestesiologia Locorregional Veterinária" aparece só na frase-ponte.
6. **Pedidos do O5 na seção 0.8:** 1 aceito com a trava da plataforma (A28); 2 aceito e ampliado às respostas do FAQ que citam o cronograma (A22 a A25, A44, A49); 3 aceito (A26, A27); 4 sem troca; 5 e 6 aceitos (A29, A30); 7 sem troca.
7. **`matriz` visível com o mês do 3º módulo em 679, 68635 e 366:** atende. A `matriz` é o cronograma oficial (dado), não texto da IA; nenhum texto da squad liga esse mês à regra de entrada (E6 e E18). O item de dado da regra do 3º módulo continua sem o mês nessas três (O3, seção 11.1).
8. **"Alopecia X" e "Um objetivo":** a O3 acertou ao tirar (E1). A O2 é a casa que alimenta O7 a O9 e recebe a mesma troca (A11), para o erro não voltar nas mensagens (E12).
9. **Pares de E4 aceitos sem "entre eles":** 68635 ("prática presencial de semiologia, exames e atendimento") descreve categorias que cobrem os nove presenciais e fica; 68617 só fica completo com "anatomia" (A13).

---

## 3. O que foi conferido e o resultado

### 3.1 Dados de curso contra ficha e catálogo, módulo a módulo

| Turma | Catálogo (linha) | Presenciais na ficha | O que os arquivos dizem | Resultado |
|---|---|---|---|---|
| 679 | linha 79: São Paulo, semipresencial, 03/04/2027, IV, 500 h, aberto | 3 (prática laboratorial; zoonoses com sábado teórico e domingo de coleta para raiva; controle de infecção hospitalar com prática no domingo) | lista completa no `sobre`, na `resposta_citavel` e no schema | confere; mas o FAQ chama os três de "prática de laboratório" (E5, A5, A19, A39) e o hero e a mensagem central citam só laboratório e zoonoses (E4, A4, A6, A18, A20) |
| 68632 | linha 80: Goiânia, presencial, 10/04/2027, V, 500 h, aberto | turma presencial, sem formato por módulo; módulo 1 presencial | nunca "online" nem "semipresencial"; temas com "Entre os temas" | confere |
| 68635 | linha 81: São Paulo, semipresencial, 10/04/2027, V, 750 h, aberto | 9 (3, 6, 10, 14, 18, 21, 24, 25 e 28) | os 9 pelo tema na prova 1; FAQ "a maior parte é online" (19 de 28) | confere |
| 366 | linha 82: São Paulo, semipresencial, 10/04/2027 (site 24/04), I, 500 h, aberto | 9 (3, 6, 9, 12, 15, 18, 20, 21 e 24); 3 e 20 sem "prática" | prova 1 nomeia o 3 e o 20 à parte | confere; "Pós-operatório" da variação 1 não está na ficha (A7); variação 2 sem "entre elas" (A8) |
| 68628 | linha 83: São Paulo, semipresencial, 10/04/2027, VII (planilha VI), 500 h, aberto | 8 (5, 7, 9, 12, 15, 17, 20 e 24) | prova 1 com "Entre os módulos presenciais" | confere na prova; o hero e a mensagem central listam quatro temas como "no presencial" sem cobrir o 12 e o 24 (E4, A9, A21) |
| 68617 | linha 85: São Paulo, semipresencial, 17/04/2027, V (planilha VII), 500 h, aberto | 2 (12 e 23): atendimento, anatomia, ultrassonografia abdominal, cirurgia e casos | FAQ e prova 3 completos | confere; variação 2 sem "anatomia" (A13) |
| 68636 | linha 86: São Paulo, semipresencial, 17/04/2027 só no site, VIII, 500 h, aberto | 6 (4, 7, 13, 16, 19 e 24), legenda "aulas práticas" | `resposta_citavel` com "entre outras" | confere na resposta; hero, mensagem central, schema e reserva do O5 dizem "aulas práticas presenciais de imagem e endoscopia" como lista fechada (E4, A14, A15, A33, A34, A41, A47) |
| 68609 | linha 87: Goiânia, semipresencial, 24/04/2027, VIII, 500 h, aberto | 10 (5, 8, 11, 14, 16, 17, 20, 21, 23 e 24); hands-on em 5, 11 e 23; castração em 16 e 17; 20 com parte online | `sobre` e FAQ com "entre outros" | confere; variação 2 da O2 sem "entre outros" (A16); `numeros` com 26 x 24 módulos visível (A35) |

Outros fatos conferidos: reembolso de inscrição presente em 68632, 68635, 366, 68628, 68617, 68636 e 68609 e ausente em 679 (atende); aviso de passagem e hotel ausente em 679 e "somente após a confirmação oficial" em 68636 (atende); 68636 e 68609 sem a frase "não serão transmitidas" (atende: nenhum texto a usa); 68609 com 26 módulos nos dados e 24 no cronograma (atende como [CONFIRMAR NO CATÁLOGO]); 68617 com "Como montar seu TCC" e sem TCC na avaliação (atende); preços da tabela 8 do O4 iguais ao catálogo (33.000,00; 33.000,00; 33.000,00; 33.000,00; 38.940,00; 36.000,00; 37.950,00; 32.450,00).

### 3.2 Nome do catálogo (E2)

H1, `sobre`, FAQ, títulos do formulário e campos de SEO usam o nome exato nas 8 turmas, com "Pós-graduação em" (D1 aceita, seção 2). "Veterinária" fora do nome só como palavra de corpo. 68609 sempre no singular; a citação do plural da página no ar está errada em três notas (A2a, A43, A48): o H1 da ficha é "Anestesiologia Veterinárias". **Atende**, com as três notas corrigidas.

### 3.3 Travas por turma

| Trava | Onde conferi | Resultado |
|---|---|---|
| Regra 8 e E22 em 68632 | O2 4, O3 2.3 a 2.5 e 11.1, O4 2, O5 2 | atende: nenhuma pergunta, item de dado, campo ou resposta sobre entrada depois do início |
| 679, 366 e 68636 sem data | textos de página e de SEO sem data nem mês; `local_e_datas` e `startDate` só com a confirmação | atende |
| 68628 e 68617 sem número de turma | `CourseInstance.name` sem turma; `numeros` com a turma só depois de OU29 e OU30; nenhum texto cita | atende |
| `diferenciais` oculta onde o dado tem problema | as 8 com "só depois da correção" (superlativos, MEC, promessas, frase normativa) | atende |
| `matriz` oculta onde o dado tem problema | 68628 (Para definir, módulos repetidos), 68617 (módulo 17), 68636 (anos fora da sequência), 68609 (frase de carreira, módulo 17) | atende na visibilidade; falha no que a página promete com ela oculta (A22 a A25) |
| 68632 e 366 sem "coordenação" | `docentes` sem o rótulo; nenhum texto | atende |
| E13 e E14 | convite da prova de Especialista de 68609, "formar especialistas" de 68632 e superlativos só no OB1 | atende |
| E15 e E16 | duplicatas com a grafia da coordenação; nenhuma sigla de diplomado nas 8 listas | atende |
| E19 (link entre turmas) | pontes com link só depois da página conferida | atende, com a ressalva de 366, cuja página só vai ao ar com a data (A24a) e a falta da marcação de link para 68632 na página de 366 (A23) |
| E21 (formulário) | O3 e O5 sem "usamos seus dados só para esse contato"; Q56 no O5 | atende |

### 3.4 Frases-ponte (E11)

As cinco pontes (A1, A2, A3, A4 e a opcional 679 x 68635) dizem "é centrada" para cada curso, não comparam valor, carga, prática nem docentes e não usam "cobre", "contém", "inteiro" ou "uma das partes". A ponte A3 diz que 68635 tem "a emergência do paciente grave no mesmo percurso" e que 68623 é "centrada no cuidado do paciente crítico": descreve cada curso pelo próprio nome, sem dizer que 68635 inclui a terapia intensiva. A ponte A4 deixa 662 fora e não usa "ortopedia" como termo. **Atende.**

### 3.5 Coerência O2, O3, O4 e O5

| Ponto | Situação | Resultado |
|---|---|---|
| Mensagens da O2 na O3 | iguais, com os ajustes de forma da O3 (seção 0, item 3) | atende; as correções de E4 e E5 têm gêmea nos dois arquivos |
| O2 depois dos ajustes da O3 | O2 ainda traz "o paciente inteiro", "alopecia X" e "pós" abreviado | corrigir na O2 (A10, A11, A12, A16b) para O7 a O9 não herdarem |
| FAQ da O3 x FAQPage do O4 | palavra por palavra nas 8; em 68617 o O4 deixa a frase do guia A7 fora até o guia sair, com regra de sincronia | atende; gêmeas de A19 e da regra da `matriz` oculta no O4 (A39, A44) |
| Apoios do formulário e do `cta_final` O3 x O5 | iguais nas 8 | atende |
| Botão | "Quero receber o retorno do time" no hero, no formulário e no `cta_final` das 8; V2 suspenso | atende |
| Notas da O3 sobre termos irmãos | dizem "só na frase-ponte", mas o apoio do `cta_final` de 68635 e 68636 também nomeia | corrigir a nota (A26, A27), como pede o O5 |

### 3.6 Formulário e LGPD (O5, seção 0.3)

| Exigência | Situação | Resultado |
|---|---|---|
| Finalidade escrita | "Usamos seus dados para o time de vendas da Faculdade Ufape retornar sobre esta turma..." | atende |
| Aceite por canal e finalidade, desmarcado | duas caixas opcionais; e-mail só com o campo preenchido | atende |
| Quem não marca não entra em S2 e S3 (E21, Q56) | escrito | atende |
| Saída fácil | SAIR e descadastro na confirmação | atende |
| Link da política de privacidade | "[CONFIRMAR: endereço da política de privacidade da Faculdade Ufape]" | **trava de publicação** de todo formulário |
| Só o necessário | nome, WhatsApp e e-mail opcional; lista do que não se pede | atende; o checklist da O3 recebe a correção (A29) |
| Erro de envio para o time, não para a secretaria (Q57) | escrito | atende |
| Cookies e pixel | [CONFIRMAR] | trava de publicação |

### 3.7 Disputa de busca (E20)

O1 (seção 5) e O4 (seção 9) registram os pares pedidos pelo plano (535 e 665 com 68632, 663 com 68635, 68607 com 68609) e os que as fichas mostram (654 com 68628, 670 com 68636, 664 e 586 com 68609), com a regra de canonical ou 301 como pedido [CONFIRMAR] ao time do site (S1 a S7). A constatação de que o 3º módulo de 535 e de 663 já passou, segundo a O1, fica como pedido de conferência ao time do site (decisão 18). **Atende.**

### 3.8 Erros já corrigidos na onda 2a que não voltaram

"Quero me inscrever" fora do botão; "conta inteira"; "nem gravadas"; "na mão"; "bombas de infusão"; "quase todos os temas"; "a teoria vem antes da prática"; "laboratório inteiro"; "de cães e gatos" fora do nome de 68632; nome do catálogo com palavra a mais; "É pensado para quem" na `resposta_citavel`; frase-ponte com "cobre" ou "uma das partes"; `matriz` visível com frase de resultado; frase "só para esse contato"; erro de envio para a secretaria. **Nenhum voltou.** O padrão de "inteiro" voltou só na O2 de 68628 ("o paciente inteiro", A10), já tirado pela O3.

---

## 4. Correções numeradas (arquivo, linha e texto exato)

Linhas como estão em 27/10/2026. Onde uma correção acrescenta linha, aplicar de baixo para cima no arquivo para não deslocar as linhas seguintes.

### O1 pesquisa-de-palavras-chave-pos-2026-10-27-onda3.md (ressalvas)

**A1. Linha 40 (alvo realista de 68628).**
- Trocar: "| 68628 | pós-graduação em oncologia veterinária | K10.1 da pesquisa de 26/10 | pós em oncologia veterinária de pequenos animais presencial em São Paulo (68628-K1) |"
- Por: "| 68628 | pós-graduação em oncologia veterinária | K10.1 da pesquisa de 26/10 | pós em oncologia veterinária semipresencial (68628-K3); o 68628-K1 fica só em lista e anúncio |"

**A2. Linha 418 (mesmo ponto na seção de 68628).**
- Trocar: "**Alvo realista de curto prazo:** pós em oncologia veterinária de pequenos animais presencial em São Paulo (68628-K1), com a ressalva da modalidade."
- Por: "**Alvo realista de curto prazo:** pós em oncologia veterinária semipresencial (68628-K3). O 68628-K1 fica só em lista e anúncio: a turma é semipresencial e a ficha não restringe a espécie."

**A3. Linha 49 (366 contradiz 366-QC2).**
- Trocar: "679, 68635 e 366 só falam da entrada depois do início sem o mês do 3º módulo (E18)."
- Por: "679 e 68635 só falam da entrada depois do início sem o mês do 3º módulo (E18); em 366 a pergunta fica bloqueada até OU20 e OU25 (366-QC2)."

**A4. Linha 295 (68632-Q4: a 665 está à venda).**
- Trocar: "Sem turma aberta em São Paulo no catálogo: a parte de São Paulo vai para \"vou confirmar com o time\" [CONFIRMAR]."
- Por: "Sem turma com status \"aberto\" em São Paulo no catálogo (a 665 está em \"verificar (turma já iniciada e com venda)\", seção 5): a parte de São Paulo vai para \"vou confirmar com o time\" [CONFIRMAR]."

**A4a. Linha 592 (curso livre chamado de pós).**
- Trocar: "A pós de Cursos Livres sobre anestesia felina é 616 (só link)."
- Por: "O curso livre de anestesia felina é o 616 (só link)."

### O2 mensagens-pos-2026-10-27-onda3.md

**A4b. Linha 88 (decisão 4 da seção 2).**
- Trocar: "uso opcional, só no `faq` de 679 e no guia A14 de 679, a critério do qa."
- Por: "uso no `faq` de 679 e no guia A14 de 679, aprovado pelo qa na revisão O18a."

**A4c. Linha 98 (679, mensagem central, E4).**
- Trocar: "> Infectologia veterinária do diagnóstico ao controle de infecção hospitalar, com módulos online e prática presencial de laboratório e de zoonoses."
- Por: "> Infectologia veterinária do diagnóstico ao controle de infecção hospitalar, com módulos online e práticas presenciais, entre elas de laboratório e de zoonoses."

**A5. Linha 111 (679, resposta de prática, E5).**
- Trocar: "Os módulos presenciais trazem prática de laboratório: coleta, armazenamento e envio de amostras, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."
- Por: "Os módulos presenciais trazem prática: coleta, armazenamento e envio de amostras no laboratório, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."

**A6. Linha 120 (679, variação 2, E4).**
- Trocar: "\"Virologia, micologia, bacteriologia e antibioticoterapia em módulos online, com prática presencial de laboratório e de zoonoses.\""
- Por: "\"Virologia, micologia, bacteriologia e antibioticoterapia em módulos online, com prática presencial de laboratório, de zoonoses e de controle de infecção hospitalar.\""

**A7. Linha 220 (366, variação 1, E3: a ficha fala em traumas, não em pós-operatório).**
- Trocar: "\"Pós-operatório, paciente neurológico, cão idoso: a reabilitação começa pela avaliação.\""
- Por: "\"Trauma, paciente neurológico, cão idoso: a reabilitação começa pela avaliação.\""

**A8. Linha 221 (366, variação 2, E4).**
- Trocar: "\"Módulos online e prática presencial de hidroterapia, recursos eletrofísicos, reabilitação neurológica e ortopédica e terapias manuais.\""
- Por: "\"Módulos online e prática presencial, entre elas hidroterapia, recursos eletrofísicos, reabilitação neurológica e ortopédica e terapias manuais.\""

**A9. Linha 232 (68628, mensagem central, E4).**
- Trocar: "cirurgia oncológica e discussão de casos no presencial, com a maior parte dos módulos online."
- Por: "cirurgia oncológica e discussão de casos entre os temas presenciais, com a maior parte dos módulos online."

**A10. Linha 238 (68628, título da prova 3, igual à O3).**
- Trocar: "**Neoplasia por neoplasia, e o paciente inteiro.**"
- Por: "**Neoplasia por neoplasia e cuidado do paciente.**"

**A11. Linha 269 (68617, E1: a letra X pode ser lida como numeral, igual à O3).**
- Trocar: "neoplasias adrenais e tireoidianas, alopecia X, dislipidemias,"
- Por: "neoplasias adrenais e tireoidianas, dislipidemias,"

**A12. Linha 279 (68617, abreviação e promessa do guia sem curso de tireoide verificado).**
- Trocar: "\"A pós percorre a endocrinologia da fisiologia às emergências endócrinas, com discussão de casos e aula prática presencial. Se você quer aprofundar só o diabetes ou só a tireoide, o guia de decisão da área mostra os caminhos lado a lado.\""
- Por: "\"A pós-graduação percorre a endocrinologia da fisiologia às emergências endócrinas, com discussão de casos e aula prática presencial. Se você quer aprofundar só o diabetes, o guia de decisão da área mostra os caminhos lado a lado.\""

**A13. Linha 287 (68617, variação 2, lista dos presenciais sem anatomia).**
- Trocar: "com aula prática presencial de atendimento, ultrassonografia abdominal e cirurgia endócrina."
- Por: "com aula prática presencial de atendimento, anatomia, ultrassonografia abdominal e cirurgia endócrina."

**A14. Linha 298 (68636, mensagem central, E4).**
- Trocar: "> Pneumologia veterinária da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais de imagem e endoscopia respiratória."
- Por: "> Pneumologia veterinária da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais, entre elas de imagem e endoscopia respiratória."

**A15. Linha 320 (68636, variação 2, E4).**
- Trocar: "\"Aulas teóricas a distância e aulas práticas presenciais de ultrassonografia pulmonar, laringotraqueobroncoscopia e rinoscopia.\""
- Por: "\"Aulas teóricas a distância e aulas práticas presenciais, entre elas ultrassonografia pulmonar, laringotraqueobroncoscopia e rinoscopia.\""

**A16. Linha 353 (68609, variação 2, E4).**
- Trocar: "\"Módulos online e prática presencial com hands-on de sedação, TIVA e TCI e anestesia em felinos e exóticos, e bloqueios em modelos anatômicos.\""
- Por: "\"Módulos online e prática presencial com, entre outros, hands-on de sedação, TIVA e TCI e anestesia em felinos e exóticos, e bloqueios em modelos anatômicos.\""

**A16b. Linha 354 (68609, variação 3, abreviação, igual à O3).**
- Trocar: "Em dúvida entre as pós de anestesiologia? O time explica a diferença."
- Por: "Em dúvida entre as pós-graduações de anestesiologia? O time explica a diferença."

### O3 landing-page-pos-2026-10-27-onda3.md

**A2a. Linha 46 (plural citado errado).**
- Trocar: "(68609 sem o plural \"Anestesiologias Veterinárias\" do H1 da página no ar)"
- Por: "(68609 sem o plural \"Anestesiologia Veterinárias\" do H1 da página no ar)"

**A17. Linha 134 (679, nota interna dentro do bloco de página; decisão 4 da seção 2).**
- Trocar: "> **Infectologia ou clínica médica ampla: qual eu faço?** (item opcional, [SUPOSIÇÃO]: ponte 2.5 da O2, que responde a pergunta 679-Q5 da O1; o qa decide se entra)"
- Por: "> **Infectologia ou clínica médica ampla: qual eu faço?**"

**A17a. Linha 146 (registro da decisão, fora do bloco).**
- Trocar: "- **Link da ponte:** só depois de a página de 68635 passar na conferência (E19, mesmo lote, qa em 18/11)."
- Por: "- **Link da ponte:** só depois de a página de 68635 passar na conferência (E19, mesmo lote, qa em 18/11). A pergunta da ponte entra no `faq` (decisão do qa na revisão O18a: responde 679-Q5 da O1 e diz em que cada curso é centrado, sem dizer que um contém o outro)."

**A18. Linha 101 (679, subtítulo, E4).**
- Trocar: "- subtitulo (145 caracteres): Infectologia veterinária do diagnóstico ao controle de infecção hospitalar, com módulos online e prática presencial de laboratório e de zoonoses."
- Por: "- subtitulo (159 caracteres, contagem do qa a recontar por script; se passar de 160, tirar \"veterinária \" do início): Infectologia veterinária do diagnóstico ao controle de infecção hospitalar, com módulos online e práticas presenciais, entre elas de laboratório e de zoonoses."

**A20. Linha 106 (679, abertura do `sobre`, mesma troca).**
- Trocar: "com módulos online e prática presencial de laboratório e de zoonoses. A Faculdade Ufape oferece a Pós-graduação em Infectologia Veterinária"
- Por: "com módulos online e práticas presenciais, entre elas de laboratório e de zoonoses. A Faculdade Ufape oferece a Pós-graduação em Infectologia Veterinária"

**A19. Linha 129 (679, FAQ, E5).**
- Trocar: "Os módulos presenciais trazem prática de laboratório: coleta, armazenamento e envio de amostras, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."
- Por: "Os módulos presenciais trazem prática: coleta, armazenamento e envio de amostras no laboratório, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."

**A24a. Linha 277 (68632, link para 366 antes da data).**
- Trocar: "- **Links da ponte (E19):** a página de 366 é do mesmo lote (qa em 18/11); a de 578 é do lote B. Sem a página conferida, o nome fica sem link."
- Por: "- **Links da ponte (E19):** a página de 366 é do mesmo lote (qa em 18/11), mas só vai ao ar com a data confirmada (P4, OU20): o nome vira link só com a página de 366 publicada; a de 578 é do lote B. Sem a página conferida e no ar, o nome fica sem link."

**A26. Linha 339 (68635, nota de SEO; pedido 3 do O5).**
- Trocar: "só aparece no nome da outra pós-graduação, na frase-ponte."
- Por: "só aparece no nome da outra pós-graduação, na frase-ponte, e no apoio do `cta_final` (que não é campo de SEO)."

**A31. Linha 440 (OB1 de 68635, item novo).**
- Trocar: "\"desempenham um papel crucial\" e \"contribuir para o seu desenvolvimento profissional\". Reescrever ou retirar (E14)."
- Por: "\"desempenham um papel crucial\" e \"contribuir para o seu desenvolvimento profissional\". Reescrever ou retirar (E14). (novo) O mesmo texto chama o curso de \"pós-graduação em clínica médica geral\": usar o nome padrão \"Pós-graduação em Clínica Médica e Emergência de Pequenos Animais\"."

**A32. Linha 510 (366, nota interna dentro do bloco de página).**
- Trocar: "com foco em fisioterapia veterinária. [SUPOSIÇÃO: a expressão final leva a palavra principal da O1 ao corpo; \"fisioterapia veterinária\" é termo da ficha]"
- Por: "com foco em fisioterapia veterinária."

**A23. Linha 539 (366, ponte sem a marcação de link para 68632).**
- Trocar: "> A Pós-graduação em Clínica Cirúrgica de Cães e Gatos é centrada na clínica cirúrgica, dos princípios"
- Por: "> A [Pós-graduação em Clínica Cirúrgica de Cães e Gatos](link para a página da turma 68632) é centrada na clínica cirúrgica, dos princípios"

**A22. Linha 626 (68628, página com `matriz` oculta chama para o cronograma).**
- Trocar: "a chave só aparece com o dado corrigido (OB1, item 7) |"
- Por: "a chave só aparece com o dado corrigido (OB1, item 7). Se a página for publicada com a `matriz` oculta, valem o `cta_final` de reserva do O5 (seção 5.3) e, no `faq`, a resposta \"Como funciona o semipresencial? Tenho de ir sempre?\" sem o trecho \", com o mês marcado no cronograma\" (o FAQPage do O4 muda junto) |"
- Atenção: na linha 896 há o mesmo trecho; esta troca vale só para a linha 626.

**A21. Linhas 643 e 648 (68628, subtítulo e abertura do `sobre`, E4).**
- Linha 643, trocar: "- subtitulo (129 caracteres): Quimioterapia, eletroquimioterapia, cirurgia oncológica e discussão de casos no presencial, com a maior parte dos módulos online."
- Por: "- subtitulo (142 caracteres, contagem do qa a recontar por script): Quimioterapia, eletroquimioterapia, cirurgia oncológica e discussão de casos entre os temas presenciais, com a maior parte dos módulos online."
- Linha 648, trocar: "cirurgia oncológica e discussão de casos no presencial, com a maior parte dos módulos online. A Faculdade Ufape"
- Por: "cirurgia oncológica e discussão de casos entre os temas presenciais, com a maior parte dos módulos online. A Faculdade Ufape"

**A24. Linha 761 (68617, `matriz` oculta).**
- Trocar: "a chave só aparece com o dado corrigido (OB1, item 8) |"
- Por: "a chave só aparece com o dado corrigido (OB1, item 8). Se a página for publicada com a `matriz` oculta, valem o `cta_final` de reserva do O5 (seção 6.3) e, no `faq`, a resposta \"Quanto do curso é presencial?\" sem o trecho \", e o cronograma está nesta página\" (o FAQPage do O4 muda junto) |"

**A36. Linha 809 (68617, FAQ, igual à A12).**
- Trocar: "Se você quer aprofundar só o diabetes ou só a tireoide, o guia de decisão da área mostra os caminhos lado a lado."
- Por: "Se você quer aprofundar só o diabetes, o guia de decisão da área mostra os caminhos lado a lado."

**A27. Linha 880 (68636, nota de SEO; pedido 3 do O5).**
- Trocar: "só aparecem nos nomes das outras pós-graduações, na frase-ponte."
- Por: "só aparecem nos nomes das outras pós-graduações, na frase-ponte, e no apoio do `cta_final` (que não é campo de SEO)."

**A25. Linha 896 (68636, `matriz` oculta).**
- Trocar: "têm data fora da sequência: a chave só aparece com o dado corrigido (OB1, item 7) |"
- Por: "têm data fora da sequência: a chave só aparece com o dado corrigido (OB1, item 7). Se a página for publicada com a `matriz` oculta, valem o `cta_final` de reserva do O5 (seção 7.3) e, no `faq`, a resposta \"Vou ver endoscopia e imagem na prática?\" sem o trecho \", e o cronograma mostra o mês de cada módulo presencial\" (o FAQPage do O4 muda junto) |"

**A33. Linhas 913 e 918 (68636, subtítulo e abertura do `sobre`, E4).**
- Linha 913, trocar: "- subtitulo (153 caracteres): Da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais de imagem e endoscopia respiratória."
- Por: "- subtitulo (152 caracteres, contagem do qa a recontar por script): Da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais, entre elas de imagem e endoscopia."
- Linha 918, trocar: "aulas práticas presenciais de imagem e endoscopia respiratória. A Faculdade Ufape"
- Por: "aulas práticas presenciais, entre elas de imagem e endoscopia respiratória. A Faculdade Ufape"

**A35. Linha 1029 (68609, `numeros` com módulos em conflito).**
- Trocar: "| numeros | sim | dado. O dado de módulos diz 26 e o cronograma traz 24: só aparece depois da conferência (OB1, item 7) |"
- Por: "| numeros | **só depois da conferência** | dado. O dado de módulos diz 26 e o cronograma traz 24: a chave só aparece com o número de módulos conferido (OB1, item 7); até lá, oculta |"

**A34. Linha 1033 (68609, `matriz` oculta).**
- Trocar: "a chave só aparece com o dado corrigido (OB1, itens 8 a 10) |"
- Por: "a chave só aparece com o dado corrigido (OB1, itens 8 a 10). Se a página for publicada com a `matriz` oculta, vale o `cta_final` de reserva do O5 (seção 8.3) |"

**A37. Linha 1160 (pedido OB1, itens comuns, 68635 descrito errado).**
- Trocar: "(e, em 68632, 68628 e 68635, a frase de reconhecimento pelo órgão, os certificados por parte da carga e o texto de certificado)"
- Por: "(e, em 68632 e 68628, a frase de reconhecimento pelo órgão e o texto de certificado; em 68635, as duas certificações e os certificados por parte da carga)"

**A28. Linhas 150, 283, 419, 555, 690, 825, 961 e 1098 (título do formulário; pedido 1 do O5).** Em cada uma das 8 linhas abaixo, a linha do botão do `formulario` ganha antes dela a linha do título, com o texto do O5 (seções 1.1 a 8.1). Se a plataforma recusar o campo, o título sai e nada mais muda [CONFIRMAR com a plataforma].
- Linha 150, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Infectologia Veterinária" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 283, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Clínica Cirúrgica de Cães e Gatos" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 419, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Clínica Médica e Emergência de Pequenos Animais" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 555, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 690, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Oncologia Veterinária" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 825, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Endocrinologia de Pequenos Animais" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 961, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Pneumologia Veterinária" e, na linha seguinte, "- botao: Quero receber o retorno do time"
- Linha 1098, trocar: "- botao: Quero receber o retorno do time"
- Por: "- titulo: Tire suas dúvidas sobre a Pós-graduação em Anestesiologia Veterinária" e, na linha seguinte, "- botao: Quero receber o retorno do time"

**A29. Linha 1201 (checklist; pedido 5 do O5).**
- Trocar: "(e-mail opcional), mais a pergunta de interesse se necessária."
- Por: "(e-mail opcional), sem pergunta de interesse (O5, seção 0.3)."

**A30. Linha 1202 (checklist; pedido 6 do O5).**
- Trocar: "- [ ] Finalidade do uso dos dados e link da política de privacidade ao lado do botão (conformidade-educacional); o O5 refina."
- Por: "- [ ] Finalidade do uso dos dados e link da política de privacidade abaixo do botão, depois da frase de risco (conformidade-educacional; texto do O5, seção 0.3)."

**A38. Linhas 1224, 1225 e 1228 (tabela de contagens desatualizada).**
- Linha 1224, trocar: "| 679 | 65 | 145 |"
- Por: "| 679 | 65 | 159 |"
- Linha 1225, trocar: "| 68632 | 62 | 118 |"
- Por: "| 68632 | 62 | 119 |"
- Linha 1228, trocar: "| 68628 | 65 | 129 |"
- Por: "| 68628 | 64 | 142 |"
- A linha de 68636 ("| 68636 | 61 | 152 |") fica igual: com a A33, o subtítulo passa a ter 152.

### O4 seo-on-page-pos-2026-10-27-onda3.md

**A39. Linha 150 (679, FAQPage, gêmea da A19).**
- Trocar: "Os módulos presenciais trazem prática de laboratório: coleta, armazenamento e envio de amostras, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."
- Por: "Os módulos presenciais trazem prática: coleta, armazenamento e envio de amostras no laboratório, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar."

**A40. Linha 193 (679, decisão 4 da seção 2).**
- Trocar: "A pergunta da ponte (quarta) é item opcional na O3 [SUPOSIÇÃO: o qa decide se entra na página]. Se sair da página, sai da marcação no mesmo dia."
- Por: "A pergunta da ponte (quarta) entra na página e na marcação (decisão do qa na revisão O18a)."

**A42. Linha 902 (68617, nota com a frase do guia, gêmea da A36).**
- Trocar: "(\"Se você quer aprofundar só o diabetes ou só a tireoide, o guia de decisão da área mostra os caminhos lado a lado.\")"
- Por: "(\"Se você quer aprofundar só o diabetes, o guia de decisão da área mostra os caminhos lado a lado.\")"

**A41. Linhas 936, 938 e 949 (68636, `descricao_schema`, E4).**
- Linha 936, trocar: "**descricao_schema** (230 caracteres, limite 300):"
- Por: "**descricao_schema** (242 caracteres, limite 300; contagem do qa a recontar por script):"
- Linhas 938 e 949, trocar: "com aulas teóricas a distância e aulas práticas presenciais de imagem e endoscopia respiratória."
- Por: "com aulas teóricas a distância e aulas práticas presenciais, entre elas de imagem e endoscopia respiratória."

**A43. Linha 1060 (plural citado errado).**
- Trocar: "(nunca \"Anestesiologias Veterinárias\", E2)"
- Por: "(nunca \"Anestesiologia Veterinárias\", E2)"

**A45. Linha 1194 (tabela de contagens).**
- Trocar: "| 68636 | 48 | 141 | 43 | 230 |"
- Por: "| 68636 | 48 | 141 | 43 | 242 |"

**A48. Linha 1216 (plural citado errado).**
- Trocar: "\"Anestesiologias\" no plural"
- Por: "\"Veterinárias\" no plural"

**A46. Linha 1275 (fonte da data de 679).**
- Trocar: "Em 679 e 68636 a data é a do site e só vale depois da confirmação."
- Por: "Em 679 a data da planilha e a do site coincidem, mas só vale depois da confirmação da P3 (OU19); em 68636 a data é só do site e só vale depois da confirmação (OU21)."

**A44. Linha 1310 (sincronia do FAQPage com a `matriz` oculta).**
- Trocar: "4. **Para a O3 e o qa:** em 68617 a frase do guia A7 só entra na resposta do FAQ e na marcação com o guia publicado e linkado."
- Por: "4. **Para a O3 e o qa:** em 68617 a frase do guia A7 só entra na resposta do FAQ e na marcação com o guia publicado e linkado. Se 68628, 68617 ou 68636 forem publicadas com a `matriz` oculta, a resposta do FAQ que cita o cronograma perde o trecho indicado na O3 (tabela de visibilidade, linha `matriz`) e a marcação muda no mesmo dia, para o FAQPage continuar igual ao FAQ visível (revisão O18a)."

### O5 otimizador-de-cta-pos-2026-10-27-onda3.md

**A50. Linha 68 (referência de regra trocada: a E4 do plano da onda 3 é de listas de presenciais).**
- Trocar: "(regras E4 e E21 do plano)"
- Por: "(regra E4 da decisão 17, D16, e regra E21 do plano)"

**A49. Linha 175 (pedido 2 ampliado às respostas do FAQ).**
- Trocar: "trocar pelo texto de reserva das seções 5.3, 6.3, 7.3 e 8.3 deste arquivo |"
- Por: "trocar pelo texto de reserva das seções 5.3, 6.3, 7.3 e 8.3 deste arquivo; em 68628, 68617 e 68636, a resposta do `faq` que cita o cronograma também perde o trecho indicado na revisão O18a |"

**A47. Linha 603 (68636, título de reserva, E4).**
- Trocar: "> **Título (reserva):** Veja as aulas práticas presenciais de imagem e endoscopia respiratória."
- Por: "> **Título (reserva):** Veja as aulas práticas presenciais, entre elas de imagem e endoscopia respiratória."

**A51. Linha 650 (plural citado errado).**
- Trocar: "nunca \"Anestesiologias Veterinárias\""
- Por: "nunca \"Anestesiologia Veterinárias\""

**A52. Sem troca de texto, trava registrada (O5):** endereço da política de privacidade (linha 94) [CONFIRMAR]; campos "Título" do formulário e "Apoio" do `cta_final` e `botao` do hero [CONFIRMAR com a plataforma]; frase de risco, "Enviar seus dados não gera cobrança" e "Nenhuma cobrança foi feita" só com o time do site confirmando que o formulário não cobra; janela do teste e limiares com o desenho-de-experimentos.

---

## 5. Pedido OB1 por turma (conferência da lista)

As listas da O3 (seções 1.6 a 8.6) e o pedido comum (seção 10) cobrem, por turma, frases ligadas ao MEC, turma mínima de 20, regra do 3º módulo, "PROVA DE BOLSA", convite da prova de Especialista (68609), superlativos e promessas da E14, "garante", "formar especialistas", data de início (679, 366, 68636), coordenação e CEP (366), turma VII ou VI e V ou VII, URL "/v/", módulos fora da sequência ou "Para definir", marcas de terceiros, duplicatas de docentes, turma antiga à venda (E20), passagem e hotel, URL sem "-em-", "Documentos para matrícula (MEC e UFAPE)", U11, 1ª mensalidade, botão COMPRAR, política e cookies, parceiros vazios e exportação da versão anterior. **Completa**, com um acréscimo (A31: 68635 chamado de "clínica médica geral" no texto da página) e uma correção de redação no pedido comum (A37).

| Turma | Itens na O3 | Resultado |
|---|---|---|
| 679 | 18 | completa |
| 68632 | 20 | completa |
| 68635 | 18 | completa com A31 |
| 366 | 19 | completa |
| 68628 | 20 | completa |
| 68617 | 20 | completa |
| 68636 | 21 | completa |
| 68609 | 25 | completa |

---

## 6. Travas de publicação (não bloqueiam o texto, bloqueiam a página no ar)

| Trava | Turmas | Quem destrava |
|---|---|---|
| Link da política de privacidade e aviso de cookies no formulário | as 8 | Ufape (endereço) e time do site |
| OB1 aprovado e feito no site | as 8 | pessoa do marketing; regulação nos itens de certificação, ato regulatório e título |
| U11 (valor da inscrição x matrícula) | as 8 | Ufape |
| Data de início confirmada (`local_e_datas` e `startDate`) | 679 (OU19), 366 (OU20, com o CEP), 68636 (OU21) | Ufape |
| `matriz` corrigida no dado, ou reserva do O5 mais os trechos de FAQ da A22 a A25 | 68628, 68617, 68636, 68609 | Ufape e editor |
| Número de módulos conferido (`numeros`) | 68609 | Ufape |
| Link para 366 só com a página de 366 no ar | 68632 | editor |
| Guia A7 publicado, ou a última frase da resposta sai | 68617 | Ufape e editor |
| URL "/v/" conferida | 68617 | time do site |
| Confirmação de que o formulário não cobra | as 8 | time do site |
| Campos `titulo` do formulário, apoio do `cta_final` e `botao` do hero aceitos | as 8 | plataforma |
| Conferência de 11/12 e reconferência de 04/01 (destino, UTM, política, lead no CRM) | as 8 | humano; gestor-de-midia confere |

---

## 7. auditorias/conformidade-educacional.md, item por item (5 arquivos)

| Item | Resultado | Onde e o que muda |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | atende | nome exato nas 8 (D1 aceita); modalidade, carga e turma só como dado; 68632 presencial, as outras semipresenciais |
| Curso com status "aberto" | atende | as 8 "aberto" (catálogo, linhas 79 a 87) |
| Modalidade clara e correta | atende | 68628 nunca descrita como presencial; 68617 sem "muita prática"; 68636 pela legenda da ficha |
| Graduação: ato regulatório | não se aplica | linha pos |
| Pós lato sensu sem "reconhecida pelo MEC" | atende | `certificacao` oculta nas 8; nenhum "MEC" no texto; frases das páginas no ar no OB1 |
| Curso livre: não confere diploma | não se aplica | |
| Nota MEC só com fonte e ano | atende | nenhuma |
| Nenhuma promessa de emprego, salário, promoção, aprovação ou sucesso | atende | "empregabilidade" (679), "do anestesista volante ao chefe de setor" (68609) e carreira (68617) só no dado oculto e no OB1 |
| Empregabilidade ou satisfação com fonte | não se aplica | |
| Superlativos só com fonte | **falha** | "o paciente inteiro" na O2 de 68628 (A10); superlativos das fichas fora do texto e no OB1 |
| Comparação com concorrente objetiva | atende | nenhuma; as pontes internas dizem em que cada curso é centrado |
| Preço com valor, parcelas e condições completas | atende no texto | nenhum valor em texto; 1ª mensalidade e U11 no OB1 comum (trava) |
| Bolsa e desconto com regra | atende | nenhuma bolsa, desconto ou promoção |
| Urgência real | atende | regra do 3º módulo só como dado; nenhum contador nem "últimas vagas" |
| Prouni, Fies ou financiamento | não se aplica | |
| Autorização de imagem, voz e depoimento | atende | docentes só como dado (decisões 8 e 10); `depoimentos` oculta |
| Menores de idade | não se aplica | |
| Formulário com finalidade e link da política | **falha até a trava** | finalidade escrita no O5; endereço da política [CONFIRMAR] |
| WhatsApp e e-mail só com consentimento e saída fácil | atende | caixas por canal desmarcadas, Q56, SAIR e descadastro |
| Nenhum dado pessoal | atende | |
| Anúncios dentro das políticas da Meta e do Google | não se aplica | nenhum anúncio neste lote |
| Página entrega o que a peça promete | **falha** | listas de presenciais apresentadas como completas sem serem (E4: A4c, A6, A8, A9, A13 a A16, A18, A20, A21, A33, A41, A47); "prática de laboratório" para os três presenciais de 679 (E5: A5, A19, A39); "Pós-operatório" fora da ficha (A7); guia de tireoide sem curso verificado (A12, A36, A42); cronograma prometido com a `matriz` oculta (A22 a A25, A34, A44, A49); `numeros` com módulos em conflito (A35) |
| Anúncios: característica pessoal, urgência falsa, pessoa pública, caixa alta, driblar análise | não se aplica | |
| Página de destino com dados da Ufape, contato e política | **falha até a trava** | política [CONFIRMAR]; contatos de vendas por praça vêm do dado |

**Resultado:** Aprovado ( ) Bloqueado (x). Itens bloqueados: superlativo na O2, formulário e política, página que entrega o que promete. Todos fecham com A1 a A52 mais as travas da seção 6.
**Revisado por:** qa-de-marketing (agente); humano: [pessoa do marketing, no OB1].
**Data:** 27/10/2026.

---

## 8. Auditorias dos departamentos

### 8.1 auditorias/03-busca.md (O1 e O4, com a O3)

| Item | Resultado |
|---|---|
| Uma única palavra-chave alvo por página | atende (O1, seção 1; `palavra_chave_principal` da O3); alvo realista de 68628 corrigido (A1, A2) |
| Títulos e descrições únicos | atende entre as 8 e contra a onda 2; iguais às turmas antigas de mesmo nome, com canonical e 301 pedidos (E20) |
| Nenhuma página importante bloqueada para indexação | [CONFIRMAR com o time do site] |
| Nenhum link interno quebrado | pendente na publicação: pontes (E19) e link para 366 (A24a) |
| Toda página aponta para a sua página pilar | pendente: 68609 é a pilar de Anestesiologia (O1); as demais áreas sem pilar definida, chamado para o seo-tecnico [SUPOSIÇÃO de dono] |
| Conteúdo responde à pergunta principal | atende (`resposta_citavel` com o que é o curso, D3) |
| Correções escritas como chamados | atende (OB1 e pedidos S1 a S7) |
| Turmas encerradas redirecionadas | atende como pedido (S4: 670, 664 e 654) |
| Dados de curso batem com o catálogo | atende (tabela 8 do O4 conferida) |
| Resposta citável, FAQ real e marcação estruturada | atende com as gêmeas A39 e A44 |
| Conteúdo principal sem JavaScript | [CONFIRMAR com o time do site] |
| Nenhum resultado de IA registrado sem checagem | atende (64 perguntas "conferir manualmente") |
| Nenhuma consulta com duas páginas disputando sem correção | atende (O1 seção 5, O4 seção 9) |

### 8.2 auditorias/08-conversao.md (O3 e O5)

| Item | Resultado |
|---|---|
| Topo passa no teste dos 5 segundos no celular | pendente na construção (checklist 11.2 da O3) |
| Uma chamada principal por página | atende; botão COMPRAR no OB1 comum |
| Formulário pede só o necessário | atende (O5, 0.3), com a A29 |
| Provas reais e autorizadas | atende depois de A7 e das correções de E4 e E5 |
| Objeções respondidas na página | atende (FAQ por turma) |
| Testes com hipótese escrita | atende (16 cartões; V2 suspenso) |
| Resultados registrados | previsto (desenho-de-experimentos e analise-cro) |
| Dados do curso conferidos com o catálogo | atende como dado |
| Eventos de lead e inscrição rastreados e lead no CRM | previsto; conferência de 11/12 e 04/01 |

### 8.3 auditorias/02-estrategia-e-posicionamento.md (O2)

| Item | Resultado |
|---|---|
| Uma meta principal | atende por herança do plano (15 matrículas por turma) |
| Persona e curso nomeados | atende |
| 8 canais avaliados | não se aplica (casa de mensagens) |
| Posicionamento nomeia a alternativa real | atende (nota interna por turma, [SUPOSIÇÃO]) |
| Todo pilar tem prova | atende depois de A5 e A7 |
| Regras de voz com exemplos | pendente na Ufape; não bloqueia (como no O0) |
| Cabe no tempo e na verba | não se aplica |
| Sem promessa de emprego, aprovação ou salário | atende |
| Preços, bolsas e condições do catálogo | atende (nenhum valor; nenhuma bolsa) |

---

## 9. Próximo passo

1. O orquestrador aplica A1 a A52 com o texto exato da seção 4 e reconta por script: subtítulos de 679 (A18, contagem do qa 159; se passar de 160, vale a reserva sem "veterinária "), 68628 (A21, 142) e 68636 (A33, 152) na O3; `descricao_schema` de 68636 (A41, 242) no O4.
2. Com as trocas feitas, as 8 páginas seguem para a aprovação humana do OB1 (OC1-A, pessoa do marketing), com as listas da O3 e as travas da seção 6; itens de certificação, ato regulatório e título de especialista passam também pela regulação [CONFIRMAR quem].
3. As próximas revisões da onda 3 (O18b e O18c) usam esta versão como destino: nenhuma mensagem, post ou roteiro traz "Pós-operatório" em 366, "ou só a tireoide", "o paciente inteiro", "alopecia X", lista fechada de presenciais sem "entre eles" ou "entre elas", nem chama para "o cronograma" de 68628, 68617, 68636 ou 68609 sem a `matriz` visível.
4. Nada é publicado, enviado ou pago a partir destes arquivos.

---

## Fatos (com fonte)

- Nome, local, modalidade, início, turma, carga horária, preço e status "aberto" das 8 turmas; 535, 665, 663 e 68607 em "verificar (turma já iniciada e com venda)"; 664 e 654 "sem venda"; 670 "encerrado": contexto/catalogo-de-cursos.md, seção 2, linhas 48 a 102.
- 679: 3 presenciais (3 prática laboratorial; 13 zoonoses, sábado teórico e domingo com coleta para raiva; 22 controle de infecção hospitalar com prática no domingo), sem reembolso de inscrição e sem aviso de passagem e hotel: ficha de 679.
- 68632: presencial, módulo 1 presencial, sem coordenação, "formar especialistas", reconhecimento pelo MEC e "garante": ficha de 68632.
- 68635: 9 presenciais (3, 6, 10, 14, 18, 21, 24, 25 e 28), "duas certificações", texto de apresentação que chama o curso de "pós-graduação em clínica médica geral": ficha de 68635.
- 366: 9 presenciais, 3 e 20 sem "prática", apresentação com "traumas, doenças adquirida, atividade física, idade e sobrepeso" (sem "pós-operatório"), coordenação "UFAPE", CEP 01428-001: ficha de 366.
- 68628: 8 presenciais (5, 7, 9, 12, 15, 17, 20 e 24), 24 com "Para definir", 21 e 22 repetidos: ficha de 68628.
- 68617: 2 presenciais (12 e 23) com atendimento, anatomia, ultrassonografia abdominal e cirurgia; módulo 17 com a data do 11: ficha de 68617. Cursos livres 542 (diabetes), 458, 103 e 104 da área, sem curso de tireoide citado: O1, seção 11.1.
- 68636: 6 presenciais (4, 7, 13, 16, 19 e 24), legenda "aulas práticas"; módulos 16 e 24 com ano fora da sequência; sem a frase "não serão transmitidas": ficha de 68636.
- 68609: 10 presenciais, hands-on em 5, 11 e 23, castração em 16 e 17, 20 com parte online; "26 módulos" nos dados e 24 no cronograma; H1 "Pós-graduação em Anestesiologia Veterinárias": ficha de 68609.
- Regras E1 a E22, travas, OU3, OU19 a OU35 e OC1-A: saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md, versão 2.
- Limites de 70 e 160 caracteres no hero, de 60, 155 e 300 nos campos de SEO e de 40 a 60 palavras na resposta citável: templates/pagina-da-turma.md.
- Correções Q1 a Q59 e decisões da onda 2: saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md.
- Opt-in por canal e finalidade como E4 da D16: docs/execucao-2026-10-26.md, decisão 17.

## [SUPOSIÇÃO]

- O título "Clínica Médica e Emergência de Pequenos Animais | Ufape" pode ser confundido com o hospital Ufape Clínica (risco registrado para a pessoa do marketing, sem troca).
- "Prática presencial de semiologia, exames e atendimento" em 68635 descreve categorias que cobrem os nove presenciais e dispensa "entre eles".
- As contagens manuais dos campos trocados (159, 142, 152 e 242), a recontar por script.
- "Trauma" como troca de "Pós-operatório" em 366, a partir de "traumas" da apresentação da ficha.
- O seo-tecnico como dono do chamado de página pilar das áreas sem pilar.
- A ponte 679 x 68635 ajuda quem compara infectologia com clínica médica ampla, sem canibalizar as duas páginas.

## [CONFIRMAR]

- Endereço da política de privacidade e aviso de cookies do pixel e das tags.
- U11, OU3, OU4, OU6, OU14, OU19, OU20, OU21, OU25, OU29, OU30, OU31, OU34 e OU35 (abertas no plano).
- Se a plataforma aceita `titulo` no formulário, apoio no `cta_final` e `botao` no hero; se o formulário não cobra.
- Se a Ufape corrige o cronograma de 68628, 68617, 68636 e 68609 antes de 10/12 (define `matriz` visível ou reserva).
- Número de módulos de 68609 (26 ou 24).
- Guia A7 publicado e com link antes da frase do guia entrar no FAQ de 68617.
- Venda de 535 e 663 depois do 3º módulo (O1) e regra de canonical e 301 (S1 a S7), com quem executa.
- Indexação e conteúdo sem JavaScript das 8 páginas; página pilar por área.
- Quem aprova certificação, ato regulatório e título (A9) e quem edita o site.

## Fontes

- /home/user/marketing-ufape/saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/contexto/ufape-geral.md, /home/user/marketing-ufape/contexto/pos-graduacao.md, /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/ (fichas de 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609)
- /home/user/marketing-ufape/templates/pagina-da-turma.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md, 02-estrategia-e-posicionamento.md, 03-busca.md, 08-conversao.md
