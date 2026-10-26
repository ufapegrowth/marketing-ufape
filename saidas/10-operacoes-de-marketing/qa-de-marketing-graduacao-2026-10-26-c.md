# QA de marketing: posts orgânicos e régua de nutrição da Graduação 2027/1 (rodada c)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 26/10/2026 (segunda-feira)
- Workflow: /campanha-de-vestibular, etapa 8 de 8 (parte final)
- Peças revisadas (não editadas):
  - saidas/05-social-e-comunidade/posts-sociais-graduacao-2026-10-26.md (auditoria 05 e conformidade educacional)
  - saidas/06-geracao-de-demanda/campanhas-de-nutricao-graduacao-2026-10-26.md (auditorias 06 e 07 e conformidade educacional)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (cabeçalho, regras de uso e seção 1)
  - contexto/cursos/graduacao/editais-2027-1.md
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md (matriz, para conferir disciplinas e semestres citados)
  - contexto/cursos/graduacao/graduacao-em-pedagogia.md (matriz e 1º parágrafo, para conferir componentes e trechos de modelo)
  - templates/post-social.md, templates/mensagem.md, templates/kit-de-lancamento-graduacao.md
  - auditorias/05-social.md, auditorias/06-geracao-de-demanda.md, auditorias/07-email-e-whatsapp.md, auditorias/conformidade-educacional.md
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (bloqueios G1 a G16, kits e calendário)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md (seções 0 a 4)
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md (seção 0 e briefing G1)
  - saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md (seções 0 a 2.1, regras e blocos)
- Status: rascunho de QA. Nada é publicado, enviado ou pago a partir deste arquivo.

---

## 0. Vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| posts-sociais-graduacao-2026-10-26.md | **CORRIGIR** | Enem sem a condição de ingresso em várias chamadas; "responsável" no lugar de "representante legal"; promessa de "regra de renovação por escrito" (proposta P1, não aprovada); datas do Enem não confirmadas no gancho sem bloqueio; posts do G2 sem bloqueio G6 no campo de publicação; G1-03 só "recomendado" até G8; kit G1 sem o post substituto do hospital; itens de conformidade em aberto |
| campanhas-de-nutricao-graduacao-2026-10-26.md | **CORRIGIR** | Desconto incompleto em 12 mensagens; mensagens com preço sem bloqueio G12 e G7; "dia 10" e reajuste de dezembro afirmados para a Pedagogia sem fonte; promessa de regras de renovação "por escrito"; "responsável legal" no lugar de "representante legal"; versões para o responsável incompletas; G2 com link para a LP sem bloqueio G6; matrícula sem "a partir de"; itens de conformidade em aberto |

Os dois arquivos falham em itens de auditorias/conformidade-educacional.md (preço e condições, menores, formulários, página de destino). Pela regra, o veredito é corrigir, sem exceção. Os dois voltam aos agentes que os produziram (posts-sociais e campanhas-de-nutricao) e não seguem para a aprovação humana nesta rodada.

---

## 1. Conferência de dados comum (contra editais e catálogo)

| Dado | Fonte | Posts | Nutrição |
|---|---|---|---|
| Inscrição gratuita, abertas desde 17/08/2026 | editais 002 e 004/2026 | ok | ok |
| Redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0 | editais | ok | ok |
| Enem: média mínima de 300 pontos, edições de 2010 em diante | editais | **falha** em CTAs, Stories e ganchos alternativos (P1) | **falha** em pré-visualizações e primeiras linhas (N9); corpos ok |
| Desconto com valor cheio, valor com desconto, percentual, validade (1º semestre de 2027), renovação semestral, perda no atraso | Editais 003/2026; oferta 0.2 | ok nos 4 posts de preço (G1-07, G1-08, G1-09, G2-05), todos bloqueados por G12 e G7 | **falha** em 12 mensagens (N1); Pedagogia com "dia 10" e reajuste sem fonte (N3) |
| Matrícula a partir de 2 dias depois do resultado | editais | ok | **falha** em L1, L7, G2-L1, G2-L7 (N8) |
| Aulas em 22/02/2027 (segunda-feira) | editais | ok | ok |
| Turma mínima de 30, devolução da 1ª parcela | editais | ok | ok |
| Cancelamento com 80% até 2 dias antes das aulas | editais | ok | ok (20/02/2027 é conta da oferta) |
| Ato Medicina Veterinária: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) | catálogo | ok na legenda; arte do G1-05 sem D.O.U. (P10) | ok em BA; L4 sem D.O.U. (N13) |
| Ato Pedagogia: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) | catálogo | ok (B-ATO-PED) | ok em BA; G2-L4 sem D.O.U. (N13) |
| Credenciamentos (176/2025 SP; 871/2022 Goiânia, sem data de publicação) | editais; ufape-geral.md | não citados | ok |
| Carga horária Medicina Veterinária 4.195 h + 75 h | catálogo | ok (G1-05) | ok (L1, 4.2) |
| Carga horária da Pedagogia ausente | catálogo [CONFIRMAR], G5 | ok, ausente | ok, ausente |
| Matriz citada (disciplinas e semestres) | fichas dos cursos (conferidas por este QA) | bate, salvo nomes resumidos em G2-06 (P9) | bate, salvo "Campos de Atuação do Médico Veterinário" (N10) |
| Nota do MEC, certificação, "reconhecido" | proibido | nenhuma ocorrência | nenhuma ocorrência |
| Emprego, salário, aprovação garantida, "últimas vagas", entrada garantida | proibido | nenhuma ocorrência | nenhuma ocorrência |
| Trechos de modelo, egresso copiado ou professores da página de Pedagogia | proibido (auditoria 22/10, item 2.3) | nenhuma ocorrência; o foco usado é do 1º parágrafo, próprio da Pedagogia | nenhuma ocorrência |
| Nome de docente ou aluno | proibido | nenhum | nenhum (só variáveis do CRM) |
| Menor: "representante legal" | Edital 002/2026; briefing (correção 6) | **falha**: "responsável" nas CTAs (P2) | **falha**: "responsável legal" (N5) |
| Destino: LP da Graduação com UTM | cmo 5; briefing regra 1 | ok, URLs com UTM por post [CONFIRMAR G13] | {link_lp_utm} [CONFIRMAR G13]; falta utm_content por mensagem (N15) |
| Travessão ou meia-risca | regra da casa | nenhum encontrado na leitura integral | nenhum encontrado na leitura integral |

