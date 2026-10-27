# QA de marketing, reconferência: posts sociais e copy de mensagens do Workshop de Neuromonitorização (20 e 21/11/2026)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** eventos (subtipo workshop)
- **Data:** 26/10/2026 (segunda-feira)
- **Tipo:** segunda passagem, item a item do QA anterior (saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b.md), mais varredura de regressão
- **Peças reconferidas (não editadas):**
  - saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (943 linhas, lido inteiro)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md (1154 linhas, lido inteiro)
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/eventos.md
  - contexto/catalogo-de-cursos.md ("Como usar"; seção 4, linha 68634; seção 9)
  - contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
  - auditorias/05-social.md, auditorias/07-email-e-whatsapp.md, auditorias/conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b.md
- Não abri faculdade.ufape.com.br. Nenhum dado pessoal lido ou citado. Nada publicado, enviado ou pago.

## Vereditos

| Arquivo | Veredito | Para onde vai |
|---|---|---|
| posts-sociais-eventos-2026-10-26.md | **CORRIGIR** | Volta ao posts-sociais (3 ajustes de texto, seção 1.4) |
| copy-de-mensagens-eventos-2026-10-26.md | **CORRIGIR** | Volta ao copy-de-mensagens (6 ajustes de texto, seção 2.4) |

Os dois arquivos resolveram todos os itens bloqueantes de texto do QA anterior. O que segue são resíduos menores encontrados na varredura de regressão (transmitido sem [T], cupom sem validade, gancho não cumprido, condição de envio). Além deles, continuam bloqueadas por dado externo as peças que dependem de E5 (parcelamento do presencial), E6 (validade do cupom), verificação do produto 68634, AP8 (texto de certificado) e autorização de imagem. Essas peças estão corretamente declaradas como bloqueadas nos dois arquivos e não impedem, sozinhas, a aprovação do rascunho depois dos ajustes; impedem a publicação ou o envio delas.

---

## 1. Arquivo 1: posts-sociais-eventos-2026-10-26.md

### 1.1 Reconferência dos itens do QA anterior

| # | Pedido | Situação | Onde conferi |
|---|---|---|---|
| P-C1 | [T] em S1 cartão 2, S2 cartão 1, tabela 3.1 linha 1 e seção 5 | **Resolvido** | S1 cartão 2 com [T] e regra de saída (linha 708); S2 cartão 1 com versão sem [T] (linha 709); tabela 3.1 com resposta sem [T] (linha 687); seção 5 libera S1 só sem o cartão 2 (linha 772); regra 8 reescrita (linha 37) |
| P-C2 | Gancho de P4 A com [T] e gancho sem transmitido | **Resolvido**, com resíduo R-P2 | Linhas 304, 305, 337 |
| P-C3 | P4 B bloqueada até E5; gancho alternativo 2 marcado [Versão B] | **Resolvido** no texto; peça segue bloqueada por E5 | Linhas 308, 318, 324, 346. Preço do transmitido confere com o catálogo, seção 4 (68634) |
| P-C4 | Cupom sem validade em P4 cartão 4, P6 e S3 | **Resolvido** no texto (validade [CONFIRMAR] explícita e bloqueio declarado); peças seguem bloqueadas por E6 | Linhas 326, 340, 346, 419, 425, 429, 710 |
| P-C5 | Linha final de P6 para a secretaria | **Resolvido** | Linha 424 |
| P-C6 | S2 cartão 5 x tabela 3.1 | **Resolvido** (as duas mandam valores, pagamento e cupom à secretaria) | Linhas 695, 709. Ver recomendação K4 na seção 3 |
| P-C7 | FAQ na semana 3 | **Resolvido**: P14 em 11/11, sem certificado e sem preço | Linhas 64, 350 a 396. Resíduo R-P3 no calendário |
| P-C8 | Dados que faltam, item 1 | **Resolvido** | Linha 929 |
| P-R1 a P-R3 (recomendações) | | P-R2 aplicada (linhas 173, 222); P-R3 registrada (linha 875); P-R1 registrada como preferência, mas a frase segue no corpo de P5 (linha 263) | Não bloqueia |

