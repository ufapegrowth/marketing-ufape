# QA de marketing: departamentos 03 (SEO técnico) e 08 (análise CRO de Pós e Livres)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** geral (revisa uma saída geral, uma de Pós e uma de Livres com uma página de Eventos)
- **Data:** 26/10/2026
- **Status:** rascunho de revisão. Os arquivos revisados não foram editados. Nada foi publicado, enviado ou pago.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/cursos-livres.md; contexto/eventos.md; contexto/catalogo-de-cursos.md (completo, seções 1 a 9)
  - auditorias/03-busca.md; auditorias/08-conversao.md; auditorias/conformidade-educacional.md
  - docs/auditoria-do-catalogo-2026-10-26.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 8)
  - Fichas: contexto/cursos/pos/694, 707, 68610, 68639, 68662, 68636, 670; contexto/cursos/livres/573, 411, 713; contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md
  - Arquivos revisados: saidas/03-seo-e-busca/seo-tecnico-geral-2026-10-26.md; saidas/08-conversao/analise-cro-pos-2026-10-26.md; saidas/08-conversao/analise-cro-livres-2026-10-26.md

## Resumo dos vereditos

| Arquivo | Auditoria do departamento | Conformidade educacional | Veredito |
|---|---|---|---|
| seo-tecnico-geral-2026-10-26.md | 03-busca: sem falha bloqueante; itens dependentes de acesso ficam pendentes | sem item bloqueado | **CORRIGIR** (1 erro de fato com efeito em LGPD, 2 ajustes menores) |
| analise-cro-pos-2026-10-26.md | 08-conversao: item 8 (dados conferidos com o catálogo) falha em parte | item "dados do curso" com fonte atribuída errado | **CORRIGIR** (3 correções obrigatórias, 2 menores) |
| analise-cro-livres-2026-10-26.md | 08-conversao: item 8 falha (código de curso trocado) | item "dados do curso" falha | **CORRIGIR** (3 correções obrigatórias, 2 menores) |

Varreduras pedidas, nos três arquivos (leitura integral):
- Travessão ou meia-risca: nenhum encontrado. O hífen aparece só em marcador de lista, em nome de produto copiado do site (ex.: "Anual 2026") ou em código.
- "Últimas vagas", "vagas limitadas", "últimas bolsas": só aparecem como proibição ou como citação de problema. Nenhum uso como chamada.
- Frase de certificação ligada ao MEC ("CERTIFICADO PELO MEC", "reconhecida pelo Ministério da Educação (MEC)", "CERTIFICAÇÃO DO MEC"): só aparece entre aspas, como citação de problema. Passa.
- Dado pessoal: nenhum nome, telefone, CPF ou e-mail de aluno ou candidato. O nome da candidata da página 694 não está reproduzido (a ficha já traz "[nome removido: dado pessoal de candidato]"). Nenhum docente é nomeado nos três arquivos. Os e-mails citados são institucionais (secretaria), não pessoais.
- Afirmações sobre o site: os três arquivos declaram que não abriram faculdade.ufape.com.br e que tudo vem das fichas, do catálogo e das auditorias (seo-tecnico seção 0; CRO "Limites desta análise"). Passa.
- Número inventado: nenhum. Todas as contas foram refeitas pelo QA (lista de fatos no fim) e conferem, com as exceções apontadas abaixo.

---

## 1. saidas/03-seo-e-busca/seo-tecnico-geral-2026-10-26.md

### 1.1 Auditoria 03-busca, item por item

