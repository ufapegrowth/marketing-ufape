# QA do enxoval da turma 68606: Pós-graduação em Gastroenterologia Veterinária, turma IX, São Paulo

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 28/10/2026 (quarta-feira)
- **Objeto:** as 5 peças novas do enxoval da 68606, antes de entrarem na apresentação ao cliente (decisões 22 e 23).
- **Status:** rascunho de revisão. Nada é publicado, enviado ou pago. As peças não foram editadas: cada correção abaixo volta para o agente dono do arquivo.
- **Entradas lidas:**
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 2, linha 68606)
  - /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha inteira, com cronograma e lista de docentes)
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 23 e regras para toda saída)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md (versão 4: seções 1 a 11)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md (slides 1 a 15)
  - As 5 peças: /home/user/marketing-ufape/saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-google-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/05-social-e-comunidade/posts-sociais-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/12-video-e-audio/tiktok-pos-2026-10-28-68606.md, /home/user/marketing-ufape/saidas/12-video-e-audio/podcast-pos-2026-10-28-ufape-cast-68606.md
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md, /home/user/marketing-ufape/auditorias/11-midia-paga.md, /home/user/marketing-ufape/auditorias/05-social.md e /home/user/marketing-ufape/auditorias/12-video-e-audio.md
- **Não aberto nesta revisão:** o arquivo do gestor-de-midia-pos, a casa de mensagens (mensagens-pos) e os ganchos do criador-de-ganchos-pos (área A6). Os trechos deles foram conferidos pelo que o plano do cmo (versão 4) e a apresentação de 28/10 citam. As citações A6-02, A6-03, A6-07 e A6-09 das peças batem com o texto do slide 8 da apresentação [SUPOSIÇÃO: o original A6 não foi relido]. faculdade.ufape.com.br não foi aberto (o texto da página está na ficha).
- **Dados pessoais:** nenhum nesta revisão. Docentes só com nome e titulação da ficha.

---

## 1. Vereditos

| # | Arquivo | Veredito | Achados que bloqueiam | Volta para |
|---|---|---|---|---|
| 1 | criativos-de-anuncio-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E3, E7, E8 | criativos-de-anuncio |
| 2 | anuncios-google-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E3, E10 (E11 e E12 são correções de texto e de conta) | anuncios-google |
| 3 | posts-sociais-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E14, E16 | posts-sociais |
| 4 | tiktok-pos-2026-10-28-68606.md | **CORRIGIR** | E1, E2, E19 | tiktok |
| 5 | podcast-pos-2026-10-28-ufape-cast-68606.md | **CORRIGIR** | E1, E2, E21, E22, E23, E25, E26 | podcast |

Regra aplicada: toda peça que falha em qualquer item de auditorias/conformidade-educacional.md recebe CORRIGIR, sem exceção. O item "Página de destino entrega exatamente o que o anúncio ou a mensagem prometeu" falha hoje nas 5 (E1), porque todas têm peças de depois de 07/11 que levam à página da turma, e a página ainda não escreve a regra do 3º módulo. Mesmo com E1 resolvido, cada arquivo tem correções próprias.

**Para a apresentação ao cliente:** as 5 peças podem entrar como rascunho, com a etiqueta "em revisão do qa, não publicar" e os achados desta lista visíveis. Nenhuma segue para a aprovação humana de publicação antes de voltar corrigida e passar de novo no qa.

**Contagens do Google (pedido do orquestrador):** conferi caractere por caractere os 90 títulos, as 24 descrições, os 4 títulos e as 8 linhas de sitelink, as 7 frases de destaque e os 3 valores do snippet. Todas as contagens declaradas estão certas e nenhum texto passa do limite (30, 90, 25, 35 e 25). O único erro está no resumo da seção 5.8 (E11).

---

## 2. Decisões das divergências que os agentes deixaram abertas

### D-A. Episódio 3 do podcast sem chamada de turma

**Decisão: o episódio 3 (22/12/2026) sai sem chamada de turma.** Motivos: (1) o plano da apresentação (slides 14 e 15) já previa assim; (2) 22/12 cai na janela de 21/12 a 03/01 sem campanha (cmo-pos, regra 5, e posts-sociais, regra 2); (3) o tema (luto e burnout) é sensível, e uma chamada de venda colada nele soa como aproveitamento. Consequências: nenhuma peça do episódio 3 (descrição, cortes, capas, card 4:5, Stories, card do convidado) leva [CHAMADA-TURMA], link da página da 68606 ou a data do 3º módulo; o link usa a exceção `pos_conteudo_202612`, que segue [CONFIRMAR com o arquiteto-de-fluxos] (cmo-pos, regra 11). Correções no arquivo do podcast: E22.

### D-B. Mês do utm_campaign (202610 contra o mês da publicação)

**Decisão: `utm_campaign=pos_68606_202610` em todo toque orgânico e de CRM da turma, em qualquer mês de publicação.** Fonte: cmo-pos, regra 11 e OA9, ajuste N2 da versão 4 (mês do primeiro envio, igual em todos os toques da turma, com o toque diferenciado no utm_content). O primeiro envio da 68606 foi o e-mail de 28/10 (OA9). O D12 do plano geral ("mês do primeiro envio ou da publicação") é a regra geral; a regra 11 do plano da turma é a aplicação dela e prevalece. A exceção `pos_conteudo_<AAAAMM>` vale só para peça sem chamada de turma (episódio 3, D-A). Já está certo nos posts-sociais; precisa mudar no tiktok e no podcast (E2). Na mídia paga, o utm_campaign é o nome da campanha (D11 e D12), e a coerência entre Meta e Google está no E3.

### D-C. "Matrícula" ou "inscrição" para os R$ 250,00

