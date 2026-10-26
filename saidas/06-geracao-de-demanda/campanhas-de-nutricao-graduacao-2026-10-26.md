# Régua de nutrição da Graduação 2027/1: WhatsApp e e-mail (G1 e G2)

- Agente: campanhas-de-nutricao
- Linha: graduacao
- Data: 26/10/2026 (segunda-feira)
- Versão: 3, corrigida após qa-de-marketing-graduacao-2026-10-26-d (N-1 e A-N4) e ajustada ao teto D16 e às regras E1 a E4 da seção 13 do plano do cmo. Versão 2: corrigida após qa-de-marketing-graduacao-2026-10-26-c (correções N1 a N16) e ajustada às decisões D1, D2, D11 e D12 da seção 12
- Workflow: /campanha-de-vestibular, etapa 7 de 8 (régua do lead até a redação e da aprovação até a matrícula; o copy-de-mensagens lapida os textos em 09/11)
- Liberações cobertas:
  - G1: Edital nº 002/2026 (Vestibular 2027) + Graduação em Medicina Veterinária, São Paulo, integral e noturno
  - G2: Edital nº 004/2026 (Processo Seletivo 2027.1 Goiânia) + Graduação em Pedagogia, Goiânia, noturno
- Status: rascunho para aprovação humana. São textos para o CRM enviar só a quem deu consentimento. A squad não dispara nada. Nada é publicado, enviado ou pago a partir deste arquivo.
- Entradas lidas:
  - docs/execucao-2026-10-26.md (decisões 1 a 14)
  - CLAUDE.md
  - .claude/agents/campanhas-de-nutricao.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (seção 1, Graduação, e regras de uso)
  - contexto/cursos/graduacao/editais-2027-1.md (fonte de todo dado do edital, inclusive descontos e suas regras)
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md (matriz do 1º semestre, para o nome exato das disciplinas)
  - templates/mensagem.md e templates/kit-de-lancamento-graduacao.md
  - .claude/skills/mapear-regua/SKILL.md
  - .claude/skills/assuntos-de-email/SKILL.md
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md (entrada principal)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md (oferta corrigida, seções 0.1 a 0.3)
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (bloqueios G1 a G16 e kit mínimo)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12: D1, D2, D4, D11 e D12; seção 13: D16, E1 a E4 e regra de serviço)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md (seção 0.1 a 0.3: kit mínimo como toques de calendário KW1 a KW5 e KE1 a KE3)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-d.md (N-1 e A-N4)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-c.md (veredito CORRIGIR, correções N1 a N16)
  - auditorias/07-email-e-whatsapp.md, auditorias/06-geracao-de-demanda.md e auditorias/conformidade-educacional.md
- Regra de fonte: preço, modalidade, turno, duração, carga horária e ato vêm do catálogo (seção 1). Datas, vagas, formas de ingresso, matrícula, cancelamento e regras do desconto vêm da ficha dos editais 2027/1. Matriz curricular vem das fichas do curso (conferida pelo qa-c); a fonte fica na nota de cada mensagem, nunca no texto que vai ao candidato. Não abri faculdade.ufape.com.br. Nenhum número de inscritos, redações, matrículas, vagas restantes, verba ou meta existe hoje.
- Nota de nome: o plano do cmo previa este arquivo com data de 06/11/2026; foi entregue em 26/10/2026, com o nome pedido pelo orquestrador.

---

## Mudanças desta versão (v3)

| Origem | O que mudou | Onde |
|---|---|---|
| N-1 do qa-d | Primeira linha B sem "pode entrar com" e com o Enem completo: "A inscrição é gratuita: redação online ou nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)." | G1-L2 e G2-L2 |
| A-N4 do qa-d | A tabela do kit mínimo saiu da seção 1. O kit é do copy-de-mensagens (toques de calendário KW1 a KW5 e KE1 a KE3, seção 0.1 do arquivo dele); esta régua é por evento do contato e só aponta a correspondência. Uma só contagem para o kit | Seção 1; 0.5, item 3; Próximo passo |
| D16 do cmo (seção 13.3) | Teto da Graduação: até 3 mensagens de campanha por semana somando WhatsApp e e-mail, no máximo 2 por canal, no máximo 1 WhatsApp a cada 3 dias úteis, 1 por dia; contato que está também na base da Pós fica com o teto menor (o da Graduação). Conferido que nenhuma semana de régua passa de 3 | 0.4 (FW), 0.7 |
| E1 a E4 do cmo | Engajamento no WhatsApp (E1), erro 131049 (E2), descadastro em até 48 h e em um clique (E3), opt-in de campanha separado do de serviço (E4) | 0.4 (FE e FW), 0.7, seção 5 |
| Regra de serviço da seção 13.3 | Classificação confirmada pelo cmo: R1, A1, M1, M5 e as versões -R são serviço; M2 e M4 só com o pedido R1 e JR3 aprovado; AT, L, R2 a R5, A2 a A6 e M3 são campanha. Limites do serviço escritos | 0.7; marcação de canal de M5 e M5-R |

## Mudanças da versão 2

| # do qa-c | O que mudou | Onde |
|---|---|---|
| N1 | Desconto sempre com os seis elementos (valor cheio, valor com desconto, percentual, validade do 1º semestre de 2027, renovação semestral com comprovação, perda no mês pago depois do vencimento) e o nome do programa. Criadas as linhas curtas LD-MV, LD-INT, LD-NOT e LD-PED para WhatsApp. A1 e M1 deixaram de citar o desconto; A2 e A4-R passaram a trazer a linha completa (o kit mínimo pede o desconto com regra no WhatsApp do aprovado); AT1-R deixou de citar o desconto | 0.3; G1-L4, L4-R, L6, L7, A1, A2, A4-R, A6, M1, M4; G2-L4, L6, L7, A1, A2, A6, M1 e as versões -R |
| N2 | Toda mensagem com preço tem a linha "Bloqueio: BLOQUEADO para envio até G12 e G7". Respostas de preço da seção 4 bloqueadas para uso até G12 e G7. Marcas internas saíram do corpo e foram para a nota da mensagem | 0.1 regra 12; mensagens com preço; 4.1, 4.2, 4.3 |
| N3 | Pedagogia sem "dia 10" e sem reajuste de dezembro: BP-PED e BD-PED corrigidos; G2-L3, G2-L6, G2-A3, G2-M1 ajustados; G2-M4 BLOQUEADO até a Ufape confirmar o vencimento | 0.3; G2 |
| N4 | Saiu a promessa de "regras de renovação por escrito". Vale o texto da oferta 0.3: "Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação." | BD-MV, BD-PED, G1-L6, G2-L6, 4.1 |
| N5 | "Responsável legal" e "aceite do responsável" viraram "representante legal" em todas as ocorrências. "Responsável" ficou só no nome da versão -R | todo o arquivo |
| N6 | Versões -R escritas por extenso: 13 por liberação (kit mínimo e as citadas). Regra nova: mensagem sem versão -R não vai a contato menor de idade nem ao representante legal dele. Follow-up do AT2-R corrigido (não existe AT3-R) | 0.5; G1; G2-V |
| N7 | G2: toda mensagem com {link_lp_utm} BLOQUEADA para envio com link da LP até G6; até lá, a chamada vira resposta à mensagem. G1: mensagens com link da LP que citam o noturno ou vão ao segmento noturno seguem a mesma regra até G8 | 0.1 regra 13; G1-L1, L3, L4, L5-alt, L7; G2-L1 a L5, L7, L2-R |
| N8 | "Matrícula a partir de 2 dias depois do resultado" em todas as ocorrências | 0.1, BX, AT2, L1, L7, G2 equivalentes, 4.1 |
| N9 | Enem com a condição completa em pré-visualizações, primeiras linhas e ganchos | AT1, R1, L1, AT2, L2 e equivalentes do G2 |
| N10 | Nome da disciplina como na ficha: "Campos de Atuação do Médico Veterinário e Práticas Hospitalares", além de "Projeto Extensionista I" e "Práticas Hospitalares". "(ficha do curso)" e "[CONFIRMAR NO CATÁLOGO]" saíram do corpo | G1-L5-alt, G1-M3, G2-L5, G2-L6, G2-M3 |
| N11 | Gancho do AT3: "Três respostas do edital sobre a redação." | G1-AT3 |
| N12 | Rodapé próprio para os e-mails do G2 | 0.4 (FE) |
| N13 | Ato com a data de publicação no D.O.U. | G1-L4, G2-L4 e versões -R |
| N14 | Resposta corrigida: "Você pode fazer a inscrição presencialmente..." | 4.2 |
| N15 e D11/D12 | UTM por mensagem no padrão do cmo: utm_source email ou whatsapp, utm_medium crm, utm_campaign grad_<curso>_<AAAAMM>, utm_content com o código da mensagem | 0.2; 6 |
| N16 | Gancho do A6: "Para começar em 22/02/2027, faltam estes passos." | G1-A6, G2-A6 |
| D1 e D2 | Teto único do cmo avaliado e aplicado à Graduação (seção 0.7), com a lista do que é serviço e do que é campanha (substituído na v3 pelo D16) | 0.4 (FW), 0.7 |
| Outros ajustes | Gancho do A2 sem "dá para fazer pelo celular" (promessa não verificada); kit mínimo definido por mensagem (substituído na v3 pelo apontamento ao copy-de-mensagens); referência a "seção G1-F e G2-F" (inexistente) trocada por "seção 4"; nota sobre a matriz do 1º semestre atualizada | G1-A2; seção 1; G1-A.1; seção 7 |

---

## 0. Regras, variáveis e blocos que valem para toda a régua

### 0.1 Regras duras (a cada mensagem, o qa confere)

1. Toda mensagem tem valor por si só (explica uma etapa, responde uma dúvida ou mostra uma regra) e uma única chamada para ação.
2. Desconto sempre com os seis elementos: valor cheio, valor com desconto, percentual, validade (só o 1º semestre de 2027), renovação a cada semestre com comprovação e perda no mês em que a mensalidade for paga depois do vencimento, mais o nome do programa. E-mail usa o bloco BP; WhatsApp usa a linha LD. Mensagem que não comporta a linha não cita o desconto.
3. Edital do desconto citado pelo nome do programa: "Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026)" para São Paulo e "Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026)" para Goiânia. Nenhuma mensagem reproduz o preâmbulo, a data de assinatura ou o item 3.5 desses editais (erros de texto, pedido G7 do cmo).
4. Ato como no catálogo, com a data de publicação no D.O.U., sem antecipar reconhecimento. Nenhuma nota do MEC. Nenhuma frase de certificação. Nenhuma promessa de emprego, salário, aprovação ou concurso. A redação é eliminatória: nunca "fácil" nem "aprovação certa".
5. Sem urgência sem número real: não há data-limite de inscrição, nem número de vagas restantes. Fatos permitidos: aulas em 22/02/2027, matrícula a partir de 2 dias depois do resultado, cancelamento com 80% até 2 dias antes das aulas.
6. Prouni, Fies e financiamento não aparecem.
7. Candidato menor de idade exige aceite do representante legal na inscrição e na matrícula (Edital 002/2026 e Edital 004/2026). Seção 0.5 trata de quem recebe cada mensagem.
8. Pedagogia: nenhuma carga horária, nenhum docente, nenhum trecho de modelo da página, nenhum bloco do egresso, nenhuma lista de professores, nenhum endereço de Goiânia, nenhum dia de vencimento e nenhum reajuste até a Ufape confirmar (pedidos G5, G6 e G9; vencimento e reajuste do Edital 004/2026).
9. Medicina Veterinária: hospital veterinário (Ufape Clínica) só depois da confirmação de uso pela graduação (pedido G11). Nenhuma mensagem obrigatória depende disso.
10. Nenhum dado pessoal neste arquivo. Todo dado do candidato entra por variável do CRM, entre chaves.
11. Nada de caixa alta para gritar, pontuação repetida ou emoji. Nunca travessão nem meia-risca. Nenhuma marca interna ([CONFIRMAR], [SUPOSIÇÃO], "(ficha do curso)") dentro do texto que vai ao candidato: elas ficam na nota da mensagem.
12. Toda mensagem com preço ou desconto leva "Bloqueio: BLOQUEADO para envio até G12 e G7" (reajuste de dezembro e erros dos Editais 003/2026). G2-M4 tem também o bloqueio do vencimento.
13. Destino: o link de campanha é sempre a LP da Graduação com UTM ({link_lp_utm}); nenhuma mensagem aponta para outra página do site. Mensagem do G2 com {link_lp_utm}: BLOQUEADA para envio com link da LP até G6. Mensagem do G1 com {link_lp_utm} que cita o noturno ou vai ao segmento noturno: BLOQUEADA para envio com link da LP até G8. Até lá, a chamada vira resposta à mensagem (texto da "Chamada até o desbloqueio" em cada uma). Os links de sistema (área do candidato, resultado, matrícula, PDF dos editais) são etapas do processo seletivo, não página de campanha.

### 0.2 Variáveis do CRM e UTM (preenchidas pelo CRM, nunca neste arquivo)

| Variável | O que é |
|---|---|
| {primeiro_nome} | Primeiro nome de quem recebe |
| {nome_candidato} | Nome do candidato, usado nas versões para o representante legal (-R) |
| {curso} | Medicina Veterinária (G1) ou Pedagogia (G2) |
| {link_lp_utm} | LP da Graduação do curso, com a UTM da mensagem (tabela abaixo) [CONFIRMAR qual URL recebe a UTM, pedido G13] |
| {link_area_candidato} | Área do candidato, onde faz a redação, envia a nota do Enem e vê o resultado [CONFIRMAR nome e URL] |
| {link_passo_a_passo} | Página ou PDF de passo a passo da redação e do Enem [CONFIRMAR se existe; se não, remover a linha] |
| {link_resultado} | Página de resultado no site [CONFIRMAR URL] |
| {link_matricula} | Plataforma de matrícula digital [CONFIRMAR URL] |
| {link_edital_vestibular} | PDF do edital de ingresso (uploads/arquivo/edital-vestibular-2027.pdf ou edital-processo-seletivo-2027-1-goiania.pdf) |
| {link_edital_desconto} | PDF do edital de desconto (uploads/arquivo/edital-descontos-2027.pdf ou edital-de-desconto-mensalidade-2027-1-goiania.pdf) |
| {link_politica} | Política de privacidade [CONFIRMAR URL, pedido G13] |
| {data_resultado} e {data_matricula} | Data de publicação do resultado e primeiro dia de matrícula (2 dias depois), do sistema de inscrição |
| {data_vencimento} | Só G2: dia do vencimento da mensalidade da Pedagogia [CONFIRMAR com a Ufape no Edital 004/2026]; enquanto vazio, G2-M4 não sai |
| {contato_captacao} | G1: Vendas São Paulo, WhatsApp (11) 91366-9290. G2: Vendas Goiânia, WhatsApp (62) 9420-1847 (contatos de contexto/ufape-geral.md; o site informou instabilidade no WhatsApp interno em 22/10/2026: [CONFIRMAR o canal de resposta ativo]) |

**UTM por mensagem (decisões D11 e D12 do cmo, seção 12.7 do cmo-geral):**

| Parâmetro | Valor |
|---|---|
| utm_source | email ou whatsapp (canal da mensagem) |
| utm_medium | crm |
| utm_campaign | chave da Graduação + mês do primeiro envio da régua: grad_medvet-integral_202611, grad_medvet-noturno_202611, grad_pedagogia_<AAAAMM> (AAAAMM do primeiro envio com link da LP, depois de G6). Lead do G1 sem turno escolhido: grad_medvet_202611 [SUPOSIÇÃO de chave; o cmo confirma] |
| utm_content | código da mensagem, em minúsculas, com hífen dentro do bloco: g1-l1, g1-l3, g1-l2-r, g2-l5 |

Exemplo (formato, URL base a confirmar em G13): {url_lp_medvet}?utm_source=whatsapp&utm_medium=crm&utm_campaign=grad_medvet-integral_202611&utm_content=g1-l2. Tudo em minúsculas, sem acento e sem dado pessoal. A plataforma gera a URL final; o CRM monta {link_lp_utm} por mensagem.

Valores por turma do G1 (catálogo e Edital 003/2026; total do semestre com desconto é conta sobre esses números):

| Variável | Integral | Noturno |
|---|---|---|
| {turno} | integral | noturno |
| {duracao} | 4 anos | 5 anos |
| {mensalidade_cheia} | R$ 10.000,00 (semestre: R$ 60.000,00 em 6 parcelas) | R$ 10.000,00 (semestre: R$ 60.000,00 em 6 parcelas) |
| {mensalidade_desc} | R$ 5.000,00 | R$ 4.000,00 |
| {percentual} | 50% | 60% |
| {total_semestre_desc} | R$ 30.000,00 | R$ 24.000,00 |
| {estagio} | 7º e 8º semestres | 9º e 10º semestres |
| {bloco_preco} | BP-INT | BP-NOT |
| {linha_desconto} | LD-INT | LD-NOT |

G2: {bloco_preco} = BP-PED; {linha_desconto} = LD-PED.

### 0.3 Blocos oficiais reutilizados (texto único; a mensagem os cola)

**BP-INT (preço, integral, e-mail):**
"Medicina Veterinária integral em São Paulo: de R$ 10.000,00 por R$ 5.000,00 por mês (50% de desconto) nas 6 mensalidades do 1º semestre de 2027. O valor cheio é de R$ 10.000,00 por mês (R$ 60.000,00 no semestre). O desconto vale para todas as formas de ingresso, é aplicado a partir da confirmação da matrícula e vale só para o 1º semestre de 2027. Para continuar nos semestres seguintes, o aluno pede a renovação a cada semestre, com comprovação, nas regras do Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026). O desconto é perdido no mês em que a mensalidade for paga depois do vencimento (dia 10) e não vale junto com programas governamentais com regras próprias."

**BP-NOT (preço, noturno, e-mail):** igual ao BP-INT, trocando o início por "Medicina Veterinária noturno em São Paulo: de R$ 10.000,00 por R$ 4.000,00 por mês (60% de desconto)".

**BP-PED (preço, Pedagogia, e-mail):**
"Pedagogia noturno em Goiânia: de R$ 1.050,00 por R$ 525,00 por mês (50% de desconto) nas 6 mensalidades do 1º semestre de 2027. O valor cheio é de R$ 1.050,00 por mês (R$ 6.300,00 no semestre). O desconto vale para todas as formas de ingresso, é aplicado a partir da confirmação da matrícula e vale só para o 1º semestre de 2027. Para continuar nos semestres seguintes, o aluno pede a renovação a cada semestre, com comprovação, nas regras do Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026). O desconto é perdido no mês em que a mensalidade for paga depois do vencimento e não vale junto com programas governamentais com regras próprias."

**Linhas curtas do desconto (WhatsApp e e-mail curto):**
- **LD-MV (os dois turnos):** "De R$ 10.000,00 por R$ 5.000,00 por mês no integral (50%) ou R$ 4.000,00 no noturno (60%), só no 1º semestre de 2027. Renovação a cada semestre, com comprovação. O desconto é perdido no mês pago depois do vencimento. Regras no Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026)."
- **LD-INT:** "Integral: de R$ 10.000,00 por R$ 5.000,00 por mês (50%), só no 1º semestre de 2027. Renovação a cada semestre, com comprovação. O desconto é perdido no mês pago depois do vencimento. Regras no Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026)."
- **LD-NOT:** "Noturno: de R$ 10.000,00 por R$ 4.000,00 por mês (60%), só no 1º semestre de 2027. Renovação a cada semestre, com comprovação. O desconto é perdido no mês pago depois do vencimento. Regras no Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026)."
- **LD-PED:** "De R$ 1.050,00 por R$ 525,00 por mês (50%), só no 1º semestre de 2027. Renovação a cada semestre, com comprovação. O desconto é perdido no mês pago depois do vencimento. Regras no Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026)."

**BD-MV (e depois do 1º semestre, Medicina Veterinária):**
"O desconto do edital vale para as 6 mensalidades do 1º semestre de 2027. Para continuar com desconto, você pede a renovação a cada semestre, com comprovação, nas regras do edital. A renovação não é automática e o valor dos semestres seguintes depende dessa análise. A mensalidade cheia hoje é de R$ 10.000,00, e o edital prevê reajuste em dezembro de cada ano. Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação."

**BD-PED (e depois do 1º semestre, Pedagogia):**
"O desconto do edital vale para as 6 mensalidades do 1º semestre de 2027. Para continuar com desconto, você pede a renovação a cada semestre, com comprovação, nas regras do edital. A renovação não é automática e o valor dos semestres seguintes depende dessa análise. A mensalidade cheia hoje é de R$ 1.050,00. Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação."

Nota dos blocos (não vai ao candidato): texto da oferta 0.2 e 0.3. [CONFIRMAR o que é a "comprovação" (proposta P1, não aprovada) e o efeito do reajuste de dezembro sobre 2027/1 (G12).] Vencimento e reajuste da Pedagogia: [CONFIRMAR com a Ufape no Edital 004/2026]; por isso BP-PED e BD-PED não trazem dia nem reajuste.

**BM (menor de idade):** "Se o candidato for menor de idade, a inscrição e a matrícula precisam do aceite do representante legal."

**BC (como fazer a avaliação):**
"Você tem dois caminhos, e a inscrição é gratuita.
1. Redação online. Não há dia marcado: você faz quando puder, depois da inscrição. A redação é eliminatória, com nota mínima 5,0.
2. Nota do Enem. Vale a média aritmética de 300 pontos ou mais, de qualquer edição a partir de 2010.
Passo a passo da redação: (1) entre na área do candidato, {link_area_candidato}; (2) abra a prova de redação; (3) faça a redação online; (4) aguarde o resultado, publicado no site.
Passo a passo do Enem: (1) tenha a nota de uma edição de 2010 em diante; (2) envie a nota pela área do candidato; (3) aguarde o resultado, publicado no site."
Nota do BC: [CONFIRMAR tempo de prova, tema, se é possível salvar, se há nova tentativa, prazo de divulgação do resultado, onde e como a nota do Enem é enviada e como a média é calculada.]

**BX (o que vem depois):**
"O resultado é publicado no site. A matrícula é eletrônica e abre a partir de 2 dias depois da publicação. Ela se confirma com o pagamento da 1ª mensalidade e a assinatura digital do contrato. Os documentos são enviados pela plataforma de matrícula digital em até 30 dias. As aulas começam em 22/02/2027."

