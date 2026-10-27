# Estrutura de Meta Ads da Pós-graduação, versão 7: parte 3 (seção 6, anúncios)

Continuação de `anuncios-meta-pos-2026-10-26-p2.md`. Mesmos marcadores, mesma versão.

---

## 6. Anúncios

### 6.1 Como o anúncio se liga à peça aprovada

- Texto principal, título, descrição e botão de cada anúncio são **exatamente** os da peça de mesmo nome no criativos v3 (seção da turma, coluna da tabela 6.2). Nenhum texto foi reescrito aqui. Nenhum tem preço, valor de inscrição, bolsa, prova, certificação ou urgência (criativos 1.1).
- O entregável padrão de 5 textos principais por conceito não se repete nesta versão: a encomenda pede anúncios ligados às peças aprovadas (1 texto, 1 título e 1 descrição por peça). Variação de texto só como iteração planejada, uma variável por vez, pedida ao criativos-de-anuncio depois de haver vencedor (cada seção do criativos traz a iteração prevista).
- Botão: "Saiba mais" em todos os anúncios, como aprovado. Motivo: o destino é a página da turma, com as condições completas, e a campanha otimiza lead. Se o evento escolhido for cadastro e a lista da Meta tiver o rótulo, "Cadastre-se" pode entrar no remarketing, por pedido [SUPOSIÇÃO de rótulo disponível].
- Primeira linha do texto principal: as primeiras linhas aprovadas têm até 117 caracteres (maior caso: 366-r2), conferido por script pelo qa [SUPOSIÇÃO de limite de cerca de 125 caracteres antes do "ver mais"; confirmar na prévia do gerenciador].
- Em Stories e Reels há pouco texto: a mensagem está dentro da arte. A arte 9:16 de adaptação (nome com `e916`) vai anexa ao mesmo anúncio, como arte do posicionamento de Stories e Reels, e não vira anúncio novo nem teste [SUPOSIÇÃO de recurso de personalização por posicionamento; conferir]. Se o recurso não existir, o estático 1:1 serve a todos os posicionamentos e a adaptação fica de fora, por pedido ao gestor.
- Rodízio (estratégia 3.7): os 3 anúncios do frio sobem juntos, na ordem c1, c2, c3. Se o CPL do frio passar de R$ 20,00 na 1ª semana fechada, ficam no ar os 2 de menor CPL (empate: maior CTR; persistindo, o de menor número), o 3º é pausado, nunca apagado, e a troca é feita na revisão de segunda (seção 9). O remarketing não tem rodízio: as 2 peças ficam no ar até o corte; na extensão, fica 1 por vez, a -exta e depois a -extb (seção 6.4), que não é rodízio nem teste.
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

Totais: 14 turmas x 3 anúncios no frio = 42; 14 x 2 no remarketing = 28; 70 anúncios até o corte. Na extensão, as 2 peças em sequência de cada turma (14 -exta e 14 -extb, 28 peças ao todo) ocupam o lugar de r1 e r2, nunca mais de 1 por turma no ar ao mesmo tempo, sem somar ao total de 70 ao mesmo tempo (seção 6.4). Em 662, c3 e r1 não têm arte nem texto liberados (criativos 17): nenhum anúncio de 662 sobe antes de o c3 estar produzido e aprovado (seção 8), e 662 só volta depois da OU18 (seção 7.5).

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

Parâmetros completos de cada anúncio (os 3 primeiros de cada bloco são do frio; os 2 últimos, do remarketing). Os parâmetros das peças -exta e -extb estão na seção 6.4. O AAAAMM de 679, 68636, 366 e 662 muda se a subida for em outro mês (seção 3.1).

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

### 6.4 Anúncios da extensão (2 peças em sequência por turma, dentro do remarketing existente)

Regra da estratégia v5 (4.1, 7.2 e EM16), com a resolução do CC1 (criativos-de-anuncio-pos-2026-10-27-ext, seção 2) e a errata do item h do memorando da onda 2: a extensão roda **dentro da campanha e do conjunto de remarketing já existentes da turma** (`pos_<código>-<área>_meta_lead_rmk30d_<AAAAMM>__rmk30d`), sem campanha nem conjunto novos, com **duas peças em sequência**, nunca as duas no ar ao mesmo tempo, ambas adaptações do r2 (**r2 fixo**, RE4). Este arquivo não copia o texto das peças: texto principal, título, descrição, botão e arte de cada -exta e -extb estão no criativos-de-anuncio-pos-2026-10-27-ext (seção 3 por turma), pendentes da conferência do qa-de-marketing. As exceções são a -exta de 333 e a de 68632, cujo texto novo vem das decisões do cmo e está copiado abaixo. O que fica definido aqui é onde cada anúncio entra, quando, com que nome e UTM, e com que verba. Diária e total não mudam.

