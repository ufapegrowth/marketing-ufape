# Revisão do qa-de-marketing: texto em linguagem simples para a diretoria (JSON da página)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** geral (graduacao, pos, livres e eventos)
- **Data:** 27/10/2026
- **Revisado (nenhum arquivo foi editado):** saidas/09-analytics-e-insights/relatorios-geral-2026-10-27-diretoria.json (commit 7edd31c) e, para saber o que aparece na tela, saidas/02-estrategia-e-posicionamento/plano-diretoria-2026-10-27.html (script de montagem)
- **Base de comparação:** saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md (narrativa aprovada, com C1 a C16) e a seção 8 de saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-documento-final.md
- **Entradas lidas:** contexto/ufape-geral.md; auditorias/conformidade-educacional.md; docs/execucao-2026-10-26.md; docs/pendencias-camada-1.md; saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (seções 8 a 11); saidas/10-operacoes-de-marketing/cursos/ (livres-573, livres-68614, livres-68637, livres-623, livres-616, livres-68618, livres-68665, livres-68666: linha literal do catálogo e início)
- **Dados pessoais:** nenhum lido ou citado.

O que a página mostra: o script não exibe os campos `codigos`, `id` nem o código das turmas nas linhas. Os códigos internos ficam só no arquivo, o que está certo. A conferência de clareza vale para os textos que aparecem na tela.

---

## 1. Veredito

**CORRIGIR.**

Motivo, em resumo: o texto está bem escrito, os números de verba, metas em reais, contagens de peças e datas de início batem com a narrativa aprovada. Mas a junção das decisões perdeu um pedido inteiro com prazo (as campanhas ativas das 6 turmas que já começaram, A4, 03/11). Três prazos mudaram: a exportação de 28/10 virou 30/10, as metas e a verba da Graduação viraram "antes de 16/11" quando o prazo é 30/10, e a pergunta sobre a forma de uso do WhatsApp foi adiantada de 07/12 para 13/11. Um prazo foi criado sem fonte: o plantão de fim de semana até 13/11. Seis cursos livres aparecem como "nome a confirmar no catálogo", mas o catálogo tem os nomes, e duas datas que estão no catálogo saíram como vazias. A suspensão de provas e Livres foi atribuída à diretoria, mas foi decisão do marketing da Ufape (docs/execucao-2026-10-26.md, "Decisões do cliente (pessoa do marketing, 26/10/2026)", decisão 14). Faltam também três marcos do calendário.

Conformidade: falha em dois itens. Nomes de curso não batem com o catálogo, e a urgência tem prazo sem fonte ou adiantado (detalhe na seção 4). Por regra, o veredito é CORRIGIR.

Nada foi publicado, enviado ou pago.

---

## 2. O que confere (não mexer)

- **Verba:** R$ 28.000,00 (R$ 17.740,00 no Meta e R$ 10.260,00 no Google); R$ 2.000,00 por turma ou curso; divisões de março (R$ 1.250,75 e R$ 749,25), de abril (R$ 1.276,25 e R$ 723,75) e da Graduação (R$ 1.440,00 e R$ 560,00; Pedagogia R$ 2.000,00; total R$ 4.000,00).
- **Metas:** 15 matrículas; R$ 133,33 por matrícula; faixas em reais da onda 1 (R$ 404.550,00 a R$ 715.500,00), de março (R$ 420.750,00 a R$ 726.000,00) e de abril (R$ 486.750,00 a R$ 584.100,00), conferidas contra a tabela 3.3 da narrativa.
- **Contagens:** 13 turmas (5 e 8), 24 mensagens, 36 posts (12 de feed e 24 de Stories), 30 posts, 53 cards, 5 roteiros, 8 páginas, 55 textos, 129 cards, 77 sem dia, 9 posts de coordenação, 48 posts, 8 roteiros, 55 toques em 31 dias, 47 contínuos, 14 páginas antigas, 3 fichas de prova, 10 turmas de maio.
- **Datas:** início das 6 turmas da onda 1, das 5 de março e das 9 de abril; pausas de mídia da onda 1; 22/02/2027; 17/08/2026; Workshop em 20 e 21/11; provas em 27/11; 03/12, 04/12, 10/12, 11/12, 04/01, 07/12, 14/12, 30/11, 30/12, 15/02/2027.
- **Graduação:** vagas (45, 45 e 80) e mensalidades com desconto (R$ 5.000,00, R$ 4.000,00 e R$ 525,00).
- **Workshop:** 16 h, 30 vagas, R$ 1.250,00 e R$ 450,00, iguais ao catálogo.
- **Decisões:** 24 itens. As decisões 1, 3, 5, 8, 10, 11, 12, 19, 20, 21, 23 e 24 mantêm prazo e sentido.
- **Avisos 1 a 7:** batem com as seções 3.4, 3.5 e [CONFIRMAR] da narrativa.

---

## 3. Correções

Localização no formato do JSON: posição contada a partir de 1 (por exemplo, "decisões, item 2" é o segundo objeto de `decisoes`).