---

## 2. Arquivo 1: posts-sociais-graduacao-2026-10-26.md

### 2.1 auditorias/05-social.md, item por item

- [ ] **A frequência de publicação segue o plano.** Quantidade bate com o kit (G1: 11 posts, kit de 6 mais 2 para famílias e 3 extras; G2: 7 posts, kit de 6 mais 1 extra). Mas G1-01 (03/11), G2-01 (04/11), G1-02 e G2-02 (06/11, Stories em 08/11 e 15/11) e G1-03 (10/11) estão antes do QA (10/11), da aprovação humana (11 a 13/11) e do início da captação (16/11) do plano do cmo, seção 6. E o kit do G1 perde um post se G11 não for confirmado, porque não há o substituto pedido pelo cmo (P7, P8).
- [x] **Todo post tem uma ideia clara.** Cada post responde uma pergunta só.
- [x] **Os ganchos são cumpridos pelo conteúdo.** Gancho principal e corpo batem em todos os posts. Os ganchos alternativos que falam do Enem sem a condição precisam de ajuste antes de virar teste (P1).
- [ ] **Histórias e números são reais.** Sem depoimentos nem números de desempenho. Mas as datas do Enem 2026 (08 e 15/11) estão no gancho de G1-02 e G2-02 e não constam no catálogo nem no edital, e o campo de publicação não diz BLOQUEADO (P5).
- [x] **Os posts estão formatados para celular.** Linhas curtas, gancho sozinho na linha 1.
- [x] **As ações de comunidade aconteceram nesta semana.** Não se aplica ao rascunho: nada foi publicado. Ações previstas (caixas de perguntas sem nome) conferidas.
- [x] **As métricas acompanhadas são conversas qualificadas e leads.** Cliques por UTM, conversas e inscritos por origem, lidos por turma. Origem no CRM depende de G13.
- [x] **Toda imagem ou depoimento de aluno e professor tem autorização registrada.** As artes são tipográficas, sem pessoas. As variantes com foto (G1-04 e G1-11) estão condicionadas a [CONFIRMAR autorização].
- [ ] **Dados de curso nos posts batem com o catálogo.** Nome, local, modalidade, turno, duração, carga horária, preço e ato batem. Falham: Enem sem a condição (P1) e nomes resumidos de componentes da Pedagogia em G2-06 (P9). A matriz citada foi conferida por este QA na ficha do curso: Práticas Hospitalares e Projeto Extensionista I no 1º semestre dos dois turnos; estágio no 7º e 8º (integral) e no 9º e 10º (noturno); Prática Docente do 1º ao 8º, Projeto Integrador do 1º ao 7º e estágio a partir do 6º na Pedagogia.

### 2.2 auditorias/conformidade-educacional.md, item por item

DADOS DO CURSO
- [x] Nome, modalidade, carga horária, duração e turno batem com o catálogo; carga horária da Pedagogia ausente.
- [x] Os dois cursos estão com status "aberto".
- [x] Modalidade presencial clara.

REGULAÇÃO (MEC)
- [x] Ato do catálogo, sem antecipar reconhecimento (B-ATO-MV em G1-05; B-ATO-PED em G2-05). Ajuste de forma na arte do G1-05 (P10).
- [x] Pós lato sensu: não se aplica.
- [x] Curso livre: não se aplica.
- [x] Nenhuma nota do MEC.

PROMESSAS E PROVAS
- [x] Nenhuma promessa de emprego, salário, aprovação ou concurso. A promessa de "regra de renovação por escrito" é tratada como promessa não verificada (P4) e bloqueia a peça pela regra do QA.
- [x] Nenhum dado de empregabilidade ou satisfação.
- [x] Nenhum superlativo.
- [x] Nenhuma comparação com concorrente.

PREÇO E CONDIÇÕES (CDC)
- [ ] Preço com condições completas: os textos estão completos, mas o efeito do reajuste de dezembro sobre 2027/1 não foi confirmado (G12) e o Edital 003/2026 tem erros (G7). G1-07, G1-08, G1-09 e G2-05 estão corretamente BLOQUEADOS.
- [x] Desconto com regra, público elegível e validade.
- [x] Urgência só real; G1-11 condicionado à turma confirmada.
- [x] Prouni, Fies e financiamento não aparecem.

