# QA de marketing, terceira passagem: itens R-P1 a R-P3 e R-M1 a R-M6 do Workshop Brasileiro de Neuromonitorização (20 e 21/11/2026)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** eventos (subtipo workshop)
- **Data:** 27/10/2026 (terça-feira)
- **Escopo:** só os itens R-P1 a R-P3 e R-M1 a R-M6 de saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b-b.md, mais checagem de problema novo criado pelas correções (commit b39be62)
- **Peças reconferidas (não editadas):**
  - saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md
- Nenhum dado pessoal lido ou citado. Nada publicado, enviado ou pago.

## Vereditos

| Arquivo | Veredito | Para onde vai |
|---|---|---|
| posts-sociais-eventos-2026-10-26.md | **CORRIGIR** | Volta ao posts-sociais, 1 troca de texto (nome do evento na alternativa sem [T] de P4) |
| copy-de-mensagens-eventos-2026-10-26.md | **APROVADO** | Segue para a aprovação humana da pessoa do marketing, com os bloqueios externos declarados |

---

## 1. Posts sociais

| # | Resultado | Trecho atual (com linha) |
|---|---|---|
| R-P1 | **APROVADO** | Linha 262: "[T] Quatro situações em que este workshop faz sentido. Sem [T]: Três situações em que este workshop faz sentido." |
| R-P2 | **CORRIGIR** (problema novo na correção) | Linha 313: "[T] Duas formas de participar do Workshop Brasileiro de Neuromonitorização." Linha 333: "**Ponto de vista:** [T] A escolha é entre ir e praticar, ... Sem [T]: O post diz o que cada dia inclui." Linha 332 (nota ajustada): "A primeira linha do corpo e o "Ponto de vista" também são [T]: sem [T], a primeira linha vira "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia: presencial, sexta e sábado."" |
| R-P3 | **APROVADO** | Linha 67: "Sem certificado e sem preço; cartão extra e resposta do corpo são [T]" |

**Detalhe de R-P2.** As marcas [T] e a nota estão certas. O problema está na versão sem [T] da primeira linha: ela usa a forma longa do nome, e a regra 11 do próprio arquivo (decisão 7; SEv2 do qa) diz que a primeira menção é "Workshop Brasileiro de Neuromonitorização" e que a forma longa só entra com autorização da Ufape [CONFIRMAR]. Registro: essa forma longa veio do texto que eu mesmo sugeri na revisão anterior (qa-de-marketing-eventos-2026-10-26-b-b.md, seção 1.5); o agente aplicou a sugestão como pedida. A correção é minha.

- Trocar: "sem [T], a primeira linha vira "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia: presencial, sexta e sábado.""
- Por: "sem [T], a primeira linha vira "Workshop Brasileiro de Neuromonitorização: presencial, sexta e sábado.""

**Varredura de problema novo nos trechos corrigidos (linhas 67, 262, 313, 332 a 334):** sem travessão nem meia-risca; sem certificado nem MEC; sem urgência; sem dado pessoal; sem número novo (as "três situações" batem com os cartões 2, 3 e 4 de P5).

**Veredito do arquivo 1: CORRIGIR.** Uma troca de texto. Depois dela o rascunho pode seguir para a aprovação humana, sem nova passagem completa do QA (basta conferir a linha 332).

---

## 2. Copy de mensagens

| # | Resultado | Trecho atual (com linha) |
|---|---|---|
| R-M1 | **APROVADO** | M2 follow-up WhatsApp, linha 320: "Validade do cupom: [CONFIRMAR]." M2 follow-up e-mail, linha 368: "Validade do cupom: [CONFIRMAR]." M3 WhatsApp aluno, linha 525: "comprovando o vínculo na secretaria. Validade do cupom: [CONFIRMAR]." R8, linha 1036: "Validade do cupom: [CONFIRMAR]." |
| R-M2 | **APROVADO** | Linha 466: "3. [T] Presencial ou só a teoria de sexta: veja como participar do workshop de 20 e 21/11" |
| R-M3 | **APROVADO** | As 8 linhas de preço [T] dizem "R$ 450,00 à vista (Pix ou boleto) ou 1x de R$ 450,00 no cartão": M1 WhatsApp A (linha 184), M1 WhatsApp B (198), M1 e-mail A (248), M1 e-mail B (265), M2 WhatsApp (309), M2 e-mail (356), M3 e-mail (480), M3 WhatsApp (519). Confere com o catálogo, seção 4 (produto 68634) |
| R-M4 | **APROVADO** | M6, linha 722: "O e-mail vai aos inscritos que autorizaram o contato por e-mail na inscrição [CONFIRMAR no checkout]". M7, linha 804: "O e-mail vai aos inscritos no presencial que autorizaram o contato por e-mail na inscrição [CONFIRMAR no checkout]" |
| R-M5 | **APROVADO** | M8, linha 870: "**Texto de pré-visualização:** Como acessar as aulas gravadas e informações sobre o certificado." |
| R-M6 | **APROVADO** | Seção 0.3, linha 93: "Os textos são em balões curtos, de até 3 linhas cada; no template, os balões viram um corpo único com quebras de linha." |