| Item | Regra |
|---|---|
| Duas peças, uma por vez | **-exta** (pré-início): do dia seguinte ao corte até 23h59 da véspera do início das aulas; diz a data de início e, onde a regra permite, que a matrícula segue aberta até o 3º módulo. **-extb** (a partir do início): do dia do início até 23h59 da véspera do 3º módulo; diz que as aulas já começaram, a regra de matrícula até o 3º módulo e que, **sobre os módulos já realizados, a pessoa fale com o time** (errata do item h, RM1; nenhuma promessa de reposição até a OU3). Mesma campanha, mesmo conjunto, mesma diária e mesmos R$ 150,00 |
| Quando começa a -exta | No dia seguinte ao corte (datas da seção 3.3), só se a turma não tiver 15 matrículas nem lotada [CONFIRMAR vagas], com a peça -exta aprovada pelo qa-de-marketing na conformidade educacional e as condições por turma da tabela abaixo. **Em 68635, 679 e 366, a -exta está liberada pelo gestor-de-midia (memorando da onda 2, item g), com diária e teto próprios e a regra do saldo para a -extb (seção 5.1); a -extb só com o dia do 3º módulo.** Fica pendente o qa desta versão antes da aprovação do MO6 (M2 do qa onda2c) |
| Troca no dia do início das aulas | O humano pausa a -exta (nunca apaga, com exportação antes) e ativa a -extb no mesmo dia, como primeira ação do dia, com a mesma diária (em 68635, 679 e 366, a diária da -extb é pelo saldo). Nunca as duas ativas ao mesmo tempo. A -extb só vai ao ar no dia do início ou depois; a frase "as aulas já começaram" antes do início seria falsa (CC1). Se o início da turma mudar, a data da troca muda junto. Em sábado, domingo e feriado, a forma de execução é a da seção 5.5b (regra automática, plantão nomeado ou plano C) |
| O que sai | Pedido de pausa da campanha fria inteira e de todo anúncio que cite a data de início sem a regra completa (r1 e r2 até o corte; r2 cita a data). Pausar, nunca apagar, com exportação antes |
| O que fica | Na campanha de remarketing, 1 anúncio por vez: a -exta e, depois da troca, a -extb, ambas adaptações do r2 (nome com `r2` fixo, pelo criativos-de-anuncio-pos-2026-10-27-ext, seção 5), sem escolha entre r1 e r2 por menor CPL (a regra de desempate da versão 5 saiu; RE4 do qa; errata do item h). Mesmo conjunto, públicos de visitantes (30 dias) e engajamento (90 dias), 18+. r1 e r2 seguem pausados. A decisão final é do gestor-de-midia |
| O que as peças dizem | A -exta, com a regra do 3º módulo na maioria das turmas (início da turma, "matrícula aberta até o 3º módulo", data do 3º módulo), e a -extb (as aulas já começaram, "matrícula até o 3º módulo", data do 3º módulo e "fale com o time" sobre os módulos já realizados) [CONFIRMAR OU3 para o texto]. **Em 333 e 68632, enquanto a OU3 estiver aberta, a -exta nova não tem "3º módulo" nem a data do 3º módulo em nenhuma linha** (tabela abaixo). Sem preço, sem valor de inscrição, sem "últimas vagas" ou urgência com a data sem a regra (decisão 18; conformidade) |
| Nome | `<código>-r2-exta_e11_regra3mod_v1` antes do início e `<código>-r2-extb_e11_regra3mod_v1` a partir do início (exemplo, 68615: `68615-r2-exta_e11_regra3mod_v1` e `68615-r2-extb_e11_regra3mod_v1`; criativos ext, seção 5). **333 e 68632, -exta nova: `333-r2-exta_e11_inicio_v2` e `68632-r2-exta_e11_inicio_v2`; a -exta antiga (`_v1`, com "Matrícula aberta até o 3º módulo") fica arquivada, sem subir, até a OU3 [SUPOSIÇÃO: o nome final é do criativos-de-anuncio, na versão 4 do arquivo de extensão].** Adaptação 9:16 anexa: `e11` por `e916` [SUPOSIÇÃO de recurso, como em 6.1] |
| UTM | `utm_source=meta&utm_medium=paid_social&utm_campaign=<campanha de remarketing da turma, seção 3.2>&utm_content=<nome do anúncio -exta ou -extb>&utm_term=rmk30d`. Exemplo, 68615, -exta: `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_rmk30d_202612&utm_content=68615-r2-exta_e11_regra3mod_v1&utm_term=rmk30d` (na -extb, `utm_content=68615-r2-extb_e11_regra3mod_v1`). Lista completa abaixo |
| Verba | R$ 150,00 por turma no período, diária da coluna "Extensão" da tabela 5.2b, igual na -exta e na -extb (em 68635, 679 e 366, -exta com o teto de R$ 39,44, R$ 37,41 e R$ 39,44 e -extb pelo saldo, seção 5.1). Diária abaixo do mínimo aceito: EM14 na extensão (seção 5.4). Sobra não é gasta |
| Quando para | Pausa total às 23h59 da véspera do 3º módulo, ou antes se o gasto do ciclo da turma chegar a R$ 2.000,00, a turma chegar a 15 matrículas ou lotar. **333 e 68632, enquanto a OU3 estiver aberta: às 23h59 da véspera do início (26/03 e 09/04), ou seja, só a -exta roda; a versão antiga fica arquivada.** 68635, 679 e 366, sem o dia do 3º módulo: a -exta para às 23h59 da véspera do início (09/04, 02/04 e 09/04) e o saldo não é gasto |
| Leitura | Mensal (diária de R$ 1,29 a R$ 5,17); frequência e CPM lado a lado com as turmas da mesma área (68615 e 333; 289 e 657). A -exta e a -extb não são teste nem rodízio: são a mesma peça em dois momentos (criativos ext, seção 5) |

