# TikTok Ads na Pós: decisão de ficar fora nesta rodada

- **Agente:** anuncios-tiktok (departamento 11 Mídia Paga)
- **Linha:** pos
- **Data:** 26/10/2026 (etapa 1.15 da camada 1)
- **Versão:** 2, corrigida após qa-de-marketing-geral-2026-10-26-loteD (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-loteD.md)
- **Status deste arquivo:** avaliação. O canal não foi ativado pelo gestor-de-midia; não há estrutura para montar. Nada sobe, nada é pago.
- **Entradas lidas:**
  - .claude/agents/anuncios-tiktok.md; .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - CLAUDE.md; docs/execucao-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12, em especial 12.6, 12.7 e 12.11)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-pos-2026-10-26.md (seção 4, linha 6)
  - contexto/catalogo-de-cursos.md; contexto/pos-graduacao.md
  - saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (seção 3, seção 4.1 e encomendas: "anuncios-tiktok: sem encomenda nesta rodada")
  - saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (canais fora; P5 só para o LinkedIn, EM8)
  - saidas/11-midia-paga/analise-de-midia-pos-2026-10-26.md (nenhuma campanha de TikTok na visão de campanhas)
  - saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-26.md (TikTok fora; nenhum Spark Ad)
  - saidas/05-social-e-comunidade/estrategia-social-pos-2026-10-26.md (TikTok fora, seção 1.3 e linha 6 da matriz)
  - auditorias/11-midia-paga.md

---

## Mudanças desta versão

- **TK-Q1:** o nome do desenho mínimo passa a seguir D12, com a chave só com o código: `pos_<código>_tiktok_lead_amplo18-<praça>_<AAAAMM>` (seção 4).
- **TK-Q2:** a referência "D8" para rastreio e evento de lead saiu (na seção 12 do cmo, D8 é a janela de silêncio). Agora aponta para o teste de rastreio de 31/10, PP4 e EM11 da estrategia-de-midia-pos (seção 2, T4 e lista de dados que faltam).
- A decisão (TikTok fora nesta rodada) não mudou.

---

## 1. Decisão

**TikTok Ads fica fora da Pós nesta rodada (trimestre de 27/10/2026 a 24/01/2027).** Este agente confirma a decisão do gestor-de-midia (seção 3) e não pede reabertura.

## 2. Fundamento

| # | Motivo | Fonte |
|---|---|---|
| 1 | Não há verba para o canal. A verba nova da Pós está toda dividida em P1 a P6, e a frente de testes (P5) é só do LinkedIn de 657 | gestor-de-midia-pos, 4.1; cmo, 12.6, EM8 |
| 2 | Não há perfil da Ufape no TikTok citado nos contextos nem quem produza vídeo nativo com frequência (referência da squad: 2 vídeos por semana) | estrategia-de-marketing-pos, seção 4; estrategia-social-pos, seção 1.3 |
| 3 | O rastreio não existe: pixel e API de eventos do TikTok não estão instalados, e o rastreio dos canais ativos (teste de rastreio de 31/10, PP4 e EM11 da estrategia-de-midia-pos) ainda está pendente. Um canal sem rastreio não produz leitura | gestor-de-midia-pos, checklist; auditorias/11-midia-paga.md |
| 4 | A persona da Pós (médico veterinário formado, 1 a 8 anos de formado) já é alcançada com o mesmo roteiro curto em Reels, e Shorts entra em teste condicionado. Presença dela no TikTok: [SUPOSIÇÃO] de baixa presença, sem dado da Ufape | contexto/pos-graduacao.md; estrategia-social-pos, matriz de canais; estrategia-de-marketing-pos |
| 5 | Ticket alto (de R$ 12.000,00 a R$ 48.780,00 no total) e decisão longa: no TikTok o criativo decide a entrega para público amplo, e sem histórico de conversão a otimização não tem do que aprender. A Meta, com o mesmo modelo de público amplo, já roda e tem pixel | catálogo; contexto da linha; skill estrutura-de-campanha-paga, passo 2 |
| 6 | Na ordem da estratégia, a Graduação é candidata ao TikTok antes da Pós | estrategia-de-marketing-pos, seção 4 |