| Item | Resultado | Observação |
|---|---|---|
| Cada página prioritária tem uma única palavra-chave alvo | Pendente (não bloqueia) | V2 propõe alvos por página como [SUPOSIÇÃO], sem dado de busca. A definição fica com pesquisa-de-palavras-chave (etapa 2.1) e seo-on-page. |
| Títulos e descrições são únicos | Atende como diagnóstico | C1 e V1 mostram o problema (27 páginas com nome repetido) e a seção 4, item 8, propõe a regra "<Nome padrão> \| Faculdade UFAPE". Tag title real: [CONFIRMAR] com rastreador. |
| Nenhuma página importante bloqueada para indexação | Pendente | Sem acesso a robots.txt, noindex e Search Console; marcado [CONFIRMAR] (seção 3). |
| Nenhum link interno quebrado nas páginas principais | Pendente | Sem rastreamento; marcado [CONFIRMAR]. Links fora do ar (670, 68656) registrados. |
| Toda página aponta para a sua página pilar | Atende como recomendação | Seção 4 (uma URL canônica por curso, turmas dentro) e chamado SEO-04. |
| O conteúdo responde à principal pergunta de quem busca | Fora do escopo do técnico | Vai para seo-on-page; não bloqueia. |
| As correções estão escritas como chamados | Atende | Chamados SEO-01 a SEO-07, com problema, correção, esforço e reconferência. |
| Páginas de cursos ou turmas encerrados foram redirecionadas | Atende como recomendação | Mapa 301 por código (55 pós e 36 provas) e estados da turma (seção 5). |
| Dados de curso nas páginas batem com o catálogo | Atende com ressalva | Códigos, nomes, turmas, cargas horárias, preço da Odontologia e datas conferem com o catálogo e com a auditoria de 26/10. Ressalva na V6 (ver problema S2). |
| Páginas prioritárias têm bloco de resposta citável, FAQ real e marcação estruturada | Atende como recomendação | V3 e SEO-06, com JSON-LD só com dados do catálogo e sem preço, certificação ou docente. |
| O conteúdo principal aparece sem JavaScript | Pendente | V4 e SEO-05 com teste por curl; [CONFIRMAR]. |
| Nenhum resultado de assistente de IA registrado sem checagem real | Atende | Nenhum resultado de assistente de IA foi registrado. |
| Nenhuma consulta com duas páginas da Ufape disputando sem correção proposta | Atende | V2 traz correção para cada grupo; cliques em risco [CONFIRMAR]. |

### 1.2 Conformidade educacional, item por item

O arquivo é uma auditoria técnica com chamados, não uma peça. Itens de peça que não se aplicam estão marcados assim.

| Item | Resultado |
|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Passa. JSON-LD de 68636: nome, 500 h, turma VIII, 17/04/2027 e São Paulo conferem com o catálogo (seção 2). |
| Curso com status "aberto" (ou sem chamada para inscrição) | Passa. Nenhuma chamada para inscrição; o exemplo de marcação usa 68636, que está aberto. |
| Modalidade clara e correta | Passa. "blended" para semipresencial marcado [SUPOSIÇÃO]. |
| Graduação: ato regulatório do catálogo | Não se aplica (nenhum ato citado). |
| Pós lato sensu: sem "reconhecida pelo MEC" | Passa. A frase só aparece como citação de problema (linhas 72, 73, 401, 435). |
| Curso livre: não confere diploma | Não se aplica. |
| Nota MEC só com fonte oficial | Passa (nenhuma nota). |
| Sem promessa de emprego, salário ou sucesso | Passa. O arquivo ainda alerta para não prometer destaque na busca (V3). |
| Empregabilidade ou satisfação com fonte | Não se aplica. |
| Superlativos com fonte | Passa. |
| Comparação com concorrente | Não se aplica. A menção à UFAPE de Pernambuco (V7) é homonímia, sem comparação. |
| Preço com parcelas e condições | Passa. Só cita o preço da Odontologia como prova de duplicidade, igual ao catálogo; a marcação omite preço de propósito. |
| Bolsa e desconto com regra | Não se aplica. |
| Urgência real | Passa. |
| Prouni, Fies ou financiamento | Não se aplica. |
| Depoimentos e imagens com autorização | Passa. Person só com autorização (P13). |
| Menores de idade | Não se aplica. |
| Formulários com finalidade e política de privacidade | Não se aplica. |
| WhatsApp e e-mail com consentimento | Não se aplica. |
| Nenhum dado pessoal na peça ou nos arquivos de trabalho | Passa. O nome publicado na página 694 não é reproduzido. |
| Políticas da Meta e do Google | Não se aplica. |
| Página de destino entrega o prometido | Passa como alerta (C4: anúncios ativos e 301). |
| Itens de anúncio (característica pessoal, urgência falsa, pessoa pública, caixa alta, destino, drible da análise) | Não se aplica; o rascunho de robots.txt não sugere camuflar nada. |

