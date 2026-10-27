# QA da montagem das campanhas das turmas de Pós de março e abril de 2027 (Meta v3 e Google v3)

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026
- **Peças revisadas:**
  - /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-meta-pos-2026-10-26.md (versão 3, 1.057 linhas)
  - /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-google-pos-2026-10-26.md (versão 3, 797 linhas)
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md e .claude/agents/qa-de-marketing.md
  - docs/execucao-2026-10-26.md (decisões 1 a 17)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12, em especial 12.6 e 12.7 com D11 e D12; seção 13, que trata do teto de mensagens e não afeta a mídia paga)
  - saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 4 aprovada: seções 3.1 a 3.8 e 4.1 a 4.5)
  - saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (versão 5 aprovada, citada pelas duas peças; os números conferidos aqui são os que a estratégia v4 copia dele)
  - saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md (versão 3 aprovada: seções 0 a 3, as 14 seções de turma, 18 e 19)
  - auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md
  - contexto/catalogo-de-cursos.md (seção 2, as 14 turmas), contexto/pos-graduacao.md e contexto/ufape-geral.md (regras de aprovação)
  - Ficha contexto/cursos/pos/68632-pos-graduacao-em-clinica-cirurgica-de-caes-e-gatos.md (conferência pontual de "1ª mensalidade 30 dias antes" e "um por mês")
- **Scripts (só leitura, nenhum arquivo do repositório alterado):** /tmp/claude-0/-home-user/266c34a1-9b23-5a3e-bf6a-85e9f1184970/scratchpad/qa-campanhas-pos/conta_meta.py, conta_google.py e confere_nomes.py, na mesma pasta.
- **Dados pessoais:** nenhum. Nenhum aluno, candidato ou lead aparece nas peças nem nesta revisão.
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web.

---

## 0. Vereditos

| Arquivo | Veredito | Motivo em uma linha |
|---|---|---|
| anuncios-meta-pos v3 | **Corrigir** (1 item obrigatório, M1) | Verba, diárias, nomes, UTM, URLs e travas batem com a estratégia v4 e o criativos v3; falta deixar escrito que o teto de R$ 2.000,00 prevalece sobre a "conversão protegida" quando o gasto anterior de 289 ou 662 passar do que o aquecimento e a manutenção absorvem |
| anuncios-google-pos v3 | **Corrigir** (7 itens obrigatórios, G1 a G7) | Contagens dentro dos limites e verba certa, mas a frase de transparência não é a aprovada, a trava das páginas com frase do MEC não acompanha a Meta, a mesma regra do teto falta, há regras de plataforma sem [SUPOSIÇÃO], a pausa no corte não tem pedido formal e a divergência de nome com o D12 não está registrada |

Nenhuma das duas peças falha em item da auditoria de conformidade educacional no texto de anúncio. Os vereditos "corrigir" vêm da verba (critério 2), da coerência entre canais e travas (critérios 3 e 5) e da marcação de regras de plataforma (critério 6). Depois das correções, as duas peças voltam a este agente só para a reconferência dos itens M1 e G1 a G7; o resto está conferido.

---

## 1. Recontagem por script (critério 1)

### 1.1 Google (anuncios-google v3)

O cabeçalho do arquivo (linha 27) diz que todas as contagens foram feitas à mão, sem script. Recontei com conta_google.py:

- **99 itens com contagem declarada** no arquivo inteiro (tabelas 8.2, 8.4, 8.5, 8.6, 8.7, 9 e seção 18): todas as contagens declaradas batem. A única diferença é de fórmula, não de peça: a linha 375 diz que " Início em dd/mm/aaaa." tem 23 caracteres; tem 22 com o espaço inicial. As DS1 reais (tabela 8.6) estão todas certas.
- **290 títulos e descrições montados**, turma por turma, pela ordem das seções 8.4 e 8.5 (texto A e texto B dos 14 anúncios, com as exceções de 68632, 662, 68636, 679, 366 e 657): **nenhum título passa de 30 e nenhuma descrição passa de 90.**
  - Maior título: "Para anestesistas já atuantes" (29, 657).
  - Maiores descrições: DS1 de 68632 e de 366 (86 cada) e DT (86).
