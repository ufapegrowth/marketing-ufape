# QA de marketing: posts sociais e copy de mensagens do Workshop de Neuromonitorização (20 e 21/11/2026)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** eventos (subtipo workshop)
- **Data:** 26/10/2026
- **Peças revisadas (não editadas):**
  - saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (auditoria 05)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md (auditoria 07)
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seção 9; também seção 2, linhas 657, 359 e 68609, e seção 4, linha 68634)
  - contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md (ficha completa)
  - templates/kit-de-lancamento-evento.md, templates/post-social.md, templates/mensagem.md
  - auditorias/05-social.md, auditorias/07-email-e-whatsapp.md, auditorias/conformidade-educacional.md
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-eventos-2026-10-26.md (briefing de campanha e calendário da reta final)
  - saidas/02-estrategia-e-posicionamento/mensagens-eventos-2026-10-26.md (casa de mensagens, seções 0 a 4)
- Não abri faculdade.ufape.com.br. Nenhum dado pessoal foi lido ou citado. Nada foi publicado, enviado ou pago.

## Vereditos

| Arquivo | Veredito | Para onde vai |
|---|---|---|
| posts-sociais-eventos-2026-10-26.md | **CORRIGIR** | Volta ao agente posts-sociais |
| copy-de-mensagens-eventos-2026-10-26.md | **CORRIGIR** | Volta ao agente copy-de-mensagens |

Motivo comum: os dois arquivos têm itens de auditorias/conformidade-educacional.md sem marcação para parte das peças (preço sem condições completas, cupom sem validade, transmitido ligado ao produto 68634 com status "verificar"), e cada um tem erros próprios de texto listados abaixo. Pela regra do QA, falha em qualquer item da conformidade dá veredito corrigir, sem exceção.

---

## 1. Conferência dos dados de curso (os dois arquivos)

| Dado | Fonte | Posts | Mensagens |
|---|---|---|---|
| 20 e 21/11/2026, sexta teórica e sábado prático | Catálogo seção 9 (20/11); ficha (21/11) | Confere | Confere |
| Das 08h às 18h; grade abre às 08h30 | Ficha | Confere (usa 08h e 08h30, divergência declarada) | Confere (usa 8h e 8h30) |
| 16 h, 8 teóricas e 8 práticas, só no presencial | Catálogo seção 9; ficha | Confere; carga do transmitido não citada | Confere; carga do transmitido não citada |
| 30 vagas, por ordem de inscrição, como total | Catálogo seção 9; ficha | Confere; nenhum "restam" | Confere; nenhum "restam" |
| R$ 1.250,00 (presencial) e R$ 450,00 (transmitido) | Catálogo seção 9 | Confere, só em P4 versão B | Confere, nas "linhas de preço" de M1 a M3 e R15 |
| Cupom SIMPNEUROMONIT, 20%, aluno e ex-aluno, vínculo na secretaria | Catálogo seção 9; ficha; briefing de execução, decisão 6 | Confere; nenhum valor calculado | Confere; nenhum valor calculado (M2 cria ordem de passos, ver C3) |
| Faculdade Ufape, Unidade 2, Av. Tiradentes, 960, São Paulo/SP | Catálogo seção 9; ficha | Confere | Confere (grafia "Faculdade UFAPE, Unidade 2", ver R2) |
| Destino https://faculdade.ufape.com.br/neuro-summit/ | Briefing de execução, decisão 6; ficha | Confere em todo post e Story | Confere em M1 a M8; M9 aponta para outra URL [CONFIRMAR URL], justificado |
| Docentes | Ficha | Nenhum nome; só faixas condicionadas à autorização | Nenhum nome nas mensagens; R11 cita a coordenação com [CONFIRMAR autorização] |
| Convidados "a definir" | Ficha | Ausentes | Ausentes |
| Apostila | Ficha ("se previsto") | Não prometida | Não prometida (R12 encaminha) |
| Certificado | Ficha; briefing, regra 5; casa, regra 5 | Ausente em todo post e Story | Só em M8 e R5, com [CONFIRMAR texto aprovado, AP8] (ver C7) |
| Status | Catálogo seção 9: aberto. Seção 4, produto 68634 (transmitido): **verificar** | Linhas do transmitido marcadas [T] (com falhas de marcação, ver P-C1) | Transmitido divulgado sem condição (ver C1) |
| Pós citadas em M9 (657, 68609, 359) | Catálogo seção 2 | Não se aplica | Conferem: nome, praça, modalidade, carga, turma, início e status aberto |

