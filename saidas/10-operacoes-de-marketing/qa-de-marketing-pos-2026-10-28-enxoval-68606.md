# QA do enxoval da turma 68606: Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 28/10/2026 (quarta-feira)
- **Versão:** 3. A versão 1 cobria 5 arquivos; a versão 2 incluiu os anúncios Meta e o calendário (arquivos 6 e 7), respondeu às decisões C4, C6, C7 e C13 e reviu o critério do utm_campaign da mídia paga (E3). Esta versão aplica a **decisão 24 do CEO** (idade mínima de 25 anos, sem máxima, com leitura por faixa), registrada em docs/execucao-2026-10-26.md e conferida pelo qa no arquivo: a D-F passa a ser a aplicação dela, o E29 (Meta) traz o texto exato e o E36 (Google) é novo.
- **Objeto:** as 7 peças novas do enxoval da 68606, antes de entrarem na apresentação ao cliente (decisões 22 e 23).
- **Status:** rascunho de revisão. Nada é publicado, enviado ou pago. As peças não foram editadas: cada correção abaixo volta para o agente dono do arquivo.
- **Entradas lidas:**
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 2, linha 68606)
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha inteira, com cronograma e lista de docentes)
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 24 e regras para toda saída)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md (versão 4: seções 1 a 11)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md (slides 1 a 15)
  - As 7 peças: /home/user/marketing-ufape/saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-google-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/05-social-e-comunidade/posts-sociais-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/12-video-e-audio/tiktok-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/12-video-e-audio/podcast-pos-2026-10-28-ufape-cast-68606.md, /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-meta-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/04-conteudo/estrategia-de-conteudo-pos-2026-10-28-calendario-68606.md
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md, /home/user/marketing-ufape/auditorias/11-midia-paga.md, /home/user/marketing-ufape/auditorias/05-social.md e /home/user/marketing-ufape/auditorias/12-video-e-audio.md. Não existe auditorias/04-conteudo.md: o calendário foi auditado pela conformidade-educacional e pela coerência com as peças.
- **Não aberto nesta revisão:** o arquivo do gestor-de-midia-pos, a estrategia-de-midia-pos, a casa de mensagens (mensagens-pos), os ganchos do criador-de-ganchos-pos (área A6) e o copy-de-mensagens-pos-onda1. Os trechos deles foram conferidos pelo que o plano do cmo (versão 4), a apresentação de 28/10 e as próprias peças citam. As citações A6-02, A6-03, A6-07 e A6-09 batem com o slide 8 da apresentação [SUPOSIÇÃO: o original A6 não foi relido]. faculdade.ufape.com.br não foi aberto (o texto da página está na ficha).
- **Dados pessoais:** nenhum nesta revisão. Docentes só com nome e titulação da ficha.

---

## 1. Vereditos

| # | Arquivo | Veredito | Achados que bloqueiam | Volta para |
|---|---|---|---|---|
| 1 | criativos-de-anuncio-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E7, E8 | criativos-de-anuncio |
| 2 | anuncios-google-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E3, E10, E36 (E11 e E12 são correções de texto e de conta) | anuncios-google |
| 3 | posts-sociais-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E14, E16 | posts-sociais |
| 4 | tiktok-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E2, E19 | tiktok |
| 5 | podcast-pos-2026-10-28-ufape-cast-68606.md | **CORRIGIR** | E1, E2, E21, E22, E23, E24, E25, E26 | podcast |
| 6 | anuncios-meta-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E27, E29 | anuncios-meta |
| 7 | estrategia-de-conteudo-pos-2026-10-28-calendario-68606.md | **CORRIGIR** | E32, E33 | estrategia-de-conteudo |

Regra aplicada: toda peça que falha em qualquer item de auditorias/conformidade-educacional.md recebe CORRIGIR, sem exceção. O item "Página de destino entrega exatamente o que o anúncio ou a mensagem prometeu" falha hoje nas 6 peças de divulgação (E1), porque todas têm peças de depois de 07/11 que levam à página da turma, e a página ainda não escreve a regra do 3º módulo. O calendário não é peça pública, mas agenda publicações com uma porta de entrada que contradiz o E1 (E32). Mesmo com E1 resolvido, cada arquivo tem correções próprias. Meta e Google também estão com a idade fora da decisão 24 (E29 e E36).

**Para a apresentação ao cliente:** as 7 podem entrar como rascunho, com a etiqueta "em revisão do qa, não publicar" e os achados visíveis. Nenhuma segue para a aprovação humana de publicação antes de voltar corrigida e passar de novo no qa.

**Contagens do Google (pedido do orquestrador):** conferi caractere por caractere os 90 títulos, as 24 descrições, os 4 títulos e as 8 linhas de sitelink, as 7 frases de destaque e os 3 valores do snippet. Todas as contagens declaradas estão certas e nenhum texto passa do limite (30, 90, 25, 35 e 25). O único erro está no resumo da seção 5.8 (E11). **Meta:** conferi a frase da regra (201 caracteres, certa), os títulos da fase 2 e o ponto de corte do "ver mais" nos textos curtos da fase 2: em nenhum deles a data do 3º módulo aparece antes do corte.

---

## 2. Decisões

### D-A. Episódio 3 do podcast sem chamada de turma (com a opção A do calendário, C4)

**Decisão: o episódio 3 sai em 22/12/2026 só no YouTube e no Spotify, sem chamada de turma, e nenhuma peça derivada dele é publicada de 21/12 a 03/01.** Aprovo a opção A proposta pelo orquestrador para o C4. Motivos: (1) o plano da apresentação (slides 14 e 15) já previa o ep. 3 sem chamada; (2) 21/12 a 03/01 é janela sem campanha (cmo-pos, regra 5) e o kit de posts não publica nela (posts-sociais, regra 2); (3) o tema (luto e burnout) é sensível, e chamada de venda colada nele soa como aproveitamento; (4) a opção B tiraria um episódio com chamada antes da pausa. Complemento do qa: as peças derivadas do ep. 3 não vão para 05 a 07/01 (colidem com o ep. 4, C7); vão para depois de 22/01, quando a turma já saiu das chamadas e o feed da Pós está livre (datas no E22). Nenhuma peça do ep. 3 leva [CHAMADA-TURMA], link da página da 68606 ou a data do 3º módulo; o link usa `pos_conteudo_202612` [CONFIRMAR com o arquiteto-de-fluxos] (cmo-pos, regra 11).

### D-B. Mês do utm_campaign (202610 contra o mês da publicação)

**Decisão: `utm_campaign=pos_68606_202610` em todo toque orgânico e de CRM da turma, em qualquer mês de publicação.** Fonte: cmo-pos, regra 11 e OA9, ajuste N2 da versão 4 (mês do primeiro envio, igual em todos os toques da turma, com o toque no utm_content). O primeiro envio da 68606 foi o e-mail de 28/10 (OA9). O D12 do plano geral ("mês do primeiro envio ou da publicação") é a regra geral; a regra 11 do plano da turma é a aplicação dela e prevalece. A exceção `pos_conteudo_<AAAAMM>` vale só para peça sem chamada de turma (ep. 3). Já está certo nos posts-sociais; muda no tiktok e no podcast (E2) e no calendário (E34). Na mídia paga, ver E3.

### D-C. "Matrícula" ou "inscrição" para os R$ 250,00

**Decisão: nas peças, "matrícula de R$ 250,00".** Motivos: (1) dado de curso só vem do catálogo, e o catálogo (seção 2) e a página dizem "matrícula R$ 250,00"; (2) a decisão 23 diz "R$ 250,00, como no site" e manda citar "a condição completa do catálogo"; (3) a peça precisa casar com a página de destino; (4) a palavra casa com a frase da regra ("A Ufape aceita matrícula até o 3º módulo"): pagar a matrícula é o ato de entrar. No funil interno segue "inscrição paga", medida à parte da 1ª mensalidade (decisões 16 e 23). Se a pessoa do marketing preferir "inscrição", a troca vale para todas as peças de uma vez e o catálogo é atualizado antes. Correções: E8 (criativos) e E31 (Meta, só o marcador). Posts, tiktok, Google e Meta já usam "matrícula" nas peças.

### D-D. Dados do cronograma marcados [CONFIRMAR NO CATÁLOGO]

**Decisão: cronograma, módulos, local, coordenação e lista de docentes da ficha valem como catálogo.** O próprio catálogo diz que os detalhes de cada curso (descrição, público, cronograma, coordenação, condições) estão na ficha em contexto/cursos/ (cabeçalho). Os marcadores sobre 24 módulos, datas dos módulos, aulas práticas, endoscopia, grupo de discussão de casos e endereço saem (E5, E34). Conferi a linha 68606 do catálogo: nome, São Paulo, semipresencial, 07/11/2026, turma IX, 500 h, "30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00", status "aberto". Bate com as 7 peças.