### 3.1 Fidelidade: quem decidiu a suspensão (decisão 14)

Fonte: docs/execucao-2026-10-26.md, "Decisões do cliente (pessoa do marketing, 26/10/2026)", decisão 14. A narrativa diz "Ordem do cliente de 26/10". O texto vai para a própria diretoria, então não pode dizer que a ordem foi dela.

**F1. `resumo`, frase 5**
- Trocar: "Depois vêm as turmas de maio de 2027 e os Cursos Livres de 2027. Provas de bolsa e Cursos Livres seguem por último, por ordem da diretoria."
- Por: "Depois vêm as turmas de maio de 2027 e os Cursos Livres de 2027. Provas de bolsa e Cursos Livres seguem por último, por decisão do marketing da Ufape em 26/10."

**F2. `linhas` provas, `frase`**
- Trocar: "Por ordem da diretoria de 26/10, as provas ficam por último e não recebem peças novas até nova ordem. A data de 27/11 não muda."
- Por: "Por decisão do marketing da Ufape em 26/10, as provas ficam por último e não recebem peças novas até nova ordem. A data de 27/11 não muda."

**F3. `linhas` livres, `frase`**
- Trocar: "Também suspensos por ordem da diretoria de 26/10: a estratégia está pronta e o kit de cada curso ainda não foi feito."
- Por: "Também suspensos por decisão do marketing da Ufape em 26/10: a estratégia está pronta e o kit de cada curso ainda não foi feito."

**F4. `proxima_etapa`, item 3, `frase`**
- Trocar: "Seguem por último, por ordem da diretoria, até nova decisão."
- Por: "Seguem por último, por decisão do marketing da Ufape em 26/10, até nova decisão."

Os textos que falam do futuro ("quando a diretoria liberar") ficam como estão, porque a narrativa (7.3) diz "quando a direção disser".

### 3.2 Fidelidade: pedido perdido na junção (A4, 03/11)

Na narrativa (4.6, item 39, e 6.1, linha de 03/11), a A4 pede decidir se as campanhas pagas ainda ativas das 6 turmas que já começaram são pausadas ou mantidas, até 03/11 [CONFIRMAR: origem da data]. O JSON não tem esse pedido em nenhuma decisão, aprovação ou marco. A "A04" da decisão 6 é outro item (backlog A04). Para manter as 24 decisões, a A4 entra na decisão 2, que trata do mesmo assunto (gasto de campanhas no ar).

**F5. `decisoes`, item 2, `prazo_texto`**
- Trocar: "até 28/10 (as duas primeiras turmas até 29/10)"
- Por: "até 28/10 (as duas primeiras turmas até 29/10; as 6 turmas que já começaram, até 03/11, data a confirmar)"

**F6. `decisoes`, item 2, `pergunta`** (junta a A4 e devolve a Busca do Google, que tinha sumido; a fonte diz "só remarketing e busca")
- Trocar: "Pode conferir o gasto das 6 campanhas, fixar a verba diária até a véspera do 3º módulo e aprovar a passagem para anúncios só a quem já visitou a página?"
- Por: "Pode conferir o gasto das 6 campanhas, fixar a verba diária até a véspera do 3º módulo e aprovar a passagem para anúncios só a quem já visitou a página ou procura o tema no Google? E as campanhas pagas ainda ativas das 6 turmas de Pós que já começaram: pausar ou manter, depois da conferência da equipe de mídia?"

**F7. `decisoes`, item 2, `codigos`:** acrescentar "A4" à lista.

**F8. `aprovacoes`, item 1, `o_que`**
- Trocar: "Envio de e-mail e WhatsApp das 6 turmas, verba diária e passagem para anúncios só a quem já visitou a página"
- Por: "Envio de e-mail e WhatsApp das 6 turmas, verba diária e passagem para anúncios só a quem já visitou a página ou procura o tema no Google"

**F9. `marcos`:** acrescentar (ver também 3.6):
`{"data": "2026-11-03", "titulo": "Conferência das campanhas pagas ainda ativas das 6 turmas de Pós que já começaram (data a confirmar)", "linha": "pos-onda1"}`

### 3.3 Fidelidade: prazos que mudaram ou foram criados

**F10. `decisoes`, item 6 (verba do trimestre e exportação):** a narrativa (4.1, item 6) dá 28/10 para a exportação e 30/10 para as metas.
- Em `prazo`, trocar: "2026-10-30"
- Por: "2026-10-28"
- Em `prazo_texto`, trocar: "até 30/10"
- Por: "até 28/10 (exportação do gerenciador e da loja) e 30/10 (verba e metas)"

**F11. `decisoes`, item 14 (U11 e U11a), `prazo_texto`:** a U11a tem como data sugerida "antes do primeiro envio pago de 07/12" (narrativa 4.3, item 23). Juntá-la ao 13/11 adianta o prazo sem fonte.
- Trocar: "até 13/11"
- Por: "até 13/11 (a forma de uso do WhatsApp, antes do primeiro envio pago de 07/12, data sugerida)"

