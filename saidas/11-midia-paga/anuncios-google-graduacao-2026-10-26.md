# Estrutura de Google Ads (Busca): Medicina Veterinária, São Paulo, Graduação 2027/1

- Agente: anuncios-google (departamento 11, Mídia Paga, sob o gestor-de-midia)
- Linha: graduacao
- Data: 26/10/2026 (rodada). Versão 2 em 27/10/2026, depois do qa-de-marketing (saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-27-campanhas.md, veredito "aprovado com ajustes" G-1 e G-2)
- Workflow: /campanha-de-vestibular, etapa 5 (montagem dos canais pagos, junto com o anuncios-meta), encomenda da seção 6 do gestor-de-midia-graduacao v3 (prazo 06/11/2026)
- Liberação coberta: G1, Edital nº 002/2026 (Vestibular 2027) + Graduação em Medicina Veterinária, São Paulo. Só o integral é montado agora. O noturno fica reservado e bloqueado (seção 13). Pedagogia, Performance Max e YouTube estão fora (decisão do gestor, seção 3.1 dele).
- Status: rascunho para aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Um humano monta as campanhas na plataforma, em estado pausado, depois da conferência do qa nos itens G-1 e G-2 e da aprovação (seção 15).
- Entradas lidas:
  - CLAUDE.md e docs/execucao-2026-10-26.md (decisões 1 a 17, em especial 15 e 16)
  - contexto/ufape-geral.md, contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (cabeçalho e seção 1) e contexto/cursos/graduacao/editais-2027-1.md
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md (pedidos G1 a G14)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12.7, D11 e D12; seção 13 só conferida quanto a mídia: sem regra nova de UTM)
  - saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (versão 3) e estrategia-de-midia-graduacao-2026-10-26.md (versão 3)
  - saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md (seção 4, anúncios de busca, e seção 9)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-d.md (ajustes A-C1 a A-C5) e qa-de-marketing-graduacao-2026-10-27-campanhas.md (G-1, G-2, R-G1 a R-G3)
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md
- Regra de fonte: nome do curso, turno, duração, modalidade, carga horária, preço e ato vêm do catálogo (seção 1); datas, vagas, formas de ingresso, regras de desconto e menor de idade vêm da ficha dos editais 2027/1; verba, fases, metas e nomes vêm do gestor-de-midia v3. Não existe exportação do Planejador de palavras-chave, histórico de CPL nem pesquisa do departamento 03: volume e CPC ficam [DADO NÃO FORNECIDO]. Nenhum dado pessoal neste arquivo.

---

## Mudanças desta versão (v2, 27/10/2026)

| # | O que mudou | Onde | Motivo |
|---|---|---|---|
| 1 | Contradição retirada: o orçamento é por campanha, e o orçamento compartilhado aparece só como item de reserva do AG2. A frase "o Google só tem orçamento por campanha" saiu | 2.1 e 3 | G-1 do qa |
| 2 | Limites de 15 títulos e 4 descrições por anúncio, e o comentário sobre a "Força do anúncio", marcados [SUPOSIÇÃO, CONFIRMAR no editor]; levados à Lista 2 | 6 e Lista 2 | G-1 do qa |
| 3 | Faixa etária "desconhecida": decisão levada ao AG5 com as duas opções, efeito no alcance e validação do jurídico (G10). Vale a opção mais restrita (excluir "desconhecida") até a resposta | 8, 15 (AG5), Lista 3 | G-2 do qa |
| 4 | Sitelinks para PDF: o humano confere se o PDF mostra contato da Ufape e política de privacidade; se não mostrar, o destino vira a LP | 7.1 e 14 (item 14) | R-G1 do qa |
| 5 | Limite de gasto com valor: R$ 560,00 somando as duas campanhas, e aviso de que a conta pode ser compartilhada com a Pós [CONFIRMAR] (limite de conta não serve de trava; valem diária e data de término) | 14 (item 13) e AG2 | R-G2 do qa |
| 6 | Etapa do workflow alinhada com o anuncios-meta (etapa 5) | Cabeçalho | R-G3 do qa |

---

## 0. Resumo em cinco linhas

1. Uma estrutura de Busca por intenção, duas campanhas: marca e genérica (um grupo cada), só Medicina Veterinária integral, São Paulo, com R$ 560,00 no ciclo de 16/11/2026 a 21/02/2027 (R$ 184,00 na marca e R$ 376,00 na genérica) e diária em reais por semana na seção 3.
2. Quatro anúncios responsivos (2 por grupo: preço e entrada), títulos até 30 e descrições até 90 recontados, com fixações para que o desconto e o Enem nunca apareçam sem as condições.
3. Recursos sem preço: 4 sitelinks (mais 1 condicionado a G7), 6 frases de destaque e nome da empresa; snippet, chamada e formulário ficam de fora, com motivo.
4. Conversão otimizada: cadastro na LP (primária); matrícula só para leitura (secundária, fora da otimização). UTM google e cpc no padrão D11 e D12, com auto tagging ligado. Sem lance em concorrente.
5. Travas que impedem a subida: MP1 e MP2 (metas e verba), G13 (URL, conversão e CRM), G14 (aprovador), G12 e G7 para os anúncios com preço, G8 para o noturno, e as datas do Enem para qualquer texto de nota (seção 11).

---

## 1. Decisões deste arquivo e conflitos registrados

| # | Decisão ou conflito | Onde | Motivo |
|---|---|---|---|
| 1 | 2 anúncios por grupo, como pedido. O esboço do criativos tinha 3 por grupo da genérica; o v2-pratica (RSA-INT-v2 do criativos, seção 4.2) fica de reserva para a fase 2 | 6.6 | Cadência do gestor: conceito novo a cada 2 semanas a partir da fase 2 |
| 2 | utm_content no padrão D12 com bloco de gancho: conceito_formato_gancho_vN (ex.: v1-preco_rsa_a_v1). O criativos usa conceito_formato_vN com a versão como gancho (v1-preco_rsa_v1). Segue o D12 e o ajuste A-C1 do qa-d; o gestor-de-midia confirma na próxima versão do plano dele | 10 | D12 é a regra aprovada pelo cmo; A-C1 do qa-d |
| 3 | Título fixado "Enem: Média Mínima 300 Pontos" na posição 1 dos anúncios de entrada (antes, "Enem com Média Mínima de 300" na posição 2), porque a palavra "pontos" faz parte da condição e a posição 1 garante que o Enem nunca aparece sem ela | 6.2 e 6.4 | Condição completa do Enem em toda peça |
| 4 | Descrição com a linha do menor de idade ("representante legal") nos 4 anúncios, no lugar da descrição "Inscrição gratuita em São Paulo. Aulas...", que já aparece em títulos | 6 | Pedido do cmo: representante legal onde couber (Edital 002/2026) |
| 5 | Descrição 2 dos anúncios com preço traz a regra de renovação com comprovação (Edital 003/2026) | 6.1 e 6.3 | Desconto só com as condições que o espaço comporta; regra completa no edital |
| 6 | Divisão da verba do Google entre marca e genérica: 30% e 70% nas semanas S1 a S11 e 40% e 60% nas S12 a S14 [SUPOSIÇÃO de desenho] | 3 | O gestor deixou a divisão para este arquivo; a marca pesa mais na reta final (gestor 3.3) |
| 7 | Bloqueio do termo "noturno" na marca e na genérica enquanto o noturno estiver bloqueado | 5 | Anúncio diz "Integral"; mostrar a quem procura o noturno seria enganoso. Segue criativos 4.1 |
| 8 | Sem Performance Max, YouTube, Display, parceiros de pesquisa, audiências, listas de contatos e remarketing de Busca | 2 | Gestor 3.1; MP7 (listas) bloqueada; verba |

---

## 2. Estrutura e configurações

### 2.1 Mapa em árvore

```
Conta Google Ads da Ufape [CONFIRMAR ID da conta com a Ufape]
  grad_medvet-integral_google_busca_marca_202611            (Busca, R$ 184,00 no ciclo)
    grupo: grad_medvet-integral_google_busca_marca_202611__marca
      palavras: seção 4.1 | negativas: seção 5
      anúncios: RSA-M1 (v1-preco) e RSA-M2 (v3-entrada), seção 6
  grad_medvet-integral_google_busca_generica_202611         (Busca, R$ 376,00 no ciclo)
    grupo: grad_medvet-integral_google_busca_generica_202611__generica
      palavras: seção 4.2 | negativas: seção 5
      anúncios: RSA-G1 (v1-preco) e RSA-G2 (v3-entrada), seção 6
  Recursos (seção 7), ligados às duas campanhas
  Lista compartilhada de negativas: grad_medvet_negativas_gerais
```

Modelo de estrutura (skill estrutura-de-campanha-paga): enxuta, dentro do lançamento por fases do gestor. 1 campanha por intenção, 1 grupo por campanha, 2 anúncios por grupo, porque a verba semanal do Google é de R$ 15,00 a R$ 64,00 e o volume não sustenta mais. Orçamento por campanha (ou compartilhado entre as duas, só no item de reserva do AG2). O AAAAMM do nome é o mês da subida e o nome não muda nos meses seguintes (as fases trocam anúncios e diária, não campanha).