PESSOAS E DADOS
- [x] Nenhum depoimento, foto ou vídeo de pessoa.
- [x] Nenhum menor em imagem. O texto do aceite precisa usar "representante legal" (P2) e aparecer em todo post do G1 que chama para inscrição (P3).
- [ ] Formulários com finalidade e política de privacidade: formulário da LP não confirmado (G13).
- [x] WhatsApp e e-mail: não se aplica (posts não enviam mensagem).
- [x] Nenhum dado pessoal.

PLATAFORMAS
- [x] Políticas de anúncio: posts orgânicos; impulsionamento só com auditoria 11 e 18 anos ou mais.
- [ ] Página de destino entrega o que o post promete: falha no G2 (página de Pedagogia com texto de modelo, G6) e nos posts do noturno (campo turno "INTEGRAL", G8). Os posts do G2 não trazem BLOQUEADO no campo de publicação e o G1-03 só traz "recomendado" (P6).

ANÚNCIOS (META E GOOGLE)
- [x] Não se aplica a orgânico. Conferido mesmo assim: nenhum texto afirma situação de quem lê, sem caixa alta, sem pontuação repetida, sem pessoa pública, sem sugestão de driblar análise.

RESULTADO: Bloqueado. Revisado por: qa-de-marketing (agente). Revisão humana: pendente. Data: 26/10/2026.

### 2.3 Lista de correções (posts)

| # | Prioridade | Onde | Problema | Correção proposta |
|---|---|---|---|---|
| P1 | alta | CTAs de G1-01, G1-04, G1-07, G2-01, G2-03 e G2-05 ("Redação online quando você puder ou nota do Enem."); G2-02, Stories tela 2 ("Nota de 2010 em diante vale para entrar em Pedagogia."); G1-05, arte cartão 4 ("mínimo de 300 pontos", sem "média" e sem "de 2010 em diante"); gancho do G1-10 ("tem nota do Enem?"); ganchos alternativos de G1-02 e G2-02 ("Enem de 2010 em diante vale para entrar na Ufape") e de G1-06 e G2-04 ("Já fez o Enem? Sua nota pode ser a sua entrada") | Enem como forma de entrada sem a condição completa. Briefing, regra 5: sempre "média mínima de 300 pontos, edições de 2010 em diante" | Trocar por "ou nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)". Nos Stories e cartões: "Nota do Enem de 2010 em diante, com média mínima de 300 pontos". Ganchos alternativos: incluir a condição ou descartar |
| P2 | alta | CTAs de G1-01, G1-02, G1-04, G1-06, G1-07, G1-09, G1-10, G2-04 e G2-07; G1-05, arte cartão 5 | "aceite do responsável", e o edital e o briefing (correção 6) usam "representante legal" | Usar o B-MENOR do próprio arquivo: "Candidato menor de idade precisa do aceite do representante legal na inscrição e na matrícula." Cartão 5: "Menor de idade? O representante legal dá o aceite na inscrição e na matrícula" |
| P3 | alta | G1-03 e G1-08 (chamam para inscrição no G1) | Sem a regra do aceite do menor, que o briefing exige em "toda peça e mensagem de inscrição e matrícula" e a regra 7 do próprio arquivo pede | Acrescentar o B-MENOR na chamada. No G2 (público adulto), recomendado acrescentar nos posts com inscrição (G2-01, G2-02, G2-03, G2-05, G2-06), conforme o cmo ("mantendo a informação do edital quando couber") |
| P4 | alta | G1-08, linha final ("Quer ver a regra de renovação por escrito antes de se inscrever?"); G2-05, linha final ("Quer a regra de renovação por escrito?"); G1-07, linha final ("Quer a regra completa do desconto por escrito?") | Promete um documento de regra de renovação que não existe: é a proposta P1 da oferta, não aprovada ("nenhuma proposta pode aparecer em peça") | G1-08 e G2-05: "Tem dúvida sobre a renovação? Fale com a nossa equipe." G1-07: "A regra completa está no edital. Dúvidas? Fale com a nossa equipe." |
| P5 | alta | G1-02 e G2-02, campo "Data de publicação" | Datas do Enem 2026 no gancho, marcadas [CONFIRMAR], sem bloqueio | Escrever "BLOQUEADO até a confirmação das datas do Enem 2026 por fonte oficial". Sem a confirmação antes de 08/11, o post não sai |
| P6 | alta | G2-01 a G2-07, campo "Data de publicação"; G1-03, campo "Data de publicação" | A nota da seção 3 diz que a chamada para a página só sai depois de G6, mas cada post do G2 traz "Link na bio" com a URL da LP e nenhum BLOQUEADO. O G1-03 traz só "Recomendado só depois da correção" (G8). Conformidade: a página precisa entregar o que o post promete | G2: "BLOQUEADO até G6" em cada post, ou chamada alternativa sem a LP (WhatsApp de Vendas Goiânia, depois de [CONFIRMAR] o canal ativo), aprovada pelo humano. G1-03: "BLOQUEADO até G8", igual ao G1-08 |
| P7 | média | Seção 1.1 e G1-04 | O G1-04 (kit 2) está bloqueado por G11 e não há substituto. O plano do cmo (5.1) pede: "sem essa confirmação, troca por projetos extensionistas desde o 1º semestre". Sem ele, o kit mínimo do G1 cai para 5 posts publicáveis | Escrever o G1-04-alt: Projeto Extensionista I no 1º semestre dos dois turnos (conferido na ficha), sem hospital, com a mesma chamada corrigida (P1, P2) |
| P8 | média | Seção 1 (fase de captação "27/10 a 06/12/2026") e datas de G1-01, G2-01, G1-02, G2-02 e G1-03 | Datas antes do QA (10/11), da aprovação (11 a 13/11) e do início da captação (16/11) do plano do cmo | Alinhar a captação a 16/11/2026 ou escrever em cada post "publica só depois da aprovação humana; se a aprovação vier depois da data, a sequência anda junto". G1-02 e G2-02 dependem também de P5 |
| P9 | baixa | G2-06, corpo e arte (cartões 2 e 5) | "Fundamentos da Educação Infantil" e "Gestão escolar" não são nomes de componentes da matriz | Usar os nomes da ficha: "Fundamentos Teóricos e Metodológicos da Educação Infantil" e "Princípios e Métodos de Gestão Escolar Integrada", ou trocar "Alguns conteúdos da matriz" por "Alguns temas da matriz" |
| P10 | baixa | G1-05, arte cartão 2 | Ato sem a data de publicação no D.O.U. | "Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025)" |
| P11 | baixa | G1-10 (09/02/2027) e G2-07 (10/02/2027) | 09/02/2027 é terça de Carnaval e 10/02 é quarta de cinzas [SUPOSIÇÃO: calculado pela Páscoa de 28/03/2027] | Mover para 11/02 e 12/02/2027, ou conferir o calendário |
| P12 | baixa | Campos "Ponto de vista" de G1-01, G1-03, G1-04, G2-03 e G2-06 | Marcas [CONFIRMAR NO CATÁLOGO] para disciplinas e semestres | Este QA conferiu na ficha: batem (salvo P9). A marca pode virar "conferido na ficha do curso em 26/10/2026"; o horário das práticas do noturno continua [CONFIRMAR NO CATÁLOGO] |

