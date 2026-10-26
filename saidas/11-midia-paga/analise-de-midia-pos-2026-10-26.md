# Revisão de mídia da Pós-graduação: diagnóstico estrutural das campanhas ativas e pausadas e roteiro de leitura para quando os números chegarem (etapa 1.12)

- **Agente:** analise-de-midia (departamento 11 Mídia Paga, reporta ao gestor-de-midia)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Etapa:** 1.12 da camada 1 do plano do cmo (diagnostico-de-midia nas campanhas ativas e pausadas)
- **Versão:** 2 (26/10/2026), aplica a seção 12 do plano do cmo e os ajustes do qa (encomenda de 12.10 para as análises de mídia: tabela de correspondência entre nomes antigos e o padrão D12, datas de 68662 e 662 pela planilha e leitura de leilão de NE1 e NE4; ajustes AM1 e AM2 do qa-de-marketing-geral-2026-10-26-loteB). O que mudou está na seção "Mudanças desta versão", no fim.
- **Status:** rascunho para o gestor-de-midia, para o qa-de-marketing (auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda ação em gerenciador de anúncios é feita por humano, depois da aprovação.
- **Natureza:** não existe nenhum número de desempenho nas fontes (gasto, impressões, cliques, CPM, CTR, CPL, leads, matrículas, custo por matrícula). A exportação pedida no memorando do gestor (seção 7.1) ainda não chegou. Por isso este diagnóstico é estrutural: cruza o que a visão de campanhas mostra (campanha, status, início, formatos, ângulos) com o catálogo (status da turma, página de destino, data e link) e escreve, antes dos números, o roteiro exato de leitura (métricas, cortes, limiares e a decisão que cada resultado dispara). Todo número de desempenho aparece como [DADO NÃO FORNECIDO] ou [CONFIRMAR]. Nenhuma métrica foi inventada.
- **Entradas lidas:**
  - /home/user/marketing-ufape/.claude/agents/analise-de-midia.md
  - /home/user/marketing-ufape/.claude/skills/diagnostico-de-midia/SKILL.md
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md
  - /home/user/marketing-ufape/docs/andamento-planejamento.md
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 3, com a tabela "Status da mídia paga por item do recorte", e seções 7 e 8)
  - /home/user/marketing-ufape/contexto/ufape-geral.md
  - /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seção 2)
  - /home/user/marketing-ufape/docs/visao-de-campanhas-2026-10-26.md
  - /home/user/marketing-ufape/docs/auditoria-do-catalogo-2026-10-26.md (seções 3, 4 e 9)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (1.11)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-geral-2026-10-26.md (memorando da onda 1, versão 2)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analise-de-campanha-pos-2026-10-26.md (1.32)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (1.10)
  - /home/user/marketing-ufape/auditorias/11-midia-paga.md
  - Versão 2: /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12); /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-loteB.md (AM1 e AM2); /home/user/marketing-ufape/saidas/11-midia-paga/analise-de-midia-eventos-2026-10-26.md (NE1, NE4 e EA3)
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web. Nenhuma exportação de plataforma ou de CRM recebida.
- **Dados pessoais:** nenhum lido nem citado. Nenhum docente, aluno, candidato ou lead aparece aqui.
- **Marcadores:** [DADO NÃO FORNECIDO] é número de desempenho que só a exportação traz. [CONFIRMAR] é fato que a Ufape precisa informar. [SUPOSIÇÃO] é hipótese deste agente, com a origem. "Regra prática" é regra de método da skill, não meta.
- **Nomes:** os cursos aparecem no padrão "Pós-graduação em <área>" (contexto da linha). Grafias do catálogo diferentes do padrão: "Pós Graduação" em 706, 341, 333 e 68629; "Pós-graduação Cirurgia Cardiorrespiratória", sem "em", em 659; "Pós-Graduação Inteligência Artificial na Saúde" em 719. O código identifica a turma.

---

## 0. Resumo em duas frases

Das 14 campanhas ativas da Pós na visão, 8 (57,1%) têm um bloqueio que vem antes de qualquer número: 6 rodam em turma que já começou e está com status "verificar" no catálogo, e 2 levam a página com data ou link que não bate com a planilha (698 e 662); das 6 restantes, só 3 (68608, 68610 e 289) têm mais de 30 dias até o início. O gargalo principal hoje não é leilão, criativo nem conversão: é elegibilidade e destino (o elo "chegada" da skill), e só depois de corrigir esse elo é que gasto, CTR e CPL passam a valer como evidência.

---

## 1. Regras de leitura aplicadas (escritas antes dos números)

1. **Sem número, sem decisão de desempenho** (memorando, regra 1; analise-de-campanha, R0). As decisões deste arquivo são de elegibilidade, conformidade e calendário. Nenhuma campanha é chamada de boa ou ruim.
2. **Dados suficientes** (skill, passo 2, regra prática): perdedor só depois de gastar de 1,5 a 2 vezes o CPL máximo sem lead; diferença entre anúncios com menos de 10 a 20 conversões de cada lado é ruído; janela mínima de 3 a 7 dias; os 2 últimos dias subcontam conversões (gestor 1.11, seção 8, item 7).
3. **Funil de cima para baixo:** entrega, atenção, interesse, chegada, conversão, matrícula, saturação. O primeiro elo fraco é a causa provável; o resto é consequência.
4. **Uma mudança por vez no mesmo conjunto,** no máximo uma por semana. Correção de conformidade é a única exceção (memorando, regra 3).
5. **Plataforma, analytics e CRM não batem: a decisão é INVESTIGAR,** e nenhuma decisão de desempenho vale até resolver.
6. **Não culpar o algoritmo antes de checar criativo, página e rastreamento** (instrução do agente).
7. **Julgar contra a meta escrita antes,** nunca contra o resultado visto depois (gestor 1.11, seção 8, item 9).

---

## 2. Metas contra realizado

As metas da Pós existem como fórmula no plano 1.11 (seção 2), sem valor em reais, porque faltam evasão, desconto, custo variável, margem e conversão (PP1). Não recalculei nada com a skill metas-de-custo: o gestor já fez a conta pronta e este arquivo só a usa.

| Frente | Meta (fonte) | Valor da meta | Realizado |
|---|---|---|---|
| 6 turmas iniciadas com campanha ativa | sem meta: decisão por elegibilidade (memorando, D1) | não se aplica | gasto acumulado e da última semana [DADO NÃO FORNECIDO] |
| Reta final (707, 68604, 68606, 698, 68608, 68610) | matrículas até a turma mínima de 15 (decisão 11 da Ufape) e custo por matrícula máximo (memorando, 7.3) | [CONFIRMAR] | matrículas, leads, gasto [DADO NÃO FORNECIDO] |
| Ativas fora da onda 1 (289, 662) | CPLmax e CMmax do cenário conservador (1.11, seção 2.3) | [CONFIRMAR]; conta pronta por ponto de conversão em 1.11, seção 2.4 | [DADO NÃO FORNECIDO] |
| Pausadas em turma futura (12) | mesma regra, só para leitura do histórico antes da pausa | [CONFIRMAR] | histórico [DADO NÃO FORNECIDO] |
| Provas de bolsa de 27/11/2026 | custo por inscrito máximo (1.11, fórmula 8) | [CONFIRMAR] | campanha ainda não existe |

Referência que já dá para usar sem inventar nada (1.11, seção 2.4, só aritmética do catálogo): na 289, cada ponto percentual de conversão lead para matrícula põe o CPL teto em R$ 356,50 no cenário base e em R$ 144,10 no conservador. Isso é teto absoluto, sem evasão, desconto, custo nem margem: a meta real é menor.

---

## 3. Retrato estrutural da mídia da Pós

### 3.1 Contagem (visão de campanhas de 26/10/2026)

| Situação | Turma já iniciada | Turma futura | Total |
|---|---|---|---|
| Campanha ativa | 6 (650, 68662, 706, 586, 554, 68612) | 8 (707, 68604, 68606, 698, 68608, 68610, 289, 662) | 14 |
| Campanha pausada | 6 (653, 665, 666, 68605, 659, 68607) | 12 (657, 68615, 341, 333, 679, 68635, 366, 68617, 578, 382, 352, 60) | 18 |
| Sem campanha | 2 (677, 564) | 8 (68628, linha "Pneumologia 10/04/2027", 68632, 68609, 68616, 719, 68623, 699) | 10 |
| **Total** | **14** | **28** | **42** |

