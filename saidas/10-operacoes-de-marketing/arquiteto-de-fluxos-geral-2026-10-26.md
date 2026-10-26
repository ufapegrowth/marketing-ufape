# Fluxo do mapa mental e dos JSON por curso: esquema versão 1, nomes, atualização, contrato de importação e riscos de dado pessoal

- Agente: arquiteto-de-fluxos (departamento 10, Operações de Marketing)
- Etapa do plano: M.1 (seção 4 do plano do cmo, "Mapa mental e JSON")
- Linha: geral (vale para graduacao, pos, livres e eventos)
- Data: 26/10/2026 (segunda-feira)
- Versão: 4 (26/10/2026), propaga as decisões 7 a 13 da Ufape e a seção 12 do cmo nos exemplos JSON antigos (707-p05, 68651-p03 e "PROVA PRESENCIAL"); mudanças no fim do arquivo. A versão 3 aplicou a seção 12 do plano do cmo e os ajustes do qa: campos de janela de silêncio, de participação em evento e de vínculo no CRM, fila D2, limite de 1 mensagem de campanha por dia e padrão de UTM D11 e D12 (seção 6 nova). Mudanças no fim do arquivo.
- Status: versão corrigida depois do veredito do qa-de-marketing (itens B1 a B6). Rascunho para nova conferência do qa-de-marketing e depois para a aprovação da pessoa do marketing. Nada foi gerado, publicado, enviado ou pago. Nenhum arquivo de .claude/commands foi criado: o texto dos workflows está na seção 3.9, pronto para virar arquivo depois da aprovação.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md, contexto/graduacao.md, contexto/pos-graduacao.md (relido com as regras das provas de bolsa), contexto/cursos-livres.md, contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seção "Como usar", resumo e seções 1 a 9; a seção 3 agora tem coluna de preço)
  - templates/kit-de-lancamento-pos.md, kit-de-lancamento-livres.md, kit-de-lancamento-evento.md, kit-de-lancamento-graduacao.md
  - templates/pagina-da-turma.md e templates/documento-de-fluxo.md
  - docs/visao-de-campanhas-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (inteiro; na versão 3, seção 12: D1, D2, D3, D8 a D12, D15 e encomendas de 12.10)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep09-10.md (veredito, seção do arquiteto-de-fluxos)
  - .claude/skills/mapear-fluxo/SKILL.md e .claude/skills/matriz-gut/SKILL.md (cabeçalho)
  - .claude/agents/arquiteto-de-fluxos.md, cmo.md, qa-de-marketing.md, relatorios.md
  - .claude/commands/arrumacao-mensal.md e campanha-de-vestibular.md (formato dos workflows)
  - auditorias/10-operacoes.md, auditorias/09-analytics.md, auditorias/conformidade-educacional.md
  - contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md
  - contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md
  - contexto/cursos/graduacao/editais-2027-1.md e graduacao-em-medicina-veterinaria.md (início)
  - contexto/cursos/eventos/neuro-summit-workshop-de-neuromonitorizacao-veterinaria.md (início)
  - README.md

## Correções desta versão (veredito do qa-de-marketing)

| Item | O que mudou |
|---|---|
| B1 | As bolsas deixam de ser "[CONFIRMAR]": bolsas_previstas vira lista de objetos (2 de 50% (monitoria), 4 de 25%, 5 de 10%), a pendência P10 está resolvida, e a pendência do 68651 trata só da turma de destino. Suposição 3 e item 5 de "dados que faltam" reescritos. O preço da prova agora vem da coluna de preço do catálogo (seção 3). |
| B2 | O mínimo de 15 alunos é copiado (não há contradição na ficha; a divergência é com os 20 das páginas de curso). Resultado por WhatsApp ou e-mail; o trecho da ficha com site e prazo de 7 dias vira pendência de divergência. Fato 7 corrigido. |
| B3 | Nenhum campo de texto do JSON repete a frase de certificação ligada ao MEC: 707-p02, 68651-p05, o texto de 1.7 e o pedido A7 usam "frase de certificação que a squad não repete". C10 e a regra 4.3 ampliadas para as variantes. |
| B4 | A conferência C11 foi reescrita (todo marcador e todo null aplicável é citado no campo "campos" de uma pendência) e os dois exemplos receberam as pendências que faltavam. Os dois exemplos passam na C11 (verificado campo a campo, ver 3.9). |
| B5 | R1 e R2 reescritas: campo de texto recebe "[CONFIRMAR]"; campo de número, data, lista ou objeto recebe null e uma pendência explica. A coluna "Tipo" e a coluna "Se vazio" de 1.3 foram ajustadas, "salvo quando a coluna Se vazio define outro valor" entrou na R1, e a C1 conta a Graduação uma vez só (184 no total). |
| B6 | Cópias da ficha 68651 agora são literais: modalidade "PROVA PRESENCIAL", nota de corte "7.0 (mínimo 70 % de acerto)"; fonte_da_data entra em campos_so_na_ficha, porque a seção 3 do catálogo não tem coluna "Fonte". |

## Resumo da proposta

1. Um arquivo JSON por item do catálogo (184 no total, Graduação incluída: 110 do recorte, 72 de histórico ou pendência e 2 da Graduação), com um esquema único, versão 1, em que tudo o que vem do catálogo é cópia literal e tudo o que falta fica marcado e explicado em pendências.
2. Um só escritor dos JSON: o agente cmo. Os outros agentes escrevem só as próprias saídas; o cmo, depois da aprovação, registra no JSON o que foi aprovado.
3. O HTML nunca lê a pasta de JSON em tempo real: o cmo embute os JSON dentro do próprio HTML, que abre offline.
4. Dois workflows novos e curtos: montar (3 etapas por onda) e atualizar (2 etapas por rodada).
5. Nada vai para o banco agora. A importação futura é um pedido ao ufape-admin, com o contrato de dados da seção 4.

---

## 1. Esquema JSON versão 1

### 1.1 Regras de preenchimento (valem para todos os campos)

| # | Regra |
|---|---|
| R1 | Origem vazia, ausente ou duvidosa em campo que se aplica ao tipo, salvo quando a coluna "Se vazio" de 1.3 define outro valor: campo de texto recebe exatamente "[CONFIRMAR]" (nos campos de autorização de imagem e voz, onde o campo é número, vale null e o marcador "[CONFIRMAR autorização]" vai na pendência). Campo de número, data, lista ou objeto recebe null, e uma pendência aberta cita o caminho do campo em "campos" (o campo irmão que explica). Nunca "", "N/A", 0 nem estimativa. |
| R2 | null sozinho (sem pendência que o cite) significa "não se aplica a este tipo ou a este item" (por exemplo, turma de uma prova de bolsa, início de um curso contínuo sem data, ficha de um item sem página). null com pendência que o cita significa "origem vazia, ainda não confirmada". A plataforma e o qa distinguem os dois pela pendência. |
| R3 | Bloco por tipo (prova_de_bolsa, graduacao, evento): só existe a chave do bloco do tipo do item. Os outros dois blocos não aparecem (nem como null). |
| R4 | Campos espelho (classe C) são cópia literal do catálogo (ou da ficha ou do contexto da linha, nos casos marcados em 1.3 e em campos_so_na_ficha). Nada é reescrito, corrigido, arredondado ou calculado. A cópia é do texto como está, inclusive espaços e grafia da fonte (por exemplo, "70 %" com espaço). Se o catálogo já traz marcador ("[CONFIRMAR NO SITE]", "[CONFIRMAR]"), o marcador é copiado em campo de texto e o item entra em pendencias. |
| R5 | Valores do catálogo que não são dado (data "XX DE XX DE 202X", "SEM DATA", "COLOCAR DATA?", "360 horas" no lugar da turma) seguem a R1: data vira null com pendência e a fonte da data vira "ausente"; texto vira "[CONFIRMAR]". |
| R6 | Dado que só existe na ficha ou no contexto da linha (não está no catálogo) pode ser copiado, mas o caminho do campo entra em fontes.campos_so_na_ficha. Assim o qa-de-marketing e a Ufape veem o que ainda não está no catálogo. |
| R7 | Se duas fontes divergem (planilha e site, ou dois trechos da mesma ficha), vale a regra do briefing (data: planilha; resto: site). Quando a divergência está dentro da mesma fonte, ou entre ficha e contexto, e não há regra, o valor do contexto da linha (já aprovado no plano) vale e a divergência vira pendência do tipo divergencia; se nem o contexto resolve, o campo segue a R1. |
| R8 | Cálculo permitido: só dias_ate_inicio, preco_estruturado (e só quando bate com o texto do site), resumo e o total do GUT. Nenhum outro número é calculado. |
| R9 | Texto livre (descricao, motivo, observacao): até 240 caracteres, sem nome de pessoa, sem e-mail, telefone ou CPF, sem frase de certificação ligada ao MEC (em nenhuma variante: "certificado pelo MEC", "reconhecida pelo MEC", "do MEC", "Ministério da Educação" como certificador), sem "últimas vagas". Para falar dessa frase, o texto escreve "frase de certificação que a squad não repete". |
| R10 | Nenhum campo de nome de pessoa em lugar nenhum do esquema. Docentes, coordenadores, palestrantes, aprovadores e alunos aparecem só como contagem ou como papel. |
| R11 | Suposição: toda proposta que não é dado (canais, destino de prova, vínculo com a visão de campanhas) leva a marca "[SUPOSIÇÃO]" no campo natureza ou marcador, e uma pendência com marcador "[SUPOSIÇÃO]". |
| R12 | Um só escritor: o cmo. Nenhum agente edita JSON de outro item nem o JSON em lote fora do fluxo da seção 3. |
| R13 | Formato do arquivo: UTF-8, sem BOM, fim de linha LF, recuo de 2 espaços, chaves na ordem do modelo de 1.5, datas AAAA-MM-DD (dia civil de São Paulo), valores em reais como número com ponto decimal (preço de 1.590,00 vira 1590.00). |
| R14 | Consistência entre status e recorte: recorte "planejar" só com status_catalogo "aberto" ou "aberto (contínuo)". Status "verificar", "sem venda", "encerrado" ou "sem página" vira "historico" ou "pendencia" (conformidade-educacional: só item aberto recebe chamada para inscrição). |

### 1.2 Classes de campo (definem quem pode mudar o quê)

| Classe | Nome | Quem muda | Quando muda |
|---|---|---|---|
| X | Controle | cmo | a cada gravação |
| C | Espelho do catálogo e da ficha | cmo, só copiando | quando o catálogo ou a ficha mudam (seção 3.5) |
| P | Plano | cmo | quando um plano do cmo é aprovado (nova versão do plano) |
| M | Mídia | cmo, com base na visão de campanhas | nova visão de campanhas, ou decisão de mídia aprovada e executada por humano (seção 3.6) |
| K | Kit e canais | cmo | saída de agente aprovada (seção 3.4) |
| A | Arquivos e aprovações | cmo | saída aprovada, ou resposta a pedido de aprovação |
| N | Números agregados e metas | cmo | quando a Ufape ou o gestor-de-midia entregam número (nunca inventado) |
| D | Derivado | cmo, calculado | a cada gravação |

### 1.3 Campo a campo

Legenda de "Obrig.": sim = a chave sempre existe; tipo X = a chave existe só nos tipos citados; não = pode faltar a chave. "Se vazio" diz o que escrever quando a origem está vazia (R1 e R2). Onde o tipo diz "ou null", o null com pendência que o cita é o vazio por origem ausente (R2).

#### Controle e fontes

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| versao_schema | X | inteiro | sim | 1 | fixo | não se aplica |
| id | X | texto | sim | igual ao nome do arquivo sem ".json" (seção 2) | regra de nomes | não se aplica |
| revisao | X | inteiro | sim | 1 ou mais; sobe 1 a cada gravação | cmo | não se aplica |
| revisao_aprovada | X | inteiro | sim | 0 ou mais, nunca maior que revisao | aprovação humana registrada | 0 até a primeira aprovação |
| estado_do_arquivo | X | texto | sim | ativo, substituido | cmo | não se aplica |
| substituido_por | X | texto ou null | sim | id de outro arquivo | cmo | null (não se aplica) |
| gerado_em | X | data | sim | AAAA-MM-DD | dia da criação | não se aplica |
| atualizado_em | X | data | sim | AAAA-MM-DD | dia da última gravação | não se aplica |
| fontes.catalogo | X | texto | sim | "contexto/catalogo-de-cursos.md" | fixo | não se aplica |
| fontes.data_catalogo | X | data ou null | sim | AAAA-MM-DD | campo "Gerado em" do catálogo | null com pendência |
| fontes.catalogo_linha_literal | X | texto | sim | cópia literal das colunas da linha do catálogo até a coluna "Fonte" (na seção 3, das provas, que não tem "Fonte", até "Status"), sem a coluna "Ficha" | catálogo | "[CONFIRMAR]" (item que só existe na planilha) |
| fontes.ficha | X | texto ou null | sim | caminho em contexto/cursos/ | catálogo | null (item sem ficha, não se aplica) |
| fontes.ficha_editais | X | texto | tipo graduacao | "contexto/cursos/graduacao/editais-2027-1.md" | catálogo, "Como usar" | "[CONFIRMAR]" |
| fontes.ficha_lida_em | X | data ou null | sim | AAAA-MM-DD | cmo | null (não se aplica) |
| fontes.contexto_da_linha | X | texto ou null | não | caminho do contexto da linha usado como fonte (por exemplo, contexto/pos-graduacao.md nas regras das provas de bolsa) | cmo | omitir a chave |
| fontes.campos_so_na_ficha | X | lista de texto | sim | caminhos de campo deste esquema, como "modulos" (dado que está na ficha ou no contexto da linha e não no catálogo) | cmo, conferido pelo qa | lista vazia |
| fontes.visao_de_campanhas | X | objeto (arquivo, data) ou texto | sim | arquivo em docs/visao-de-campanhas-AAAA-MM-DD.md | visão de campanhas | "[CONFIRMAR]" |
| fontes.plano | X | texto | sim | caminho do plano do cmo em vigor | plano | "[CONFIRMAR]" |
| fontes.auditorias | X | lista de texto | sim | caminhos em docs/ | auditorias do catálogo | lista vazia |

#### Identidade

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| codigo | C | texto | sim | código do catálogo, só dígitos, sem zero à esquerda; ou "sem-codigo" | catálogo | "sem-codigo" |
| linha | C | texto | sim | pos, livres, eventos, graduacao | seção do catálogo, ou plano quando o plano move o item | não se aplica |
| linha_origem | C | texto | sim | catalogo, plano | cmo | não se aplica |
| tipo | C | texto | sim | pos, prova_de_bolsa, livre_presencial (inclui semipresencial), livre_online (inclui gravados), minicurso, grupo_de_estudos, espanhol, aprimoramento, workshop, simposio, graduacao | seção e nome no catálogo | "[CONFIRMAR]" |
| nome_no_site | C | texto | sim | cópia literal | catálogo | "[CONFIRMAR]" |
| nome_padrao | C | texto | sim | pos: "Pós-graduação em <área>"; prova_de_bolsa: igual ao nome_no_site; demais tipos: igual ao nome_no_site [SUPOSIÇÃO: os contextos de Livres, Eventos e Graduação não definem padrão de nome] | regra da linha (contexto/pos-graduacao.md, "Padrão de nome") | "[CONFIRMAR]" |
| slug_sugerido | C | texto | sim | pos: "pos-graduacao-em-<area>" (sem acento, hífen); demais tipos: sem regra definida. É do curso, não da turma: duas turmas podem ter o mesmo slug | contexto/pos-graduacao.md | "[CONFIRMAR]" (todos os tipos fora de pos) |
| aliases | C | lista de texto | sim | outros nomes do mesmo item (por exemplo, o nome da planilha) | planilha e catálogo | lista vazia |
| pagina_oficial | C | texto ou null | sim | URL da página oficial | ficha (campo em campos_so_na_ficha) | "[CONFIRMAR]" se o status é aberto; null (não se aplica) se "sem página" |

#### Plano

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| area.codigo | P | texto | sim | A1 a A14, sem_area (item fora das 14 áreas, como histórico e Graduação), nao_se_aplica (Graduação) | plano, seção 2.3 | sem_area |
| area.nome | P | texto | sim | nome da área na seção 2.3 | plano | "[CONFIRMAR]" |
| area.natureza | P | texto | sim | plano_do_cmo, proposta ("[SUPOSIÇÃO]") | plano | não se aplica |
| recorte | P | texto | sim | planejar, historico, pendencia | plano, seções 2.1 a 2.4; regra R14 | não se aplica |
| motivo_do_recorte | P | texto | sim | até 240 caracteres | plano | "[CONFIRMAR]" |
| onda | P | inteiro ou null | sim | 1, 2, 3, null | plano, seção 3 | null (histórico e pendência, não se aplica) |
| modo_de_venda | P | texto | sim | com_data, continuo | status_catalogo ("aberto (contínuo)" vira continuo) | não se aplica |
| grupo_de_campanha | P | texto ou null | sim | id do grupo, por exemplo "provas-de-bolsa-2026-11-27" ou "sempre-ligado-A1" | plano, decisão A3 | null (não se aplica) |
| gut | P | objeto ou null | sim | g, u, t (inteiros de 1 a 5), total (g x u x t), motivo, natureza ("avaliacao_do_agente"), fonte | plano, seção 3 (skill .claude/skills/matriz-gut/SKILL.md) | null (não se aplica) se recorte não é planejar; null com pendência se é planejar e o grupo não tem nota |
| relacionados | P | lista de objetos | sim | id, relacao (duplicidade_provavel, modalidade_do_mesmo_evento, turma_de_destino, substitui), natureza (dado ou "[SUPOSIÇÃO]") | plano, P7 e seção 2.3; catálogo | lista vazia |