Veredito do arquivo 1: **CORRIGIR**. Volta para o posts-sociais.

---

## 3. Arquivo 2: campanhas-de-nutricao-graduacao-2026-10-26.md

### 3.1 auditorias/07-email-e-whatsapp.md, item por item

- [ ] **Consentimento e descadastro funcionando.** FE e FW estão bem escritos e toda mensagem de WhatsApp termina com "Para não receber mais mensagens, responda SAIR" (conferido em todas, G1 e G2). Mas o opt-in registrado, o consentimento de menor (G10) e o teste do SAIR e do descadastro dependem do CRM. Bloqueia o envio.
- [x] **Cada mensagem tem um objetivo.**
- [ ] **Assuntos e primeiras linhas honestos.** Sem vagas acabando, prazo inventado ou aprovação certa. Falham: primeiras linhas e pré-visualizações com Enem sem a condição (N9); gancho do AT3 com afirmação não verificada ("geralmente", N11).
- [ ] **Segmentos recebem mensagens relevantes para a etapa.** Réguas por etapa corretas. Falha: contato menor de idade em mensagens sem versão "-R" não tem regra, e as versões "-R" do G2 não foram escritas (N6).
- [x] **Réguas têm regras de saída.** Seção 5 completa (SAIR, descadastro, sem engajamento, menor sem consentimento, não aprovado).
- [x] **Resultados registrados para cada envio.** Não se aplica ao rascunho; plano de registro na seção 6.
- [ ] **Cliques, respostas e conversões medidos.** Definidos na seção 6, mas dependem de G13 e falta utm_content por mensagem (N15).
- [ ] **WhatsApp em horário comercial, frequência humana e template aprovado pela Meta.** Horário e frequência escritos (FW). Nenhum template submetido nem aprovado. Bloqueia o envio.

### 3.2 auditorias/06-geracao-de-demanda.md, item por item

- [x] **Toda campanha tem um briefing escrito** (estrategia-de-campanha-graduacao-2026-10-26.md).
- [ ] **Metas definidas antes do lançamento.** Piso de 30 por turma; alvos e taxas [CONFIRMAR] (G2, G3).
- [x] **A isca digital entrega a promessa do título.** Não há isca; {link_passo_a_passo} só entra se existir.
- [x] **Toda captura de lead tem nutrição em seguida.**
- [x] **Plano de distribuição por peça.**
- [x] **Regras das comunidades respeitadas.** Não se aplica.
- [x] **Revisão no ponto de checagem realizada.** Não se aplica ainda: C0 é 30/10/2026.
- [ ] **Consentimento coletado em todo formulário.** Formulário da LP não confirmado (G10, G13).
- [ ] **Bolsas, descontos e prazos batem com o catálogo e a ficha da oferta.** Falham: desconto incompleto (N1), "dia 10" e reajuste na Pedagogia contra a oferta 0.1, que marca [CONFIRMAR] (N3), matrícula sem "a partir de" (N8).

### 3.3 auditorias/conformidade-educacional.md, item por item

DADOS DO CURSO
- [x] Nome, modalidade, carga horária, duração e turno batem; carga horária da Pedagogia ausente.
- [x] Os dois cursos estão "aberto".
- [x] Modalidade presencial clara; até 30% a distância informado sem esconder.

