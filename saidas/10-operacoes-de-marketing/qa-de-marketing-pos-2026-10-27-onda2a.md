# QA de marketing: páginas das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), cadeia /pagina-de-curso F1 a F5, onda 2, revisão a

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Encomenda:** F13, primeira revisão do lote da onda 2 (páginas), do plano saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (versão 2), seção 10.
- **Arquivos revisados (não editados):**
  - F1 /home/user/marketing-ufape/saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md (457 linhas, inteiro)
  - F2 /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda2.md (307 linhas, inteiro)
  - F3 /home/user/marketing-ufape/saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md (779 linhas, inteiro)
  - F4 /home/user/marketing-ufape/saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda2.md (834 linhas, inteiro)
  - F5 /home/user/marketing-ufape/saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md (526 linhas, inteiro)
- **Entradas lidas:**
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 20)
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 2 inteira)
  - Fichas inteiras: /home/user/marketing-ufape/contexto/cursos/pos/657-pos-graduacao-em-anestesiologia-avancada.md, 341-pos-graduacao-em-medicina-interna-equina.md, 289-pos-graduacao-em-cardiologia-veterinaria.md, 68615-pos-graduacao-em-patologia-clinica.md e 333-pos-graduacao-em-citopatologia-veterinaria.md
  - /home/user/marketing-ufape/templates/pagina-da-turma.md
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md, 02-estrategia-e-posicionamento.md, 03-busca.md e 08-conversao.md
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (versão 2, inteiro)
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2.md (revisão F0, inteira)
- **Não refeito (conferido por script pelo orquestrador):** as 20 contagens do F4, os botões do F5 (31, 26 e 18 caracteres) e a busca de travessão e meia-risca nos 5 arquivos. As contagens dos campos que esta revisão manda trocar (Q40 a Q52) foram feitas à mão e precisam de nova conferência por script.
- **Não aberto:** faculdade.ufape.com.br; nenhuma busca na web.
- **Dados pessoais:** nenhum nos 5 arquivos nem nesta revisão. Docentes só aparecem como dado da ficha, fora do texto da IA.
- **Marcadores:** [SUPOSIÇÃO] é leitura ou escolha deste agente; [CONFIRMAR] é dado que só a Ufape ou a plataforma tem; [CONFIRMAR NO CATÁLOGO] é dado de curso fora do catálogo.

---

## 1. Vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| F1 pesquisa-de-palavras-chave | **APROVADO COM RESSALVAS** | arquivo de trabalho, sem texto de página; um dado de 289 descrito errado (Q1) |
| F2 mensagens | **CORRIGIR** | texto para a página com número por extenso ("dois"), promessa não verificada ("conta inteira", "teoria antes da prática"), recorte "de cães e gatos" marcado [CONFIRMAR NO CATÁLOGO] dentro da mensagem central de 289, "quase todos os temas" mais forte que a ficha, frase-ponte que insinua que 68615 contém 333 |
| F3 landing-page | **CORRIGIR** | herda os problemas da F2 e acrescenta: nome de curso alterado no `sobre` de 657 e 68615, botão "Quero me inscrever" num formulário que só pede contato (conformidade: página entrega o que promete), frase do formulário que contradiz o aceite por canal, `matriz` de 657 visível com frases de resultado clínico no dado |
| F4 seo-on-page | **CORRIGIR** | nome de curso fora do catálogo em `titulo_seo` e `descricao_schema` de 657 e 68615 ("Anestesiologia Avançada Veterinária", "Patologia Clínica Veterinária"); FAQPage repete as frases a corrigir; premissa errada sobre 68605 (está à venda) |
| F5 otimizador-de-cta | **CORRIGIR** | braço V2 "Quero me inscrever" promete inscrição num formulário de contato; link da política de privacidade ainda [CONFIRMAR] (item de conformidade sem marcação); mensagem de erro manda para "a secretaria" num botão que é de vendas |

**Destino:** os 5 arquivos voltam ao orquestrador para aplicar Q1 a Q59 com o texto exato da seção 4 (os agentes donos podem aplicar, se o orquestrador preferir). Aplicadas com o texto exato e com a recontagem por script dos campos do F4 trocados, as páginas **não precisam de nova rodada deste agente** e seguem para a aprovação humana do OB1 (pessoa do marketing), que continua presa às travas de publicação da seção 6. Nada é publicado, enviado ou pago a partir destes arquivos.

---

## 2. Decisões do qa nesta revisão (pedidas pelos agentes)

1. **"Um" e "uma" (F3, linha 701; F4, linha 31; F5, linha 464).** Artigo indefinido não é número e passa ("é um curso semipresencial", "um percurso maior", "de um laboratório"). Quando a palavra conta alguma coisa, ela é número e sai: "uma das partes" (frase-ponte, Q13, Q34, Q36, Q53), "Há um módulo de medicina equina" (Q8, Q27), "abre com um módulo presencial" (Q15, Q35). Número por extenso que não é artigo também sai: "os dois caminhos" em 289 (Q12, Q31). Ordinais: nenhum no texto de página dos 5 arquivos. Algarismos e romanos: nenhum. Se o validador da plataforma barrar qualquer "um" ou "uma", vale a troca pelo artigo definido [CONFIRMAR com a plataforma].
2. **Reembolso em 68615 (F3, linha 485).** Confere: a ficha de 68615 traz, em Considerações, "Eventuais pedidos de reembolso dos valores de inscrição, só serão devidos caso a turma não seja confirmada", igual a 657, 289 e 333. A frase da F3 fica. O erro está na nota da F2 (linha 49), que limita a frase a 657, 289 e 333 (Q3). O que entra em "valores de inscrição" (matrícula, 1ª mensalidade antecipada) fica [CONFIRMAR com a secretaria].
3. **"Ecocardiografia" no `sobre` de 289 (F4, linha 781).** Aceito como conteúdo: é o nome do módulo 8 da ficha ("Princípios Básicos De Ecocardiografia; Estudo Doppler e Hemodinâmica na Ecocardiografia"), aparece uma vez numa lista de temas e não está em título, descrição, resposta citável nem entidade. Não toma a palavra da página de 698.
4. **"De cães e gatos" em 289 (F4, linha 782).** Sai do texto de página (Q11, Q29, Q30). A ficha tem cardiologia equina (módulo 22) e de pets não convencionais (módulo 23); a F2 e a F3 marcaram o recorte [CONFIRMAR NO CATÁLOGO], e texto marcado [CONFIRMAR] não vai para seção visível (template). O F4 já estava certo ao deixar o termo fora.
5. **Botão.** Vale o controle do F5, "Quero receber o retorno do time", nas três posições (hero, formulário e `cta_final`) das 5 páginas (Q17, Q25). "Quero me inscrever" sai do texto provisório da F3 e o V2 do F5 fica suspenso (Q58, Q59), porque o clique não inscreve: pede retorno do time.
6. **"Você decide com a conta inteira na frente".** Sai das 5 páginas (Q2, Q10, Q21, Q24, Q48). É promessa de que a página mostra todos os custos, e isso não está verificado: em 657 a prova de recuperação é "cobrada separadamente" sem valor (ficha), e o valor da inscrição (R$ 260,00 informado pelo CEO) diverge da matrícula do site (R$ 250,00) até a U11 (decisão 16).

---

## 3. O que foi conferido e o resultado

### 3.1 Texto de página sem número, preço, data, local nem nome de docente

| Verificação | F2 | F3 | F4 | F5 | Resultado |
|---|---|---|---|---|---|
| Algarismo, romano, ordinal | nenhum | nenhum | nenhum | nenhum | atende |
| Número por extenso | "dois caminhos" (L140) | "dois caminhos" (L349) | nenhum (frase fora da marcação) | nenhum | corrigir: Q12, Q31 |
| "Um" ou "uma" que conta | "Há um módulo" (L100), "um módulo presencial" (L210), "uma das partes" (L158) | L210, L573, L470, L590 | L522, L654 | nenhum | corrigir: Q8, Q13, Q15, Q27, Q34, Q35, Q36, Q53 |
| Preço, parcela, valor de inscrição | nenhum | nenhum | só chave `{{catalogo.preco_total}}` na marcação | nenhum | atende |
| Data, vaga, carga, duração | nenhum | nenhum | só chaves de dado | nenhum | atende |
| Local (cidade, bairro, endereço, hospital) | nenhum | nenhum (289 sem cidade; 341 sem "hospital veterinário") | nenhum no texto; cidade só em `addressLocality` | nenhum | atende |
| Nome de docente | nenhum | nenhum | nenhum (sem `instructor` nem `Person`) | nenhum | atende |