Conferido linha a linha na visão e igual à contagem da analise-de-campanha (1.32, seção 1.1). Fora da visão: as 22 provas de bolsa de 27/11/2026, 68636, 68629 e 359 (plano do cmo, seção 3).

**Quebra por plataforma:** a visão não diz em que plataforma cada campanha roda (Meta, Google Busca, Performance Max, YouTube). Plataforma, objetivo e evento de otimização de cada uma: [CONFIRMAR] na exportação. Sem isso, a quebra por plataforma pedida pelo método não pode ser feita.

### 3.2 As 14 ativas cruzadas com o catálogo

Dias até o início contados em 26/10/2026 pela data da planilha (via catálogo). "1ª mensalidade" é a conta de 30 dias antes do início, porque "na maioria das páginas, a 1ª mensalidade é paga 30 dias antes do início" (contexto da linha); se essa data é prazo de matrícula, é [CONFIRMAR] por turma. "Frase MEC" indica se a página de destino está na lista de 46 páginas com a frase de certificação ligada ao MEC (auditoria do catálogo de 26/10, seção 9).

| Código | Turma (catálogo) | Início | Dias | Status no catálogo | Formatos e ângulos (visão) | Página de destino | Frase MEC | 1ª mensalidade (30 dias antes) | Bloqueio antes dos números |
|---|---|---|---|---|---|---|---|---|---|
| 650 | Pós-graduação em Medicina de Felinos, VI | 15/08/2026 | -72 | verificar | estático, sem 5 | sem alerta de data | sim | já passou | **elegibilidade** |
| 68662 | Pós-graduação em Odontologia Veterinária, V | 15/08/2026 | -72 | verificar | estático, sem 5 | **site mostra 24 e 25/04/2027, turma V** (link trocado) | sim | já passou | **elegibilidade e destino** |
| 706 | Pós-graduação em Ultrassonografia de Pequenos Animais, II | 15/08/2026 | -72 | verificar | estático, sem 5 | sem alerta; a turma III (68629, 22/05/2027) só existe no site | sim | já passou | **elegibilidade** |
| 586 | Pós-graduação em Anestesiologia Veterinária (Direto ao ponto), EAD, I | 22/08/2026 | -65 | verificar | estático, sem 5 | sem alerta | não | já passou | **elegibilidade** |
| 554 | Pós-graduação em Dor e Cuidados Paliativos na Veterinária, III | 22/08/2026 | -65 | verificar | estático e vídeo, sem 5 | sem alerta | sim | já passou | **elegibilidade** |
| 68612 | Pós-graduação em Nefrologia e Urologia Veterinária, VIII | 24/10/2026 | -2 | verificar | estático e vídeo, com 5 | sem alerta | sim | já passou | **elegibilidade** |
| 707 | Pós-graduação em Oftalmologia Veterinária, VII | 30/10/2026 | 4 | aberto | estático, sem 5 | sem alerta | não | 30/09/2026 (já passou) | calendário |
| 68604 | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, VI | 31/10/2026 | 5 | aberto | estático, com 5 | conferir que é 68604 e não 68611 (mesmo nome, sem data) | sim | 01/10/2026 (já passou) | calendário |
| 68606 | Pós-graduação em Gastroenterologia Veterinária, IX | 07/11/2026 | 12 | aberto | estático e vídeo, com 5 | sem alerta | sim | 08/10/2026 (já passou) | calendário |
| 698 | Pós-graduação em Ecocardiografia, III | 28/11/2026 | 33 | aberto | estático e vídeo, com 5 | **site mostra 28/11/2027 no campo Início** (memorando, 2.1) | sim | 29/10/2026 | **destino** |
| 68608 | Pós-graduação em Hematologia Veterinária, VIII | 28/11/2026 | 33 | aberto | estático e vídeo, com 5 | sem alerta | sim | 29/10/2026 | nenhum |
| 68610 | Pós-graduação em Dermatologia Veterinária, V | 28/11/2026 | 33 | aberto | estático, com 5 | sem alerta | sim | 29/10/2026 | nenhum |
| 289 | Pós-graduação em Cardiologia Veterinária, II, Goiânia | 20/03/2027 | 145 | aberto | estático, com 5 | sem alerta na página da turma; links das provas de Cardiologia SP e GO invertidos (P3) | sim | 18/02/2027 | nenhum |
| 662 | Pós-graduação em Ortopedia Veterinária, IV | 24/04/2027 | 180 | aberto | estático e vídeo, sem 5 | **site mostra 15 e 16/08/2026, turma IV** (link trocado; turma diverge, P5) | sim | 25/03/2027 | **destino** |

Leitura (fatos, contados na tabela):

- 8 de 14 ativas (57,1%) têm bloqueio de elegibilidade ou de destino. Nelas, qualquer CPL ou CTR que chegar não vale como evidência de criativo, público ou leilão até o bloqueio ser resolvido (R1 e R2 da analise-de-campanha).
- 12 de 14 ativas (85,7%) levam a página com a frase de certificação ligada ao MEC. As exceções são 707 e 586. Isso não é motivo de pausa pela regra da squad (sinalização, pedido A7 do cmo), mas entra no item "página de destino" da conformidade de toda leitura.
- Nas 3 turmas da reta final mais curta (707, 68604, 68606), a data de 30 dias antes do início já passou. Se a Ufape tratar essa data como prazo de matrícula, essas campanhas estão gastando depois do prazo [CONFIRMAR].
- Nas 3 turmas de 28/11 (698, 68608, 68610), essa data é 29/10/2026, daqui a 3 dias. Se for prazo, a reta final delas termina em 29/10 e não em 28/11 [CONFIRMAR].
- Só 3 ativas (68608, 68610 e 289) não têm bloqueio e têm mais de 30 dias até o início. São as únicas em que uma leitura de desempenho poderá orientar ajuste quando a exportação chegar.

### 3.3 As 18 pausadas cruzadas com o catálogo

| Código | Turma (catálogo) | Início | Dias | Status no catálogo | Formatos e ângulos (visão) | Alerta de página ou dado | Frase MEC | Leitura estrutural |
|---|---|---|---|---|---|---|---|---|
| 653 | Pós-graduação em Endoscopia Veterinária, III | 15/08/2026 | -72 | verificar | estático e vídeo, sem 5 | prova 68649 sem turma futura | sim | manter pausada |
| 665 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, VIII | 19/09/2026 | -37 | verificar | estático, sem 5 | prova 68643 SP sem turma futura em SP | sim | manter pausada |
| 666 | Pós-graduação em Terapia Intensiva e Emergência Veterinária, XI | 19/09/2026 | -37 | verificar | estático, com 5 | criativos com 5 ângulos reaproveitáveis em 68623 (GO) [CONFIRMAR ligação] | sim | manter pausada; fonte de criativo |
| 68605 | Pós-graduação em Cardiologia Veterinária, XI | 17/10/2026 | -9 | verificar | estático e vídeo, com 5 | mesma área da 289 (ativa) | sim | manter pausada; histórico serve de linha de base para 289 |
| 659 | Pós-graduação em Cirurgia Cardiorrespiratória em Cães e Gatos, II | 17/10/2026 | -9 | verificar | estático e vídeo, com 5 | sem alerta | sim | manter pausada |
| 68607 | Pós-graduação em Anestesiologia Veterinária, X | 24/10/2026 | -2 | verificar | só vídeo, sem 5 | turma começou há 2 dias | sim | manter pausada (R2) |
| 657 | Pós-graduação em Anestesiologia Avançada, II | 13/03/2027 | 138 | aberto | estático, sem 5 | pré-requisito a escrever na página (1.11, PP7) | sim | histórico prioritário (1.11, seção 7) |
| 68615 | Pós-graduação em Patologia Clínica, VII | 20/03/2027 | 145 | aberto | estático, com 5 | sem alerta | sim | candidata a reativar em 07/12 (PP6) |
| 341 | Pós-graduação em Medicina Interna Equina, I | 20/03/2027 | 145 | aberto | estático, sem 5 | promoção de 20% com texto cortado (P16) | sim | só com a regra da promoção (PP7) |
| 333 | Pós-graduação em Citopatologia Veterinária, I | 27/03/2027 | 152 | aberto | estático, sem 5 | a visão tem duas linhas "Citopatologia" (27/03 e 03/04) | sim | candidata a reativar em 07/12 (PP6) |
| 679 | Pós-graduação em Infectologia Veterinária, IV (linha da visão "Citopatologia 03/04") | 03/04/2027 | 159 | aberto | estático, sem 5 | identidade da campanha [CONFIRMAR] | sim | não reativar até saber o curso anunciado |
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, V | 10/04/2027 | 166 | aberto | estático, sem 5 | sem alerta | sim | reativar em 06/01 (PP11) |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, I | 10/04/2027 | 166 | aberto | estático e vídeo, com 5 | data diverge: planilha 10/04/2027, site 24/04/2027 (P4) | sim | pacote completo parado; reativar só com a data corrigida |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais, V | 17/04/2027 | 173 | aberto | estático, com 5 | turma diverge: planilha VII, site V (P5) | sim | reativar em 06/01 sem número de turma (PP11) |
| 578 | Pós-graduação em Videocirurgia Veterinária, IV | 22/05/2027 | 208 | aberto | estático, sem 5 | sem alerta | sim | manter pausada (fora do trimestre) |
| 382 | Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos, I | 22/05/2027 | 208 | aberto | estático, sem 5 | sem alerta | sim | manter pausada |
| 352 | Pós-graduação em Ventilação Mecânica, I | 24/05/2027 | 210 | aberto | estático, sem 5 | data diverge: planilha 24/05/2027, site 24/04/2027 (P4) | não | manter pausada |
| 60 | Pós-graduação em Medicina de Silvestres, I | 28/05/2027 | 214 | aberto | estático, sem 5 | sem alerta | sim | manter pausada |