**-exta nova de 333 e de 68632 (copiada das decisões do cmo; o qa confere e o criativos-de-anuncio fecha o nome na versão 4 do arquivo de extensão).** Regras: sem "3º módulo" e sem a data do 3º módulo em nenhuma linha (E6); nenhum título com data; campus como campus da turma (E17); botão "Saiba mais".

| Campo (Meta) | 68632, `68632-r2-exta_e11_inicio_v2` | Caracteres | 333, `333-r2-exta_e11_inicio_v2` | Caracteres |
|---|---|---|---|---|
| Trecho visível | "Pós-graduação em Clínica Cirúrgica de Cães e Gatos: aulas em 10/04/2027. Turma presencial, campus Goiânia." | 106 | "Pós-graduação em Citopatologia Veterinária: aulas em 27/03/2027. Módulo 1 presencial, campus São Paulo." | 103 |
| Restante | "A turma pode não ser formada: compre passagem e hotel só depois de a turma ser confirmada. Veja parcelas, total e matrícula na página da turma." | 143 | o mesmo texto | 143 |
| Título | "Matrícula aberta" | 16 | "Matrícula aberta" | 16 |
| Descrição | "Aulas em 10/04/2027" | 19 | "Aulas em 27/03/2027" | 19 |
| Imagem 1:1 e 9:16, selo | "Pós-graduação em Clínica Cirúrgica de Cães e Gatos" | 50 | "Pós-graduação em Citopatologia Veterinária" | 42 |
| Imagem, título | "Matrícula aberta" | 16 | "Matrícula aberta" | 16 |
| Imagem, apoio | "Aulas em 10/04/2027. Turma presencial." | 38 | "Aulas em 27/03/2027. Módulo 1 presencial." | 41 |
| Imagem, rodapé | "Campus Goiânia. Faculdade UFAPE" | 31 | "Campus São Paulo. Faculdade UFAPE" | 33 |

Nota: 333 é semipresencial, então nenhuma peça diz "Turma presencial"; "Módulo 1 presencial" é dado do cronograma da ficha. 68632 é presencial (nunca "semipresencial"). Contagens à mão: recontar por script e na prévia do gerenciador antes de subir. A -exta antiga de cada uma (`_v1`, com a frase "Matrícula aberta até o 3º módulo") não sobe enquanto a OU3 estiver aberta; com a OU3 respondida, o cmo decide em ciclo extra se ela volta e se a -extb sobe. A mídia dessas duas turmas para às 23h59 da véspera do início (26/03 em 333, 09/04 em 68632), e o saldo não gasto fica na turma.