### 2.2 Configurações das duas campanhas (humano confere no editor)

| Item | Valor | Observação |
|---|---|---|
| Tipo e objetivo | Rede de Pesquisa, objetivo Leads (cadastro na LP) | Sem meta de "vendas" nem de tráfego |
| Redes | Só Rede de Pesquisa do Google. Parceiros de pesquisa desligados. Rede de Display desligada | [SUPOSIÇÃO de desenho]: verba pequena, sem controle de posicionamento |
| Locais | Seção 8 | |
| Idioma | Português | |
| Estratégia de lance, fase 1 | Maximizar cliques, com limite de CPC máximo | Segue o gestor (4.3). Teto numérico: [DADO NÃO FORNECIDO]. Regra: CPC máximo menor ou igual a CPL máximo x taxa de clique para cadastro. A taxa não existe; o teto sai do Planejador de palavras-chave e da leitura da 1ª semana, aprovado pelo gestor-de-midia (pedido AG4). Sem teto numérico aprovado, a campanha não é ativada |
| Estratégia de lance, depois | Maximizar conversões (lead), com CPA alvo igual ao CPL máximo aprovado em MP1 | Só por proposta do gestor-de-midia, com volume de conversões da conta [DADO NÃO FORNECIDO] e aprovação humana |
| Correspondência | Frase e exata. Correspondência ampla fora | Sem histórico para a ampla acertar a intenção |
| Recursos automáticos | Desligar ativos criados automaticamente, expansão de URL final e AI Max para Busca, se a conta oferecer [CONFIRMAR no editor] | O Google poderia gerar texto com preço ou Enem sem as condições |
| Inserção dinâmica de palavra-chave, personalizadores e contagem regressiva | Não usar | Sem urgência falsa; texto só como aprovado |
| Programação | Sem restrição de dia e horário [SUPOSIÇÃO de desenho] | Volume baixo |
| Dispositivos | Todos | |
| Audiências | Nenhuma segmentada ou em observação. Customer Match e semelhantes bloqueados (MP7) | Base pode ter menores (G10) |
| Rotação de anúncios | Otimizar | Com as fixações da seção 6 |
| Rastreamento | Auto tagging ligado, mais UTM no sufixo do URL final (seção 10) | |
| Data de início | 16/11/2026 (segunda-feira), só com MP1, MP2 e os demais itens da seção 11 aprovados | Não subir em 08 e 15/11, dias informados do Enem 2026 [CONFIRMAR no calendário oficial do Inep] |
| Data de término | 21/02/2027 | Pausa geral em 22/02/2027 (MP13), com a data de término como segunda trava |
| Estado na montagem | Pausada. O humano ativa em 16/11 | |
| Nome da empresa | Faculdade UFAPE | Logotipo: [CONFIRMAR arquivo aprovado]; sem logotipo até lá |

---

## 3. Verba e diária por semana (até 21/02/2027)

Total do Google: R$ 560,00 (R$ 2.000,00 do curso menos R$ 1.440,00 da Meta, tabela 3.3 do gestor). Fases: 1 captação R$ 150,00; 2 aquecimento R$ 75,00; 3 inscrições abertas R$ 175,00; 4 reta final R$ 160,00. Divisão entre as duas campanhas: marca 30% e genérica 70% de S1 a S11; marca 40% e genérica 60% de S12 a S14 [SUPOSIÇÃO de desenho, aprovação em MP3].

Enquanto o noturno estiver bloqueado, todo o valor roda no integral. Depois do desbloqueio (MP8), metade da verba semanal vai para o noturno (gestor 1.1), e este arquivo é refeito.

| Semana | Datas | Fase | Total da semana | Marca na semana | Marca, diária | Genérica na semana | Genérica, diária |
|---|---|---|---|---|---|---|---|
| S1 | 16 a 22/11/2026 | 1 | R$ 50,00 | R$ 15,00 | R$ 2,14 | R$ 35,00 | R$ 5,00 |
| S2 | 23 a 29/11/2026 | 1 | R$ 50,00 | R$ 15,00 | R$ 2,14 | R$ 35,00 | R$ 5,00 |
| S3 | 30/11 a 06/12/2026 | 1 | R$ 50,00 | R$ 15,00 | R$ 2,14 | R$ 35,00 | R$ 5,00 |
| S4 | 07 a 13/12/2026 | 2 | R$ 22,50 | R$ 6,75 | R$ 0,96 | R$ 15,75 | R$ 2,25 |
| S5 | 14 a 20/12/2026 | 2 | R$ 22,50 | R$ 6,75 | R$ 0,96 | R$ 15,75 | R$ 2,25 |
| S6 | 21 a 27/12/2026 | 2 | R$ 15,00 | R$ 4,50 | R$ 0,64 | R$ 10,50 | R$ 1,50 |
| S7 | 28/12/2026 a 03/01/2027 | 2 | R$ 15,00 | R$ 4,50 | R$ 0,64 | R$ 10,50 | R$ 1,50 |
| S8 | 04 a 10/01/2027 | 3 | R$ 43,75 | R$ 13,13 | R$ 1,87 | R$ 30,62 | R$ 4,37 |
| S9 | 11 a 17/01/2027 | 3 | R$ 43,75 | R$ 13,13 | R$ 1,87 | R$ 30,62 | R$ 4,37 |
| S10 | 18 a 24/01/2027 | 3 | R$ 43,75 | R$ 13,13 | R$ 1,87 | R$ 30,62 | R$ 4,37 |
| S11 | 25 a 31/01/2027 | 3 | R$ 43,75 | R$ 13,13 | R$ 1,87 | R$ 30,62 | R$ 4,37 |
| S12 | 01 a 07/02/2027 | 4 | R$ 64,00 | R$ 25,60 | R$ 3,65 | R$ 38,40 | R$ 5,48 |
| S13 | 08 a 14/02/2027 | 4 | R$ 48,00 | R$ 19,20 | R$ 2,74 | R$ 28,80 | R$ 4,11 |
| S14 | 15 a 21/02/2027 | 4 | R$ 48,00 | R$ 19,20 | R$ 2,74 | R$ 28,80 | R$ 4,11 |
| Total | 16/11/2026 a 21/02/2027 | | **R$ 560,00** | **R$ 184,00** | | **R$ 376,00** | |
| 22/02/2027 | Início das aulas | | R$ 0,00 | pausa | | pausa | |

Regras de leitura:
- Diária = verba semanal dividida por 7, arredondada para baixo ao centavo. O gasto máximo da semana (7 x diária) nunca passa do valor da tabela; a sobra de centavos vira economia. Em S8 a S11 os valores exatos são R$ 13,125 e R$ 30,625; a tabela mostra centavos arredondados e os totais por campanha (R$ 184,00 e R$ 376,00) valem.
- Total diário das duas campanhas por fase: S1 a S3, R$ 7,14; S4 e S5, R$ 3,21; S6 e S7, R$ 2,14; S8 a S11, R$ 6,24; S12, R$ 9,13; S13 e S14, R$ 6,85.
- O humano troca a diária de cada campanha na segunda-feira de cada semana (14 trocas por campanha). Pesos semanais e fases: os do estrategia-de-midia (2.3 e 2.4), com a regra do Enem e do Sisu dele quando as datas forem confirmadas; nunca muda o total.
- O Google pode gastar até o dobro da diária em um dia e compensar em outros [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda do Google Ads]. O teto que vale é o gasto acumulado: nunca acima de R$ 560,00 no Google nem de R$ 2.000,00 no curso (gestor 6.2, regra 1).
- Diárias abaixo de R$ 2,00 (marca em quase todo o ciclo; genérica em S6 e S7) podem não entregar [SUPOSIÇÃO]. O orçamento é por campanha. Só se o painel mostrar zero impressões em uma campanha por 3 dias seguidos, o gestor-de-midia propõe orçamento compartilhado entre as duas campanhas nessas semanas, sem mudar o total (item de reserva do AG2, com aprovação).
- Leads que a verba compra, só como referência: no cenário base do gestor (CPL máximo R$ 6,67, [SUPOSIÇÃO de cenário], aprovação em MP1), R$ 560,00 compram cerca de 84 leads se o CPL ficar exatamente no máximo (560 dividido por 6,67). Não é previsão.
- A genérica só segue depois de 3 semanas se trouxer cadastro com CPL até o máximo aprovado. Se não trouxer, a verba dela passa para a marca; passar para a Meta é pedido ao cmo (gestor 3.5 e estrategia 6.2, regra 3).

---

## 4. Palavras-chave sementes [SUPOSIÇÃO]

Todas as palavras abaixo são sementes de intenção escritas por este agente. Volume e CPC: [DADO NÃO FORNECIDO]. Antes da montagem, o humano consulta o Planejador de palavras-chave, registra volume e CPC estimado em arquivo de retorno e a pesquisa-de-palavras-chave (departamento 03) revisa a lista final. Palavra sem volume no Planejador não é cadastrada. Nenhuma palavra usa nome de outra instituição.

