# QA de marketing: Graduação 2027/1, rodada b (reconferência de A1 a A5 e revisão dos criativos)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 26/10/2026
- Status: rascunho de QA. Nada é publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 1)
  - contexto/cursos/graduacao/editais-2027-1.md
  - contexto/cursos/graduacao/graduacao-em-medicina-veterinaria.md (matriz do integral e do noturno, para conferir as disciplinas citadas nos criativos)
  - templates/kit-de-lancamento-graduacao.md
  - auditorias/02-estrategia-e-posicionamento.md, 06-geracao-de-demanda.md, 11-midia-paga.md e conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-a.md (vereditos A1 a A5)
  - Arquivos revisados:
    - A1 saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md
    - A2 saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md
    - A3 saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md
    - A4 saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md
    - A5 saidas/11-midia-paga/estrategia-de-midia-graduacao-2026-10-26.md
    - C1 saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md
- Códigos: **OK** (cumpre); **NA** (não se aplica); **PE** (pendente externo, bloqueia a peça que depender dele, não o arquivo); **FALHA** (o texto precisa mudar). Qualquer FALHA leva o arquivo a "corrigir". Linhas citadas são as da leitura de 26/10/2026.

## Resumo dos vereditos

| Arquivo | Veredito | Correções obrigatórias |
|---|---|---|
| A1 cmo | **aprovado** (segue para aprovação humana) | 0 (3 ajustes de menor peso, não bloqueiam) |
| A2 estrategia-de-campanha | **aprovado** (segue para aprovação humana) | 0 (1 ajuste de menor peso) |
| A3 estrategia-de-oferta | **corrigir** | 3 (mais 1 de menor peso) |
| A4 gestor-de-midia | **aprovado** (segue para aprovação humana) | 0 (1 ajuste de menor peso) |
| A5 estrategia-de-midia | **aprovado** (segue para aprovação humana) | 0 |
| C1 criativos-de-anuncio | **corrigir** | 6 (mais 3 de menor peso) |

"Aprovado" aqui quer dizer aprovado pelo QA para ir à aprovação humana. A tabela de aprovadores de contexto/ufape-geral.md continua vazia (G14): nenhum arquivo pode ser dado como aprovado por humano até a nomeação. Peças com ato regulatório passam também pela regulação.

---

## Parte 1. Reconferência dos itens dos vereditos A1 a A5

### A1. cmo-graduacao-2026-10-26.md

| Item do veredito A1 | Situação agora | Onde | Resultado |
|---|---|---|---|
| 1. Pilar "hospital desde o começo" sem prova | Cruzamento reescrito: "prática desde o 1º semestre" (matriz, verificada) e hospital como prova separada, só depois de [CONFIRMAR uso pela graduação e autorização, G11]. Post de captação do hospital condicionado a G11, com troca por projetos extensionistas | L110, L182, L213, L221; auditoria L346 | **Resolvido** |
| 2. Caminhos das etapas 2 a 4 com datas futuras | Tabela da seção 7 com os caminhos reais (...-2026-10-26.md) | L302 a L304 | **Resolvido** |
| 3. Noturno "não escala" | "anúncio pago do noturno bloqueado até G8 e MP4" | L110, L198, L222, L325, L364 | **Resolvido** |
| 4. "8 a 10 vezes menor" | "cerca de 7,6 (R$ 4.000,00 / R$ 525,00) a 9,5 vezes (R$ 5.000,00 / R$ 525,00)" | L140 | **Resolvido** (conta conferida: 7,62 e 9,52) |
| 5. Nome da campanha da Pedagogia | grad_pedagogia_meta_cadastro_goiania18_AAAAMM | L145 | **Resolvido** |

Ajustes de menor peso (não bloqueiam):
- L125: "presencial, à noite, com prática em escola desde o 1º semestre". A matriz prova "Prática Docente desde o 1º semestre", não que a prática ocorra em escola. Trocar por "com prática docente desde o 1º semestre", como em L261 e nos demais arquivos.
- L305: o caminho previsto da etapa 5 (criativos-de-anuncio-graduacao-2026-11-04.md) não bate com o arquivo entregue (criativos-de-anuncio-graduacao-2026-10-26.md). Atualizar, como foi feito nas etapas 2 a 4.
- L198 e L212: status dos criativos ainda "a fazer"; já foram entregues em 26/10/2026 (em QA nesta rodada).