### D-E. Grafia da titulação dos docentes

**Decisão [SUPOSIÇÃO a validar com a Ufape]:** só a caixa pode ser ajustada (DR. para Dr., DRA. para Dra., MSC. para MSc.); nome e titulação nunca mudam, e o ajuste vale igual em todas as peças e na apresentação. Motivo: nos anúncios a caixa alta conta como "caixa alta excessiva". Correção: E6.

### D-F. Idade na mídia paga (decisão 24 do CEO)

**Decisão registrada (decisão 24, CEO, 28/10/2026, aplicada até nova ordem): idade mínima de 25 anos, sem idade máxima, com leitura semanal por faixa (25 a 34, 35 a 44, 45 ou mais).** Ela substitui o 18+ sem corte do anuncios-meta e da estratégia de mídia e a faixa de 22 a 35 do deck da The Growth Hub. O qa aplica como correção em todo lugar onde a idade aparece:

| Arquivo | Onde | Achado |
|---|---|---|
| anuncios-meta | resumo item 8, tabela 4.1 (linha "Idade"), tabela 4.2 (linha "Idade e gênero"), seção 4.4, utm_term da seção 8, AM7, checklist da seção 12, seção 13 (linha 3), seção 14.1 (linha de segmentação), "Dados que faltam" | E29 |
| anuncios-google | seção 9.7 (linha "Público"), checklist item 15, seção 12 (linha de públicos) | E36 |
| criativos, posts, tiktok, podcast, calendário | idade não aparece | sem achado |
| apresentação do cmo (fora desta revisão) | slide 4 ("idade mínima de 20 anos, sugestão de 22 a 35" e a recomendação de manter 22 a 35) | nota ao cmo: trocar pela decisão 24 antes de ir ao cliente |

**Quando aplicar:** no remarketing da Meta desde a criação do conjunto (07/11); nos conjuntos de frio da Meta, na operação única de 03/11, junto com a troca de criativo [SUPOSIÇÃO: conta como uma mudança só na regra R6, como o próprio anuncios-meta já supõe para as exclusões; o gestor confirma]; no Google, na montagem de 07/11.

**Registro de risco para a aprovação humana (não bloqueia, porque é decisão do CEO):** (1) o corte em 25 anos tira do alcance o recém-formado de 22 a 24 anos, que o contexto da linha lista como persona secundária ("Recém-formado que quer sair da faculdade já especializado", [SUPOSIÇÃO]) e que a persona principal começa em 24 anos; (2) no remarketing, quem visitou a página e tem menos de 25 deixa de ver o anúncio, mas segue alcançado pela base (WhatsApp e e-mail com opt-in) e pelo orgânico; (3) a auditoria pede segmentação sem exclusão por atributo sensível: a idade mínima fica justificada pelo perfil do produto (formado) e registrada como decisão; nenhuma outra exclusão por atributo pessoal entra. Nenhum texto de anúncio menciona idade.

### D-G. Decisões do calendário propostas pelo orquestrador

| Conflito | Proposta | Resposta do qa | Condição |
|---|---|---|---|
| C4 | Opção A: ep. 3 só no YouTube e no Spotify, sem peças derivadas no fim de ano | **Aprovo** | Peças derivadas do ep. 3 só depois de 22/01, sem chamada de turma (D-A, E22, E35) |
| C6 | Card 4:5 do ep. 1 vira Story | **Aprovo** | O Story leva a [CHAMADA-TURMA] inteira se tiver link para a turma; uso como anúncio de remarketing só pelo AP-4, trocando uma peça (nunca somando) |
| C7 | Corte 2 de cada episódio vira Story | **Aprovo** | Vale para as semanas em que o feed da Pós passaria de 3 itens ou de 1 por dia; Story com link da turma leva a frase inteira; P2 e P4 nunca saem do feed; o posts-sociais confere slot a slot |
| C13 | Fase 1 termina em 06/11, 23h59, programada na sexta | **Aprovo** | Vale para Meta e Google; data de término e início programados na sexta (a Meta já prevê envio da fase 2 para revisão em 05/11); quem executa e quem confere na manhã de sábado 07/11 nomeados antes de 05/11 [CONFIRMAR]; se a conta não permitir programar, a troca manual é na sexta 06/11 à noite, nunca depois de 07/11, 00:00 |

### D-H. Transparência da turma mínima nos textos curtos da Meta (pedido do anuncios-meta, seção 14.1)

**Decisão:** na fase 1, todo texto que for ao ar leva "A turma pode não ser formada se não atingir o número mínimo de alunos." Hoje só os T1 sobem, e eles já têm a frase. Os textos curtos em espera (F1-E T2, T3 e T5; F1-C T2, T3 e T4; F1-V T2, T3 e T4) só sobem com a frase acrescentada no fim (E30). Na fase 2 a frase não é obrigatória: a turma já começou, e o anúncio não afirma que ela está confirmada.

---

## 3. Achados

Formato: arquivo, onde, trecho atual, correção exata. "Bloqueia" indica item de conformidade, de promessa ou contrário a decisão registrada; "ajuste" indica correção que precisa entrar, sem item próprio.

### Transversais

**E1. Página de destino não entrega a regra do 3º módulo (bloqueia, as 6 peças de divulgação)**
- Onde: toda peça de depois de 07/11 com link ou chamada para a página da turma: F2-A, F2-B e V-P (criativos e Meta); os 6 RSAs, sitelinks e frases de destaque da fase 2 (Google); P3 a P6 (posts); versão B (tiktok); ep. 1, 2, 4 e 5 e seus pacotes (podcast).
- Trecho atual: a ficha (texto da página) não traz a regra "matrícula até o 3º módulo", traz a frase ligada ao MEC e "Turma mínima de 20 alunos". Os próprios agentes marcaram "pendente externo" (A7, A12 e A13 do OA10; AM9 na Meta).
- Correção exata: nenhuma dessas peças sobe ou é publicada antes de (1) a página da 68606 publicar a frase "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram." (A13), conferida pelo qa na ficha atualizada; e (2) a troca da frase ligada ao MEC (A7) e da turma mínima (A12), ou o registro da decisão da regulação sobre publicar antes dela (cmo-pos, regra 9). Cada arquivo acrescenta essa condição na sua lista de aprovações. As peças de antes de 07/11 (F1-E, F1-C, F1-V, P1, P2, versão A) dependem só do item (2).

**E2. utm_campaign fora da decisão D-B (bloqueia rastreio por turma; tiktok e podcast)**
- tiktok, seção 2.2: `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`.
- tiktok, seção 6, "Regras da versão B": `utm_campaign=pos_68606_202611 (mesmo mês do primeiro toque)`. Trocar por `utm_campaign=pos_68606_202610 (mês do primeiro envio da turma, regra 11 do cmo-pos)`.
- tiktok, lista [SUPOSIÇÃO]: "mês 202611 como mês de publicação". Trocar por "mês 202610, do primeiro envio da turma (decisão D-B do qa de 28/10/2026)".
- podcast, seção 0, [LINK-TURMA]: `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`, e "o `utm_campaign` e o `utm_content` mudam por episódio" por "só o `utm_content` muda por episódio".
- podcast, seção 0, linha "Mês do `utm_campaign` segue o mês de publicação (...)": trocar por "O `utm_campaign` é `pos_68606_202610` em todo episódio com chamada da turma (regra 11 do cmo-pos). Episódio sem chamada de turma usa `pos_conteudo_<AAAAMM>` [CONFIRMAR com o arquiteto-de-fluxos]."
- podcast, seções 2.3 e 2.4 (links do ep. 1): `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`.
- podcast, ep. 2: `utm_campaign=pos_68606_202612`; ep. 4 e ep. 5: `utm_campaign=pos_68606_202701`. Trocar os três por `utm_campaign=pos_68606_202610`.

**E3. Critério do utm_campaign da mídia paga diferente entre Meta e Google (bloqueia rastreio; Google)**
- Trechos atuais: Meta, seção 8: "utm_campaign: nome da campanha, exatamente como no gerenciador, em minúsculas e sem acento (...) registrar na tabela de correspondência". Criativos, seção 1.4: "utm_campaign igual ao da campanha existente do 68606". Google, seção 3: "O `utm_campaign` dos anúncios novos usa o nome D12 de referência acima, para a leitura por turma fechar."
- Decisão: vale o critério da Meta e dos criativos, que é o literal do D11 e D12 ("utm_campaign igual ao nome da campanha"): nome real da campanha no ar, em minúsculas e sem acento, e a leitura por turma fecha pela tabela de correspondência (ação A4). Um utm_campaign diferente do nome real quebraria a conferência entre gerenciador e CRM.
- Correção exata no Google, seção 3, terceiro parágrafo: trocar "O `utm_campaign` dos anúncios novos usa o nome D12 de referência acima, para a leitura por turma fechar." por "O `utm_campaign` dos anúncios novos é o nome real da campanha no ar, em minúsculas e sem acento [DADO NÃO FORNECIDO, exportação D6]; a leitura por turma fecha pela tabela de correspondência (ação A4), como na Meta." Na seção 8.2 e no modelo de URL, trocar `pos_68606-gastro_google_lead_busca_202610` por `NOME_DA_CAMPANHA_ATUAL` (a preencher na exportação D6). Criativos e Meta não mudam.

