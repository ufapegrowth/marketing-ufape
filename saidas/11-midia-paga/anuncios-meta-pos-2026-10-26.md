# Estrutura de Meta Ads da Pós-graduação: turmas de março e abril de 2027 (2 campanhas por turma, verba em reais), com a montagem das provas suspensa (etapa 1.14)

- **Agente:** anuncios-meta (departamento 11 Mídia Paga, por encomenda do gestor-de-midia e da estrategia-de-midia-pos v4)
- **Linha:** pos
- **Data:** 26/10/2026 (rodada); versão 3 em 27/10/2026
- **Versão:** 3. Substitui a versão 2 (26/10/2026, corrigida pelo qa-de-marketing-geral-2026-10-26-loteD). A versão 2 montava as provas de bolsa, o pós-prova e as turmas com verba em percentual da verba nova (VN). Esta versão monta só as turmas de março e abril, por turma, em reais, e guarda a montagem das provas na seção 13, marcada "suspenso (decisão 14)". O que mudou está em "Mudanças desta versão", no fim.
- **Etapa:** 1.14 da camada 1 do plano do cmo; encomenda da seção 7 da estrategia-de-midia-pos v4 (linha anuncios-meta) e da seção 12.8 do gestor-de-midia-pos v5. Prazos: março até 30/11/2026; abril até 30/12/2026.
- **Status:** rascunho para o qa-de-marketing (auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda linha de montagem, troca de diária e pausa é pedido para um humano executar no Gerenciador de Anúncios, depois da aprovação (seção 12).
- **Entradas lidas:**
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 17; nesta versão pesam 8, 10, 11, 12, 14, 15, 16 e 17)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 7, 8 e 12; D11 e D12; seção 13 não muda nada aqui, porque trata do teto de mensagens)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (versão 5, seções 12.1 a 12.8)
  - /home/user/marketing-ufape/saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 4: seções 2, 3, 4, 6, 7 e 8; entrada principal)
  - /home/user/marketing-ufape/saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md (versão 3, aprovada: peças c1 a c3, r1 e r2 das 14 turmas, nomes, URL e UTM)
  - /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-meta-pos-2026-10-26.md (versão 2, base da seção 13)
  - /home/user/marketing-ufape/.claude/skills/estrutura-de-campanha-paga/SKILL.md
  - /home/user/marketing-ufape/auditorias/11-midia-paga.md e /home/user/marketing-ufape/auditorias/conformidade-educacional.md
  - /home/user/marketing-ufape/contexto/ufape-geral.md, /home/user/marketing-ufape/contexto/pos-graduacao.md e /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seção 2)
  - /home/user/marketing-ufape/docs/visao-de-campanhas-2026-10-26.md (situação atual das campanhas de 289 e 662 e das turmas de março e abril)
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web nesta etapa.
- **Dados pessoais:** nenhum. Nenhum aluno, candidato ou lead é citado. Docentes não são nomeados aqui; os anúncios de docente (c3) usam o texto aprovado do criativos v3, com nome e titulação como na ficha (decisões 8 e 10).
- **Marcadores:** [CONFIRMAR] é fato ou número que a Ufape ou o gerenciador precisa informar. [CONFIRMAR NO CATÁLOGO] é dado de curso fora do catálogo. [SUPOSIÇÃO] é escolha de desenho ou regra de plataforma sem fonte nos arquivos (toda regra de política ou de recurso da Meta que não vem de um arquivo do repositório está marcada assim). [DADO NÃO FORNECIDO] é número de mídia que não existe nos arquivos. Nenhum gasto, CPL, CTR, lead, inscrição ou matrícula observado existe nos arquivos. Verba (R$ 2.000,00 por turma) e meta (15 matrículas) vêm do CEO (decisões 15 e 16). Os CPL máximos de R$ 4,00, R$ 10,00 e R$ 18,00 vêm de taxas [SUPOSIÇÃO ilustrativa] do gestor.

---

## 0. Resumo em cinco linhas

1. Estrutura: por turma, 2 campanhas Meta (frio `amplo18` da praça e remarketing `rmk30d`), 1 conjunto em cada, orçamento na campanha, evento de otimização lead; 14 turmas (5 de março, 9 de abril), 28 campanhas e 70 anúncios (42 no frio, 28 no remarketing), todos ligados às peças aprovadas do criativos v3. A Busca do Google é do anuncios-google.
2. Verba da Meta: março R$ 1.295,00 por turma (frio R$ 787,00, remarketing R$ 508,00) e abril R$ 1.325,00 (frio R$ 865,00, remarketing R$ 460,00), R$ 18.400,00 no total dos R$ 28.000,00; diárias por fase na seção 5, trocas em 21/12, 04/01 e 25/01, pausa no dia seguinte ao corte (EM16).
3. Anúncios: 3 no frio, prontos para o rodízio (pausar, nunca apagar), e 2 no remarketing; nenhum texto com preço, valor de inscrição, bolsa ou prova (decisões 14 e 16, U11); nomes e UTM no padrão D11 e D12, com a chave `pos_<código>-<área>` da estratégia v4.
4. 289 e 662: campanha atual sem renomear, gasto informado e limite de R$ 500,00 até a véspera da estrutura nova, diárias recalculadas em 30/11 e 30/12 (seção 7); gasto e diária atuais são [DADO NÃO FORNECIDO].
5. Travas de subida: P3 de 679, 68636 e 662; P4 de 366; U10 de 657; PP7 de 657 e 341; URL de 68617; c3 de 662 (seção 8). Doze pedidos de aprovação (AMP13 a AMP24). A montagem das provas fica suspensa na seção 13.

---

## 1. Regras que valem para toda a montagem

| Regra | Valor nesta montagem | Fonte |
|---|---|---|
| Verba | R$ 2.000,00 por turma no ciclo, somando Meta e Google, da subida até o corte da 1ª mensalidade. Nada passa de uma turma para outra sem nova decisão do CEO. Pagamento só com aprovação humana | decisão 15; estrategia 3.1; gestor 12.5 |
| Parte da Meta | Março R$ 1.295,00 por turma; abril R$ 1.325,00 por turma. Google: R$ 705,00 e R$ 675,00 (anuncios-google) | gestor 12.5; estrategia 3.3 e 3.4 |
| Metas de custo (escritas antes de subir) | Custo máximo por matrícula R$ 133,33. CPL máximo R$ 4,00 (conservador, meta de corte), R$ 10,00 (base), R$ 18,00 (otimista). Custo máximo por inscrição R$ 80,00, R$ 100,00 e R$ 120,00. Taxas de lead para inscrição e de inscrição para matrícula são [SUPOSIÇÃO ilustrativa] do gestor | estrategia 2.2; gestor 12.3 |
| Preço e inscrição | Nenhum texto, título, descrição ou arte mostra preço (parcela, total ou matrícula) nem o valor da inscrição (R$ 260,00, R$ 250,00 ou R$ 350,00) até a resposta da U11. O investimento completo fica na página da turma. Só o remarketing usa a frase "Veja parcelas, total e matrícula na página da turma", nas 4 condições do AP7 | decisão 16; criativos 1.1 e 1.2 |
| Fora desta rodada | Provas de bolsa, bolsa, pós-prova, Cursos Livres, YouTube, LinkedIn, TikTok, WhatsApp como destino, Performance Max e Display | decisão 14; gestor 12.6 |
| Certificação e MEC | Nenhuma frase de certificação, nenhuma menção ao MEC, nenhuma nota | conformidade; criativos 1.1 |
| Urgência | Nenhum "últimas vagas", "vagas limitadas", contador ou "termina hoje". O único fato de tempo é a data de início da planilha | conformidade; criativos 1.1 |
| Quem vê | Nenhum texto afirma ou insinua característica pessoal de quem vê. Público 18+; nenhuma exclusão por idade (acima de 18), gênero, renda, emprego, saúde, religião ou origem | conformidade; estrategia 4.1 |
| Listas de contatos | Nenhuma lista de alunos, ex-alunos, leads ou inscritos até a Ufape confirmar a base legal (LGPD). Só pixel e engajamento | estrategia 4.1 |
| Destino | Sempre a página da turma, com UTM. Nunca WhatsApp. Nunca formulário instantâneo (seção 10). Página com link trocado não recebe anúncio | gestor 3; criativos 1.4 |
| Nomes | Campanha = `pos_<código>-<área curta>_meta_lead_<público>_<AAAAMM da subida>`; conjunto = nome da campanha + `__` + público; anúncio = `<código>-<conceito>_<formato>_<gancho>_vN` (nome do criativos v3). Minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos | D12; estrategia 4.2 |
| UTM | `utm_source=meta`, `utm_medium=paid_social`, `utm_campaign` = nome da campanha, `utm_content` = nome do anúncio, `utm_term` = público. Nenhum dado pessoal | D11 e D12; estrategia 4.3 |
| Campanhas já no ar ou pausadas | 289 e 662 (ativas) e as campanhas antigas pausadas das turmas deste plano não são renomeadas nem apagadas; a análise lê por tabela de correspondência (analise-de-midia) | D12, último item |
| Sobreposição | Sem exclusão de público entre campanhas de turmas diferentes e sem anúncio que misture ofertas. Registro lado a lado de CPM, alcance e frequência (EA3). Turmas da mesma área (68615 e 333; 289 e 657) podem disputar o mesmo público [SUPOSIÇÃO do criativos 2.3] | cmo 12.6; criativos 2.3 |
| Execução | Só humano, depois da aprovação. Esta squad não sobe, altera, pausa nem aumenta verba | CLAUDE.md |

**Nota de nomes (chave da campanha).** O D12 do cmo exige que o `utm_campaign` comece pela chave `<linha>_<código>` (exemplo `pos_68615`). A estratégia v4 (4.2) e o criativos v3, aprovado, acrescentam a área curta à chave (`pos_68615-patclin`), que continua começando por `pos_68615`. Esta versão segue a estratégia v4 e o criativos v3, para os nomes e as UTM dos 70 anúncios coincidirem com o que foi aprovado. A versão 2 deste arquivo usava a chave só com o código; a análise lê as duas pela parte `pos_<código>`. Confirmar com o cmo que a chave com área curta cumpre o D12 [CONFIRMAR, AMP13].

---

## 2. Modelo de estrutura (skill estrutura-de-campanha-paga, passo 2)

| Frente | Modelo | Motivo |
|---|---|---|
| Turmas de março (5) e de abril (9) | Lançamento por fases, por turma: 1 campanha de público frio e 1 de remarketing, cada uma com 1 conjunto e orçamento na campanha | Há data de início por turma, fases com verba escrita (aquecimento, manutenção de fim de ano, conversão) e verba de R$ 2.000,00 por turma. Separar frio e remarketing deixa a manutenção desligar só o frio, sem mexer no remarketing (EM3, PP10). Uma campanha de teste e uma de escala separadas não cabem em verba tão pequena: o teste dos 3 conceitos é o rodízio dentro do frio |

**Orçamento na campanha, nunca no conjunto.** Cada campanha tem 1 conjunto; a meta e a verba são por turma e o código da turma vai no nome. As diárias mudam por fase nas datas da seção 5, sempre por humano. Orçamento nos dois níveis seria sobreposição.

**Volume.** A estrutura é a menor possível sem diminuir o kit mínimo (3 conceitos no frio, 2 peças no remarketing). Os limites de volume da tabela 3.6 da estratégia (fonte única) estão copiados na seção 5.2; no papel, os CPL máximos de R$ 4,00 a R$ 18,00 ficam abaixo de todos eles. O gestor (12.6) estima que cada turma gere de 11 a 18 leads por semana na Meta, longe das cerca de 50 conversões por semana que a plataforma usa para sair do aprendizado [SUPOSIÇÃO do gestor]. Por isso nenhuma promessa de sair do aprendizado, de prazo ou de resultado entra neste arquivo, e a campanha pode ficar em "aprendizado limitado" [SUPOSIÇÃO de plataforma].

---

## 3. Mapa das campanhas (campanha, conjunto, anúncio)

### 3.1 Árvore padrão (por turma)

```
pos_<código>-<área>_meta_lead_amplo18-<sp|go>_<AAAAMM>          (orçamento na campanha)
└── pos_<código>-<área>_meta_lead_amplo18-<sp|go>_<AAAAMM>__amplo18-<sp|go>
      <código>-c1-...   (+ arte 9:16 anexa, quando houver)
      <código>-c2-...
      <código>-c3-...
pos_<código>-<área>_meta_lead_rmk30d_<AAAAMM>                    (orçamento na campanha)
└── pos_<código>-<área>_meta_lead_rmk30d_<AAAAMM>__rmk30d
      <código>-r1-...
      <código>-r2-...   (+ arte 9:16 anexa)
```

AAAAMM é o mês da subida (D12): 202612 em março e 202701 em abril. Turma que sobe atrasada por correção de página (679, 68636, 366 e 662) usa o mês em que realmente subir (por exemplo 202702); o nome do anúncio não muda. A Meta fria de março, pausada na manutenção, volta em 04/01 como a mesma campanha, com o mesmo nome e a mesma UTM.

### 3.2 Nomes das campanhas, por turma

| Onda | Turma | Praça | Campanha frio | Campanha remarketing |
|---|---|---|---|---|
| Março | 68615 Pós-graduação em Patologia Clínica | São Paulo | pos_68615-patclin_meta_lead_amplo18-sp_202612 | pos_68615-patclin_meta_lead_rmk30d_202612 |
| Março | 289 Pós-graduação em Cardiologia Veterinária | Goiânia | pos_289-cardio-go_meta_lead_amplo18-go_202612 | pos_289-cardio-go_meta_lead_rmk30d_202612 |
| Março | 333 Pós-graduação em Citopatologia Veterinária | São Paulo | pos_333-citopato_meta_lead_amplo18-sp_202612 | pos_333-citopato_meta_lead_rmk30d_202612 |
| Março | 657 Pós-graduação em Anestesiologia Avançada | São Paulo | pos_657-anest-avancada_meta_lead_amplo18-sp_202612 | pos_657-anest-avancada_meta_lead_rmk30d_202612 |
| Março | 341 Pós-graduação em Medicina Interna Equina | São Paulo | pos_341-equina_meta_lead_amplo18-sp_202612 | pos_341-equina_meta_lead_rmk30d_202612 |
| Abril | 68635 Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | São Paulo | pos_68635-clinmed-emerg_meta_lead_amplo18-sp_202701 | pos_68635-clinmed-emerg_meta_lead_rmk30d_202701 |
| Abril | 68636 Pós-graduação em Pneumologia Veterinária | São Paulo | pos_68636-pneumo_meta_lead_amplo18-sp_202701 | pos_68636-pneumo_meta_lead_rmk30d_202701 |
| Abril | 68617 Pós-graduação em Endocrinologia de Pequenos Animais | São Paulo | pos_68617-endocrino_meta_lead_amplo18-sp_202701 | pos_68617-endocrino_meta_lead_rmk30d_202701 |
| Abril | 68628 Pós-graduação em Oncologia Veterinária | São Paulo | pos_68628-onco_meta_lead_amplo18-sp_202701 | pos_68628-onco_meta_lead_rmk30d_202701 |
| Abril | 68609 Pós-graduação em Anestesiologia Veterinária | Goiânia | pos_68609-anest-go_meta_lead_amplo18-go_202701 | pos_68609-anest-go_meta_lead_rmk30d_202701 |
| Abril | 68632 Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Goiânia | pos_68632-cirurgia-go_meta_lead_amplo18-go_202701 | pos_68632-cirurgia-go_meta_lead_rmk30d_202701 |
| Abril | 679 Pós-graduação em Infectologia Veterinária | São Paulo | pos_679-infecto_meta_lead_amplo18-sp_202701 | pos_679-infecto_meta_lead_rmk30d_202701 |
| Abril | 366 Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | São Paulo | pos_366-fisio_meta_lead_amplo18-sp_202701 | pos_366-fisio_meta_lead_rmk30d_202701 |
| Abril | 662 Pós-graduação em Ortopedia Veterinária | São Paulo | pos_662-orto_meta_lead_amplo18-sp_202701 | pos_662-orto_meta_lead_rmk30d_202701 |

Conjunto de cada campanha: nome da campanha + `__amplo18-sp`, `__amplo18-go` ou `__rmk30d`. Nomes de turma e praça: catálogo, seção 2. 68628 e 68617 sem número de turma e 662 sem número de turma em qualquer peça (P5).

### 3.3 Datas, corte e subida

Corte = vencimento da 1ª mensalidade, 30 dias antes do início [SUPOSIÇÃO por turma, da estratégia 2.3; CONFIRMAR na ficha]. Todo o resto desta tabela vem da estratégia v4 (2.3 e 6.1). O pedido de pausa é o dia seguinte ao corte (EM16).