**BA (ato, G1):** "Medicina Veterinária, bacharelado presencial em São Paulo, com ato autorizativo na Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). A Faculdade UFAPE de São Paulo é credenciada pela Portaria MEC nº 176, de 27/02/2025 (D.O.U. 28/02/2025)."
**BA (ato, G2):** "Pedagogia, licenciatura presencial em Goiânia, com ato autorizativo na Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). A Faculdade UFAPE de Goiânia é credenciada pela Portaria MEC nº 871, de 10/11/2022."

### 0.4 Campos fixos (valem para toda mensagem do tipo, para não repetir)

**FE (campos fixos de e-mail):**
- Opt-in: consentimento de e-mail registrado no CRM, com data e origem. Sem registro, o CRM não envia.
- Template Meta: não se aplica.
- Forma de sair: link de descadastro em um clique no rodapé de todo e-mail de campanha, que vale para todas as linhas no mesmo dia e, no máximo, em 48 h (regra E3 do cmo).
- Opt-in por categoria (E4): o consentimento de e-mail de campanha é separado do de serviço. R1, A1, M1, M5 e as versões -R saem com o opt-in de serviço ou com o dado da inscrição; o resto exige o opt-in de campanha.
- Rodapé do G1: "Você recebe este e-mail porque se cadastrou no Vestibular 2027 da Faculdade UFAPE e aceitou receber contatos. Para parar de receber, use o link de descadastro. Política de privacidade: {link_politica}. UFAPE - CURSOS ESPECIALIZADOS LTDA, CNPJ 27.409.162/0001-34, Av. 9 de Julho, 3939, Jardim Paulista, São Paulo, SP."
- Rodapé do G2: "Você recebe este e-mail porque se cadastrou no Processo Seletivo 2027.1 da Faculdade UFAPE em Goiânia e aceitou receber contatos. Para parar de receber, use o link de descadastro. Política de privacidade: {link_politica}. UFAPE - CURSOS ESPECIALIZADOS LTDA, CNPJ 27.409.162/0001-34, Av. 9 de Julho, 3939, Jardim Paulista, São Paulo, SP."
- Razão social, CNPJ e sede de contexto/ufape-geral.md (a sede é a mesma para as duas liberações).
- Assinatura: "Equipe de captação da Faculdade UFAPE" e {contato_captacao}.

**FW (campos fixos de WhatsApp):**
- Opt-in de WhatsApp confirmado: sim, exigido antes de cada envio. O CRM só envia se o campo de opt-in de WhatsApp estiver "sim", com data e origem. Sem registro, a mensagem não sai.
- Mensagem iniciada pela Ufape: sempre por template aprovado pela Meta (nome na mensagem). Resposta do time dentro da janela de 24 horas do contato pode ser texto livre. As variáveis entre chaves viram {{1}}, {{2}} e assim por diante, na ordem em que aparecem; a pessoa que submeter o template informa um exemplo fictício por variável. Categoria (utilidade ou marketing): [CONFIRMAR com a Meta e o responsável pelo CRM]. Nenhum template foi submetido: pendente de aprovação humana e da Meta.
- Forma de sair: última linha de toda mensagem, "Para não receber mais mensagens, responda SAIR."
- Horário: segunda a sexta, das 9h às 18h, nunca em fim de semana nem feriado.
- Frequência: teto D16 do cmo para a Graduação (seção 0.7): no máximo 2 WhatsApp de campanha por semana, no máximo 1 a cada 3 dias úteis, dentro de até 3 mensagens de campanha por semana somando os canais e 1 por dia.
- Engajamento (E1): contato que não respondeu, não clicou e não abriu conversa nas últimas 4 mensagens de campanha por WhatsApp recebe no máximo 1 WhatsApp de campanha por semana, até interagir; sem nenhuma interação em 90 dias, sai do WhatsApp de campanha e fica só no e-mail (se tiver opt-in) [SUPOSIÇÃO de critério do cmo].
- Erro 131049 (E2): mensagem barrada pelo limite da Meta não é reenviada por WhatsApp antes de 24 h e conta como suprimida (não muda de dia).
- SAIR (E3): vale para todas as linhas no mesmo dia, no máximo em 48 h. Opt-in de WhatsApp de campanha separado do de serviço (E4).
- Assinatura: "Faculdade UFAPE".

### 0.5 Consentimento e menores de idade (quem recebe cada mensagem)

1. Adulto (18 anos ou mais): recebe a versão normal, no canal em que deu consentimento.
2. Candidato menor de idade: a mensagem vai ao representante legal cadastrado, com a versão "para o responsável" (marcada "-R"), e só se o consentimento do representante legal estiver registrado. Mensagem direta ao menor fica suspensa até o jurídico e o responsável pelo CRM validarem o tratamento de consentimento de menor (pedido G10, [CONFIRMAR]). Até lá, o CRM não envia WhatsApp nem e-mail de marketing a contato identificado como menor.
3. **Mensagem sem versão -R não vai a contato menor de idade nem ao representante legal dele.** As versões -R existentes (13 por liberação): AT1-R, AT2-R, L2-R, L4-R, R1-R, R2-R, A1-R, A3-R, A4-R, A6-R, M1-R, M2-R e M5-R. Elas cobrem as mensagens da régua que tratam dos mesmos assuntos do kit mínimo; as -R dos toques do kit (KW1 a KW5, KE1 a KE3) são do copy-de-mensagens.
4. O CRM precisa ter o campo "menor de idade: sim ou não" e "representante legal: contato e consentimento" [CONFIRMAR se existe]. Se não existir, a régua do G1 só dispara para quem o time marcar como adulto ou representante legal, e o resto espera.
5. Versões -R falam com o adulto, sem pressão de compra dirigida ao menor, sem urgência e sem imagem ou nome além da variável {nome_candidato}. Nenhuma frase se dirige ao menor.
6. Anúncio pago continua só para 18 anos ou mais (plano do cmo). Esta régua não muda isso.
7. G2 (público adulto de Goiânia): a regra do aceite entra no BM, sem ser o argumento central; as versões -R existem para o caso de candidato menor.

### 0.6 Etiquetas e dados necessários no CRM e no atendimento

- Etapa do funil: lead, inscrito, avaliado (redação feita ou Enem enviado), aprovado, matriculado, ativo em 22/02/2027, encerrado.
- Liberação e turno: G1-integral, G1-noturno, G1-sem-turno (lead), G2.
- Consentimento: e-mail (sim ou não, data, origem), WhatsApp (sim ou não, data, origem), saída solicitada (canal e data).
- Menor de idade (sim ou não) e contato do representante legal com consentimento.
- Origem (UTM) e data da inscrição, data do resultado, data da matrícula.
- Etiqueta "falar com a captação", "sem engajamento" e "aguardando G10".
- Cada envio registra: mensagem (código), canal, data e hora, entregue, aberto ou lido, clique, resposta, saída.
- Atendimento e CRM: ferramentas [CONFIRMAR] (contexto/ufape-geral.md deixa o campo em branco).

### 0.7 Teto D16, regras E1 a E4 e fila D2 do cmo: aplicação na Graduação

**Histórico.** Na versão 2, esta seção avaliou o D1 (seção 12.2 do cmo) e registrou que ele valia para a Graduação. A seção 13.3 do cmo substituiu o número do D1 pelo D16 e criou um teto próprio da Graduação, porque a base tem vestibulandos, responsáveis e possíveis menores (LGPD art. 14 e ECA). O resto do D1 (janelas e dias sem campanha) e a fila D2 seguem valendo.

**Teto D16 da Graduação (decisão do cmo; número [SUPOSIÇÃO] a calibrar com os alertas da seção 13.4):**

| Regra | Valor na Graduação |
|---|---|
| WhatsApp de campanha | até 2 por semana (segunda a domingo) e no máximo 1 a cada 3 dias úteis; até 1 por semana para contato sem engajamento (E1) |
| E-mail de campanha | até 2 por semana |
| Soma dos canais | **até 3 mensagens de campanha por semana** |
| Por dia | no máximo 1 mensagem de campanha por contato, em qualquer canal |
| Contato que está nas duas bases (por exemplo, profissional da base de Pós que é representante legal de candidato) | soma tudo o que recebe de todas as linhas; vale o teto menor, o da Graduação (até 3 por semana, 1 por dia) |
| Candidato menor de idade | nenhuma mensagem de campanha direta ao menor (0.5, mantido até G10) |
| Janela | WhatsApp em dia útil, das 9h às 18h; e-mail em qualquer dia, das 7h às 19h |
| Dias sem campanha | 02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço. Toque de campanha que cair nesses dias passa para o próximo dia permitido, na mesma ordem, sem envio extra [SUPOSIÇÃO de desenho; o cmo confirma, porque o D2 diz que o suprimido não acumula] |

**Conferência: nenhuma semana da régua passa de 3 mensagens de campanha** (serviço fora da conta; semana de segunda a domingo):

| Régua | Toques de campanha e dias | Pior semana | Por canal |
|---|---|---|---|
| AT | AT1 (ter 03/11), AT2 (qua 04/11), AT3 (ter 10/11) | 2 (03 e 04/11) | 1 e-mail e 1 WhatsApp |
| L | L1 D0, L2 D2, L3 D5, L4 D8, L5 D12, L6 D15, L7 D20 | 3 (L1, L2 e L3, ou L2, L3 e L4 quando D2 cai na segunda): quatro toques nunca cabem em 7 dias | no máximo 2 e-mails (L1 e L3) e 1 WhatsApp; L2, L4 e L6 ficam a 3 dias úteis ou mais um do outro |
| R | R1 D0 (serviço), R2 D2, R3 D5, R4 D9, R5 D14 | 2 (R2 e R3, ou R3 e R4) | R2 e R4 a 7 dias um do outro |
| A | A1 D0 (serviço), A2 D+2, A3 D+3, A5 D+7, A6 D+14 | 3 (A2, A3 e A5 quando D+2 cai na segunda) | 2 WhatsApp (A2 e A5, a 5 dias) e 1 e-mail |
| M | M1 D0 (serviço), M2 D+5 (campanha até o pedido R1 e JR3), M3 D+14, M4 (campanha até o mesmo pedido), M5 15/02/2027 (serviço) | 2 (M3 e M4, se o vencimento cair na mesma semana do M3) | M2 e M4 a 3 dias úteis ou mais |
| Versões -R | seguem os dias da versão adulta (A4-R no lugar do A2) | iguais às da régua | iguais |

Passagem de uma régua para outra (lead que se inscreve, inscrito aprovado) e toques do kit do copy-de-mensagens podem somar mais de 3 na mesma semana. Nesse caso, o CRM aplica o teto por contato: o toque que passaria de 3 (ou de 2 no canal, ou de 1 no dia) segue a fila D2 e muda para o próximo dia permitido; o kit já não sai para quem tem toque da régua 5 dias úteis antes ou depois (copy-de-mensagens, 0.3, item 2).

**Regras que entram junto (E1 a E4, seção 13.3 do cmo):**
- E1. Engajamento no WhatsApp: sem resposta, clique ou conversa nas últimas 4 mensagens de campanha por WhatsApp, o contato recebe no máximo 1 WhatsApp de campanha por semana, até interagir; sem interação em 90 dias, sai do WhatsApp de campanha e fica no e-mail, se tiver opt-in [SUPOSIÇÃO de critério do cmo]. Na régua L, isso faz o L4 ou o L6 mudar de semana para quem não respondeu ao L2.
- E2. Erro 131049: não há reenvio por WhatsApp antes de 24 h; a mensagem conta como suprimida. O CRM registra o erro por envio.
- E3. Descadastro: SAIR e descadastro valem para todas as linhas no mesmo dia, no máximo em 48 h; todo e-mail de campanha leva descadastro em um clique.
- E4. Opt-in por categoria: o opt-in de campanha é separado do de serviço, por canal.
- Sem API oficial do WhatsApp Business, E1 e E2 não se aplicam como regra automática (pedido U11a do cmo) [CONFIRMAR].

**Serviço (fora do teto), como a seção 13.3 do cmo classifica:**
- Serviço: R1 (confirmação de inscrição), A1 (resultado), M1 (confirmação de matrícula), M5 (semana de início, como a véspera) e as versões -R delas (R1-R, A1-R, M1-R, M5-R).
- Serviço só se a Ufape aprovar o J3 e o J4 da Pós no mesmo pedido (R1 e JR3 da seção 12): M2 (documentos), M4 (vencimento) e M2-R. Até lá, contam como campanha.
- Campanha: AT, L, R2 a R5, A2 a A6, M3 e as versões -R delas.
- Limites do serviço: só com opt-in de serviço ou dado da inscrição (E4); sem oferta de outro curso no texto (se tiver, conta como campanha); WhatsApp na janela de dia útil, das 9h às 18h; no máximo 1 serviço por dia por canal para o mesmo pedido [SUPOSIÇÃO do cmo]. Serviço não conta no teto, mas entra nos indicadores de qualidade do número (seção 13.4 do cmo).

**Fila D2:** contato que está na Graduação e em outra linha segue a fila do cmo: serviço primeiro; depois o toque principal com data mais próxima; follow-ups depois. Na Graduação, os toques principais são AT1, L1, R2, A2 e A6; os demais contam como follow-up. O CRM aplica a fila e o teto por contato (pedido do cmo ao arquiteto-de-fluxos).

---

## 1. Mapa da jornada do lead ao candidato pronto para se matricular

| Etapa | O que conta | Gatilho de entrada | Régua | Objetivo final da etapa | Próximo passo do candidato |
|---|---|---|---|---|---|
| 0. Lead | Cadastro na LP com UTM, sem inscrição concluída [CONFIRMAR se o formulário da LP já é a inscrição] | Cadastro | L1 a L7 (lead novo) | Concluir a inscrição gratuita | Inscrever-se |
| 1. Inscrito | Inscrição concluída, sem redação nem Enem | Inscrição | AT (base existente) e R1 a R5 (inscritos novos) | Redação feita ou nota do Enem enviada | Avaliação |
| 2. Avaliado | Redação feita ou Enem enviado, resultado pendente | Redação ou Enem registrados | Sem mensagem de venda. Só o aviso de serviço do sistema [CONFIRMAR] | Aguardar resultado | Resultado no site |
| 3. Aprovado | Resultado publicado como aprovado | Resultado no site | A1 a A6 | 1ª mensalidade paga e contrato assinado | Matrícula |
| 4. Matriculado | Matrícula confirmada | Pagamento mais assinatura | M1 a M5 | Documentos enviados e matrícula mantida até as aulas | 22/02/2027 |
| 5. Ativo | Aulas iniciadas | 22/02/2027 | Fim da régua; jornada do aluno (jornada-do-aluno) | Permanecer | Rematrícula |

Se o formulário da LP já é a inscrição, o lead novo entra direto em R1 e a régua L fica só para quem deixou contato sem se inscrever (por exemplo, quem veio de anúncio e pediu informação) [CONFIRMAR, pedido G13].

Visão geral das réguas (cada uma com 5 a 7 contatos; 51 mensagens para adulto, 25 por liberação mais a G1-L5 condicionada, e 26 versões -R, 13 por liberação):

| Régua | G1 (Medicina Veterinária) | G2 (Pedagogia) | Contatos |
|---|---|---|---|
| Ativação da base | G1-AT1 e-mail, AT2 WhatsApp, AT3 WhatsApp | G2-AT1, AT2, AT3 | 3 |
| Lead novo | G1-L1 e-mail, L2 WhatsApp, L3 e-mail, L4 WhatsApp, L5 e-mail, L6 WhatsApp, L7 e-mail | G2-L1 a L7 (mesmos canais) | 7 |
| Inscrito até a redação | G1-R1 e-mail, R2 WhatsApp, R3 e-mail, R4 WhatsApp, R5 e-mail | G2-R1 a R5 | 5 |
| Aprovado até a matrícula | G1-A1 e-mail, A2 WhatsApp, A3 e-mail, A5 WhatsApp, A6 e-mail (A4-R é a versão do A2 para o representante legal) | G2-A1 a A6 | 5 |
| Matriculado até 22/02/2027 | G1-M1 e-mail, M2 WhatsApp, M3 e-mail, M4 WhatsApp, M5 e-mail | G2-M1 a M5 | 5 |

**Kit mínimo (5 WhatsApp e 3 e-mails por liberação, cmo-graduacao): uma só contagem.** O kit é do copy-de-mensagens e está em saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md, seção 0.1: oito toques de calendário (KE1, KW1, KW2, KE2, KW3, KW4, KE3, KW5), com data fixa, que só saem para quem não está com régua ativa. Esta régua é disparada por evento do contato e não conta como kit. A correspondência de assuntos (qual mensagem da régua cobre o mesmo tema de cada item do kit) está na tabela da seção 0.1 do copy-de-mensagens; este arquivo não repete a tabela, para não haver duas contagens. Leitura a confirmar pelo cmo (A-N4 do qa-d).

---

# PARTE G1: Medicina Veterinária (São Paulo, integral e noturno)

## G1-A. Ativação da base: inscritos que ainda não fizeram a redação

Objetivo único: levar quem já se inscreveu a fazer a redação online ou a enviar a nota do Enem.

### G1-A.1 Segmento e passo a passo para o time

1. Segmento no CRM: inscrito no G1 desde 17/08/2026, sem redação realizada e sem nota do Enem registrada, não matriculado, sem pedido de saída, com consentimento de e-mail e, para WhatsApp, com opt-in registrado. Dois recortes: integral e noturno [CONFIRMAR se o CRM guarda o turno escolhido e o status "redação feita"].
2. Excluir: menores sem consentimento do representante legal validado (pedido G10) e qualquer contato com a etiqueta "falar com a captação" aberta.
3. Escolher a versão: adulto (texto normal) ou representante legal (versão "-R").
4. Ordem: AT1 (e-mail), AT2 (WhatsApp, 1 dia útil depois), AT3 (WhatsApp, 4 dias úteis depois do AT2, só para quem não respondeu e segue sem redação). Quem faz a redação ou responde sai da sequência na hora.
5. Datas sugeridas, se o texto for aprovado até 30/10: AT1 em 03/11/2026 (terça; 02/11 é dia sem campanha pelo D1), AT2 em 04/11, AT3 em 10/11. Horário sugerido: 10h30 ou 14h30, para testar [SUPOSIÇÃO]. A data real depende da aprovação humana e do segmento no CRM [CONFIRMAR].
6. Quem responder vai ao time de captação com a etiqueta "falar com a captação". O time usa as respostas da seção 4.
7. Depois do AT3, quem segue sem redação e sem resposta entra na régua R no contato R3 (não repete o que já recebeu).
8. Medir por mensagem: entregue, aberto ou lido, clique, resposta, redação feita em até 7 dias, saída. Resultado por turno, nunca somado.

### G1-A.2 O prazo que vale (texto de apoio para o time e para as mensagens)

- Não há data de prova: a redação é online e pode ser feita a qualquer momento depois da inscrição (Edital 002/2026).
- Não há data final de inscrição no edital. [CONFIRMAR com a Ufape se existe data-limite interna de inscrição e de matrícula, pedido G4.] Até a resposta, nenhuma mensagem fala em prazo de inscrição.
- O que limita de verdade: as aulas começam em 22/02/2027 e a matrícula só abre a partir de 2 dias depois do resultado. O cancelamento com devolução de 80% só vale se pedido até 2 dias antes do início das aulas (20/02/2027).
- Conselho dado ao candidato, sem pressão: fazer a redação com folga, porque o resultado e a matrícula também levam alguns dias [CONFIRMAR o prazo de divulgação do resultado].
- Meta interna (não vai para o candidato): redações e Enem cumpridos até 31/01/2027 [SUPOSIÇÃO de desenho do briefing].
- As vagas existem (45 no integral e 45 no noturno, Edital 002/2026), mas não há número de vagas restantes: nenhuma mensagem fala em vagas acabando.

### G1-AT1 (e-mail): sua inscrição está feita, falta a avaliação

- Canal: e-mail
- Linha e curso: Graduação, Medicina Veterinária, São Paulo, {turno}
- Objetivo: fazer o inscrito abrir a área do candidato e fazer a redação ou enviar o Enem
- Segmento: inscrito sem redação (etapa 1), adulto
- Assunto A: {primeiro_nome}, sua inscrição está feita: o próximo passo é a redação ou o Enem
- Assunto B: Redação online, sem dia marcado: veja como fazer
- Texto de pré-visualização: Faça quando puder, ou use sua nota do Enem (média mínima de 300 pontos, edições de 2010 em diante).
- Gancho: Você já fez o mais difícil de começar: a inscrição.
- Corpo:
  "Olá, {primeiro_nome}.
  Você se inscreveu no Vestibular 2027 de Medicina Veterinária {turno} da Faculdade UFAPE. Para seguir no processo, falta a avaliação.
  {BC}
  O que vem depois: {BX}
  Se tiver qualquer dúvida, responda este e-mail ou fale com o time de captação em {contato_captacao}. {BM}"
- Chamada para ação: "Acessar minha inscrição" ({link_area_candidato})
- Follow-up para quem não abriu ou não respondeu: AT2 (WhatsApp, 1 dia útil depois); reenvio do AT1 com o assunto B só se não houver opt-in de WhatsApp.
- Data e horário: ver G1-A.1, item 5.
- Opt-in e saída: FE.

### G1-AT1-R (e-mail, versão para o representante legal)

- Assunto A: Vestibular 2027 de {nome_candidato}: o próximo passo é a redação ou o Enem
- Assunto B: Para o representante legal: como {nome_candidato} faz a redação online
- Texto de pré-visualização: Sem dia marcado. O aceite do representante legal também é necessário na matrícula.
- Gancho: Você consta como representante legal de {nome_candidato}, que já se inscreveu.
- Corpo:
  "Olá.
  {nome_candidato} se inscreveu no Vestibular 2027 de Medicina Veterinária {turno} da Faculdade UFAPE. A inscrição é gratuita e, como o candidato é menor de idade, ela exigiu o aceite do representante legal. Esse aceite também é necessário na matrícula.
  Para seguir, {nome_candidato} precisa fazer a avaliação:
  {BC}
  O que vem depois: {BX}
  Antes de qualquer pagamento, o time explica o valor e todas as condições. Dúvidas: responda este e-mail ou fale com o time de captação em {contato_captacao}."
- Chamada para ação: "Ver o passo a passo" ({link_area_candidato})
- Follow-up: AT2-R.
- Opt-in e saída: FE, com consentimento do representante legal registrado (seção 0.5).