**Varredura de problema novo nos trechos corrigidos:** sem travessão nem meia-risca; a única menção a certificado tocada (M8, linha 870) não liga o certificado ao MEC nem promete data; sem urgência; sem dado pessoal (só campos entre colchetes); sem número inventado (condições do preço [T] copiadas do catálogo, seção 4). A lista de mudanças (linha 1185) descreve as correções sem extrapolar.

**Veredito do arquivo 2: APROVADO** como rascunho para a aprovação humana. Continuam bloqueados para envio, como o próprio arquivo declara (linha 1093): linhas de preço do presencial (E5), cupom sem validade (E6), todo trecho [T] e M1 versão B (verificação do 68634), M8 (AP8, link e prazo da gravação), M9 (A4, URL e [bloco_prova] com R7 e U3), WhatsApp de M6 e M7 (A2), templates Meta (A5) e opt-in no CRM e no checkout.

---

## 3. Conformidade educacional (só os itens tocados por esta passagem)

| Bloco | Item | Posts | Mensagens |
|---|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração e turno batem com o catálogo | [ ] Falha pontual: forma longa do nome na alternativa sem [T] de P4, linha 332 (R-P2) | [x] Passa |
| Dados do curso | Status "aberto" ou sem chamada | [x] Passa: P4 linhas 313 e 333 com [T] | [x] Passa: M3 assunto 3 com [T] |
| Preço e condições | Valor, parcelas e condições completas | [x] Sem mudança nesta passagem | [x] Passa no texto (R-M3); presencial segue pendente de E5, declarado |
| Preço e condições | Desconto com regra, público e validade | [x] Sem mudança nesta passagem | [x] Passa no texto (R-M1); validade real segue pendente de E6, declarado |
| Pessoas e dados | WhatsApp e e-mail com consentimento e saída | [x] Não se aplica | [x] Passa (R-M4); registro no checkout [CONFIRMAR] |
| Pessoas e dados | Nenhum dado pessoal | [x] Passa | [x] Passa |
| Regulação | Certificado sem ligação ao MEC | [x] Nenhum post cita | [x] Passa (R-M5) |
| Texto | Travessão e meia-risca | [x] Nenhum nos trechos corrigidos | [x] Nenhum nos trechos corrigidos |

Demais itens da conformidade: sem mudança em relação a qa-de-marketing-eventos-2026-10-26-b-b.md, seções 1.4 e 2.4 (não reabertos, como pedido).

Resultado no formato do checklist:
- Arquivo 1 (posts): Aprovado ( ) Bloqueado (x). Item bloqueado: nome do evento na versão sem [T] de P4 (R-P2, linha 332).
- Arquivo 2 (mensagens): Aprovado (x) Bloqueado ( ), como rascunho; envio das peças com pendência externa segue bloqueado, como declarado no arquivo.
- Revisado por: qa-de-marketing (agente). Revisão humana: [pendente]. Data: 27/10/2026.

## Suposições

1. [SUPOSIÇÃO] A regra 11 do arquivo de posts (forma curta do nome na primeira menção, decisão 7 e SEv2) vale também para as alternativas sem [T]. As mensagens usam a forma longa em todo o arquivo; essa divergência entre os dois arquivos é anterior e não foi reaberta.
2. [SUPOSIÇÃO] "Até 3 linhas" na seção 0.3 das mensagens se refere a linhas do texto-fonte, como no ajuste pedido em R-M6.

## Fontes

- saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b-b.md (itens R-P1 a R-P3 e R-M1 a R-M6)
- saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (versão do commit b39be62, linhas 1 a 523, onde estão todos os trechos corrigidos)
- saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md (versão do commit b39be62, lido inteiro)
- contexto/catalogo-de-cursos.md, seção 4 (produto 68634), conforme registrado na revisão anterior