**Decisão: nas peças, "matrícula de R$ 250,00".** Motivos: (1) dado de curso só vem do catálogo, e o catálogo (seção 2) e a página da turma dizem "matrícula R$ 250,00"; (2) a decisão 23 diz "R$ 250,00, como no site" e manda citar "a condição completa do catálogo"; (3) a peça precisa casar com a página de destino (item de plataforma da auditoria); (4) a palavra também casa com a frase da regra ("A Ufape aceita matrícula até o 3º módulo"): pagar a matrícula é o ato de entrar. Nos relatórios e no funil interno, segue "inscrição paga" como etapa medida à parte da 1ª mensalidade (decisões 16 e 23). Se a pessoa do marketing preferir "inscrição", a troca vale para todas as peças de uma vez e o catálogo é atualizado antes (pedido ao orquestrador). Correção: E8 (criativos). Posts (P5), tiktok e Google já usam "matrícula" nas peças.

### D-D. Dados do cronograma marcados [CONFIRMAR NO CATÁLOGO]

**Decisão: o cronograma, os módulos, o local, a coordenação e a lista de docentes da ficha valem como catálogo.** O próprio catálogo diz que os detalhes de cada curso (descrição, público, cronograma, coordenação, condições) estão na ficha em contexto/cursos/ (cabeçalho, linha 8). Os marcadores [CONFIRMAR NO CATÁLOGO] sobre 24 módulos, aulas práticas, endoscopia, grupo de discussão de casos e endereço saem (E5). Também conferi a linha 68606 do catálogo, que o podcast não abriu: nome, São Paulo, semipresencial, 07/11/2026, turma IX, 500 h, "30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00", status "aberto", fonte "planilha e site". Bate com as 5 peças.

### D-E. Grafia da titulação dos docentes

**Decisão [SUPOSIÇÃO a validar com a Ufape]:** só a caixa pode ser ajustada (DR. para Dr., DRA. para Dra., MSC. para MSc.); nome e titulação nunca mudam. O ajuste vale igual em todas as peças e na apresentação (o slide 14 ainda escreve "DR. Fabrizio Grandi" e o podcast "Dr. Fabrizio Grandi"). Motivo: nos anúncios a caixa alta conta como "caixa alta excessiva" na auditoria. Correção: E6.

---

## 3. Achados

Formato: arquivo, onde, trecho atual, correção exata. "Bloqueia" indica item de conformidade ou de promessa; "ajuste" indica correção que precisa entrar, sem item de conformidade próprio.

### Transversais

**E1. Página de destino não entrega a regra do 3º módulo (bloqueia, os 5 arquivos)**
- Onde: toda peça de depois de 07/11 com link ou chamada para a página da turma: F2-A, F2-B e V-P (criativos); os 6 RSAs, sitelinks e frases de destaque da fase 2 (Google); P3 a P6 (posts); versão B (tiktok); episódios 1, 2, 4 e 5 e seus pacotes (podcast).
- Trecho atual: a ficha (texto da página) não traz a regra "matrícula até o 3º módulo", traz a frase ligada ao MEC e "Turma mínima de 20 alunos". Os próprios agentes marcaram "pendente externo" (A7, A12 e A13 do OA10).
- Correção exata: nenhuma dessas peças sobe ou é publicada antes de (1) a página da 68606 publicar a frase "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram." (A13), conferida pelo qa na ficha atualizada; e (2) a troca da frase ligada ao MEC (A7) e da turma mínima (A12), ou o registro da decisão da regulação sobre publicar antes dela (cmo-pos, regra 9). Cada arquivo acrescenta essa condição na sua lista de aprovações. As peças de antes de 07/11 (F1-E, F1-C, F1-V, P1, P2, versão A) dependem só do item (2).

**E2. utm_campaign fora da decisão D-B (bloqueia rastreio por turma; tiktok e podcast)**
- tiktok, seção 2.2: `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`.
- tiktok, seção 6, "Regras da versão B": `utm_campaign=pos_68606_202611 (mesmo mês do primeiro toque)`. Trocar por `utm_campaign=pos_68606_202610 (mês do primeiro envio da turma, regra 11 do cmo-pos)`.
- tiktok, lista [SUPOSIÇÃO]: "mês 202611 como mês de publicação". Trocar por "mês 202610, do primeiro envio da turma (decisão D-B do qa de 28/10/2026)".
- podcast, seção 0, [LINK-TURMA]: `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`, e a frase "o `utm_campaign` e o `utm_content` mudam por episódio" por "só o `utm_content` muda por episódio".
- podcast, seção 0, linha "Mês do `utm_campaign` segue o mês de publicação (...)": trocar por "O `utm_campaign` é `pos_68606_202610` em todo episódio com chamada da turma (regra 11 do cmo-pos). Episódio sem chamada de turma usa `pos_conteudo_<AAAAMM>` [CONFIRMAR com o arquiteto-de-fluxos]."
- podcast, seções 2.3 e 2.4 (links do ep. 1): `utm_campaign=pos_68606_202611`. Trocar por `utm_campaign=pos_68606_202610`.
- podcast, ep. 2: `utm_campaign=pos_68606_202612`; ep. 4 e ep. 5: `utm_campaign=pos_68606_202701`. Trocar os três por `utm_campaign=pos_68606_202610`.

**E3. Critério do utm_campaign diferente entre Meta e Google (ajuste, criativos e Google)**
- criativos, seção 1.4: "utm_campaign igual ao da campanha existente do 68606 [CONFIRMAR o nome na exportação D6]". Google, seção 3: "O `utm_campaign` dos anúncios novos usa o nome D12 de referência acima, para a leitura por turma fechar."
- Correção exata: as duas plataformas usam o mesmo critério, o do Google (nome D12 de referência, minúsculas, sem acento, com a tabela de correspondência da ação A4 para o nome real no ar). No criativos, trocar a linha por: "utm_campaign = nome D12 de referência da campanha Meta da 68606, definido pelo anuncios-meta no mesmo padrão do Google (`pos_68606-gastro_meta_..._<AAAAMM da subida>`), com tabela de correspondência para o nome real no ar [CONFIRMAR na exportação D6]." No Google, manter, e acrescentar na seção 11, item 2: "Conferir que o anuncios-meta usa o mesmo critério." O AAAAMM da subida da campanha paga é o mês real da exportação D6 (o 202610 do Google segue [SUPOSIÇÃO] até lá).

