# Revisão de QA: versão para o cliente da apresentação do plano de marketing da Pós-graduação em Gastroenterologia Veterinária (turma 68606)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 28/10/2026 (quarta-feira)
- **Peça revisada:** os 18 slides de /home/user/marketing-ufape/ferramentas/apresentacao-68606-cliente/project/slides/, na ordem de ../deck.json (capa, resumo, aprendizados, estrategia, curso, meta, investimento, publico, mensagem, canais, relacionamento, docentes, podcast, pauta, calendario, pronto, precisamos, proximos), texto visível e aside de cada um.
- **Base de comparação:** a versão interna de 72 slides já aprovada (dossiê), em /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/slides/ (lidos: curso, meta, verba, pracas, publico, mensagem, canais, regua, docentes, podcast, episodio-funil, pauta, calendario, kit, decisoes), e a reconferência de QA dela (qa-de-marketing-pos-2026-10-28-apresentacao.md, seção 8).
- **Entradas lidas (fontes):**
  - /home/user/marketing-ufape/contexto/ufape-geral.md; /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha inteira, com "Participantes")
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json (inclui a linha literal do catálogo)
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 22)
  - /home/user/marketing-ufape/saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-28-benchmarks.md
  - /home/user/marketing-ufape/saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-26.md (seções 0 a 5, para conferir UFPA e Semesp)
  - /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (seções 0, 1 e 6A)
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md
- **Não aberto:** faculdade.ufape.com.br; nenhuma busca na web. Nenhum slide foi editado pelo qa.
- **Dados pessoais:** nenhum. Docentes só com nome e titulação da ficha.

---

## 1. Veredito

**CORRIGIR.**

A versão para o cliente é bem mais clara que o dossiê e a maior parte dos números bate com as fontes: datas da turma, os dois textos de anúncio, a frase da regra no remarketing, o WhatsApp de 29/10 (igual ao 6A.2 do copy-de-mensagens, sem o link), os cenários do funil, a divisão por praça, as fases de R$ 250 e R$ 1.750 com a ressalva "se nada foi gasto", o pacote de 10 peças do podcast e os nomes dos docentes.

Mas a simplificação apagou ressalvas que a reconferência do dossiê tinha exigido (OU6 na bandeira do 3º módulo, condição da 1ª mensalidade junto do preço, "a turma pode não ser formada" no pilar 3, regra completa nas chamadas depois do início), pôs preço no texto visível, contou a coordenação duas vezes nos "38 docentes", marcou como pronto um item que ainda é rascunho e usou uma referência de concorrente que não sustenta a frase do slide. Dois itens de auditorias/conformidade-educacional.md ficam sem marcação (preço e condições; turma já iniciada sem a regra completa), e pela regra do agente o veredito é CORRIGIR, sem exceção.

São 24 achados: 12 bloqueiam (B) e 12 são ajustes (A). Depois das correções, a versão volta ao qa só para K1 a K24.

---

## 2. O que foi conferido e bate com a fonte