- **Recursos:** frases de destaque (maior 23, "Corpo docente na página"), sitelinks (maior 23, "Todas as pós-graduações"), 26 valores de snippet (maior 24, "Bloqueios locorregionais" e "Avaliação pré-anestésica") e 14 caminhos de exibição (maior 14, "anestesiologia", "clinica-medica" e "endocrinologia"): todos dentro de 25, 25, 25 e 15.
- **Seção 18 (suspensa):** 34 itens com contagem declarada, todos certos; maior título "Prova 27/11: Patologia Clínica" (30, no limite) e maior descrição 87.
- **Nenhum item passa do limite.** Lista dos que passam: vazia.

Contas de apoio para as correções: a frase aprovada do r2 (criativos 1.2, AP8) "A turma pode não ser formada: compre passagem e hotel só depois de a turma ser confirmada." tem **90** caracteres e cabe na descrição. A DS1 de 68632 com "Início em 10/04/2027." tem 89 e também cabe.

### 1.2 Meta (anuncios-meta v3)

O arquivo Meta fixa três limites: título até 40, descrição até 30 (criativos 1.3 e seção 13.6 do próprio arquivo, [SUPOSIÇÃO] de plataforma) e primeira linha do texto principal até cerca de 125 caracteres (linha 305). Como o texto de cada anúncio de turma é o do criativos v3 (linha 302), recontei os textos do criativos v3 com conta_meta.py:

- **69 títulos** (70 peças menos o c3 de 662, sem texto): nenhum passa de 40. Maior: "Mês a mês na Anestesiologia Avançada" (36) e "Quem ensina Anestesiologia Avançada" (35).
- **69 descrições:** nenhuma passa de 30.
- **70 primeiras linhas:** nenhuma passa de 125. Maior: 117, do 366-r2, como a linha 305 do Meta afirma.
- **Seção 13 (suspensa):** 80 itens contados; títulos e descrições dentro de 40 e 30. Uma primeira frase passa de 125: texto 4 de C4 (linha 830, 173 caracteres), já registrado pelo próprio arquivo (linha 833) e suspenso.
- **Lista dos que passam:** na parte ativa, nenhum. Na parte suspensa, só o texto 4 de C4 (linha 830).

Achado só de registro, sem efeito nas peças revisadas: 12 contagens declaradas no criativos v3 estão erradas por 1 caractere (11 títulos e 1 descrição; por exemplo "Só 6 presenciais em 24 módulos", declarado 29, tem 30; "Infectologia não é só antibiótico", declarado 34, tem 33). Nenhuma passa do limite. Fica como nota ao criativos-de-anuncio; o Meta não repete essas contagens.

---

## 2. Verba e diárias (critério 2)

Conferido com script contra as tabelas 3.3, 3.4 e 3.6 da estratégia v4:

| Item | Meta v3 | Google v3 | Estratégia v4 | Situação |
|---|---|---|---|---|
| Março por turma | frio R$ 787,00 + remarketing R$ 508,00 = R$ 1.295,00 | R$ 705,00 | R$ 2.000,00 | Bate. Soma Meta e Google = R$ 2.000,00, sem passar |
| Abril por turma | frio R$ 865,00 + remarketing R$ 460,00 = R$ 1.325,00 | R$ 675,00 | R$ 2.000,00 | Bate. Soma = R$ 2.000,00 |
| Total das 14 turmas | R$ 18.400,00 | R$ 9.600,00 | R$ 28.000,00 | Bate |
| Diárias por fase (11 linhas de fase) | todas iguais à 3.3 e à 3.4, arredondadas para baixo | todas iguais | - | Bate (por semana = total x 7 / dias; diária = piso de total / dias) |
| Dias das fases | 14, 7, 14, 46, 53, 39, 19, 39, 46, 53 e 60 | idem | idem | Conferidos no calendário |
| Limite de volume (3.6) | frio 2 x semana / 3; remarketing = semana | Google = semana | idem | Bate nas 11 linhas |
| EM14 (remarketing para o frio) | 10 diárias recalculadas | não se aplica | - | Contas certas (ex.: R$ 845,00 / 46 = R$ 18,36) |
| 289 e 662 | limite de R$ 500,00 até a véspera (06/12 e 05/01); A = R$ 500,00 menos G; frio 56%, remarketing 14% | Google 30% de A | 3.8 | Bate |