| Turma | Praça | Início (catálogo) | Corte [SUPOSIÇÃO] | Subida (humano) | Conversão | Pedido de pausa |
|---|---|---|---|---|---|---|
| 68615 | SP | 20/03/2027 | 18/02/2027 | 07/12/2026 | 04/01 a 18/02 | 19/02/2027 |
| 289 | GO | 20/03/2027 | 18/02/2027 | 07/12/2026 (estrutura nova; campanha atual já ativa, seção 7) | 04/01 a 18/02 | 19/02/2027 |
| 333 | SP | 27/03/2027 | 25/02/2027 | 07/12/2026 | 04/01 a 25/02 | 26/02/2027 |
| 657 | SP | 13/03/2027 | 11/02/2027 | 14/12/2026, só com PP7 e U10 | 04/01 a 11/02 | 12/02/2027 |
| 341 | SP | 20/03/2027 | 18/02/2027 | 14/12/2026, só com PP7 | 04/01 a 18/02 | 19/02/2027 |
| 679 | SP | 03/04/2027 | 04/03/2027 | 06/01/2027, só com link corrigido (P3) | 25/01 a 04/03 | 05/03/2027 |
| 68632 | GO | 10/04/2027 | 11/03/2027 | 06/01/2027 | 25/01 a 11/03 | 12/03/2027 |
| 68635 | SP | 10/04/2027 | 11/03/2027 | 06/01/2027 | 25/01 a 11/03 | 12/03/2027 |
| 366 | SP | 10/04/2027 (planilha) | 11/03/2027 | 06/01/2027, só com data conferida (P4) | 25/01 a 11/03 | 12/03/2027 |
| 68628 | SP | 10/04/2027 | 11/03/2027 | 06/01/2027 | 25/01 a 11/03 | 12/03/2027 |
| 68617 | SP | 17/04/2027 | 18/03/2027 | 06/01/2027, só com a URL conferida | 25/01 a 18/03 | 19/03/2027 |
| 68636 | SP | 17/04/2027 [CONFIRMAR na planilha] | 18/03/2027 | 06/01/2027, só com data conferida (P3) | 25/01 a 18/03 | 19/03/2027 |
| 68609 | GO | 24/04/2027 | 25/03/2027 | 06/01/2027 | 25/01 a 25/03 | 26/03/2027 |
| 662 | SP | 24/04/2027 (planilha) | 25/03/2027 | 06/01/2027, só com link corrigido (P3); campanha atual já ativa (seção 7) | 25/01 a 25/03 | 26/03/2027 |

Ordem de liberação de março: 68615, 289, 333, depois 657 e 341 (PP7). Se o corte mudar na ficha, as datas de pausa e as semanas da conversão são recalculadas numa nova versão, escrita antes da subida.

---

## 4. Configuração das campanhas e dos conjuntos

### 4.1 Campos comuns (as duas campanhas de cada turma)

| Campo | Valor | Marcação |
|---|---|---|
| Objetivo | Cadastros (leads), com local de conversão no site. Se o teste de rastreio de 30/10 mostrar que a página só registra início de checkout, objetivo Vendas com esse evento | [SUPOSIÇÃO de nome e de disponibilidade do objetivo; conferir no gerenciador]; resultado do teste [CONFIRMAR] |
| Evento de otimização | Lead (cadastro), se a página da turma o registrar; senão início de checkout (EM11). O nome da campanha leva `lead` nos dois casos (D12: objetivo de captação) | pixel e API de Conversões, testados em 30/10 |
| Conversões só para leitura | Inscrição paga e 1ª mensalidade paga, registradas como conversões separadas (por exemplo eventos `inscricao_paga` e `mensalidade1_paga`) e lidas no CRM, somadas por turma. Não otimizam: 17 a 25 inscrições no ciclo inteiro não dão volume ao algoritmo (gestor 12.6) | nomes dos eventos [SUPOSIÇÃO]; envio a partir do CRM depende do arquiteto-de-fluxos [CONFIRMAR] |
| Categoria especial de anúncio | Nenhuma | [SUPOSIÇÃO: educação não é categoria especial da Meta; conferir ao criar] |
| Orçamento | Diário, na campanha, nos valores da seção 5. Nunca no conjunto | decisão de desenho (seção 2) |
| Lance | Menor custo (padrão), sem teto de custo na plataforma. Os limites de CPL são lidos por humano (seção 9) | [SUPOSIÇÃO de desenho: com diárias de R$ 3,68 a R$ 40,00, um teto de custo pode zerar a entrega] |
| Programação | Contínua, sem data de término. A pausa é pedido no dia seguinte ao corte (EM16). Trava de segurança: limite de gasto da campanha igual ao total da campanha na turma (seção 5.1), se o recurso existir | [SUPOSIÇÃO de recurso; AMP24] |
| Idade e gênero | 18 anos ou mais, sem máximo; todos os gêneros | estratégia 4.1 |
| Público frio | Amplo da praça, com sugestão de interesses profissionais ligados à medicina veterinária; o criativo seleciona o resto. Se a conta usar público Advantage+, os interesses entram como sugestão | [SUPOSIÇÃO de nome do recurso; conferir] |
| Região do frio | Turmas de São Paulo: estado de São Paulo. Turmas de Goiânia (289, 68609, 68632): Goiás e Distrito Federal. Ampliação só quando o CRM mostrar a procedência | EM6 [SUPOSIÇÃO de desenho]; procedência [CONFIRMAR] |
| Remarketing (30 dias) | Dois públicos no mesmo conjunto: visitantes da página da turma nos últimos 30 dias (pixel; regra de URL contendo `/produto/<código>/`) e quem engajou com o Instagram @ufapevet nos últimos 90 dias. Sem recorte de região | EM7 [SUPOSIÇÃO de janela e de regra de URL]; sem recorte: [SUPOSIÇÃO de desenho, AMP20], porque quem visitou a página já se qualificou e a persona secundária mora fora da praça |
| Exclusões | Compradores do produto da turma, por evento de compra do pixel (180 dias), nas duas campanhas. O conjunto frio exclui o público do remarketing da turma (visitantes 30 dias e engajamento 90 dias). Nenhuma lista de contatos | EM7; sem dado pessoal na plataforma |
| Posicionamentos | Manuais: Facebook e Instagram (Feed, Stories, Reels e Explorar). Sem Audience Network e sem Messenger. Se o gerenciador marcar o remarketing como público pequeno, voltar aos posicionamentos automáticos, com aprovação | [SUPOSIÇÃO de desenho: leitura por posicionamento e controle de onde a marca aparece] |
| Melhorias automáticas do criativo | Desligadas (texto gerado, variações de texto, música, retoque de imagem) | [SUPOSIÇÃO de nome do recurso]: uma variação automática poderia criar afirmação não aprovada (preço, certificação) |
| Limite de frequência | Em objetivo de cadastros o limite fixo pode não existir; controle por leitura de frequência na revisão semanal e troca de anúncio | [SUPOSIÇÃO de plataforma; conferir] |
| Janela de atribuição | A padrão da conta, registrada no relatório | [CONFIRMAR qual] |
| Parâmetros de URL | No campo próprio do anúncio, não na URL de destino, para não quebrar a URL da página | [SUPOSIÇÃO de boa prática de plataforma] |
| Domínio e eventos | Domínio faculdade.ufape.com.br verificado e eventos priorizados na configuração de eventos | [SUPOSIÇÃO de exigência da conta; conferir] |
| Ordem dos cartões do carrossel | Ordenação automática desligada (criativos 1.3) | criativos 1.3 |

### 4.2 Público por turma

| Turma | Região do frio | `utm_term` do frio | Interesses sugeridos no frio [SUPOSIÇÃO] | Remarketing (30 dias) |
|---|---|---|---|---|
| 68615 | estado de SP | amplo18-sp | medicina veterinária | página de 68615; Instagram 90 dias |
| 289 | GO e DF | amplo18-go | medicina veterinária | página de 289; Instagram 90 dias |
| 333 | estado de SP | amplo18-sp | medicina veterinária | página de 333; Instagram 90 dias |
| 657 | estado de SP | amplo18-sp | medicina veterinária; anestesiologia veterinária (persona) | página de 657; Instagram 90 dias |
| 341 | estado de SP | amplo18-sp | medicina veterinária; equinos (persona) | página de 341; Instagram 90 dias |
| 68635, 68636, 68617, 68628, 679, 366, 662 | estado de SP | amplo18-sp | medicina veterinária | página da turma; Instagram 90 dias |
| 68609, 68632 | GO e DF | amplo18-go | medicina veterinária | página da turma; Instagram 90 dias |

Os públicos de visitantes e de engajamento precisam existir antes da subida. O tamanho de cada público é lido no gerenciador e registrado antes de subir: [DADO NÃO FORNECIDO] hoje. Se um público de pixel não retroagir sobre o histórico da página, a janela de 30 dias só enche depois da criação [SUPOSIÇÃO de plataforma].

---

## 5. Verba da Meta em reais, por fase, semana e dia

### 5.1 Regras

- A verba é por turma. Nenhuma tabela soma mais de R$ 2.000,00 por turma (Meta e Google juntos). Nada passa de uma turma para outra.
- Divisão do frio e do remarketing dentro da Meta [SUPOSIÇÃO de desenho da estratégia, EM4]: aquecimento 80% frio e 20% remarketing; manutenção 0% frio e 100% remarketing; conversão 60% frio e 40% remarketing, em março e em abril.
- Valor da semana = total da fase x 7 / dias da fase. Diária = total da fase / dias da fase, arredondada para baixo em duas casas, para a diária vezes os dias nunca passar do total.
- Sobra de uma fase passa para a fase seguinte da mesma turma e da mesma campanha; a sobra da última fase não é gasta [SUPOSIÇÃO de desenho, EM4].
- Total por turma: março, frio R$ 787,00 (280,00 + 0,00 + 507,00) e remarketing R$ 508,00 (70,00 + 100,00 + 338,00); abril, frio R$ 865,00 (280,00 + 585,00) e remarketing R$ 460,00 (70,00 + 390,00). Esses totais são também o limite de gasto sugerido de cada campanha (AMP24).
- Total da Meta nas 14 turmas: 5 x R$ 1.295,00 = R$ 6.475,00 em março; 9 x R$ 1.325,00 = R$ 11.925,00 em abril; R$ 18.400,00. Google: 5 x R$ 705,00 + 9 x R$ 675,00 = R$ 9.600,00. Soma: R$ 28.000,00.
- Troca de diária pode reiniciar o aprendizado [SUPOSIÇÃO de plataforma]. As trocas são as datas do plano, não otimização de desempenho.
- Gasto diário pode passar da diária em alguns dias e a plataforma compensa em outros [SUPOSIÇÃO de plataforma, sem fonte no repositório]. Por isso o gasto da turma (Meta e Google) é lido toda segunda e o limite de gasto da campanha é pedido (AMP24).

### 5.2 Diárias por fase (Meta). Cada célula: total da fase; por semana; diária

**Março** (frio e remarketing por turma; 289 com os valores como teto, seção 7)

| Turmas | Fase | Datas (dias) | Meta frio | Meta remarketing | Limite de volume da tabela 3.6 (frio / remarketing) |
|---|---|---|---|---|---|
| 68615, 289, 333 | Aquecimento | 07/12 a 20/12 (14) | R$ 280,00; R$ 140,00; R$ 20,00 | R$ 70,00; R$ 35,00; R$ 5,00 | R$ 93,33 / R$ 35,00 |
| 657, 341 | Aquecimento | 14/12 a 20/12 (7) | R$ 280,00; R$ 280,00; R$ 40,00 | R$ 70,00; R$ 70,00; R$ 10,00 | R$ 186,67 / R$ 70,00 |
| as 5 de março (289: teto) | Manutenção | 21/12 a 03/01 (14) | pausado | R$ 100,00; R$ 50,00; R$ 7,14 | pausado / R$ 50,00 |
| 68615, 289, 341 | Conversão | 04/01 a 18/02 (46) | R$ 507,00; R$ 77,15; R$ 11,02 | R$ 338,00; R$ 51,43; R$ 7,34 | R$ 51,43 / R$ 51,43 |
| 333 | Conversão | 04/01 a 25/02 (53) | R$ 507,00; R$ 66,96; R$ 9,56 | R$ 338,00; R$ 44,64; R$ 6,37 | R$ 44,64 / R$ 44,64 |
| 657 | Conversão | 04/01 a 11/02 (39) | R$ 507,00; R$ 91,00; R$ 13,00 | R$ 338,00; R$ 60,67; R$ 8,66 | R$ 60,67 / R$ 60,67 |

**Abril** (662 com o aquecimento como teto, seção 7)

| Turmas | Fase | Datas (dias) | Meta frio | Meta remarketing | Limite de volume da tabela 3.6 (frio / remarketing) |
|---|---|---|---|---|---|
| as 9 de abril (662: teto) | Aquecimento | 06/01 a 24/01 (19) | R$ 280,00; R$ 103,16; R$ 14,73 | R$ 70,00; R$ 25,79; R$ 3,68 | R$ 68,77 / R$ 25,79 |
| 679 | Conversão | 25/01 a 04/03 (39) | R$ 585,00; R$ 105,00; R$ 15,00 | R$ 390,00; R$ 70,00; R$ 10,00 | R$ 70,00 / R$ 70,00 |
| 68632, 68635, 366, 68628 | Conversão | 25/01 a 11/03 (46) | R$ 585,00; R$ 89,02; R$ 12,71 | R$ 390,00; R$ 59,35; R$ 8,47 | R$ 59,35 / R$ 59,35 |
| 68617, 68636 | Conversão | 25/01 a 18/03 (53) | R$ 585,00; R$ 77,26; R$ 11,03 | R$ 390,00; R$ 51,51; R$ 7,35 | R$ 51,51 / R$ 51,51 |
| 68609, 662 | Conversão | 25/01 a 25/03 (60) | R$ 585,00; R$ 68,25; R$ 9,75 | R$ 390,00; R$ 45,50; R$ 6,50 | R$ 45,50 / R$ 45,50 |

Contas de conferência: frio de março na conversão, R$ 845,00 x 60% = R$ 507,00; R$ 507,00 / 46 = R$ 11,0217, diária R$ 11,02. Remarketing de abril no aquecimento, R$ 70,00 / 19 = R$ 3,684, diária R$ 3,68. A coluna do limite é o maior CPL que a campanha aguenta com os conceitos ativos (verba semanal x 3 maior ou igual a conceitos x 1,5 x CPL, ou CPL máximo = 2 x verba semanal / conceitos), copiada da tabela 3.6 da estratégia, que é a fonte única. Se o CPL observado de uma campanha ficar acima do limite dela por 2 semanas fechadas, vale a regra "frio sai" (seção 9).

### 5.3 Leads por semana que a verba da Meta compra no CPL máximo

Leads por semana = verba semanal da campanha / CPL máximo. É a conta do plano, não previsão: os três CPL máximos são [SUPOSIÇÃO ilustrativa] do gestor e nenhum CPL observado existe [DADO NÃO FORNECIDO]. Arredondado em duas casas.

| Turmas | Fase | Campanha | Verba por semana | Leads por semana a R$ 4,00 | a R$ 10,00 | a R$ 18,00 |
|---|---|---|---|---|---|---|
| 68615, 289, 333 | Aquecimento | frio | R$ 140,00 | 35,00 | 14,00 | 7,78 |
| 68615, 289, 333 | Aquecimento | remarketing | R$ 35,00 | 8,75 | 3,50 | 1,94 |
| 657, 341 | Aquecimento | frio | R$ 280,00 | 70,00 | 28,00 | 15,56 |
| 657, 341 | Aquecimento | remarketing | R$ 70,00 | 17,50 | 7,00 | 3,89 |
| as 5 de março | Manutenção | remarketing | R$ 50,00 | 12,50 | 5,00 | 2,78 |
| 68615, 289, 341 | Conversão | frio | R$ 77,15 | 19,29 | 7,72 | 4,29 |
| 68615, 289, 341 | Conversão | remarketing | R$ 51,43 | 12,86 | 5,14 | 2,86 |
| 333 | Conversão | frio | R$ 66,96 | 16,74 | 6,70 | 3,72 |
| 333 | Conversão | remarketing | R$ 44,64 | 11,16 | 4,46 | 2,48 |
| 657 | Conversão | frio | R$ 91,00 | 22,75 | 9,10 | 5,06 |
| 657 | Conversão | remarketing | R$ 60,67 | 15,17 | 6,07 | 3,37 |
| as 9 de abril | Aquecimento | frio | R$ 103,16 | 25,79 | 10,32 | 5,73 |
| as 9 de abril | Aquecimento | remarketing | R$ 25,79 | 6,45 | 2,58 | 1,43 |
| 679 | Conversão | frio | R$ 105,00 | 26,25 | 10,50 | 5,83 |
| 679 | Conversão | remarketing | R$ 70,00 | 17,50 | 7,00 | 3,89 |
| 68632, 68635, 366, 68628 | Conversão | frio | R$ 89,02 | 22,26 | 8,90 | 4,95 |
| 68632, 68635, 366, 68628 | Conversão | remarketing | R$ 59,35 | 14,84 | 5,94 | 3,30 |
| 68617, 68636 | Conversão | frio | R$ 77,26 | 19,32 | 7,73 | 4,29 |
| 68617, 68636 | Conversão | remarketing | R$ 51,51 | 12,88 | 5,15 | 2,86 |
| 68609, 662 | Conversão | frio | R$ 68,25 | 17,06 | 6,83 | 3,79 |
| 68609, 662 | Conversão | remarketing | R$ 45,50 | 11,38 | 4,55 | 2,53 |

