# QA de marketing (conferência d): versão 4 do lote de mensagens da onda 1 da Pós-graduação (698, 68610, 68608, 707, 68604 e 68606)

- **Agente:** qa-de-marketing (10 Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Peça revisada:** /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md, versão 4 (1.077 linhas). O arquivo não foi alterado por esta revisão.
- **Revisões anteriores:** qa-de-marketing-pos-2026-10-26-onda1-mensagens.md, -b.md e qa-de-marketing-pos-2026-10-27-onda1-mensagens-c.md (N1, M1 e M2), na mesma pasta.
- **Entradas lidas:**
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md, versão 4: seção 10 (E2 e E3), seção 11 inteira, tabela do OA9 e "Mudanças desta versão" (N2)
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
  - Releituras desta sessão: decisões 14 e 18 de docs/execucao-2026-10-26.md, fichas das outras 5 turmas, catálogo seção 2, cmo-geral 12.2 e 13, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md
- **Limite desta conferência:** o qa-de-marketing não tem ferramenta de terminal nesta sessão, então não rodou `git show ce629ea:<arquivo>`. A comparação das 5 turmas com a v3 foi feita lendo a v4 inteira contra a v3, que foi lida por inteiro nesta mesma sessão. Se o orquestrador quiser a prova pelo git, basta conferir o diff das linhas citadas na seção 2.
- **Dados pessoais:** nenhum.

---

## Veredito: CORRIGIR (2 grupos de correção de texto, sem mudança de mensagem ao candidato)

As correções N1, M1 e M2 entraram com o texto do relatório c. Nas 5 turmas, o texto das mensagens não mudou em relação à v3. A seção 6A (68606) confere com a ficha e com o OA9 e passa em conformidade.

Ficam duas incoerências com o plano do cmo v4, nas regras de envio e nas tabelas de teto, que o CRM vai seguir:
- **D1:** a UTM segue o mês de cada envio, mas o plano manda usar o mês do primeiro envio.
- **D2:** o arquivo ainda trata provas, Livres, 616 e 68665 como réguas ativas. Pela seção 11 do plano, elas não enviam. A linha 84, do jeito que está, faria o CRM reservar 29/10 para o 68665 e suprimir o T2 da 698 na área A2, o contrário do que o cmo decidiu.

Os corpos de T1 (28/10) e de T2 (29/10) das 6 turmas estão aprovados como texto. Nenhuma correção abaixo mexe neles. As correções D1 e D2 precisam entrar antes de o OA9 ir à aprovação humana, porque mudam as instruções ao CRM.

---

## 1. Correções obrigatórias (texto exato)

### D1. UTM com o mês do primeiro envio (plano do cmo v4, N2 e E2 f)

| Linha | Hoje | Trocar por |
|---|---|---|
| 113 | "utm_campaign=pos_<código>_<AAAAMM do envio> (202610 para os envios de outubro, 202611 para novembro, 202612 para dezembro, 202701 para janeiro)" | "utm_campaign=pos_<código>_<AAAAMM do primeiro envio da turma>, igual em todos os toques da turma (nesta onda, pos_<código>_202610 nas 6 turmas)" |
| 792 | "utm_campaign=pos_68606_202611" | "utm_campaign=pos_68606_202610" |
| 991 | "UTM com utm_medium=crm e utm_campaign=pos_<código>_<AAAAMM do envio> nas mensagens com link de página." | "UTM com utm_medium=crm e utm_campaign=pos_<código>_202610 (mês do primeiro envio, igual em todos os toques da turma) nas mensagens com link de página." |

### D2. Réguas que não enviam (plano do cmo v4, seção 11; decisão 14)

**Linha 83, trocar o item inteiro por:**
"- Pós: até 2 WhatsApp e 2 e-mails de campanha por contato por semana, no máximo 1 mensagem de campanha por dia, **entre todas as campanhas autorizadas a enviar** (Workshop, Graduação, newsletter e estas). Pela decisão 14 e pela seção 11 do plano do cmo, a régua das provas e os kits de Livres (inclusive 68665, 68666 e 616) não enviam campanha enquanto a decisão 14 valer e não disputam dia com a Pós."

**Linha 84, trocar o item inteiro por:**
"- **A contagem inclui os toques principais já agendados:** Workshop M1 ou M2 por e-mail em 30/10, 9h (e por WhatsApp em 30/10 só para quem não tem opt-in de e-mail) e mensagens da Graduação. O CRM reserva esses toques antes de liberar os deste arquivo."

**Linha 798, trocar por:**
"- **Data e horário de envio:** sex 06/11, 10h (dia útil). A régua das provas não envia nesta data (decisão 14; plano do cmo, seção 11)."

**Linha 949, trocar por:**
"Entram na conta os toques principais já agendados: Workshop M1 ou M2 por e-mail em 30/10, 9h (e por WhatsApp em 30/10 para quem não tem opt-in de e-mail) e Graduação. O 68665 não envia (decisão 14; plano do cmo, seção 11). Teto: até 2 WhatsApp, até 2 e-mails, 1 por dia entre todas as campanhas autorizadas."

**Linha 963, trocar o parágrafo inteiro por:**
"**29/10, área A2 (decidido pelo cmo, seção 11, choque 1).** Sai o T2 da 698 em 29/10, 10h, só com o site corrigido até 28/10, 18h. O 68665 não envia, porque Livres está suspenso pela decisão 14. Se a Ufape liberar Livres antes de 29/10, vale a remarcação da seção 11 do plano do cmo (o 68665 fica com 29/10 e o T2 da 698 passa para 03/11, 10h), num ciclo extra do cmo antes do envio."

**Linhas 965 a 977, trocar o título e a tabela da 8.2 por:**

"### 8.2 Toques posteriores de 707, 68604 e 68606 contra o que já está agendado

Pela seção 11 do plano do cmo, a régua das provas e os kits de Livres (inclusive 616) não enviam enquanto a decisão 14 valer. Os toques deste arquivo saem como estão. Se a decisão 14 mudar, valem as remarcações condicionais da seção 11 do plano do cmo, num ciclo extra do cmo antes do envio.

| Data | Toque | Choque com réguas autorizadas | Resolução |
|---|---|---|---|
| sex 06/11 | W2 de 68606 (WhatsApp) | nenhum (provas suspensas) | sai |
| ter 10/11 | W2 de 707 (WhatsApp) | nenhum (provas suspensas) | sai |
| qua 11/11 | W2 de 68604 (WhatsApp) | nenhum (Livres suspensos) | sai |
| ter 24/11 | E2 de 707 (e-mail) | nenhum (provas suspensas) | sai |
| ter 01/12 | W3 de 707 e E2 de 68604 | contato nas duas turmas: 1 por dia, vence 707 (3º módulo em 18/12) | sai |
| qua 02/12 | E2 de 68606 (e-mail) | nenhum (616 suspenso) | sai |
| ter 15/12 | W4 de 707 e W3 de 68604 | contato nas duas turmas: 1 por dia, vence 707; 21/12 a 03/01 é sem campanha | sai |
| qua 16/12 | W3 de 68606 | nenhum | sai |
| ter 12/01 | W4 de 68604 e W4 de 68606 | contato nas duas turmas: empate do 3º módulo (23/01/2027), vence a maior GUT da seção 3 do plano geral; a outra é suprimida | sai |"

**Linha 1058, trocar por:**
"- Empate de 12/01 entre 68604 e 68606 resolvido pela maior GUT da seção 3 do plano geral."

**Linha 1069, trocar por:**
"- Datas de envio da Graduação no CRM e se a decisão 14 muda para provas e Livres (ativa as remarcações condicionais da seção 11 do plano do cmo)."

---

## 2. Conferência de N1, M1 e M2 e do resto das 5 turmas

| Item | Linha da v4 | Resultado |
|---|---|---|
| N1, e-mail T1 de 68610 | 245: "- aulas online ao vivo e gravadas, e plantões de dúvidas mensais;" | entrou com o texto exato |
| N1, R4 de 68610 | 912: "A página informa que as aulas online são ao vivo e gravadas; como isso vale para quem entra depois, confirmo com a coordenação." | entrou com o texto exato |
| M1, E2 de 707 | 479: "- atendimentos clínicos reais em mutirões supervisionados." (sem gravação) | entrou com o texto exato |
| M2, E2 de 707 | 472 | entrou com o texto exato |
| M2, E2 de 68604 | 641 | entrou com o texto exato |
| Demais mensagens de 698, 68610, 68608, 707 e 68604 | seções 2 a 6.3 e 7 | corpos, assuntos, primeiras linhas, links e UTM de 28 e 29/10 iguais aos da v3. Só houve acréscimos de contexto: a nota da linha 382, que repete a M1; a inclusão de 68606 nos blocos fixos; e a de 68606 na R8 |

---

## 3. Seção 6A (68606) contra a ficha e o plano

**Dados conferidos com a ficha:**
- turma IX, 500 h, 24 módulos, semipresencial, São Paulo, link do produto 68606;
- início em 07/11/2026, sábado;
- módulo 1 em 07 e 08/11, online, com semiologia e fisiologia gastrointestinal;
- módulo 2 em 19 e 20/12, online;
- **3º módulo em 23 e 24/01/2027, online** (ficha, linha 68);
- módulos 1 a 5 online;
- módulo 6 presencial em 17 e 18/04/2027, com anatomia prática, cirurgia esofágica, gástrica e intestinal e parasitologia ou transplante fecal;
- "Grupo para discussão de casos entre os alunos e os coordenadores";
- coordenação Esp. Maria Carolina Pappalardo, com 38 nomes contando a coordenação (37 professores mais a coordenadora, linhas 263 a 300).

**Datas e dias da semana do OA9:**
- e-mails em 28/10 e em 02/12 (quarta);
- WhatsApp em 29/10, 06/11 (sexta, véspera do início), 16/12 (quarta) e 12/01/2027 (terça).

Todos caem em dia útil e fora dos dias sem campanha. Batem com a tabela do OA9.

**Regra e conformidade:**
- A frase da regra está completa no E2, no W3 e no W4.
- O E2 diz que os módulos em curso são online, que é a M2 aplicada.
- Nada promete gravação; a ficha não cita gravação.
- Não aparecem preço, matrícula com valor, bolsa, prova, MEC, estágio nem os superlativos da página ("referências nacionais", "emergente e carente de profissionais").
- A turma mínima, antes do início, aparece sem número.
- SAIR está em todos os WhatsApp e o descadastro em todos os e-mails.
- Todos os WhatsApp ficam abaixo de 1.024 caracteres (estimativa na leitura).

**Nome e UTM:**
- A forma curta "Pós-graduação em Gastroenterologia" aparece só em primeira linha (749 e 752). Aceita pelo mesmo critério da 68604.
- A UTM do W2 está na D1.

---

## 4. Ajustes recomendados (não bloqueiam)

- **W4 de 707 (518):** usar a primeira linha B.
- **E2 de 707, 68604 e 68606 (481, 650 e 827):** a frase "Parcelas, total e matrícula você vê na página da turma" aparece num e-mail sem link para a página. Ou o time passa o link na conversa, ou a frase sai.
- **Linha 1047:** a citação da régua das provas pode ficar como histórico, mas convém acrescentar "(suspensa pela decisão 14)".

## 5. Auditorias

- **auditorias/07-email-e-whatsapp.md:**
  - Atendidos no desenho: um objetivo por mensagem, honestidade, segmento, regra de saída e horário.
  - O item "frequência humana" fica atendido depois da D2, porque a regra de reserva passa a refletir as réguas que de fato enviam.
  - Seguem como pendente externo: medição (P15) e template da Meta (U11a).
- **auditorias/conformidade-educacional.md:**
  - Nenhum item falha nas 6 turmas.
  - O destino segue atendido com gate em 698, e as páginas seguem pendentes (A7, A12, A13).
  - A D1 e a D2 são de coerência operacional com o plano, não de conformidade.

## 6. Destino

Volta ao copy-de-mensagens só para a D1 e a D2, com o texto exato acima. Com elas aplicadas e o diff conferido pelo orquestrador (linhas 83, 84, 113, 792, 798, 949, 963, 965 a 977, 991, 1058 e 1069), o lote das 6 turmas segue para a aprovação humana (OA9). O T1 sai em 28/10 às 9h, com o gate de 698 e a decisão da regulação da regra 9. Nada foi publicado, enviado ou pago.

---

## Fatos (com fonte)

- Seção 11 do plano do cmo v4, linhas 408, 411, 415 e 416: a régua das provas e os kits de Livres (inclusive 68665, 68666 e 616) não enviam enquanto a decisão 14 valer; o T2 da 698 sai em 29/10; os toques de 707 e 68604 saem como estão.
- UTM com o mês do primeiro envio, igual em todos os toques da turma: plano do cmo v4, linha 390 (E2 f) e linha 436 (N2).
- Ficha de 68606: linhas 11, 13, 16, 17, 22, 51, 57 a 59, 62 a 63, 68 a 69, 91 a 96, 263 a 301.
- Decisão 14 e decisão 18: docs/execucao-2026-10-26.md, linhas 20 e 24.

## [SUPOSIÇÃO]

- A comparação da v4 com a v3 foi feita por leitura das duas versões nesta sessão, e não por `git show`.
- A contagem de caracteres dos WhatsApp de 68606 é estimada na leitura.

## [CONFIRMAR]

- OU3, OU4, OU6, OU7, OU8 e OU9; A6, A7, A12 e A13; regulação sobre o envio antes da troca da frase do MEC; U11 e U11a.
- Se e quando a decisão 14 muda (ativa as remarcações da seção 11 do plano do cmo).
- Regras do estágio de 68606 (as mensagens não citam).