#### Espelho do curso, da turma ou da edição

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| local | C | texto | sim | cópia literal ("São Paulo", "SP", "Online", "Goiânia", "Lima - Peru" etc.) | catálogo | "[CONFIRMAR]" |
| modalidade | C | texto | sim | cópia literal (inclui erros de grafia do catálogo e, na prova de bolsa, o texto da ficha, como "PROVA PRESENCIAL", que é texto a corrigir no site: as provas são online, decisão 11 da Ufape) | catálogo ou ficha | "[CONFIRMAR]" |
| modalidade_normalizada | C | texto | sim | presencial, semipresencial, ead, online, gravacao, "[CONFIRMAR]". Tabela de equivalência em 1.4 | cmo, a partir de modalidade | "[CONFIRMAR]" |
| turma | C | texto ou null | sim | numeral romano do catálogo | catálogo | "[CONFIRMAR]" em pos com coluna vazia; null (não se aplica) em tipos sem turma (provas, livres, graduação, eventos) |
| carga_horaria | C | texto ou null | sim | cópia literal ("600 h", "4.195 h + 75 h de atividades complementares") | catálogo | "[CONFIRMAR]"; null (não se aplica) em prova_de_bolsa (a ficha da prova repete a carga horária da Pós, não a da prova) [SUPOSIÇÃO] |
| modulos | C | inteiro ou null | sim | número de módulos da ficha | ficha (campos_so_na_ficha) | null com pendência em pos; null (não se aplica) nos demais |
| inicio | C | data ou null | sim | AAAA-MM-DD; Graduação: início das aulas | catálogo (planilha) | null com pendência e fonte_da_data "ausente" (R5); null sem pendência em contínuo sem data |
| fonte_da_data | C | texto | sim | planilha, site, edital, pagina_do_evento, ausente | coluna "Fonte" do catálogo; na seção 3 (provas), que não tem a coluna, vem da ficha e entra em campos_so_na_ficha | ausente |
| dias_ate_inicio | D | inteiro ou null | sim | inicio menos atualizado_em, só quando modo_de_venda é com_data e inicio é data | calculado | null |
| fim_das_inscricoes | C | data ou null | sim | AAAA-MM-DD | catálogo ou ficha (nenhum traz hoje) | null com pendência; null sem pendência em contínuo |
| preco_texto_site | C | texto | sim | cópia literal da coluna de preço e condições (nas provas, coluna "Preço (site)" da seção 3) | catálogo ("site em 26/10/2026; conferir antes de publicar") | "[CONFIRMAR]" |
| preco_estruturado | D | objeto ou null | sim | moeda ("BRL"), parcelas, valor_parcela, total, matricula (matricula pode ser null). Só se bater com o texto; nunca é a fonte do preço | cmo, a partir de preco_texto_site | null |
| condicoes_especiais | C | lista de objetos | sim | tipo (cupom, promocao, desconto, outro), texto, codigo (só cupom), publico, validade (data ou null) | catálogo | lista vazia; promoção citada sem regra: validade null com pendência |
| status_catalogo | C | texto | sim | aberto, aberto (contínuo), verificar, sem venda, encerrado, sem página | catálogo | "[CONFIRMAR]" |
| status_catalogo_texto | C | texto | sim | cópia literal da célula de status | catálogo | "[CONFIRMAR]" |
| vagas.turma_minima | C | inteiro ou null | sim | número | catálogo ("Como usar", Graduação), contexto da linha ou ficha | null com pendência; null sem pendência quando o mínimo fica em outro bloco (prova de bolsa) |
| vagas.vagas_ofertadas | C | inteiro ou null | sim | número | ficha ou edital | null com pendência; null (não se aplica) na Graduação (vagas por turno ficam em graduacao.turnos) |
| vagas.vagas_restantes | N | inteiro ou null | sim | número somado entregue pela Ufape | números agregados | null com pendência P11 até a Ufape mandar número agregado (sem número real, nenhuma peça fala em últimas vagas) |
| equipe | C | objeto ou null | sim | coordenadores_na_ficha (inteiro ou null), docentes_na_ficha (inteiro ou null), autorizacoes_de_imagem_registradas (inteiro ou null). Só contagens, nunca nomes | ficha | null em cada contagem com pendência; autorizações: null com pendência de marcador "[CONFIRMAR autorização]"; equipe inteira null (não se aplica) em prova_de_bolsa, graduação e itens sem ficha |

#### Blocos por tipo (R3)

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| prova_de_bolsa.data_da_prova | C | data ou null | tipo prova_de_bolsa | AAAA-MM-DD | catálogo e ficha | null com pendência |
| prova_de_bolsa.horario_texto | C | texto | tipo prova_de_bolsa | cópia literal ("9 às 13h") | ficha (campos_so_na_ficha) | "[CONFIRMAR]" |
| prova_de_bolsa.formato | C | texto | tipo prova_de_bolsa | presencial, online | ficha | "[CONFIRMAR]" |
| prova_de_bolsa.local_texto | C | texto | tipo prova_de_bolsa | cidade do catálogo | catálogo | "[CONFIRMAR]" |
| prova_de_bolsa.nota_de_corte_texto | C | texto | tipo prova_de_bolsa | cópia literal da ficha, como "7.0 (mínimo 70 % de acerto)" | ficha | "[CONFIRMAR]" |
| prova_de_bolsa.turma_de_destino | P | objeto | tipo prova_de_bolsa | codigo ("[CONFIRMAR]" até a Ufape confirmar), sugestao_do_plano (código do catálogo ou null), natureza_da_sugestao ("[SUPOSIÇÃO]") | plano, seção 2.3; contexto/pos-graduacao.md ("A turma de destino de cada prova não aparece na página: [CONFIRMAR]") | codigo "[CONFIRMAR]", sugestao_do_plano null |
| prova_de_bolsa.bolsas_previstas | C | lista de objetos ou null | tipo prova_de_bolsa | quantidade (inteiro), percentual_texto (cópia literal, como "50% (monitoria)", "25%", "10%") | contexto/pos-graduacao.md (regras das 22 provas, P10 resolvido em 26/10/2026) e ficha | null com pendência |
| prova_de_bolsa.prazo_de_matricula_apos_resultado | C | texto | tipo prova_de_bolsa | cópia literal do contexto da linha ("10 dias úteis") | contexto/pos-graduacao.md | "[CONFIRMAR]" |
| prova_de_bolsa.divulgacao_do_resultado | C | texto | tipo prova_de_bolsa | cópia literal do contexto da linha ("WhatsApp ou e-mail") | contexto/pos-graduacao.md | "[CONFIRMAR]" |
| prova_de_bolsa.minimo_para_confirmar_turma | C | inteiro ou null | tipo prova_de_bolsa | número da página da prova (15); a divergência com os 20 das páginas de curso vira pendência | ficha e contexto/pos-graduacao.md | null com pendência |
| graduacao.edital | C | objeto | tipo graduacao | numero, titulo, url | ficha de editais; catálogo, seção 1 | "[CONFIRMAR]" em cada subcampo |
| graduacao.edital_de_desconto | C | objeto | tipo graduacao | numero, titulo, url | ficha de editais; catálogo, seção 1 | "[CONFIRMAR]" em cada subcampo |
| graduacao.ato_autorizativo | C | texto | tipo graduacao | cópia literal do catálogo | catálogo, seção 1 | "[CONFIRMAR]" |
| graduacao.reconhecimento | C | texto | tipo graduacao | cópia literal | contexto/graduacao.md ([PREENCHER COM A REGULAÇÃO]) | "[CONFIRMAR]" |
| graduacao.grau | C | texto | tipo graduacao | bacharelado, licenciatura | ficha de editais | "[CONFIRMAR]" |
| graduacao.turnos | C | lista de objetos | tipo graduacao | turno (integral, noturno), duracao_anos (inteiro ou null), vagas (inteiro ou null), mensalidade_texto (cópia literal) | catálogo e ficha de editais | null nos números com pendência; "[CONFIRMAR]" no texto |
| graduacao.formas_de_ingresso | C | lista de texto ou null | tipo graduacao | redacao, enem, transferencia_externa, diplomado, vagas_remanescentes | ficha de editais | null com pendência |
| graduacao.inscricoes_abertas_desde | C | data ou null | tipo graduacao | AAAA-MM-DD | ficha de editais | null com pendência |
| graduacao.inscricao_ate | C | data ou null | tipo graduacao | AAAA-MM-DD | edital (não traz hoje) | null com pendência |
| graduacao.inicio_das_aulas | C | data ou null | tipo graduacao | AAAA-MM-DD (igual a inicio) | ficha de editais | null com pendência |
| graduacao.validade_do_desconto | C | texto | tipo graduacao | cópia literal | ficha de editais | "[CONFIRMAR]" |
| graduacao.lp.url | C | texto | tipo graduacao | URL da LP da Graduação | catálogo ou ufape-site | "[CONFIRMAR]" |
| graduacao.lp.alterada_pela_squad | C | booleano | tipo graduacao | sempre false | regra do CLAUDE.md | não se aplica |
| graduacao.lp.utm | C | objeto | tipo graduacao | gerada_por ("plataforma"), parametros (utm_source, utm_medium, utm_campaign, utm_content, utm_term), utm_campaign. Nenhum valor que identifique pessoa | plataforma; padrão D11 e D12 do plano do cmo (seção 12.7; seção 6.3 deste arquivo) | utm_campaign "[CONFIRMAR]" |
| evento.subtipo | C | texto | tipo workshop ou simposio | workshop, simposio | contexto/eventos.md (subtipo obrigatório) | "[CONFIRMAR]" |
| evento.data_inicio | C | data ou null | tipos de evento | AAAA-MM-DD | catálogo | null com pendência |
| evento.data_fim | C | data ou null | tipos de evento | AAAA-MM-DD | página do evento | null com pendência; null (não se aplica) em evento gravado contínuo |
| evento.horario_texto | C | texto | tipos de evento | cópia literal | página do evento | "[CONFIRMAR]" |
| evento.formato | C | texto | tipos de evento | presencial, online_ao_vivo, gravado, hibrido | catálogo e página | "[CONFIRMAR]" |
| evento.modalidades | C | lista de objetos | tipos de evento | nome, preco_texto_site (literal), vagas (inteiro ou null), produto (código do catálogo, quando houver) | catálogo e página | "[CONFIRMAR]" no texto; null no número, com pendência |
| evento.carga_horaria_oficial | C | texto | tipos de evento | cópia literal | decisão da Ufape de 26/10/2026, ficha do evento | "[CONFIRMAR]" |
| evento.cupom | C | objeto ou null | tipos de evento | codigo, publico, desconto_texto, comprovacao_texto | catálogo | null (não se aplica) se não há cupom |
| evento.pagina_oficial | C | texto | tipos de evento | URL | ficha do evento | "[CONFIRMAR]" |
| evento.destino_das_campanhas_pagas | P | texto | tipos de evento | URL | decisão da Ufape de 26/10/2026 | "[CONFIRMAR]" |
| evento.palestrantes | C | objeto | tipos de evento | confirmados_na_ficha (inteiro ou null), convidados_a_definir (inteiro ou null), autorizacoes_de_imagem_registradas (inteiro ou null). Só contagens | ficha do evento | null em cada contagem com pendência; autorizações: pendência de marcador "[CONFIRMAR autorização]" |

#### Mídia, kit, canais, arquivos, números, pendências e derivados

| Campo | Cl. | Tipo | Obrig. | Valores permitidos | Origem | Se vazio |
|---|---|---|---|---|---|---|
| status_midia.campanha | M | texto | sim | ativa, pausada, sem_campanha, nao_consta | visão de campanhas | nao_consta |
| status_midia.formatos | M | lista | sim | estatico, video | visão de campanhas | lista vazia |
| status_midia.cinco_angulos | M | texto | sim | com, sem, nao_se_aplica, nao_consta | visão de campanhas | nao_consta |
| status_midia.vinculo_com_a_visao | M | texto | sim | exato (mesmo nome, data e UF), provavel ("[SUPOSIÇÃO]", a visão não tem código), nenhum | cmo | nenhum |
| status_midia.inicio_na_visao | M | data ou null | sim | AAAA-MM-DD | visão de campanhas | null (não se aplica) |
| status_midia.divergencia_de_data | M | booleano | sim | true se inicio_na_visao difere de inicio | cmo | false |
| status_midia.observacao | M | texto | não | até 240 caracteres | visão de campanhas | omitir a chave |
| status_midia.fonte e lido_em | M | texto e data | sim | caminho e AAAA-MM-DD | visão de campanhas | "[CONFIRMAR]" no texto; null com pendência na data |
| kit.template | K | texto ou null | sim | caminho de um dos 4 templates de kit; null em prova_de_bolsa e contínuo (plano, decisão A3) | plano, seção 4 | null (não se aplica) |
| kit.variacao | K | texto ou null | sim | workshop, simposio (só eventos); null nos demais | plano e template de evento | "[CONFIRMAR]" em evento |
| kit.escopo | K | texto | sim | item, grupo (campanha única ou kit sempre ligado) | plano, A3 | item |
| kit.entregas | K | lista de objetos | sim | uma por linha do template do tipo, com as quantidades mínimas intactas (1.4). Campos: chave, entrega, quantidade_minima (inteiro ou null), regra_quantidade, autorizados (inteiro ou null), responsavel (lista de agentes), prazo (data ou null), status, qa, arquivo, secao, ref_aprovacao (texto ou null) | template do tipo | prazo e quantidade: null com pendência; em escopo grupo as entregas são definidas pelo cmo e a quantidade_minima fica null com pendência |
| kit.acrescimos | K | lista de objetos | sim | mesmos campos de entregas, com quantidade (inteiro ou null) no lugar de quantidade_minima | plano do cmo | lista vazia |
| kit.inventario | K | objeto ou null | não | situacao (pendente, conferido), prazo (data ou null), responsavel. Só para itens da onda 1 com campanha ativa (plano, seção 4) | plano | omitir a chave |
| canais | K | lista de 8 objetos | sim | canal (instagram, facebook, tiktok, x, linkedin, youtube, podcast, whatsapp), estado (ativo, teste, fora), motivo, natureza (proposta_do_cmo, confirmado_em_1.20) | plano, seção 5 | não se aplica: sempre 8 |
| arquivos_por_camada | A | objeto | sim | geral, linha, area, curso: listas de objetos com agente, caminho, secao, estado (pendente_de_aprovacao, aprovado, devolvido), aprovado_em, ref_aprovacao (texto) | saídas dos agentes | listas vazias; ref_aprovacao "[CONFIRMAR]" até a plataforma informar o id |
| metas | N | objeto | sim | matriculas_alvo, cpl_maximo, custo_por_matricula_maximo, verba (número ou null), fonte (texto) | gestor-de-midia e Ufape | null em cada número, com pendência |
| numeros_agregados | N | objeto | sim | leads, inscricoes, matriculas, verba_gasta (número ou null), lido_em (data ou null). Só números somados por turma | analista-de-dados e Ufape | null em cada número, com pendência; lido_em null |
| pendencias | X | lista de objetos | sim | id, ref_plano (P1 a P18 ou seção), tipo, descricao, marcador, campos (lista de caminhos de campo que a pendência explica, aceita "[*]" para todos os itens de uma lista), bloqueia, fonte, aberta_em, resolvida_em | auditorias e plano | lista vazia |
| aprovacoes | A | lista de objetos | sim | ref (A1 a A12 do plano, ou id da plataforma), o_que, por_que, quanto, efeito_esperado, como_desfazer, status, pedido_em, decidido_em, decidido_por_papel | plano, seção 8 | lista vazia |
| historico | X | lista de objetos | sim | revisao, em, campo, de, para, motivo, origem, aplicado_por | cmo | pelo menos a linha de criação |
| resumo.pendencias_abertas | D | inteiro | sim | contagem de pendencias com resolvida_em null | calculado | 0 |
| resumo.bloqueado | D | booleano | sim | true se há pendência aberta cujo bloqueia contém "peca_final" | calculado | false |

### 1.4 Vocabulários fechados e regras de apoio

- pendencias.tipo: certificacao, link, data, turma, duplicidade, preco_ou_condicao, regra_de_bolsa, meta_ou_verba, aprovador, autorizacao, ferramenta, regulatorio, kit, conformidade, divergencia, outro.
- pendencias.marcador: "[CONFIRMAR]", "[CONFIRMAR autorização]", "[SUPOSIÇÃO]". Marcadores como "[PREENCHER COM A REGULAÇÃO]" do catálogo entram como "[CONFIRMAR]".
- pendencias.bloqueia (lista, pode ser vazia): peca_final, anuncio, pagina, preco, data, certificacao, autorizacao_docente, meta.
- aprovacoes.status: pendente, aprovado, recusado, executado_por_humano. decidido_por_papel: pessoa_do_marketing, ou o papel que a tabela de aprovação de contexto/ufape-geral.md vier a nomear. Nunca o nome da pessoa.
- entregas.status: a_fazer, inventario_pendente, aguardando_autorizacao, aguardando_aprovacao, aprovado, devolvido, revisar_por_mudanca, nao_aplicavel. "aprovado" só com qa "aprovado" e aprovação humana registrada (ref_aprovacao).
- entregas.qa: pendente, aprovado, corrigir (veredito do qa-de-marketing).
- entregas.regra_quantidade: null, 1_por_docente_autorizado, 1_por_palestrante_autorizado. Nessas duas, quantidade_minima é null e autorizados guarda a contagem apurada ou null com pendência de marcador "[CONFIRMAR autorização]". O template diz "1 por docente da ficha" e "1 por palestrante da ficha"; o plano (P13) restringe a quem tem autorização registrada, e quem não tem não conta como entrega faltante. Isso não diminui o mínimo: é a regra do plano.
- Chaves de entrega por template (a quantidade mínima é a do template e nunca diminui):
  - kit-de-lancamento-pos: pagina (1), plano_8_canais (1), plano_de_midia (1), posts_organicos (6), criativos (3), post_por_docente (1 por docente autorizado), whatsapp (4), email (2), roteiro_video (1).
  - kit-de-lancamento-livres: pagina (1), plano_8_canais (1), posts_organicos (4), criativos (2), whatsapp (3), email (1).
  - kit-de-lancamento-evento, variação workshop: pagina (1), posts_organicos (3), criativos (2), mensagem_convite (1), mensagem_vespera (1), mensagem_do_dia (1), email_convite (1).
  - kit-de-lancamento-evento, variação simpósio: pagina (1), plano_8_canais (1), plano_de_midia (1), post_por_palestrante (1 por palestrante autorizado), posts_organicos (4), criativos (3), email_convite (1), email_lembrete (1), email_programacao (1), mensagem_vespera (1), mensagem_do_dia (1).
  - kit-de-lancamento-graduacao (sem página; a LP nunca é alterada): plano_8_canais (1), plano_de_midia (1), posts_organicos (6), criativos_com_utm (4), whatsapp_prazos_do_edital (5), email_prazos_do_edital (3), roteiro_video (2).
  - Provas de bolsa e contínuos (sem template): entregas definidas pelo cmo na campanha única ou no kit sempre ligado, com chaves livres em letras minúsculas e sublinhado.