### A2. estrategia-de-campanha-graduacao-2026-10-26.md

| Item do veredito A2 | Situação agora | Onde | Resultado |
|---|---|---|---|
| 1. Subida "em teste" sem metas numéricas | Regra 9: nenhuma campanha sobe, nem em teste, sem CPL máximo e custo por matrícula máximo numéricos e limite de gasto aprovados (MP1 e MP2); sem números em C0, 16/11 é adiada | L49, L76, L162, L214, L220, L311, L346, L348 | **Resolvido** |
| 2. Mensagem central do noturno só com percentual | "de R$ 10.000,00 por R$ 4.000,00 por mês no 1º semestre de 2027 (60% de desconto). Condições e validade no edital." | L120 | **Resolvido** |
| 3. Enem sem a condição de ingresso | "use sua nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)" em todas as ocorrências como forma de entrada | L45, L59, L114, L123, L161, L163, L171, L272, L281, L310, L312, L318 | **Resolvido** |
| 4. Hospital como prova da prática do 1º semestre | Provas separadas; hospital só depois de G11 | L118, L131, L162, L199 | **Resolvido** |
| 5. Noturno "só escala" | "anúncio pago do noturno bloqueado até G8 e MP4" | L84, L130, L187, L418 | **Resolvido** |
| 6. "responsável legal" | "representante legal" | L96, L137, L240, L260 | **Resolvido** |

Ajuste de menor peso: L424 (nota para outros donos) diz que o plano do cmo ainda indica este arquivo com data de 28/10/2026 na seção 7; o cmo já corrigiu. Remover a nota.

### A3. estrategia-de-oferta-graduacao-2026-10-26.md

| Item do veredito A3 | Situação agora | Onde | Resultado |
|---|---|---|---|
| 1. Projeto Integrador "em todos os semestres" | "Prática Docente em todos os 8 semestres; Projeto Integrador do 1º ao 7º semestre; estágio supervisionado obrigatório a partir do 6º semestre" | L209 | **Resolvido** |
| 2. Docentes com cargos | Só nome e titulação, com [CONFIRMAR autorização]; vínculo com as pós como fato geral | L134 | **Resolvido** |
| 3. Vencimento e reajuste aplicados à Pedagogia | Coluna Pedagogia com [CONFIRMAR com a Ufape: vencimento e reajuste no Edital 004/2026]; reajuste citado só para a Medicina Veterinária | L53, L64, L86, L282 | **Resolvido** |
| 4. Hospital na proposta e na promessa; percentual sem valores | Hospital fora de 1.3, 1.6 e 2.3; percentuais trocados pelas versões curtas de 0.2 | L113, L141, L158 | **Resolvido nos três pontos apontados.** Ver FALHA nova 3 abaixo (mesmo problema em 2.6, 3.3 e 3.6) |
| 5. Regras de renovação "por escrito" | "Antes de se matricular, fale com a nossa equipe sobre como funciona a renovação", com [CONFIRMAR] até a P1 | L86, L132 | **Resolvido** |
| 6. "como a lei permite" | "conforme o edital, que cita o Decreto 14.256/2025" | L95 | **Resolvido** |

Os seis itens do veredito A3 estão resolvidos. A conferência de consistência (Parte 2) encontrou três falhas novas, listadas no veredito A3.

### A4. gestor-de-midia-graduacao-2026-10-26.md

| Item do veredito A4 | Situação agora | Onde | Resultado |
|---|---|---|---|
| 1. Exceção de C0 permitia subir sem CPLmax e CPMmax | "Nenhuma campanha sobe, nem em teste, sem CPLmax e CPMmax numéricos (mesmo provisórios, cenário conservador) aprovados em MP1 e verba aprovada em MP2. Sem isso, MP11 não é pedido e a subida de 16/11/2026 é adiada" | L34, L377, L412, L425, L467, L500, L513 | **Resolvido** |
| 2. Consistência do bloqueio do noturno | Bloqueio total mantido (L75, MP8); A1 e A2 já alinhados | L75, L207, L208, L409 | **Resolvido** |