---

## 2. Arquivo 1: posts-sociais-eventos-2026-10-26.md

### 2.1 auditorias/05-social.md, item por item

| Item | Resultado | Observação |
|---|---|---|
| A frequência de publicação segue o plano | [x] Passa, com ressalva | No máximo um post de feed por dia; P1 a P4 nas datas do briefing (30/10, 03/11, 05/11, 09/11). Ressalvas de consistência em P-C5 e P-R3 |
| Todo post tem uma ideia clara | [x] Passa | Uma ideia por post |
| Os ganchos são cumpridos pelo conteúdo | [ ] Falha | P4 versão A: o gancho "Dois dias em São Paulo ou só a teoria de sexta, online" só se cumpre se o cartão [T] sair; sem [T], o gancho promete o que o corpo não traz (P-C2). Demais ganchos conferidos e cumpridos |
| Histórias e números são reais | [x] Passa | Só números da ficha e do catálogo; nenhum depoimento, resultado ou número de participantes |
| Os posts estão formatados para celular | [x] Passa | Gancho na linha 1, linhas curtas, sem emoji, sem caixa alta além do código do cupom |
| As ações de comunidade aconteceram nesta semana | [x] Não se aplica ainda | Caixas de perguntas em 06/11 e 16/11; conferir na semana |
| Métricas são conversas qualificadas e leads, não vaidade | [x] Passa | Seção 6: cliques por UTM, perguntas, inscrições com origem e usos do cupom |
| Toda imagem ou depoimento de aluno e professor tem autorização registrada | [ ] Falha para P11 (foto), P12 (foto), S6, S8 e S9 | Nenhuma autorização registrada. As artes-base não têm pessoas; essas peças só saem com a autorização ou na versão sem pessoa |
| Dados de curso batem com o catálogo | [ ] Falha para as linhas [T] | Todos os dados conferem (seção 1), mas o transmitido é o produto 68634, com status "verificar" no catálogo, e há linhas de transmitido sem a marca [T] (P-C1) |

### 2.2 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | [x] Passa |
| Dados do curso | Status "aberto" (ou sem chamada para inscrição) | [ ] Falha nas linhas do transmitido sem [T]: S1 (enquete), S2 cartão 1, tabela 3.1 linha 1 e gancho de P4 A. Produto 68634 em "verificar" |
| Dados do curso | Modalidade clara e correta | [x] Passa: "apenas teórico" em toda menção ao transmitido |
| Regulação | Graduação: ato do catálogo | [x] Não se aplica |
| Regulação | Pós lato sensu: sem "reconhecida pelo MEC" | [x] Não se aplica; nenhuma menção ao MEC |
| Regulação | Curso livre: não confere diploma | [x] Não se aplica: nenhum post cita certificado ou diploma |
| Regulação | Nota MEC com fonte | [x] Nenhuma nota |
| Promessas e provas | Sem promessa de emprego, salário, aprovação ou sucesso | [x] Passa; nenhuma promessa clínica nos textos publicáveis |
| Promessas e provas | Empregabilidade ou satisfação com fonte | [x] Não se aplica |
| Promessas e provas | Superlativos com fonte | [x] Nenhum |
| Promessas e provas | Comparação com concorrente | [x] Nenhuma |
| Preço e condições | Valor, parcelas e condições completas | [ ] Falha em P4 versão B (preço sem parcelamento nem formas de pagamento; E5) |
| Preço e condições | Desconto com regra, público e prazo de validade | [ ] Falha em P4 (cartão 4), P6 e S3: validade e limite do cupom [CONFIRMAR] (E6) |
| Preço e condições | Urgência real | [x] Passa: só data e capacidade total |
| Preço e condições | Prouni, Fies, financiamento | [x] Não se aplica |
| Pessoas e dados | Autorização de uso de imagem | [ ] Falha para P11 e P12 com foto, S6, S8 e S9 (sem autorização registrada) |
| Pessoas e dados | Menores de idade | [x] Não se aplica |
| Pessoas e dados | Formulários com finalidade e política de privacidade | [x] Não se aplica aos posts (checkout é da página, pendência do site) |
| Pessoas e dados | WhatsApp e e-mail com consentimento | [x] Não se aplica (orgânico) |
| Pessoas e dados | Nenhum dado pessoal | [x] Passa; Stories não citam autor de pergunta |
| Plataformas | Políticas da Meta e do Google | [x] Passa para orgânico; se impulsionar, nova passagem como anúncio |
| Plataformas | Página de destino entrega o que o post promete | [x] Passa: nenhum post promete o que a página não tem. Ressalva: a página ainda mostra "A definir" e o cupom sem código (E1, E12) |
| Anúncios | Característica pessoal, escassez falsa, pessoa pública, caixa alta, drible | [x] Não se aplica (orgânico); textos já compatíveis |
| Texto | Travessão e meia-risca | [x] Nenhum encontrado na leitura completa |