**Ponto que impede o "corrigido" (M1 e G3):** as duas peças escrevem que a conversão de 289 e de 662 nunca é tocada pelo gasto anterior e, para o caso de o gasto passar do que o aquecimento e a manutenção absorvem (662 acima de R$ 500,00; 289 acima de R$ 700,00), só mandam aviso ao gestor e ao cmo. Lido ao pé da letra, esse caminho soma mais de R$ 2.000,00 na turma (por exemplo, 662 com G = R$ 600,00 e conversão intacta de R$ 1.500,00 dá R$ 2.100,00). A regra do teto (Meta seção 9, linha 559; Google seção 12, linha 486) segura o gasto, mas o texto se contradiz. Correção na seção 6.

---

## 3. Detalhes do anuncios-meta-pos v3

### 3.1 Correção obrigatória

| # | Linha | Problema | Correção |
|---|---|---|---|
| M1 | 476, 485, 497 e 498 (seção 7) | "Conversão protegida" sem limite: se o gasto anterior de 662 passar de R$ 500,00, ou o de 289 passar de R$ 700,00, a linha 498 diz que "a conversão continua protegida", o que permite passar de R$ 2.000,00 na turma (critério 2 e decisão 15) | Escrever na 7.3 e na 7.1: "O teto de R$ 2.000,00 por turma (decisão 15) prevalece sobre a conversão protegida. Se o gasto anterior passar do que o aquecimento (662) ou o aquecimento e a manutenção (289) absorvem, o excesso sai da conversão da mesma turma, na mesma divisão por canal (frio 60%, remarketing 40% da parte Meta; Google na mesma proporção da 3.3 e 3.4), em nova versão escrita antes de 04/01 (289) ou 25/01 (662), com aviso ao gestor e ao cmo; até lá vale a pausa pelo teto da seção 9." Manter o [CONFIRMAR o caminho com o gestor] e anotar que a estratégia v4 (3.8) não escreve este caso. |

### 3.2 O que foi conferido e está certo

- **Textos (critério 3):** o arquivo não reescreve texto; cada anúncio usa o texto da peça de mesmo nome do criativos v3 (linha 302). Os 98 nomes da tabela 6.2 (70 anúncios e 28 artes 9:16 anexas) são idênticos aos 98 nomes v1 do criativos v3, sem sobra nem falta (confere_nomes.py). Varredura dos textos aprovados (texto principal, título, roteiro, cartões e arte das seções 4 a 17 do criativos): sem preço, valor de matrícula ou inscrição, "inscrição", bolsa, prova, MEC, certificação, urgência ou turma mínima com número. A única menção a matrícula é a frase sem valor do AP7, só no remarketing, com as 4 condições (linha 44 e S7).
- **Nome do curso:** "Pós-graduação em <área>" como no catálogo nas 14 linhas da tabela 3.2; datas, campus e status batem com o catálogo, seção 2 (679 com 03/04/2027, 68636 com 17/04/2027 "só no site" e [CONFIRMAR], 366 e 662 pela planilha).
- **UTM e nomes (critério 4):** 28 campanhas da tabela 3.2 iguais às 28 do criativos v3 e às 28 utm_campaign da 6.3; 70 linhas de parâmetros com `utm_source=meta`, `utm_medium=paid_social`, utm_content igual ao nome do anúncio e utm_term igual ao público; AAAAMM 202612 em março e 202701 em abril; URLs iguais às do criativos v3 e às do Google.
- **Travas (critério 5):** P3 de 679, 68636 e 662; c3 de 662; P4 de 366; U10 de 657; PP7 de 657 e 341 (com PR7 e AP11); URL de 68617; páginas com frase ligada ao MEC só com decisão registrada ou página corrigida (linha 534 e S8); campanhas antigas pausadas seguem pausadas. Todas iguais às da seção 18 do criativos v3 (AP9 a AP13).
- **Pedidos (critério 6):** AMP13 a AMP24 no formato o que, por que, quanto, efeito e como desfazer; execução só por humano (linhas 8, 55 e 616). Regras de recurso e de política da Meta sem fonte estão marcadas [SUPOSIÇÃO] (seção 4.1 e Lista 2, linha 1032).
- **Travessão e meia-risca (critério 7):** U+2014 e U+2013: zero ocorrências.