REGULAÇÃO (MEC)
- [x] Atos e credenciamentos do catálogo e dos editais; reconhecimento não citado. Ajuste de forma em L4 e G2-L4 (N13).
- [x] Pós lato sensu: não se aplica.
- [x] Curso livre: não se aplica.
- [x] Nenhuma nota do MEC.

PROMESSAS E PROVAS
- [x] Nenhuma promessa de emprego, salário, aprovação ou concurso. As promessas não verificadas ("regras de renovação por escrito", N4; "dá para fazer pelo celular", em [CONFIRMAR] no A2) bloqueiam pela regra do QA.
- [x] Nenhum dado de empregabilidade ou satisfação.
- [x] Nenhum superlativo.
- [x] Comparação com EAD (G2-L6, 4.3) só por atributos verificáveis, sem preço de terceiros.

PREÇO E CONDIÇÕES (CDC)
- [ ] Preço com condições completas: falha em L4, L4-R, L6, L7, A6, G2-L4, G2-L6, G2-L7, G2-A6; desconto citado sem valores em A1, A2, A4-R, M1, G2-A1, G2-A2, G2-M1 (N1). Mensagens com preço sem bloqueio G12 e G7 (N2).
- [ ] Desconto com regra e validade: Pedagogia com "vencimento (dia 10)" e "reajuste previsto em dezembro" sem fonte (N3).
- [x] Urgência só real.
- [x] Prouni, Fies e financiamento não são afirmados; a resposta 4.1 só diz que não há informação confirmada.

PESSOAS E DADOS
- [x] Nenhuma foto, vídeo, depoimento ou docente.
- [ ] Menores: "responsável legal" em vez de "representante legal" (N5); versões para o responsável incompletas e sem regra para mensagens sem "-R" (N6); consentimento de menor no CRM pendente (G10).
- [ ] Formulários com finalidade e política de privacidade: {link_politica} no rodapé, formulário da LP não confirmado (G13).
- [ ] WhatsApp e e-mail só com consentimento: regra escrita, registro depende do CRM (G10).
- [x] Nenhum dado pessoal (só variáveis).

PLATAFORMAS
- [x] Não é anúncio; nenhuma frase afirma característica de quem recebe.
- [ ] Página de destino entrega o que a mensagem prometeu: mensagens do G2 com {link_lp_utm} sem bloqueio G6 (G2-L1 deixa "o time decide"); mensagens do G1 que oferecem o noturno levam à página com "INTEGRAL" no turno (G8) (N7).

ANÚNCIOS (META E GOOGLE)
- [x] Não se aplica à régua.

RESULTADO: Bloqueado. Revisado por: qa-de-marketing (agente). Revisão humana: pendente. Data: 26/10/2026.

### 3.4 Lista de correções (nutrição)