### G1-AT2 (WhatsApp): redação online, sem dia marcado

- Canal: WhatsApp automático (template grad_mv_ativacao_redacao_v1; variáveis: {primeiro_nome}, {turno}, {link_area_candidato})
- Objetivo: levar o inscrito à área do candidato
- Segmento: inscrito sem redação, adulto, sem resposta ao AT1 ou sem abertura
- Primeira linha A: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE. Sua redação do Vestibular pode ser feita online, sem dia marcado.
- Primeira linha B: Oi, {primeiro_nome}. Já fez o Enem? Com média mínima de 300 pontos (edições de 2010 em diante), sua nota pode ser a sua entrada na Medicina Veterinária da Ufape.
- Gancho: Duas formas de entrar, as duas sem custo de inscrição.
- Corpo:
  "Resumo para a sua inscrição de Medicina Veterinária {turno}:
  1) Redação online: sem dia marcado, você faz quando puder. É eliminatória, com nota mínima 5,0.
  2) Nota do Enem: média de 300 pontos ou mais, de qualquer edição a partir de 2010.
  Depois, o resultado sai no site e a matrícula abre a partir de 2 dias depois. As aulas começam em 22/02/2027.
  Se quiser falar com uma pessoa do time, é só responder esta mensagem.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: AT3 (4 dias úteis depois).
- Data e horário: ver G1-A.1, item 5 (horário comercial).
- Opt-in e saída: FW.

### G1-AT2-R (WhatsApp, versão para o representante legal)

- Template: grad_mv_ativacao_redacao_resp_v1 (variáveis: {nome_candidato}, {turno}, {link_area_candidato})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE. Sobre o Vestibular 2027 de {nome_candidato}: falta a redação ou o Enem.
- Primeira linha B: Olá. Você é o representante legal de {nome_candidato}? Temos um aviso sobre a inscrição.
- Corpo:
  "{nome_candidato} se inscreveu em Medicina Veterinária {turno}. Para seguir, falta a redação online (sem dia marcado, eliminatória, nota mínima 5,0) ou a nota do Enem (média de 300 pontos ou mais, edições de 2010 em diante). Como o candidato é menor de idade, o aceite do representante legal também é necessário na matrícula. Dúvidas? Responda esta mensagem e o time de captação fala com você.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver o passo a passo: {link_area_candidato}"
- Follow-up: nenhum WhatsApp automático (não existe AT3-R). Quem responde vai ao time de captação. O AT1-R não se repete.
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-AT3 (WhatsApp): três perguntas sobre a redação

- Canal: WhatsApp automático (template grad_mv_ativacao_perguntas_v1; variáveis: {primeiro_nome}, {link_area_candidato})
- Objetivo: tirar a dúvida que impede a redação e levar à área do candidato
- Segmento: inscrito sem redação e sem resposta ao AT2
- Primeira linha A: Oi, {primeiro_nome}. Três respostas rápidas sobre a redação do Vestibular da Ufape.
- Primeira linha B: Oi, {primeiro_nome}. Ficou alguma dúvida sobre a redação ou sobre o Enem?
- Gancho: Três respostas do edital sobre a redação.
- Corpo:
  "Dá para fazer de casa? A redação é online. Precisa esperar uma data? Não: é feita a qualquer momento depois da inscrição. Já fiz o Enem, vale? Vale a média de 300 pontos ou mais, de qualquer edição a partir de 2010.
  Se a sua dúvida for outra, responda aqui que o time de captação te ajuda.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: nenhum WhatsApp novo. Sem resposta, o inscrito entra na régua R no R3.
- Opt-in e saída: FW.

---

## G1-B. Régua do lead novo (até a inscrição)

Objetivo único da régua: concluir a inscrição gratuita. Gatilho: cadastro na LP. Tempo entre toques em dias corridos, ajustados ao horário comercial e ao D1: D0, D2, D5, D8, D12, D15, D20. Saída: seção 5.

Bloqueio do noturno (regra 13, pedido G8): L1, L3, L4 e L7 citam o noturno e L5-alt cita o estágio do noturno para esse segmento. Até G8, essas mensagens saem sem o link da LP, com a "Chamada até o desbloqueio" escrita em cada uma.

### G1-L1 (e-mail, D0): boas-vindas e como funciona o ingresso

- Canal: e-mail
- Linha e curso: Graduação, Medicina Veterinária, São Paulo
- Objetivo: mostrar o caminho inteiro e levar à inscrição gratuita
- Segmento: lead novo, adulto
- Assunto A: Boas-vindas ao Vestibular 2027 de Medicina Veterinária da Faculdade UFAPE
- Assunto B: Como entrar em Medicina Veterinária na Ufape: 4 passos e inscrição gratuita
- Texto de pré-visualização: Redação online sem dia marcado ou nota do Enem com média mínima de 300 pontos. Aulas a partir de 22/02/2027.
- Gancho: O caminho do cadastro até a matrícula, em 4 passos.
- Corpo:
  "Olá, {primeiro_nome}. Boas-vindas.
  Você pediu informações sobre Medicina Veterinária na Faculdade UFAPE. Veja como funciona:
  1) Inscrição gratuita, pelo site ou presencial, de segunda a sexta, das 9h às 18h, na Av. Nove de Julho, 3913 e 3939, Jardim Paulista, São Paulo.
  2) Avaliação: redação online sem dia marcado (eliminatória, nota mínima 5,0) ou nota do Enem (média de 300 pontos ou mais, edições de 2010 em diante).
  3) Resultado no site.
  4) Matrícula eletrônica, a partir de 2 dias depois do resultado, com a 1ª mensalidade e a assinatura digital do contrato. Documentos em até 30 dias.
  O curso: {BA} Integral, em 4 anos, ou noturno, em 5 anos. Carga horária de 4.195 h, mais 75 h de atividades complementares. As aulas começam em 22/02/2027.
  {BM}
  Dúvidas? Responda este e-mail ou fale com o time em {contato_captacao}."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio com link da LP até G8 (cita o noturno).
- Chamada até o desbloqueio: "Quer se inscrever? Responda este e-mail e o time de captação te ajuda."
- Follow-up: L2 (WhatsApp, D2). Se não houver opt-in de WhatsApp, L3 sobe para D3.
- Data e horário: imediato após o cadastro; depois, das 7h às 19h (D1).
- Opt-in e saída: FE.

### G1-L2 (WhatsApp, D2): Enem desde 2010 ou redação

- Canal: WhatsApp automático (template grad_mv_lead_enem_v1; variáveis: {primeiro_nome}, {link_lp_utm})
- Objetivo: mostrar as duas portas de entrada e levar à inscrição
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Já fez o Enem? Com média mínima de 300 pontos (edições de 2010 em diante), sua nota pode ser a sua entrada na Medicina Veterinária da Ufape.
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE. A inscrição é gratuita: redação online ou nota do Enem (média mínima de 300 pontos, edições de 2010 em diante).
- Gancho: Quem fez o Enem anos atrás também pode usar a nota, de qualquer edição a partir de 2010, com média mínima de 300 pontos.
- Corpo:
  "Para Medicina Veterinária, a inscrição é gratuita e há duas formas de entrar:
  Enem: média de 300 pontos ou mais, de qualquer edição a partir de 2010.
  Redação online: sem dia marcado, você faz quando puder. É eliminatória, com nota mínima 5,0.
  Em qualquer das duas, as aulas começam em 22/02/2027.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Fazer minha inscrição: {link_lp_utm}"
- Bloqueio: para o segmento noturno, BLOQUEADO com link da LP até G8; chamada até o desbloqueio: "Quer se inscrever? Responda esta mensagem."
- Follow-up: L3 (e-mail, D5).
- Opt-in e saída: FW.

### G1-L2-R (WhatsApp, versão para o representante legal)

- Template: grad_mv_lead_enem_resp_v1 (variáveis: {nome_candidato}, {link_lp_utm})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE. Esta mensagem é para o representante legal de {nome_candidato}: as duas formas de entrar na Medicina Veterinária.
- Primeira linha B: Olá. {nome_candidato} pediu informações sobre a Medicina Veterinária da Ufape. Veja como funciona o ingresso.
- Corpo:
  "A inscrição é gratuita e há duas formas de entrar: nota do Enem, com média de 300 pontos ou mais, de qualquer edição a partir de 2010; ou redação online, sem dia marcado, eliminatória, com nota mínima 5,0. Como {nome_candidato} é menor de idade, a inscrição e a matrícula precisam do seu aceite como representante legal. As aulas começam em 22/02/2027. Dúvidas? Responda esta mensagem e o time de captação fala com você.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver como se inscrever: {link_lp_utm}"
- Bloqueio: para o segmento noturno, BLOQUEADO com link da LP até G8; chamada até o desbloqueio: "Responda esta mensagem para falar com o time."
- Follow-up: nenhum automático. Quem responde vai ao time.
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-L3 (e-mail, D5): o desconto, com valor cheio e validade

- Canal: e-mail
- Objetivo: mostrar o preço inteiro, sem letra miúda, e levar à inscrição
- Segmento: lead sem inscrição, adulto (a família que decide junto pode receber o encaminhamento)
- Assunto A: Medicina Veterinária na Ufape: de R$ 10.000,00 por R$ 5.000,00 (integral) ou R$ 4.000,00 (noturno) por mês no 1º semestre de 2027
- Assunto B: O desconto do 1º semestre de 2027, com todas as regras
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e renovação, num lugar só.
- Gancho: Antes de decidir, a conta inteira.
- Corpo:
  "Olá, {primeiro_nome}.
  Estas são as condições do Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026) para Medicina Veterinária em São Paulo.
  Integral (4 anos): de R$ 10.000,00 por R$ 5.000,00 por mês, 50% de desconto. Em 6 mensalidades, R$ 30.000,00 no semestre, contra R$ 60.000,00 no valor cheio.
  Noturno (5 anos): de R$ 10.000,00 por R$ 4.000,00 por mês, 60% de desconto. Em 6 mensalidades, R$ 24.000,00 no semestre, contra R$ 60.000,00 no valor cheio.
  Regras: o desconto vale para todas as formas de ingresso, é aplicado a partir da confirmação da matrícula e vale só para o 1º semestre de 2027. Para continuar nos semestres seguintes, o aluno pede a renovação a cada semestre, com comprovação. A renovação não é automática e o valor dos semestres seguintes depende dessa análise. O desconto é perdido no mês em que a mensalidade for paga depois do vencimento (dia 10) e não vale junto com programas governamentais com regras próprias. O edital prevê reajuste do valor cheio em dezembro de cada ano.
  A inscrição é gratuita e o edital não prevê taxa de matrícula: a matrícula se confirma com o pagamento da 1ª mensalidade e a assinatura do contrato.
  Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio até G12 e G7. Com link da LP, também até G8 (cita o noturno).
- Chamada até o desbloqueio de G8: "Quer se inscrever? Responda este e-mail e o time de captação te ajuda."
- Nota (não vai ao candidato): [CONFIRMAR o efeito do reajuste de dezembro sobre 2027/1, G12.]
- Follow-up: L4 (WhatsApp, D8).
- Opt-in e saída: FE.

### G1-L4 (WhatsApp, D8): dúvidas de pais e responsáveis (adulto que decide com a família)

- Canal: WhatsApp automático (template grad_mv_lead_familia_v1; variável: {primeiro_nome})
- Objetivo: dar à família as respostas de que precisa para apoiar a decisão
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Se a sua família participa da decisão, pode encaminhar esta mensagem.
- Primeira linha B: Oi, {primeiro_nome}. O que pais e responsáveis precisam saber sobre a Medicina Veterinária da Ufape.
- Gancho: A família decide melhor com a conta inteira.
- Corpo:
  "Pontos para quem decide junto:
  Menor de idade: a inscrição e a matrícula precisam do aceite do representante legal.
  Inscrição gratuita. Matrícula: 1ª mensalidade e assinatura digital do contrato.
  Mensalidade: {LD-MV}
  Desistir antes de começar: devolução de 80% do valor pago, se pedida até 2 dias antes das aulas (20/02/2027).
  Se a turma tiver menos de 30 matriculados, a Ufape pode cancelar a oferta e devolve a 1ª parcela.
  Ato autorizativo: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025).
  Quer conversar com o time? É só responder.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda esta mensagem e o time liga ou escreve para a família" (resposta como ação única).
- Bloqueio: BLOQUEADO para envio até G12 e G7. Sem botão da LP no template até G8 (cita o noturno); depois de G8, o link da LP pode entrar como botão informativo, se o template aceitar [SUPOSIÇÃO de desenho].
- Follow-up: L5 (e-mail, D12).
- Opt-in e saída: FW.

### G1-L4-R (WhatsApp, versão para o representante legal do candidato menor)

- Template: grad_mv_lead_familia_resp_v1 (variável: {nome_candidato})
- Primeira linha A: Olá. Esta mensagem é para o representante legal de {nome_candidato}: o que você precisa saber sobre a Medicina Veterinária da Ufape.
- Primeira linha B: Olá, aqui é da Faculdade UFAPE. Respostas para o representante legal de {nome_candidato}.
- Corpo:
  "Pontos para quem decide:
  Como {nome_candidato} é menor de idade, a inscrição e a matrícula precisam do seu aceite como representante legal.
  Inscrição gratuita. Matrícula: 1ª mensalidade e assinatura digital do contrato.
  Mensalidade: {LD-MV}
  Desistir antes de começar: devolução de 80% do valor pago, se pedida até 2 dias antes das aulas (20/02/2027).
  Se a turma tiver menos de 30 matriculados, a Ufape pode cancelar a oferta e devolve a 1ª parcela.
  Ato autorizativo: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025).
  Se preferir, o time conversa por telefone ou por escrito, no horário que for melhor para você, de segunda a sexta, das 9h às 18h.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda esta mensagem para falar com o time"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: nenhum automático. Quem responde vai ao time.
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-L5 (e-mail, D12): visita (só se existir) ou o curso por dentro

Atenção: a visita guiada hoje é proposta (P4 da oferta), não existe. [CONFIRMAR se existe visita, quem conduz, agenda, regras para menores e autorização de imagem.] Sem essa confirmação, enviar a versão L5-alt, que não promete nada que não exista.

**G1-L5 (condicionado à confirmação da visita):**
- Canal: e-mail
- Objetivo: agendar uma visita
- Segmento: lead sem inscrição, adulto
- Assunto A: Quer conhecer a Faculdade UFAPE antes de decidir?
- Assunto B: Visita à Faculdade UFAPE: como agendar
- Texto de pré-visualização: {data_visita} em {local_visita}. Menores vão com o representante legal.
- Gancho: Ver o lugar ajuda a decidir.
- Corpo: "Olá, {primeiro_nome}. A Faculdade UFAPE recebe candidatos e famílias em visitas em {data_visita}, {local_visita}. Como funciona: {como_agendar}. Candidato menor de idade vai acompanhado do representante legal. A visita não substitui a inscrição, que é gratuita. Dúvidas: {contato_captacao}."
- Chamada para ação: "Agendar minha visita" ({link_agendamento})
- Nota (não vai ao candidato): [CONFIRMAR data, local, como agendar e o link de agendamento; sem isso, a mensagem não existe.]
- Follow-up: L6 (WhatsApp, D15).
- Opt-in e saída: FE.

**G1-L5-alt (e-mail, sem dependência de confirmação externa):**
- Canal: e-mail
- Objetivo: mostrar o curso e a autorização para quem ainda pergunta "é sério?", e levar à inscrição
- Segmento: lead sem inscrição, adulto
- Assunto A: Medicina Veterinária na Ufape: o que se estuda e como o curso é autorizado
- Assunto B: Antes de se inscrever: matriz, estágio e ato autorizativo
- Texto de pré-visualização: Prática desde o 1º semestre, estágio supervisionado e portaria, com a fonte.
- Gancho: Três coisas que dá para conferir antes de decidir.
- Corpo:
  "Olá, {primeiro_nome}.
  1) O que se estuda. Entre as disciplinas do 1º semestre estão Campos de Atuação do Médico Veterinário e Práticas Hospitalares, Projeto Extensionista I e Práticas Hospitalares. O estágio supervisionado fica nos {estagio}.
  2) Como o curso é autorizado. {BA}
  3) Onde tirar dúvidas pessoalmente. A inscrição também pode ser feita presencialmente, de segunda a sexta, das 9h às 18h, na Av. Nove de Julho, 3913 e 3939, Jardim Paulista, São Paulo.
  A inscrição é gratuita. Dúvidas: {contato_captacao}."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: para o segmento noturno, BLOQUEADO com link da LP até G8; chamada até o desbloqueio: "Quer se inscrever? Responda este e-mail."
- Nota (não vai ao candidato): disciplinas e estágio conferidos na ficha do curso (contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md) pelo qa-c. Linha opcional, só depois do pedido G11: "A Ufape tem hospital veterinário próprio, a Ufape Clínica."
- Follow-up: L6 (WhatsApp, D15).
- Opt-in e saída: FE.

### G1-L6 (WhatsApp, D15): objeção "e depois do 1º semestre?"

- Canal: WhatsApp automático (template grad_mv_lead_depois_v1; variável: {primeiro_nome})
- Objetivo: responder a objeção de preço com a regra real e abrir conversa com o time
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Uma pergunta justa antes de decidir: e depois do 1º semestre?
- Primeira linha B: Oi, {primeiro_nome}. A mensalidade com desconto vale por quanto tempo?
- Gancho: O desconto é do 1º semestre, e é melhor saber isso antes.
- Corpo:
  "{LD-MV}
  A renovação não é automática e o valor dos semestres seguintes depende dessa análise. A mensalidade cheia hoje é de R$ 10.000,00, e o edital prevê reajuste em dezembro de cada ano.
  Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação.
  Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Quer que o time explique? Responda QUERO."
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: L7 (e-mail, D20).
- Opt-in e saída: FW.

### G1-L7 (e-mail, D20): lembrete com o resumo

- Canal: e-mail
- Objetivo: lembrar o caminho e perguntar o que falta para decidir
- Segmento: lead sem inscrição, adulto, sem resposta à régua
- Assunto A: Sua inscrição gratuita no Vestibular 2027 de Medicina Veterinária
- Assunto B: Resumo em 6 linhas: como entrar na Medicina Veterinária da Ufape
- Texto de pré-visualização: Redação online, Enem, desconto do 1º semestre e matrícula.
- Gancho: Se faltou alguma resposta, é só dizer qual.
- Corpo:
  "Olá, {primeiro_nome}.
  Resumo: inscrição gratuita; redação online sem dia marcado (eliminatória, nota mínima 5,0) ou Enem com média de 300 pontos ou mais, de 2010 em diante; resultado no site; matrícula a partir de 2 dias depois, com a 1ª mensalidade e a assinatura digital; aulas a partir de 22/02/2027.
  Mensalidade: {LD-MV}
  O que falta para você decidir? Responda este e-mail com a sua dúvida e o time de captação responde. Edital de ingresso: {link_edital_vestibular}. {BM}"
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio até G12 e G7. Com link da LP, também até G8 (cita o noturno).
- Chamada até o desbloqueio de G8: a própria pergunta do corpo ("Responda este e-mail com a sua dúvida").
- Follow-up: nenhum. Sem engajamento, o lead recebe a etiqueta "sem engajamento" e a régua encerra (seção 5).
- Opt-in e saída: FE.

---

## G1-C. Régua do inscrito até a redação feita

Objetivo único: redação feita ou nota do Enem enviada. Gatilho: inscrição concluída. Toques: R1 (D0), R2 (D2), R3 (D5), R4 (D9), R5 (D14). Para a base existente, a entrada é pelo AT; quem não avançar entra em R3.

### G1-R1 (e-mail, D0): inscrição recebida e próximos passos

- Canal: e-mail (serviço, fora do teto D16)
- Objetivo: confirmar a inscrição e explicar a avaliação
- Segmento: inscrito novo, adulto
- Assunto A: Inscrição recebida: veja o que fazer agora no Vestibular 2027
- Assunto B: {primeiro_nome}, sua inscrição foi recebida. Próximo passo: redação ou Enem
- Texto de pré-visualização: Redação online sem dia marcado, ou nota do Enem com média mínima de 300 pontos (edições de 2010 em diante).
- Gancho: Sua inscrição entrou. Agora é escolher a avaliação.
- Corpo: "Olá, {primeiro_nome}. Recebemos a sua inscrição em Medicina Veterinária {turno}, Vestibular 2027, da Faculdade UFAPE. {BC} O que vem depois: {BX} {BM} Dúvidas: responda este e-mail ou fale em {contato_captacao}."
- Chamada para ação: "Acessar minha inscrição" ({link_area_candidato})
- Follow-up: R2 (WhatsApp, D2).
- Opt-in e saída: FE.

### G1-R1-R (e-mail, D0, versão para o representante legal)

- Canal: e-mail (serviço, fora do teto D16)
- Assunto A: Inscrição de {nome_candidato} recebida: o próximo passo é a redação ou o Enem
- Assunto B: Para o representante legal: como {nome_candidato} segue no Vestibular 2027
- Texto de pré-visualização: Redação online sem dia marcado ou Enem com média mínima de 300 pontos (edições de 2010 em diante).
- Gancho: A inscrição de {nome_candidato} entrou. Agora é a avaliação.
- Corpo: "Olá. Recebemos a inscrição de {nome_candidato} em Medicina Veterinária {turno}, Vestibular 2027, da Faculdade UFAPE. Como o candidato é menor de idade, a inscrição exigiu o aceite do representante legal, que também é necessário na matrícula. Para seguir, {nome_candidato} faz a avaliação: {BC} O que vem depois: {BX} Antes de qualquer pagamento, o time explica o valor e todas as condições. Dúvidas: responda este e-mail ou fale com o time de captação em {contato_captacao}."
- Chamada para ação: "Ver o passo a passo" ({link_area_candidato})
- Follow-up: R2-R (WhatsApp, D2).
- Opt-in e saída: FE, com consentimento do representante legal.

### G1-R2 (WhatsApp, D2): passo a passo e oferta de ajuda