### 3.2 Certificação oculta

`certificacao` com visivel nao nas 5 páginas (F3, linhas 74, 187, 308, 426 e 552); nenhum "MEC", "certificado", "reconhecida" ou "especialista" como título em texto de página; F4 sem `educationalCredentialAwarded`; F5 põe selo e frase de certificação fora do botão. **Atende.**

### 3.3 Coerência entre F2, F3, F4 e F5

| Ponto | Situação | Resultado |
|---|---|---|
| Mensagem central, provas, objeções e chamadas da F2 na F3 | usadas sem reescrita, com a divisão título e subtítulo | atende; as correções da F2 se repetem na F3 com o mesmo texto |
| FAQ do F4 x FAQ da F3 | palavra por palavra nas 5 turmas; em 289 o F4 tira a frase do guia de decisão (só entra com o guia A2 publicado) e em 68615 tira só o link | atende; cada correção de FAQ da F3 tem a gêmea no F4 (Q45 a Q48, Q53) |
| Botão do hero da F3 x F5 | F3 usa "Quero me inscrever" (provisório) no hero, no formulário e no `cta_final`; F5 propõe "Quero receber o retorno do time" | corrigir na F3 (Q17, Q25) |
| Frase de apoio do formulário F3 x F5 | F3 diz "Usamos seus dados só para esse contato"; F5 tem duas caixas de aceite para campanha | a frase da F3 contradiz o aceite por canal: vale a do F5 (Q26) |
| `cta_final` F3 x F5 | títulos iguais (chamada principal da F2); apoio diferente | vale o apoio do F5 (Q26) |
| Nome de curso | F2 e F5 usam o nome do catálogo; F3 (`sobre` de 657 e 68615) e F4 (título e schema de 657 e 68615) acrescentam "veterinária" ao nome | corrigir: Q19, Q32, Q39 a Q43, Q49 a Q52 |
| "De cães e gatos" em 289 | F2 e F3 usam; F4 deixa fora | corrigir na F2 e na F3 (Q11, Q29, Q30) |
| Reembolso em 68615 | F2 limita a frase a 3 turmas; F3 e F4 incluem 68615 | a ficha dá razão à F3 (decisão 2); corrigir a nota da F2 (Q3) |

### 3.4 Travas por turma

| Trava | Onde conferi | Resultado |
|---|---|---|
| 657 sem pré-requisito | `para_quem` oculta; F5 não pergunta se é anestesista; F4 sem `audience` e sem `coursePrerequisites` | atende no texto; a frase do F4 "É pensado para quem quer aprofundar a decisão crítica" descreve público e sai (Q42) |
| 657 sem prova de Especialista | nenhuma menção no texto; convite só no OB1 | atende |
| 657 sem a frase de resultado clínico | "reduzir complicações e mortalidade perioperatória" fora do texto e da ordem | atende no texto; **a `matriz` (dado, visível) traz "elevando drasticamente as taxas de retorno à circulação espontânea" e "a decisão do anestesista dita a sobrevivência"**: corrigir a visibilidade (Q18) |
| 341 sem promoção | nenhuma frase, pergunta ou chamada; `diferenciais` oculta; `offers` só com dado limpo | atende |
| 341 sem local | sem "hospital veterinário", sem Indaiatuba; `local_e_datas` só depois da correção | atende (a página não sai antes de OU11) |
| 333 sem "coordenação" | nenhum texto de página; `docentes` sem o rótulo | atende |
| 333 sem pós-início | nenhuma pergunta nem item de dado sobre entrada depois do início | atende |
| 289 sem cidade (CP1) | F2, F3, F4 e F5 sem Goiânia no texto; cidade só no dado e em `addressLocality` | atende |
| 68615 x 333 sem canibalização | vocabulário separado nos campos de SEO; âncoras cruzadas; leitura somada no teste do F5 | atende com uma correção: a frase-ponte diz que 68615 "cobre o laboratório clínico inteiro" e "tem a citologia como uma das partes", o que insinua que 68615 contém 333 e puxa o candidato de 333 (Q13, Q34, Q36, Q53); "O laboratório inteiro" sai pelo mesmo motivo (Q14, Q33) |

### 3.5 Dados de curso contra a ficha e o catálogo

| Afirmação | Fonte conferida | Resultado |
|---|---|---|
| Nome, local, modalidade, CH, turma, início, total e status das 5 (F4, seção 7) | catálogo, seção 2, linhas 74 a 78 | confere (657: 48.400,00, 360 h, II; 341: 43.500,00, 500 h, I; 289: 35.400,00, 500 h, II, "Semi presencial"; 68615: 35.400,00, 500 h, VII; 333: 28.050,00, 500 h, I) |
| 289: "a maior parte dos módulos presenciais é de prática hands-on de ecocardiograma" | ficha de 289: presenciais 6 (sem conteúdo), 9, 13, 16, 19 e 24 (aula prática e prova final); ecocardiograma em 9, 13, 16 e 19 | confere (correção do orquestrador) |
| 289: "com ecocardiograma na mão nos módulos práticos" (mensagem central, subtítulo e `sobre`) | mesma ficha | **generaliza para todos os presenciais**: corrigir para "com ecocardiograma na prática" (Q11, Q29, Q30) |
| 289: "de cães e gatos" | ficha: cardiologia equina (22) e pets não convencionais (23) | não confere: Q11, Q29, Q30 |
| 657: "As aulas práticas não são transmitidas nem gravadas" | ficha: "não serão transmitidas ou disponibilizadas posteriormente" | "gravadas" não está na ficha: Q4, Q20 |
| 657: prática presencial "com ventiladores, monitores e bombas de infusão na mão" | ficha: ventiladores e monitores no módulo 8 (presencial); "bombas de infusão" só no módulo 14, que é ONLINE | "bombas de infusão na mão" no presencial não confere: Q5, Q22, Q45 |
| 657: demais provas (anestesia de precisão, risco moderado a alto, crises, bloqueios, hemodinâmica, TIVA e TCI, reanimação viscoelástica) | ficha, apresentação, objetivo e cronograma | confere |
| 341: "Prática em quase todos os temas" | ficha: "treinamentos práticos e demonstrativos na maioria dos temas" | mais forte que a ficha: Q7, Q27 |
| 341: "A teoria vem antes da prática em cada sistema" | ficha: módulos "ONLINE PRESENCIAL" sem ordem descrita; neonatologia (9) só online | não está na ficha: Q9, Q28, Q47 |
| 341: sistemas, estágio obrigatório, medicina baseada em evidências, avaliação | ficha, cronograma e "Avaliação e metodologia" | confere |
| 68615: objetivo, módulos, presenciais (4, 6, 7, 9, 11, 17, 23 citados) e laudos | ficha de 68615 | confere |
| 68615: reembolso e aviso de passagem e hotel | ficha (reembolso sim; aviso não, vem de contexto/pos-graduacao.md) | confere |
| 333: 6 presenciais (1, 5, 10, 12, 13, 20), 3 de leitura (5, 10, 20), demais pelo tema | ficha de 333 | confere |
| 333: temas por sistema e atualizações (imunocitopatologia, automação, citoinclusão) | ficha de 333 | confere |
| 68605 "não está à venda" (F4, linha 723) | catálogo, linha 65: "verificar (turma já iniciada e com venda)" | não confere: Q55 |

### 3.6 Formulário e LGPD (F5, seção 0.3)

