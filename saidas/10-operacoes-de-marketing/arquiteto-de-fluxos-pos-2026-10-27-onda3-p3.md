# Fluxos de CRM do kit das 8 turmas de abril de 2027 da Pós-graduação, parte 3 (seções 13 a 17): fluxo de cada turma, campos, pedidos de aprovação, etapas e workflow, auditorias e listas finais

- **Agente:** arquiteto-de-fluxos (departamento 10), encomenda O10 do plano do CMO da onda 3 (versão 2), lote A
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1 (lote A). Continuação de saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-pos-2026-10-27-onda3.md (seções 0 a 7) e de arquiteto-de-fluxos-pos-2026-10-27-onda3-p2.md (seções 8 a 12). As três listas finais (fatos, suposições e dados que faltam) estão no fim deste arquivo e valem para as três partes.
- **Status:** rascunho para o qa-de-marketing (auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC8 (seção 15). **Nada é ligado, agendado, enviado ou pago.** Toda ação no CRM é de humano, depois da aprovação. Nenhum arquivo de .claude/commands foi criado: o texto do workflow está na seção 16.3.
- **Dados pessoais:** nenhum.

---

## 13. Fluxo de cada turma

Em todas as linhas valem **CC1 a CC12** (seção 5) e as saídas **SA1 a SA10** (seção 4). A coluna "Condição" traz só o que é específico do toque. "Saída padrão" quer dizer: quem pagou, respondeu, saiu ou foi suprimido não recebe; o toque suprimido não acumula. **"Cai se"** lista o que o contato precisa receber (aceito pela fila gulosa, seção 6) para este toque ser suprimido: "no dia" é o mesmo dia; "na semana" é 2 toques do mesmo canal aceitos antes dele. **"Nunca cai"** quer dizer que nenhuma combinação do lote A, da onda 2, da onda 1 e da newsletter o derruba (o lote B reservado só passa à frente dos pós-inícios de 03 a 09/05). Os horários são e-mail às 9h e WhatsApp às 10h. A conta completa está nas seções 9 (pior caso) e 6 (ordem da fila). Cada tabela termina com "Como desfazer".

### 13.1 68628, Pós-graduação em Oncologia Veterinária (A10), lista L-A10, utm_campaign pos_68628_202701

Portão da turma: página publicada e conferida em 11/12 e reconferida em 04/01 (CC12); nenhuma peça cita o número da turma (P5). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; reconferência da página antes das 9h; primeiro toque de A10. **Nunca cai** (primeiro da fila no dia e na semana) | enviar E1 (botão "Ver a turma e as condições", utm_content=e1-68628); ligar a flag de saída da NP2 de A10 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | qua 20/01, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 657 em 21/01 (A1) e 333 em 19/01 (A11). Na variante de 341, 2 entre 657, 341 em 18/01 (A14 equinos) e 333 | enviar W1 (utm_content=w1-68628; template pos_68628_kit_w1 aprovado na Meta, se API [CONFIRMAR U11a]) | saída padrão |
| 3 | sex 05/02, 10h | **Nunca cai** (no máximo 1 WhatsApp à frente: 657 em 04/02) | enviar W2 (w2-68628) | saída padrão |
| 4 | qua 17/02, 9h | **Nunca cai** (primeiro e-mail da fila; no dia vence 366 e 68636 pela nota 60); cabe com a newsletter de 18/02 | enviar E2 (e2-68628) | saída padrão |
| 5 | qua 03/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 657 em 02/03 (A1) e 679 em 01/03 (A14) | enviar W3, com a frase de turma mínima sem número (w3-68628) | saída padrão |
| 6 | seg 05/04, 10h | **Nunca cai**, salvo com a DEC4: com ela, cai para quem está em A4 (o pré-início de 68632 do mesmo dia passa à frente) | enviar pré-início (pr-68628; pos_68628_kit_pr) | saída padrão |
| 7 | qua 28/04, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 289 PI em 27/04 e 68636 PI em 30/04 (as duas são de A2: basta estar em A2) | enviar PI, sem link, com a regra completa (3º módulo em 26 e 27/06/2027) e "responda TURMA"; resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 25/06 (SA3) |

**Como desfazer:** pausar a régua de 68628 no CRM, o que cancela os agendamentos pendentes dos toques 2 a 7; limpar a flag da NP2 de A10 (os contatos voltam à NP2 no próximo toque pendente, sem reenvio do que passou); a lista fica arquivada, não apagada. Toque já enviado não volta. SAIR e descadastro nunca são desfeitos.

### 13.2 68617, Pós-graduação em Endocrinologia de Pequenos Animais (A7), lista L-A7, utm_campaign pos_68617_202701

Portão da turma: URL com "/v/" conferida em 11/12, em 04/01 e antes de cada toque com link (OU29); nenhuma peça cita o número da turma (P5). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; URL conferida; primeiro toque de A7. **Cai se** recebe no mesmo dia o E1 de 68628 (A10) ou o E1 de 68636 (A2; nota 45 contra 36) | enviar E1 (e1-68617); ligar a flag de saída da NP2 de A7 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 22/01, 10h | **Cai se**, no dia, recebe o E1 de 679 (A14) ou o E1 de 68632 (A4); ou, na semana, 2 WhatsApp antes entre 657 em 21/01 (A1), 333 em 19/01 (A11), 68628 em 20/01 (A10), 68636 em 20/01 (A2) e, na variante de 341, 341 em 18/01 (A14 equinos) | enviar W1 (w1-68617; template pos_68617_kit_w1) | saída padrão |
| 3 | seg 15/02, 10h | **Cai se**, no dia, recebe o W1 de 68632 (A4); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68635 em 19/02 (A3), 68636 em 17/02 (A2) e 366 em 17/02 (A4) | enviar W2 (w2-68617) | saída padrão |
| 4 | qua 24/02, 9h | **Cai se**, no dia, recebe o E2 de 679 (A14) ou o W2 de 366 (A4, se couber no teto de WhatsApp); ou, na semana, 2 e-mails antes: 679 em 24/02 e 68636 em 26/02 (A14 e A2 juntas) | enviar E2 (e2-68617) | saída padrão |
| 5 | sex 12/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2), 68615 em 11/03 (A11), 68635 em 08/03 (A3) e 366 em 08/03 (A4) | enviar W3 (w3-68617) | saída padrão |
| 6 | seg 12/04, 10h | **Nunca cai** (só o pré-início de 68636, de 13/04, fica à frente); vence o PI de 341 de 14/04 | enviar pré-início (pr-68617) | saída padrão |
| 7 | qui 06/05, 10h | **Cai se**, na semana de 03 a 09/05, recebe antes 2 WhatsApp entre 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e, pela reserva do lote B, 719 pré-início em 03/05 (A14 719) e 68616 pré-início em 04/05 (A12) | enviar PI, sem link, com a regra completa (3º módulo em 19 e 20/06/2027); resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 18/06 (SA3) |