### 2.3 Lista de correções (posts)

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| P-C1 | Seção 3.2, S2 cartão 1 (linha 655); S1 cartão 2, enquete "presencial ou online" (linha 654); tabela 3.1, linha 1 (linha 633); seção 5, linha "S1 a S9: Sim" (linha 717) | O próprio arquivo condiciona todo texto do transmitido à marca [T] (regra 8), mas estes trechos falam do online sem a marca e a seção 5 os libera | Marcar [T] nesses trechos. Sem [T] liberado, S2 cartão 1 diz só "O workshop completo é presencial, sexta e sábado" e a enquete do S1 sai. Atualizar a seção 5 |
| P-C2 | P4, gancho da versão A (linha 300) e capa (linha 333) | Gancho cita "só a teoria de sexta, online" sem [T]; se o cartão 3 for adiado, o gancho não é cumprido | Marcar o gancho com [T] e prever gancho sem transmitido, por exemplo "Workshop presencial: o que a sexta e o sábado incluem" |
| P-C3 | P4 versão B (linhas 313, 319, 323) e gancho alternativo 2 (linha 303) | Preço sem parcelamento nem formas de pagamento (conformidade, preço e condições) | Manter bloqueado até E5. O gancho alternativo 2 também leva preço: marcar "[Versão B]" nele |
| P-C4 | P6 e S3 (linhas 346 a 375 e 656); P4 cartão 4 | Desconto sem prazo de validade (conformidade) | Bloqueado até E6. Quando a Ufape definir, acrescentar uma linha com validade e limite. Até lá P4 versão A sai sem o cartão 4 ou com ele, só depois de E6 |
| P-C5 | P6, "Linha final ou pergunta" (linha 370) | Convida a perguntar sobre comprovação de vínculo nos Stories, mas S3 cartão 5 e a tabela 3.1 mandam essa dúvida para a secretaria | Trocar por "Dúvida sobre como comprovar o vínculo? Fale com a secretaria." |
| P-C6 | S2 cartão 5 (linha 655) | "Dúvida sobre valores e condições? Fale com a secretaria", mas a tabela 3.1 manda parcelamento e pagamento para o time de vendas | Trocar por "Dúvida sobre valores e formas de pagamento? Fale com o time de vendas." ou alinhar a tabela 3.1 |
| P-C7 | Calendário (linha 49 a 75) contra o briefing de campanha, seção 2, semana 3 | O briefing pede um post de FAQ na semana de 09/11 a 13/11; o arquivo trocou por Stories S1 e S2 (06 e 07/11) e não registrou a troca como pedido de aprovação | Ou incluir um carrossel de FAQ na semana 3 (reaproveitando S2, sem certificado e sem preço), ou registrar a troca como pedido de aprovação à pessoa do marketing |
| P-C8 | Lista "Dados que faltam", item 1 (linha 848) | Diz que o parcelamento das duas modalidades falta no catálogo; o catálogo (seção 4, 68634) traz "R$ 450,00 à vista (Pix ou boleto) ou 1x de R$ 450,00 no cartão", ainda com status "verificar" | Reescrever: presencial sem condições no catálogo; transmitido com condições no catálogo, mas produto em "verificar" |

### 2.4 Recomendações (não bloqueiam)

- P-R1. P5 (linha 259): a frase "cães, gatos, equinos e bovinos" é texto literal da página, mas a grade não tem caso de grande animal. Preferir "no centro cirúrgico e na UTI" até a coordenação confirmar.
- P-R2. P2 e P3, "Ponto de vista" (linhas 169 e 218): são afirmações técnicas ("quem entende o sinal lê melhor o índice"; "instalar mal compromete o índice"). Se forem para a legenda, passam pela coordenação científica (AP6).
- P-R3. P7 sai em 13/11 e o briefing põe "falta 1 semana" entre 14 e 16/11. A data de 13/11 é a correta para o texto (7 dias). Pedir ao estrategia-de-campanha que ajuste o calendário dele.

### 2.5 Peças sem defeito próprio