| Exigência | Situação | Resultado |
|---|---|---|
| Finalidade escrita | "Usamos seus dados para o time de vendas da Faculdade Ufape retornar sobre esta turma e orientar sua inscrição..." | atende |
| Aceite por canal e finalidade, nunca pré-marcado | duas caixas (WhatsApp e e-mail), opcionais, desmarcadas; e-mail só vale com o campo preenchido | atende; falta dizer que quem não marca não entra nas listas de campanha (Q56) |
| Saída fácil | SAIR no WhatsApp; descadastro no e-mail | atende |
| Link da política de privacidade | "[CONFIRMAR: endereço da política de privacidade da Faculdade Ufape]" | **sem marcação**: trava de publicação de todo formulário até a Ufape informar o endereço |
| Só o necessário | nome e WhatsApp obrigatórios, e-mail opcional, lista do que não se pede | atende |
| Cookies e pixel | [CONFIRMAR] no F5 | trava de publicação |
| Frase "não gera cobrança nem compromisso" | [SUPOSIÇÃO] do F5, condicionada | atende como texto; o time do site confirma antes de publicar |
| Campo "Título" do formulário e "Apoio" do `cta_final` | o template só prevê botão e frase de apoio (formulário) e título e botão (`cta_final`) | [CONFIRMAR com a plataforma]; se ela recusar, o título do formulário sai e o apoio do `cta_final` vira a frase de apoio do formulário |

---

## 4. Correções numeradas (arquivo, linha e texto exato)

Linhas dos arquivos como estão em 27/10/2026. Onde a mesma troca vale para várias linhas, todas estão listadas.

### F1 pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md

**Q1. Linha 231 (dado de 289).**
- Trocar: "24 módulos, 6 presenciais (hands-on de ecocardiograma);"
- Por: "24 módulos, 6 presenciais, 4 deles de prática de ecocardiograma (módulos 9, 13, 16 e 19), o 24 de aula prática e prova final e o 6 sem conteúdo no cronograma;"

### F2 mensagens-pos-2026-10-27-onda2.md

**Q2. Linha 48 (promessa não verificada).**
- Trocar: "\"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.\""
- Por: "\"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento.\""

**Q3. Linha 49 (reembolso em 68615).**
- Trocar: "Frase de reembolso só em 657, 289 e 333, onde a ficha diz"
- Por: "Frase de reembolso em 657, 289, 68615 e 333, onde a ficha diz"

**Q4. Linha 65 (657, fato da ficha).**
- Trocar: "As aulas práticas não são transmitidas nem gravadas."
- Por: "As aulas práticas não são transmitidas nem disponibilizadas depois."

**Q5. Linha 73 (657, bombas de infusão).**
- Trocar: "Nos módulos presenciais, a prática é guiada, com ventiladores, monitores e bombas de infusão na mão."
- Por: "Nos módulos presenciais, a prática é guiada, com ventiladores e monitores hemodinâmicos na mão e execução de TIVA e TCI."

**Q6. Linha 74 (657, investimento).**
- Trocar: "\"O total, as parcelas e a matrícula estão nesta página, ao lado do cronograma de cada módulo presencial. Você vê o que paga e o que vai praticar antes de decidir.\""
- Por: "\"O total, as parcelas e a matrícula estão nesta página, assim como o cronograma de cada módulo presencial. Você vê as condições e o que vai praticar antes de decidir.\""

**Q7. Linha 99 (341).**
- Trocar: "**Prática em quase todos os temas.**"
- Por: "**Prática na maioria dos temas.**"

**Q8. Linha 100 (341, "um" que conta).**
- Trocar: "Há um módulo de medicina equina baseada em evidências,"
- Por: "O cronograma inclui medicina equina baseada em evidências,"

**Q9. Linha 106 (341, afirmação fora da ficha).**
- Trocar: "do paciente crítico à podologia. A teoria vem antes da prática em cada sistema.\""
- Por: "do paciente crítico à podologia.\""

**Q10. Linha 108 (341, investimento).**
- Trocar: "\"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.\" (Mesma resposta"
- Por: "\"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento.\" (Mesma resposta"

**Q11. Linha 127 (289, mensagem central).**
- Trocar: "> Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância."
- Por: "> Cardiologia veterinária da fisiologia ao laudo, com ecocardiograma na prática e toda a teoria acompanhada a distância."

**Q12. Linha 140 (289, número por extenso).**
- Trocar: "o guia de decisão da área mostra os dois caminhos lado a lado."
- Por: "o guia de decisão da área mostra os caminhos lado a lado."

**Q13. Linha 158 (frase-ponte 68615 x 333).**
- Trocar: "> \"A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes."
- Por: "> \"A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório."
- O resto da frase ("A Pós-graduação em Citopatologia Veterinária é centrada na leitura de lâminas... A escolha depende do trabalho que você quer fazer na rotina.\"") fica igual.

**Q14. Linha 177 (68615).**
- Trocar: "**O laboratório inteiro, fase por fase.**"
- Por: "**O laboratório, fase por fase.**"

**Q15. Linha 210 (333, "um" que conta).**
- Trocar: "O curso abre com um módulo presencial de manejo"
- Por: "O curso abre com o módulo presencial de manejo"

**Q16. Linhas 57, 90, 123, 168 e 201 (auditoria 02: alternativa real por turma, pedida pela C23 do F0).** Acrescentar no fim de cada bloco "Notas internas":
- Linha 57 (657): " Alternativa real [SUPOSIÇÃO, contexto da linha]: seguir só com a rotina do centro cirúrgico, cursos curtos e congressos, ou aprender com um colega anestesista."
- Linha 90 (341): " Alternativa real [SUPOSIÇÃO, contexto da linha]: seguir aprendendo a campo com um colega de equinos, ou cursos curtos e congressos."
- Linha 123 (289): " Alternativa real [SUPOSIÇÃO, contexto da linha]: fazer só a formação de exame (Ecocardiografia, 698) ou cursos curtos de eletrocardiograma, ou adiar a especialização."
- Linha 168 (68615): " Alternativa real [SUPOSIÇÃO, contexto da linha]: aprender na rotina de um laboratório com um colega, fazer só a Hematologia (68608) ou adiar a especialização."
- Linha 201 (333): " Alternativa real [SUPOSIÇÃO, contexto da linha]: aprender a ler lâminas com um patologista na rotina, conteúdo gratuito e congressos, ou adiar a especialização."

### F3 landing-page-pos-2026-10-27-onda2.md

**Q17. Linha 38 (chamada principal).**
- Trocar: "8. **Chamada principal única por página:** \"Quero me inscrever\" (formulário)."
- Por: "8. **Chamada principal única por página:** \"Quero receber o retorno do time\" (formulário), o mesmo texto no hero, no formulário e no `cta_final` (braço de controle do F5)."

**Q18. Linha 72 (657, `matriz`).**
- Trocar: "| matriz | sim | dado. Ver pedido OB1 sobre frases de resultado clínico no cronograma |"
- Por: "| matriz | **só depois da correção** | dado. O cronograma da ficha traz \"elevando drasticamente as taxas de retorno à circulação espontânea\" e \"a decisão do anestesista dita a sobrevivência\": a página de 657 só é publicada com essas frases corrigidas no dado (OB1, item 6) |"

**Q19. Linha 93 (657, nome do curso).**
- Trocar: "A Faculdade Ufape oferece a pós-graduação em anestesiologia avançada veterinária em formato semipresencial."
- Por: "A Faculdade Ufape oferece a Pós-graduação em Anestesiologia Avançada em formato semipresencial, voltada à anestesia veterinária de pacientes de risco."

**Q20. Linha 99 (657).**
- Trocar: "As aulas práticas não são transmitidas nem gravadas."
- Por: "As aulas práticas não são transmitidas nem disponibilizadas depois."

**Q21. Linhas 105, 221, 341, 462 e 585 (`investimento`, as 5 turmas).**
- Trocar: "> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente."
- Por: "> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."

**Q22. Linha 110 (657, FAQ).**
- Trocar: "Nos módulos presenciais, a prática é guiada, com ventiladores, monitores e bombas de infusão na mão."
- Por: "Nos módulos presenciais, a prática é guiada, com ventiladores e monitores hemodinâmicos na mão e execução de TIVA e TCI."

**Q23. Linha 116 (657, FAQ de investimento).**
- Trocar: "> O total, as parcelas e a matrícula estão nesta página, ao lado do cronograma de cada módulo presencial. Você vê o que paga e o que vai praticar antes de decidir."
- Por: "> O total, as parcelas e a matrícula estão nesta página, assim como o cronograma de cada módulo presencial. Você vê as condições e o que vai praticar antes de decidir."

**Q24. Linhas 232, 355, 479 e 602 (FAQ de investimento de 341, 289, 68615 e 333).**
- Trocar: "> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente."
- Por: "> O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."