**E4. Termo do valor de R$ 250,00 (decisão D-C)**
- Aplicação nas peças: E8 (criativos). Nos trechos internos (criativos 1.1 e 7, Google 8.3), basta registrar "matrícula de R$ 250,00 (decisão D-C do qa de 28/10/2026)".

**E5. Marcadores [CONFIRMAR NO CATÁLOGO] sobre dados da ficha (ajuste, Google e podcast; decisão D-D)**
- Google, título 15 do RSA area1: "Prática em endoscopia [CONFIRMAR NO CATÁLOGO]". Trocar por "Prática em endoscopia" (21). Módulo 13 presencial "Endoscopia" e o diferencial "Aulas práticas de anatomia, Cirurgia e endoscopia" estão na ficha.
- Google, seção 5.1 (dois últimos itens), seção 4.4 (linha K6.6), checklist item 7, seção 12 (linha "Dado que só está na ficha") e "Dados que faltam": tirar o [CONFIRMAR NO CATÁLOGO] e escrever "ficha da 68606, que o catálogo indica como fonte do cronograma".
- podcast, lista [CONFIRMAR], linha "Confirmar no catálogo (...)": apagar. Conferido pelo qa em 28/10/2026 (D-D).

**E6. Caixa da titulação dos docentes (ajuste, podcast e apresentação; decisão D-E)**
- podcast, cabeçalho: "Docentes só com nome e titulação como estão na ficha (maiúsculas normalizadas)". Manter, acrescentando: "Só a caixa muda (DR. para Dr.); nome e titulação como na ficha. Mesmo ajuste na apresentação."
- Nota ao cmo (sem editar o arquivo dele): o slide 14 escreve "DR. Fabrizio Grandi" e o slide 11 "DRA. VIVIANE DE MARCO" e "DRA. Maria Anete Lallo"; aplicar o mesmo ajuste de caixa da peça que for ao cliente.

### Arquivo 1: criativos-de-anuncio-pos-2026-10-28-68606.md

**E7. F2-A e F2-B marcam o módulo 2 como "já aconteceu" desde 07/11 (bloqueia: informação falsa até 20/12)**
- Onde: seção 4.2, briefing visual ("agora com os módulos 1 e 2 em tom de 'já aconteceu'"); seção 4.3, roteiro 0:03 a 0:07 ("Linha do tempo de 24 quadrados com os módulos 1 e 2 em tom de 'já aconteceu'").
- Problema: a fase 2 roda de 07/11/2026 a 22/01/2027. O módulo 2 é em 19 e 20/12/2026 (ficha). De 07/11 a 20/12 a arte mostraria como passado um módulo que ainda não aconteceu.
- Correção exata, nas duas seções: trocar o trecho por "a linha do tempo de 24 quadrados fica neutra, sem nenhum módulo marcado como 'já aconteceu', com os 3 presenciais (6, 13 e 21) em cor de destaque". Assim uma só arte vale de 07/11 a 22/01.

**E8. Variante V-P: termo e condição incompleta (bloqueia preço)**
- Onde: seção 4.4, parágrafo a acrescentar.
- Trecho atual: "Condições: 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; inscrição de R$ 250,00, à vista (Pix ou boleto) ou em 1x no cartão."
- Correção exata do texto: "Condições: 30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula de R$ 250,00, à vista (Pix ou boleto) ou 1x de R$ 250,00 no cartão."
- Condição de uso: a V-P segue bloqueada até a resposta da OU8 (como paga a 1ª mensalidade quem entra depois do início). A ficha diz que a 1ª mensalidade é paga até 30 dias antes do início; para quem entra depois de 07/11 essa condição é impossível e a peça não pode omitir nem inventar a regra nova (auditoria, "Preço mostra valor, número de parcelas e condições completas"). Com a OU8 respondida, a frase dela entra no mesmo parágrafo, logo depois da matrícula, e a V-P volta ao qa. Atualizar a seção 7, itens 2 e 3, e a matriz 5.1 (linhas F2-A-vp e F2-B-vp) com "bloqueado até OU8 e aprovação de preço".

**E9. Título do cartão 4 do carrossel passa do limite que o próprio arquivo fixou (ajuste)**
- Onde: seção 3.2, "Título por cartão (... até cerca de 32 caracteres)".
- Trecho atual: "4. Online, de 22/05/2027 a 20/02/2028" (o texto do campo tem 34 caracteres).
- Correção exata: "4. Online, 05/2027 a 02/2028" (o texto do campo tem 25 caracteres).

### Arquivo 2: anuncios-google-pos-2026-10-28-68606.md

**E10. Textos de "entrada" sem a frase completa da regra (bloqueia)**
- Regra: depois do início, toda peça que fala de entrada diz a regra inteira (cmo-pos, regra 6); a frase não cabe em 90 caracteres. Decisão do qa: o plano B (data de início mais "veja as condições na página") só é aceito se nenhum texto do RSA falar de entrada; o título fixado "Turma iniciada em 07/11" fica, porque é fato passado e protege contra a leitura de que a turma ainda vai começar; e a subida segue presa ao P1 (E1). Trocas exatas:
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
- Problema: na fase 2 ficam ativos os grupos `__marca` e `__area`, que dividem um só orçamento. Com 2 RSAs por grupo são 4 anúncios, e a regra da própria tabela (maior CPL aguentado = 2 x semanal / número de anúncios) pede semanal de pelo menos R$ 36,00, não R$ 18,00.
- Correção exata da tabela:

| Situação | Condição | Resultado na fase 2 |
|---|---|---|
| 2 RSAs por grupo (4 anúncios) | semanal do Google maior ou igual a R$ 36,00 (diária maior ou igual a R$ 5,14) | Vale para G até R$ 1.177,14 |
| 1 RSA por grupo (2 anúncios) | semanal maior ou igual a R$ 18,00 (diária maior ou igual a R$ 2,57) | Vale para G até R$ 1.588,57 |
| Só `__marca`, 1 RSA | semanal maior ou igual a R$ 9,00 (diária maior ou igual a R$ 1,29) | Vale para G até R$ 1.794,29; acima disso, pedido de pausa ao gestor [SUPOSIÇÃO] |

- Conta: diária do Google na fase 2 = 0,50 x (2.000 menos G) / 80; R$ 36,00 / 7 = R$ 5,14 por dia, logo 2.000 menos G maior ou igual a R$ 822,86. A frase "Com G = 0, a semanal do Google na fase 2 é R$ 87,50: passa com folga" continua certa.

### Arquivo 3: posts-sociais-pos-2026-10-28-68606.md

**E13. Gancho do P3 não é cumprido pelo conteúdo (ajuste, auditoria 05)**
- Trecho atual: gancho "Quando um caso gastrointestinal pede uma segunda opinião?"; as telas 2 e 3 não respondem à pergunta (de propósito, para não pôr conduta na voz de ninguém).
- Correção exata: usar o gancho alternativo 1 como linha 1 e como texto grande da tela 1: "Discussão de casos entre alunos e coordenação: o que a página da Pós-graduação em Gastroenterologia Veterinária prevê." A legenda de apoio começa com a mesma frase no lugar da pergunta. A pergunta da segunda opinião fica para o episódio 2 do podcast, onde o convidado responde.

**E14. P2 (feed) continua no perfil depois de 07/11 com chamada de entrada sem a regra (bloqueia)**
- Trecho atual, card 6: "A turma IX começa em 07/11/2026, em São Paulo." e "Fale com o time para saber como entrar na turma."; legenda com as mesmas linhas.
- Problema: post de feed não sai do ar sozinho. A partir de 07/11 o card diria que a turma "começa" e chamaria para entrar sem a frase completa. O texto da arte não pode ser editado depois de publicado.
- Correção exata do card 6: "Turma IX, São Paulo." / "24 módulos, 500 horas, semipresencial." / "Cronograma completo e docentes na página da turma." / "Link na bio." (sem data e sem chamada de entrada na arte). A data de início e a chamada ficam só na legenda, e em 07/11 a legenda é editada para o texto de contingência da seção 7 (frase completa mais "Fale com o time para saber como entrar na turma."). Acrescentar na seção 7: "Em 07/11, editar a legenda do P2 no Instagram e no Facebook; se o P1 estiver nos Destaques, tirar dos Destaques em 07/11."

**E15. Jargão interno no P4 (ajuste)**
- Trecho atual, card 3: "Neste módulo, a ficha não lista cirurgia."
- Correção exata: "Neste módulo, o cronograma não lista cirurgia."

**E16. P5 com preço sem a condição da 1ª mensalidade (bloqueia preço)**
- Trecho atual, tela 2: "30x de R$ 1.180,00 no cartão ou boleto." / "Total: R$ 35.400,00."; tela 3: "R$ 250,00, à vista (Pix ou boleto) ou 1x de R$ 250,00 no cartão."; legenda com os mesmos dados.
- Problema: o P5 sai em 15/12, depois do início. A página manda pagar a 1ª mensalidade até 30 dias antes do início, o que é impossível para quem entra agora, e a regra para quem entra depois (OU8) não existe. "A conta inteira" fica incompleta (auditoria, preço com condições completas; contexto da linha, "Toda peça com preço mostra número de parcelas, valor da parcela, total e matrícula", mais as condições).
- Correção exata, se a OU8 for respondida até 14/12: tela 2 vira "30x de R$ 1.180,00." / "R$ 35.400,00 no cartão ou boleto." (a forma do catálogo); tela 3 ganha a linha "1ª mensalidade: [texto da resposta da OU8]"; a legenda segue a mesma ordem. O P5 volta ao qa.
- Correção exata, se a OU8 não for respondida até 14/12 (o kit não perde o post): gancho e tela 1 "Quanto custa a Pós-graduação em Gastroenterologia Veterinária? Onde ver a conta inteira."; telas 2 e 3 viram uma só: "Parcelas, total e matrícula estão na página da turma." / "500 horas, 24 módulos, semipresencial, São Paulo."; tela 4 sem mudança; nenhum valor na peça.

**E17. Métricas do kit não aparecem (ajuste, auditoria 05)**
- Correção exata: acrescentar no fim da seção 0.1 o item 10: "Métricas: cliques no link com UTM por peça, respostas e mensagens recebidas, conversas com o time de vendas que citam o post (só contagem), salvamentos. Alcance e curtidas só como contexto."

### Arquivo 4: tiktok-pos-2026-10-28-68606.md

**E18. Captura da página oficial no vídeo (ajuste, coerência com os criativos)**
- Trecho atual, seção 4, imagem 8: "Recorte da tela do cronograma na página da turma | Bloco 5 | Captura de tela"; bloco 5 do roteiro: "o recorte da página mostra só o cronograma".
- Problema: o pacote de criativos proíbe captura da página oficial, porque ela traz a frase ligada ao MEC; um recorte pode mudar quando o site mudar.
- Correção exata: apagar a imagem 8 e, no bloco 5, trocar "o recorte da página mostra só o cronograma (ver nota de gravação 3)" por "só o gráfico da imagem 7, com o texto da ficha". Ajustar a nota de gravação 3: "Se a Ufape alterar o cronograma, refazer o gráfico."