Por turma (datas de início e de pausa total da seção 3.3; troca e bloqueios do criativos ext, seção 2, e das decisões do cmo):

| Turma | -exta no ar de (dia seguinte ao corte) | -exta até 23h59 (véspera do início) | Troca: pausa a -exta e ativa a -extb (início das aulas) | -extb até 23h59 (pausa total) | Diária Meta (igual nas duas) | Situação |
|---|---|---|---|---|---|---|
| 68615 | 19/02/2027 | 19/03/2027 | 20/03/2027 | 21/05/2027 | R$ 1,63 | sobe com as duas peças e as condições |
| 289 | 19/02/2027 | 19/03/2027 | 20/03/2027 | 14/05/2027 | R$ 1,76 | idem; diária de manutenção e aquecimento recalculadas (seção 7) |
| 333 | 26/02/2027 | **26/03/2027** | 27/03/2027, só com OU3 | 28/05/2027, só com OU3 | R$ 5,17 | **só a -exta nova (`_v2`) enquanto OU3 estiver aberta, com pausa total às 23h59 de 26/03**; com OU3, a -extb entra e a diária é recalculada pelo saldo até 28/05; a -exta antiga arquivada |
| 657 | 12/02/2027 | 12/03/2027 | 13/03/2027 | 21/05/2027 | R$ 1,51 | revisão de 10/02 decide a condição das 15 matrículas; U10 e PP7 |
| 341 | 19/02/2027 | 19/03/2027 | 20/03/2027 | 30/04/2027 | R$ 2,11 | PP7; formato do 3º módulo [CONFIRMAR] |
| 679 | 05/03/2027 | 02/04/2027 | 03/04/2027 (planilha; só com a data de início conferida, P3, e o dia do 3º módulo) | [CONFIRMAR] (3º módulo em junho de 2027) | **-exta R$ 1,29 (teto R$ 37,41); -extb pelo saldo** | **-exta liberada pelo gestor (memorando da onda 2, item g); -extb só com o dia do 3º módulo**; texto da -exta pronto (cita só o mês) |
| 68632 | 12/03/2027 | **09/04/2027** | 10/04/2027, só com OU3 | 11/06/2027, só com OU3 | R$ 5,17 | **só a -exta nova (`_v2`) enquanto OU3 estiver aberta, com pausa total às 23h59 de 09/04**; com OU3, em vez da pausa, a troca para a -extb em 10/04 e saldo até 11/06; presencial; a -exta antiga arquivada |
| 68635 | 12/03/2027 | 09/04/2027 | 10/04/2027 (só com o dia do 3º módulo) | [CONFIRMAR] (3º módulo em junho de 2027) | **-exta R$ 1,36 (teto R$ 39,44); -extb pelo saldo** | **-exta liberada pelo gestor (memorando da onda 2, item g); -extb só com o dia do 3º módulo** |
| 366 | 12/03/2027 | 09/04/2027 | 10/04/2027 (planilha; o site diz 24/04/2027; só com a data de início conferida, P4, e o dia do 3º módulo) | [CONFIRMAR] (3º módulo em junho de 2027) | **-exta R$ 1,36 (teto R$ 39,44); -extb pelo saldo** | **-exta liberada pelo gestor (memorando da onda 2, item g), só com P4 resolvida; -extb só com o dia do 3º módulo**; texto da -exta sem data de início |
| 68628 | 12/03/2027 | 09/04/2027 | 10/04/2027 | 25/06/2027 | R$ 1,41 | sobe com as duas peças e as condições |
| 68617 | 19/03/2027 | 16/04/2027 | 17/04/2027 | 18/06/2027 | R$ 1,63 | idem; URL a conferir (seção 8) |
| 68636 | 19/03/2027 | 16/04/2027 | 17/04/2027 (só no site; planilha [CONFIRMAR]; troca só com a data conferida, P3) | 18/06/2027 | R$ 1,63 | idem; peças sem data de início e sem a frase do AP7 |
| 68609 | 26/03/2027 | 23/04/2027 | 24/04/2027 | 25/06/2027 | R$ 1,63 | sobe com as duas peças e as condições |
| 662 | 26/03/2027 | 23/04/2027 | 24/04/2027 (planilha; a página mostra 15/08/2026, P3) | [CONFIRMAR] (ficha com módulos de 2026) | (R$ 150,00 menos metade do excedente) / dias | **as duas peças bloqueadas** (ficha de 2026 e sem 3º módulo); campanha atual pausada pelo OM2 até a OU18; só nome, campus e data; a extensão é o caminho do excedente de 662 (seção 7.3) |