**Q25. Botões e checklist (linhas 126, 133, 244, 250, 366, 373, 491, 497, 614, 620, 676 e 677).**
- Linhas 126, 133, 244, 250, 366, 373, 491, 497, 614 e 620, trocar: "- botao: Quero me inscrever"
- Por: "- botao: Quero receber o retorno do time"
- Linha 676, trocar: "botão \"Quero me inscrever\" visível sem rolar" por: "botão \"Quero receber o retorno do time\" visível sem rolar"
- Linha 677, trocar: "(\"Quero me inscrever\", rola até o formulário)" por: "(\"Quero receber o retorno do time\", rola até o formulário)"

**Q26. Frase de apoio do formulário (linhas 127, 245, 367, 492 e 615) e apoio do `cta_final` (linhas 134, 251, 374, 498 e 621): passam a ser os do F5.**
- Linhas 127, 245, 367, 492 e 615, trocar: "- frase de apoio: Deixe seus dados e o time de vendas retorna para tirar suas dúvidas e orientar a inscrição. Usamos seus dados só para esse contato, conforme a política de privacidade."
- Por, em cada turma:
  - 657 (linha 127): "- frase de apoio: Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, os módulos de prática guiada e as condições da turma, e orientar a inscrição. Abaixo do botão: frase de risco, finalidade e link da política do F5, seção 0.3."
  - 341 (linha 245): "- frase de apoio: Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre os sistemas, os módulos práticos e as condições da turma, e orientar a inscrição. Abaixo do botão: frase de risco, finalidade e link da política do F5, seção 0.3."
  - 289 (linha 367): "- frase de apoio: Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma, a teoria a distância, os módulos práticos e as condições da turma, e orientar a inscrição. Abaixo do botão: frase de risco, finalidade e link da política do F5, seção 0.3."
  - 68615 (linha 492): "- frase de apoio: Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma do laboratório clínico e as condições da turma, e orientar a inscrição. Abaixo do botão: frase de risco, finalidade e link da política do F5, seção 0.3."
  - 333 (linha 615): "- frase de apoio: Deixe seus dados e o time de vendas retorna pelo WhatsApp para responder suas dúvidas sobre o cronograma de leitura de lâminas e as condições da turma, e orientar a inscrição. Abaixo do botão: frase de risco, finalidade e link da política do F5, seção 0.3."
- Linhas 134, 251, 374, 498 e 621, trocar o texto depois de "- apoio (opcional): " pelo "Apoio" do F5 da mesma turma, literal:
  - 657 (linha 134): "Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre os módulos de prática guiada e as condições. Enviar seus dados não gera cobrança."
  - 341 (linha 251): "Viu os sistemas e os módulos práticos? Deixe seus dados e o time de vendas responde suas dúvidas e orienta a inscrição. Enviar seus dados não gera cobrança."
  - 289 (linha 374): "Viu o cronograma? Deixe seus dados e o time de vendas responde suas dúvidas sobre a teoria a distância e os módulos práticos. Enviar seus dados não gera cobrança."
  - 68615 (linha 498): "Viu o cronograma? Em dúvida entre patologia clínica e citopatologia, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança."
  - 333 (linha 621): "Viu o cronograma? Em dúvida entre citopatologia e patologia clínica, o time de vendas explica a diferença. Deixe seus dados. Enviar seus dados não gera cobrança."

**Q27. Linha 210 (341, `sobre`).**
- Trocar: "**Prática em quase todos os temas.**"
- Por: "**Prática na maioria dos temas.**"
- Trocar: "Há um módulo de medicina equina baseada em evidências,"
- Por: "O cronograma inclui medicina equina baseada em evidências,"

**Q28. Linha 226 (341, FAQ).**
- Trocar: "do paciente crítico à podologia. A teoria vem antes da prática em cada sistema."
- Por: "do paciente crítico à podologia."

**Q29. Linha 323 (289, subtítulo).**
- Trocar: "- subtitulo (150 caracteres): Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância."
- Por: "- subtitulo (118 caracteres): Cardiologia veterinária da fisiologia ao laudo, com ecocardiograma na prática e toda a teoria acompanhada a distância."

**Q30. Linha 327 (289, `sobre`).**
- Trocar: "> Cardiologia veterinária de cães e gatos da fisiologia ao laudo, com ecocardiograma na mão nos módulos práticos e toda a teoria acompanhada a distância."
- Por: "> Cardiologia veterinária da fisiologia ao laudo, com ecocardiograma na prática e toda a teoria acompanhada a distância."

**Q31. Linha 349 (289, número por extenso).**
- Trocar: "o guia de decisão da área mostra os dois caminhos lado a lado."
- Por: "o guia de decisão da área mostra os caminhos lado a lado."

**Q32. Linha 445 (68615, nome do curso).**
- Trocar: "A Faculdade Ufape oferece a pós-graduação em patologia clínica veterinária em formato semipresencial, com foco no laboratório clínico."
- Por: "A Faculdade Ufape oferece a Pós-graduação em Patologia Clínica em formato semipresencial, com foco no laboratório clínico veterinário."

**Q33. Linha 449 (68615).**
- Trocar: "**O laboratório inteiro, fase por fase.**"
- Por: "**O laboratório, fase por fase.**"

**Q34. Linha 470 (68615, frase-ponte).**
- Trocar: "> A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes."
- Por: "> A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório."

**Q35. Linha 573 (333, "um" que conta).**
- Trocar: "O curso abre com um módulo presencial de manejo"
- Por: "O curso abre com o módulo presencial de manejo"

**Q36. Linha 590 (333, frase-ponte).**
- Trocar: "> A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes."
- Por: "> A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório."

**Q37. Linha 485 (nota de reembolso em 68615).**
- Trocar: "Incluída aqui por ter fonte na ficha [CONFIRMAR com o qa e a secretaria];"
- Por: "Incluída aqui por ter fonte na ficha (conferida pelo qa na revisão F13a: ficha de 68615, Considerações); o alcance de \"valores de inscrição\" fica [CONFIRMAR com a secretaria];"

**Q38. Listas OB1 (linhas 152, 273, 391, 517, 640 e 650).** Acrescentar ao fim de cada lista os itens novos da seção 5 desta revisão (marcados "novo"), com o mesmo texto. Na linha 650 (tabela do OB1, "O que"), acrescentar no fim: "; e os itens comuns novos da revisão F13a: valor da matrícula e da inscrição conferido (U11), condição da 1ª mensalidade junto do investimento, decisão sobre o botão COMPRAR da página e link da política de privacidade no formulário".

### F4 seo-on-page-pos-2026-10-27-onda2.md

**Q39. Linha 35 (regra 6).**
- Trocar: "\"Veterinária\" aparece no título e na resposta citável de 657 e de 68615, como pede a F1 (o nome do catálogo não a traz); nos outros dois, o nome já a traz. Isso é palavra de SEO, não troca o nome do catálogo, que continua no H1 e nos dados [SUPOSIÇÃO: escolha deste agente, sobre a regra da seção 2.4 da F1]."
- Por: "Em 657 e 68615 o nome do catálogo não traz \"veterinária\": o nome fica exatamente como no catálogo em todo campo, e a palavra entra fora do nome (\"anestesia veterinária\", \"laboratório clínico veterinário\", \"para veterinários\"), como pede a F1 (\"sem trocar o nome do catálogo\"; correção do qa na revisão F13a)."

**Q40. Linhas 49 e 51 (657, `titulo_seo`).**
- Linha 49, trocar: "> Pós-graduação em Anestesiologia Avançada Veterinária | Ufape"
- Por: "> Pós-graduação em Anestesiologia Avançada | Ufape"
- Linha 47, trocar "(60 caracteres, limite 60)" por "(48 caracteres, limite 60)".
- Linha 51, trocar: "Está no limite. Se o validador contar diferente, a versão de reserva é a mesma sem a marca: \"Pós-graduação em Anestesiologia Avançada Veterinária\" (52 caracteres)."
- Por: "O nome fica igual ao do catálogo; \"veterinária\" vai na descrição e na resposta citável."

**Q41. Linhas 53 e 55 (657, `descricao_seo`).**
- Linha 53, trocar: "(151 caracteres, limite 155; recontado por script pelo orquestrador)" por "(147 caracteres, limite 155; contagem do qa, a recontar por script)".
- Linha 55, trocar: "> Pós-graduação em anestesiologia avançada veterinária semipresencial: hemodinâmica, ventilação do paciente especial e prática guiada. Veja o cronograma."
- Por: "> Pós-graduação em Anestesiologia Avançada, semipresencial: anestesia veterinária com hemodinâmica, ventilação do paciente especial e prática guiada."