| # | Prioridade | Onde | Problema | Correção proposta |
|---|---|---|---|---|
| N1 | alta | G1-L4 e L4-R ("de R$ 10.000,00 por R$ 5.000,00 (integral) ou R$ 4.000,00 (noturno), só no 1º semestre de 2027"); G1-L6 (só valor cheio); G1-L7 (sem perda no atraso); G1-A6 ("{total_semestre_desc} no semestre, de R$ 60.000,00"); G2-L4, G2-L6, G2-L7, G2-A6 (mesmas faltas); G1-A1, A2, A4-R, M1 e G2-A1, A2, M1 (desconto citado sem valores) | Desconto sem os seis elementos: valor cheio, valor com desconto, percentual, validade do 1º semestre de 2027, renovação semestral e perda no atraso | Colar {bloco_preco} (e-mail) ou, no WhatsApp, a linha: "De R$ 10.000,00 por R$ 5.000,00 por mês no integral (50%) ou R$ 4.000,00 no noturno (60%), só no 1º semestre de 2027. Renovação a cada semestre, com comprovação. O desconto é perdido no mês pago depois do vencimento. Regras no Programa de Desconto de Mensalidade 2027/1 (Edital 003/2026)." Pedagogia: "De R$ 1.050,00 por R$ 525,00 por mês (50%)", com o mesmo resto e o nome do programa de Goiânia (sem "dia 10", ver N3). Em A1, A2, A4-R e M1, ou incluir a linha ou tirar a menção ao desconto |
| N2 | alta | Toda mensagem com preço: G1-L3, L4, L6, L7, R5, A3, A6, M1, M4 e as equivalentes do G2; respostas 4.2 e 4.3 de preço; G1-L3 e G2-L3, texto "[CONFIRMAR efeito sobre 2027/1]" dentro do corpo | Sem bloqueio G12 (reajuste de dezembro) e G7 (erros dos Editais 003/2026), ao contrário dos posts de preço. Marca interna dentro do texto que vai ao candidato | Acrescentar em cada uma: "BLOQUEADO para envio até G12 e G7". Tirar a marca do corpo e deixá-la como nota da mensagem |
| N3 | alta | BP-PED ("vencimento (dia 10)"); G2-L3 ("dia 10" e "reajuste previsto em dezembro"); G2-L6 ("tem reajuste previsto em dezembro"); G2-A3 (BD com R$ 1.050,00, que inclui o reajuste); G2-M4 ("vence no dia 10") | A ficha da oferta (0.1) marca vencimento e reajuste da Pedagogia como [CONFIRMAR com a Ufape: vencimento e reajuste no Edital 004/2026]; a ficha dos editais não os traz para Goiânia | Tirar "dia 10" e o reajuste dos textos do G2 até a confirmação. G2-M4: BLOQUEADO até a Ufape confirmar o vencimento |
| N4 | alta | BD ("peça ao time as regras de renovação por escrito"); G1-L6 ("o time te passa as regras de renovação por escrito"); G2-L6 ("O time passa as regras de renovação por escrito"); 4.1, linha "E depois do 1º semestre?" ("confirmo por escrito antes da matrícula") | Promete documento de regra de renovação que não existe (proposta P1, não aprovada) | Usar o texto da oferta 0.3: "Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação." |
| N5 | alta | BM; AT1-R; AT2-R; L4 e L4-R; A4-R; G2-L4; 0.1 item 7; 4.1, linha do menor | "responsável legal"; o edital e o briefing usam "representante legal" | BM: "Se o candidato for menor de idade, a inscrição e a matrícula precisam do aceite do representante legal." Trocar em todas as ocorrências. "Responsável" pode seguir só como nome da versão "-R" |
| N6 | alta | Seção 0.5; G2 (parágrafo "As versões para o responsável do G2 seguem os textos do G1..."); G1-R1-R, A1-R e M1-R (só descritas); G1-AT2-R, follow-up (cita "AT3-R", que não existe) | As versões "-R" do G2 não estão escritas, três do G1 só estão descritas e não há regra para candidato menor nas mensagens sem "-R" (L1 a L7, salvo L4; R2 a R5; A2, A3, A5, A6; M2 a M5). O QA não aprova texto que não existe | Escrever por extenso todas as "-R" do kit mínimo (5 WhatsApp e 3 e-mails por liberação) e as citadas. Em 0.5, regra: "mensagem sem versão -R não vai a contato menor de idade nem ao representante legal dele". Corrigir o follow-up do AT2-R |
| N7 | alta | G2-L1 ("o time decide se envia antes da correção"), G2-L2, G2-L3, G2-L5, G2-L7 e o botão do template do G2-L4 ({link_lp_utm} de Pedagogia); G1-L1, L3, L4 e L7 (oferecem o noturno e levam à LP) | Página de Pedagogia com texto de modelo (G6) e bloco do noturno com "INTEGRAL" (G8): a página não entrega o que a mensagem promete. Os posts equivalentes estão bloqueados | G2: "BLOQUEADO para envio com link da LP até G6"; até lá, a chamada vira resposta à mensagem. G1: mesmo tratamento dos posts G1-03 e G1-08 para o trecho do noturno: "bloqueado até G8", ou link sem a LP aprovado pelo humano |
| N8 | média | G1-L1 e G2-L1, passo 4 ("Matrícula eletrônica, 2 dias depois do resultado"); G1-L7 e G2-L7 ("matrícula 2 dias depois") | Falta "a partir de" (edital: matrícula a partir de 2 dias após o resultado) | "Matrícula eletrônica a partir de 2 dias depois do resultado" |
| N9 | média | Pré-visualizações de AT1, G2-AT1, R1, G2-R1 ("nota do Enem de 2010 em diante") e de L1, G2-L1 ("ou nota do Enem"); primeira linha B de AT2 e G2-AT2 e primeira linha A de L2 e G2-L2 ("Já fez o Enem? Sua nota pode ser a sua entrada...") | Enem sem a condição completa em texto que aparece sozinho na notificação | Incluir "(média mínima de 300 pontos, edições de 2010 em diante)" ou, por espaço, "com média mínima de 300 pontos" e a condição completa na linha seguinte |
| N10 | média | G1-L5-alt e G1-M3 ("Campos de Atuação do Médico Veterinário"); G1-L5-alt marcado "enviável hoje" com "[CONFIRMAR NO CATÁLOGO]" e "(ficha do curso)" no corpo; "(ficha do curso)" também no corpo de G2-L5, G2-L6 e G2-M3 | Nome da disciplina na ficha: "Campos de Atuação do Médico Veterinário e Práticas Hospitalares". Marcas internas dentro do texto que vai ao candidato | Usar o nome da ficha. Tirar as marcas do corpo e passá-las para uma nota da mensagem. O QA conferiu a matriz citada na ficha: o resto bate |
| N11 | média | G1-AT3, gancho ("Quem trava na redação geralmente tem uma dessas dúvidas.") | Afirmação sobre comportamento sem dado ([SUPOSIÇÃO] no próprio texto) | "Três respostas do edital sobre a redação." |
| N12 | baixa | FE, rodapé único | Cita "Vestibular 2027" e só o endereço de São Paulo, mas vale também para os e-mails do G2 | Criar o rodapé do G2: "...se cadastrou no Processo Seletivo 2027.1 da Faculdade UFAPE em Goiânia...". Razão social, CNPJ e sede seguem iguais (ufape-geral.md) |
| N13 | baixa | G1-L4 e G2-L4, linha do ato | Ato sem a data de publicação no D.O.U. | "Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025)"; "Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022)" |
| N14 | baixa | 4.2, linha "Posso visitar a faculdade?" | Resposta em primeira pessoa errada ("Posso fazer a inscrição presencialmente") | "Você pode fazer a inscrição presencialmente, de segunda a sexta, das 9h às 18h..." |
| N15 | baixa | 0.2, variável {link_lp_utm}; seção 6 | A medição é por mensagem, mas a UTM não tem utm_source, utm_medium e utm_content por canal e mensagem | Propor: utm_source=email ou whatsapp, utm_medium=crm, utm_campaign=grad_<curso>_regua_202611, utm_content=código da mensagem (ex.: g1-l3) [SUPOSIÇÃO de nomenclatura; a plataforma gera a final, G13] |
| N16 | baixa | G1-A6 e G2-A6, gancho ("Se você ainda quer a vaga, falta pouco.") | Pode ser lido como escassez de vaga | "Para começar em 22/02/2027, faltam estes passos." |