**Como desfazer:** pausar a régua de 68617 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A7; a lista fica arquivada. Se a URL com "/v/" não estiver conferida, o E1 e os toques com link não são agendados e nada acumula.

### 13.3 68636, Pós-graduação em Pneumologia Veterinária, turma VIII (A2), lista L-A2 (estendida), utm_campaign pos_68636_202701

Portão da turma: OU21 (data de 17/04 só no site): todos os toques saem com "abril de 2027" (texto aprovado do O7) até a resposta; com data diferente, ciclo extra. A lista L-A2 já existe (289). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; página conferida. **Cai se** recebe no mesmo dia o E1 de 68628 (A10). Vence o E1 de 68617 pela nota (45 contra 36) | enviar E1 (e1-68636); a flag de saída da NP2 de A2 já está ligada desde 08/12 (onda 2); se não estiver, liga às 00h05 | saída padrão |
| 2 | qua 20/01, 10h | **Cai se**, no dia, recebe o W1 de 68628 (A10) ou o E1 de 68635 (A3), o que couber primeiro na fila; ou, na semana, 2 WhatsApp antes: 657 em 21/01 (A1) e 333 em 19/01 (A11); na variante de 341, 2 entre 657, 341 e 333 | enviar W1 (w1-68636; template pos_68636_kit_w1) | saída padrão |
| 3 | qua 17/02, 10h | **Cai se**, no dia, recebe o E2 de 68628 (A10) ou o W1 de 366 (A4); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68632 em 15/02 (A4) e 68635 em 19/02 (A3) | enviar W2 (w2-68636) | saída padrão |
| 4 | sex 26/02, 9h | **Nunca cai** (só o E2 de 679, de 24/02, fica à frente) | enviar E2 (e2-68636) | saída padrão |
| 5 | seg 15/03, 10h | **Nunca cai** (só o W4 de 333, de 16/03, fica à frente, 1 WhatsApp) | enviar W3 (w3-68636) | saída padrão |
| 6 | ter 13/04, 10h | **Nunca cai** (vence o PI de 341 de 14/04 pela data de início) | enviar pré-início (pr-68636), com "abril de 2027" até a OU21 | saída padrão |
| 7 | sex 30/04, 10h | **Nunca cai** (no máximo o PI de 289, de 27/04, fica à frente); vence a versão de WhatsApp da newsletter desse dia | enviar PI, sem link, com a regra completa (3º módulo em 19 e 20/06/2027); resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 18/06 (SA3) |

**Como desfazer:** pausar a régua de 68636 sem mexer em L-A2 nem na régua de 289 (limpar só a marca de turma 68636); a flag da NP2 de A2 é da onda 2 e não muda aqui.

### 13.4 68635, Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, turma V (A3), lista L-A3, utm_campaign pos_68635_202701

Portão da turma: página conferida (a frase de "duas certificações", OU35, é da página); o PI só sai com o dia do 3º módulo (OU25). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | qua 20/01, 9h | OC2 do E1; primeiro toque de A3. **Cai se**, no dia, recebe o W1 de 68628 (A10), desde que ele caiba no teto de WhatsApp. Por teto semanal de e-mail nunca cai | enviar E1 (e1-68635); ligar a flag de saída da NP2 de A3 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 05/02, 10h | **Cai se**, no dia, recebe o W2 de 68628 (A10) | enviar W1 (w1-68635; template pos_68635_kit_w1) | saída padrão |
| 3 | sex 19/02, 10h | **Cai se**, no dia, recebe o W1 de 679 (A14); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14) e 68632 em 15/02 (A4). Vence a newsletter por WhatsApp desse dia | enviar W2 (w2-68635) | saída padrão |
| 4 | seg 01/03, 9h | **Cai se**, no dia, recebe o W3 de 679 (A14). Por teto semanal de e-mail nunca cai | enviar E2 (e2-68635), com a frase-ponte de A3 sem link para 68623 (E19) | saída padrão |
| 5 | seg 08/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2) e 68615 em 11/03 (A11) | enviar W3 (w3-68635) | saída padrão |
| 6 | ter 06/04, 10h | **Nunca cai** (no máximo 1 WhatsApp à frente, o de 05/04) | enviar pré-início (pr-68635) | saída padrão |
| 7 | seg 03/05, 10h | **Só com o dia do 3º módulo (OU25).** **Cai se**, no dia, recebe o pré-início de 719 (A14 719, lote B reservado); ou, na semana, 2 WhatsApp antes entre 719 em 03/05, 68616 em 04/05 (A12, lote B), 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e 68617 PI em 06/05 (A7) | enviar PI, sem link, com a regra completa e o dia do 3º módulo; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 68635 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A3; a lista fica arquivada.

### 13.5 366, Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, turma I (A4), lista L-A4, utm_campaign pos_366_202702