- modalidade_normalizada, equivalências: "Presencial" é presencial; "PROVA PRESENCIAL" é online, porque as provas de bolsa são online (decisão 11 da Ufape, 26/10/2026) e a página é que está desatualizada; "Semipresencial", "Semi-presencial", "Semi presencial" e "Semiprensecial" são semipresencial; "Ead" é ead; "Online" e "On-line" são online; "Gravação" é gravacao; "Presencial e Online" ou outra mistura sem regra: "[CONFIRMAR]".
- area.codigo e nomes: A1 Anestesiologia e dor; A2 Cardiorrespiratório; A3 Emergência, terapia intensiva e clínica médica; A4 Cirurgia, ortopedia e reabilitação; A5 Diagnóstico por imagem e endoscopia; A6 Gastroenterologia; A7 Endocrinologia e nefrologia; A8 Dermatologia; A9 Oftalmologia; A10 Oncologia; A11 Laboratório; A12 Neurologia; A13 Medicina felina; A14 Outras especialidades (plano, seção 2.3).
- Evolução do esquema: campo novo opcional não muda a versão; remover, renomear, mudar tipo ou valor permitido exige versao_schema 2 e um novo documento de fluxo. Os arquivos da versão 1 continuam válidos.

### 1.5 Modelo em branco (versão 1)

Os textos entre "<" e ">" ou separados por " | " são instruções, não valores. O modelo mostra todas as chaves; do bloco por tipo, só um existe em cada arquivo (R3).

```json
{
  "versao_schema": 1,
  "id": "<linha>-<codigo ou slug>",
  "revisao": 1,
  "revisao_aprovada": 0,
  "estado_do_arquivo": "ativo | substituido",
  "substituido_por": null,
  "gerado_em": "AAAA-MM-DD",
  "atualizado_em": "AAAA-MM-DD",
  "fontes": {
    "catalogo": "contexto/catalogo-de-cursos.md",
    "data_catalogo": "AAAA-MM-DD | null",
    "catalogo_linha_literal": "<colunas da linha até Fonte> | [CONFIRMAR]",
    "ficha": "contexto/cursos/<pasta>/<arquivo>.md | null",
    "ficha_editais": "só na graduacao",
    "ficha_lida_em": "AAAA-MM-DD | null",
    "contexto_da_linha": "contexto/<linha>.md (opcional)",
    "campos_so_na_ficha": [],
    "visao_de_campanhas": { "arquivo": "docs/visao-de-campanhas-AAAA-MM-DD.md", "data": "AAAA-MM-DD" },
    "plano": "saidas/02-estrategia-e-posicionamento/cmo-geral-AAAA-MM-DD.md",
    "auditorias": []
  },
  "codigo": "<digitos do catalogo | sem-codigo>",
  "linha": "pos | livres | eventos | graduacao",
  "linha_origem": "catalogo | plano",
  "tipo": "pos | prova_de_bolsa | livre_presencial | livre_online | minicurso | grupo_de_estudos | espanhol | aprimoramento | workshop | simposio | graduacao",
  "nome_no_site": "<literal>",
  "nome_padrao": "<regra de 1.3>",
  "slug_sugerido": "<regra de 1.3 | [CONFIRMAR]>",
  "aliases": [],
  "pagina_oficial": "<URL | [CONFIRMAR] | null>",
  "area": { "codigo": "A1 a A14 | sem_area | nao_se_aplica", "nome": "<nome>", "natureza": "plano_do_cmo | proposta" },
  "recorte": "planejar | historico | pendencia",
  "motivo_do_recorte": "<ate 240 caracteres>",
  "onda": "1 | 2 | 3 | null",
  "modo_de_venda": "com_data | continuo",
  "grupo_de_campanha": null,
  "gut": { "g": 0, "u": 0, "t": 0, "total": 0, "motivo": "<texto>", "natureza": "avaliacao_do_agente", "fonte": "<caminho e seção>" },
  "relacionados": [ { "id": "<id de outro arquivo>", "relacao": "duplicidade_provavel | modalidade_do_mesmo_evento | turma_de_destino | substitui", "natureza": "dado | [SUPOSIÇÃO]" } ],
  "local": "<literal>",
  "modalidade": "<literal>",
  "modalidade_normalizada": "presencial | semipresencial | ead | online | gravacao | [CONFIRMAR]",
  "turma": "<romano | [CONFIRMAR] | null>",
  "carga_horaria": "<literal | [CONFIRMAR] | null>",
  "modulos": "<inteiro | null>",
  "inicio": "AAAA-MM-DD | null",
  "fonte_da_data": "planilha | site | edital | pagina_do_evento | ausente",
  "dias_ate_inicio": null,
  "fim_das_inscricoes": "AAAA-MM-DD | null",
  "preco_texto_site": "<literal | [CONFIRMAR]>",
  "preco_estruturado": { "moeda": "BRL", "parcelas": 0, "valor_parcela": 0.0, "total": 0.0, "matricula": null },
  "condicoes_especiais": [ { "tipo": "cupom | promocao | desconto | outro", "texto": "<literal>", "codigo": "<só cupom>", "publico": "<texto>", "validade": "AAAA-MM-DD | null" } ],
  "status_catalogo": "aberto | aberto (contínuo) | verificar | sem venda | encerrado | sem página",
  "status_catalogo_texto": "<literal>",
  "vagas": { "turma_minima": "<inteiro | null>", "vagas_ofertadas": "<inteiro | null>", "vagas_restantes": null },
  "equipe": { "coordenadores_na_ficha": "<inteiro | null>", "docentes_na_ficha": "<inteiro | null>", "autorizacoes_de_imagem_registradas": "<inteiro | null>" },
  "prova_de_bolsa": { "...": "só tipo prova_de_bolsa; campos em 1.3" },
  "graduacao": { "...": "só tipo graduacao; campos em 1.3" },
  "evento": { "...": "só tipos workshop e simposio; campos em 1.3" },
  "status_midia": {
    "campanha": "ativa | pausada | sem_campanha | nao_consta",
    "formatos": [],
    "cinco_angulos": "com | sem | nao_se_aplica | nao_consta",
    "vinculo_com_a_visao": "exato | provavel | nenhum",
    "inicio_na_visao": null,
    "divergencia_de_data": false,
    "fonte": "docs/visao-de-campanhas-AAAA-MM-DD.md",
    "lido_em": "AAAA-MM-DD"
  },
  "kit": {
    "template": "templates/kit-de-lancamento-<tipo>.md | null",
    "variacao": null,
    "escopo": "item | grupo",
    "entregas": [
      {
        "chave": "<chave de 1.4>",
        "entrega": "<texto do template>",
        "quantidade_minima": "<inteiro | null>",
        "regra_quantidade": null,
        "autorizados": null,
        "responsavel": [],
        "prazo": "AAAA-MM-DD | null",
        "status": "a_fazer",
        "qa": "pendente",
        "arquivo": null,
        "secao": null,
        "ref_aprovacao": null
      }
    ],
    "acrescimos": [],
    "inventario": { "situacao": "pendente | conferido", "prazo": "AAAA-MM-DD | null", "responsavel": "cmo" }
  },
  "canais": [ { "canal": "instagram", "estado": "ativo | teste | fora", "motivo": "<texto>", "natureza": "proposta_do_cmo | confirmado_em_1.20" } ],
  "arquivos_por_camada": { "geral": [], "linha": [], "area": [], "curso": [] },
  "metas": { "matriculas_alvo": null, "cpl_maximo": null, "custo_por_matricula_maximo": null, "verba": null, "fonte": "gestor-de-midia e Ufape" },
  "numeros_agregados": { "leads": null, "inscricoes": null, "matriculas": null, "verba_gasta": null, "lido_em": null },
  "pendencias": [ { "id": "<codigo>-p01", "ref_plano": "P1", "tipo": "certificacao", "descricao": "<ate 240 caracteres>", "marcador": "[CONFIRMAR]", "campos": ["<caminho do campo>"], "bloqueia": ["peca_final"], "fonte": "<caminho>", "aberta_em": "AAAA-MM-DD", "resolvida_em": null } ],
  "aprovacoes": [ { "ref": "A7", "o_que": "<texto>", "por_que": "<texto>", "quanto": "<texto>", "efeito_esperado": "<texto>", "como_desfazer": "<texto>", "status": "pendente", "pedido_em": "AAAA-MM-DD", "decidido_em": null, "decidido_por_papel": null } ],
  "historico": [ { "revisao": 1, "em": "AAAA-MM-DD", "campo": "(arquivo)", "de": null, "para": "criado", "motivo": "<texto>", "origem": "<caminho>", "aplicado_por": "cmo" } ],
  "resumo": { "pendencias_abertas": 0, "bloqueado": false }
}
```

### 1.6 Exemplo completo 1: Pós 707 (arquivo pos-707.json)

Os dados vêm de contexto/catalogo-de-cursos.md (linha 707), da ficha contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md, da visão de campanhas e do plano do cmo. Este exemplo ilustra a especificação; o arquivo real nasce na etapa M.3 e passa pelo qa-de-marketing. Nenhum nome de docente ou coordenador aparece: a ficha lista 3 coordenadores e 19 professores, e o JSON guarda só as contagens. Este exemplo passa na conferência C11: todo campo com "[CONFIRMAR]" ou null por origem vazia é citado em "campos" de uma pendência (fim_das_inscricoes, vagas.vagas_ofertadas, vagas.vagas_restantes, equipe.autorizacoes_de_imagem_registradas, kit.entregas[*].autorizados, kit.entregas[*].prazo, kit.acrescimos[*].quantidade e prazo, kit.inventario, metas.*, numeros_agregados.*, arquivos_por_camada.geral[0].ref_aprovacao e os canais com suposição).

```json
{
  "versao_schema": 1,
  "id": "pos-707",
  "revisao": 1,
  "revisao_aprovada": 0,
  "estado_do_arquivo": "ativo",
  "substituido_por": null,
  "gerado_em": "2026-10-26",
  "atualizado_em": "2026-10-26",
  "fontes": {
    "catalogo": "contexto/catalogo-de-cursos.md",
    "data_catalogo": "2026-10-26",
    "catalogo_linha_literal": "| 707 | Pós-graduação em Oftalmologia Veterinária | São Paulo | Semipresencial | 30/10/2026 | VII | 600 h | 30x de R$ 1.590,00; R$ 47.700,00 no cartão ou boleto; matrícula R$ 250,00 | aberto | planilha e site |",
    "ficha": "contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md",
    "ficha_lida_em": "2026-10-26",
    "campos_so_na_ficha": ["modulos", "vagas.turma_minima", "equipe.coordenadores_na_ficha", "equipe.docentes_na_ficha", "pagina_oficial"],
    "visao_de_campanhas": { "arquivo": "docs/visao-de-campanhas-2026-10-26.md", "data": "2026-10-26" },
    "plano": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md",
    "auditorias": ["docs/auditoria-do-catalogo-2026-10-22.md", "docs/auditoria-do-catalogo-2026-10-26.md"]
  },
  "codigo": "707",
  "linha": "pos",
  "linha_origem": "catalogo",
  "tipo": "pos",
  "nome_no_site": "Pós-graduação em Oftalmologia Veterinária",
  "nome_padrao": "Pós-graduação em Oftalmologia Veterinária",
  "slug_sugerido": "pos-graduacao-em-oftalmologia-veterinaria",
  "aliases": [],
  "pagina_oficial": "https://faculdade.ufape.com.br/produto/707/pos-graduacao-em-oftalmologia-veterinaria",
  "area": { "codigo": "A9", "nome": "Oftalmologia", "natureza": "plano_do_cmo" },
  "recorte": "planejar",
  "motivo_do_recorte": "Turma aberta com início a partir de 26/10/2026 (plano, seção 2.2).",
  "onda": 1,
  "modo_de_venda": "com_data",
  "grupo_de_campanha": null,
  "gut": { "g": 4, "u": 5, "t": 3, "total": 60, "motivo": "Faltam 4 dias; campanha ativa; reta final e encerramento.", "natureza": "avaliacao_do_agente", "fonte": "plano, seção 3" },
  "relacionados": [],
  "local": "São Paulo",
  "modalidade": "Semipresencial",
  "modalidade_normalizada": "semipresencial",
  "turma": "VII",
  "carga_horaria": "600 h",
  "modulos": 24,
  "inicio": "2026-10-30",
  "fonte_da_data": "planilha",
  "dias_ate_inicio": 4,
  "fim_das_inscricoes": null,
  "preco_texto_site": "30x de R$ 1.590,00; R$ 47.700,00 no cartão ou boleto; matrícula R$ 250,00",
  "preco_estruturado": { "moeda": "BRL", "parcelas": 30, "valor_parcela": 1590.00, "total": 47700.00, "matricula": 250.00 },
  "condicoes_especiais": [],
  "status_catalogo": "aberto",
  "status_catalogo_texto": "aberto",
  "vagas": { "turma_minima": 15, "vagas_ofertadas": null, "vagas_restantes": null },
  "equipe": { "coordenadores_na_ficha": 3, "docentes_na_ficha": 19, "autorizacoes_de_imagem_registradas": null },
  "status_midia": {
    "campanha": "ativa",
    "formatos": ["estatico"],
    "cinco_angulos": "sem",
    "vinculo_com_a_visao": "exato",
    "inicio_na_visao": "2026-10-30",
    "divergencia_de_data": false,
    "fonte": "docs/visao-de-campanhas-2026-10-26.md",
    "lido_em": "2026-10-26"
  },
  "kit": {
    "template": "templates/kit-de-lancamento-pos.md",
    "variacao": null,
    "escopo": "item",
    "entregas": [
      { "chave": "pagina", "entrega": "Página da turma (workflow /pagina-de-curso, template pagina-da-turma.md)", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["landing-page", "seo-on-page"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "plano_8_canais", "entrega": "Plano dos 8 canais", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["cmo"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "plano_de_midia", "entrega": "Plano de mídia (workflow /plano-de-midia-da-turma)", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["gestor-de-midia"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "posts_organicos", "entrega": "Posts orgânicos", "quantidade_minima": 6, "regra_quantidade": null, "autorizados": null, "responsavel": ["posts-sociais"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "criativos", "entrega": "Criativos de anúncio", "quantidade_minima": 3, "regra_quantidade": null, "autorizados": null, "responsavel": ["criativos-de-anuncio"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "post_por_docente", "entrega": "Post por docente (só com autorização registrada)", "quantidade_minima": null, "regra_quantidade": "1_por_docente_autorizado", "autorizados": null, "responsavel": ["autoridade-docente"], "prazo": null, "status": "aguardando_autorizacao", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "whatsapp", "entrega": "Mensagens de WhatsApp de nutrição", "quantidade_minima": 4, "regra_quantidade": null, "autorizados": null, "responsavel": ["copy-de-mensagens"], "prazo": "2026-10-28", "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "email", "entrega": "E-mails de nutrição", "quantidade_minima": 2, "regra_quantidade": null, "autorizados": null, "responsavel": ["copy-de-mensagens"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "roteiro_video", "entrega": "Roteiro de vídeo curto", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["tiktok"], "prazo": null, "status": "inventario_pendente", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null }
    ],
    "acrescimos": [
      { "chave": "inventario_do_kit", "entrega": "Inventário do que já existe do kit, conferido item por item", "quantidade": 1, "responsavel": ["cmo"], "prazo": "2026-10-28", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "whatsapp_reta_final", "entrega": "Mensagens de reta final, sem urgência por vagas, porque não há número de vagas", "quantidade": null, "responsavel": ["copy-de-mensagens"], "prazo": "2026-10-28", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "pausa_e_relatorio_final", "entrega": "Pedido de pausa das campanhas e relatório final", "quantidade": 2, "responsavel": ["cmo", "gestor-de-midia"], "prazo": null, "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null }
    ],
    "inventario": { "situacao": "pendente", "prazo": "2026-10-28", "responsavel": "cmo" }
  },
  "canais": [
    { "canal": "instagram", "estado": "ativo", "motivo": "Canal em uso; feed, Reels e anúncios Meta.", "natureza": "proposta_do_cmo" },
    { "canal": "facebook", "estado": "ativo", "motivo": "Inventário de mídia Meta; orgânico só reaproveitado do Instagram.", "natureza": "proposta_do_cmo" },
    { "canal": "tiktok", "estado": "fora", "motivo": "Sem perfil citado e produção não comprovada; o roteiro do kit serve a Reels e Shorts.", "natureza": "proposta_do_cmo" },
    { "canal": "x", "estado": "fora", "motivo": "Sem perfil e sem sinal de público veterinário ativo [SUPOSIÇÃO].", "natureza": "proposta_do_cmo" },
    { "canal": "linkedin", "estado": "teste", "motivo": "Teste na onda 3, com foco em Pós; depende de verba e de docente autorizado.", "natureza": "proposta_do_cmo" },
    { "canal": "youtube", "estado": "ativo", "motivo": "Ativo leve: Shorts com o roteiro do kit.", "natureza": "proposta_do_cmo" },
    { "canal": "podcast", "estado": "fora", "motivo": "Pede produção recorrente com docentes; candidato a teste em 2027.", "natureza": "proposta_do_cmo" },
    { "canal": "whatsapp", "estado": "ativo", "motivo": "Canal principal de vendas; textos para o CRM enviar, só com opt-in.", "natureza": "proposta_do_cmo" }
  ],
  "arquivos_por_camada": {
    "geral": [ { "agente": "cmo", "caminho": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md", "secao": null, "estado": "aprovado", "aprovado_em": "2026-10-26", "ref_aprovacao": "[CONFIRMAR]" } ],
    "linha": [],
    "area": [],
    "curso": []
  },
  "metas": { "matriculas_alvo": null, "cpl_maximo": null, "custo_por_matricula_maximo": null, "verba": null, "fonte": "gestor-de-midia e Ufape" },
  "numeros_agregados": { "leads": null, "inscricoes": null, "matriculas": null, "verba_gasta": null, "lido_em": null },
  "pendencias": [
    { "id": "707-p01", "ref_plano": "P1", "tipo": "certificacao", "descricao": "Texto oficial de certificação ainda não aprovado pela regulação; as peças saem sem afirmação de certificação.", "marcador": "[CONFIRMAR]", "campos": [], "bloqueia": ["peca_final", "certificacao"], "fonte": "contexto/catalogo-de-cursos.md, seção Como usar", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p02", "ref_plano": "P2", "tipo": "certificacao", "descricao": "A página oficial tem bloco de certificação. Conferir se traz a frase de certificação que a squad não repete (auditoria de 26/10, seção 9) antes de anúncio que leve a ela.", "marcador": "[CONFIRMAR]", "campos": ["pagina_oficial"], "bloqueia": ["anuncio"], "fonte": "docs/auditoria-do-catalogo-2026-10-26.md, seção 9", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p03", "ref_plano": "P11", "tipo": "meta_ou_verba", "descricao": "Sem metas, verba, vagas ofertadas, vagas restantes e números agregados por turma. Nenhuma peça diz últimas vagas.", "marcador": "[CONFIRMAR]", "campos": ["vagas.vagas_ofertadas", "vagas.vagas_restantes", "metas.matriculas_alvo", "metas.cpl_maximo", "metas.custo_por_matricula_maximo", "metas.verba", "numeros_agregados.leads", "numeros_agregados.inscricoes", "numeros_agregados.matriculas", "numeros_agregados.verba_gasta"], "bloqueia": ["meta"], "fonte": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 7", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p04", "ref_plano": "P12", "tipo": "aprovador", "descricao": "Tabela de quem aprova cada tipo de peça está vazia, e o id de aprovação da plataforma ainda não foi informado; a aprovação vai à pessoa do marketing que fez o pedido.", "marcador": "[CONFIRMAR]", "campos": ["arquivos_por_camada.geral[0].ref_aprovacao"], "bloqueia": [], "fonte": "contexto/ufape-geral.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p05", "ref_plano": "P13", "tipo": "autorizacao", "descricao": "Autorização de imagem e citação de todos os docentes registrada pela Ufape em 26/10/2026 (decisões 8 e 10); post por docente liberado. Falta o cmo lançar as contagens.", "marcador": "[CONFIRMAR]", "campos": ["equipe.autorizacoes_de_imagem_registradas", "kit.entregas[5].autorizados"], "bloqueia": [], "fonte": "docs/execucao-2026-10-26.md, decisões 8 e 10", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p06", "ref_plano": "seção 4, situação especial da onda 1", "tipo": "kit", "descricao": "Inventário do que já existe do kit pendente com a Ufape; sem ele os prazos das entregas e a quantidade das mensagens de reta final ficam em aberto.", "marcador": "[CONFIRMAR]", "campos": ["kit.inventario", "kit.entregas[*].prazo", "kit.acrescimos[*].prazo", "kit.acrescimos[1].quantidade"], "bloqueia": [], "fonte": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 4", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p07", "ref_plano": "seção 10", "tipo": "data", "descricao": "Fim das inscrições não consta no catálogo nem na ficha; sem ele o pedido de pausa fica sem data.", "marcador": "[CONFIRMAR]", "campos": ["fim_das_inscricoes"], "bloqueia": [], "fonte": "contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "707-p08", "ref_plano": "seção 5", "tipo": "outro", "descricao": "Estado dos 8 canais é proposta do cmo, a confirmar nas etapas 1.20 e 1.11.", "marcador": "[SUPOSIÇÃO]", "campos": ["canais[*]"], "bloqueia": [], "fonte": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 5", "aberta_em": "2026-10-26", "resolvida_em": null }
  ],
  "aprovacoes": [
    { "ref": "A1", "o_que": "Aprovar o recorte de 110 itens, as 14 áreas e as 3 ondas", "por_que": "Define o que a squad planeja e em que ordem.", "quanto": "Sem custo de mídia.", "efeito_esperado": "A squad foca nos 35 itens da onda 1.", "como_desfazer": "Refazer o recorte em nova versão do plano.", "status": "aprovado", "pedido_em": "2026-10-26", "decidido_em": "2026-10-26", "decidido_por_papel": "pessoa_do_marketing" },
    { "ref": "A7", "o_que": "Pedir à regulação o texto oficial de certificação e a troca da frase de certificação que a squad não repete nas 46 páginas", "por_que": "Risco de propaganda enganosa (auditoria de 22/10, item 2.1).", "quanto": "Sem custo de mídia.", "efeito_esperado": "Libera a seção de certificação nas peças.", "como_desfazer": "Não se aplica.", "status": "pendente", "pedido_em": "2026-10-26", "decidido_em": null, "decidido_por_papel": null },
    { "ref": "A8", "o_que": "Enviar metas e verba por linha e os números agregados por turma; o gestor-de-midia devolve as metas de custo em três cenários", "por_que": "Sem isso não há meta nem como checar se a conta fecha.", "quanto": "Verba: a confirmar com a Ufape.", "efeito_esperado": "Metas escritas antes de subir qualquer campanha.", "como_desfazer": "Metas revisadas na segunda-feira seguinte.", "status": "pendente", "pedido_em": "2026-10-26", "decidido_em": null, "decidido_por_papel": null },
    { "ref": "A9", "o_que": "Nomear quem aprova posts, anúncios e verba, mensagens em massa, páginas e preços, e peças com certificação", "por_que": "Tabela de aprovação vazia.", "quanto": "Sem custo.", "efeito_esperado": "Aprovação sem gargalo.", "como_desfazer": "Trocar o responsável na tabela.", "status": "pendente", "pedido_em": "2026-10-26", "decidido_em": null, "decidido_por_papel": null }
  ],
  "historico": [
    { "revisao": 1, "em": "2026-10-26", "campo": "(arquivo)", "de": null, "para": "criado", "motivo": "Criação a partir do catálogo de 26/10/2026, da ficha, da visão de campanhas e do plano do cmo.", "origem": "contexto/catalogo-de-cursos.md", "aplicado_por": "cmo" }
  ],
  "resumo": { "pendencias_abertas": 8, "bloqueado": true }
}
```