Nota sobre 679, 68635 e 366: o texto da -exta dessas três não depende do dia do 3º módulo, porque cita só o mês da ficha ("junho de 2027"). O gestor-de-midia liberou a -exta com diária própria, para a turma não ficar sem remarketing nas semanas antes do início, que são as que mais decidem a matrícula de quem já visitou a página. A diária vem de R$ 150,00 divididos pelos dias do dia seguinte ao corte até 29/06/2027 (véspera do último dia possível de junho), com piso de R$ 1,29 em 679 que mantém o limite de volume acima de R$ 18,00 [SUPOSIÇÃO de desenho do item g]. A -extb não sobe sem o dia, e o texto dela não usa marcador no lugar do dia. O texto do CE2 desta versão: **-exta liberada pelo gestor (memorando da onda 2, item g); -extb só com o dia do 3º módulo.**

UTM dos anúncios da extensão (campo "Parâmetros de URL" de cada anúncio; campanha de remarketing da seção 3.2; `utm_term=rmk30d`). Os de peça bloqueada ficam escritos e sem uso até a liberação; os de peça arquivada não são usados:

```
68615
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_rmk30d_202612&utm_content=68615-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615-patclin_meta_lead_rmk30d_202612&utm_content=68615-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

289
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_rmk30d_202612&utm_content=289-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_289-cardio-go_meta_lead_rmk30d_202612&utm_content=289-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

333 (só a -exta nova, _v2, enquanto OU3 estiver aberta; -extb só com OU3; a -exta _v1 arquivada, sem uso)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_rmk30d_202612&utm_content=333-r2-exta_e11_inicio_v2&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_333-citopato_meta_lead_rmk30d_202612&utm_content=333-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

657
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_rmk30d_202612&utm_content=657-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_657-anest-avancada_meta_lead_rmk30d_202612&utm_content=657-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

341
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_rmk30d_202612&utm_content=341-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_341-equina_meta_lead_rmk30d_202612&utm_content=341-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68635 (-exta liberada pelo gestor; -extb só com o dia do 3º módulo)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_rmk30d_202701&utm_content=68635-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68635-clinmed-emerg_meta_lead_rmk30d_202701&utm_content=68635-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68636
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_rmk30d_202701&utm_content=68636-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68636-pneumo_meta_lead_rmk30d_202701&utm_content=68636-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68617
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_rmk30d_202701&utm_content=68617-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68617-endocrino_meta_lead_rmk30d_202701&utm_content=68617-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68628
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_rmk30d_202701&utm_content=68628-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68628-onco_meta_lead_rmk30d_202701&utm_content=68628-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68609
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_rmk30d_202701&utm_content=68609-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68609-anest-go_meta_lead_rmk30d_202701&utm_content=68609-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

68632 (só a -exta nova, _v2, enquanto OU3 estiver aberta; -extb só com OU3; a -exta _v1 arquivada, sem uso)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_rmk30d_202701&utm_content=68632-r2-exta_e11_inicio_v2&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68632-cirurgia-go_meta_lead_rmk30d_202701&utm_content=68632-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

679 (-exta liberada pelo gestor; -extb só com o dia do 3º módulo)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_rmk30d_202701&utm_content=679-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_679-infecto_meta_lead_rmk30d_202701&utm_content=679-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

366 (-exta liberada pelo gestor; -extb só com o dia do 3º módulo)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_rmk30d_202701&utm_content=366-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_366-fisio_meta_lead_rmk30d_202701&utm_content=366-r2-extb_e11_regra3mod_v1&utm_term=rmk30d

662 (as duas bloqueadas: ficha de 2026 e sem 3º módulo)
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_rmk30d_202701&utm_content=662-r2-exta_e11_regra3mod_v1&utm_term=rmk30d
utm_source=meta&utm_medium=paid_social&utm_campaign=pos_662-orto_meta_lead_rmk30d_202701&utm_content=662-r2-extb_e11_regra3mod_v1&utm_term=rmk30d
```

---

**Continua em `anuncios-meta-pos-2026-10-26-p4.md` (seções 7 a 9).**
