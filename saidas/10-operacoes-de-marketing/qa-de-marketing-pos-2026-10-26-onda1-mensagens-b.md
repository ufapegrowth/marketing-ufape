# QA de marketing (conferência b): versão 2 do lote 1 de mensagens de reta final da onda 1 da Pós-graduação

- **Agente:** qa-de-marketing (10 Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira). O nome do arquivo usa a data da rodada (26/10) com o sufixo -onda1-mensagens-b, como pedido pelo orquestrador.
- **Peça revisada:** /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md, versão 2 (704 linhas; não alterada por esta revisão)
- **Revisão anterior:** /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-26-onda1-mensagens.md (C1 a C8)
- **Escopo pedido:** reconferir só as correções obrigatórias C1 a C8 e ver se a versão 2 criou problema novo. Os ajustes recomendados R1 a R10 não foram reavaliados um a um.
- **Entradas usadas:** as mesmas da revisão anterior (CLAUDE.md, docs/execucao-2026-10-26.md, plano do cmo da onda 1, cmo-geral seções 12 e 13, auditorias/07-email-e-whatsapp.md, auditorias/conformidade-educacional.md, catálogo seção 2 e fichas de 707, 68604, 698, 68610 e 68608), já lidas nesta sessão.
- **Dados pessoais:** nenhum.

---

## Veredito: CORRIGIR (1 correção de texto, sem mudança de conteúdo)

As correções C1 a C8 estão todas resolvidas. A versão 2 trouxe um erro novo de concordância num texto que vai a público, no e-mail T1 de 68610, e repetiu o mesmo erro na resposta R4 do time de vendas. A correção é literal e está abaixo. Com ela aplicada, o lote segue para a aprovação humana (OA9) sem nova revisão completa: basta o orquestrador conferir no diff que só as linhas 231 e 573 mudaram.

---

## 1. Correção obrigatória

| # | Onde (linha da v2) | Problema | Correção literal |
|---|---|---|---|
| N1 | 3.1, corpo do e-mail T1 de 68610 (231); 7.3, R4 cenário B de 68610 (573) | Erro de concordância criado na aplicação da C5. A linha 231 diz "aulas online ao vivo, gravada," e a linha 573 diz "as aulas são online ao vivo, gravada". O e-mail vai para a base, e a resposta vai para o candidato. | Linha 231: "- aulas online ao vivo e gravadas, e plantões de dúvidas mensais;". Linha 573: "A página informa que as aulas online são ao vivo e gravadas." O resto das duas linhas fica igual. |

---

## 2. Reconferência de C1 a C8

| # | Situação na v2 | Resultado |
|---|---|---|
| C1 | T1, T2, T1b e T2b (linhas 146, 186, 227, 267, 308, 348, 387, 431, 469 e 511) dizem "com o módulo 1 online; os módulos presenciais são na sede da Ufape" e citam o 1º presencial. Conferido com as fichas: 698 módulo 2, 19 e 20/12/2026; 68610 módulo 5, 20 e 21/03/2027; 68608 módulo 6, abril de 2027; 707 módulo 4, 29 a 31/01/2027; 68604 módulo 4, fevereiro de 2027. | Resolvida |
| C2 | F1, F2, F1b e F2b estão marcados "proposta ao cmo, fora do OA9: não enviar" e saíram do 0.1 (6 no cenário A, 10 no B) e do 0.2. O status no cabeçalho (linha 7) diz o mesmo. | Resolvida |
| C3 | 1.2 (linhas 72 a 77): os toques principais já agendados (Workshop de 30/10, 68606, 68665, Graduação) são reservados antes; 1 por dia entre todas as campanhas; 68606 entrou na ordem; Graduação com 1 WhatsApp a cada 3 dias úteis. A seção 8 foi refeita com os casos que faltavam. Nenhum caso passa de 2 e 2 por semana nem de 1 por dia. | Resolvida |
| C4 | R3 B só com OU3 por escrito (linha 567); R2 A sem a oferta de registro até a OU4 (561); R9 com a mesma condição (593). | Resolvida |
| C5 | 707 e 68610 separados no e-mail, na 7.2 e na R4, com o texto de cada ficha. | Resolvida no conteúdo; a concordância da frase de 68610 virou N1 |
| C6 | Juliana Jorge aparece sem titulação nas linhas 368, 396 e 673 e está em [CONFIRMAR] (692). | Resolvida |
| C7 | "com mais 4 professores listados" (linhas 121, 151 e 673), conforme a ficha de 698. | Resolvida |
| C8 | F2b (518) com o nome completo do catálogo; nota de 707 (368) com "CERTIFICAÇÃO DO MEC" e A7. | Resolvida |