Portão da turma: **OU20.** Nada sai antes da data confirmada; verificação às 18h de 03/02 [SUPOSIÇÃO do horário]: início em 10/04 confirmado, vale o calendário; aberta ou com 24/04, nenhum toque de 366 é agendado e nada acumula (ciclo extra com 24/04). Nenhuma peça diz "coordenação" (OU34). O PI só sai com a data e o dia do 3º módulo (OU25). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 05/02, 9h | OC2 do E1; OU20 resolvida até 03/02 às 18h. **Cai se**, no dia, recebe o W2 de 68628 (A10) ou o W1 de 68635 (A3; só vale se ele couber); ou, na semana, 2 e-mails antes entre 657 em 01/02 (A1), 341 em 02/02 (A14 equinos) e 333 em 03/02 (A11) | enviar E1 (e1-366); a flag da NP2 de A4 já está ligada desde 22/01 (E1 de 68632) | saída padrão |
| 2 | qua 17/02, 10h | **Cai se**, no dia, recebe o E2 de 68628 (A10); ou, na semana, além do W1 de 68632 de 15/02 (que todo contato de A4 tem à frente), recebe antes 68615 em 16/02 (A11), 679 em 19/02 (A14) ou 68635 em 19/02 (A3) | enviar W1 (w1-366; template pos_366_kit_w1) | saída padrão |
| 3 | qua 24/02, 10h | **Cai se**, no dia, recebe o E2 de 679 (A14); ou, na semana, além do W2 de 68632 de 22/02, recebe antes 333 em 23/02 (A11) | enviar W2 (w2-366) | saída padrão |
| 4 | seg 01/03, 9h | **Cai se**, no dia, recebe o W3 de 679 (A14) ou o E2 de 68635 (A3). Para quem está só em A4, é a newsletter de 04/03 que cai (8.4), não este e-mail | enviar E2 (e2-366) | saída padrão |
| 5 | seg 08/03, 10h | **Cai se**, no dia, recebe o W3 de 68635 (A3); ou, na semana, 2 WhatsApp antes entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2) e 68615 em 11/03 (A11) | enviar W3 (w3-366), com a frase de turma mínima sem número | saída padrão |
| 6 | qua 07/04, 10h | **Cai se** está em A3: o pré-início de 68635 (06/04) soma com o de 68632 ou de 68628 (05/04) e fecha 2 WhatsApp na semana | enviar pré-início (pr-366) | saída padrão |
| 7 | seg 03/05, 10h | **Só com a data e o dia do 3º módulo (OU20 e OU25).** **Cai se**, no dia, recebe o PI de 68635 (A3); ou, na semana, 2 WhatsApp antes entre 719 em 03/05 e 68616 em 04/05 (lote B reservado), 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e 68617 PI em 06/05 (A7) | enviar PI, sem link, com a regra completa; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 366 (cancela os agendamentos pendentes) e limpar só a marca de turma 366 em L-A4 (a régua de 68632 não muda); a flag da NP2 de A4 só é limpa se as duas réguas de A4 forem pausadas. Se a OU20 voltar a abrir, repetir a verificação.

### 13.6 68632, Pós-graduação em Clínica Cirúrgica de Cães e Gatos, turma V, Goiânia, presencial (A4), lista L-A4, utm_campaign pos_68632_202701

Portão da turma: **OU3** (módulo 1 presencial) e regra 8 (E22): nenhuma mensagem fala de entrada depois do início; o pré-início de 05/04 sai sem "matrícula aberta até o 3º módulo"; a data do 3º módulo (12 e 13/06) não aparece. Nenhuma peça diz "coordenação" (OU34). Campus Goiânia no assunto e na primeira linha (E17). Atendimento: vendas de Goiânia.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 22/01, 9h | OC2 do E1; primeiro toque de A4. **Cai se**, no dia, recebe o E1 de 679 (A14). Por teto semanal nunca cai | enviar E1 (e1-68632); ligar a flag de saída da NP2 de A4 às 00h05 (vale para 68632 e 366), mesmo que o E1 seja suprimido | saída padrão |
| 2 | seg 15/02, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 68615 em 16/02 (A11) e 679 em 19/02 (A14) | enviar W1 (w1-68632; template pos_68632_kit_w1) | saída padrão |
| 3 | seg 22/02, 10h | **Cai se**, no dia, recebe o W2 de 679 (A14) (A14 já fecha 2 WhatsApp na semana com o W3 de 333 de 23/02, que vem à frente quando A11 também está) | enviar W2 (w2-68632), com a frase de passagem e hotel só depois da turma confirmada | saída padrão |
| 4 | qua 03/03, 9h | **Cai se**, no dia, recebe o W3 de 68628 (A10), que só cabe se o contato não tem antes 657 em 02/03 e 679 em 01/03. Por teto semanal de e-mail nunca cai | enviar E2 (e2-68632); a newsletter de 04/03 cai para quem recebe este e o E2 de 366 (8.4) | saída padrão |
| 5 | sex 05/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 657 em 02/03 (A1), 679 em 01/03 (A14) e 68628 em 03/03 (A10). Vence a newsletter por WhatsApp desse dia | enviar W3 (w3-68632) | saída padrão |
| 6 | seg 05/04, 10h | **Cai se**, no dia, recebe o pré-início de 68628 (A10; nota 60 contra 45), salvo com a DEC4. É a última mensagem de 68632 | enviar pré-início (pr-68632; pos_68632_kit_pr), sem a frase do 3º módulo | **a lista de 68632 fecha às 23h59 de 09/04 (SA4)** enquanto a OU3 estiver aberta |
| 7 | ter 04/05, 10h | **Não é agendado.** Só com a OU3 respondida, texto novo aprovado e qa; sem a OU3 nunca existe | nenhuma; reabertura é pedido novo (DEC6 da onda 2), com relatório de data nova | sem a OU3, a lista não reabre |

**Como desfazer:** pausar a régua de 68632 (cancela os agendamentos pendentes dos toques 2 a 6) e limpar só a marca de turma 68632 em L-A4 (a régua de 366 não muda); a flag da NP2 de A4 só é limpa se as duas réguas de A4 forem pausadas. A reabertura da lista depois de 09/04 só por pedido novo.

### 13.7 679, Pós-graduação em Infectologia Veterinária, turma IV (A14, infectologia), lista L-A14-679, utm_campaign pos_679_202701

Portão da turma: **OU19** (data de 03/04): todos os toques saem com "abril de 2027" (texto aprovado do O7) até a resposta; marca de curso (EN11, DEC7); o PI só sai com o dia do 3º módulo (OU25) e a data confirmada. A linha de campanha "Citopatologia 03/04" da visão de campanhas é da mídia (gestor), não do CRM. Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 22/01, 9h | OC2 do E1; [curso_de_interesse]=infectologia ou 679; primeiro toque do curso. **Nunca cai** (primeiro da fila no dia e na semana) | enviar E1 (e1-679); ligar a flag de saída da NP2 de A14 para infectologia às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 19/02, 10h | **Nunca cai** (no máximo o W de 68615, de 16/02, fica à frente); vence a newsletter por WhatsApp desse dia | enviar W1 (w1-679; template pos_679_kit_w1) | saída padrão |
| 3 | seg 22/02, 10h | **Nunca cai** (no máximo o W de 333, de 23/02, fica à frente) | enviar W2 (w2-679) | saída padrão |
| 4 | qua 24/02, 9h | **Nunca cai** (primeiro e-mail da fila no dia e na semana) | enviar E2 (e2-679) | saída padrão |
| 5 | seg 01/03, 10h | **Nunca cai** (no máximo o AC de 657, de 02/03, fica à frente) | enviar W3 (w3-679), com a frase de turma mínima sem número | saída padrão |
| 6 | seg 29/03, 10h | **Nunca cai**; mesmo com A14 numa lista só e os toques de 699, 719 e 382 do lote B, 679 vence pela data de início | enviar pré-início (pr-679), com "abril de 2027" até a OU19 | saída padrão |
| 7 | seg 26/04, 10h | **Só com o dia do 3º módulo (OU25) e a OU19.** **Cai se** está em A2 (289 PI em 27/04 e 68636 PI em 30/04 ficam à frente) | enviar PI, sem link, com a regra completa e o dia do 3º módulo; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 679 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A14 para infectologia (a de equinos é da onda 2 e não muda); a marca [curso_de_interesse] é mantida: ela é filtro, não envio.