**E4. Termo do valor de R$ 250,00 (decisão D-C)**
- Aplicação nas peças: E8 (criativos) e E31 (Meta). Nos trechos internos (criativos 1.1 e 7, Google 8.3), basta registrar "matrícula de R$ 250,00 (decisão D-C do qa de 28/10/2026)".

**E5. Marcadores [CONFIRMAR NO CATÁLOGO] sobre dados da ficha (ajuste, Google e podcast; decisão D-D)**
- Google, título 15 do RSA area1: "Prática em endoscopia [CONFIRMAR NO CATÁLOGO]". Trocar por "Prática em endoscopia" (21). O módulo 13 presencial "Endoscopia" e o diferencial "Aulas práticas de anatomia, Cirurgia e endoscopia" estão na ficha.
- Google, seção 5.1 (dois últimos itens), seção 4.4 (linha K6.6), checklist item 7, seção 12 (linha "Dado que só está na ficha") e "Dados que faltam": tirar o marcador e escrever "ficha da 68606, que o catálogo indica como fonte do cronograma".
- podcast, lista [CONFIRMAR], linha "Confirmar no catálogo (...)": apagar. Conferido pelo qa em 28/10/2026 (D-D).

**E6. Caixa da titulação dos docentes (ajuste, podcast e apresentação; decisão D-E)**
- podcast, cabeçalho: "Docentes só com nome e titulação como estão na ficha (maiúsculas normalizadas)". Acrescentar: "Só a caixa muda (DR. para Dr.); nome e titulação como na ficha. Mesmo ajuste na apresentação."
- Nota ao cmo (sem editar o arquivo dele): o slide 14 escreve "DR. Fabrizio Grandi" e o slide 11 "DRA. VIVIANE DE MARCO" e "DRA. Maria Anete Lallo"; aplicar o mesmo ajuste de caixa na peça que for ao cliente.

### Arquivo 1: criativos-de-anuncio-pos-2026-10-28-68606.md

**E7. F2-A e F2-B marcam o módulo 2 como "já aconteceu" desde 07/11 (bloqueia: informação falsa até 20/12)**
- Onde: seção 4.2, briefing visual ("agora com os módulos 1 e 2 em tom de 'já aconteceu'"); seção 4.3, roteiro 0:03 a 0:07 ("Linha do tempo de 24 quadrados com os módulos 1 e 2 em tom de 'já aconteceu'").
- Problema: a fase 2 roda de 07/11/2026 a 22/01/2027 e o módulo 2 é em 19 e 20/12/2026 (ficha). De 07/11 a 20/12 a arte mostraria como passado um módulo que ainda não aconteceu.
- Correção exata, nas duas seções: trocar o trecho por "a linha do tempo de 24 quadrados fica neutra, sem nenhum módulo marcado como 'já aconteceu', com os 3 presenciais (6, 13 e 21) em cor de destaque". Uma só arte vale de 07/11 a 22/01. O anuncios-meta usa as mesmas artes: a correção vale para F2-A e F2-B lá também.

**E8. Variante V-P: termo e condição incompleta (bloqueia preço)**
- Onde: seção 4.4, parágrafo a acrescentar.
- Trecho atual: "Condições: 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; inscrição de R$ 250,00, à vista (Pix ou boleto) ou em 1x no cartão."
- Correção exata do texto: "Condições: 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula de R$ 250,00, à vista (Pix ou boleto) ou 1x de R$ 250,00 no cartão." (é o texto que o anuncios-meta já usa na seção 7.6).
- Condição de uso: a V-P segue bloqueada até a resposta da OU8 (como paga a 1ª mensalidade quem entra depois do início). A ficha manda pagar a 1ª mensalidade até 30 dias antes do início; para quem entra depois de 07/11 isso é impossível, e a peça não pode omitir nem inventar a regra nova (auditoria, "condições completas"). Com a OU8 respondida, a frase dela entra no mesmo parágrafo, logo depois da matrícula, e a V-P volta ao qa. Atualizar a seção 7, itens 2 e 3, e a matriz 5.1 (linhas F2-A-vp e F2-B-vp) com "bloqueado até OU8 e aprovação de preço".

**E9. Título do cartão 4 do carrossel passa do limite que o próprio arquivo fixou (ajuste)**
- Onde: seção 3.2, "Título por cartão (... até cerca de 32 caracteres)".
- Trecho atual: "4. Online, de 22/05/2027 a 20/02/2028" (o texto do campo tem 34 caracteres).
- Correção exata: "4. Online, 05/2027 a 02/2028" (o texto do campo tem 25 caracteres). Mesma troca na Meta (E28).

### Arquivo 2: anuncios-google-pos-2026-10-28-68606.md

**E10. Textos de "entrada" sem a frase completa da regra (bloqueia)**
- Regra: depois do início, toda peça que fala de entrada diz a regra inteira (cmo-pos, regra 6); a frase não cabe em 90 caracteres. Decisão do qa: o plano B (data de início mais "veja as condições na página") só é aceito se nenhum texto do RSA falar de entrada; o título fixado "Turma iniciada em 07/11" fica, porque é fato passado e evita a leitura de que a turma ainda vai começar; a subida segue presa ao P1 (E1). Trocas exatas:
- RSA marca1, título 13: "Condições de entrada na página" (30). Trocar por "Fale com o time da turma" (24).
- RSA custo1, título 6: "Condições de entrada na página" (30). Trocar por "Fale com o time da turma" (24).
- RSA marca2, descrição 2: "Turma IX iniciada em 07/11/2026. Veja as condições de entrada na página." (72). Trocar por "Turma IX iniciada em 07/11/2026. Fale com o time da turma." (58).
- RSA custo1, descrição 2: "Turma IX iniciada em 07/11/2026. Veja parcelas e condições de entrada na página." (80). Trocar por "Turma IX iniciada em 07/11/2026. Veja parcelas na página e fale com o time." (75).
- Sitelink 2, linha 2: "Veja as condições de entrada (28)". Trocar por "Fale com o time da turma (24)".
- Seção 2, linha 07/11: "Sai tudo que cita 'começa em', 'início em' ou 'inscrições até' sem a regra". Acrescentar: "e todo texto com 'entrada', 'entrar', 'matricule-se' ou 'inscreva-se'".

**E11. Resumo dos limites da seção 5.8 (ajuste)**
- Trecho atual: "Nenhum título passa de 30 (maior: 30, em quatro títulos)".
- Correção exata: "Nenhum título passa de 30 (maior: 30, em cinco títulos: marca1 13, area1 3, area2 15, custo1 5 e custo1 6)". Depois do E10, os títulos de 30 caracteres passam a ser três (area1 3, area2 15 e custo1 5).

**E12. Conta de controle da seção 9.4 ignora que o orçamento é da campanha (ajuste)**
- Problema: na fase 2 ficam ativos `__marca` e `__area`, que dividem um só orçamento. Com 2 RSAs por grupo são 4 anúncios, e a regra da própria tabela (maior CPL aguentado = 2 x semanal / número de anúncios) pede semanal de pelo menos R$ 36,00, não R$ 18,00.
- Correção exata da tabela:

| Situação | Condição | Resultado na fase 2 |
|---|---|---|
| 2 RSAs por grupo (4 anúncios) | semanal do Google maior ou igual a R$ 36,00 (diária maior ou igual a R$ 5,14) | Vale para G até R$ 1.177,14 |
| 1 RSA por grupo (2 anúncios) | semanal maior ou igual a R$ 18,00 (diária maior ou igual a R$ 2,57) | Vale para G até R$ 1.588,57 |
| Só `__marca`, 1 RSA | semanal maior ou igual a R$ 9,00 (diária maior ou igual a R$ 1,29) | Vale para G até R$ 1.794,29; acima disso, pedido de pausa ao gestor [SUPOSIÇÃO] |

- Conta: diária do Google na fase 2 = 0,50 x (2.000 menos G) / 80; R$ 36,00 / 7 = R$ 5,14 por dia, logo 2.000 menos G maior ou igual a R$ 822,86. "Com G = 0, a semanal do Google na fase 2 é R$ 87,50: passa com folga" continua certo.