Proporcionalidade: abrir um canal novo agora tiraria verba e horas das frentes com data (provas de 27/11 e turmas de março) para um teste que não teria rastreio nem criativo próprio.

## 3. O que faria o TikTok entrar (todas juntas)

| # | Condição | Quem confirma |
|---|---|---|
| T1 | Perfil da Ufape no TikTok criado e ativo, com quem publique e responda comentários [CONFIRMAR] | Ufape; estrategia-social |
| T2 | Inventário de pelo menos 3 vídeos verticais 9:16 da Pós, com som, legenda, gancho nos 2 primeiros segundos e áudio com direito de uso comercial (os roteiros curtos do kit e os Reels podem servir, se adaptados) [CONFIRMAR] | criativos-de-anuncio; tiktok |
| T3 | Verba própria aprovada, sem tirar de P1 a P5, e uma turma com CPLmax_h conhecido (PP1) | pessoa do marketing; gestor-de-midia; cmo |
| T4 | Pixel e API de eventos do TikTok instalados e testados no domínio, com o mesmo evento de lead das campanhas da Meta (EM11 da estrategia-de-midia-pos) | humano de site e rastreio; arquiteto-de-fluxos |
| T5 | Algum sinal de público: origem "TikTok" aparecendo no CRM ("como conheceu"), ou resultado de teste do canal na Graduação ou em Cursos Livres [CONFIRMAR] | analista-de-dados; gestor-de-midia |
| T6 | Decisão do gestor-de-midia levada ao cmo, porque muda os canais ativos | gestor-de-midia; cmo |

Momento de reavaliação sugerido: revisão do plano do trimestre seguinte (rascunho em 22/01/2027, gestor-de-midia-pos, 4.1), com as condições T1 a T5 respondidas.

## 4. Desenho mínimo, se entrar

Só referência para a próxima rodada. Não vale como pedido de subida.

- **Modelo:** enxuta (skill estrutura-de-campanha-paga, passo 2): 1 campanha, 1 grupo de anúncios, 3 a 4 vídeos de conceitos diferentes. Orçamento na campanha.
- **Turma:** uma só, escolhida pelo gestor-de-midia entre as que já têm vídeo vertical aprovado e meta de PP1. Sem turma bloqueada (por exemplo, 657 enquanto o pré-requisito não estiver na página, PP7).
- **Objetivo:** conversão no site (lead na página da turma), sem formulário instantâneo, pelo mesmo motivo do LinkedIn: o dado fica na política de privacidade da página [SUPOSIÇÃO de desenho].
- **Público:** amplo, 18 anos ou mais, localização da praça da turma (ou Brasil, se a turma tiver a maior parte online) [SUPOSIÇÃO]. Nenhum interesse empilhado; nenhum público menor de 18 anos. Remarketing só quando houver público suficiente de visitantes da página ou de quem viu a maior parte do vídeo.
- **Anúncios:** professor explicando um tema do cronograma, dúvida frequente respondida (como funciona o semipresencial, turma mínima de 15 alunos), bastidor de módulo prático. Uma ideia por vídeo, legenda sempre, nome exibido da Ufape, CTA "Saiba mais". Spark Ads de post de docente só com o post publicado pelo próprio docente (autorização de imagem e de citação registrada nas decisões 8 e 10; texto em primeira pessoa com o ok dele). Música só da biblioteca comercial ou licenciada.
- **Conteúdo:** nome "Pós-graduação em <área>"; preço, se aparecer, com parcelas, valor da parcela, total e matrícula; nenhuma frase de certificação; nenhuma urgência; nenhuma frase que afirme característica de quem vê; nenhuma promessa de cargo ou renda.
- **Nomes e UTM (D11 e D12 do cmo):** campanha `pos_<código>_tiktok_lead_amplo18-<praça>_<AAAAMM>`; grupo = nome da campanha + `__amplo18-<praça>`; anúncio `<código>-<conceito>_v916_<gancho>_vN`; utm_source=tiktok, utm_medium=paid_social, utm_campaign = nome da campanha, utm_content = nome do anúncio, utm_term = público.
- **Leitura:** 3 semanas, como no LinkedIn: semana 1 só rastreio e destino; semana 2 uma mudança única (pausa de anúncio com gasto de 1,5 a 2 x CPLmax_h sem lead); semana 3 sem mudança; leitura final contra CPLmax_h e a qualidade do lead no CRM.
- **Critério de parar:** pixel sem registrar lead em 48 h; destino diferente do catálogo; fim do período aprovado; verba, CPL e leads por semana: [CONFIRMAR].