Depois das correções acima e da aprovação humana, ficam sem defeito próprio: P1 (sem [T]), P2, P3, P5 (sem [T]), P7 (sem [T]), P8 (sem [T]), P10, P12 (só depois do evento, versão sem foto), S4, S5 e S6 sem docente. Continuam bloqueadas por dado externo: P4 versão B, P6, S3, P9, P11 e P12 com foto, P13, S7, S8 e S9 com pessoas.

### 2.6 Veredito do arquivo 1

**CORRIGIR.** Volta ao posts-sociais com P-C1 a P-C8.

---

## 3. Arquivo 2: copy-de-mensagens-eventos-2026-10-26.md

### 3.1 auditorias/07-email-e-whatsapp.md, item por item

| Item | Resultado | Observação |
|---|---|---|
| Consentimento e descadastro funcionando | [ ] Pendente externo | Texto de saída presente: "Responda SAIR" e botão nas mensagens de marketing; link de descadastro em todo e-mail; rodapé fixo nos templates de serviço. Opt-in registrado no CRM e no checkout [CONFIRMAR] (E15). Recomendação C-R3 |
| Cada mensagem tem um objetivo | [x] Passa | Objetivo único por mensagem no mapa |
| Assuntos e primeiras linhas honestos | [ ] Falha | M3 WhatsApp, linhas 2 e 5 (data errada) e M1, linha 4 e assunto 4 (não cumpridos pelo corpo). Ver C4 e C5 |
| Segmentos recebem mensagens da etapa | [x] Passa | Base geral, alunos e ex-alunos, quem abriu e não comprou, inscritos por modalidade, participantes |
| Réguas têm regras de saída | [x] Passa | Seção 1, regras de saída |
| Resultados registrados para cada envio | [ ] Pendente externo | Plano de registro escrito; execução depende do CRM e de P15 |
| Cliques, respostas e conversões medidos | [ ] Pendente externo | UTM por peça definida; inscrição por origem depende do site e do CRM |
| WhatsApp só em horário comercial, frequência humana, template Meta | [ ] Falha | M6 (20/11, 8h, feriado nacional) e M7 (21/11, sábado, 8h) fora do horário comercial; estão marcadas para aprovação, mas sem alternativa que cumpra o kit (C2). Seção 0.4 tem a regra escrita ao contrário (C8). Templates ainda não aprovados pela Meta (A5) |

### 3.2 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | [x] Passa (seção 1). M9 confere com o catálogo, seção 2 |
| Dados do curso | Status "aberto" (ou sem chamada para inscrição) | [ ] Falha: M1 versão B, M1 a M3 (linha do transmitido), M2, R1, R7 e R15 chamam para o ingresso transmitido, produto 68634 com status "verificar" no catálogo, sem a condição que os posts usam (C1) |
| Dados do curso | Modalidade clara e correta | [x] Passa: "apenas teórico" em toda menção ao transmitido |
| Regulação | Graduação: ato do catálogo | [x] Não se aplica |
| Regulação | Pós lato sensu: sem "reconhecida pelo MEC" | [x] Passa: M9 não cita MEC nem validade |
| Regulação | Curso livre: não confere diploma | [ ] Falha em R5: diz "certificado de participação" e "atividade de 16 h" (texto que não está na página e que erra para o transmitido). Texto oficial de certificado [PREENCHER COM A REGULAÇÃO] (C7) |
| Regulação | Nota MEC com fonte | [x] Nenhuma nota |
| Promessas e provas | Sem promessa de emprego, salário, aprovação ou sucesso | [x] Passa; M9 sem promessa; R16 não afirma eficácia |
| Promessas e provas | Empregabilidade ou satisfação com fonte | [x] Não se aplica |
| Promessas e provas | Superlativos com fonte | [x] Nenhum |
| Promessas e provas | Comparação com concorrente | [x] Nenhuma |
| Preço e condições | Valor, parcelas e condições completas | [ ] Falha nas "linhas de preço" de M1, M2, M3 e em R15: presencial sem parcelamento (E5) |
| Preço e condições | Desconto com regra, público e prazo de validade | [ ] Falha em M2, M3 (aluno), R8: validade [CONFIRMAR] (E6). Além disso, M2 e-mail inventa a ordem dos passos (C3) |
| Preço e condições | Urgência real | [x] Passa: nenhum "últimas vagas", "corra" ou contador |
| Preço e condições | Prouni, Fies, financiamento | [x] Não se aplica |
| Pessoas e dados | Autorização de uso de imagem e nome | [x] Passa: nenhum nome nas mensagens; R11 só com [CONFIRMAR autorização] |
| Pessoas e dados | Menores de idade | [x] Não se aplica |
| Pessoas e dados | Formulários com finalidade e política de privacidade | [ ] Pendente externo: checkout [CONFIRMAR no site] |
| Pessoas e dados | WhatsApp e e-mail só com consentimento e saída fácil | [ ] Falha parcial: M6 e M7 só têm WhatsApp; inscrito sem opt-in de WhatsApp fica sem mensagem do dia, contra o briefing ("sem opt-in, só e-mail") (C2). Opt-in registrado [CONFIRMAR] |
| Pessoas e dados | Nenhum dado pessoal | [x] Passa: só campos do CRM entre colchetes |
| Plataformas | Políticas Meta e Google | [x] Passa (mensagens de CRM; templates a aprovar) |
| Plataformas | Página de destino entrega o que a mensagem promete | [x] Passa, com ressalva: a página não mostra o passo a passo do cupom que M2 descreve (E12) |
| Anúncios | Itens de anúncio | [x] Não se aplica |
| Texto | Travessão e meia-risca | [x] Nenhum encontrado na leitura completa |