**Q42. Linhas 57, 59 e 61 (657, `resposta_citavel`).**
- Linha 57, trocar "(55 palavras, faixa de 40 a 60)" por "(54 palavras, faixa de 40 a 60)".
- Linha 59, trocar: "> A pós-graduação em anestesiologia avançada veterinária da Faculdade Ufape é um curso semipresencial que leva a anestesia do protocolo à anestesia de precisão. O programa trata de fisiologia aplicada, hemodinâmica, ventilação do paciente especial, bloqueio neuromuscular e coagulação, com prática presencial guiada. É pensado para quem quer aprofundar a decisão crítica em pacientes de risco."
- Por: "> A Pós-graduação em Anestesiologia Avançada da Faculdade Ufape é um curso semipresencial de anestesia veterinária que leva a anestesia do protocolo à anestesia de precisão. O programa trata de fisiologia aplicada, hemodinâmica, ventilação do paciente especial, bloqueio neuromuscular e coagulação, com prática presencial guiada. O foco é a decisão crítica em pacientes de risco."
- Linha 61, trocar: "\"Quem quer aprofundar a decisão crítica\" descreve o motivo do curso, não um requisito. A frase \"para quem\" fica assim até a Ufape escrever o pré-requisito real."
- Por: "Nenhuma frase descreve público (U10): \"O foco é a decisão crítica\" fala do curso, não de quem entra."

**Q43. Linhas 73, 75 e 86 (657, `descricao_schema` e JSON-LD).**
- Linha 73, trocar "(249 caracteres, limite 300)" por "(260 caracteres, limite 300)".
- Linhas 75 e 86, trocar: "Pós-graduação semipresencial em Anestesiologia Avançada Veterinária da Faculdade Ufape. Da anestesia de protocolo à anestesia de precisão:"
- Por: "Pós-graduação em Anestesiologia Avançada da Faculdade Ufape, semipresencial. Anestesia veterinária da anestesia de protocolo à anestesia de precisão:"
- O resto ("fisiologia aplicada, hemodinâmica, ventilação, bloqueio neuromuscular, coagulação e prática presencial guiada.") fica igual.

**Q44. Linha 95 (657, `about`; recomendada).**
- Trocar: "{ \"@type\": \"Thing\", \"name\": \"anestesiologia veterinária\" },"
- Por: "{ \"@type\": \"Thing\", \"name\": \"anestesiologia avançada\" },"
- Motivo: o termo genérico é da página de 68609 (F1, seção 3; regra do próprio F4, seção 6.2).

**Q45. Linha 132 (657, FAQPage).**
- Trocar: "Nos módulos presenciais, a prática é guiada, com ventiladores, monitores e bombas de infusão na mão."
- Por: "Nos módulos presenciais, a prática é guiada, com ventiladores e monitores hemodinâmicos na mão e execução de TIVA e TCI."

**Q46. Linha 148 (657, FAQPage).**
- Trocar: "\"text\": \"O total, as parcelas e a matrícula estão nesta página, ao lado do cronograma de cada módulo presencial. Você vê o que paga e o que vai praticar antes de decidir.\""
- Por: "\"text\": \"O total, as parcelas e a matrícula estão nesta página, assim como o cronograma de cada módulo presencial. Você vê as condições e o que vai praticar antes de decidir.\""

**Q47. Linha 256 (341, FAQPage).**
- Trocar: "do paciente crítico à podologia. A teoria vem antes da prática em cada sistema.\""
- Por: "do paciente crítico à podologia.\""

**Q48. Linhas 272, 406, 546 e 686 (FAQPage de investimento de 341, 289, 68615 e 333).**
- Trocar: "\"text\": \"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento. Você decide com a conta inteira na frente.\""
- Por: "\"text\": \"O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento.\""

**Q49. Linhas 433 e 435 (68615, `titulo_seo`).**
- Linha 433, trocar "(54 caracteres, limite 60)" por "(60 caracteres, limite 60; reserva sem \"para veterinários\": 42)".
- Linha 435, trocar: "> Pós-graduação em Patologia Clínica Veterinária | Ufape"
- Por: "> Pós-graduação em Patologia Clínica para veterinários | Ufape"
- Se o script contar mais de 60, usar a reserva: "> Pós-graduação em Patologia Clínica | Ufape".

**Q50. Linhas 437 e 439 (68615, `descricao_seo`).**
- Linha 437, trocar "(135 caracteres, limite 155)" por "(136 caracteres, limite 155)".
- Linha 439, trocar: "> Pós-graduação em patologia clínica veterinária semipresencial: o laboratório clínico do pré-analítico ao laudo, com prática presencial."
- Por: "> Pós-graduação em Patologia Clínica, semipresencial: o laboratório clínico veterinário do pré-analítico ao laudo, com prática presencial."

**Q51. Linha 443 (68615, `resposta_citavel`; segue com 52 palavras).**
- Trocar: "> A pós-graduação em patologia clínica veterinária da Faculdade Ufape é um curso semipresencial com foco no laboratório clínico: do pré-analítico ao laudo,"
- Por: "> A Pós-graduação em Patologia Clínica da Faculdade Ufape é um curso semipresencial com foco no laboratório clínico veterinário: do pré-analítico ao laudo,"

**Q52. Linhas 455, 457 e 468 (68615, `descricao_schema` e JSON-LD).**
- Linha 455, trocar "(268 caracteres, limite 300)" por "(269 caracteres, limite 300)".
- Linhas 457 e 468, trocar: "Pós-graduação semipresencial em Patologia Clínica Veterinária da Faculdade Ufape. O laboratório clínico do pré-analítico ao laudo:"
- Por: "Pós-graduação em Patologia Clínica da Faculdade Ufape, semipresencial. O laboratório clínico veterinário do pré-analítico ao laudo:"

**Q53. Linhas 522 e 654 (frase-ponte no FAQPage de 68615 e 333).**
- Trocar: "A Pós-graduação em Patologia Clínica cobre o laboratório clínico inteiro, do pré-analítico ao laudo, e tem a citologia como uma das partes."
- Por: "A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório."

**Q54. Linhas 713 e 716 (tabela de contagens).**
- Linha 713, trocar: "| 657 | 60 | 152 | 55 | 249 |" por "| 657 | 48 | 147 | 54 | 260 |"
- Linha 716, trocar: "| 68615 | 54 | 135 | 52 | 268 |" por "| 68615 | 60 | 136 | 52 | 269 |"
- Linha 719, trocar: "Só o título de 657 está no limite exato." por "Só o título de 68615 está no limite exato (reserva de 42 caracteres na seção 4.1). Contagens de 657 e 68615 feitas à mão pelo qa: recontar por script."

**Q55. Linha 723 (289 x 68605).**
- Trocar: "O título de 289 é igual ao que a turma 68605 (Cardiologia, São Paulo, status \"verificar\", não divulgada) teria se usasse o mesmo padrão. Enquanto 68605 não estiver à venda, não há duas páginas disputando; quando reabrir, a F1 manda decidir canonical ou 301 pela regra T3, e o título dela leva outro diferencial [SUPOSIÇÃO]."
- Por: "O título de 289 é igual ao que a turma 68605 (Cardiologia, São Paulo) teria no mesmo padrão. O catálogo marca 68605 como \"verificar (turma já iniciada e com venda)\": a página dela está no ar e vende, então as duas páginas disputam a consulta \"pós-graduação em cardiologia veterinária\". Chamado proposto: com a CP1 aprovada, a cidade entra no título das duas; sem a CP1, a página de 68605 sai de venda depois do 3º módulo (decisão 18) e recebe 301 para a próxima turma de Cardiologia de São Paulo ou para a página do curso [CONFIRMAR com o time do site]."

### F5 otimizador-de-cta-pos-2026-10-27-onda2.md

**Q56. Linha 73 (lead sem aceite).**
- Trocar: "O retorno do time de vendas pedido no formulário não depende de nenhuma das duas caixas."
- Por: "O retorno do time de vendas pedido no formulário não depende de nenhuma das duas caixas. Quem não marca uma caixa recebe só o retorno pedido e não entra nas listas de campanha (S2 e S3) daquele canal (encomenda F10)."