### 1.2 Varredura de regressão

| Verificação | Resultado |
|---|---|
| Transmitido sem marca [T] | **Falha pontual:** P4, primeira linha do corpo "Duas formas de participar..." (linha 311) e "Ponto de vista" (linha 331) falam das duas modalidades sem [T]. A nota da linha 330 não diz que essa frase sai. Demais menções (P1, P5, P6, P7, P8, P9, P13, P14, S1, S2, S3, tabela 3.1) estão marcadas |
| Cupom sem validade | Passa: toda peça que cita o cupom traz "Validade: [CONFIRMAR]" e está bloqueada (P4 cartão 4, P6, S3). S2 cartão 5 e P14 só encaminham dúvida à secretaria |
| Certificado em peça | Passa: nenhum post nem Story cita certificado ou MEC |
| Envio sem opt-in | Não se aplica (orgânico) |
| Gancho não cumprido | **Falha pontual:** P5, gancho alternativo 2 "Quatro situações em que este workshop faz sentido" (linha 260). Sem [T] liberado, o cartão 5 sai e o corpo fica com três situações |
| Travessão e meia-risca | Passa: nenhum encontrado na leitura completa |

### 1.3 auditorias/05-social.md, item por item

| Item | Resultado | Observação |
|---|---|---|
| A frequência de publicação segue o plano | [x] Passa | P1 a P4 e P14 nas semanas do briefing; um post de feed por dia |
| Todo post tem uma ideia clara | [x] Passa | |
| Os ganchos são cumpridos pelo conteúdo | [ ] Falha | P5 gancho alternativo 2 sem [T] (R-P1) |
| Histórias e números são reais | [x] Passa | Só ficha e catálogo |
| Os posts estão formatados para celular | [x] Passa | |
| As ações de comunidade aconteceram nesta semana | [x] Não se aplica ainda | Caixas de perguntas em 06/11 e 16/11 |
| Métricas são conversas qualificadas e leads | [x] Passa | Seção 6 |
| Toda imagem ou depoimento tem autorização registrada | [ ] Pendente externo | P11 e P12 com foto, S6, S8 e S9 com pessoas: bloqueados até a autorização; versões sem pessoa liberadas |
| Dados de curso batem com o catálogo | [ ] Falha pontual | Dados conferem (20/11, 16 h, 30 vagas, R$ 1.250,00, R$ 450,00 com condições da seção 4, cupom, local). Resíduo: frase de P4 sobre duas modalidades sem [T], com o 68634 em "verificar" (R-P2) |

### 1.4 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração e turno | [x] Passa |
| Dados do curso | Status "aberto" ou sem chamada | [ ] Falha pontual: P4 linha 311 e linha 331 (transmitido sem [T], 68634 em "verificar") |
| Dados do curso | Modalidade clara | [x] Passa ("apenas teórico" em toda menção [T]) |
| Regulação | Graduação, Pós, curso livre, nota MEC | [x] Não se aplica; nenhum post cita certificado ou MEC |
| Promessas e provas | Emprego, salário, aprovação, sucesso | [x] Passa |
| Promessas e provas | Empregabilidade ou satisfação | [x] Não se aplica |
| Promessas e provas | Superlativos | [x] Nenhum |
| Promessas e provas | Comparação com concorrente | [x] Nenhuma |
| Preço e condições | Valor, parcelas, condições completas | [ ] Pendente externo: P4 versão B bloqueada até E5 (declarado) |
| Preço e condições | Desconto com regra, público e validade | [ ] Pendente externo: P4 cartão 4, P6 e S3 bloqueados até E6 (declarado) |
| Preço e condições | Urgência real | [x] Passa |
| Preço e condições | Prouni, Fies | [x] Não se aplica |
| Pessoas e dados | Autorização de imagem | [ ] Pendente externo: P11 e P12 com foto, S6, S8, S9 com pessoas (declarado) |
| Pessoas e dados | Menores | [x] Não se aplica |
| Pessoas e dados | Formulários e privacidade | [x] Não se aplica aos posts |
| Pessoas e dados | Consentimento WhatsApp e e-mail | [x] Não se aplica |
| Pessoas e dados | Nenhum dado pessoal | [x] Passa |
| Plataformas | Políticas Meta e Google | [x] Passa (orgânico) |
| Plataformas | Página entrega o prometido | [x] Passa |
| Anúncios | Itens de anúncio | [x] Não se aplica; textos compatíveis |
| Texto | Travessão e meia-risca | [x] Nenhum |