A curva de leads acumulados por fase e por turma (contra a qual a revisão semanal lê o ritmo) está na seção 2.4 da estratégia. Leads acumulados abaixo da coluna do otimista, com a verba da fase gasta, mandam aviso ao cmo antes de qualquer pedido de verba.

### 5.4 Mínimo diário da plataforma e regra EM14

O mínimo diário aceito pela Meta para cada campanha é [CONFIRMAR no gerenciador] e não aparece em nenhum arquivo. As diárias mais expostas são as do remarketing: R$ 3,68 (aquecimento de abril), R$ 5,00 e R$ 6,37 a R$ 10,00. Na montagem, o humano lê o mínimo que o gerenciador mostra para cada campanha e compara com a diária da tabela 5.2.

Regra EM14 (sem mudar o total da turma): se a diária do remarketing de uma fase ficar abaixo do mínimo, a parte do remarketing dessa fase passa para o frio da mesma turma, e o remarketing da fase fica pausado até a diária de remarketing caber (na fase seguinte, se couber). A diária do frio vira (frio + remarketing da fase) / dias da fase, arredondada para baixo:

| Turmas | Fase | Diária do frio se o remarketing for movido |
|---|---|---|
| 68615, 289, 333 | Aquecimento | R$ 350,00 / 14 = R$ 25,00 |
| 657, 341 | Aquecimento | R$ 350,00 / 7 = R$ 50,00 |
| 68615, 289, 341 | Conversão | R$ 845,00 / 46 = R$ 18,36 |
| 333 | Conversão | R$ 845,00 / 53 = R$ 15,94 |
| 657 | Conversão | R$ 845,00 / 39 = R$ 21,66 |
| as 9 de abril | Aquecimento | R$ 350,00 / 19 = R$ 18,42 |
| 679 | Conversão | R$ 975,00 / 39 = R$ 25,00 |
| 68632, 68635, 366, 68628 | Conversão | R$ 975,00 / 46 = R$ 21,19 |
| 68617, 68636 | Conversão | R$ 975,00 / 53 = R$ 18,39 |
| 68609, 662 | Conversão | R$ 975,00 / 60 = R$ 16,25 |

**Caso que a EM14 não cobre: manutenção de março.** O frio está pausado de propósito (PP10), então não há frio para receber a parte do remarketing (R$ 7,14 por dia). Se o mínimo da plataforma for maior que R$ 7,14, a regra de sobra de fase (5.1) leva o valor para a conversão do mesmo remarketing, e o remarketing fica pausado na manutenção. Decisão do gestor, por pedido (AMP22) [CONFIRMAR].

### 5.5 Calendário de subidas, trocas de diária e pausas (todas por humano, depois da aprovação)

| Data | O que | Turmas | Condição |
|---|---|---|---|
| 28/10 | Gasto do ciclo e URL de 662 na exportação (PP5, PP15) | 289 e 662 | exportação; gestor confere |
| 30/10 | Teste de rastreio: lead, inscrição paga e 1ª mensalidade como conversões separadas; UTM até o CRM (EA4) | todas | Ufape e humano |
| 03/11 | Gasto previsto até a véspera contra R$ 500,00; pedido de redução da diária, se passar (seção 7) | 289 e 662 | exportação |
| 30/11 | Estruturas de março prontas para aprovação; diárias de 289 recalculadas pelo saldo informado pela analise-de-midia | março; 289 | seção 7 |
| 07/12 | Sobem as duas campanhas de 68615, 289 (estrutura nova; pausa da campanha atual) e 333, com as diárias do aquecimento | 68615, 289, 333 | PP6, PP16, rastreio testado, travas liberadas |
| 14/12 | Sobem 657 e 341, com as diárias do aquecimento de 7 dias | 657, 341 | PP7, U10 (657), PR7 (341) |
| 21/12 | Manutenção: pausa do frio; diária de manutenção no remarketing. Gatilho do rodízio das 5 lido nesta revisão | as 5 de março | PP10 |
| 30/12 | Estruturas de abril prontas para aprovação; diárias de 662 recalculadas | abril; 662 | seção 7 |
| 04/01 | Conversão de março: o frio volta (mesma campanha) com a diária da conversão; remarketing troca a diária; rodízio onde disparou em 21/12 | as 5 de março | revisão de 04/01 |
| 06/01 (quarta) | Sobem as duas campanhas das turmas de abril, com as diárias do aquecimento (662 com as diárias de 30/12; pausa da campanha atual) | as 9 de abril, as de lote 2 só destravadas | PP11, PP16, travas liberadas |
| 18/01 | Gatilho do rodízio de abril lido (1ª semana fechada, 11 a 17/01) | as 9 de abril | revisão de 18/01 |
| 25/01 | Conversão de abril: diárias da conversão em frio e remarketing | as 9 de abril | 25/01 é feriado municipal em São Paulo: [CONFIRMAR com quem executa se a troca é feita no dia] |
| 12/02 | Pedido de pausa das duas campanhas | 657 | corte em 11/02 |
| 19/02 | idem | 68615, 289, 341 | corte em 18/02 |
| 26/02 | idem | 333 | corte em 25/02 |
| 05/03 | idem | 679 | corte em 04/03 |
| 12/03 | idem | 68632, 68635, 366, 68628 | corte em 11/03 |
| 19/03 | idem | 68617, 68636 | corte em 18/03 |
| 26/03 | idem | 68609, 662 | corte em 25/03 |

### 5.6 Turma que sobe atrasada

As partes são as mesmas, contadas da data de subida (estratégia 3.1). Diária do aquecimento = total da fase por campanha dividido pelos dias que restam da subida até 24/01, arredondada para baixo (frio R$ 280,00 e remarketing R$ 70,00 em abril). Se a turma subir depois de 24/01, o aquecimento vai para a conversão: frio R$ 585,00 + R$ 280,00 = R$ 865,00 e remarketing R$ 390,00 + R$ 70,00 = R$ 460,00, divididos pelos dias da subida até o corte. A mudança vira nova versão deste arquivo, antes da subida, e o AAAAMM do nome da campanha passa para o mês real da subida (seção 3.1).

---

## 6. Anúncios

### 6.1 Como o anúncio se liga à peça aprovada

- Texto principal, título, descrição e botão de cada anúncio são **exatamente** os da peça de mesmo nome no criativos v3 (seção da turma, coluna da tabela 6.2). Nenhum texto foi reescrito aqui. Nenhum tem preço, valor de inscrição, bolsa, prova, certificação ou urgência (criativos 1.1).
- O entregável padrão de 5 textos principais por conceito não se repete nesta versão: a encomenda pede anúncios ligados às peças aprovadas (1 texto, 1 título e 1 descrição por peça). Variação de texto só como iteração planejada, uma variável por vez, pedida ao criativos-de-anuncio depois de haver vencedor (cada seção do criativos traz a iteração prevista).
- Botão: "Saiba mais" em todos os anúncios, como aprovado. Motivo: o destino é a página da turma, com as condições completas, e a campanha otimiza lead. Se o evento escolhido for cadastro e a lista da Meta tiver o rótulo, "Cadastre-se" pode entrar no remarketing, por pedido [SUPOSIÇÃO de rótulo disponível].
- Primeira linha do texto principal: as primeiras linhas aprovadas têm até 117 caracteres (maior caso: 366-r2) [conferido por leitura; confirmar na prévia do gerenciador, que mostra cerca de 125 caracteres antes do "ver mais"].
- Em Stories e Reels há pouco texto: a mensagem está dentro da arte. A arte 9:16 de adaptação (nome com `e916`) vai anexa ao mesmo anúncio, como arte do posicionamento de Stories e Reels, e não vira anúncio novo nem teste [SUPOSIÇÃO de recurso de personalização por posicionamento; conferir]. Se o recurso não existir, o estático 1:1 serve a todos os posicionamentos e a adaptação fica de fora, por pedido ao gestor.
- Rodízio (estratégia 3.7): os 3 anúncios do frio sobem juntos, na ordem c1, c2, c3. Se o CPL do frio passar de R$ 20,00 na 1ª semana fechada, ficam no ar os 2 de menor CPL (empate: maior CTR; persistindo, o de menor número), o 3º é pausado, nunca apagado, e a troca é feita na revisão de segunda (seção 9). O remarketing não tem rodízio: as 2 peças ficam no ar.
- **Combinação sugerida para o primeiro teste:** em cada turma, os 3 conceitos do frio juntos, cada um com seu texto aprovado, na mesma campanha e no mesmo conjunto. No aquecimento só se lê direção (CPL e CTR por conceito, sem decidir). O julgamento de conceito é da conversão, com 3 dias de dados e R$ 27,00 gastos por conceito.

### 6.2 Anúncios por turma

Nome completo do anúncio = código da turma + hífen + o texto da célula (exemplo: `68615-c1-hemograma_e11_percurso_v1`). Frio: c1, c2, c3. Remarketing: r1 e r2. Artes 9:16 anexas: as 2 por turma indicadas na última coluna (também com o código na frente).

| Turma | Criativos v3 | c1 (frio) | c2 (frio) | c3 (frio) | r1 (remarketing) | r2 (remarketing) | Artes 9:16 anexas |
|---|---|---|---|---|---|---|---|
| 68615 | seção 4 | c1-hemograma_e11_percurso_v1 | c2-clinico-lab_vid916_pergunta_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-hemograma_e916_percurso_v1; r2-turma_e916_data_v1 |
| 289 | seção 5 | c1-presenciais_e11_numero_v1 | c2-ecg-eco_vid916_percurso_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-presenciais_e916_numero_v1; r2-turma_e916_data_v1 |
| 333 | seção 6 | c1-presenciais_vid916_numero_v1 | c2-mielograma_e11_pergunta_v1 | c3-modulos_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c2-mielograma_e916_pergunta_v1; r2-turma_e916_data_v1 |
| 657 | seção 7 | c1-hemodinamica_e11_pergunta_v1 | c2-ventilador_vid916_percurso_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-hemodinamica_e916_pergunta_v1; r2-turma_e916_data_v1 |
| 341 | seção 8 | c1-percurso_e11_percurso_v1 | c2-claudicacao_vid916_pergunta_v1 | c3-calendario_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-percurso_e916_percurso_v1; r2-turma_e916_data_v1 |
| 68635 | seção 9 | c1-presenciais_e11_numero_v1 | c2-plantao_vid916_pergunta_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-presenciais_e916_numero_v1; r2-turma_e916_data_v1 |
| 68636 | seção 10 | c1-fisiologia-semiologia_e11_percurso_v1 | c2-praticas_vid916_numero_v1 | c3-docentes_car_numero_v1 | r1-modulos_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-fisiologia-semiologia_e916_percurso_v1; r2-turma_e916_data_v1 |
| 68617 | seção 11 | c1-cushing_e11_numero_v1 | c2-pratica_vid916_pergunta_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-cushing_e916_numero_v1; r2-turma_e916_data_v1 |
| 68628 | seção 12 | c1-imuno-eletro_vid916_percurso_v1 | c2-presenciais_e11_numero_v1 | c3-biosseguranca_car_pergunta_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c2-presenciais_e916_numero_v1; r2-turma_e916_data_v1 |
| 68609 | seção 13 | c1-fimdesemana_e11_cena_v1 | c2-preanestesico_vid916_percurso_v1 | c3-docentes_car_numero_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-fimdesemana_e916_cena_v1; r2-turma_e916_data_v1 |
| 68632 | seção 14 | c1-fimdesemana_vid916_cena_v1 | c2-roteiro_e11_percurso_v1 | c3-passagem_car_pergunta_v1 | r1-mesames_car_pergunta_v1 | r2-turma_e11_data_v1 | c2-roteiro_e916_percurso_v1; r2-turma_e916_data_v1 |
| 679 | seção 15 | c1-zoonoses_vid916_cena_v1 | c2-online-presencial_e11_numero_v1 | c3-antibiotico_car_contrario_v1 | r1-modulos_car_pergunta_v1 | r2-turma_e11_data_v1 | c2-online-presencial_e916_numero_v1; r2-turma_e916_data_v1 |
| 366 | seção 16 | c1-presenciais_e11_numero_v1 | c2-felinos_vid916_pergunta_v1 | c3-docentes_car_numero_v1 | r1-modulos_car_pergunta_v1 | r2-turma_e11_data_v1 | c1-presenciais_e916_numero_v1; r2-turma_e916_data_v1 |
| 662 | seção 17 | c1-turma_e11_data_v1 | c2-graduados_vid916_pergunta_v1 | c3-formato_car_numero_v1 (estrutura sem arte final) | r1-modulos_car_pergunta_v1 (estrutura sem arte final) | r2-turma_e11_data_v1 | c1-turma_e916_data_v1; r2-turma_e916_data_v1 |

Totais: 14 turmas x 3 anúncios no frio = 42; 14 x 2 no remarketing = 28; 70 anúncios. Em 662, c3 e r1 não têm arte nem texto liberados (criativos 17): nenhum anúncio de 662 sobe antes de o c3 estar produzido e aprovado (seção 8).

### 6.3 URL de destino e parâmetros de URL, por turma

Destino sempre a página da turma (criativos v3). Parâmetros no campo próprio do anúncio, sem o `?`: `utm_source=meta&utm_medium=paid_social&utm_campaign=<campanha>&utm_content=<nome do anúncio>&utm_term=<público>`. Nenhum dado pessoal em UTM. O `utm_content` é sempre igual ao nome do anúncio no gerenciador; o mesmo criativo em outra turma é outro anúncio, com outro nome.

| Turma | URL de destino (ficha) |
|---|---|
| 68615 | https://faculdade.ufape.com.br/produto/68615/pos-graduacao-patologia-clinica/sao-paulo |
| 289 | https://faculdade.ufape.com.br/produto/289/pos-graduacao-em-cardiologia-veterinaria |
| 333 | https://faculdade.ufape.com.br/produto/333/pos-graduacao-em-citopatologia-veterinaria |
| 657 | https://faculdade.ufape.com.br/produto/657/pos-graduacao-em-anestesiologia-avancada |
| 341 | https://faculdade.ufape.com.br/produto/341/pos-graduacao-em-medicina-interna-equina |
| 68635 | https://faculdade.ufape.com.br/produto/68635/pos-graduacao-clinica-medica-e-emergencia-de-pequenos-animais/sao-paulo |
| 68636 | https://faculdade.ufape.com.br/produto/68636/pos-graduacao-em-pneumologia-veterinaria |
| 68617 | https://faculdade.ufape.com.br/produto/68617/pos-graduacao-endocrinologia-de-pequenos-animais/v/sao-paulo (final "/v/" a conferir, seção 8) |
| 68628 | https://faculdade.ufape.com.br/produto/68628/pos-graduacao-oncologia-veterinaria/sao-paulo |
| 68609 | https://faculdade.ufape.com.br/produto/68609/pos-graduacao-anestesiologia-veterinaria/goiania |
| 68632 | https://faculdade.ufape.com.br/produto/68632/pos-graduacao-clinica-cirurgica-de-caes-e-gatos/goiania |
| 679 | https://faculdade.ufape.com.br/produto/679/pos-graduacao-em-infectologia-veterinaria |
| 366 | https://faculdade.ufape.com.br/produto/366/pos-graduacao-fisioterapia-fisiatria-e-reabilitacao-veterinaria/sao-paulo |
| 662 | https://faculdade.ufape.com.br/produto/662/pos-graduacao-em-ortopedia-veterinaria (página com link trocado, seção 8) |

Parâmetros completos de cada anúncio (os 3 primeiros de cada bloco são do frio; os 2 últimos, do remarketing). O AAAAMM de 679, 68636, 366 e 662 muda se a subida for em outro mês (seção 3.1).