**E36. Idade fora da decisão 24 (bloqueia: contraria decisão registrada)**
- Seção 9.7, linha "Público". Trecho atual: "| Público | 18 anos ou mais; listas de remarketing só como observação, nunca como restrição; nenhuma lista de contatos sem base legal [CONFIRMAR] | Estratégia, 4.1 |". Correção exata: "| Público | 25 anos ou mais, sem idade máxima (decisão 24): excluir a faixa de 18 a 24 anos e manter 25 a 34, 35 a 44, 45 a 54, 55 a 64, 65 ou mais e "desconhecida" [SUPOSIÇÃO: "desconhecida" fica, porque não indica menos de 25 anos; o gestor confirma]. Leitura semanal por faixa: 25 a 34, 35 a 44 e 45 ou mais. Listas de remarketing só como observação, nunca como restrição; nenhuma lista de contatos sem base legal [CONFIRMAR] | Decisão 24 (docs/execucao-2026-10-26.md) |".
- Checklist, item 15. Trecho atual: "Conferir rede (só Pesquisa), local (estado de São Paulo), idioma, 18 anos ou mais e a trava de gasto." Correção exata: "Conferir rede (só Pesquisa), local (estado de São Paulo), idioma, idade de 25 anos ou mais com a faixa de 18 a 24 excluída (decisão 24) e a trava de gasto."
- Seção 12, linha "Públicos de 18 anos ou mais, sem segmentação sensível, sem lista de contatos sem base legal". Correção exata: "| Público de 25 anos ou mais, sem idade máxima (decisão 24); sem outra segmentação sensível; sem lista de contatos sem base legal | Atendido no desenho | Leitura semanal por faixa: 25 a 34, 35 a 44 e 45 ou mais |".
- Quando: na montagem de 07/11 (seção 11, "Montagem em 07/11").

### Arquivo 3: posts-sociais-pos-2026-10-28-68606.md

**E13. Gancho do P3 não é cumprido pelo conteúdo (ajuste, auditoria 05)**
- Trecho atual: gancho "Quando um caso gastrointestinal pede uma segunda opinião?"; as telas 2 e 3 não respondem à pergunta (de propósito, para não pôr conduta na voz de ninguém).
- Correção exata: usar o gancho alternativo 1 como linha 1 e como texto grande da tela 1: "Discussão de casos entre alunos e coordenação: o que a página da Pós-graduação em Gastroenterologia Veterinária prevê." A legenda de apoio começa com a mesma frase. A pergunta da segunda opinião fica para o ep. 2 do podcast, onde o convidado responde.

**E14. P2 (feed) continua no perfil depois de 07/11 com chamada de entrada sem a regra (bloqueia)**
- Trecho atual, card 6: "A turma IX começa em 07/11/2026, em São Paulo." e "Fale com o time para saber como entrar na turma."; legenda com as mesmas linhas.
- Problema: post de feed não sai do ar sozinho; a partir de 07/11 o card diria que a turma "começa" e chamaria para entrar sem a frase completa. Texto de arte não se edita depois de publicado.
- Correção exata do card 6: "Turma IX, São Paulo." / "24 módulos, 500 horas, semipresencial." / "Cronograma completo e docentes na página da turma." / "Link na bio." (sem data e sem chamada de entrada na arte). A data de início e a chamada ficam só na legenda, e em 07/11 a legenda é editada para o texto de contingência da seção 7. Acrescentar na seção 7: "Em 07/11, editar a legenda do P2 no Instagram e no Facebook; se o P1 estiver nos Destaques, tirar dos Destaques em 07/11."

**E15. Jargão interno no P4 (ajuste)**
- Trecho atual, card 3: "Neste módulo, a ficha não lista cirurgia."
- Correção exata: "Neste módulo, o cronograma não lista cirurgia."

**E16. P5 com preço sem a condição da 1ª mensalidade (bloqueia preço)**
- Trecho atual, tela 2: "30x de R$ 1.180,00 no cartão ou boleto." / "Total: R$ 35.400,00."; tela 3: "R$ 250,00, à vista (Pix ou boleto) ou 1x de R$ 250,00 no cartão."; legenda com os mesmos dados.
- Problema: o P5 sai em 15/12, depois do início. A página manda pagar a 1ª mensalidade até 30 dias antes do início, o que é impossível para quem entra agora, e a regra para quem entra depois (OU8) não existe. "A conta inteira" fica incompleta.
- Correção exata, se a OU8 for respondida até 14/12: tela 2 vira "30x de R$ 1.180,00." / "R$ 35.400,00 no cartão ou boleto." (a forma do catálogo); tela 3 ganha a linha "1ª mensalidade: [texto da resposta da OU8]"; a legenda segue a mesma ordem; o P5 volta ao qa.
- Correção exata, se a OU8 não for respondida até 14/12 (o kit não perde o post): gancho e tela 1 "Quanto custa a Pós-graduação em Gastroenterologia Veterinária? Onde ver a conta inteira."; telas 2 e 3 viram uma só: "Parcelas, total e matrícula estão na página da turma." / "500 horas, 24 módulos, semipresencial, São Paulo."; tela 4 sem mudança; nenhum valor na peça.

**E17. Métricas do kit não aparecem (ajuste, auditoria 05)**
- Correção exata: acrescentar no fim da seção 0.1 o item 10: "Métricas: cliques no link com UTM por peça, respostas e mensagens recebidas, conversas com o time de vendas que citam o post (só contagem), salvamentos. Alcance e curtidas só como contexto."

### Arquivo 4: tiktok-pos-2026-10-28-68606.md

**E18. Captura da página oficial no vídeo (ajuste, coerência com os criativos)**
- Trecho atual, seção 4, imagem 8: "Recorte da tela do cronograma na página da turma | Bloco 5 | Captura de tela"; bloco 5: "o recorte da página mostra só o cronograma".
- Problema: o pacote de criativos proíbe captura da página oficial, porque ela traz a frase ligada ao MEC.
- Correção exata: apagar a imagem 8 e, no bloco 5, trocar "o recorte da página mostra só o cronograma (ver nota de gravação 3)" por "só o gráfico da imagem 7, com o texto da ficha". Nota de gravação 3: "Se a Ufape alterar o cronograma, refazer o gráfico."

**E19. Número de WhatsApp de vendas sem a conferência (bloqueia o item de destino)**
- Trecho atual, seção 2.2: "WhatsApp de vendas São Paulo: (11) 91366-9290 (contexto/ufape-geral.md)", para botão ou comentário fixado.
- Problema: o contexto registra instabilidade do WhatsApp em 22/10/2026 e não informa o horário de vendas (auditoria 11, "Destino de WhatsApp é número oficial com atendimento informado").
- Correção exata: acrescentar depois do número: "[CONFIRMAR antes de publicar que o número voltou a funcionar e o horário de atendimento de vendas]". Sem a confirmação, o comentário fixado leva só à página da turma.

### Arquivo 5: podcast-pos-2026-10-28-ufape-cast-68606.md

**E20. Data do 3º módulo falada fora da frase no ep. 5 (ajuste preventivo)**
- Onde: ep. 5, "Tema da ficha: módulo 3 (...), que acontece em 23 e 24/01/2027" e pergunta 5, num episódio que sai a 4 dias do 3º módulo.
- Correção exata: acrescentar nos cuidados do ep. 5: "Ninguém fala a data do módulo 3 nem 'neste fim de semana' fora da [CHAMADA-TURMA]; na pauta, a pergunta 5 cita só 'o módulo 3 da Pós-graduação em Gastroenterologia Veterinária', sem data."

**E21. Regra de entrada pedida à coordenadora (bloqueia: frase institucional na voz da docente)**
- Trecho atual, ep. 1, bloco 5, pergunta 4: "Que orientação vocês dão a quem quer entrar depois do início da turma? (a resposta é a [CHAMADA-TURMA]; o que a coordenação não souber, o apresentador diz 'o time confirma', sem prometer reposição)".
- Problema: o arquivo escreve a resposta da docente e abre espaço para promessa de reposição na voz dela (OU3 aberta).
- Correção exata: apagar a pergunta 4 do bloco 5. A regra aparece só como FALA INSTITUCIONAL do apresentador no bloco 6, como já está. Acrescentar em "Não perguntar nem afirmar": "regra de entrada depois do início (é fala do apresentador)".