**F12. `decisoes`, item 15, `pergunta`:** o plantão de fim de semana não tem data nos planos (narrativa 2.5 e [CONFIRMAR]). Ao entrar nesta decisão, ganhou o prazo de 13/11.
- Trocar: "Quantas horas por semana o time tem para o perfil de Instagram e os comentários? Quem grava os Reels e os roteiros, e quem produz as artes (com custo, se houver)? Quem forma o plantão de sábado e feriado, com duas pessoas?"
- Por: "Quantas horas por semana o time tem para o perfil de Instagram e os comentários? Quem grava os Reels e os roteiros, e quem produz as artes (com custo, se houver)? Quem forma o plantão de sábado e feriado, com duas pessoas (sem prazo nos planos)?"

**F13. `decisoes`, item 15, `por_que`:** exagero. A narrativa (2.5) prevê três planos por data: regra programada, plantão ou execução no dia útil seguinte.
- Trocar: "Sem isso, 77 dos 129 cards de docente de abril ficam sem dia no calendário e as trocas de anúncio de fim de semana não acontecem."
- Por: "Sem isso, 77 dos 129 cards de docente de abril ficam sem dia no calendário e as trocas de anúncio de fim de semana dependem de regra programada ou ficam para o dia útil seguinte."

**F14. `decisoes`, item 17, `por_que`:** para editais e reajuste, 16/11 vem de anuncios-meta-graduacao (seção 0). Só para menores e G11 a data é sugestão (narrativa 4.2, itens 13 e 16).
- Trocar: "Sem isso, a Graduação sobe só com o teste sem preço e as listas de contatos seguem bloqueadas. A data de 16/11 é sugestão."
- Por: "Sem isso, a Graduação sobe só com o teste sem preço e as listas de contatos seguem bloqueadas. A data de 16/11 vem do plano de anúncios para os editais e o reajuste; para os outros pontos, é sugestão."

**F15. `decisoes`, item 18, `prazo_texto`:** para Pedagogia, 16/11 é [SUPOSIÇÃO] (narrativa 4.2, item 14). Para o noturno, vem da fonte (item 15).
- Trocar: "até 16/11"
- Por: "até 16/11 (para Pedagogia, data sugerida)"

**F16. `decisoes`, item 22 (política de privacidade), `prazo_texto`:** [SUPOSIÇÃO] na narrativa (4.3, item 22).
- Trocar: "antes de 03/12"
- Por: "antes de 03/12 (data sugerida)"

**F17. `aprovacoes`, item 7 (Graduação), `quando`:** metas e verba têm prazo de 30/10 (narrativa 4.2, item 11; decisão 9 do próprio JSON: "Sem isso nenhuma campanha da Graduação sobe, nem em teste").
- Trocar: "antes de 16/11"
- Por: "metas e verba até 30/10; o resto antes de 16/11"

**F18. `aprovacoes`, item 5 (kit de abril), `quando`:** não há fonte para "até 30/12" no kit. O 30/12 é da mídia de abril (PP16). As páginas têm prazo de 10/12 (OC1-A, cmo-pos onda 3, seção 9). Os envios de abril começam em 04/01 (narrativa 6.2; OC5, "peças prontas para 04/01").
- Trocar: "até 30/12"
- Por: "páginas até 10/12; o resto antes de 04/01/2027, quando começam os envios de abril"

**F19. `aprovacoes`, item 3 (kit de março), `quando`:** em 30/11 se aprovam OB2 a OB5; as páginas (OB1) vão até 03/12 (narrativa 6.1). Além disso, "aprovação das campanhas" não descreve este item.
- Trocar: "aprovação das campanhas em 30/11"
- Por: "até 30/11 (as páginas, até a publicação de 03/12)"

**F20. `aprovacoes`, item 9 (Workshop), `quando`:** o 28/10 é da sequência de mídia (R3). As mensagens de serviço (R2) e a mensagem pós-evento (R7) não têm esse prazo.
- Trocar: "28/10"
- Por: "28/10 para a sequência de mídia"

### 3.4 Fidelidade: partes de pedidos que sumiram na junção

**F21. `decisoes`, item 7 (OU3 a OU8), `pergunta`:** faltam OU6 e o dia do módulo 2 da 68604 (narrativa 4.1, item 8).
- Trocar: "Como o aluno repõe módulos perdidos, inclusive o módulo presencial de Ecocardiografia? Quantas vagas restam por turma? O que a Ufape já tem pronto de cada turma? Quando paga a 1ª mensalidade quem entra depois?"
- Por: "Como o aluno repõe módulos perdidos, inclusive o módulo presencial de Ecocardiografia? Quantas vagas restam por turma? O que a Ufape já tem pronto de cada turma? A matrícula vale até a véspera do 3º módulo ou inclui o 1º dia dele? Qual é o dia do módulo 2 de Diagnóstico por Imagem? Quando paga a 1ª mensalidade quem entra depois?"