| Item | Onde | Fonte | Resultado |
|---|---|---|---|
| Turma IX, São Paulo, semipresencial, 500 h, 24 módulos, início 07/11/2026, "aberto" | curso, capa, mensagem | catálogo (linha literal no pos-68606.json) e ficha | Certo |
| Módulos 1, 2 e 3 online em 07/11/2026, 19/12/2026 e 23/01/2027; presenciais 17/04/2027 (módulo 6), 27/11/2027 (13) e julho de 2028 (21) | curso, estrategia, mensagem, calendario | ficha | Certo |
| Coordenação Esp. Maria Carolina Pappalardo; Dr. Rodolfo Oliveira Leal; Dra. Cibele Figueira Carvalho; DR. Fabrizio Grandi | curso, docentes, pauta | ficha, Participantes | Certo, grafia da ficha |
| 17 Dr./Dra., 12 MSc., 6 Esp., 3 Profa. = 38 | docentes | contagem da ficha (inclui a coordenação, ver K7) | Certo |
| Turma mínima 15 | curso, resumo | decisão 11 | Certo |
| Captação até 22/01 (véspera do 3º módulo) | resumo, calendario | decisão 18 | Certo, sem a pendência OU6 (K1) |
| R$ 2.000,00 de verba; R$ 133,33 por matrícula; meta 15 | resumo, meta | decisões 15 e 16 | Certo |
| Cenário base 200 / 20 / 15, até R$ 10 por interessado; conservador e otimista no aside | meta | dossiê, meta.html | Certo, com a marca "estimativa" visível |
| Fases: até R$ 250 e até R$ 1.750, "Valores máximos, se nada foi gasto ainda no ciclo. Gasto atual: a confirmar." | investimento | dossiê, verba.html | Certo, ressalva mantida |
| Base e verba por praça (27,8/30; 21,5/25; 9,1/20; 10,5/14; 7,8/11); 8.016 de 10.447 = 76,7% | investimento | dossiê, pracas.html e verba.html | Certo |
| Anúncio até 06/11 e remarketing a partir de 07/11 | mensagem | dossiê, mensagem.html (F1 e F2) | Iguais, palavra por palavra |
| WhatsApp de 29/10 | relacionamento | copy-de-mensagens, 6A.2 | Igual ao corpo aprovado; link só na mensagem real (aside) |
| Régua: 28/10, 29/10, 06/11, 02/12, 16/12, 12/01; 4 WhatsApp e 2 e-mails | relacionamento, pronto | copy-de-mensagens, 0.1 e 0.2 | Certo |
| Pausa em 02/11, 20 e 21/11 e 21/12 a 03/01 | relacionamento, calendario (aside) | dossiê, regua.html | Certo |
| Pacote do episódio: 3 cortes, 3 capas, 1 card, 2 Stories, 1 card do convidado = 10 | podcast | decisão 21 | Certo |
| Cinco episódios (24/11, 08/12, 22/12, 05/01, 19/01) e reserva em 02/02 | pauta | dossiê, pauta.html | Certo |
| Relatório final em 25/01 e 22/02/2027 | calendario (aside) | dossiê, calendario.html | Certo |
| EAD de 23,4% (2016) para 65,4% (2022) | aprendizados (aside) | pesquisa de 26/10, seção 2 (Semesp) | Certo |
| 223.704 atuantes (CRMV-RJ, 08/03/2026; outras fontes 218 mil a 228 mil); 63.128 em SP; 63,8% em 5 UFs | publico (aside) | pesquisa de 28/10, 1.1 e 1.2 | Certo (ver K12 sobre a mistura de bases) |
| 43,98% de abertura e 2,15% de clique, ressalva da abertura inflada | relacionamento (aside) | pesquisa de 28/10, 4.1 | Certo |
| Mediana de 27 downloads em 7 dias; top 10% acima de 409 | podcast (aside) | pesquisa de 28/10, 5.1 | Certo |
| Dezembro com matrícula pelo 13º (Educa Insights e ABMES, 2024) | calendario (aside) | pesquisa de 28/10, seção 6 | Certo, falta o escopo (K14) |

### 2.1 Regras do pedido

| Regra | Resultado | Onde |
|---|---|---|
| Nada de "certificado/reconhecido pelo MEC" como afirmação | Atende. Só "frase de certificação", como item a tirar da página | estrategia (aside), precisamos |
| Nenhum dado pessoal | Atende. "[nome]" no WhatsApp é campo de mesclagem, não dado (ver K22) | relacionamento |
| Preço só nas notas, como uso interno | **Não atende** | precisamos, item 3 (K3); curso, aside sem a condição completa (K2) |
| Sem urgência sem a regra completa | Atende nos textos de anúncio e mensagem; **não atende** nas chamadas do podcast depois do início (K5) | mensagem; podcast, pauta |
| "Pós-graduação em" no nome | **Não atende** no título da capa (K18) | capa |
| Nunca travessão nem meia-risca | Atende na leitura integral dos 18 slides e asides; nenhum encontrado. A busca automática dos caracteres U+2014 e U+2013 fica com o orquestrador | todos |
| Nunca "agência" | Atende. Sempre "The Growth Hub" | aprendizados, investimento, publico (asides) |
| Nome exato "Workshop Brasileiro de Neuromonitorização" | Atende; nenhum "simpósio" | relacionamento e calendario (asides) |

---

## 3. Achados

Legenda: **B** bloqueia (conformidade, regra do pedido, marca perdida ou mudança de sentido); **A** ajuste (clareza, precisão ou encaixe, sem mudar o sentido).

### K1 (B) Limite do 3º módulo sem a pendência "véspera ou 1º dia"
- **Slides:** curso (bandeira do módulo 3 e rodapé); resumo (coluna "22/01").
- **Texto atual:** curso: "Módulo 3 · online / 23/01/2027 / limite para entrar" e "Turma mínima: 15 alunos. Reposição dos módulos para quem entra depois do início: a confirmar."; resumo: "último dia de captação, véspera do 3º módulo".
- **Problema:** no dossiê a pendência OU6 está na bandeira e no rodapé (F19 da reconferência). Aqui foi só para o aside, e "limite para entrar" afirma uma regra que a Ufape ainda não fechou.
- **Correção exata:**
  - curso, bandeira: "matrícula até o 3º módulo (a confirmar se vale no 1º dia)".
  - curso, rodapé: "Turma mínima: 15 alunos. A confirmar: se a matrícula vale até a véspera ou também no 1º dia do 3º módulo, e como ficam os módulos perdidos."
  - resumo, coluna 22/01: "último dia de captação, véspera do 3º módulo (a confirmar se inclui o 1º dia)".