Resultado da conformidade: aprovado (nenhum item bloqueado). O veredito do arquivo é corrigir por erro de fato (S1).

### 1.3 Problemas e correções

| # | Onde | Problema | Correção proposta | Obrigatória |
|---|---|---|---|---|
| S1 | Seção 1, item 2 (linha 21); C2, "Exemplo" e "O que isso custa" (linhas 72 e 73); chamado SEO-02, "Chamado paralelo" (linha 340); "Dados que faltam" (linha 433) | Afirma que **uma** das provas antigas publica nome de aprovado e deixa [CONFIRMAR se as outras provas antigas também listam aprovados]. A docs/auditoria-do-catalogo-2026-10-26.md, seção 2a, já registra que **13 provas antigas (680, 681, 682, 684, 685, 687, 688, 689, 690, 691, 693, 694 e 695) e a página 715** publicam a lista de aprovados com nome completo. O arquivo subestima o alcance de um problema de LGPD e o chamado paralelo ficaria incompleto. | Trocar por "14 páginas públicas (as 13 provas antigas e a 715, Programa de Aprimoramento em Terapia Intensiva) publicam nome completo de aprovados (auditoria de 26/10, seção 2a)". No chamado paralelo, listar os 14 códigos. Na tabela de C2, marcar a 715 com o mesmo alerta. Remover o [CONFIRMAR] respondido. Continuar sem reproduzir nenhum nome. | Sim |
| S2 | V6 (linha 199) e "Fatos" (linha 400) | "11 páginas sem data de início" lista 718, 68668 e 68618, que têm data no catálogo vinda da planilha (29/08/2026, 19/10/2026 e 18/12/2026). A auditoria de 26/10, seção 7, diz "site sem data de início". | Escrever "11 páginas sem data de início **no site** (a planilha tem data para 718, 68668 e 68618)". | Sim (precisão de dado de curso) |
| S3 | C2, "Exemplo" (linha 72) | "Mostra 'Avise-me'..." pode ser lido como acesso ao vivo, embora a seção 0 explique a origem. | Acrescentar "(texto da ficha contexto/cursos/pos/694)". | Não (recomendado) |
| S4 | V3 (linha 124) e Fontes | Datas do Google (12/06/2025 e 09/09/2025) vêm de fonte externa que o QA não conferiu. | Manter com a fonte citada; o próximo agente não deve transformar isso em peça sem reconferir. | Não (nota) |

**Veredito: CORRIGIR.** Volta ao seo-tecnico para S1 e S2. Depois da correção, segue para aprovação humana; os chamados só vão ao time do ufape-site com essa aprovação.

---

## 2. saidas/08-conversao/analise-cro-pos-2026-10-26.md

### 2.1 Auditoria 08-conversao, item por item