### 1.5 Lista exata do que ainda falta (posts)

| # | Local | Problema | Correção |
|---|---|---|---|
| R-P1 | P5, gancho alternativo 2 (linha 260) | "Quatro situações" só é cumprido com o cartão 5 [T]; sem ele são três | Marcar [T] ou trocar por "Três situações em que este workshop faz sentido" na versão sem [T] |
| R-P2 | P4, primeira linha do corpo (linha 311) e "Ponto de vista" (linha 331) | Falam das duas modalidades sem [T] | Marcar as duas com [T]. Versão sem [T] da linha 311: "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia: presencial, sexta e sábado." Ponto de vista sem [T]: "O post diz o que cada dia inclui." Ajustar a nota da linha 330 |
| R-P3 | Calendário, linha 64 (P14) | Diz "cartão 1 é [T]", mas o cartão 1 de P14 é a capa; o [T] é o "cartão extra" (linha 392) e a resposta do corpo (linha 375) | Trocar por "cartão extra e resposta do corpo são [T]" |

Bloqueios externos que continuam (não são correção do agente): P4 versão B (E5), P4 cartão 4, P6 e S3 (E6), todo trecho [T] (68634), P9 e S7 (horário de chegada), P13 (68634 e venda da gravação), fotos de pessoas (autorização).

### 1.6 Veredito do arquivo 1

**CORRIGIR.** Volta ao posts-sociais com R-P1, R-P2 e R-P3. São ajustes de uma linha cada; depois deles, o rascunho pode seguir para a aprovação humana com os bloqueios externos da seção 5 do próprio arquivo.

---

## 2. Arquivo 2: copy-de-mensagens-eventos-2026-10-26.md

### 2.1 Reconferência dos itens do QA anterior

| # | Pedido | Situação | Onde conferi |
|---|---|---|---|
| C1 | [T] em todo trecho do transmitido; M1 B não enviada; R7 sem condições | **Resolvido**, com resíduos R-M2 e R-M3 | Regra 0.1 item 11 (linha 43); M1 (147, 156, 173, 179, 212, 237, 244); M2 (298, 345); M3 (469, 498, 508); R1, R4, R5, R7, R15; template c02 [T] |
| C2 | E-mail de M6 e M7 como mensagem do dia; feriado registrado | **Resolvido**, com resíduo R-M4 | M6 e M7 por e-mail às 7h (linhas 709 a 751, 791 a 821); feriado em 707, 712, 782 |
| C3 | Tirar ordem de passos do cupom | **Resolvido** | Linhas 279, 300, 341, 356, 357; R8 sem ordem |
| C4 | Datas de M3 WhatsApp | **Resolvido** | Linhas 497, 500; nota de datas (448) |
| C5 | Ganchos de M1 cumpridos | **Resolvido** | Linha 155 com aula citada no corpo (167); e-mail A abre a sexta com Guedel e awareness (227) |
| C6 | M8 transmitido incoerente | **Resolvido** | Linha 886 |
| C7 | R5 só com o texto da página | **Resolvido** | Linha 1017: sem "certificado de participação", sem carga, resposta sobre MEC conforme pedido, AP8 marcado |
| C8 | Regra de horário invertida | **Resolvido** | Linha 95 |
| C9 | Balões longos | **Resolvido** nas mensagens (M1 A, M6, M7 quebradas), com resíduo R-M6 na regra da seção 0.3 | Linhas 165 a 177, 760 a 767, 830 a 839 |
| C10 | Datas dos follow-ups de M1 | **Resolvido** | Linhas 194, 200, 262, 266 |
| C11 | E-mail de programação | **Resolvido**: M10 em 05/11, grade da ficha, sem docente, sem convidados, sem certificado, sem preço, com descadastro | Linhas 366 a 437 |
| C-R1 a C-R5 (recomendações) | | C-R1 aplicada (M9, linha 935; A4); C-R3 aplicada (frase de saída por extenso em M4 a M8); C-R2 registrada (linha 1099); C-R4 e C-R5 não aplicadas | Não bloqueia |