### 1.7 Exemplo completo 2: prova de bolsa 68651 (arquivo pos-68651.json)

Dados de contexto/catalogo-de-cursos.md (seção 3, linha 68651, agora com coluna de preço), da ficha contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md e de contexto/pos-graduacao.md (regras das 22 provas, publicadas em 26/10/2026). Decisões de preenchimento:
- A pendência P10 do plano está resolvida: as bolsas (2 de 50% (monitoria), 4 de 25% e 5 de 10%), a nota de corte e o prazo de matrícula são copiados. O que segue aberto é a turma de destino de cada prova, que a página da prova não traz.
- O mínimo de 15 alunos é copiado da página da prova (a ficha o repete sem contradição). Ele diverge dos 20 das páginas de curso: a divergência vira pendência. O resultado sai por WhatsApp ou e-mail (contexto da linha); o trecho REGRAS da ficha cita o site e 7 dias de prazo, e isso também vira pendência.
- A carga horária da ficha (500 h) é da Pós, não da prova: carga_horaria é null (não se aplica).
- O texto da página traz uma afirmação de certificação não aprovada, um superlativo e dados clínicos com fonte: nada disso é copiado.
- As cópias da ficha são literais ("PROVA PRESENCIAL", "7.0 (mínimo 70 % de acerto)"). Pela decisão 11 da Ufape, a prova é online: modalidade_normalizada e prova_de_bolsa.formato ficam "online", e o texto da página vira a pendência 68651-p10. O preço vem do catálogo, que agora tem a coluna de preço.
- Este exemplo passa na conferência C11: todo "[CONFIRMAR]" e todo null por origem vazia (slug_sugerido, fim_das_inscricoes, vagas, kit, metas, números, ref_aprovacao, turma de destino e a sugestão) é citado em "campos" de uma pendência.

```json
{
  "versao_schema": 1,
  "id": "pos-68651",
  "revisao": 1,
  "revisao_aprovada": 0,
  "estado_do_arquivo": "ativo",
  "substituido_por": null,
  "gerado_em": "2026-10-26",
  "atualizado_em": "2026-10-26",
  "fontes": {
    "catalogo": "contexto/catalogo-de-cursos.md",
    "data_catalogo": "2026-10-26",
    "catalogo_linha_literal": "| 68651 | Prova de Bolsa de Estudos para Hematologia Veterinária | São Paulo | 27/11/2026 | R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão | aberto |",
    "ficha": "contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md",
    "ficha_lida_em": "2026-10-26",
    "contexto_da_linha": "contexto/pos-graduacao.md",
    "campos_so_na_ficha": ["modalidade", "fonte_da_data", "pagina_oficial", "prova_de_bolsa.horario_texto", "prova_de_bolsa.formato", "prova_de_bolsa.nota_de_corte_texto", "prova_de_bolsa.bolsas_previstas", "prova_de_bolsa.prazo_de_matricula_apos_resultado", "prova_de_bolsa.divulgacao_do_resultado", "prova_de_bolsa.minimo_para_confirmar_turma"],
    "visao_de_campanhas": { "arquivo": "docs/visao-de-campanhas-2026-10-26.md", "data": "2026-10-26" },
    "plano": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md",
    "auditorias": ["docs/auditoria-do-catalogo-2026-10-22.md", "docs/auditoria-do-catalogo-2026-10-26.md"]
  },
  "codigo": "68651",
  "linha": "pos",
  "linha_origem": "catalogo",
  "tipo": "prova_de_bolsa",
  "nome_no_site": "Prova de Bolsa de Estudos para Hematologia Veterinária",
  "nome_padrao": "Prova de Bolsa de Estudos para Hematologia Veterinária",
  "slug_sugerido": "[CONFIRMAR]",
  "aliases": [],
  "pagina_oficial": "https://faculdade.ufape.com.br/produto/68651/prova-de-bolsa-de-estudos-para-hematologia-veterinaria/sao-paulo",
  "area": { "codigo": "A11", "nome": "Laboratório (hematologia, patologia clínica, citopatologia)", "natureza": "plano_do_cmo" },
  "recorte": "planejar",
  "motivo_do_recorte": "Prova de bolsa aberta de 27/11/2026, tratada em campanha única (decisão A3).",
  "onda": 1,
  "modo_de_venda": "com_data",
  "grupo_de_campanha": "provas-de-bolsa-2026-11-27",
  "gut": { "g": 5, "u": 5, "t": 4, "total": 100, "motivo": "Porta de entrada da Pós; faltam 32 dias; não consta na visão de campanhas.", "natureza": "avaliacao_do_agente", "fonte": "plano, seção 3" },
  "relacionados": [ { "id": "pos-68608", "relacao": "turma_de_destino", "natureza": "[SUPOSIÇÃO]" } ],
  "local": "São Paulo",
  "modalidade": "PROVA PRESENCIAL",
  "modalidade_normalizada": "online",
  "turma": null,
  "carga_horaria": null,
  "modulos": null,
  "inicio": "2026-11-27",
  "fonte_da_data": "planilha",
  "dias_ate_inicio": 32,
  "fim_das_inscricoes": null,
  "preco_texto_site": "R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão",
  "preco_estruturado": { "moeda": "BRL", "parcelas": 1, "valor_parcela": 100.00, "total": 100.00, "matricula": null },
  "condicoes_especiais": [],
  "status_catalogo": "aberto",
  "status_catalogo_texto": "aberto",
  "vagas": { "turma_minima": null, "vagas_ofertadas": null, "vagas_restantes": null },
  "equipe": null,
  "prova_de_bolsa": {
    "data_da_prova": "2026-11-27",
    "horario_texto": "9 às 13h",
    "formato": "online",
    "local_texto": "São Paulo",
    "nota_de_corte_texto": "7.0 (mínimo 70 % de acerto)",
    "turma_de_destino": { "codigo": "[CONFIRMAR]", "sugestao_do_plano": "68608", "natureza_da_sugestao": "[SUPOSIÇÃO]" },
    "bolsas_previstas": [
      { "quantidade": 2, "percentual_texto": "50% (monitoria)" },
      { "quantidade": 4, "percentual_texto": "25%" },
      { "quantidade": 5, "percentual_texto": "10%" }
    ],
    "prazo_de_matricula_apos_resultado": "10 dias úteis",
    "divulgacao_do_resultado": "WhatsApp ou e-mail",
    "minimo_para_confirmar_turma": 15
  },
  "status_midia": {
    "campanha": "nao_consta",
    "formatos": [],
    "cinco_angulos": "nao_consta",
    "vinculo_com_a_visao": "nenhum",
    "inicio_na_visao": null,
    "divergencia_de_data": false,
    "observacao": "As provas de bolsa não aparecem na visão de campanhas de 26/10/2026.",
    "fonte": "docs/visao-de-campanhas-2026-10-26.md",
    "lido_em": "2026-10-26"
  },
  "kit": {
    "template": null,
    "variacao": null,
    "escopo": "grupo",
    "entregas": [
      { "chave": "campanha_unica", "entrega": "Plano da campanha única das provas de bolsa, com variação por especialidade", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["estrategia-de-campanha"], "prazo": "2026-10-29", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "oferta_e_regras_da_bolsa", "entrega": "Oferta com as regras da bolsa", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["estrategia-de-oferta"], "prazo": null, "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "plano_de_midia", "entrega": "Plano de mídia da campanha", "quantidade_minima": 1, "regra_quantidade": null, "autorizados": null, "responsavel": ["gestor-de-midia"], "prazo": null, "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "criativos", "entrega": "Criativos de anúncio", "quantidade_minima": null, "regra_quantidade": null, "autorizados": null, "responsavel": ["criativos-de-anuncio"], "prazo": "2026-11-03", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "posts_organicos", "entrega": "Posts orgânicos", "quantidade_minima": null, "regra_quantidade": null, "autorizados": null, "responsavel": ["posts-sociais"], "prazo": "2026-11-03", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null },
      { "chave": "mensagens", "entrega": "Mensagens de WhatsApp e e-mail", "quantidade_minima": null, "regra_quantidade": null, "autorizados": null, "responsavel": ["copy-de-mensagens"], "prazo": "2026-11-03", "status": "a_fazer", "qa": "pendente", "arquivo": null, "secao": null, "ref_aprovacao": null }
    ],
    "acrescimos": []
  },
  "canais": [
    { "canal": "instagram", "estado": "ativo", "motivo": "Canal em uso; feed, Reels e anúncios Meta.", "natureza": "proposta_do_cmo" },
    { "canal": "facebook", "estado": "ativo", "motivo": "Inventário de mídia Meta; orgânico só reaproveitado do Instagram.", "natureza": "proposta_do_cmo" },
    { "canal": "tiktok", "estado": "fora", "motivo": "Sem perfil citado e produção não comprovada.", "natureza": "proposta_do_cmo" },
    { "canal": "x", "estado": "fora", "motivo": "Sem perfil e sem sinal de público veterinário ativo [SUPOSIÇÃO].", "natureza": "proposta_do_cmo" },
    { "canal": "linkedin", "estado": "teste", "motivo": "Teste na onda 3, com foco em Pós; depende de verba e de docente autorizado.", "natureza": "proposta_do_cmo" },
    { "canal": "youtube", "estado": "ativo", "motivo": "Ativo leve: Shorts reaproveitando roteiro.", "natureza": "proposta_do_cmo" },
    { "canal": "podcast", "estado": "fora", "motivo": "Pede produção recorrente com docentes; candidato a teste em 2027.", "natureza": "proposta_do_cmo" },
    { "canal": "whatsapp", "estado": "ativo", "motivo": "Canal principal de vendas; textos para o CRM enviar, só com opt-in.", "natureza": "proposta_do_cmo" }
  ],
  "arquivos_por_camada": {
    "geral": [ { "agente": "cmo", "caminho": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md", "secao": null, "estado": "aprovado", "aprovado_em": "2026-10-26", "ref_aprovacao": "[CONFIRMAR]" } ],
    "linha": [],
    "area": [],
    "curso": []
  },
  "metas": { "matriculas_alvo": null, "cpl_maximo": null, "custo_por_matricula_maximo": null, "verba": null, "fonte": "gestor-de-midia e Ufape" },
  "numeros_agregados": { "leads": null, "inscricoes": null, "matriculas": null, "verba_gasta": null, "lido_em": null },
  "pendencias": [
    { "id": "68651-p01", "ref_plano": "P1", "tipo": "certificacao", "descricao": "Texto oficial de certificação ainda não aprovado pela regulação; as peças saem sem afirmação de certificação.", "marcador": "[CONFIRMAR]", "campos": [], "bloqueia": ["peca_final", "certificacao"], "fonte": "contexto/catalogo-de-cursos.md, seção Como usar", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p02", "ref_plano": "seção 2.3", "tipo": "turma", "descricao": "A página da prova não traz a turma de destino da bolsa. O contexto da linha marca como a confirmar.", "marcador": "[CONFIRMAR]", "campos": ["prova_de_bolsa.turma_de_destino.codigo"], "bloqueia": ["peca_final"], "fonte": "contexto/pos-graduacao.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p03", "ref_plano": "U1 do plano do cmo", "tipo": "divergencia", "descricao": "Turma mínima fechada em 15, também na Pós (decisão 11). Segue aberto: o trecho REGRAS da ficha cita o site como local do resultado e 7 dias para a matrícula, contra 10 dias no topo.", "marcador": "[CONFIRMAR]", "campos": ["prova_de_bolsa.prazo_de_matricula_apos_resultado", "prova_de_bolsa.divulgacao_do_resultado"], "bloqueia": ["peca_final"], "fonte": "contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md; docs/execucao-2026-10-26.md, decisão 11", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p04", "ref_plano": "P2", "tipo": "conformidade", "descricao": "O texto da página oficial traz afirmação de certificação não aprovada, um superlativo e dados clínicos com fonte. Nada disso é repetido; anúncio que leve à página é sinalizado.", "marcador": "[CONFIRMAR]", "campos": ["pagina_oficial"], "bloqueia": ["anuncio"], "fonte": "contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p05", "ref_plano": "P11", "tipo": "meta_ou_verba", "descricao": "Sem metas, verba, vagas e número de inscritos na prova.", "marcador": "[CONFIRMAR]", "campos": ["vagas.vagas_ofertadas", "vagas.vagas_restantes", "metas.matriculas_alvo", "metas.cpl_maximo", "metas.custo_por_matricula_maximo", "metas.verba", "numeros_agregados.leads", "numeros_agregados.inscricoes", "numeros_agregados.matriculas", "numeros_agregados.verba_gasta"], "bloqueia": ["meta"], "fonte": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 7", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p06", "ref_plano": "P12", "tipo": "aprovador", "descricao": "Tabela de quem aprova cada tipo de peça está vazia, e o id de aprovação da plataforma ainda não foi informado; a aprovação vai à pessoa do marketing que fez o pedido.", "marcador": "[CONFIRMAR]", "campos": ["arquivos_por_camada.geral[0].ref_aprovacao"], "bloqueia": [], "fonte": "contexto/ufape-geral.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p07", "ref_plano": "seção 3", "tipo": "outro", "descricao": "Status de mídia: a visão de campanhas não traz as provas; só a Ufape confirma se há campanha.", "marcador": "[CONFIRMAR]", "campos": ["status_midia.campanha"], "bloqueia": [], "fonte": "docs/visao-de-campanhas-2026-10-26.md", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p08", "ref_plano": "seção 4", "tipo": "kit", "descricao": "Kit de campanha única definido pelo cmo: prazos, quantidades, fim das inscrições e slug da prova ainda sem definição.", "marcador": "[CONFIRMAR]", "campos": ["slug_sugerido", "fim_das_inscricoes", "kit.entregas[*].prazo", "kit.entregas[*].quantidade_minima"], "bloqueia": [], "fonte": "saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 4", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p09", "ref_plano": "seção 2.3", "tipo": "turma", "descricao": "A sugestão 68608 como turma de destino é do plano e começa em 28/11/2026, um dia depois da prova.", "marcador": "[SUPOSIÇÃO]", "campos": ["prova_de_bolsa.turma_de_destino.sugestao_do_plano", "relacionados[0]", "canais[*]"], "bloqueia": [], "fonte": "contexto/catalogo-de-cursos.md, seções 2 e 3", "aberta_em": "2026-10-26", "resolvida_em": null },
    { "id": "68651-p10", "ref_plano": "U2 do plano do cmo", "tipo": "divergencia", "descricao": "A página diz PROVA PRESENCIAL; a prova é online (decisão 11), texto a corrigir no site. Acesso à prova online e regras de documento e celular a confirmar.", "marcador": "[CONFIRMAR]", "campos": ["modalidade", "prova_de_bolsa.formato"], "bloqueia": [], "fonte": "docs/execucao-2026-10-26.md, decisão 11; ficha da 68651", "aberta_em": "2026-10-26", "resolvida_em": null }
  ],
  "aprovacoes": [
    { "ref": "A3", "o_que": "Tratar as 22 provas de bolsa como uma campanha única com variação por especialidade, e os 47 contínuos com kit sempre ligado por área", "por_que": "Não há kit de prova nem de contínuo nos templates; uma peça por prova multiplicaria o trabalho sem ganho claro.", "quanto": "Reduz cerca de 150 rodadas.", "efeito_esperado": "Campanha das provas pronta até 03/11.", "como_desfazer": "Voltar a um kit por item.", "status": "aprovado", "pedido_em": "2026-10-26", "decidido_em": "2026-10-26", "decidido_por_papel": "pessoa_do_marketing" },
    { "ref": "A8", "o_que": "Enviar metas e verba por linha e os números agregados por turma", "por_que": "Sem isso não há meta nem como checar se a conta fecha.", "quanto": "Verba: a confirmar com a Ufape.", "efeito_esperado": "Metas escritas antes de subir qualquer campanha.", "como_desfazer": "Metas revisadas na segunda-feira seguinte.", "status": "pendente", "pedido_em": "2026-10-26", "decidido_em": null, "decidido_por_papel": null },
    { "ref": "A9", "o_que": "Nomear quem aprova posts, anúncios e verba, mensagens em massa, páginas e preços, e peças com certificação", "por_que": "Tabela de aprovação vazia.", "quanto": "Sem custo.", "efeito_esperado": "Aprovação sem gargalo.", "como_desfazer": "Trocar o responsável na tabela.", "status": "pendente", "pedido_em": "2026-10-26", "decidido_em": null, "decidido_por_papel": null }
  ],
  "historico": [
    { "revisao": 1, "em": "2026-10-26", "campo": "(arquivo)", "de": null, "para": "criado", "motivo": "Criação a partir do catálogo de 26/10/2026, da ficha, do contexto da linha e do plano do cmo.", "origem": "contexto/catalogo-de-cursos.md", "aplicado_por": "cmo" }
  ],
  "resumo": { "pendencias_abertas": 10, "bloqueado": true }
}
```