### 3.3 Lista de correções (mensagens)

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| C1 | M1 versão B (linhas 171 a 181 e 234 a 249), linhas do transmitido em M1 A, M2 e M3, R1, R7 (linha 817) e R15 | O transmitido é o produto 68634, status "verificar" no catálogo; os posts condicionam esse conteúdo à marca [T] e as mensagens não. R7 cita as condições de pagamento de um produto em "verificar" | Adotar a mesma condição dos posts: marcar [T] em todo trecho do transmitido e não enviar M1 versão B nem a linha do transmitido até a Ufape confirmar o 68634. Em R7, trocar as condições por [CONFIRMAR NO CATÁLOGO] até a verificação |
| C2 | M6 (linhas 614 a 641) e M7 (linhas 645 a 665) | Só WhatsApp, às 8h, em feriado (20/11) e sábado (21/11). Se a exceção não for aprovada, nenhuma mensagem do dia é enviada e o kit mínimo ("Mensagem do dia", 1) deixa de ser cumprido. Inscrito sem opt-in de WhatsApp não recebe nada, contra o briefing | Criar versão por e-mail de M6 e M7 (envio às 7h do dia, sem restrição de horário de WhatsApp), que vale como mensagem do dia em qualquer cenário. O WhatsApp das 8h segue como exceção a aprovar. Em M6, registrar que 20/11 é feriado nacional, não só "antes das 9h" |
| C3 | M2 e-mail, "Como usar a condição" (linhas 330 a 332), follow-up "em 2 passos" (linhas 347 e 348) | Numera a ordem (cupom na compra, depois comprovação) enquanto o mesmo texto diz "Ordem e prazo da comprovação: [CONFIRMAR]". Os posts, a casa e o briefing proíbem criar ordem de passos | Tirar a numeração e o "em 2 passos": "Para usar a condição, informe o cupom SIMPNEUROMONIT e comprove o vínculo com a secretaria." Assunto do follow-up: "Como usar o cupom SIMPNEUROMONIT no workshop de 20 e 21/11" |
| C4 | M3 WhatsApp, primeiras linhas 2 e 5 (linhas 412 e 415); escolhidas para teste (linha 417) | Envio em 16/11 (segunda). Linha 2 diz "Falta uma semana" e linha 5 diz "Semana que vem": em 16/11 faltam 4 dias e o evento é nesta semana | Linha 2: "Oi, [primeiro_nome]. É nesta sexta, 20/11: o workshop de neuromonitorização." Linha 5: "Nesta semana: sexta teórica, sábado prático, na Unidade 2." |
| C5 | M1 WhatsApp, linha 4 (linha 151, escolhida para teste); M1 e-mail, assunto 4 (linha 201, escolhido para teste) | Ganchos não cumpridos pelo corpo. A linha 4 promete "uma aula só sobre o que está validado" ligada ao BIS; a aula da grade é sobre eletrodos de agulha, e o corpo da versão A não cita essa aula. O assunto 4 promete "Dos planos de Guedel ao awareness intraoperatório" e o corpo do e-mail A não cita essa aula | Linha 4: "Se o BIS já está na sua rotina, o workshop de 20 e 21/11 tem uma aula sobre evidências e limitações dos índices BIS, PSI e qNOX", e citar essa aula no corpo. E-mail A: abrir o parágrafo de sexta com "Dos planos de Guedel ao awareness intraoperatório" |
| C6 | M8 e-mail, primeiro parágrafo (linha 686) | Na versão do transmitido o texto fica "Foram dois dias de aulas teóricas na sexta-feira", frase incoerente | Versão transmitido: "Obrigado por acompanhar as aulas teóricas de sexta-feira, 20/11, do Workshop..." |
| C7 | R5 (linha 815) | "Certificado de participação" e "atividade de 16 h" não estão na página; para o comprador do transmitido, "16 h" é errado. Briefing (regra 5) e casa (regra 5) divergem sobre responder certificado a quem ainda não se inscreveu | Usar só o texto da página: "Sim, conforme presença, emitido pela UFAPE." Pergunta sobre MEC: "Não é um curso de pós-graduação. Vou confirmar o texto oficial e te respondo." Manter [CONFIRMAR texto aprovado, AP8] e levar a divergência briefing x casa à pessoa do marketing |
| C8 | Seção 0.4 (linha 92) | "Em dia útil e em feriado nacional, o CRM não envia mensagem de marketing": a regra está escrita ao contrário | "Fora de dia útil (sábado, domingo e feriado nacional), o CRM não envia mensagem de marketing por WhatsApp." |
| C9 | M1 versão A WhatsApp, segundo parágrafo (linha 163); M7 corpo (linha 655); M6 presencial (linha 624) | Blocos de 60 a 75 palavras num só balão: ruim de ler no celular, contra o próprio limite de "até 3 balões curtos" | Quebrar em balões de até 3 linhas: sexta; sábado; local, horário e vagas. Em M7, separar a programação dos horários de intervalo |
| C10 | M1 follow-ups (linhas 184, 190, 252 e 256) | "3 dias úteis depois" com data 04/11: com o feriado de 02/11, 04/11 é o segundo dia útil. "3 dias depois" com data 03/11: são 4 dias | Ajustar o texto à data ("2 dias úteis depois, 04/11"; "no primeiro dia útil depois do feriado, 03/11") |
| C11 | Kit de evento, variação simpósio adotada no briefing (seção 3, "E-mail de programação", 30/10) | Não há e-mail de programação na régua. O follow-up de M1 (03/11) só leva link e vai só a quem não abriu. O mínimo do kit nunca diminui | Criar o e-mail de programação: grade por dia com horários e temas, sem convidados "a definir", sem nome de docente sem autorização, sem certificado, envio na semana 2 (03 a 05/11) para a base com opt-in, com descadastro |