- Canal: WhatsApp automático (template grad_mv_inscrito_passo_v1; variáveis: {primeiro_nome}, {turno}, {link_area_candidato})
- Objetivo: fazer o inscrito começar a avaliação
- Segmento: inscrito sem redação, adulto
- Primeira linha A: Oi, {primeiro_nome}. Sua inscrição foi recebida. Quer ajuda para fazer a redação?
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE. O próximo passo da sua inscrição é a redação ou o Enem.
- Gancho: Sem dia marcado: dá para fazer no seu ritmo.
- Corpo: "Para Medicina Veterinária {turno}: faça a redação online quando puder (eliminatória, nota mínima 5,0) ou envie sua nota do Enem (média de 300 pontos ou mais, de 2010 em diante). O passo a passo está na área do candidato. Se algo não funcionar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: R3 (e-mail, D5).
- Opt-in e saída: FW.

### G1-R2-R (WhatsApp, D2, versão para o representante legal)

- Template: grad_mv_inscrito_passo_resp_v1 (variáveis: {nome_candidato}, {turno}, {link_area_candidato})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE. A inscrição de {nome_candidato} foi recebida: o próximo passo é a redação ou o Enem.
- Primeira linha B: Olá. Você é o representante legal de {nome_candidato}? Temos o passo a passo da avaliação.
- Corpo: "Para Medicina Veterinária {turno}, {nome_candidato} faz a redação online quando puder (eliminatória, nota mínima 5,0) ou envia a nota do Enem (média de 300 pontos ou mais, de 2010 em diante). O passo a passo está na área do candidato. Como o candidato é menor de idade, o seu aceite como representante legal também é necessário na matrícula. Se algo não funcionar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver o passo a passo: {link_area_candidato}"
- Follow-up: nenhum automático. Quem responde vai ao time.
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-R3 (e-mail, D5): perguntas sobre a redação e o Enem, respondidas

- Canal: e-mail
- Objetivo: tirar as dúvidas que seguram a avaliação
- Segmento: inscrito sem redação, adulto (inclui a base existente depois do AT3)
- Assunto A: Redação e Enem no Vestibular da Ufape: as dúvidas respondidas
- Assunto B: Posso fazer a redação de casa? Vale o Enem antigo? Respostas do edital
- Texto de pré-visualização: Cada resposta vem do edital do Vestibular 2027.
- Gancho: Respostas curtas, com a fonte.
- Corpo:
  "Olá, {primeiro_nome}.
  Posso fazer a redação de casa? A prova é online.
  Tem data marcada? Não. Você faz a qualquer momento depois da inscrição.
  Reprovo se tirar menos de 5,0? A redação é eliminatória, com nota mínima 5,0.
  Vale o Enem de anos atrás? Vale a média aritmética de 300 pontos ou mais, de qualquer edição a partir de 2010.
  E se eu já tiver outro diploma, ou quiser transferência? Há ingresso de diplomado e transferência externa, mas só depois dos ingressantes por redação e Enem. Fale com o time.
  Edital completo: {link_edital_vestibular}."
- Chamada para ação: "Fazer minha redação ou enviar o Enem" ({link_area_candidato})
- Nota (não vai ao candidato): [CONFIRMAR se há nova tentativa, como a média do Enem é calculada e como a nota é enviada.]
- Follow-up: R4 (WhatsApp, D9).
- Opt-in e saída: FE.

### G1-R4 (WhatsApp, D9): ajuda do time

- Canal: WhatsApp automático (template grad_mv_inscrito_ajuda_v1; variável: {primeiro_nome})
- Objetivo: descobrir o que trava e passar ao time
- Segmento: inscrito sem redação, sem resposta
- Primeira linha A: Oi, {primeiro_nome}. O que está faltando para você fazer a redação?
- Primeira linha B: Oi, {primeiro_nome}. Podemos ajudar com a sua redação ou com o Enem?
- Gancho: Uma resposta de uma palavra já ajuda.
- Corpo: "Responda com o número: 1) não sei por onde começar; 2) prefiro usar a nota do Enem; 3) tenho dúvida sobre o valor; 4) outro motivo. O time de captação te responde no horário comercial. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda com o número da sua situação."
- Follow-up: R5 (e-mail, D14).
- Opt-in e saída: FW.

### G1-R5 (e-mail, D14): o que acontece depois da redação

- Canal: e-mail
- Objetivo: mostrar o que vem depois (resultado, matrícula, valor) para reduzir o medo do passo seguinte
- Segmento: inscrito sem redação
- Assunto A: Depois da redação: resultado, matrícula e valor, passo a passo
- Assunto B: O que acontece depois que você faz a redação do Vestibular
- Texto de pré-visualização: Do resultado no site à primeira mensalidade, sem surpresas.
- Gancho: Saber o que vem depois ajuda a dar o primeiro passo.
- Corpo: "Olá, {primeiro_nome}. {BX} Valor: {bloco_preco} E depois do 1º semestre? {BD-MV} A inscrição é gratuita e o edital não prevê taxa de matrícula. {BM}"
- Chamada para ação: "Fazer minha redação ou enviar o Enem" ({link_area_candidato})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: nenhuma mensagem automática. No D21, o time de captação recebe a tarefa de contato humano (seção 5).
- Opt-in e saída: FE.

---

## G1-D. Régua do aprovado até a matrícula

Objetivo único: 1ª mensalidade paga e contrato assinado. Gatilho: resultado publicado com status "aprovado" no sistema de inscrição. Só entra quem tem esse status; nenhum "parabéns" sai por suposição. Aprovado via redação ou via Enem recebe a mesma régua. Toques: A1 (D0), A2 (D+2, matrícula aberta), A3 (D+3), A5 (D+7), A6 (D+14 ou, no máximo, a partir de 01/02/2027 para quem segue sem matrícula). Representante legal de candidato menor: A1-R (D0), A4-R (D+2, no lugar do A2), A3-R (D+3), A6-R (D+14).

### G1-A1 (e-mail, D0): seu resultado está no site

- Canal: e-mail (serviço, fora do teto D16)
- Objetivo: avisar o resultado e a data da matrícula
- Segmento: aprovado, adulto
- Assunto A: Seu resultado do Vestibular 2027 está no site
- Assunto B: {primeiro_nome}, parabéns pela aprovação: veja como fazer a matrícula
- Texto de pré-visualização: A matrícula abre a partir de 2 dias depois da publicação do resultado.
- Gancho: Você passou. Agora vêm 3 passos curtos.
- Corpo:
  "Olá, {primeiro_nome}. Parabéns pela aprovação em Medicina Veterinária {turno}, Vestibular 2027, da Faculdade UFAPE.
  Resultado: {link_resultado}.
  Matrícula: eletrônica, a partir de {data_matricula} (2 dias depois da publicação). Para confirmar, são 3 passos: (1) pagar a 1ª mensalidade; (2) assinar o contrato digitalmente; (3) enviar os documentos pela plataforma de matrícula digital em até 30 dias.
  Antes de pagar, o próximo e-mail traz o valor e todas as condições.
  {BM} As aulas começam em 22/02/2027.
  Dúvidas: {contato_captacao}."
- Chamada para ação: "Ver meu resultado" ({link_resultado})
- Nota (não vai ao candidato): [CONFIRMAR de quando contam os 30 dias dos documentos.]
- Follow-up: A2 (WhatsApp, D+2).
- Opt-in e saída: FE.

### G1-A1-R (e-mail, D0, versão para o representante legal)

- Canal: e-mail (serviço, fora do teto D16)
- Assunto A: O resultado de {nome_candidato} no Vestibular 2027 está no site
- Assunto B: Para o representante legal: como fazer a matrícula de {nome_candidato}
- Texto de pré-visualização: A matrícula é eletrônica, abre a partir de 2 dias depois do resultado e precisa do seu aceite.
- Gancho: O resultado saiu. A matrícula de {nome_candidato} precisa de você.
- Corpo: "Olá. Parabéns pela aprovação de {nome_candidato} em Medicina Veterinária {turno}, Vestibular 2027, da Faculdade UFAPE. Resultado: {link_resultado}. Matrícula: eletrônica, a partir de {data_matricula} (2 dias depois da publicação). Como {nome_candidato} é menor de idade, a matrícula precisa do aceite do representante legal. Para confirmar, são 3 passos: (1) pagar a 1ª mensalidade; (2) assinar o contrato digitalmente; (3) enviar os documentos pela plataforma de matrícula digital em até 30 dias. Antes de pagar, o próximo e-mail traz o valor e todas as condições. As aulas começam em 22/02/2027. Dúvidas: {contato_captacao}."
- Chamada para ação: "Ver o resultado" ({link_resultado})
- Nota (não vai ao candidato): [CONFIRMAR como o aceite do representante legal é dado na matrícula e de quando contam os 30 dias.]
- Follow-up: A4-R (WhatsApp, D+2).
- Opt-in e saída: FE, com consentimento do representante legal.

### G1-A2 (WhatsApp, D+2): matrícula aberta

- Canal: WhatsApp automático (template grad_mv_aprovado_matricula_v1; variáveis: {primeiro_nome}, {link_matricula})
- Objetivo: levar à matrícula
- Segmento: aprovado sem matrícula, adulto
- Primeira linha A: Oi, {primeiro_nome}. Sua matrícula na Medicina Veterinária da Ufape já está aberta.
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE. Hoje abre a matrícula do seu curso.
- Gancho: São 3 passos.
- Corpo: "Para confirmar a matrícula: 1) pague a 1ª mensalidade; 2) assine o contrato digitalmente; 3) envie os documentos na plataforma em até 30 dias. Valor: {linha_desconto} As aulas começam em 22/02/2027. Se tiver dúvida antes de pagar, responda aqui. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Fazer minha matrícula: {link_matricula}"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: A3 (e-mail, D+3).
- Opt-in e saída: FW.

### G1-A3 (e-mail, D+3): antes de pagar, as regras

- Canal: e-mail
- Objetivo: dar a conta inteira (desconto, renovação, cancelamento, turma mínima) para decidir sem susto
- Segmento: aprovado sem matrícula, adulto
- Assunto A: Antes de se matricular: desconto, renovação e cancelamento em linguagem simples
- Assunto B: Sua matrícula na Ufape: o que você paga, quando e o que acontece se desistir
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e devolução de 80%.
- Gancho: A decisão de pagar fica mais segura com todas as regras na mesa.
- Corpo:
  "Olá, {primeiro_nome}.
  O que você paga: {bloco_preco}
  E depois do 1º semestre? {BD-MV}
  Primeira mensalidade: {valor_primeira_mensalidade}. O edital não prevê taxa de matrícula.
  Se você desistir antes de começar: a devolução é de 80% do valor pago, se o pedido de cancelamento for feito até 2 dias antes do início das aulas, ou seja, até 20/02/2027.
  Se a turma não formar: a turma precisa de pelo menos 30 matriculados. Abaixo disso, a Ufape pode cancelar a oferta e devolve a 1ª parcela.
  {BM}
  Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Fazer minha matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR se a 1ª mensalidade já sai com o desconto; sem a resposta, a linha da 1ª mensalidade sai do texto. CONFIRMAR a data em que a Ufape decide sobre a turma mínima, pedido G4.]
- Follow-up: A5 (WhatsApp, D+7).
- Opt-in e saída: FE.

### G1-A3-R (e-mail, D+3, versão para o representante legal)

- Assunto A: Antes da matrícula de {nome_candidato}: valor, renovação e cancelamento
- Assunto B: Para o representante legal: o que se paga, quando e o que acontece em caso de desistência
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e devolução de 80%.
- Gancho: Todas as regras na mesa antes de qualquer pagamento.
- Corpo: "Olá. O que se paga: {bloco_preco} E depois do 1º semestre? {BD-MV} Primeira mensalidade: {valor_primeira_mensalidade}. O edital não prevê taxa de matrícula. Aceite: como {nome_candidato} é menor de idade, a matrícula precisa do aceite do representante legal. Desistência antes de começar: devolução de 80% do valor pago, se o cancelamento for pedido até 2 dias antes do início das aulas, ou seja, até 20/02/2027. Se a turma não formar: a turma precisa de pelo menos 30 matriculados; abaixo disso, a Ufape pode cancelar a oferta e devolve a 1ª parcela. Dúvidas: responda este e-mail ou fale com o time em {contato_captacao}. Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Ir para a matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): as mesmas do A3.
- Follow-up: nenhum automático até o A6-R.
- Opt-in e saída: FE, com consentimento do representante legal.

### G1-A4-R (WhatsApp, D+2, versão do A2 para o representante legal de candidato menor)

- Canal: WhatsApp automático (template grad_mv_aprovado_resp_v1; variáveis: {nome_candidato}, {link_matricula})
- Objetivo: orientar o representante legal sobre o aceite e a matrícula
- Segmento: aprovado menor de idade, contato do representante legal
- Primeira linha A: Olá. Esta mensagem é para o representante legal de {nome_candidato}: a matrícula já pode ser feita.
- Primeira linha B: Olá, aqui é da Faculdade UFAPE. Sobre a matrícula de {nome_candidato}, o aceite do representante legal é necessário.
- Gancho: A matrícula de menor de idade precisa de você.
- Corpo: "O aceite do representante legal é necessário na matrícula de candidato menor de idade. A matrícula se confirma com a 1ª mensalidade e a assinatura digital do contrato; os documentos entram em até 30 dias. Valor: {linha_desconto} Se desistir até 20/02/2027, a devolução é de 80% do valor pago. O time explica por telefone, se preferir. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Falar com o time: responda esta mensagem"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR como o aceite é dado: assinatura do contrato pelo representante legal ou outro meio.]
- Follow-up: A3-R (e-mail, D+3).
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-A5 (WhatsApp, D+7): o que travou?

- Canal: WhatsApp automático (template grad_mv_aprovado_trava_v1; variável: {primeiro_nome})
- Objetivo: descobrir e resolver o que impede a matrícula
- Segmento: aprovado sem matrícula, adulto
- Primeira linha A: Oi, {primeiro_nome}. A sua matrícula ainda não foi concluída. Podemos ajudar?
- Primeira linha B: Oi, {primeiro_nome}. Algo travou na sua matrícula?
- Gancho: Se travou em um ponto, a gente resolve com você.
- Corpo: "Responda com o número: 1) pagamento da 1ª mensalidade; 2) contrato ou assinatura digital; 3) documentos; 4) dúvida sobre o valor ou o desconto; 5) outro motivo. O time te responde no horário comercial. As aulas começam em 22/02/2027. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda com o número da sua situação."
- Follow-up: A6 (e-mail, D+14).
- Opt-in e saída: FW.

### G1-A6 (e-mail, D+14 ou a partir de 01/02/2027): como concluir a matrícula antes das aulas

- Canal: e-mail
- Objetivo: lembrar o que falta para começar com a turma
- Segmento: aprovado sem matrícula, adulto
- Assunto A: Aulas começam em 22/02/2027: como concluir a sua matrícula
- Assunto B: {primeiro_nome}, o que falta para a sua matrícula na Ufape
- Texto de pré-visualização: Passos, regras e quem chamar. Sem pressa falsa, só os fatos.
- Gancho: Para começar em 22/02/2027, faltam estes passos.
- Corpo: "Olá, {primeiro_nome}. As aulas de Medicina Veterinária {turno} começam em 22/02/2027. Para participar, a matrícula precisa estar confirmada: 1ª mensalidade paga e contrato assinado. Se você mudar de ideia depois de se matricular, o cancelamento com devolução de 80% vale se pedido até 2 dias antes do início das aulas (20/02/2027). Valor: {linha_desconto} Se algo o impede, responda este e-mail e o time ajuda. {BM}"
- Chamada para ação: "Concluir minha matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): revisar em 25/01/2027 com números reais de matrícula; nenhuma frase sobre vagas entra sem número real.
- Follow-up: nenhum. Sem resposta, o aprovado recebe a etiqueta "sem engajamento" e a régua encerra (seção 5).
- Opt-in e saída: FE.

### G1-A6-R (e-mail, D+14, versão para o representante legal)

- Assunto A: Aulas começam em 22/02/2027: o que falta na matrícula de {nome_candidato}
- Assunto B: Para o representante legal: como concluir a matrícula de {nome_candidato}
- Texto de pré-visualização: Passos, regras e quem chamar. Só os fatos.
- Gancho: Para começar em 22/02/2027, faltam estes passos.
- Corpo: "Olá. As aulas de Medicina Veterinária {turno} começam em 22/02/2027. Para {nome_candidato} participar, a matrícula precisa estar confirmada: 1ª mensalidade paga e contrato assinado, com o aceite do representante legal. Se a família mudar de ideia depois da matrícula, o cancelamento com devolução de 80% vale se pedido até 2 dias antes do início das aulas (20/02/2027). Valor: {linha_desconto} Se algo impede a matrícula, responda este e-mail e o time ajuda."
- Chamada para ação: "Concluir a matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): a mesma do A6.
- Follow-up: nenhum.
- Opt-in e saída: FE, com consentimento do representante legal.

---

## G1-E. Régua do matriculado até 22/02/2027

Objetivo único: matrícula completa (documentos enviados) e permanência até o início das aulas. Gatilho: matrícula confirmada (1ª mensalidade e contrato). Toques: M1 (D0), M2 (D+5), M3 (D+14), M4 (antes do vencimento do dia 10), M5 (15/02/2027). Mensagens de cobrança e de contrato são do financeiro e da secretaria (financeiro@intercursos.com.br, (11) 94525-3730 no WhatsApp); a régua de marketing não cobra [CONFIRMAR com o financeiro].

### G1-M1 (e-mail, D0): matrícula confirmada

- Canal: e-mail (serviço, fora do teto D16)
- Objetivo: confirmar e listar o que falta fazer
- Segmento: matriculado, adulto
- Assunto A: Matrícula confirmada: o que acontece até as aulas, em 22/02/2027
- Assunto B: {primeiro_nome}, sua matrícula na Ufape está confirmada. Veja os próximos passos
- Texto de pré-visualização: Documentos em até 30 dias, mensalidade no dia 10 e como falar com a secretaria.
- Gancho: Matrícula feita. Agora, o que falta.
- Corpo: "Olá, {primeiro_nome}. Sua matrícula em Medicina Veterinária {turno} da Faculdade UFAPE está confirmada. O que fazer: enviar os documentos pela plataforma de matrícula digital em até 30 dias. O que vale para você: a mensalidade vence no dia 10. Se precisar cancelar, a devolução de 80% vale se o pedido for feito até 20/02/2027. As aulas começam em 22/02/2027. Secretaria: (11) 97492-8443 (WhatsApp) ou (11) 5054-1204, duvidas@intercursos.com.br, de segunda a sexta, das 9h às 18h."
- Chamada para ação: "Enviar meus documentos" ({link_matricula})
- Follow-up: M2 (WhatsApp, D+5).
- Opt-in e saída: FE.

### G1-M1-R (e-mail, D0, versão para o representante legal)

- Canal: e-mail (serviço, fora do teto D16)
- Assunto A: Matrícula de {nome_candidato} confirmada: o que acontece até 22/02/2027
- Assunto B: Para o representante legal: próximos passos da matrícula de {nome_candidato}
- Texto de pré-visualização: Documentos em até 30 dias, vencimento no dia 10 e contatos da secretaria.
- Gancho: Matrícula feita. Agora, o que falta.
- Corpo: "Olá. A matrícula de {nome_candidato} em Medicina Veterinária {turno} da Faculdade UFAPE está confirmada. O que fazer: enviar os documentos pela plataforma de matrícula digital em até 30 dias. A mensalidade vence no dia 10. Se precisar cancelar, a devolução de 80% vale se o pedido for feito até 20/02/2027. As aulas começam em 22/02/2027. Secretaria: (11) 97492-8443 (WhatsApp) ou (11) 5054-1204, duvidas@intercursos.com.br, de segunda a sexta, das 9h às 18h."
- Chamada para ação: "Enviar os documentos" ({link_matricula})
- Follow-up: M2-R (WhatsApp, D+5).
- Opt-in e saída: FE, com consentimento do representante legal.

### G1-M2 (WhatsApp, D+5): documentos

- Canal: WhatsApp automático (template grad_mv_matriculado_docs_v1; variáveis: {primeiro_nome}, {link_matricula})
- Objetivo: documentos enviados
- Segmento: matriculado sem todos os documentos, adulto
- Primeira linha A: Oi, {primeiro_nome}. Lembrete: os documentos da matrícula entram pela plataforma, em até 30 dias.
- Primeira linha B: Oi, {primeiro_nome}. Faltam documentos na sua matrícula na Ufape?
- Gancho: Enviar agora evita correria depois.
- Corpo: "Os documentos da matrícula são enviados pela plataforma de matrícula digital, em até 30 dias. A lista de documentos está na plataforma. As aulas começam em 22/02/2027. Se tiver dificuldade para enviar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Enviar documentos: {link_matricula}"
- Nota (não vai ao candidato): [CONFIRMAR a lista de documentos na plataforma.]
- Follow-up: M3 (e-mail, D+14).
- Opt-in e saída: FW.

### G1-M2-R (WhatsApp, D+5, versão para o representante legal)

- Template: grad_mv_matriculado_docs_resp_v1 (variáveis: {nome_candidato}, {link_matricula})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE. Lembrete para o representante legal de {nome_candidato}: os documentos da matrícula entram pela plataforma, em até 30 dias.
- Primeira linha B: Olá. Faltam documentos na matrícula de {nome_candidato}?
- Corpo: "Os documentos da matrícula de {nome_candidato} são enviados pela plataforma de matrícula digital, em até 30 dias. A lista está na plataforma. As aulas começam em 22/02/2027. Se tiver dificuldade para enviar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Enviar documentos: {link_matricula}"
- Follow-up: M5-R (15/02/2027).
- Opt-in e saída: FW, com consentimento do representante legal.

### G1-M3 (e-mail, D+14): o que esperar do 1º semestre

- Canal: e-mail
- Objetivo: diminuir a ansiedade e confirmar o essencial do começo
- Segmento: matriculado, adulto
- Assunto A: Seu 1º semestre de Medicina Veterinária na Ufape: o que esperar
- Assunto B: Antes das aulas de 22/02/2027: o que você já pode saber
- Texto de pré-visualização: Início, turno, matriz do 1º semestre e contatos.
- Gancho: Como vai ser o começo.
- Corpo: "Olá, {primeiro_nome}. Início das aulas: 22/02/2027, em São Paulo, no turno {turno}, com duração de {duracao}. Entre as disciplinas do 1º semestre estão Campos de Atuação do Médico Veterinário e Práticas Hospitalares, Projeto Extensionista I e Práticas Hospitalares. Local do primeiro dia, horários e calendário: {local_primeiro_dia}, {horarios}, {calendario}. Dúvidas: {contato_captacao}."
- Chamada para ação: "Falar com a secretaria" (WhatsApp da secretaria)
- Nota (não vai ao candidato): disciplinas conferidas na ficha do curso pelo qa-c. [CONFIRMAR local, horários e calendário; se a Ufape não confirmar, a frase vira "Local, horários e calendário chegam por e-mail antes do início das aulas".]
- Follow-up: M4 (WhatsApp).
- Opt-in e saída: FE.