### 1.8 Trechos de Graduação e de workshop (só o que muda em relação ao modelo)

Graduação, Medicina Veterinária (arquivo graduacao-medicina-veterinaria-sp-2027-1.json). Dados do catálogo (seção 1) e da ficha de editais. O catálogo não tem código para a Graduação.

```json
{
  "id": "graduacao-medicina-veterinaria-sp-2027-1",
  "codigo": "sem-codigo",
  "linha": "graduacao",
  "tipo": "graduacao",
  "nome_no_site": "Medicina Veterinária",
  "nome_padrao": "Medicina Veterinária",
  "slug_sugerido": "[CONFIRMAR]",
  "area": { "codigo": "nao_se_aplica", "nome": "Graduação (ramo à parte)", "natureza": "plano_do_cmo" },
  "recorte": "planejar",
  "motivo_do_recorte": "Graduação entra com plano próprio pelo /campanha-de-vestibular (decisão A2, 26/10/2026).",
  "onda": 1,
  "modo_de_venda": "com_data",
  "local": "São Paulo, SP",
  "modalidade": "Presencial",
  "modalidade_normalizada": "presencial",
  "turma": null,
  "carga_horaria": "4.195 h + 75 h de atividades complementares",
  "modulos": null,
  "inicio": "2027-02-22",
  "fonte_da_data": "edital",
  "dias_ate_inicio": 119,
  "fim_das_inscricoes": null,
  "preco_texto_site": "Integral: de R$ 10.000,00 por R$ 5.000,00/mês (desconto de 50%). Noturno: de R$ 10.000,00 por R$ 4.000,00/mês (desconto de 60%). Regras no Edital de Descontos 2027",
  "preco_estruturado": null,
  "vagas": { "turma_minima": 30, "vagas_ofertadas": null, "vagas_restantes": null },
  "equipe": null,
  "graduacao": {
    "edital": { "numero": "002/2026", "titulo": "Vestibular 2027 (Medicina Veterinária, São Paulo)", "url": "https://faculdade.ufape.com.br/uploads/arquivo/edital-vestibular-2027.pdf" },
    "edital_de_desconto": { "numero": "003/2026", "titulo": "Programa de Desconto de Mensalidade 2027/1", "url": "https://faculdade.ufape.com.br/uploads/arquivo/edital-descontos-2027.pdf" },
    "ato_autorizativo": "Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025), conforme o Edital 002/2026",
    "reconhecimento": "[CONFIRMAR]",
    "grau": "bacharelado",
    "turnos": [
      { "turno": "integral", "duracao_anos": 4, "vagas": 45, "mensalidade_texto": "de R$ 10.000,00 por R$ 5.000,00/mês (desconto de 50%)" },
      { "turno": "noturno", "duracao_anos": 5, "vagas": 45, "mensalidade_texto": "de R$ 10.000,00 por R$ 4.000,00/mês (desconto de 60%)" }
    ],
    "formas_de_ingresso": ["redacao", "enem", "transferencia_externa", "diplomado", "vagas_remanescentes"],
    "inscricoes_abertas_desde": "2026-08-17",
    "inscricao_ate": null,
    "inicio_das_aulas": "2027-02-22",
    "validade_do_desconto": "1º semestre letivo de 2027",
    "lp": {
      "url": "[CONFIRMAR]",
      "alterada_pela_squad": false,
      "utm": { "gerada_por": "plataforma", "parametros": ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"], "utm_campaign": "[CONFIRMAR]" }
    }
  },
  "kit": {
    "template": "templates/kit-de-lancamento-graduacao.md",
    "variacao": null,
    "escopo": "item",
    "entregas": [
      { "chave": "plano_8_canais", "quantidade_minima": 1, "responsavel": ["cmo"] },
      { "chave": "plano_de_midia", "quantidade_minima": 1, "responsavel": ["gestor-de-midia"] },
      { "chave": "posts_organicos", "quantidade_minima": 6, "responsavel": ["posts-sociais"] },
      { "chave": "criativos_com_utm", "quantidade_minima": 4, "responsavel": ["criativos-de-anuncio"] },
      { "chave": "whatsapp_prazos_do_edital", "quantidade_minima": 5, "responsavel": ["copy-de-mensagens"] },
      { "chave": "email_prazos_do_edital", "quantidade_minima": 3, "responsavel": ["copy-de-mensagens"] },
      { "chave": "roteiro_video", "quantidade_minima": 2, "responsavel": ["tiktok"] }
    ]
  }
}
```

Observações do trecho: dias_ate_inicio é de 26/10/2026 até 22/02/2027 (119 dias, calculado). As entregas aparecem reduzidas a chave, quantidade e responsável só para caber aqui; no arquivo real levam todos os campos do modelo. No arquivo real, cada "[CONFIRMAR]" e cada null por origem vazia deste trecho (slug_sugerido, reconhecimento, lp.url, utm_campaign, inscricao_ate, fim_das_inscricoes, vagas_restantes) é citado em "campos" de uma pendência; vagas_ofertadas e turma null sem pendência significam "não se aplica" (vagas por turno ficam em turnos). Os alertas dos editais (data de assinatura "17 de agosto de 2027", preâmbulo com "2º semestre de 2026", seção 6 com numeração repetida, desconto da Pedagogia citando Medicina Veterinária) viram pendências do tipo divergencia, com o texto da ficha como fonte.

Workshop de Neuromonitorização (arquivo eventos-workshop-neuromonitorizacao-2026-11-20.json). Dados do catálogo (seção 9) e da ficha do evento.

```json
{
  "id": "eventos-workshop-neuromonitorizacao-2026-11-20",
  "codigo": "sem-codigo",
  "linha": "eventos",
  "linha_origem": "plano",
  "tipo": "workshop",
  "nome_no_site": "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia",
  "nome_padrao": "Workshop Brasileiro de Neuromonitorização Veterinária, Anestesia e Neurologia",
  "aliases": ["I SIMPÓSIO BRASILEIRO DE NEUROMONITORIZAÇÃO VETERINÁRIA"],
  "area": { "codigo": "A12", "nome": "Neurologia", "natureza": "plano_do_cmo" },
  "relacionados": [ { "id": "livres-68634", "relacao": "modalidade_do_mesmo_evento", "natureza": "dado" } ],
  "local": "São Paulo, Av. Tiradentes, 960 (Unidade 2)",
  "modalidade": "Presencial",
  "modalidade_normalizada": "presencial",
  "carga_horaria": "16 h",
  "inicio": "2026-11-20",
  "fonte_da_data": "planilha",
  "dias_ate_inicio": 25,
  "preco_texto_site": "Presencial (teórico e prático, 16 h, 30 vagas): R$ 1.250,00. Transmitido + gravado (só teoria): R$ 450,00 (produto 68634). Aluno e ex-aluno Ufape: 20% de desconto com o cupom SIMPNEUROMONIT",
  "preco_estruturado": null,
  "condicoes_especiais": [ { "tipo": "cupom", "texto": "20% de desconto para aluno e ex-aluno Ufape", "codigo": "SIMPNEUROMONIT", "publico": "aluno e ex-aluno Ufape", "validade": null } ],
  "vagas": { "turma_minima": null, "vagas_ofertadas": 30, "vagas_restantes": null },
  "equipe": null,
  "evento": {
    "subtipo": "workshop",
    "data_inicio": "2026-11-20",
    "data_fim": "2026-11-21",
    "horario_texto": "08h às 18h nos dois dias",
    "formato": "presencial",
    "modalidades": [
      { "nome": "Presencial (teórico e prático)", "preco_texto_site": "R$ 1.250,00", "vagas": 30, "produto": null },
      { "nome": "Transmitido + gravado (só teoria)", "preco_texto_site": "R$ 450,00", "vagas": null, "produto": "68634" }
    ],
    "carga_horaria_oficial": "16 h",
    "cupom": { "codigo": "SIMPNEUROMONIT", "publico": "aluno e ex-aluno Ufape", "desconto_texto": "20% de desconto", "comprovacao_texto": "comprovação do vínculo na secretaria" },
    "pagina_oficial": "https://faculdade.ufape.com.br/neuro-summit/",
    "destino_das_campanhas_pagas": "https://faculdade.ufape.com.br/neuro-summit/",
    "palestrantes": { "confirmados_na_ficha": 5, "convidados_a_definir": null, "autorizacoes_de_imagem_registradas": null }
  },
  "status_midia": { "campanha": "ativa", "formatos": ["estatico"], "cinco_angulos": "nao_se_aplica", "vinculo_com_a_visao": "provavel", "inicio_na_visao": "2026-11-20", "divergencia_de_data": false, "observacao": "A visão chama o item de I Simpósio e informa que o racional de 5 ângulos não se aplica a eventos." },
  "kit": { "template": "templates/kit-de-lancamento-evento.md", "variacao": "simposio", "escopo": "item" }
}
```

Observações do trecho: kit.variacao é "simposio" porque o plano do cmo (seção 4, camada 3) aplicou a variação simpósio, mas a ficha e a decisão da Ufape de 26/10/2026 chamam o evento de workshop; vira pendência do tipo divergencia, "[CONFIRMAR]" qual variação do template vale. Também são pendências, no arquivo real: a carga horária do produto 68634 na loja (24 h contra 16 h oficiais), a falta de data no 68634, a validade do cupom (validade null), a quantidade de convidados a definir (null), as vagas da modalidade transmitida (null), a turma mínima e as vagas restantes (null) e a autorização de imagem dos palestrantes (null, marcador "[CONFIRMAR autorização]"). Nenhum nome de docente, de coordenador científico ou de convidado aparece.

---

## 2. Nome e pasta dos arquivos

### 2.1 Regra geral

- Pasta única, sem subpastas: saidas/10-operacoes-de-marketing/cursos/
- Nome: `<linha>-<codigo>.json`, com a linha em minúsculas (pos, livres, eventos ou graduacao) e o código exatamente como está no catálogo (só dígitos, sem zero à esquerda). Nunca "geral": todo JSON pertence a uma linha.
- Exemplos: pos-707.json, pos-68651.json, livres-68614.json, livres-68634.json, eventos-700.json, eventos-202.json.
- A linha do nome é o campo linha do JSON, que segue o catálogo, ou o plano quando o plano move o item (700 e 202 estão na seção "Simpósios e congressos" do catálogo e são Eventos no plano; linha_origem registra "plano").
- O id do JSON é igual ao nome do arquivo sem ".json". O id nunca muda e nunca é reaproveitado.
- Caracteres: letras minúsculas sem acento, dígitos e hífen; nada de espaço, travessão, meia-risca ou sublinhado no nome.
- Contagem esperada na primeira geração: 184 arquivos no total, Graduação incluída (110 do recorte, 72 de histórico ou pendência e 2 da Graduação), igual ao total do catálogo na seção 2.2 do plano.

### 2.2 Caso sem código

Quando o catálogo não tem código, o nome é `<linha>-<slug>[-<AAAA-MM-DD>].json`:

- slug: do nome_no_site, em minúsculas, sem acento, só letras e números, palavras separadas por hífen, até 60 caracteres, cortando na última palavra inteira. Fica com a grafia do catálogo (rastreável), mesmo que o nome tenha erro; o nome certo vai em aliases ou nome_padrao.
- sufixo de data: data de início em AAAA-MM-DD quando existe; "sem-data" quando não existe.
- Graduação: `graduacao-<curso>-<praça>-<AAAA>-<semestre>.json`, porque a liberação é por edital mais curso.
- campo codigo do JSON: "sem-codigo".

| Item | Arquivo |
|---|---|
| Graduação, Medicina Veterinária (edital 002/2026) | graduacao-medicina-veterinaria-sp-2027-1.json |
| Graduação, Pedagogia (edital 004/2026) | graduacao-pedagogia-go-2027-1.json |
| Workshop de Neuromonitorização (20 e 21/11/2026) | eventos-workshop-neuromonitorizacao-2026-11-20.json |
| Simpósio Plantonista Veterinário (só na planilha, 10/10/2026) | eventos-simposio-plantonista-veterinario-2026-10-10.json |
| Paciente Grave Multidiciplinar (só na planilha, sem data) | eventos-paciente-grave-multidiciplinar-foco-em-casos-clinicos-sem-data.json |

Nota sobre o workshop: o plano (seção 6.2) dá como exemplo "eventos-simposio-neuromonitorizacao-2026-11-20.json". Proponho "workshop" no nome porque a decisão da Ufape de 26/10/2026 e a ficha chamam o evento de workshop; o padrão de nomes aprovado em A11 não muda. O nome da planilha fica em aliases. Fica como decisão para a pessoa do marketing (lista de dados que faltam).

### 2.3 Quando o código aparece depois

Se um item sem código ganhar código no catálogo, o cmo cria o arquivo novo `<linha>-<codigo>.json` (revisao 1, com a linha de histórico "origem: arquivo anterior"), marca o antigo com estado_do_arquivo "substituido" e substituido_por com o id novo, e registra o vínculo em relacionados (relacao "substitui"). O arquivo antigo não é apagado nem renomeado, para o HTML e a plataforma não perderem a referência.

### 2.4 Relatórios e outros arquivos do fluxo