### K2 (B) Preço no aside sem a condição completa
- **Slide:** curso, aside.
- **Texto atual:** "Investimento (uso interno, não vai em peça até a confirmação do valor da inscrição): 30x de R$ 1.180,00 ou R$ 35.400,00 no cartão ou boleto, mais matrícula de R$ 250,00 no site; o CEO informou inscrição de R$ 260,00. Presenciais: (...) módulo 13 (27 e 28/11/2027: endoscopia) (...)"
- **Problema:** sumiu a condição da 1ª mensalidade que a F3 exigiu junto do preço (item "preço mostra valor, parcelas e condições completas"). Também sumiu "parasitologia ou transplante fecal" do módulo 13, que está na ficha.
- **Correção exata:** "Investimento (uso interno; nenhuma peça cita valor até a Ufape confirmar a inscrição): 30x de R$ 1.180,00 ou R$ 35.400,00 no cartão ou boleto, mais matrícula de R$ 250,00 no site; 1ª mensalidade paga até 30 dias antes do início, segundo a página. O CEO informou inscrição de R$ 260,00: a diferença está a confirmar." e "módulo 13 (27 e 28/11/2027: endoscopia, parasitologia ou transplante fecal)".

### K3 (B) Preço no texto visível
- **Slide:** precisamos, item 3.
- **Texto atual:** "Valor da inscrição: R$ 260 ou R$ 250"
- **Problema:** regra do pedido (preço só nas notas, como uso interno). No dossiê o item tinha a marca "uso interno"; aqui o valor está na tela, sem marca.
- **Correção exata:** item 3: "Valor da inscrição: qual vale, o da página ou o informado à equipe". No aside, acrescentar: "Item 3 (uso interno): a página mostra matrícula de R$ 250,00; o CEO informou inscrição de R$ 260,00."

### K4 (B) Pergunta da regra do 3º módulo incompleta
- **Slide:** precisamos, item 4.
- **Texto atual:** "Como o aluno repõe os módulos que perdeu e como paga quem entra depois do início"
- **Problema:** o dossiê (decisoes.html, item 6) cobre OU3, OU6 e OU8; a versão do cliente perdeu a OU6, a única que muda a data de corte de 22/01.
- **Correção exata:** "Como o aluno repõe os módulos que perdeu, como paga quem entra depois do início e se a matrícula vale até a véspera ou também no 1º dia do 3º módulo".

### K5 (B) Chamadas do podcast depois do início sem a regra completa
- **Slides:** podcast (linha "Para quê"); pauta (aside).
- **Texto atual:** podcast: "Mostrar quem ensina e levar à página da turma, sem mensagem extra para a base."; pauta, aside: "Regras: a opinião é do convidado; conteúdo clínico com revisão docente; nenhum paciente, tutor ou aluno identificável; sem promessa de emprego ou renda."
- **Problema:** todos os episódios saem depois de 07/11, com a turma já iniciada. O dossiê (episodio-funil.html, "Chamada"; pauta.html, aside) manda usar a frase completa do 3º módulo, sem frase de certificação e sem "últimas vagas", e cita o nome exato do Workshop. Isso sumiu. Falha o item de conformidade "status aberto ou não chama para inscrição" (contexto da linha: a turma iniciada só é divulgada com a regra completa) e a regra "sem urgência sem a regra completa".
- **Correção exata:**
  - podcast, "Para quê": "Mostrar quem ensina e levar à página da turma. Depois de 07/11, toda chamada para a turma traz a regra completa do 3º módulo. Sem mensagem extra para a base."
  - pauta, aside, no fim das regras: "sem frase de certificação; sem "últimas vagas"; a data do 3º módulo só dentro da frase completa da regra ("A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram."); o evento de 20 e 21/11, se citado, é o "Workshop Brasileiro de Neuromonitorização"."

### K6 (B) Pilar "Condições claras" sem a turma mínima
- **Slide:** estrategia, coluna "Condições claras"; aside.
- **Texto atual:** "Parcelas, total e matrícula na página. Sem preço no anúncio, sem "últimas vagas"."; aside: "O que nenhuma peça diz: preço ou valor de inscrição (até a confirmação), (...)"
- **Problema:** a F21 pôs "a turma pode não ser formada" no pilar 3, e o próprio slide de aprendizados diz que o medo é a turma não fechar. A ressalva saiu do texto visível. No aside, "(até a confirmação)" pode ser lido como se o preço pudesse ir ao anúncio depois.
- **Correção exata:** coluna: "Parcelas, total e matrícula na página, e o aviso de que a turma pode não ser formada. Sem preço no anúncio, sem "últimas vagas"." Aside: "O que nenhuma peça diz: preço (nunca no anúncio), valor da inscrição (até a resposta da Ufape), (...)".