### G1-M4 (WhatsApp): mensalidade no dia 10 e o desconto

- Canal: WhatsApp automático (template grad_mv_matriculado_mensalidade_v1; variáveis: {primeiro_nome}, {linha_desconto})
- Objetivo: proteger o desconto do aluno
- Segmento: matriculado, 3 a 5 dias úteis antes de cada vencimento do dia 10 do 1º semestre
- Primeira linha A: Oi, {primeiro_nome}. A sua mensalidade vence no dia 10.
- Primeira linha B: Oi, {primeiro_nome}. Um lembrete para você não perder o desconto do mês.
- Gancho: O desconto é perdido no mês em que a mensalidade é paga depois do vencimento.
- Corpo: "A mensalidade vence no dia 10. Se for paga depois do vencimento, o desconto do edital é perdido naquele mês. O seu desconto: {linha_desconto} Dúvidas sobre boleto ou pagamento: financeiro@intercursos.com.br ou (11) 94525-3730 (WhatsApp). Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Falar com o financeiro: (11) 94525-3730"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR o calendário das 6 mensalidades e quem envia: financeiro ou marketing.] Serviço só se o cmo aprovar (seção 0.7).
- Follow-up: nenhum.
- Opt-in e saída: FW.

### G1-M5 (e-mail, 15/02/2027): semana de início

- Canal: e-mail (serviço, fora do teto D16)
- Objetivo: confirmar a segunda-feira de início e dar o contato certo
- Segmento: matriculado, adulto
- Assunto A: Segunda-feira, 22/02/2027: começam as suas aulas de Medicina Veterinária
- Assunto B: {primeiro_nome}, sua semana de início na Faculdade UFAPE
- Texto de pré-visualização: Local, horário e documentos pendentes, num e-mail só.
- Gancho: Falta uma semana.
- Corpo: "Olá, {primeiro_nome}. As aulas de Medicina Veterinária {turno} começam em 22/02/2027. Documentos pendentes: {docs_pendentes} (enviar em {link_matricula}). Local e horário do primeiro dia: {local_primeiro_dia}, {horarios}. Lembrete de regra: o cancelamento com devolução de 80% vale se pedido até 20/02/2027. Contato da secretaria: (11) 97492-8443 (WhatsApp), de segunda a sexta, das 9h às 18h."
- Chamada para ação: "Enviar os documentos que faltam" ({link_matricula}); se não houver pendência, o CTA vira "Falar com a secretaria"
- Nota (não vai ao candidato): revisar em 25/01/2027 com os dados reais antes do envio. [CONFIRMAR local e horário.]
- Follow-up: nenhum. A régua termina em 22/02/2027.
- Opt-in e saída: FE.

### G1-M5-R (e-mail, 15/02/2027, versão para o representante legal)

- Assunto A: Segunda-feira, 22/02/2027: começam as aulas de {nome_candidato}
- Assunto B: Para o representante legal: a semana de início de {nome_candidato}
- Texto de pré-visualização: Local, horário e documentos pendentes, num e-mail só.
- Gancho: Falta uma semana.
- Corpo: "Olá. As aulas de Medicina Veterinária {turno} de {nome_candidato} começam em 22/02/2027. Documentos pendentes: {docs_pendentes} (enviar em {link_matricula}). Local e horário do primeiro dia: {local_primeiro_dia}, {horarios}. Lembrete de regra: o cancelamento com devolução de 80% vale se pedido até 20/02/2027. Contato da secretaria: (11) 97492-8443 (WhatsApp), de segunda a sexta, das 9h às 18h."
- Chamada para ação: "Enviar os documentos que faltam" ({link_matricula}); sem pendência, "Falar com a secretaria"
- Nota (não vai ao candidato): a mesma do M5.
- Follow-up: nenhum.
- Opt-in e saída: FE, com consentimento do representante legal.

---

# PARTE G2: Pedagogia (Goiânia, noturno)

Restrições próprias (0.1, item 8): nenhuma carga horária, docente, trecho de modelo da página, bloco do egresso, lista de professores, endereço de Goiânia, dia de vencimento ou reajuste. Contato: {contato_captacao} = Vendas Goiânia, (62) 9420-1847. E-mail de dúvidas: duvidas@intercursos.com.br [CONFIRMAR se atende Goiânia]. Variáveis: {curso} = Pedagogia; {bloco_preco} = BP-PED; {linha_desconto} = LD-PED; e depois do 1º semestre = BD-PED; edital de ingresso = Edital nº 004/2026. Rodapé de e-mail: o do G2 (FE).

Inscrição presencial: o edital cita a Av. T-9, 102, Jardim América, Goiânia, e a página cita outro endereço (pedido G9). Até a confirmação, as mensagens dizem "inscrição pelo site ou presencial em Goiânia; o time informa o endereço" e não trazem o endereço.

Matriz própria da Pedagogia que pode ser citada (ficha do curso, conferida pelo qa-c): Prática Docente e Projeto Integrador desde o 1º semestre; Educação Inclusiva; Letramento em Libras; docência na Educação Infantil e nos anos iniciais do Ensino Fundamental e gestão educacional (1º parágrafo da página, próprio da Pedagogia); estágio supervisionado a partir do 6º semestre.

**Bloqueio da página (regra 13, pedido G6):** toda mensagem do G2 com {link_lp_utm} (L1, L2, L2-R, L3, L4 sem botão, L5, L7) está BLOQUEADA para envio com link da LP até G6. Até lá, a chamada vira resposta à mensagem, com o texto da "Chamada até o desbloqueio" de cada uma. As mensagens com link de sistema (área do candidato, resultado, matrícula) não dependem de G6.

Público adulto de Goiânia: a regra do aceite do representante legal para menor entra no BM, sem ser o argumento central. As versões -R do G2 estão escritas por extenso na seção G2-V.

## G2-A. Ativação da base: inscritos de Goiânia sem redação

Mesmo segmento, ordem, datas e medição do G1-A.1, com o contato de Goiânia. Prazo que vale: igual ao G1-A.2 (sem data de prova, sem data final publicada, aulas em 22/02/2027, matrícula a partir de 2 dias depois do resultado, cancelamento com 80% até 20/02/2027). Vagas existem (80, Edital 004/2026), sem número de restantes: nenhuma mensagem fala em vagas acabando. Os passos de BC valem para Goiânia (o Edital 004/2026 repete as regras de São Paulo).

### G2-AT1 (e-mail)

- Canal: e-mail
- Linha e curso: Graduação, Pedagogia, Goiânia, noturno
- Objetivo: levar o inscrito a fazer a redação online ou enviar o Enem
- Segmento: inscrito sem redação, adulto
- Assunto A: {primeiro_nome}, sua inscrição na Pedagogia está feita: o próximo passo é a redação ou o Enem
- Assunto B: Redação online, sem dia marcado: veja como fazer
- Texto de pré-visualização: Faça quando puder, ou use sua nota do Enem (média mínima de 300 pontos, edições de 2010 em diante).
- Gancho: Sua inscrição entrou. Falta mostrar a sua nota.
- Corpo: "Olá, {primeiro_nome}. Você se inscreveu no Processo Seletivo 2027.1 de Pedagogia noturno, em Goiânia, da Faculdade UFAPE. Para seguir, falta a avaliação. {BC} O que vem depois: {BX} {BM} Dúvidas: responda este e-mail ou fale com o time de Goiânia em (62) 9420-1847."
- Chamada para ação: "Acessar minha inscrição" ({link_area_candidato})
- Follow-up: G2-AT2 (WhatsApp, 1 dia útil depois).
- Opt-in e saída: FE (rodapé do G2).

### G2-AT2 (WhatsApp)

- Canal: WhatsApp automático (template grad_ped_ativacao_redacao_v1; variáveis: {primeiro_nome}, {link_area_candidato})
- Objetivo: levar à área do candidato
- Segmento: inscrito sem redação, adulto, sem resposta ao AT1
- Primeira linha A: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE de Goiânia. Sua redação pode ser feita online, sem dia marcado.
- Primeira linha B: Oi, {primeiro_nome}. Já fez o Enem? Com média mínima de 300 pontos (edições de 2010 em diante), sua nota pode ser a sua entrada na Pedagogia.
- Gancho: Duas formas de entrar, as duas sem custo de inscrição.
- Corpo: "Para a sua inscrição na Pedagogia noturno: 1) redação online, sem dia marcado, eliminatória, nota mínima 5,0; 2) ou nota do Enem, média de 300 pontos ou mais, de qualquer edição a partir de 2010. Depois, o resultado sai no site e a matrícula abre a partir de 2 dias depois. As aulas começam em 22/02/2027. Quer falar com uma pessoa do time? Responda esta mensagem. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: G2-AT3 (4 dias úteis depois).
- Opt-in e saída: FW.

### G2-AT3 (WhatsApp)

- Canal: WhatsApp automático (template grad_ped_ativacao_perguntas_v1; variáveis: {primeiro_nome}, {link_area_candidato})
- Objetivo: tirar a dúvida que trava a redação
- Segmento: sem resposta ao AT2, adulto
- Primeira linha A: Oi, {primeiro_nome}. Três respostas rápidas sobre a redação do Processo Seletivo da Ufape.
- Primeira linha B: Oi, {primeiro_nome}. Ficou alguma dúvida sobre a redação ou sobre o Enem?
- Gancho: Respostas curtas, direto do edital.
- Corpo: "Dá para fazer de casa? A redação é online. Tem data marcada? Não: é feita a qualquer momento depois da inscrição. Já fiz o Enem, vale? Vale a média de 300 pontos ou mais, de qualquer edição a partir de 2010. Se a sua dúvida for outra, responda aqui e o time de Goiânia te ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: nenhum WhatsApp novo; entra na régua R no G2-R3.
- Opt-in e saída: FW.

## G2-B. Régua do lead novo (até a inscrição)

Mesmos tempos do G1-B (D0, D2, D5, D8, D12, D15, D20). Bloqueio G6 em toda mensagem com link da LP.

### G2-L1 (e-mail, D0): boas-vindas e como funciona o ingresso

- Canal: e-mail
- Objetivo: mostrar o caminho e levar à inscrição gratuita
- Segmento: lead novo, adulto
- Assunto A: Boas-vindas ao Processo Seletivo 2027.1 de Pedagogia da Faculdade UFAPE, em Goiânia
- Assunto B: Como entrar na Pedagogia noturno em Goiânia: 4 passos e inscrição gratuita
- Texto de pré-visualização: Redação online sem dia marcado ou nota do Enem com média mínima de 300 pontos. Aulas a partir de 22/02/2027.
- Gancho: Do cadastro à matrícula, em 4 passos.
- Corpo: "Olá, {primeiro_nome}. Boas-vindas. Você pediu informações sobre Pedagogia na Faculdade UFAPE de Goiânia. 1) Inscrição gratuita, pelo site ou presencial em Goiânia (o time informa o endereço). 2) Avaliação: redação online sem dia marcado (eliminatória, nota mínima 5,0) ou nota do Enem (média de 300 pontos ou mais, edições de 2010 em diante). 3) Resultado no site. 4) Matrícula eletrônica, a partir de 2 dias depois do resultado, com a 1ª mensalidade e a assinatura digital do contrato. Documentos em até 30 dias. O curso: {BA} Presencial, noturno, em 4 anos. As aulas começam em 22/02/2027. {BM} Dúvidas: responda este e-mail ou fale em (62) 9420-1847."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio com link da LP até G6.
- Chamada até o desbloqueio: "Quer se inscrever? Responda este e-mail e o time de Goiânia te ajuda."
- Follow-up: G2-L2 (WhatsApp, D2).
- Opt-in e saída: FE (rodapé do G2).

### G2-L2 (WhatsApp, D2): Enem desde 2010 ou redação

- Canal: WhatsApp automático (template grad_ped_lead_enem_v1; variáveis: {primeiro_nome}, {link_lp_utm})
- Objetivo: mostrar as duas portas de entrada
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Já fez o Enem? Com média mínima de 300 pontos (edições de 2010 em diante), sua nota pode ser a sua entrada na Pedagogia da Ufape.
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE de Goiânia. A inscrição é gratuita: redação online ou nota do Enem (média mínima de 300 pontos, edições de 2010 em diante).
- Gancho: Quem fez o Enem anos atrás também pode usar a nota, de qualquer edição a partir de 2010, com média mínima de 300 pontos.
- Corpo: "Para a Pedagogia noturno, a inscrição é gratuita e há duas formas de entrar. Enem: média de 300 pontos ou mais, de qualquer edição a partir de 2010. Redação online: sem dia marcado, você faz quando puder; é eliminatória, com nota mínima 5,0. As aulas começam em 22/02/2027. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Fazer minha inscrição: {link_lp_utm}"
- Bloqueio: BLOQUEADO para envio com link da LP até G6.
- Chamada até o desbloqueio: "Quer se inscrever? Responda esta mensagem."
- Follow-up: G2-L3 (e-mail, D5).
- Opt-in e saída: FW.

### G2-L3 (e-mail, D5): o desconto, com valor cheio e validade

- Canal: e-mail
- Objetivo: mostrar o preço inteiro e levar à inscrição
- Segmento: lead sem inscrição, adulto
- Assunto A: Pedagogia noturno na Ufape: de R$ 1.050,00 por R$ 525,00 por mês no 1º semestre de 2027
- Assunto B: O desconto do 1º semestre de 2027 na Pedagogia, com todas as regras
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e renovação, num lugar só.
- Gancho: Antes de decidir, a conta inteira.
- Corpo: "Olá, {primeiro_nome}. Condições do Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026): de R$ 1.050,00 por R$ 525,00 por mês, 50% de desconto. Em 6 mensalidades, R$ 3.150,00 no semestre, contra R$ 6.300,00 no valor cheio. Regras: o desconto vale para todas as formas de ingresso, é aplicado a partir da confirmação da matrícula e vale só para o 1º semestre de 2027. Para continuar nos semestres seguintes, o aluno pede a renovação a cada semestre, com comprovação. A renovação não é automática e o valor dos semestres seguintes depende dessa análise. O desconto é perdido no mês em que a mensalidade for paga depois do vencimento e não vale junto com programas governamentais com regras próprias. A inscrição é gratuita e o edital não prevê taxa de matrícula: a matrícula se confirma com a 1ª mensalidade e a assinatura do contrato. Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio até G12 e G7; com link da LP, também até G6.
- Chamada até o desbloqueio de G6: "Quer se inscrever? Responda este e-mail e o time de Goiânia te ajuda."
- Nota (não vai ao candidato): sem dia de vencimento e sem reajuste até a Ufape confirmar o Edital 004/2026.
- Follow-up: G2-L4 (WhatsApp, D8).
- Opt-in e saída: FE (rodapé do G2).

### G2-L4 (WhatsApp, D8): dúvidas de quem decide junto, incluindo responsáveis

- Canal: WhatsApp automático (template grad_ped_lead_familia_v1; variável: {primeiro_nome})
- Objetivo: dar à família ou a quem apoia a decisão as respostas de que precisa
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Se alguém da sua família participa da decisão, pode encaminhar esta mensagem.
- Primeira linha B: Oi, {primeiro_nome}. O que quem decide junto precisa saber sobre a Pedagogia da Ufape.
- Gancho: A decisão fica mais segura com a conta inteira.
- Corpo: "Pontos para quem decide junto: inscrição gratuita; se o candidato for menor de idade, a inscrição e a matrícula precisam do aceite do representante legal; mensalidade: {LD-PED} Desistir antes de começar tem devolução de 80% do valor pago, se pedida até 2 dias antes das aulas (20/02/2027); se a turma tiver menos de 30 matriculados, a Ufape pode cancelar a oferta e devolve a 1ª parcela; ato autorizativo: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). Quer conversar com o time de Goiânia? É só responder. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda esta mensagem para falar com o time."
- Bloqueio: BLOQUEADO para envio até G12 e G7. Sem botão da LP no template até G6.
- Follow-up: G2-L5 (e-mail, D12).
- Opt-in e saída: FW.

### G2-L5 (e-mail, D12): o que se estuda e como o curso é autorizado

(A aula aberta de Pedagogia, proposta P9, não existe: não há versão condicional a oferecer.)

- Canal: e-mail
- Objetivo: mostrar o curso de forma verificável e levar à inscrição
- Segmento: lead sem inscrição, adulto
- Assunto A: Pedagogia na Ufape: o que se estuda e como o curso é autorizado
- Assunto B: Antes de se inscrever: prática docente, estágio e ato autorizativo
- Texto de pré-visualização: Matriz e portaria, com a fonte.
- Gancho: Três coisas que dá para conferir antes de decidir.
- Corpo: "Olá, {primeiro_nome}. 1) O foco: docência na Educação Infantil e nos anos iniciais do Ensino Fundamental e gestão educacional. 2) A matriz: Prática Docente e Projeto Integrador desde o 1º semestre, Educação Inclusiva, Letramento em Libras e estágio supervisionado a partir do 6º semestre. 3) A autorização: {BA} Presencial, noturno, em Goiânia. A inscrição é gratuita. Dúvidas: (62) 9420-1847."
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio com link da LP até G6.
- Chamada até o desbloqueio: "Quer se inscrever? Responda este e-mail."
- Nota (não vai ao candidato): foco e matriz da ficha do curso (contexto/cursos/graduacao/graduacao-em-pedagogia.md), conferidos pelo qa-c.
- Follow-up: G2-L6 (WhatsApp, D15).
- Opt-in e saída: FE (rodapé do G2).

### G2-L6 (WhatsApp, D15): objeção "EAD é mais barato" e "e depois do 1º semestre?"

- Canal: WhatsApp automático (template grad_ped_lead_ead_v1; variável: {primeiro_nome})
- Objetivo: comparar só por atributos verificáveis e responder à regra de renovação, sem depreciar ninguém
- Segmento: lead sem inscrição, adulto
- Primeira linha A: Oi, {primeiro_nome}. Comparando com a Pedagogia a distância? Aqui vai o que dá para conferir.
- Primeira linha B: Oi, {primeiro_nome}. Uma pergunta justa antes de decidir: e depois do 1º semestre?
- Gancho: Cada formato serve a uma rotina. Estas são as informações da Ufape.
- Corpo: "Na Faculdade UFAPE, a Pedagogia é presencial, à noite, em Goiânia, com Prática Docente desde o 1º semestre. Pelo edital, até 30% da carga horária pode ser oferecida a distância. Mensalidade: {LD-PED} A renovação não é automática e o valor dos semestres seguintes depende dessa análise. Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Quer que o time explique? Responda QUERO."
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): Prática Docente desde o 1º semestre conferida na ficha do curso. Sem reajuste até a Ufape confirmar o Edital 004/2026.
- Follow-up: G2-L7 (e-mail, D20).
- Opt-in e saída: FW.

### G2-L7 (e-mail, D20): lembrete com o resumo

- Canal: e-mail
- Objetivo: lembrar o caminho e perguntar o que falta para decidir
- Segmento: lead sem inscrição, sem resposta, adulto
- Assunto A: Sua inscrição gratuita no Processo Seletivo 2027.1 de Pedagogia
- Assunto B: Resumo em 6 linhas: como entrar na Pedagogia da Ufape
- Texto de pré-visualização: Redação online, Enem, desconto do 1º semestre e matrícula.
- Gancho: Se faltou alguma resposta, é só dizer qual.
- Corpo: "Olá, {primeiro_nome}. Resumo: inscrição gratuita; redação online sem dia marcado (eliminatória, nota mínima 5,0) ou Enem com média de 300 pontos ou mais, de 2010 em diante; resultado no site; matrícula a partir de 2 dias depois, com a 1ª mensalidade e a assinatura digital; aulas a partir de 22/02/2027. Mensalidade: {LD-PED} O que falta para você decidir? Responda este e-mail com a sua dúvida. Edital de ingresso: {link_edital_vestibular}. {BM}"
- Chamada para ação: "Fazer minha inscrição gratuita" ({link_lp_utm})
- Bloqueio: BLOQUEADO para envio até G12 e G7; com link da LP, também até G6.
- Chamada até o desbloqueio de G6: a própria pergunta do corpo ("Responda este e-mail com a sua dúvida").
- Follow-up: nenhum; "sem engajamento" e encerra.
- Opt-in e saída: FE (rodapé do G2).

## G2-C. Régua do inscrito até a redação feita

Toques: R1 (D0), R2 (D2), R3 (D5), R4 (D9), R5 (D14); base existente entra pelo G2-AT e, sem avanço, em R3. Objetivo, segmento (adulto) e follow-up como no G1-C, com o contato (62) 9420-1847 e o Edital nº 004/2026. Texto de cada um:

### G2-R1 (e-mail, D0)
- Canal: e-mail (serviço, fora do teto D16); FE (rodapé do G2)
- Assunto A: Inscrição recebida: veja o que fazer agora no Processo Seletivo 2027.1
- Assunto B: {primeiro_nome}, sua inscrição na Pedagogia foi recebida. Próximo passo: redação ou Enem
- Texto de pré-visualização: Redação online sem dia marcado, ou nota do Enem com média mínima de 300 pontos (edições de 2010 em diante).
- Gancho: Sua inscrição entrou. Agora é escolher a avaliação.
- Corpo: "Olá, {primeiro_nome}. Recebemos a sua inscrição em Pedagogia noturno, Goiânia, Processo Seletivo 2027.1. {BC} O que vem depois: {BX} {BM} Dúvidas: (62) 9420-1847."
- Chamada para ação: "Acessar minha inscrição" ({link_area_candidato})
- Follow-up: G2-R2.

### G2-R2 (WhatsApp, D2)
- Template: grad_ped_inscrito_passo_v1 ({primeiro_nome}, {link_area_candidato}); FW
- Primeira linha A: Oi, {primeiro_nome}. Sua inscrição foi recebida. Quer ajuda para fazer a redação?
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE de Goiânia. O próximo passo é a redação ou o Enem.
- Gancho: Sem dia marcado: no seu ritmo.
- Corpo: "Para Pedagogia noturno: faça a redação online quando puder (eliminatória, nota mínima 5,0) ou envie sua nota do Enem (média de 300 pontos ou mais, de 2010 em diante). O passo a passo está na área do candidato. Se algo não funcionar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Acessar minha inscrição: {link_area_candidato}"
- Follow-up: G2-R3.