### 13.8 68609, Pós-graduação em Anestesiologia Veterinária, turma VIII, Goiânia (A1), lista L-A1 (estendida), utm_campaign pos_68609_202701

Portão da turma: o convite da prova de Especialista que a página traz é item do OC1-A (nenhuma peça o repete); L-A1 já existe (657). Atendimento: vendas de Goiânia.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | qua 20/01, 9h | OC2 do E1. **Cai se**, no dia, recebe o W1 de 68628 (A10), o E1 de 68635 (A3) ou o W1 de 68636 (A2), cada um quando couber. Por teto semanal de e-mail nunca cai sem um desses | enviar E1 (e1-68609); a flag de saída da NP2 de A1 já está ligada desde 05/01 (E1 de 657); se não estiver, liga às 00h05 | saída padrão |
| 2 | seg 15/02, 10h | **Cai se**, no dia, recebe o W1 de 68632 (A4) ou o W2 de 68617 (A7); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68635 em 19/02 (A3) e 68636 em 17/02 (A2) | enviar W1 (w1-68609; template pos_68609_kit_w1) | saída padrão |
| 3 | qui 25/02, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 333 em 23/02 (A11), 679 em 22/02 (A14), 68632 em 22/02 (A4) e 366 em 24/02 (A4). A4 sozinha já traz 2 | enviar W2 (w2-68609) | saída padrão |
| 4 | seg 08/03, 9h | **Cai se**, no dia, recebe o W3 de 68635 (A3) ou o W3 de 366 (A4), o que couber. Por teto semanal nunca cai | enviar E2 (e2-68609); os nomes de 657 e 359 entram sem link (E19) | saída padrão |
| 5 | qua 17/03, 10h | **Cai se**, na semana, recebe antes 333 em 16/03 (A11) e 68636 em 15/03 (A2) | enviar W3 (w3-68609) | saída padrão |
| 6 | seg 19/04, 10h | **Nunca cai** (vence o PI de 657 de 20/04: referência de 24/04 contra 21/05) | enviar pré-início (pr-68609) | saída padrão |
| 7 | ter 11/05, 10h | **Nunca cai** (no máximo o PI de 333, de 12/05, só com OU3, fica à frente) | enviar PI, sem link, com a regra completa (3º módulo em 26 e 27/06/2027); resposta vai a vendas de Goiânia | SA6; a lista fecha às 23h59 de 25/06 (SA3) |

**Como desfazer:** pausar a régua de 68609 e limpar só a marca de turma 68609 em L-A1 (a régua de 657 não muda); a flag da NP2 de A1 é da onda 2 e não muda aqui.

---

## 14. Campos do CRM

Nomes provisórios [SUPOSIÇÃO]. Nenhum guarda dado pessoal em arquivo da squad; o CRM guarda no contato e a squad lê só contagens. **Esta onda não cria campo novo**: reaproveita os da onda 2 (seção 12 do arquivo dela) e acrescenta valores.

| Campo | Onde | Tipo | Uso | Situação e valores desta onda |
|---|---|---|---|---|
| [opt_in_email], [opt_in_whatsapp] (com data, origem, finalidade) | contato | sim ou não | EN1 a EN3 | existe no desenho |
| [área_de_interesse], [praça] | contato | texto | listas | existe; valores A1, A2, A3, A4, A7, A10 e A14 |
| [curso_de_interesse] | contato | texto ou etiqueta | L-A14-679 (infectologia ou 679) e L-A14E (equinos ou 341) | novo na onda 2; esta onda acrescenta o valor "infectologia" |
| [respondeu_em], [pediu_sair], [matriculou] | contato | data ou sim ou não | SA1, SA5, SA6 | existe |
| [time_assumiu] | contato | sim ou não | EN5, SA6 | novo na onda 2 |
| [fim_janela_silencio], [vinculo_ufape] | contato | data, lista | EN7, EN6 | existe |
| [base_graduacao] | contato | sim ou não | teto de 3 por semana (CC8) | novo na onda 2 |
| [regua_com_data_ativa_área] | contato, por área (por curso em A14) | sim ou não | EN12, seção 11 | existe; esta onda liga A10, A7, A3, A4 e A14 infectologia |
| [kit_ultimo_toque_<código>] | contato, por turma | texto | EN8, auditoria | novo na onda 2; códigos 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609 |
| [kit_saiu_motivo_<código>] | contato, por turma | pagou, pagou_mesma_area, data_limite, regra8, sair, descadastro, devolucao, respondeu, turma_parada, engajamento | SA1 a SA10; leitura só somada | novo na onda 2; esta onda troca "pagou_gemea" por "pagou_mesma_area" (DEC3) e acrescenta "regra8" (SA4) |
| [wa_campanha_sem_interacao] | contato | número | SA9 (E1) | novo na onda 2 |
| [data_limite_turma], [estado_da_turma_hoje] | turma | data, texto | SA3, SA4, CC4 | valores: 68628 e 68609, 25/06/2027; 68617 e 68636, 18/06/2027; 68632, 09/04/2027 (11/06 com OU3); 679, 68635 e 366, 31/05/2027 até a OU25 (trava de segurança) |
| [nota_gut_fila] | turma | número | desempate da seção 6.2 | valores: 68628 = 60; 68632, 68636 e 679 = 45; 68635 e 366 = 36 (desempate por urgência: 68635 = 4, 366 = 3); 68617 = 36; 68609 = 12 |
| [data_do_item] | turma | data | D2, seção 6.1 | início antes de começar; véspera do 3º módulo depois; PI sem dia fica depois de qualquer dia de junho (DEC2) |
| registro de supressão | contagem | número por semana, motivo (dia, teto semanal, fila), toque e combinação de áreas | relatório do cmo e painel somado | novo na onda 2; esta onda acrescenta semana e combinação de áreas, para a tabela 9.2 |