| Item | Resultado | Observação |
|---|---|---|
| Topo passa no teste dos 5 segundos (celular) | Atende como análise | Teste feito nas três páginas pela ordem do texto, marcado [SUPOSIÇÃO] e [CONFIRMAR no site, no celular]. |
| Uma chamada para ação principal por página | Atende | COMPRAR continua principal; o botão de WhatsApp entra como secundário. |
| Formulário pede só o necessário | Pendente | Propõe "formulário curto" sem listar os campos. Recomendado: o landing-page define os campos mínimos, com finalidade e política de privacidade. Não bloqueia. |
| Provas reais e autorizadas | Atende | Depoimentos, vídeo e docentes só com autorização registrada. |
| Objeções respondidas na página | Atende | As três objeções da linha mapeadas por página, com texto proposto. |
| Testes têm hipóteses escritas | Atende | Três correções com hipótese [SUPOSIÇÃO], métrica primária e de proteção por página. |
| Resultados registrados, vencedores e perdedores | Não se aplica ainda | Nenhum teste rodou; linha de base [CONFIRMAR]. |
| Dados do curso conferidos com o catálogo | **Falha em parte** | 707 e 68610 conferem. Na 68639, o preço é atribuído à seção 3 do catálogo, que não tem coluna de preço (problema P2). |
| Eventos de lead e inscrição rastreados e lead no CRM | Pendente | Recomendado; ferramenta e CRM [CONFIRMAR]. |

### 2.2 Conformidade educacional, item por item

| Item | Resultado |
|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | **Falha em parte.** 707 (600 h, 24 módulos, VII, 30/10/2026, 30x de R$ 1.590,00, R$ 47.700,00, matrícula R$ 250,00) e 68610 (500 h, V, 28/11/2026, 30x de R$ 1.000,00, R$ 30.000,00) conferem. A 68639 cita preço como se viesse do catálogo (P2). |
| Curso com status "aberto" | Passa. 707, 68610 e 68639 estão abertos. |
| Modalidade clara e correta | Passa. |
| Graduação: ato regulatório | Não se aplica. |
| Pós lato sensu: sem "reconhecida pelo MEC" | Passa. Só citações de problema (linhas 131, 143, 243, 254, 384). |
| Curso livre | Não se aplica. |
| Nota MEC | Passa (nenhuma). |
| Sem promessa de emprego, salário ou sucesso | Passa. Os subtítulos propostos para 707 e 68610 descrevem conteúdo e formato da ficha, sem promessa. |
| Empregabilidade com fonte | Não se aplica. |
| Superlativos com fonte | Passa. Os superlativos da página são apontados e não repetidos. |
| Comparação com concorrente | Não se aplica. |
| Preço com parcelas e condições | Passa. Totais conferidos; matrícula separada apontada. |
| Bolsa e desconto com regra, público e prazo | Passa como alerta. O arquivo exige regra, turma elegível e validade antes de qualquer peça. |
| Urgência real | Passa. Proíbe "últimas vagas" sem número. |
| Prouni, Fies | Não se aplica. |
| Autorização de imagem | Passa. |
| Menores | Não se aplica. |
| Formulários com finalidade e política | Passa como alerta ([CONFIRMAR no site]). |
| WhatsApp e e-mail com consentimento | Passa. O lembrete da prova vai só "com consentimento", pelo CRM. |
| Nenhum dado pessoal | Passa. Coordenadores e docentes não são nomeados. |
| Plataformas e anúncios | Passa como alerta (página de destino com frase ligada ao MEC sinalizada, pedido A7). |

Resultado da conformidade: bloqueado no item de dados do curso até corrigir P2.

### 2.3 Problemas e correções