### 3.4 Recomendações (não bloqueiam)

- C-R1. M9 aponta para as Pós de Anestesiologia; o briefing (fase 5) previa ponte para as provas de bolsa de 27/11. O pedido A4 deve dizer explicitamente que a venda cruzada é para a Pós, para a AP10 cobrir o caso.
- C-R2. O briefing (fase 4) prevê agradecimento em 21/11, fim do dia; a régua agradece só em M8 (23/11). Registrar a troca como pedido de aprovação ou criar um agradecimento curto por e-mail em 21/11.
- C-R3. Escrever o rodapé de saída por extenso nos textos de M4 a M8 por WhatsApp, e não só como "rodapé do template", para o CRM não perder a frase.
- C-R4. M1 e M2 mandam e-mail às 9h e WhatsApp às 10h ou 10h30 do mesmo dia ao mesmo contato. Para frequência humana, afastar os dois canais em pelo menos um dia.
- C-R5. "Obrigada" (M4, M8, M9) e "Obrigado" (posts P12): unificar a voz da marca.

### 3.5 Mensagens sem defeito próprio

Depois das correções e da aprovação humana, ficam sem defeito próprio: M1 versão A (sem linha de preço e sem a linha do transmitido até C1), M3 e-mail geral (sem linha de preço), M4 e M5 (com os [CONFIRMAR] preenchidos), R2, R3, R4, R6, R9 a R14 e R16. Continuam bloqueadas por dado externo: toda linha de preço (E5), M2 e M3 aluno (E6), M8 (AP8 e gravação), M9 (AP10 e URL), M6 e M7 por WhatsApp (exceção de horário).

### 3.6 Veredito do arquivo 2

**CORRIGIR.** Volta ao copy-de-mensagens com C1 a C11.

---

## 4. Consistência entre as peças e com briefing, casa de mensagens e calendário