### 2.2 Varredura de regressão

| Verificação | Resultado |
|---|---|
| Transmitido sem marca [T] | **Falha pontual:** M3 e-mail, assunto 3 "Presencial ou só a teoria de sexta..." (linha 455) sem [T] na lista (a nota da linha 459 o condiciona, mas o CRM pega a lista). Demais menções marcadas. M4 a M8 seguem a inscrição já feita, regra declarada (linha 43) |
| Cupom sem validade | **Falha:** a validade [CONFIRMAR] falta em M3 WhatsApp versão aluno (linha 514), M2 follow-up WhatsApp (linha 309), M2 follow-up e-mail (linha 357) e R8 (linha 1020). M2 corpo e M3 e-mail aluno estão certos |
| Certificado em peça | Passa: só em M8 e R5, para inscritos, participantes ou quem pergunta, com [CONFIRMAR texto aprovado, AP8]; M8 bloqueada |
| Envio sem opt-in | **Falha pontual:** M6 e M7 por e-mail dizem "vai a todos os inscritos com e-mail" (linhas 711, 793), sem a condição da regra 0.1 item 9 ("só pelo canal que a pessoa consentiu, registro no checkout [CONFIRMAR]"). Mensagens de marketing estão com opt-in e saída |
| Gancho não cumprido | **Falha pontual:** M8, texto de pré-visualização "Como acessar as aulas gravadas e quando sai o certificado" (linha 859): o corpo não diz quando sai ([CONFIRMAR processo e prazo]). Demais assuntos e primeiras linhas conferidos |
| Travessão e meia-risca | Passa: nenhum encontrado na leitura completa |

### 2.3 auditorias/07-email-e-whatsapp.md, item por item

| Item | Resultado | Observação |
|---|---|---|
| Consentimento e descadastro funcionando | [ ] Falha pontual e pendente externo | Saída presente em todo texto. Resíduo R-M4 (M6 e M7 por e-mail sem condição de consentimento). Opt-in no CRM e no checkout [CONFIRMAR] |
| Cada mensagem tem um objetivo | [x] Passa | |
| Assuntos e primeiras linhas honestos | [ ] Falha pontual | M8 pré-visualização (R-M5); M3 assunto 3 sem [T] (R-M2) |
| Segmentos recebem mensagens da etapa | [x] Passa | |
| Réguas têm regras de saída | [x] Passa | Inclui M10 |
| Resultados registrados por envio | [ ] Pendente externo | CRM e P15 |
| Cliques, respostas e conversões medidos | [ ] Pendente externo | UTM c01 a c12 definidas |
| WhatsApp em horário comercial, frequência humana, template Meta | [ ] Pendente externo | Marketing em dia útil e horário comercial; M6 e M7 por WhatsApp como exceção a aprovar (A2), com o e-mail cobrindo o dia; templates a aprovar (A5) |