---

## 15. Pedidos de aprovação humana e como desfazer cada automação

Quem aprova: a pessoa do marketing que aprovou o plano geral, até a tabela de ufape-geral.md ser preenchida (A9) [CONFIRMAR]. Quem executa no CRM: [CONFIRMAR]. **Nada abaixo está ligado.** O envio de cada toque continua sendo o OC2 do plano da onda 3, uma aprovação por toque.

### 15.1 Automações (AF)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AF1 | Criar L-A3, L-A4, L-A7, L-A10 e L-A14-679 e estender L-A1 e L-A2 com as marcas de 68609 e de 68636, em **rascunho**, com os filtros das seções 2 e 3, sem agendar envio | uma regra única de quem recebe cada kit | sem custo de mídia; horas de quem configura [CONFIRMAR]; tamanho de cada lista só somado [CONFIRMAR, OC2] | sete listas auditáveis, sem envio | arquivar a lista nova (não apaga contato nem histórico); nas estendidas, remover só a marca de turma (a lista da onda 2 não muda) |
| AF2 | Ligar as regras de saída SA1 a SA10 para as 8 turmas, a regra 8 de 68632 (a lista fecha às 23h59 de 09/04 sem OU3), a trava de 31/05 para 679, 68635 e 366 e a reconferência antes do disparo (06h e 30 minutos antes) | o plano manda sair quem pagou, a turma depois da data limite, 68632 na véspera do início e o descadastro em até 48 h | sem custo de mídia; horas [CONFIRMAR] | ninguém recebe o que já não cabe | desligar regra por regra e voltar ao envio com conferência manual. **SA5 (SAIR e descadastro) não se desliga** |
| AF3 | Ligar a fila gulosa D2 da seção 6 (data de referência da decisão 4, nota GUT só para empate), o 1 por dia, o teto de 2 e 2 (1 no E1; 3 na base da Graduação), os dias sem campanha e o aviso ao cmo quando um dia passar de 4 toques da onda 3 ou repetir área | toda a base da Pós divide o teto; sem fila o CRM aplicaria a ordem de agendamento | sem custo de mídia; horas [CONFIRMAR] | no máximo 1 mensagem por dia e 2 e 2 por semana para o contato, sem exceção manual | desligar a fila e voltar à conferência manual semana a semana (só com decisão do cmo); o teto e o limite diário são suposições do cmo e voltam ao valor anterior só pelo R1 do plano |
| AF4 | Agendar os 55 toques nas datas da seção 7 (o 56º, PI de 68632 em 04/05, **não** é agendado), cada um **só depois do OC2 daquele toque**, do qa próprio e do teste de humano; 366 com o portão OU20 (verificação em 03/02, 18h), 679, 68635 e 366 no PI só com o dia do 3º módulo, 679 e 68636 com "abril de 2027" até a OU19 e a OU21 | a base é a alavanca mais barata da turma | sem custo de mídia; custo por conversa de marketing do WhatsApp Business se o envio for por API [CONFIRMAR U11a]; o valor precisa vir antes de 04/01 | 16 e-mails e 39 WhatsApp dentro do teto | cancelar o agendamento do toque ou pausar a régua; toque já enviado não volta, por isso cada toque tem aprovação própria |
| AF5 | Ligar a saída da NP2 nas datas da seção 11: A10 e A7 em 04/01, A3 em 20/01, A4 e A14 infectologia em 22/01; e, só se a flag da onda 2 não estiver ligada, A2 em 04/01 e A1 em 20/01 | dono único do convite | sem custo | a nutrição não repete o convite do kit | limpar a flag [regua_com_data_ativa_área] da área (volta à NP2 no próximo toque pendente, sem reenviar o passado) |
| AF6 | Parametrizar a UTM da seção 12 em links e templates e registrar na tabela de correspondência o desvio da NP2 de dezembro e os dois nomes do utm_content do pré-início ("ac" e "pr") | atribuição por turma | sem custo | cliques e respostas por toque, só somados | trocar o nome na tabela de correspondência; link já enviado mantém a UTM antiga |
| AF7 | Ligar o registro de supressões por semana, motivo, toque e combinação de áreas e o relatório de segunda-feira com a tabela 9.2 | o cmo lê só número somado e precisa saber quantos toques a fila cortou | sem custo de mídia; horas [CONFIRMAR] | relatório de segunda-feira com supressões por semana e motivo | desligar o registro; nenhum dado pessoal sai do CRM |

### 15.2 Decisões de política (DEC)