| # | Tema | Posts | Mensagens | Briefing e casa | Situação |
|---|---|---|---|---|---|
| K1 | Transmitido (68634 em "verificar") | Condicionado a [T], com falhas de marcação | Sem condição | Briefing e casa divulgam o transmitido sem condição; catálogo diz "verificar" | **Inconsistente.** Corrigir por P-C1 e C1 e pedir à pessoa do marketing uma regra única até a Ufape confirmar o 68634 |
| K2 | Certificado | Nenhum | Só a inscritos, participantes e a quem pergunta, com AP8 | Briefing: só a inscritos depois de aprovado. Casa: também a quem pergunta | Divergência de origem (briefing x casa). Decisão AP8; corrigir a redação de R5 (C7) |
| K3 | Cupom | Regra da página, sem prazo nem ordem | M2 cria ordem de passos | Ordem e prazo [CONFIRMAR] | **Inconsistente.** C3 |
| K4 | Dúvida sobre pagamento | S2 manda para a secretaria; tabela 3.1 manda para vendas | Vendas (R7) e financeiro para cobrança | Briefing: vendas e secretaria | Corrigir P-C6 |
| K5 | Calendário | P1 30/10, P2 03/11, P3 05/11, P4 09/11, P7 13/11, P9 19/11 | M1 e M2 30/10, M3 14 e 16/11, M5 19/11, M6 e M7 20 e 21/11, M8 23/11, M9 25/11 | Briefing: convite 30/10; e-mail de programação na semana 2; FAQ na semana 3; lembrete 14 a 16/11; agradecimento 21/11 | Falta e-mail de programação (C11) e post de FAQ na semana 3 (P-C7); agradecimento deslocado (C-R2); P7 em 13/11 (P-R3) |
| K6 | Kit mínimo de evento | 4 posts cumpridos (P1 a P4) | Convite, véspera, lembrete cumpridos; mensagem do dia condicional; e-mail de programação ausente | Briefing adota a soma das variações workshop e simpósio | Corrigir C2 e C11 |
| K7 | Horário | 08h e 08h30 | 8h e 8h30 | Ficha: 08h | Mesma informação; padronizar o formato (recomendação) |
| K8 | Grafia do local | "Faculdade Ufape, Unidade 2" (como na página) | "Faculdade UFAPE, Unidade 2" | Página: "Faculdade Ufape, Unidade 2"; marca de realização: "Faculdade UFAPE" | Padronizar o local como na página (recomendação) |
| K9 | Docentes, convidados, apostila, escassez, valor com cupom, nome do evento, destino | Conformes | Conformes | Conformes | Sem divergência |

---

## 5. Resultado da conformidade (formato do checklist)

- Arquivo 1 (posts): Aprovado ( ) Bloqueado (x). Itens bloqueados: status do transmitido sem [T] (P-C1, P-C2), preço sem condições (P-C3), cupom sem validade (P-C4), autorização de imagem (P11, P12 com foto, S6, S8, S9).
- Arquivo 2 (mensagens): Aprovado ( ) Bloqueado (x). Itens bloqueados: status do transmitido (C1), texto de certificado (C7), preço sem condições (linhas de preço), cupom sem validade e com ordem inventada (C3), consentimento e canal da mensagem do dia (C2).
- Revisado por: qa-de-marketing (agente). Revisão humana: [pendente]. Data: 26/10/2026.

Próximo passo: os dois arquivos voltam aos agentes que os produziram (posts-sociais e copy-de-mensagens). Depois das correções, nova passagem pelo qa-de-marketing; só então seguem para a aprovação humana da pessoa do marketing. Nada é publicado ou enviado pela squad.

---

## Fatos (com fonte)