### 2.4 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração e turno | [x] Passa; M9 confere com o catálogo, seção 2 (conferência do QA anterior mantida) |
| Dados do curso | Status "aberto" ou sem chamada | [ ] Falha pontual: M3 assunto 3 sem [T] (R-M2) |
| Dados do curso | Modalidade clara | [x] Passa |
| Regulação | Graduação | [x] Não se aplica |
| Regulação | Pós lato sensu sem "reconhecida pelo MEC" | [x] Passa (M9) |
| Regulação | Curso livre: não confere diploma | [ ] Pendente externo: texto oficial de certificado de eventos [PREENCHER COM A REGULAÇÃO]; M8 e R5 usam só a frase da página com AP8 e estão bloqueadas |
| Regulação | Nota MEC | [x] Nenhuma |
| Promessas e provas | Emprego, salário, aprovação, sucesso | [x] Passa |
| Promessas e provas | Empregabilidade ou satisfação | [x] Não se aplica |
| Promessas e provas | Superlativos | [x] Nenhum |
| Promessas e provas | Comparação com concorrente | [x] Nenhuma |
| Preço e condições | Valor, parcelas, condições completas | [ ] Falha: linhas de preço [T] dizem só "R$ 450,00", sem as condições do catálogo, seção 4 (R-M3). Presencial pendente de E5 (declarado) |
| Preço e condições | Desconto com regra, público e validade | [ ] Falha: validade ausente em M3 WhatsApp aluno, M2 follow-ups e R8 (R-M1). Demais pendentes de E6 (declarado) |
| Preço e condições | Urgência real | [x] Passa |
| Preço e condições | Prouni, Fies | [x] Não se aplica |
| Pessoas e dados | Autorização de imagem e nome | [x] Passa; R11 com [CONFIRMAR autorização] |
| Pessoas e dados | Menores | [x] Não se aplica |
| Pessoas e dados | Formulários e privacidade | [ ] Pendente externo: checkout [CONFIRMAR no site] |
| Pessoas e dados | WhatsApp e e-mail com consentimento e saída | [ ] Falha pontual: M6 e M7 por e-mail (R-M4) |
| Pessoas e dados | Nenhum dado pessoal | [x] Passa |
| Plataformas | Políticas Meta e Google | [x] Passa |
| Plataformas | Página entrega o prometido | [x] Passa, com a ressalva E1 e E12 da página |
| Anúncios | Itens de anúncio | [x] Não se aplica |
| Texto | Travessão e meia-risca | [x] Nenhum |

### 2.5 Lista exata do que ainda falta (mensagens)

| # | Local | Problema | Correção |
|---|---|---|---|
| R-M1 | M3 WhatsApp aluno (linha 514), M2 follow-up WhatsApp (linha 309), M2 follow-up e-mail (linha 357), R8 (linha 1020) | Cupom citado sem validade | Acrescentar "Validade do cupom: [CONFIRMAR]." em cada um, como já está em M2 corpo e M3 e-mail |
| R-M2 | M3 e-mail, assunto 3 (linha 455) | Cita o transmitido sem [T] na lista de assuntos | Marcar "[T]" no início do assunto 3, como em M1 assunto 5 |
| R-M3 | Linhas de preço [T]: M1 WhatsApp A (173) e B (187), M1 e-mail A (237) e B (254), M2 WhatsApp (298) e e-mail (345), M3 e-mail (469) e WhatsApp (508) | "R$ 450,00" sem as condições do catálogo, seção 4 | Trocar por "R$ 450,00 à vista (Pix ou boleto) ou 1x de R$ 450,00 no cartão", como nos posts (P4 versão B) |
| R-M4 | M6 segmento (linha 711) e M7 segmento (linha 793) | E-mail do dia "a todos os inscritos com e-mail", sem a condição de consentimento da regra 0.1 item 9 | "O e-mail vai aos inscritos que autorizaram o contato por e-mail na inscrição [CONFIRMAR no checkout]" |
| R-M5 | M8, texto de pré-visualização (linha 859) | Promete "quando sai o certificado", e o corpo não diz | "Como acessar as aulas gravadas e informações sobre o certificado." |
| R-M6 | Seção 0.3 (linha 91) | Afirma "Os textos têm até 3 balões curtos", mas M1 A tem 5 blocos de conteúdo | Ajustar a frase ("balões curtos, de até 3 linhas cada") ou reduzir M1 A a 3 balões |