### 3.3 Recomendações (não bloqueiam)

- **R1, seção 13 (linhas 637 a 936):** a montagem suspensa das provas guarda textos com "Inscrição de R$ 100,00", bolsa, "Inscreva-se" e uma primeira frase de 173 caracteres. Está marcada "Não executar" e cumpre a decisão 14 (nada novo foi produzido). Para ninguém montar por engano, mover a seção para um arquivo de arquivo morto ou deixar o aviso "suspenso, não executar" também no título de cada subseção. Qualquer retomada passa de novo por este agente.
- **R2, linha 57 e AMP13:** a pergunta ao cmo sobre a chave com área curta está certa e deve sair antes de 30/11 (ver seção 5).

---

## 4. Detalhes do anuncios-google-pos v3

### 4.1 Correções obrigatórias

| # | Linha | Problema | Correção |
|---|---|---|---|
| G1 | 344, 402, 547 (AGP20) e 774 | A descrição DT "A turma pode não ser formada: compre passagem e hotel só depois de ela ser confirmada." não é a frase do AP8 do criativos v3. A justificativa ("a versão aprovada tem 90 e ficaria no limite") não se sustenta: 90 cabe no limite de 90, e o AGP20 pede a "mesma aprovação do AP8" para um texto diferente (critério 3) | Usar a frase do AP8 sem mudar nada: "A turma pode não ser formada: compre passagem e hotel só depois de a turma ser confirmada." (90 caracteres, contado por script). Atualizar a tabela 8.4 (DT, 90), a nota da 8.8, o AGP20 e retirar a suposição da linha 774 |
| G2 | 469 (trava "Páginas com CERTIFICADO PELO MEC") e 520 (S6) | A Meta só sobe para página com a frase ligada ao MEC com decisão registrada da pessoa do marketing ou com a página corrigida (Meta linha 534 e S8). O Google deixa subir com "anúncio sem frase de certificação". As mesmas 14 páginas ficariam liberadas num canal e travadas no outro (critério 5; conformidade, "página de destino entrega exatamente o que o anúncio prometeu") | Na coluna "O que fica valendo até lá" da linha 469, escrever "a campanha da turma só sobe com decisão registrada da pessoa do marketing ou com a página corrigida (igual ao S8 do anuncios-meta)"; acrescentar o mesmo item ao S6 e ao AGP22 |
| G3 | 135, 150 e 151 (seção 4.3) | Mesmo problema do M1: "A conversão ... nunca é tocada pelo gasto anterior", sem dizer que o teto de R$ 2.000,00 prevalece. Falta também a fórmula do excesso de 289 na manutenção para a parte Google (a linha 135 diz "recalculada pelo saldo", mas a 4.3 não diz como) | Acrescentar na 4.3: "Excesso de 289 (E = G menos R$ 500,00): manutenção nova = R$ 200,00 menos E; o Google fica com 50% dela, dividido por 14 dias, arredondado para baixo (mesma regra do anuncios-meta, 7.3)" e o mesmo texto do M1 sobre o teto prevalecer |
| G4 | 75, 200, 201, 285 e 419 | Regras de plataforma sem fonte e sem [SUPOSIÇÃO] (critério 6): conversão secundária "sem entrar no lance" (75); "Rotação: Otimizar (padrão dos responsivos)" (200); ajuste de demografia de 18 anos ou mais na Busca (201); "o limite é 15 e 4" títulos e descrições (285); snippet "até 25 caracteres, de 3 a 10 por conjunto" (419). O cabeçalho (linha 27) só cobre título, descrição, frase de destaque, sitelink e caminho | Marcar cada uma com [SUPOSIÇÃO de plataforma; conferir no editor] e incluir as cinco na Lista 2 (linha 765) |
| G5 | 354 e 775 | O arquivo deixa para o qa a escolha de 662 ficar com 1 anúncio por grupo. Decisão do qa: A e B de 662 têm os mesmos 8 títulos em outra ordem e as mesmas 3 descrições, então não são dois anúncios diferentes | 662 sobe com 1 anúncio por grupo (texto A: `rsa-662-area-a_v1` e `rsa-662-marca-a_v1`) até a ficha ser corrigida; o texto B de 662 só entra em nova versão, com conteúdo liberado. Registrar na 8.5, na tabela 8.1 e na Lista 2. O limite da 4.5 para 662 passa a ser o de 1 anúncio (dobra), como a própria escada prevê |
| G6 | 537 a 550 (seção 15) | A pausa no dia seguinte ao corte e a pausa pelo teto de R$ 2.000,00 aparecem na 4.2, na 12 e na 13, mas não têm pedido formal com quanto, efeito e como desfazer (o Meta tem o AMP16) (critério 6) | Acrescentar o AGP24: "Pausa da campanha de Busca de cada turma no dia seguinte ao corte (12/02, 19/02, 26/02, 05/03, 12/03, 19/03 e 26/03), ou antes se o gasto do ciclo da turma (Meta e Google) chegar a R$ 2.000,00 (EM16); por quê: fim do ciclo e teto do CEO; quanto: sem gasto novo; efeito: nenhum gasto depois do corte nem acima da verba; como desfazer: reativar só com verba nova aprovada" |
| G7 | 56, 565, 606 e 753 | A chave com área curta (`pos_<código>-<área curta>`) e o nome do anúncio `rsa-<código>-<grupo>-<a ou b>_v1` divergem da letra do D12 (seção 5), mas o arquivo marca a nomenclatura como "Atendido no desenho" sem levar a pergunta ao cmo, ao contrário do anuncios-meta (linha 57 e AMP13) | Na regra "Nomes" (linha 56) e no AGP12, acrescentar "[CONFIRMAR com o cmo que a chave com área curta e o nome do anúncio responsivo cumprem o D12]"; na auditoria (linha 565), "Atendido no desenho, pendente a confirmação do cmo" |