Leitura (fatos): das 12 pausadas em turma futura, 3 têm os 5 ângulos prontos (68615, 366, 68617) e 4 têm alerta de página ou de dado que impede a reativação até a correção (679, 366, 341 e, para fora do trimestre, 352). O motivo de cada pausa é [CONFIRMAR]: pausa por calendário, por verba ou por página mudam a leitura do histórico.

### 3.4 Sem campanha e fora da visão (informativo)

- Sem campanha: 677 e 564 estão em turma iniciada ("verificar"): correto não ter campanha. As 8 futuras sem campanha (68628, 68632, 68609, 68616, 719, 68623, 699 e a linha "Pneumologia") entram ou não na mídia pela divisão de verba do 1.11 (PP11 para 68628, 68632 e 68609).
- A linha da visão "Pós-graduação em Pneumologia Veterinária, 10/04/2027, sem campanha" tem a data da 670 (catálogo: 10/04/2027, turma VII, encerrado, link fora do ar), e não a da 68636 (17/04/2027, turma VIII, só no site). [SUPOSIÇÃO: a linha da visão é a da 670.] Se for, a 68636, que está à venda, não tem linha na planilha nem status de mídia.
- As 22 provas de bolsa não constam na visão. A campanha única ainda não existe (subida prevista em 03/11, memorando D4). Não há o que diagnosticar; o roteiro de leitura está na seção 8.5.

---

## 4. Gargalo do funil (diagnóstico estrutural, elo por elo)

A skill lê o funil de cima para baixo com números. Sem números, o que dá para ler é se cada elo tem condição de funcionar. Ordem de checagem: o elo que falha primeiro invalida a leitura dos de baixo.

| Elo | O que a estrutura mostra hoje | Campanhas afetadas | Diagnóstico | Evidência |
|---|---|---|---|---|
| 0. Elegibilidade (a turma pode receber aluno?) | 6 ativas em turma "verificar", de 2 a 72 dias depois do início | 650, 68662, 706, 586, 554, 68612 | **primeiro elo fraco**: a campanha pode estar gerando lead que não tem turma para entrar | catálogo, status "verificar"; visão, status ativo |
| 1. Entrega (CPM) | sem dado | todas | [DADO NÃO FORNECIDO]. Risco estrutural de leilão mais caro entre campanhas da mesma área (cardio: 289, 698 e as provas 68641 e 68642; H7 da 1.32) | visão; tabela por área do plano do cmo |
| 2. Atenção (retenção de 3 segundos, ThruPlay) | 21 de 32 campanhas da Pós são só estáticas; nas ativas, 8 de 14 | 650, 68662, 706, 586, 707, 68604, 68610, 289 | não mensurável nessas: sem vídeo não há retenção a ler | visão |
| 3. Interesse (CTR do link, CPC) | sem dado; ângulos sem rótulo na visão ("com" ou "sem" 5) | todas | [DADO NÃO FORNECIDO]. Mesmo com número, não dá para dizer qual ângulo funciona sem o rótulo de cada anúncio (H3 da 1.32) | visão |
| 4. Chegada (visualizações da página por clique) | 2 ativas com página que não bate com a planilha; 12 de 14 com a frase ligada ao MEC | 698, 662 (e 68662, já no elo 0) | **segundo elo fraco**: a página pode não entregar o que o anúncio promete; CTR e CPL dessas campanhas não valem como evidência até a correção | auditoria do catálogo de 26/10, seções 3, 4 e 9 |
| 5. Conversão (taxa da página, CPL) | evento de conversão que a página registra (cadastro, início de checkout, compra) [CONFIRMAR]; pixel e API de Conversões sem teste (D8) | todas | [DADO NÃO FORNECIDO]. Sem saber o evento, o CPL de uma campanha não é comparável com o de outra | memorando, D8; 1.11, seção 5 |
| 6. Matrícula (custo por matrícula, lead para matrícula) | CRM não informado (ufape-geral.md, Ferramentas); código do catálogo no nome ou na UTM [CONFIRMAR] | todas | [DADO NÃO FORNECIDO]. Sem o código, lead e matrícula não se ligam à turma (H4 da 1.32) | ufape-geral.md; 1.11, PP4 |
| 7. Saturação (frequência, CTR ao longo dos dias) | campanhas de janela longa ou com pacote único | 289 (145 dias), 662 (180 dias), 707 (só estático, sem 5) | risco a medir, não fato: são as primeiras candidatas a fadiga na exportação | visão |
| Calendário | 3 ativas com a data de 30 dias antes do início já passada; 3 com essa data em 29/10 | 707, 68604, 68606; 698, 68608, 68610 | a janela de conversão pode ser mais curta que a de veiculação [CONFIRMAR o que essa data significa] | contexto da linha; conta da seção 3.2 |

**Conclusão do diagnóstico:** o primeiro elo fraco é a elegibilidade (6 campanhas) e o segundo é a chegada (698 e 662). A ação certa nos dois é de conformidade e não de desempenho, e já está pedida (memorando D1 e D2; 1.11 PP5). Nas 6 ativas sem bloqueio, o diagnóstico de entrega, atenção, interesse e conversão só sai com a exportação.

---

## 5. Achados novos deste diagnóstico (não estavam nas entradas)