| # | Onde | Problema | Correção proposta | Obrigatória |
|---|---|---|---|---|
| P1 | Página 3, "O que já funciona", 2º item (linha 279); "Conformidade" da Página 3, 2º item (linha 343); "Fatos", último item (linha 391) | Afirma que contexto/pos-graduacao.md e o plano do cmo (P10) tratam os percentuais de bolsa como vazios ou [PREENCHER]. **É falso:** contexto/pos-graduacao.md (atualizado em 26/10/2026, linha 17) já traz 11 bolsas por prova (2 de 50% com monitoria, 4 de 25%, 5 de 10%), e a P10 do plano do cmo está "resolvido em 26/10/2026". Contradiz o contexto e o plano. | Reescrever: "Os percentuais estão na ficha 68639 e em contexto/pos-graduacao.md (P10 resolvida em 26/10/2026). Não estão na tabela do catálogo; antes de peça final, [CONFIRMAR NO CATÁLOGO]". Apagar a "nota para o cmo atualizar". | Sim |
| P2 | Página 3, "Dados conferidos no catálogo (seção 3)" (linha 265); "Fatos", item da 68639 (linha 386) | Atribui ao catálogo, seção 3, o preço da inscrição (R$ 100,00 à vista ou 1x no cartão). A seção 3 do catálogo só tem código, curso, local, início e status. O preço está na ficha 68639 e em contexto/pos-graduacao.md. Há divergência interna: a auditoria de 26/10, seção 2, diz que o preço "passa a ter" lugar no catálogo, mas a tabela não tem a coluna. | Mudar a fonte para "ficha 68639 e contexto/pos-graduacao.md; o catálogo, seção 3, não traz preço: [CONFIRMAR NO CATÁLOGO]". Registrar a divergência como nota para o cmo pedir a coluna de preço na seção 3. | Sim |
| P3 | "Suposições", último item (linha 403) | "[SUPOSIÇÃO] A prova 68646 segue regras parecidas com as da 68639." O contexto da linha registra que as regras das 22 provas são iguais em todas (lidas em 26/10/2026). | Transformar em fato com fonte: "Regras das 22 provas iguais (contexto/pos-graduacao.md); a turma de destino da 68646 continua [CONFIRMAR]". | Sim (suposição já respondida por fonte interna) |
| P4 | Página 1, problema 2 (linha 65) e "Fatos" (linha 381) | "Módulos 11 e 22 com rótulo misto": o 11 é "Prático/Presencial" (não é misto) e o 15 é "Teórico/On-line". A contagem de 10 presenciais e 14 online confere. | Trocar por "módulo 22 com rótulo misto (Teórico/Prátrico/Presencial)". | Não (precisão) |
| P5 | Página 3, "Site ou plataforma nova", item 2 (linha 309) | Cita "decisão P72" sem dizer de que documento é (o plano do cmo de 26/10 só vai de P1 a P18). | Indicar o documento de origem da P72 ou marcar [CONFIRMAR fonte]. | Não |

**Veredito: CORRIGIR.** Volta ao analise-cro para P1, P2 e P3. Os textos propostos (heróis, FAQ, blocos) seguem como rascunho e não viram peça sem o texto de certificação aprovado e a turma de destino das provas.

---

## 3. saidas/08-conversao/analise-cro-livres-2026-10-26.md

### 3.1 Auditoria 08-conversao, item por item

| Item | Resultado | Observação |
|---|---|---|
| Topo passa no teste dos 5 segundos (celular) | Atende como análise | Feito nas quatro páginas, marcado [SUPOSIÇÃO] e [CONFIRMAR no celular]. |
| Uma chamada para ação principal por página | Atende | No evento, propõe "Ver ingressos" no topo como ação principal; nos demais, COMPRAR segue principal. |
| Formulário pede só o necessário | Pendente | "Formulário curto" sem campos definidos; mesmo encaminhamento da Pós. |
| Provas reais e autorizadas | Atende | Docentes não nomeados; tudo com [CONFIRMAR autorização]. |
| Objeções respondidas na página | Atende | Objeções 1, 2 e 3 da linha mapeadas. |
| Testes têm hipóteses escritas | Atende | Três correções com hipótese por página; antes e depois para 573 e evento, pela janela curta. |
| Resultados registrados | Não se aplica ainda | Nenhum teste rodou. |
| Dados do curso conferidos com o catálogo | **Falha** | 573, 411, 713 e evento conferem com o catálogo e as fichas, mas a Página 3 atribui o código 68635 à Pós em Terapia Intensiva (problema L1). |
| Eventos de lead e inscrição rastreados e lead no CRM | Pendente | Recomendado; ferramenta e CRM [CONFIRMAR]. |