```
68615
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_amplo18-sp_202612&utm_content=68615-c1-hemograma_e11_percurso_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_amplo18-sp_202612&utm_content=68615-c2-clinico-lab_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_amplo18-sp_202612&utm_content=68615-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_rmk30d_202612&utm_content=68615-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_rmk30d_202612&utm_content=68615-r2-turma_e11_data_v1&utm_term=rmk30d

289
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_amplo18-go_202612&utm_content=289-c1-presenciais_e11_numero_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_amplo18-go_202612&utm_content=289-c2-ecg-eco_vid916_percurso_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_amplo18-go_202612&utm_content=289-c3-docentes_car_numero_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_rmk30d_202612&utm_content=289-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_rmk30d_202612&utm_content=289-r2-turma_e11_data_v1&utm_term=rmk30d

333
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_amplo18-sp_202612&utm_content=333-c1-presenciais_vid916_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_amplo18-sp_202612&utm_content=333-c2-mielograma_e11_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_amplo18-sp_202612&utm_content=333-c3-modulos_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_rmk30d_202612&utm_content=333-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_rmk30d_202612&utm_content=333-r2-turma_e11_data_v1&utm_term=rmk30d

657
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_amplo18-sp_202612&utm_content=657-c1-hemodinamica_e11_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_amplo18-sp_202612&utm_content=657-c2-ventilador_vid916_percurso_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_amplo18-sp_202612&utm_content=657-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_rmk30d_202612&utm_content=657-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_rmk30d_202612&utm_content=657-r2-turma_e11_data_v1&utm_term=rmk30d

341
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_amplo18-sp_202612&utm_content=341-c1-percurso_e11_percurso_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_amplo18-sp_202612&utm_content=341-c2-claudicacao_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_amplo18-sp_202612&utm_content=341-c3-calendario_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_rmk30d_202612&utm_content=341-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_rmk30d_202612&utm_content=341-r2-turma_e11_data_v1&utm_term=rmk30d

68635
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_amplo18-sp_202701&utm_content=68635-c1-presenciais_e11_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_amplo18-sp_202701&utm_content=68635-c2-plantao_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_amplo18-sp_202701&utm_content=68635-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_rmk30d_202701&utm_content=68635-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_rmk30d_202701&utm_content=68635-r2-turma_e11_data_v1&utm_term=rmk30d

68636
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_amplo18-sp_202701&utm_content=68636-c1-fisiologia-semiologia_e11_percurso_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_amplo18-sp_202701&utm_content=68636-c2-praticas_vid916_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_amplo18-sp_202701&utm_content=68636-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_rmk30d_202701&utm_content=68636-r1-modulos_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_rmk30d_202701&utm_content=68636-r2-turma_e11_data_v1&utm_term=rmk30d

68617
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_amplo18-sp_202701&utm_content=68617-c1-cushing_e11_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_amplo18-sp_202701&utm_content=68617-c2-pratica_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_amplo18-sp_202701&utm_content=68617-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_rmk30d_202701&utm_content=68617-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_rmk30d_202701&utm_content=68617-r2-turma_e11_data_v1&utm_term=rmk30d

68628
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_amplo18-sp_202701&utm_content=68628-c1-imuno-eletro_vid916_percurso_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_amplo18-sp_202701&utm_content=68628-c2-presenciais_e11_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_amplo18-sp_202701&utm_content=68628-c3-biosseguranca_car_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_rmk30d_202701&utm_content=68628-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_rmk30d_202701&utm_content=68628-r2-turma_e11_data_v1&utm_term=rmk30d

68609
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_amplo18-go_202701&utm_content=68609-c1-fimdesemana_e11_cena_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_amplo18-go_202701&utm_content=68609-c2-preanestesico_vid916_percurso_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_amplo18-go_202701&utm_content=68609-c3-docentes_car_numero_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_rmk30d_202701&utm_content=68609-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_rmk30d_202701&utm_content=68609-r2-turma_e11_data_v1&utm_term=rmk30d

68632
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_amplo18-go_202701&utm_content=68632-c1-fimdesemana_vid916_cena_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_amplo18-go_202701&utm_content=68632-c2-roteiro_e11_percurso_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_amplo18-go_202701&utm_content=68632-c3-passagem_car_pergunta_v1&utm_term=amplo18-go
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_rmk30d_202701&utm_content=68632-r1-mesames_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_rmk30d_202701&utm_content=68632-r2-turma_e11_data_v1&utm_term=rmk30d

679
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_amplo18-sp_202701&utm_content=679-c1-zoonoses_vid916_cena_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_amplo18-sp_202701&utm_content=679-c2-online-presencial_e11_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_amplo18-sp_202701&utm_content=679-c3-antibiotico_car_contrario_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_rmk30d_202701&utm_content=679-r1-modulos_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_rmk30d_202701&utm_content=679-r2-turma_e11_data_v1&utm_term=rmk30d

366
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_amplo18-sp_202701&utm_content=366-c1-presenciais_e11_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_amplo18-sp_202701&utm_content=366-c2-felinos_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_amplo18-sp_202701&utm_content=366-c3-docentes_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_rmk30d_202701&utm_content=366-r1-modulos_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_rmk30d_202701&utm_content=366-r2-turma_e11_data_v1&utm_term=rmk30d

662
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_amplo18-sp_202701&utm_content=662-c1-turma_e11_data_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_amplo18-sp_202701&utm_content=662-c2-graduados_vid916_pergunta_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_amplo18-sp_202701&utm_content=662-c3-formato_car_numero_v1&utm_term=amplo18-sp
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_rmk30d_202701&utm_content=662-r1-modulos_car_pergunta_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_rmk30d_202701&utm_content=662-r2-turma_e11_data_v1&utm_term=rmk30d
```

A UTM chega ao CRM com origem se o teste de rastreio de 30/10 passar (S6). Os parâmetros dinâmicos da Meta (nome da campanha, do conjunto e do anúncio) podem substituir os valores fixos se o arquiteto-de-fluxos preferir, desde que o valor final saia em minúsculas e sem acento [SUPOSIÇÃO de recurso; conferir].

---

## 7. 289 e 662: campanhas que já rodam

Regra única da estratégia v4 (3.8, EM15), igual para as duas: o gasto que já roda conta dentro dos R$ 2.000,00 da turma.

### 7.1 Situação e o que não muda

| Item | 289 (Cardiologia Veterinária, Goiânia) | 662 (Ortopedia Veterinária, São Paulo) |
|---|---|---|
| Campanha atual | Ativa, estático, "com 5 ângulos" (visão de campanhas de 26/10) | Ativa, estático e vídeo, "sem 5 ângulos" (visão de campanhas de 26/10) |
| Nome | **Não é renomeada** (D12). Nome atual: [DADO NÃO FORNECIDO]. A tabela de correspondência é da analise-de-midia | **Não é renomeada** (D12). Nome atual: [DADO NÃO FORNECIDO] |
| Canal e diária atual | [DADO NÃO FORNECIDO] (exportação de 28/10). Nunca aumentar | [DADO NÃO FORNECIDO]. Nunca aumentar |
| Gasto informado (G) | [DADO NÃO FORNECIDO]. Fonte: analise-de-midia, em 30/11 | [DADO NÃO FORNECIDO]. Fonte: analise-de-midia, em 30/12 |
| Véspera da estrutura nova | 06/12/2026 | 05/01/2027 |
| Limite do gasto até a véspera | **R$ 500,00** (é o aquecimento da turma) | **R$ 500,00** |
| Checagem do previsto | 03/11 (AMP17) | 03/11 (AMP18) |
| Estrutura nova | 07/12, nomes `pos_289-cardio-go_...` | 06/01, nomes `pos_662-orto_...`, só com link corrigido |
| Conversão (protegida) | R$ 1.300,00 no total da turma (Meta R$ 845,00); não muda por causa do gasto anterior | R$ 1.500,00 no total da turma (Meta R$ 975,00); idem |
| Situação da página | sem pendência de link | **link trocado (P3)**: a página mostra início em 15 e 16 de agosto de 2026, turma IV e preço de outra turma; conferir a URL em 28/10 (PP5) |

### 7.2 O que fazer, em ordem

1. **03/11 (e toda segunda):** o gestor compara o gasto previsto da campanha atual até a véspera com R$ 500,00. Se o previsto passar, vai o pedido de **reduzir a diária atual** (ou de pausar, se a redução não bastar). Nunca aumento.
2. **28/10 em 662:** se a URL levar à página errada, vai o pedido de **pausa**, o que também zera o gasto até a correção (EM9, PP5). Pausar, nunca excluir, com exportação antes.
3. **Recálculo:** em 30/11 (289) e em 30/12 (662), a analise-de-midia informa o gasto, e as diárias do aquecimento da estrutura nova são recalculadas (7.3). O gasto até a véspera é o acumulado informado mais a diária atual vezes os dias restantes até a véspera [SUPOSIÇÃO de leitura da regra, que fala em "gasto até a véspera"].
4. **Subida da estrutura nova** (289 em 07/12; 662 em 06/01, só com link corrigido): as duas campanhas novas sobem com o nome padrão. A campanha atual é **pausada no mesmo dia**, com exportação, sem renomear e sem excluir, para não gastar duas vezes na mesma turma [SUPOSIÇÃO de desenho; a estratégia limita o gasto da atual até a véspera e a v2 recomendava pausar a atual, AMP17 e AMP18].
5. **Conversão protegida:** nada do gasto anterior sai da conversão. Em 289, o excesso sai da manutenção; em 662, que não tem manutenção, o pedido de redução do item 1 vem antes de o gasto chegar a R$ 500,00.

### 7.3 Fórmulas do recálculo (mesma divisão por canal das tabelas 5.2)

Com G = gasto até a véspera:

- Aquecimento novo da turma, A = R$ 500,00 menos G, se positivo; se G for R$ 500,00 ou mais, A = 0.
- Divisão do aquecimento por canal: frio 56% de A, remarketing 14% de A, Google 30% de A (Meta 70%, com 80% de frio e 20% de remarketing).
- Diária do frio = (0,56 x A) / dias da fase, arredondada para baixo em duas casas. Diária do remarketing = (0,14 x A) / dias da fase. Dias da fase: 14 em 289 (07/12 a 20/12) e 19 em 662 (06/01 a 24/01).
- Conferência com G = 0: A = R$ 500,00; 289, frio R$ 280,00 / 14 = R$ 20,00 e remarketing R$ 70,00 / 14 = R$ 5,00; 662, frio R$ 280,00 / 19 = R$ 14,73 e remarketing R$ 70,00 / 19 = R$ 3,68. São os valores das tabelas 5.2, que por isso são o teto.
- **Só 289, excesso:** E = G menos R$ 500,00, se positivo. A manutenção nova = R$ 200,00 menos E, se positivo; o remarketing da manutenção recebe 50% dela, dividido por 14 dias. O excesso nunca sai da conversão.
- **Se A = 0:** a estrutura nova de 289 sobe em 21/12, já na manutenção (recalculada pelo excesso), e a de 662 sobe em 25/01, na conversão.
- **Se o gasto de 289 já registrado em 30/11 passar de R$ 700,00:** aviso ao gestor e ao cmo antes da subida de 07/12 [CONFIRMAR o caminho com o gestor, EM15].
- Se o gasto de 662 passar de R$ 500,00 mesmo assim: aviso ao gestor e ao cmo, e a conversão continua protegida [CONFIRMAR o caminho com o gestor; a estratégia não escreve este caso].
- Se o aquecimento recalculado ficar menor que o da tabela, o limite de volume da fase cai na mesma proporção e é reescrito em 30/11 e 30/12, antes da subida (estratégia 3.6).

### 7.4 Ficha de recálculo (preencher em 30/11 e em 30/12, só com números somados)

| Campo | 289 (30/11) | 662 (30/12) |
|---|---|---|
| Gasto acumulado informado (G) | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] |
| Diária atual vigente e dias até a véspera | [DADO NÃO FORNECIDO] | [DADO NÃO FORNECIDO] |
| Gasto até a véspera | [calcular] | [calcular] |
| A (aquecimento novo) | [calcular] | [calcular] |
| Frio: diária nova | [calcular] | [calcular] |
| Remarketing: diária nova | [calcular] | [calcular] |
| E e manutenção nova | [calcular] | não se aplica |
| Limite de volume reescrito (frio / remarketing) | [calcular, 3.6] | [calcular, 3.6] |

---

## 8. Travas de subida

Nenhuma destas turmas sobe, nem tem campanha montada para publicação, antes da liberação escrita de quem confirma. A estrutura fica descrita neste arquivo; o humano só monta depois da liberação.

| Trava | Turma | O que impede | O que muda na montagem | Quem libera |
|---|---|---|---|---|
| **P3** | 679 | O link da campanha na planilha está trocado (a linha "Citopatologia 03/04" aponta para 679); sem data de início e sem preço em peça final | Nenhuma campanha publicada. O r2 traz [DATA, após correção de P3]. AAAAMM pelo mês real da subida. A frase do AP7 só vale depois da liberação | Ufape (pedido A12) ou liberação expressa do cmo |
| **P3** | 68636 | Sem data de início e sem preço em peça final; data 17/04/2027 só no site (U6); datas dos módulos da ficha incoerentes | Idem. Nenhuma peça cita data de módulo. O r2 traz [DATA, após correção de P3]. A frase "as datas estão no cronograma da página" e a do AP7 só valem depois da correção do site e da liberação | Ufape (A12, U6) ou cmo |
| **P3** | 662 | Página mostra outra turma (agosto de 2026, turma IV, preço de outra turma). As peças trazem só nome, campus e data da planilha (24/04/2027) | Conferência da URL em 28/10 (PP5). Estrutura nova só com link, data e cronograma corrigidos. A frase do AP7 não vale enquanto a página mostrar o preço de outra turma; no frio e no r2 vale "Veja o cronograma na página da turma". Sem número de turma | Ufape (A12) e cmo |
| **c3 de 662** | 662 | O c3 e o r1 são estrutura sem arte final: não há conteúdo permitido para eles | O kit mínimo de 3 conceitos nunca diminui e o rodízio pede 3: o c3 precisa estar produzido e aprovado **antes** de a estrutura nova de 662 subir. Nova versão do criativos com conteúdo só depois da ficha corrigida ou da liberação do cmo | criativos-de-anuncio, qa-de-marketing e cmo |
| **P4** | 366 | A data diverge: planilha 10/04/2027, site 24/04/2027. Vale a planilha (decisão 12), mas o destino mostra outra data | Só sobe com a data conferida na página. As peças de frio não citam data de início; o r2 cita 10/04/2027 e só sobe depois da conferência. Nenhuma peça traz data de módulo | Ufape |
| **U10** | 657 | A ficha não traz pré-requisito formal, só o público "médicos veterinários anestesistas já atuantes" | Todas as peças repetem o texto da página. Pré-requisito formal (tempo de atuação, comprovação) [CONFIRMAR U10] antes de subir | Ufape |
| **PP7** | 657 e 341 | Desbloqueio dos dois para subir em 14/12. Em 341 ainda: regra da promoção de 20% (PR7), local da prática e número de módulos presenciais (AP11) | Sobem em 14/12 só com PP7 aprovado. 341 sem promoção em qualquer texto; nenhuma peça diz onde a prática acontece | pessoa do marketing e cmo; Ufape (U10, PR7, AP11) |
| **URL de 68617** | 68617 | A URL da ficha termina em "/v/" (turma V no site; a planilha diz VII): conferir se o destino é a turma da planilha antes de subir | Sobe só com a URL conferida na página. Sem número de turma em nenhuma peça (P5) | Ufape |

Outras condições que valem para toda turma antes de subir, sem trava própria:

- Página de destino com data, campus e modalidade iguais ao anúncio (68632 é presencial; nunca "semipresencial"). Algumas páginas ainda dizem turma mínima de 20: nenhum anúncio cita o número (criativos v3), e a correção da página é o pedido A12 do cmo.
- Páginas com frase ligada ao MEC (12 de 14 ativas, segundo a análise): o anúncio não a repete, e a página de destino é sinalizada no item "página de destino" da conformidade (pedido A7 do cmo). Subida só com decisão registrada da pessoa do marketing ou com a página corrigida [CONFIRMAR].
- Política de privacidade e finalidade do formulário visíveis na página da turma (conformidade) [CONFIRMAR em cada página].
- Frase de remarketing "Veja parcelas, total e matrícula na página da turma": o humano confere, no dia da subida, que parcelas, total e matrícula estão visíveis na página (condição 2 do AP7). Se a U11 mudar o rótulo "Matrícula" para "Inscrição", a frase muda junto, em nova versão do criativos (condição 3).
- As campanhas antigas pausadas das turmas de março e abril (657, 68615, 341, 333, 68635, 366, 68617 e a de 679) seguem **pausadas**, sem renomear e sem excluir; nenhuma é reativada. As novas sobem no padrão, para não herdar público, verba e nome antigos [SUPOSIÇÃO de desenho, mantida da versão 2].

---

## 9. Protocolo de teste e limites (escritos antes de subir, não mudam depois)

Copiados da estratégia v4 (2.5, 3.7 e 6.3), sem número novo.