**E19. Número de WhatsApp de vendas sem a conferência (bloqueia o item de destino)**
- Trecho atual, seção 2.2: "WhatsApp de vendas São Paulo: (11) 91366-9290 (contexto/ufape-geral.md)", para botão ou comentário fixado.
- Problema: o próprio contexto registra instabilidade do WhatsApp em 22/10/2026 e não informa horário de atendimento de vendas (auditoria 11, "Destino de WhatsApp é número oficial com atendimento informado"; o posts-sociais já marca a conferência).
- Correção exata: acrescentar depois do número: "[CONFIRMAR antes de publicar que o número voltou a funcionar e o horário de atendimento de vendas]". Sem a confirmação, o comentário fixado leva só à página da turma.

### Arquivo 5: podcast-pos-2026-10-28-ufape-cast-68606.md

**E20. Data do 3º módulo falada fora da frase no episódio 5 (ajuste preventivo)**
- Onde: ep. 5, "Tema da ficha: módulo 3 (...), que acontece em 23 e 24/01/2027" e pergunta 5, num episódio que sai a 4 dias do 3º módulo.
- Correção exata: acrescentar nos cuidados do ep. 5: "Ninguém fala a data do módulo 3 nem 'neste fim de semana' fora da [CHAMADA-TURMA]; na pauta, a pergunta 5 cita só 'o módulo 3 da Pós-graduação em Gastroenterologia Veterinária', sem data."

**E21. Regra de entrada pedida à coordenadora (bloqueia: frase institucional na voz da docente)**
- Trecho atual, ep. 1, bloco 5, pergunta 4: "Que orientação vocês dão a quem quer entrar depois do início da turma? (a resposta é a [CHAMADA-TURMA]; o que a coordenação não souber, o apresentador diz 'o time confirma', sem prometer reposição)".
- Problema: o arquivo escreve a resposta da docente e abre espaço para promessa de reposição na voz dela (OU3 aberta). A regra é institucional.
- Correção exata: apagar a pergunta 4 do bloco 5. A regra aparece só como FALA INSTITUCIONAL do apresentador no bloco 6, como já está. Acrescentar em "Não perguntar nem afirmar": "regra de entrada depois do início (é fala do apresentador)".

**E22. Episódio 3: aplicar a decisão D-A (bloqueia o pacote do ep. 3)**
- Trecho atual: "Chamada: sem chamada de turma (...). Link da Ufape com `utm_campaign=pos_conteudo_202612` [CONFIRMAR exceção de UTM]. Se a Ufape preferir manter a chamada da turma, usa-se a [CHAMADA-TURMA] completa. **Decisão da Ufape [CONFIRMAR].**"
- Correção exata: "Chamada: sem chamada de turma (decisão D-A do qa de 28/10/2026). Chamada única: 'Siga o UFAPE Cast e envie sua pergunta para o próximo episódio.' Link: canal do UFAPE Cast no YouTube ou no Spotify; se o link for para o site, https://faculdade.ufape.com.br/?utm_source=<youtube|spotify|instagram>&utm_medium=organic_social&utm_campaign=pos_conteudo_202612&utm_content=ufapecast_ep03 [CONFIRMAR exceção com o arquiteto-de-fluxos]. Nenhuma peça do ep. 3 leva [CHAMADA-TURMA], link da 68606 ou data do 3º módulo." Apagar o item 10 da seção 6.
- Pergunta 5 do ep. 3: "Por que esse tema aparece num curso técnico, como o módulo 24 da ficha da pós?". Trocar por "Por que esse tema aparece num curso técnico, como no módulo 24 da Pós-graduação em Gastroenterologia Veterinária?".
- Calendário (seção 4): faltam o corte 2, o corte 3 e o Story de link do ep. 3. Acrescentar, sem chamada de turma: "ter 29/12: corte 2 e Story 2 do ep. 3 (link para o episódio)" e "sex 08/01: corte 3 do ep. 3" [SUPOSIÇÃO de datas: fora de 25/12 e 01/01 e sem outro post de feed da Pós no mesmo dia].

**E23. Calendário passa do teto de feed da Pós (bloqueia a grade)**
- Trechos atuais: "ter 24/11: Ep. 1 no ar; corte 1; Story de estreia; card 4:5" e, na mesma semana, card do convidado (25/11) e corte 2 (26/11).
- Problema: corte (Reel) e card 4:5 no mesmo dia somam 2 posts de feed da Pós; o teto é 1 por linha por dia (D5, citado no posts-sociais). A semana de 23 a 29/11 fica com 4 posts de feed da Pós, contra os 3 slots semanais da linha (cmo-pos, seção 4). O mesmo se repete nas semanas dos ep. 2, 4 e 5, e a nota do posts-sociais (P4 pode ir para 01/12) cairia no dia do corte 3 do ep. 1.
- Correção exata: (1) o card 4:5 do ep. 1 sai de 24/11 e vira peça de remarketing (AP-4, só com aprovação) ou Story, nunca feed no mesmo dia do corte 1; (2) acrescentar na seção 4: "No máximo 1 post de feed da Pós por dia e 3 por semana, somando o kit da turma, os posts de docente e o podcast; a conferência slot a slot é do posts-sociais antes da aprovação"; (3) o P4 do posts-sociais fica em 03/12, sem a opção de 01/12; (4) trocar a ordem das linhas "ter 26/01" e "seg 25/01" (a de 25/01 vem antes).