### 3.2 Conformidade educacional, item por item

| Item | Resultado |
|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | **Falha.** 573 (28 h, 14/11/2026, R$ 2.350,00 ou 10x de R$ 303,00), 411 (12 h, R$ 420,00 ou 6x de R$ 98,00), 713 (R$ 734,00 ou 10x de R$ 88,00) e evento (16 h, 30 vagas, R$ 1.250,00 e R$ 450,00, cupom SIMPNEUROMONIT) conferem. Erro: 68635 apresentado como turma de Terapia Intensiva (L1). |
| Curso com status "aberto" | Passa. 573 aberto; 411 e 713 aberto (contínuo); evento aberto. |
| Modalidade clara e correta | Passa. "Semiprensecial" é apontado como erro de grafia do site e não é repetido em texto novo. |
| Graduação | Não se aplica. |
| Pós lato sensu | Passa (nenhuma frase ligada ao MEC; linha 372 registra a ausência na página do evento). |
| Curso livre: não confere diploma | Passa. O arquivo exige o texto padrão [PREENCHER COM A REGULAÇÃO] e mantém a seção de certificação oculta. |
| Nota MEC | Passa. |
| Sem promessa de emprego, salário ou sucesso | Passa. O subtítulo da 573 evita "o melhor diagnóstico". |
| Empregabilidade com fonte | Não se aplica. |
| Superlativos com fonte | Passa com nota: o texto proposto para o 713 fala em "literatura mais recente" (linha 296); é leve, mas o editor deve trocar por "artigos científicos", como está na ficha. |
| Comparação com concorrente | Passa. O bloco sobre conteúdo gratuito do 411 não ataca terceiros. |
| Preço com parcelas e condições | Passa. Totais conferidos pelo QA: R$ 3.030,00, R$ 3.300,00, R$ 588,00 (40% acima), R$ 880,00 (20% acima), R$ 1.000,00 e R$ 360,00 com cupom. |
| Bolsa e desconto com regra, público e prazo | Passa como alerta (cupom sem validade nem limite na página). |
| Urgência real | Passa. "Somente 30 vagas" tem número real no catálogo; "Garanta sua vaga!" do 573 é apontado como problema. |
| Prouni, Fies | Não se aplica. |
| Autorização de imagem | Passa. |
| Menores | Não se aplica. |
| Formulários com finalidade e política | Passa como alerta. |
| WhatsApp e e-mail com consentimento | Passa (o texto do cupom para a base fica condicionado ao CRM). |
| Nenhum dado pessoal | Passa. Nenhum docente nem participante nomeado. |
| Plataformas e anúncios | Passa como alerta: data 14/11 contra 29/11 do 573 (P6) e link para outro domínio no 411. |

Resultado da conformidade: bloqueado no item de dados do curso até corrigir L1.

### 3.3 Problemas e correções