**E22. Episódio 3: aplicar a decisão D-A (bloqueia o pacote do ep. 3)**
- Trecho atual: "Chamada: sem chamada de turma (...). Link da Ufape com `utm_campaign=pos_conteudo_202612` [CONFIRMAR exceção de UTM]. Se a Ufape preferir manter a chamada da turma, usa-se a [CHAMADA-TURMA] completa. **Decisão da Ufape [CONFIRMAR].**"
- Correção exata: "Chamada: sem chamada de turma (decisão D-A do qa de 28/10/2026). O episódio sai em 22/12 só no YouTube e no Spotify. Chamada única: 'Siga o UFAPE Cast e envie sua pergunta para o próximo episódio.' Link: canal do UFAPE Cast; se o link for para o site, https://faculdade.ufape.com.br/?utm_source=<youtube|spotify|instagram>&utm_medium=organic_social&utm_campaign=pos_conteudo_202612&utm_content=ufapecast_ep03 [CONFIRMAR exceção com o arquiteto-de-fluxos]. Nenhuma peça do ep. 3 leva [CHAMADA-TURMA], link da 68606 ou data do 3º módulo." Apagar o item 10 da seção 6.
- Pergunta 5 do ep. 3: "Por que esse tema aparece num curso técnico, como o módulo 24 da ficha da pós?". Trocar por "Por que esse tema aparece num curso técnico, como no módulo 24 da Pós-graduação em Gastroenterologia Veterinária?".
- Calendário (seção 4): tirar o corte 1, o Story de estreia (22/12) e o card do convidado (23/12) do ep. 3 e acrescentar, sem chamada de turma: "qua 27/01: corte 1 e Story 1 do ep. 3"; "qui 28/01: Story 2 do ep. 3 (link para o episódio)"; "qua 03/02: card do convidado do ep. 3"; "qui 04/02: corte 2 do ep. 3"; "qua 17/02: corte 3 do ep. 3" [SUPOSIÇÃO de datas: depois da pausa de 22/01, fora da semana de Carnaval e sem outro post de feed da Pós no mesmo dia; o posts-sociais confere com as turmas de março].

**E23. Calendário passa do teto de feed da Pós (bloqueia a grade)**
- Trechos atuais: "ter 24/11: Ep. 1 no ar; corte 1; Story de estreia; card 4:5" e, na mesma semana, card do convidado (25/11) e corte 2 (26/11).
- Problema: corte (Reel) e card 4:5 no mesmo dia somam 2 posts de feed da Pós (teto de 1 por linha por dia, D5); a semana de 23 a 29/11 fica com 4 posts de feed da Pós, contra 3 slots semanais (cmo-pos, seção 4). O mesmo se repete nas semanas dos ep. 2, 4 e 5.
- Correção exata (com as decisões C6 e C7, D-G): (1) o card 4:5 de todo episódio vira Story, ou anúncio de remarketing só pelo AP-4, nunca feed; (2) o corte 2 de cada episódio vira Story; (3) acrescentar na seção 4: "No máximo 1 post de feed da Pós por dia e 3 por semana, somando o kit da turma, os posts de docente e o podcast; Story com link da turma leva a [CHAMADA-TURMA] inteira; a conferência slot a slot é do posts-sociais antes da aprovação"; (4) o P4 do posts-sociais fica em 03/12, sem a opção de 01/12; (5) trocar a ordem das linhas "ter 26/01" e "seg 25/01".

**E24. Pergunta da comunidade: dados pessoais e formulário (bloqueia o bloco 4 antes da abertura)**
- Trecho atual: "caixa de perguntas nos Stories e formulário curto da Ufape, abertos de 09/11 a 17/11 [SUPOSIÇÃO de prazo] (...) [CONFIRMAR formulário com política de privacidade (pendência p04)]".
- Correção exata: acrescentar "A caixa de perguntas do Instagram mostra o perfil de quem enviou: o perfil nunca vai para arquivo de trabalho, planilha ou chat da squad; a triagem copia só o texto da pergunta. O formulário só abre com finalidade escrita e link da política de privacidade. Sem isso até a véspera da abertura, o ep. 1 usa a pergunta de reserva e o bloco 4 não abre formulário." (A abertura pode ir para 10/11, como propõe o C10 do calendário.)

**E25. Egresso no ep. 1 é depoimento (bloqueia o ep. 1 com egresso)**
- Trecho atual: "Egresso de pós da Ufape: [CONFIRMAR nome, de qual pós, e autorização de imagem, voz e citação]".
- Correção exata: acrescentar "Relato de egresso é depoimento: além do termo assinado de imagem, voz e citação, o episódio com egresso passa pela aprovação de 'Peças com certificação, ato regulatório ou depoimento' de contexto/ufape-geral.md (responsável e regulação, hoje [CONFIRMAR]). Sem as duas coisas, o ep. 1 sai só com a coordenação, e a descrição, os títulos, o Story e o card tiram toda menção ao egresso."

**E26. Capacidade de produção não definida (bloqueia a aprovação da série, auditoria 12)**
- Trecho atual: seção 6, itens 1 e 2 (nome, perfis, quem apresenta, grava, edita e publica, horas, custo) em aberto.
- Correção exata: acrescentar na lista de aprovações: "A série só vai à aprovação de produção (AP-2) com equipe, horas por semana e custo informados pela Ufape. Até lá, o pacote é plano, não calendário."

### Arquivo 6: anuncios-meta-pos-2026-10-28-68606.md

**E27. F2-B T5 fica falso depois de 20/12 (bloqueia)**
- Onde: seção 7.5, T5 ("O que vem depois do início da turma?").
- Trecho atual: "Pelo cronograma atual: o módulo 2 é online, em 19 e 20/12/2026, e os 3 módulos presenciais são em 17 e 18/04/2027, 27 e 28/11/2027 e julho de 2028."
- Problema: o conjunto de remarketing roda até 22/01/2027. De 21/12 em diante o texto diria que o módulo 2 "vem depois", quando já aconteceu.
- Correção exata: trocar o trecho por "Pelo cronograma atual, os 3 módulos presenciais são em 17 e 18/04/2027, 27 e 28/11/2027 e julho de 2028." Assim o T5 vale de 07/11 a 22/01.

**E28. Título do cartão 4 do carrossel (ajuste, igual ao E9)**
- Onde: seção 7.2, "Arte": "4. Online, de 22/05/2027 a 20/02/2028".
- Correção exata: "4. Online, 05/2027 a 02/2028".

**E29. Idade fora da decisão 24 (bloqueia: contraria decisão registrada)**
- **Seção 4.4.** Trocar o título e todo o texto da seção (os dois parágrafos, de "O roteiro do cmo (slide 4) recomenda..." até "...vale o que já está configurado [DADO NÃO FORNECIDO].") por:
  > ### 4.4 Idade (decisão 24 do CEO, 28/10/2026)
  >
  > Idade mínima de 25 anos, sem idade máxima, em todos os conjuntos da 68606: no conjunto de remarketing desde a criação (07/11) e nos conjuntos de frio da fase 1 na operação única de 03/11, junto com a troca de criativo [SUPOSIÇÃO: conta como uma mudança só na regra R6; o gestor confirma]. A idade entra no relatório semanal como quebra de leitura em três faixas: 25 a 34, 35 a 44 e 45 ou mais. A decisão 24 substitui o 18+ sem corte da estratégia de mídia (4.1) e a faixa de 22 a 35 do deck da The Growth Hub. Referência citada na decisão: veterinários atuantes concentrados de 30 a 49 anos (Demografia da Medicina Veterinária 2022). Mudar a faixa só com nova decisão humana.
- **Tabela 4.1, linha "Idade".** Trecho atual: "| Idade | 18 anos ou mais, sem corte superior (4.4) |". Correção exata: "| Idade | 25 anos ou mais, sem idade máxima (decisão 24, 4.4); aplicada na operação de 03/11, junto com a troca de criativo; leitura semanal por faixa: 25 a 34, 35 a 44 e 45 ou mais |".
- **Tabela 4.2, linha "Idade e gênero".** Trecho atual: "| Idade e gênero | 18 anos ou mais, todos os gêneros, sem exclusão |". Correção exata: "| Idade e gênero | 25 anos ou mais, sem idade máxima (decisão 24); todos os gêneros, sem exclusão |".
- **Seção 0, item 8.** Trecho atual: "**Quatro decisões humanas pedem atenção antes de subir:** faixa de idade (18+ contra a sugestão de 22 a 35, seção 4.4), exclusão de quem pagou (...)". Correção exata: "**Três decisões humanas pedem atenção antes de subir:** exclusão de quem pagou e de alunos por lista (base legal, seção 4.3), subida com a página de destino ainda pendente (seção 11, AM9) e a variante com preço (AM8). A idade já está decidida: 25 anos ou mais, sem máxima (decisão 24, seção 4.4)."
- **Seção 8, utm_term.** Trecho atual: "`vetform18` na fase 1". Correção exata: "`vetform25` na fase 1", e trocar `utm_term=vetform18` por `utm_term=vetform25` nas URLs de F1-E, F1-C e F1-V.
- **Seção 11, AM7.** Trocar a linha inteira por: "| AM7 | Aplicar a idade mínima de 25 anos, sem idade máxima, nos conjuntos de frio (na operação de 03/11) e no remarketing (desde 07/11), com leitura semanal por faixa (25 a 34, 35 a 44, 45 ou mais) | Decisão 24 do CEO (28/10/2026) | Sem verba | Gasto só em quem tem o perfil de pós (formado), pela decisão do CEO | Voltar à idade da exportação anterior, só com nova decisão humana |".
- **Seção 12, checklist "Públicos".** Trecho atual: "Idade 18+ (AM7). Sem exclusão por gênero, renda, saúde, religião ou origem." Correção exata: "Idade mínima de 25 anos, sem máxima (decisão 24, AM7). Sem exclusão por gênero, renda, saúde, religião ou origem."
- **Seção 13, linha 3.** Correção exata: "| 3 | Idade: roteiro do cmo sugeria 22 a 35; regra do agente e estratégia 4.1 mandavam 18+ | Resolvido pela decisão 24: 25 anos ou mais, sem máxima, com leitura semanal por faixa |".
- **Seção 14.1, linha "Segmentação não discriminatória".** Correção exata: "| Segmentação não discriminatória | Atendido com decisão registrada | Idade mínima de 25 anos pela decisão 24 do CEO (perfil formado e valor do curso); nenhuma outra exclusão por atributo pessoal |".
- **"Dados que faltam".** Trecho atual: "[CONFIRMAR] Decisão sobre a faixa de idade (AM7) e sobre os 20% de Goiás e DF (slide 17, item 9)." Correção exata: "[CONFIRMAR] Decisão sobre os 20% de Goiás e DF (slide 17, item 9)." E em "Fatos", linha do público base: acrescentar "Idade: 25 anos ou mais, sem máxima (decisão 24)".