| Item | Regra | O que acontece |
|---|---|---|
| Leitura permitida | Campanha com pelo menos 3 dias de dados e gasto de pelo menos R$ 27,00 (1,5 x R$ 18,00) [SUPOSIÇÃO de desenho da estratégia]; nada de tendência com os 2 últimos dias | antes disso, só direção |
| Meta de corte | CPL da semana fechada até R$ 4,00; custo por inscrição até R$ 80,00 | dentro da meta |
| Alerta | CPL da semana fechada acima de R$ 4,00, ou taxa de lead para inscrição abaixo da mínima | ordem de checagem do gestor; uma mudança por conjunto por semana |
| Rodízio | CPL do frio acima de R$ 20,00 na 1ª semana fechada da turma [SUPOSIÇÃO do gestor] | ficam os 2 anúncios de menor CPL; pedido de pausa do 3º. Março: lido em 21/12, vale a partir de 04/01 (o frio fica pausado na manutenção). Abril: lido em 18/01 |
| Troca de anúncio | Cada um dos 2 no ar com pelo menos 3 dias de dados e R$ 27,00 gastos | pedido de pausa do pior dos 2 e de reativação do pausado; uma troca por semana por campanha |
| Saída do rodízio | Conceito que perder duas trocas | sai do rodízio e vira pedido de iteração ao criativos-de-anuncio, uma variável por vez |
| Volta dos 3 | CPL do frio abaixo de R$ 10,00 por 2 semanas fechadas com rodízio [SUPOSIÇÃO de desenho] | os 3 voltam juntos |
| Pausa de anúncio | Anúncio com R$ 36,00 gastos (2 x R$ 18,00) sem nenhum lead [SUPOSIÇÃO de desenho] | pedido de pausa do anúncio; nunca todos os anúncios da campanha ao mesmo tempo |
| Frio sai | CPL do frio acima do limite da seção 5.2 por 2 semanas fechadas | pedido: o frio pausa e a parte dele vai metade para o remarketing e metade para a busca da mesma turma [SUPOSIÇÃO de desenho] |
| Revisão da campanha | CPL acima de R$ 18,00 por 2 semanas fechadas, ou 2 semanas fora da meta depois de um ajuste | aviso ao cmo com as alavancas da skill; verba extra só como pedido separado ao cmo |
| Escalar dentro da turma | CPL da semana fechada abaixo de R$ 10,00, com pelo menos 10 leads e 3 dias de dados, e outra campanha da turma e da fase acima de R$ 18,00 | mover até 20% da diária da pior para a melhor; nunca aumentar o total da turma, nem antecipar fase, nem passar verba para outra turma |
| Cadência de criativo novo | Aquecimento sem julgar conceito; manutenção sem criativo novo; conversão julga | nenhum anúncio novo sem pedido |
| Teto da turma | Gasto acumulado do ciclo (Meta e Google) chega a R$ 2.000,00, ou dia seguinte ao corte | pedido de pausa de todas as campanhas da turma (EM16) |

Revisão toda segunda-feira (feriado passa para o dia útil seguinte, D15): 03/11, 26/01 (25/01 é feriado municipal em São Paulo) e 10/02 (08 e 09/02 são Carnaval) estão na seção 6.2 da estratégia. Gasto, leads, inscrições pagas e 1ª mensalidade somados por turma vêm da analise-de-midia.

---

## 10. Formulário instantâneo e mensagem de WhatsApp

Não se aplica nesta rodada. Toda campanha da Pós leva à página da turma (gestor-de-midia-pos, seção 3: WhatsApp como destino fora; atendimento instável em 22/10). Formulário instantâneo também fica fora: a coleta de dados aconteceria fora da página, sem a política de privacidade da página na mesma tela [SUPOSIÇÃO de risco], e o CRM recebe a origem pela UTM da página. Se a Ufape quiser formulário instantâneo, vira pedido novo, com finalidade e link de privacidade no formulário (conformidade, LGPD). Por isso este arquivo não traz perguntas de formulário nem mensagem inicial de WhatsApp. Se um dia houver anúncio de WhatsApp, só leva a número oficial da Ufape, com atendimento em horário comercial informado (secretaria, vendas São Paulo e vendas Goiânia, em contexto/ufape-geral.md).

---

## 11. Checklists

### 11.1 Checklist de subida (pré-lançamento), por campanha

| # | Item | Quem confere |
|---|---|---|
| S1 | Metas de CPL e de custo por matrícula e verba em reais escritas, com aprovador registrado (PP16; aprovador de "Anúncios e verba" ainda não nomeado em contexto/ufape-geral.md) | gestor-de-midia |
| S2 | Pixel e API de Conversões recebendo o evento de otimização na página de destino (teste de 30/10) e as conversões de inscrição paga e 1ª mensalidade separadas | humano; arquiteto-de-fluxos |
| S3 | Domínio faculdade.ufape.com.br verificado e eventos priorizados [SUPOSIÇÃO de exigência da conta] | humano |
| S4 | Objetivo e evento certos na campanha (lead ou, se o teste exigir, início de checkout) | humano |
| S5 | Nome da campanha, do conjunto e do anúncio exatamente como nas seções 3 e 6 | humano; qa |
| S6 | Parâmetros de URL completos (seção 6.3), no campo próprio, e chegada da UTM ao CRM no teste | humano; arquiteto-de-fluxos |
| S7 | Página de destino confere com o anúncio: data, campus e modalidade; sem pendência de link; frase de parcelas, total e matrícula visível (AP7) | humano; qa |
| S8 | Página com frase ligada ao MEC: só com decisão registrada da pessoa do marketing ou com a página corrigida | pessoa do marketing |
| S9 | Peças aprovadas pelo qa-de-marketing na conformidade educacional; texto, título e descrição do anúncio iguais ao criativos v3; nenhum texto com preço, inscrição, bolsa ou prova (varredura) | qa; humano |
| S10 | 18+, região, exclusões e posicionamentos como na seção 4 | humano |
| S11 | Orçamento só na campanha, com a diária da fase (seção 5.2); limite de gasto da campanha [SUPOSIÇÃO de recurso]; sem data de término | humano |
| S12 | Mínimo diário da plataforma lido e comparado com a diária de cada campanha; EM14 aplicada se for o caso | humano; gestor |
| S13 | Tamanho do público lido no gerenciador e registrado [DADO NÃO FORNECIDO hoje] | humano |
| S14 | Prévia de cada posicionamento conferida (Stories e Reels com a mensagem dentro da arte e sem corte nas zonas de interface; carrossel com ordenação automática desligada) | humano |
| S15 | Melhorias automáticas do criativo desligadas | humano |
| S16 | 3 anúncios no frio e 2 no remarketing, com as 2 artes 9:16 anexas | humano |
| S17 | Travas da turma (seção 8) liberadas por escrito | gestor-de-midia |
| S18 | Forma de pagamento ativa e limite de gasto da conta acima da soma das diárias aprovadas [SUPOSIÇÃO de configuração] | humano |
| S19 | Campanhas antigas pausadas da turma continuam pausadas | humano |
| S20 | Registro de quem montou, quem revisou e quem aprovou (montagem: humano do gerenciador [CONFIRMAR nome]; revisão: gestor-de-midia e qa-de-marketing; aprovação: pessoa do marketing) | humano |

### 11.2 Checklist de pausa (dia seguinte ao corte, EM16)

| # | Item |
|---|---|
| P1 | Pedido de pausa aprovado antes (datas da seção 5.5), ou antes da data se o gasto do ciclo da turma (Meta e Google) chegar a R$ 2.000,00, ou se o destino estiver errado |
| P2 | Exportação da campanha, dos conjuntos e dos anúncios antes de pausar (configuração, texto, URL e parâmetros) |
| P3 | Pausar as **duas** campanhas da turma (frio e remarketing); **pausar, nunca excluir**; avisar o anuncios-google, que pausa a Busca da mesma turma |
| P4 | Conferir no dia seguinte que o gasto parou (status inativo e gasto zero) |
| P5 | Registrar data, hora, motivo e gasto final da Meta no relatório da semana; a analise-de-midia soma com o Google contra R$ 2.000,00 |
| P6 | Como desfazer: reativar no gerenciador com a configuração exportada, só com verba nova aprovada; uma reativação conta como mudança da semana |
| P7 | Pausa do frio de março em 21/12 (manutenção): mesmo roteiro, mas com volta em 04/01 como a mesma campanha |
| P8 | Pausa da campanha atual de 289 (07/12) e de 662 (06/01), no dia em que a estrutura nova sobe, com exportação (seção 7.2) |
| P9 | Pausa de anúncio isolado (R$ 36,00 sem lead) e do 3º anúncio no rodízio: nunca todos os anúncios da campanha ao mesmo tempo |

---

## 12. Pedidos de aprovação humana (AMP13 a AMP24)

Até a tabela de aprovação de contexto/ufape-geral.md ser preenchida, todos vão à pessoa do marketing que aprovou o plano do cmo; os que mudam canal ou distribuição vão também ao gestor e ao cmo. Quem executa: humano no gerenciador. Nada é executado pela squad. Os pedidos AMP1 a AMP12 da versão 2 são das provas e estão suspensos na seção 13.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AMP13 | Montar e subir a estrutura de março: 10 campanhas Meta (2 por turma em 68615, 289, 333, 657 e 341), 1 conjunto em cada, orçamento na campanha, evento lead, nomes e parâmetros de URL das seções 3 e 6 (chave com área curta, [CONFIRMAR com o cmo que cumpre o D12]). 657 e 341 só com PP7 e U10 | Meta e verba são por turma; a manutenção desliga só o frio | Meta R$ 1.295,00 por turma (frio R$ 787,00, remarketing R$ 508,00), R$ 6.475,00 nas 5, dentro dos R$ 2.000,00 por turma | Leitura por turma; 28 leads por semana a R$ 10,00 no frio das 68615, 289 e 333 no aquecimento (seção 5.3), sem promessa de resultado | Pausar as 10 campanhas com exportação (nunca excluir); reativar as antigas só com nova aprovação | 30/11; subida em 07/12 (657 e 341 em 14/12) |
| AMP14 | Montar e subir a estrutura de abril: 18 campanhas Meta (2 por turma nas 9 turmas), mesmo desenho, sem manutenção. 679, 366 e 662 (lote 2), 68636 e 68617 só com as travas da seção 8 liberadas | Idem | Meta R$ 1.325,00 por turma (frio R$ 865,00, remarketing R$ 460,00), R$ 11.925,00 nas 9, dentro dos R$ 2.000,00 por turma | Leitura por turma a partir de 06/01 | Pausar as 18 campanhas com exportação; reativar as antigas só com nova aprovação | 30/12; subida em 06/01 |
| AMP15 | Trocas de diária por humano, com os valores da seção 5.2: 21/12 (frio pausa; remarketing de manutenção), 04/01 (frio volta e conversão de março), 25/01 (conversão de abril) | Verba e mensagem de cada fase escritas antes de começar | Sem aumento do total: soma das fases = total da turma | Cada fase gasta o que o plano previu | Voltar à diária da fase anterior (pode reiniciar o aprendizado [SUPOSIÇÃO]) | datas da seção 5.5 |
| AMP16 | Pausa das duas campanhas Meta de cada turma no dia seguinte ao corte, ou antes se o gasto do ciclo chegar a R$ 2.000,00 (EM16) | Fim do ciclo e teto do CEO | Sem gasto novo | Nenhum gasto depois do corte nem acima da verba | Reativar só com verba nova aprovada | 12/02, 19/02, 26/02, 05/03, 12/03, 19/03 e 26/03 |
| AMP17 | 289: limite de R$ 500,00 de gasto da campanha atual até 06/12; pedido de redução da diária se o previsto passar; recálculo das diárias da estrutura nova em 30/11; pausa da campanha atual em 07/12 (recomendação, [SUPOSIÇÃO de desenho]) | O gasto anterior conta nos R$ 2.000,00 e a conversão fica protegida (EM15) | Sem aumento; aquecimento da estrutura nova = R$ 500,00 menos o gasto; diária atual [DADO NÃO FORNECIDO] | Conversão de R$ 1.300,00 (Meta R$ 845,00) intacta | Reativar a diária anterior | 03/11; 30/11; 07/12 |
| AMP18 | 662: conferir a URL em 28/10 e pausar se levar à página errada; limite de R$ 500,00 até 05/01; recálculo em 30/12; pausa da campanha atual em 06/01; estrutura nova só com link corrigido e c3 aprovado | Idem; página com link trocado não recebe anúncio | Sem aumento; diária atual [DADO NÃO FORNECIDO] | Conversão de R$ 1.500,00 (Meta R$ 975,00) intacta; nenhum clique pago para destino errado | Reativar a diária anterior | 28/10; 03/11; 30/12; 06/01 |
| AMP19 | Evento de otimização lead (cadastro ou início de checkout, conforme o teste) e inscrição paga e 1ª mensalidade como conversões separadas, só para leitura (EM11) | Sem volume de inscrição para o algoritmo aprender | Sem custo | Funil de duas etapas medido por turma | Trocar o evento (reinicia o aprendizado) | teste em 30/10; aprovação até 30/11 |
| AMP20 | Públicos, região, exclusões e posicionamentos da seção 4: 18+; SP, ou GO e DF no frio; remarketing de 30 dias da página e 90 dias do Instagram, sem recorte de região; exclusão de compradores por 180 dias; posicionamentos manuais; melhorias automáticas desligadas | Não pagar duas vezes pela mesma pessoa e controlar onde a marca aparece | Sem custo | Menos sobreposição e leitura por posicionamento | Ampliar a região; voltar ao posicionamento automático; retirar exclusão | 30/11; 30/12 |
| AMP21 | Rodízio de conceitos (pedidos condicionais): se o CPL do frio passar de R$ 20,00 na 1ª semana fechada, pausar o pior dos 3 anúncios (nunca apagar); trocas semanais; volta dos 3 | CPL acima de R$ 20,00 não sustenta 3 conceitos ao mesmo tempo | Até 30% da verba da turma em teste (R$ 20,00 x 30 leads = R$ 600,00) | Verba concentrada no que converte | Voltar aos 3 no ar | março: lido em 21/12, vale em 04/01; abril: lido em 18/01 |
| AMP22 | Mínimo diário da plataforma: ler no gerenciador e, se a diária do remarketing ficar abaixo, aplicar a EM14 (parte do remarketing da fase vai para o frio da turma); decidir a manutenção de março, que a EM14 não cobre | Diárias de R$ 3,68 a R$ 10,00 no remarketing | Sem mudar o total da turma | Campanhas aceitas pela plataforma | Voltar o remarketing quando a diária couber | 30/11; 30/12 |
| AMP23 | Liberar as travas por escrito: P3 de 679, 68636 e 662; P4 de 366; U10 de 657; PP7 de 657 e 341; URL de 68617; c3 de 662 | Página com link trocado ou data divergente não recebe anúncio | Sem custo | Cada turma sobe só com destino certo | Voltar a turma ao estado bloqueado e pausar | antes de 07/12 (março) e de 06/01 (abril) |
| AMP24 | Limite de gasto por campanha (se o recurso existir), igual ao total da campanha na turma (seção 5.1); limite de gasto da conta acima da soma das diárias | A diária pode oscilar acima do valor em alguns dias [SUPOSIÇÃO de plataforma] e o teto de R$ 2.000,00 é do CEO | Sem aumento de verba | Teto por campanha respeitado | Retirar o limite, com aprovação | 30/11; 30/12 |

**Os 3 primeiros:** AMP19 (teste de rastreio de 30/10), AMP17 e AMP18 (gasto de 289 e 662, antes de 03/11) e AMP13 (estrutura de março, com a pergunta do D12). **Vão ao cmo:** AMP13 (nome com área curta) e AMP23 (liberação de P3 por exceção). Nenhum pedido muda a verba total nem o canal.

---

## 13. SUSPENSO (decisão 14): montagem das provas de bolsa e do pós-prova

**Estado: suspenso. Não executar.** A decisão 14 do CEO (26/10/2026) manda não produzir peças novas das provas de bolsa nem de Livres, e as encomendas das provas ficam suspensas até nova ordem (gestor-de-midia-pos 12.8; estrategia-de-midia-pos v4, seção 1). O conteúdo abaixo é o da versão 2 deste arquivo, guardado sem apagar e sem mudar o texto. Verba aparece como percentual da verba nova da Pós (VN) e o valor em reais é VN x percentual [CONFIRMAR]. As datas (03/11, 10/11, 26/11, 27/11) e os percentuais valiam na versão 2; se o CEO retomar as provas, tudo volta a passar pelo qa-de-marketing e pela conformidade, com as datas conferidas de novo. Nada desta seção sobe, muda, pausa ou gasta. O pedido de retomada seria novo, com nova ordem do CEO.

### 13.1 Regras próprias das provas (versão 2, seção 1)

| Regra | Valor nesta montagem | Fonte |
|---|---|---|
| Prova de bolsa | Online. Toda peça diz o campus da prova (São Paulo ou Goiânia). Sem endereço, sem "presencial", sem documento com foto, sem "sem celular". Data e horário como na ficha: 27/11/2026, das 9h às 13h. Acesso online: [CONFIRMAR, U2] | decisão 11; seção 12.9 |
| Bolsa | Só nas provas e no pós-prova, sempre com a distribuição completa (2 de 50% com monitoria, 4 de 25%, 5 de 10%) e "Bolsa não acumulativa e intransferível". Anúncio de turma não fala de bolsa | criativos-de-anuncio-pos, 1.1 a 1.3; 1.13, 4.1 |
| Crédito e ponte Livres para Pós | Nenhuma menção a crédito, combo ou desconto da ponte | D7 da seção 12.4 |
| Nomes | Campanha = chave + `_<plataforma>_<objetivo>_<público>_<AAAAMM>`; chave = `pos_provas20261127`. Conjunto = nome da campanha + `__` + público. Minúsculas, sem acento | D12 |
| Sobreposição | Sem exclusão de público entre campanhas e sem anúncio que misture ofertas. Registro lado a lado de CPM, alcance e frequência (EA3) | seção 12.6 |

**Divergência resolvida pela seção 12 do cmo (nota para quem monta):** a 1.13 (seção 4.2) usava a área curta na chave (`pos_68615-patclin_...`) e mantinha a UTM antiga das provas (`utm_medium=pago`, `utm_campaign=provas-de-bolsa-2026-11-27`). D11 e D12 mandam o padrão `meta` e `paid_social` também nas provas, porque os anúncios das provas ainda não subiram. A versão 2 seguiu D11 e D12. (Para as turmas, esta versão 3 segue a estratégia v4, que usa a área curta; ver a nota de nomes na seção 1.)