### 4.2 O que foi conferido e está certo

- **Contagens (critério 1):** seção 1.1 desta revisão; nenhum item acima do limite.
- **Verba (critério 2):** seção 2 desta revisão; 289 e 662 com o limite de R$ 500,00, o recálculo de 30/11 e 30/12 e a parte Google de 30% do aquecimento novo.
- **Textos (critério 3):** o Google não tem peça própria no criativos v3 (o criativos deixa a Busca para o anuncios-google, seção 19). Os textos usam só fatos das fichas que o criativos v3 também usa: carga horária, número de módulos, contagem de presenciais (289, 333, 657 e 68636 com 6; 68635 e 366 com 9; 68628 com 8; 679 com 3; 68617 com 2), "um por mês" de 68632, "Aulas presenciais não são transmitidas" só em 68632 (fora de 68636 e 68609, como no criativos 1.2), "Para médicos veterinários anestesistas já atuantes" em 657, sem número de turma em 68628, 68617 e 662, sem data em 679, 68636 e 366, 662 só com nome, campus e data. "Docentes listados na página" só nas 8 turmas que têm o c3 de docentes. Sem preço, valor de matrícula ou inscrição, "inscrição", bolsa, prova, MEC, certificação, desconto, promoção (341), urgência ou turma mínima com número. Coerente com o Meta.
- **Nome do curso:** a descrição fixada na posição 1 (DS1) traz "Pós-graduação em <área>" completo nas 14 turmas, igual ao catálogo; os títulos com forma curta (68635, 68617, 68632 e 366) são trechos do nome do catálogo, sem outro nome de curso. Isso só vale com a fixação da DS1 (AGP18): se o AGP18 não for aprovado, as formas curtas saem dos títulos (regra de contexto/pos-graduacao.md, linha 25).
- **UTM (critério 4):** 14 campanhas com a chave da estratégia 4.2, AAAAMM certo por onda; sufixo com `utm_source=google`, `utm_medium=cpc`, utm_campaign igual ao nome, utm_content igual ao nome do anúncio e `utm_term={keyword}` (D11, D12 e estratégia 4.3); URLs iguais às do Meta e do criativos v3.
- **Travas (critério 5):** rastreio de 30/10, P3 de 679, 68636 e 662, P4 de 366, U10 e PP7 de 657, PP7 e PR7 de 341, URL de 68617, P5 de 68628, limite de 289, PP6 de 68615 e 333. Falta só a das páginas com frase do MEC (G2).
- **Pedidos (critério 6):** AGP12 a AGP23 no formato completo; execução só por humano. Falta o da pausa (G6).
- **Travessão e meia-risca (critério 7):** zero ocorrências.