Veredito do arquivo 2: **CORRIGIR**. Volta para o campanhas-de-nutricao (e, depois, para o copy-de-mensagens, que lapida os textos).

---

## 4. Consistência entre peças, briefing, oferta, criativos e plano do cmo

### 4.1 Bloqueios do plano do cmo

| Pedido | O que o cmo bloqueia | Posts | Nutrição |
|---|---|---|---|
| G6 (página de Pedagogia) | Anúncio pago do G2; página precisa entregar o prometido | Nota geral na seção 3, mas nenhum post do G2 traz BLOQUEADO (P6) | Sem bloqueio; G2-L1 deixa a decisão ao time (N7) |
| G8 (turno do noturno na página) | Anúncio pago do noturno | G1-08 bloqueado; G1-03 só "recomendado" (P6) | Sem tratamento para o noturno nas mensagens com LP (N7) |
| G10 (menores) | Regras para menor e consentimento no CRM | Não se aplica (sem envio); texto do aceite com termo errado (P2) | Envio a menor suspenso, ok; termo errado e "-R" incompletas (N5, N6) |
| G11 (hospital e imagem) | Hospital só depois da confirmação | G1-04 bloqueado, ok; falta substituto do kit (P7) | Linha opcional no L5-alt, ok; resposta 4.2 sobre o hospital condiciona o uso a G11, ok |
| G12 (reajuste de dezembro) | Preço estável até 22/02/2027 | G1-07, G1-08, G1-09, G2-05 bloqueados, ok | Nenhuma mensagem bloqueada (N2) |
| G13 (URL com UTM e origem no CRM) | Medição por canal e peça | Pendência geral declarada, ok | Pendência declarada; falta UTM por mensagem (N15) |

### 4.2 Briefing, oferta e criativos

- **Enem:** briefing (regra 5 e correção 3) e criativos (regra 4) exigem a condição completa sempre. Posts e nutrição divergem em chamadas, Stories, pré-visualizações e primeiras linhas (P1, N9).
- **Menor:** briefing (correção 6), oferta (0.1) e criativos (B-MENOR) usam "representante legal". Posts usam "responsável" e nutrição usa "responsável legal" (P2, N5).
- **Renovação:** a oferta (0.3 e seção 4) proíbe divulgar a P1 ("regra de renovação por escrito"). Posts G1-07, G1-08 e G2-05 e nutrição BD, L6 e G2-L6 prometem o documento (P4, N4).
- **Pedagogia:** a oferta (0.1) deixa vencimento e reajuste da Pedagogia em [CONFIRMAR]. Os posts respeitam (B-DESC-PED sem "dia 10"); a nutrição não (N3). Há, portanto, divergência entre os dois arquivos.
- **Textos do desconto:** B-DESC-INT, B-DESC-NOT e B-DESC-PED dos posts são iguais aos blocos dos criativos e da oferta 0.2. BP-INT e BP-PED da nutrição acrescentam o valor do semestre e "(dia 10)": correto para a Medicina Veterinária, a corrigir na Pedagogia (N3).
- **Matriz:** posts, criativos e nutrição citam os mesmos componentes. A nutrição separa "Campos de Atuação do Médico Veterinário" do nome real da disciplina (N10); a oferta (1.4) traz o nome certo.
- **Destino:** posts e criativos usam as mesmas URLs base com UTM; nutrição usa a variável. Todos dependem de G13.
- **Atos:** os três arquivos usam o mesmo texto do catálogo; só as versões curtas (arte G1-05, L4, G2-L4) omitem o D.O.U. (P10, N13).
- **Calendário:** criativos e cmo começam a captação em 16/11/2026. Os posts começam em 03/11 (P8). A nutrição começa a ativação da base em 03/11 com aprovação própria, o que o plano do cmo permite (ativação fora da ordem, por prioridade GUT).

### 4.3 Pendências externas (não dependem dos agentes; bloqueiam publicação e envio mesmo depois das correções)

- G6 e G8 (páginas), G7 (Editais 003/2026), G10 (consentimento de menor no CRM), G11 (hospital e imagem), G12 (reajuste), G13 (URL, UTM, origem e formulário), G14 (aprovadores, tabela vazia em ufape-geral.md).
- Datas oficiais do Enem 2026 e da divulgação das notas.
- Templates de WhatsApp submetidos e aprovados pela Meta; opt-in registrado no CRM.
- Vencimento e reajuste da Pedagogia no Edital 004/2026.

### 4.4 Encaminhamento

- posts-sociais-graduacao-2026-10-26.md: volta para o **posts-sociais**, com P1 a P12.
- campanhas-de-nutricao-graduacao-2026-10-26.md: volta para o **campanhas-de-nutricao**, com N1 a N16; depois segue para o copy-de-mensagens.
- Nova rodada de QA (...-d) depois das correções. Só então as peças seguem para a aprovação humana, com as pendências externas da seção 4.3 ainda bloqueando a publicação e o envio.