| # | Achado | Evidência | Fato ou hipótese | O que muda |
|---|---|---|---|---|
| N1 | As datas de 68662 e 662 aparecem cruzadas entre planilha e site: Odontologia está em 15/08/2026 na planilha e em 24/04/2027 no site; Ortopedia está em 24/04/2027 na planilha e em 15/08/2026 no site. O catálogo ainda tem a 678 (Odontologia, turma IV, 15/08/2026, só no site) | auditoria do catálogo de 26/10, seção 3; catálogo, linhas 678, 68662 e 662 | **fechado na versão 2 pela decisão 12 da Ufape:** valem as datas da planilha, 68662 em 15/08/2026 e 662 em 24/04/2027; a suposição de datas trocadas na planilha sai | 68662 é turma iniciada, segue "verificar" e em pausa (D1, pedido A4 do cmo). 662 começa em 24/04/2027; a página dela mostra a turma de 15/08/2026 (link trocado): a URL dos anúncios é conferida em 28/10 e, se levar à página errada, vai o pedido de pausa (PP5; R5 do cmo). A prova 68655 de Odontologia continua sem turma de destino (U4 do cmo) |
| N2 | Na reta final de 707, 68604 e 68606, a data de 30 dias antes do início já passou (30/09, 01/10 e 08/10/2026) | contexto da linha; conta da seção 3.2 | a conta é fato; se essa data é prazo de matrícula é [CONFIRMAR] | Se for prazo e a Ufape não aceitar matrícula depois dele, as pausas de D9 (30/10, 31/10 e 07/11) estão atrasadas e devem ser antecipadas (ação A3) |
| N3 | Em 698, 68608 e 68610, a mesma data cai em 29/10/2026 | mesma conta | idem | Se for prazo, a reta final dessas três termina em 29/10 e D18 (pausa em 28/11) precisa ser revista |
| N4 | 12 de 14 ativas levam a página com a frase de certificação ligada ao MEC; nas pausadas, 17 de 18 (a exceção é 352) | auditoria do catálogo, seção 9 | fato | Reforça o pedido A7 do cmo. Na leitura, toda campanha com destino nessas páginas é marcada "página com pendência de conformidade" |
| N5 | Só 3 das 14 ativas (68608, 68610 e 289) estão sem bloqueio e a mais de 30 dias do início | tabela 3.2 | fato | É nelas que o primeiro diagnóstico de desempenho poderá virar ajuste. Nas outras, a leitura é registro (para a linha de base e para a revisão pós-campanha), não decisão |
| N6 | A linha "Pneumologia, 10/04/2027" da visão tem a data da 670 (encerrada), e não a da 68636 (à venda) | catálogo, linhas 670 e 68636; visão | a coincidência de data é fato; a ligação é [SUPOSIÇÃO] | 68636 pode estar sem nenhuma linha de mídia na planilha; entra no pedido do analista (1.10, ação 2) |

---

## 6. Divergências com o CRM

Não há exportação do CRM nem das plataformas. A conciliação não pode ser feita. O que já se sabe, pela estrutura, que vai impedir ou distorcer a conciliação:

| Risco | Onde | Efeito na leitura | Como tratar quando os dados chegarem |
|---|---|---|---|
| Código do catálogo ausente no nome da campanha ou no utm_campaign [CONFIRMAR] | todas as 32 com status | lead e matrícula não se ligam à turma; o custo por matrícula por turma não fecha | medir o percentual de leads com código e UTM; abaixo de 100%, separar os leads sem código como "origem não atribuída" e não distribuir entre turmas por estimativa |
| Duas turmas com o mesmo nome | 68604 e 68611 (Diagnóstico por Imagem); 706 e 68629 (Ultrassonografia); 68662 e 678 (Odontologia); 68605 e 289 (Cardiologia SP e GO) | lead pode cair na turma errada no CRM | conciliar pelo código do produto da compra na loja, não pelo nome do curso |
| Evento de conversão diferente entre campanhas [CONFIRMAR] | todas | "lead" no gerenciador pode ser cadastro numa campanha e início de checkout em outra | ler cada campanha só contra o próprio evento; comparar campanhas só com o mesmo objetivo e evento |
| Página de destino errada | 698, 662, 68662 | o CRM pode registrar o lead na turma da página, não na da campanha | registrar a URL final de cada anúncio na exportação e conciliar pela URL |
| Turma iniciada com campanha ativa | 650, 68662, 706, 586, 554, 68612 | lead sem turma para entrar pode ser contado como perda de atendimento | separar esses leads no CRM com a marca "turma iniciada" antes de ler a taxa lead para matrícula |

Regra: se o gerenciador e o CRM diferirem, a decisão do item é INVESTIGAR, e nenhuma decisão de desempenho vale até resolver (regra 5 da seção 1). A tolerância aceitável de diferença entre as fontes é [CONFIRMAR com o analista-de-dados]; não fixo um número sem histórico.

---

## 7. Criativos cansados

Sem frequência, CTR nem CPL por anúncio ao longo das semanas, nenhum criativo pode ser chamado de cansado hoje. Candidatos a olhar primeiro, pela estrutura (hipótese, não fato):

| Campanha | Por que é candidata | O que confirma fadiga | O que derruba |
|---|---|---|---|
| 289 | 145 dias até o início, campanha já ativa, só estático; mesma área de 698 e das provas de Cardiologia | frequência subindo e CTR do link caindo por 3 dias ou mais no mesmo anúncio, com CPL subindo (memorando, D20; skill, tabela de sintomas) | frequência estável e CTR estável; ou CPL subindo com CTR estável (aí é leilão, não fadiga) |
| 662 | 180 dias até o início, sem 5 ângulos | mesma regra | idem; e, antes de tudo, o destino precisa estar certo (elo 4) |
| 707 | reta final com só estático e sem 5 ângulos | mesma regra | idem. Mesmo confirmada, não entra criativo novo com menos de 7 dias até o início (memorando, 5.1) |
| 68606 | pacote completo rodando junto (estático, vídeo e 5 ângulos); 12 dias | mesma regra (D20 já prevê a troca pelo ângulo pronto até 03/11) | idem |

Fadiga confirmada pede conceito novo, não só título novo (skill, tabela de sintomas). Exceção desta rodada: nas Pós de março e abril com 5 ângulos já prontos e pausados (68615, 366, 68617), o "novo" pode ser o pacote pronto, que custa menos que produzir (analista 1.10, insight 2).

---

## 8. Roteiro de leitura quando a exportação chegar

Prazo: 2 dias úteis depois de receber a exportação (encomenda do gestor, 1.11, seção 7). Ordem fixa: portões de qualidade, funil de cima para baixo, leitura por grupo, decisão.

### 8.1 Portões de qualidade do dado (antes de qualquer conta)

| # | Portão | Passa quando | Se não passar |
|---|---|---|---|
| G1 | Exportação sem dado pessoal | só contagens e somas | devolver; não abrir |
| G2 | Campos mínimos do memorando (seção 7.1) | campanha, status, data da última mudança, objetivo, evento de otimização, gasto e orçamento por semana, impressões, alcance, frequência, cliques no link, CTR, CPC, CPM, leads, inícios de checkout, compras, URL de destino, formato e ângulo por anúncio, parcela de impressões perdida (Google) | ler só o que existe e marcar o resto [DADO NÃO FORNECIDO] |
| G3 | Janela e granularidade | uma linha por campanha (e por anúncio) e por semana, de 01/08/2026 até a data da exportação | se vier só acumulado, não há leitura de tendência nem de fadiga; pedir de novo |
| G4 | Ligação com a turma | chave <linha>_<código> no nome ou no utm_campaign (D12 do cmo); nas campanhas já no ar, que não são renomeadas, pela tabela de correspondência da seção 8.7 | campanha sem chave e fora da tabela vai para "não atribuída"; pedido PP4 do 1.11 |
| G5 | Contexto do período | o que mudou no período (verba, criativo, página, oferta, pausa, data da entrada da data errada em 698) | sem isso, mudança de resultado não tem causa atribuível; registrar como hipótese |
| G6 | Conciliação | leads do gerenciador contra leads do CRM pelo código | diferença acima da tolerância [CONFIRMAR]: decisão INVESTIGAR |

### 8.2 Funil de cima para baixo: métrica, corte, limiar e decisão disparada

Limiares numéricos de custo são [CONFIRMAR] até PP1 do 1.11. Limiares de tendência são regras práticas da skill. Onde não há regra, a referência é a própria conta (linha de base das 2 primeiras semanas fechadas), nunca benchmark externo.