| # | Decisão proposta | Quem decide | Se não for aprovada |
|---|---|---|---|
| DEC1 | **Fila em ordem de prioridade (gulosa):** o CRM aceita os toques candidatos na ordem da D2 e recusa o que fecharia o dia ou o teto da semana; um concorrente só derruba outro se ele mesmo for aceito. Mesmo resultado da tabela 7.4 da onda 2 (em 14 a 20/12 a newsletter fica para quem perde o W1 de 333). | cmo | o CRM corta o dia e depois a semana, o que deixa o contato sem nenhum dos dois toques onde bastava cortar um (20/01 e 01/03 desta onda, 17/12 da onda 2) |
| DEC2 | **Notas GUT por turma e posição dos pós-inícios sem dia:** 68628 = 60; 68632, 68636 e 679 = 45; 68635 e 366 = 36 (68635 na frente pela urgência); 68617 = 36; 68609 = 12. PI de 679, 68635 e 366 ficam depois de qualquer referência com dia de junho até a OU25. Vale só para empate de data de referência. | cmo | a fila fica sem desempate e o CRM decide pela ordem de agendamento, o que não é explicável |
| DEC3 | **Pagou uma turma, sai das outras turmas da mesma área** (68632 e 366; 68609 e 657; 68636 e 289). Só dos toques; o contato segue elegível a outras áreas. Se o CRM já trata S6 como matriculado em qualquer turma, só confirma. | pessoa do marketing | cada turma sai só a sua e o contato que pagou uma turma continua a receber os toques das outras da área |
| DEC4 | **Opcional: o pré-início de 68632 de 05/04 passa à frente do de 68628 só nesse dia.** É a última mensagem de 68632 antes de a regra 8 fechar a lista; 68628 ainda tem o PI de 28/04. Muda quem perde o toque para quem está em A10 e A4. | cmo | vale a nota: quem está em A10 e A4 perde o pré-início de 68632 |
| DEC5 | **NP2 e página de abril antes de 11/12:** o T1 (01/12) e o T2 (09/12) da NP2 de A3, A4, A7, A10 e A14 infectologia saem sem link para a turma de abril (ou ficam suspensos nessas áreas) e o T3 (16/12) só depois da conferência de 11/12. Sem acúmulo se a conferência atrasar. | cmo, com a pessoa do marketing | a NP2 aponta para páginas com "CERTIFICADO PELO MEC", contra a regra 13, salvo decisão humana registrada no OC1 com a regulação |
| DEC6 | **UTM:** manter os nomes do O7 (202701; 202702 em 366), usar o mesmo nome nos links da NP2 de dezembro e registrar o desvio na tabela de correspondência | pessoa do marketing | o nome muda para 202612 nos links de dezembro e os templates da Meta voltam à aprovação |
| DEC7 | **A14 por curso:** lista e flag de NP2 de A14 por [curso_de_interesse] (L-A14-679 só para infectologia ou 679); sem a marca, o contato não entra | cmo | A14 numa lista só: 679 vence todos os A14 do lote B pela data, mas a flag de A14 em 22/01 tiraria da NP2 quem quer 382, 699 ou 60 antes do kit deles |
| DEC8 | **Newsletter por WhatsApp nos dias de kit (19/02, 05/03 e 30/04):** o kit vence e a versão da newsletter não muda de dia. Nota ao agente newsletter, sem alterar o arquivo dele, com a edição 7 sem 662 e só com 366 se a data estiver confirmada (CF7) | newsletter, com o cmo | a newsletter por WhatsApp concorre com o kit e pela fila perde o dia do mesmo jeito (prioridade 5) |

---

## 16. Etapas, cortes e o workflow de reuso

### 16.1 Quantas etapas

| Fluxo | Etapas | Chamadas de agente | Aprovações humanas |
|---|---|---|---|
| Este desenho (O10, lote A) | 1 | 1 (arquiteto-de-fluxos) | 1 |
| Conferência do qa (O18c, "onda3c") | 1 | 1 (qa-de-marketing) | 1 |
| Execução no CRM (etapas 4 a 7 do documento de fluxo) | 4 | 0 (humano) | 4 mais 1 por toque (OC2) |
| Nova versão com o lote B (O10, 22/01/2027) | 1 | 1 | 1 |
| Workflow de reuso `/conferir-fila-de-mensagens` (16.3) | 2 | 2 | 2 |

### 16.2 O que foi cortado (nenhum corte muda a entrega)

1. Agente próprio para validar calendário: cortado. A conta está nas seções 7 a 9 e o qa-de-marketing a confere.
2. Nova rodada de copy-de-mensagens: cortada. Os textos e as datas são os do O7; este arquivo não toca neles. As duas correções de contagem (CF1 e CF2) vão como nota.
3. Reenvio de e-mail para quem não abriu: cortado (DEC4 da onda 2 mantida). Cada reenvio seria um toque a mais na fila.
4. Lista por curso em A1, A2, A3, A4, A7 e A10: cortada. A área basta; só A14 vira lista de curso.
5. Lista própria para 68632 e para 366: cortada. A4 é uma lista com duas marcas de turma.
6. Exceção codificada para 20/01, 01/03 ou 17/02: cortada. A fila gulosa resolve sozinha.
7. Nota GUT por contato: cortada. A nota é por turma e só desempata data de referência igual.
8. Painel novo de acompanhamento: cortado. Usa-se o painel somado que o analista-de-dados já tem como encomenda (13.4 do plano geral).
9. Datas de contingência para página atrasada: não reservadas. Se o atraso acontecer, o arquiteto entrega nova versão com a conta da seção 9 refeita (como o CF8 da onda 2), para não bloquear dias à toa.
10. Lista, regra e toque para 662: nenhum (espera total, OU18).
11. Workflow semanal novo de revisão: cortado. A revisão de segunda-feira do cmo já existe e lê as contagens.

### 16.3 Texto do workflow para .claude/commands (não gravado)

Arquivo `.claude/commands/conferir-fila-de-mensagens.md`, versão revisada do texto proposto na onda 2 (fila em ordem de prioridade, conferência contra ondas anteriores e supressões por semana). Serve para a onda 3, lote B, e para qualquer onda ou turma nova na mesma base:

```
---
description: Confere listas, opt-in, saídas, fila D2, limite de 1 por dia, teto semanal, saída da NP2 e UTM de um lote de turmas contra as ondas já aprovadas e a newsletter. Cadeia: arquiteto-de-fluxos, qa-de-marketing
argument-hint: [linha: pos, livres ou eventos] [caminho do arquivo com os toques do lote] [turmas do lote] [arquivos de fluxos das ondas anteriores]
---
Execute o workflow "Conferir a fila de mensagens de um lote".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha, arquivo de toques, turmas e arquivos de fluxos anteriores deste pedido: $ARGUMENTS

Regras: siga o teto D16 e as regras E1 a E4 da seção 13 de saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md e a fila D2 da seção 12, com a data de referência da decisão do plano da onda (início antes de começar, véspera do 3º módulo depois). Dados de curso só de contexto/catalogo-de-cursos.md; o que faltar vira [CONFIRMAR NO CATÁLOGO]. Nenhum dado pessoal. Nada é ligado, agendado, enviado ou pago. Nunca use travessão.

1. Use o agente arquiteto-de-fluxos para produzir as listas por área, o opt-in S2 e S3, as regras de saída, a fila D2 aplicada em ordem de prioridade, a conta semana a semana do pior caso contra os toques das ondas anteriores e a newsletter, a saída da NP2 só nas áreas que ainda não saíram, as supressões previstas por semana (só números), a UTM do CRM, o fluxo de cada turma e os pedidos de aprovação (o que, por que, quanto, efeito esperado, como desfazer). Use a skill matriz-gut (.claude/skills/matriz-gut/SKILL.md) só para desempatar toques com a mesma data de referência e a skill mapear-fluxo (.claude/skills/mapear-fluxo/SKILL.md) para o SIPOC. Salve e passe o arquivo para a próxima etapa.
2. Use o agente qa-de-marketing para conferir o arquivo contra os toques aprovados, as datas e os dias da semana, o teto, a fila e as supressões, e devolver aprovado ou as correções numeradas. Salve e passe o arquivo para a próxima etapa.
3. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.
4. Rode também auditorias/07-email-e-whatsapp.md nas listas e nas saídas.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: nenhum dia do lote tem dois toques para o mesmo contato, nenhuma semana passa de 2 WhatsApp e 2 e-mails (3 somando canais na base da Graduação), todo empate de data de referência tem desempate escrito, toda supressão prevista tem número por semana, toda automação tem pedido de aprovação com o que desfazer, nenhuma UTM foge de pos_<código>_<AAAAMM> e o lote está aprovado pelo qa-de-marketing e pela pessoa do marketing.
```