**Q57. Linha 81 (mensagem de erro).**
- Trocar: "> Não conseguimos enviar seus dados agora. Tente de novo ou fale com a secretaria pelo WhatsApp desta página."
- Por: "> Não conseguimos enviar seus dados agora. Tente de novo ou fale com o time pelo WhatsApp desta página."
- Motivo: o botão de WhatsApp da página é o de vendas da praça (F3 e F5, seção 0.1, item 6), não o da secretaria.

**Q58. Linhas 101 e 110 (braço V2).**
- Linha 101, trocar: "| V2 | Quero me inscrever | 18 | é o texto provisório da F3, com a palavra de intenção |"
- Por: "| V2 | Quero me inscrever | 18 | suspenso: só entra no teste se o clique levar à inscrição de fato; com o formulário de contato, promete mais do que entrega (conformidade, página de destino) [CONFIRMAR com o time do site] |"
- Linha 110, trocar: "com divisão igual entre C, V1 e V2," por: "com divisão igual entre C e V1 (V2 suspenso, seção 0.4),"

**Q59. Linhas 195, 255, 315, 375 e 435 (cartões do V2).**
- Trocar: "**V2: \"Quero me inscrever\" (18 caracteres)**"
- Por: "**V2: \"Quero me inscrever\" (18 caracteres), suspenso até a confirmação da seção 0.4**"

**Sem troca de texto, trava registrada (F5):** endereço da política de privacidade (linha 91) [CONFIRMAR]; campo "Título" do formulário e "Apoio" do `cta_final` fora dos campos do template [CONFIRMAR com a plataforma]; frase de risco e "Nenhuma cobrança foi feita" (linhas 85 e 130) só com o time do site confirmando que o formulário não cobra.

---

## 5. Pedido OB1 completo por turma (o que corrigir no site no ar)

Junta as listas da F3 (seções 1.6, 2.6, 3.6, 4.6 e 5.6) com os itens que esta revisão achou nas fichas. Item "novo" é acréscimo do qa. Nenhum item muda o texto da squad; todos são ação humana no site, depois da aprovação.

### 5.1 Itens comuns às 5 páginas

1. "CERTIFICADO PELO MEC": remover; `certificacao` oculta até o texto da regulação.
2. Turma mínima de 20: trocar para 15 (decisão 11, A12) ou deixar só o aviso sem número.
3. Regra do 3º módulo como dado da turma, com a data e a redação final depois de OU6 (decisão 18, OU14); em 333 só depois de OU3.
4. Bloco "Documentos para matrícula (MEC e UFAPE)": a regulação diz se o título fica [CONFIRMAR].
5. (novo) Valor da matrícula do site (R$ 250,00) conferido contra o valor da inscrição informado pelo CEO (R$ 260,00) antes de publicar (U11, decisão 16): o dado de `investimento` mostra o valor certo.
6. (novo) Condição da 1ª mensalidade (paga até 30 dias antes do início, fichas) visível junto de total, parcelas e matrícula no `investimento` (CDC: condições completas).
7. (novo) Botão "COMPRAR" da página atual: decidir se fica ao lado do formulário. Se ficar, vira chamada secundária e o formulário continua como a principal (auditoria 08: uma chamada principal) [CONFIRMAR].
8. (novo) Formulário com o link da política de privacidade e com o aviso de cookies do pixel e das tags, antes da subida de 07/12 [CONFIRMAR endereço].
9. (novo) Bloco "Parceiros e patrocinadores" vazio nas 5 fichas: ocultar.
10. Versão anterior de cada página exportada antes da troca (como desfazer).

### 5.2 657 Pós-graduação em Anestesiologia Avançada

1. a 4. Itens comuns 1 a 4.
5. Convite "Tem interesse em prestar a prova de Especialista em Anestesiologia? Clique aqui": retirar ou passar pela regulação [CONFIRMAR].
6. Público-alvo "exclusiva para médicos veterinários anestesistas já atuantes": a Ufape escreve o pré-requisito real ou retira (U10).
7. Frases de resultado clínico e superlativos para a regulação (o cronograma é dado visível, então a página só sai com elas corrigidas): "Reduzir complicações e mortalidade perioperatória", "com maestria", "profissionais diferenciados", "elevando drasticamente as taxas de retorno à circulação espontânea", "a decisão do anestesista dita a sobrevivência", "máxima segurança e previsibilidade"; (novo) "garantir maior segurança assistencial", "Se diferenciar no mercado com expertise real e prática" e "mercado crescente de animais silvestres e exóticos".
8. "Prova de recuperação (Prova cobrada separadamente)" sem valor: a Ufape informa o valor ou a regra e ele aparece como dado [CONFIRMAR]. Sem isso, a página de 657 não sai.
9. Docente listada duas vezes com grafias diferentes (Dra. Mayara Travalini de Lima e Profa. Mayara Travalini): uniformizar no dado.
10. (novo) Nome do programa no texto ("Programa Avançado em Anestesiologia Veterinária da Faculdade Ufape"): trocar por "Pós-graduação em Anestesiologia Avançada".
11. (novo) "Aula dada por instrutor RECOVER": marca de terceiro; a Ufape documenta a credencial ou retira [CONFIRMAR].
12. Itens comuns 5 a 10.

### 5.3 341 Pós-graduação em Medicina Interna Equina

1. a 4. Itens comuns 1 a 4.
5. Promoção "20% DE DESCONTO EM TODO O CURSO" com a regra cortada, também no campo de preço do catálogo: regra completa (quem, quando, até quando, se acumula) ou retirada (OU10).
6. Segundo local ("Pressa. Português: Ermênio de Oliveira Penteado... Indaiatuba") com o texto quebrado e "as aulas práticas serão realizadas no EQUIPAMENTO HOSPITAL VETERINÁRIO": a Ufape diz onde acontece cada módulo presencial (OU11).
7. Módulos marcados "ONLINE PRESENCIAL" (o 3º e outros): dizer o formato de cada um (OU11).
8. "possibilidade de descontos e bolsas de estudo": retirar (decisão 14).
9. "veterinários formados com pouca experiência prática e, consequentemente, inseguros e sem nenhum diferencial competitivo": reescrever.
10. "corpo docente de excelência" e "conteúdo inovador": retirar ou documentar.
11. Reembolso truncado e contraditório ("Solicitados, serão solicitados reembolsos de valores de inscrição, apenas se a turma for confirmada"): reescrever com a regra clara [CONFIRMAR].
12. Data do 3º módulo em feriado nacional (01/05/2027, OU17): a Ufape confirma.
13. Nome padrão "Pós-graduação em Medicina Interna Equina" (a ficha traz "Pós Graduação" e "Pós-Graduação/Especialização").
14. (novo) "objetivando especialistas formando em medicina equina": sugere título de especialista; passar pela regulação.
15. (novo) Erros no cronograma e no texto: "águas gestantes" (éguas), "Reanimação cardiopulmonar em vasos críticos" (o tema certo [CONFIRMAR]), "COMPLEMETARES", "comun acordo", "inico", "sigulrmente": corrigir no dado.
16. Itens comuns 5 a 10.

### 5.4 289 Pós-graduação em Cardiologia Veterinária

1. a 4. Itens comuns 1 a 4.
5. Bloco "PROVA DE BOLSA: Tem interesse em prestar a prova de bolsa? Clique aqui": retirar (decisão 14).
6. "opções diagnósticas de ponta" e "atendimento cardiológico de excelência": retirar ou documentar.
7. Erros no cronograma: "Ecocargiograma", "Afeccções", aspas abertas no módulo 22; (novo) "cardiovascula", "Taquiarritimias", "Bradiarritimias", "Neoplásia", "Sindrome Cardio-renal".
8. Descrever o conteúdo de cardiologia equina e de pets não convencionais (módulos 22 e 23).
9. (novo) Módulo 6 marcado PRESENCIAL sem conteúdo no cronograma: completar no dado.
10. (novo) Nome "A Pós-Graduação Lato Sensu em Cardiologia Veterinária" no texto: padrão "Pós-graduação em Cardiologia Veterinária".
11. (novo) Contato e endereço de documentos: a página manda para secretaria@intercursos.com.br e para um endereço de São Paulo, enquanto o contexto geral traz duvidas@intercursos.com.br e a turma é de Goiânia: a Ufape confirma [CONFIRMAR].
12. Itens comuns 5 a 10.

