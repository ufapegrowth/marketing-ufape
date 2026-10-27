# Revisão do qa-de-marketing: mapa mental HTML e 184 JSON por item (etapa M.4)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** geral (graduacao, pos, livres e eventos)
- **Data:** 27/10/2026
- **Encomenda:** M.4 do plano geral (saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seções 4 e 6)
- **Revisado:** saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27.html e saidas/10-operacoes-de-marketing/cursos/*.json, gerados por ferramentas/mapa-mental/mapa_json.py e ferramentas/mapa-mental/mapa_html.py. Nenhum arquivo revisado foi editado.
- **Entradas lidas:**
  - contexto/ufape-geral.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20)
  - contexto/catalogo-de-cursos.md (inteiro, seções 1 a 9)
  - contexto/cursos/graduacao/editais-2027-1.md (linhas 1 a 59)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 9)
  - saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md (cabeçalho, correções e seção 1 inteira, com o exemplo 707)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (cabeçalho, seções 0 e 1)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (cabeçalho, seções 0, 1.1 e 1.2)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (cabeçalho, para conferir que o arquivo citado existe)
  - auditorias/09-analytics.md, auditorias/10-operacoes.md, auditorias/conformidade-educacional.md
  - docs/pendencias-camada-1.md (inteiro)
  - docs/andamento-planejamento.md (inteiro)
  - ferramentas/mapa-mental/mapa_json.py e mapa_html.py (inteiros)
  - HTML: linhas 1 a 121 (cabeçalho, estilo, estrutura e rodapé). A linha de dados embutidos não foi lida byte a byte: ela é gerada do mesmo ferramentas/mapa-mental/saida/mapa-dados.json que gera os JSON [SUPOSIÇÃO: o HTML foi gerado na mesma rodada dos JSON].
- **Método:** como os 184 arquivos saem de um script, conferi a regra no gerador e a confirmei numa amostra estratificada de 26 JSON (lista na seção 2). Cada achado traz a regra que o script deve seguir.

---

## 1. Veredito

**CORRIGIR.**

Motivo em uma frase: o mapa abre offline, não tem dado pessoal, nome de pessoa nem frase de certificação ligada ao MEC, e os dados copiados do catálogo batem com a fonte. Mas o gerador contradiz o plano e o diário em pontos que mudam decisão. São estes:

- as 6 turmas iniciadas com campanha ativa aparecem como "mídia não consta", sem pendência;
- a 623 não traz a trava da decisão 13;
- a Graduação e a 352 aparecem sem bloqueio;
- as 14 provas fora de venda entram na campanha de 27/11;
- o preço estruturado de Livres e Eventos soma o à vista com o parcelado;
- o transmitido 68634 aparece como presencial;
- o nome do workshop traz "Simpósio";
- faltam pendências e aprovações dos planos das ondas;
- há desvios de vocabulário e de campos obrigatórios do esquema versão 1.

Pela regra do qa, uma falha em auditorias/conformidade-educacional.md (modalidade do 68634 e preço estruturado) já basta para o veredito ser corrigir. Todas as correções cabem no gerador. Depois de aplicadas, peço nova rodada curta de conferência (mesma amostra e os itens B1 a B14).

---

## 2. Amostra conferida (26 JSON, todas as linhas e tipos)

| # | Arquivo | Estrato |
|---|---|---|
| 1 | pos-707.json | Pós, onda 1 (reta final) |
| 2 | pos-698.json | Pós, onda 1 (decisão 19) |
| 3 | pos-657.json | Pós, onda 2 |
| 4 | pos-333.json | Pós, onda 2 (regra 8, OU12, OU17) |
| 5 | pos-68632.json | Pós, onda 3 lote A (abril) |
| 6 | pos-662.json | Pós, onda 3 (espera total, OU18) |
| 7 | pos-352.json | Pós, onda 3 lote B (maio) |
| 8 | pos-68642.json | prova de bolsa, Goiânia (decisão 20) |
| 9 | pos-691.json | prova de bolsa, histórico (sem venda) |
| 10 | pos-68656.json | prova de bolsa, encerrada (link fora do ar) |
| 11 | pos-650.json | Pós iniciada com campanha ativa (pendência) |
| 12 | pos-670.json | Pós encerrada (link fora do ar) |
| 13 | livres-623.json | livre presencial, onda 1 (decisão 13) |
| 14 | livres-68634.json | transmitido do workshop, pendência |
| 15 | livres-616.json | livre online com data, onda 2 |
| 16 | livres-469.json | minicurso contínuo |
| 17 | livres-347.json | espanhol contínuo |
| 18 | livres-575.json | espanhol presencial em Lima, pendência |
| 19 | livres-68665.json | grupo de estudos com data, onda 1 |
| 20 | livres-721.json | grupo de estudos contínuo |
| 21 | livres-639.json | aprimoramento na Ufape Clínica, pendência |
| 22 | eventos-workshop-neuromonitorizacao-2026-11-20.json | workshop |
| 23 | eventos-700.json | congresso gravado contínuo (tipo simposio) |
| 24 | eventos-sem-codigo-simposio-plantonista-veterinario.json | simpósio passado, sem página |
| 25 | graduacao-medicina-veterinaria.json | Graduação |
| 26 | graduacao-pedagogia.json | Graduação |

Conferência campo a campo contra o catálogo, linha literal, local, modalidade, turma, CH, início, preço, status: todos os 26 batem com contexto/catalogo-de-cursos.md. Os itens com regra fora do catálogo também batem com as fontes:

- metas: 15 matrículas e R$ 2.000,00 só em Pós com recorte "planejar" e na Graduação (decisões 15 e 16);
- turma mínima: 15 na Pós (decisão 11) e 30 na Graduação (catálogo, "Como usar");
- data_fim do workshop (21/11/2026) e 16 h: decisão 6;
- notas GUT: seção 3 do plano;
- dias_ate_inicio: contados de 27/10/2026, igual a atualizado_em (R8). O plano contava de 26/10, por isso a diferença de 1 dia é esperada;
- datas e números das descrições de pendência: decisão 16, planos das ondas 2 e 3 e editais. São elas 27 e 28/03/2027, 01/05/2027, 24/04/2027, 26 contra 24 módulos, R$ 260,00, 17/08/2026, 22/02/2027 e "só para o 1º semestre de 2027".

---

## 3. Achados que bloqueiam (B): a correção é obrigatória

### B1. As 6 turmas iniciadas com campanha ativa aparecem sem campanha e sem pendência

- **Arquivos:** pos-650.json (conferido), pos-68662.json, pos-706.json, pos-586.json, pos-554.json e pos-68612.json (mesma regra do gerador).
- **Campos:**
  - status_midia.campanha = "nao_consta" e status_midia.vinculo_com_a_visao = "nenhum";
  - pendencias só com P1;
  - aprovacoes = [];
  - resumo.bloqueado = false;
  - motivo_do_recorte genérico.
- **Fonte:** o plano geral, 2.1 item 2, trata esses itens como "pendência urgente", e a seção 3 lhes dá GUT 80. A pendência é P8 e o pedido é o A4, aberto pelo briefing ("Decisão sobre as 6 turmas iniciadas com campanha ativa"). O backlog também lista a pausa das 6 campanhas (docs/pendencias-camada-1.md, seção 4).
- **Regra para o gerador:**
  - incluir em MIDIA os códigos de 2.1 item 2 do plano geral com "ativa";
  - para esses códigos, gravar motivo_do_recorte "pendência urgente: turma iniciada com campanha ativa (plano geral, 2.1 item 2)";
  - criar a pendência ref_plano "P8", tipo "outro", bloqueia ["anuncio"], descrição "Decidir pausa ou manutenção da campanha ativa em turma iniciada (A4)", campos ["status_midia.campanha"];
  - criar a aprovação "A4" copiada da seção 8 do plano (o que, por que, quanto "[CONFIRMAR]", efeito, como desfazer).
  - Ler a lista do plano, não digitar à mão.

### B2. A 623 não traz a trava da decisão 13

- **Arquivo:** livres-623.json.
- **Campos:** pendencias (só P1 e decisão 14), aprovacoes = [], relacionados = [], resumo.bloqueado = false, enquanto status_midia.campanha = "ativa".
- **Fonte:**
  - decisão 13: até a correção do site, nenhuma campanha nova aponta para a 623;
  - pedido R8 (docs/pendencias-camada-1.md): trocar para a 68637 ou pausar;
  - P7 do plano: 623 e 68637 são duplicidade provável;
  - diário: a página 623 mostra 01 e 02/08/2026.
- **Regra para o gerador:**
  - em ESPECIFICAS["623"], criar a pendência ref_plano "decisão 13", tipo "link", bloqueia ["anuncio", "peca_final"], descrição "Página com data de início errada; nenhuma campanha nova aponta para ela até a correção no site";
  - criar a aprovação "R8" com o texto de docs/pendencias-camada-1.md;
  - em 623 e em 68637, gravar relacionados com relacao "duplicidade_provavel" e natureza "[SUPOSIÇÃO]", nos dois sentidos.

### B3. A Graduação aparece sem bloqueio, mas o diário diz que publicação e envio estão bloqueados

- **Arquivos:** graduacao-medicina-veterinaria.json e graduacao-pedagogia.json.
- **Campos:** pendencias (só P1 e "edital"), resumo.bloqueado = false, resumo.pendencias_abertas fixo em 2 no código (mapa_json.py, linha 379).
- **Fonte:**
  - diário de 26/10, qa rodada e: "Publicação e envio bloqueados pelas pendências G6, G7, G8, G10 a G14, templates da Meta, datas do Enem e U12 e U13";
  - diário de 27/10: "nada sobe sem MP1, MP2, MP4, MP10, G13 e G14; peça com preço ou desconto também precisa de G7 e G12";
  - U13 (MP15): meta de 15 contra a turma mínima de 30;
  - CH da Pedagogia: o catálogo traz "3.440 h no site; 3.640 h no edital [CONFIRMAR]".
- **Regra para o gerador:**
  - criar uma pendência por código de trava da Graduação, lido da revisão do qa da Graduação e do diário, com bloqueia ["peca_final"] para G6 a G14, ["anuncio"] para MP1, MP2, MP4 e MP10 e ["meta"] para U12 e U13;
  - criar a pendência de divergência da CH da Pedagogia, com campos ["carga_horaria"], porque a R4 manda abrir pendência quando o catálogo traz marcador;
  - calcular resumo.pendencias_abertas e resumo.bloqueado com a mesma função dos outros itens, nunca com número fixo;
  - aprovacoes: na Pedagogia, citar só AM1 a AM12 (o diário diz "Pedagogia 100% Meta"; AG1 a AG11 são da Medicina Veterinária).

### B4. As provas fora de venda entram na campanha das provas de 27/11

- **Arquivos:**
  - pos-691.json (conferido) e as outras 12 provas "sem venda": 687, 689, 695, 682, 681, 684, 680, 688, 694, 685, 690 e 693;
  - pos-68656.json (encerrada).
- **Campos:**
  - grupo_de_campanha = "provas-de-bolsa-2026-11-27";
  - kit.entregas com "Campanha única das provas de 27/11";
  - a pendência "decisão 14" põe resumo.bloqueado = true;
  - canais com instagram, facebook, youtube e whatsapp "ativo".
- **Efeito:** no HTML, essas 14 provas mostram um kit e canais ativos e entram na contagem "com pendência que bloqueia peça final".
- **Regra para o gerador:**
  - grupo_de_campanha, kit da campanha única e pendência "decisão 14" só para tipo prova_de_bolsa com recorte "planejar";
  - em qualquer item com recorte "historico" ou "pendencia": kit.entregas = [], grupo_de_campanha = null e os 8 canais com estado "fora" e motivo "fora do recorte do plano (seção 2.4)". O esquema pede sempre 8 canais.

### B5. O preço estruturado de Livres, Eventos e provas soma o à vista com o parcelado

- **Arquivos:**
  - livres-616.json: 5x de R$ 240,00 com total 990.00, e 5 x 240 = 1.200;
  - livres-469.json: 5x de R$ 62,40 com total 260.00;
  - livres-623.json: 6x de R$ 205,00 com total 890.00;
  - livres-575.json: 6x de R$ 1.368,00 com total 6840.00;
  - eventos-700.json: 10x de R$ 98,00 com total 780.00;
  - livres-347.json: 10x de R$ 75,00 com total 580.00;
  - e todos os itens com o padrão "R$ X à vista ... ou Nx de R$ Y no cartão".
- **Campo:** preco_estruturado.
- **Por que bloqueia:** a R8 só permite preco_estruturado "quando bate com o texto do site". Nesses itens, a plataforma leria "5 parcelas de R$ 240,00, total R$ 990,00", condição que o site não oferece. Isso falha no item de preço da conformidade (CDC).
- **Regra para o gerador:** gravar preco_estruturado só quando parcelas x valor_parcela for igual ao total do texto, com diferença de no máximo R$ 0,01 por parcela (arredondamento). Caso contrário, gravar null, e preco_texto_site segue como a fonte. Campo opcional novo (por exemplo "a_vista") só com acordo do arquiteto-de-fluxos: campo novo opcional não muda a versão, mas tem de entrar no documento de fluxo.

### B6. Faltam nos JSON pendências dos planos das ondas e das travas registradas

Para conferir as pendências por turma, comparei cada JSON com a coluna "Bloqueio" das tabelas 1.1 e 1.2 do plano da onda 3, com a seção 1 do plano da onda 2 e com as travas de docs/pendencias-camada-1.md.

| Turma | O que falta no JSON | Fonte |
|---|---|---|
| 352 | P4: data diverge (planilha 24/05/2027, uma segunda-feira; site e cronograma em 24/04/2027); OU23 (desconto de 10%). Hoje resumo.bloqueado = false, enquanto a 366, com o mesmo problema, bloqueia | onda 3, tabela 1.2; plano geral, P4 |
| 719 | OU28 (público não veterinário) | onda 3, tabela 1.2 |
| 68629 | data só no site, sem linha na planilha | onda 3, tabela 1.2 |
| 359 | OU24 (desconto de 12% e pré-requisito) | onda 3, tabela 1.2 |
| 699 | OU27 (público contra ingresso) | onda 3, tabela 1.2 |
| 68623 | OU26 (local da prática) | onda 3, tabela 1.2 |
| 60 | dia do 3º módulo [CONFIRMAR NO CATÁLOGO] | onda 3, tabela 1.2 |
| 68616 | dia do módulo 2 presencial | onda 3, tabela 1.2 |
| 68609 | convite da prova de Especialista na página; `matriz` corrigida no site | onda 3, tabela 1.1; pendencias-camada-1, travas do lote A |
| 68617 | URL "/v/" conferida antes da subida; `matriz` corrigida no site | onda 3, tabela 1.1; travas do lote A |
| 68628 e 68636 | `matriz` corrigida no site | travas do lote A |
| 8 turmas de abril | OU15 (quem grava os Reels) | travas do lote A |
| 662 | P5 (turma IV no site e V na planilha) e P3 (link trocado) | onda 3, tabela 1.1; plano geral, P3 e P5 |
| 68615 | OU13 (CEP diferente) | onda 2, seção 1 |

- **Regra para o gerador:**
  - ler a coluna "Bloqueio" das tabelas 1.1 e 1.2 do plano da onda 3 e a lista "Travas" de cada bloco de docs/pendencias-camada-1.md;
  - criar uma pendência por código citado, com a fonte do arquivo lido;
  - divergência de data entre planilha e site (P4) recebe sempre bloqueia ["data", "peca_final"], como já acontece na 366;
  - não manter pendências digitadas à mão em ESPECIFICAS quando a fonte é uma tabela.

### B7. Faltam as pendências P3, P6, P7 e P17 do plano geral e o campo relacionados está sempre vazio

- **Arquivos e campos:**
  - pos-68641.json e pos-68642.json: falta P3 (links das provas de Cardiologia de São Paulo e de Goiânia invertidos). O plano manda que nenhuma peça cite preço ou data desses itens até a correção. Hoje pagina_oficial vem da ficha sem aviso;
  - livres-573.json, livres-68614.json e livres-68618.json: falta P6 (data da visão de campanhas diferente). status_midia.divergencia_de_data = false e status_midia.inicio_na_visao = null, mas a visão traz 29/11, 18/12 e 22/05/2027. O plano manda peças sem data até a confirmação;
  - P7, relacionados vazio em 623 e 68637, 643 e 713, 642 e 712, e na linha "Paciente Grave" sem página e o 700;
  - 68634 sem relacao "modalidade_do_mesmo_evento" com o workshop (2.1 item 7);
  - livres-347.json e livres-501.json: falta P17 (revisão por falante nativo antes de marcar como pronto);
  - livres-721.json, livres-720.json e livres-68663.json: falta a pendência de política de entrada dos grupos já iniciados (2.1 item 3).
- **Regra para o gerador:**
  - ler a tabela da seção 7 do plano geral e criar, para cada código citado em "Itens afetados", a pendência com o ref_plano da linha (P3 a P17);
  - preencher relacionados a partir de P7 e de 2.1 item 7;
  - preencher status_midia.inicio_na_visao com a data da visão quando o plano a cita, e divergencia_de_data = true quando ela difere de inicio.

### B8. Faltam aprovações pedidas e algumas vêm com valor errado

- **Arquivos e campos:**
  - pos-707.json, pos-68604.json, pos-68606.json, pos-698.json, pos-68610.json e pos-68608.json: aprovacoes = []. O plano da onda 1 pede OA1 a OA12, inclusive o OA9 (envio de 28/10 às 9h) e OA2-B e OA3-B (diário e docs/pendencias-camada-1.md, 2b);
  - pos-662.json: aprovacoes = []. Faltam OC8 e OM2 (pausa da campanha ativa);
  - eventos-workshop-neuromonitorizacao-2026-11-20.json: aprovacoes = []. Faltam R3 (EVM1, calendário de mídia) e R7;
  - onda 2 e lote A: faltam OB4 e OB5, AD-F6-1 a AD-F6-5, AF1 a AF7, DEC1 a DEC7 e MO1 a MO6 (onda 2), e OM1 a OM7, AD-O6-1 a AD-O6-8, AF e DEC (onda 3);
  - aprovação "AMP13 a AMP25 e AGP12 a AGP25" com quanto = "sem verba nova": está errado, porque a mídia é R$ 2.000,00 por turma (decisão 15);
  - efeito_esperado "turma pronta para a subida de 07/12" em 657 e 341: as duas sobem em 14/12, só com PP7 (onda 2, seção 1);
  - efeito_esperado "subida de abril" nas turmas de abril: não há subida em abril.
- **Regra para o gerador:**
  - montar aprovacoes a partir das tabelas de pedidos de cada plano (onda 1, seção de pedidos; onda 2 e onda 3, seção 9) e de docs/pendencias-camada-1.md, filtrando pela turma citada;
  - quanto da mídia = metas.verba formatado ("R$ 2.000,00 por turma, decisão 15");
  - efeito_esperado copiado do plano, ou neutro ("conforme o plano da onda") quando o plano não traz texto por turma. Nunca uma data montada pelo script.

### B9. Workshop e transmitido 68634: nome, modalidade e dados do catálogo

- **eventos-workshop-neuromonitorizacao-2026-11-20.json:**
  - nome_padrao copia o nome com "(na planilha: I Simpósio Brasileiro de Neuromonitorização Veterinária)". O HTML usa esse nome como título do nó. A decisão 7 manda o nome oficial "Workshop Brasileiro de Neuromonitorização" e nunca "simpósio".
  - **Regra:** nome_padrao do workshop = nome oficial da decisão 7; o nome da planilha vai para aliases; o HTML mostra nome_padrao (ver B11).
- **evento.cupom.desconto_texto = "[CONFIRMAR]"**, mas o catálogo traz "20% de desconto".
  - **Regra:** copiar o trecho literal do catálogo (R4).
- **evento.modalidades = []**, mas o catálogo traz duas: presencial, teórico e prático, 16 h, 30 vagas, R$ 1.250,00; transmitido mais gravado, só teoria, R$ 450,00, produto 68634.
  - **Regra:** preencher modalidades com nome, preco_texto_site literal, vagas (30 no presencial; null com pendência no transmitido) e produto.
- **Kit:**
  - a chave "mensagem_convite" junta 4 entregas com quantidade_minima 4. O esquema (1.4) pede mensagem_convite (1), mensagem_vespera (1), mensagem_do_dia (1) e email_convite (1) separadas;
  - "pagina" está como "nao_aplicavel", mas o template pede página (1) e a página neuro-summit existe.
  - **Regra:** gerar as 7 chaves do template na variação workshop. A página entra com status "inventario_pendente" e o arquivo da página oficial, porque o que já existe conta como entregue se passar na conformidade (plano, seção 4).
- **Pendências que faltam:** U9 (fim das inscrições e validade e limite do cupom), com campos ["fim_das_inscricoes", "evento.cupom"].
- **livres-68634.json:**
  - linha "livres", tipo "livre_presencial", modalidade_normalizada "presencial". O produto é "TRANSMITIDO + GRAVADO", e o plano (2.1 item 7) o põe na linha Eventos, no kit do evento. Aparecer como presencial falha no item da conformidade "EAD não aparece como presencial nem o contrário";
  - **Regra:** 68634 com linha "eventos", linha_origem "plano", tipo "workshop", modalidade_normalizada "online" (ou "[CONFIRMAR]"), relacionados com o workshop e a pendência P9 (CH de 24 h no produto contra 16 h oficiais; local "Saiba Mais"), bloqueia ["peca_final"].

### B10. Recorte de 670 e 68656 diferente do plano

- **Arquivos:** pos-670.json e pos-68656.json.
- **Campo:** recorte = "historico". O plano diz "pendência" (2.1 item 5: "Os dois aparecem no mapa como pendência"; 2.4: 670 e 68611 em pendência).
- **Problema associado:** dias_ate_inicio = 165 e 31 nesses itens encerrados. O HTML mostra "faltam 165 dias" num curso encerrado.
- **Regra para o gerador:**
  - os itens citados no plano como pendência (2.1 item 5 e 2.4) recebem recorte "pendencia", mesmo com status "encerrado";
  - dias_ate_inicio só é calculado em recorte "planejar". Nos demais, null.

### B11. HTML: contagens rotuladas de forma diferente do plano e nome errado no nó

- **Arquivo:** cmo-geral-2026-10-27.html.
- **Contagens:** o cartão "no recorte do plano" conta recorte "planejar" e dá 112, porque inclui as 2 Graduações. O plano fixa 110 no recorte mais 2 da Graduação, ramo à parte. O cartão "onda 1" dá 37 contra 35 itens do plano.
  - **Regra:** o cartão do recorte conta linha diferente de graduacao e mostra "110 no recorte + 2 da Graduação". O cartão da onda 1 mostra "35 + 2 da Graduação" (o briefing põe a Graduação na onda 1).
- **Nó do item:** mostra nome_no_site. A seção 6.1, nível 4, pede o nome padrão, e o workshop aparece com "Simpósio" (B9).
  - **Regra:** o título do nó usa nome_padrao. nome_no_site vai no detalhe.
- **Coluna "Mín." do kit:** mostra "1 por docente".
  - **Regra:** escrever "1 por docente autorizado" (regra_quantidade).

### B12. Vocabulários fechados e campos obrigatórios do esquema versão 1

| Arquivo | Campo | Desvio | Regra para o gerador |
|---|---|---|---|
| Pós das ondas 2 e 3 (pos-657, pos-352, pos-68632 e outras) | canais[*].natureza | "plano_da_onda" não está no vocabulário (proposta_do_cmo, confirmado_em_1.20). Mudar valor permitido exige versao_schema 2 | usar "proposta_do_cmo" e citar o plano da onda no motivo |
| todos com kit | kit.entregas[*].responsavel | texto; o esquema pede lista de agentes | gravar lista (["landing-page", "seo-on-page"] na página, como no exemplo 707) |
| todos com kit | kit.entregas[*].secao e ref_aprovacao | chaves obrigatórias ausentes | gravar as duas, com null |
| Pós da onda 1 | kit.inventario e kit.acrescimos | inventário pendente e acréscimos da seção 4 do plano (inventário, reta final, pausa e relatório final) ausentes | gerar kit.inventario {situacao "pendente", prazo, responsavel "cmo"} e os 3 acréscimos do exemplo 707 do arquiteto |
| 13 minicursos de 8 h (livres-469 e outros "Mini Curso") | tipo | "livre_online"; o vocabulário tem "minicurso" e o plano conta 13 minicursos à parte | tipo "minicurso" quando o nome começa com "Mini Curso" ou "Mini curso" |
| 68668, 68622, 68613 e 715 (seção 4 do catálogo) | tipo | "livre_presencial"; o nome é de aprimoramento | tipo "aprimoramento" quando o nome contém "Aprimoramento" |
| todos | pendencias[*].id | "P1", "decisão 14", "E1": fora do padrão "<codigo>-p01" e com espaço e acento | id = "<codigo>-p" + número de 2 dígitos; a referência fica só em ref_plano |
| todos | ordem das chaves (R13) | blocos prova_de_bolsa, evento e graduacao gravados depois de historico | gravar na ordem do modelo 1.5 (bloco por tipo depois de equipe) |

### B13. null sem pendência significa "não se aplica" (R2), e o gerador deixa null por origem vazia sem pendência

- **Campos, em todos os itens do recorte:**
  - fim_das_inscricoes, vagas.vagas_ofertadas, vagas.vagas_restantes;
  - equipe.coordenadores_na_ficha, equipe.docentes_na_ficha, equipe.autorizacoes_de_imagem_registradas;
  - metas.cpl_maximo, metas.custo_por_matricula_maximo, numeros_agregados.*, kit.entregas[*].prazo e kit.entregas[*].autorizados;
  - nas provas: prova_de_bolsa.bolsas_previstas;
  - no workshop: evento.palestrantes.*;
  - na Graduação: graduacao.turnos = [] e graduacao.inscricao_ate.
- **Efeito:** a plataforma vai ler "não se aplica" onde o dado só falta. A conferência C11 do esquema não passa.
- **Regra para o gerador:** criar em todo item do recorte uma pendência padrão que cite esses caminhos em "campos":
  - P11, para metas, números e vagas restantes;
  - OU4, para vagas ofertadas na Pós;
  - U3, para inscrições e resultado das provas;
  - U9, para o workshop;
  - "[CONFIRMAR autorização]", para as contagens de autorização;
  - prazo do kit, com fonte no plano da onda.
- Em prova_de_bolsa, equipe inteira vira null (não se aplica), como manda 1.3.

### B14. Arquivos de camada marcados como pendentes de aprovação quando o diário os tirou de uso

- **Arquivos:** livres-*.json com arquivos_por_camada.linha e area apontando para cmo-livres-2026-10-26.md e mensagens-livres-2026-10-26.md, estado "pendente_de_aprovacao" (conferido em livres-623.json).
- **Fonte:** diário de 27/10 (integração do branch): esses arquivos foram escritos antes das decisões 7 a 18 e "ficam como rascunho a revisar, sem uso em peça".
- **Regra para o gerador:** manter uma lista de saídas "a revisar" lida do diário. Esses caminhos entram com estado "devolvido" e, no HTML, com o rótulo "rascunho a revisar". Nunca com "pendente_de_aprovacao".

---

## 4. Ressalvas e desvios aceitáveis (não bloqueiam; registrar e alinhar)

| # | Desvio | Por que é aceitável | O que fazer |
|---|---|---|---|
| D1 | Provas com prova_de_bolsa.formato "presencial" e modalidade_normalizada "presencial", contra a tabela 1.4 do esquema, que diz "online" | decisão 20 do CEO (27/10/2026) revoga a parte "online" da decisão 11 | arquiteto-de-fluxos atualiza 1.3 e 1.4 na próxima versão do esquema; até lá, o desvio fica registrado |
| D2 | Campos deixados "[CONFIRMAR]" ou null embora a fonte tenha o dado: nota de corte, prazo de matrícula, canal do resultado e bolsas das provas; número, título e URL dos editais e turnos e vagas da Graduação (45, 45 e 80 em editais-2027-1.md); contagens de docentes da ficha; ficha_lida_em | conservador: nas provas, a decisão 11 manda a regra de cada ficha e 12 fichas se contradizem (U1); nada foi inventado | com B13 aplicado, cada lacuna fica explicada. Recomendo copiar edital, turnos e vagas da Graduação com campos_so_na_ficha (R6) e gravar ficha_lida_em quando o script lê a ficha (modulos e pagina_oficial já saem dela) |
| D3 | status_midia.vinculo_com_a_visao "provavel" em todos os itens com mídia, formatos = [] e cinco_angulos "nao_consta" | a visão de campanhas não traz código; "provavel" é a leitura mais segura | quando o cmo conferir a visão por item, trocar para "exato" e copiar formatos e ângulos |
| D4 | historico[*].aplicado_por "orquestrador"; o esquema (R12) diz que o único escritor é o cmo | o script foi rodado pelo orquestrador sobre o plano do cmo | o cmo ratifica a versão 1 (ou o gerador grava "cmo" com origem "gerador"); revisao_aprovada sobe só com a aprovação humana |
| D5 | Canais da onda 1 da Pós, das provas e dos Livres seguem a seção 5 do plano geral (LinkedIn "teste" e YouTube "ativo") | natureza "proposta_do_cmo" é verdadeira | atualizar com 1.15 v2 (LinkedIn só como teste da 657), a estratégia de mídia v3 e posteriores (com R$ 2.000,00 por turma, sem YouTube e LinkedIn) e o youtube v2 (teste condicionado) |
| D6 | Graduação com TikTok "teste"; a seção 5 diz "Ativo, se houver perfil e quem produza" | é condicional, e a leitura "teste" é razoável | marcar o motivo com [SUPOSIÇÃO] (R11) |
| D7 | Grupos 68665 e 68666 com o kit inteiro de Livres; o plano fala em "kit leve" | o mínimo nunca diminui, e a decisão 14 suspende Livres | cmo confirma qual kit vale para grupos de estudos com data |
| D8 | 662 com o kit todo "a_fazer"; o plano diz "espera total (OU18)" | a pendência OU18 explica e bloqueia | opcional: status "aguardando_autorizacao" não serve; manter "a_fazer" com a pendência |
| D9 | Graduação com fontes.ficha apontando para editais-2027-1.md, e não para a ficha do curso do catálogo; status_catalogo_texto montado ("inscrições abertas desde 17/08/2026 (edital)") | o texto vem de "Como usar" do catálogo e bate | gravar a ficha do curso (coluna "Ficha" do catálogo) e incluir status_catalogo_texto em campos_so_na_ficha |
| D10 | Pendência "privacidade" com ref_plano "OB1" em todas as Pós, inclusive onda 1 e maio; em 68615, OB1 é outra coisa (página no ar) | a trava da política de privacidade vale para toda página com formulário | ref_plano "OB1 e OC1-A (política de privacidade)" e fonte do lote certo |
| D11 | 700 com tipo "simposio" (é congresso gravado) | o vocabulário não tem congresso | marcar evento.subtipo com [SUPOSIÇÃO] na pendência |
| D12 | catalogo_linha_literal do Simpósio Plantonista (sem ficha) inclui a coluna vazia de Ficha | só aparência | cortar na coluna "Fonte" também quando a ficha está vazia |
| D13 | Início de contínuos com data antiga (488 em 15/05/2024) aparece no HTML como data de início | é cópia literal do catálogo | no HTML, para modo "continuo", rotular "venda contínua (data do catálogo: ...)" |
| D14 | O diário diz que o HTML foi "publicado como página privada" | é visualização interna, sem dado pessoal | [CONFIRMAR] que o link não é público; publicação para o cliente só com aprovação humana |

---

## 5. HTML (item 7): o que abre e o que a seção 6.1 pede

**Abre sem dependência externa: sim.**

- Um arquivo só, com CSS e JS embutidos, sem `<link>`, sem `src` externo, sem CDN e sem fonte web: só fontes do sistema.
- Busca por nome, código ou local.
- Filtros por linha, onda, área, status do catálogo, mídia e "só com bloqueio".
- Cor por onda e selo vermelho "bloqueia peça final".
- Preço com a nota "site em 26/10/2026; conferir antes de publicar".
- Sem dado pessoal.
- Sem frase de certificação ligada ao MEC: o ato da Graduação não é exibido.

| Nível da seção 6.1 | Mostra | Falta |
|---|---|---|
| 0 | data do recorte, regra de fonte (texto de abertura), total do catálogo, recorte, ondas, bloqueios | meta principal [CONFIRMAR] (turmas de Pós confirmadas com a turma mínima); contagem "110 + 72 + 2" com os rótulos do plano (B11) |
| 1 | ramos Pós, Livres, Eventos, Graduação, com o histórico dentro de cada linha | ramos "Ondas e calendário", "Pendências e bloqueios", "Aprovações", "Squad e camadas" e "Histórico" como ramos próprios |
| 2 (linha) | contagem do ramo e de bloqueios | estratégia da linha (persona, posicionamento, oferta, canais com motivo, metas) e links para os arquivos da camada 1 |
| 2 (ondas) | janela de cada onda (cartões) | itens, GUT, responsáveis e datas de checagem por onda |
| 3 (área) | nome da área e contagem | mensagem central, palavras-chave, conceitos de criativo, docentes autorizados e links da camada 2 |
| 4 (item) | código, local, modalidade, início e fonte, dias, status do catálogo, mídia, onda, GUT, canais, caminho da ficha | nome padrão (B11); a ficha aparece como texto, sem link |
| 5 (dentro do item) | kit com mínimo, responsável, situação e arquivo; pendências; aprovações | prazo da entrega; marcador de cada pendência ([CONFIRMAR] ou [SUPOSIÇÃO]) |

Pelo plano (seção 9), a versão 1 do mapa leva "estrutura, recorte, status, ondas, pendências e aprovações" e a versão 2 leva as camadas 1 e 2. Por isso, o que falta nos níveis 2 (linha) e 3 (área) fica como ressalva para a versão 2. Só B11 é obrigatório agora.

---

## 6. Resultado de auditorias/conformidade-educacional.md, item por item (mapa e JSON)

**DADOS DO CURSO**

| Item | Resultado | Onde |
|---|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | **falha** | os campos literais batem nos 26 da amostra; falham o nome do workshop com "Simpósio" (B9, decisão 7) e a modalidade normalizada do 68634 (B9) |
| Curso com status "aberto" ou a peça não chama para inscrição | ok | o mapa não chama para inscrição; R14 respeitada (recorte "planejar" só com aberto ou contínuo) |
| Modalidade clara e correta; EAD não aparece como presencial | **falha** | livres-68634.json: "TRANSMITIDO + GRAVADO" normalizado como "presencial" (B9) |

**REGULAÇÃO**

| Item | Resultado | Onde |
|---|---|---|
| Graduação: ato do catálogo, sem arredondar | ok | graduacao.ato_autorizativo copiado literal da seção 1 do catálogo |
| Pós: não diz "reconhecida pelo MEC" | ok | nenhum campo de texto repete a frase; P2 e 68615 usam "órgão regulador" |
| Curso livre: não confere diploma | não se aplica | o mapa não é peça de venda |
| Nota MEC só com fonte | ok | nenhuma nota |

**PROMESSAS E PROVAS**

| Item | Resultado | Onde |
|---|---|---|
| Sem promessa de emprego, salário ou aprovação | ok | nenhuma |
| Empregabilidade com fonte | não se aplica | nenhum dado |
| Superlativos com fonte | ok | nenhum |
| Comparação com concorrente | não se aplica | nenhuma |

**PREÇO E CONDIÇÕES**

| Item | Resultado | Onde |
|---|---|---|
| Preço com valor, parcelas e condições completas | **falha** | preco_texto_site está certo, mas preco_estruturado mistura à vista e parcelado (B5) |
| Bolsa e desconto com regra, público e validade | ok | 341 travada por OU10; cupom do workshop sem percentual inventado; bolsas das provas não exibidas |
| Urgência real | ok | nenhum "últimas vagas"; vagas restantes null |
| Prouni, Fies, financiamento | ok | nenhum |

**PESSOAS E DADOS**

| Item | Resultado | Onde |
|---|---|---|
| Autorização de uso de imagem e voz | ok | só contagens, nenhum nome (R10); decisões 8 e 10 |
| Menores de idade | não se aplica | nenhum |
| Formulário com finalidade e política de privacidade | não se aplica | sem formulário; a trava da política aparece como pendência |
| WhatsApp e e-mail só com consentimento | não se aplica | nada enviado |
| Nenhum dado pessoal | ok | nenhum nome, telefone, CPF ou e-mail de aluno, candidato ou docente nos 26 JSON nem no HTML |

**PLATAFORMAS E ANÚNCIOS:** não se aplica, porque o mapa não é anúncio. Mesmo assim, o item "página de destino entrega o que foi prometido" depende de B2 (623), porque o mapa mostra mídia ativa sem a trava.

**RESULTADO:** Bloqueado. Itens bloqueados: modalidade do 68634, nome do workshop e preço estruturado (B5 e B9). Revisado por: qa-de-marketing (agente); falta o humano. Data: 27/10/2026.

## 7. Resultado de auditorias/10-operacoes.md

| Item | Resultado |
|---|---|
| conhecimento/INDICE.md atualizado | [CONFIRMAR]: o diário de 27/10 registra "Pendente: conhecimento/INDICE.md"; o mapa e os JSON precisam entrar no índice |
| Workflows citam só agentes, skills e auditorias que existem | não se aplica: o gerador não é workflow. Os dois workflows do arquiteto (seção 3.9) ainda não viraram arquivo |
| Workflow termina com auditoria e critério de pronto | não se aplica |
| Aprovação humana antes de publicar | ok no texto do HTML ("Nada aqui foi publicado"); ver D14 |
| Acesso mínimo às ferramentas | não se aplica |
| Nenhuma chave em arquivo | ok |
| Documentos com data de revisão | ok (gerado_em, atualizado_em e cabeçalho do HTML) |
| Peça pública passou por qa e conformidade | esta revisão; resultado: corrigir |
| Dados de curso batem com o catálogo | falha em B5 e B9; o resto bate |

## 8. Resultado de auditorias/09-analytics.md

| Item | Resultado |
|---|---|
| Árvore de métricas existe e está atualizada | não está no mapa (fica na estrategia-de-marketing da camada 1); ressalva para a versão 2 do mapa |
| Toda métrica com fonte nomeada | ok: metas com fonte "decisões 15 e 16 do briefing"; números null |
| Relatórios comparam com metas | não se aplica (nenhum número real) |
| Metas não batidas mostradas | não se aplica |
| Insights terminam com ação | não se aplica |
| Lacunas de dados sinalizadas | **falha** parcial: null sem pendência (B13) |
| Backlog revisado | não se aplica |
| CPL, custo por matrícula, conversão e receita por linha | todos null, [CONFIRMAR]; ok como lacuna depois de B13 |
| Nenhum dado pessoal | ok |

## 9. Esquema versão 1 (item 6): R1 a R14

| Regra | Resultado |
|---|---|
| R1 e R2 | falha: null sem pendência (B13) |
| R3 | ok: só o bloco do tipo existe |
| R4 | parcial: cupom do workshop e modalidades não copiados (B9); "PROVA PRESENCIAL" não está no catálogo nem em campos_so_na_ficha |
| R5 | ok: "360 horas", "XX DE XX DE 202X", "SEM DATA" e "2024" viram null e "ausente" |
| R6 | parcial: campos_so_na_ficha não lista data_fim, CH oficial e cupom do workshop, nem fonte_da_data das provas (B6 do arquiteto) |
| R7 | ok |
| R8 | falha: preço estruturado (B5); dias_ate_inicio em itens fora do recorte (B10) |
| R9 | ok: textos curtos, sem nome, sem frase ligada ao MEC, sem "últimas vagas" |
| R10 | ok |
| R11 | parcial: propostas sem pendência [SUPOSIÇÃO] (D3, D6, D11) |
| R12 | desvio registrado (D4) |
| R13 | falha leve: ordem das chaves (B12); UTF-8, LF e recuo de 2 ok |
| R14 | ok |

---

## 10. Fontes

- contexto/catalogo-de-cursos.md (26/10/2026)
- contexto/cursos/graduacao/editais-2027-1.md
- docs/execucao-2026-10-26.md
- docs/andamento-planejamento.md
- docs/pendencias-camada-1.md
- saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md
- saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md
- saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md
- saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md
- ferramentas/mapa-mental/mapa_json.py e mapa_html.py
- auditorias/conformidade-educacional.md, auditorias/10-operacoes.md e auditorias/09-analytics.md

## Fatos (com fonte)

- São 184 JSON (182 das seções 2 a 9 do catálogo e 2 da Graduação), recorte de 110 mais 2 da Graduação e ondas com 37, 54 e 21 itens (diário de 27/10; contagem das seções do catálogo conferida: 55, 36, 32, 37, 4, 10, 3 e 5).
- Metas de 15 matrículas e R$ 2.000,00 aparecem só nas Pós com recorte "planejar" e na Graduação (mapa_json.py, linhas 289 e 290; decisões 15 e 16).
- O gerador marca as 6 turmas iniciadas com campanha ativa como "nao_consta" (mapa_json.py, dicionário MIDIA; plano geral, 2.1 item 2).
- A Graduação tem pendencias_abertas fixo em 2 (mapa_json.py, linha 379); o diário registra as travas G6 a G14, MP1, MP2, MP4, MP10, U12 e U13.
- Kit da onda 2 e do lote A da onda 3: "aguardando_aprovacao" com qa "aprovado"; workshop com posts e mensagens "devolvido"; provas com "revisar_por_mudanca" e pendência da decisão 14. Os três estados batem com o diário.
- O HTML não carrega nenhum recurso externo (cmo-geral-2026-10-27.html, linhas 1 a 121; mapa_html.py).

## Suposições ([SUPOSIÇÃO])

- [SUPOSIÇÃO] A linha de dados do HTML foi gerada do mesmo mapa-dados.json da rodada dos JSON; não li a linha embutida byte a byte.
- [SUPOSIÇÃO] Os 158 JSON fora da amostra seguem as mesmas regras do gerador, porque o código não tem exceção por item além das listadas em ESPECIFICAS, MIDIA e das listas de ondas.
- [SUPOSIÇÃO] A exceção ao status "verificar" registrada em contexto/pos-graduacao.md pela decisão 18 (turma só iniciada) não muda o recorte das 6 turmas: o plano geral continua a tratá-las como pendência até o A4.

## Dados que faltam ([CONFIRMAR])

- [CONFIRMAR] A4: pausar ou manter as campanhas das 6 turmas iniciadas, e a verba gasta.
- [CONFIRMAR] U9: fim das inscrições do workshop e validade e limite do cupom SIMPNEUROMONIT.
- [CONFIRMAR] U1, U3 e U4: regras contraditórias das provas, prazo de inscrição e turma de destino.
- [CONFIRMAR] U13 e U12: meta de 15 matrículas contra a turma mínima de 30 na Graduação, e o que é "valor do curso".
- [CONFIRMAR] Se a página privada do mapa não é pública (D14), e se conhecimento/INDICE.md foi atualizado.
- [CONFIRMAR] OU14 da onda 2: não localizei a turma a que se refere nas seções lidas do plano da onda 2; o gerador não a cita.