Este workflow tem **2 etapas de agente**: 2 chamadas ao Claude e 2 aprovações humanas, mais as auditorias. Cita só agentes, skills e auditorias que existem no repositório (arquiteto-de-fluxos, qa-de-marketing, matriz-gut, mapear-fluxo, auditorias 10-operacoes, 07-email-e-whatsapp e conformidade-educacional).

---

## 17. Auditorias

**auditorias/10-operacoes.md**
- [ ] conhecimento/INDICE.md está atualizado: **não feito por este agente** (a encomenda manda editar só este arquivo, que agora são três partes); o orquestrador atualiza.
- [x] Todo workflow cita só agentes, skills e auditorias que existem (arquiteto-de-fluxos, qa-de-marketing, matriz-gut, mapear-fluxo, auditorias 10-operacoes, 07-email-e-whatsapp e conformidade-educacional).
- [x] Todo workflow termina com auditoria e critério de pronto conferível (16.3 e "Concluído quando" da seção 1.2).
- [x] Aprovação humana antes de publicar, enviar ou pagar (AF1 a AF7, DEC1 a DEC8, OC2 por toque).
- [x] Acesso mínimo: a squad escreve texto; o CRM é de humano.
- [x] Nenhuma chave em arquivo de texto.
- [x] Documento com data de revisão (11/12/2026, 04/01/2027 e 22/01/2027).
- [ ] Toda peça pública passou por qa-de-marketing e por conformidade-educacional: este arquivo não é peça pública; vai ao qa (O18c, "onda3c").
- [x] Dados de curso batem com o catálogo: nome, turma, campus, modalidade e início citados vêm do catálogo (seção 2) e do plano; nenhum preço, bolsa ou ato regulatório neste arquivo. As metas em reais da seção 6.2 são o total do catálogo multiplicado por 15 (decisão 16).

**auditorias/07-email-e-whatsapp.md**
- [x] Consentimento e descadastro funcionando: EN1 a EN3, SA5; teste de humano antes do primeiro envio.
- [x] Cada mensagem tem um objetivo: herdado do O7.
- [x] Assuntos e primeiras linhas honestos: do O7; não tocados aqui.
- [x] Segmentos recebem mensagens da etapa da jornada: S2 e S3 da área; S6, S8 e S9 fora (EN6).
- [x] Réguas têm regras de saída: seção 4 e saídas por turma da seção 13.
- [ ] Resultados registrados para cada envio: registro de supressões (AF7) e UTM (seção 12); depende do CRM [CONFIRMAR P15].
- [ ] Cliques, respostas e conversões medidos: UTM e contagem de respostas "TURMA"; o PI não tem clique.
- [x] WhatsApp em horário comercial, com frequência humana e template da Meta quando usar a API: CC5, CC7, CC8; template só se a Ufape usar API (U11a).

**auditorias/conformidade-educacional.md**
- [x] Nenhuma peça nova: o arquivo não tem texto de mensagem nem de página.
- [x] Sem frase ligada ao MEC, sem preço, sem bolsa, sem "últimas vagas", sem nota de curso, sem promessa: nada disso aparece. A frase "CERTIFICADO PELO MEC" só aparece entre aspas como o que a página de origem traz e que bloqueia o envio (CC12).
- [x] WhatsApp e e-mail só com consentimento e saída fácil (EN1 a EN3, SA5).
- [x] Nenhum dado pessoal em peça ou arquivo de trabalho.
- [x] Status "aberto" (ou "verificar" só por já ter começado, decisão 18): CC4.
- [x] Regra 8 de 68632 (nada sobre entrada depois do início, lista fecha em 09/04 sem OU3): SA4 e 13.6.
- [ ] Página de destino entrega o que a mensagem promete: pendente do OC1-A; trava no CC12 e na DEC5.
- [ ] Formulários com finalidade e política de privacidade: pendente externo, conferido em 11/12 e 04/01.

**Resultado:** pronto para o qa-de-marketing (O18c). A execução depende do OC2 por toque, do OC1-A, de AF1 a AF7, de DEC1 a DEC8 e das respostas de OU3, OU19, OU20, OU21, OU25, OU29, U11a e P15. Busca de travessão e meia-risca: feita pelo agente na escrita; a conferência por busca é do orquestrador.

**Próximo agente sugerido:** qa-de-marketing (O18c, revisão "onda3c": fluxos, com auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md).

---

## Fatos (com fonte)