**F22. `decisoes`, item 9 (Graduação), `pergunta`:** falta a U12, que está nos códigos (narrativa 4.2, item 11, e 3.3).
- Trocar: "A meta da Graduação é 15 ou 30 matrículas? Medicina Veterinária conta como 1 curso ou 2 turmas? Aprova a verba de R$ 2.000,00 por curso e o limite de R$ 133,33 por matrícula?"
- Por: "A meta da Graduação é 15 ou 30 matrículas? Medicina Veterinária conta como 1 curso ou 2 turmas? Qual conta vale como valor do curso para a meta em reais? Aprova a verba de R$ 2.000,00 por curso e o limite de R$ 133,33 por matrícula?"

**F23. `decisoes`, item 13, `pergunta`:** falta a MP10 (rastreio), que é separada do endereço com UTM (G13).
- Trocar: "Pode enviar os números da Graduação desde 17/08 (inscritos, redações e matrículas), a data limite de inscrição, o endereço da página com rastreio e os públicos de 18 anos ou mais?"
- Por: "Pode enviar os números da Graduação desde 17/08 (inscritos, redações e matrículas), a data limite de inscrição, o endereço da página com rastreio, os públicos de 18 anos ou mais e a configuração de rastreio das campanhas?"

**F24. `decisoes`, item 16, `pergunta`:** faltam OU4, OU5 e OU14 (narrativa 4.3, item 20).
- Trocar: "Pode responder as dúvidas de março: reposição do módulo presencial de Citopatologia, local e formato do módulo 3 de Medicina Interna Equina, coordenação e docentes de Citopatologia, CEP de Patologia Clínica e datas em feriado?"
- Por: "Pode responder as dúvidas de março: reposição do módulo presencial de Citopatologia, vagas e o que a Ufape já tem de cada turma, local e formato do módulo 3 de Medicina Interna Equina, coordenação e docentes de Citopatologia, CEP de Patologia Clínica, regra do 3º módulo na página e datas em feriado?"

**F25. `decisoes`, item 17, `pergunta`:** a G11 está nos códigos, mas não na pergunta (narrativa 4.2, item 16).
- Trocar: "Pode corrigir os textos dos editais, responder sobre o reajuste de dezembro e validar com o jurídico as regras para menores de idade?"
- Por: "Pode corrigir os textos dos editais, responder sobre o reajuste de dezembro, validar com o jurídico as regras para menores de idade e informar as horas do time, os perfis, a autorização de imagem e se a Graduação usa o hospital veterinário nas peças?"

**F26. `decisoes`, item 4, `por_que`:** "sem gerar cadastro" não está na fonte. A fonte diz "Nenhum gasto fora do plano" (R5) e "Nenhum clique para página com data errada" (R8).
- Trocar: "Anúncios com destino errado gastam verba sem gerar cadastro."
- Por: "Anúncios com destino errado gastam verba fora do plano e levam a uma página com data ou turma errada."

**F27. `linhas` pos-marco, `pronto`, item 4:** na 333 são 4 WhatsApp até a resposta sobre reposição (narrativa 2.3).
- Trocar: "Mensagens por turma (2 e-mails e 5 WhatsApp)"
- Por: "Mensagens por turma (2 e-mails e 5 WhatsApp; em Citopatologia Veterinária, 4 WhatsApp até a resposta sobre reposição)"

**F28. `linhas` pos-marco, `depende_da_ufape`, item 4:** as datas em feriado são de 333 e de 341 (OU17; narrativa 2.3; pendências, travas da onda 2).
- Trocar: "Responder sobre reposição, docentes e datas em feriado de Citopatologia Veterinária"
- Por: "Responder sobre reposição e docentes de Citopatologia Veterinária e sobre as datas em feriado de Citopatologia Veterinária e de Medicina Interna Equina"

**F29. `aprovacoes`, item 4, `o_que`:** em 07/12 sobem 68615, 333 e a nova estrutura da 289 (narrativa 6.1). A Cardiologia ficou de fora.
- Trocar: "Subida da mídia das 5 turmas, a começar pelas de Patologia Clínica e Citopatologia em 07/12"
- Por: "Subida da mídia das 5 turmas, a começar por Patologia Clínica, Citopatologia e Cardiologia Veterinária em 07/12"

**F30. `linhas` graduacao, `frase`:** "estão aprovados" sem dizer por quem soa como liberado. "Só Pedagogia e noturno não sobem" contradiz a decisão 9 (nada sobe sem metas e verba).
- Trocar: "O kit e as campanhas estão aprovados, mas Pedagogia e o noturno de Medicina Veterinária ainda não podem subir."
- Por: "O kit e as campanhas foram aprovados pela revisão de qualidade e esperam a aprovação da Ufape; Pedagogia e o noturno de Medicina Veterinária ainda dependem de correções nas páginas."

**F31. `linhas` graduacao, `meta`**
- Trocar: "Pelo menos 15 matrículas por curso e no máximo R$ 133,33 por matrícula. O edital pede turma mínima de 30, o que ainda precisa ser decidido"
- Por: "Pelo menos 15 matrículas por curso e no máximo R$ 133,33 por matrícula. O edital pede turma mínima de 30 por turma; a Ufape ainda precisa decidir se a meta é 15 ou 30"