**E30. Turma mínima nos textos curtos da fase 1 (ajuste, D-H)**
- Onde: F1-E T2, T3 e T5; F1-C T2, T3 e T4; F1-V T2, T3 e T4 (todos "em espera").
- Correção exata: acrescentar ao fim de cada um "A turma pode não ser formada se não atingir o número mínimo de alunos." e atualizar a contagem total de caracteres. Na seção 14.1, linha "Transparência da turma mínima": "Decidido pelo qa (D-H): obrigatória em todo texto da fase 1 que for ao ar; não obrigatória na fase 2".

**E31. Marcador do termo da matrícula (ajuste, D-C)**
- Seções 7.6, 13 (linha 5) e "Dados que faltam": tirar "[CONFIRMAR NO CATÁLOGO o termo único]" e escrever "decisão D-C do qa de 28/10/2026". O texto da V-P já está certo; ela segue bloqueada por OU8 e AM8 (como em E8).

### Arquivo 7: estrategia-de-conteudo-pos-2026-10-28-calendario-68606.md

**E32. Porta de entrada da página contradiz o E1 (bloqueia o calendário)**
- Onde: seção 3.3, C14, "Ajuste proposto": "Registrar hoje no OA9 a decisão de usar a página (T1 sai em 28/10). Pedir A13 à Ufape até 05/11; sem isso, os RSAs de entrada não sobem (só marca, sem texto de entrada)".
- Problema: pelo E1, a decisão humana de usar a página antes da correção só cobre A7 e A12, e só para peças de antes de 07/11. Peça de depois de 07/11 que chama para entrar não sai sem A13 publicada: isso vale para F2-A, F2-B, RSAs, P3 a P6, TK-B e os ep. 1, 2, 4 e 5, não só para o Google.
- Correção exata do C14: "Registrar hoje no OA9 a decisão da regulação sobre usar a página com A7 e A12 pendentes (vale para T1, T2, W2, F1-E, F1-C, F1-V, P1, P2 e TK-A). Pedir A13 à Ufape até 05/11. Sem A13 publicada e conferida pelo qa, nenhuma peça de depois de 07/11 com chamada ou link da turma sai (E1 do qa de 28/10/2026): os RSAs não sobem e o remarketing da Meta não liga em 07/11." Acrescentar a mesma nota nas linhas de 07/11 (F2-A, F2-B, P3 do Google), 10/11 (TK-B) e 12/11 (P3).

**E33. Calendário da Meta desatualizado (bloqueia: datas de execução erradas)**
- Onde: cabeçalho ("O arquivo saidas/11-midia-paga/anuncios-meta-pos-2026-10-28-68606.md **ainda não existe**"); semana 2, linha 03/11 de F1-C ("subida, CA2"); C23; tabela do kit, linha "Plano de mídia" ("Meta sem arquivo (C23)", "Parcial").
- Problema: o arquivo da Meta existe e define outra sequência: F1-C é reserva (só entra se n = 3 ou como reposição), os públicos de remarketing são criados até 04/11 e F2-A e F2-B vão para a revisão da plataforma em 05/11, com início agendado em 07/11, 00:00.
- Correção exata: (1) cabeçalho: tirar a frase e listar o arquivo da Meta nas entradas; (2) 03/11, F1-C: "F1-C em reserva da troca de 03/11 (entra só se n = 3 ou como reposição, anuncios-meta AM1)"; na linha de F1-E de 03/11, acrescentar "na mesma operação: idade mínima de 25 anos nos conjuntos de frio (decisão 24)"; (3) acrescentar "até qua 04/11 | Meta Ads | Criar os públicos de remarketing (visitantes 30 dias, engajamento 90 dias); conjunto com idade mínima de 25 anos (decisão 24) | F1 | humano no gerenciador | rascunho" e "qui 05/11 | Meta Ads | Enviar F2-A e F2-B para revisão da Meta, conjunto de remarketing com início agendado em 07/11, 00:00 | F1 | humano | rascunho"; (4) C23: "Resolvido: anuncios-meta-pos-2026-10-28-68606.md entregue em 28/10"; (5) kit, linha "Plano de mídia": "Google (anuncios-google) e Meta (anuncios-meta) | Rascunho, em revisão do qa"; (6) na seção 6, linha "Anúncios (Meta e Google)" da medição, acrescentar "custo por lead por faixa de idade: 25 a 34, 35 a 44 e 45 ou mais (decisão 24)".

**E34. Divergências já decididas continuam abertas no calendário (ajuste)**
- C19: trocar o "Ajuste proposto" por "Decidido pelo qa (D-B): pos_68606_202610 em todo toque orgânico e de CRM; pos_conteudo_202612 só no ep. 3; mídia paga com o nome real da campanha (E3)".
- C18: trocar por "P5 com preço só com a OU8 respondida até 14/12; sem ela, P5 sem valores (E16). Termo: 'matrícula' (D-C)".
- C4, C6, C7 e C13: marcar "Decidido em 28/10/2026 (D-G do qa)" e aplicar nas tabelas: em 22/12 só o EP3 no YouTube e no Spotify, sem EP3-C1 e EP3-S1; 23/12 sem EP3-CONV; peças do ep. 3 nas datas do E22; EP1-CARD de 24/11 e os cortes 2 viram Stories.
- Seção 4.1, título: tirar "(datas dos módulos: [CONFIRMAR NO CATÁLOGO])"; lista [CONFIRMAR], linha "[CONFIRMAR NO CATÁLOGO]: 24 módulos (...)": apagar (D-D).
- 12/11, P3: trocar o gancho pelo do E13.
- Acrescentar em 07/11: "Instagram e Facebook | Editar a legenda do P2 para o texto de contingência; tirar P1 dos Destaques, se estiver (E14) | F2 | posts-sociais; humano".
- Seção 0, item 3 e visão mensal de dezembro: trocar "Exceção a decidir: o episódio 3 (...) (conflito C4)" e "(em dia sem campanha: decidir, C4)" por "Episódio 3 em 22/12 só no YouTube e no Spotify, sem peças derivadas no fim de ano (D-G)".

**E35. Peças derivadas do ep. 3 sem data (ajuste, C22)**
- Onde: C22, "Peças do pacote do podcast sem data nos arquivos: (...) cortes 2 e 3 e Story de link do EP3".
- Correção exata: incluir nas semanas 14 a 17 as datas do E22 (27/01, 28/01, 03/02, 04/02 e 17/02), sem chamada de turma, e no C22 escrever "datas do ep. 3 definidas pelo E22 do qa; cards 4:5 dos ep. 2 a 5 viram Story (C6)".

---

## 4. auditorias/conformidade-educacional.md, item por item

Legenda: OK = atendido; FALHA = bloqueia (achado); PENDENTE = depende de resposta ou ação fora da peça, também bloqueia publicação; N/A = não se aplica. C = criativos; G = Google; P = posts; T = tiktok; Pc = podcast; M = Meta; Cal = calendário (avaliado pelo que ele agenda).

