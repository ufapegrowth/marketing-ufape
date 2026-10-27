# Landing page: hub da prova de bolsa da Pós-graduação, 27/11/2026 (22 provas, São Paulo e Goiânia)

- **Agente:** landing-page (departamento 08 Conversão), camada 3, onda 1, campanha das provas de bolsa
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Formato:** templates/landing-page.md, com as seções do método do agente. Texto pronto para a Ufape publicar no site atual ou na plataforma nova.
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada foi publicado, enviado ou pago. Toda mudança no site, no checkout, no CRM ou em tag de medição é pedido de aprovação humana.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md (item "Prova de bolsa" e regras de comunicação)
  - contexto/catalogo-de-cursos.md (seções 1 a 4, que incluem as seções 2 e 3; a seção 3 é a fonte de código, cidade, data, inscrição e status das provas)
  - As 22 fichas de prova de contexto/cursos/pos/ com status "aberto" (68639 a 68655 e 68657 a 68661), lidas por inteiro, inclusive 68639 e 68640 (modelos de São Paulo e Goiânia)
  - templates/landing-page.md e templates/pagina-da-turma.md
  - .claude/skills/raio-x-de-pagina/SKILL.md e .claude/skills/schema-de-curso/SKILL.md
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md (briefing e grupos D1 a D4 por destino)
  - saidas/08-conversao/analise-cro-pos-2026-10-26.md (página 3, prova 68639)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (seções 1 a 3, início da seção 4, seções 5 a 9; a seção 5 trata do hub T1 e das provas)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 3, 4 e 7)
  - auditorias/08-conversao.md e auditorias/conformidade-educacional.md
- **Não abri faculdade.ufape.com.br.** Tudo que a página atual mostra vem do texto copiado nas fichas. O comportamento do botão, do checkout e do celular não foi visto: está marcado [CONFIRMAR no site].
- **Dados pessoais:** nenhum. Nenhum docente, aluno ou aprovado é citado. Nenhum depoimento foi escrito.

## Como ler este arquivo

- Texto entre aspas ou em bloco de citação com o título "Texto da página" é o que vai para a página.
- [CONFIRMAR ...] no texto da página marca o ponto em que a Ufape precisa responder antes da publicação. O editor não publica a frase com a marca: oculta o trecho ou usa a variante indicada.
- [SUPOSIÇÃO] marca hipótese minha, não fato.
- A coluna "Turma de destino" da tabela mostra a leitura do briefing (grupos D1 a D4). Nenhum destino é fato até a Ufape confirmar.

## Bloqueios para publicar (resumo; o checklist completo está na seção 8)

1. Destino de cada prova (pedido A-C2 da campanha). Sem ele, o hub publica só as provas com destino confirmado, ou mostra "destino a informar".
2. Local da prova em Goiânia: as três páginas de Goiânia (68640, 68642, 68644) mostram o endereço de São Paulo.
3. Links de Cardiologia (68641 e 68642): conferir e testar antes de liberar as duas linhas.
4. Regras divergentes entre páginas: 12 páginas trazem "7 dias" para a matrícula e "no site" para o resultado, contra 10 dias úteis e WhatsApp ou e-mail no restante.
5. Frase de reconhecimento ligada ao MEC em 15 páginas de prova. O hub não repete a frase; as páginas de destino do botão precisam sair dela (pedido A7 do plano do cmo).
6. Aprovação humana de quem aprova páginas e preços [CONFIRMAR quem].

---

# 1. A PÁGINA (texto completo, na ordem das seções)

## LANDING PAGE

**Linha de negócio e curso:** Pós-graduação, hub das provas de bolsa de 27/11/2026 (22 provas: 19 em São Paulo e 3 em Goiânia, status "aberto" no catálogo, seção 3).

**Tipo de página:** hub. Não existe o tipo "prova_de_bolsa" no template pagina-da-turma.md (tipos: pos, livre, workshop, simposio). Esta página usa o formato de templates/landing-page.md. Se a plataforma nova criar o tipo, as seções abaixo viram as chaves sugeridas pela analise-cro: como_funciona, bolsas_previstas, regras, faq_bolsa e turma_de_destino (seção nova só entra em versão nova do template).

**Persona:** P4, o candidato que usa a prova de bolsa como porta de entrada, atravessando P1 (clínico de pequenos animais), P2 (quem viaja de outra cidade) e P3 (recém-formado). Tudo [SUPOSIÇÃO] até chegarem conversas anonimizadas do WhatsApp de vendas. Voz do aluno: nenhuma disponível. Não inventei frase de aluno. Quando chegarem as conversas, as frases das seções "problema" e "dúvidas" são trocadas pelas palavras reais.

---

### 1.1 Topo da página

**Título (H1, até 70 caracteres):**
Prova de bolsa de estudos da Pós-graduação

**Subtítulo (até 160 caracteres):**
Faça a prova presencial em 27 de novembro de 2026, em São Paulo ou em Goiânia, e dispute uma das 11 bolsas da sua especialidade. Inscrição de R$ 100,00.

**Promessa, sem exagero (frase abaixo do subtítulo):**
Você sabe as regras antes de pagar: quantas bolsas, qual nota, quando e onde. Nenhuma bolsa é garantida: ela depende do seu resultado na prova.

**Chamada para ação principal (botão):**
Ver as provas e me inscrever
(leva à tabela da seção 1.4; é o botão de maior peso visual)

**Chamada secundária (botão de contorno, ao lado ou abaixo):**
Falar com o time no WhatsApp
(abre a escolha entre São Paulo e Goiânia, ver seção 1.11)

**Linha de prova (faixa com 4 itens, todos com fonte no catálogo, no contexto ou nas páginas das provas):**
- 11 bolsas por prova, de 10% a 50%
- Inscrição de R$ 100,00
- Sexta-feira, 27/11/2026, das 9h às 13h
- Prova presencial em São Paulo e em Goiânia

Sem depoimento, sem número de inscritos, sem nota do MEC e sem nome de docente nesta faixa.

**Teste dos 5 segundos (conferir no celular antes de publicar):** que página é (prova de bolsa de pós-graduação), para quem (quem quer cursar uma pós da Faculdade UFAPE), qual formato (presencial, 27/11, 9h às 13h) e o que fazer agora (botão "Ver as provas e me inscrever"). O texto acima responde as quatro perguntas; a conferência visual no celular fica [CONFIRMAR no site].

---

### 1.2 Problema

**H2:** Antes de assumir uma pós-graduação, você precisa de respostas

**Texto da página:**

Uma pós-graduação é um compromisso de longo prazo, com mensalidades e módulos presenciais. Antes de se matricular, você quer saber se a especialidade é a certa, quanto vai pagar por mês e se a turma e a viagem cabem na sua rotina.

As dúvidas mais comuns antes de decidir:
- Quanto fica a mensalidade se eu conseguir uma bolsa?
- A bolsa vale para qual turma e em qual cidade?
- Vale pagar para tentar?
- E se eu não passar?

[SUPOSIÇÃO: as quatro dúvidas são hipóteses da persona P4 (H-PB3 e H-PB7 da pesquisa de persona), não citações de candidato. Trocar pelas frases reais quando as conversas anonimizadas chegarem.]

---

### 1.3 Solução

**H2:** A prova de bolsa deixa você tentar antes de decidir

**Texto da página:**

Com a inscrição de R$ 100,00, você faz a prova da sua especialidade e disputa uma das 11 bolsas daquela prova. A matrícula só entra depois do resultado, dentro do prazo de 10 dias úteis para quem for aprovado.

As bolsas de cada prova são estas:
- 2 bolsas de 50% (monitoria)
- 4 bolsas de 25%
- 5 bolsas de 10%

A prova é presencial e tem questões de múltipla escolha e dissertativas. A nota de corte é 7,0, o que equivale a no mínimo 70% de acerto.

Nenhuma bolsa é garantida. O resultado da prova define quem recebe cada bolsa.

---

### 1.4 Como funciona, da inscrição à matrícula

**H2:** Como funciona a prova de bolsa da Pós-graduação

**Texto da página (passo a passo):**

1. **Escolha a sua prova.** Procure a sua especialidade e a sua cidade na tabela abaixo.
2. **Inscreva-se.** Clique em "Inscrever-me na prova" na linha da sua prova e pague a inscrição de R$ 100,00 (Pix ou boleto à vista, ou 1x no cartão).
3. **Faça a prova.** Vá à prova na sexta-feira, 27 de novembro de 2026, das 9h às 13h. Leve documento com foto. Celular e relógios não são permitidos.
4. **Receba o resultado.** O resultado é informado por WhatsApp ou e-mail. [CONFIRMAR data de divulgação; sem a data, a página não cita data]
5. **Recorra, se precisar.** O prazo para recorrer é de 2 dias úteis depois da divulgação do resultado.
6. **Matricule-se, se for aprovado.** Quem é aprovado tem até 10 dias úteis para fazer a matrícula. [CONFIRMAR: 12 páginas de prova ainda dizem 7 dias; ver seção 3]

Observação para quem vem de outra cidade (texto da analise-cro, ajustado): a prova é presencial. Se você mora fora de São Paulo ou de Goiânia, planeje a viagem com antecedência e reserve passagem e hospedagem só depois de se inscrever. [CONFIRMAR se existe outra data ou outro local]

---

### 1.5 Tabela das provas

**H2:** Especialidades com prova

**Texto de abertura:** Todas as provas são em 27/11/2026, das 9h às 13h, presenciais, com inscrição de R$ 100,00 e as mesmas regras. Escolha a sua especialidade e a sua cidade.

**Como mostrar (design):** no computador, tabela com filtro por cidade e por especialidade. No celular, um cartão por prova, com o botão "Inscrever-me na prova" dentro do cartão. Ordem: por área e, dentro da área, São Paulo antes de Goiânia.

**Regra da coluna "Turma de destino":** o texto público só aparece depois da confirmação da Ufape. Enquanto a linha estiver com [CONFIRMAR destino], a célula mostra "Destino a informar pela Ufape" ou a linha fica oculta (ver gates na seção 8). Sem data de início e sem preço da turma na tabela do hub. O investimento da pós aparece na página da turma de destino, com a condição completa.