**F32. `linhas` workshop, `frase`:** a narrativa diz "criativos sem revisão". "Em ajuste" sugere trabalho em andamento.
- Trocar: "Posts e mensagens foram aprovados pela revisão de qualidade em 27/10; os criativos ainda estão em ajuste e a mídia já no ar precisa de conferência."
- Por: "Posts e mensagens foram aprovados pela revisão de qualidade em 27/10; os criativos ainda não foram revisados e a mídia já no ar precisa de conferência."

**F33. `linhas` workshop, `depende_da_ufape`, item 1:** os valores já estão no catálogo (R$ 1.250,00 aparece na própria turma). O que falta são as linhas de preço e de pagamento (E5).
- Trocar: "Informar os valores do presencial, a validade e o limite do cupom e o fim das inscrições"
- Por: "Informar as linhas de preço e de pagamento do presencial, a validade e o limite do cupom e o fim das inscrições"

**F34. `linhas` workshop, `depende_da_ufape`, item 3:** falta a A2 (WhatsApp das mensagens M6 e M7).
- Trocar: "Informar o link e o prazo da gravação, o endereço e o bloco da prova"
- Por: "Informar o link e o prazo da gravação, o endereço e o bloco da prova e o WhatsApp a usar em duas das mensagens"

**F35. `linhas` pos-abril, turma 68632, `nota`**
- Trocar: "módulo 1 presencial; mídia para na véspera até a resposta sobre reposição"
- Por: "módulo 1 presencial; até a resposta sobre reposição, a mídia para na véspera do início"

**F36. `proxima_etapa`, item 1, `frase`:** faltam o prazo de 15/01 das respostas de maio (narrativa 4.4, itens 25 a 27) e a 352, que pode ir para 24/04 (narrativa 7.1; observação da revisão do documento final).
- Trocar: "10 turmas começam entre 08/05 e 28/05. O plano de mídia está pronto, com R$ 2.000,00 por turma e subida não antes de 15/02/2027. Páginas, mensagens, posts e anúncios ainda estão por fazer."
- Por: "10 turmas começam entre 08/05 e 28/05 (uma delas pode passar para 24/04, se a Ufape confirmar a data do site). O plano de mídia está pronto, com R$ 2.000,00 por turma e subida não antes de 15/02/2027. Páginas, mensagens, posts e anúncios ainda estão por fazer. As respostas da Ufape sobre maio têm prazo até 15/01/2027."

**F37. `proxima_etapa`, item 2, `frase`:** só a 68638 tem data a confirmar. A 560 está sem campanha e fora da visão (narrativa 7.2).
- Trocar: "Dois cursos têm data ainda a confirmar e falta o plano, a página, o kit mínimo e a verba. Entram quando a diretoria liberar a vez dos Cursos Livres."
- Por: "São dois cursos: um com data ainda a confirmar na planilha e outro ainda sem campanha. Falta o plano, a página, o kit mínimo de peças e a verba. Entram quando a diretoria liberar a vez dos Cursos Livres."

**F38. `avisos`, item 8:** na narrativa, a perda de sentido do teste é [SUPOSIÇÃO] ("talvez"). A decisão é da pessoa do marketing porque o teste é um item de aprovação, não porque o LinkedIn saiu.
- Trocar: "A decisão sobre o teste de LinkedIn de Anestesiologia Avançada fica com a pessoa do marketing, porque o LinkedIn pago saiu do plano de mídia."
- Por: "O teste de LinkedIn de Anestesiologia Avançada (11 a 31/01/2027) talvez tenha perdido o sentido, porque o LinkedIn pago saiu do plano de mídia; a decisão fica com a pessoa do marketing."

### 3.5 Dados de curso: Cursos Livres (bloqueia pela conformidade)

As seis turmas de `linhas` livres saem como "Curso Livre (nome a confirmar no catálogo)", mas o catálogo tem o nome de todas (linha literal do catálogo nos JSON por curso). Duas datas do catálogo saíram vazias. Também faltam os dois grupos de estudos da onda 1, 68665 (01/11) e 68666 (25/11), que a narrativa lista (2.9) e que começam até abril. Cada `nome` abaixo é o valor exato a trocar, na turma do código indicado.

**F39. Turma 573, `nome`**
- Trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "Curso Hands-On de Ecocardiografia Veterinária Básica- SÃO PAULO"

**F40. Turma 68614, `nome`**
- Trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "Curso Livre em Videotoscopia"

**F41. Turma 68637, `nome`**
- Trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "Curso de imersão teórico e prático em Endoscopia Digestiva - SÃO PAULO"

**F42. Turma 623, `nome` e `inicio`:** o catálogo tem 28/11/2026 pela planilha; o site mostra agosto. Pela decisão 12, vale a planilha.
- Em `nome`, trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "III curso de imersão teórico e prático em endoscopia digestiva- SÃO PAULO"
- Em `inicio`, trocar `null` por "2026-11-28". A nota fica como está.