Bloqueios externos que continuam (não são correção do agente): toda linha de preço do presencial (E5), M2 e M3 aluno (E6), todo trecho [T] e M1 versão B (68634), M8 (AP8, link e prazo da gravação), M9 (AP10 e URL), M6 e M7 por WhatsApp (A2), templates Meta (A5).

### 2.6 Veredito do arquivo 2

**CORRIGIR.** Volta ao copy-de-mensagens com R-M1 a R-M6. R-M1, R-M3 e R-M4 tocam itens da conformidade (desconto, preço, consentimento) e bloqueiam pela regra; R-M2, R-M5 e R-M6 são de honestidade de assunto e consistência.

---

## 3. Consistência entre as peças (atualização da tabela K do QA anterior)

| # | Tema | Situação agora |
|---|---|---|
| K1 | Transmitido (68634) | Alinhado: mesma regra [T] nos dois arquivos; pedido A6 de regra única à pessoa do marketing. Resíduos R-P2 e R-M2 |
| K2 | Certificado | Sem certificado nos posts; mensagens só a inscritos, participantes ou quem pergunta, com AP8. Divergência briefing x casa segue para decisão humana |
| K3 | Cupom | Alinhado (sem ordem de passos). Resíduo R-M1 |
| K4 | Dúvida sobre pagamento | Posts mandam à secretaria; mensagens (R7) ao time de vendas, com escalada ao financeiro. Não bloqueia; recomendação: a pessoa do marketing define um único destino para pagamento |
| K5 | Calendário | E-mail de programação (M10, 05/11) e FAQ (P14, 11/11) incluídos. P7 em 13/11 com pedido ao estrategia-de-campanha. Agradecimento de 21/11 registrado como troca (C-R2) |
| K6 | Kit mínimo | Cumprido: 4 posts, convite, programação, lembrete, véspera, dia (e-mail em qualquer cenário) |
| K7 e K8 | Horário e grafia do local | Recomendação mantida (08h x 8h; "Faculdade Ufape, Unidade 2" já usado nas mensagens) |

---

## 4. Resultado da conformidade (formato do checklist)

- Arquivo 1 (posts): Aprovado ( ) Bloqueado (x). Itens bloqueados: status do transmitido em P4 linhas 311 e 331 (R-P2); gancho de P5 (R-P1, auditoria 05). Pendências externas declaradas: E5, E6, 68634, autorização de imagem.
- Arquivo 2 (mensagens): Aprovado ( ) Bloqueado (x). Itens bloqueados: desconto sem validade (R-M1), condições do preço [T] (R-M3), consentimento do e-mail do dia (R-M4), status do transmitido em M3 assunto 3 (R-M2). Pendências externas declaradas: E5, E6, 68634, AP8, AP10, A2, A5, opt-in no CRM.
- Revisado por: qa-de-marketing (agente). Revisão humana: [pendente]. Data: 26/10/2026.

Próximo passo: os dois arquivos voltam aos agentes que os produziram (posts-sociais e copy-de-mensagens) para os ajustes acima. Depois, terceira passagem rápida pelo qa-de-marketing só nos itens R-P1 a R-P3 e R-M1 a R-M6; então seguem para a aprovação humana da pessoa do marketing. Nada é publicado ou enviado pela squad.

---

## Fatos (com fonte)