### 4.1 Grupo marca (grad_medvet-integral_google_busca_marca_202611__marca)

| Palavra-chave | Correspondência | Intenção |
|---|---|---|
| ufape veterinária | frase e exata | Marca mais curso |
| ufape medicina veterinária | frase e exata | Marca mais nome completo do curso |
| faculdade ufape | frase e exata | Marca institucional |
| faculdade ufape veterinária | exata | Marca institucional mais curso |
| vestibular ufape | frase e exata | Marca mais processo seletivo |
| ufape vestibular 2027 | frase e exata | Marca mais processo seletivo do ciclo |
| faculdade ufape são paulo | frase | Marca mais praça |

### 4.2 Grupo genérico (grad_medvet-integral_google_busca_generica_202611__generica)

| Palavra-chave | Correspondência | Intenção | Observação |
|---|---|---|---|
| faculdade de veterinária em são paulo | frase e exata | Escolha da faculdade | |
| faculdade de veterinária sp | frase e exata | Escolha da faculdade | |
| faculdade de medicina veterinária em são paulo | frase | Escolha da faculdade | |
| medicina veterinária são paulo | frase | Escolha do curso | |
| curso de medicina veterinária em sp | frase | Escolha do curso | |
| graduação em medicina veterinária sp | frase | Escolha do curso | |
| medicina veterinária presencial são paulo | frase | Modalidade | |
| faculdade de veterinária particular sp | frase | Escolha da faculdade | |
| faculdade de veterinária integral sp | frase | Turno | O integral é o único montado |
| vestibular medicina veterinária 2027 | frase | Processo seletivo | |
| vestibular veterinária 2027 são paulo | frase | Processo seletivo | |
| inscrição vestibular medicina veterinária | frase | Processo seletivo | |
| mensalidade faculdade de veterinária sp | frase | Comparação de preço | O anúncio de preço leva as condições (seção 6) |
| faculdade de veterinária que aceita enem | frase | Forma de ingresso | Anúncio de entrada, com a condição completa do Enem |
| veterinária com nota do enem | frase | Forma de ingresso | Criar em pausa. Ativar só na semana da divulgação das notas, depois de a data ser confirmada [CONFIRMAR] (seção 11, trava 5) |

Um grupo só na genérica, como decide o gestor (4.3 e 3.5): a verba não sustenta dois grupos e o anúncio de entrada cobre as palavras de Enem.

---

## 5. Negativas

Correspondência de frase, salvo onde indicado. Lista [SUPOSIÇÃO] do plano do gestor, ampliada por este agente; revisar toda segunda-feira no relatório de termos de pesquisa (o humano adiciona o que for fora de escopo, com a autorização permanente do pedido AG7).

### 5.1 Lista compartilhada nas duas campanhas (grad_medvet_negativas_gerais)

| Tema | Termos |
|---|---|
| Gratuidade, bolsa e financiamento (a Ufape não oferece Prouni nem Fies na Graduação) | grátis, gratis, gratuito, gratuita, de graça, bolsa, prouni, fies, financiamento estudantil, sisu |
| Emprego, renda e concurso | emprego, empregos, vaga de emprego, vagas de emprego, vaga para veterinário, vagas para veterinário, vaga de estágio, vagas de estágio, trabalho, contratação, salário, salario, piso salarial, quanto ganha, concurso, concursos, apostila, edital de concurso |
| Instituições públicas e exames de terceiros (sem lance em concorrente) | pública, publica, públicas, federal, estadual, universidade federal, universidade estadual, fuvest, vunesp, nota de corte, gabarito |
| Modalidade e nível | ead, a distância, à distância, ensino a distância, curso online, 100% online, semipresencial, curso livre, cursos livres, técnico, tecnico, curso técnico, auxiliar, pós, pós-graduação, pos graduacao, pós graduação, especialização, mestrado, doutorado, mba, residência, workshop, congresso, simpósio |
| Outras áreas e praças | pedagogia, enfermagem, medicina humana, odontologia, psicologia, zootecnia, agronomia, biologia, biomedicina, banho e tosa, tosador, adestrador, goiânia, goiania, goiás |
| Quem não é candidato | consulta, consultas, vacina, castração, pet shop, agendar, portal do aluno, área do aluno, boleto, segunda via, login |
| Turno (enquanto o noturno estiver bloqueado) | noturno, noturna, à noite, a noite, período noturno |
| Preço mais baixo e promessa de entrada | barata, barato, mais barata, mais barato, menor mensalidade, sem vestibular, sem prova |
| Datas do Enem (até a divulgação das notas ser confirmada) | enem 2026, resultado do enem, nota do enem 2026 |

Notas:
- "Sisu" fica fora por padrão (EM6): os editais não preveem ingresso pelo Sisu. Termos com Sisu só entram por decisão humana.
- "Enem 2026", "resultado do enem" e "nota do enem 2026" saem da lista na semana da divulgação das notas, depois de a data ser confirmada (seção 11, trava 5).
- Nome de outra instituição que aparecer no relatório de termos de pesquisa vira negativa na mesma semana. Lista de concorrentes da Ufape: [DADO NÃO FORNECIDO] (contexto/ufape-geral.md está em branco).

### 5.2 Negativas só da campanha de marca

clínica, hospital, clínica veterinária (quem procura o hospital veterinário da Ufape Clínica, não a graduação), cursos (no plural, para não trazer curso livre), trabalhe conosco, vaga de professor.

### 5.3 Negativas só da campanha genérica

Nenhuma além da lista compartilhada. Se algum termo com "ufape" aparecer na genérica, vira palavra exata da marca, em pedido ao gestor-de-midia (EM8: marca só no integral).

---

## 6. Anúncios responsivos

Limites: título até 30 caracteres e descrição até 90, contados com espaços (contagem feita nesta redação, uma a uma, e recontada pelo qa por script: 0 divergências). **O humano confere de novo no editor antes de montar.** Quantidade máxima de títulos e descrições por anúncio: 15 títulos e 4 descrições [SUPOSIÇÃO, CONFIRMAR no editor]. Sem ponto de exclamação, sem caixa alta para gritar, sem emoji, sem nome de concorrente, sem "últimas vagas", sem nota do MEC e sem frase de certificação.

Regras fixas que valem para os quatro anúncios:
- Desconto: o título "Integral: 50% de Desconto" e a descrição 1 de preço são fixados juntos na posição 1, para o desconto nunca aparecer sem valor cheio, valor com desconto, validade (1º semestre 2027) e "Condições e validade no edital".
- Enem: o título "Enem: Média Mínima 300 Pontos" (posição 1) e a descrição 1 de entrada (posição 1) são fixados juntos; a descrição 1 traz a condição completa, "média mínima de 300 pontos, edições de 2010 em diante". Nenhum outro título com Enem fica sem a condição.
- Ato: só como no catálogo, "Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025)", sem reconhecimento e sem nota.
- Menor de idade: "representante legal", como no Edital 002/2026.
- Com as fixações, a "Força do anúncio" do Google pode ficar em "Média" ou "Ruim" [SUPOSIÇÃO, CONFIRMAR no editor]. Se ficar, é aceito: a conformidade vem antes da nota de força. Não remover fixação para subir a força.

### 6.1 RSA-M1 (campanha de marca, conceito preço) utm_content v1-preco_rsa_a_v1

| Posição | Tipo | Texto | Caracteres |
|---|---|---|---|
| Título 1 (fixar na posição 1) | Título | Integral: 50% de Desconto | 25 |
| Título 2 | Título | Faculdade UFAPE Veterinária | 27 |
| Título 3 | Título | Medicina Veterinária em SP | 26 |
| Título 4 | Título | Vestibular UFAPE 2027 | 21 |
| Título 5 | Título | Vestibular 2027 Veterinária | 27 |
| Título 6 | Título | Inscrição Gratuita | 18 |
| Título 7 | Título | Curso Presencial, Integral | 26 |
| Título 8 | Título | Veterinária Integral, 4 Anos | 28 |
| Título 9 | Título | Aulas a partir de 22/02/2027 | 28 |
| Título 10 | Título | Faculdade UFAPE em São Paulo | 28 |
| Título 11 | Título | Redação Online | 14 |
| Título 12 | Título | Bacharelado Presencial | 22 |
| Título 13 | Título | Veja o Edital 002/2026 | 22 |
| Título 14 | Título | Medicina Veterinária Integral | 29 |
| Título 15 | Título | Graduação em Veterinária | 24 |
| Descrição 1 (fixar na posição 1) | Descrição | De R$ 10.000,00 por R$ 5.000,00/mês no 1º semestre 2027. Condições e validade no edital. | 88 |
| Descrição 2 | Descrição | Desconto do Edital 003/2026: vale só no 1º semestre de 2027; renovação com comprovação. | 87 |
| Descrição 3 | Descrição | Inscrição gratuita. Menor de idade precisa do aceite do representante legal. | 76 |
| Descrição 4 | Descrição | Curso autorizado pela Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). | 83 |

Sem Enem em nenhum ativo deste anúncio. Status: só ativa com G7 e G12 respondidos (seção 11).