**F43. Turma 616, `nome`**
- Trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "Imersão Avançada em Anestesia Felina"

**F44. Turma 68618, `nome`, `inicio` e `nota`:** o catálogo tem 18/12/2026 (planilha e site). Só a visão de campanhas diverge.
- Em `nome`, trocar: "Curso Livre (nome a confirmar no catálogo)"
- Por: "Curso de Ventilação Mecânica Aplicada à Anestesia Veterinária - Curso Teórico-Prático"
- Em `inicio`, trocar `null` por "2026-12-18".
- Em `nota`, trocar: "data ainda a confirmar"
- Por: "a visão de campanhas mostra outra data; vale a da planilha"

**F45. Acrescentar em `linhas` livres, `turmas`:**
- `{"codigo": "68665", "nome": "Grupo de Estudos em Cardiologia e Ecocardiografia Veterinária", "inicio": "2026-11-01", "nota": "online"}`
- `{"codigo": "68666", "nome": "Grupo de Estudos em Clínica Médica e Emergência de Cães e Gatos", "inicio": "2026-11-25", "nota": "online"}`

Observação: os hifens dos nomes são os do catálogo (hífen comum), não travessão.

### 3.6 Calendário (30 marcos)

Os 30 marcos conferem em data e sentido, com quatro ajustes e três faltas. Faltam:
- 17/04, início de 68617 e 68636. O calendário pula de 10/04 para 24/04.
- 15/01, pausa de Hematologia Veterinária. As outras pausas da onda 1 estão no calendário.
- 03/11, a A4 (F9).

O script do HTML não limita a quantidade de marcos. Com os acréscimos, ficam 33.

**F46. `marcos`, 10/11**
- Trocar: "Mudança do público frio da mídia do Workshop"
- Por: "Mudança do público da mídia do Workshop"

**F47. `marcos`, 16/11**
- Trocar: "Começa a captação da Graduação, se as travas estiverem resolvidas"
- Por: "Começa a captação da Graduação, se metas, verba, públicos, rastreio e aprovadores estiverem definidos"

**F48. `marcos`, 06/01/2027:** a narrativa (6.2) diz que 679, 366 e 68636 sobem só com a data confirmada.
- Trocar: "Sobe a mídia de abril, sem a turma de Ortopedia Veterinária"
- Por: "Sobe a mídia de abril, sem a turma de Ortopedia Veterinária; Infectologia, Fisioterapia e Pneumologia só com a data confirmada"

**F49. `marcos`, 18/02/2027:** é prazo, não fato garantido.
- Trocar: "Resposta da área de regulação sobre siglas de título"
- Por: "Prazo para a resposta da área de regulação sobre siglas de título"

**F50. Acrescentar em `marcos`:**
- `{"data": "2027-01-15", "titulo": "Pausa da mídia de Hematologia Veterinária, às 23h59", "linha": "pos-onda1"}`
- `{"data": "2027-04-17", "titulo": "Início de Endocrinologia de Pequenos Animais e de Pneumologia Veterinária (data a confirmar)", "linha": "pos-abril"}`
- o marco de 03/11 da F9.

### 3.7 Clareza para a diretoria

**F51. `linhas` pos-onda1, `depende_da_ufape`, item 1:** "uma frase que não pode ficar" não diz à diretoria o que corrigir. A troca nomeia a frase como pendência, sem afirmar certificação, como a revisão anterior aceitou.
- Trocar: "Corrigir nas páginas uma frase que não pode ficar, o texto de turma mínima e a regra do 3º módulo"
- Por: "Corrigir nas páginas a frase que cita o MEC (o texto oficial está pedido à área de regulação), a turma mínima de 20 (vale 15) e a regra do 3º módulo"

**F52. `decisoes`, item 11, `pergunta`**
- Trocar: "Pode corrigir nas páginas das 6 turmas uma frase que não pode ficar, o texto de turma mínima e a regra do 3º módulo, e acertar a data de Ecocardiografia?"
- Por: "Pode corrigir nas páginas das 6 turmas a frase que cita o MEC, a turma mínima de 20 (vale 15) e a regra do 3º módulo, e acertar a data de Ecocardiografia?"