Ajuste de menor peso: as notas L472 e L473 dizem que o cmo, o estrategia-de-campanha e o estrategia-de-midia ainda usam "não escala" e ainda permitem subir em teste. Depois das correções isso não é mais verdade; atualizar as notas para "alinhado na rodada b".

### A5. estrategia-de-midia-graduacao-2026-10-26.md

| Item do veredito A5 | Situação agora | Onde | Resultado |
|---|---|---|---|
| 1. Datas do Enem 2026 como fato | Saíram dos fatos; em "Dados que faltam" como "[CONFIRMAR no calendário oficial do Inep] Datas do Enem 2026 informadas pelo orquestrador: 08 e 15/11/2026"; marcador repetido nas seções 0, 2.5 e 4 | L36, L158, L320, L323, L329, L521 | **Resolvido** |
| 2. Exceção de C0 | Mesma regra do A4 | L35, L66, L316, L322, L329, L345, L442 | **Resolvido** |
| 3. Referência errada ao contexto/graduacao.md | "seguem [CONFIRMAR] neste arquivo (seção 11) e nos pedidos ao cmo" | L489 | **Resolvido** |
| 4. Grupo "veterinária para quem trabalha" | Mantido só com confirmação do anuncios-google; texto nunca afirma emprego | L282, L448, L480, L525 | **Resolvido** |
| 5. Arredondamento dos mínimos da Pedagogia | Percentuais exatos (1,2375% e 0,4125%); 484,8 e 727,3 x CPLmax | L146, L206, L207 | **Resolvido** (conta conferida: 6 / 0,012375 = 484,85; 3 / 0,004125 = 727,27) |

---

## Parte 2. Consistência entre os cinco arquivos depois das correções

| Regra | A1 | A2 | A3 | A4 | A5 | Resultado |
|---|---|---|---|---|---|---|
| Nenhuma subida sem CPL máximo, custo por matrícula máximo e verba aprovados | OK (G3, L133, L320, L367) | OK | OK (variações dependem do gestor, L257) | OK | OK | **Consistente** |
| Noturno bloqueado (G8 e MP4) | OK | OK | **FALHA**: L154 "Anúncio pago do noturno só escala depois da correção do campo turno"; L323 e L326 citam só G8, sem MP4 | OK | OK | **Inconsistente no A3** |
| Pedagogia bloqueada (G6; A4 e A5 com MP4 e MP1) | OK | OK | OK (L197, L326) | OK | OK | **Consistente** |
| Hospital condicionado a G11 | OK | OK | OK (L109, L121, L133, L166, L177, L264) | OK (L388, L467) | OK (L247, L484) | **Consistente** |
| Enem sempre com 300 pontos quando aparece como forma de entrada | OK | OK | **FALHA**: L265 (variação V3 do G1, título "inscrição gratuita: faça a redação online quando quiser ou use sua nota do Enem", sem a condição). Menor peso: L197 e L223 ("Enem antigo vale") | OK | OK | **Inconsistente no A3** |
| Datas do Enem 2026 como [CONFIRMAR] | OK (L106, L285, L397) | OK (L176, L380) | NA (não cita) | OK (L506) | OK | **Consistente** |
| Desconto com valor cheio, valor com desconto, percentual e validade | OK | OK | **FALHA**: L184 (promessa do noturno sem "60%"), L201 (proposta de valor da Pedagogia sem "50%" e sem "Condições e validade no edital"), L228 (promessa da Pedagogia sem "50%"). Contraria a regra 1 do próprio arquivo (L32) | OK | OK | **Inconsistente no A3** |
| Nomenclatura goiania18_AAAAMM | OK | OK | NA | OK | OK | **Consistente** |
| Notas cruzadas entre arquivos | menor (L305) | menor (L424) | OK | menor (L472, L473) | OK | Desatualizadas, não bloqueiam |

---

## Parte 3. Revisão completa de criativos-de-anuncio-graduacao-2026-10-26.md

### 3.1 Conferência de dados (editais, catálogo e ficha)