### 5.5 68615 Pós-graduação em Patologia Clínica

1. a 4. Itens comuns 1 a 4.
5. "Este curso de pós-graduação tem reconhecimento pelo Ministério da Educação (MEC) o que comprova a qualidade do ensino oferecido pela instituição que é referência nacional em educação": retirar inteira.
6. Bloco "PROVA DE BOLSA": retirar (decisão 14).
7. Aviso de passagem e hotel ausente: incluir (regra da linha).
8. CEP 01428-001 diferente das outras páginas de São Paulo (01407-100): confirmar (OU13).
9. "O curso garante além de embasamento teórico simulações de habilidades": retirar "garante".
10. Erros no cronograma ("regulameno", "sedmentoscopia"): corrigir no dado.
11. (novo) Endereço da página fora do padrão (/produto/68615/pos-graduacao-patologia-clinica/sao-paulo, sem "-em-"): a página nova usa pos-graduacao-em-patologia-clinica e a antiga recebe 301 [CONFIRMAR com o time do site].
12. Itens comuns 5 a 10.

### 5.6 333 Pós-graduação em Citopatologia Veterinária

1. a 4. Itens comuns 1 a 4 (item 3 só depois de OU3).
5. Coordenação "UFAPE" e uma só professora listada: coordenação e corpo docente reais (OU12); até lá, `docentes` sem o rótulo de coordenação.
6. "oportunidade única", "eleva o nível de excelência", "contribui para o avanço da ciência", "o que há de mais recente nas descobertas científicas", "oportunidade valiosa para quem busca se destacar": retirar ou documentar.
7. Módulo 1 presencial em Sábado de Aleluia e Páscoa (27 e 28/03/2027) sem reposição conhecida: OU3 e OU17.
8. Erros no cronograma ("masculine", "Experiência práticas citopatológicas"): corrigir no dado.
9. Nome padrão "Pós-graduação em Citopatologia Veterinária" (a ficha traz "Pós Graduação").
10. Itens comuns 5 a 10.

---

## 6. Travas de publicação (não bloqueiam o texto, bloqueiam a página no ar)

| Trava | Turmas | Quem destrava |
|---|---|---|
| Link da política de privacidade e aviso de cookies no formulário | as 5 | Ufape (endereço) e time do site |
| OB1 aprovado e feito no site | as 5 | pessoa do marketing; regulação nos itens de certificação |
| U11 (valor da inscrição x matrícula) | as 5 | Ufape |
| Prova de recuperação com valor no dado e cronograma sem frases de resultado clínico | 657 | Ufape e regulação |
| U10 (pré-requisito; `para_quem` segue oculta até lá) | 657 | Ufape |
| OU10 e OU11 (promoção, local e formato dos módulos; `local_e_datas` só depois) | 341 | Ufape |
| OU13 (CEP) | 68615 | Ufape |
| OU12 (docentes sem rótulo de coordenação) | 333 | Ufape e plataforma |
| Guia A2 publicado, ou a última frase da resposta sai | 289 | Ufape e editor |
| Confirmação de que o formulário não cobra (frase de risco) | as 5 | time do site |
| Campos "Título" do formulário e "Apoio" do `cta_final` aceitos pela plataforma | as 5 | plataforma |
| Conferência de 04/12 (destino, UTM, política, lead no CRM) | as 5 | humano; gestor-de-midia confere |

---

## 7. auditorias/conformidade-educacional.md, item por item (5 arquivos)

| Item | Resultado | Onde e o que muda |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | **falha** | F4: "Pós-graduação em Anestesiologia Avançada Veterinária" e "Pós-graduação em Patologia Clínica Veterinária" em título e schema; F3: nome alterado no `sobre` de 657 e 68615 (Q19, Q32, Q39 a Q43, Q49 a Q52). Modalidade, CH e turma só como dado: atendem |
| Curso com status "aberto" | atende | as 5 "aberto" (catálogo, linhas 74 a 78) |
| Modalidade clara e correta | atende | semipresencial; teoria online e presencial nos módulos práticos, como nas fichas |
| Graduação: ato regulatório | não se aplica | linha pos |
| Pós lato sensu sem "reconhecida pelo MEC" | atende | `certificacao` oculta nas 5; nenhum "MEC" em texto; frases das páginas no ar no OB1 |
| Curso livre: não confere diploma | não se aplica | |
| Nota MEC só com fonte e ano | atende | nenhuma nota |
| Nenhuma promessa de emprego, salário, promoção, aprovação ou sucesso | **falha** | texto da squad atende, mas a `matriz` de 657, que é dado visível, traz "elevando drasticamente as taxas de retorno à circulação espontânea" e "a decisão do anestesista dita a sobrevivência" (Q18 e OB1 657, item 7) |
| Empregabilidade ou satisfação com fonte | não se aplica | nenhum dado desse tipo |
| Superlativos só com fonte | **falha** | "o laboratório clínico inteiro" e "O laboratório inteiro" (68615) e "Prática em quase todos os temas" (341), sem base na ficha (Q7, Q13, Q14, Q27, Q33, Q34, Q36, Q53); superlativos das fichas fora do texto e listados no OB1 |
| Comparação com concorrente objetiva | atende | nenhuma; 68615 x 333 é comparação interna, corrigida para não insinuar que uma contém a outra |
| Preço com valor, parcelas e condições completas | **falha** | "Você decide com a conta inteira na frente" e "Você vê o que paga" sem verificação (657 com prova cobrada à parte; U11) (Q2, Q6, Q10, Q21, Q23, Q24, Q46, Q48); 1ª mensalidade e U11 no OB1 comum |
| Bolsa e desconto com regra, público e prazo | atende | nenhuma bolsa, desconto ou promoção; 341 com `diferenciais` oculta e `offers` só com dado limpo |
| Urgência real | atende | nenhuma; regra do 3º módulo só como dado |
| Prouni, Fies ou financiamento | não se aplica | |
| Autorização de imagem, voz e depoimento | atende | docentes só como dado (decisões 8 e 10); `depoimentos` oculta; imagem do acervo, escolha do editor |
| Menores de idade | não se aplica | |
| Formulário com finalidade e link da política | **falha** | finalidade escrita no F5; link "[CONFIRMAR]"; a frase da F3 ("só para esse contato") contradiz o aceite (Q26); trava da seção 6 |
| WhatsApp e e-mail só com consentimento e saída fácil | atende com correção | caixas por canal, desmarcadas, SAIR e descadastro; Q56 diz que quem não marca não entra nas listas |
| Nenhum dado pessoal | atende | |
| Anúncios dentro das políticas da Meta e do Google | não se aplica | nenhum anúncio neste lote |
| Página entrega o que a peça promete | **falha** | botão "Quero me inscrever" (F3 e V2 do F5) leva a um formulário de contato (Q17, Q25, Q58, Q59); "bombas de infusão na mão" e "nem gravadas" em 657 sem base na ficha (Q4, Q5, Q20, Q22, Q45); "A teoria vem antes da prática" em 341 (Q9, Q28, Q47); "ecocardiograma na mão nos módulos práticos" e "de cães e gatos" em 289 (Q11, Q29, Q30) |
| Anúncios: característica pessoal, urgência falsa, pessoa pública, caixa alta, driblar análise | não se aplica | nenhum anúncio |
| Página de destino com dados da Ufape, contato e política | **falha até a trava** | política [CONFIRMAR]; contatos oficiais no checklist da F3 (7.2) |

**Resultado:** Aprovado ( ) Bloqueado (x). Itens bloqueados: nome do curso, promessa de resultado clínico no dado de 657, superlativos novos, condições de preço, formulário e política, página que entrega o que promete. Todos fecham com Q1 a Q59 mais as travas da seção 6.
**Revisado por:** qa-de-marketing (agente); humano: [pessoa do marketing, no OB1].
**Data:** 27/10/2026.

---

## 8. Auditorias dos departamentos

### 8.1 auditorias/03-busca.md (F1 e F4, com a F3)