### K7 (B) "38 docentes" conta a coordenação duas vezes e passa por cima da possível duplicidade
- **Slides:** aprendizados ("38 docentes com nome"), estrategia ("Coordenação e 38 docentes na página da turma."), curso ("Esp. Maria Carolina Pappalardo · 38 docentes"), docentes (título "38 docentes com nome são a melhor prova do curso.").
- **Problema:** os 38 são nomes listados, coordenação incluída (copy-de-mensagens 6A: "38 nomes listados, coordenação incluída"; a contagem 17 + 12 + 6 + 3 inclui a coordenadora como Esp.). "Coordenação e 38" soma 39. Dois nomes podem ser a mesma pessoa (a confirmar, só no aside). O dossiê fala sempre em "38 nomes". O título do slide docentes também troca "a prova que o candidato procura" por um superlativo sem fonte ("a melhor prova").
- **Correção exata:**
  - aprendizados: "Três módulos presenciais com data e 38 nomes de docentes na página. Isso convence mais que qualquer slogan."
  - estrategia: "38 nomes na página da turma, coordenação incluída."
  - curso: "Esp. Maria Carolina Pappalardo · 38 nomes listados, com a coordenação"
  - docentes, título: "38 nomes na página: <span>a prova que o candidato procura.</span>"; abaixo dos números, em 24px: "Contagem pela titulação da ficha; dois nomes podem ser a mesma pessoa (a confirmar)."

### K8 (B) Podcast como solução de "um post por docente"
- **Slide:** docentes, frase abaixo dos números.
- **Texto atual:** "Cada docente convidado do UFAPE Cast ganha um card e um corte com o nome dele: é assim que chegamos a um post por docente."
- **Problema:** muda o sentido. O plano tem 5 episódios até 22/01 com 4 docentes da ficha, e a lacuna do kit é de 37 posts (OA8). O dossiê diz "o podcast fecha parte dela" e põe a condição: card e corte contam juntos como 1 post só para docente da ficha e só com o ok e a revisão dele (checklist C1 a C8, critério do qa).
- **Correção exata:** "Cada docente da ficha convidado do UFAPE Cast ganha um card e um corte com o nome dele, que contam como o post dele no kit, sempre com o ok e a revisão do próprio docente. Até 22/01, isso cobre parte dos 38 nomes, não todos."

### K9 (B) Stories da coordenação marcados como prontos
- **Slide:** pronto, coluna "Pronto".
- **Texto atual:** "Ganchos e Stories da coordenação"
- **Problema:** no dossiê (kit.html) o post da coordenação (Stories de 09 a 15/11) está em "Inventário pendente", "em rascunho", e no pos-68606.json o post por docente está com qa "pendente". O aside do slide define "Pronto" como "escrito e revisado pela qualidade", o que não vale para esse item.
- **Correção exata:** coluna "Pronto": trocar o item por "Ganchos dos vídeos e carrosséis". Coluna "Em produção": acrescentar "Stories da coordenação (rascunho, espera o ok e a revisão da coordenadora)". Se os ganchos também não tiverem qa próprio, levar para "Em produção" [SUPOSIÇÃO: o dossiê trata os ganchos do criador-de-ganchos como recomendados, sem registro de qa próprio que eu tenha lido].

### K10 (B) Referência de concorrente que não sustenta a frase
- **Slide:** aprendizados, "Preço não é o caminho" e aside.
- **Texto atual:** visível: "Pós pública e EAD custam menos."; aside: "Pós pública citada: UFPA com mensalidade de R$ 1.920,00".
- **Problema:** a mensalidade da UFPA (R$ 1.920,00 em 18 meses, total de cerca de R$ 34.560,00 mais inscrição, pesquisa de 26/10, seção 5) é maior que a parcela da Ufape e o total é quase igual ao da 68606. O exemplo contradiz a frase. A oferta mais barata com fonte é a Unicruz (comunitária, total de R$ 8.899,00 a R$ 10.056,00, ano do edital a confirmar) e o agregador (mensalidades de R$ 60,00 a R$ 2.235,84, sem data). Comparação com concorrente precisa ser objetiva e verificável.
- **Correção exata:** visível: "Há pós mais baratas, sobretudo em EAD. O que diferencia a Ufape é a prática presencial com data marcada." Aside: trocar a frase da UFPA por "Referência de mercado: especialização em pequenos animais da Unicruz com total de R$ 8.899,00 a R$ 10.056,00 (edital 05/2026, ano a confirmar) e agregador com mensalidades de R$ 60,00 a R$ 2.235,84 (sem data); a UFPA tem mensalidade de R$ 1.920,00 em 18 meses, total parecido com o da Ufape, e por isso não entra como exemplo de preço menor. Duração, carga e modalidade diferem."