| Etapa | Métrica e conta | Cortes | Limiar | Resultado e decisão que dispara |
|---|---|---|---|---|
| Ritmo de gasto | gasto da semana dividido pelo orçamento semanal (diária x 7) | campanha, semana | abaixo do orçamento com poucas impressões | entrega travada (público estreito, lance, anúncio reprovado): AJUSTAR orçamento, lance ou público, um por vez |
| Entrega | CPM = gasto dividido por impressões x 1.000 | plataforma, campanha, praça (SP, GO), semana | CPM subindo semana a semana contra a própria linha de base, com CTR estável | leilão mais caro (época de prova e de concorrência): renovar criativo ou ampliar público; não mexer em verba |
| Atenção (só vídeo) | retenção de 3 segundos = visualizações de 3 s divididas por impressões; ThruPlay | anúncio, formato | baixa contra os outros vídeos da conta | se quem assiste vira lead: o corpo funciona e a abertura não; AJUSTAR o gancho |
| Interesse | CTR do link = cliques no link divididos por impressões; CPC do link = gasto dividido por cliques no link | anúncio, formato (estático, vídeo), ângulo (1 a 5, se rotulado), praça | CTR abaixo da mediana dos anúncios da mesma campanha, com volume suficiente (regra prática: 10 a 20 conversões de cada lado para comparar conversão; 3 a 7 dias) | AJUSTAR: trocar ângulo ou formato. Menos que isso: "ainda é ruído" |
| Chegada | visualizações da página divididas por cliques no link | campanha, URL de destino | queda forte contra a própria linha de base ou contra outras campanhas da mesma página | carregamento, redirecionamento ou pixel: INVESTIGAR página e rastreio antes de mexer no anúncio |
| Conversão | taxa da página = leads (ou inícios de checkout) divididos por visualizações da página; CPL = gasto dividido por leads | campanha, evento de otimização, URL | CPL acima do CPLmax conservador da turma (1.11) depois de gastar de 1,5 a 2 vezes o CPLmax | com CTR bom: o problema é depois do clique; INVESTIGAR página, formulário e pixel (pedir analise-cro). Com CTR ruim: voltar à etapa de interesse |
| Conversão mínima | c mínima = CPL observado dividido por CMmax (1.11, fórmula 7) | turma | c mínima maior que a conversão histórica da linha [CONFIRMAR] | o CPL observado não cabe na meta com a conversão que a Ufape tem: AJUSTAR (criativo, público ou página) ou levar ao gestor a pausa |
| Matrícula | taxa lead para matrícula por coorte; custo por matrícula = gasto dividido por matrículas | turma, origem (UTM), semana do lead | lido só com 2 semanas fechadas e 30 dias depois do início da turma (1.11, seção 8, item 3) | lead barato e matrícula cara: olhar o CRM, o tempo de primeira resposta no WhatsApp e a qualidade do lead; não mexer no anúncio |
| Saturação | frequência e CTR do link por anúncio, dia a dia | anúncio, semana | frequência subindo e CTR caindo por 3 dias ou mais, com CPL subindo (memorando, D20) | AJUSTAR: entrar com conceito novo ou ângulo pronto, um anúncio por vez |
| Queda súbita | todas as métricas estáveis e queda num dia | campanha | queda de entrega ou de conversão de um dia para outro | pagamento recusado, anúncio reprovado, página fora do ar ou evento de pixel parado: INVESTIGAR no mesmo dia |
| Concentração | parte do gasto num único anúncio | campanha | um anúncio com quase todo o gasto | normal na entrega; não pausar os outros por gastarem pouco; preparar substitutos |

Decisões possíveis por item (skill, passo 5): ESCALAR (abaixo da meta com volume confiável por vários dias, em passos de até 20% da diária por vez, 1.11, seção 8, item 5, dentro da verba aprovada), MANTER (dentro da meta ou aprendendo), AJUSTAR (um elo fraco, uma mudança), PAUSAR (gastou o suficiente para julgar e está fora da meta por 2 semanas depois de um ajuste, R6), INVESTIGAR (fontes não batem).

### 8.3 Leitura por grupo

| Grupo | Itens | O que ler | Para que serve a leitura | Decisão possível |
|---|---|---|---|---|
| Turmas iniciadas com campanha ativa | 650, 68662, 706, 586, 554, 68612 | gasto dos últimos 7 dias e acumulado desde o início da turma; leads e compras depois do início; URL de destino de cada anúncio | registro da pausa D1 e valor da verba liberada (D11); nenhuma leitura de desempenho | só a pausa (D1) ou, com E1 e E2 confirmados por escrito, reativação |
| Reta final curta | 707 (30/10), 68604 (31/10), 68606 (07/11) | matrículas pagas contra a turma mínima de 15; leads da última semana; frequência e CTR (68606, por D20) | revisão pós-campanha (1.32, seção 3.3) e linha de base da área | MANTER sem mudanças até a pausa (D9); em 68606, uma troca de anúncio por fadiga até 03/11 |
| Reta final de 28/11 | 698, 68608, 68610 | as mesmas, mais: anúncios que citam data ou "2027" (698) e anúncios que citam bolsa (as três começam um dia depois das provas; 68610 e 68608 têm as provas da área, 68646 e 68651, e a 698 tem as de Cardiologia, 68641 e 68642; nenhuma pode prometer bolsa, memorando 5.1, regra 4) | ajuste ainda cabe (33 dias), se a data de 29/10 não for prazo | 698 por D2; 68608 e 68610: MANTER, e AJUSTAR por um elo só se o número mostrar; vídeo para 68610 (D18) |
| Ativas de longo prazo | 289, 662 | ritmo de gasto acumulado contra os dias até o início; frequência; leads qualificados no CRM; praça GO no público de 289; URL de 662 | evitar gasto cedo demais e saturação; 662 depende do destino | 289: MANTER sem aumento, com o gasto até 06/12 contado na parte dela em P3 (PP9; EM9 do cmo); se o gasto crescer sem lead qualificado, INVESTIGAR antes de mexer. 662: diária fora de VN até o lote 2 (EM9); conferir URL em 28/10; se abrir turma ou data diferente da planilha (24/04/2027), PAUSAR os anúncios afetados (PP5; R5 do cmo) |
| Histórico das pausadas prioritárias | 657, 68615, 366, 68617 (e 341, 333 para março) | data e motivo da pausa; gasto, leads e CPL do período ativo; frequência no momento da pausa; melhor anúncio por CTR e CPL | linha de base para a reativação (PP6, PP7, PP11) e escolha de qual criativo volta primeiro | nenhuma decisão de desempenho; só a ordem de reativação sugerida ao gestor |
| Histórico das pausadas em turma iniciada | 653, 665, 666, 68605, 659, 68607 | os mesmos campos | linha de base por área (68605 para 289; 666 para 68623; 68607 e 586 para 657 e 68609) | manter pausadas |

### 8.4 Contas que a leitura vai mostrar (fórmulas; valores [DADO NÃO FORNECIDO])

- CPM = gasto / impressões x 1.000
- CTR do link = cliques no link / impressões
- CPC do link = gasto / cliques no link
- Taxa de chegada = visualizações da página / cliques no link
- Taxa da página = leads (ou inícios de checkout) / visualizações da página
- CPL = gasto / leads
- Custo por matrícula = gasto / matrículas da turma com a origem da campanha
- c mínima = CPL / CMmax da turma (1.11, fórmula 7)
- Gasto mínimo para julgar um anúncio = 1,5 x CPLmax (regra prática)
- Ritmo necessário = (15 menos matrículas acumuladas) / semanas até a data de corte (1.32, seção 2.2, com a turma mínima de 15 da decisão 11)

Toda conta aparece com os números usados, para o gestor conferir.

### 8.5 Provas de bolsa (quando a campanha subir, a partir de 03/11)

- Unidade de leitura: a prova (especialidade e praça), não a campanha única (1.32, seção 3.4).
- Antecedente: custo por inscrito = gasto da área / inscritos pagos na loja, contra o custo por inscrito máximo do 1.11 (fórmula 8) [CONFIRMAR o valor].
- Julgamento final: custo por matrícula via prova, por turma de destino, só depois do resultado, dos 2 dias úteis de recurso e dos 10 dias úteis de matrícula (data do resultado [CONFIRMAR]).
- Fases do 1.11 (PP3): nenhuma realocação antes de 06/11 (3 dias de dados); primeira decisão na revisão de 09/11.
- Sobreposição a ler: frequência das provas de Cardiologia com a 289 e a 698; das provas de Dermatologia e Hematologia com 68610 e 68608.
- Leitura de leilão (NE1 e NE4 da analise-de-midia-eventos; plano do cmo, 12.6): de 03/11 a 18/11, as provas de Anestesiologia (68639, 68640) e de Neurologia (68654) disputam o mesmo público com o frio e o remarketing do Workshop Brasileiro de Neuromonitorização e, desde a subida (10/11, ou 19/11 se o pedido R4 do cmo for aprovado), com a 616 de Livres. Nessas áreas, CPM subindo com CTR estável é lido primeiro como disputa de leilão, não como criativo fraco: não mexer em criativo nem em verba por isso; registrar lado a lado CPM, alcance e frequência (EA3 da analise-de-midia-eventos). Sem exclusão de público entre campanhas (regra do cmo) [SUPOSIÇÃO de efeito no leilão, origem: conjuntos da mesma conta com públicos parecidos disputam a mesma entrega].