1. Workshop em 20/11/2026 (catálogo, seção 9) e 21/11 (ficha), Faculdade Ufape, Unidade 2, Av. Tiradentes, 960, São Paulo; presencial 16 h, 30 vagas, R$ 1.250,00; transmitido + gravado (só teoria) R$ 450,00, produto 68634; cupom SIMPNEUROMONIT, 20% para aluno e ex-aluno; status aberto. Fonte: contexto/catalogo-de-cursos.md, seção 9.
2. Produto 68634: 24 h, sem data, "R$ 450,00 à vista (Pix ou boleto) ou 1x de R$ 450,00 no cartão", status "verificar"; status "verificar" exige confirmação da Ufape antes de qualquer peça. Fonte: catálogo, seção 4 e "Como usar".
3. Grade, perguntas frequentes, "Certificado UFAPE conforme presença", "apostila e material digital, se previsto", comprovação do vínculo na secretaria. Fonte: ficha do evento.
4. Contatos oficiais: secretaria (segunda a sexta, 9h às 18h), vendas São Paulo, financeiro; voz da marca sem travessão; tabela de aprovação ainda vazia. Fonte: contexto/ufape-geral.md.
5. Regras de peça: sem certificação ligada ao MEC, docentes só com autorização, sem urgência sem número, nada publicado sem aprovação humana. Fonte: docs/execucao-2026-10-26.md.
6. Itens P-C1 a P-C8, C1 a C11 e recomendações. Fonte: saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b.md.
7. Os textos reconferidos e os números de linha citados. Fonte: os dois arquivos revisados, lidos inteiros em 26/10/2026.

## Suposições

1. [SUPOSIÇÃO] Peças bloqueadas por dado externo e declaradas como tal no próprio arquivo não impedem a aprovação do rascunho como um todo depois dos ajustes de texto; impedem só a publicação ou o envio delas.
2. [SUPOSIÇÃO] O e-mail de serviço a inscritos depende do consentimento registrado no checkout, como a própria regra 0.1 item 9 do arquivo de mensagens determina.
3. [SUPOSIÇÃO] O CRM usa a lista de assuntos como está escrita, por isso a marca [T] precisa estar no próprio assunto (R-M2).
4. [SUPOSIÇÃO] Horário comercial do WhatsApp de segunda a sexta, das 9h às 18h, como no QA anterior.

## Dados que faltam

1. [CONFIRMAR NO CATÁLOGO] Verificação do produto 68634 (carga, data, condições) para liberar todo trecho [T].
2. [CONFIRMAR NO CATÁLOGO] Parcelamento e formas de pagamento do presencial (E5).
3. [CONFIRMAR] Validade, limite e prazo de comprovação do cupom; regra para aluno de pós em curso e ex-aluno de curso livre (E6).
4. [PREENCHER COM A REGULAÇÃO] Texto oficial de certificado de eventos; decisão AP8.
5. [CONFIRMAR autorização] Imagem e nome de docentes; termo de imagem no credenciamento.
6. [CONFIRMAR] Opt-in de WhatsApp e e-mail no CRM e consentimento de contato no checkout; exceção de horário de M6 e M7 (A2); templates Meta (A5).
7. [CONFIRMAR] Horário de credenciamento, o que levar, almoço, canal de suporte em 20 e 21/11.
8. [CONFIRMAR] Venda cruzada para a Pós (AP10) e URL da página das pós de anestesiologia.
9. [CONFIRMAR] Destino único para dúvidas de pagamento (secretaria ou vendas), K4.
10. [CONFIRMAR] Quem aprova cada tipo de peça (tabela vazia em contexto/ufape-geral.md).

## Fontes

- contexto/catalogo-de-cursos.md ("Como usar"; seções 4 e 9)
- contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
- contexto/ufape-geral.md; contexto/eventos.md
- docs/execucao-2026-10-26.md; CLAUDE.md
- auditorias/05-social.md; auditorias/07-email-e-whatsapp.md; auditorias/conformidade-educacional.md
- saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-26-b.md
- saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (reconferido, não editado)
- saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md (reconferido, não editado)