### 4.3 Recomendações (não bloqueiam)

- **R3, linha 389:** a DS1 de 68632 cabe com "Início em 10/04/2027." (89 caracteres). Usar a forma padrão das outras turmas.
- **R4, linhas 261 e 427:** 68628 nega "eletroquimioterapia" (para não disputar com o curso livre 560) e mostra "Eletroquimioterapia" no snippet. Não é erro de política, mas é incoerente: ou o snippet troca o valor, ou a negativa vira exata para o nome do curso livre.
- **R5, linhas 458 e 459:** quem libera a P3 de 679 e 68636 está "Ufape e cmo" no Google e "Ufape ou cmo" no Meta (linhas 522 e 523). Alinhar os dois arquivos; até lá vale a leitura mais restrita (Ufape e cmo).
- **R6, linha 27:** trocar "sem script" por "recontado por script pelo qa-de-marketing em 27/10/2026 (saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-campanhas.md)".
- **R7, seção 18:** mesma recomendação do R1 para os textos suspensos das provas.

---

## 5. Chave da campanha e D12 (critério 4)

- **O que o D12 diz** (cmo-geral, 12.7): todo utm_campaign começa pela chave `<linha>_<código do catálogo>` (exemplo `pos_68615`); no pago, nome da campanha = chave + `_<plataforma>_<objetivo>_<público>_<AAAAMM>` "(seção 4.2 da estrategia-de-midia-pos)"; anúncio = `<código ou conceito>_<formato>_<gancho>_vN`; hífen dentro do bloco e sublinhado entre blocos.
- **O que as peças usam:** `pos_<código>-<área curta>` (por exemplo `pos_68615-patclin_meta_lead_amplo18-sp_202612`), igual à estratégia v4 (4.2) e ao criativos v3, nas 14 turmas e nos dois canais (conferido por script: nenhuma chave diferente da lista de áreas curtas da 4.2).
- **Há conflito?** Não há conflito de leitura: todo utm_campaign continua começando por `pos_<código>`, nenhum código das 14 turmas é prefixo de outro, e o próprio D12 manda seguir a seção 4.2 da estratégia, que é a que define a área curta. **Há divergência de forma** com a letra do D12: (a) o segundo bloco entre sublinhados vira `68615-patclin` e não `68615`; (b) no CRM, na newsletter e no orgânico a mesma turma usa `pos_68615_<AAAAMM>`, então quem separar por sublinhado lê blocos diferentes para a mesma turma; (c) no Google, o nome do anúncio `rsa-<código>-<grupo>-<a ou b>_v1` não tem os blocos de formato e gancho do D12.
- **O que fazer:** não bloqueia a revisão. O cmo ratifica a chave com área curta e o nome do anúncio responsivo antes de 30/11 (AMP13 do Meta; AGP12 do Google depois do G7), e a analise-de-midia lê a turma pela expressão `^pos_<código>[-_]`, que junta pago, CRM e orgânico. Se o cmo não ratificar, a troca tem de ser feita antes da subida de 07/12, porque depois o D12 proíbe renomear campanha no ar.

---

## 6. Auditorias, item por item

### 6.1 auditorias/11-midia-paga.md