- JSON: só em saidas/10-operacoes-de-marketing/cursos/.
- HTML: saidas/02-estrategia-e-posicionamento/cmo-geral-AAAA-MM-DD.html (nome aprovado em A11), um arquivo por versão do mapa (v1 em 30/10, v2 em 20/11, v3 em 11/12, datas do plano).
- Relatório do lote ou das mudanças (Markdown): como o nome padrão cmo-<linha>-AAAA-MM-DD.md pode já existir no mesmo dia (plano ou revisão semanal), o relatório leva o sufixo "-mapa": cmo-<linha>-AAAA-MM-DD-mapa.md, em saidas/02-estrategia-e-posicionamento/. Isso é uma exceção à regra de nomes do briefing e precisa de ok (lista de dados que faltam).
- Veredito do qa: o do agente, qa-de-marketing-<linha>-AAAA-MM-DD.md em saidas/10-operacoes-de-marketing/.
- A pasta cursos/ entra uma vez em conhecimento/INDICE.md (um registro da pasta, não um por arquivo).

---

## 3. Fluxo de geração e atualização

### 3.1 SIPOC (skill .claude/skills/mapear-fluxo/SKILL.md)

| Fornecedores | Entradas | Processo | Saídas | Clientes |
|---|---|---|---|---|
| Responsável pelo catálogo na Ufape ([nome, área] ainda vazio no catálogo) | contexto/catalogo-de-cursos.md e fichas em contexto/cursos/ (dados de curso, datas da planilha, preço e status do site) | 1. Gatilho e leitura das fontes | JSON por curso, um por item, com o esquema versão 1 | Pessoa do marketing (aprova o lote) |
| Time de captação | Números agregados por turma (leads, inscrições, matrículas, vagas restantes, verba gasta) e inventário do que já existe do kit [CONFIRMAR se vai enviar] | 2. Montagem ou atualização dos JSON pelo cmo | Relatório do lote ou das mudanças (o que mudou, de quê, para quê, por quê) | Diretoria e cliente da Ufape (apresentação do mapa) |
| Regulação | Texto oficial de certificação e atos regulatórios [CONFIRMAR] | 3. Geração do HTML com os JSON embutidos (cmo) | Mapa mental HTML, arquivo único que abre offline | Time de captação (vê dono, prazo e pendência de cada curso) |
| Coordenação de curso | Autorização de imagem e voz de docentes e palestrantes [CONFIRMAR autorização]; confirmação de datas e docentes | 4. Conferência do qa-de-marketing (auditorias/10-operacoes.md, auditorias/09-analytics.md, auditorias/conformidade-educacional.md) | Veredito de QA com lista de problemas | cmo (corrige o que voltar) |
| Agentes da squad (saídas aprovadas das camadas 1, 2 e 3) | Saídas aprovadas em saidas/, com cabeçalho (agente, linha, data) e seção por código ou área | 5. Aprovação humana do lote e do mapa | JSON com revisao_aprovada atualizada e histórico | Plataforma (futura importação, por pedido ao admin) |
| gestor-de-midia | Revisão semanal de mídia e metas de custo; visão de campanhas atualizada (planilha) | 6. Registro do que foi aprovado e atualização contínua (seções 3.4 a 3.6) | Pedidos de aprovação (A1 a A12) registrados em cada item | Regulação e coordenação (veem as pendências que dependem delas) |
| Plataforma (fila de aprovação e registro de entrega) | Registro de aprovação: ref, data, papel de quem aprovou | | | |

### 3.2 Quem produz cada campo e quando

| Bloco de campos | Quem produz | Etapa | Como muda depois |
|---|---|---|---|
| X controle, fontes, historico | cmo | etapa 1 de /mapa-de-cursos-montar (e de /mapa-de-cursos-atualizar) | a cada gravação: revisao sobe 1, atualizado_em, uma linha em historico |
| C espelho (identidade, local, modalidade, turma, CH, início, preço, status, vagas, equipe, blocos por tipo) | cmo copia do catálogo, da ficha e do contexto da linha; o responsável pelo catálogo na Ufape é a fonte | montagem | só quando o catálogo ou a ficha mudam (3.5); nunca por saída de agente |
| P plano (area, recorte, onda, gut, grupo, relacionados, turma de destino) | cmo, a partir do plano aprovado (skill .claude/skills/matriz-gut/SKILL.md para itens sem nota) | montagem | só com nova versão aprovada do plano |
| M status_midia | cmo, lendo a visão de campanhas | montagem | nova visão de campanhas (3.6); decisão de pausa só vale depois de executada por humano e refletida na visão |
| K kit e canais | cmo abre o kit do tipo (templates/kit-de-lancamento-*.md) e propõe os canais | montagem | saída de agente aprovada (3.4) |
| A arquivos_por_camada e aprovacoes | cmo, a partir dos cabeçalhos das saídas e dos pedidos do plano (seção 8) | montagem | saída aprovada, resposta a pedido de aprovação |
| N metas e numeros_agregados | gestor-de-midia (metas) e Ufape (números); o cmo só registra | quando o número chegar | nunca inventado; sem número, null com pendência |
| pendencias | cmo, a partir de auditorias, plano (seção 7) e "dados que faltam" das saídas | montagem | aberta em divergência nova; resolvida_em quando a fonte muda |
| D derivados (dias_ate_inicio, preco_estruturado, resumo) | cmo, calculados | a cada gravação | recalculados sempre |

### 3.3 Etapas macro (de 5 a 7) com responsável, entrada e saída

| # | Etapa | Responsável | Tipo | Entrada | Saída |
|---|---|---|---|---|---|
| 1 | Gatilho e leitura das fontes | cmo | agente | catálogo, fichas, visão de campanhas, plano, saídas aprovadas | lista de itens a criar ou a mudar |
| 2 | Escrita dos JSON (só os afetados) e relatório do lote | cmo | agente | etapa 1 | JSON em cursos/ e cmo-<linha>-AAAA-MM-DD-mapa.md |
| 3 | Geração do HTML com os JSON embutidos | cmo | agente | JSON da etapa 2 | cmo-geral-AAAA-MM-DD.html |
| 4 | Conferência de QA | qa-de-marketing | agente | etapas 2 e 3, catálogo | qa-de-marketing-<linha>-AAAA-MM-DD.md |
| 5 | Aprovação humana do lote e do mapa | pessoa do marketing | humano | etapa 4 | revisao_aprovada atualizada; liberação do mapa para o cliente |
| 6 | Apresentação ao cliente (fora do fluxo de agentes) | pessoa do marketing | humano | HTML aprovado | nenhuma ação automática |

As etapas 1 a 3 rodam numa só chamada do cmo (seção 3.10), o que dá 2 chamadas de agente por rodada de atualização. A aprovação humana acontece depois de cada chamada, como exige a plataforma (CLAUDE.md, "Execução pela plataforma").

### 3.4 Atualização quando uma saída de agente é aprovada

Gatilho: saída aprovada pela pessoa do marketing, com veredito "aprovado" do qa-de-marketing. Para não pagar uma chamada por saída, as saídas aprovadas na semana entram juntas na rodada da segunda-feira (revisão do cmo), e também no fim de cada onda.

1. O cmo lê o cabeçalho da saída (agente, linha, data) e o registro de aprovação (ref, data, papel).
2. Descobre o alcance: camada 1, linha ou geral: todos os itens da linha (ou de todas) recebem o arquivo em arquivos_por_camada.linha ou .geral; camada 2: itens com area.codigo igual à área da seção; camada 3: itens cujo código aparece no título da seção (regra do briefing: uma seção por curso, com o código do catálogo no título).
3. Atualiza a entrega do kit pela tabela abaixo: arquivo e secao preenchidos, status "aguardando_aprovacao" quando a saída existe sem aprovação, "devolvido" se o qa mandou corrigir, "aprovado" só com qa "aprovado" e aprovação humana (ref_aprovacao).
4. Saída de agente nunca muda campo C. Se a saída contradiz o catálogo, o cmo abre pendência do tipo divergencia; o catálogo continua mandando.
5. Dados que faltam citados pela saída entram em pendencias só se o cmo os aceita, com "campos" preenchido; suposições da saída entram com marcador "[SUPOSIÇÃO]".
6. revisao sobe 1, uma linha em historico por campo alterado, resumo recalculado.

| Agente (saída aprovada) | Chave da entrega atualizada | Outros campos |
|---|---|---|
| cmo (plano da liberação) | plano_8_canais | canais, metas, gut, onda, recorte, kit.acrescimos, aprovacoes |
| landing-page, seo-on-page, otimizador-de-cta (via /pagina-de-curso) | pagina | |
| gestor-de-midia (/plano-de-midia-da-turma) | plano_de_midia | metas (custo); status_midia só pela regra de 3.6 |
| posts-sociais | posts_organicos | |
| criativos-de-anuncio | criativos (criativos_com_utm na Graduação) | |
| autoridade-docente | post_por_docente ou post_por_palestrante | autorizados |
| copy-de-mensagens | whatsapp, email, mensagem_convite, mensagem_vespera, mensagem_do_dia, email_convite, email_lembrete, email_programacao, whatsapp_prazos_do_edital, email_prazos_do_edital | |
| tiktok | roteiro_video | |
| estrategia-de-campanha, estrategia-de-oferta | campanha_unica, oferta_e_regras_da_bolsa (grupo de provas) | |
| demais agentes das camadas 1 e 2 | nenhuma entrega do kit | só arquivos_por_camada |

### 3.5 Atualização quando um dado do catálogo muda

Gatilho: o responsável pelo catálogo na Ufape (a squad não altera o catálogo) atualiza o catálogo ou uma ficha, e a pessoa do marketing pede /mapa-de-cursos-atualizar com o gatilho "catalogo". O ciclo extra do cmo (quando mudar preço, data, vagas, local, formato ou docentes) usa a mesma rodada.

1. O cmo compara a linha atual do catálogo com fontes.catalogo_linha_literal de cada JSON. Linha igual: nada muda. Linha diferente: segue.
2. Linha nova no catálogo (sem arquivo): cria JSON com recorte "pendencia" até o cmo decidir o recorte e abrir o kit, e informa no relatório. Linha que sumiu do catálogo: o JSON não é apagado; recorte vira "historico" com motivo e pendência.
3. Campo C diferente: o cmo grava o valor novo (cópia literal), atualiza catalogo_linha_literal e data_catalogo, e escreve uma linha em historico com campo, de, para, origem (catálogo e data) e motivo.
4. Se mudou preço, início, local, modalidade, carga horária, turma, status ou condições, toda entrega do kit em "aguardando_aprovacao" ou "aprovado" passa para "revisar_por_mudanca" e abre-se uma pendência do tipo preco_ou_condicao, data ou divergencia, com "campos" citando o campo mudado e bloqueia ["peca_final"] (e ["anuncio"] se há campanha ativa). Peça já publicada é por conta da pessoa do marketing: o relatório só lista, e qualquer pausa é pedido de aprovação.
5. Se status_catalogo muda para "verificar", "sem venda", "encerrado" ou "sem página", a regra R14 pede mudar o recorte. Mudança de recorte, onda ou GUT é decisão (classe P): o cmo a propõe no relatório e só grava depois da aprovação.
6. Recalcula dias_ate_inicio, preco_estruturado e resumo; revisao sobe 1.
7. O relatório de mudanças traz uma tabela com id, campo, de, para, entregas afetadas e pendências abertas ou fechadas.

Exemplo: o preço da 707 muda de 30x de R$ 1.590,00 para outro valor. Só o pos-707.json é regravado: preco_texto_site novo, preco_estruturado recalculado, catalogo_linha_literal novo, as entregas aprovadas voltam a "revisar_por_mudanca", nasce a pendência de preço, e o HTML mostra o selo vermelho no item.

### 3.6 Outros gatilhos

- Nova visão de campanhas: o cmo atualiza status_midia (campanha, formatos, cinco_angulos, inicio_na_visao, divergencia_de_data, lido_em). O vínculo com a visão é por nome, data e UF (a visão não tem código): "exato" quando os três batem, "provavel" ([SUPOSIÇÃO]) quando só dois, "nenhum" quando nenhum. Uma decisão de pausa do gestor-de-midia só altera status_midia depois que o humano executou a ação no gerenciador de anúncios e a visão de campanhas refletir isso; antes, a decisão é um pedido em aprovacoes.
- Virada de onda: no fim de cada onda, o cmo roda a atualização geral (todos os itens da onda), recalcula dias_ate_inicio e abre a próxima onda.
- Metas ou números chegam: o cmo preenche metas e numeros_agregados só com número entregue pela Ufape ou pelo gestor-de-midia, com a fonte, e fecha a pendência (resolvida_em).
- Autorização de imagem registrada: o cmo atualiza apenas a contagem (autorizados e equipe.autorizacoes_de_imagem_registradas); nome nenhum entra no arquivo.

### 3.7 Como o HTML lê os JSON

- O HTML é um arquivo só, sem CDN, e abre offline. Os navegadores em geral não deixam uma página aberta de um arquivo local ler outros arquivos locais, então o HTML não busca a pasta cursos/: o cmo copia cada JSON, sem editar, para dentro de um bloco `<script type="application/json" id="dados-do-mapa">` do próprio HTML, ordenado por id. Os JSON mandam; o HTML é só vista.
- Toda contagem (itens por linha, onda, área, status, bloqueados) é calculada no navegador a partir desses dados, nunca escrita à mão. O cabeçalho do mapa mostra a data do catálogo, a data de geração e a quantidade de itens por estado (revisao maior que revisao_aprovada aparece como "rascunho").
- Dias até o início: o navegador recalcula a partir de inicio e da data de hoje, e mostra também o valor do JSON com a data da gravação.
- O HTML só desenha as chaves deste esquema (lista fechada) e escreve os textos como texto, nunca como HTML, para que um campo livre não vire código nem vaze dado fora do esquema.
- Valor null com pendência que o cita aparece como "-" com o selo da pendência; null sem pendência não aparece.
- Mapa de campos para os nós do plano (seção 6.1):

| Nó do mapa | Chaves lidas |
|---|---|
| Nível 0: plano e contagem geral | fontes.data_catalogo, fontes.plano, contagens por recorte e linha, metas (principal, null com pendência) |
| Nível 1: linhas, Ondas e calendário, Pendências e bloqueios, Aprovações, Histórico | linha, onda, resumo.bloqueado, pendencias, aprovacoes, historico |
| Nível 2: estratégia da linha e áreas | arquivos_por_camada.linha, area.codigo, area.nome, canais |
| Nível 3: área | arquivos_por_camada.area, area, contagem de itens |
| Nível 4: curso, turma ou edição | codigo, nome_no_site, nome_padrao, local, modalidade_normalizada, inicio, fonte_da_data, dias_ate_inicio, status_catalogo, status_midia.campanha, onda, gut, canais, fontes.ficha |
| Nível 5: kit, pendências, aprovações | kit, pendencias, aprovacoes |

- Preço aparece só no nó do curso, com preco_texto_site e a nota "site em 26/10/2026; conferir antes de publicar".
- Filtros (linha, onda, área, status do catálogo, status de mídia, bloqueado) usam linha, onda, area.codigo, status_catalogo, status_midia.campanha e resumo.bloqueado. Selo vermelho em item com resumo.bloqueado igual a true. Links para os arquivos de camada são relativos (o HTML fica em saidas/02-estrategia-e-posicionamento/, os arquivos em saidas/ e contexto/).
- O qa confere que o conjunto de id e revisao do HTML é igual ao da pasta cursos/.

### 3.8 Documento de fluxo (templates/documento-de-fluxo.md)

DOCUMENTO DE FLUXO

Nome do fluxo: Mapa de cursos (montar e atualizar), workflows /mapa-de-cursos-montar e /mapa-de-cursos-atualizar

Linha de negócio: geral (Graduação, Pós-graduação, Cursos Livres e Eventos)

Gatilho:
- Montar: fim de cada onda (27/10 a 06/11, 07/11 a 27/11, a partir de 30/11), pedido da pessoa do marketing.
- Atualizar: segunda-feira (revisão do cmo), mudança no catálogo ou em uma ficha, nova visão de campanhas, ou saída aprovada na semana.

Etapas (responsável / entrada / saída):
- Montar, etapa 1: relatorios / saídas aprovadas da onda / narrativa e roteiro de apresentação (saidas/09-analytics-e-insights/relatorios-geral-AAAA-MM-DD.md).
- Montar, etapa 2: cmo / catálogo, fichas, plano, visão de campanhas, saída da etapa 1 / JSON por item, HTML e relatório do lote.
- Montar, etapa 3: qa-de-marketing / saída da etapa 2 / veredito de QA.
- Atualizar, etapa 1: cmo / gatilho, catálogo, saídas aprovadas / JSON regravados, HTML novo e relatório de mudanças.
- Atualizar, etapa 2: qa-de-marketing / saída da etapa 1 / veredito de QA.

Etapas de agente: relatorios (só ao montar), cmo, qa-de-marketing.

Etapas de aprovação humana: depois de cada etapa (a plataforma pede); a última aprovação libera o mapa para apresentação ao cliente. Aprovação de mudança de recorte, onda, GUT, pausa de campanha e qualquer ação fora da plataforma é pedido explícito (o que, por que, quanto, efeito esperado, como desfazer). Responsável pela aprovação: pessoa do marketing que fez o pedido, até a tabela de aprovação de contexto/ufape-geral.md ser preenchida (P12).

Checagens de QA e conformidade (qa-de-marketing e auditorias/conformidade-educacional.md): as 12 conferências da seção 3.9, mais auditorias/10-operacoes.md, auditorias/09-analytics.md e auditorias/conformidade-educacional.md.

Ferramentas usadas: repositório de arquivos da squad (saidas/, contexto/, docs/); plataforma de orquestração (registro de entrega e fila de aprovação). CRM, Chatwoot, n8n, ClickUp, Supabase, GA4, Meta Ads e Google Ads: nenhuma neste fluxo (nada vai para o banco agora; a visão de campanhas vem da planilha, lida como arquivo).

Concluído quando: a pasta cursos/ tem um JSON por item da onda com o nome da seção 2; todos passam nas 12 conferências do qa-de-marketing; o HTML abre offline e tem os mesmos id e revisao dos JSON; nenhum campo de nome de pessoa; e a pessoa do marketing aprovou o lote e o mapa.

Data de revisão: 02/11/2026 (primeira segunda-feira depois da primeira rodada de atualização) [SUPOSIÇÃO].

### 3.9 Texto dos workflows para .claude/commands

Os dois textos abaixo seguem o formato dos workflows existentes (por exemplo, arrumacao-mensal.md e campanha-de-vestibular.md). Só citam agentes, skills e auditorias que existem. Não foram gravados em .claude/commands: é a pasta onde a plataforma lê os workflows, e a criação dos arquivos fica para depois da aprovação.