### 13.2 Modelo de estrutura das provas (versão 2, seção 2)

| Frente | Modelo | Motivo (2 a 3 linhas) |
|---|---|---|
| P1 Provas | Lançamento por fases, em 1 campanha de vendas com 3 conjuntos | Data fixa (27/11) e fases já escritas (40%, 35%, 25%, PP3). Um conjunto por praça e um de remarketing porque São Paulo, Goiânia e visitantes têm tamanhos muito diferentes; com orçamento na campanha, o algoritmo levaria quase tudo para São Paulo (EM5) |
| P2 Pós-prova | Enxuta: 1 campanha de remarketing, 1 conjunto por turma de destino confirmada | Público pequeno (visitantes das páginas da prova e da turma) e janela curta (10 dias úteis) |

Orçamento: nas provas, no conjunto; no pós-prova, na campanha. Nunca nos dois.

### 13.3 P1 Provas de bolsa (sobe em 03/11, pausa em 27/11)

```
pos_provas20261127_meta_compra_misto18_202611   (objetivo Vendas; orçamento no conjunto)
├── pos_provas20261127_meta_compra_misto18_202611__amplo18-sp
│     anúncios por área liberada (E1 em 03/11; E2 com decisão registrada):
│     c1-bolsas_<área>_e11_numero_v1, c1-bolsas_<área>_e916_numero_v1,
│     c2-entrada_<área>_e11_numero_v1, c2-entrada_<área>_e916_numero_v1,
│     c2-entrada_<área>_vid916_pergunta_v1 (se o vídeo estiver pronto),
│     c6-rotina_<área>_e11_cena_v1, c6-rotina_<área>_e916_cena_v1
├── pos_provas20261127_meta_compra_misto18_202611__amplo18-go
│     mesmos conceitos, com <área>-go (a1-anest-go, a4-cirurgia-go; a2-cardio-go só depois da correção dos links)
│     sobe só com a página de Goiânia dizendo prova online e campus Goiânia (AMP5)
└── pos_provas20261127_meta_compra_misto18_202611__rmk30d
      c4-regra_<área>_car_pergunta_v1 (carrossel "Como funciona")
      estático de remarketing da área (seção 13.6, C6)
```

Em 10/11 (fase 2) entram, por pedido, C3 reescrito (seção 13.6, só com U2 respondido), as iterações do vencedor (uma variável por vez) e as áreas de E5 com destino confirmado. C5 fica travado até A-C2.

| Campo | Valor |
|---|---|
| Objetivo da campanha | Vendas |
| Evento de otimização | Compra (inscrição de R$ 100,00) no pixel e na API de Conversões. Se o teste de 30/10 não mostrar a compra disparando, ou se a 1ª semana não registrar compra com volume, troca única para início de checkout, com aprovação (memorando 3.2; AMP3) |
| Categoria especial de anúncio | Nenhuma [SUPOSIÇÃO: educação não está entre as categorias especiais da Meta; conferir no gerenciador ao criar] |
| Idade | 18 anos ou mais |
| Região | __amplo18-sp: estado de São Paulo. __amplo18-go: Goiás e Distrito Federal. __rmk30d: sem recorte (EM6) |
| Público frio | Amplo, com sugestão de interesses profissionais ligados à medicina veterinária (Advantage+ de público, se a conta usar) [SUPOSIÇÃO de nome do recurso; conferir no gerenciador] |
| Remarketing | Visitantes das páginas de Pós e das provas nos últimos 30 dias (pixel) e quem engajou com o Instagram @ufapevet em 90 dias |
| Exclusões | Compradores da inscrição (evento de compra do pixel nas páginas das provas, 180 dias). Os conjuntos frios excluem __rmk30d. Nenhuma lista de contatos até a base legal [CONFIRMAR] |
| Posicionamentos | Facebook e Instagram: Feed, Stories, Reels e Explorar. Sem Audience Network e sem Messenger [SUPOSIÇÃO de desenho: leitura por posicionamento e controle de onde a marca aparece; se o gerenciador marcar o público como pequeno, voltar aos posicionamentos automáticos com aprovação] |
| Limite de frequência | Em objetivo de Vendas o limite fixo pode não estar disponível [SUPOSIÇÃO de plataforma; conferir]. Controle por leitura diária de frequência e troca de anúncio (EM12) |
| Data de término programada | 26/11/2026, 23h59, nos três conjuntos (pausa de A-C6 confirmada em 23/11) |

### 13.4 P2 Pós-prova (sobe na data do resultado [CONFIRMAR], pausa no fim dos 10 dias úteis)

```
pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM do resultado>   (Vendas; orçamento na campanha)
└── um conjunto por turma de destino confirmada: ...__rmk-prova-<código da turma>
      c5-turma_<área>_e11_resultado_v1 (só depois de A-C2)
      <código da turma>-c2-investimento_e11_numero_v1 (seção 5.8 da versão 2, que continha preço e não foi mantida)
```

Observação de nome: a chave `pos_provas20261127-matricula` é a da 1.13 (seção 4.6). D12 não prevê chave para o pós-prova; proponho mantê-la para separar a leitura da inscrição da leitura da matrícula (AMP6).

| Campo | Valor |
|---|---|
| Evento | Compra do produto da turma de destino; se não houver volume, início de checkout |
| Público | Visitantes, em 30 dias, da página da prova da área e da página da turma de destino. É público de visitantes, não de aprovados: o texto vale para quem fez e para quem não fez a prova |
| Exclusões | Compradores da turma de destino (pixel, 180 dias) |
| Texto | Sem prazo de matrícula até U1 e U3 responderem; sem valor com bolsa; com o investimento completo da turma |

### 13.5 Verba das provas e do pós-prova (versão 2, seção 4; percentual de VN, reais = VN x percentual [CONFIRMAR])

Todos os percentuais vêm da 1.13 (seções 3.1 a 3.3). Diária = parte da fase dividida pelos dias da fase.

**P1 Provas, Meta, por conjunto e fase**

| Fase (dias) | __amplo18-sp | __amplo18-go | __rmk30d | Total Meta da fase | Diária SP / GO / rmk (em VN) |
|---|---|---|---|---|---|
| 1. 03/11 a 09/11 (7) | 5,8800% | 1,2600% | 1,2600% | 8,4000% | 0,8400% / 0,1800% / 0,1800% |
| 2. 10/11 a 19/11 (10) | 4,7775% | 1,1025% | 1,4700% | 7,3500% | 0,4778% / 0,1103% / 0,1470% |
| 3. 20/11 a 26/11 (7) | 2,2500% | 0,4500% | 1,8000% | 4,5000% | 0,3214% / 0,0643% / 0,2571% |
| **Total** | 12,9075% | 2,8125% | 4,5300% | **20,2500%** | |

Enquanto Goiânia estiver bloqueada, a parte de __amplo18-go passa para __amplo18-sp na mesma fase (1.13, 3.1). Área bloqueada não guarda verba. Leads por semana esperados = verba semanal do conjunto dividida pelo CPImax da área [CONFIRMAR em PP1]; sem CPImax, [DADO NÃO FORNECIDO]. Condição de volume da 1.13: VN mínima = 50 x CPImax com 4 conceitos, ou 25 x CPImax na versão enxuta (só C1 e C6).

**P2 Pós-prova:** 5,00% de VN no total, em partes iguais por turma de destino confirmada. Diária = 5% de VN dividido pelos dias corridos da janela [CONFIRMAR data do resultado] e pelo número de turmas de destino.

### 13.6 Anúncios das provas (versão 2, seção 5)

Contagem de caracteres: a primeira frase do texto principal aparece entre parênteses, seguida do número de caracteres. Títulos até 40 e descrições até 30 (referência de plataforma [SUPOSIÇÃO]; conferir a prévia no gerenciador). Em Stories e Reels a mensagem está dentro da arte: o texto principal complementa. Quando a primeira frase passa de cerca de 125 caracteres (textos em lista e de investimento), só o começo aparece antes do "ver mais": por isso esses textos põem curso, data e preço logo no início.

Exemplos preenchidos com as duas provas que sobem em 03/11 sem pendência (E1): 68654 Neurologia e 68658 Patologia Clínica. As demais áreas usam o mesmo texto, trocando {nome curto} e {nome completo} pela tabela da seção 4.1 do criativos-de-anuncio-pos e o campus pela praça da prova.

#### 13.6.1 Corpo fixo das provas (substitui BODY_SP e BODY_GO do criativos-de-anuncio-pos)

- **Corpo São Paulo:** "Prova de bolsa do campus São Paulo da Faculdade UFAPE, online, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). São 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Bolsa não acumulativa e intransferível. Regras completas na página da prova."
- **Corpo Goiânia:** igual, com "campus Goiânia". Sem endereço. Sem prazo de matrícula e sem canal do resultado em nenhuma prova até U1 (12 fichas têm versões contraditórias: 68641, 68642, 68643, 68644, 68645, 68650, 68651, 68652, 68653, 68657, 68659, 68661).
- **Fica de fora de todo texto das provas:** "presencial", endereço, "documento com foto", "sem celular", "sem relógio", data do resultado, prazo de inscrição, turma de destino (até A-C2).

#### 13.6.2 C1. 11 bolsas por prova (frio, São Paulo e Goiânia)

Nomes: `c1-bolsas_a12-neuro_e11_numero_v1`, `c1-bolsas_a11-patclin_e11_numero_v1` e as versões e916.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | Prova de bolsa de Neurologia: 11 bolsas, de 10% a 50%. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia: 11 bolsas, de 10% a 50%." (54) |
| 2 | Curto, pergunta | Quantas bolsas tem a prova de Patologia Clínica? São 11 por prova. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Quantas bolsas tem a prova de Patologia Clínica?" (48) |
| 3 | Lista de benefícios (longo) | 11 bolsas na prova da Pós-graduação em Neurologia e Neurocirurgia Veterinária. 2 bolsas de 50%, com monitoria. 4 bolsas de 25%. 5 bolsas de 10%. Nota de corte 7,0, com questões de múltipla escolha e dissertativas. Desempate por análise de currículo. + corpo São Paulo | "11 bolsas na prova da Pós-graduação em Neurologia e Neurocirurgia Veterinária." (78) |
| 4 | Objeção primeiro | Não é uma bolsa só: a prova de Patologia Clínica tem 11, de 10% a 50%. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Não é uma bolsa só: a prova de Patologia Clínica tem 11, de 10% a 50%." (70) |
| 5 | Curto, data | Sexta, 27/11: prova de bolsa online de Neurologia, com 11 bolsas. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. Regras na página da prova. | "Sexta, 27/11: prova de bolsa online de Neurologia, com 11 bolsas." (65) |

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova de bolsa: Neurologia" (26) | "Inscrição de R$ 100,00" (22) |
| "11 bolsas por prova" (19) | "Prova online em 27/11" (21) |
| "Bolsas de 10% a 50%, na distribuição" (36) | "Campus São Paulo" (16) |
| "Prova online de bolsa em 27/11" (30) | |
| "Prova de bolsa: Patologia Clínica" (33) | |

O título "Bolsas de 10% a 50%, na distribuição" só vai junto de texto principal que traga a distribuição completa (todos os cinco trazem). Para Goiânia, a descrição "Campus Goiânia" (14).

- **Chamada:** "Saiba mais". Motivo: o frio ainda não conhece a prova; "Saiba mais" leva à página com as regras, e o botão da página é "COMPRAR".
- **Combinação para o 1º teste (T1 do criativos):** arte `c1-bolsas_<área>_e11_numero_v1` + texto 1 + título "Prova de bolsa: {nome curto}" + descrição "Inscrição de R$ 100,00", contra a combinação de C2 da seção 13.6.3. Mesmo conjunto, mesma área, mesmo formato.

#### 13.6.3 C2. R$ 100,00 para concorrer (frio)

Nomes: `c2-entrada_<área>_e11_numero_v1`, `_e916_numero_v1`, `_vid916_pergunta_v1`.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | Concorrer a uma bolsa da Pós-graduação em Neurologia e Neurocirurgia Veterinária custa R$ 100,00. É a inscrição na prova online do campus São Paulo, em 27/11/2026: Pix, boleto ou 1x no cartão. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Concorrer a uma bolsa da Pós-graduação em Neurologia e Neurocirurgia Veterinária custa R$ 100,00." (97) |
| 2 | Curto, pergunta | Quanto custa concorrer a uma bolsa de pós-graduação? R$ 100,00. Prova online de Patologia Clínica, campus São Paulo, em 27/11/2026, das 9h às 13h. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Quanto custa concorrer a uma bolsa de pós-graduação?" (52) |
| 3 | Problema, agitação e solução (longo) | O valor total de uma pós-graduação pesa na decisão. A prova de bolsa existe para isso: com a inscrição de R$ 100,00, você concorre a uma das 11 bolsas da prova de Neurologia. São 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. A inscrição é só a entrada na prova: as condições da pós estão na página da turma. + corpo São Paulo | "O valor total de uma pós-graduação pesa na decisão." (51) |
| 4 | Antes, depois e ponte | Hoje: o preço cheio da pós. Depois da prova: a chance de uma bolsa de 10% a 50%. A ponte é a inscrição de R$ 100,00 na prova online de Patologia Clínica, campus São Paulo, em 27/11/2026. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Hoje: o preço cheio da pós." (27) |
| 5 | Curto, número | R$ 100,00 para concorrer a uma das 11 bolsas da prova de Neurologia. Prova online, campus São Paulo, 27/11/2026. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "R$ 100,00 para concorrer a uma das 11 bolsas da prova de Neurologia." (68) |

Cuidado de verdade nos textos 3 e 4: nenhum diz que a bolsa é certa nem que R$ 100,00 é o único custo; "a chance" e "concorre" descrevem o que a inscrição dá. O texto 3 fala do preço da pós de forma geral, sem afirmar a situação financeira de quem lê.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "R$ 100,00 para concorrer" (24) | "11 bolsas por prova" (19) |
| "Inscrição de R$ 100,00 na prova" (31) | "Prova online em 27/11" (21) |
| "Prova de bolsa: Neurologia" (26) | "Bolsas de 10% a 50%" (19) |
| "Inscrição na prova: R$ 100,00" (29) | |
| "Prova em 27/11: Patologia Clínica" (33) | |

- **Chamada:** "Saiba mais" (mesmo motivo de C1).
- **Combinação para o 1º teste:** `c2-entrada_<área>_e11_numero_v1` + texto 5 + título "R$ 100,00 para concorrer" + descrição "11 bolsas por prova". O vídeo `c2-entrada_<área>_vid916_pergunta_v1` entra com o texto 2 se estiver pronto em 03/11.
- **Vídeo (roteiro da seção 3.8 do criativos):** o quadro de 8 a 14 s muda para "Prova online / Sexta, 27/11/2026, das 9h às 13h / Campus São Paulo" e a locução opcional para "A prova é online, em 27 de novembro, das 9 às 13 horas." Sai "Documento com foto".

#### 13.6.4 C3 reescrito. Prova online, 27/11, das 9h às 13h (fase 2, só com U2 respondido)

O conceito original (logística da prova presencial, local, documento e celular) deixou de ser verdade com a decisão 11. A versão reescrita mantém o ângulo "economia de incerteza", agora sobre o formato online e o campus. Sobe em 10/11 só se a Ufape responder U2 (plataforma, acesso e regras do dia) e a página da prova disser "online". Nomes: `c3-online_<área>_e916_data_v1`, `c3-online_<área>_e11_data_v1`.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto, data | Sexta, 27/11, das 9h às 13h: a prova de bolsa de Neurologia é online. Campus São Paulo. Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Sexta, 27/11, das 9h às 13h: a prova de bolsa de Neurologia é online." (69) |
| 2 | Curto, pergunta | Como é a prova de bolsa de Patologia Clínica? Online, em 27/11/2026, das 9h às 13h. Questões de múltipla escolha e dissertativas. Nota de corte 7,0. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Como é a prova de bolsa de Patologia Clínica?" (45) |
| 3 | Lista (longo) | Prova de bolsa de Neurologia, em 4 pontos. 1. Online, em 27/11/2026, das 9h às 13h. 2. Questões de múltipla escolha e dissertativas. 3. Nota de corte 7,0; desempate por análise de currículo. 4. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Campus São Paulo. Inscrição de R$ 100,00. Como acessar a prova: na página da prova [CONFIRMAR U2]. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia, em 4 pontos." (42) |
| 4 | Objeção primeiro | A prova é online: o campus indica a turma, não o lugar da prova. Prova de bolsa de Patologia Clínica, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "A prova é online: o campus indica a turma, não o lugar da prova." (64) |
| 5 | Curto direto | Prova de bolsa online, campus São Paulo: Neurologia, 27/11. Das 9h às 13h. Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Prova de bolsa online, campus São Paulo: Neurologia, 27/11." (59) |