| Item | Meta v3 | Google v3 |
|---|---|---|
| Plano do gestor-de-midia aprovado, com canais ativados e fora justificados | Pendente externo (PP16) | Pendente externo (PP16) |
| Metas de CPL e custo por matrícula escritas antes de subir | Atende (linha 43) | Atende (seção 2) |
| Verba dentro do valor aprovado, com aprovador registrado | Corrigir M1; aprovador [CONFIRMAR] | Corrigir G3; aprovador [CONFIRMAR] |
| Nomenclatura padrão | Atende no desenho, com [CONFIRMAR cmo] | Corrigir G7 (registrar a pergunta ao cmo) |
| UTMs completas e origem chegando ao CRM | Completas; chegada ao CRM pendente do teste de 30/10 | Completas; idem |
| Pixel, API de Conversões e conversões do Google | Pendente externo (30/10) | Pendente externo (30/10) |
| Criativos aprovados na conformidade | Atende (textos do criativos v3) | Atende no texto; corrigir G1 |
| Anúncios dentro das políticas de cada plataforma | Atende no desenho [SUPOSIÇÃO de política] | Atende no desenho; corrigir G4 (marcação) |
| Nenhum público com menores de 18 anos | Atende | Atende [SUPOSIÇÃO de recurso, G4] |
| Post de docente promovido com autorização registrada | Atende (decisões 8 e 10; AP2 com o docente) | Não se aplica |
| Relatório semanal ao CMO | Pendente externo | Pendente externo |
| Sem segmentação discriminatória | Atende | Atende |
| Públicos sem dados pessoais sem base legal | Atende (nenhuma lista) | Atende |
| Dados de curso conferidos no catálogo | Atende | Atende |
| Destino de WhatsApp | Não se aplica | Não se aplica |
| Números só das exportações | Atende (nenhum número observado) | Atende |
| Nenhuma alteração sem humano executar e aprovar | Atende | Corrigir G6 (pausa sem pedido formal) |

### 6.2 auditorias/conformidade-educacional.md (texto dos anúncios das duas peças; páginas de destino como pendência externa)

| Item | Meta v3 | Google v3 |
|---|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | Atende | Atende (DS1 fixada; G1 e R3 não mudam dado) |
| Curso com status "aberto" | Atende (14 abertas) | Atende |
| Modalidade clara e correta (68632 presencial) | Atende | Atende (e negativa "semipresencial") |
| Graduação: ato regulatório | Não se aplica | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Atende | Atende |
| Curso livre sem equivalência | Não se aplica | Não se aplica |
| Nota MEC | Atende (nenhuma) | Atende (nenhuma) |
| Sem promessa de emprego, salário ou aprovação | Atende | Atende |
| Empregabilidade com fonte | Não se aplica | Não se aplica |
| Superlativos com fonte | Atende (nenhum) | Atende (nenhum) |
| Comparação com concorrente | Atende (nenhuma) | Atende (concorrente só como negativa) |
| Preço com condições completas | Atende (nenhum preço; frase do AP7 sem valor, só no remarketing) | Atende (nenhum preço) |
| Bolsa e desconto com regra | Atende (nenhum na parte ativa; 341 sem promoção) | Atende |
| Urgência real | Atende (só data de início da planilha) | Atende |
| Prouni, Fies ou financiamento | Não se aplica | Não se aplica |
| Autorização de uso de docentes | Atende (decisões 8 e 10) | Não se aplica (nenhum nome) |
| Menores de idade | Atende | Atende |
| Formulários com finalidade e política de privacidade | Pendente externo (cada página) | Pendente externo |
| WhatsApp e e-mail com consentimento | Não se aplica | Não se aplica |
| Nenhum dado pessoal | Atende | Atende |
| Políticas da Meta e do Google para educação | Atende no desenho [SUPOSIÇÃO] | Atende no desenho; G4 |
| Destino entrega o que o anúncio promete | Pendente externo (travas da seção 8) | Corrigir G2 (páginas com frase do MEC) |
| Sem característica pessoal de quem vê | Atende ("para anestesistas já atuantes" repete o público da página) | Atende (mesmo critério) |
| Sem escassez falsa, contador ou falsa interface | Atende | Atende |
| Sem pessoa pública ou parceria falsa | Atende | Atende |
| Sem caixa alta excessiva ou símbolos | Atende ("DR." e "DRA." seguem a ficha) | Atende (só a sigla UFAPE) |
| Página carrega, sem domínio inesperado, com contato e privacidade | Pendente externo | Pendente externo |
| Sem sugestão para driblar a análise | Atende (melhorias automáticas desligadas) | Atende |

**RESULTADO**
- anuncios-meta-pos v3: Aprovado ( )  Bloqueado (x) até M1.
- anuncios-google-pos v3: Aprovado ( )  Bloqueado (x) até G1 a G7.
- Itens bloqueados e o que precisa mudar: seções 3.1 e 4.1.
- Revisado por: qa-de-marketing (agente); humano: pessoa do marketing que aprovou o plano do cmo [CONFIRMAR nome].
- Data: 27/10/2026.

---

## 7. Próximo passo