| Dado no criativo | Fonte | Resultado |
|---|---|---|
| Integral: de R$ 10.000,00 por R$ 5.000,00/mês, 50%, 6 parcelas, 1º semestre de 2027 | catálogo seção 1; Edital 003/2026 | OK (L128, L175, L180 a L182, L266, L683) |
| Noturno: de R$ 10.000,00 por R$ 4.000,00/mês, 60% | idem | OK (L130, L290, L295 a L297, L381, L617, L618, L715) |
| Pedagogia: de R$ 1.050,00 por R$ 525,00/mês, 50% | catálogo; Edital 003/2026 Goiânia | OK (L132, L463, L468 a L470, L498, L754) |
| Validade só no 1º semestre de 2027; renovação semestral com comprovação; perda por atraso; sem acúmulo | Editais 003/2026 | OK nos blocos B-DESC (L128 a L132) |
| Inscrição gratuita; redação online, eliminatória, nota mínima 5,0; Enem 300 pontos, 2010 em diante | Editais 002 e 004/2026 | OK no B-ENTRADA (L134); FALHA em várias peças curtas (ver 3.3, item C-1) |
| Aulas em 22/02/2027; 80% até 2 dias antes; turma mínima 30 com devolução da 1ª parcela | editais | OK (L142) |
| Matrícula "a partir de 2 dias após o resultado" | Edital 002/2026 | OK em B-PASSOS (L144); **FALHA** na arte da fase 4 (L540: "2 dias depois do resultado") |
| Aceite do representante legal | Edital 002/2026 | OK em B-MENOR (L136); **FALHA** no cartão final dos vídeos (L567: "aceite do responsável") |
| Ato Medicina Veterinária: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) | catálogo | OK (L138, L266, L381, L685, L694, L717, L726); arte 1:1 sem a data do D.O.U. (L264, L379) não é arredondamento, o complemento traz o texto completo |
| Ato Pedagogia: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) | catálogo | OK (L140, L498, L746, L756) |
| Carga horária Medicina Veterinária 4.195 h + 75 h | catálogo | OK (L266, L381) |
| Carga horária da Pedagogia | divergente, fora de peça | **Ausente**, OK |
| Integral 4 anos; noturno 5 anos; Pedagogia noturno 4 anos; presencial | catálogo | OK |
| 1º semestre do integral: Anatomia, Práticas Hospitalares, Projeto Extensionista I | ficha da Medicina Veterinária, matriz | OK (as três disciplinas existem no 1º semestre do integral); marcado [CONFIRMAR NO CATÁLOGO] |
| 1º semestre do noturno: Práticas Hospitalares, Projeto Extensionista I | ficha, matriz do noturno | OK |
| Pedagogia: Prática Docente do 1º ao 8º; Projeto Integrador do 1º ao 7º; estágio a partir do 6º | ficha da Pedagogia (conferida no QA a) | OK (L424, L435, L644, L645) |
| Credenciamento de Goiânia | data de publicação [CONFIRMAR] | Não usado, OK (L481) |
| Nota do MEC, frase de certificação | proibido | Ausente (só na lista de ganchos cortados, L555) |
| "Últimas vagas", "vagas limitadas", contagem regressiva | proibido | Ausente (só na lista de ganchos cortados, L548) |
| Promessa de emprego ou salário | proibido | Ausente; "salário" só como negativa de busca |
| Nome de docente ou aluno | proibido nesta versão | Ausente |
| Prouni, Fies, Sisu associado à Ufape | proibido | Ausente; "sisu" só como negativa (L663 a L665) |

### 3.2 Itens específicos pedidos