### K11 (B) Persona e faixa de idade sem marca no texto visível; recomendação trocada no aside
- **Slide:** publico.
- **Texto atual:** visível: "Clínico de pequenos animais, de 1 a 8 anos de formado. Começamos com 22 a 35 anos; no mercado, a maior faixa é de 30 a 39. Ajustamos pela leitura do custo por idade."; aside: "O peso da faixa de 30 a 39 sugere testar a idade acima de 35 cedo."
- **Problema:** (1) a persona é suposição da linha (contexto/pos-graduacao.md) e aparece como fato; (2) a faixa de 30 a 39 é referência de mercado, mas a etiqueta está na outra coluna, junto dos 224 mil; a pesquisa pede "predominam 30 a 49, com pico de 30 a 39"; (3) o dossiê recomenda "não abrir a faixa de idade antes de ter dado", e o aside do cliente recomenda o contrário, sem decisão registrada.
- **Correção exata:** visível: "Clínico de pequenos animais, de 1 a 8 anos de formado (estimativa, a validar com o CRM). Começamos com 22 a 35 anos e ajustamos pelo custo por idade. Referência de mercado: predominam os de 30 a 49 anos, com pico de 30 a 39." Aside: trocar a última frase por "Recomendação do plano: não abrir a faixa de idade antes de ter dado. O pico de 30 a 39 entra como hipótese para o primeiro ajuste, se o custo por idade confirmar."

### K12 (A) Referências de mercado sem "global" ou sem etiqueta no texto visível
- **Slides:** podcast ("Serve a"), relacionamento (rodapé da régua), publico (aside).
- **Texto atual:** podcast: "No mercado, um podcast mediano tem 27 downloads por episódio na 1ª semana."; relacionamento: "Referência de mercado: e-mail de ensino superior tem cerca de 2% de clique."; publico, aside: 223.704 e 63.128 citados juntos.
- **Problema:** a pesquisa pede que todo número de fora do Brasil diga isso na frase. O dado do podcast está sem a etiqueta "referência de mercado" e solto na linha "Serve a". Os 224 mil (CRMV-RJ, março de 2026) e os 63 mil (PetBioID, base de 228.167, setembro de 2026) vêm de bases diferentes.
- **Correção exata:**
  - podcast: tirar a frase de "Serve a" e pôr abaixo da tabela, em 24px: "Referência de mercado (global): um podcast mediano tem 27 downloads por episódio na 1ª semana. O valor do UFAPE Cast está nas peças que ele gera."
  - relacionamento: "Referência de mercado (global): e-mail de ensino superior tem cerca de 2% de clique."
  - publico, aside: acrescentar "Os dois números vêm de bases diferentes (223.704 de março de 2026; 63.128 de uma base de 228.167, de setembro de 2026): são ordem de grandeza, não se dividem um pelo outro."

### K13 (A) Teto de mensagens sem marca de regra própria
- **Slide:** relacionamento, rodapé da régua.
- **Texto atual:** "No máximo 2 WhatsApp e 2 e-mails por semana, 1 por dia. Só para quem autorizou. Referência de mercado: (...)"
- **Problema:** o teto é decisão da squad sem referência publicada ([SUPOSIÇÃO] no dossiê, D16). Logo antes de uma "referência de mercado", o cliente pode ler o teto como dado de mercado (o mesmo erro da F5).
- **Correção exata:** "No máximo 2 WhatsApp e 2 e-mails por semana, 1 por dia: regra nossa, sem referência publicada, ajustada pelos alertas de spam e descadastro. Só para quem autorizou." Aside: acrescentar "Envio do e-mail de 28/10: a confirmar (depende da aprovação de hoje)."

### K14 (A) Fim de ano ambíguo e 13º sem escopo
- **Slide:** calendario, coluna "21/12 a 03/01" e aside.
- **Texto atual:** "Fim de ano sem campanha · mídia reduzida · episódio 3"; aside: "Referência de mercado (Educa Insights e ABMES, 2024): dezembro ainda tem matrícula em educação por causa do 13º salário (...)".
- **Problema:** "sem campanha" e "mídia reduzida" na mesma linha se contradizem; o certo é sem mensagens de campanha e mídia pela metade, que é estimativa do plano de mídia. No aside, a fonte é de 14 instituições privadas de ensino superior e não diz se é graduação ou pós.
- **Correção exata:** "Fim de ano: sem mensagens de campanha · mídia pela metade (estimativa) · episódio 3". Aside: "(...) por causa do 13º salário (levantamento com 14 instituições privadas de ensino superior; não separa graduação e pós) (...)".

### K15 (A) Leitura do funil mais forte que a do dossiê
- **Slide:** meta, frase ao lado de "estimativa".
- **Texto atual:** "Cenário base com taxas estimadas, sem histórico da Ufape. A conta só fecha se a base de contatos, o time de vendas e o conteúdo trouxerem parte das matrículas."
- **Problema:** no cenário base a mídia sozinha fecha a conta (200 interessados a R$ 10 = R$ 2.000). O dossiê diz "Ainda não dá para dizer" e marca a participação da base como suposição. O que faz a conta não fechar é o gasto já feito e um custo por interessado acima do estimado.
- **Correção exata:** "Cenário base com taxas estimadas, sem histórico da Ufape e sem referência de mercado confiável. Ainda não dá para dizer se a mídia fecha a conta sozinha: parte da verba pode já ter sido gasta. Por isso a base de contatos, o time de vendas e o conteúdo entram para trazer parte das matrículas."