---

## Lista 1. Fatos (com fonte)

- Inscrição gratuita desde 17/08/2026; redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0; Enem com média aritmética mínima de 300 pontos, edições de 2010 em diante (contexto/cursos/graduacao/editais-2027-1.md, Editais 002 e 004/2026).
- Matrícula eletrônica a partir de 2 dias depois do resultado, com a 1ª mensalidade e a assinatura digital do contrato; documentos em até 30 dias; aulas em 22/02/2027; turma mínima de 30 com reembolso da 1ª parcela; devolução de 80% se o cancelamento for pedido até 2 dias antes das aulas (idem).
- Candidato menor de idade precisa do aceite do representante legal na inscrição e na matrícula (Edital 002/2026; briefing, correção 6; oferta 0.1; criativos B-MENOR).
- Medicina Veterinária: de R$ 10.000,00 por R$ 5.000,00 (integral, 50%) ou R$ 4.000,00 (noturno, 60%) por mês no 1º semestre de 2027; vencimento no dia 10; reajuste em dezembro; 4.195 h + 75 h; Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) (catálogo, seção 1; Editais 002 e 003/2026).
- Pedagogia: de R$ 1.050,00 por R$ 525,00 por mês (50%) no 1º semestre de 2027; Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022); carga horária em [CONFIRMAR] (catálogo, seção 1). Vencimento e reajuste da Pedagogia: [CONFIRMAR] (oferta 0.1).
- Desconto: só 1º semestre de 2027, todas as formas de ingresso, renovação a cada semestre com comprovação, perda no mês pago com atraso, sem acúmulo com programa governamental (Editais 003/2026).
- Matriz da Medicina Veterinária: Práticas Hospitalares e Projeto Extensionista I no 1º semestre dos dois turnos; disciplina "Campos de Atuação do Médico Veterinário e Práticas Hospitalares"; estágio no 7º e 8º (integral) e 9º e 10º (noturno); o bloco do noturno mostra "INTEGRAL" no turno (contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md, conferido por este QA).
- Matriz da Pedagogia: Prática Docente I a VIII; Projeto Integrador I a VII; Estágio Curricular Supervisionado Obrigatório a partir do 6º semestre; "Fundamentos Teóricos e Metodológicos da Educação Infantil", "Alfabetização e Letramento", "Literatura Infantil", "Educação Inclusiva", "Letramento em Libras", "Educação de Jovens e Adultos - EJA", "Princípios e Métodos de Gestão Escolar Integrada"; a página tem trechos de modelo e o bloco do egresso copiado (contexto/cursos/graduacao/graduacao-em-pedagogia.md, conferido por este QA).
- A proposta P1 (regra de renovação por escrito) não está aprovada e não pode aparecer em peça (oferta, seção 4).
- Bloqueios G6, G7, G8, G10, G11, G12 e G13, calendário (QA em 10/11, aprovação de 11 a 13/11, captação a partir de 16/11/2026) e kit com substituto do hospital (cmo-graduacao-2026-10-26.md, seções 5, 6 e 8).
- 26/10/2026 é segunda-feira; 22/02/2027 é segunda-feira; 08/11 e 15/11/2026 são domingos (calendário).

## Lista 2. Suposições

- [SUPOSIÇÃO] Carnaval de 2027 em 09/02 (terça), calculado pela Páscoa de 28/03/2027; afeta G1-10 e G2-07.
- [SUPOSIÇÃO] Nomenclatura de UTM proposta para a régua (N15); a plataforma gera a final.
- [SUPOSIÇÃO] A ausência de travessão e meia-risca foi verificada por leitura integral dos dois arquivos, sem busca automática.
- [SUPOSIÇÃO] Para o G2 (público adulto), a regra do menor nos posts fica como recomendação, seguindo o cmo ("quando couber"); no G1 é obrigatória pelo briefing.

## Lista 3. Dados que faltam

- [CONFIRMAR] Datas oficiais do Enem 2026 e da divulgação das notas (G1-02, G2-02 e slot reservado).
- [CONFIRMAR] Efeito do reajuste de dezembro sobre 2027/1 (G12) e correção dos Editais 003/2026 (G7).
- [CONFIRMAR] Vencimento e reajuste da Pedagogia no Edital 004/2026.
- [CONFIRMAR] Correção da página de Pedagogia (G6) e do turno do noturno (G8).
- [CONFIRMAR] Consentimento de menor no CRM e campos de menor e representante legal (G10); opt-in registrado; templates aprovados pela Meta.
- [CONFIRMAR] Uso da Ufape Clínica pela graduação e autorização de imagem (G11).
- [CONFIRMAR] URL que recebe a UTM, origem no CRM, finalidade e política de privacidade no formulário da LP (G13).
- [CONFIRMAR] Aprovadores de posts, mensagens em massa e peças com ato regulatório (G14).
- [CONFIRMAR] Se o pedido de cancelamento com 80% pode ser feito em 20/02/2027, que é sábado.
- [CONFIRMAR NO CATÁLOGO] Carga horária da Pedagogia (G5); horário das práticas e do estágio do noturno.
- [CONFIRMAR] Canal de WhatsApp de vendas ativo em São Paulo e Goiânia (instabilidade informada em 22/10/2026) e perfil de Goiânia no Instagram.