| Item | C | G | P | T | Pc | M | Cal |
|---|---|---|---|---|---|---|---|
| **Dados do curso** | | | | | | | |
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | OK | OK | OK | OK | OK | OK | OK |
| Status "aberto" (ou sem chamada para inscrição) | OK (fase 2 pela exceção da linha, com a frase completa) | PENDENTE (E10, E1) | OK | OK | OK (ep. 3 sem chamada) | OK | OK |
| Modalidade clara e correta | OK | OK | OK | OK | OK | OK | OK |
| **Regulação (MEC)** | | | | | | | |
| Graduação: ato do catálogo | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Pós lato sensu: sem "reconhecida pelo MEC" | OK | OK | OK | OK | OK | OK | OK |
| Curso livre: não confere diploma | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Nota MEC só com fonte oficial | OK (nenhuma) | OK | OK | OK | OK | OK | OK |
| **Promessas e provas** | | | | | | | |
| Sem promessa de emprego, salário, aprovação ou sucesso | OK | OK | OK | OK | OK (corte de relato de ganho previsto) | OK | OK |
| Empregabilidade com fonte, período e amostra | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Superlativos só com fonte | OK | OK | OK | OK | OK | OK | OK |
| Comparação com concorrente objetiva | N/A | OK (concorrentes só em negativas) | N/A | N/A | OK | N/A | N/A |
| **Preço e condições** | | | | | | | |
| Preço com parcelas e condições completas, sem esconder matrícula | FALHA (E8, V-P) | OK (sem preço) | FALHA (E16, P5) | OK (sem preço) | OK (sem preço) | OK (V-P bloqueada por OU8 e AM8) | FALHA até E34 (P5 agendado com preço) |
| Bolsa e desconto com regra | OK (nenhum) | OK | OK | OK | OK | OK | OK |
| Urgência real, com data | OK | OK | OK | OK | OK (E20 preventivo) | OK | OK |
| Prouni, Fies ou financiamento | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **Pessoas e dados** | | | | | | | |
| Autorização de imagem e voz registrada | OK (sem pessoas) | N/A | OK (coordenação, decisões 8 e 10; ok dela e foto [CONFIRMAR]) | PENDENTE (voz do narrador, acervo) | FALHA até E25; PENDENTE (apresentador, convidados de fora) | PENDENTE (locução do F1-V e do F2-B) | PENDENTE (herda das peças) |
| Menores só com autorização | OK | N/A | OK | OK | OK | OK | N/A |
| Formulários com finalidade e política de privacidade | PENDENTE (página, E1) | PENDENTE (E1) | PENDENTE (E1) | PENDENTE (E1) | FALHA até E24; PENDENTE (página) | PENDENTE (página e checkout, seção 6) | PENDENTE (caixa de perguntas, C10) |
| WhatsApp e e-mail só com consentimento e saída fácil | N/A | N/A | N/A | OK (contato iniciado pela pessoa) | OK (newsletter no teto D16) | N/A (sem destino WhatsApp) | OK (só opt-in, fila D2, C1 a C3) |
| Nenhum dado pessoal na peça ou nos arquivos | OK | OK | OK | OK | OK (E24 protege a triagem) | OK (lista de contatos bloqueada até base legal, AM6) | OK |
| **Plataformas** | | | | | | | |
| Políticas da Meta e do Google para educação, sem segmentação discriminatória | OK | FALHA até E36 (idade fora da decisão 24) | N/A | N/A | N/A | FALHA até E29 (idade fora da decisão 24) | N/A |
| Página de destino entrega o que a peça promete | FALHA (E1, fase 2) | FALHA (E1, P1) | FALHA (E1, P3 a P6) | FALHA (E1, versão B) | FALHA (E1, ep. 1, 2, 4 e 5) | FALHA (E1, AM9) | FALHA (E32) |
| **Anúncios (Meta e Google)** | | | | | | | |
| Sem característica pessoal de quem vê (texto, título, imagem) | OK | OK | N/A | N/A | N/A | OK (nenhum texto cita idade) | N/A |
| Sem urgência falsa, contador, play falso ou imitação da interface | OK | OK | N/A | N/A | N/A | OK | N/A |
| Sem pessoa pública ou parceria inexistente | OK | OK | N/A | N/A | N/A | OK | N/A |
| Sem caixa alta excessiva, pontuação repetida ou símbolos | OK (conferir nas artes) | OK (só a sigla UFAPE) | N/A | N/A | N/A | OK (conferir nas artes) | N/A |
| Página carrega, sem domínio inesperado, com dados, contato e privacidade | PENDENTE (E1) | PENDENTE (E1) | N/A | N/A | N/A | PENDENTE (E1; caminho de contato com o time [CONFIRMAR]) | N/A |
| Nada para driblar a análise | OK | OK | N/A | N/A | N/A | OK (melhorias automáticas desligadas) | N/A |

**Resultado:** Aprovado ( )  Bloqueado (x) nos 7 arquivos.
**Itens bloqueados e o que precisa mudar:** E1, E3, E7, E8, E10, E14, E16, E19, E21 a E27, E29, E32, E33 e E36, mais os ajustes E2, E4 a E6, E9, E11 a E13, E15, E17, E18, E20, E28, E30, E31, E34 e E35.
**Revisado por:** qa-de-marketing (agente). Humano: [CONFIRMAR, pessoa do marketing; a tabela de aprovação de contexto/ufape-geral.md está vazia].
**Data:** 28/10/2026.

---

## 5. Auditorias de departamento

### auditorias/11-midia-paga.md (criativos, Google e Meta)

| Item | C | G | M |
|---|---|---|---|
| Plano do gestor-de-midia aprovado, com canais justificados | OK (cmo-pos, OA4; seção 5) | OK | OK |
| Metas de CPL e custo por matrícula escritas antes de subir | OK (ilustrativas; R$ 133,33) | OK | OK (seção 2) |
| Verba dentro do valor aprovado, com aprovador registrado | PENDENTE (aprovador [CONFIRMAR]; G [DADO NÃO FORNECIDO]) | PENDENTE (idem; E12) | PENDENTE (idem; contas da seção 9 conferidas e certas) |
| Nomenclatura padrão | OK | OK | OK (tabela de correspondência 3.4) |
| UTMs completas e origem chegando ao CRM | PENDENTE (teste de 30/10) | FALHA até E3; PENDENTE (P6) | PENDENTE (teste de 30/10; utm_term pelo E29) |
| Pixel, API de Conversões e conversões do Google testados | PENDENTE | PENDENTE (P6) | PENDENTE (seção 6, AM10) |
| Criativos aprovados em conformidade-educacional | FALHA (seção 4) | FALHA (seção 4) | FALHA (seção 4) |
| Anúncios dentro das políticas | OK | OK | OK |
| Nenhum público com menos de 18 anos | OK (via Meta) | OK (mínimo 25 pelo E36) | OK (mínimo 25 pelo E29) |
| Post de docente promovido com autorização | N/A | N/A | N/A |
| Relatório semanal ao CMO | N/A (começa com a veiculação) | N/A | N/A |
| Sem segmentação discriminatória nem exclusão por atributo sensível | OK | FALHA até E36 (aplicar a decisão 24; risco registrado em D-F) | FALHA até E29 (idem) |
| Públicos sem dados pessoais sem base legal | OK | OK | OK (AM6) |
| Dados de curso conferidos no catálogo | OK | OK (E5) | OK |
| Destino de WhatsApp oficial com atendimento | N/A | N/A (chamada desligada) | N/A (destino é a página) |
| Números só das exportações | OK | OK | OK |
| Nenhuma alteração sem humano | OK | OK | OK |

### auditorias/05-social.md (posts)

| Item | Resultado |
|---|---|
| Frequência segue o plano | OK (6 posts, 2 feed e 4 Stories, 03/11 a 19/01; slot a slot pendente, E23 e D-G) |
| Todo post tem uma ideia clara | OK |
| Ganchos cumpridos pelo conteúdo | FALHA no P3 (E13); OK nos demais |
| Histórias e números reais | OK (só ficha e catálogo) |
| Formatados para celular | OK |
| Ações de comunidade da semana | N/A (começa com a publicação) |
| Métricas de conversa e lead, não de vaidade | FALHA até E17 |
| Autorização de imagem e depoimento | OK (P3, decisões 8 e 10; ok da docente [CONFIRMAR]) |
| Dados de curso batem com o catálogo | OK (E15 é só redação) |

### auditorias/12-video-e-audio.md (tiktok e podcast)

| Item | T | Pc |
|---|---|---|
| Gancho de 3 segundos funciona sem som e é cumprido | OK | OK |
| Legenda revisada em todo vídeo | PENDENTE (revisão na edição) | PENDENTE (SRT revisado previsto) |
| Autorização de imagem, voz e depoimento | PENDENTE (narrador) | FALHA até E25; PENDENTE (apresentador, convidados) |
| Título, capa e descrição não prometem além do conteúdo | OK | OK |
| Sem promessa de emprego ou urgência falsa | OK | OK |
| Dados de curso batem com o catálogo | OK | OK (D-D) |
| Cadência cabe na capacidade do time | PENDENTE (V1, capacidade [CONFIRMAR]) | FALHA até E26 |
| Métricas de retenção, conversa e clique | OK | OK |