### K16 (A) "Inscrição" e "matrícula" confundem o cliente
- **Slides:** meta, estrategia, mensagem, relacionamento, precisamos.
- **Problema:** a página chama de "matrícula" a taxa de R$ 250,00; o plano chama essa taxa de "inscrição" e chama de "matrícula" a 1ª mensalidade paga. No mesmo deck, "Parcelas, total e matrícula na página" (taxa) e "Matrículas: 1ª mensalidade paga" (meta) usam a mesma palavra para coisas diferentes.
- **Correção exata:** meta, abaixo dos três cards, em 24px: "Inscrição paga = taxa paga no site (na página ela aparece como "matrícula"). Matrícula = 1ª mensalidade paga." Os textos de peça (mensagem e WhatsApp) ficam como estão, porque repetem o nome usado na página.

### K17 (A) "Meta" com dois sentidos e jargão de mídia
- **Slides:** resumo ("anúncios no Meta"), aprendizados ("A especialidade não existe no Meta"), meta (eyebrow "Meta e funil"), mensagem ("Remarketing a partir de 07/11").
- **Problema:** "Meta" aparece como objetivo e como empresa dos anúncios no mesmo deck. "Remarketing" é jargão de mídia.
- **Correção exata:** resumo: "frentes: anúncios no Instagram e Facebook, base de contatos e o UFAPE Cast"; aprendizados, título do card: "A especialidade não existe nos anúncios do Instagram e Facebook"; meta, eyebrow: "Objetivo e funil"; mensagem, etiqueta: "Anúncio para quem já visitou a página, a partir de 07/11".

### K18 (B) Capa sem "Pós-graduação em" no nome do curso
- **Slide:** capa, título.
- **Texto atual:** "Plano de marketing.<br><span>Gastroenterologia Veterinária.</span>"
- **Problema:** regra da linha e do pedido: o nome do curso é sempre "Pós-graduação em Gastroenterologia Veterinária".
- **Correção exata:** "Plano de marketing.<br><span>Pós-graduação em Gastroenterologia Veterinária.</span>". Encaixe: em 120px o nome quebra em 2 linhas (título com 3 linhas, cerca de 342px); a capa ainda cabe (cerca de 564px de 824px). Se o desenho pedir 2 linhas, baixar o h1 para 96px.

### K19 (A) Nome do podcast e motivo do X sem marca no texto visível
- **Slides:** capa, resumo, canais.
- **Texto atual:** canais: "UFAPE Cast" (card 03) e "X (sem público veterinário ativo)".
- **Problema:** o nome ainda está em aprovação (decisão 21); a marca só aparece no slide podcast e no aside de canais. A F11 do dossiê pediu a marca visível na tela de canais. O motivo do X é suposição no dossiê.
- **Correção exata:** canais, card 03: "UFAPE Cast (nome em aprovação)"; rodapé: "X (sem perfil; público veterinário ativo não comprovado)". Na capa e no resumo, basta a marca do slide canais e do slide podcast.

### K20 (A) Divisão por praça sem dizer que não vira cinco campanhas nesta turma
- **Slide:** investimento.
- **Texto atual:** tabela "Praça / Da base / Da verba", sem nota visível; título "Cinco praças com 77% da base, em duas fases."
- **Problema:** o cliente lê cinco campanhas. A recomendação (não abrir cinco campanhas a 10 dias do início; a divisão serve para acompanhar) está só no aside. "Da base" não diz de que base.
- **Correção exata:** título: "Cinco praças com 77% dos cadastros, em duas fases."; abaixo da tabela, em 24px: "Nesta turma, a divisão serve para acompanhar resultados por praça. As campanhas separadas por praça começam nas turmas de março."

### K21 (A) Título do slide "pronto" e prazo das perguntas
- **Slides:** pronto (título); proximos (item 02).
- **Texto atual:** "As peças visuais entram até 05/11." e "Responder as seis perguntas até 30/10".
- **Problema:** o pacote do podcast está em produção e só sai a partir de 24/11. Na tela "precisamos", os prazos são hoje, o quanto antes, 30/10, toda segunda e 06/11, não todos até 30/10.
- **Correção exata:** pronto: "O plano e as mensagens estão escritos. <span>Posts, criativos e vídeo entram até 05/11.</span>"; proximos, item 02: "Responder as seis perguntas, cada uma no seu prazo".

### K22 (A) Exemplos sem a palavra "exemplo"
- **Slides:** mensagem (etiquetas dos dois cards), relacionamento (etiqueta "WhatsApp de 29/10").
- **Problema:** o cliente pode ler o texto como peça já aprovada para subir. "[nome]" pode parecer marca interna.
- **Correção exata:** "Exemplo de anúncio até 06/11", "Exemplo de anúncio a partir de 07/11" (ver K17), "Exemplo: WhatsApp de 29/10". Aside de relacionamento: "[nome] é o primeiro nome, preenchido pelo sistema; sem nome, a mensagem começa só com "Olá"."