| Pedido | Resultado | Nota |
|---|---|---|
| Todo dado conferido nos editais e no catálogo | OK, salvo L540 e L567 | Ver C-4 e C-5 |
| Desconto sempre com valor cheio, valor com desconto, percentual e validade | OK nos cartões (texto principal, arte, carrossel), nos B-DESC e nos RSA (título e descrição 1 fixados na posição 1, L656) | **FALHA** no título do NOT-V1 (L292, sem "de 2027") e no gancho C do INT-V1 (L171, sem valores e sem ano). Títulos "50% no 1º semestre de 2027" (L177, L465) passam porque o texto principal visível e a arte trazem os valores |
| Nenhuma nota do MEC, frase de certificação, emprego, salário, "últimas vagas" | OK | |
| Nenhum nome de docente ou aluno | OK | |
| Carga horária da Pedagogia ausente | OK | |
| Anúncios do noturno e da Pedagogia marcados como bloqueados | OK | L40, L41, L270, L300, L328, L356, L384, L386, cartões P1 a P5, L598, L611, L624, L637, L707, L737, L893, L894, seções 9.2 e 9.3 |
| Destino LP da Graduação com UTM | OK / PE | Todos os cartões com URL e UTM completas; URL base [CONFIRMAR, G13] |
| Público 18+ | OK | Regra 1.1.2; todas as personas de anúncio são 18+ |
| Sem imagem de menor sem autorização | OK | Grafismo de texto; sem criança na Pedagogia; imagem real só com autorização |
| Travessão ou meia-risca | OK | Nenhum encontrado na leitura integral [SUPOSIÇÃO: conferência visual] |
| Gancho cumprido pelo corpo | OK na maioria | **FALHA** nos ganchos que prometem entrada sem a condição: "Nota do Enem de 2010 em diante vale para entrar" (L340, L513) e o gancho da fase 3 "escolha como entrar" (L538). O corpo traz a condição, mas o gancho, sozinho, afirma algo que o edital não garante |
| Regra de subida coerente com o plano | **FALHA** | L823 ("Todas as subidas com escala") e L840 ("Bloqueia escala") deixam entender que dá para subir em teste sem MP1. O plano (A4, A5) diz: nenhuma subida, nem em teste |

### 3.3 Auditoria 11 (mídia paga), item por item

| Item | Resultado | Nota |
|---|---|---|
| Plano do gestor-de-midia aprovado, canais justificados | PE | Plano aprovado pelo QA nesta rodada; aprovação humana pendente |
| Metas de CPL e custo por matrícula escritas antes de subir | **FALHA** / PE | Valores [CONFIRMAR] aceitos, mas L823 e L840 limitam o bloqueio à "escala" (C-3) |
| Verba dentro do aprovado, com aprovador | PE | MP2; o arquivo não aloca verba |
| Nomenclatura padrão | OK | Seção 9; pedido 21 para "carrossel-1x1" |
| UTMs completas e origem no CRM | OK / PE | UTM em todos os destinos; G13 e MP10 |
| Pixel e conversões | PE | [DADO NÃO FORNECIDO] |
| Criativos aprovados na conformidade | **FALHA** | Ver 3.4 |
| Políticas das plataformas | OK | Sem atributo pessoal, sem caixa alta, sem emoji; títulos dos RSA em maiúscula inicial, aceito pelo Google |
| Nenhum público com menores; YouTube sem conteúdo infantil | OK | |
| Spark Ad ou post de docente com autorização | OK | Nenhuma pessoa; Spark Ad só com autorização |
| Relatório semanal ao cmo | NA | Começa em 23/11/2026 |
| Sem segmentação discriminatória | OK | |
| Públicos sem dado pessoal sem base legal | OK | Sem listas |
| Dados de curso conferidos no catálogo | OK / **FALHA** | L540 e L567 (C-4, C-5) |
| Destino de WhatsApp | NA | |
| Números só das exportações | OK | Nenhum número de desempenho |
| Nenhuma alteração sem humano | OK | |

### 3.4 Conformidade educacional, item por item