### 6.2 RSA-M2 (campanha de marca, conceito entrada) utm_content v3-entrada_rsa_a_v1

| Posição | Tipo | Texto | Caracteres |
|---|---|---|---|
| Título 1 (fixar na posição 1) | Título | Enem: Média Mínima 300 Pontos | 29 |
| Título 2 | Título | Faculdade UFAPE Veterinária | 27 |
| Título 3 | Título | Medicina Veterinária em SP | 26 |
| Título 4 | Título | Vestibular UFAPE 2027 | 21 |
| Título 5 | Título | Vestibular 2027 Veterinária | 27 |
| Título 6 | Título | Inscrição Gratuita | 18 |
| Título 7 | Título | Redação Online | 14 |
| Título 8 | Título | Enem de 2010 em Diante | 22 |
| Título 9 | Título | Curso Presencial, Integral | 26 |
| Título 10 | Título | Aulas a partir de 22/02/2027 | 28 |
| Título 11 | Título | Faculdade UFAPE em São Paulo | 28 |
| Título 12 | Título | Veja o Edital 002/2026 | 22 |
| Título 13 | Título | Bacharelado Presencial | 22 |
| Título 14 | Título | Medicina Veterinária Integral | 29 |
| Título 15 | Título | Faculdade UFAPE | 15 |
| Descrição 1 (fixar na posição 1) | Descrição | Use a nota do Enem (média mínima de 300 pontos, edições de 2010 em diante) ou a redação. | 88 |
| Descrição 2 | Descrição | A redação online é eliminatória, com nota mínima 5,0, e é feita depois da inscrição. | 84 |
| Descrição 3 | Descrição | Inscrição gratuita. Menor de idade precisa do aceite do representante legal. | 76 |
| Descrição 4 | Descrição | Curso autorizado pela Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). | 83 |

Status: pode subir na fase 1 sem G12 (não cita preço), mas depende de G13, MP1, MP2, G14 e da trava das datas do Enem.

### 6.3 RSA-G1 (campanha genérica, conceito preço) utm_content v1-preco_rsa_a_v1

| Posição | Tipo | Texto | Caracteres |
|---|---|---|---|
| Título 1 (fixar na posição 1) | Título | Integral: 50% de Desconto | 25 |
| Título 2 | Título | Faculdade de Veterinária em SP | 30 |
| Título 3 | Título | Medicina Veterinária em SP | 26 |
| Título 4 | Título | Vestibular 2027 Veterinária | 27 |
| Título 5 | Título | Inscrição Gratuita | 18 |
| Título 6 | Título | Curso Presencial, Integral | 26 |
| Título 7 | Título | Veterinária Integral, 4 Anos | 28 |
| Título 8 | Título | Aulas a partir de 22/02/2027 | 28 |
| Título 9 | Título | Faculdade UFAPE | 15 |
| Título 10 | Título | Graduação em Veterinária | 24 |
| Título 11 | Título | Veterinária Presencial em SP | 28 |
| Título 12 | Título | Medicina Veterinária Integral | 29 |
| Título 13 | Título | Bacharelado Presencial | 22 |
| Título 14 | Título | Veja o Edital 002/2026 | 22 |
| Título 15 | Título | Redação Online | 14 |
| Descrição 1 (fixar na posição 1) | Descrição | De R$ 10.000,00 por R$ 5.000,00/mês no 1º semestre 2027. Condições e validade no edital. | 88 |
| Descrição 2 | Descrição | Desconto do Edital 003/2026: vale só no 1º semestre de 2027; renovação com comprovação. | 87 |
| Descrição 3 | Descrição | Inscrição gratuita. Menor de idade precisa do aceite do representante legal. | 76 |
| Descrição 4 | Descrição | Curso autorizado pela Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). | 83 |

Sem Enem em nenhum ativo. Status: só ativa com G7 e G12 respondidos.

### 6.4 RSA-G2 (campanha genérica, conceito entrada) utm_content v3-entrada_rsa_a_v1

| Posição | Tipo | Texto | Caracteres |
|---|---|---|---|
| Título 1 (fixar na posição 1) | Título | Enem: Média Mínima 300 Pontos | 29 |
| Título 2 | Título | Faculdade de Veterinária em SP | 30 |
| Título 3 | Título | Medicina Veterinária em SP | 26 |
| Título 4 | Título | Vestibular 2027 Veterinária | 27 |
| Título 5 | Título | Inscrição Gratuita | 18 |
| Título 6 | Título | Redação Online | 14 |
| Título 7 | Título | Enem de 2010 em Diante | 22 |
| Título 8 | Título | Curso Presencial, Integral | 26 |
| Título 9 | Título | Aulas a partir de 22/02/2027 | 28 |
| Título 10 | Título | Faculdade UFAPE | 15 |
| Título 11 | Título | Graduação em Veterinária | 24 |
| Título 12 | Título | Veterinária Presencial em SP | 28 |
| Título 13 | Título | Veja o Edital 002/2026 | 22 |
| Título 14 | Título | Medicina Veterinária Integral | 29 |
| Título 15 | Título | Bacharelado Presencial | 22 |
| Descrição 1 (fixar na posição 1) | Descrição | Use a nota do Enem (média mínima de 300 pontos, edições de 2010 em diante) ou a redação. | 88 |
| Descrição 2 | Descrição | A redação online é eliminatória, com nota mínima 5,0, e é feita depois da inscrição. | 84 |
| Descrição 3 | Descrição | Inscrição gratuita. Menor de idade precisa do aceite do representante legal. | 76 |
| Descrição 4 | Descrição | Curso autorizado pela Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025). | 83 |

Status: igual ao RSA-M2.

### 6.5 Ativos extras da fase 4 (reta final, trocar em 01/02/2027)

Em cada um dos quatro anúncios, o humano troca dois títulos de pior desempenho (nunca os fixados) por estes e acrescenta a descrição, pedindo antes a aprovação do cmo (nova versão, MP12):

| Tipo | Texto | Caracteres |
|---|---|---|
| Título | Passos da Matrícula | 19 |
| Título | Aulas em 22/02/2027 | 19 |
| Descrição | Resultado no site, matrícula eletrônica e documentos em até 30 dias. | 68 |

Sem "últimas vagas" e sem contagem regressiva. Não existe número de vagas restantes nem data-limite de inscrição (G4).

### 6.6 Reserva: conceito v2-pratica (fase 2)

O RSA-INT-v2 do criativos (seção 4.2) fica de reserva. Entra na fase 2 como conceito novo na genérica, no lugar do anúncio de pior desempenho, só depois de renomear o utm_content para v2-pratica_rsa_a_v1 e de nova contagem de caracteres no editor. Não é montado agora. Os nomes das disciplinas (Anatomia, Práticas Hospitalares, Projeto Extensionista I) são [CONFIRMAR NO CATÁLOGO] com o acadêmico.

### 6.7 Por que estes dois conceitos primeiro

- Entrada (v3): ataca o gargalo provável do funil, o inscrito que não faz a redação [SUPOSIÇÃO do cmo]. Prioridade 1 na ordem de teste do criativos (1.5).
- Preço (v1): ataca a objeção principal da persona, mensalidade alta [SUPOSIÇÃO do contexto da linha]. Prioridade 2.
- Duas ideias diferentes em 3 semanas dão aprendizado antes da escala de janeiro. O terceiro conceito espera a fase 2.

---

## 7. Recursos (extensões), todos sem preço

Não são criados recursos de preço nem de promoção: mostrariam valor sem as condições. Nenhum recurso cita Enem nem a palavra desconto. Limites: título do sitelink até 25, descrições até 35, frase de destaque até 25, contados com espaços.

### 7.1 Sitelinks (conjunto por campanha, com sufixo de URL completo; ver seção 10)

| # | Título | Descrição 1 | Descrição 2 | Destino | utm_content |
|---|---|---|---|---|---|
| SL1 | Como Fazer a Inscrição (22) | Inscrição gratuita pelo site (28) | Redação online, quando puder (28) | LP da Graduação [CONFIRMAR, G13] | sl-inscricao_sitelink_a_v1 |
| SL2 | Edital do Vestibular 2027 (25) | Regras, ingresso e matrícula (28) | Edital nº 002/2026 (18) | https://faculdade.ufape.com.br/uploads/arquivo/edital-vestibular-2027.pdf (catálogo, seção 1) | sl-edital_sitelink_a_v1 |
| SL3 | Prática no 1º Semestre (22) | Anatomia e Práticas Hospitalares (32) | Projeto Extensionista I (23) | LP da Graduação [CONFIRMAR, G13] | sl-pratica_sitelink_a_v1 |
| SL4 | Passos da Matrícula (19) | Matrícula eletrônica (20) | Documentos em até 30 dias (25) | LP da Graduação [CONFIRMAR, G13] | sl-matricula_sitelink_a_v1 |
| SL5 (só com G7) | Regras de Mensalidade (21) | Programa 2027/1: Edital 003/2026 (32) | Condições do 1º semestre de 2027 (32) | https://faculdade.ufape.com.br/uploads/arquivo/edital-descontos-2027.pdf (catálogo, seção 1) | sl-regras_sitelink_a_v1 |