### K23 (A) Resumo: número que pode quebrar e Google fora das frentes
- **Slide:** resumo.
- **Texto atual:** "R$ 2 mil" em 96px numa coluna de cerca de 350px; "matrículas, no mínimo: a turma mínima para a turma abrir"; "3 frentes: anúncios no Meta, base de contatos e o UFAPE Cast".
- **Problema:** "R$ 2 mil" em 96px tem cerca de 390px na estimativa e pode quebrar em "R$ 2" / "mil" na 2ª coluna. A busca no Google entra depois de 07/11 e não aparece nas frentes. "turma mínima para a turma abrir" repete palavra.
- **Correção exata:** número da 2ª coluna em 80px (ou "R$ 2.000" em 80px); "matrículas, no mínimo: o número para a turma abrir"; frentes como em K17, e no aside: "A busca no Google entra junto dos anúncios, depois de 07/11."

### K24 (A) Encaixe (estimativa)
- Nenhum slide passa de 824px de altura útil. Estimativas do conteúdo em fluxo (o rodapé é absoluto): capa cerca de 564px; resumo 500 (590 se "R$ 2 mil" quebrar); aprendizados 545; estrategia 660; curso 670; meta 595; investimento 530; publico 615; mensagem 645; canais 590; relacionamento 680; docentes 625; podcast 725; pauta 615; calendario 585; pronto 490; precisamos 640; proximos 430.
- Atenção: os slides com padding inferior de 160px têm 792px livres antes da área do rodapé. O mais apertado é **podcast** (cerca de 725px; com a frase nova de K12 vai a cerca de 790px). Se passar, tirar a linha "Serve a" para o aside ou baixar as linhas da tabela para 24px. **Relacionamento** (cerca de 680px) aguenta a frase nova de K13 sem sobra grande.
- Risco horizontal: "4,7 a 5,5 mi" em 96px na coluna de cerca de 640px do publico (cerca de 565px, cabe por pouco).

---

## 4. auditorias/conformidade-educacional.md, item por item

Aplicada aos exemplos de peça que a apresentação mostra (anúncios e remarketing em mensagem; WhatsApp de 29/10 em relacionamento; Stories da coordenação em docentes; pauta e chamadas do podcast em podcast e pauta) e aos dados citados.

| Bloco | Item | Resultado | Onde e por quê |
|---|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atende | 500 h, 24 módulos, semipresencial, turma IX, 07/11/2026 |
| Dados do curso | Status "aberto" (ou a peça não chama para inscrição) | **Não atende** | Anúncio e remarketing atendem. As chamadas do podcast saem com a turma iniciada e perderam a regra completa (K5) |
| Dados do curso | Modalidade clara e correta | Atende | "módulo 1 online", "Teoria online e 3 módulos presenciais"; WhatsApp com online e presenciais |
| Regulação | Graduação: ato do catálogo | Não se aplica | linha pos |
| Regulação | Pós lato sensu sem "reconhecida pelo MEC" | Atende | nenhuma frase de certificação nas peças |
| Regulação | Curso livre sem diploma | Não se aplica | |
| Regulação | Nota MEC só com fonte | Atende | nenhuma nota |
| Promessas e provas | Sem promessa de emprego, salário ou sucesso | Atende | regra repetida no aside de pauta |
| Promessas e provas | Empregabilidade e satisfação com fonte | Não se aplica | |
| Promessas e provas | Superlativos só com fonte | Atende nas peças | na apresentação, "a melhor prova do curso" sai (K7) |
| Promessas e provas | Comparação com concorrente objetiva e verificável | Atende nas peças (nenhuma compara) | na apresentação, o exemplo da UFPA não sustenta a frase (K10) |
| Preço e condições | Valor, parcelas e condições completas | **Não atende** | valor na tela (K3) e aside sem a condição da 1ª mensalidade (K2); as peças não citam preço |
| Preço e condições | Bolsa e desconto com regra | Atende | nenhuma bolsa, prova ou desconto |
| Preço e condições | Urgência real | Atende nos textos de anúncio e mensagem | remarketing com a frase inteira; "último convite" é rótulo interno da régua; ver K5 para o podcast |
| Preço e condições | Prouni, Fies ou financiamento | Não se aplica | |
| Pessoas e dados | Autorização de uso de imagem | Atende | docentes, palestrantes e convidados autorizados (decisões 8 e 10); egresso "com nome e autorização a confirmar" (aside de pauta) |
| Pessoas e dados | Menores de idade | Não se aplica | público formado |
| Pessoas e dados | Formulários com finalidade e política de privacidade | Pendente externo | item 2 da tela "precisamos" (p04); bloqueia a publicação das peças, não a apresentação |
| Pessoas e dados | WhatsApp e e-mail só com consentimento e saída fácil | Atende | "Só para quem autorizou"; "responda SAIR" |
| Pessoas e dados | Nenhum dado pessoal | Atende | "[nome]" é campo de mesclagem (K22) |
| Plataformas | Políticas da Meta e do Google, sem segmentação discriminatória | Atende no desenho | público por formação e cargo; idade como faixa de partida |
| Plataformas | Página de destino entrega o que a peça promete | Pendente externo | a página ainda tem frase de certificação, turma mínima de 20 e não tem a regra do 3º módulo (item 2 de "precisamos", OA10) |
| Anúncios | Sem característica pessoal de quem vê | Atende | "para médicos veterinários formados" descreve o público do curso |
| Anúncios | Sem urgência falsa, contador ou imitação de interface | Atende | |
| Anúncios | Sem pessoa pública ou parceria inexistente | Atende | |
| Anúncios | Sem caixa alta excessiva ou símbolos | Atende | |
| Anúncios | Página carrega, domínio esperado, contato e privacidade | Pendente externo | p04 e OA10 |
| Anúncios | Sem sugestão para driblar a análise | Atende | |