| Item | Resultado | Nota |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | OK | Carga horária só da Medicina Veterinária |
| Status "aberto" | OK | Os dois cursos |
| Modalidade clara | OK | Presencial em todas as peças |
| Graduação: ato do catálogo, sem antecipar | OK / PE | Regulação aprova (INT-V4, NOT-V4, P4, descrição 3 das RSA) |
| Pós lato sensu | NA | |
| Curso livre | NA | |
| Nota MEC só com fonte | OK | Nenhuma |
| Sem promessa de emprego, salário, concurso ou sucesso | **FALHA** | "Entre com a nota do Enem" (L233, L521), "vale para entrar" (L340, L351, L353, L513, L524, L526) e "escolha como entrar" / "Entre por nota ou redação" (L538) insinuam entrada garantida pela nota, sem a média mínima de 300 pontos (C-1, C-2) |
| Empregabilidade com fonte | NA | |
| Superlativos com fonte | OK | Nenhum; "maior desconto da linha" só na justificativa interna (L117, L278) |
| Comparação com concorrente | OK | Nenhuma em peça |
| Preço completo, sem esconder taxa ou reajuste | OK / PE | Sem taxa de matrícula no edital; reajuste [CONFIRMAR, G12] com ciclo extra (L109) |
| Desconto com regra, público e validade | **FALHA** pontual | NOT-V1 título (L292) sem "de 2027"; INT-V1 gancho C (L171) sem valores e sem ano (C-6) |
| Urgência real | OK | |
| Prouni, Fies, financiamento | OK | Ausentes |
| Autorização de imagem e depoimento | OK / PE | Nenhuma pessoa; locução e trilha [CONFIRMAR] |
| Menores só com autorização | OK | |
| Formulário com finalidade e política de privacidade | PE | G13 |
| WhatsApp e e-mail com consentimento | NA | Sem campanha de mensagem |
| Nenhum dado pessoal | OK | |
| Políticas Meta e Google, sem segmentação discriminatória | OK | |
| Página de destino entrega o prometido | PE | Integral G13; noturno G8; Pedagogia G6 |
| Texto não afirma característica pessoal | OK | "Para quem quer..." em vez de "Você trabalha...?" |
| Sem escassez falsa, contador, botão falso | OK | |
| Sem pessoa pública ou parceria inexistente | OK | |
| Sem caixa alta excessiva ou símbolos | OK | |
| Página carrega, domínio, dados da Ufape, política | PE | G13 e checklist 4.8 do gestor |
| Sem sugestão de driblar análise | OK | |

---

## Vereditos

### Veredito A1: **aprovado** (segue para aprovação humana)

Os 5 itens do veredito A1 estão resolvidos. Ajustes de menor peso, que podem entrar na próxima versão sem nova rodada de QA: L125 ("prática em escola" por "prática docente"); L305 (caminho real do arquivo de criativos); L198 e L212 (status dos criativos).

### Veredito A2: **aprovado** (segue para aprovação humana)

Os 6 itens do veredito A2 estão resolvidos. Ajuste de menor peso: remover a nota desatualizada de L424.

### Veredito A3: **corrigir** (volta para o estrategia-de-oferta)

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| 1 | Seção 2.2, L154; seção 7, L323 e L326 | Noturno "só escala depois da correção do campo turno" e bloqueio citado só com G8, contra o bloqueio total do A1, A2, A4 e A5 | "Anúncio pago do noturno bloqueado até G8 e MP4." Em L323 e L326, acrescentar MP4 |
| 2 | Seção 5, variação V3 do G1, L265 | "use sua nota do Enem" sem a condição de ingresso; é o título que deu origem ao conceito v3-entrada | "inscrição gratuita: faça a redação online quando quiser ou use sua nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)" |
| 3 | Seção 2.6, L184; seção 3.3, L201; seção 3.6, L228 | Desconto sem percentual (L184, L201, L228) e sem "Condições e validade no edital" (L201), contra a regra 1 do próprio arquivo (L32) | Usar as versões curtas da seção 0.2: "de R$ 10.000,00 por R$ 4.000,00/mês no 1º semestre de 2027 (60%). Condições e validade no edital."; "de R$ 1.050,00 por R$ 525,00/mês no 1º semestre de 2027 (50%). Condições e validade no edital." |
| 4 (menor peso) | L197 e L223 | "Enem" e "Enem antigo vale" sem a condição | Acrescentar "(média mínima de 300 pontos, edições de 2010 em diante)" |

### Veredito A4: **aprovado** (segue para aprovação humana)

Os 2 itens do veredito A4 estão resolvidos. Ajuste de menor peso: atualizar as notas de L472 e L473, que descrevem inconsistências já corrigidas no A1, A2 e A5.

### Veredito A5: **aprovado** (segue para aprovação humana)

Os 5 itens do veredito A5 estão resolvidos, sem ajuste pendente.

### Veredito C1 criativos-de-anuncio: **corrigir** (volta para o criativos-de-anuncio)