Notas:
- SL3: nomes de disciplina da matriz da ficha, [CONFIRMAR NO CATÁLOGO].
- SL2 e SL5 apontam para PDF. O Google pode recusar PDF como destino de sitelink [CONFIRMAR na análise da plataforma]. Antes de usar, o humano abre o PDF e confere se ele mostra o contato da Ufape e a política de privacidade (auditoria de conformidade, item de plataformas); se não mostrar, ou se o Google recusar, o destino vira a LP, com a mesma UTM.
- SL5 só é criado depois de G7 (correção dos textos do Edital 003/2026: preâmbulo, data de assinatura e item 3.5 de Goiânia). Ele é o caminho para a regra completa do desconto (perda por atraso, não acúmulo com programa governamental), que não cabe nas descrições.
- As descrições dos sitelinks podem ser mostradas juntas ou separadas [CONFIRMAR no editor]; por isso nenhuma frase se divide entre as duas linhas.
- Sem sitelink de "ato do curso": a portaria completa não cabe em 35 caracteres sem arredondar; o ato fica na descrição 4 dos anúncios.

### 7.2 Frases de destaque

| # | Texto | Caracteres |
|---|---|---|
| FD1 | Inscrição gratuita | 18 |
| FD2 | Redação online | 14 |
| FD3 | Presencial em São Paulo | 23 |
| FD4 | Bacharelado presencial | 22 |
| FD5 | Aulas em 22/02/2027 | 19 |
| FD6 | Faculdade UFAPE | 15 |

### 7.3 Snippets estruturados, chamada e formulário

| Recurso | Decisão | Motivo |
|---|---|---|
| Snippets estruturados | Não criar nesta versão | O Google pede pelo menos 3 valores por cabeçalho [CONFIRMAR]; só há um curso liberado em São Paulo (o noturno está bloqueado) e usar disciplinas como "cursos" pode ser reprovado. Reavaliar quando o noturno desbloquear (cabeçalho com os dois turnos) |
| Chamada | Não criar nesta versão | A conversão otimizada é o cadastro na LP e não há medição de chamada. O número de vendas de São Paulo, (11) 91366-9290, é citado como WhatsApp de vendas em contexto/ufape-geral.md, e a chamada de voz não está confirmada [CONFIRMAR]. A secretaria, (11) 5054-1204, atende de segunda a sexta, das 9h às 18h, e é de dúvidas. Cada clique em chamada gastaria verba sem lead medido. Se a Ufape quiser: usar só o número que atende voz, com o horário da secretaria, e conversão de chamada secundária |
| Formulário de lead do Google | Não criar | Captaria dado pessoal dentro do Google, fora do formulário da LP e do CRM, sem controle do aviso de finalidade (G13) nem do tratamento de candidato menor (G10) |

---

## 8. Localização e público

| Item | Configuração | Fonte ou marca |
|---|---|---|
| Locais | Município de São Paulo e municípios da Região Metropolitana. Lista exata dos municípios: [CONFIRMAR com o comercial de São Paulo] | [SUPOSIÇÃO: Grande São Paulo], gestor 1.1 e MP4 |
| Opção de segmentação | Presença: pessoas que estão ou regularmente estão nos locais (não "presença ou interesse") | [SUPOSIÇÃO de desenho] |
| Exclusão de locais | Nenhuma. Goiânia e Goiás já estão nas negativas de texto | |
| Idade | Anúncio só para 18 anos ou mais. A Busca do Google não tem faixa abaixo de 18 [CONFIRMAR no editor]. **A faixa "desconhecida" pode incluir menores: a decisão é do AG5, com duas opções e validação do jurídico (G10). Até a resposta, vale a opção mais restrita: excluir a faixa "desconhecida"** (falha fechada). Como menor pode ver anúncio de Busca por contexto, o texto não pressiona menor e fala com a família | Gestor 4.5; G10 [CONFIRMAR com o jurídico]; qa G-2 |
| Renda, emprego e outras características | Nenhuma segmentação nem exclusão | Gestor 4.5 |
| Audiências | Nenhuma. Listas de contatos e semelhantes bloqueadas até o jurídico validar (MP7) | |
| Remarketing | Não nesta versão (verba) | Gestor 3.5, linha 4 |

---

## 9. Conversões

| Ação de conversão | Papel | Configuração proposta | Condição para existir |
|---|---|---|---|
| Lead, nome sugerido grad_medvet_lead_lp | **Primária**: é o que as duas campanhas otimizam | Evento de cadastro (envio do formulário) na LP da Graduação, por tag do Google ou importação do GA4 [CONFIRMAR]. Contagem: uma por clique. Janela: 30 dias [SUPOSIÇÃO]. Incluir em "Conversões": sim. Sem valor | G13: URL que recebe a UTM, se o formulário é a inscrição ou só captura de contato, política de privacidade no formulário. MP10: tag testada |
| Matrícula, nome sugerido grad_medvet_matricula_crm | **Secundária, só para leitura**: fora da otimização | Importação offline de conversões do CRM por identificador do clique (gclid), sem e-mail, telefone ou outro dado pessoal. Matrícula é o pagamento da 1ª mensalidade. Janela: 90 dias [SUPOSIÇÃO]. Incluir em "Conversões": não. Sem valor | G13 (o gclid chega ao CRM junto com o lead) e validação do jurídico sobre o uso de dados (G10). Até lá, a matrícula é lida no CRM pela utm_campaign e pelo utm_content, sem enviar nada ao Google |
| Inscrição concluída (opcional) | Secundária, leitura | Só se o formulário da LP for captura de contato e a inscrição acontecer em outra página com evento próprio [CONFIRMAR, G13] | G13 |

Regras:
- Nenhuma campanha é ativada sem a conversão de lead testada (envio de teste aparece no Google Ads e no CRM com a origem). Checklist da seção 14.
- A meta de custo por matrícula (R$ 133,33, MP1) é lida fora do Google, no CRM e no financeiro, por utm_campaign e utm_content (gestor 5).
- Modo de consentimento e aviso de cookies: [CONFIRMAR com o jurídico e a plataforma] antes de ligar a tag.

---

## 10. Nomenclatura e UTM (padrão D11 e D12)

### 10.1 Nomes

Padrão (skill e D12; a Graduação mantém o prefixo grad_): linha_curso_plataforma_objetivo_publico_AAAAMM. Grupo: nome da campanha + "__" + público. Anúncio, igual ao utm_content: conceito_formato_gancho_vN. Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos, sem dado pessoal.

| Nível | Nome |
|---|---|
| Campanha 1 | grad_medvet-integral_google_busca_marca_202611 |
| Grupo 1 | grad_medvet-integral_google_busca_marca_202611__marca |
| Anúncios do grupo 1 | v1-preco_rsa_a_v1 e v3-entrada_rsa_a_v1 |
| Campanha 2 | grad_medvet-integral_google_busca_generica_202611 |
| Grupo 2 | grad_medvet-integral_google_busca_generica_202611__generica |
| Anúncios do grupo 2 | v1-preco_rsa_a_v1 e v3-entrada_rsa_a_v1 |
| Lista de negativas | grad_medvet_negativas_gerais |

Correspondência com o criativos-de-anuncio: v1-preco_rsa_v1 passa a v1-preco_rsa_a_v1 e v3-entrada_rsa_v1 passa a v3-entrada_rsa_a_v1. O bloco de gancho "a" é o gancho A do conceito, o título fixado na posição 1. Troca de gancho por iteração: b ou c (ex.: v1-preco_rsa_b_v1).

### 10.2 UTM

| Parâmetro | Valor |
|---|---|
| utm_source | google (D11) |
| utm_medium | cpc (D11, Google Busca) |
| utm_campaign | nome da campanha (D12) |
| utm_content | nome do anúncio ou do sitelink (D12) |
| utm_term | {keyword} (palavra cadastrada, entregue pelo Google; fica com a grafia da palavra-chave, com acento quando houver [SUPOSIÇÃO: o arquiteto-de-fluxos confere a leitura no GA4 e no CRM]) |

Como montar: URL final limpa, "https://faculdade.ufape.com.br/graduacao" [CONFIRMAR, G13], e **sufixo do URL final completo no nível do anúncio e no nível do sitelink**, porque o sufixo do nível mais baixo prevalece sobre o da campanha [SUPOSIÇÃO, CONFIRMAR no editor]. Sem sufixo no nível da campanha. Auto tagging ligado ao mesmo tempo [CONFIRMAR com o arquiteto-de-fluxos qual dos dois o GA4 e o CRM usam na atribuição].

| Peça | Sufixo do URL final |
|---|---|
| RSA-M1 | utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_marca_202611&utm_content=v1-preco_rsa_a_v1&utm_term={keyword} |
| RSA-M2 | utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_marca_202611&utm_content=v3-entrada_rsa_a_v1&utm_term={keyword} |
| RSA-G1 | utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_generica_202611&utm_content=v1-preco_rsa_a_v1&utm_term={keyword} |
| RSA-G2 | utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_generica_202611&utm_content=v3-entrada_rsa_a_v1&utm_term={keyword} |
| Sitelink SL1 a SL5, em cada campanha | utm_source=google&utm_medium=cpc&utm_campaign=<nome da campanha>&utm_content=<utm_content do sitelink, seção 7.1>&utm_term=sitelink |