### G2-R3 (e-mail, D5)
- Canal: e-mail; FE (rodapé do G2)
- Assunto A: Redação e Enem no Processo Seletivo da Ufape: as dúvidas respondidas
- Assunto B: Posso fazer a redação de casa? Vale o Enem antigo? Respostas do edital
- Texto de pré-visualização: Cada resposta vem do edital do Processo Seletivo 2027.1.
- Gancho: Respostas curtas, com a fonte.
- Corpo: "Olá, {primeiro_nome}. Posso fazer a redação de casa? A prova é online. Tem data marcada? Não: você faz a qualquer momento depois da inscrição. Reprovo se tirar menos de 5,0? A redação é eliminatória, com nota mínima 5,0. Vale o Enem de anos atrás? Vale a média aritmética de 300 pontos ou mais, de qualquer edição a partir de 2010. Quero transferência ou já tenho outro diploma? Há transferência externa e ingresso de diplomado, só depois dos ingressantes por redação e Enem: fale com o time. Edital: {link_edital_vestibular}."
- Chamada para ação: "Fazer minha redação ou enviar o Enem" ({link_area_candidato})
- Nota (não vai ao candidato): [CONFIRMAR se há nova tentativa, como a média é calculada e como a nota é enviada.]
- Follow-up: G2-R4.

### G2-R4 (WhatsApp, D9)
- Template: grad_ped_inscrito_ajuda_v1 ({primeiro_nome}); FW
- Primeira linha A: Oi, {primeiro_nome}. O que está faltando para você fazer a redação?
- Primeira linha B: Oi, {primeiro_nome}. Podemos ajudar com a sua redação ou com o Enem?
- Gancho: Uma resposta de uma palavra já ajuda.
- Corpo: "Responda com o número: 1) não sei por onde começar; 2) prefiro usar a nota do Enem; 3) tenho dúvida sobre o valor; 4) outro motivo. O time de Goiânia te responde no horário comercial. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda com o número da sua situação."
- Follow-up: G2-R5.

### G2-R5 (e-mail, D14)
- Canal: e-mail; FE (rodapé do G2)
- Assunto A: Depois da redação: resultado, matrícula e valor, passo a passo
- Assunto B: O que acontece depois que você faz a redação do Processo Seletivo
- Texto de pré-visualização: Do resultado no site à primeira mensalidade, sem surpresas.
- Gancho: Saber o que vem depois ajuda a dar o primeiro passo.
- Corpo: "Olá, {primeiro_nome}. {BX} Valor: {BP-PED} E depois do 1º semestre? {BD-PED} A inscrição é gratuita e o edital não prevê taxa de matrícula. {BM}"
- Chamada para ação: "Fazer minha redação ou enviar o Enem" ({link_area_candidato})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: tarefa humana em D21.

## G2-D. Régua do aprovado até a matrícula

Mesmas regras, tempos e condições do G1-D (A1 em D0, A2 em D+2, A3 em D+3, A5 em D+7, A6 em D+14 ou a partir de 01/02/2027; representante legal de menor: A1-R, A4-R, A3-R e A6-R). Só entra quem tem status "aprovado" no sistema.

### G2-A1 (e-mail, D0)
- Canal: e-mail (serviço, fora do teto D16); FE (rodapé do G2)
- Assunto A: Seu resultado do Processo Seletivo 2027.1 está no site
- Assunto B: {primeiro_nome}, parabéns pela aprovação: veja como fazer a matrícula
- Texto de pré-visualização: A matrícula abre a partir de 2 dias depois da publicação do resultado.
- Gancho: Você passou. Agora vêm 3 passos curtos.
- Corpo: "Olá, {primeiro_nome}. Parabéns pela aprovação em Pedagogia noturno, Goiânia, da Faculdade UFAPE. Resultado: {link_resultado}. Matrícula: eletrônica, a partir de {data_matricula} (2 dias depois da publicação). Para confirmar: (1) pagar a 1ª mensalidade; (2) assinar o contrato digitalmente; (3) enviar os documentos pela plataforma de matrícula digital em até 30 dias. Antes de pagar, o próximo e-mail traz o valor e todas as condições. {BM} As aulas começam em 22/02/2027. Dúvidas: (62) 9420-1847."
- Chamada para ação: "Ver meu resultado" ({link_resultado})
- Nota (não vai ao candidato): [CONFIRMAR de quando contam os 30 dias.]
- Follow-up: G2-A2.

### G2-A2 (WhatsApp, D+2)
- Template: grad_ped_aprovado_matricula_v1 ({primeiro_nome}, {link_matricula}); FW
- Primeira linha A: Oi, {primeiro_nome}. Sua matrícula na Pedagogia da Ufape já está aberta.
- Primeira linha B: Oi, {primeiro_nome}, aqui é da Faculdade UFAPE de Goiânia. Hoje abre a matrícula do seu curso.
- Gancho: São 3 passos.
- Corpo: "Para confirmar a matrícula: 1) pague a 1ª mensalidade; 2) assine o contrato digitalmente; 3) envie os documentos na plataforma em até 30 dias. Valor: {LD-PED} As aulas começam em 22/02/2027. Dúvida antes de pagar? Responda aqui. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Fazer minha matrícula: {link_matricula}"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: G2-A3.

### G2-A3 (e-mail, D+3)
- Canal: e-mail; FE (rodapé do G2)
- Assunto A: Antes de se matricular: desconto, renovação e cancelamento em linguagem simples
- Assunto B: Sua matrícula na Ufape: o que você paga, quando e o que acontece se desistir
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e devolução de 80%.
- Gancho: A decisão fica mais segura com todas as regras na mesa.
- Corpo: "Olá, {primeiro_nome}. O que você paga: {BP-PED} E depois do 1º semestre? {BD-PED} Primeira mensalidade: {valor_primeira_mensalidade}. O edital não prevê taxa de matrícula. Se você desistir antes de começar: devolução de 80% do valor pago, se o cancelamento for pedido até 2 dias antes do início das aulas (20/02/2027). Se a turma não formar: precisa de pelo menos 30 matriculados; abaixo disso, a Ufape pode cancelar a oferta e devolve a 1ª parcela. {BM} Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Fazer minha matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR se a 1ª mensalidade já sai com o desconto; sem a resposta, a linha sai. CONFIRMAR a data de decisão da turma mínima, pedido G4.]
- Follow-up: G2-A5.

### G2-A5 (WhatsApp, D+7)
- Template: grad_ped_aprovado_trava_v1 ({primeiro_nome}); FW
- Primeira linha A: Oi, {primeiro_nome}. A sua matrícula ainda não foi concluída. Podemos ajudar?
- Primeira linha B: Oi, {primeiro_nome}. Algo travou na sua matrícula?
- Gancho: Se travou em um ponto, a gente resolve com você.
- Corpo: "Responda com o número: 1) pagamento da 1ª mensalidade; 2) contrato ou assinatura digital; 3) documentos; 4) dúvida sobre o valor ou o desconto; 5) outro motivo. O time de Goiânia te responde no horário comercial. As aulas começam em 22/02/2027. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda com o número da sua situação."
- Follow-up: G2-A6.

### G2-A6 (e-mail, D+14 ou a partir de 01/02/2027)
- Canal: e-mail; FE (rodapé do G2)
- Assunto A: Aulas começam em 22/02/2027: como concluir a sua matrícula
- Assunto B: {primeiro_nome}, o que falta para a sua matrícula na Ufape
- Texto de pré-visualização: Passos, regras e quem chamar. Só os fatos.
- Gancho: Para começar em 22/02/2027, faltam estes passos.
- Corpo: "Olá, {primeiro_nome}. As aulas de Pedagogia noturno começam em 22/02/2027. Para participar, a matrícula precisa estar confirmada: 1ª mensalidade paga e contrato assinado. O cancelamento com devolução de 80% vale se pedido até 2 dias antes do início das aulas (20/02/2027). Valor: {LD-PED} Se algo o impede, responda este e-mail e o time de Goiânia ajuda. {BM}"
- Chamada para ação: "Concluir minha matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): revisar em 25/01/2027 com números reais; nenhuma frase sobre vagas entra sem número real.
- Follow-up: nenhum; "sem engajamento" e encerra.

## G2-E. Régua do matriculado até 22/02/2027

Mesmos toques e regras do G1-E: M1 (D0), M2 (D+5), M3 (D+14), M4 (antes do vencimento, só depois da confirmação), M5 (15/02/2027). Cobrança e contrato são do financeiro e da secretaria.

### G2-M1 (e-mail, D0)
- Canal: e-mail (serviço, fora do teto D16); FE (rodapé do G2)
- Assunto A: Matrícula confirmada: o que acontece até as aulas, em 22/02/2027
- Assunto B: {primeiro_nome}, sua matrícula na Ufape está confirmada. Veja os próximos passos
- Texto de pré-visualização: Documentos em até 30 dias, início das aulas e contatos.
- Gancho: Matrícula feita. Agora, o que falta.
- Corpo: "Olá, {primeiro_nome}. Sua matrícula em Pedagogia noturno, Goiânia, está confirmada. O que fazer: enviar os documentos pela plataforma de matrícula digital em até 30 dias. Se precisar cancelar, a devolução de 80% vale se o pedido for feito até 20/02/2027. As aulas começam em 22/02/2027. Dúvidas: Vendas Goiânia, (62) 9420-1847; pagamento: financeiro@intercursos.com.br ou (11) 94525-3730 (WhatsApp)."
- Chamada para ação: "Enviar meus documentos" ({link_matricula})
- Nota (não vai ao candidato): sem dia de vencimento até a Ufape confirmar o Edital 004/2026.
- Follow-up: G2-M2.

### G2-M2 (WhatsApp, D+5)
- Template: grad_ped_matriculado_docs_v1 ({primeiro_nome}, {link_matricula}); FW
- Primeira linha A: Oi, {primeiro_nome}. Lembrete: os documentos da matrícula entram pela plataforma, em até 30 dias.
- Primeira linha B: Oi, {primeiro_nome}. Faltam documentos na sua matrícula na Ufape?
- Gancho: Enviar agora evita correria depois.
- Corpo: "Os documentos da matrícula são enviados pela plataforma de matrícula digital, em até 30 dias. A lista está na plataforma. As aulas começam em 22/02/2027. Se tiver dificuldade, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Enviar documentos: {link_matricula}"
- Nota (não vai ao candidato): [CONFIRMAR a lista de documentos.]
- Follow-up: G2-M3.

### G2-M3 (e-mail, D+14)
- Canal: e-mail; FE (rodapé do G2)
- Assunto A: Seu 1º semestre de Pedagogia na Ufape: o que esperar
- Assunto B: Antes das aulas de 22/02/2027: o que você já pode saber
- Texto de pré-visualização: Início, turno e o que se estuda.
- Gancho: Como vai ser o começo.
- Corpo: "Olá, {primeiro_nome}. Início das aulas: 22/02/2027, em Goiânia, no turno noturno, com duração de 4 anos. Desde o 1º semestre há Prática Docente e Projeto Integrador. Local do primeiro dia, horários e calendário: {local_primeiro_dia}, {horarios}, {calendario}. Dúvidas: (62) 9420-1847."
- Chamada para ação: "Falar com o time de Goiânia" (WhatsApp (62) 9420-1847)
- Nota (não vai ao candidato): componentes do 1º semestre conferidos na ficha do curso pelo qa-c. [CONFIRMAR local, horários e calendário; sem a confirmação, a frase vira "Local, horários e calendário chegam por e-mail antes do início das aulas".]
- Follow-up: G2-M4, quando desbloqueado; senão, G2-M5.

### G2-M4 (WhatsApp, antes do vencimento)
- Template: grad_ped_matriculado_mensalidade_v1 ({primeiro_nome}, {data_vencimento}); FW
- Primeira linha A: Oi, {primeiro_nome}. A sua mensalidade vence em {data_vencimento}.
- Primeira linha B: Oi, {primeiro_nome}. Um lembrete para você não perder o desconto do mês.
- Gancho: O desconto é perdido no mês em que a mensalidade é paga depois do vencimento.
- Corpo: "A sua mensalidade vence em {data_vencimento}. Se for paga depois do vencimento, o desconto do edital é perdido naquele mês. O seu desconto: {LD-PED} Dúvidas sobre boleto ou pagamento: financeiro@intercursos.com.br ou (11) 94525-3730 (WhatsApp). Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Falar com o financeiro: (11) 94525-3730"
- Bloqueio: BLOQUEADO para envio até a Ufape confirmar o vencimento da Pedagogia (Edital 004/2026) e até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR o calendário das 6 mensalidades e quem envia.] Serviço só se o cmo aprovar (seção 0.7).
- Follow-up: nenhum.

### G2-M5 (e-mail, 15/02/2027)
- Canal: e-mail (serviço, fora do teto D16); FE (rodapé do G2)
- Assunto A: Segunda-feira, 22/02/2027: começam as suas aulas de Pedagogia
- Assunto B: {primeiro_nome}, sua semana de início na Faculdade UFAPE
- Texto de pré-visualização: Local, horário e documentos pendentes, num e-mail só.
- Gancho: Falta uma semana.
- Corpo: "Olá, {primeiro_nome}. As aulas de Pedagogia noturno começam em 22/02/2027. Documentos pendentes: {docs_pendentes} (enviar em {link_matricula}). Local e horário do primeiro dia: {local_primeiro_dia}, {horarios}. Lembrete de regra: o cancelamento com devolução de 80% vale se pedido até 20/02/2027. Contato: (62) 9420-1847."
- Chamada para ação: "Enviar os documentos que faltam" ({link_matricula}); sem pendência, "Falar com o time de Goiânia"
- Nota (não vai ao candidato): revisar em 25/01/2027 antes do envio. [CONFIRMAR local e horário.]
- Follow-up: nenhum.

## G2-V. Versões para o representante legal (-R), por extenso

Todas com consentimento do representante legal registrado (seção 0.5), rodapé do G2 nos e-mails e "Para não receber mais mensagens, responda SAIR" nos WhatsApp. Nenhuma frase se dirige ao menor.

### G2-AT1-R (e-mail)
- Assunto A: Processo Seletivo 2027.1 de {nome_candidato}: o próximo passo é a redação ou o Enem
- Assunto B: Para o representante legal: como {nome_candidato} faz a redação online
- Texto de pré-visualização: Sem dia marcado. O aceite do representante legal também é necessário na matrícula.
- Gancho: Você consta como representante legal de {nome_candidato}, que já se inscreveu.
- Corpo: "Olá. {nome_candidato} se inscreveu no Processo Seletivo 2027.1 de Pedagogia noturno, em Goiânia, da Faculdade UFAPE. A inscrição é gratuita e, como o candidato é menor de idade, ela exigiu o aceite do representante legal. Esse aceite também é necessário na matrícula. Para seguir, {nome_candidato} precisa fazer a avaliação: {BC} O que vem depois: {BX} Antes de qualquer pagamento, o time explica o valor e todas as condições. Dúvidas: responda este e-mail ou fale com o time de Goiânia em (62) 9420-1847."
- Chamada para ação: "Ver o passo a passo" ({link_area_candidato})
- Follow-up: G2-AT2-R.

### G2-AT2-R (WhatsApp)
- Template: grad_ped_ativacao_redacao_resp_v1 ({nome_candidato}, {link_area_candidato})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE de Goiânia. Sobre o Processo Seletivo de {nome_candidato}: falta a redação ou o Enem.
- Primeira linha B: Olá. Você é o representante legal de {nome_candidato}? Temos um aviso sobre a inscrição.
- Corpo: "{nome_candidato} se inscreveu em Pedagogia noturno, em Goiânia. Para seguir, falta a redação online (sem dia marcado, eliminatória, nota mínima 5,0) ou a nota do Enem (média de 300 pontos ou mais, edições de 2010 em diante). Como o candidato é menor de idade, o aceite do representante legal também é necessário na matrícula. Dúvidas? Responda esta mensagem e o time de Goiânia fala com você. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver o passo a passo: {link_area_candidato}"
- Follow-up: nenhum WhatsApp automático (não existe AT3-R). Quem responde vai ao time.

### G2-L2-R (WhatsApp)
- Template: grad_ped_lead_enem_resp_v1 ({nome_candidato}, {link_lp_utm})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE de Goiânia. Esta mensagem é para o representante legal de {nome_candidato}: as duas formas de entrar na Pedagogia.
- Primeira linha B: Olá. {nome_candidato} pediu informações sobre a Pedagogia da Ufape em Goiânia. Veja como funciona o ingresso.
- Corpo: "A inscrição é gratuita e há duas formas de entrar: nota do Enem, com média de 300 pontos ou mais, de qualquer edição a partir de 2010; ou redação online, sem dia marcado, eliminatória, com nota mínima 5,0. Como {nome_candidato} é menor de idade, a inscrição e a matrícula precisam do seu aceite como representante legal. As aulas começam em 22/02/2027. Dúvidas? Responda esta mensagem e o time de Goiânia fala com você. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver como se inscrever: {link_lp_utm}"
- Bloqueio: BLOQUEADO para envio com link da LP até G6.
- Chamada até o desbloqueio: "Responda esta mensagem para falar com o time."
- Follow-up: nenhum automático.

### G2-L4-R (WhatsApp)
- Template: grad_ped_lead_familia_resp_v1 ({nome_candidato})
- Primeira linha A: Olá. Esta mensagem é para o representante legal de {nome_candidato}: o que você precisa saber sobre a Pedagogia da Ufape.
- Primeira linha B: Olá, aqui é da Faculdade UFAPE de Goiânia. Respostas para o representante legal de {nome_candidato}.
- Corpo: "Pontos para quem decide: como {nome_candidato} é menor de idade, a inscrição e a matrícula precisam do seu aceite como representante legal; inscrição gratuita; matrícula com a 1ª mensalidade e a assinatura digital do contrato; mensalidade: {LD-PED} Desistir antes de começar tem devolução de 80% do valor pago, se pedida até 2 dias antes das aulas (20/02/2027); se a turma tiver menos de 30 matriculados, a Ufape pode cancelar a oferta e devolve a 1ª parcela; ato autorizativo: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). Se preferir, o time conversa por telefone ou por escrito, de segunda a sexta, das 9h às 18h. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Responda esta mensagem para falar com o time"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Follow-up: nenhum automático.

### G2-R1-R (e-mail, serviço)
- Assunto A: Inscrição de {nome_candidato} recebida: o próximo passo é a redação ou o Enem
- Assunto B: Para o representante legal: como {nome_candidato} segue no Processo Seletivo 2027.1
- Texto de pré-visualização: Redação online sem dia marcado ou Enem com média mínima de 300 pontos (edições de 2010 em diante).
- Gancho: A inscrição de {nome_candidato} entrou. Agora é a avaliação.
- Corpo: "Olá. Recebemos a inscrição de {nome_candidato} em Pedagogia noturno, Goiânia, Processo Seletivo 2027.1, da Faculdade UFAPE. Como o candidato é menor de idade, a inscrição exigiu o aceite do representante legal, que também é necessário na matrícula. Para seguir, {nome_candidato} faz a avaliação: {BC} O que vem depois: {BX} Antes de qualquer pagamento, o time explica o valor e todas as condições. Dúvidas: (62) 9420-1847."
- Chamada para ação: "Ver o passo a passo" ({link_area_candidato})
- Follow-up: G2-R2-R.

### G2-R2-R (WhatsApp)
- Template: grad_ped_inscrito_passo_resp_v1 ({nome_candidato}, {link_area_candidato})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE de Goiânia. A inscrição de {nome_candidato} foi recebida: o próximo passo é a redação ou o Enem.
- Primeira linha B: Olá. Você é o representante legal de {nome_candidato}? Temos o passo a passo da avaliação.
- Corpo: "Para Pedagogia noturno, {nome_candidato} faz a redação online quando puder (eliminatória, nota mínima 5,0) ou envia a nota do Enem (média de 300 pontos ou mais, de 2010 em diante). O passo a passo está na área do candidato. Como o candidato é menor de idade, o seu aceite como representante legal também é necessário na matrícula. Se algo não funcionar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Ver o passo a passo: {link_area_candidato}"
- Follow-up: nenhum automático.

### G2-A1-R (e-mail, serviço)
- Assunto A: O resultado de {nome_candidato} no Processo Seletivo 2027.1 está no site
- Assunto B: Para o representante legal: como fazer a matrícula de {nome_candidato}
- Texto de pré-visualização: A matrícula é eletrônica, abre a partir de 2 dias depois do resultado e precisa do seu aceite.
- Gancho: O resultado saiu. A matrícula de {nome_candidato} precisa de você.
- Corpo: "Olá. Parabéns pela aprovação de {nome_candidato} em Pedagogia noturno, Goiânia, da Faculdade UFAPE. Resultado: {link_resultado}. Matrícula: eletrônica, a partir de {data_matricula} (2 dias depois da publicação). Como {nome_candidato} é menor de idade, a matrícula precisa do aceite do representante legal. Para confirmar: (1) pagar a 1ª mensalidade; (2) assinar o contrato digitalmente; (3) enviar os documentos pela plataforma de matrícula digital em até 30 dias. Antes de pagar, o próximo e-mail traz o valor e todas as condições. As aulas começam em 22/02/2027. Dúvidas: (62) 9420-1847."
- Chamada para ação: "Ver o resultado" ({link_resultado})
- Nota (não vai ao candidato): [CONFIRMAR como o aceite é dado e de quando contam os 30 dias.]
- Follow-up: G2-A4-R (D+2).

### G2-A4-R (WhatsApp, D+2, versão do A2)
- Template: grad_ped_aprovado_resp_v1 ({nome_candidato}, {link_matricula})
- Primeira linha A: Olá. Esta mensagem é para o representante legal de {nome_candidato}: a matrícula já pode ser feita.
- Primeira linha B: Olá, aqui é da Faculdade UFAPE de Goiânia. Sobre a matrícula de {nome_candidato}, o aceite do representante legal é necessário.
- Gancho: A matrícula de menor de idade precisa de você.
- Corpo: "O aceite do representante legal é necessário na matrícula de candidato menor de idade. A matrícula de {nome_candidato} em Pedagogia noturno, em Goiânia, se confirma com a 1ª mensalidade e a assinatura digital do contrato; os documentos entram em até 30 dias. Valor: {LD-PED} Se desistir até 20/02/2027, a devolução é de 80% do valor pago. O time de Goiânia explica por telefone, se preferir: (62) 9420-1847. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Falar com o time: responda esta mensagem"
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): [CONFIRMAR como o aceite é dado.]
- Follow-up: G2-A3-R.