**E24. Pergunta da comunidade: dados pessoais e formulário (bloqueia o bloco 4 antes de 09/11)**
- Trecho atual: "caixa de perguntas nos Stories e formulário curto da Ufape, abertos de 09/11 a 17/11 [SUPOSIÇÃO de prazo] (...) [CONFIRMAR formulário com política de privacidade (pendência p04)]".
- Correção exata: acrescentar "A caixa de perguntas do Instagram mostra o perfil de quem enviou: o perfil nunca vai para arquivo de trabalho, planilha ou chat da squad; a triagem copia só o texto da pergunta. O formulário só abre com finalidade escrita e link da política de privacidade. Sem isso até 08/11, o ep. 1 usa a pergunta de reserva e o bloco 4 não abre formulário."

**E25. Egresso no ep. 1 é depoimento (bloqueia o ep. 1 com egresso)**
- Trecho atual: "Egresso de pós da Ufape: [CONFIRMAR nome, de qual pós, e autorização de imagem, voz e citação]".
- Correção exata: acrescentar "Relato de egresso é depoimento: além do termo assinado de imagem, voz e citação, o episódio com egresso passa pela aprovação de 'Peças com certificação, ato regulatório ou depoimento' de contexto/ufape-geral.md (responsável e regulação, hoje [CONFIRMAR]). Sem as duas coisas, o ep. 1 sai só com a coordenação, e a descrição, os títulos, o card 4:5 e o Story 1 tiram toda menção ao egresso."

**E26. Capacidade de produção não definida (bloqueia a aprovação da série, auditoria 12)**
- Trecho atual: seção 6, itens 1 e 2 (nome, perfis, quem apresenta, grava, edita e publica, horas por semana, custo) em aberto.
- Correção exata: acrescentar na lista de aprovações: "A série só vai à aprovação de produção (AP-2) com equipe, horas por semana e custo informados pela Ufape. Até lá, o pacote é plano, não calendário." O item "Cadência cabe na capacidade de gravação e edição do time" fica sem marcação até a resposta.

---

## 4. auditorias/conformidade-educacional.md, item por item

Legenda: OK = atendido; FALHA = bloqueia (achado); PENDENTE = depende de resposta ou ação fora da peça, também bloqueia publicação; N/A = não se aplica. C = criativos; G = Google; P = posts; T = tiktok; Pc = podcast.

| Item | C | G | P | T | Pc |
|---|---|---|---|---|---|
| **Dados do curso** | | | | | |
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | OK | OK | OK | OK | OK |
| Status "aberto" (ou sem chamada para inscrição) | OK (fase 2 pela exceção da linha, com a frase completa) | PENDENTE (E10, E1) | OK | OK | OK (ep. 3 sem chamada) |
| Modalidade clara e correta | OK | OK | OK | OK | OK |
| **Regulação (MEC)** | | | | | |
| Graduação: ato do catálogo | N/A | N/A | N/A | N/A | N/A |
| Pós lato sensu: sem "reconhecida pelo MEC" | OK | OK | OK | OK | OK |
| Curso livre: não confere diploma | N/A | N/A | N/A | N/A | N/A |
| Nota MEC só com fonte oficial | OK (nenhuma) | OK (nenhuma) | OK (nenhuma) | OK (nenhuma) | OK (nenhuma) |
| **Promessas e provas** | | | | | |
| Sem promessa de emprego, salário, aprovação ou sucesso | OK | OK | OK | OK | OK (corte de relato de ganho previsto) |
| Empregabilidade com fonte, período e amostra | N/A | N/A | N/A | N/A | N/A |
| Superlativos só com fonte | OK | OK | OK | OK | OK |
| Comparação com concorrente objetiva | N/A | OK (concorrentes só em negativas) | N/A | N/A | OK (pauta proíbe nome de concorrente) |
| **Preço e condições** | | | | | |
| Preço com parcelas e condições completas, sem esconder matrícula | FALHA (E8, variante V-P) | OK (sem preço) | FALHA (E16, P5) | OK (sem preço) | OK (sem preço) |
| Bolsa e desconto com regra | OK (nenhum) | OK (nenhum) | OK (nenhum) | OK (nenhum) | OK (nenhum) |
| Urgência real, com data | OK | OK | OK | OK | OK (E20 preventivo) |
| Prouni, Fies ou financiamento | N/A | N/A | N/A | N/A | N/A |
| **Pessoas e dados** | | | | | |
| Autorização de imagem e voz registrada | OK (sem pessoas; opção B só com autorização) | N/A | OK (coordenação, decisões 8 e 10; ok dela e foto [CONFIRMAR]) | PENDENTE (voz do narrador e acervo) | FALHA até E25 (egresso); PENDENTE (apresentador e convidados de fora) |
| Menores só com autorização | OK | N/A | OK | OK | OK (menor não participa) |
| Formulários com finalidade e política de privacidade | PENDENTE (página, E1) | PENDENTE (página, E1) | PENDENTE (página, E1) | PENDENTE (página, E1) | FALHA até E24 (caixa de perguntas); PENDENTE (página) |
| WhatsApp e e-mail só com consentimento e saída fácil | N/A | N/A | N/A | OK (contato iniciado pela pessoa) | OK (newsletter dentro do teto D16; WhatsApp só 1 a 1) |
| Nenhum dado pessoal na peça ou nos arquivos | OK | OK | OK | OK | OK (E24 protege a triagem) |
| **Plataformas** | | | | | |
| Políticas da Meta e do Google para educação | OK | OK | N/A | N/A | N/A (card 4:5 em remarketing só com AP-4) |
| Página de destino entrega o que a peça promete | FALHA (E1, fase 2) | FALHA (E1, P1) | FALHA (E1, P3 a P6) | FALHA (E1, versão B) | FALHA (E1, ep. 1, 2, 4 e 5) |
| **Anúncios (Meta e Google)** | | | | | |
| Sem característica pessoal de quem vê | OK | OK | N/A | N/A | N/A |
| Sem urgência falsa, contador, play falso ou imitação da interface | OK | OK | N/A | N/A | N/A |
| Sem pessoa pública ou parceria inexistente | OK | OK | N/A | N/A | N/A |
| Sem caixa alta excessiva, pontuação repetida ou símbolos | OK (conferir nas artes finais) | OK (só a sigla UFAPE) | N/A | N/A | N/A |
| Página carrega, sem domínio inesperado, com dados, contato e privacidade | PENDENTE (E1) | PENDENTE (E1) | N/A | N/A | N/A |
| Nada para driblar a análise | OK | OK | N/A | N/A | N/A |