Exemplo de URL completo (genérica, entrada):
https://faculdade.ufape.com.br/graduacao?utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_generica_202611&utm_content=v3-entrada_rsa_a_v1&utm_term={keyword}

A squad nunca altera a LP. Origem chegando ao CRM com utm_campaign e utm_content: [CONFIRMAR, G13 e MP10].

---

## 11. Travas (nada sobe, nem em teste, sem elas)

| # | Trava | O que bloqueia | O que libera |
|---|---|---|---|
| 1 | **MP1, MP2 e MP15** do gestor: metas numéricas aprovadas e gasto de R$ 560,00 do Google aprovado, com aprovador | Ativação de qualquer campanha | A ativação em 16/11/2026 |
| 2 | **G8**: campo "turno" do bloco do noturno na página mostra "INTEGRAL" | Campanha e anúncios do noturno (seção 13). Não são montados nesta versão | MP8, depois de G8 corrigido e MP4 aprovado |
| 3 | **G12**: efeito do reajuste de dezembro nos valores de 2027/1 | RSA-M1 e RSA-G1 (os que citam preço) | Ativação deles com G12 respondido. Se o reajuste mudar valores, os dois anúncios pausam e voltam depois de ciclo extra (nova versão, nova contagem, nova aprovação) |
| 4 | **G7**: correção dos textos dos Editais 003/2026 e aprovação humana do texto do desconto (regulação) | RSA-M1, RSA-G1 e o sitelink SL5 | Ativação com G7 respondido |
| 5 | **Datas do Enem**: Enem 2026 informado para 08 e 15/11 e divulgação das notas, ambos [CONFIRMAR no calendário oficial do Inep] | (a) Nada no ar em 08 e 15/11 (a subida é 16/11). (b) Nenhum texto diz ou sugere que a nota do Enem 2026 já pode ser usada, nem fala em "sua nota", "resultado" ou "nota do Sisu". (c) A palavra "veterinária com nota do enem" e a retirada das negativas "enem 2026", "resultado do enem" e "nota do enem 2026" esperam a semana da divulgação das notas. (d) Enem sempre com a condição completa, sem reescrever a regra do edital | Versão de texto da semana E, só com a data confirmada, por nova versão deste arquivo |
| 6 | **G13**: URL da LP que recebe a UTM, se o formulário é a inscrição ou só captura, origem no CRM e política de privacidade no formulário | Conversão de lead, UTM final e a conferência "a página entrega o que o anúncio promete" | Montagem final |
| 7 | **G14**: ninguém nomeado para aprovar anúncios, verba e peças com ato regulatório | Registro de qualquer aprovação deste arquivo | Aprovações dos pedidos da seção 15 |
| 8 | **G10**: tratamento de menor de idade (anúncio de Busca visto por menor, faixa etária "desconhecida", consentimento no CRM, uso de dados na importação de matrícula) | Importação de conversão de matrícula, qualquer lista de contatos e a abertura da faixa "desconhecida" | Importação e faixa "desconhecida", depois da validação do jurídico |
| 9 | **MP4**: públicos 18 ou mais e área geográfica confirmada pelo comercial | Configuração final de locais | Montagem final |
| 10 | **MP10**: tag do Google e conversão de lead testadas | Ativação | Ativação |
| 11 | **qa-de-marketing** (auditoria 11 e conformidade-educacional), previsto para 10/11/2026 | Montagem | Montagem entre 11 e 13/11 (MP11), em pausa |

---

## 12. Metas e critérios de leitura (do gestor-de-midia v3, pendentes de MP1)

| Meta | Valor | Fonte |
|---|---|---|
| Custo por matrícula máximo | R$ 133,33 (R$ 2.000,00 dividido por 15) | gestor 2.3, decisões 15 e 16 |
| CPL máximo, cenário base (meta provisória) | R$ 6,67 [SUPOSIÇÃO de cenário]. Conservador R$ 2,67; otimista R$ 13,33 | gestor 2.4 |
| Custo por inscrito máximo, base | R$ 16,67 [SUPOSIÇÃO de cenário] | gestor 2.4 |

Critérios (regras práticas, não metas; valores do cenário base):
- Pausar anúncio: gasto de R$ 13,33 (2 x CPL máximo) sem nenhum cadastro, depois de 3 dias no ar. Proposta ao humano. Nunca pausar todos os anúncios de um grupo ao mesmo tempo.
- Manter: CPL até R$ 6,67 e passagem lead para inscrito estável.
- Ajustar: CPL entre R$ 6,67 e R$ 8,67 por 2 semanas: trocar texto antes de mexer em palavras; conferir página e rastreamento antes de culpar o algoritmo.
- Revisar a campanha: CPL acima de R$ 8,67 por 2 semanas depois de um ajuste, com o cmo.
- Leitura semanal às segundas, de 23/11/2026 a 22/02/2027. Decisão de desempenho só com 2 semanas seguidas. C1 em 30/11/2026, C2 em 04/01/2027, C3 em 25/01/2027.
- Relatório de termos de pesquisa toda segunda: novas negativas, termos de outra instituição, termos com "sisu" e "enem 2026".

---

## 13. Noturno: reservado e BLOQUEADO (não montar agora)

Faz sentido ter um grupo do noturno só depois de G8 e MP4 resolvidos e de MP8 aprovado. Até lá, o noturno não recebe verba nem campanha, e os termos de turno noturno ficam negativados (seção 5). Estrutura reservada, para o humano não improvisar:

- Campanha: grad_medvet-noturno_google_busca_generica_AAAAMM (AAAAMM do mês do desbloqueio). Grupo: ...__generica. Um grupo, sem campanha de marca própria (EM8: a marca geral fica no integral).
- Sementes [SUPOSIÇÃO]: medicina veterinária noturno são paulo; faculdade de veterinária noturno sp; veterinária à noite sp; curso de veterinária à noite. Volume e CPC: [DADO NÃO FORNECIDO].
- Negativas: lista compartilhada sem as de turno; negativas cruzadas: termos sem "noturno" ou "à noite" ficam no integral.
- Anúncios: RSA-NOT-v1, v2 e v3 do criativos (seção 4.3), com o ajuste de utm_content do D12 e nova contagem. Escolher 2 na montagem. Sem "sem largar o trabalho", sem horário de prática e estágio [CONFIRMAR NO CATÁLOGO] e sem afirmar situação de quem vê.
- Verba: metade da verba semanal do Google do curso, a partir da semana seguinte a MP8 (gestor 1.1). Este arquivo é refeito com a nova diária.

---

## 14. Checklist de montagem (humano executa; gestor-de-midia confere)

Ordem: 1 a 6 até 10/11; 7 a 12 de 11 a 13/11, tudo em pausa; 13 a 15 em 16/11.

- [ ] 1. Pedidos AG1 a AG7 aprovados e aprovador registrado (G14).
- [ ] 2. MP1, MP2, MP15 e MP4 aprovados (seção 11, trava 1).
- [ ] 3. Planejador de palavras-chave consultado: volume e CPC registrados em arquivo de retorno; palavras sem volume retiradas (seção 4).
- [ ] 4. Teto de CPC máximo aprovado pelo gestor-de-midia (AG4); sem ele, não ativar.
- [ ] 5. G13 respondido: URL final, formulário (inscrição ou captura), origem no CRM, política de privacidade.
- [ ] 6. qa-de-marketing conferiu G-1 e G-2 desta versão e aprovou os 4 anúncios e os recursos (auditoria 11 e conformidade-educacional).
- [ ] 7. Tag do Google e conversão de lead criadas, com envio de teste aparecendo no Google Ads e no CRM com utm_campaign e utm_content (MP10). Conversão de matrícula só depois de G13 e G10.
- [ ] 8. Duas campanhas criadas em pausa, com os nomes da seção 10, Rede de Pesquisa, sem parceiros de pesquisa nem Display, locais e idioma da seção 8, data de início 16/11/2026 e de término 21/02/2027. Faixa etária: excluir "desconhecida" até a resposta do AG5.
- [ ] 9. Recursos automáticos, expansão de URL final e AI Max desligados [CONFIRMAR no editor]; sem inserção dinâmica de palavra-chave.
- [ ] 10. Grupos, palavras (seção 4, sem a de nota do Enem ativa) e lista compartilhada de negativas anexada; negativas da marca (5.2) na campanha de marca.
- [ ] 11. Quatro anúncios com as fixações da seção 6, contagens conferidas no editor e sufixo de URL final completo por anúncio (seção 10.2). RSA-M1 e RSA-G1 em pausa até G7 e G12.
- [ ] 12. Sitelinks SL1 a SL4 (SL5 só com G7), frases de destaque e nome da empresa; confirmar que o Google aceitou os PDFs.
- [ ] 13. Conferir: diária da S1 (marca R$ 2,14 e genérica R$ 5,00), teto de CPC, estratégia de lance, data de término e limite de gasto de R$ 560,00 somando as duas campanhas. A conta de anúncios pode ser compartilhada com a Pós [CONFIRMAR]; se for, o limite de gasto da conta não serve de trava, e valem a diária, a data de término e o acompanhamento do gasto acumulado.
- [ ] 14. Conferir o destino de cada anúncio e sitelink: carrega, mostra dados da Ufape, contato e política de privacidade, sem redirecionar para domínio inesperado. Nos sitelinks para PDF (SL2 e SL5), abrir o arquivo e ver se mostra contato e política de privacidade; se não mostrar, trocar o destino para a LP.
- [ ] 15. Ativar em 16/11/2026 e anotar no relatório; trocar a diária toda segunda-feira (seção 3); pausar em 22/02/2027 (MP13).