- Os 55 toques do lote A (16 e-mails e 39 WhatsApp), mais 1 reservado de 68632, as datas, os horários (e-mail 9h, WhatsApp 10h), os templates, os IDs de utm_content e a regra de que 679, 68635 e 366 dependem do dia do 3º módulo: O7 (copy-de-mensagens-pos-2026-10-27-onda3.md, seções 0.1, 0.2 e 2) e plano do CMO da onda 3, seção 7.3. A contagem de 55 (e não 49) e os 14 dias com mais de um toque são contas deste arquivo sobre essas tabelas (seção 7.2).
- Início, turma, campus, modalidade e status "aberto" das 8 turmas: contexto/catalogo-de-cursos.md, seção 2 (linhas de 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609). Totais do catálogo usados nas metas: R$ 33.000,00 (679, 68632, 68635 e 366), R$ 38.940,00 (68628), R$ 36.000,00 (68617), R$ 37.950,00 (68636) e R$ 32.450,00 (68609).
- 3º módulo e fechamento das listas (26 e 27/06 em 68628 e 68609; 19 e 20/06 em 68617 e 68636; 12 e 13/06 em 68632; junho sem dia em 679, 68635 e 366): plano da onda 3, seções 1.1 e 4.1 a 4.9; O7, seção 0.1. Regra 8 e mídia de 68632 até 09/04: plano, seção 2.1 (regra 8) e 4.2.
- Teto de 2 WhatsApp e 2 e-mails por semana somando linhas, 1 por dia, janela, dias sem campanha, regras E1 a E4 e fila D2 com a newsletter em 5º: plano da onda 3, regra 11; newsletter-geral, seção 3.2; docs/execucao-2026-10-26.md, decisão 17.
- Data de referência (início antes, véspera do 3º módulo depois): plano da onda 3, seção 6, decisão 4; resultado da fila em cada semana de 7.4 do plano (que este arquivo confere).
- Datas da onda 2 (37), onda 1 (6) e das edições da newsletter: plano da onda 3, seção 7.3; arquiteto-de-fluxos-pos-2026-10-27-onda2.md, seção 7.1; newsletter-geral, seção 3.1. NP2 (T1 em 01/12, T2 em 09/12, T3 em 16/12 e T4 em 05/01): campanhas-de-nutricao-pos, seção 4. Saída da NP2 por área nas datas de 04/01, 20/01 e 22/01: plano da onda 3, seção 7.3, regra "Saída da NP2".
- Notas de grupo GUT 30 (5, 2, 3) das turmas de abril: cmo-geral, seção 3. Notas da onda 2 (341 = 80; 289 e 68615 = 48; 657 e 333 = 45): meu arquivo da onda 2, seção 7.4. Desempate (urgência, depois menor esforço): skill matriz-gut, passo 5.
- Metas em reais por turma de abril: plano da onda 3, seção 1 (15 vezes o total do catálogo; decisão 16).
- Decisões 11, 14, 16, 17 e 18: docs/execucao-2026-10-26.md. Pós-início: matrícula até o 3º módulo (decisão 18).
- Calendário: 01/01/2027 é sexta-feira; 08 e 09/02 são Carnaval; 10/02 é Cinzas; 26/03 é sexta-feira da Paixão; 28/03 é domingo de Páscoa; 21/04 é quarta-feira (Tiradentes); 01/05 é sábado; 04/01, 15/02, 22/02, 01/03, 08/03, 15/03, 29/03, 05/04, 12/04, 19/04, 26/04 e 03/05 são segundas-feiras.
- As ferramentas do agente arquiteto-de-fluxos são Read e Write: ele não executa no CRM (.claude/agents/arquiteto-de-fluxos.md).

## [SUPOSIÇÃO]

- As notas GUT por turma e a escala (G pela meta em reais, U pela data de início com ajustes para 68632 e 366, T pela turma I) (seção 6.2), ancoradas nas notas da onda 2.
- [data_do_item] igual à data limite quando a turma já começou (herdada da onda 2); posição dos pós-inícios sem dia (679, 68635 e 366) depois de qualquer dia de junho, como posição na fila, nunca como data de peça.
- Trava de segurança de 31/05/2027 para o fechamento das listas de 679, 68635 e 366 até a OU25.
- Fila em ordem de prioridade (DEC1) como leitura correta da D2 e do resultado já aprovado da tabela 7.4 da onda 2.
- Pagou uma turma, sai das outras da mesma área (DEC3); resposta a um toque de uma turma de A4 só tira a turma respondida.
- Não filtrar L-A1 e L-A4 por praça.
- A14 com lista e flag de NP2 por curso (DEC7).
- "Pior caso" como o contato que está em todas as áreas que disputam a semana, com opt-in nos dois canais.
- Geração da lista às 06h e reconferência 30 minutos antes; horário de verificação da OU20 às 18h de 03/02; aprovação dos pedidos até 11/12; testes de 14 a 18/12.
- Horários de job (00h05) para a saída por data limite e para a flag da NP2.
- Edições da newsletter depois de 18/02 em quintas quinzenais (decisão 10 do plano) e versão de WhatsApp no dia seguinte a cada edição.
- Nomes provisórios dos campos do CRM da seção 14.
- Resposta com "parar" ou parecida vai a humano para registro; a flag da NP2 liga mesmo com o primeiro toque do kit suprimido.
- Os prazos de 48 h e de 24 h dependem da ferramenta; a regra de E3 é o limite máximo.
- Que o CRM pode tratar S6 como "matriculado em qualquer turma de Pós" (efeito da DEC3).

## [CONFIRMAR]

- **OU3** (reposição dos módulos presenciais; 68632 depois do início), **OU6** (3º módulo: véspera ou 1º dia), **OU19** (data de 679 e linha "Citopatologia 03/04"), **OU20** (início de 366: 10/04 ou 24/04), **OU21** (data de 68636), **OU25** (dia do 3º módulo de 679, 68635 e 366), **OU29** (URL "/v/" e turma de 68617), **OU34** (quem representa 68632 e 366), **U11** (valor da inscrição, para distinguir inscrição de 1ª mensalidade na SA1), **U11a** (API oficial do WhatsApp e templates), **P15** (ferramenta de CRM, e-mail e WhatsApp, e rastreio de wa.me), **OU18** (662, que fica sem lista).
- Contatos com opt-in por área e canal e o tamanho de cada lista (OC2); campo de finalidade aceita; existência da marca [curso_de_interesse]; como o CRM marca conversa ativa com o time; se o CRM trata S6 como matriculado em qualquer turma.
- Se as flags de NP2 de A1 (05/01) e A2 (08/12) da onda 2 foram ligadas (CF10); se AF1 da onda 2 foi aprovada (L-A1 e L-A2).
- Quem executa no CRM, quem aprova cada tipo de peça (A9) e o custo por conversa de marketing, se houver API.
- Datas da newsletter depois de 18/02 e existência de WhatsApp nas edições 3 a 7; calendário da Graduação (CF6 da onda 2).
- Decisão humana sobre a NP2 com link para página de abril antes de 11/12 (DEC5) e sobre página com frase ligada ao MEC (regra 13, OC1 com a regulação).
- Tabela de correspondência entre nomes de campanha (analise-de-midia) para os desvios de mês (DEC6).
- Toques do lote B (O10 de 22/01/2027), que refaz a conta das semanas de 03 a 09/05 e seguintes.