## 3. Problemas novos da v2

- **N1:** acima. É o único que bloqueia.
- **Conformidade:** nenhum problema novo. Não aparecem preço, valor de matrícula ou de inscrição, bolsa, prova, MEC, certificação, "últimas vagas" nem número de turma mínima. A frase da 1ª mensalidade, os links e a UTM ficaram iguais.
- **Canal:** todos os WhatsApp seguem com SAIR. Os corpos de WhatsApp ficaram mais longos com a frase do módulo 1, mas por estimativa na leitura ficam entre cerca de 620 e 720 caracteres, abaixo de 1.024. Todos os e-mails seguem com o rodapé de descadastro.
- **Gates:** 698 continua preso à correção do site. Para 707 e 68604, a v2 passou a exigir "OU2 e OU3 por escrito" (linhas 53, 366 e 448); o plano do cmo pede só a OU2 para o cenário B. É mais restrito e não cria risco, mas pode travar envios que o cmo liberaria (ver A1).
- **Travessão e meia-risca:** nenhum, pela busca automática e pela leitura.

## 4. Ajustes recomendados (não bloqueiam)

| # | Onde (linha) | Ajuste |
|---|---|---|
| A1 | 53, 366 e 448 | Alinhar o gate de 707 e 68604 com o cmo. A mensagem sai antes do início, então basta a OU2 (matrícula depois do corte até a véspera). A OU3 só é necessária nas respostas R3 e R4. Se o copy quiser manter as duas, o cmo precisa concordar. |
| A2 | 387 e 431 | "em 29 a 31/01/2027" passa a "de 29 a 31/01/2027". |
| A3 | 194, 275, 356 e 518 | Se o cmo aprovar algum F2 ou F2b, usar a frase fixa "Fale com o time para saber como entrar na turma" e a identificação de quem envia (já pedido na C2 e na R4 da revisão anterior). |
| A4 | 112 | Envio sem API continua previsto; vale a R9 da revisão anterior (sem API, só 1 a 1). |

## 5. Auditorias (efeito da v2)

- **auditorias/07-email-e-whatsapp.md:** o item "frequência humana" passa a Atendido no desenho (C2 e C3 resolvidas); o template segue [CONFIRMAR U11a]. Os itens de registro e medição continuam como pendente externo (P15). Os demais itens seguem atendidos.
- **auditorias/conformidade-educacional.md:** "Nome... batem com o catálogo" (C8a) e "Modalidade clara e correta" (C1) passam a Atendido. "Destino entrega o que a mensagem prometeu" segue Atendido com gate (698). Nenhum item falha. O bloqueio que resta (N1) é de ortografia (método, passo 2), não de conformidade.

## 6. Destino

Volta ao copy-de-mensagens só para a N1. Com a N1 aplicada e o diff conferido pelo orquestrador (só as linhas 231 e 573), segue para a aprovação humana (OA9) até 28/10, com os gates de cada turma. Nada foi publicado, enviado ou pago.

---

## Fatos (com fonte)

- 1º presencial e módulo 1 online: fichas de 698 (linhas 48 a 53), 68610 (57 a 58 e 76 a 78), 68608 (51 a 52 e 67 a 68), 707 (60 a 61 e 69 a 70), 68604 (56 a 57 e 66 a 67).
- "online ao vivo, gravada" (68610): ficha, linha 49. "Acesso a aulas gravadas, disponíveis na plataforma do curso" (707): ficha, linha 55.
- Cenário B do cmo (matrícula depois do corte até a véspera do início, só com OU2): cmo-pos, linhas 85 e 102.
- D2, D3 e D16 com a regra de 1 WhatsApp a cada 3 dias úteis na Graduação: cmo-geral, linhas 567 a 582 e 857 a 864.

## [SUPOSIÇÃO]

- Contagem de caracteres dos WhatsApp feita por estimativa na leitura.
- A conferência do diff pelo orquestrador basta para liberar a N1, porque a correção é literal e não muda dado nenhum.

## [CONFIRMAR]

- OU1 a OU4, A6 (site de 698 até 28/10, 18h), A7, A12, U11 e U11a, como na revisão anterior.
- Decisão do cmo sobre o gate OU2 e OU3 de 707 e 68604 (A1) e sobre o conflito de 29/10 na área A2.
- Titulação de Juliana Jorge.