O texto 4 traduz a decisão 11 ("o local não importa, mas a peça diferencia o campus"); a formulação "o campus indica a turma" é leitura deste agente [SUPOSIÇÃO] e vai à Ufape junto com U2 antes de subir.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova online em 27/11" (21) | "Das 9h às 13h" (13) |
| "Prova de bolsa online: Neurologia" (33) | "Campus São Paulo" (16) |
| "Das 9h às 13h, online" (21) | "Inscrição de R$ 100,00" (22) |
| "Como é a prova de bolsa" (23) | |
| "Prova online: Patologia Clínica" (31) | |

- **Chamada:** "Saiba mais".
- **Arte 9:16 (sequência de 3 Stories), troca dos quadros do criativos:** quadro 1 "Prova de bolsa online / Sexta, 27/11/2026 / Das 9h às 13h"; quadro 2 "Múltipla escolha e dissertativas / Nota de corte 7,0"; quadro 3 "Campus São Paulo (ou Goiânia) / Inscrição de R$ 100,00 / 11 bolsas por prova". Sem endereço.

#### 13.6.5 C4. Nota de corte 7,0 e carrossel "Como funciona" (remarketing)

Nomes: `c4-regra_<área>_car_pergunta_v1` (carrossel) e `c4-regra_<área>_e11_pergunta_v2` (iteração de formato, fase 2).

**Troca no carrossel do criativos (seção 3.7):** cartão 3 passa a "2. A prova / 27/11/2026, das 9h às 13h / Online. Campus São Paulo (ou Goiânia)", título do cartão "Prova online em 27/11" (21). Cartão 6 (resultado, recurso, matrícula) continua travado até U1 e U3. Nenhum cartão cita endereço, documento ou celular.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto, pergunta | Como funciona a prova de bolsa de Neurologia, passo a passo. Inscrição de R$ 100,00, prova online em 27/11/2026, das 9h às 13h, e 11 bolsas por prova. Passe os cartões. Bolsa não acumulativa e intransferível. | "Como funciona a prova de bolsa de Neurologia, passo a passo." (60) |
| 2 | Curto, número | Nota de corte 7,0: é o que a prova de bolsa de Patologia Clínica exige. Mínimo de 70% de acerto. Prova online, campus São Paulo, 27/11/2026. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Nota de corte 7,0: é o que a prova de bolsa de Patologia Clínica exige." (71) |
| 3 | Objeção primeiro (longo) | E se empatar? Na prova de bolsa de Neurologia, o desempate é por análise de currículo. A nota de corte é 7,0 (mínimo de 70% de acerto), em questões de múltipla escolha e dissertativas. Atingir a nota não garante bolsa: a distribuição das 11 bolsas segue as regras da página da prova. + corpo São Paulo | "E se empatar?" (13) |
| 4 | Lista | Prova de bolsa de Patologia Clínica: inscrição de R$ 100,00; prova online em 27/11, das 9h às 13h; nota de corte 7,0; 11 bolsas (2 de 50% com monitoria, 4 de 25%, 5 de 10%). Campus São Paulo. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Patologia Clínica: inscrição de R$ 100,00; prova online em 27/11, das 9h às 13h; nota de corte 7,0; 11 bolsas (2 de 50% com monitoria, 4 de 25%, 5 de 10%)." (173) |
| 5 | Curto direto, remarketing | A prova de bolsa de Neurologia é em 27/11/2026, das 9h às 13h, online. Veja as regras e inscreva-se. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "A prova de bolsa de Neurologia é em 27/11/2026, das 9h às 13h, online." (70) |

O texto 4 é uma frase única longa: só os primeiros cerca de 125 caracteres aparecem antes do "ver mais", e eles já trazem inscrição, data e nota. Uso só no estático, não no carrossel.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Como funciona a prova de bolsa" (30) | "Desempate por currículo" (23) |
| "Nota de corte 7,0" (17) | "Inscrição de R$ 100,00" (22) |
| "Prova de bolsa em 27/11" (23) | "Prova online em 27/11" (21) |
| "Regras da prova de bolsa" (24) | |
| "Prova online: Neurologia" (24) | |

- **Chamada:** "Inscreva-se" no remarketing [SUPOSIÇÃO: rótulo disponível na lista de chamadas da Meta; se não houver, "Saiba mais"]. Motivo: quem já visitou a página conhece a prova; a chamada combina com a ação da página (comprar a inscrição).
- **Combinação para o 1º teste (T3 do criativos):** carrossel com o texto 1 + título "Como funciona a prova de bolsa" + descrição "Inscrição de R$ 100,00", contra `c1-bolsas_<área>_e11_numero_v1` com o texto 1 de C1, no conjunto __rmk30d.

#### 13.6.6 C6. Rotina da especialidade (camada de área, frio)

Nomes: `c6-rotina_<área>_e11_cena_v1`, `_e916_cena_v1`, `_e11_numero_v2` (iteração, fase 2). Os ganchos de rotina vêm do criativos (seção 4.2) e são [SUPOSIÇÃO] de tema, não fala de aluno.

| # | Estrutura | Texto principal (Neurologia, 68654) | Primeira frase |
|---|---|---|---|
| 1 | História curta da rotina (gancho B) | O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11. Prova de bolsa para a Pós-graduação em Neurologia e Neurocirurgia Veterinária. + corpo São Paulo | "O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (89) |
| 2 | Curto, número (gancho A) | Neurologia: 11 bolsas por prova, inscrição de R$ 100,00. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Neurologia: 11 bolsas por prova, inscrição de R$ 100,00." (56) |
| 3 | Lista de benefícios | Prova de bolsa de Neurologia: o que você encontra na página. Data e horário (27/11/2026, das 9h às 13h, online). As 11 bolsas e a distribuição (2 de 50% com monitoria, 4 de 25%, 5 de 10%). Nota de corte 7,0 e desempate por currículo. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia: o que você encontra na página." (60) |
| 4 | Curto direto | A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11. Campus São Paulo. Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11." (93) |
| 5 | Pergunta sobre o tema (longo) | Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa? A prova de 27/11 distribui 11 bolsas para a Pós-graduação em Neurologia e Neurocirurgia Veterinária: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. A nota de corte é 7,0. A bolsa não é garantida: a distribuição segue as regras da página. + corpo São Paulo | "Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa?" (67) |

Patologia Clínica (68658): mesmos cinco, com o gancho B "Os exames laboratoriais na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (90) e o nome completo como na seção 2 do catálogo, "Pós-graduação em Patologia Clínica" (turma 68615), ou o nome da prova como na seção 3 ("prova de bolsa de Patologia Clínica Veterinária") até A-C2 dizer a turma de destino. Nunca "Pós-graduação em Patologia Clínica Veterinária", que não existe no catálogo (AMP-Q2).

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova de bolsa: Neurologia" (26) | "Inscrição de R$ 100,00" (22) |
| "Prova em 27/11: Neurologia" (26) | "11 bolsas por prova" (19) |
| "Prova de bolsa: Patologia Clínica" (33) | "Prova online, campus SP" (23) |
| "Prova em 27/11: Patologia Clínica" (33) | |
| "Neurologia: prova online em 27/11" (33) | |

Nenhum título usa "Pós em" ou abreviação do nome do curso: a regra da 1.13 (4.1) reserva essas formas para palavra-chave.

- **Chamada:** "Saiba mais".
- **Combinação para o 1º teste (T2 do criativos):** `c6-rotina_<área>_e11_cena_v1` + texto 1 + título "Prova de bolsa: {nome curto}" + descrição "Inscrição de R$ 100,00", contra `c1-bolsas_<área>_e11_numero_v1` na mesma área.

#### 13.6.7 C5. A bolsa vale para a turma de {mês} (travado)

Não sobe até A-C2 (destino por prova) e até a página da prova trazer o bloco de destino. Quando liberar, usa o modelo da seção 3.9 do criativos com duas trocas: "A prova é presencial" vira "A prova é online"; "A turma é confirmada quando atinge o número mínimo de alunos" vira "A turma é confirmada com o mínimo de 15 alunos" (decisão 11). Título: "A bolsa vale para a turma de {mês}" (até 37). Chamada: "Saiba mais".

### 13.7 UTM das provas e do pós-prova (versão 2, seção 7)

Campo "Parâmetros de URL" do anúncio (não na URL de destino), para não quebrar a URL da página [SUPOSIÇÃO de boa prática de plataforma].

| Campanha | Modelo de parâmetros |
|---|---|
| Provas, frio SP | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127_meta_compra_misto18_202611&utm_content=c1-bolsas_a12-neuro_e11_numero_v1&utm_term=amplo18-sp` |
| Provas, frio GO | idem, com `utm_content=<anúncio>-go` e `utm_term=amplo18-go` |
| Provas, remarketing | idem, com `utm_content=c4-regra_a12-neuro_car_pergunta_v1&utm_term=rmk30d` |
| Pós-prova | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM>&utm_content=<anúncio>&utm_term=rmk-prova-<código da turma>` |

### 13.8 Protocolo de teste das provas (versão 2, seção 8, coluna das provas)

| Item | Provas (P1) |
|---|---|
| Leitura permitida | gasto de pelo menos 1,5 x CPImax da área e 3 dias de dados; nenhuma realocação antes de 06/11 |
| Pausa de anúncio | 1,5 a 2 x CPImax sem inscrição; nunca todos os antigos juntos |
| Promoção à escala | menor custo por inscrito abaixo do CPImax, em 2 leituras seguidas |
| Cadência de criativo novo | fase 1 sem criativo novo; fase 2 (10/11) entra C3 e as iterações; reta final sem conceito novo |
| Uma mudança por conjunto | no máximo uma por semana; correção de conformidade quando achada |
| Últimos 2 dias | não entram em tendência |
| Sobreposição (A1 e A12 com o Workshop Brasileiro de Neuromonitorização) | de 20/11 a 26/11, se frequência subir e CTR cair por 3 dias seguidos, troca do anúncio mais cansado por ângulo pronto, sem cortar verba antes de 23/11 (EM12); CPM subindo com CTR estável de 03/11 a 18/11 é lido como disputa de leilão (NE4), com registro lado a lado (EA3) |

CPImax: [CONFIRMAR em PP1]. Sem ele, nenhuma campanha das provas sobe.

### 13.9 Itens do checklist próprios das provas (versão 2, seção 9)

| # | Item | Provas (03/11) |
|---|---|---|
| S2 | Pixel e API de Conversões recebendo o evento escolhido na página de destino (teste de 30/10, com compra de R$ 100,00 nas provas) | obrigatório |
| S4 | Evento de otimização certo no conjunto (compra ou início de checkout) | obrigatório |
| S7 | Página de destino confere com o anúncio: nas provas, diz "online" (AMP2); sem endereço contraditório; Goiânia com o campus certo; Cardiologia com links corrigidos | obrigatório |
| S8 | Página com frase de certificação ligada ao MEC: só com decisão registrada da pessoa do marketing ou com a página corrigida (estado E2) | obrigatório nas 5 provas E2 |
| S11 | Data de término programada (26/11 nas provas) | obrigatório |
| P1 (pausa) | Pausa aprovada antes (A-C6 nas provas, confirmada em 23/11). Pausas previstas: provas em 27/11 (término programado em 26/11, 23h59); pós-prova no fim dos 10 dias úteis [CONFIRMAR] | obrigatório |

### 13.10 Pedidos das provas (versão 2, AMP1 a AMP6, AMP10 e AMP12), todos suspensos

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AMP1 | Estrutura das provas da seção 13.3 (1 campanha, 3 conjuntos, orçamento no conjunto) com nomes e UTM de D11 e D12 desde 03/11, substituindo a UTM antiga do criativos e a exceção de EM2 e PP4 | D12 manda as provas no padrão, porque ainda não subiram | dentro de P1: 20,25% de VN na Meta [CONFIRMAR reais] | relatório das provas somando com as demais linhas | trocar os parâmetros de URL (não reinicia aprendizado [SUPOSIÇÃO]) | 30/10 |
| AMP2 | Textos das provas reescritos (seções 13.6.1 a 13.6.6): "online" e campus no lugar de "presencial", endereço, documento e celular; pedido à Ufape para as 22 páginas das provas dizerem "online" antes de 03/11 | decisão 11; a página precisa entregar o que o anúncio diz | sem verba | anúncio e página coerentes | voltar ao texto anterior só se a Ufape revogar a decisão 11 | 30/10 (páginas até 02/11) |
| AMP3 | Evento de otimização das provas: compra; troca única para início de checkout se o teste de 30/10 falhar ou não houver volume na 1ª semana | a compra de R$ 100,00 tem pouco volume por área | sem verba | campanha aprende com um evento que registra | trocar o evento (reinicia aprendizado) | 30/10 |
| AMP4 | Posicionamentos manuais (Feed, Stories, Reels, Explorar), sem Audience Network nem Messenger | leitura por posicionamento e controle de onde a marca aparece | sem verba | menos entrega fora do Instagram e do Facebook | voltar ao automático | 30/10 |
| AMP5 | Conjunto de Goiânia só depois de as páginas 68640, 68642 e 68644 dizerem "online" e "campus Goiânia" (o endereço de São Paulo deixa de ser o bloqueio, pela decisão 11, mas a página ainda diz presencial); Cardiologia só com os links corrigidos | página coerente com o anúncio | 2,8125% de VN no conjunto GO; enquanto bloqueado, vai para SP na mesma fase | entrega em Goiânia sem destino errado | pausar o conjunto | 31/10 |
| AMP6 | Estrutura do pós-prova (seção 13.4) com a chave pos_provas20261127-matricula | separar a leitura de inscrição e de matrícula | 5% de VN | matrículas com bolsa lidas por turma de destino | renomear antes da subida | data do resultado [CONFIRMAR] |
| AMP10 | Registro lado a lado de CPM, alcance e frequência dos conjuntos de A1 e A12 com o Workshop Brasileiro de Neuromonitorização e a 616 (EA3) e regra de fadiga de EM12 | sobreposição de 03/11 a 18/11 (seção 12.6) | sem verba | decisão de 09/11 e 10/11 sem confundir leilão com criativo fraco | não se aplica | 06/11 e 09/11 |
| AMP12 | C3 reescrito só em 10/11 e só com U2 respondido; C5 só com A-C2 | sem o acesso online confirmado, o texto não pode explicar a prova | dentro de P1 | conceito de logística verdadeiro | não subir | 09/11 |

(AMP7, AMP8, AMP9 e AMP11 da versão 2 eram das turmas e do campo de UTM; foram substituídos pelos pedidos AMP13 a AMP24 e pela seção 6.3.)

### 13.11 Pendências e suposições próprias das provas (versão 2)

- [CONFIRMAR] U2: plataforma, acesso e regras do dia da prova online; páginas das provas atualizadas para "online" com o campus.
- [CONFIRMAR] U1 e U3: prazo de matrícula, canal e data do resultado, fim das inscrições; sem isso, nenhum texto cita prazo.
- [CONFIRMAR] A-C2: turma de destino de cada prova (libera C5 e P2); U4 para as 4 provas sem turma.
- [CONFIRMAR] Correção dos links de Cardiologia (68641 e 68642) e das páginas de Goiânia.
- [CONFIRMAR] Decisão registrada sobre as 5 provas em E2 (página com frase ligada ao MEC).
- [CONFIRMAR] VN em reais, aprovador e quem executa no gerenciador (PP2); CPImax por área (PP1).
- [SUPOSIÇÃO] Limite de frequência fixo indisponível no objetivo Vendas; posicionamentos manuais; limites de 40 caracteres no título e 30 na descrição como referência de exibição; rótulos "Inscreva-se" e "Cadastre-se" disponíveis na lista da Meta; troca de parâmetros de URL não reinicia o aprendizado; "o campus indica a turma, não o lugar da prova" como leitura da decisão 11 (texto 4 de C3); ganchos de rotina por área (do criativos) como tema, não como fala de aluno.

---

## 14. Auditorias

### 14.1 auditorias/11-midia-paga.md (aplicada à montagem das turmas)