---

## 6. Conferências feitas e sem achado

- **Frase da regra do 3º módulo:** igual, palavra por palavra, à regra 6 do cmo-pos com as datas da ficha, em F2-A e F2-B (arte, locução e legenda), nos 10 textos principais da fase 2 da Meta, em P3 a P6, na versão B do tiktok e nos ep. 1, 2, 4 e 5 do podcast. A data do 3º módulo não aparece fora da frase em nenhuma peça.
- **Coerência de datas entre as peças:** início 07/11/2026; módulos 1, 2 e 3 em 07 e 08/11/2026, 19 e 20/12/2026 e 23 e 24/01/2027; presenciais 6 (17 e 18/04/2027), 13 (27 e 28/11/2027) e 21 (julho de 2028); fase 1 até 06/11, 23h59; fase 2 de 07/11/2026 a 22/01/2027, 23h59; sem peça em 02/11, 20 e 21/11, 25/12 e 01/01. Tudo bate com a ficha, o cmo-pos e o calendário. Os dias da semana de todas as datas citadas estão certos. As incoerências são só E7, E27, E22 e E35 (ep. 3), E23 (grade de feed) e E33 (Meta no calendário).
- **Idade:** só aparece na Meta e no Google (E29 e E36). Nenhum texto, título, arte ou legenda das 7 peças menciona idade de quem vê.
- **Nome do curso:** inteiro em todas as peças; "pós" sozinho só como termo genérico em pergunta (podcast) e "gastro vet" só como palavra-chave do Google.
- **Certificação, "últimas vagas", bolsa, emprego:** nenhuma ocorrência em texto de peça; as palavras só aparecem nas listas de proibição.
- **Docentes:** Esp. Maria Carolina Pappalardo, Dr. Rodolfo Oliveira Leal, Dra. Cibele Figueira Carvalho e DR. Fabrizio Grandi (Dr., pela D-E) com nome e titulação da ficha; nenhuma opinião clínica escrita na voz deles (o problema de voz está só no E21, regra institucional).
- **Contas:** Google 9.2 (87 dias, 80 equivalentes, R$ 962,50 e R$ 1.037,50 com G = 0) e Meta 2 e 9 (R$ 875,00 na fase 2, tabela de recálculo 9.1) certas. Calendário: 118 dias e 18 semanas, certos.
- **Dados pessoais:** nenhum; telefones citados são os oficiais de contexto/ufape-geral.md.
- **"Agência":** nenhuma ocorrência nas 7 peças.
- **Travessão e meia-risca:** nenhuma ocorrência encontrada na leitura integral das 7 peças. Limitação: conferência por leitura, sem busca automática de caracteres nesta sessão; o orquestrador roda a busca dos dois caracteres nos 7 arquivos antes de reenviar ao qa. O "·" do selo do tiktok e o "|" das capas do podcast não são travessão.

## 7. Observações que não bloqueiam

- Google, títulos "Especialização em Cães e Gatos" (area1 3 e area2 15): sozinhos, podem soar como nome de outro curso; a descrição 1 fixada resolve.
- tiktok, legenda da versão B: começa direto pela frase da regra; pode abrir com "Cinco módulos online, depois a prática." e trazer a frase na linha seguinte, como nos criativos.
- Google, local "estado de São Paulo" (EM6, [SUPOSIÇÃO]): a persona secundária viaja de outro estado; vale ler os termos de busca de fora de SP na revisão semanal. A Meta lê por praça (4.5), o que ajuda a comparar.
- Meta, títulos de 34 a 37 caracteres na fase 1 e 2: podem ser cortados em alguns posicionamentos; o nome do curso está na arte e no texto.
- Decisão 24: risco de deixar de fora o recém-formado de 22 a 24 anos registrado em D-F, para a pessoa do marketing ver junto com a aprovação do plano de mídia.
- Calendário, C9 e C10 (Story do ep. 5 em 20/01; caixa de perguntas de 10 a 17/11): de acordo.

---

## Fatos (com fonte)

- 68606: Pós-graduação em Gastroenterologia Veterinária, São Paulo, semipresencial, início 07/11/2026, turma IX, 500 h, "30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00", status "aberto" (contexto/catalogo-de-cursos.md, seção 2).
- O catálogo indica a ficha como fonte do cronograma, da coordenação e das condições (contexto/catalogo-de-cursos.md, cabeçalho).
- Cronograma, presenciais 6, 13 e 21, coordenação, 38 nomes listados, "1ª mensalidade deverá ser paga até 30 dias de antecedência da data de seu início", "Turma mínima de 20 alunos" e a frase ligada ao MEC na página (ficha 68606).
- Decisões 8, 10, 11, 14, 15, 16, 18, 21, 22, 23 e 24 (docs/execucao-2026-10-26.md). Decisão 24: idade mínima de 25 anos, sem máxima, leitura semanal por faixa (25 a 34, 35 a 44, 45 ou mais), substitui 22 a 35 e 18+; referência citada: Demografia da Medicina Veterinária 2022.
- Regras 4, 5, 6, 7, 9 e 11, OA4, OA9 a OA12, OU3, OU6 e OU8, seção 5 dos canais (cmo-pos-2026-10-26.md, versão 4).
- Episódio 3 sem chamada de turma, faixa de 22 a 35 do deck e calendário do podcast (cmo-pos-2026-10-28-apresentacao-68606.md, slides 4 e 13 a 15).
- Contatos oficiais e instabilidade do WhatsApp em 22/10/2026; tabela de aprovação vazia (contexto/ufape-geral.md).
- Toda peça com preço mostra parcelas, valor da parcela, total e matrícula; persona de 24 a 40 anos e persona secundária recém-formada [SUPOSIÇÃO do contexto]; exceção de divulgação de turma iniciada até a véspera do 3º módulo, com a regra completa (contexto/pos-graduacao.md).

## [SUPOSIÇÃO]

- Os ganchos A6 citados nas peças batem com o original do criador-de-ganchos-pos (conferidos só pela citação do slide 8).
- Ajuste de caixa da titulação permitido (D-E).
- Datas das peças derivadas do ep. 3 depois de 22/01 (E22 e E35).
- Pedido de pausa ao gestor quando G passar de R$ 1.794,29 (E12).
- A idade de 25 anos nos conjuntos de frio entra na mesma operação da troca de 03/11 e conta como uma mudança só (E29); no Google, a faixa "desconhecida" fica incluída (E36). O gestor confirma as duas.

## [CONFIRMAR]

- A13, A7 e A12 na página da 68606, ou decisão da regulação sobre publicar antes de A7 e A12 (E1, E32).
- OU8: pagamento da 1ª mensalidade de quem entra depois do início (E8, E16, V-P da Meta). OU3 e OU6 seguem abertas; nenhuma peça promete reposição.
- Exceção `pos_conteudo_<AAAAMM>` com o arquiteto-de-fluxos (D-A, E22).
- Nome real das campanhas Meta e Google da 68606 (exportação D6) (E3).
- Preferência da pessoa do marketing entre "matrícula" e "inscrição" (D-C).
- Quem executa e quem confere a troca de fase na sexta 06/11 e no sábado 07/11 (D-G, C13).
- WhatsApp de vendas funcionando e horário de atendimento (E19).
- Termo do egresso e aprovação de depoimento (E25); equipe e capacidade do podcast (E26); formulário com política de privacidade (E24).
- Ok da Esp. Maria Carolina Pappalardo para o P3 e foto aprovada; voz do narrador do tiktok e das locuções F1-V e F2-B.
- Quem aprova cada tipo de peça (tabela de contexto/ufape-geral.md vazia; até lá, a pessoa do marketing).

## Fontes

- /home/user/marketing-ufape/contexto/ufape-geral.md
- /home/user/marketing-ufape/contexto/pos-graduacao.md
- /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md (inclusive a decisão 24)
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md, /home/user/marketing-ufape/auditorias/11-midia-paga.md, /home/user/marketing-ufape/auditorias/05-social.md, /home/user/marketing-ufape/auditorias/12-video-e-audio.md
- As 7 peças revisadas (cabeçalho).
- Externas: nenhuma.

**Próximo passo:** cada arquivo volta ao seu agente com os achados dele (criativos-de-anuncio: E4, E7 a E9; anuncios-google: E3, E5, E10 a E12, E36; posts-sociais: E13 a E17; tiktok: E2, E18, E19; podcast: E2, E5, E6, E20 a E26; anuncios-meta: E27 a E31, mais E7 nas artes de F2-A e F2-B; estrategia-de-conteudo: E32 a E35). Nota ao cmo: slide 4 da apresentação com a decisão 24 e a caixa da titulação (E6). E1 é pedido à Ufape (OA10). Depois das correções, as 7 peças voltam ao qa-de-marketing antes da aprovação humana.