### 8.6 Calendário de leitura

| Data | Leitura |
|---|---|
| 27/10 | registro do gasto das 6 turmas iniciadas antes da pausa D1 (se a exportação vier) |
| 28/10 | URL de 698, 662 e 68662; prazo do gerenciador para a exportação (D6) |
| 2 dias úteis depois da exportação | primeira versão numérica deste diagnóstico, no mesmo formato |
| 03/11 | revisão semanal 1; subida das provas |
| 06/11 e 09/11 | primeira leitura das provas (3 dias de dados) e revisão 2, com a leitura de leilão das áreas de Anestesiologia e Neurologia (8.5) |
| 16/11, 23/11, 30/11 | revisões 3 a 5 |
| 30/11 e 07/12 | leitura final tardia de 707, 68604 e 68606 (30 dias depois do início) |
| 07/12 | leitura antes da reativação de 68615 e 333 (PP6) |

### 8.7 Tabela de correspondência entre nomes antigos e o padrão D12 (versão 2)

O plano do cmo (12.7, D12) fixa a chave de cada item como `pos_<código do catálogo>` e manda não renomear as campanhas já no ar; a leitura liga o nome antigo à chave por esta tabela. A linha da visão e o código vêm da seção 3.2; o nome da campanha e o utm_campaign atuais só chegam com a exportação (ação A1) e são preenchidos por quem recebe a exportação, sem renomear nada no gerenciador.

| Linha da visão (curso, início pela planilha) | Código | Chave D12 | Nome da campanha no gerenciador | utm_campaign atual | Tratamento |
|---|---|---|---|---|---|
| Pós-graduação em Medicina de Felinos, 15/08/2026 | 650 | pos_650 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1); só leitura histórica |
| Pós-graduação em Odontologia Veterinária, 15/08/2026 | 68662 | pos_68662 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1); conferir que não é a 678 (mesmo nome) |
| Pós Graduação em Ultrassonografia de Pequenos Animais, 15/08/2026 | 706 | pos_706 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1); conferir que não é a 68629 (mesmo nome) |
| Pós-graduação em Anestesiologia Veterinária: Direto ao ponto, 22/08/2026 | 586 | pos_586 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1) |
| Pós-graduação em Dor e Cuidados Paliativos na Veterinária, 22/08/2026 | 554 | pos_554 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1) |
| Pós-graduação em Nefrologia Veterinária, 24/10/2026 | 68612 | pos_68612 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | em pausa (D1) |
| Pós-graduação em Oftalmologia Veterinária, 30/10/2026 | 707 | pos_707 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar até a pausa (D9); não renomear |
| Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, 31/10/2026 | 68604 | pos_68604 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar até a pausa (D9); não renomear; conferir que não é a 68611 (mesmo nome) |
| Pós-graduação em Gastroenterologia Veterinária, 07/11/2026 | 68606 | pos_68606 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar até a pausa (D9); não renomear |
| Pós-graduação em Ecocardiografia, 28/11/2026 | 698 | pos_698 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | D2; não renomear |
| Pós-graduação em Hematologia Veterinária, 28/11/2026 | 68608 | pos_68608 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar até a pausa (D18); não renomear |
| Pós-graduação em Dermatologia Veterinária, 28/11/2026 | 68610 | pos_68610 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar até a pausa (D18); não renomear |
| Pós-graduação em Cardiologia Veterinária, 20/03/2027, GO | 289 | pos_289 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar, sem aumento (PP9); não renomear; conferir que não é a 68605 (mesmo nome, SP) |
| Pós-graduação em Ortopedia Veterinária, 24/04/2027 | 662 | pos_662 | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] | no ar, fora de VN (EM9); não renomear; URL em 28/10 (PP5) |
| Provas de bolsa de 27/11/2026 (campanha nova, fora da visão) | 22 provas abertas | pos_provas20261127 | nasce no padrão (estrategia-de-midia-pos, 4.2) | nasce no padrão (paid_social e cpc) | não precisa de correspondência |

Pausadas que forem reativadas (68615, 333, 657, 341, 68635, 68617): a linha entra na tabela no dia da reativação, do mesmo jeito; se o gestor decidir por campanha nova, o nome já segue D12 (estrategia-de-midia-pos, 4.2). Regra de leitura: lead ou compra com utm_campaign que não começa pela chave e não está nesta tabela vai para "não atribuída" (G4).

---

## 9. Tabela de decisão (estrutural, hoje)

"Hoje" vale sem número. A coluna "Muda quando" diz o que tiraria o item da decisão atual.

| Item | Métrica-chave quando houver número | Diagnóstico hoje | Decisão hoje | Referência | Muda quando |
|---|---|---|---|---|---|
| 650, 706, 586, 554 | gasto desde o início da turma | turma iniciada, "verificar" | PAUSAR (pedido já feito) | memorando D1 | E1 e E2 confirmados por escrito |
| 68612 | gasto desde 24/10 | turma iniciada há 2 dias | PAUSAR e reativar no dia da confirmação | memorando D1 | E1 e E2 confirmados |
| 68662 | URL final dos anúncios | iniciada (15/08/2026, data da planilha, decisão 12) e com destino que mostra 24/04/2027 | PAUSAR; conferir o destino junto com 662 em 28/10 | D1; ação A2 abaixo | E1 e E2 confirmados por escrito |
| 707, 68604 | matrículas contra a turma mínima | reta final de 4 e 5 dias; data de 30 dias antes já passou | MANTER sem mudanças até a pausa | D9; ação A3 | se a data de 30 dias antes for prazo: PAUSAR antes |
| 68606 | frequência e CTR por anúncio | reta final de 12 dias | MANTER; uma troca por fadiga até 03/11 | D9, D20; ação A3 | idem |
| 698 | anúncios com data ou "2027"; URL | página com data errada | AJUSTAR (pausar anúncios com data); PAUSAR a campanha se o site não for corrigido até 28/10 às 18h | D2 | site corrigido |
| 68608 | CTR, CPL, frequência; matrículas | sem bloqueio; 33 dias | MANTER; leitura completa assim que a exportação chegar | D18 | número fora da meta por um elo: AJUSTAR esse elo |
| 68610 | CTR do estático com frequência | sem bloqueio; só estático | MANTER; vídeo pedido | D18 | CTR caindo com frequência subindo: o vídeo é a alavanca |
| 289 | ritmo de gasto; leads qualificados | sem bloqueio; 145 dias | MANTER sem aumento | 1.11 PP9 | gasto sem lead qualificado: INVESTIGAR |
| 662 | URL final; frequência | início em 24/04/2027 (planilha, decisão 12); destino mostra 15/08/2026, turma IV | INVESTIGAR o destino em 28/10; PAUSAR os anúncios se a página não bater | 1.11 PP5; R5 do cmo; N1 | página corrigida |
| 653, 665, 666, 68605, 659, 68607 | histórico | turma iniciada | manter pausadas | 1.32, 2.5.1 | E1 e E2 (só 68607 é candidata realista) |
| 68615, 333 | histórico antes da pausa | prontas para março | manter pausadas até 07/12 | 1.11 PP6 | condições de PP6 |
| 657, 341 | histórico; pré-requisito e promoção | bloqueio de página e de regra | manter pausadas | 1.11 PP7 | regra escrita na página |
| 679 | identidade da campanha | curso anunciado incerto | manter pausada | 1.32, 2.5.2 | Ufape confirma curso e link |
| 68635, 68617 | histórico | prontas para abril (68617 sem número de turma) | manter pausadas até 06/01 | 1.11 PP11 | condições de PP11 |
| 366 | histórico | pacote completo; data diverge | manter pausada | 1.32, 2.5.2 | data corrigida no site |
| 578, 382, 352, 60 | histórico | fora do trimestre | manter pausadas | 1.11, seção 1 | janela de maio no próximo plano |