**F53. "CRM" sem explicação.** O próprio aviso 2 já usa "sistema de contatos".
- `linhas` pos-marco, `pronto`, item 5. Trocar: "Listas e regras do CRM" / Por: "Listas e regras do sistema de contatos (CRM)"
- `linhas` pos-abril, `pronto`, item 5. Trocar: "Listas do CRM com 55 toques em 31 dias, sem choque de datas" / Por: "Listas do sistema de contatos com 55 mensagens programadas em 31 dias, sem choque de datas"
- `decisoes`, item 5, `pergunta`. Trocar: "Quem aprova posts, anúncios, verba, mensagens em massa e páginas? Quem executa no gerenciador de anúncios, no CRM e no site?" / Por: "Quem aprova posts, anúncios, verba, mensagens em massa e páginas? Quem executa no gerenciador de anúncios, no sistema de contatos (CRM) e no site?"
- `aprovacoes`, item 3, `o_que`. Trocar: "Páginas, mensagens, 30 posts, posts de docente e 53 cards, 5 Reels e artes, listas e automações do CRM" / Por: "Páginas, mensagens, 30 posts, posts de docente e 53 cards, 5 Reels e artes, listas e automações do sistema de contatos"
- `avisos`, item 5. Trocar: "Ainda a confirmar: quem aprova cada tipo de peça, quem executa no site, no CRM e nos anúncios e quem forma o plantão de fim de semana." / Por: "Ainda a confirmar: quem aprova cada tipo de peça, quem executa no site, no sistema de contatos e nos anúncios e quem forma o plantão de fim de semana."

**F54. `linhas` pos-marco, `pronto`, item 1 (SEO)**
- Trocar: "5 páginas novas (texto, SEO e formulário)"
- Por: "5 páginas novas (texto, ajustes para a busca do Google e formulário)"

**F55. "cards" sem explicação (primeira vez em cada linha)**
- `linhas` pos-marco, `pronto`, item 3. Trocar: "Posts de docente: 5 já existentes conferidos, 1 novo e 53 cards" / Por: "Posts de docente: 5 já existentes conferidos, 1 novo e 53 cards (Stories que apresentam um docente)"
- `linhas` pos-abril, `pronto`, item 3. Trocar: "129 cards de docente e 9 posts de coordenação" / Por: "129 cards de docente (Stories que apresentam um docente) e 9 posts de coordenação"

**F56. `decisoes`, item 14, `pergunta` ("API")**
- Trocar: "A inscrição da Pós custa R$ 260,00 ou R$ 250,00? A Ufape usa a API oficial do WhatsApp ou o aplicativo no celular?"
- Por: "A inscrição da Pós custa R$ 260,00 ou R$ 250,00? A Ufape envia WhatsApp pela plataforma oficial do WhatsApp Business ou pelo aplicativo no celular?"

**F57. `verba` das linhas workshop, provas e livres.** O mesmo valor aparece nas três; a marca interna vira texto simples.
- Trocar: "[DADO NÃO FORNECIDO]"
- Por: "Ainda não informada pela Ufape"

**F58. "aprovado" sem dizer por quem.** A diretoria pode ler como liberado para publicar.
- `numeros`, item 5, `rotulo`. Trocar: "turmas de Pós de março e abril com o kit completo aprovado" / Por: "turmas de Pós de março e abril com o kit completo aprovado pela revisão de qualidade"
- `linhas` pos-abril, `frase`. Trocar: "As 8 turmas do primeiro lote têm o kit completo aprovado; a de Ortopedia Veterinária está em espera total." / Por: "As 8 turmas de abril têm o kit completo aprovado pela revisão de qualidade; a de Ortopedia Veterinária está em espera total."

### 3.8 Observações (não bloqueiam)

- `resumo`, frase 3: a narrativa (frase 3) também cita datas, quem grava e as horas do time. O resumo encurtou sem mudar o sentido. Se couber, acrescentar "datas".
- Ficaram fora das decisões, sem prazo nos planos: U1, U3 e U4 (provas, suspensas), U6 (linha "Pneumologia" da visão de campanhas) e a contagem de 46 páginas com a frase do MEC. Estão cobertas de forma genérica em `depende_da_ufape` e no item 23. Não é perda de prazo.
- A pausa recomendada de Ecocardiografia em 18/12 está na nota da turma e não no calendário. Aceitável.
- Decisão 3, `por_que`: "pode estar levando o público ao lugar errado" é dedução, mas está em tom de possibilidade e bate com o motivo da conferência (narrativa 2.7). Passa.

---