**Resultado:** Aprovado ( )  Bloqueado (x) nos 5 arquivos.
**Itens bloqueados e o que precisa mudar:** E1, E8, E10, E14, E16, E19, E21 a E26, mais os ajustes E2 a E7, E9, E11 a E13, E15, E17, E18 e E20.
**Revisado por:** qa-de-marketing (agente). Humano: [CONFIRMAR, pessoa do marketing; a tabela de aprovação de contexto/ufape-geral.md está vazia].
**Data:** 28/10/2026.

---

## 5. Auditorias de departamento

### auditorias/11-midia-paga.md (criativos e Google)

| Item | C | G |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais justificados | OK (cmo-pos, OA4; seção 5) | OK |
| Metas de CPL e custo por matrícula escritas antes de subir | OK (R$ 4,00, R$ 10,00 e R$ 18,00 ilustrativos; R$ 133,33) | OK |
| Verba dentro do valor aprovado, com aprovador registrado | PENDENTE (aprovador [CONFIRMAR]; G real [DADO NÃO FORNECIDO]) | PENDENTE (idem; E12 na conta) |
| Nomenclatura padrão | OK | OK |
| UTMs completas e origem chegando ao CRM | PENDENTE (E3; teste de rastreio de 30/10) | PENDENTE (E3; P6) |
| Pixel, API de Conversões e conversões do Google testados | PENDENTE | PENDENTE (P6) |
| Criativos aprovados em conformidade-educacional | FALHA (seção 4) | FALHA (seção 4) |
| Anúncios dentro das políticas | OK | OK |
| Nenhum público com menos de 18 anos | OK [SUPOSIÇÃO: o anuncios-meta confere] | OK (18 anos ou mais) |
| Post de docente promovido com autorização | N/A (C4 de reserva) | N/A |
| Relatório semanal ao CMO | N/A (começa com a veiculação) | N/A |
| Sem segmentação discriminatória | OK | OK |
| Públicos sem dados pessoais sem base legal | OK | OK (sem lista de contatos) |
| Dados de curso conferidos no catálogo | OK | OK (E5) |
| Destino de WhatsApp oficial com atendimento | N/A | N/A (extensão de chamada desligada) |
| Números só das exportações | OK | OK (marcados [DADO NÃO FORNECIDO]) |
| Nenhuma alteração sem humano | OK | OK |

### auditorias/05-social.md (posts)

| Item | Resultado |
|---|---|
| Frequência segue o plano | OK (6 posts, 2 feed e 4 Stories, 03/11 a 19/01; conferência slot a slot pendente, E23) |
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
| Gancho de 3 segundos funciona sem som e é cumprido | OK | OK (cortes com título na tela) |
| Legenda revisada em todo vídeo | PENDENTE (revisão na edição) | PENDENTE (SRT revisado previsto) |
| Autorização de imagem, voz e depoimento | PENDENTE (narrador) | FALHA até E25; PENDENTE (apresentador, convidados) |
| Título, capa e descrição não prometem além do conteúdo | OK | OK |
| Sem promessa de emprego ou urgência falsa | OK | OK |
| Dados de curso batem com o catálogo | OK | OK (D-D) |
| Cadência cabe na capacidade do time | PENDENTE (V1, capacidade [CONFIRMAR]) | FALHA até E26 |
| Métricas de retenção, conversa e clique | OK | OK |

---

## 6. Conferências feitas e sem achado

- **Frase da regra do 3º módulo:** igual, palavra por palavra, à regra 6 do cmo-pos com as datas da ficha, em F2-A e F2-B (arte, locução e legenda), P3 a P6 (chamada e legenda), versão B do tiktok (2 cards, locução e legenda) e ep. 1, 2, 4 e 5 do podcast (descrição, fechamento, card 4:5, Story 2 e legendas dos cortes). A data do 3º módulo não aparece fora da frase em nenhuma peça.
- **Coerência de datas entre as peças:** início 07/11/2026; módulos 1, 2 e 3 em 07 e 08/11/2026, 19 e 20/12/2026 e 23 e 24/01/2027; presenciais 6 (17 e 18/04/2027), 13 (27 e 28/11/2027) e 21 (julho de 2028); fase 1 até 06/11, 23h59; fase 2 de 07/11/2026 a 22/01/2027, 23h59; sem peça em 02/11, 20 e 21/11, 25/12 e 01/01. Tudo bate com a ficha e com o cmo-pos. Os dias da semana de todas as datas citadas estão certos (conferidos a partir de 28/10/2026, quarta). As únicas incoerências são E7 (módulo 2), E22 (cortes do ep. 3 sem data) e E23 (grade de feed).
- **Nome do curso:** "Pós-graduação em Gastroenterologia Veterinária" inteiro em todas as peças; "pós" sozinho só como termo genérico em pergunta (podcast) e "gastro vet" só como palavra-chave do Google, nunca em texto visível.
- **Certificação, "últimas vagas", bolsa, emprego:** nenhuma ocorrência em texto de peça; as palavras só aparecem nas listas de proibição.
- **Docentes:** Esp. Maria Carolina Pappalardo, Dr. Rodolfo Oliveira Leal, Dra. Cibele Figueira Carvalho e DR. Fabrizio Grandi (Dr., pela D-E) com nome e titulação da ficha; nenhuma opinião clínica escrita na voz deles (o problema de voz está só no E21, que é regra institucional).
- **Contagens do Google:** todas certas (ver seção 1).
- **Contas de verba do Google (seção 9.2):** 87 dias, 80 equivalentes, R$ 962,50 do Google e R$ 1.037,50 da Meta com G = 0, soma R$ 2.000,00: certas.
- **Dados pessoais:** nenhum; os telefones citados são os oficiais de contexto/ufape-geral.md.
- **"Agência":** nenhuma ocorrência nas 5 peças.
- **Travessão e meia-risca:** nenhuma ocorrência encontrada na leitura integral das 5 peças. Limitação: a conferência foi por leitura, sem busca automática de caracteres nesta sessão; o orquestrador roda a busca dos dois caracteres nos 5 arquivos antes de reenviar ao qa (o criativos pede isso na seção 8.3). O "·" do selo do tiktok e o "|" das capas do podcast não são travessão.