Nenhuma decisão de ESCALAR é possível nesta rodada: não há meta em reais nem volume lido.

---

## 10. Até 5 ações em ordem de impacto (pedidos de aprovação humana)

Executa: humano no gerenciador ou na Ufape. Aprovador: a pessoa do marketing que aprovou o plano do cmo, até a tabela de aprovação de contexto/ufape-geral.md ser preenchida. Ordem pelo impacto na leitura e no gasto, não por preferência.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| A1 | Enviar a exportação do memorando (seção 7.1) com quatro campos a mais por anúncio: URL final, data de criação, formato e ângulo (rótulo de 1 a 5, se existir) | sem ela nenhum elo de entrega, atenção, interesse ou conversão pode ser lido; os campos a mais fecham N1, a fadiga e o teste de ângulo | sem custo de mídia | primeira versão numérica deste diagnóstico em 2 dias úteis | não se aplica | 28/10 (D6) |
| A2 | Um humano confere em 28/10, no mesmo dia, a URL final dos anúncios de 68662 e de 662 contra as datas da planilha (15/08/2026 e 24/04/2027, decisão 12); a Ufape confirma a turma de 662 (turma diverge, P5) e a situação da 678 | as páginas mostram as datas trocadas (N1, fechado quanto à data); 662 pode estar levando à página da turma que começou em 15/08/2026 | sem custo de mídia; a diária das duas é [CONFIRMAR] | pausa certa em 68662 (D1) e pausa ou manutenção certa em 662 (PP5; R5 do cmo) | não se aplica (é conferência); a pausa de 662, se houver, se desfaz reativando a campanha depois da correção (PP5) | 28/10 |
| A3 | Ufape confirma por turma se a "1ª mensalidade 30 dias antes do início" é prazo de matrícula para 707, 68604, 68606, 698, 68608 e 68610 | se for prazo, 707, 68604 e 68606 já estão depois dele, e 698, 68608 e 68610 chegam a ele em 29/10 (N2, N3) | sem custo de mídia; a economia possível é a diária dessas campanhas entre o prazo e a pausa prevista [CONFIRMAR] | pausas no dia certo, sem gasto em matrícula que não pode mais acontecer | se a pausa for antecipada e a Ufape aceitar matrícula tardia, reativar no gerenciador | 28/10 (junto com D3) |
| A4 | Rotular formato e ângulo no nome de todo anúncio novo ou reativado da Pós (provas, março e abril), no padrão D12 do cmo; registrar na planilha o rótulo dos anúncios ativos e preencher a tabela de correspondência da seção 8.7 (nome e utm_campaign atuais de cada campanha no ar, ligados à chave pos_<código>), sem renomear no gerenciador o que já roda | sem rótulo, não dá para saber qual ângulo funciona (H3 da 1.32); renomear anúncio ativo não é necessário para a leitura e evita qualquer efeito na entrega [SUPOSIÇÃO de precaução] | sem custo de mídia | leitura de ângulo e formato a partir de 03/11 | voltar ao padrão de nome anterior nas campanhas novas | 31/10 (com a estrutura das provas, anuncios-meta e anuncios-google) |
| A5 | Congelar mudanças por desempenho nas 6 ativas sem bloqueio de elegibilidade (707, 68604, 68606, 68608, 68610, 289) até a primeira leitura com 3 a 7 dias de dados e metas de PP1; só valem as ações de calendário e conformidade já aprovadas (D2, D9, D18, D20, PP5, PP9) | mudança antes da linha de base apaga a comparação e pode reabrir o aprendizado (skill, passo 2) | sem custo de mídia | linha de base limpa para a 1.13 e para a revisão de 09/11 | liberar ajustes na revisão seguinte, com pedido | a partir de hoje até a primeira leitura numérica |

---

## 11. O que observar a seguir

| Métrica | Onde | Confirma o diagnóstico | Derruba o diagnóstico |
|---|---|---|---|
| URL final dos anúncios de 662, 68662 e 698 | gerenciador | 662 abre a página com 15/08/2026, 68662 abre a de 24/04/2027 e 698 mostra 2027: o elo "chegada" é o gargalo dessas três | as URLs abrem páginas com a data da planilha (decisão 12): essas campanhas entram na leitura normal |
| Gasto acumulado das 6 turmas iniciadas desde a data de início | gerenciador | gasto acima de zero depois do início: houve verba em turma "verificar" | gasto zero desde o início (campanha ativa sem entrega): a visão estava desatualizada (C1 da 1.32) |
| Percentual de leads com código do catálogo e UTM | CRM e gerenciador | abaixo de 100% [valor exato DADO NÃO FORNECIDO]: o elo "matrícula" não fecha por turma e PP4 é urgente | 100% com código: a leitura por turma já é possível |

---

## 12. Notas sobre arquivos de outros agentes (não alterados)

- gestor-de-midia-pos-2026-10-26.md (1.11), seção 7: a encomenda desta etapa pedia diagnóstico "com a exportação do memorando". A exportação não chegou; este arquivo entrega a parte estrutural e o roteiro, e a versão numérica sai 2 dias úteis depois da exportação.
- gestor-de-midia-geral-2026-10-26.md (memorando), D1: a decisão para 68662 não muda, mas N1 (datas cruzadas com 662) pede que a conferência de URL das duas campanhas seja feita no mesmo dia. D9 e D18 podem precisar ser antecipadas se A3 confirmar que a data de 30 dias antes é prazo.
- analise-de-campanha-pos-2026-10-26.md (1.32), seção 1.1: a linha "Pneumologia (código [CONFIRMAR])" sem campanha tem a data da 670, e não a da 68636 (N6). Sugestão para a próxima versão: tratar como 670 até a Ufape dizer o contrário.
- Para a estrategia-de-midia (1.13): as 3 ativas sem bloqueio (68608, 68610, 289) são as únicas com leitura de desempenho útil nesta rodada; para março e abril, os históricos de 68605, 666, 68607 e 586 são a linha de base por área (seção 8.3).

---

## 13. Auditorias

### 13.1 auditorias/11-midia-paga.md (aplicada a este diagnóstico)

| Item | Resultado | Observação |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais justificados | Pendente externo | 1.11 aguarda PP2, PP13 e PP14 |
| Metas de CPL e custo por matrícula escritas antes de subir | Pendente externo | fórmulas no 1.11; valores em PP1 |
| Verba dentro do valor aprovado, com aprovador | Pendente externo | verba e aprovador [CONFIRMAR] |
| Nomenclatura padrão | Pendente externo | ação A4, tabela de correspondência (8.7) e PP4 do 1.11, no padrão D12 do cmo |
| UTMs completas e origem no CRM | Pendente externo | seção 6; portão G4 |
| Pixel, API de Conversões, conversões do Google | Pendente externo | D8 do memorando; elo 5 da seção 4 |
| Criativos em conformidade educacional | Pendente externo | este arquivo não cria criativo |
| Anúncios dentro das políticas | Não se aplica | nenhum anúncio criado aqui |
| Nenhum público com menores de 18 anos | Não se aplica | nenhum público criado aqui |
| Post de docente promovido com autorização | Não se aplica | nenhum post |
| Relatório semanal ao cmo | Atendido no desenho | calendário de leitura na seção 8.6 |
| Sem segmentação discriminatória | Não se aplica | |
| Públicos sem dados pessoais sem base legal | Atendido | nenhum público, nenhum dado pessoal |
| Dados de curso conferidos no catálogo | Atendido | códigos, turmas, datas, status e alertas da seção 3 vêm do catálogo e da auditoria de 26/10 |
| Destino de WhatsApp oficial | Não se aplica | a mídia da Pós não leva ao WhatsApp |
| Números da análise só das exportações fornecidas | Atendido | nenhum número de desempenho; as únicas contas são dias, datas de 30 dias antes e contagens da visão e da auditoria |
| Nenhuma alteração sem humano executar e aprovar | Atendido | toda ação está na seção 10 com o que, por que, quanto, efeito e como desfazer |