## 4. auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado | Onde |
|---|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | **falha** | `linhas` livres: 6 turmas com "nome a confirmar no catálogo", mas o catálogo tem os nomes; 623 e 68618 sem a data do catálogo (F39 a F44). Pós, Graduação e Workshop batem |
| Dados do curso | Status "aberto" ou sem chamada para inscrição | ok | o texto não chama para inscrição |
| Dados do curso | Modalidade clara | ok | Workshop separa presencial e transmitido |
| Regulação | Graduação com ato do catálogo | não se aplica | nenhum ato citado |
| Regulação | Pós sem "reconhecida pelo MEC" | ok | nenhuma frase liga certificado ao MEC; a F51 e a F52 citam a frase só como pendência a corrigir |
| Regulação | Curso livre não confere diploma | não se aplica | não é peça de venda |
| Regulação | Nota MEC com fonte | ok | nenhuma |
| Promessas | Emprego, salário, aprovação | ok | nenhuma |
| Promessas | Empregabilidade, superlativos, comparação | ok | nenhum |
| Preço | Valor, parcelas e condições | ok | preços como dado do catálogo, não como oferta; mensalidades da Graduação com "no 1º semestre, com desconto" |
| Preço | Bolsa e desconto com regra | ok | nenhum desconto citado |
| Preço | Urgência real, com data | **falha** | o prazo do plantão até 13/11 não tem fonte (F12); a U11a foi adiantada de 07/12 para 13/11 (F11); sugestões sem marca nos itens 18 e 22 (F15, F16); exagero em "não acontecem" (F13) |
| Preço | Prouni, Fies | ok | nenhum |
| Pessoas | Autorização de imagem | ok | nenhum docente citado |
| Pessoas | Menores | não se aplica | só como pendência do jurídico |
| Pessoas | Formulário com privacidade | não se aplica | só como pendência |
| Pessoas | WhatsApp e e-mail com consentimento | ok | "registrar o consentimento dos contatos" aparece como pendência do Workshop |
| Pessoas | Nenhum dado pessoal | ok | nenhum nome, telefone, CPF ou e-mail; só funções ("pessoa do marketing", "área de regulação", "jurídico") |
| Marca | Nunca chamar a TGH de "Agência" | ok | nenhuma ocorrência de "Agência" nem de TGH |
| Escrita | Sem travessão nem meia-risca | ok | nenhuma ocorrência no JSON; os hifens são comuns (ids, "OA2-B") |
| Plataformas e anúncios | Todos os itens | não se aplica | o texto não é anúncio |

**Resultado:** Bloqueado. Itens bloqueados: nomes e datas dos Cursos Livres (F39 a F45) e prazos sem fonte ou adiantados (F11 a F16). Revisado por: qa-de-marketing (agente); falta o humano. Data: 27/10/2026.

---

## 5. Próximo passo

1. O relatorios (ou o orquestrador, dono do JSON) aplica F1 a F58 com o texto exato e gera a página de novo.
2. Reconferência curta do qa: só F1 a F58 e a contagem de marcos (33) e de decisões (24).
3. Depois disso, segue para a aprovação humana da pessoa do marketing antes de ir à diretoria da Ufape.

---

## Fatos (com fonte)

- Decisão 14 tomada pelo cliente (pessoa do marketing) em 26/10/2026: docs/execucao-2026-10-26.md, "Decisões do cliente".
- A4 (6 turmas iniciadas com campanha ativa, 03/11 [CONFIRMAR]): relatorios-geral-2026-10-27.md, 4.6, item 39, e 6.1; docs/execucao-2026-10-26.md, "Pendências abertas".
- Exportação até 28/10 e metas até 30/10: relatorios-geral-2026-10-27.md, 4.1, item 6.
- U11a antes de 07/12 [SUPOSIÇÃO]: relatorios-geral-2026-10-27.md, 4.3, item 23.
- Plantão sem data: relatorios-geral-2026-10-27.md, 2.5 e [CONFIRMAR].
- OC1-A com prazo 10/12, PP16 até 30/12, envios de abril a partir de 04/01: cmo-pos-2026-10-27-onda3.md, seção 9; relatorios-geral-2026-10-27.md, 6.2.
- Nomes e datas dos Livres: linha literal do catálogo em saidas/10-operacoes-de-marketing/cursos/livres-573, -68614, -68637, -623, -616, -68618, -68665 e -68666.json.
- Datas em feriado de 333 e 341 (OU17): docs/pendencias-camada-1.md, travas da onda 2.

## Suposições ([SUPOSIÇÃO])

- [SUPOSIÇÃO] "Marketing da Ufape" é a forma certa de nomear, para a diretoria, a "pessoa do marketing" que decidiu como cliente. Se a pessoa do marketing não for da Ufape, trocar por "pela pessoa do marketing".
- [SUPOSIÇÃO] A MP10 é a configuração de rastreio das campanhas (pixel e conversões), separada da UTM do endereço (G13). Li só a narrativa, não o gestor-de-midia-graduacao.
- [SUPOSIÇÃO] A E5 do Workshop trata das linhas de preço e de pagamento, pela soma de "linhas de preço do presencial" (narrativa 2.7) e "pagamento do presencial" (texto anterior, revisão do documento final, C5).

## Dados que faltam ([CONFIRMAR])

- [CONFIRMAR] Origem da data de 03/11 da A4 (já marcada na narrativa).
- [CONFIRMAR] Quem aprova cada tipo de peça (contexto/ufape-geral.md, regras de aprovação, ainda vazio).
- [CONFIRMAR NO CATÁLOGO] Modalidade da 68618 (o catálogo traz o campo vazio); carga horária da 68666.

## Fontes

- contexto/ufape-geral.md
- auditorias/conformidade-educacional.md
- docs/execucao-2026-10-26.md
- docs/pendencias-camada-1.md
- saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md
- saidas/02-estrategia-e-posicionamento/plano-diretoria-2026-10-27.html
- saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md
- saidas/09-analytics-e-insights/relatorios-geral-2026-10-27-diretoria.json
- saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-documento-final.md
- saidas/10-operacoes-de-marketing/cursos/ (livres-573, livres-68614, livres-68637, livres-623, livres-616, livres-68618, livres-68665, livres-68666)