| Código | Área da prova (Pós-graduação em) | Cidade | Turma de destino (briefing) | Conteúdo programático na página da prova (em 26/10/2026) | Link da página de inscrição |
|---|---|---|---|---|---|
| 68639 | Anestesiologia Veterinária | São Paulo | [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68639/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/sao-paulo |
| 68640 | Anestesiologia Veterinária | Goiânia | 68609, Pós-graduação em Anestesiologia Veterinária, Goiânia [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68640/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/goiania |
| 68641 | Cardiologia Veterinária | São Paulo | [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68641/prova-de-bolsa-de-estudos-para-cardiologia-veterinaria/sao-paulo [CONFIRMAR link: ver correção 2 da seção 3] |
| 68642 | Cardiologia Veterinária | Goiânia | 289, Pós-graduação em Cardiologia Veterinária, Goiânia [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68642/prova-de-bolsa-de-estudos-para-cardiologia-veterinaria/goiania [CONFIRMAR link: ver correção 2 da seção 3] |
| 68659 | Pneumologia Veterinária | São Paulo | 68636, Pós-graduação em Pneumologia Veterinária, São Paulo [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68659/prova-de-bolsa-de-estudos-para-pneumologia-veterinaria/sao-paulo |
| 68645 | Clínica Médica e Emergência Veterinária | São Paulo | 68635, Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, São Paulo [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68645/prova-de-bolsa-de-estudos-para-clinica-medica-e-emergencia-veterinaria/sao-paulo |
| 68660 | Terapia Intensiva Veterinária | São Paulo | [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68660/prova-de-bolsa-de-estudos-para-terapia-intensiva-veterinaria/sao-paulo |
| 68643 | Clínica Cirúrgica de Cães e Gatos | São Paulo | [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68643/prova-de-bolsa-pos-graduacao-clinica-cirurgica-de-caes-e-gatos/sao-paulo |
| 68644 | Clínica Cirúrgica de Cães e Gatos | Goiânia | 68632, Pós-graduação em Clínica Cirúrgica de Cães e Gatos, Goiânia (presencial) [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68644/prova-de-bolsa-pos-graduacao-clinica-cirurgica-de-caes-e-gatos/goiania |
| 68647 | Diagnóstico por Imagem | São Paulo | [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68647/prova-de-bolsa-de-estudos-para-diagnostico-por-imagem/sao-paulo |
| 68661 | Ultrassonografia em Pequenos Animais | São Paulo | 68629, Pós-graduação em Ultrassonografia de Pequenos Animais, São Paulo [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68661/prova-de-bolsa-de-estudos-para-ultrassonografia-em-pequenos-animais/sao-paulo |
| 68649 | Endoscopia Veterinária | São Paulo | [CONFIRMAR destino e se a prova segue à venda] | Não | https://faculdade.ufape.com.br/produto/68649/prova-de-bolsa-de-estudos-para-endoscopia-veterinaria/sao-paulo |
| 68650 | Gastroenterologia Veterinária | São Paulo | [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68650/prova-de-bolsa-pos-graduacao-gastroenterologia/sao-paulo |
| 68648 | Endocrinologia de Pequenos Animais | São Paulo | 68617, Pós-graduação em Endocrinologia de Pequenos Animais, São Paulo [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68648/prova-de-bolsa-pos-graduacao-endocrinologia-de-pequenos-animais/sao-paulo |
| 68653 | Nefrologia e Urologia Veterinária | São Paulo | [CONFIRMAR destino e se a prova segue à venda] | Sim | https://faculdade.ufape.com.br/produto/68653/prova-de-bolsa-pos-graduacao-nefrologia-e-urologia/sao-paulo |
| 68646 | Dermatologia Veterinária | São Paulo | [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68646/prova-de-bolsa-de-estudos-para-dermatologia-veterinaria/sao-paulo |
| 68657 | Oncologia Veterinária | São Paulo | 68628, Pós-graduação em Oncologia Veterinária, São Paulo [CONFIRMAR destino] | Sim | https://faculdade.ufape.com.br/produto/68657/prova-de-bolsa-pos-graduacao-oncologia-veterinaria/sao-paulo |
| 68651 | Hematologia Veterinária | São Paulo | [CONFIRMAR destino] | Só bibliografia | https://faculdade.ufape.com.br/produto/68651/prova-de-bolsa-de-estudos-para-hematologia-veterinaria/sao-paulo |
| 68658 | Patologia Clínica Veterinária | São Paulo | 68615, Pós-graduação em Patologia Clínica, São Paulo [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68658/prova-de-bolsa-de-estudos-para-patologia-clinica-veterinaria/sao-paulo |
| 68654 | Neurologia e Neurocirurgia Veterinária | São Paulo | 68616, Pós-graduação em Neurologia e Neurocirurgia Veterinária, São Paulo [CONFIRMAR destino] | Não | https://faculdade.ufape.com.br/produto/68654/prova-de-bolsa-de-estudos-para-neurologia-e-neurocirurgia-veterinaria/sao-paulo |
| 68652 | Medicina de Felinos | São Paulo | [CONFIRMAR destino e se a prova segue à venda] | Sim | https://faculdade.ufape.com.br/produto/68652/prova-de-bolsa-pos-graduacao-medicina-de-felinos/sao-paulo |
| 68655 | Odontologia Veterinária | São Paulo | [CONFIRMAR destino e se a prova segue à venda] | Não | https://faculdade.ufape.com.br/produto/68655/prova-de-bolsa-pos-graduacao-odontologia-veterinaria/sao-paulo |

Conferência da tabela: 22 linhas, 19 em São Paulo e 3 em Goiânia (68640, 68642, 68644). A prova de Oftalmologia (68656, "encerrado, link fora do ar" no catálogo) e as 13 provas antigas com "sem venda (avise-me)" não aparecem. Nenhuma linha mostra data de início de turma nem preço de turma. Os dados de cada turma candidata ficam no Anexo A.

**Link com medição:** o botão de cada linha leva à página da prova no endereço acima, sem UTM nova no link interno (UTM em link interno apaga a origem do visitante no GA4). A origem do clique vai como parâmetro do evento (seção 8.3). Links externos que trazem o visitante ao hub usam o padrão da campanha: utm_source, utm_medium, utm_campaign=provas-de-bolsa-2026-11-27 e utm_content=<área>-<código da prova> [SUPOSIÇÃO de padrão; o arquiteto-de-fluxos confere].

---

### 1.6 Regras exatas da prova

**H2:** Quantas bolsas e quais percentuais

**Texto da página:**

Cada prova tem 11 bolsas:

| Quantidade | Percentual da bolsa |
|---|---|
| 2 bolsas | 50% (monitoria) |
| 4 bolsas | 25% |
| 5 bolsas | 10% |

Nenhuma bolsa é garantida. Como as 11 bolsas são distribuídas entre os aprovados: [CONFIRMAR regra de ordem]. Em caso de empate, o critério é a análise de currículo.

**H2:** Datas, local e inscrição

| Item | Regra |
|---|---|
| Data e horário | Sexta-feira, 27 de novembro de 2026, das 9h às 13h |
| Formato | Prova presencial, com questões de múltipla escolha e dissertativas |
| Inscrição | R$ 100,00, à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão |
| Local em São Paulo | Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100 |
| Local em Goiânia | [CONFIRMAR endereço em Goiânia; as páginas atuais mostram o endereço de São Paulo] |
| No dia | Leve documento com foto. Celular e relógios não são permitidos. Chegue com antecedência. |
| Prazo para se inscrever | [CONFIRMAR data-limite; sem a data, a página não escreve "inscrições até"] |

**H2:** Resultado, recurso e matrícula

| Item | Regra |
|---|---|
| Nota de corte | 7,0 (no mínimo 70% de acerto) |
| Resultado | Informado por WhatsApp ou e-mail. [CONFIRMAR data de divulgação] |
| Recurso | 2 dias úteis depois da divulgação do resultado |
| Matrícula | Até 10 dias úteis depois do resultado, para quem for aprovado. [CONFIRMAR: 10 dias úteis ou 7 dias, pois 12 páginas divergem] |
| Desempate | Análise de currículo |
| A bolsa | Não é acumulativa e é intransferível |
| Turma | A turma é confirmada quando atinge o número mínimo de alunos: [CONFIRMAR 15 ou 20]. Reserve passagem e hotel dos módulos só depois da confirmação da turma. |

Nota de redação: a grafia "intransferível" está correta aqui. As páginas atuais das provas escrevem "intrasferível" (correção G6, seção 3).

---

### 1.7 Provas: seção de confiança

**H2:** Quem está por trás da prova e como falar com a gente

**O que esta seção mostra, e o que ela deliberadamente não mostra:**

Mostra: as regras publicadas antes de você pagar; quem organiza; os contatos oficiais; o que acontece com os seus dados. Não mostra depoimento, nome de aprovado, foto de aluno, nome de docente, número de inscritos, número de aprovados, nota do MEC ou frase de certificação. Motivo: nenhuma autorização de uso de imagem, voz ou nome está registrada [CONFIRMAR autorização], nenhum número real de inscritos existe hoje e o texto oficial de certificação ainda não existe [PREENCHER COM A REGULAÇÃO].

**Texto da página:**

**Regras na mesa antes de pagar.** Quantas bolsas, qual percentual, qual nota de corte, quanto tempo para recorrer e para se matricular: tudo está nesta página antes da inscrição.

**Quem organiza.** A prova é da Faculdade UFAPE, com sede em São Paulo (Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100). Razão social: UFAPE CURSOS ESPECIALIZADOS LTDA, CNPJ 27.409.162/0001-34. [CONFIRMAR grafia da razão social]

**Fale com quem responde:**
- Vendas São Paulo: WhatsApp (11) 91366-9290
- Vendas Goiânia: WhatsApp (62) 9420-1847 [CONFIRMAR o número: o contexto traz 8 dígitos depois do DDD]
- Secretaria: WhatsApp (11) 97492-8443 ou telefone (11) 5054-1204, e-mail duvidas@intercursos.com.br, de segunda a sexta, das 9h às 18h
- SAC: sac@intercursos.com.br. Ouvidoria: ouvidoria@intercursos.com.br

**Seus dados.** Usamos o seu nome e o seu contato só para a inscrição, o aviso da prova e a resposta às suas dúvidas. Política de privacidade: [CONFIRMAR link]. O texto copiado das páginas atuais não mostra finalidade de uso dos dados nem link para a política no checkout [CONFIRMAR no site].

---

### 1.8 Oferta e o que está incluído

**H2:** O que a bolsa cobre e o que não cobre

**Texto da página:**

**O que você paga para fazer a prova.** A inscrição é de R$ 100,00, à vista (Pix ou boleto) ou 1x no cartão. Ela dá direito à participação na prova de 27/11/2026 e ao resultado, informado por WhatsApp ou e-mail. [CONFIRMAR o que mais a inscrição inclui; esta página não promete material de estudo]

**O que a bolsa é.** Um desconto de 10%, 25% ou 50% na pós-graduação de destino, para quem receber bolsa. A base de cálculo (mensalidades, valor total ou matrícula) ainda não está publicada: [CONFIRMAR base de cálculo]. Esta página não calcula valor de mensalidade com bolsa. A Ufape informa o valor por turma de destino [CONFIRMAR].

**O que fica de fora ou depende de regra:**
- A bolsa é intransferível: vale só para quem fez a prova.
- A bolsa não é acumulativa. [CONFIRMAR o alcance: se não soma com outros descontos da Ufape, como o desconto de aluno e ex-aluno ou promoções de turma] [SUPOSIÇÃO de leitura]
- A matrícula da pós de destino tem valor próprio: R$ 250,00 na maioria das turmas e R$ 350,00 na Pós-graduação em Ultrassonografia de Pequenos Animais (catálogo, seção 2). [CONFIRMAR se a bolsa incide sobre a matrícula]
- Passagem e hospedagem para a prova e para os módulos presenciais ficam por sua conta [SUPOSIÇÃO: o catálogo não lista viagem entre os itens da pós].
- A bolsa de monitoria (50%) pode ter contrapartida. [CONFIRMAR o que a monitoria exige; até lá a página escreve só "50% (monitoria)"]
- Quem é aprovado e não recebe bolsa: [CONFIRMAR regra do aprovado sem bolsa]

**Condições da pós de destino (modelo de frase, para preencher por turma depois da confirmação do destino; texto-padrão da estratégia de oferta):**
"Investimento da pós: [N]x de R$ [parcela] no cartão ou boleto (total de R$ [total]), mais matrícula de R$ [matrícula]. A 1ª mensalidade é paga até 30 dias antes do início. [CONFIRMAR para cada turma] Valores sem o desconto da bolsa."
Os valores de cada turma candidata estão no Anexo A, copiados do catálogo e sem desconto aplicado.

Regras desta seção: nenhum valor com bolsa calculado, nenhuma comparação de preço, nenhum "de R$ X por R$ Y", nenhum desconto de turma citado (a promoção de Medicina Interna Equina e os descontos de Anestesiologia Locorregional e Ventilação Mecânica não entram: sem regra completa no catálogo).

---

### 1.9 Objeções e perguntas frequentes

**H2:** Perguntas frequentes sobre a prova de bolsa

As perguntas F1 a F16 têm resposta confirmada (fatos do catálogo, do contexto da linha e das páginas das provas). Elas aparecem na página e viram o FAQPage do JSON-LD, com o mesmo texto. As perguntas PF1 a PF15 dependem de resposta da Ufape: ficam ocultas e fora do JSON-LD até a confirmação. Várias delas são o que os assistentes de IA recebem (ver seção 2.5).

#### Perguntas publicáveis hoje

**F1. O que é a prova de bolsa da pós-graduação da Faculdade UFAPE?**
É uma prova presencial, por especialidade, que define bolsas parciais de 10%, 25% e 50% para a pós-graduação da Faculdade UFAPE. A inscrição custa R$ 100,00 e a prova acontece em 27 de novembro de 2026.

**F2. Quanto custa a inscrição na prova de bolsa?**
R$ 100,00, à vista (Pix ou boleto) ou em 1x de R$ 100,00 no cartão.

**F3. Quando é a prova e qual é o horário?**
Na sexta-feira, 27 de novembro de 2026, das 9h às 13h.

**F4. A prova de bolsa é presencial? Existe versão online?**
A prova é presencial, em São Paulo ou em Goiânia, conforme a prova escolhida. Não há versão online.

**F5. Quantas bolsas existem e de quanto são?**
Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.

**F6. Qual é a nota de corte?**
A nota de corte é 7,0, que equivale a no mínimo 70% de acerto.

**F7. Como é a prova?**
A prova tem questões de múltipla escolha e dissertativas.

**F8. O que preciso levar e o que não posso levar?**
Leve documento com foto. Celular e relógios não são permitidos no dia da prova.

**F9. Como recebo o resultado?**
O resultado é informado por WhatsApp ou e-mail.

**F10. Posso recorrer do resultado?**
Sim. O prazo para recorrer é de 2 dias úteis depois da divulgação do resultado.

**F11. Quanto tempo tenho para me matricular depois do resultado?**
Quem for aprovado tem até 10 dias úteis para fazer a matrícula.

**F12. Preciso me matricular antes de fazer a prova?**
Não. Você se inscreve na prova por R$ 100,00 e decide sobre a matrícula depois do resultado, dentro do prazo.

**F13. A bolsa pode ser transferida para outra pessoa ou somada a outras?**
A bolsa é intransferível e não é acumulativa.

**F14. Como é feito o desempate?**
O desempate é feito por análise de currículo.

**F15. Quem organiza a prova de bolsa?**
A Faculdade UFAPE organiza a prova. A sede fica na Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100. A razão social é UFAPE CURSOS ESPECIALIZADOS LTDA, CNPJ 27.409.162/0001-34. Esta página não é da universidade federal de mesma sigla.
[SUPOSIÇÃO: a homonímia com a universidade federal aparece na pesquisa de palavras-chave, QT6. CONFIRMAR grafia da razão social.]

**F16. Como a prova de bolsa da Faculdade UFAPE se compara com a de outras instituições?**
Cada instituição define as suas próprias regras, taxa de inscrição e número de bolsas. Aqui estão as da Faculdade UFAPE: inscrição de R$ 100,00, 11 bolsas por prova (2 de 50%, 4 de 25% e 5 de 10%) e nota de corte 7,0. Para comparar, leia as regras publicadas por cada instituição.

#### Perguntas que dependem da Ufape (ocultas até a confirmação)

Cada item traz a resposta provisória para o time de vendas e a marca do que falta. Nenhuma resposta provisória vai para a página.

| # | Pergunta | Resposta provisória (só interna) | O que falta |
|---|---|---|---|
| PF1 | Para qual turma a bolsa vale? | "A turma de destino de cada prova está na tabela." | Destino de cada prova (A-C2). A ficha 68661 diz "pós-graduações participantes com início no primeiro semestre de 2027": conferir se vale para todas as provas [SUPOSIÇÃO de que vale] |
| PF2 | Posso fazer a prova em uma cidade e cursar em outra? | Sem resposta | [CONFIRMAR] |
| PF3 | Se eu passar e não receber bolsa, posso me matricular sem bolsa? | Sem resposta | [CONFIRMAR regra do aprovado sem bolsa] |
| PF4 | O que é a bolsa de monitoria? | "É a bolsa de 50%." | [CONFIRMAR o que a monitoria exige: horas, atividades, contrapartida] |
| PF5 | Como as 11 bolsas são distribuídas? | Sem resposta | [CONFIRMAR ordem: por nota, com desempate por currículo?] |
| PF6 | Até quando posso me inscrever? | Sem resposta | [CONFIRMAR data-limite] |
| PF7 | Quando sai o resultado? | "Por WhatsApp ou e-mail." | [CONFIRMAR data] |
| PF8 | E se eu não puder comparecer? A inscrição é devolvida? | Sem resposta. Nenhuma devolução é prometida | [CONFIRMAR política de ausência e de devolução] |
| PF9 | O que cai na prova? | "Parte das páginas das provas traz conteúdo programático e bibliografia sugerida (coluna da tabela)." | [CONFIRMAR conteúdo das provas sem material publicado: 9 páginas sem conteúdo e 1 só com bibliografia] |
| PF10 | Onde será a prova em Goiânia? | Sem resposta | [CONFIRMAR local] |
| PF11 | Quem pode se inscrever? | "A pós é para quem é formado em Medicina Veterinária." (contexto da linha) | [CONFIRMAR o requisito de inscrição na prova] |
| PF12 | Qual é o número mínimo para a turma abrir e o que acontece se ela não fechar? | "A turma é confirmada quando atinge o número mínimo." | [CONFIRMAR 15 ou 20, e a regra de devolução se a turma não for confirmada] |
| PF13 | Quanto fica a mensalidade com a bolsa? | "Veja a página da turma; o valor com bolsa é informado pela Ufape." Sem cálculo | [CONFIRMAR base de cálculo e publicar valor por turma (PR9)] |
| PF14 | A matrícula é em até 10 dias úteis depois do resultado mesmo que a turma comece só em 2027? Quando começo a pagar? | Sem resposta | [CONFIRMAR]: as turmas candidatas começam entre março e maio de 2027, e o prazo de matrícula cai em dezembro de 2026 |
| PF15 | Posso usar a bolsa junto com outro desconto? | "A bolsa não é acumulativa." | [CONFIRMAR o alcance] |

---

### 1.10 Chamada final

**H2:** Escolha a sua prova

**Texto da página:**

A prova é em 27 de novembro de 2026, das 9h às 13h. Escolha a sua especialidade e a sua cidade, faça a inscrição de R$ 100,00 e decida sobre a matrícula só depois do resultado.

**Botão principal:** Ver as provas e me inscrever (volta à tabela)
**Botão secundário:** Falar com o time no WhatsApp

Sem contador, sem "últimas vagas", sem frase de pressão. Só a data da prova, que é um fato.

---

### 1.11 Formulário, WhatsApp e hierarquia de botões

**Formulário curto (secundário, abaixo da chamada final e no rodapé do cartão do WhatsApp):**

- **Título:** Quer ajuda para escolher a prova?
- **Frase de apoio:** Deixe o seu contato e o time de vendas responde às suas dúvidas em horário comercial. [CONFIRMAR horário e responsável]
- **Campos (só o necessário):**
  1. Nome (obrigatório)
  2. WhatsApp com DDD (obrigatório)
  3. E-mail (opcional)
  4. Especialidade de interesse (lista das áreas da tabela, mais "ainda não sei")
  5. Cidade da prova (São Paulo, Goiânia ou "ainda não sei")
  6. Caixa de consentimento, desmarcada: "Concordo em receber contato da Faculdade UFAPE por WhatsApp e e-mail sobre a prova de bolsa. Posso sair quando quiser. Política de privacidade: [CONFIRMAR link]"
- **Botão:** Quero ajuda para escolher
- **Mensagem depois do envio:** "Recebemos o seu contato. Se preferir, fale agora no WhatsApp." [CONFIRMAR prazo de resposta]
- **Quem recebe o lead:** CRM [CONFIRMAR ferramenta]. O lead chega com prova de interesse, cidade, consentimento e origem (UTM). Dado pessoal fica no CRM, nunca na squad.

**Botão de WhatsApp:**
- Dois botões, um por unidade: "WhatsApp São Paulo" ((11) 91366-9290) e "WhatsApp Goiânia" ((62) 9420-1847 [CONFIRMAR número]).
- Mensagem pré-preenchida sugerida: "Olá, quero saber sobre a prova de bolsa de [especialidade] em [cidade]." [SUPOSIÇÃO de texto; a Ufape aprova]
- O site informou instabilidade no WhatsApp interno em 22/10/2026 (contexto/ufape-geral.md): testar os dois números no celular antes de publicar [CONFIRMAR].

**Hierarquia de botões (uma chamada principal por tela):**

| Nível | Botão | Onde | Estilo | Ação |
|---|---|---|---|---|
| Principal | Ver as provas e me inscrever | Topo e chamada final | Cor cheia, maior peso visual | Rola até a tabela |
| Principal, por linha | Inscrever-me na prova | Em cada linha da tabela (cartão no celular) | Cor cheia, tamanho médio | Abre a página da prova no endereço da tabela |
| Secundário | Falar com o time no WhatsApp | Topo, ao lado da tabela e no rodapé | Contorno, sem cor cheia | Abre o WhatsApp da unidade |
| Terciário | Quero ajuda para escolher | Formulário | Cor cheia só dentro do formulário | Envia o lead |
| Terciário | Ver as regras completas | Texto do topo | Link de texto | Rola até a seção 1.6 |
| Barra fixa no celular | Inscrever-me (leva à tabela) e ícone do WhatsApp | Rodapé fixo da tela | Compacta | Mesmas ações do topo |

Regras: nenhum botão com o rótulo "COMPRAR" (a página atual usa o mesmo rótulo de produto para uma inscrição); nenhum botão que disfarça propaganda de outra oferta; um único botão cheio visível por vez no celular.

---

# 2. SEO, GEO E JSON-LD

## 2.1 Notas de SEO

| Item | Proposta | Observação |
|---|---|---|
| Palavra principal | prova de bolsa pós-graduação veterinária | Uma única página por palavra principal (hub T1). Pontuação 60 (28/14/18) na pesquisa de palavras-chave |
| Palavras secundárias | como funciona a prova de bolsa de pós veterinária; prova de bolsa Ufape; prova de bolsa 27 de novembro; bolsa de estudos pós em medicina veterinária; prova de bolsa pós em Goiânia; prova de bolsa pós em São Paulo; quanto custa a inscrição da prova de bolsa; quantas bolsas tem a prova | Nomes populares ("pós vet") só em lista de palavras e grupo de anúncio, nunca em texto visível |
| Título SEO (até 60 caracteres) | Prova de Bolsa de Estudos da Pós-graduação, Faculdade UFAPE | 59 caracteres. A marca "Faculdade UFAPE" separa da universidade federal de mesma sigla |
| Título alternativo | Prova de Bolsa da Pós-graduação Veterinária, Faculdade UFAPE | 59 caracteres; inclui "veterinária" da palavra principal |
| Descrição (até 155 caracteres) | Prova de bolsa para a pós-graduação da Faculdade UFAPE em 27/11/2026, em São Paulo e Goiânia. Veja as especialidades, as regras e como se inscrever. | 148 caracteres. Sem número de provas, porque as linhas D4 podem ficar ocultas |
| H1 | Prova de bolsa de estudos da Pós-graduação | Um H1 só |
| H2 (nesta ordem na página) | Antes de assumir uma pós-graduação, você precisa de respostas; A prova de bolsa deixa você tentar antes de decidir; Como funciona a prova de bolsa da Pós-graduação; Especialidades com prova; Quantas bolsas e quais percentuais; Datas, local e inscrição; Resultado, recurso e matrícula; Quem está por trás da prova e como falar com a gente; O que a bolsa cobre e o que não cobre; Perguntas frequentes sobre a prova de bolsa; Escolha a sua prova | Cobre os 7 H2 propostos na pesquisa (T1), com o bloco "Especialidades com prova" em tabela (um cartão por Pós-graduação em <área>) |
| URL sugerida | /pos-graduacao/prova-de-bolsa | [SUPOSIÇÃO: padrão do CMS, [CONFIRMAR]]. URL sem data para servir às próximas edições; a data fica no texto e no JSON-LD |
| Canonical | A própria URL do hub | Páginas individuais das provas linkam para o hub, e o hub linka para cada uma |
| Links internos | Hub para as 22 páginas de prova (tabela) e para a página da turma de destino (depois da confirmação). Cada página de prova para o hub | Âncora do link: "Prova de bolsa para a Pós-graduação em <área>" |
| Breadcrumb | Início, Pós-graduação, Prova de bolsa | |
| Imagem de compartilhamento | [CONFIRMAR: escolha do editor] | Sem foto de pessoa sem autorização; sem selo do MEC na arte |
| Indexação | Indexar | Páginas individuais mantêm indexação própria (uma palavra principal por página) |

## 2.2 Resposta citável (para buscadores e assistentes de IA)

Bloco de 57 palavras, no topo do corpo do texto, abaixo do primeiro parágrafo. Contém números porque o hub é uma página de regras, diferente da página de turma (a regra "sem número" do template vale para texto da plataforma em página de turma):

> A prova de bolsa da Faculdade UFAPE é uma prova presencial para quem quer cursar uma pós-graduação em medicina veterinária com bolsa parcial. Acontece em 27 de novembro de 2026, em São Paulo e em Goiânia, com inscrição de R$ 100,00. Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.

Só publicar depois de [CONFIRMAR NO CATÁLOGO] as regras da bolsa (hoje no contexto da linha e nas páginas das provas, não como coluna do catálogo).

## 2.3 Entidades que a página precisa nomear (e onde)

| Entidade | Onde citar |
|---|---|
| Faculdade UFAPE (primeira menção), Ufape (depois) | H1 em contexto, descrição, resposta citável, seção de confiança |
| Pós-graduação em <área> (nome padrão de cada especialidade) | Tabela, âncoras de links internos, FAQ |
| Prova de bolsa de estudos; bolsa de 10%, 25% e 50%; monitoria; nota de corte | Seção 1.3 e 1.6, FAQ |
| São Paulo, Goiânia | Tabela, regras, JSON-LD |
| Médico veterinário, Medicina Veterinária | Seção de solução e FAQ |
| Av. 9 de Julho, 3939, Jardim Paulista (local em São Paulo) | Regras e JSON-LD |

## 2.4 Consistência da marca (checagem da skill schema-de-curso, passo 4)

| Item | Situação |
|---|---|
| Nome | "Faculdade UFAPE" na primeira menção e "Ufape" depois, como o guia de marca. "Ufape Intercursos" não é usado como marca (aparece só nos endereços de e-mail oficiais). As páginas 68643 e 68644 usam "UFAPE - Intercursos" no texto: divergência registrada na correção G10 |
| Cidade e sede | São Paulo, Av. 9 de Julho, 3939, esquina com Honduras, 765 (contexto geral) |
| Modalidade da prova | Presencial em todas |
| Credenciamento | Não citado: o texto oficial de certificação da Pós ainda não existe. O credenciamento da Graduação não entra nesta página |
| Divergências com outras páginas | Ver seção 3 (endereço de Goiânia, regras de resultado e matrícula, nome "Medicina de Felinos Veterinária" no texto de 68652, "UFAPE - Intercursos") |

## 2.5 Perguntas para assistentes de IA que a página responde

Do roteiro da pesquisa de palavras-chave (QP1 a QP7) e das transversais (QT4, QT6, QT9):

| ID | Pergunta | Onde a página responde | Situação |
|---|---|---|---|
| QP1 | Como funciona a prova de bolsa da Ufape e quantas bolsas tem cada especialidade? | Seções 1.3, 1.4, 1.6; F1, F5 | Respondida |
| QP2 | Quanto custa a inscrição da prova de bolsa da Ufape e quando é a prova? | F2, F3 | Respondida |
| QP3 | A prova de bolsa da Ufape é presencial? Onde fazer? | F4 e seção "Datas, local e inscrição" | São Paulo respondida; Goiânia depende do local (PF10) |
| QP4 | O que cai na prova de bolsa de pós em medicina veterinária da Ufape? | PF9 e coluna "Conteúdo programático" da tabela | Parcial: 12 páginas com conteúdo, 1 só com bibliografia, 9 sem nada |
| QP5 | Se eu passar na prova de bolsa, em quanto tempo preciso me matricular e a bolsa vale para qual turma? | F11 e PF1 | Prazo respondido (10 dias úteis, a confirmar); turma depende do destino |
| QP6 | Prova de bolsa de pós veterinária: Ufape ou outra instituição, qual vale mais a pena? | F16 (sem nomear concorrente e sem ranking) | Respondida em termos neutros |
| QP7 | Posso acumular a bolsa com outro desconto da Ufape? | F13 e PF15 | Parcial: o alcance de "não acumulativa" depende da Ufape |
| QT6 | Faculdade UFAPE é a mesma coisa que a UFAPE de Pernambuco? | F15 | Respondida com nome, CNPJ e sede |
| QT9 | A pós da Ufape tem prova de bolsa? Qual é a inscrição? | F1, F2 | Respondida |

A coluna "Ufape aparece em assistentes" fica "conferir manualmente": a squad não consulta assistentes (roteiro da seção 8 da pesquisa de palavras-chave). Nenhuma taxa de citação foi inventada.

## 2.6 JSON-LD

Tipos usados, conforme a skill schema-de-curso e o pedido: EducationalOrganization (a instituição), EducationEvent (cada prova, porque a prova é um evento com data, local e preço, e a turma de destino ainda não está confirmada) e FAQPage (as perguntas F1 a F16, as mesmas do texto visível). Course e CourseInstance não entram no hub: pertencem às páginas das turmas, que a plataforma monta com os dados do banco. Person não entra (nenhum docente autorizado).

Todo campo tem fonte no catálogo, no contexto ou nas páginas das provas. Campo sem dado ficou de fora: logotipo, sameAs (URLs oficiais dos perfis a confirmar), rua do local em Goiânia, disponibilidade, validFrom e qualquer dado de turma. Preço aparece só como o da inscrição (R$ 100,00), nunca preço de curso. Nenhuma nota do MEC, nenhum ato regulatório e nenhuma frase de certificação.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "EducationalOrganization",
      "@id": "https://faculdade.ufape.com.br/#organizacao",
      "name": "Faculdade UFAPE",
      "legalName": "UFAPE CURSOS ESPECIALIZADOS LTDA",
      "url": "https://faculdade.ufape.com.br/",
      "telephone": "+55 11 5054-1204",
      "email": "duvidas@intercursos.com.br",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista",
        "addressLocality": "São Paulo",
        "addressRegion": "SP",
        "postalCode": "01407-100",
        "addressCountry": "BR"
      }
    },
    {
      "@type": "EducationEvent",
      "@id": "https://faculdade.ufape.com.br/produto/68639/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/sao-paulo#evento",
      "name": "Prova de Bolsa de Estudos para Anestesiologia Veterinária",
      "description": "Prova presencial de bolsa de estudos para a pós-graduação da Faculdade UFAPE, com questões de múltipla escolha e dissertativas.",
      "inLanguage": "pt-BR",
      "startDate": "2026-11-27T09:00:00-03:00",
      "endDate": "2026-11-27T13:00:00-03:00",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {
        "@type": "Place",
        "name": "Faculdade UFAPE, São Paulo",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista",
          "addressLocality": "São Paulo",
          "addressRegion": "SP",
          "postalCode": "01407-100",
          "addressCountry": "BR"
        }
      },
      "organizer": { "@id": "https://faculdade.ufape.com.br/#organizacao" },
      "offers": {
        "@type": "Offer",
        "price": "100.00",
        "priceCurrency": "BRL",
        "url": "https://faculdade.ufape.com.br/produto/68639/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/sao-paulo"
      }
    },
    {
      "@type": "EducationEvent",
      "@id": "https://faculdade.ufape.com.br/produto/68640/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/goiania#evento",
      "name": "Prova de Bolsa de Estudos para Anestesiologia Veterinária",
      "description": "Prova presencial de bolsa de estudos para a pós-graduação da Faculdade UFAPE, com questões de múltipla escolha e dissertativas.",
      "inLanguage": "pt-BR",
      "startDate": "2026-11-27T09:00:00-03:00",
      "endDate": "2026-11-27T13:00:00-03:00",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {
        "@type": "Place",
        "name": "Goiânia",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Goiânia",
          "addressRegion": "GO",
          "addressCountry": "BR"
        }
      },
      "organizer": { "@id": "https://faculdade.ufape.com.br/#organizacao" },
      "offers": {
        "@type": "Offer",
        "price": "100.00",
        "priceCurrency": "BRL",
        "url": "https://faculdade.ufape.com.br/produto/68640/prova-de-bolsa-pos-graduacao-anestesiologia-veterinaria/goiania"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "O que é a prova de bolsa da pós-graduação da Faculdade UFAPE?",
          "acceptedAnswer": { "@type": "Answer", "text": "É uma prova presencial, por especialidade, que define bolsas parciais de 10%, 25% e 50% para a pós-graduação da Faculdade UFAPE. A inscrição custa R$ 100,00 e a prova acontece em 27 de novembro de 2026." }
        },
        {
          "@type": "Question",
          "name": "Quanto custa a inscrição na prova de bolsa?",
          "acceptedAnswer": { "@type": "Answer", "text": "R$ 100,00, à vista (Pix ou boleto) ou em 1x de R$ 100,00 no cartão." }
        },
        {
          "@type": "Question",
          "name": "Quando é a prova e qual é o horário?",
          "acceptedAnswer": { "@type": "Answer", "text": "Na sexta-feira, 27 de novembro de 2026, das 9h às 13h." }
        },
        {
          "@type": "Question",
          "name": "A prova de bolsa é presencial? Existe versão online?",
          "acceptedAnswer": { "@type": "Answer", "text": "A prova é presencial, em São Paulo ou em Goiânia, conforme a prova escolhida. Não há versão online." }
        },
        {
          "@type": "Question",
          "name": "Quantas bolsas existem e de quanto são?",
          "acceptedAnswer": { "@type": "Answer", "text": "Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%." }
        },
        {
          "@type": "Question",
          "name": "Qual é a nota de corte?",
          "acceptedAnswer": { "@type": "Answer", "text": "A nota de corte é 7,0, que equivale a no mínimo 70% de acerto." }
        },
        {
          "@type": "Question",
          "name": "Como é a prova?",
          "acceptedAnswer": { "@type": "Answer", "text": "A prova tem questões de múltipla escolha e dissertativas." }
        },
        {
          "@type": "Question",
          "name": "O que preciso levar e o que não posso levar?",
          "acceptedAnswer": { "@type": "Answer", "text": "Leve documento com foto. Celular e relógios não são permitidos no dia da prova." }
        },
        {
          "@type": "Question",
          "name": "Como recebo o resultado?",
          "acceptedAnswer": { "@type": "Answer", "text": "O resultado é informado por WhatsApp ou e-mail." }
        },
        {
          "@type": "Question",
          "name": "Posso recorrer do resultado?",
          "acceptedAnswer": { "@type": "Answer", "text": "Sim. O prazo para recorrer é de 2 dias úteis depois da divulgação do resultado." }
        },
        {
          "@type": "Question",
          "name": "Quanto tempo tenho para me matricular depois do resultado?",
          "acceptedAnswer": { "@type": "Answer", "text": "Quem for aprovado tem até 10 dias úteis para fazer a matrícula." }
        },
        {
          "@type": "Question",
          "name": "Preciso me matricular antes de fazer a prova?",
          "acceptedAnswer": { "@type": "Answer", "text": "Não. Você se inscreve na prova por R$ 100,00 e decide sobre a matrícula depois do resultado, dentro do prazo." }
        },
        {
          "@type": "Question",
          "name": "A bolsa pode ser transferida para outra pessoa ou somada a outras?",
          "acceptedAnswer": { "@type": "Answer", "text": "A bolsa é intransferível e não é acumulativa." }
        },
        {
          "@type": "Question",
          "name": "Como é feito o desempate?",
          "acceptedAnswer": { "@type": "Answer", "text": "O desempate é feito por análise de currículo." }
        },
        {
          "@type": "Question",
          "name": "Quem organiza a prova de bolsa?",
          "acceptedAnswer": { "@type": "Answer", "text": "A Faculdade UFAPE organiza a prova. A sede fica na Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100. A razão social é UFAPE CURSOS ESPECIALIZADOS LTDA, CNPJ 27.409.162/0001-34. Esta página não é da universidade federal de mesma sigla." }
        },
        {
          "@type": "Question",
          "name": "Como a prova de bolsa da Faculdade UFAPE se compara com a de outras instituições?",
          "acceptedAnswer": { "@type": "Answer", "text": "Cada instituição define as suas próprias regras, taxa de inscrição e número de bolsas. Aqui estão as da Faculdade UFAPE: inscrição de R$ 100,00, 11 bolsas por prova (2 de 50%, 4 de 25% e 5 de 10%) e nota de corte 7,0. Para comparar, leia as regras publicadas por cada instituição." }
        }
      ]
    }
  ]
}
```

**Como replicar o EducationEvent para as outras 20 provas:** cada prova usa nome, URL e cidade da tabela da seção 1.5, as mesmas datas, o mesmo preço e a mesma descrição. Para provas em São Paulo, o bloco "location" é igual ao de 68639. Para as provas de Goiânia (68642 e 68644), o bloco "location" é igual ao de 68640 e só ganha "streetAddress" depois de a Ufape confirmar o local. Provas ocultas na tabela (grupo D4, se a Ufape decidir) ficam fora do JSON-LD também. A plataforma nova monta esse JSON-LD pelo banco; este texto é a referência.

**Notas do JSON-LD:**
- A pergunta F11 usa "10 dias úteis" e só vale depois da correção das 12 páginas divergentes.
- O JSON-LD não pode ficar diferente do FAQ visível: se uma pergunta F for retirada da página, sai do código.
- As perguntas PF1 a PF15 não entram no JSON-LD até serem respondidas e publicadas.
- sameAs (Instagram @ufapevet e Facebook /Ufape): incluir quando a Ufape confirmar as URLs oficiais.
- Depois da prova: ver o item de pós-publicação do checklist (eventStatus e arquivo da página).

---

# 3. CORREÇÕES RECOMENDADAS NAS PÁGINAS INDIVIDUAIS DE PROVA

A squad não altera o site. Tudo abaixo é pedido de aprovação humana (A-C8 da campanha): o que muda, por que, efeito esperado e como desfazer. Nenhuma correção tem custo de mídia. Base: texto copiado nas fichas em 26/10/2026. Não abri o site, então o comportamento do botão e do checkout é [CONFIRMAR no site].

## Correção 1: 68640 com endereço de São Paulo (e o mesmo em 68642 e 68644)

- **O que a ficha mostra (evidência):** a página 68640 diz "Localidade: Goiânia", mas o bloco LOCAL e o campo Endereço trazem a Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo. As fichas 68642 e 68644 (as outras duas provas de Goiânia) têm o mesmo erro. As três fichas marcam "Alertas: nenhum".
- **Por que importa:** o candidato de Goiânia pode ir ao endereço errado no dia 27/11; a página de destino deixa de entregar o que o anúncio promete (conformidade, bloco Plataformas); risco de reclamação por informação errada (CDC).
- **O que mudar:** trocar o bloco LOCAL e o campo Endereço das três páginas pelo local real da prova em Goiânia [CONFIRMAR endereço completo]. Acrescentar a frase já usada em 68655 e 68660: "Pedimos que todos os participantes se organizem para chegar com antecedência."
- **Enquanto não corrigir:** o hub não mostra endereço de Goiânia; a linha de Goiânia aponta para o WhatsApp de vendas de Goiânia; nenhum anúncio de Goiânia cita endereço (regra da campanha); o time de vendas informa o local por mensagem.
- **Como conferir depois:** abrir as três páginas no celular e comparar a cidade da URL, o campo Localidade e o campo Local.
- **Efeito esperado:** menos risco de comparecimento no lugar errado [SUPOSIÇÃO]. **Como desfazer:** voltar ao texto anterior no site.

## Correção 2: links trocados das provas de Cardiologia (68641 e 68642)

- **O que o plano registra (P3):** os links das provas de Cardiologia de São Paulo e de Goiânia estão invertidos.
- **O que consegui conferir nas fichas (evidência):** os endereços das duas páginas batem com a cidade (68641 termina em /sao-paulo e 68642 termina em /goiania), mas os dois textos são idênticos; a página de Goiânia (68642) escreve "Pós-graduação em Cardiologia Veterinária da UFAPE - São Paulo" no texto e mostra o endereço de São Paulo. Onde os links se cruzam (botão COMPRAR, link na página da turma 289, planilha, anúncio) não aparece no texto copiado: [CONFIRMAR no site].
- **O que mudar:** (1) abrir os dois botões de inscrição e conferir o código e a cidade do produto no checkout; (2) trocar os links que estiverem invertidos; (3) no texto de 68642, trocar "São Paulo" por Goiânia e corrigir o endereço (correção 1); (4) aplicar as correções G1, G2 e G9 da seção 3.4, que também valem para as duas.
- **No hub:** as duas linhas de Cardiologia mostram o aviso [CONFIRMAR link] até o teste ser feito. Nenhum anúncio de Cardiologia sobe antes disso (regra da campanha).
- **Efeito esperado:** o candidato paga na prova da cidade certa. **Como desfazer:** voltar aos links anteriores.

## Correção 3: 68652 (Medicina de Felinos) com regras contraditórias e frase ligada ao MEC

Contradições na mesma página (evidência, ficha 68652):

| Tema | O que a página diz | Regra comum (contexto da linha) |
|---|---|---|
| Resultado | "Via email" (bloco de composição), "Via telefone (WhatsApp e/ou e-mail)" (considerações) e "no site da Faculdade Ufape" (regras) | WhatsApp ou e-mail |
| Matrícula | "até 10 dias (úteis)" (topo), "10 dias" (considerações) e "7 dias" (regras) | 10 dias úteis |
| Composição da prova | "10 a 20 questões objetivas e/ou dissertativas, totalizando 10 pontos" | Questões de múltipla escolha e dissertativas |
| Frase de reconhecimento | O texto de apresentação afirma que a pós é reconhecida pelo MEC | Nenhuma frase de certificação ou reconhecimento até a regulação aprovar o texto |
| Nome | "Pós-graduação em Medicina de Felinos Veterinária" no texto | Padrão "Pós-graduação em Medicina de Felinos" |
| Destino | Nenhuma turma de Felinos aberta no catálogo (650 já começou; "verificar") | Destino [CONFIRMAR] |

- **O que mudar:** manter só as regras comuns (resultado por WhatsApp ou e-mail, matrícula em 10 dias úteis, composição como nas outras provas, se a Ufape confirmar); apagar o bloco REGRAS duplicado; retirar a frase de reconhecimento ligada ao MEC (texto aprovado: [PREENCHER COM A REGULAÇÃO]); ajustar o nome. Manter o conteúdo programático e a bibliografia.
- **No hub:** a linha de 68652 fica oculta ou com "destino a informar" até a Ufape confirmar o destino e corrigir a página (grupo D4 da campanha). A página de destino de qualquer anúncio de Felinos fica sinalizada enquanto tiver a frase.
- **Efeito esperado:** uma só regra por prova; menos risco de propaganda enganosa. **Como desfazer:** voltar ao texto anterior.

## 3.4 Correções que valem para várias páginas (achados novos desta leitura das 22 fichas)

Estas correções não estavam no plano. Os dois primeiros itens mostram que o problema de regras contraditórias não é só de Felinos.

| # | Achado (evidência nas fichas) | Páginas | O que fazer |
|---|---|---|---|
| G1 | Frase de reconhecimento pelo MEC no texto de apresentação | 68641, 68642, 68643, 68644, 68645, 68648, 68650, 68651, 68652, 68653, 68655, 68657, 68659, 68660, 68661 (15 de 22) | Retirar. Texto aprovado: [PREENCHER COM A REGULAÇÃO] (pedido A7 do plano do cmo). As 7 sem a frase: 68639, 68640, 68646, 68647, 68649, 68654, 68658 |
| G2 | Bloco REGRAS repetido no fim da página, com "7 dias" para a matrícula (o resto da página diz 10 dias úteis) e resultado "no site da Faculdade UFAPE" ou "via email" (o resto diz WhatsApp e/ou e-mail) | 68641, 68642, 68643, 68644, 68645, 68650, 68651, 68652, 68653, 68657, 68659, 68661 (12 de 22) | Apagar o bloco repetido ou alinhar à regra comum que a Ufape confirmar. Sem isso, o hub contradiz a página aberta pelo botão |
| G3 | Provas de Goiânia com endereço de São Paulo | 68640, 68642, 68644 | Correção 1 |
| G4 | Links de Cardiologia | 68641, 68642 | Correção 2 |
| G5 | Composição da prova inconsistente: "múltipla escolha e dissertativas" (14 páginas), "10 a 20 questões objetivas e/ou dissertativas, totalizando 10 pontos" (8 páginas: 68641, 68642, 68645, 68650, 68651, 68652, 68653, 68657, 68659, e 68645 incluída na contagem de 68641 a 68659), "20 questões objetivas e/ou dissertativas" (68643 e 68644) | Todas | Uniformizar. [CONFIRMAR qual texto vale] |
| G6 | Grafia "intrasferível" ("não é acumulativa e é intrasferível") | As 22 | Corrigir para "intransferível" |
| G7 | Botão COMPRAR e rótulo "Valor" para uma inscrição de prova | As 22 | Trocar o botão por "Inscrever-me na prova de bolsa" e o rótulo por "Inscrição" (rótulo sugerido pela analise-cro) |
| G8 | Informações que faltam: turma de destino, prazo de inscrição, política de ausência, o que a monitoria exige, regra do aprovado sem bolsa, requisito para se inscrever, base de cálculo da bolsa | As 22 | Escrever as respostas que a Ufape confirmar (PF1 a PF15) e apontar para a turma de destino |
| G9 | Dados numéricos sem fonte no texto de apresentação: "Cerca de 60-65% dos casos" de afecções cardiológicas (68641, 68642), "aproximadamente 30% dos cães" com alteração hematológica, com citação de estudo (68651), "Cerca de 85% dos pacientes" (68655), "1 em cada 4 cães" e "principal causa de óbito" (68657) | 68641, 68642, 68651, 68655, 68657 | Citar fonte, período e amostra, ou retirar (conformidade: dados com fonte) |
| G10 | Superlativos sem fonte e contagem de turma divergente: "a primeira do Brasil", "referência nacional" e "7ª turma" (o catálogo registra a turma de Hematologia como VIII) | 68651 | Retirar superlativos sem fonte e conferir a turma no catálogo |
| G11 | "UFAPE - Intercursos" no texto como nome da instituição | 68643, 68644 | Usar "Faculdade UFAPE" (guia de marca: "Ufape Intercursos" não é marca de venda) |
| G12 | Parágrafo de apresentação repetido duas vezes; frase "bolsas parciais em pós-graduações participantes com início no primeiro semestre de 2027" que não aparece nas outras 21 | 68661 | Remover a repetição. Confirmar se a frase do primeiro semestre de 2027 vale para todas as provas (ver PF1) |
| G13 | Turma mínima: 15 na página da prova, 20 nas páginas de turma | As 22 | [CONFIRMAR qual vale e para o quê] |
| G14 | Regras de celular e de documento repetidas duas vezes na mesma página | As 22 | Manter uma vez |
| G15 | Checkout sem finalidade de uso dos dados nem link para a política de privacidade (no texto copiado) | As 22 | [CONFIRMAR no site]; incluir se faltar |
| G16 | Cada página não leva ao hub nem à turma de destino | As 22 | Acrescentar link para o hub e, depois da confirmação, para a turma de destino |

Conferência da contagem do G5 (para o editor): as 14 páginas com "múltipla escolha e dissertativas" são 68639, 68640, 68646, 68647, 68648, 68649, 68654, 68655, 68658, 68660, 68661 e as demais sem o texto de "questões objetivas", mais as duas de G5 acima; recomendo o editor recontar na hora de corrigir, porque esta linha foi contada a olho nas fichas. [CONFIRMAR contagem]

**Ordem recomendada de correção (impacto provável, [SUPOSIÇÃO]):** G3 e G4 (risco de comparecer ou pagar no lugar errado), G2 (regra visível que contradiz o hub), G1 (frase proibida em página de destino de anúncio), G7 e G8 (conversão), depois G5, G6, G9 a G16.

**Pedido de aprovação (formato do plano):** O que: correções 1 a 3 e G1 a G16 nas páginas das 22 provas. Por que: página de destino precisa entregar o que o hub e o anúncio prometem. Quanto: sem custo de mídia. Efeito esperado: menos risco de reclamação e de comparecimento errado; regras iguais em toda a campanha. Como desfazer: voltar ao texto anterior no site. Quem aprova: [CONFIRMAR quem aprova páginas e preços].

---

# 4. SEÇÃO PARA CRIAR O TIPO DE PÁGINA (recomendação ao cmo)

O template templates/pagina-da-turma.md não tem o tipo prova de bolsa. Sem ele, a plataforma nova não valida a página. Pedido ao cmo: abrir versão nova do template com o tipo "prova_de_bolsa" e as chaves sugeridas pela analise-cro (como_funciona, bolsas_previstas, regras, faq_bolsa, turma_de_destino) mais "hub" para esta página. Os campos de dado (data, horário, inscrição, bolsas, regras, local, turma de destino, link) vêm do banco, não do texto da IA. Banco, tabela e função nunca nascem na squad: o pedido vira item para o ufape-admin, único dono do banco compartilhado. Esta página não depende dessa decisão para ser publicada no site atual.

---

# 5. CHECKLIST DE PUBLICAÇÃO

Marque cada item antes de pedir a publicação. Item sem marcação bloqueia.

## 5.1 Decisões e confirmações da Ufape (bloqueiam a publicação)

- [ ] Destino de cada prova, ou decisão de ocultar a coluna e as linhas sem destino (A-C2)
- [ ] Decisão sobre as provas D4 (68649, 68652, 68653 e 68655): seguem à venda? Se não, linhas ocultas e fora do JSON-LD
- [ ] Decisão sobre Dermatologia (68646) e Hematologia (68651): as turmas 68610 e 68608 começam um dia depois da prova; qual turma recebe os aprovados
- [ ] Local da prova em Goiânia (ou as linhas de Goiânia ocultas)
- [ ] Links de Cardiologia testados no checkout (código e cidade conferidos)
- [ ] Regras unificadas: 10 dias úteis ou 7 dias; resultado por WhatsApp ou e-mail ou no site
- [ ] Turma mínima: 15 ou 20
- [ ] Prazo de inscrição na prova (se existir) e data de divulgação do resultado (a página não escreve datas sem confirmação)
- [ ] Regras que faltam respondidas: aprovado sem bolsa, monitoria, distribuição das 11 bolsas, ausência e devolução, requisito de inscrição, base de cálculo da bolsa
- [ ] Número do WhatsApp de Goiânia conferido (8 dígitos no contexto)
- [ ] Link da política de privacidade e texto de consentimento do formulário
- [ ] Quem aprova páginas e preços nomeado (tabela vazia em contexto/ufape-geral.md)

## 5.2 Conteúdo e conformidade

- [ ] Nenhuma frase de certificação, reconhecimento ou nota do MEC na página
- [ ] Nenhuma frase de escassez ou urgência sem número real; sem contador
- [ ] Nenhuma comparação com outra instituição (F16 só em termos neutros)
- [ ] Nenhum percentual de aprovação; nenhum número de inscritos; nenhuma promessa de bolsa, emprego, renda ou aprovação
- [ ] Nenhum valor de curso com bolsa calculado; nenhum desconto de turma citado
- [ ] Nenhum docente, aluno ou aprovado citado; nenhum depoimento
- [ ] "50%" sempre com a distribuição completa das 11 bolsas
- [ ] Nenhuma menção a "Black Friday" ou a promoção junto da prova (a prova cai em 27/11/2026)
- [ ] Nomes no padrão "Pós-graduação em <área>"; "Faculdade UFAPE" na primeira menção
- [ ] Português do Brasil, sem travessão nem meia-risca em nenhum lugar (texto, título, alt de imagem, botão, JSON-LD)
- [ ] Todo [CONFIRMAR] resolvido ou o trecho oculto
- [ ] Dados da tabela conferidos com catálogo, seção 3 (código, cidade, data, inscrição, status "aberto")

## 5.3 Design (resumo)

- [ ] Teste dos 5 segundos no celular passa (que página, para quem, formato e data, o que fazer)
- [ ] Um botão cheio por tela; hierarquia da seção 1.11 respeitada
- [ ] Tabela com filtro por cidade e por especialidade; cartões no celular
- [ ] Barra fixa no celular com "Inscrever-me" e WhatsApp
- [ ] Botões de WhatsApp de São Paulo e de Goiânia testados no celular
- [ ] Formulário com 4 campos obrigatórios no máximo (nome, WhatsApp, consentimento; e-mail opcional)
- [ ] Carregamento rápido no celular; sem pop-up que cubra o botão; contraste e tamanho de toque conferidos
- [ ] Imagem sem pessoa sem autorização, sem selo do MEC, com texto alternativo sem travessão

## 5.4 Rastreamento (GA4, Meta e Google Ads)

Nomes de evento são proposta [SUPOSIÇÃO]; o arquiteto-de-fluxos confere. Ferramenta de medição, CRM e checkout: [CONFIRMAR].

| Evento | Quando dispara | Parâmetros | GA4 | Pixel da Meta | Google Ads |
|---|---|---|---|---|---|
| visualização do hub | Carga da página | origem (utm), cidade se filtrada | page_view | PageView e ViewContent | Remarketing do hub (com consentimento) |
| prova_inscricao_clique | Clique em "Inscrever-me na prova" | prova_codigo, area, cidade, posicao_na_tabela, botao (tabela, topo, barra fixa) | evento e evento-chave | InitiateCheckout | Conversão secundária "Clique de inscrição" |
| generate_lead | Envio do formulário | prova_interesse, cidade, origem=hub | generate_lead e evento-chave | Lead | Conversão "Lead do hub" |
| whatsapp_clique | Clique em um dos botões de WhatsApp | unidade (sp ou go), posicao | evento e evento-chave | Contact | Conversão secundária "Clique no WhatsApp" |
| prova_inscricao_concluida | Confirmação de pagamento da inscrição, no checkout | prova_codigo, valor 100.00, moeda BRL, transaction_id | purchase (evento-chave principal) | Purchase com valor 100.00 BRL | Conversão principal "Inscrição na prova", valor 100.00 |
| filtro_uso | Uso do filtro da tabela | tipo (cidade ou especialidade), valor | evento | (nenhum) | (nenhum) |

- [ ] A conclusão do pagamento (compra de R$ 100,00) é medida na página de confirmação do checkout, não no hub. Se o checkout não permite tag, a Ufape informa e a medição fica por clique mais conciliação com o CRM [CONFIRMAR]
- [ ] UTM, gclid e fbclid preservados até o checkout; nenhum UTM em link interno
- [ ] Banner e modo de consentimento da LGPD ativos antes de disparar Pixel e tag do Google Ads [CONFIRMAR]
- [ ] Teste com GA4 DebugView, Meta Pixel Helper e Tag Assistant antes de subir anúncio
- [ ] Lead chega ao CRM com prova de interesse, cidade, consentimento e UTM; nenhum dado pessoal sai do CRM para a squad [CONFIRMAR CRM]
- [ ] Número de inscrições por prova registrado como número somado por prova (sem dado pessoal) para os pontos de checagem de 03/11, 09/11, 16/11, 23/11 e 30/11

## 5.5 Antes de subir anúncio

- [ ] Páginas de destino dos anúncios corrigidas (G1 a G4) ou o anúncio leva ao hub
- [ ] Anúncios de Cardiologia, de Goiânia com endereço e de Felinos só depois da correção (regra da campanha)

## 5.6 Depois da publicação e depois da prova

- [ ] Primeira leitura de cliques por linha da tabela e de envios do formulário em 03/11/2026 (primeiro ponto de checagem da campanha)
- [ ] Pedido de pausa dos anúncios de inscrição em 27/11/2026 (aprovação humana prévia)
- [ ] Em 28/11/2026: trocar os botões por aviso de que a prova foi realizada e apontar para a página das turmas; atualizar eventStatus e as datas do JSON-LD; manter a URL para a próxima edição
- [ ] Registrar presentes, aprovados e matrículas por prova (números somados), para as metas da próxima prova

## 5.7 Hipóteses de teste (para o desenho-de-experimentos refinar; não aprovadas)

Todas [SUPOSIÇÃO]. Sem tráfego e linha de base medidos, o teste vira leitura de antes e depois.

| # | Hipótese | Teste | Métrica principal | Métrica de proteção |
|---|---|---|---|---|
| H1 | Se a tabela mostrar a turma de destino e o botão disser "Inscrever-me na prova", mais visitantes clicam para se inscrever, porque a pergunta que decide a inscrição é "a bolsa vale para qual turma" | Antes e depois, por prova com destino confirmado, ou A/B por especialidade se o tráfego permitir | Cliques em "Inscrever-me na prova" por visitante do hub | Abandono no checkout |
| H2 | Se o WhatsApp aparecer como segundo passo, mais visitantes indecisos viram conversa, porque a dúvida sobre destino e regras costuma ir ao time de vendas | A/B do botão secundário (com e sem) | Conversas iniciadas por visitante | Cliques em inscrever |
| H3 | Se o resumo "como funciona" ficar acima da tabela, menos visitantes saem sem clicar, porque as regras ficam visíveis antes da escolha | A/B de ordem (passos antes ou depois da tabela) | Cliques na tabela por visitante | Rolagem até as regras |

---

# 6. AUDITORIAS

## 6.1 auditorias/08-conversao.md

| Item | Resultado | Observação |
|---|---|---|
| Topo da página passa no teste dos 5 segundos (no celular) | Atendido no texto, conferência visual pendente | Título, subtítulo, botão e linha de prova respondem as quatro perguntas. Falta abrir no celular com a página montada [CONFIRMAR no site] |
| Uma chamada para ação principal por página | Atendido | "Ver as provas e me inscrever" (topo e fim) e "Inscrever-me na prova" por linha são a mesma ação. O WhatsApp e o formulário são secundários e terciários (seção 1.11) |
| Formulário pede só o necessário | Atendido | Nome, WhatsApp, consentimento e duas escolhas; e-mail opcional. Política de privacidade [CONFIRMAR link] |
| Provas são reais e autorizadas | Atendido | Nenhum depoimento, nome, foto ou número de inscritos. Só fatos do catálogo, do contexto e das páginas das provas |
| Objeções respondidas na página | Parcial | 16 perguntas respondidas (F1 a F16). As objeções centrais (destino, bolsa com valor em reais, aprovado sem bolsa, monitoria, ausência) estão em PF1 a PF15 e dependem da Ufape |
| Testes têm hipóteses escritas | Atendido | Seção 5.7 (H1 a H3), marcadas [SUPOSIÇÃO] |
| Resultados registrados, vencedores e perdedores | Não se aplica | Nenhum teste rodou. Registro depois dos pontos de checagem |
| Dados do curso conferidos com contexto/catalogo-de-cursos.md | Atendido, com ressalvas | Código, cidade, data, horário, inscrição e status das 22 provas conferidos com a seção 3. Regras da bolsa vêm do contexto da linha e das páginas, ainda não do catálogo: [CONFIRMAR NO CATÁLOGO]. Turmas candidatas conferidas com a seção 2 (Anexo A) |
| Eventos de lead e inscrição rastreados (GA4, Meta e Google Ads) e lead chegando ao CRM | Pendente | Plano na seção 5.4. Implementação, consentimento e CRM dependem do time do site e da Ufape [CONFIRMAR ferramentas] |

## 6.2 auditorias/conformidade-educacional.md

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atendido: nomes e modalidade (presencial) das provas conforme a seção 3. Nenhuma carga horária, duração ou turno de turma aparece no texto da página |
| Dados do curso | Status "aberto" | Atendido: as 22 linhas estão "aberto". 68656 e as 13 provas "sem venda" ficam fora |
| Dados do curso | Modalidade clara | Atendido: "presencial" em todo o texto. Turma 68632 marcada "presencial" na tabela, como no catálogo |
| Regulação | Pós lato sensu sem a frase de reconhecimento | Atendido na página. Alerta: 15 páginas de destino dos botões trazem a frase (G1) |
| Regulação | Nota MEC | Atendido: nenhuma |
| Regulação | Curso livre sem diploma | Não se aplica |
| Promessas | Sem promessa de emprego, salário, aprovação ou bolsa garantida | Atendido: a página diz que nenhuma bolsa é garantida |
| Promessas | Dados de empregabilidade ou satisfação | Não se aplica: nenhum |
| Promessas | Superlativos com fonte | Atendido: nenhum na página. Superlativos de 68651 ficam na correção G10 |
| Promessas | Comparação com concorrente | Atendido: nenhum concorrente nomeado; F16 só em termos neutros |
| Preço e condições | Valor, parcelas e condições completas | Atendido para a inscrição (R$ 100,00, formas de pagamento). Para as turmas, o texto-padrão do Anexo A traz parcelas, valor da parcela, total e matrícula, sem desconto |
| Preço e condições | Bolsa com regra, público elegível e prazo | Parcial: regra, percentuais e prazos de recurso e matrícula claros; público elegível, turma de destino e base de cálculo [CONFIRMAR]. Bloqueia a camada turma |
| Preço e condições | Urgência real | Atendido: só a data da prova, sem contador e sem escassez; sem "inscrições até" sem data |
| Preço e condições | Prouni, Fies ou financiamento | Não se aplica: nenhum |
| Pessoas e dados | Autorização de imagem e depoimento | Atendido: nenhum depoimento, nenhuma foto de pessoa, nenhum docente |
| Pessoas e dados | Menores | Não se aplica |
| Pessoas e dados | Formulários com finalidade e política de privacidade | Pendente: texto previsto na seção 1.7 e 1.11, link [CONFIRMAR] |
| Pessoas e dados | WhatsApp e e-mail só com consentimento | Atendido no desenho: caixa de consentimento desmarcada, forma de sair no texto |
| Pessoas e dados | Nenhum dado pessoal na peça ou nos arquivos | Atendido. Os telefones e e-mails são contatos oficiais da instituição (contexto/ufape-geral.md) |
| Plataformas | Políticas da Meta e do Google; página entrega o que o anúncio promete | Parcial: Cardiologia (links), Goiânia (endereço) e Felinos (regras e frase) bloqueiam anúncio até a correção |
| Anúncios | Sem característica pessoal de quem vê, sem escassez falsa, sem caixa alta, sem camuflagem | Atendido na página. O qa confere cada anúncio à parte |

**Resultado:** Aprovado como rascunho, para o qa-de-marketing e a aprovação humana. **Bloqueado para publicação** até os itens de 5.1 (destino, local de Goiânia, links de Cardiologia, regras unificadas, turma mínima, privacidade e aprovador). Revisado por: landing-page (autoavaliação); qa-de-marketing e pessoa do marketing: pendentes. Data: 26/10/2026.

Conferência de forma feita por este agente: nenhum travessão e nenhuma meia-risca no arquivo; nenhum dado pessoal; nenhum depoimento; nenhuma frase de certificação ou nota do MEC na página; nenhuma comparação com concorrente; nenhum percentual de aprovação; nenhum valor de curso com bolsa calculado; nenhuma expressão de escassez; nenhum docente citado.

---

# 7. NOTAS PARA ARQUIVOS DE OUTROS AGENTES (este agente não edita arquivo alheio)

- **saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md:** (1) a seção A13 diz que Felinos é a única prova com conteúdo e bibliografia: na leitura das 22 fichas, 12 páginas trazem conteúdo programático e 1 traz bibliografia (tabela da seção 1.5). (2) A contradição de "7 dias" e de "no site" aparece em 12 páginas, não só em Felinos (G2). (3) A seção 2.3 cita só 68640 para o endereço de São Paulo em Goiânia e pede conferir 68642 e 68644: conferido, as três têm o erro. (4) A frase de reconhecimento ligada ao MEC está em 15 páginas de prova (G1), não só em Felinos.
- **saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md:** o bloco citável da seção 5.1 diz "não é acumulativa nem intransferível para outra pessoa": o certo é "não é acumulativa e é intransferível" (a bolsa não passa para outra pessoa).
- **contexto/catalogo-de-cursos.md e contexto/pos-graduacao.md:** subir para o catálogo as regras da prova de bolsa (11 bolsas, percentuais, nota de corte, prazos, desempate, turma mínima), a turma de destino de cada prova e o local da prova em cada cidade. O contexto traz o WhatsApp de vendas de Goiânia com 8 dígitos depois do DDD: [CONFIRMAR].
- **Fichas das provas:** todas marcam "Alertas: nenhum", mas há endereço de São Paulo em páginas de Goiânia, regras divergentes e frase ligada ao MEC. Atualizar os alertas.
- **saidas/08-conversao/analise-cro-pos-2026-10-26.md:** a análise cobre só a prova 68639. As correções G1 a G16 ampliam o raio-x às 22 páginas.

---

# 8. ANEXOS

## Anexo A: turmas candidatas ao destino, com as condições do catálogo (não publicar antes da confirmação)

Valores copiados do catálogo (seção 2, site em 26/10/2026), sem arredondar e sem nenhum desconto de bolsa aplicado. O hub não mostra esta tabela. Ela serve à Ufape para confirmar o destino e ao editor para preencher a frase de investimento da seção 1.8 depois da confirmação. Início das turmas: planilha, fonte da verdade para datas.

**Grupo D1: há turma futura aberta da mesma especialidade e cidade (destino provável, [CONFIRMAR])**

| Prova | Turma candidata | Local e modalidade | Início | Carga horária | Condições no catálogo | Observação |
|---|---|---|---|---|---|---|
| 68640 | 68609, Pós-graduação em Anestesiologia Veterinária (turma VIII) | Goiânia, semipresencial | 24/04/2027 | 500 h | 30x de R$ 1.081,67; R$ 32.450,00 no cartão ou boleto; matrícula R$ 250,00 | Parcela vezes 30 não fecha o total ao centavo (R$ 32.450,10): copiar os dois números como estão |
| 68642 | 289, Pós-graduação em Cardiologia Veterinária (turma II) | Goiânia, semipresencial | 20/03/2027 | 500 h | 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00 | Link da prova invertido com 68641 (correção 2) |
| 68644 | 68632, Pós-graduação em Clínica Cirúrgica de Cães e Gatos (turma V) | Goiânia, presencial | 10/04/2027 | 500 h | 30x de R$ 1.100,00; R$ 33.000,00 no cartão ou boleto; matrícula R$ 250,00 | Única pós presencial integral do recorte; não escrever "semipresencial" |
| 68645 | 68635, Pós-graduação em Clínica Médica e Emergência de Pequenos Animais (turma V) | São Paulo, semipresencial | 10/04/2027 | 750 h | 30x de R$ 1.100,00; R$ 33.000,00 no cartão ou boleto; matrícula R$ 250,00 | |
| 68648 | 68617, Pós-graduação em Endocrinologia de Pequenos Animais | São Paulo, semipresencial | 17/04/2027 | 500 h | 30x de R$ 1.200,00; R$ 36.000,00 no cartão ou boleto; matrícula R$ 250,00 | Turma diverge entre planilha e site: sem número de turma na peça |
| 68654 | 68616, Pós-graduação em Neurologia e Neurocirurgia Veterinária (turma IX) | São Paulo, semipresencial | 08/05/2027 | 500 h | 30x de R$ 1.192,40; R$ 35.772,00 no cartão ou boleto; matrícula R$ 250,00 | |
| 68657 | 68628, Pós-graduação em Oncologia Veterinária | São Paulo, semipresencial | 10/04/2027 | 500 h | 30x de R$ 1.298,00; R$ 38.940,00 no cartão ou boleto; matrícula R$ 250,00 | Turma diverge entre planilha e site: sem número de turma na peça |
| 68658 | 68615, Pós-graduação em Patologia Clínica (turma VII) | São Paulo, semipresencial | 20/03/2027 | 500 h | 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00 | |
| 68659 | 68636, Pós-graduação em Pneumologia Veterinária (turma VIII) | São Paulo, semipresencial | 17/04/2027 | 500 h | 30x de R$ 1.265,00; R$ 37.950,00 no cartão ou boleto; matrícula R$ 250,00 | Fonte "só no site": data [CONFIRMAR com a planilha] |
| 68661 | 68629, Pós-graduação em Ultrassonografia de Pequenos Animais (turma III) | São Paulo, semipresencial | 22/05/2027 | 360 h | 24x de R$ 685,67; R$ 16.456,00 no cartão ou boleto; matrícula R$ 350,00 | Fonte "só no site": data [CONFIRMAR com a planilha]. O catálogo escreve "Pós Graduação"; usar o padrão "Pós-graduação em" |

**Grupo D2: a turma aberta da área começa antes da prova ou um dia depois ([CONFIRMAR destino], decisão A-C2)**

| Prova | Situação |
|---|---|
| 68646 Dermatologia | A turma 68610 começa em 28/11/2026, um dia depois da prova. O resultado e os 10 dias úteis de matrícula caem depois do início |
| 68651 Hematologia | A turma 68608 começa em 28/11/2026, um dia depois da prova. Mesma situação |
| 68647 Diagnóstico por Imagem | A turma 68604 começa em 31/10/2026, antes da prova; a 68611 está sem data ("verificar") |
| 68650 Gastroenterologia | A turma 68606 começa em 07/11/2026, 20 dias antes da prova |

Leitura de apoio [SUPOSIÇÃO]: a ficha 68661 diz que as bolsas valem para pós-graduações com início no primeiro semestre de 2027. Se isso valer para todas as provas, nenhuma das turmas do grupo D2 (que começam em 2026) seria destino, e as provas D2 precisariam de outra turma. A Ufape confirma.

**Grupo D3: só há turma aberta de subárea diferente ou de outra cidade ([CONFIRMAR destino])**

| Prova | Situação |
|---|---|
| 68639 Anestesiologia, São Paulo | Não há Pós-graduação em Anestesiologia Veterinária aberta em São Paulo. A 657 (Anestesiologia Avançada) e a 359 (Anestesiologia Locorregional, com pré-requisito na ficha) são outros cursos |
| 68641 Cardiologia, São Paulo | Nenhuma Cardiologia futura em São Paulo; a 68605 já começou ("verificar") e a 698 é Ecocardiografia |
| 68660 Terapia Intensiva, São Paulo | A 68623 (Terapia Intensiva e Emergência Veterinária) é em Goiânia; a 68635 é Clínica Médica e Emergência |
| 68643 Clínica Cirúrgica, São Paulo | Nenhuma Clínica Cirúrgica futura em São Paulo; a 578 é Videocirurgia e a 662 é Ortopedia (esta com link trocado) |

**Grupo D4: sem turma futura aberta na área (fora da campanha até haver destino)**

68649 Endoscopia, 68652 Medicina de Felinos, 68653 Nefrologia e Urologia, 68655 Odontologia. Risco: inscrição de R$ 100,00 sem curso de destino (reclamação e CDC). Linhas ocultas no hub e fora do JSON-LD até a decisão da Ufape.

Contagem: 10 em D1, 4 em D2, 4 em D3 e 4 em D4 (22).

## Anexo B: conferência página a página (texto copiado das fichas, 26/10/2026)

Legenda: "Endereço" confere com a cidade? "Resultado" consistente (WhatsApp e/ou e-mail) ou divergente (também "no site" ou "via email"). "Matrícula" 10 dias úteis, ou 10 e também 7 (divergente). "MEC" é a frase de reconhecimento ligada ao MEC no texto.

| Código | Cidade | Endereço | Resultado | Matrícula | Composição da prova | MEC | Conteúdo |
|---|---|---|---|---|---|---|---|
| 68639 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68640 | Goiânia | Erro (São Paulo) | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68641 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68642 | Goiânia | Erro (São Paulo) | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68643 | São Paulo | Confere | Divergente | 10 e 7 | 20 questões | Sim | Sim |
| 68644 | Goiânia | Erro (São Paulo) | Divergente | 10 e 7 | 20 questões | Sim | Sim |
| 68645 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68646 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68647 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68648 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Sim | Sim |
| 68649 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68650 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68651 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Só bibliografia |
| 68652 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68653 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68654 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68655 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Sim | Não |
| 68657 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68658 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Não | Não |
| 68659 | São Paulo | Confere | Divergente | 10 e 7 | 10 a 20 questões | Sim | Sim |
| 68660 | São Paulo | Confere | Consistente | 10 | Múltipla escolha e dissertativas | Sim | Não |
| 68661 | São Paulo | Confere | Divergente | 10 e 7 | Múltipla escolha e dissertativas | Sim | Sim |

Totais desta tabela: endereço errado em 3; resultado e matrícula divergentes em 12 (68641, 68642, 68643, 68644, 68645, 68650, 68651, 68652, 68653, 68657, 68659, 68661); frase ligada ao MEC em 15; conteúdo programático em 12, só bibliografia em 1 e nenhum em 9. Na coluna "Composição": 10 páginas com "10 a 20 questões" (68641, 68642, 68645, 68650, 68651, 68652, 68653, 68657, 68659 e a contagem do G5 corrigida abaixo), 2 com "20 questões" (68643 e 68644) e 11 com "múltipla escolha e dissertativas".

Correção da contagem do G5: pela tabela acima, "10 a 20 questões" aparece em 9 páginas (68641, 68642, 68645, 68650, 68651, 68652, 68653, 68657, 68659), "20 questões" em 2 (68643 e 68644) e "múltipla escolha e dissertativas" em 11 (68639, 68640, 68646, 68647, 68648, 68649, 68654, 68655, 68658, 68660, 68661). Total 22. O texto do G5 na seção 3.4 trouxe números aproximados: vale a contagem desta tabela.

---

# Próximo passo

1. Pessoa do marketing: aprovar este rascunho e levar à Ufape os pedidos de 5.1 (destino, local de Goiânia, links de Cardiologia, regras unificadas, turma mínima, privacidade e aprovador) e de seção 3 (correções das páginas), com resposta até 29/10 para não atrasar o prazo de 03/11 das peças da campanha.
2. **Próximo agente sugerido: analise-cro**, para refazer o raio-x com o hub montado no celular (teste dos 5 segundos, atritos de tabela, formulário e WhatsApp) e estender a análise das páginas das 22 provas com os achados G1 a G16. Em seguida: otimizador-de-cta (rótulos dos botões), seo-on-page (título, descrição e H2), arquiteto-de-fluxos (eventos, UTM e CRM), qa-de-marketing (auditoria 08-conversao e conformidade) e desenho-de-experimentos (H1 a H3, quando houver tráfego).

---

## Lista 1. Fatos (com fonte)

- 22 provas de bolsa com status "aberto" em 27/11/2026, 19 em São Paulo e 3 em Goiânia (68640, 68642, 68644); inscrição de R$ 100,00 à vista (Pix ou boleto) ou 1x no cartão. Fonte: catálogo, seção 3.
- 68656 (Oftalmologia) "encerrado, link fora do ar" e 13 provas antigas "sem venda (avise-me)". Fonte: catálogo, seção 3.
- Prova presencial das 9h às 13h; questões de múltipla escolha e dissertativas; 11 bolsas por prova (2 de 50% com monitoria, 4 de 25%, 5 de 10%); nota de corte 7,0 (mínimo 70% de acerto); resultado por WhatsApp e/ou e-mail; recurso em 2 dias úteis; matrícula em até 10 dias úteis; bolsa não acumulativa e intransferível; desempate por análise de currículo; documento com foto; sem celular e relógios. Fonte: contexto/pos-graduacao.md; fichas 68639 e 68640 e as demais.
- Turma mínima de 15 nas páginas das provas e de 20 nas páginas de turma e no contexto da linha. Fonte: contexto/pos-graduacao.md; fichas.
- Endereço de São Paulo: Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, 01407-100. Fonte: contexto/ufape-geral.md; fichas.
- As páginas 68640, 68642 e 68644 (Goiânia) mostram o endereço de São Paulo. Fonte: fichas.
- 12 páginas trazem "7 dias" para a matrícula e "no site" ou "via email" para o resultado; 15 trazem a frase de reconhecimento ligada ao MEC; 12 trazem conteúdo programático e 1 só bibliografia; todas escrevem "intrasferível". Fonte: leitura das 22 fichas (Anexo B).
- A ficha 68652 contradiz as regras comuns (resultado, matrícula e composição) e traz a frase ligada ao MEC. Fonte: ficha 68652.
- A ficha 68661 diz "bolsas parciais em pós-graduações participantes com início no primeiro semestre de 2027". Fonte: ficha 68661.
- Turmas candidatas e condições: seção 2 do catálogo, Anexo A. A 68610 (Dermatologia) e a 68608 (Hematologia) começam em 28/11/2026; a 68604 em 31/10/2026; a 68606 em 07/11/2026. Fonte: catálogo, seção 2.
- Contatos oficiais: vendas São Paulo (11) 91366-9290; vendas Goiânia (62) 9420-1847; secretaria (11) 97492-8443 e (11) 5054-1204, duvidas@intercursos.com.br, segunda a sexta, 9h às 18h; SAC e ouvidoria em intercursos.com.br. Fonte: contexto/ufape-geral.md.
- Razão social UFAPE CURSOS ESPECIALIZADOS LTDA e CNPJ 27.409.162/0001-34; sede na Av. 9 de Julho, 3939. Fonte: contexto/ufape-geral.md (a grafia da razão social no contexto traz um hífen com espaços; aqui aparece sem ele).
- O site informou instabilidade no WhatsApp interno em 22/10/2026. Fonte: contexto/ufape-geral.md.
- 27/11/2026 cai numa sexta-feira. Fonte: 26/10/2026 é segunda-feira (plano do cmo).
- Hub T1 proposto na pesquisa de palavras-chave: palavra principal, URL sugerida, título, descrição, H1 e H2. Fonte: pesquisa de palavras-chave, seção 5.1.
- A página 68639 atual: botão COMPRAR, sem destino, sem prazo de inscrição, sem política de ausência. Fonte: analise-cro, página 3.
- "Ufape Intercursos" não é marca de venda; nenhuma frase de certificação até a regulação aprovar. Fonte: estrategia-de-marca, contexto/pos-graduacao.md.

## Lista 2. Suposições

- [SUPOSIÇÃO] Persona P4 e as quatro dúvidas da seção 1.2 (hipóteses, sem citação de candidato).
- [SUPOSIÇÃO] Destino provável de cada prova (grupos D1 a D4), vindo da leitura do briefing e do catálogo; o destino real é da Ufape.
- [SUPOSIÇÃO] "Não acumulativa" significa que a bolsa não soma com outros descontos.
- [SUPOSIÇÃO] Passagem e hospedagem não estão incluídas na pós (o catálogo não as lista).
- [SUPOSIÇÃO] Se a frase do primeiro semestre de 2027 (ficha 68661) valer para todas as provas, as turmas de 28/11/2026 não são destino.
- [SUPOSIÇÃO] Padrão de UTM, nomes de evento, texto da mensagem pré-preenchida do WhatsApp, rótulos dos botões e hierarquia visual.
- [SUPOSIÇÃO] URL /pos-graduacao/prova-de-bolsa e padrão de CMS.
- [SUPOSIÇÃO] A maioria dos candidatos chega pelo celular (a confirmar no GA4).
- [SUPOSIÇÃO] A homonímia com a universidade federal de mesma sigla justifica a pergunta F15.
- [SUPOSIÇÃO] Ordem de correção por impacto provável, e efeitos esperados das correções e dos testes.
- [SUPOSIÇÃO] Barra fixa no celular, filtro da tabela e formulário curto aumentam a conversão (hipóteses H1 a H3).

## Lista 3. Dados que faltam

- [CONFIRMAR] Turma de destino de cada uma das 22 provas; decisão sobre 68649, 68652, 68653 e 68655 (seguem à venda?); decisão sobre 68646 e 68651 (turmas começam um dia depois) e sobre 68647 e 68650.
- [CONFIRMAR] Local da prova em Goiânia; número do WhatsApp de vendas de Goiânia (8 dígitos no contexto).
- [CONFIRMAR] Links de Cardiologia (68641 e 68642): onde se cruzam e o resultado do teste no checkout.
- [CONFIRMAR] Regras: 10 dias úteis ou 7 dias; canal do resultado; composição da prova; turma mínima de 15 ou 20.
- [CONFIRMAR] Prazo de inscrição, data de divulgação do resultado, data final de matrícula.
- [CONFIRMAR] Regra do aprovado sem bolsa; o que a monitoria exige; ordem de distribuição das 11 bolsas; política de ausência e de devolução; requisito para se inscrever; base de cálculo da bolsa; alcance de "não acumulativa"; se a bolsa incide sobre a matrícula; se vale para turma de outra cidade.
- [CONFIRMAR] Quando a 1ª mensalidade começa para quem se matricula em dezembro de 2026 numa turma que começa em 2027.
- [CONFIRMAR NO CATÁLOGO] Regras da prova de bolsa (hoje só no contexto da linha e nas páginas); datas das turmas 68636 e 68629 (só no site).
- [CONFIRMAR] O que mais a inscrição de R$ 100,00 inclui (material de estudo, por exemplo).
- [CONFIRMAR] Conteúdo programático das 9 provas sem conteúdo e das que têm só bibliografia.
- [CONFIRMAR] Comportamento do botão, do checkout e do celular (não abri o site); consentimento e política de privacidade no checkout.
- [CONFIRMAR] Ferramentas: GA4, CRM, tag do checkout, banner de consentimento; se o checkout permite medir a conclusão do pagamento.
- [CONFIRMAR] Horário e responsável pelo atendimento do formulário e do WhatsApp; prazo de resposta.
- [CONFIRMAR] Grafia da razão social para o JSON-LD; URLs oficiais dos perfis para sameAs; imagem de compartilhamento.
- [CONFIRMAR] Quem aprova páginas e preços (tabela vazia em contexto/ufape-geral.md).
- [CONFIRMAR autorização] Qualquer docente, aluno ou aprovado que a Ufape queira usar na página no futuro.
- [CONFIRMAR] Fonte de dados numéricos de apresentação nas páginas 68641, 68642, 68651, 68655 e 68657; turma de Hematologia (VII no texto, VIII no catálogo).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação da Pós (a página não afirma nada até lá).
- [CONFIRMAR] Números reais de inscritos, presentes, aprovados e matrículas por prova (hoje nenhum número existe), meta e verba da campanha.

## Fontes

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (seções 2 e 3); contexto/cursos/pos/ (fichas 68639, 68640, 68641, 68642, 68643, 68644, 68645, 68646, 68647, 68648, 68649, 68650, 68651, 68652, 68653, 68654, 68655, 68657, 68658, 68659, 68660 e 68661); templates/landing-page.md; templates/pagina-da-turma.md; .claude/skills/raio-x-de-pagina/SKILL.md; .claude/skills/schema-de-curso/SKILL.md; saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md; saidas/08-conversao/analise-cro-pos-2026-10-26.md; saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md; auditorias/08-conversao.md; auditorias/conformidade-educacional.md.

Externas: nenhuma. Não abri faculdade.ufape.com.br e não fiz busca na web.