1. Evento em 20 e 21/11/2026, Faculdade Ufape, Unidade 2, Av. Tiradentes, 960, São Paulo/SP; presencial com 16 h e 30 vagas por R$ 1.250,00; transmitido e gravado (só teoria) por R$ 450,00 (produto 68634); cupom SIMPNEUROMONIT com 20% para aluno e ex-aluno; status aberto. Fonte: contexto/catalogo-de-cursos.md, seção 9.
2. Produto 68634: 24 h, sem data, "R$ 450,00 à vista (Pix ou boleto) ou 1x de R$ 450,00 no cartão", status "verificar". Fonte: catálogo, seção 4. Regra do status "verificar": a Ufape confirma antes de qualquer peça. Fonte: catálogo, "Como usar".
3. 21/11, das 08h às 18h, grade com abertura às 08h30, intervalos e almoço, docentes confirmados, convidados "a definir", "apostila e material digital, se previsto", "Certificado UFAPE conforme presença", vínculo comprovado na secretaria. Fonte: ficha do evento.
4. Pós 657 (São Paulo, semipresencial, 360 h, turma II, 13/03/2027), 68609 (Goiânia, semipresencial, 500 h, turma VIII, 24/04/2027) e 359 (São Paulo, semipresencial, 360 h, turma I, 22/05/2027), todas abertas. Fonte: catálogo, seção 2.
5. Decisões da Ufape de 26/10/2026: só docentes confirmados, cupom para aluno e ex-aluno, 16 h, destino neuro-summit. Fonte: docs/execucao-2026-10-26.md, decisão 6.
6. Kit de evento: variação workshop (3 posts, convite, véspera, dia, e-mail de convite) e simpósio (4 posts, e-mails de convite, lembrete e programação, véspera, dia); o mínimo nunca diminui; o briefing adota a soma. Fonte: templates/kit-de-lancamento-evento.md; briefing de campanha, seção 3.
7. Calendário da reta final, regras 5 e 7 e pendências E1 a E15. Fonte: saidas/06-geracao-de-demanda/estrategia-de-campanha-eventos-2026-10-26.md.
8. Regra de certificado da casa (só a quem pergunta) e frases obrigatórias por modalidade. Fonte: saidas/02-estrategia-e-posicionamento/mensagens-eventos-2026-10-26.md, seções 0 e 2.2.
9. Contatos oficiais e horário da secretaria (segunda a sexta, 9h às 18h). Fonte: contexto/ufape-geral.md.
10. 26/10/2026 é segunda-feira; os dias da semana das datas citadas foram conferidos a partir dela.

## Suposições

1. [SUPOSIÇÃO] O e-mail não está sujeito à janela de horário comercial da auditoria 07 (que fala de WhatsApp); por isso a proposta de e-mail do dia às 7h em C2.
2. [SUPOSIÇÃO] O checkout do ingresso transmitido passa pelo produto 68634; por isso o status "verificar" alcança as peças que chamam para esse ingresso.
3. [SUPOSIÇÃO] "Ponto de vista" e "Linha final" do template de post podem ir para a legenda; por isso a recomendação P-R2.
4. [SUPOSIÇÃO] Horário comercial do WhatsApp de segunda a sexta, das 9h às 18h, como proposto pelo copy-de-mensagens (mesma janela da secretaria).

## Dados que faltam

1. [CONFIRMAR NO CATÁLOGO] Verificação do produto 68634 (carga horária, data, condições) e liberação do transmitido nas peças.
2. [CONFIRMAR NO CATÁLOGO] Parcelamento e formas de pagamento do presencial (E5).
3. [CONFIRMAR] Validade, limite e prazo de comprovação do cupom; regra para aluno de pós em curso e ex-aluno de curso livre (E6).
4. [CONFIRMAR] Fim das inscrições por ingresso; vagas restantes com data.
5. [PREENCHER COM A REGULAÇÃO] Texto oficial de certificado de eventos; decisão AP8 sobre responder certificado a quem ainda não se inscreveu.
6. [CONFIRMAR autorização] Imagem e nome de cada docente; termo de imagem de participantes no credenciamento.
7. [CONFIRMAR] Opt-in de WhatsApp e e-mail no CRM e no checkout (E15); aprovação da exceção de horário de M6 e M7; templates aprovados pela Meta.
8. [CONFIRMAR] Horário de credenciamento, o que levar, almoço, canal de suporte em 20 e 21/11 (feriado e sábado).
9. [CONFIRMAR] Venda cruzada no pós-evento (AP10) e URL da página das Pós de Anestesiologia.
10. [CONFIRMAR] Quem aprova cada tipo de peça (tabela de aprovação vazia em contexto/ufape-geral.md).

## Fontes

- contexto/catalogo-de-cursos.md (seções 2, 4 e 9; "Como usar")
- contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
- contexto/ufape-geral.md; contexto/eventos.md
- docs/execucao-2026-10-26.md
- templates/kit-de-lancamento-evento.md; templates/post-social.md; templates/mensagem.md
- auditorias/05-social.md; auditorias/07-email-e-whatsapp.md; auditorias/conformidade-educacional.md
- saidas/06-geracao-de-demanda/estrategia-de-campanha-eventos-2026-10-26.md
- saidas/02-estrategia-e-posicionamento/mensagens-eventos-2026-10-26.md
- saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (revisado, não editado)
- saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md (revisado, não editado)