Arquivo `.claude/commands/mapa-de-cursos-montar.md`:

```
---
description: Fim de cada onda. Monta o mapa mental HTML e os JSON por curso. Cadeia: relatorios -> cmo -> qa-de-marketing
argument-hint: [onda 1, 2 ou 3] [linha: pos, livres, eventos, graduacao ou geral]
---
Execute o workflow "Mapa de cursos: montar".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar (os quatro contextos, quando a linha for geral). Onda e linha deste pedido: $ARGUMENTS

Regras do esquema: siga a seção 1 de saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md (esquema versao 1) e os nomes da seção 2. Dados de curso só de contexto/catalogo-de-cursos.md; o que faltar vira "[CONFIRMAR]" em campo de texto, ou null com pendência em campo de número ou data. Nenhum campo de nome de pessoa.

1. Use o agente relatorios para produzir a narrativa e o roteiro de apresentação da onda ao cliente, a partir das saídas aprovadas. Salve e passe o arquivo para a próxima etapa.
2. Use o agente cmo para produzir um JSON por item da onda em saidas/10-operacoes-de-marketing/cursos/ (nome <linha>-<codigo>.json), o mapa mental HTML em saidas/02-estrategia-e-posicionamento/ (cmo-geral-AAAA-MM-DD.html, com os JSON embutidos) e o relatório do lote em Markdown (cmo-<linha>-AAAA-MM-DD-mapa.md): itens criados, campos pendentes, pendências que bloqueiam e pedidos de aprovação. Use a skill matriz-gut (.claude/skills/matriz-gut/SKILL.md) só para item sem nota de GUT. Salve e passe os arquivos para a próxima etapa.
3. Use o agente qa-de-marketing para conferir o lote e o HTML contra o catálogo e o esquema (as 12 conferências do documento de fluxo) e devolver aprovado ou corrigir. Salve e passe o arquivo para a próxima etapa.
4. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto, e também auditorias/09-analytics.md para o mapa.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: cada item da onda tem um JSON com o nome da seção 2 e passa nas 12 conferências, o HTML abre offline com os mesmos id e revisao dos JSON, nenhum campo de nome de pessoa existe e o lote e o mapa estão aprovados.
```

Arquivo `.claude/commands/mapa-de-cursos-atualizar.md`:

```
---
description: Toda segunda-feira, ou quando o catálogo, a visão de campanhas ou uma saída aprovada mudar. Cadeia: cmo -> qa-de-marketing
argument-hint: [gatilho: saida-aprovada, catalogo, visao-de-campanhas ou virada-de-onda] [linha ou geral] [caminhos das saídas aprovadas, se houver]
---
Execute o workflow "Mapa de cursos: atualizar".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Gatilho, linha e saídas deste pedido: $ARGUMENTS

Regras: siga as seções 1, 2 e 3.4 a 3.6 de saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md. Regrave só os JSON afetados (revisao mais 1, uma linha de historico por campo). Saída de agente nunca muda dado de catálogo. Mudança de recorte, onda ou GUT e qualquer pausa de campanha são pedidos de aprovação, não gravações diretas. Nenhum campo de nome de pessoa.

1. Use o agente cmo para produzir o relatório de mudanças em saidas/02-estrategia-e-posicionamento/ (cmo-<linha>-AAAA-MM-DD-mapa.md: id, campo, de, para, fonte, entregas afetadas, pendências abertas e fechadas, pedidos de aprovação), regravar os JSON afetados em saidas/10-operacoes-de-marketing/cursos/ e gerar o HTML novo (cmo-geral-AAAA-MM-DD.html, com os JSON embutidos). Salve e passe os arquivos para a próxima etapa.
2. Use o agente qa-de-marketing para conferir só os JSON do relatório e o HTML (as 12 conferências do documento de fluxo, mais a conferência de que nenhum outro JSON mudou) e devolver aprovado ou corrigir. Salve e passe o arquivo para a próxima etapa.
3. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: cada mudança do relatório está em um JSON com revisao mais 1 e linha em historico, nenhum JSON fora do relatório mudou, o HTML novo tem os mesmos id e revisao dos JSON e o lote está aprovado.
```

As 12 conferências do qa-de-marketing (citadas nos dois workflows):

| # | Conferência |
|---|---|
| C1 | Nome do arquivo igual ao id e ao padrão da seção 2; id único; contagem de arquivos igual ao total do catálogo (184, Graduação incluída). |
| C2 | versao_schema 1; todas as chaves obrigatórias do tipo; nenhuma chave fora do esquema; só o bloco por tipo certo. |
| C3 | Todo valor de campo fechado está no vocabulário de 1.4. |
| C4 | Campos de classe C idênticos à linha atual do catálogo (e à ficha ou ao contexto da linha, nos campos_so_na_ficha), em cópia literal; catalogo_linha_literal igual à linha do catálogo. |
| C5 | Origem vazia aparece como "[CONFIRMAR]" em campo de texto e como null com pendência em campo de número, data, lista ou objeto (R1); sem "", sem "N/A", sem número fora do catálogo, da ficha ou do contexto da linha. |
| C6 | Kit igual ao template do tipo, com as quantidades mínimas intactas e as chaves de 1.4. |
| C7 | dias_ate_inicio recalculado; recorte "planejar" só com status aberto ou aberto (contínuo) (R14). |
| C8 | preco_estruturado bate com preco_texto_site, ou é null. |
| C9 | Nenhum dado pessoal: nenhuma chave de nome de pessoa, nenhum e-mail, telefone, CPF, tratamento seguido de nome (Dr., Dra., Prof., MSc, PhD) ou texto livre acima de 240 caracteres. |
| C10 | Nenhuma frase de certificação ligada ao MEC em nenhum campo de texto, em qualquer variante ("certificado pelo MEC", "reconhecida pelo MEC", "do MEC", "pelo MEC", "Ministério da Educação" como certificador), nem nota do MEC, depoimento ou "últimas vagas". Única exceção: o ato regulatório da Graduação copiado do catálogo (por exemplo, "Portaria SERES/MEC nº 162, de 13/03/2025"). Nas pendências, a frase é descrita como "frase de certificação que a squad não repete". |
| C11 | Todo valor "[CONFIRMAR]" ou "[CONFIRMAR autorização]" em campo inteiro, e todo null em campo que se aplica ao tipo e tem origem vazia, é citado em "campos" de uma pendência aberta (aceita "[*]"); todo "[SUPOSIÇÃO]" em campo (natureza, vínculo) é citado por pendência de marcador "[SUPOSIÇÃO]". Ficam fora da conferência o texto descritivo de aprovacoes que cita o plano e o null sem pendência que a regra R2 define como "não se aplica". Os exemplos 1.6 e 1.7 passam na C11. |
| C12 | HTML: mesmos id e revisao dos JSON, sem CDN, abre sem rede, contagens calculadas e nenhuma chave fora do esquema desenhada. |

### 3.10 O que foi cortado e quantas etapas o fluxo tem

Cada etapa é uma chamada ao Claude, com custo e uma aprovação humana.

| Fluxo | Etapas | Chamadas de agente | Aprovações humanas |
|---|---|---|---|
| /mapa-de-cursos-montar (uma vez por onda) | 3 | 3 (relatorios, cmo, qa-de-marketing) | 3 |
| /mapa-de-cursos-atualizar (por rodada) | 2 | 2 (cmo, qa-de-marketing) | 2 |
| M.1, este desenho | feito uma vez | 1 | 1 (a do plano M.1) |

O plano previa 4 chamadas por onda (M.1 a M.4). Como o M.1 é um desenho que roda uma vez, sobram 3 por onda, que é o montar. O total de rodadas do mapa no plano (4 por onda, 12 nas 3 ondas) cai para 1 desenho mais 9 chamadas de montagem (3 ondas) mais 2 por rodada de atualização.

Cortes (nenhum muda a entrega):

1. Agente de validação de esquema: cortado. O qa-de-marketing já confere dado de curso contra o catálogo e a conformidade; as 12 conferências cobrem o esquema.
2. Chamada separada para o HTML: cortada. O HTML é derivado dos JSON e sai na mesma chamada do cmo, porque ele embute os arquivos que acabou de gravar (como no M.3 do plano).
3. Chamada do relatorios na atualização: cortada. A narrativa só muda na montagem de cada onda; atualização não altera a história contada ao cliente.
4. Uma chamada por saída aprovada: cortada. As saídas aprovadas entram em lote, na segunda-feira e no fim da onda.
5. Regravar todos os JSON a cada rodada: cortado. Só os afetados são regravados, e o qa confere que nenhum outro mudou.
6. Arquivo de índice e hash dos arquivos: cortados. O id e a revisao já identificam versão; um índice a mais criaria um segundo lugar para ficar desatualizado. O hash de verdade fica para a plataforma calcular na importação.
7. Etapa de "validar com a Ufape" dentro do fluxo: cortada. O que depende da Ufape vira pendência e pedido de aprovação no próprio JSON, sem parar o fluxo.
8. Documento separado de contrato para o admin: cortado. O contrato é a seção 4 deste arquivo.

Risco de tamanho: a onda 2 tem 54 itens. Se o cmo não couber o lote numa só chamada, divide-se por linha dentro da onda [SUPOSIÇÃO: o limite de contexto ainda não foi testado com 54 JSON]. Isso acrescenta chamadas e deve ser dito antes, não depois.

---

## 4. O que a plataforma precisa para importar esses arquivos depois

Nada vai para o banco agora. Este documento não cria tabela, função, migration, rota nem chamada de IA. Os JSON são só arquivos na pasta saidas/10-operacoes-de-marketing/cursos/. A importação futura é um pedido ao ufape-admin, que é o único projeto que cria migrations e que segue o rito completo (plano aprovado pelo CEO, testes, revisão) [SUPOSIÇÃO: o pedido segue esse rito]. Esta seção é só o contrato de dados que a squad oferece.

### 4.1 Contrato do arquivo

- Chave natural: id (igual ao nome do arquivo). Ligação com o cadastro de cursos e turmas pela dupla linha e codigo; o admin diz qual é a chave dele ([CONFIRMAR]: como o código do catálogo se liga às tabelas cursos e turmas). Para Graduação e itens sem código, vale o id.
- Formato: UTF-8, JSON, um objeto por arquivo, versao_schema 1, regras de 1.1 (R13).
- Idempotência: reimportar o mesmo arquivo não duplica. Um arquivo com revisao menor que a já importada é rejeitado; revisao igual com conteúdo diferente é divergência e não é aplicada.
- Marcadores e vazios: todo texto que começa com "[CONFIRMAR" ou é "[SUPOSIÇÃO]" é tratado como valor ausente, com sinalização na tela. Campo de número ou data null cujo caminho aparece em "campos" de uma pendência aberta também é valor ausente (R1 e R2); null sem pendência é "não se aplica". Nenhum vira zero, data vazia nem texto de peça.
- Vocabulários fechados de 1.4: valor fora da lista rejeita o arquivo.
- Arquivos com estado_do_arquivo "substituido": importados só como histórico, sem entrar em contagem de itens ativos.
- Arquivos que começam com "_" (se algum dia existirem) são ignorados.

### 4.2 O que importar e o que só conferir

| Classe | O que são | Tratamento sugerido |
|---|---|---|
| C espelho | Cópia do catálogo e da ficha | Não importar como verdade. Na plataforma, a ficha congelada da liberação faz o papel do catálogo (CLAUDE.md da squad) e as tabelas cursos e turmas mandam nos dados de curso (CLAUDE.md do admin). O espelho serve para conferir: se divergir, gerar relatório de divergência, sem sobrescrever. Preço nunca é lido do JSON. |
| P plano, K kit e canais, M mídia, N metas e números | Camada de planejamento de marketing | Candidatos a importar, ligados ao curso ou turma pela chave natural. |
| A arquivos_por_camada e aprovacoes | Referências a saídas e pedidos | A plataforma já registra entrega e aprovação; o registro dela prevalece [SUPOSIÇÃO]. O JSON guarda a ref para cruzar. |
| pendencias | Lacunas e bloqueios | Importar, com resolvida_em e campos. |
| historico | Linha do tempo do arquivo | Opcional. |
| D derivados (dias_ate_inicio, resumo, preco_estruturado) | Calculados | Não importar; a plataforma recalcula. |

### 4.3 Validações na entrada (o que a plataforma deve recusar)

1. versao_schema desconhecida, id diferente do nome do arquivo, ou chave obrigatória do tipo ausente.
2. Valor fora de vocabulário fechado.
3. Chave de nome de pessoa, ou texto livre que case com e-mail, telefone, CPF ou tratamento seguido de nome (as mesmas regras do C9).
4. kit.entregas com menos itens ou quantidades menores que o template do tipo (o mínimo nunca diminui).
5. Qualquer campo de texto com frase de certificação ligada ao MEC em qualquer variante (as mesmas da C10, com a exceção do ato regulatório da Graduação copiado do catálogo) ou com "últimas vagas".
6. Item com codigo que não existe no cadastro de cursos ou turmas: vai para uma lista de órfãos, nunca cria curso.
7. Divergência entre o espelho e a ficha congelada: relatório, não gravação.
8. Marcador ou null por origem vazia sem pendência que o cite em "campos" (a mesma regra da C11).

### 4.4 Pedido ao admin (texto para a pessoa do marketing levar ao CEO)

O pedido não cria nada. Ele pergunta e propõe:

1. A plataforma quer importar a camada de planejamento (classes P, K, M, N e pendências) dos JSON da squad? Se sim, o admin escreve o plano dele em docs/plans; nada disso é migration deste projeto.
2. Qual é a chave que liga o código do catálogo ao cadastro de cursos e turmas ([CONFIRMAR])?
3. Como a plataforma lê os arquivos: pelo repositório da squad (marketing-ufape, privado), por envio pelo painel ou por outro caminho ([CONFIRMAR])?
4. Quem aprova a importação e com que papel de acesso (a regra de acesso mora no Postgres, no admin).
5. Como mostrar na tela os marcadores "[CONFIRMAR]" e "[SUPOSIÇÃO]" e os null com pendência (o CLAUDE.md do admin pede "-" como marcador de vazio na tela e números reais ou marcados como ilustrativos).
6. Os JSON só levam dados de curso e planejamento, sem dado pessoal, e portanto podem passar pelo gateway de IA do admin, que só aceita dados de curso (seção 5).

---

## 5. Riscos de dado pessoal e como o esquema os evita

| # | Risco | Onde poderia aparecer | Como o esquema evita | Quem confere |
|---|---|---|---|---|
| 1 | Nome de docente, coordenador ou palestrante (a ficha e a página os listam, com titulação) | equipe, evento.palestrantes, textos livres, pendências | Não existe campo de nome de pessoa (R10). equipe e evento.palestrantes guardam só contagens. O nome continua na página, que o pega do banco. | C9 do qa |
| 2 | Imagem e voz sem autorização | kit.entregas de post por docente ou palestrante | A entrega fica "aguardando_autorizacao" até haver registro; o JSON guarda só a contagem de autorizados, não quem. Só aparece em peça quem tem autorização registrada. | C6 e C9 |
| 3 | Dado de aluno, candidato ou lead (nome, telefone, CPF, e-mail) | numeros_agregados, pendencias, historico | numeros_agregados aceita só números somados por turma. Nenhum campo recebe lista de pessoas. O cmo só lê números somados, como no agente dele. | C9 |
| 4 | Dado pessoal escondido em texto livre (o ponto mais frágil) | descricao, motivo, observacao, historico.motivo, comentário de aprovação | Texto livre limitado a 240 caracteres, sem nome (R9); comentários de aprovação da plataforma não são copiados (só ref, data e papel). Os vocabulários fechados reduzem o texto livre ao mínimo. | C9 |
| 5 | Nome de quem aprova ou aplica | aprovacoes, historico | Só o papel (pessoa_do_marketing) e o agente que aplicou (cmo). | C9 |
| 6 | Dado pessoal em link | graduacao.lp.utm, URLs | UTM só com os cinco parâmetros de campanha; nenhum valor que identifique pessoa (identificador de lead, e-mail). A UTM é gerada pela plataforma. | C9 e C4 |
| 7 | Contato de pessoa ou da equipe | texto livre | Contatos oficiais (telefone e e-mail da secretaria e das vendas) não têm campo e não são copiados. | C9 |
| 8 | Menores de idade (Graduação) | peças e canais | Nenhum campo de pessoa; a regra de cuidado com menores fica no kit e na conformidade, não no JSON. | conformidade-educacional |
| 9 | HTML mostrando algo que o esquema não prevê | HTML | O HTML só desenha chaves do esquema e escreve texto como texto. | C12 |
| 10 | Importação trazendo dado de fora do esquema | plataforma | A validação de entrada recusa chave fora do esquema e texto com padrão de dado pessoal (4.3). | plataforma |

Risco que sobra: um texto livre com nome de pessoa que o regex e a leitura do qa não pegarem. Por isso o vocabulário é fechado onde dá, o limite é de 240 caracteres e a conferência C9 roda em toda rodada. A conferência por regra (palavras como Dr., Dra., Prof., MSc, PhD) é feita por leitura do qa-de-marketing, porque os agentes só têm Read e Write [SUPOSIÇÃO: nenhum script de validação existe hoje]; um validador automático fica como sugestão para a plataforma.

---

## 6. Regras de envio no CRM pedidas pelo cmo (seção 12 do plano, versão 3)

Esta seção atende a encomenda da seção 12.10 do plano do cmo. Ela não muda o esquema JSON da seção 1: os campos abaixo são do cadastro do contato no CRM, onde já existe dado pessoal, e nunca entram no JSON do curso (R10). A squad lê só números somados. A ferramenta de CRM, e-mail e WhatsApp que vai aplicar as regras ainda não foi informada [CONFIRMAR, P15]; os números do teto são [SUPOSIÇÃO] até a Ufape confirmar (pedido R1 do cmo).

### 6.1 Campos novos no contato