| # | Onde | Problema | Correção proposta | Obrigatória |
|---|---|---|---|---|
| L1 | Página 3 (713), problema 7 (linha 287) | "pós de Terapia Intensiva (turmas abertas no catálogo, 68635 e 68623)". No catálogo, 68635 é a **Pós-graduação em Clínica Médica e Emergência de Pequenos Animais**. A única turma aberta de Terapia Intensiva e Emergência Veterinária é a 68623 (Goiânia, 22/05/2027); a 666 (SP) está "verificar". | Trocar por "Pós-graduação em Terapia Intensiva e Emergência Veterinária (68623, Goiânia, aberta; 666, SP, em verificar)". Se quiser citar a 68635, nomeá-la corretamente como Clínica Médica e Emergência. | Sim |
| L2 | Página 2 (411), "O que já funciona", 2º item (linha 166) | "Cronograma específico com 14 itens". A ficha 411 lista 15 itens (14 tópicos mais "PRÁTICA DE ECOCARDIOGRAMA"). | Trocar por "15 itens (14 tópicos e a prática)". | Sim (número sem conferência) |
| L3 | Cabeçalho, "Linha" (linha 4), e toda a Página 4 | O arquivo de linha livres inclui a página do evento. O briefing (regras de nome) e contexto/eventos.md pedem saída por linha (<agente>-eventos-AAAA-MM-DD.md), e a etapa 1.30 do plano do cmo prevê só "pos, livres". | Mover a Página 4 para saidas/08-conversao/analise-cro-eventos-2026-10-26.md (com cabeçalho e as três listas) ou registrar a decisão do cmo que autoriza o arquivo misto. | Sim (organização; o conteúdo da Página 4 está correto) |
| L4 | Página 3, "Comparação com o template" (linha 337) | Cita "decisão P72" sem documento de origem. | Indicar o documento ou marcar [CONFIRMAR fonte]. | Não |
| L5 | Página 3, "O que a squad escreve", item 2 (linha 296) | "a literatura mais recente": superlativo leve, sem fonte. | Trocar por "artigos científicos" (texto da ficha 713). | Não (recomendado) |

**Veredito: CORRIGIR.** Volta ao analise-cro para L1, L2 e L3.

---

## 4. Contradições entre os arquivos e com as fontes

| # | Entre | Situação | Encaminhamento |
|---|---|---|---|
| X1 | seo-tecnico x docs/auditoria-do-catalogo-2026-10-26.md | Uma prova contra 14 páginas com nome publicado. | S1. |
| X2 | analise-cro-pos x contexto/pos-graduacao.md e plano do cmo (P10) | Percentuais "vazios" contra percentuais registrados e P10 resolvida. | P1. |
| X3 | analise-cro-pos x catálogo, seção 3 | Preço da prova atribuído ao catálogo, que não o traz. | P2; nota ao cmo sobre a coluna de preço. |
| X4 | seo-tecnico x analise-cro-pos | Os dois falam em 46 páginas com a frase ligada ao MEC, com fontes diferentes (auditoria de 26/10, seção 9, e plano do cmo, P2). O número confere nas duas fontes. | Sem correção. |
| X5 | seo-tecnico x analise-cro-livres | 68634 com 24 h na loja contra 16 h do evento: os dois registram igual e mandam corrigir a loja. Duplicidades 623/68637 e 643/713: os dois deixam a escolha com a Ufape. | Sem correção. |
| X6 | Os três arquivos | Nenhum diverge sobre turma mínima, datas de início, preços ou status. A divergência 15 contra 20 alunos (prova contra turma) aparece só na análise da Pós e já está registrada no contexto da linha. | Sem correção. |

## 5. Encaminhamento

- seo-tecnico-geral-2026-10-26.md: volta ao **seo-tecnico** (S1 e S2). Depois, aprovação humana antes de qualquer chamado ir ao time do ufape-site.
- analise-cro-pos-2026-10-26.md: volta ao **analise-cro** (P1, P2 e P3).
- analise-cro-livres-2026-10-26.md: volta ao **analise-cro** (L1, L2 e L3).
- Regra de aprovação: a tabela de ufape-geral.md está vazia. Até a Ufape nomear quem aprova (P12 e A9 do plano), a aprovação vai à pessoa do marketing que fez o pedido.
- Nada foi publicado, enviado ou pago. Os arquivos revisados não foram alterados.

---

## Fatos (com fonte)