| Item | Resultado |
|---|---|
| Uma única palavra-chave alvo por página | atende (F1, seção 1; campo `palavra_chave_principal` da F3) |
| Títulos e descrições únicos | atende entre as 5; 289 x 68605 na Q55 |
| Nenhuma página importante bloqueada para indexação | [CONFIRMAR com o time do site] |
| Nenhum link interno quebrado | pendente na publicação: âncoras 68615 e 333 e link do guia A2 (conferência de 04/12) |
| Toda página aponta para a sua página pilar | pendente: nenhum arquivo define a página pilar de cada área; os guias A1, A2, A11 e 341 fazem a ponte. Fica como chamado para o seo-tecnico [SUPOSIÇÃO de dono] |
| Conteúdo responde à pergunta principal | atende (`resposta_citavel` com o que é e para quem é, sem público em 657) |
| Correções escritas como chamados | atende com o OB1 completo (seção 5) |
| Turmas encerradas redirecionadas | atende com o pedido de 301 de 68615 (OB1 68615, item 11) e o chamado de 68605 (Q55) |
| Dados de curso batem com o catálogo | falha até Q39 a Q43 e Q49 a Q52 (nome); valores das chaves conferem |
| Resposta citável, FAQ real e marcação estruturada | atende |
| Conteúdo principal sem JavaScript | [CONFIRMAR com o time do site] |
| Nenhum resultado de IA registrado sem checagem | atende (40 perguntas "conferir manualmente") |
| Nenhuma consulta com duas páginas disputando sem correção | atende com Q55 (289 x 68605) e com a frase-ponte corrigida (68615 x 333) |

### 8.2 auditorias/08-conversao.md (F3 e F5)

| Item | Resultado |
|---|---|
| Topo passa no teste dos 5 segundos no celular | pendente na construção (checklist 7.2 da F3) |
| Uma chamada principal por página | atende com Q17 e Q25; botão "COMPRAR" no OB1 comum, item 7 |
| Formulário pede só o necessário | atende (F5, seção 0.3) |
| Provas reais e autorizadas | atende depois de Q4, Q5, Q7, Q9, Q11 (só fatos da ficha) |
| Objeções respondidas na página | atende (FAQ por turma) |
| Testes com hipótese escrita | atende (cartões do F5; V2 suspenso, Q58 e Q59) |
| Resultados registrados | previsto (desenho-de-experimentos e analise-cro) |
| Dados do curso conferidos com o catálogo | atende como dado; nome na Q19 e na Q32 |
| Eventos de lead e inscrição rastreados e lead no CRM | previsto; conferência de 04/12 |

### 8.3 auditorias/02-estrategia-e-posicionamento.md (F2)

| Item | Resultado |
|---|---|
| Uma meta principal | atende por herança do plano (15 matrículas por turma) |
| Persona e curso nomeados | atende |
| 8 canais avaliados | não se aplica (casa de mensagens) |
| Posicionamento nomeia a alternativa real | falha até a Q16 (o F0 pediu à F2 a alternativa por turma, C23) |
| Todo pilar tem prova | atende depois de Q4, Q5, Q7, Q9 e Q11 |
| Regras de voz com exemplos | pendente na Ufape; não bloqueia (como no F0) |
| Cabe no tempo e na verba | não se aplica |
| Sem promessa de emprego, aprovação ou salário | atende |
| Preços, bolsas e condições do catálogo | atende depois de Q2, Q6 e Q10 |

---

## 9. Próximo passo

1. Orquestrador aplica Q1 a Q59 com o texto exato da seção 4 e recontagem por script dos campos do F4 trocados (657 e 68615) e do subtítulo de 289. Se o título de 68615 passar de 60, vale a reserva da Q49.
2. Com as trocas feitas, as 5 páginas seguem para a aprovação humana do OB1 (pessoa do marketing), com a lista completa da seção 5 e as travas da seção 6; itens de certificação e de ato regulatório passam também pela regulação.
3. As próximas revisões do F13 (onda2b e onda2c) usam esta versão das páginas como destino: nenhuma mensagem nem post cita "conta inteira", "bombas de infusão", "de cães e gatos" (289) ou "laboratório inteiro".
4. Nada é publicado, enviado ou pago a partir destes arquivos.

---

## Fatos (com fonte)

- Nome, local, modalidade, início, turma, CH, preço e status das 5 turmas; 68605 em "verificar (turma já iniciada e com venda)"; 68609, 359, 698, 68608, 68636 e 352 abertas: contexto/catalogo-de-cursos.md, seção 2.
- 657: aulas práticas "não serão transmitidas ou disponibilizadas posteriormente"; ventiladores e monitores no módulo 8 (presencial); "bombas de infusão" no módulo 14 (online); "Prova cobrada separadamente" sem valor; frases "elevando drasticamente...", "a decisão do anestesista dita a sobrevivência", "garantir maior segurança assistencial", "Se diferenciar no mercado", "mercado crescente de animais silvestres e exóticos", "Programa Avançado em Anestesiologia Veterinária" e "instrutor RECOVER": ficha de 657.
- 341: "treinamentos práticos e demonstrativos na maioria dos temas"; módulos "ONLINE PRESENCIAL"; neonatologia só online; "objetivando especialistas formando"; erros de digitação citados; reembolso truncado: ficha de 341.
- 289: presenciais 6 (sem conteúdo), 9, 13, 16, 19 (ecocardiograma) e 24 (aula prática e prova final); módulos 22 (cardiologia equina) e 23 (pets não convencionais); "Pós-Graduação Lato Sensu"; secretaria@intercursos.com.br e endereço de São Paulo para documentos: ficha de 289.
- 68615: reembolso dos valores de inscrição só se a turma não for confirmada; sem aviso de passagem e hotel; URL sem "-em-": ficha de 68615.
- 333: presenciais 1, 5, 10, 12, 13 e 20, com leitura de lâminas em 5, 10 e 20: ficha de 333.
- Orientação de comprar passagem e hotel só com a turma confirmada: contexto/pos-graduacao.md (turma mínima).
- Inscrição de R$ 260,00 informada pelo CEO contra matrícula de R$ 250,00 do site, U11: docs/execucao-2026-10-26.md, decisão 16.
- Regras do texto da IA, campos de `formulario` e `cta_final` e ordem do tipo pos: templates/pagina-da-turma.md.
- Alternativa real pedida à F2 (C23) e regras do plano: saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2.md e cmo-pos-2026-10-27-onda2.md (v2).
- Contatos oficiais (duvidas@intercursos.com.br; vendas por praça): contexto/ufape-geral.md.

## [SUPOSIÇÃO]

- O validador da plataforma trata "um" e "uma" como artigo; onde contam, foram trocados.
- "Ecocardiografia" uma vez como nome de módulo não toma a palavra-alvo da página de 698.
- Os textos das alternativas reais da Q16, escritos a partir do contexto da linha (cursos curtos, congressos, aprender com um colega, adiar).
- O seo-tecnico como dono do chamado de página pilar.
- As contagens manuais dos campos trocados do F4 (48, 147, 54, 260; 60, 136, 52, 269) e do subtítulo de 289 (118), a recontar por script.
- "Para veterinários" no título de 68615 descreve o público-alvo da ficha ("Médicos Veterinários") sem criar requisito.

## [CONFIRMAR]

- Endereço da política de privacidade da Faculdade Ufape e aviso de cookies do pixel e das tags.
- U11 (inscrição x matrícula), U10 (657), OU3, OU6, OU10, OU11, OU12, OU13, OU14 e OU17, CP1 e A12 (abertas no plano).
- Valor ou regra da prova de recuperação cobrada à parte em 657.
- Alcance de "valores de inscrição" no reembolso (matrícula, 1ª mensalidade).
- Se o formulário não cobra (frase de risco) e se a plataforma aceita "Título" no formulário e "Apoio" no `cta_final`.
- Se o botão "COMPRAR" fica na página nova.
- Credencial do "instrutor RECOVER" de 657.
- Tema certo de "Reanimação cardiopulmonar em vasos críticos" em 341.
- Contato e endereço de documentos de 289 (secretaria@ e São Paulo).
- Redirecionamento de 68605 e da URL antiga de 68615; indexação e conteúdo sem JavaScript.
- Quem aprova certificação e ato regulatório (A9) e quem edita o site.

## Fontes

- /home/user/marketing-ufape/saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/contexto/ufape-geral.md, /home/user/marketing-ufape/contexto/pos-graduacao.md, /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/ (fichas de 657, 341, 289, 68615 e 333)
- /home/user/marketing-ufape/templates/pagina-da-turma.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md, 02-estrategia-e-posicionamento.md, 03-busca.md, 08-conversao.md