| Item | Resultado | Observação |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais ativados e fora justificados | Pendente externo | Meta e Google Busca; YouTube e LinkedIn fora (PP13 e PP14 ao cmo); aprovação em PP16 |
| Metas de CPL e custo por matrícula escritas antes de subir | Atendido em parte | Seção 1: R$ 133,33, R$ 4,00, R$ 10,00 e R$ 18,00; taxas [SUPOSIÇÃO ilustrativa]; taxas reais [CONFIRMAR] |
| Verba dentro do valor aprovado, com aprovador registrado | Atendido em parte | Meta R$ 1.295,00 e R$ 1.325,00 por turma dentro dos R$ 2.000,00; 289 e 662 com limite de R$ 500,00; aprovador de "Anúncios e verba" [CONFIRMAR] |
| Nomenclatura padrão | Atendido no desenho | Seção 3; chave com área curta [CONFIRMAR com o cmo, AMP13] |
| UTMs completas e origem chegando ao CRM | Pendente externo | Seção 6.3; chegada ao CRM depende do teste de 30/10 |
| Pixel e API de Conversões | Pendente externo | AMP19 e teste de 30/10; TikTok e LinkedIn fora |
| Criativos aprovados em conformidade-educacional | Atendido nas peças, pendente a subida | Peças do criativos v3 aprovadas; página de cada turma conferida antes de subir (S7 e S9) |
| Anúncios dentro das políticas de cada plataforma | Atendido no desenho [SUPOSIÇÃO] | Sem atributo pessoal, sem escassez, sem preço; regras da Meta sem fonte marcadas |
| Nenhum público com menores de 18 anos | Atendido no desenho | 18+ na seção 4 |
| Post de docente promovido com autorização registrada | Atendido no desenho | Só nome e titulação em texto e arte (decisões 8 e 10); nenhuma imagem de docente |
| Relatório semanal ao CMO | Pendente externo | Seção 9 e seção 6.2 da estratégia |
| Sem segmentação discriminatória | Atendido | Seção 4; exclusões só por comportamento (compra, visita, engajamento) |
| Públicos sem dados pessoais usados sem base legal | Atendido | Nenhuma lista de contatos |
| Dados de curso conferidos no catálogo | Atendido | Datas, praças, turmas e modalidade do catálogo, seção 2; divergências em 68636, 366, 68617, 68628 e 662 marcadas |
| Destino de WhatsApp | Não se aplica | A mídia leva à página da turma (seção 10) |
| Números só das exportações | Atendido | Nenhum número de mídia observado; contas só com a verba e a meta do CEO e as divisões da estratégia; leads por semana são aritmética sobre CPL [SUPOSIÇÃO ilustrativa] |
| Nenhuma alteração feita na plataforma sem um humano executar e aprovar | Atendido | Seções 5.5, 8 e 12 escritas como pedido |

### 14.2 auditorias/conformidade-educacional.md (bloco de anúncios, preço e dados)

Esta versão não escreve texto de anúncio: os textos são os do criativos v3, que já passaram pelo bloco. O que cabe aqui é o que este arquivo muda ou promete.

| Bloco | Resultado | Observação |
|---|---|---|
| Dados do curso batem com o catálogo | Atendido | Nomes "Pós-graduação em <área>", campus, início e modalidade do catálogo, seção 2; 68632 presencial; 68636 com data [CONFIRMAR] |
| Status "aberto" | Atendido | As 14 turmas estão "aberto" no catálogo; 679, 68636 e 662 com bloqueio de página (seção 8) |
| Pós sem frase de certificação | Atendido | Nenhum anúncio cita; páginas com a frase sinalizadas (S8) |
| Sem promessa de emprego, salário, aprovação ou bolsa | Atendido | Nenhum anúncio de turma fala de bolsa |
| Preço com parcelas, valor, total e matrícula | Atendido | Nenhum anúncio mostra preço até U11; o investimento fica na página |
| Urgência real | Atendido | Só a data de início da planilha e a informação de turma que pode não ser formada, sem número |
| Autorização de imagem | Atendido | Docentes só por nome (c3); nenhuma imagem de pessoa |
| Característica pessoal de quem vê | Atendido | Textos aprovados descrevem o curso; público definido por praça, comportamento e 18+ |
| Menores de idade | Atendido | 18+ |
| Formulários com finalidade e política de privacidade | Pendente externo | Conferir na página de cada turma antes de subir |
| Destino entrega o que o anúncio promete | Pendente externo | 679, 68636 e 662 (P3), 366 (P4), 68617 (URL), 657 (U10), 341 (PR7 e local da prática) |
| Sem sugestão para driblar a análise das plataformas | Atendido | Melhorias automáticas desligadas; nenhuma troca de conteúdo depois de aprovado |
| Sem travessão nem meia-risca | Atendido | Conferido na leitura do arquivo |

**Resultado:** pronto para a conferência do qa-de-marketing e, depois, para a aprovação humana dos pedidos AMP13 a AMP24. Nenhuma campanha sobe antes disso nem antes da liberação das travas da seção 8.

---

## Mudanças desta versão

**Versão 3 (27/10/2026)**, por encomenda da estrategia-de-midia-pos v4 (seção 7), do gestor-de-midia-pos v5 (12.8) e da decisão 14 do CEO:

- **Provas e pós-prova suspensos (decisão 14):** a montagem das provas de bolsa (P1) e do pós-prova (P2) saiu do corpo do arquivo e ficou na seção 13, marcada "suspenso (decisão 14)", com o texto da versão 2 sem alteração (regras, mapa, verba em percentual de VN, anúncios C1 a C6, UTM, protocolo, itens de checklist e pedidos AMP1 a AMP6, AMP10 e AMP12).
- **Corpo do arquivo agora só de turmas:** 2 campanhas Meta por turma (frio `amplo18` da praça e remarketing `rmk30d`), 1 conjunto em cada, orçamento na campanha, para as 14 turmas de março e abril.
- **Verba em reais:** saem os percentuais de VN e a reserva P6; entram R$ 1.295,00 (março) e R$ 1.325,00 (abril) por turma na Meta, com diária por fase e por semana, trocas em 21/12, 04/01 e 25/01, leads por semana no CPL máximo, limite de volume da tabela 3.6, mínimo diário [CONFIRMAR no gerenciador] e regra EM14 com os valores de cada caso (seção 5).
- **Anúncios ligados às peças aprovadas do criativos v3:** 3 no frio, prontos para o rodízio, e 2 no remarketing, com as 2 artes 9:16 de cada turma anexas; 70 anúncios, com nomes e parâmetros de URL completos (seção 6). Saem os textos de anúncio da versão 2 (seções 5.8 e 5.9), que mostravam preço e valor de matrícula, contra as decisões 15 e 16 e a U11; o texto de cada anúncio é o do criativos v3. A chave da campanha passa a ter a área curta (`pos_<código>-<área>`), como na estratégia v4 e no criativos v3; a versão 2 usava só o código (nota na seção 1).
- **Evento de otimização:** lead (cadastro ou início de checkout, conforme o teste de 30/10); inscrição paga e 1ª mensalidade como conversões separadas, só para leitura (EM11). Sai o evento de compra, que valia para as provas.
- **289 e 662 (seção 7):** sem renomear, gasto informado [DADO NÃO FORNECIDO], limite de R$ 500,00 até a véspera, fórmulas de recálculo para 30/11 e 30/12, ficha de preenchimento e pausa da campanha atual no dia da subida da nova [SUPOSIÇÃO].
- **Travas de subida (seção 8):** P3 de 679, 68636 e 662; c3 de 662; P4 de 366; U10 de 657; PP7 de 657 e 341; URL de 68617.
- **Pausa no dia seguinte ao corte (EM16)** com as sete datas e o checklist de pausa (seção 11.2).
- **Pedidos:** AMP13 a AMP24 no formato o que, por que, quanto, efeito e como desfazer. AMP7 a AMP9 e AMP11 da versão 2 foram substituídos.
- **Formulário e WhatsApp:** seguem fora (seção 10).
- Histórico da versão 2 (correções do loteD, mantidas dentro da seção 13): AMP-Q1 (título de C2 "Inscrição na prova: R$ 100,00"), AMP-Q2 (nome da pós de 68658 em C1, C6 e nos textos com 68658) e AMP-Q3 (sem prazo de matrícula e sem canal do resultado em nenhuma prova até U1, com as 12 fichas contraditórias).

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 de mídia por turma de Pós no ciclo; meta de 15 matrículas; meta em reais de 15 vezes o valor do curso; inscrição de R$ 260,00 medida separada da 1ª mensalidade; nenhuma peça cita o valor da inscrição até U11; provas de bolsa e Livres fora desta rodada (docs/execucao-2026-10-26.md, decisões 14, 15 e 16).
- Autorização de uso de imagem e de citação de docentes, palestrantes e convidados; em divergência entre planilha e site, valem as datas da planilha; página 623 sem campanha nova (docs/execucao-2026-10-26.md, decisões 8, 10, 12 e 13).
- Parte da Meta: março R$ 1.295,00 e abril R$ 1.325,00 por turma; divisão do frio e do remarketing (80/20, 0/100 e 60/40, [SUPOSIÇÃO] da estratégia); diárias por fase e semana (gestor-de-midia-pos v5, 12.5; estrategia-de-midia-pos v4, 3.3, 3.4 e 3.5).
- Custo máximo por matrícula R$ 133,33; CPL máximo R$ 4,00, R$ 10,00 e R$ 18,00 (taxas [SUPOSIÇÃO ilustrativa]); rodízio com gatilho de R$ 20,00 na 1ª semana fechada; leitura com 3 dias e R$ 27,00 (estrategia-de-midia-pos v4, 2.2, 2.5 e 3.7).
- Limites de volume por fase, fonte única (estrategia-de-midia-pos v4, 3.6; gestor-de-midia-pos v5, 12.6).
- Evento de otimização lead; inscrição paga e 1ª mensalidade como conversões separadas, só para leitura; 17 a 25 inscrições no ciclo não dão volume ao algoritmo (estrategia-de-midia-pos v4, 4.1; gestor-de-midia-pos v5, 12.6).
- 289 e 662: gasto da campanha atual até a véspera limitado a R$ 500,00; recálculo em 30/11 e 30/12; conversão protegida; 662 com link trocado e URL conferida em 28/10 (estrategia-de-midia-pos v4, 3.8 e EM15).
- Pausa no dia seguinte ao corte, ou antes se o gasto do ciclo chegar a R$ 2.000,00 (EM16); datas de pausa (estrategia-de-midia-pos v4, 6.1).
- Padrão D11 (utm_source meta, utm_medium paid_social) e D12 (chave `<linha>_<código>`, nome da campanha = utm_campaign, AAAAMM do mês da subida; campanhas já no ar não são renomeadas) (cmo-geral, 12.7).
- Peças aprovadas, nomes, URL e UTM dos 70 anúncios; frase "Veja parcelas, total e matrícula na página da turma" só no remarketing, com 4 condições; 662 só com nome, campus e data, c3 e r1 sem arte (criativos-de-anuncio-pos-turmas v3).
- Início, praça, turma, modalidade e status das 14 turmas; 68636 com data "só no site"; 670 encerrada (catálogo, seção 2, 26/10/2026).
- Situação atual: 289 com campanha ativa (estático, "com 5 ângulos"); 662 com campanha ativa (estático e vídeo, "sem 5 ângulos"); 657, 68615, 341, 333, 68635, 366 e 68617 com campanha pausada; 68628, 68636, 68632 e 68609 sem campanha (docs/visao-de-campanhas-2026-10-26.md).
- 12 de 14 turmas ativas e 17 de 18 pausadas levam página com frase ligada ao MEC (análise de mídia da Pós, N4, citada pela estrategia 4.1 e pela versão 2).
- Contatos oficiais com horário informado (secretaria, vendas São Paulo e vendas Goiânia) (contexto/ufape-geral.md).
- Calendário: 07/12, 14/12, 04/01 e 25/01/2027 são segundas-feiras; 06/01/2027 é quarta-feira; 25/01 é feriado municipal em São Paulo; 08 e 09/02/2027 são Carnaval; cortes caem em quintas-feiras (estrategia-de-midia-pos v4, lista de fatos).

## Lista 2. Suposições

- [SUPOSIÇÃO ilustrativa] Taxas de lead para inscrição (5%, 10%, 15%) e de inscrição para matrícula (60%, 75%, 90%), origem gestor-de-midia-pos 12.3, sem fonte; por isso os CPL máximos e os leads por semana da seção 5.3 são conta, não previsão.
- [SUPOSIÇÃO] Data de corte = 30 dias antes do início, por turma; divisão 80/20, 0/100 e 60/40 entre frio e remarketing; sobra de fase vai para a fase seguinte; turma atrasada leva o aquecimento para a conversão (estratégia, EM4).
- [SUPOSIÇÃO] Região por praça, remarketing de 30 e 90 dias, exclusões de compradores em 180 dias, interesses de 657 e 341 pela persona (estratégia, EM6 e EM7).
- [SUPOSIÇÃO] Remarketing sem recorte de região (a estratégia não distingue frio e remarketing; escolha mantida da versão 2).
- [SUPOSIÇÃO] Leitura de R$ 27,00 e pausa de anúncio de R$ 36,00; rodízio com troca por 3 dias e R$ 27,00; volta dos 3 com CPL abaixo de R$ 10,00 por 2 semanas; frio que sai vai metade para o remarketing e metade para a busca (estratégia 2.5 e 3.7).
- [SUPOSIÇÃO] Pausar a campanha atual de 289 em 07/12 e a de 662 em 06/01, no dia da subida da nova; canal e diária da campanha atual não constam nos arquivos.
- [SUPOSIÇÃO] Gasto até a véspera = acumulado informado mais diária atual vezes os dias restantes até a véspera, na leitura do recálculo de 30/11 e 30/12.
- [SUPOSIÇÃO] As campanhas antigas pausadas das turmas deste plano ficam pausadas e as novas sobem no padrão.
- [SUPOSIÇÃO] Regras e recursos da Meta sem fonte nos arquivos: nome do objetivo "Cadastros"; educação fora de categoria especial; lance de menor custo sem teto de custo; posicionamentos manuais sem Audience Network e Messenger; melhorias automáticas e seus nomes; personalização por posicionamento para a arte 9:16 anexa; público Advantage+ com interesses como sugestão; regra de URL contendo `/produto/<código>/`; retroação do público de pixel; limite de gasto da campanha; troca de diária que reinicia o aprendizado; gasto diário acima da diária em alguns dias; aprendizado limitado com poucas conversões; domínio verificado e eventos priorizados; limite de 125 caracteres antes do "ver mais"; rótulo "Cadastre-se"; nomes dos eventos `inscricao_paga` e `mensalidade1_paga`; parâmetros de URL no campo próprio; parâmetros dinâmicos em minúsculas e sem acento; formulário instantâneo coletando fora da página.
- [SUPOSIÇÃO] Primeiras linhas aprovadas com no máximo 117 caracteres, conferido por leitura (confirmar na prévia).
- [SUPOSIÇÃO] Time sem trabalho no Carnaval; troca de diária de 25/01 pode ser feita no feriado ou deslocada (a confirmar com quem executa).

## Lista 3. Dados que faltam

- [DADO NÃO FORNECIDO] Gasto acumulado, diária atual, canal e nome das campanhas atuais de 289 e 662; gasto da onda 1; CPL, CTR, custo por inscrição e custo por matrícula observados da Pós; tamanho dos públicos de visitantes e de engajamento; criativos cansados ou vencedores.
- [CONFIRMAR] Mínimo diário aceito pela Meta para cada campanha (EM14); se o mínimo cobre o remarketing da manutenção de março (R$ 7,14).
- [CONFIRMAR] Resultado do teste de rastreio de 30/10: evento que a página de cada turma registra (lead ou início de checkout) e chegada da UTM ao CRM; envio de inscrição paga e 1ª mensalidade ao gerenciador.
- [CONFIRMAR U11] Valor da inscrição (R$ 260,00 do CEO contra R$ 250,00 e R$ 350,00 do site) e rótulo "matrícula" ou "inscrição" nas páginas; até lá nenhum anúncio cita valor.
- [CONFIRMAR] Período exato do ciclo e data de corte da 1ª mensalidade de cada turma (decisão 15); taxas reais de lead para inscrição e de inscrição para matrícula; matrículas esperadas da base e do orgânico (Mmid).
- [CONFIRMAR] Aprovação de PP16 e dos pedidos AMP13 a AMP24; aprovador de "Anúncios e verba" (tabela vazia em contexto/ufape-geral.md); nome de quem monta no gerenciador.
- [CONFIRMAR] Com o cmo: a chave com área curta cumpre o D12 (AMP13); caminho se o gasto de 289 passar de R$ 700,00 em 30/11 e se o de 662 passar de R$ 500,00.
- [CONFIRMAR] Travas: link e data de 679 e 68636, link, data, cronograma, modalidade, carga horária e público de 662 (P3) e c3 de 662 com conteúdo liberado; data de 366 (P4); pré-requisito de 657 (U10); PP7, regra da promoção de 341 (PR7) e local da prática (AP11); turma da URL de 68617; número de turma de 68628, 68617 e 662.
- [CONFIRMAR] Procedência dos alunos por estado (para ampliar a região); base legal para listas de contatos; política de privacidade e finalidade do formulário nas 14 páginas; páginas com frase ligada ao MEC (decisão da pessoa do marketing ou correção); correção das páginas que dizem turma mínima de 20.
- [CONFIRMAR] Se a troca de diária de 25/01 é feita no feriado; janela de atribuição da conta.
- [CONFIRMAR] Motivo das pausas antigas das turmas de março e abril e se os 5 ângulos antigos de 68615, 68617 e 366 podem voltar (o criativos v3 não os reaproveitou).
- Entregável padrão de 5 textos principais por conceito: não produzido nesta versão, por pedido de ligar os anúncios às peças aprovadas; variações só como iteração do criativos-de-anuncio.

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma. Regras de política e de recurso da Meta sem fonte nos arquivos estão marcadas [SUPOSIÇÃO].

---

**Próximo agente sugerido:** anuncios-google (campanhas de Busca das 14 turmas, com as diárias das seções 3.3 e 3.4 da estratégia, a mesma regra de 289 e 662 e as mesmas travas de subida), depois qa-de-marketing (conferência desta versão e da nova versão do anuncios-google).