| # | Onde | Problema | Correção proposta |
|---|---|---|---|
| C-1 | Enem sem a média mínima de 300 pontos em peça que circula sozinha: INT-V4 carrossel cartão 3 (L266); NOT-V2 carrossel cartão 5 (L325); P1 carrossel cartão 5 (L413); P4 carrossel cartão 3 (L498); R-P1 cena 3, fala e texto (L632); RSA-INT-v1 descrição 2 (L684); RSA-PED-p1 descrição 2 (L745); títulos de Enem das RSA-INT-v3 e RSA-NOT-v3 sem fixação (L700, L732); título NOT-V3 "Veterinária noturno com Enem" (L348) | O Enem aparece como forma de entrada sem a condição do edital (regra 4 do próprio arquivo, L52, e regra 5 do A2) | Em cartão, cena e descrição: "nota do Enem (média mínima de 300 pontos, edições de 2010 em diante)". Nas RSA-v3: fixar a descrição 1 na posição 1 e o título "Enem com Média Mínima de 300" na posição 2. Título NOT-V3: por exemplo "Enem 2010+ com média mínima 300" (conferir o limite no gerenciador) |
| C-2 | Ganchos que afirmam entrada: título "Entre com a nota do Enem" (INT-V3, L233; P5, L521); gancho A "Nota do Enem de 2010 em diante vale para entrar" (NOT-V3, L340, arte L351, carrossel L353; P5, L513, arte L524, carrossel L526); troca da fase 3 (L538: gancho "escolha como entrar", título "Entre por nota ou redação", arte "Nota do Enem ou redação online") | Insinuam entrada garantida e omitem a condição; o QA a pediu trocar "entre com sua nota" por "use sua nota" | Títulos: "Use sua nota do Enem". Gancho A: "Com média mínima de 300 pontos, a nota do Enem de 2010 em diante pode ser usada para concorrer." Fase 3: gancho "Nota do Enem (média mínima de 300 pontos) ou redação online: veja como se inscrever", título "Nota do Enem ou redação", arte com a linha "Média mínima de 300 pontos, edições de 2010 em diante" |
| C-3 | Lista de aprovações, item 15 (L823: "Todas as subidas com escala"); auditoria 7.1 (L840: "Bloqueia escala") | Contraria a regra do A4 e do A5: nenhuma subida, nem em teste, sem CPLmax e CPMmax numéricos aprovados em MP1 e verba em MP2 | L823: "Todas as subidas, inclusive em teste". L840: "Bloqueia qualquer subida, inclusive em teste" |
| C-4 | Troca de texto da fase 4, arte (L540) | "Matrícula eletrônica, 2 dias depois do resultado"; o edital diz "a partir de dois dias após" | "Matrícula eletrônica a partir de 2 dias depois do resultado" |
| C-5 | Padrão dos roteiros, cartão final (L567) | "aceite do responsável"; o edital e o B-MENOR usam "representante legal" | "Menor de idade: aceite do representante legal na inscrição e na matrícula" |
| C-6 | NOT-V1, título (L292); INT-V1, gancho C de reserva (L171) | Título sem "de 2027" (regra 3 do arquivo, L51); gancho C "Metade do preço no 1º semestre" sem valores e sem ano | Título: "Noturno: 60% no 1º sem. de 2027" ou "60% no 1º semestre de 2027" (conferir o limite). Gancho C: "De R$ 10.000,00 por R$ 5.000,00: metade no 1º semestre de 2027" |
| C-7 (menor peso) | L35 e L883 | "9 anúncios responsivos"; o arquivo tem 8 (3 integral, 3 noturno, 2 Pedagogia, L39 a L41) | Trocar por 8 |
| C-8 (menor peso) | L49, L762, L842 | Remetem à "seção 10", que não existe; destinos e nomes estão na seção 9 | Trocar por "seção 9" |
| C-9 (menor peso) | Lista 1, L964 | "perda por atraso (dia 10)" atribuída aos Editais 003/2026 das duas praças; o vencimento no dia 10 vem do Edital 002/2026 (SP) e, na Pedagogia, é [CONFIRMAR] | "perda por atraso (vencimento no dia 10 na Medicina Veterinária, Edital 002/2026; Pedagogia [CONFIRMAR])". Nenhuma peça cita o dia 10, então não afeta os textos |