### G2-A3-R (e-mail, D+3)
- Assunto A: Antes da matrícula de {nome_candidato}: valor, renovação e cancelamento
- Assunto B: Para o representante legal: o que se paga, quando e o que acontece em caso de desistência
- Texto de pré-visualização: Valor cheio, valor com desconto, validade e devolução de 80%.
- Gancho: Todas as regras na mesa antes de qualquer pagamento.
- Corpo: "Olá. O que se paga: {BP-PED} E depois do 1º semestre? {BD-PED} Primeira mensalidade: {valor_primeira_mensalidade}. O edital não prevê taxa de matrícula. Aceite: como {nome_candidato} é menor de idade, a matrícula precisa do aceite do representante legal. Desistência antes de começar: devolução de 80% do valor pago, se o cancelamento for pedido até 2 dias antes do início das aulas (20/02/2027). Se a turma não formar: precisa de pelo menos 30 matriculados; abaixo disso, a Ufape pode cancelar a oferta e devolve a 1ª parcela. Dúvidas: (62) 9420-1847. Edital do desconto: {link_edital_desconto}."
- Chamada para ação: "Ir para a matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): as mesmas do G2-A3.
- Follow-up: G2-A6-R.

### G2-A6-R (e-mail, D+14)
- Assunto A: Aulas começam em 22/02/2027: o que falta na matrícula de {nome_candidato}
- Assunto B: Para o representante legal: como concluir a matrícula de {nome_candidato}
- Texto de pré-visualização: Passos, regras e quem chamar. Só os fatos.
- Gancho: Para começar em 22/02/2027, faltam estes passos.
- Corpo: "Olá. As aulas de Pedagogia noturno começam em 22/02/2027. Para {nome_candidato} participar, a matrícula precisa estar confirmada: 1ª mensalidade paga e contrato assinado, com o aceite do representante legal. O cancelamento com devolução de 80% vale se pedido até 2 dias antes do início das aulas (20/02/2027). Valor: {LD-PED} Se algo impede a matrícula, responda este e-mail e o time de Goiânia ajuda."
- Chamada para ação: "Concluir a matrícula" ({link_matricula})
- Bloqueio: BLOQUEADO para envio até G12 e G7.
- Nota (não vai ao candidato): revisar em 25/01/2027 com números reais.
- Follow-up: nenhum.

### G2-M1-R (e-mail, serviço)
- Assunto A: Matrícula de {nome_candidato} confirmada: o que acontece até 22/02/2027
- Assunto B: Para o representante legal: próximos passos da matrícula de {nome_candidato}
- Texto de pré-visualização: Documentos em até 30 dias, início das aulas e contatos.
- Gancho: Matrícula feita. Agora, o que falta.
- Corpo: "Olá. A matrícula de {nome_candidato} em Pedagogia noturno, Goiânia, está confirmada. O que fazer: enviar os documentos pela plataforma de matrícula digital em até 30 dias. Se precisar cancelar, a devolução de 80% vale se o pedido for feito até 20/02/2027. As aulas começam em 22/02/2027. Dúvidas: Vendas Goiânia, (62) 9420-1847; pagamento: financeiro@intercursos.com.br ou (11) 94525-3730 (WhatsApp)."
- Chamada para ação: "Enviar os documentos" ({link_matricula})
- Follow-up: G2-M2-R.

### G2-M2-R (WhatsApp)
- Template: grad_ped_matriculado_docs_resp_v1 ({nome_candidato}, {link_matricula})
- Primeira linha A: Olá, aqui é da Faculdade UFAPE de Goiânia. Lembrete para o representante legal de {nome_candidato}: os documentos da matrícula entram pela plataforma, em até 30 dias.
- Primeira linha B: Olá. Faltam documentos na matrícula de {nome_candidato}?
- Corpo: "Os documentos da matrícula de {nome_candidato} são enviados pela plataforma de matrícula digital, em até 30 dias. A lista está na plataforma. As aulas começam em 22/02/2027. Se tiver dificuldade para enviar, responda aqui e o time ajuda. Para não receber mais mensagens, responda SAIR."
- Chamada para ação: "Enviar documentos: {link_matricula}"
- Follow-up: G2-M5-R.

### G2-M5-R (e-mail, 15/02/2027)
- Canal: e-mail (serviço, fora do teto D16)
- Assunto A: Segunda-feira, 22/02/2027: começam as aulas de {nome_candidato}
- Assunto B: Para o representante legal: a semana de início de {nome_candidato}
- Texto de pré-visualização: Local, horário e documentos pendentes, num e-mail só.
- Gancho: Falta uma semana.
- Corpo: "Olá. As aulas de Pedagogia noturno de {nome_candidato} começam em 22/02/2027. Documentos pendentes: {docs_pendentes} (enviar em {link_matricula}). Local e horário do primeiro dia: {local_primeiro_dia}, {horarios}. Lembrete de regra: o cancelamento com devolução de 80% vale se pedido até 20/02/2027. Contato: (62) 9420-1847."
- Chamada para ação: "Enviar os documentos que faltam" ({link_matricula}); sem pendência, "Falar com o time de Goiânia"
- Nota (não vai ao candidato): revisar em 25/01/2027. [CONFIRMAR local e horário.]
- Follow-up: nenhum.

---

## 4. Respostas prontas para o time de captação

Como usar: o time responde só com o que está abaixo. Pergunta fora da lista: "Vou confirmar com a equipe e te retorno" e registra no CRM; nunca improvisar dado de curso, preço, prazo, ato ou regra. Nunca prometer aprovação, vaga, emprego ou valor dos semestres seguintes. Nunca citar nota do MEC. Nunca dizer "últimas vagas". Falar com o representante legal quando o candidato for menor de idade. Tom: simples e direto, "você". Fontes entre parênteses.

Respostas de preço (marcadas "BLOQUEADO até G12 e G7" abaixo): só podem ser usadas depois de G12 e G7. Até lá, o time diz "Vou confirmar o valor com a equipe e te retorno" e registra no CRM.

### 4.1 Regras iguais para G1 e G2 (os editais 002 e 004/2026 têm as mesmas regras)

| Pergunta | Resposta | Fonte |
|---|---|---|
| Quando é a prova? | Não há data de prova. A redação é online e pode ser feita a qualquer momento depois da inscrição. | Editais 002 e 004/2026 |
| Tem data final de inscrição? | O edital não traz data final. A matrícula só pode acontecer antes das aulas, que começam em 22/02/2027, e a matrícula abre a partir de 2 dias depois do resultado. Vou confirmar se há alguma data interna e te aviso. | Editais; [CONFIRMAR G4] |
| A inscrição é gratuita? | Sim, gratuita, pelo site ou presencialmente, de segunda a sexta, das 9h às 18h. | Editais |
| Como funciona a redação? | É online, eliminatória, com nota mínima 5,0. O passo a passo está na área do candidato. Sobre tema, tempo de prova e nova tentativa, vou confirmar. | Editais; [CONFIRMAR] |
| Como funciona o Enem? | Vale a média aritmética de 300 pontos ou mais, de qualquer edição a partir de 2010. Como enviar a nota e como a média é calculada: vou confirmar. | Editais; [CONFIRMAR] |
| Se eu não passar na redação? | A redação é eliminatória. Quanto a uma nova tentativa ou ao uso do Enem, vou confirmar com a equipe. Não prometo aprovação. | Editais; [CONFIRMAR] |
| Quando sai o resultado? | O resultado é publicado no site. O prazo de divulgação eu confirmo com a equipe. | Editais; [CONFIRMAR] |
| Quando faço a matrícula? | A partir de 2 dias depois da publicação do resultado, de forma eletrônica. | Editais |
| O que confirma a matrícula? | O pagamento da 1ª mensalidade e a assinatura digital do contrato. Os documentos entram pela plataforma de matrícula digital em até 30 dias. | Editais |
| Tem taxa de matrícula? | O edital não prevê taxa de matrícula. A matrícula se confirma com a 1ª mensalidade. | Editais |
| A 1ª mensalidade já vem com desconto? | O desconto é aplicado a partir da confirmação da matrícula. Como a 1ª mensalidade é cobrada, vou confirmar o valor exato com o financeiro antes de você pagar. | Editais; [CONFIRMAR] |
| Quando começam as aulas? | Em 22/02/2027, para todas as formas de ingresso. | Editais |
| Quando vence a mensalidade? | Medicina Veterinária: no dia 10 de cada mês. Pedagogia: vou confirmar com o financeiro. Nos dois cursos, se a mensalidade for paga depois do vencimento, o desconto é perdido naquele mês. | Edital 002/2026; Editais 003/2026; [CONFIRMAR vencimento da Pedagogia no Edital 004/2026] |
| O desconto vale para o curso todo? | Não. Vale só para as 6 mensalidades do 1º semestre de 2027. Para continuar, a renovação é pedida a cada semestre, com comprovação, e não é automática. | Editais 003/2026 |
| E depois do 1º semestre? | Use o bloco BD-MV (Medicina Veterinária) ou BD-PED (Pedagogia): o valor dos semestres seguintes depende da análise da renovação. "Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação." BLOQUEADO até G12 e G7. | Editais 003/2026; oferta 0.3; [CONFIRMAR P1 e G12] |
| O desconto vale para quem entra pelo Enem? | Sim. Vale para todas as formas de ingresso. | Edital 003/2026 |
| Posso juntar o desconto com Prouni, Fies ou outro programa? | O desconto não vale junto com programas governamentais com regras próprias. Sobre programas específicos, não tenho informação confirmada; vou verificar com a equipe. | Edital 003/2026; [CONFIRMAR NO CATÁLOGO] |
| Quais as formas de pagamento? | Vou confirmar com o financeiro. | [CONFIRMAR NO CATÁLOGO: boleto, cartão, outros] |
| Quando perco o desconto? | Se a mensalidade for paga depois do vencimento no mês; se o curso deixar de ser ofertado; em transferência; no fim do semestre; com atraso de uma ou mais mensalidades; com interrupção dos estudos; ou se a turma tiver menos de 30 matrículas confirmadas até o início das aulas. | Edital 003/2026 |
| Posso desistir? Recebo de volta? | Se o cancelamento for pedido até 2 dias antes do início das aulas (até 20/02/2027), a devolução é de 80% do valor pago. | Editais |
| E se a turma não formar? | A turma precisa de pelo menos 30 matriculados. Abaixo disso, a Ufape pode cancelar a oferta e devolve a 1ª parcela. A data em que isso é decidido eu confirmo. Não usar como pressão de compra. | Editais; [CONFIRMAR G4] |
| Quantas vagas tem? | São 45 vagas no integral e 45 no noturno de Medicina Veterinária, e 80 na Pedagogia, conforme o edital. Não tenho o número de vagas restantes. | Editais; [CONFIRMAR] |
| O candidato é menor de idade. O que muda? | A inscrição e a matrícula precisam do aceite do representante legal. Falo com o representante legal. Como o aceite é dado na matrícula, vou confirmar o procedimento. | Editais; [CONFIRMAR] |
| Tem aula a distância? | O curso é presencial. Pelo edital, até 30% da carga horária pode ser oferecida a distância, como a lei permite. Quais disciplinas e em que semestres, vou confirmar com a coordenação. | Editais; [CONFIRMAR] |
| Posso transferir de outra faculdade ou entrar com outro diploma? | Há transferência externa e ingresso de diplomado, mas só depois dos ingressantes por redação e Enem. Posso abrir um pedido para a equipe analisar. | Edital 002/2026 |
| O curso é autorizado pelo MEC? Tem reconhecimento? Qual a nota do MEC? | Informo o ato autorizativo do curso (G1 ou G2, abaixo) e o credenciamento da faculdade. Sobre reconhecimento do curso, vou confirmar com a regulação antes de responder. Não informamos nota do MEC. | Catálogo; editais; [CONFIRMAR] |
| Que diploma eu recebo? | Medicina Veterinária: bacharelado. Pedagogia: licenciatura (Edital 004/2026). | Editais; catálogo |
| Posso falar com o coordenador? | Passo o pedido para a equipe. Nome da coordenação: [CONFIRMAR NO CATÁLOGO]. | [CONFIRMAR] |
| Quero cancelar a inscrição ou parar de receber mensagens. | Registrar o pedido na hora, encerrar o canal e confirmar uma vez. Pedido de exclusão de dados vai ao responsável pela LGPD [CONFIRMAR canal]. | LGPD |

### 4.2 Respostas próprias do G1 (Medicina Veterinária, São Paulo)

| Pergunta | Resposta | Fonte |
|---|---|---|
| Quanto custa o integral? | De R$ 10.000,00 por R$ 5.000,00 por mês, 50% de desconto, nas 6 mensalidades do 1º semestre de 2027 (R$ 30.000,00 no semestre, contra R$ 60.000,00 no valor cheio). Regras: use o BP-INT. BLOQUEADO até G12 e G7. | Catálogo; Edital 003/2026 |
| Quanto custa o noturno? | De R$ 10.000,00 por R$ 4.000,00 por mês, 60% de desconto, nas 6 mensalidades do 1º semestre de 2027 (R$ 24.000,00 no semestre, contra R$ 60.000,00 no valor cheio). Regras: use o BP-NOT. BLOQUEADO até G12 e G7. | Catálogo; Edital 003/2026 |
| Quanto tempo dura? Qual a carga horária? | Integral: 4 anos. Noturno: 5 anos. Carga horária de 4.195 h, mais 75 h de atividades complementares. Presencial, em São Paulo. | Catálogo |
| Qual o ato do curso? | Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). A Faculdade UFAPE de São Paulo é credenciada pela Portaria MEC nº 176, de 27/02/2025 (D.O.U. 28/02/2025). | Catálogo; editais |
| Como é o noturno? Posso trabalhar de dia? | As aulas são no período noturno e o curso dura 5 anos. O horário das atividades práticas e do estágio (9º e 10º semestres) eu confirmo; não prometo que seja compatível com trabalho. | Catálogo; [CONFIRMAR NO CATÁLOGO] |
| Quando é o estágio? | Estágio supervisionado nos 7º e 8º semestres (integral) e 9º e 10º semestres (noturno), conforme a matriz. | Ficha do curso |
| Quando começa a prática? | Já no 1º semestre, com Campos de Atuação do Médico Veterinário e Práticas Hospitalares, Projeto Extensionista I e Práticas Hospitalares, conforme a matriz. | Ficha do curso |
| A Ufape tem hospital veterinário? | Sim, a Ufape Clínica, hospital veterinário próprio. Como os alunos da graduação o usam em cada semestre, vou confirmar com a coordenação. | contexto/ufape-geral.md; [CONFIRMAR G11] |
| Quem são os professores? | Passo o pedido para a coordenação, que informa o corpo docente do curso. | [CONFIRMAR corpo docente da graduação] |
| Posso visitar a faculdade? | Você pode fazer a inscrição presencialmente, de segunda a sexta, das 9h às 18h, na Av. Nove de Julho, 3913 e 3939, Jardim Paulista, São Paulo. Sobre visita guiada, vou confirmar se existe. | Edital 002/2026; [CONFIRMAR P4] |
| Qual o contato? | Vendas São Paulo (11) 91366-9290 e secretaria (11) 97492-8443 (WhatsApp), de segunda a sexta, das 9h às 18h. | contexto/ufape-geral.md |

### 4.3 Respostas próprias do G2 (Pedagogia, Goiânia)

| Pergunta | Resposta | Fonte |
|---|---|---|
| Quanto custa? | De R$ 1.050,00 por R$ 525,00 por mês, 50% de desconto, nas 6 mensalidades do 1º semestre de 2027 (R$ 3.150,00 no semestre, contra R$ 6.300,00 no valor cheio). Regras: use o BP-PED. BLOQUEADO até G12 e G7. | Catálogo; Edital 003/2026 Goiânia |
| Quanto tempo dura? É presencial? | 4 anos, presencial, noturno, em Goiânia. | Catálogo |
| Qual a carga horária? | Vou confirmar com a secretaria e te passo. Não informo número até a Ufape confirmar. | [CONFIRMAR NO CATÁLOGO, G5] |
| Qual o ato do curso? | Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022). A Faculdade UFAPE de Goiânia é credenciada pela Portaria MEC nº 871, de 10/11/2022. | Catálogo; editais |
| EAD é mais barato. Por que escolher a Ufape? | Não comparo preço de outras instituições. Posso dizer o que a Ufape oferece: Pedagogia presencial, à noite, em Goiânia, com Prática Docente desde o 1º semestre, e R$ 525,00 por mês no 1º semestre de 2027 (de R$ 1.050,00, 50%), com renovação a cada semestre, com comprovação, e perda do desconto no mês pago depois do vencimento, nas regras do Programa de Desconto de Mensalidade 2027/1 Goiânia (Edital 003/2026). Pelo edital, até 30% da carga horária pode ser a distância. BLOQUEADO até G12 e G7. | Catálogo; ficha; editais |
| Quais disciplinas e o que posso fazer com o curso? | A página destaca a docência na Educação Infantil e nos anos iniciais do Ensino Fundamental e a gestão educacional; a matriz tem Educação Inclusiva e Letramento em Libras. Não prometo emprego nem salário. | Ficha do curso |
| Quem é o coordenador? Quem são os professores? | Vou confirmar com a Ufape. Não informo docente até a Ufape informar o corpo docente do curso. | [CONFIRMAR NO CATÁLOGO] |
| Quando é o estágio? | O estágio supervisionado começa a partir do 6º semestre, conforme a matriz. Horários eu confirmo. | Ficha do curso; [CONFIRMAR horários] |
| Onde fica a unidade? Posso me inscrever presencialmente? | A inscrição pode ser feita pelo site ou presencialmente em Goiânia. Vou te passar o endereço confirmado pela equipe. | Edital 004/2026; [CONFIRMAR G9] |
| Qual o contato? | Vendas Goiânia (62) 9420-1847. | contexto/ufape-geral.md |

### 4.4 Quando passar para outra pessoa

| Situação | Para quem |
|---|---|
| Dúvida de pagamento, boleto, cobrança ou 1ª mensalidade | Financeiro: financeiro@intercursos.com.br, (11) 94525-3730 (WhatsApp) |
| Documentos, contrato, calendário | Secretaria: (11) 97492-8443, (11) 5054-1204, duvidas@intercursos.com.br [CONFIRMAR para Goiânia] |
| Reconhecimento, regras de renovação, comprovação, aulas a distância | Regulação e coordenação [CONFIRMAR responsáveis] |
| Reclamação, ouvidoria | sac@intercursos.com.br, ouvidoria@intercursos.com.br |
| Menor de idade sem consentimento registrado, pedido de exclusão de dados | Responsável pela LGPD e jurídico [CONFIRMAR] |

---

## 5. Regras de saída (valem para todas as réguas)

| Evento | O que acontece | Quem faz |
|---|---|---|
| Lead conclui a inscrição | Sai da régua L na hora. Entra em R1, sem repetir contato feito nos últimos 2 dias. Cancelar toques L pendentes | CRM |
| Inscrito faz a redação ou envia o Enem | Sai de R e de AT. Nenhuma mensagem de venda. Só o aviso de serviço do sistema [CONFIRMAR]. Aguarda o resultado | CRM |
| Resultado: aprovado | Entra em A1 (ou A1-R) na data de publicação, só com status do sistema | CRM |
| Resultado: não aprovado na redação | Sai de todas as réguas. Nenhuma mensagem automática de marketing. Alerta ao time de captação para contato humano e cuidadoso (nova tentativa, Enem). Regra de nova tentativa [CONFIRMAR] | Captação |
| Aprovado se matricula (1ª mensalidade e contrato) | Sai de A. Entra em M1 (ou M1-R) | CRM |
| Matriculado conclui documentos | Cancela M2 e a pendência em M5 (o CTA muda) | CRM |
| Candidato ou representante legal responde com dúvida ou pede para falar com a captação | Para todo envio automático na hora. Etiqueta "falar com a captação". O time responde no horário comercial (prazo interno [CONFIRMAR]; proposta: até 1 dia útil [SUPOSIÇÃO]). A régua só volta se o time liberar | Captação |
| Para de responder | Sem abertura, clique ou resposta até o último toque da régua (L7, R5, A6): recebe "sem engajamento", encerra WhatsApp e e-mail da régua e fica fora de novos envios até agir (voltar ao site, abrir e-mail, responder). Não há "último aviso" com urgência | CRM |
| Responde SAIR (WhatsApp) | Encerra o WhatsApp de marketing na hora e registra data e canal. Uma única mensagem de confirmação ("Pronto, você não vai mais receber mensagens da Ufape por aqui"). O e-mail só para se também pedir | CRM |
| Clica em descadastrar (e-mail) | Encerra o e-mail de marketing na hora, registra data e canal | CRM |
| Bloqueia o número, número inválido, e-mail devolvido | Encerra o canal e marca o contato | CRM |
| Mensagem de serviço depois da saída | Contrato, cobrança, documentos e aviso de turma não são marketing; seguem pelo financeiro e pela secretaria [CONFIRMAR com o jurídico e o financeiro]. A régua de marketing nunca as usa para vender | Jurídico, financeiro |
| Candidato menor sem consentimento do representante legal registrado | Nenhum envio. Etiqueta "aguardando G10". Entra na régua só depois da validação, e só com as versões -R | CRM |
| Candidato menor, mensagem sem versão -R | Não sai, nem para o menor nem para o representante legal (0.5, item 3) | CRM |
| Representante legal pede para apagar os dados do menor | Para todo envio, encaminha ao responsável pela LGPD [CONFIRMAR canal] | Jurídico |
| Pediu transferência, ingresso de diplomado ou vaga remanescente | Sai das réguas e vai ao time de captação (formas de ingresso depois dos ingressantes por redação e Enem) | Captação |
| Cancela a matrícula (até 20/02/2027) ou a Ufape cancela a turma | Sai de M. Nenhuma mensagem de marketing. A mensagem de serviço é da secretaria | Secretaria |
| Toque de campanha cai em dia sem campanha do D1 ou passa do teto D16 (3 por semana, 2 por canal, 1 por dia; teto menor para quem está também na base da Pós) | Passa para o próximo dia permitido, na ordem da fila D2 (seção 0.7) | CRM |
| Erro 131049 no WhatsApp (E2) | Sem reenvio por WhatsApp antes de 24 h; conta como suprimida | CRM |
| Contato sem engajamento no WhatsApp (E1) | No máximo 1 WhatsApp de campanha por semana; sem interação em 90 dias, só e-mail | CRM |
| 22/02/2027 | Todas as réguas da Graduação 2027/1 encerram. Pedido de pausa das campanhas (aprovação humana, pedido G16 do cmo) | cmo, humano |
| Ufape informar data-limite interna de inscrição ou matrícula | Puxar A6 e M5 para essa data, em ciclo extra do cmo | cmo |