## 5. Pedido de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| TK1 | Confirmar o TikTok fora da mídia paga da Pós neste trimestre, com reavaliação no plano do trimestre seguinte pelas condições T1 a T6 | sem verba, sem perfil, sem rastreio e sem criativo nativo (seção 2) | sem custo | verba e horas concentradas nas frentes com data | reabrir o canal numa revisão de segunda-feira, com T1 a T6 respondidas |

## 6. Auditorias aplicadas

- auditorias/11-midia-paga.md: canal fora, com motivo; pixel e API de eventos do TikTok listados como condição de entrada; Spark Ads só com autorização registrada.
- auditorias/conformidade-educacional.md: o desenho mínimo já traz as regras de preço, certificação, urgência e idade mínima.

Próximo agente sugerido: qa-de-marketing.

---

## Fatos (com fonte)

- TikTok fora nas quatro frentes de verba da Pós: "Sem perfil e sem produção comprovada" (gestor-de-midia-pos, seção 3); encomenda ao anuncios-tiktok: "Sem encomenda nesta rodada" (gestor-de-midia-pos, encomendas).
- P5 só para o LinkedIn de 657 (cmo, 12.6, EM8).
- TikTok fora na estratégia da Pós; a Graduação é candidata antes da Pós (estrategia-de-marketing-pos, seção 4).
- TikTok fora na estratégia social da Pós; nenhum perfil aberto para a Pós; o roteiro curto serve a Reels e Shorts (estrategia-social-pos, seções 1.3 e 1.5).
- Pixel do TikTok listado como pendente e "TikTok fora" no checklist do gestor (gestor-de-midia-pos).
- Preço total das Pós de R$ 12.000,00 a R$ 48.780,00 (contexto/pos-graduacao.md; catálogo).
- Turma mínima de 15 alunos na Pós (decisão 11 de 26/10/2026).
- Padrão de UTM e nomes: utm_source=tiktok e utm_medium=paid_social (cmo, D11 e D12).

## Suposições ([SUPOSIÇÃO])

- [SUPOSIÇÃO] Baixa presença da persona da Pós no TikTok (sem dado da Ufape).
- [SUPOSIÇÃO] Referência de 2 vídeos por semana para um perfil no TikTok ter vida (estrategia-de-marketing-pos e estrategia-social-pos).
- [SUPOSIÇÃO de desenho] Conversão no site em vez de formulário instantâneo; localização pela praça da turma; 3 a 4 vídeos no modelo enxuta.
- [SUPOSIÇÃO] Regras de política de anúncio do TikTok citadas no desenho mínimo (idade mínima, áudio comercial, Spark Ads com autorização) são as da instrução do agente; não foram conferidas na política atual da plataforma.

## Dados que faltam ([CONFIRMAR])

- [CONFIRMAR] Se a Ufape tem perfil no TikTok e quem publica.
- [CONFIRMAR] Verba própria para o canal; CPLmax_h da turma candidata (PP1); CPC, CPM e CPL do canal: [DADO NÃO FORNECIDO].
- [CONFIRMAR] Inventário de vídeos verticais aprovados, com áudio de uso comercial.
- [CONFIRMAR] Instalação do pixel e da API de eventos do TikTok e evento de lead das páginas (EM11; teste de rastreio de 31/10).
- [CONFIRMAR] Origem "TikTok" no CRM ou resultado de teste do canal em outra linha.