O que está bom e não muda: blocos B-DESC, B-ATO, B-COND, B-PASSOS e B-MENOR; todos os cartões de preço com valor cheio, valor com desconto, percentual e validade; fixação do desconto nas RSA; bloqueio do noturno e da Pedagogia; ausência de carga horária da Pedagogia, de docentes, de hospital e de menores; UTM em todos os destinos; teste de similaridade; ganchos cortados.

---

## Encaminhamento

- A1, A2, A4 e A5: **seguem para a aprovação humana** (pessoa do marketing; peças com ato também pela regulação). Os ajustes de menor peso podem entrar junto, sem nova rodada.
- A3: **volta para o estrategia-de-oferta**, com as 3 correções obrigatórias. Depois, conferência só desses pontos.
- C1: **volta para o criativos-de-anuncio**, com as 6 correções obrigatórias. Depois, conferência só desses pontos (arquivo ...-c). Nenhum criativo vai para montagem antes disso, e nenhum sobe sem MP1, MP2, MP4 e EM1.
- Nota ao cmo: os criativos saíram com data de 26/10/2026, não de 04/11/2026 como prevê a seção 7 do plano.

---

## Fatos (com fonte)

- Preços, percentuais, validade, renovação, perda por atraso, vagas, turma mínima, cancelamento com 80%, aulas em 22/02/2027 e Enem com média mínima de 300 pontos, edições de 2010 em diante (catálogo seção 1; contexto/cursos/graduacao/editais-2027-1.md).
- Matrícula eletrônica "a partir de dois dias após a publicação do resultado"; candidato menor precisa do aceite do "representante legal" (Edital 002/2026, na ficha dos editais).
- Vencimento no dia 10 e reajuste de dezembro constam do Edital 002/2026 (SP); a ficha não os lista para o Edital 004/2026.
- Matriz da Medicina Veterinária: 1º semestre do integral com Anatomia, Práticas Hospitalares e Projeto Extensionista I; 1º semestre do noturno com Anatomia I, Práticas Hospitalares e Projeto Extensionista I (ficha da Medicina Veterinária).
- Matriz da Pedagogia: Prática Docente do 1º ao 8º; Projeto Integrador do 1º ao 7º; estágio a partir do 6º (QA a, a partir da ficha da Pedagogia).
- Atos: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025); Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) (catálogo).
- Tabela de aprovadores vazia (contexto/ufape-geral.md).

## Suposições

- [SUPOSIÇÃO] A conferência de travessão e meia-risca nos seis arquivos foi visual, na leitura integral; nenhum foi encontrado.
- [SUPOSIÇÃO] Títulos de Meta com percentual ("50% no 1º semestre de 2027") são vistos junto do texto principal ou da arte, que trazem os valores; por isso não foram tratados como falha.
- [SUPOSIÇÃO] "vale para entrar" e "Entre com a nota" seriam lidos pelo público como entrada garantida; por isso viraram correção obrigatória.
- [SUPOSIÇÃO] Os ajustes de menor peso de A1, A2 e A4 não mudam conteúdo de peça e podem seguir sem nova rodada de QA.

## Dados que faltam

- [CONFIRMAR] CPLmax, CPMmax, verba e aprovador por recorte (MP1, MP2, G3), antes de qualquer subida, inclusive em teste.
- [CONFIRMAR] URL da LP que recebe a UTM, formulário (inscrição ou captura), origem no CRM e política de privacidade (G13).
- [CONFIRMAR] Correção das páginas do noturno (G8) e da Pedagogia (G6); públicos 18+ (MP4); divisão por curso (EM1).
- [CONFIRMAR NO CATÁLOGO] Nomes das disciplinas do 1º semestre como dado de catálogo; carga horária, coordenação e corpo docente da Pedagogia; horário de prática e estágio do noturno.
- [CONFIRMAR] Vencimento e reajuste da Pedagogia no Edital 004/2026; efeito do reajuste de dezembro (G12).
- [CONFIRMAR no calendário oficial do Inep] Datas do Enem 2026, da divulgação das notas e do resultado do Sisu.
- [CONFIRMAR] Uso da Ufape Clínica pela graduação e autorizações de imagem (G11); voz da locução, trilha, paleta e logotipo.
- [CONFIRMAR] Aprovadores por tipo de peça (G14).