---

## 15. Pedidos de aprovação humana

Aprovador: [CONFIRMAR, G14]. Nada é feito pela squad: um humano executa no Google Ads.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AG1 | Aprovar a estrutura: 2 campanhas de Busca (marca e genérica), 1 grupo cada, sementes, negativas, localização e configurações das seções 2, 4, 5 e 8 | É o que o gestor encomendou (seção 6 do plano dele) e define o que o humano monta | Sem custo de mídia (campanhas criadas em pausa) | Estrutura pronta e conferida antes da subida | Excluir as campanhas pausadas no Google Ads, por humano |
| AG2 | Aprovar a diária semanal da seção 3 e as datas de início (16/11/2026) e término (21/02/2027), dentro dos R$ 2.000,00 do curso (MP2, MP3), com limite de gasto de R$ 560,00 somando as duas campanhas. Item de reserva: orçamento compartilhado entre marca e genérica, só nas semanas em que uma delas ficar 3 dias seguidos sem impressões, sem mudar o total | Verba por curso (decisão 15); a marca e as semanas de festas ficam com diárias muito baixas. Se a conta for compartilhada com a Pós [CONFIRMAR], o limite de conta não vale como trava | R$ 560,00 no ciclo (R$ 184,00 marca e R$ 376,00 genérica). Nada acima | Gasto semanal conforme a curva do plano | Reduzir ou pausar a diária no editor, por humano |
| AG3 | Aprovar os 4 anúncios responsivos, as fixações, o ato (regulação) e o texto do desconto (regulação, com G7 e G12) | Preço, desconto, Enem e ato passam por aprovação; fixações garantem as condições | Sem custo adicional | Anúncios aprovados para montagem. M1 e G1 só ativam com G7 e G12 | Pausar o anúncio; voltar à versão anterior |
| AG4 | Aprovar o teto de CPC máximo, a partir do Planejador de palavras-chave e da 1ª semana | Sem teto, maximizar cliques gasta a diária em poucos cliques caros; valor [DADO NÃO FORNECIDO] | Dentro da diária | Gasto previsível por clique | Trocar o teto no editor |
| AG5 | Aprovar localização (Grande São Paulo, lista de municípios do comercial), idade 18 ou mais, ausência de audiências e a regra para menor de idade (liga a MP4 e G10). **Decidir a faixa etária "desconhecida" com o jurídico (G10). Opção A, a mais restrita e a que vale até a resposta: excluir "desconhecida"; menos risco de mostrar a menor identificado como sem idade, mas o alcance cai, porque a faixa inclui adultos sem idade conhecida pelo Google (tamanho do corte: [DADO NÃO FORNECIDO]). Opção B: não excluir; mais alcance, com o risco de menor na faixa; só com parecer do jurídico** | ECA, LGPD e políticas do Google; a Busca não tem faixa abaixo de 18 [CONFIRMAR no editor] | Sem custo | Entrega só à praça certa, sem público de menor ou sensível | Editar locais, faixa etária e configurações no editor, por humano |
| AG6 | Aprovar as conversões: lead primária; matrícula secundária por importação offline sem dado pessoal, só depois de G13 e da validação do jurídico | Sem conversão não há leitura nem otimização | Sem custo de mídia | Leitura por campanha e por anúncio | Remover a tag ou a ação de conversão, por humano |
| AG7 | Autorizar a rotina semanal de negativas (adicionar termo fora de escopo, de outra instituição, com "sisu" ou "enem 2026") sem pedido novo a cada vez, sem mexer em verba, lance ou texto | Termo ruim gasta a pouca verba; o pedido por termo seria lento | Sem custo | Menos gasto em busca fora de escopo | Remover a negativa no editor |
| AG8 | Autorizar a subida em 16/11/2026 (MP11 e MP12 do gestor), depois dos itens da seção 11 | Montagem e publicação são de humano | R$ 150,00 na fase 1 (R$ 45,00 marca e R$ 105,00 genérica) | Captação a partir de 16/11 | Pausar as campanhas, por humano |
| AG9 | Aprovar a troca de ativos da fase 4 (seção 6.5) em 01/02/2027 e a troca de diárias de cada fase | Cada fase muda a mensagem | Verba da fase (seção 3) | Mensagem de reta final no prazo | Voltar aos ativos anteriores |
| AG10 | Pausar as duas campanhas em 22/02/2027 (MP13), com a data de término como segunda trava | Fim do ciclo | Encerra o gasto | Relatório final até 05/03/2027 | Reativar no editor, por humano |
| AG11 | Não montar o noturno agora; refazer este arquivo depois de MP8 (G8 e MP4) | Página mostra turno errado no bloco do noturno | Sem custo | Sem anúncio que promete o que a página não mostra | Não se aplica |

---

## 16. Auditorias

**auditorias/11-midia-paga.md**
- [ ] Plano do gestor-de-midia aprovado: aprovação humana pendente (MP1 a MP4).
- [ ] Metas de CPL e custo por matrícula escritas antes de subir: escritas (seção 12); aprovação pendente em MP1.
- [ ] Verba dentro do valor aprovado, com aprovador: R$ 560,00 soma exata (seção 3); aprovação e aprovador pendentes (MP2, G14).
- [x] Nomenclatura padrão em campanhas, grupos e anúncios (seção 10).
- [ ] UTM completas e origem no CRM: UTM completas por anúncio e sitelink (seção 10); URL e chegada ao CRM [CONFIRMAR] (G13, MP10).
- [ ] Conversões do Google configuradas e testadas: desenhadas (seção 9); estado atual [DADO NÃO FORNECIDO].
- [ ] Criativos aprovados na conformidade: qa aprovou com ajustes G-1 e G-2, tratados nesta versão; conferência do qa antes da montagem.
- [x] Anúncios dentro das políticas do Google: sem ponto de exclamação, sem caixa alta excessiva, sem inserção dinâmica, sem recurso automático, sem urgência falsa, sem recurso de preço ou promoção.
- [ ] Nenhum público com menores de 18: sem audiências nem listas; texto sem pressão sobre menor; faixa "desconhecida" excluída até a resposta (AG5); busca vista por menor [CONFIRMAR com o jurídico, G10].
- [x] Spark Ad e post de docente promovido: não se aplicam.
- [ ] Relatório semanal ao cmo: começa em 23/11/2026.
- [x] Sem segmentação discriminatória nem exclusão por atributo sensível.
- [x] Públicos sem dado pessoal sem base legal: importação de matrícula só por gclid e só depois do jurídico.
- [x] Dados de curso conferidos no catálogo e na ficha dos editais.
- [x] Destino de WhatsApp: não há; sem recurso de chamada.
- [x] Números só das fontes fornecidas: verba e metas do gestor; nenhum volume ou CPC.
- [x] Nenhuma alteração na plataforma sem humano: tudo é pedido de aprovação (seção 15).

**auditorias/conformidade-educacional.md**
- [x] Nome, modalidade, duração, turno e carga horária batem com o catálogo (Medicina Veterinária, presencial, integral, 4 anos; 4.195 h e 75 h de atividades complementares não são citadas nos anúncios).
- [x] Status "aberto" no catálogo (Graduação, 2 abertos).
- [x] Modalidade presencial clara; até 30% a distância fica no atendimento, sem esconder.
- [x] Ato como no catálogo, sem reconhecimento: "Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025)".
- [x] Nenhuma nota do MEC, nenhuma frase de certificação, nenhuma promessa de emprego, salário, aprovação ou concurso.
- [x] Enem sempre com a condição completa (média mínima de 300 pontos, edições de 2010 em diante), pelas fixações; redação com a regra de eliminatória e nota mínima 5,0.
- [x] Desconto com valor cheio, valor com desconto, percentual, validade (1º semestre de 2027), regra de renovação com comprovação e "Condições e validade no edital"; regra completa no edital (SL5, com G7). Sem taxa escondida (inscrição gratuita; a matrícula é a 1ª mensalidade).
- [ ] Reajuste de dezembro e erros dos editais: G12 e G7 pendentes (bloqueiam M1 e G1).
- [x] Sem urgência falsa, sem "últimas vagas", sem contagem regressiva.
- [x] Prouni, Fies e financiamento: não aparecem (estão nas negativas).
- [x] Menor de idade: "representante legal" nos anúncios; sem imagem de menor.
- [x] Nenhum dado pessoal neste arquivo.
- [x] Sem comparação com concorrente, sem nome de outra instituição em texto ou palavra-chave, sem lance em concorrente.
- [ ] Formulário com finalidade e política de privacidade: [CONFIRMAR] (G13); a squad não altera a LP.
- [ ] Página de destino entrega o que o anúncio promete: [CONFIRMAR] (G13); PDFs conferidos no item 14 do checklist. O bloco do noturno com turno errado (G8) está fora das campanhas.
- [x] Texto não afirma característica de quem vê.