---

## 6. Registro e medição por mensagem

| Régua | Mensagem | Sucesso é | Onde mede |
|---|---|---|---|
| AT | AT1, AT2, AT3 | Redação feita ou Enem enviado em até 7 dias; resposta | Sistema de inscrição e CRM |
| L | L1 a L7 | Inscrição concluída; resposta; clique na LP | LP, CRM (UTM por mensagem) [CONFIRMAR G13] |
| R | R1 a R5 | Redação feita ou Enem enviado | Sistema de inscrição e CRM |
| A | A1 a A6 | 1ª mensalidade paga e contrato assinado | Financeiro e CRM |
| M | M1 a M5 | Documentos enviados; matrícula mantida até 22/02/2027 | Secretaria e CRM |

Cada clique na LP chega ao CRM com utm_source (email ou whatsapp), utm_medium=crm, utm_campaign (grad_<curso>_<AAAAMM>) e utm_content (código da mensagem, inclusive as -R), no padrão D11 e D12 do cmo (seção 0.2). Assim a leitura é por mensagem, por canal e por liberação, e soma com as outras linhas pelo mesmo utm_medium.

Cliques, respostas e conversões (inscrição, redação, matrícula) contam mais do que abertura e leitura. Leitura por liberação e por turno, nunca somada. Testes sugeridos: primeira linha A contra B (AT2, L2, R2, A2) e assunto A contra B (AT1, L3, A1, A3); cada teste vai ao registro de testes com resultado. Volume por teste e limite estatístico: [CONFIRMAR após os números do funil, pedido G2 do cmo]. Nenhuma abertura ou leitura é usada como prova de interesse para decidir pressão.

Fica de fora de toda a medição: nome, telefone, e-mail ou CPF de candidato em relatório e em UTM. O cmo lê só números somados por turma.

---

## 7. Auditorias

Aplicadas por este agente ao rascunho corrigido. A conferência final é do qa-de-marketing (rodada d) e a aprovação é humana.

### auditorias/07-email-e-whatsapp.md

- [ ] Consentimento e descadastro funcionando (opt-in registrado para WhatsApp e forma simples de sair nos dois canais). As regras e os campos fixos FE e FW estão escritos, com rodapé próprio de cada liberação, e todo envio exige opt-in registrado. O teste do SAIR e do link de descadastro e o registro de opt-in e de consentimento de menor dependem do CRM [CONFIRMAR, pedidos G10 e G13]. Bloqueia o envio.
- [x] Cada mensagem tem um objetivo (campo "Objetivo" ou título de cada contato).
- [x] Assuntos e primeiras linhas de WhatsApp são honestos: nenhum fala em vagas acabando, prazo inexistente, aprovação certa ou desconto sem validade; Enem sempre com a condição (média mínima de 300 pontos, edições de 2010 em diante) em pré-visualizações, primeiras linhas e ganchos; gancho do AT3 sem afirmação sem dado; gancho do A2 sem promessa de celular.
- [x] Segmentos recebem mensagens relevantes para a etapa: AT, L, R, A e M, com 13 versões -R por liberação escritas por extenso e a regra de que mensagem sem -R não vai a menor nem ao representante legal.
- [x] Réguas têm regras de saída (seção 5).
- [ ] Resultados registrados para cada envio: o plano de registro está na seção 6; nada foi enviado. Pendente até o primeiro envio.
- [ ] Cliques, respostas e conversões medidos, não só aberturas: UTM por mensagem no padrão D11 e D12 (seção 0.2); depende da URL e da origem chegando ao CRM [CONFIRMAR, pedido G13].
- [ ] WhatsApp só em horário comercial, com frequência humana e template aprovado pela Meta: horário, teto D16, regras E1 a E4 e frequência escritos (FW e 0.7); nenhum template foi submetido nem aprovado. Pendente.

### auditorias/06-geracao-de-demanda.md

- [x] Toda campanha tem um briefing escrito: estrategia-de-campanha-graduacao-2026-10-26.md (G1 e G2).
- [ ] Metas definidas antes do lançamento: piso de 30 matrículas por turma e meta de redações até 31/01/2027 [SUPOSIÇÃO de desenho]; alvos, custos e taxas [CONFIRMAR]. Não é meta desta régua, mas bloqueia a leitura dela.
- [x] A isca digital entrega a promessa do título: não há isca nesta régua; {link_passo_a_passo} só entra se existir.
- [x] Toda captura de lead tem nutrição em seguida: L (lead), R (inscrito) e AT (base existente), em e-mail e WhatsApp.
- [x] Plano de distribuição por peça: cada contato tem canal, momento, segmento e, quando cabe, bloqueio.
- [x] Regras das comunidades respeitadas: não se aplica.
- [ ] Revisão no ponto de checagem realizada: C0 (30/10), C1 (30/11), C2 (04/01/2027) e C3 (25/01/2027) definidos pelo cmo; ainda não realizados.
- [ ] Consentimento para contato por e-mail e WhatsApp coletado em todo formulário: a squad não altera a LP; [CONFIRMAR] com a plataforma e o jurídico (G10 e G13). Bloqueia o envio.
- [x] Bolsas, descontos e prazos batem com o catálogo e a ficha da oferta: os seis elementos do desconto em toda mensagem que o cita (BP e LD); "dia 10" e reajuste só na Medicina Veterinária; Pedagogia sem vencimento e sem reajuste; matrícula "a partir de" 2 dias; 22/02/2027, 20/02/2027, 30 dias e 80% conferidos com a ficha dos editais. O total do semestre com desconto é aritmética sobre esses valores.

### auditorias/conformidade-educacional.md

DADOS DO CURSO
- [x] Nome, modalidade, duração e turno batem com o catálogo; carga horária da Medicina Veterinária (4.195 h + 75 h) bate; a da Pedagogia não aparece em nenhuma mensagem nem resposta.
- [x] Os dois cursos estão "aberto" no catálogo.
- [x] Modalidade presencial clara; até 30% a distância informado nas respostas e na comparação com EAD, sem esconder.

REGULAÇÃO (MEC)
- [x] Atos autorizativos como no catálogo, com o D.O.U. (Portaria SERES/MEC nº 162, de 13/03/2025, D.O.U. 21/03/2025; Portaria nº 992, de 08/12/2022, D.O.U. 20/12/2022); credenciamentos só com número e data; reconhecimento não citado.
- [x] Pós lato sensu e curso livre: não se aplica.
- [x] Nenhuma nota do MEC; nenhuma frase de certificação.

PROMESSAS E PROVAS
- [x] Nenhuma promessa de emprego, salário, promoção, aprovação ou concurso; a redação é descrita como eliminatória. Sem promessa de "regras de renovação por escrito" e sem "dá para fazer pelo celular".
- [x] Nenhum dado de empregabilidade ou satisfação.
- [x] Nenhum superlativo sem fonte.
- [x] Comparação com EAD só por atributos verificáveis, sem preço de terceiros e sem depreciar.

PREÇO E CONDIÇÕES (CDC)
- [x] Preço com valor cheio, valor com desconto, percentual, validade, renovação e perda no atraso, e o nome do programa; sem taxa escondida.
- [ ] Preço estável e texto do edital sem ambiguidade: toda mensagem e resposta com preço BLOQUEADA até G12 (reajuste) e G7 (erros dos Editais 003/2026). G2-M4 também até a confirmação do vencimento da Pedagogia.
- [x] Sem urgência falsa: sem "últimas vagas", sem contagem regressiva; gancho do A6 sem leitura de escassez; a turma mínima aparece como regra do edital, nunca como pressão.
- [x] Prouni, Fies e financiamento não aparecem em mensagem; na resposta pronta, só dizem que não há informação confirmada.

PESSOAS E DADOS (LGPD E DIREITO DE IMAGEM)
- [x] Nenhuma foto, vídeo, depoimento ou docente nas mensagens; hospital só como linha opcional em nota, condicionada a G11.
- [ ] Menores: aceite do representante legal na inscrição e na matrícula, 13 versões -R por liberação e a regra de que mensagem sem -R não sai; nenhum envio a menor sem validação jurídica. O consentimento de menor no CRM depende de G10.
- [ ] Formulários informam a finalidade do uso dos dados e têm link para a política de privacidade: o rodapé dos e-mails traz {link_politica}; o formulário da LP não é da squad [CONFIRMAR, pedido G13].
- [ ] WhatsApp e e-mail só vão para quem deu consentimento, com forma fácil de sair: regra e campos escritos; consentimento registrado e consentimento de menor dependem do CRM e do jurídico [CONFIRMAR, G10].
- [x] Nenhum dado pessoal de aluno ou candidato neste arquivo nem nas UTM (só variáveis do CRM).

PLATAFORMAS
- [x] Anúncios: não se aplica (a régua não é anúncio). Nenhuma frase afirma ou insinua característica pessoal de quem recebe.
- [ ] Página de destino entrega o que a mensagem prometeu: toda mensagem do G2 com link da LP BLOQUEADA até G6 e toda mensagem do G1 com link da LP que cita o noturno BLOQUEADA até G8; até lá, a chamada vira resposta à mensagem. A correção das páginas é da equipe do site.

RESULTADO: correções N1 a N16 aplicadas; rascunho pronto para a rodada d do qa-de-marketing. Bloqueado para envio até: consentimento e menores (G10, G13), templates da Meta, preço (G12 e G7), página de Pedagogia (G6) e do noturno (G8) quando o link for a LP, vencimento da Pedagogia (G2-M4) e aprovação humana do envio em massa (aprovadores a nomear, G14). Revisado por: campanhas-de-nutricao (agente). Revisão do qa-de-marketing e humana: pendente. Data: 26/10/2026.

Notas para arquivos de outros donos (não alterados por este agente):
- O plano do cmo prevê este arquivo com data de 06/11/2026; foi entregue em 26/10/2026.
- A resposta pronta sobre Prouni e Fies não vem do catálogo: precisa de decisão da Ufape (participa ou não).
- Matriz do 1º semestre da Medicina Veterinária, conferida na ficha: são três componentes, "Campos de Atuação do Médico Veterinário e Práticas Hospitalares", "Projeto Extensionista I" e "Práticas Hospitalares". O briefing e a oferta, que às vezes juntam ou separam esses nomes, podem usar a mesma lista.
- Para o cmo: confirmar (a) a classificação de serviço da Graduação na seção 0.7 (R1, A1, M1 e as -R; M2 e M4 como J3 e J4; M5 como véspera); (b) que o toque em dia sem campanha muda de data em vez de ser suprimido; (c) a chave grad_medvet_<AAAAMM> para lead sem turno.
- Para o posts-sociais: a nutrição passou a usar "representante legal" e a mesma regra de Pedagogia sem "dia 10" dos posts.

---

## Lista 1. Fatos (com fonte)

- Medicina Veterinária: bacharelado presencial em São Paulo, integral em 4 anos e noturno em 5 anos, 4.195 h + 75 h de atividades complementares (catálogo, seção 1; Edital 002/2026).
- Pedagogia: licenciatura presencial em Goiânia, noturno, 4 anos (catálogo, seção 1; Edital 004/2026). Nenhuma carga horária é usada.
- Medicina Veterinária: de R$ 10.000,00 por R$ 5.000,00 por mês (integral, 50%) ou R$ 4.000,00 (noturno, 60%); semestre cheio de R$ 60.000,00 em 6 parcelas de R$ 10.000,00 (catálogo; Edital 003/2026).
- Pedagogia: de R$ 1.050,00 por R$ 525,00 por mês (50%); semestre cheio de R$ 6.300,00 em 6 parcelas (catálogo; Edital 003/2026 Goiânia).
- Totais do semestre com desconto (R$ 30.000,00, R$ 24.000,00 e R$ 3.150,00): aritmética sobre os valores acima.
- Desconto só no 1º semestre de 2027, todas as formas de ingresso, aplicado a partir da confirmação da matrícula, renovação a cada semestre com comprovação, perda no mês pago com atraso, sem acúmulo com programa governamental, queda se a turma tiver menos de 30 matrículas confirmadas (Editais 003/2026).
- Vencimento no dia 10 e reajuste em dezembro de cada ano: Medicina Veterinária, São Paulo (Edital 002/2026). A ficha dos editais não traz vencimento nem reajuste para a Pedagogia (oferta 0.1: [CONFIRMAR]).
- Inscrição gratuita desde 17/08/2026, pelo site ou presencial, de segunda a sexta, das 9h às 18h; São Paulo: Av. Nove de Julho, 3913 e 3939, Jardim Paulista (Edital 002/2026).
- Redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0; Enem com média aritmética mínima de 300 pontos, edições de 2010 em diante (Editais 002 e 004/2026).
- Resultado no site; matrícula eletrônica a partir de 2 dias depois; confirmada com a 1ª mensalidade e a assinatura digital do contrato; documentos pela plataforma de matrícula digital em até 30 dias (editais).
- Aulas em 22/02/2027; turma mínima de 30, com reembolso da 1ª parcela se a oferta for cancelada; devolução de 80% se o cancelamento for pedido até 2 dias antes das aulas (editais); 20/02/2027 é a conta sobre 22/02/2027.
- Vagas: 45 integral, 45 noturno, 80 Pedagogia (editais). Até 30% da carga horária pode ser a distância (editais).
- Candidato menor de idade precisa do aceite do representante legal na inscrição e na matrícula (Edital 002/2026; Edital 004/2026 com as mesmas regras; ficha dos editais).
- Atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025); Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) (catálogo). Credenciamento: Portaria MEC nº 176, de 27/02/2025 (D.O.U. 28/02/2025, São Paulo); Portaria MEC nº 871, de 10/11/2022 (Goiânia) (editais; contexto/ufape-geral.md).
- Contatos oficiais: secretaria (11) 97492-8443 e (11) 5054-1204, duvidas@intercursos.com.br; Vendas São Paulo (11) 91366-9290; Vendas Goiânia (62) 9420-1847; financeiro (11) 94525-3730 e financeiro@intercursos.com.br; SAC e ouvidoria @intercursos.com.br (contexto/ufape-geral.md). Razão social, CNPJ 27.409.162/0001-34 e sede na Av. 9 de Julho, 3939 (idem).
- Matriz da Medicina Veterinária: no 1º semestre, Campos de Atuação do Médico Veterinário e Práticas Hospitalares, Projeto Extensionista I e Práticas Hospitalares; estágio nos 7º e 8º (integral) e 9º e 10º (noturno) (contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md, conferido pelo qa-c e por este agente). Pedagogia: Prática Docente e Projeto Integrador desde o 1º semestre, Educação Inclusiva, Letramento em Libras e estágio a partir do 6º semestre (ficha do curso, conferida pelo qa-c).
- Janelas e dias sem campanha do D1, fila D2 e padrão de UTM D11 e D12 (utm_medium=crm, prefixo grad_, utm_content com o código da mensagem) (cmo-geral-2026-10-26.md, seção 12). Teto D16 da Graduação: até 3 mensagens de campanha por semana somando canais, até 2 por canal, 1 por dia, teto menor para quem está nas duas bases; regras E1 a E4; classificação de serviço (cmo-geral-2026-10-26.md, seção 13.3).
- O kit mínimo da Graduação foi entregue como toques de calendário KW1 a KW5 e KE1 a KE3 (copy-de-mensagens-graduacao-2026-10-26.md, seção 0.1).
- Bloqueios G6, G7, G8, G10, G11, G12 e G13 e kit mínimo de 5 WhatsApp e 3 e-mails por liberação (cmo-graduacao-2026-10-26.md, seções 5, 6 e 8).
- A Graduação não tem número de vagas restantes, nota do MEC, data de prova nem data final de inscrição publicados (ficha dos editais).
- 30/10/2026 é sexta-feira; 03/11/2026 é terça-feira; 22/02/2027 é segunda-feira (calendário).

## Lista 2. Suposições

- [SUPOSIÇÃO] Números do D16 (3 por semana, 2 por canal, 1 por dia) e critério do E1 (4 mensagens, 90 dias): decisão do cmo sem fonte de número, a calibrar com a seção 13.4; horários de envio (10h30 e 14h30) a testar.
- [SUPOSIÇÃO] Os tempos entre toques (D0, D2, D5, D8, D12, D15, D20 e os das réguas R, A e M) são desenho meu e precisam de teste com números reais.
- [SUPOSIÇÃO] A sobreposição entre a base da Graduação e as bases de Pós, Livres e Eventos é pequena; o CRM não tem o número.
- [SUPOSIÇÃO de desenho] Toque de campanha em dia sem campanha do D1 muda para o próximo dia permitido, sem envio extra.
- [SUPOSIÇÃO de chave] utm_campaign grad_medvet_<AAAAMM> para lead do G1 sem turno escolhido.
- [SUPOSIÇÃO de desenho] Meta interna de redações e Enem cumpridas até 31/01/2027 (briefing).
- [SUPOSIÇÃO] O gargalo do funil é o inscrito que não faz a redação (plano do cmo); a ativação da base nasce dessa hipótese.
- [SUPOSIÇÃO] 20/11/2026 é feriado (de todo modo, dia sem campanha pelo D1); Carnaval de 2027 em 8 a 10/02. Conferir o calendário antes de agendar.
- [SUPOSIÇÃO] Prazo interno de resposta do time de captação de até 1 dia útil.
- [SUPOSIÇÃO] Personas e objeções de contexto/graduacao.md (mensalidade alta, faculdade pouco conhecida, Pedagogia EAD mais barata) sustentam os temas de L3, L4, L5-alt e L6.
- [SUPOSIÇÃO] Os templates da Meta caberão nos limites de tamanho, inclusive com a linha LD do desconto; a categoria (utilidade ou marketing) será definida na submissão; o link da LP pode entrar como botão informativo no L4 depois de G8 e G6.
- [SUPOSIÇÃO de leitura] "Toda peça aponta para a LP da Graduação com UTM" vale para o link de campanha; os links de sistema (área do candidato, resultado, matrícula, editais) são etapas do processo seletivo.

## Lista 3. Dados que faltam

- [CONFIRMAR] Passo a passo exato da redação e do envio do Enem na área do candidato (tema, tempo, nova tentativa, como a média é calculada, prazo do resultado) e se existe {link_passo_a_passo}.
- [CONFIRMAR] Data-limite interna de inscrição e matrícula e data de decisão sobre a turma mínima (pedido G4).
- [CONFIRMAR] Vencimento e reajuste da Pedagogia no Edital 004/2026 (G2-M4 bloqueado até a resposta).
- [CONFIRMAR] Efeito do reajuste de dezembro sobre 2027/1 (G12) e correção dos textos dos Editais 003/2026 (G7): toda mensagem com preço depende disso.
- [CONFIRMAR] Se a 1ª mensalidade já sai com o desconto; calendário das 6 mensalidades; formas de pagamento; de quando contam os 30 dias dos documentos; lista de documentos.
- [CONFIRMAR] O que é a "comprovação" da renovação (proposta P1, não aprovada).
- [CONFIRMAR] Como o aceite do representante legal é dado na matrícula e como o CRM trata o consentimento de menor (pedido G10); se o CRM guarda menor de idade, representante legal, turno e status de redação.
- [CONFIRMAR] Se o formulário da LP é a inscrição; URL que recebe a UTM; origem no CRM; política de privacidade no formulário (pedido G13).
- [CONFIRMAR] Opt-in de WhatsApp registrado, templates submetidos e aprovados na Meta, categoria de cada um; ferramenta de CRM e de atendimento; o canal de WhatsApp de vendas ativo em São Paulo e Goiânia.
- [CONFIRMAR] Se existe visita guiada (P4) ou aula aberta (P9); sem isso, L5-alt.
- [CONFIRMAR] Uso da Ufape Clínica pela graduação (pedido G11) e corpo docente da graduação.
- [CONFIRMAR NO CATÁLOGO] Horário das práticas e do estágio do noturno; coordenação, corpo docente e carga horária da Pedagogia (pedido G5); quais disciplinas usam os 30% a distância.
- [CONFIRMAR] Endereço da unidade de Goiânia e data de publicação da Portaria MEC nº 871/2022 (pedido G9); se duvidas@intercursos.com.br atende Goiânia.
- [CONFIRMAR] Correção das páginas de Pedagogia (G6) e do turno do noturno (G8).
- [CONFIRMAR] Local, horário e calendário do primeiro dia de aula; dados para M3 e M5.
- [CONFIRMAR] Regra para o candidato não aprovado (nova tentativa, Enem); procedimento de transferência, diplomado e vagas remanescentes.
- [CONFIRMAR] Com o cmo: mudança de data em dia sem campanha, chave de UTM sem turno (seção 0.7 e 0.2) e a leitura do kit como só os toques de calendário do copy-de-mensagens (A-N4).
- [CONFIRMAR] Se a Ufape usa a API oficial do WhatsApp Business (pedido U11a); sem ela, E1 e E2 não se aplicam como regra automática. Aprovação do pedido R1 e JR3 (M2 e M4 como serviço).
- [CONFIRMAR] Números agregados e metas por turma (pedidos G2 e G3); aprovadores do envio em massa (pedido G14); responsável pela LGPD e canal de pedidos de titular.

---

## Próximo passo

Próximo agente sugerido: copy-de-mensagens (09/11/2026), que lapida estes textos, mantém o kit mínimo nos toques de calendário do arquivo dele (KW1 a KW5 e KE1 a KE3), confere a contagem do D16, escreve as respostas-padrão finais e roda os testes A e B das primeiras linhas e dos assuntos. Depois, nova conferência do qa-de-marketing sobre a v3. A ativação da base (G1-AT e G2-AT) não depende de G6, G8, G12 nem G7 e pode ser antecipada para 03/11/2026, na ordem do plano do cmo, depois do QA e da aprovação humana. Nada é enviado, publicado ou pago sem a aprovação humana.