As duas peças **voltam aos agentes que as produziram** (anuncios-meta para o M1; anuncios-google para G1 a G7). Depois, reconferência curta deste agente só nesses itens, e então a aprovação humana dos pedidos AMP13 a AMP24 e AGP12 a AGP24. Nada sobe, muda, pausa ou gasta antes disso. As recomendações R1 a R7 podem entrar na mesma versão.

---

## Lista 1. Fatos (com fonte)

- Verba de R$ 2.000,00 por turma de Pós no ciclo; meta de 15 matrículas; nenhuma peça cita valor de inscrição até U11; provas de bolsa e Livres fora desta rodada (docs/execucao-2026-10-26.md, decisões 14, 15 e 16).
- Meta R$ 1.295,00 e Google R$ 705,00 por turma em março; Meta R$ 1.325,00 e Google R$ 675,00 em abril; diárias, dias e limites de volume das tabelas 3.3, 3.4 e 3.6; regra de 289 e 662 da 3.8 (estrategia-de-midia-pos v4); conferidos por script.
- D11 (meta e paid_social; google e cpc) e D12 (chave `<linha>_<código>`, nome = utm_campaign, AAAAMM da subida, anúncio `<código ou conceito>_<formato>_<gancho>_vN`, campanhas no ar sem renomear) (cmo-geral, 12.7).
- Áreas curtas e padrão de nome com área (estrategia-de-midia-pos v4, 4.2); 98 nomes de anúncio e 28 campanhas Meta (criativos-de-anuncio-pos-turmas v3), iguais aos do anuncios-meta v3 (confere_nomes.py).
- Frase do r2 e do AP8 com 90 caracteres; frase do AP7 só no remarketing, com 4 condições (criativos v3, 1.2 e 18).
- Nome, campus, modalidade, CH, turma, início e status das 14 turmas (catálogo, seção 2).
- Todo curso da linha se chama "Pós-graduação em <área>" em anúncios (contexto/pos-graduacao.md, linha 25).
- Zero ocorrências de U+2014 e U+2013 nas duas peças (conta_meta.py).

## Lista 2. Suposições

- [SUPOSIÇÃO] Limites de 30 e 90 (Google) e de 40, 30 e cerca de 125 (Meta), como as próprias peças e o criativos v3 registram; o editor e o gerenciador são a conferência final.
- [SUPOSIÇÃO] A Busca mostra sempre a descrição fixada na posição 1; por isso aceito os títulos com forma curta do nome do curso só com a fixação da DS1 (AGP18).
- [SUPOSIÇÃO] Na correção M1 e G3, o excesso que sai da conversão segue a mesma divisão por canal da fase; o caminho final é do gestor e do cmo.
- [SUPOSIÇÃO] A leitura `^pos_<código>[-_]` pela analise-de-midia junta pago, CRM e orgânico sem colisão entre os 14 códigos (nenhum é prefixo de outro).
- [SUPOSIÇÃO] A varredura de palavras proibidas cobriu texto principal, título, descrição, roteiro, cartões e arte do criativos v3; o texto das artes e dos vídeos produzidos precisa da mesma conferência na prévia antes da subida.

## Lista 3. Dados que faltam

- [CONFIRMAR] Ratificação do cmo para a chave com área curta e o nome do anúncio responsivo (antes de 30/11).
- [CONFIRMAR] Caminho do gestor e do cmo quando o gasto anterior de 662 passar de R$ 500,00 ou o de 289 passar de R$ 700,00.
- [CONFIRMAR] Decisão registrada da pessoa do marketing (ou correção) sobre as páginas com "CERTIFICADO PELO MEC" (A7).
- [CONFIRMAR] Aprovação do AP7 e do AP8 pela pessoa do marketing; aprovador de "Anúncios e verba" em contexto/ufape-geral.md.
- [CONFIRMAR] Teste de rastreio de 30/10; mínimo diário de cada plataforma; política de privacidade e finalidade do formulário nas 14 páginas.
- [CONFIRMAR] Travas de 679, 68636, 662, 366, 657, 341 e 68617; quem libera a P3 (R5).
- [DADO NÃO FORNECIDO] Gasto e diária atuais de 289 e 662; volume e CPC das palavras-chave; nenhum número de desempenho existe nos arquivos.