**Resultado:** rascunho pronto para a conferência do qa nos itens G-1 e G-2. Bloqueados até resposta: ativação de qualquer campanha (MP1, MP2, G14, G13, MP10, MP4), anúncios com preço (G7, G12), noturno (G8, MP8), importação de matrícula e faixa "desconhecida" (G10) e texto de nota do Enem (datas do Enem). Revisado por: anuncios-google (agente), versão 2. Revisão humana: pendente. Data: 27/10/2026.

**Notas para arquivos de outros donos (não alterados por este agente):**
- criativos-de-anuncio-graduacao-2026-10-26.md: o utm_content dos RSA usa a versão como gancho; este arquivo segue o D12 com bloco de gancho (A-C1 do qa-d). O RSA-INT-v3 fixava o título de Enem na posição 2; aqui a posição 1 leva "Enem: Média Mínima 300 Pontos". A descrição "Inscrição gratuita em São Paulo..." deu lugar à linha do menor de idade.
- gestor-de-midia-graduacao-2026-10-26.md: a divisão 30% e 70% (40% e 60% na reta final) entre marca e genérica está proposta aqui; o gestor confirma na próxima versão. O gestor lista 3 anúncios na genérica; aqui são 2 (o terceiro, v2-pratica, entra na fase 2). A 4.8 dele pede limite de conta de R$ 4.000,00: no Google vale R$ 560,00 somando as duas campanhas.

---

## Lista 1. Fatos (com fonte)

- Medicina Veterinária: bacharelado, presencial, São Paulo; integral de 4 anos (R$ 10.000,00 por R$ 5.000,00 por mês, 50%) e noturno de 5 anos; 4.195 h mais 75 h de atividades complementares; Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025), conforme o Edital 002/2026 (contexto/catalogo-de-cursos.md, seção 1).
- Desconto: 6 mensalidades, só no 1º semestre de 2027, todas as formas de ingresso, renovação pedida a cada semestre com comprovação, perda no mês pago com atraso, sem acúmulo com programa governamental (contexto/cursos/graduacao/editais-2027-1.md, Edital 003/2026).
- Inscrição gratuita desde 17/08/2026; redação online a qualquer momento depois da inscrição, eliminatória, nota mínima 5,0; Enem com média mínima de 300 pontos, edições de 2010 em diante; matrícula eletrônica a partir de 2 dias depois do resultado, com a 1ª mensalidade e a assinatura digital; documentos em até 30 dias; aulas em 22/02/2027 (editais 002 e 004/2026, ficha dos editais).
- Candidato menor de idade precisa do aceite do representante legal na inscrição e na matrícula (Edital 002/2026, ficha dos editais).
- Os editais não preveem ingresso pelo Sisu, não trazem data-limite de inscrição, nota do MEC nem número de vagas restantes (ficha dos editais).
- Links dos editais em PDF (catálogo, seção 1): edital-vestibular-2027.pdf e edital-descontos-2027.pdf em faculdade.ufape.com.br/uploads/arquivo.
- Verba do Google R$ 560,00 no ciclo de 16/11/2026 a 21/02/2027, por fase e semana (gestor-de-midia v3, seção 3.3; estrategia-de-midia v3, 2.4). Metas: R$ 133,33 por matrícula; CPL base R$ 6,67 (gestor v3, 2.3 e 2.4).
- Canais e bloqueios: Google Search só na Medicina Veterinária; Performance Max, YouTube e TikTok fora; noturno bloqueado por G8 e MP4; anúncio só para 18 anos ou mais (gestor v3, 3.1 e 4.5).
- Padrão D11 (Google: utm_source google e utm_medium cpc) e D12 (utm_campaign igual ao nome da campanha; anúncio conceito_formato_gancho_vN; prefixo grad_) (cmo-geral-2026-10-26.md, seção 12.7).
- Secretaria: (11) 5054-1204, segunda a sexta, 9h às 18h; vendas São Paulo: (11) 91366-9290 (contexto/ufape-geral.md).
- Recontagem do qa: 100 itens de texto do Google, 0 divergências, 0 acima do limite (qa-de-marketing-graduacao-2026-10-27-campanhas.md, 2.1).
- 16/11/2026 e 22/02/2027 são segundas-feiras (calendário).

## Lista 2. Suposições

- [SUPOSIÇÃO] Todas as palavras-chave sementes, as negativas ampliadas e as correspondências escolhidas.
- [SUPOSIÇÃO de desenho] Divisão da verba do Google entre marca e genérica (30% e 70%; 40% e 60% na reta final); parceiros de pesquisa e Display desligados; sem programação horária; "presença" (e não "presença ou interesse") na localização.
- [SUPOSIÇÃO] Grande São Paulo como área de entrega; lista de municípios a confirmar com o comercial.
- [SUPOSIÇÃO de cenário, do gestor] CPL base de R$ 6,67 e taxas de conversão do funil, sem histórico nem CRM.
- [SUPOSIÇÃO] Janelas de conversão de 30 dias (lead) e 90 dias (matrícula).
- [SUPOSIÇÃO] Diárias abaixo de R$ 2,00 podem não entregar.
- [SUPOSIÇÃO] O gargalo do funil é o inscrito que não faz a redação (hipótese do cmo); a objeção principal é mensalidade alta (contexto da linha).
- [SUPOSIÇÃO] O {keyword} do Google chega ao GA4 e ao CRM com a grafia cadastrada, com acento quando houver.
- [SUPOSIÇÃO, CONFIRMAR no editor] Regras de plataforma do Google citadas neste arquivo: máximo de 15 títulos e 4 descrições por anúncio; "Força do anúncio" que pode ficar em "Média" ou "Ruim" com fixações; a Busca não tem faixa etária abaixo de 18; o sufixo de URL de nível mais baixo prevalece sobre o da campanha; o Google pode gastar até o dobro da diária em um dia; orçamento compartilhado entre campanhas de Busca.
- [SUPOSIÇÃO] A conta de anúncios do Google pode ser compartilhada com campanhas da Pós, o que tira o valor do limite de conta como trava.

## Lista 3. Dados que faltam

- [DADO NÃO FORNECIDO] Volume de busca e CPC estimado de cada palavra (Planejador de palavras-chave ou exportação); teto de CPC máximo; pesquisa do departamento 03; histórico de CPL; estado da tag e das conversões do Google; ID da conta; lista de concorrentes da Ufape; tamanho do corte de alcance ao excluir a faixa etária "desconhecida".
- [CONFIRMAR] MP1 e MP15 (metas, leitura de "valor do curso", meta de 15 e turma mínima de 30); MP2 (gasto de R$ 560,00) e aprovador nomeado (G14).
- [CONFIRMAR] G13: URL da LP que recebe a UTM, se o formulário é a inscrição ou só captura de contato, origem no CRM, política de privacidade no formulário, gclid chegando ao CRM.
- [CONFIRMAR] G12: efeito do reajuste de dezembro nos valores de 2027/1. G7: correção dos textos dos Editais 003/2026. G8: campo turno do noturno na página.
- [CONFIRMAR] Datas do Enem 2026 (08 e 15/11 informadas) e da divulgação das notas, no calendário oficial do Inep.
- [CONFIRMAR] G10, com o jurídico: faixa etária "desconhecida" no Google (AG5), consentimento de candidato menor no CRM, anúncio de Busca visto por menor e uso de dados na importação de matrícula; modo de consentimento da tag.
- [CONFIRMAR] Área geográfica e lista de municípios com o comercial de São Paulo (MP4).
- [CONFIRMAR] Se a conta de anúncios do Google é só da Graduação ou compartilhada com a Pós.
- [CONFIRMAR] Se o número de vendas de São Paulo atende chamada de voz; logotipo aprovado para o nome da empresa; se os PDFs dos editais mostram contato e política de privacidade.
- [CONFIRMAR NO CATÁLOGO] Nomes das disciplinas do 1º semestre (Anatomia, Práticas Hospitalares, Projeto Extensionista I) como dado de catálogo; horário de prática e estágio do noturno.
- [CONFIRMAR no editor e na Central de Ajuda do Google Ads] Limites de caracteres, aceitação de PDF em sitelink, número mínimo de valores de snippet, regra de gasto diário, desligamento de AI Max e ativos automáticos, comportamento do sufixo de URL.

---

## Próximo passo

Arquivo: saidas/11-midia-paga/anuncios-google-graduacao-2026-10-26.md (versão 2). Próximo agente: **qa-de-marketing**, que confere só G-1 e G-2 antes da aprovação humana e da montagem entre 11 e 13/11/2026. Nada é publicado, enviado ou pago sem aprovação humana.