- Catálogo, seção 2: 55 páginas de pós; 707 (São Paulo, semipresencial, VII, 30/10/2026, 600 h, 30x de R$ 1.590,00, R$ 47.700,00, matrícula R$ 250,00, aberto); 68610 (V, 28/11/2026, 500 h, 30x de R$ 1.000,00, R$ 30.000,00, aberto); 68636 (VIII, 17/04/2027, 500 h, aberto, só no site); 68635 = Clínica Médica e Emergência de Pequenos Animais; 68623 = Terapia Intensiva e Emergência Veterinária, Goiânia, aberto; 666 = Terapia Intensiva, SP, verificar.
- Catálogo, seção 3: colunas código, curso, local, início e status (sem preço); 22 provas abertas em 27/11/2026; 13 antigas sem venda; 68656 fora do ar.
- Catálogo, seções 4, 5, 7 e 9: 573, 411, 713 e evento com os dados citados na seção 3.2 deste relatório. Resumo do catálogo: 184 produtos.
- docs/auditoria-do-catalogo-2026-10-26.md: seção 2a (13 provas antigas e a 715 publicam nome completo de aprovados); seção 3 (2 links trocados); seção 4 (7 datas divergentes); seção 5 (3 turmas divergentes); seção 6 (36 iniciadas à venda, 18 delas de pós); seção 7 (11 sem data no site); seção 8 (25 sem venda ou fora do ar); seção 9 (46 páginas com a frase ligada ao MEC).
- contexto/pos-graduacao.md (26/10/2026): regras iguais nas 22 provas, 11 bolsas (2 de 50%, 4 de 25%, 5 de 10%), nota de corte 7,0, mínimo 15 na prova contra 20 nas turmas.
- Plano do cmo: P10 resolvida em 26/10/2026; etapa 1.30 com linhas "pos, livres"; pendências numeradas de P1 a P18.
- Ficha 694: nome do aprovado já removido; prova de 04/02/2026; frase "reconhecida pelo Ministério da Educação (MEC)".
- Ficha 707: 10 módulos presenciais (4, 6, 8, 11, 14, 17, 19, 21, 22, 24) e 14 online; "Alertas: nenhum"; cabeçalho "CERTIFICAÇÃO DO MEC".
- Ficha 68610: 7 módulos presenciais (5, 9, 14, 18, 21, 22, 24); primeiro presencial em 20 e 21/03/2027; 18 professores; alerta de certificação marcado.
- Ficha 411: cronograma com 15 itens. Ficha 713: 23 aulas, 17 até 14/10/2026, 5 de 28/10 a 23/12/2026 e 1 a definir; 20 professores, 4 marcados "(EUA)".
- Contas refeitas pelo QA: 4, 19, 25, 32 e 33 dias a partir de 26/10/2026; 28/11 menos 30 dias = 29/10; 47.700 + 250 = 47.950; 10 x 303 = 3.030; 6 x 550 = 3.300; 6 x 98 = 588; 10 x 88 = 880; 20% de 1.250 e de 450 = 1.000 e 360 finais; 40 destinos e 55 códigos no mapa 301; 55 + 36 = 91.

## Suposições

- [SUPOSIÇÃO] A diferença sobre o preço das provas (auditoria de 26/10 diz que entrou no catálogo; a tabela da seção 3 não mostra) é falha de geração do catálogo, não decisão da Ufape.
- [SUPOSIÇÃO] A "decisão P72" citada nas duas análises CRO vem de um plano anterior da squad; não localizei o documento nesta revisão.
- [SUPOSIÇÃO] As datas de mudanças do Google citadas pelo seo-tecnico estão corretas; o QA não conferiu fontes externas.

## Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Preço da inscrição e percentuais das provas de bolsa na tabela da seção 3 do catálogo.
- [CONFIRMAR] Documento de origem da decisão P72.
- [CONFIRMAR] Decisão do cmo sobre manter a página do evento no arquivo de livres ou criar analise-cro-eventos-2026-10-26.md.
- [CONFIRMAR] Quem aprova cada tipo de peça (tabela vazia em contexto/ufape-geral.md; P12 e A9).
- [CONFIRMAR] Decisão da Ufape e do jurídico sobre as 14 páginas que publicam nome de aprovados (auditoria de 26/10, seção 2a).