### 13.2 auditorias/conformidade-educacional.md (pontos que este arquivo toca)

| Item | Resultado | Observação |
|---|---|---|
| Dados de curso iguais ao catálogo | Atendido | seção 3; divergências marcadas (68662, 662, 698, 366, 352, 68617, 679) |
| Turma "verificar" sem chamada para inscrição | Atendido | as 6 iniciadas ativas seguem com pedido de pausa (D1) |
| Sem frase de certificação ligada ao MEC | Atendido | a frase é citada só como pendência das páginas (N4), nunca como afirmação |
| Bolsa e desconto com regra | Atendido | anúncio de turma não promete bolsa (8.3); 341 só com a regra (PP7) |
| Urgência real | Atendido | nenhuma urgência sem número real do catálogo; turma mínima tratada como piso |
| Destino entrega o que o anúncio promete | Pendente externo | 698, 662 e 68662 (ação A2; D2; PP5) |
| Nenhum dado pessoal | Atendido | |
| Texto sem travessão nem meia-risca | Atendido | conferido por busca dos caracteres no arquivo |

**Resultado:** pronto para o gestor-de-midia e para o qa-de-marketing. Não libera nenhuma mudança no gerenciador; as ações da seção 10 esperam aprovação humana.

---

## Mudanças desta versão

Versão 2 (26/10/2026), pela seção 12 do plano do cmo e pela revisão qa-de-marketing-geral-2026-10-26-loteB:
- **Tabela de correspondência (D12):** nova seção 8.7, que liga as 14 ativas da visão à chave pos_<código>, com nome e utm_campaign atuais a preencher pela exportação (A1), sem renomear nada; A4 e G4 passam a usá-la.
- **Datas da planilha (decisão 12):** 68662 em 15/08/2026 e 662 em 24/04/2027; N1 fechado quanto à data, a suposição de datas trocadas sai; A2, tabela de decisão e "o que observar" refeitos para a conferência de URL de 28/10 (PP5; R5 do cmo).
- **Leitura de leilão (NE1 e NE4):** seção 8.5 e calendário de 06/11 e 09/11, para as provas de Anestesiologia e Neurologia na janela de 03/11 a 18/11.
- **AM1:** as provas ligadas às turmas de 28/11 completas (68646 e 68651 para 68610 e 68608; 68641 e 68642 para a 698). **AM2:** grafias de 659 e 719 acrescentadas.
- **Turma mínima de 15 (decisão 11):** metas, leitura por grupo e conta do ritmo necessário (15 menos matrículas acumuladas).
- **EM9 do cmo** refletido na leitura de 289 e 662.

## Fatos (com fonte)

- 42 linhas de Pós na visão: 14 ativas, 18 pausadas, 10 sem campanha; 6 ativas em turma já iniciada (visão de campanhas; 1.32, seção 1.1).
- Status "verificar" de 650, 68662, 706, 586, 554, 68612, 653, 665, 666, 68605, 659 e 68607; datas, turmas e preços de todas as turmas citadas (catálogo, seção 2, 26/10/2026).
- 68662: planilha 15/08/2026, site 24 e 25/04/2027, turma V; 662: planilha 24/04/2027, site 15 e 16/08/2026, turma IV; 678 é Odontologia, turma IV, 15/08/2026, só no site (auditoria do catálogo de 26/10, seção 3; catálogo). Valem as datas da planilha (decisão 12 da Ufape, docs/execucao-2026-10-26.md).
- 698 com 28/11/2027 no site e 28/11/2026 na planilha; 366 e 352 com data divergente; 68617, 68628 e 662 com turma divergente (auditoria de 26/10, seção 4; plano do cmo, P3 a P5).
- 46 páginas com a frase de certificação ligada ao MEC; entre as ativas da Pós, só 707 e 586 não estão na lista (auditoria de 26/10, seção 9).
- 1ª mensalidade paga 30 dias antes do início na maioria das páginas (contexto da linha); turma mínima de 15, também nas turmas de Pós (decisão 11 da Ufape); algumas páginas de turma ainda mostram 20.
- Padrão de nomes D12 (chave pos_<código>; campanhas no ar não renomeadas, lidas por tabela de correspondência), EM9 e sobreposição de público de 03/11 a 18/11 (plano do cmo, 12.6 e 12.7).
- Grafias "Pós-graduação Cirurgia Cardiorrespiratória" (659) e "Pós-Graduação Inteligência Artificial na Saúde" (719) (catálogo, seção 2).
- 670 (Pneumologia, turma VII) com início em 10/04/2027, encerrado; 68636 (turma VIII) com 17/04/2027, só no site (catálogo).
- Formatos e ângulos de cada campanha (visão de campanhas).
- Regras de decisão, metas como fórmula e pedidos D1 a D21 e PP1 a PP14 (memorando e 1.11).
- Regras práticas de dados suficientes e tabela de sintomas (skill diagnostico-de-midia).

## Suposições

- [SUPOSIÇÃO] Efeito de disputa de leilão entre as provas de Anestesiologia e Neurologia, o Workshop e a 616 de 03/11 a 18/11 (NE1 e NE4). Origem: conjuntos da mesma conta com públicos parecidos disputam a mesma entrega.
- [SUPOSIÇÃO] A linha "Pneumologia, 10/04/2027" da visão é a da 670, e não a da 68636 (N6). Origem: a data igual à da 670.
- [SUPOSIÇÃO de precaução] Não renomear anúncios que já rodam (A4), para não arriscar efeito na entrega; o rótulo dos ativos fica na planilha.
- [SUPOSIÇÃO] As campanhas de janela longa (289, 662) e a de pacote único na reta final (707) são as primeiras candidatas a fadiga. Origem: janela de veiculação e pacote na visão.
- Usadas como estão, das entradas: N = 2 semanas em R6, escala em passos de até 20% da diária, leitura de custo por matrícula 30 dias depois do início (todas [SUPOSIÇÃO] do 1.11 e da 1.32).

## Dados que faltam

- [CONFIRMAR] Exportação agregada de Meta e Google por campanha, anúncio e semana desde 01/08/2026 (memorando 7.1), com URL final, data de criação, formato e ângulo por anúncio (A1).
- [CONFIRMAR] Plataforma, objetivo e evento de otimização de cada uma das 32 campanhas com status.
- [CONFIRMAR] Metas em reais (PP1 do 1.11): evasão, desconto, custo variável, margem, conversão lead para matrícula e inscrito para matrícula.
- [CONFIRMAR] Turma real de 662 (turma diverge, P5), situação da 678 e URL final dos anúncios de 68662 e 662 (A2).
- [CONFIRMAR] Se a 1ª mensalidade 30 dias antes do início é prazo de matrícula, por turma (A3).
- [CONFIRMAR] Política de entrada em turma iniciada (E1 e E2 do memorando).
- [CONFIRMAR] Motivo da pausa de cada uma das 18 pausadas.
- [CONFIRMAR] Nome e utm_campaign atuais de cada campanha ativa, para a tabela de correspondência (8.7); CRM usado e definição de lead, inscrito e matriculado.
- [CONFIRMAR] Tolerância aceitável de diferença entre gerenciador e CRM (com o analista-de-dados).
- [CONFIRMAR] Curso realmente anunciado pela campanha pausada da linha "Citopatologia 03/04" (679).
- [CONFIRMAR] Linha da visão que corresponde à 68636 e status de mídia de 68636, 68629 e 359.
- [CONFIRMAR] Status do pixel, da API de Conversões e das conversões do Google (D8).
- [DADO NÃO FORNECIDO] Gasto, impressões, alcance, frequência, cliques, CTR, CPC, CPM, leads, inscritos, matrículas, CPL e custo por matrícula de qualquer campanha.

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma.

---

**Próximo agente sugerido:** criativos-de-anuncio (pacote de reativação de 68615, 366 e 68617 e vídeo de 68610, com rótulo de formato e ângulo no nome, ação A4). Antes, o gestor-de-midia leva as ações A1 a A5 à aprovação humana e o qa-de-marketing revisa este arquivo.