| Campo | Tipo | Valores | Quem preenche | Para que serve |
|---|---|---|---|---|
| fim_janela_silencio | data ou vazio | AAAA-MM-DD. Presencial e evento: 2 dias úteis depois do último dia do curso ou evento. Online e minicurso: 7 dias corridos depois do primeiro acesso; enquanto a plataforma não informar o acesso, 7 dias corridos depois da compra (D8) [SUPOSIÇÃO de prazo] | CRM, no pedido pago (loja) | Enquanto a data de hoje for menor ou igual a fim_janela_silencio, o contato não entra em campanha nova de outra linha (P5 da Pós, convite de Livres, convite do Workshop). Régua com data em que ele já estava antes da compra continua: a janela impede entrada nova, não interrompe régua em curso |
| participou_evento_<código> | texto, um campo por evento ou edição | inscrito (pedido pago) ou presente [CONFIRMAR como a presença é medida]. O <código> é o código do catálogo; sem código, a chave de D12 (exemplo: participou_evento_neuro26 para o Workshop Brasileiro de Neuromonitorização de 20 e 21/11/2026) | CRM, a partir da loja e do credenciamento | Separa participante do Workshop nas réguas: provas M8 às 16h para participante (D3), M9 de 25/11 só para participantes (D9), supressões da semana S5 |
| vinculo_ufape | lista de texto | aluno_pos, ex_aluno_pos, comprador_livres, nenhum [SUPOSIÇÃO de nomes]; Graduação [CONFIRMAR se entra] | secretaria e loja | D10: [segmento] = ex_aluno na régua das provas quer dizer ex_aluno_pos; comprador só de Livres (comprador_livres sem aluno_pos nem ex_aluno_pos) não entra na régua das provas, salvo se também for lead de Pós com opt-in. Também marca quem pode usar o cupom SIMPNEUROMONIT (aluno e ex-aluno, com comprovação na secretaria) |

Campos de apoio que cada mensagem precisa levar na régua: tipo (servico ou campanha), prioridade (1 a 6, abaixo), data_do_item (data da turma, prova ou edição), nota_gut (seção 3 do plano do cmo) e canal (whatsapp ou email).

### 6.2 Fila de prioridade (D2) e limite diário no CRM

Antes de agendar qualquer mensagem de campanha para um contato, o CRM confere, nesta ordem:

1. **Serviço passa sempre.** Confirmação de inscrição ou compra, véspera, dia, resultado da prova (M16 a M20), gravação e certificado do Workshop (M8), acesso ao online e material do pós-curso ficam fora do teto e da fila.
2. **Dia sem campanha.** 02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço e manutenção. Para quem está na campanha das provas, também 26 e 27/11. Mensagem de campanha nesses dias é suprimida.
3. **Janela de horário.** WhatsApp em dia útil, das 9h às 18h; e-mail em qualquer dia, das 7h às 19h.
4. **Janela de silêncio.** Se hoje for menor ou igual a fim_janela_silencio e a mensagem for entrada em campanha nova de outra linha, ela é suprimida.
5. **Limite diário.** No máximo 1 mensagem de campanha por contato por dia, em qualquer canal. Se o dia já tem mensagem de campanha para o contato, a nova é suprimida; reenvio não muda de dia.
6. **Teto semanal.** Até 2 WhatsApp e 2 e-mails de campanha por contato na semana (segunda a domingo), somando Pós, Livres, Eventos, Graduação e newsletter. Livres não tem sub-teto.
7. **Disputa.** Quando duas mensagens de campanha disputam o mesmo dia ou a última vaga da semana no mesmo canal, vence a de menor número na fila D2:
   1. serviço de qualquer linha (fora do teto);
   2. toque principal de cada campanha com data (convite, programação, lembrete principal, toque do kit de turma);
   3. entre toques principais, vence o de data_do_item mais próxima; empate, vence a maior nota_gut;
   4. follow-ups e reenvios, na mesma ordem;
   5. nutrição (newsletter, rotação dos contínuos);
   6. reativação (lead frio, ex-aluno sem campanha ativa).

O que é suprimido não acumula para a semana seguinte, salvo onde a seção 12.2 do plano do cmo diz "muda de data". O CRM registra cada supressão com o motivo (dia sem campanha, horário, janela de silêncio, limite diário, teto semanal, fila), só em contagem para a squad.

### 6.3 Padrão de UTM (D11 e D12)

| Tipo de envio ou peça | utm_source | utm_medium |
|---|---|---|
| Mensagem enviada pelo CRM (régua, kit, P1 a P9, RL1 a RL10, Workshop) | whatsapp ou email | crm |
| Newsletter | email ou whatsapp | newsletter |
| Orgânico social | instagram, facebook ou youtube | organic_social |
| Pago na Meta, TikTok e LinkedIn | meta, tiktok ou linkedin | paid_social |
| Pago no Google (Busca e YouTube) | google | cpc |

- utm_medium aceita só crm, newsletter, organic_social, paid_social e cpc. Os valores base, disparo, organico e pago saem.
- utm_campaign começa pela chave do item, <linha>_<código do catálogo> (exemplos: pos_68615, livres_573, eventos_700). Sem código: pos_provas20261127, eventos_neuro26, geral_newsletter. Graduação mantém o prefixo grad_.
- CRM, newsletter e orgânico: utm_campaign = chave + _<AAAAMM do primeiro envio ou da publicação> (exemplos: pos_provas20261127_202611, eventos_neuro26_202610, geral_newsletter_202611).
- Pago: nome da campanha = chave + _<plataforma>_<objetivo>_<público>_<AAAAMM>, e utm_campaign = nome da campanha. Anúncios já no ar não são renomeados; a análise lê por tabela de correspondência.
- utm_content = ID da mensagem ou da peça (exemplos: m2-a1-anest-68639, rl1-573-t3, ed01-botao, c01).
- Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Nenhum dado pessoal em UTM (risco 6 da seção 5).
- A validação de entrada da plataforma (4.3) pode recusar utm_medium fora da lista acima [SUPOSIÇÃO de regra útil, a combinar com o admin].

---

## Mudanças desta versão

- Versão 4 (26/10/2026), propaga as decisões 7 a 13 da Ufape e a seção 12 do cmo só nos exemplos JSON antigos: 707-p05 deixa de bloquear o post por docente (autorização registrada, decisões 8 e 10) e fica só a contagem; 68651-p03 perde a turma mínima (fechada em 15, decisão 11) e fica com a contradição interna da ficha (U1); "PROVA PRESENCIAL" passa a online na normalização e no formato da prova, com a pendência 68651-p10 (U2) e o resumo do exemplo com 10 pendências abertas.

### Mudanças da versão 3

- Versão 3 (26/10/2026), pela seção 12 do plano do cmo (encomenda de 12.10) e pelos ajustes do qa. A versão 2 tinha as correções B1 a B6.
- Seção 6 nova: campos fim_janela_silencio (D8), participou_evento_<código> e vinculo_ufape (D10) no contato do CRM; fila D2, limite de 1 mensagem de campanha por contato por dia e teto semanal D1; padrão de UTM D11 e D12.
- graduacao.lp.utm passa a citar o padrão D11 e D12. Turma mínima de 15 e autorização de imagem e citação para todos registradas nas listas (decisões 8, 10 e 11); os exemplos 1.6 e 1.7 são de antes dessas decisões: no arquivo real, a pendência 707-p05 não é aberta e a 68651-p03 fecha com turma mínima de 15.
- Revisão deste documento em 03/11 (D15). Listas finais atualizadas.

---

## Fatos (com fonte)

1. O mapa HTML é um arquivo único, sem CDN, offline, sem dado pessoal, com nós do nível 0 ao 5; o JSON por item não leva nome de docente; nada vai para o banco agora e a carga futura depende de plano próprio no ufape-admin (plano do cmo, seções 6.1 e 6.2).
2. Campos da seção 6.2 do plano, incluindo versao_schema 1, fontes, kit, canais, arquivos_por_camada, metas, pendencias e aprovacoes (plano do cmo, seção 6.2).
3. Recorte de 110 itens, 72 de histórico ou pendência, 2 da Graduação, total 184 (plano do cmo, seção 2.2; catálogo, resumo).
4. Nome dos arquivos aprovado em A11, pasta saidas/10-operacoes-de-marketing/cursos/<linha>-<codigo>.json (plano do cmo, seções 6.2 e 8; briefing, decisão do cliente).
5. Decisões do cliente de 26/10/2026: Graduação com plano próprio (A2), provas de bolsa em campanha única (A3), pendências marcadas, workshop de 20 e 21/11 com cupom SIMPNEUROMONIT e 16 h (docs/execucao-2026-10-26.md).
6. Pós 707: turma VII, São Paulo, semipresencial, 600 h, início 30/10/2026 (planilha), 30x de R$ 1.590,00, R$ 47.700,00, matrícula R$ 250,00, status aberto (catálogo, seção 2); 24 módulos, turma mínima de 20, 3 coordenadores, 19 professores listados (ficha da 707).
7. Prova 68651: Hematologia, São Paulo, 27/11/2026, R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão, aberto (catálogo, seção 3, com coluna de preço); 9 às 13h, prova presencial, nota de corte 7.0 (mínimo 70 % de acerto) e mínimo de 15 alunos nas duas menções da ficha (ficha da 68651). Regras das 22 provas, iguais em todas: 11 bolsas por prova (2 de 50% (monitoria), 4 de 25% e 5 de 10%), nota de corte 7,0, resultado por WhatsApp ou e-mail, 10 dias úteis para a matrícula, turma mínima de 15 na página da prova contra 20 nas páginas de curso (fechado pela decisão 11 da Ufape: turma mínima de 15, também nas turmas de Pós; provas online), turma de destino não consta na página [CONFIRMAR] (contexto/pos-graduacao.md). O trecho REGRAS da ficha cita ainda o site como local do resultado e 7 dias para a matrícula (ficha da 68651). O plano dá P10 como resolvido (plano do cmo, seção 7).
8. Visão de campanhas de 26/10/2026: 707 com campanha ativa, estático, sem 5 ângulos; o Simpósio de Neuromonitorização com campanha ativa, estático, 5 ângulos "não se aplica"; as provas de bolsa não constam (visão de campanhas; plano, seção 3).
9. GUT: provas de bolsa 5, 5, 4 = 100; Pós 707, 68604 e 68606: 4, 5, 3 = 60 (plano, seção 3).
10. Onda 1 e situação especial das turmas com campanha ativa: inventário do kit pelo cmo em 28/10, mensagens de reta final em 28/10, plano da campanha das provas em 29/10, peças das provas em 03/11 (plano, seção 4).
11. Graduação: Medicina Veterinária, Edital 002/2026, 45 vagas no integral (4 anos) e 45 no noturno (5 anos), ingresso por redação, Enem, transferência externa, diplomado e vagas remanescentes, inscrições desde 17/08/2026, aulas em 22/02/2027, turma mínima 30 (ficha de editais). A LP da Graduação não é alterada pela squad e as peças apontam para ela com UTM da plataforma (templates/kit-de-lancamento-graduacao.md; workflow /campanha-de-vestibular).
12. Workshop de Neuromonitorização: 20 e 21/11/2026, 16 h, 30 vagas, R$ 1.250,00 presencial e R$ 450,00 transmitido e gravado (produto 68634), cupom SIMPNEUROMONIT, destino das campanhas em https://faculdade.ufape.com.br/neuro-summit/, 5 docentes confirmados (ficha do evento; catálogo, seção 9).
13. Eventos têm subtipo obrigatório (workshop ou simpósio) e cada edição é uma turma (contexto/eventos.md).
14. Os kits mínimos por tipo e suas quantidades (templates/kit-de-lancamento-*.md).
15. Auditorias existentes: auditorias/10-operacoes.md, auditorias/09-analytics.md, auditorias/conformidade-educacional.md. Agentes existentes: cmo, qa-de-marketing, relatorios, arquiteto-de-fluxos, entre os 60 (README.md; .claude/agents). Skills usadas: mapear-fluxo e matriz-gut (.claude/skills).
16. cmo, qa-de-marketing e relatorios têm as ferramentas Read e Write (cmo também WebSearch e WebFetch); nenhum tem execução de script (.claude/agents).
17. A plataforma pede aprovação depois de cada etapa e registra a entrega (CLAUDE.md do marketing, "Execução pela plataforma"). O admin é o único projeto que cria migrations e as tabelas cursos e turmas mandam nos dados de curso (CLAUDE.md do admin).
18. O veredito do qa-de-marketing pediu as correções B1 a B6 (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep09-10.md).
19. Teto único D1, fila D2, janela de silêncio D8, ex-aluno de Pós na régua das provas D10, padrão de UTM D11 e D12 e revisão no dia útil seguinte quando a segunda-feira é feriado D15 (plano do cmo, seções 12.2, 12.5, 12.7 e 12.8).
20. Autorização de imagem e citação para todos (docentes, palestrantes e convidados) e turma mínima de 15 com provas online (docs/execucao-2026-10-26.md, decisões 8, 10 e 11).

## Suposições

1. [SUPOSIÇÃO] nome_padrao dos tipos fora da Pós é igual ao nome do site, porque os contextos de Livres, Eventos e Graduação não definem padrão de nome.
2. [SUPOSIÇÃO] A carga horária da ficha da prova de bolsa (500 h) é a da Pós e não da prova; por isso carga_horaria da prova é null (não se aplica).
3. [SUPOSIÇÃO] A Pós 68608 como turma de destino da prova 68651 (mesma área; a sugestão fica marcada e vira pendência).
4. [SUPOSIÇÃO] O vínculo entre linhas da visão de campanhas e itens do catálogo é por nome, data e UF, porque a visão não tem código; o Simpósio de Neuromonitorização fica "provavel".
5. [SUPOSIÇÃO] Os navegadores em geral bloqueiam a leitura de arquivos locais a partir de uma página local, por isso os JSON são embutidos no HTML.
6. [SUPOSIÇÃO] O pedido de importação ao admin segue o rito completo do admin e o registro de aprovação da plataforma prevalece sobre aprovacoes e arquivos_por_camada do JSON.
7. [SUPOSIÇÃO] Um lote por onda cabe numa chamada do cmo; se não couber, divide-se por linha (a onda 2 tem 54 itens).
8. [SUPOSIÇÃO] O responsável pela aprovação é, por enquanto, a pessoa do marketing que fez o pedido (P12 aberto), registrada só como papel.
9. [SUPOSIÇÃO] Os canais dos exemplos são os da proposta do cmo (seção 5 do plano), não confirmados nas etapas 1.20 e 1.11.
10. [SUPOSIÇÃO] A conferência C9 (dado pessoal) é feita por leitura do qa-de-marketing, porque nenhum agente executa script.
11. [SUPOSIÇÃO] A data de revisão deste documento é 03/11/2026 (02/11 é feriado; D15), a primeira revisão semanal depois da primeira rodada.
12. [SUPOSIÇÃO] Itens da Graduação ficam na onda 1 (Graduação aparece na onda 1 do briefing, "inscrições abertas, aulas em 22/02/2027") e sem área das 14.
13. [SUPOSIÇÃO] Para a prova de bolsa, vale o texto do contexto da linha (resultado por WhatsApp ou e-mail, 10 dias úteis), já aprovado no plano, e os trechos divergentes da ficha viram pendência.
14. [SUPOSIÇÃO] Números do teto D1 e prazos da janela de silêncio D8, até a Ufape confirmar (pedido R1 do cmo); nomes dos valores de vinculo_ufape.

## Dados que faltam

1. [CONFIRMAR] Responsável pelo catálogo na Ufape ([nome, área] está vazio no catálogo): é quem dispara a atualização por mudança de catálogo.
2. [CONFIRMAR] Chave que liga o código do catálogo às tabelas cursos e turmas do admin, e como a plataforma lê os arquivos (seção 4.4).
3. [CONFIRMAR] URL da LP da Graduação (o catálogo só traz https://faculdade.ufape.com.br/graduacao) e utm_campaign da Graduação com o prefixo grad_ (o padrão D11 e D12 já está definido).
4. [CONFIRMAR] Fim das inscrições de cada turma, prova e edição (nenhum traz hoje).
5. [CONFIRMAR] Turma de destino de cada prova de bolsa (a página não traz; as 4 provas sem turma futura aberta são 68652, 68649, 68653 e 68655), (a turma mínima de 15 foi fechada pela decisão 11).
6. [CONFIRMAR] Quem aprova cada tipo de peça (P12) e o formato do id de aprovação da plataforma (campo ref_aprovacao, hoje "[CONFIRMAR]").
7. [CONFIRMAR] Termo de imagem de participantes e de alunos; a autorização de docentes, palestrantes e convidados foi registrada pelas decisões 8 e 10 (P13 fechado para eles).
8. [CONFIRMAR] Metas, verba, vagas restantes e números agregados por turma (P11).
9. [CONFIRMAR] Texto oficial de certificação da regulação (P1) e a validade do cupom e das promoções (por exemplo, 20% da Pós 341, P16).
10. [CONFIRMAR] Decisão da pessoa do marketing: nome do arquivo do workshop com "workshop" (proposto) ou "simposio" (exemplo do plano); sufixo "-mapa" nos relatórios do lote; e qual variação do kit de evento vale para o workshop de 20 e 21/11 (o plano usou a de simpósio).
11. [CONFIRMAR] Código no catálogo para itens que hoje não têm (workshop de Neuromonitorização, Simpósio Plantonista, Paciente Grave, Graduação), se a Ufape for criar.
12. [CONFIRMAR] Se "aprimoramento" fica como tipo próprio (proposto aqui, para os itens da Ufape Clínica) ou entra em livre_presencial.
13. [CONFIRMAR] Inventário do que já existe do kit de 707, 68604, 68606, 698, 68610, 68608, 573, 623 e 68614 (plano, seção 4).
14. [CONFIRMAR] Qual carga horária vale na Pedagogia (3.440 h no site, 3.640 h no edital) e as datas e textos dos editais apontados como alerta na ficha de editais.
15. [CONFIRMAR] Ferramenta de CRM, e-mail e WhatsApp que aplica a seção 6 (P15); como a presença no evento é medida; se a Graduação entra em vinculo_ufape.

## Próximo agente

qa-de-marketing: conferir esta versão corrigida (itens B1 a B6) com auditorias/10-operacoes.md e auditorias/conformidade-educacional.md, e devolver aprovado ou corrigir antes da aprovação da pessoa do marketing. Depois da aprovação, o cmo roda a etapa M.3 com o esquema da seção 1.