**Resultado:** Bloqueado ( X ). Itens que precisam mudar: status e regra da turma iniciada (K5) e preço e condições (K2, K3). Pendentes externos que seguem bloqueando a publicação das peças, não a apresentação: política de privacidade do formulário e correção da página.
**Revisado por:** qa-de-marketing (agente). Revisão humana: pendente.
**Data:** 28/10/2026.

---

## 5. Próximo passo

A versão para o cliente **volta para o agente que a produziu** (cmo, com o orquestrador que montou os slides) para aplicar K1 a K24, com nova conferência do qa só desses itens. Depois do APROVADO, segue para a aprovação humana. Nada foi publicado, enviado ou pago.

---

## Fatos (com fonte)

- Linha 68606 do catálogo: São Paulo, semipresencial, 07/11/2026, turma IX, 500 h, 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00; aberto (pos-68606.json, catalogo_linha_literal).
- Cronograma, presenciais e temas, 38 nomes na lista "Participantes" com a coordenação, 1ª mensalidade até 30 dias antes do início, turma mínima de 20 na página (ficha 68606).
- 38 nomes listados, coordenação incluída; corpo do WhatsApp T2 da 68606; frase da regra (copy-de-mensagens-pos-onda1, seções 1.4, 6A e 6A.2).
- Decisões 11, 15, 16, 18, 21 e 22 (docs/execucao-2026-10-26.md).
- Lacuna de 37 posts por docente na 68606 (pos-68606.json, OA8); post por docente com qa "pendente" (pos-68606.json, kit).
- UFPA com mensalidade de R$ 1.920,00 em 18 meses; Unicruz de R$ 8.899,00 a R$ 10.056,00; Semesp 23,4% e 65,4% (pesquisa de mercado de 26/10, seções 2 e 5).
- 223.704, 63.128, 63,8%, 30 a 49 com pico de 30 a 39, 43,98% e 2,15%, 27 e 409, 13º com 14 instituições (pesquisa de mercado de 28/10, seções 1, 4, 5 e 6).

## [SUPOSIÇÃO]

- [SUPOSIÇÃO do qa] Larguras e alturas de texto estimadas com média de 0,5 em por caractere e as alturas de linha do estilo de cada slide; o CSS de tabela e lista não foi lido. Conferir no navegador os slides podcast, relacionamento e resumo.
- [SUPOSIÇÃO do qa] Os ganchos citados em "pronto" não têm qa próprio registrado nos arquivos que li (K9).

## [CONFIRMAR]

- Se a matrícula vale até a véspera ou também no 1º dia do 3º módulo (OU6); reposição dos módulos perdidos (OU3); pagamento de quem entra depois (OU8).
- Valor da inscrição (R$ 260,00 informado contra R$ 250,00 da página).
- Gasto já feito no ciclo da 68606.
- Política de privacidade do formulário e correção da página.
- Podcast: nome, perfis, canal do YouTube, quem produz, custo, convidados e egresso.
- Possível duplicidade entre "Profa. Ísis Carvalho" e "ESP. Isis de Carvalho Rodrigues Santana Lemes".

## Fontes

- /home/user/marketing-ufape/ferramentas/apresentacao-68606-cliente/project/deck.json e slides/*.html
- /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/slides/ (curso, meta, verba, pracas, publico, mensagem, canais, regua, docentes, podcast, episodio-funil, pauta, calendario, kit, decisoes)
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-28-apresentacao.md
- /home/user/marketing-ufape/contexto/ufape-geral.md
- /home/user/marketing-ufape/contexto/pos-graduacao.md
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-28-benchmarks.md
- /home/user/marketing-ufape/saidas/01-inteligencia-de-mercado/pesquisa-de-mercado-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md
