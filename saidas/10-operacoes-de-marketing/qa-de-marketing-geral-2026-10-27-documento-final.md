# Revisão do qa-de-marketing: reconferência M.4 (B1 a B14) e documento final para o cliente

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** geral (graduacao, pos, livres e eventos)
- **Data:** 27/10/2026
- **Commit revisado:** 45cbc09
- **Revisado (nenhum arquivo foi editado):**
  - Parte 1: saidas/10-operacoes-de-marketing/cursos/*.json (amostra da seção 2 da revisão M.4 e arquivos citados em cada B), ferramentas/mapa-mental/mapa_html.py
  - Parte 2: saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27-documento-final.html, saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md, ferramentas/mapa-mental/documento_final.py
- **Entradas lidas:** contexto/ufape-geral.md; auditorias/conformidade-educacional.md; contexto/catalogo-de-cursos.md (cabeçalho, seções 1 e 2); docs/execucao-2026-10-26.md (decisões 1 a 20); docs/andamento-planejamento.md (inteiro); docs/pendencias-camada-1.md (inteiro); saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (cabeçalho, seções 1 e 2); saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (linhas 1 a 210 e 780 a 1013: tabelas 1.1 e 1.2, regras, 2.3, 7.5, 7.7, 8, 9, 10 e 11); saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-mapa.md; saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-27-c.md; saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md (linhas 328 a 335)
- **JSON abertos:** pos-650, pos-698, pos-707, pos-657, pos-352, pos-359, pos-679, pos-68636, pos-68629, pos-366, pos-662, pos-691, pos-670, pos-68656, pos-68641, livres-623, livres-68637, livres-68634, livres-616, livres-469, livres-575, livres-573, livres-347, livres-721, livres-639, livres-68668, eventos-workshop-neuromonitorizacao-2026-11-20, eventos-sem-codigo-simposio-plantonista-veterinario, graduacao-medicina-veterinaria, graduacao-pedagogia
- **Dados pessoais:** nenhum lido ou citado.

---

## 1. Vereditos

| Parte | Veredito | Para onde vai |
|---|---|---|
| Parte 1: mapa e 184 JSON (B1 a B14) | **CORRIGIR** | Volta ao orquestrador (gerador ferramentas/mapa-mental/mapa_json.py): B6, B7, B13 e os problemas novos N1 e N2. B1 a B5, B8 a B12 e B14 passam |
| Parte 2: documento final para o cliente | **CORRIGIR** | Volta ao relatorios (texto da narrativa, seção 4 desta revisão) e ao orquestrador (gerador documento_final.py, seção 5) |

Motivo em uma frase: o gerador resolveu quase todos os bloqueios, mas a 359 ficou sem a trava do desconto que o plano manda (regra 10), a P3 não segura a subida de 679 e 68636 e vários textos saem cortados com "…"; o documento final bate com as fontes em verba, metas em reais, contagens e recorte, mas traz números e situações desatualizados ou trocados (cards de abril, travas do Workshop, PP13 e PP14, "13 campanhas", A4), nomes "[CONFIRMAR]" na lista da próxima etapa, um link quebrado e termos internos sem explicação para a diretoria.

Nada foi publicado, enviado ou pago. Nenhuma das duas partes segue para a aprovação humana antes das correções.

---

## 2. Parte 1: reconferência B1 a B14

### 2.1 Decisões do orquestrador

| Decisão | Avaliação | Motivo |
|---|---|---|
| 68634 continua livres-68634.json, com linha "eventos" | **ACEITA** | O esquema diz que o id nunca muda; o JSON traz linha "eventos", linha_origem "plano", tipo "workshop" e relacionados com o workshop. Condição: o arquiteto-de-fluxos registra no documento de fluxo que a linha vem do campo `linha`, nunca do prefixo do id (a plataforma não pode filtrar por prefixo) |
| 679, 68636, 68629 e 359 deixam de bloquear peça final (OU19, OU21, OU22) | **ACEITA para 679, 68636 e 68629; RECUSADA para 359** | O plano da onda 3, 2.3, permite peça com o mês no lugar do dia só pela trava de data. A 359 tem outra trava: regra 10 ("Toques, posts e cards dessas turmas só saem com a página corrigida (regra completa) ou com o desconto retirado, em qualquer mês") e 2.3 ("359 sem pré-requisito, sem desconto"). É a mesma lógica da OU23 em 352, que o orquestrador manteve bloqueando. Ver B6 |
| P4 da 698 resolvida em 27/10 pela decisão 19 | **ACEITA** | Decisão 19: "As peças e a mídia saem sem esperar a correção da página". A pendência "decisão 19" segue aberta (698-p05), como deve. Ver N2 sobre o texto da descrição |
| Pedidos agrupados ("OM1 a OM7", "AMP13 a AMP25") como um pedido só | **ACEITA** | Em docs/pendencias-camada-1.md cada grupo é uma linha única, com um arquivo só. Condição: ref com a faixa literal e o_que literal da linha (confere em pos-679 e pos-657); onde o plano detalha código a código (OA1 a OA12 da onda 1), continuam separados (confere em pos-707 e pos-698) |

### 2.2 B1 a B14

| B | Resultado | Trecho do JSON | Regra para o gerador (se CORRIGIR) |
|---|---|---|---|
| B1 | **APROVADO** | pos-650.json: `"motivo_do_recorte": "pendência urgente: turma iniciada com campanha ativa (plano geral, 2.1 item 2)"`, `"campanha": "ativa"`, pendência `"ref_plano": "P8"` com `"bloqueia": ["anuncio"]` e aprovação `"ref": "A4"` | - |
| B2 | **APROVADO** | livres-623.json: `"ref_plano": "decisão 13"`, `"bloqueia": ["anuncio", "peca_final"]`; aprovação `"ref": "R8"`; `"relacionados": [{"id": "livres-68637", "relacao": "duplicidade_provavel", "natureza": "[SUPOSIÇÃO]"}]`; livres-68637.json com o sentido inverso; `"bloqueado": true` | - |
| B3 | **APROVADO** (ver N1) | graduacao-pedagogia.json: G6, G7, G10, G11, G12, G13, G14 com `"bloqueia": ["peca_final"]`; MP1, MP2, MP4, MP10 com `["anuncio"]`; U12 e U13 com `["meta"]`; G5 com `"campos": ["carga_horaria"]`; `"pendencias_abertas": 19`, `"bloqueado": true`; aprovação só `"AM1 a AM12"`. graduacao-medicina-veterinaria.json com G8 e sem G6, `"AM1 a AM12 e AG1 a AG11"` | - |
| B4 | **APROVADO** | pos-691.json: `"recorte": "historico"`, `"grupo_de_campanha": null`, `"entregas": []`, 8 canais `"estado": "fora"`, `"motivo": "fora do recorte do plano (seção 2.4)"`, sem a pendência "decisão 14", `"bloqueado": false` | - |
| B5 | **APROVADO** | livres-616.json, livres-469.json, livres-575.json, livres-623.json: `"preco_estruturado": null`; pos-698.json: 18 x 1.498,33 = 26.969,94 contra 26.970,00 (diferença dentro de R$ 0,01 por parcela), estruturado mantido | - |
| B6 | **CORRIGIR** | pos-359.json: `"ref_plano": "OU24"`, `"bloqueia": ["preco"]`, descrição só com "desconto de 12%"; `"resumo": {"pendencias_abertas": 14, "bloqueado": false}`. Em pos-352.json a OU23 sai com `"tipo": "data"`, `"campos": ["inicio"]` e `"bloqueia": ["data", "peca_final"]` | (a) OU24 em 359: `"tipo": "preco_ou_condicao"`, `"campos": ["condicoes_especiais"]`, `"bloqueia": ["preco", "peca_final"]`, descrição com os três pontos da pergunta (desconto de 12% sem regra completa, pré-requisito de residência ou pós, convite da prova de Especialista), fonte "cmo-pos-2026-10-27-onda3.md, regra 10, 2.3 e seção 8". (b) Regra geral: código de pergunta cujo texto no plano trata de desconto ou público (OU23, OU24, OU27, OU28) recebe `"peca_final"` quando a regra 9 ou 10 do plano da onda diz que a peça não sai; não derivar `bloqueia` só da palavra "data". (c) OU23 em 352: manter `"tipo": "data"` e acrescentar `"condicoes_especiais"` em `campos` e `"preco"` em `bloqueia`, porque a pergunta cobre data e desconto |
| B7 | **CORRIGIR** | pos-679.json e pos-68636.json: `"ref_plano": "P3"`, `"bloqueia": ["data", "preco"]`, descrição terminando em `"Tratamento no plano……"`; pos-679.json: `"ref_plano": "OU19"`, `"bloqueia": ["data"]`, descrição "afeta: data nas peças, subida, contagem de cards". livres-573.json e pos-662.json: `"Tratamento no plano: [CONFIRMAR]."` (P6 e P5). Relacionados, P17, política de entrada e inicio_na_visao conferem (livres-573: `"inicio_na_visao": "2026-11-29"`, `"divergencia_de_data": true`; livres-347: P17 com `peca_final`; livres-721: "2.1 item 3") | (a) P3 em 679, 68636 e 662: `"bloqueia": ["data", "preco", "anuncio"]`, porque o plano da onda 3 diz "subida só com P3 (lote 2)" (4.1) e o inventário diz "subida 06/01 com as travas P3 (679, 68636, 662)". (b) Pergunta cujo "Por que importa" cita "subida", "mídia" ou "campanha" recebe `"anuncio"` em `bloqueia` (OU19 em 679). (c) A descrição da P3 em cada item diz o que vale para aquele item (em 68636: "data só no site, sem linha na planilha"), sem a lista dos outros códigos. (d) "Tratamento no plano" é copiado da coluna de tratamento da seção 7 do plano geral; "[CONFIRMAR]" só quando a coluna estiver vazia |
| B8 | **APROVADO** (ver N1) | pos-707.json: OA1, OA2-B, OA8, OA10, OA9, OA11, OA12; pos-698.json: OA1, OA5, OA8, OA10, OA9, OA11, OA12; pos-662.json: OC8, AMP13 a AMP25, AGP12 a AGP25, PP16 e MO6, OM1 a OM7, R5; workshop: R2, R3, R7; pos-657.json: OB5, AD-F6-1 a AD-F6-5, AF1 a AF7 e DEC1 a DEC7, MO1 a MO5, AMP13 a AMP25, AGP12 a AGP25, R6. `"quanto": "R$ 2.000,00 por turma, decisão 15"` nos pedidos de mídia; efeito_esperado copiado ou "conforme o plano da onda" | - |
| B9 | **APROVADO** | workshop: `"nome_padrao": "Workshop Brasileiro de Neuromonitorização"`, `"aliases": ["I Simpósio Brasileiro de Neuromonitorização Veterinária"]`, `"desconto_texto": "20% de desconto"`, `"modalidades"` com 2 itens (30 vagas; produto 68634), 7 chaves do kit (pagina com `"inventario_pendente"`), U9. livres-68634.json: `"linha": "eventos"`, `"tipo": "workshop"`, `"modalidade_normalizada": "online"`, P9 com `"bloqueia": ["peca_final"]`. Posts do workshop com `"qa": "aprovado"`: confere, porque a troca pedida em qa-de-marketing-eventos-2026-10-27-c.md (R-P2) está aplicada na linha 332 de posts-sociais-eventos-2026-10-26.md, conferida nesta revisão | - |
| B10 | **APROVADO** | pos-670.json e pos-68656.json: `"recorte": "pendencia"`, `"dias_ate_inicio": null` | - |
| B11 | **APROVADO** | mapa_html.py: título do nó com `nome_padrao`; cartões `` `${recS.length} + ${recG.length}` `` e onda 1 `` `... + ...` ``; `QM` com "1 por docente autorizado" | - |
| B12 | **APROVADO** | `"natureza": "proposta_do_cmo"` nas ondas 2 e 3; `responsavel` em lista; `secao` e `ref_aprovacao` presentes; `kit.inventario` e 3 acréscimos na onda 1 (pos-698); `"tipo": "minicurso"` (livres-469); `"tipo": "aprimoramento"` (livres-68668, livres-639); ids `"<codigo>-p01"`; bloco `prova_de_bolsa` e `evento` logo depois de `equipe` | - |
| B13 | **CORRIGIR** (leve) | graduacao-pedagogia.json e graduacao-medicina-veterinaria.json: `"vagas": {"turma_minima": 30, "vagas_ofertadas": null, ...}` e nenhuma pendência cita `vagas.vagas_ofertadas` (a P11 lista só `vagas.vagas_restantes`; a "editais" não lista vagas). Os demais itens do recorte conferidos têm as lacunas com pendência (P11, OU4, P13, U3, U9, "fim das inscrições", "prazo do kit") | Na Graduação, copiar as vagas do edital (45 integral, 45 noturno, 80 Pedagogia; contexto/cursos/graduacao/editais-2027-1.md) com `campos_so_na_ficha`, ou acrescentar `"vagas.vagas_ofertadas"` em `campos` da pendência "editais". Regra geral: todo campo null de item com recorte "planejar" tem de aparecer em `campos` de alguma pendência, conferido por script antes de gravar |
| B14 | **APROVADO** | livres-623.json: `cmo-livres-2026-10-26.md` e `mensagens-livres-2026-10-26.md` com `"estado": "devolvido"`; mapa_html.py: `CAM.devolvido = 'rascunho a revisar'` | - |

### 2.3 Problemas novos criados pela correção

**N1. Textos cortados com "…" (descrição de pendência e o_que de aprovação).**
- pos-679.json, pos-68636.json, pos-662.json, pos-68641.json: P3 termina em `"Tratamento no plano……"` ou `"Tratamento no plano…"`.
- graduacao-*.json: G11 termina em `"... (em que semestre) com…"`; MP4 termina em `"Define o público adulto que desbloqueia noturno…"`.
- pos-707.json e pos-698.json: OA10 termina em `"... com a…"`.
- pos-679.json: OC1-A termina em `"valor da matrícula…"`.
- **Efeito:** o mapa do documento do cliente mostra esses textos; a regra ou o tratamento some no meio da frase.
- **Regra:** nunca cortar. Copiar o texto inteiro da fonte. Se houver limite de tamanho, cortar no fim de uma frase, sem reticências, e acrescentar "(texto completo: <arquivo>, <seção>)".

**N2. Descrição da P4 copiada igual em todos os itens.**
- pos-366.json, pos-352.json e livres-623.json trazem "anúncio novo de 698 só depois de o site ser corrigido (pedido A6)". Isso não vale para esses itens, e na própria 698 foi revogado pela decisão 19.
- **Regra:** a descrição da P4 diz a divergência do item (datas da planilha e do site) e o tratamento que vale para ele. Na 698, que está resolvida, acrescentar "revogado pela decisão 19 (27/10/2026)".

**Ressalva (não bloqueia):** em pos-662.json, R5 sai com `"quanto": "R$ 2.000,00 por turma, decisão 15"`, mas o pedido diz "289 sem aumento de verba". Prefira copiar o "sem aumento de verba" quando o pedido não mexe em verba.

---

## 3. Parte 2: documento final (conferência)

### 3.1 O que bate com as fontes

- **Verba das 14 turmas de março e abril:** Meta R$ 17.740,00 e Google R$ 10.260,00, total R$ 28.000,00.
  - Conta: 5 x 1.250,75 + 9 x 1.276,25 = 17.740,00; 5 x 749,25 + 9 x 723,75 = 10.260,00.
  - Fontes: diário de 27/10; docs/pendencias-camada-1.md; plano da onda 3, seção 1.
- **Graduação:** Medicina Veterinária com Meta R$ 1.440,00 e Google R$ 560,00 (184,00 + 376,00); Pedagogia com R$ 2.000,00 na Meta; total R$ 4.000,00 (diário).
- **Mensalidades da Graduação:** 5.000,00, 4.000,00 e 525,00 (catálogo, seção 1).
- **Metas em reais:** todas conferidas contra o total do catálogo, seção 2 (15 x o total). São as 6 da onda 1, as 5 de março e as 9 de abril.
- **Receita dos 12 primeiros meses:** 333 com R$ 11.470,00 (12 x 935,00 + 250,00); 657 com R$ 19.609,96 (12 x 1.613,33 + 250,00).
- **Onda 1:** as datas do 3º módulo e as datas de pausa batem com o diário (cmo-pos v3, 27/10). A decisão 18 e a decisão 19 estão citadas certo.
- **Contagens que batem com o diário:**
  - março: 30 posts, 53 cards, 5 roteiros, 2 e-mails e 5 WhatsApp por turma;
  - abril: 8 páginas, 55 textos (7 x 7 + 6), 129 cards, 9 posts de coordenação, 48 posts, 8 roteiros, 55 toques em 31 dias;
  - camada 1: 33 etapas e 71 itens no backlog (24 + 47);
  - Livres: 45 contínuos mais 2 gravados de Eventos.
- **Recorte do mapa:**
  - 100 itens: 3 de Eventos, 2 da Graduação, 53 de Livres e 42 de Pós (20 turmas e 22 provas, sem a 68656). São os 112 do recorte menos os 12 da próxima etapa.
  - Ondas: onda 1 com 35, onda 2 com 54 e abril com 9.
  - Nenhum item tem início depois de 30/04/2027. Contínuos sem data entram, o que está certo: estão à venda agora.
  - A lista da próxima etapa tem as 12 certas: as 10 turmas de maio da tabela 1.2 do plano da onda 3, mais 68638 e 560.
- **Situação dos kits no mapa:**
  - março, abril (menos 662) e Graduação: "aguarda aprovação";
  - onda 1: inventário pendente;
  - provas: "revisar por mudança";
  - Livres: "a fazer".
  - Bate com a narrativa (2.1 a 2.9).

### 3.2 Problemas encontrados

| # | Onde | Problema | Tipo |
|---|---|---|---|
| D1 | 2.4, "Ponto de atenção honesto" e Fatos | Usa 262 cards, 103 firmes e 159 de lacuna, que são abril e maio somados. Maio é próxima etapa. Pelo diário (entrega O6), abril tem 129 cards: 52 firmes, 77 de lacuna e 65 com as reservas | número fora do recorte |
| D2 | 2.7 | As travas do Workshop estão agrupadas errado. "A2, A4, A5 (templates da Meta)" junta três travas diferentes; pela qa-de-marketing-eventos-2026-10-27-c.md, só a A5 é dos templates. A2 é o WhatsApp de M6 e M7; A4 é a URL e o bloco da prova na M9; AP8 é link e prazo da gravação na M8. Também diz que posts e mensagens foram "aprovados" na reconferência, mas nela os posts voltaram com 1 troca (aplicada e conferida nesta revisão) | fato |
| D3 | 2.1 (linha do mapa) e Fatos | "qa M.4 pendente" está desatualizado: a M.4 voltou CORRIGIR, o gerador foi corrigido e esta reconferência ainda pede ajustes | situação |
| D4 | 4.6, item 39, e 6.1, linha de 03/11 | "6 turmas iniciadas e pausadas" contradiz o plano geral (2.1 item 2: "seguem com campanha paga ATIVA"), o briefing ("6 turmas iniciadas com campanha ativa") e o mapa (pos-650.json: `"campanha": "ativa"`, A4 "pausar ou manter"). Não localizei fonte que diga que foram pausadas [CONFIRMAR] | contradição narrativa x mapa |
| D5 | 5, linha "Pós onda 1, mídia" | "(PP13 e PP14 também ao cmo)": o diário (F11, 27/10) registra "PP13 e PP14 fechados", e o plano da onda 3 (O11 g) diz "PP13 e PP14 fora também na onda 3" | situação |
| D6 | 5, linha "Mídia das 14 turmas" | "13 campanhas Meta ativas (662 pausada)": a fonte diz "Campanhas Meta das 14 turmas (13 ativas; 662 pausada até OU18)". São turmas, não campanhas (o Meta v3 tinha 28 campanhas) | número |
| D7 | 6.1, 30/11 | PP16 aparece em 30/11 e de novo em 30/12. O plano da onda 3 diz "PP16 com prazo 30/12 para abril" [CONFIRMAR as datas dos pedidos de mídia no gestor-de-midia-pos] | data |
| D8 | 7.1, tabela "O que falta" | A 662 é turma de abril, está no mapa do documento e aparece também como próxima etapa | recorte |
| D9 | 7.1 | "aprovado pelo qa com 29 correções aplicadas": a revisão O0 foi CORRIGIR e o orquestrador aplicou C1 a C29 (diário); não houve um novo "aprovado" | situação |
| D10 | 5, R6 | "perdeu o sentido porque LinkedIn saiu pela decisão 15" é uma leitura: a decisão 15 fixa a verba, e quem tirou o LinkedIn pago foi o gestor (diário, gestor v3). Está como [SUPOSIÇÃO] nas notas, mas não no texto | suposição sem marca |
| D11 | 1, frase 1 | "9 de abril" no resumo contra "8 turmas; 662 em espera" em 2.1 e 2.4 | contagem |
| D12 | documento inteiro | Termos internos sem explicação: squad, qa, qa-de-marketing, camada 1 e 2, onda, lote, kit mínimo, card, slot, remarketing, Busca, UTM, CRM, opt-in, extensão, PP, OA, OB, OC, OU, U, G, MP, AMP, AGP, AD, AF, DEC, MO, OM, R, A, P, E5, AP8, EVM1, C0, CP1, "rodada onda1c", "versão 5.1". Também caminhos de arquivo em quase toda linha. Sem um glossário, a diretoria não consegue ler as seções 4 a 6 | linguagem |
| D13 | gerador, próxima etapa | 719 e 68629 aparecem com o nome "[CONFIRMAR]" (`j.get('nome_padrao') or ...` aceita a string "[CONFIRMAR]") | gerador |
| D14 | gerador, 2.7 | O link vira `href="https://faculdade.ufape.com.br/neuro-summit/."`: o ponto final entra no endereço | gerador |
| D15 | gerador, notas | A seção "Fontes" mostra caminhos absolutos do ambiente (`/home/user/marketing-ufape/...`) para o cliente | gerador |
| D16 | mapa do documento | Os nós do mapa mostram textos cortados (N1), nomes de agente na coluna "Responsável", o bloco "Arquivos das camadas" e rótulos com "qa". Para a diretoria, isso é ruído | gerador e linguagem |

**Não conferido nesta revisão** (fontes não abertas; não marquei como erro):
- "46 páginas segundo a auditoria de 26/10" (4.5, item 30);
- "O plantão precisa de duas pessoas nomeadas" (2.5);
- "cerca de R$ 142,86 por semana por curso" e "o plano do cmo usa 30 como meta principal da Graduação" (3.5);
- "20/02, devolução de 80%" (6.2).

Na seção 7, também não conferi:
- "5 das 10 turmas sobem sem resposta" (7.1);
- "aprovação das páginas em 11/01 e do plano de mídia em 29/01" (7.1).

O relatorios confirma cada um na fonte antes da versão final ou marca [CONFIRMAR].

**Observação (não bloqueia):**
- A 352 está na próxima etapa pela data da planilha (24/05), que vale pela decisão 12. Se a OU23 confirmar 24/04, ela entra no recorte de abril.
- A 366 pode sair de 10/04 para 24/04 e continua no recorte.
- Sugiro uma linha em 7.1 dizendo isso.

---

## 4. Correções de texto da narrativa (saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md)

**C1 (D11, seção 1, frase 1)**
- Trocar: "6 turmas de Pós que começam entre 30/10 e 28/11, 5 turmas de março e 9 de abril de 2027, a Graduação 2027.1"
- Por: "6 turmas de Pós que começam entre 30/10 e 28/11, 5 turmas de março e 9 de abril de 2027 (8 com o kit pronto e a 662 em espera), a Graduação 2027.1"

**C2 (D2, seção 2.1)**
- Trocar: "| Workshop Brasileiro de Neuromonitorização | PRONTO PARA APROVAR (posts e mensagens) e ESPERA | Posts e mensagens aprovados pelo qa em 27/10; criativos sem revisão; a mídia já está no ar e precisa de conferência em 28/10 |"
- Por: "| Workshop Brasileiro de Neuromonitorização | PRONTO PARA APROVAR (posts e mensagens) e ESPERA | Mensagens aprovadas pelo qa em 27/10 e posts com a última troca aplicada e conferida no mesmo dia; criativos sem revisão; a mídia já está no ar e precisa de conferência em 28/10 |"

**C3 (D3, seção 2.1)**
- Trocar: "| Mapa mental e JSON | Mapa e 184 JSON gerados em 27/10; qa M.4 pendente | Esta narrativa é a etapa M.2 |"
- Por: "| Mapa por curso | Mapa e 184 arquivos por curso gerados em 27/10 e refeitos depois da primeira revisão de qualidade; a reconferência de 27/10 ainda pede ajustes no gerador | O mapa deste documento mostra os 100 itens que começam até abril de 2027 |"

**C4 (D1, seção 2.4)**
- Trocar: "Ponto de atenção honesto: dos 262 cards de docente das ondas de abril e maio (129 e 133), só 103 têm dia firme no calendário e 159 ficaram como lacuna registrada, por falta de capacidade do perfil e por falta da resposta sobre as horas do time (U8). O mínimo do kit não foi reduzido; a lacuna está escrita com o motivo."
- Por: "Ponto de atenção: dos 129 cards de docente de abril, 52 têm dia firme no calendário e 77 ficaram como lacuna registrada (65 se as reservas da onda 2 forem liberadas), por falta de capacidade do perfil e por falta da resposta sobre as horas do time (U8). O mínimo do kit não foi reduzido; a lacuna está escrita com o motivo. Os 133 cards de maio estão na próxima etapa (seção 7)."

**C5 (D2, seção 2.7)**
- Trocar: "posts e mensagens foram corrigidos e aprovados pelo qa na reconferência de 27/10 (saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-27-c.md) e aguardam a aprovação humana; os criativos seguem sem revisão. Envio e publicação continuam travados por E5 (pagamento do presencial), E6 (validade do cupom), verificação do produto 68634 (segura todo trecho do transmitido), AP8 (texto do certificado), A2, A4, A5 (templates da Meta) e opt-in no CRM e no checkout."
- Por: "as mensagens foram aprovadas pelo qa na reconferência de 27/10 (saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-27-c.md); os posts receberam ali uma última troca de texto, já aplicada e conferida no mesmo dia; os dois aguardam a aprovação humana, e os criativos seguem sem revisão. Mesmo com a aprovação, envio e publicação esperam: as linhas de preço do presencial (E5), a validade do cupom (E6), a verificação do produto transmitido 68634 (segura todo trecho sobre o transmitido), o link e o prazo da gravação na mensagem M8 (AP8), o endereço e o bloco da prova na mensagem M9 (A4), o WhatsApp das mensagens M6 e M7 (A2), a aprovação dos modelos de mensagem na Meta (A5) e o registro do consentimento no CRM e no checkout."

**C6 (D4, seção 4.6, item 39).** Vale se nenhuma fonte mais nova disser que as 6 campanhas foram pausadas. Se existir, cite essa fonte no texto e o orquestrador atualiza o dicionário MIDIA do gerador.
- Trocar: "| 39 | A4, A6, A12 | A4: as 6 turmas iniciadas e pausadas ainda antes do 3º módulo serão conferidas pelo gestor e trazidas ao cmo, sem reativar nada (03/11); A6: correção de 698; A12: planilha e site (P3 a P7) | 03/11 (A4); demais sem data fixa |"
- Por: "| 39 | A4, A6, A12 | A4: decidir se as campanhas pagas ainda ativas das 6 turmas já iniciadas (650, 68662, 706, 586, 554 e 68612) são pausadas ou mantidas, depois da conferência do gestor de mídia; A6: correção de 698; A12: planilha e site (P3 a P7) | 03/11 (A4) [CONFIRMAR: origem da data]; demais sem data fixa |"

**C7 (D4, seção 6.1)**
- Trocar: "conferência das 6 turmas iniciadas e pausadas (A4)"
- Por: "conferência das 6 turmas iniciadas com campanha ativa (A4)"

**C8 (D5, seção 5)**
- Trocar: "| Pós onda 1, mídia | PP15, PP17, EM4, EM11, EM13 a EM16 (PP13 e PP14 também ao cmo) |"
- Por: "| Pós onda 1, mídia | PP15, PP17, EM4, EM11, EM13 a EM16 (PP13 e PP14 já fechados no memorando de mídia da onda 2) |"

**C9 (D6, seção 5)**
- Trocar: "13 campanhas Meta ativas (662 pausada), Busca Google,"
- Por: "Campanhas Meta das 14 turmas (13 ativas; 662 pausada até OU18), Busca Google,"

**C10 (D10, seção 5)**
- Trocar: "R6: teste de LinkedIn só da 657 (11 a 31/01/2027), que perdeu o sentido porque LinkedIn saiu pela decisão 15;"
- Por: "R6: teste de LinkedIn só da 657 (11 a 31/01/2027), que talvez tenha perdido o sentido, porque o LinkedIn pago saiu do plano de mídia com a verba de R$ 2.000,00 por turma (decisão 15) [SUPOSIÇÃO];"

**C11 (D7, seção 6.1)**
- Trocar: "| 30/11 (seg) | Aprovação de PP16, AMP13 a AMP25, AGP12 a AGP25 e OB2 a OB5 | pessoa do marketing |"
- Por: "| 30/11 (seg) | Aprovação de AMP13 a AMP25, AGP12 a AGP25 e OB2 a OB5; o PP16 (plano de abril) fica para 30/12 [CONFIRMAR: data de cada pedido no gestor-de-midia-pos] | pessoa do marketing |"

**C12 (D9, seção 7.1)**
- Trocar: "| Plano do cmo da onda 3 (19 turmas), aprovado pelo qa com 29 correções aplicadas | cmo-pos-2026-10-27-onda3.md |"
- Por: "| Plano do cmo da onda 3 (19 turmas), revisado pelo qa, com as 29 correções pedidas já aplicadas (versão 2) | cmo-pos-2026-10-27-onda3.md |"

**C13 (D8, seção 7.1)**
- Trocar: "| 662 | espera total até OU18 |"
- Por: "| 662 (turma de abril, já no mapa deste documento) | espera total até OU18 (ver 2.4) |"

**C14 (D3, Fatos)**
- Trocar: "- Mapa mental HTML e 184 JSON gerados em 27/10; qa M.4 pendente: docs/andamento-planejamento.md (última linha)."
- Por: "- Mapa HTML e 184 JSON gerados em 27/10 e refeitos depois da revisão M.4 (commit 45cbc09); reconferência e revisão deste documento em saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-documento-final.md: docs/andamento-planejamento.md (últimas linhas)."

**C15 (D1, Fatos)**
- Trocar: "- 262 cards de docente em abril e maio, 103 com dia firme e 159 de lacuna: cmo-pos-2026-10-27-onda3.md, seção 7.5."
- Por: "- 129 cards de docente em abril, 52 com dia firme e 77 de lacuna registrada (65 com as reservas): docs/andamento-planejamento.md (entrega O6 de 27/10); 133 cards de maio, na próxima etapa: cmo-pos-2026-10-27-onda3.md, seção 7.5."

**C16 (D12, glossário depois de "Como ler as situações")**
- Trocar: "| A FAZER | Ainda não foi produzido |"
- Por: "| A FAZER | Ainda não foi produzido |

### Termos usados neste documento

| Termo | O que quer dizer |
|---|---|
| Squad | Equipe de agentes de marketing que planeja, escreve e revisa os rascunhos. Nada vai ao ar sem a pessoa do marketing |
| qa | Revisão de qualidade e de conformidade (dados do catálogo, regras do MEC e do consumidor, privacidade) feita antes da aprovação humana |
| Onda | Grupo de turmas planejadas juntas pela data de início (onda 1: começam até 28/11/2026; onda 2: março de 2027; onda 3: abril e maio de 2027) |
| Camada 1 e camada 2 | Camada 1: estratégia de cada linha. Camada 2: mensagens e peças-base por área de especialidade |
| Kit mínimo | Lista mínima de peças que toda turma recebe (página, posts, criativos, mensagens, roteiro de vídeo) |
| Card | Story do Instagram que apresenta um docente da turma |
| Remarketing e Busca | Anúncio só para quem já visitou a página; anúncio no Google para quem procura o tema |
| UTM, CRM e opt-in | Etiqueta no link que mostra de onde veio o contato; sistema de contatos da Ufape; autorização do contato para receber mensagens |
| Extensão | Últimos 15% da verba da turma, usados depois da data de corte até a véspera do 3º módulo |
| Códigos | OA, OB e OC: pedidos de aprovação das ondas 1, 2 e 3 da Pós. OU e U: perguntas à Ufape. G e MP: pedidos da Graduação. AMP e AGP: campanhas Meta e Google da Pós. R, A e P: aprovações, pedidos e pendências do plano geral. Os demais códigos seguem a lista de aprovação do arquivo citado na mesma linha |"

A troca C16 só define termos: não cria dado. Nenhuma correção acima usa travessão nem meia-risca.

---

## 5. Regras para o gerador

### 5.1 ferramentas/mapa-mental/mapa_json.py (Parte 1)

- **R-B6:** a OU24 em 359 bloqueia `["preco", "peca_final"]`, com a descrição completa. Pergunta de desconto ou de público bloqueia peça final quando a regra 9 ou 10 do plano da onda manda. A OU23 em 352 acrescenta `condicoes_especiais` e `preco`.
- **R-B7:** a P3 em 679, 68636 e 662 bloqueia também `anuncio`. Pergunta cujo "Por que importa" cita subida, mídia ou campanha bloqueia `anuncio`. Descrição e tratamento valem para o próprio item, e o tratamento é copiado da coluna da seção 7 do plano geral.
- **R-B13:** vagas da Graduação copiadas do edital, ou o campo entra numa pendência. Antes de gravar, uma conferência por script garante que todo null em item "planejar" aparece em `campos`.
- **R-N1:** nenhum texto termina em "…". Copiar o texto inteiro, ou cortar no fim de uma frase com a indicação da fonte.
- **R-N2:** a descrição da P4 é específica de cada item. Na 698, a resolvida, registra que a decisão 19 revogou a trava.

### 5.2 ferramentas/mapa-mental/documento_final.py (Parte 2)

- **R-D13:** o nome na lista da próxima etapa usa a mesma regra de mapa_html.py. Se `nome_padrao == '[CONFIRMAR]'`, mostrar `nome_no_site` mais " (nome padrão [CONFIRMAR])". Melhor ainda: o mapa_json.py grava em `nome_padrao` o nome da regra E2 do plano da onda 3 ("Pós-graduação em Inteligência Artificial na Saúde", "Pós-graduação em Ultrassonografia de Pequenos Animais").
- **R-D14:** na função `inline`, o endereço não leva a pontuação final. Usar `(https://[^\s<)]+?)([.,;:]?)(?=\s|<|$)`; o link fica com o grupo 1 e o grupo 2 vai depois de `</a>`.
- **R-D15:** antes de converter as notas, tirar o prefixo `/home/user/marketing-ufape/` dos caminhos. A seção "Fontes" fica com caminhos relativos.
- **R-D16:** no modo documento, o script do mapa:
  - oculta o bloco "Arquivos das camadas" e a coluna "Responsável" do kit;
  - troca "qa" por "revisão de qualidade" nos rótulos (`ST.aguardando_aprovacao` e o cartão `t-ag`);
  - tira da legenda o item "Fora do recorte", que não tem item no documento.
  - Os textos das pendências passam a sair inteiros com a R-N1.
- **Conferência automática:** o script grava os itens e falha se algum deles tiver `inicio` depois de 30/04/2027. Também falha se `len(ids) + len(proxima)` for diferente do número de itens com recorte "planejar".

---

## 6. auditorias/conformidade-educacional.md, item por item

### 6.1 Parte 1 (mapa e JSON)

| Bloco | Item | Resultado | Onde |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH, duração e turno batem com o catálogo | ok | B9 resolvido (nome do workshop, modalidade do 68634); campos literais conferem nos JSON abertos |
| Dados do curso | Status "aberto" ou sem chamada | ok | o mapa não chama para inscrição |
| Dados do curso | Modalidade clara; EAD não aparece como presencial | ok | livres-68634.json com `"modalidade_normalizada": "online"` e P9 |
| Regulação | Graduação com ato do catálogo | ok | `ato_autorizativo` literal; o HTML não o exibe |
| Regulação | Pós sem "reconhecida pelo MEC" | ok | P2 e OC1-A falam em "órgão regulador" |
| Regulação | Curso livre não confere diploma | não se aplica | não é peça de venda |
| Regulação | Nota MEC com fonte | ok | nenhuma |
| Promessas | Emprego, salário, aprovação | ok | nenhuma |
| Promessas | Empregabilidade com fonte; superlativos; comparação | não se aplica | nenhum |
| Preço | Valor, parcelas e condições completas | ok | B5 resolvido |
| Preço | Bolsa e desconto com regra, público e validade | **falha** | pos-359.json: o desconto de 12% sem regra não segura peça final (B6). A peça sairia para uma página com desconto incompleto, contra a regra 10 |
| Preço | Urgência real | ok | nenhum "últimas vagas"; vagas restantes null com P11 |
| Preço | Prouni, Fies | ok | nenhum |
| Pessoas | Autorização de imagem e voz | ok | só contagens, decisões 8 e 10 |
| Pessoas | Menores | não se aplica | G10 registrado como pendência |
| Pessoas | Formulário com finalidade e privacidade | não se aplica | trava OB1 registrada |
| Pessoas | WhatsApp e e-mail com consentimento | não se aplica | nada enviado |
| Pessoas | Nenhum dado pessoal | ok | nenhum nos JSON abertos |
| Plataformas | Página de destino entrega o prometido | **falha** | pos-679.json e pos-68636.json: a P3 (link trocado e data sem planilha) não bloqueia anúncio, mas o plano manda a subida esperar a P3 (B7) |
| Anúncios (Meta e Google) | Todos os itens | não se aplica | o mapa não é anúncio |

**Resultado:** Bloqueado. Itens bloqueados: desconto da 359 (B6) e página de destino de 679 e 68636 (B7). Revisado por: qa-de-marketing (agente); falta o humano. Data: 27/10/2026.

### 6.2 Parte 2 (documento final)

| Bloco | Item | Resultado | Onde |
|---|---|---|---|
| Dados do curso | Nome, modalidade, CH, duração e turno batem com o catálogo | **falha** | lista da próxima etapa: 719 e 68629 com o nome "[CONFIRMAR]" (D13); no resto, nomes, datas, campus e preços batem com o catálogo |
| Dados do curso | Status "aberto" ou sem chamada | ok | o documento não chama para inscrição |
| Dados do curso | Modalidade clara | ok | 2.7 separa presencial e transmitido |
| Regulação | Graduação com ato do catálogo | não se aplica | o documento não cita o ato |
| Regulação | Pós sem frase ligada ao MEC | ok | "frase ligada ao MEC" só como pendência a corrigir no site (seção 1, frase 3; 2.2; 4.5, itens 29 a 31) |
| Regulação | Curso livre não confere diploma | não se aplica | não é peça |
| Regulação | Nota MEC com fonte | ok | nenhuma |
| Promessas | Emprego, salário, aprovação | ok | nenhuma |
| Promessas | Superlativos, comparação | ok | nenhum |
| Preço | Valor, parcelas e condições completas | ok | os preços aparecem como dado do catálogo e não como oferta; mensalidades da Graduação com a regra do edital citada |
| Preço | Bolsa e desconto com regra | ok | regras das provas do catálogo; cupom com público e validade [CONFIRMAR] |
| Preço | Urgência real | ok | toda data de 4.1 a 4.6 tem origem ou [SUPOSIÇÃO]; nenhum "últimas vagas" |
| Preço | Prouni, Fies | ok | nenhum |
| Pessoas | Autorização de imagem | ok | nenhum docente citado por nome |
| Pessoas | Nenhum dado pessoal | ok | nenhum nome, telefone, CPF ou e-mail; "informado pelo CEO" é função |
| Pessoas | Nome de pessoa | ok | nenhum na narrativa nem nos JSON abertos [SUPOSIÇÃO: os 70 JSON do recorte não abertos seguem a mesma regra do gerador] |
| Marca | Nunca chamar a TGH de "Agência" | ok | nenhuma ocorrência de "Agência" nem de TGH na narrativa ou nos trechos do HTML lidos |
| Dados | Número inventado | **falha** | "13 campanhas Meta ativas" (D6) e números de cards fora do recorte (D1); não são inventados, mas estão errados contra a fonte |
| Plataformas | Página de destino | não se aplica | o documento não é anúncio |

**Resultado:** Bloqueado. Itens bloqueados: nomes da próxima etapa (D13) e números D1 e D6. Revisado por: qa-de-marketing (agente); falta o humano. Data: 27/10/2026.

---

## 7. Próximo passo

1. O orquestrador aplica 5.1 e 5.2 nos geradores e gera de novo os JSON, o mapa e o documento.
2. O relatorios aplica C1 a C16 com o texto exato. Antes da versão final, confirma ou marca os itens "não conferido" da seção 3.2.
3. Nova reconferência curta do qa: B6, B7, B13, N1, N2 e D1 a D16. Depois disso, o documento segue para a aprovação humana (pessoa do marketing) antes de ir à diretoria da Ufape.

---

## Fatos (com fonte)

- A regra 10 do plano da onda 3 segura toques, posts e cards de 359 e 352 até a página corrigida ou o desconto retirado. A 2.3 diz "359 sem pré-requisito, sem desconto". Fonte: cmo-pos-2026-10-27-onda3.md.
- Subida de 679 e 68636 só com P3: cmo-pos-2026-10-27-onda3.md, seção 3 (anuncios-meta v6) e 4.1.
- Decisão 19 libera peças e mídia da 698: docs/execucao-2026-10-26.md.
- Na revisão qa-de-marketing-eventos-2026-10-27-c.md os posts voltaram CORRIGIR com 1 troca e as mensagens foram APROVADAS. A troca está aplicada na linha 332 de posts-sociais-eventos-2026-10-26.md.
- Abril tem 129 cards: 52 firmes, 77 de lacuna e 65 com reservas. Fonte: docs/andamento-planejamento.md (O6).
- PP13 e PP14 estão fechados: docs/andamento-planejamento.md (F11).
- "Campanhas Meta das 14 turmas (13 ativas; 662 pausada até OU18)": docs/pendencias-camada-1.md.
- As 6 turmas iniciadas "seguem com campanha paga ATIVA": cmo-geral-2026-10-26.md, 2.1 item 2; docs/execucao-2026-10-26.md.
- O documento tem 100 itens no mapa e 12 na próxima etapa (HTML, linhas 231 e 256; lista IDS na linha 263).

## Suposições ([SUPOSIÇÃO])

- [SUPOSIÇÃO] Os JSON fora da amostra seguem as mesmas regras do gerador, sem exceção por item além das já vistas.
- [SUPOSIÇÃO] A data de 03/11 do item 39 vem de algum plano que não abri. Só o texto "pausadas" contradiz as fontes lidas.
- [SUPOSIÇÃO] As definições do glossário (C16) descrevem o uso dos termos nos planos lidos. Não criam regra nem dado.

## Dados que faltam ([CONFIRMAR])

- [CONFIRMAR] Fonte de "6 turmas iniciadas e pausadas" e da data de 03/11 (A4).
- [CONFIRMAR] Data de cada pedido de mídia (30/11 e 30/12) no gestor-de-midia-pos.
- [CONFIRMAR] Os itens "não conferido" da seção 3.2.
- [CONFIRMAR] Quem aprova cada tipo de peça (contexto/ufape-geral.md, regras de aprovação, ainda vazio).

## Fontes

- contexto/ufape-geral.md
- contexto/catalogo-de-cursos.md
- auditorias/conformidade-educacional.md
- docs/execucao-2026-10-26.md
- docs/andamento-planejamento.md
- docs/pendencias-camada-1.md
- saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md
- saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md
- saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27-documento-final.html
- saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md
- saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-mapa.md
- saidas/10-operacoes-de-marketing/qa-de-marketing-eventos-2026-10-27-c.md
- saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md
- saidas/10-operacoes-de-marketing/cursos/ (JSON listados no cabeçalho)
- ferramentas/mapa-mental/mapa_html.py e ferramentas/mapa-mental/documento_final.py