## 7. Observações que não bloqueiam

- Google, títulos "Especialização em Cães e Gatos" (area1 3 e area2 15): sozinhos, podem soar como nome de outro curso; a descrição 1 fixada resolve. Se o anuncios-google quiser trocar, uma opção é "Para cães e gatos" com outro título de área [SUPOSIÇÃO].
- tiktok, legenda da versão B: começa direto pela frase da regra. Para ficar igual aos criativos (gancho curto antes da frase), pode abrir com "Cinco módulos online, depois a prática." e trazer a frase na linha seguinte.
- Google, local "estado de São Paulo" (EM6, [SUPOSIÇÃO]): a persona secundária é quem viaja de outro estado; vale ler os termos de busca de fora de SP na revisão semanal.
- Posts P6 e Story de estreia do ep. 5 no mesmo dia (19/01): cabem, mas o posts-sociais confere a sequência de Stories.

---

## Fatos (com fonte)

- 68606: Pós-graduação em Gastroenterologia Veterinária, São Paulo, semipresencial, início 07/11/2026, turma IX, 500 h, "30x de R$ 1.180,00; R$ 35.400,00 no cartão ou boleto; matrícula R$ 250,00", status "aberto" (contexto/catalogo-de-cursos.md, seção 2).
- O catálogo indica a ficha como fonte do cronograma, da coordenação e das condições (contexto/catalogo-de-cursos.md, cabeçalho).
- Cronograma, presenciais 6, 13 e 21, coordenação, 38 nomes listados, "1ª mensalidade deverá ser paga até 30 dias de antecedência da data de seu início", "Turma mínima de 20 alunos" e a frase ligada ao MEC na página (ficha 68606).
- Decisões 8, 10, 11, 14, 16, 18, 21, 22 e 23 (docs/execucao-2026-10-26.md).
- Regras 4, 5, 6, 7, 9 e 11, OA4, OA9 a OA12, OU3, OU6 e OU8, seção 5 dos canais (cmo-pos-2026-10-26.md, versão 4).
- Episódio 3 sem chamada de turma e calendário do podcast (cmo-pos-2026-10-28-apresentacao-68606.md, slides 13 a 15).
- Contatos oficiais e instabilidade do WhatsApp em 22/10/2026; tabela de aprovação vazia (contexto/ufape-geral.md).
- Toda peça com preço mostra parcelas, valor da parcela, total e matrícula; exceção de divulgação de turma iniciada até a véspera do 3º módulo, com a regra completa (contexto/pos-graduacao.md).

## [SUPOSIÇÃO]

- Os ganchos A6 citados nas peças batem com o original do criador-de-ganchos-pos (conferidos só pela citação do slide 8 da apresentação).
- Ajuste de caixa da titulação permitido (D-E).
- Datas sugeridas para os cortes 2 e 3 do ep. 3 (29/12 e 08/01).
- Pedido de pausa ao gestor quando G passar de R$ 1.794,29 (E12).
- Público de 18 anos ou mais também no gerenciador da Meta (a conferir pelo anuncios-meta).

## [CONFIRMAR]

- A13, A7 e A12 na página da 68606, ou decisão da regulação sobre publicar antes de A7 e A12 (E1).
- OU8: pagamento da 1ª mensalidade de quem entra depois do início (E8 e E16). OU3 e OU6 seguem abertas; nenhuma peça promete reposição.
- Exceção `pos_conteudo_<AAAAMM>` com o arquiteto-de-fluxos (D-A, E22).
- Nome real e mês de subida das campanhas Meta e Google da 68606 (exportação D6) (E3).
- Preferência da pessoa do marketing entre "matrícula" e "inscrição" (D-C); se mudar, muda em todas as peças e no catálogo.
- WhatsApp de vendas funcionando e horário de atendimento (E19).
- Termo do egresso e aprovação de depoimento (E25); equipe e capacidade do podcast (E26); formulário com política de privacidade (E24).
- Ok da Esp. Maria Carolina Pappalardo para o P3 e foto aprovada; voz do narrador do tiktok.
- Quem aprova cada tipo de peça (tabela de contexto/ufape-geral.md vazia; até lá, a pessoa do marketing).

## Fontes

- /home/user/marketing-ufape/contexto/ufape-geral.md
- /home/user/marketing-ufape/contexto/pos-graduacao.md
- /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md, /home/user/marketing-ufape/auditorias/11-midia-paga.md, /home/user/marketing-ufape/auditorias/05-social.md, /home/user/marketing-ufape/auditorias/12-video-e-audio.md
- As 5 peças revisadas (cabeçalho).
- Externas: nenhuma.

**Próximo passo:** cada arquivo volta ao seu agente com os achados dele (criativos-de-anuncio: E3, E4, E7 a E9; anuncios-google: E3, E5, E10 a E12; posts-sociais: E13 a E17; tiktok: E2, E18, E19; podcast: E2, E5, E6, E20 a E26). E1 é pedido à Ufape (OA10). Depois das correções, as 5 peças voltam ao qa-de-marketing antes da aprovação humana.
