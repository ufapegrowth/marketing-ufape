# Plano de mídia paga: Graduação 2027/1 (Medicina Veterinária e Pedagogia)

- Agente: gestor-de-midia (chefe do departamento 11, Mídia Paga, reporta ao cmo)
- Linha: graduacao
- Data: 26/10/2026 (segunda-feira)
- Versão: 3, aplica as decisões 15 e 16 do CEO (docs/execucao-2026-10-26.md): verba estimada de R$ 2.000,00 de mídia por curso no ciclo de captação e meta de pelo menos 15 matrículas por curso, com meta em reais de 15 vezes o valor do curso. Versão 2 foi a correção do QA (veredito A4 de saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-a.md); as correções dela continuam valendo.
- Workflow: /campanha-de-vestibular, etapa 4 de 8 (plano do chefe da mídia paga; o plano detalhado por semana é do estrategia-de-midia, seção 6)
- Liberações cobertas:
  - G1: Edital nº 002/2026 (Vestibular 2027) + Graduação em Medicina Veterinária, São Paulo, integral e noturno
  - G2: Edital nº 004/2026 (Processo Seletivo 2027.1 Goiânia) + Graduação em Pedagogia, Goiânia, noturno
- Status: rascunho para aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. A verba das decisões 15 e 16 é estimada: continua valendo que nada é pago sem aprovação humana (MP2). Toda ação em gerenciador de anúncios é feita por humano, depois da aprovação.
- Entradas lidas:
  - docs/execucao-2026-10-26.md (decisões 1 a 17, em especial 15 e 16)
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/graduacao.md
  - contexto/catalogo-de-cursos.md (seção 1, Graduação)
  - contexto/cursos/graduacao/editais-2027-1.md (mensalidade, descontos, duração e regras)
  - .claude/agents/gestor-de-midia.md e .claude/agents/estrategia-de-midia.md
  - .claude/skills/metas-de-custo/SKILL.md
  - .claude/skills/estrutura-de-campanha-paga/SKILL.md
  - templates/briefing-de-midia.md
  - saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 12: D11 e D12, padrão de UTM)
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-graduacao-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-graduacao-2026-10-26.md
  - saidas/11-midia-paga/estrategia-de-midia-graduacao-2026-10-26.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-26-a.md (veredito A4 e conferência de dados)
  - auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md
- Regra de fonte: preço, turno, duração, modalidade e ato vêm do catálogo (seção 1); datas, vagas, turma mínima, número de parcelas e regras de desconto vêm da ficha dos editais 2027/1. Verba e meta de matrículas vêm das decisões 15 e 16 do CEO. Não existe histórico de CPL, exportação de plataforma nem número de CRM: taxas de conversão são [SUPOSIÇÃO de cenário] ou [CONFIRMAR]. Nenhum dado pessoal neste arquivo.

---

## Mudanças desta versão

| # | O que mudou | Onde | Motivo |
|---|---|---|---|
| 1 | Verba deixa de ser [CONFIRMAR]: R$ 2.000,00 por curso, R$ 4.000,00 na Graduação (Medicina Veterinária e Pedagogia), estimada e ainda dependente de aprovação humana | 0, 1, 3, 7 | Decisão 15 |
| 2 | Meta de matrículas: pelo menos 15 por curso; meta em reais = 15 x valor do curso, com as seis leituras possíveis de "valor do curso" calculadas e a escolha marcada [CONFIRMAR com o CEO] | 2.1 e 2.2 | Decisão 16 |
| 3 | Custo máximo por matrícula numérico: R$ 133,33 por curso (R$ 2.000,00 / 15). CPL e custo por inscrito máximos em três cenários | 2.3 e 2.4 | Decisões 15 e 16 |
| 4 | Divisão da verba em reais por canal, fase e semana até 22/02/2027 | 3.2 a 3.4 | Decisão 15 |
| 5 | TikTok e YouTube saem por verba: R$ 2.000,00 não sustentam um terceiro canal com volume para decidir em 2 ou 3 semanas. Pedidos MP5 e MP6 ficam suspensos | 3.1, 4.3, 6, 7 | Regra do método (passo 2) |
| 6 | A verba é por curso: integral e noturno da Medicina Veterinária dividem os mesmos R$ 2.000,00. A divisão por recorte proporcional à receita (EM1 do estrategia-de-midia, 52,5%, 42,0% e 5,5%) deixa de valer | 1, 3.3 | Decisão 15 |
| 7 | Nova seção "Onde R$ 2.000,00 limitam o volume e o que fazer" | 3.5 | Pedido do orquestrador |
| 8 | C0 de 30/10/2026: MP1 passa a ser a aprovação das metas numéricas desta versão (não mais o preenchimento do formulário) | 5, 7 | Metas agora existem |
| 9 | Conflito registrado: meta do CEO (15 por curso) x turma mínima do edital (30 por turma) e meta do plano do cmo (30 por turma) | 0, 2.1, 7 (MP15) | Coerência entre decisões |
| 10 | UTM conferida contra D11 e D12 da seção 12 do plano do cmo: sem mudança (já seguia paid_social, cpc e o prefixo grad_) | 4.6 | Conferência pedida |

---

## 0. Situação em uma frase

Com R$ 2.000,00 por curso e meta de 15 matrículas, a mídia pode gastar no máximo R$ 133,33 por matrícula; isso é muito menos do que qualquer leitura do valor do curso, então a conta econômica fecha, mas a verba compra pouco volume (cerca de R$ 142,86 por semana por curso), o que obriga a um canal principal (Meta), busca do Google pequena, TikTok e YouTube fora, e a ativação da base de inscritos como parte da meta.

**Aviso ao cmo (regra do método, passo 1):**
1. A conta econômica fecha em todas as leituras: R$ 133,33 por matrícula é 2,67% da 1ª mensalidade com desconto do integral (R$ 5.000,00), 3,33% da do noturno (R$ 4.000,00) e 25,40% da da Pedagogia (R$ 525,00).
2. O que não se sabe é se o CPL necessário é alcançável. No cenário base [SUPOSIÇÃO de cenário], o CPL máximo é R$ 6,67; não há histórico da conta para dizer se a Meta entrega cadastro de vestibular nesse custo em São Paulo e em Goiânia. A primeira leitura válida sai entre a 2ª e a 3ª semana no ar.
3. Conflito a decidir [CONFIRMAR com o CEO, MP15]: a meta do CEO é 15 matrículas por curso; o edital exige turma mínima de 30 por turma (Medicina Veterinária tem duas turmas, integral e noturno) e o plano do cmo tem como meta principal 30 por turma. Este plano usa 15 por curso como meta da mídia paga (decisão 16) e não muda a meta do cmo.

---

## 1. Briefing de mídia por liberação (formato templates/briefing-de-midia.md)

### 1.1 G1: Medicina Veterinária, São Paulo (integral e noturno, uma verba só)

BRIEFING DE MÍDIA

| Campo | Conteúdo |
|---|---|
| Nome da campanha | Vestibular 2027 Medicina Veterinária SP. Campanhas-mãe: grad_medvet-integral e grad_medvet-noturno (nomes completos na seção 4) |
| Linha | Graduação |
| Curso | Medicina Veterinária, bacharelado, presencial, São Paulo. Integral, 4 anos; noturno, 5 anos; 4.195 h + 75 h de atividades complementares (catálogo). Ato: Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025) |
| Objetivo e conversão otimizada | Cadastro na LP da Graduação (evento de inscrição ou de lead, conforme o formulário). [CONFIRMAR se o formulário da LP já é a inscrição ou só captura de contato, G13 do cmo]. Sem campanha de mensagem para WhatsApp: o destino de toda peça é a LP |
| Meta de matrículas | Pelo menos 15 matrículas no curso, somando integral e noturno (decisão 16). A matrícula de fato é o pagamento da 1ª mensalidade (inscrição gratuita pelo edital). Divisão entre turnos: [CONFIRMAR com o CEO]. Turma mínima do edital: 30 por turma (MP15) |
| Meta em reais | 15 x valor do curso, com a leitura de "valor do curso" [CONFIRMAR com o CEO]: de R$ 60.000,00 a R$ 9.000.000,00 conforme a leitura e o turno (seção 2.2) |
| Verba aprovada e quem aprovou | R$ 2.000,00 estimados no ciclo (decisão 15 do CEO, 26/10/2026). Aprovação do gasto: pendente (MP2). Aprovador nomeado: [CONFIRMAR] (G14 do cmo) |
| Período | Ciclo do plano do cmo: 16/11/2026 a 21/02/2027 (14 semanas); pausa pedida para 22/02/2027. Período exato do ciclo: [CONFIRMAR] (decisão 15) |
| Divisão de verba | Meta 72%, Google Search 28% no ciclo (R$ 1.440,00 e R$ 560,00), por fase e semana na seção 3. TikTok e YouTube fora por verba |
| Meta de CPL | Cenário base [SUPOSIÇÃO]: R$ 6,67. Conservador R$ 2,67; otimista R$ 13,33 (seção 2.4) |
| Meta de custo por matrícula | R$ 133,33 (R$ 2.000,00 / 15) |
| Taxa lead para matrícula usada | Base 5% [SUPOSIÇÃO de cenário]; conservador 2%; otimista 10%. Trocar pelo número do CRM (G2 do cmo) assim que existir, antes da subida |
| Públicos e persona | Anúncio só para 18 anos ou mais: pais e responsáveis e candidatos adultos, Grande São Paulo [SUPOSIÇÃO: área a confirmar com o comercial]. Persona do contexto: jovem de 17 a 22 anos e família [SUPOSIÇÃO]; parte do público é menor de idade (ECA e LGPD): o menor não é público de anúncio, a mensagem fala com "você e sua família" e lembra o aceite do representante legal (Edital 002/2026) |
| Canais e papel | Meta (Instagram e Facebook): criação de demanda e remarketing. Google Search: demanda existente (marca e um grupo genérico) |
| Criativos | Integral: v1-preco, v2-pratica, v3-entrada (ficha de oferta, seção 5); noturno: os mesmos conceitos com o ângulo do noturno. No máximo 3 conceitos ativos por curso por vez (seção 3.5) |
| Destino | LP da Graduação, faculdade.ufape.com.br/graduacao [CONFIRMAR com a plataforma qual URL recebe a UTM, G13]. A squad nunca altera a LP |
| Rastreamento | Pixel e API de Conversões (Meta), tag e conversão do Google Ads, UTM completa (D11 e D12), origem chegando ao CRM. Estado atual: [DADO NÃO FORNECIDO] |
| Checagem semanal | Segundas, de 23/11/2026 a 22/02/2027, no relatório ao cmo |
| Critérios de decisão | Seção 5 |
| Quem monta | Humano indicado pela Ufape [CONFIRMAR], a partir das estruturas de anuncios-meta e anuncios-google |
| Aprovações | Seção 7 |

**Noturno: anúncio pago bloqueado.** Desbloqueia quando as duas condições forem cumpridas: (1) campo turno do bloco do noturno corrigido na página (hoje mostra "INTEGRAL", G8 do cmo); (2) público adulto aprovado (MP4). Enquanto bloqueado, os R$ 2.000,00 do curso rodam só no integral. Depois do desbloqueio (MP8), a verba semanal do curso em cada canal passa a ser dividida 50% integral e 50% noturno [SUPOSIÇÃO de desenho], com leitura da meta no curso (15) e acompanhamento por turno pelo utm_campaign. Criativos do noturno sem prometer "sem largar o trabalho" nem horário de prática e estágio [CONFIRMAR NO CATÁLOGO]. Sem segmentação por emprego, renda ou situação profissional.

### 1.2 G2: Pedagogia, Goiânia

| Campo | Conteúdo |
|---|---|
| Nome da campanha | Processo Seletivo 2027.1 Pedagogia Goiânia. Campanha-mãe: grad_pedagogia |
| Curso | Pedagogia, licenciatura, presencial, Goiânia, noturno, 4 anos (catálogo e Edital 004/2026). Carga horária fora de toda peça: [CONFIRMAR NO CATÁLOGO] (3.440 h no site, 3.640 h no edital). Ato: Portaria nº 992, de 08/12/2022 (D.O.U. 20/12/2022) |
| Status do anúncio pago | **Bloqueado.** Desbloqueia com: (1) página de Pedagogia corrigida (textos de modelo, egresso copiado e docentes de outro curso, G6 do cmo); (2) público adulto aprovado (MP4); (3) metas numéricas desta versão aprovadas (MP1) |
| Modelo de estrutura | Local (Goiânia), enxuto: 1 campanha Meta com 1 conjunto. Google Search fora por verba (seção 3.1) |
| Meta de matrículas | Pelo menos 15 (decisão 16). Turma mínima do edital: 30 (MP15). Vagas: 80 |
| Meta em reais | 15 x valor do curso [CONFIRMAR leitura com o CEO]: de R$ 7.875,00 a R$ 756.000,00 (seção 2.2) |
| Verba | R$ 2.000,00 estimados no ciclo (decisão 15), 100% Meta. Aprovação do gasto: MP2 |
| Metas de custo | Custo por matrícula máximo R$ 133,33; CPL base R$ 6,67 [SUPOSIÇÃO de cenário] (seção 2.4) |
| Públicos | 18 anos ou mais, Goiânia e região metropolitana [SUPOSIÇÃO: raio a confirmar com o comercial de Goiânia], público amplo. Sem segmentação por emprego ("trabalha em escola") nem por renda. Persona adulta, mas a regra de 18+ vale igual (LGPD) |
| Canais | Meta. Google Search, TikTok, YouTube e LinkedIn fora (seção 3.1) |
| Criativos | Até 3 conceitos ativos por vez entre p1-noite, p2-pratica, p3-preco e p4-ato (prioridade: p1-noite, p3-preco com desconto completo, p4-ato), sem carga horária, sem docentes, sem endereço até confirmação |
| Destino | faculdade.ufape.com.br/graduacao/pedagogia [CONFIRMAR, G13] |
| Restante | Igual ao G1 |

---

## 2. Metas (decisões 15 e 16, skill metas-de-custo)

As metas são limites, não previsão de resultado. Conta separada por curso, nunca somada. Valores em reais.

### 2.1 Dados de entrada

| Dado | Medicina Veterinária integral | Medicina Veterinária noturno | Pedagogia | Fonte |
|---|---|---|---|---|
| Mensalidade cheia | R$ 10.000,00 | R$ 10.000,00 | R$ 1.050,00 | catálogo; Editais 003/2026 |
| Mensalidade com desconto (1º semestre de 2027) | R$ 5.000,00 (50%) | R$ 4.000,00 (60%) | R$ 525,00 (50%) | catálogo; Editais 003/2026 |
| Parcelas por semestre | 6 | 6 | 6 | Editais 002, 003 e 004/2026 |
| Duração | 4 anos (8 semestres, 48 mensalidades) | 5 anos (10 semestres, 60 mensalidades) | 4 anos (8 semestres, 48 mensalidades) | catálogo; editais |
| Taxa de matrícula | Não há: a matrícula é confirmada com o pagamento da 1ª mensalidade | idem | idem | editais |
| Inscrição | Gratuita | Gratuita | Gratuita | editais |
| Validade do desconto | Só o 1º semestre de 2027; renovação semestral com comprovação | idem | idem | Editais 003/2026 |
| Reajuste | Em dezembro de cada ano; efeito em 2027/1 [CONFIRMAR, G12] | idem | idem | Edital 002/2026 |
| Meta de matrículas | 15 no curso, somando os dois turnos | (no curso) | 15 | decisão 16 |
| Verba de mídia no ciclo | R$ 2.000,00 no curso | (no curso) | R$ 2.000,00 | decisão 15 |
| Turma mínima | 30 | 30 | 30 | editais |

### 2.2 O que é "valor do curso" na Graduação [CONFIRMAR com o CEO qual leitura ele quis dizer]

Na Pós, o catálogo traz um preço do curso; na Graduação, o catálogo traz só a mensalidade ("Investimento (site)"). Por isso "valor do curso" tem mais de uma leitura. Todas abaixo usam só catálogo e editais, sem reajuste e sem evasão (as duas coisas reduzem ou mudam o número e estão [CONFIRMAR]).

**Valor por matrícula em cada leitura**

| Leitura | Como se calcula | Integral | Noturno | Pedagogia |
|---|---|---|---|---|
| A. 1ª mensalidade com desconto (a matrícula de fato, pela decisão 16; é o "investimento" que o catálogo mostra) | 1 x mensalidade com desconto | R$ 5.000,00 | R$ 4.000,00 | R$ 525,00 |
| B. 1º semestre com desconto (única receita que o edital garante com o preço anunciado) | 6 x mensalidade com desconto | R$ 30.000,00 | R$ 24.000,00 | R$ 3.150,00 |
| C1. Primeira anualidade, com o desconto renovado no 2º semestre | 12 x mensalidade com desconto | R$ 60.000,00 | R$ 48.000,00 | R$ 6.300,00 |
| C2. Primeira anualidade, sem renovação no 2º semestre | 6 x com desconto + 6 x cheia | R$ 90.000,00 | R$ 84.000,00 | R$ 9.450,00 |
| D1. Mensalidade x duração, com o desconto renovado em todos os semestres | mensalidade com desconto x mensalidades do curso (48, 60, 48) | R$ 240.000,00 | R$ 240.000,00 | R$ 25.200,00 |
| D2. Mensalidade x duração, pelo valor cheio | mensalidade cheia x mensalidades do curso (48, 60, 48) | R$ 480.000,00 | R$ 600.000,00 | R$ 50.400,00 |

**Meta em reais (15 x valor do curso)**

| Leitura | Medicina Veterinária, se as 15 forem do integral | Medicina Veterinária, se as 15 forem do noturno | Pedagogia |
|---|---|---|---|
| A | R$ 75.000,00 | R$ 60.000,00 | R$ 7.875,00 |
| B | R$ 450.000,00 | R$ 360.000,00 | R$ 47.250,00 |
| C1 | R$ 900.000,00 | R$ 720.000,00 | R$ 94.500,00 |
| C2 | R$ 1.350.000,00 | R$ 1.260.000,00 | R$ 141.750,00 |
| D1 | R$ 3.600.000,00 | R$ 3.600.000,00 | R$ 378.000,00 |
| D2 | R$ 7.200.000,00 | R$ 9.000.000,00 | R$ 756.000,00 |

Na Medicina Veterinária, a meta em reais do curso fica entre as duas colunas, conforme a mistura de turnos das 15 matrículas: soma, matrícula a matrícula, do valor do turno de cada uma.

**Leitura provisória até o CEO responder [SUPOSIÇÃO]:** B (1º semestre com desconto), porque é a única receita por matrícula que o edital garante com o preço anunciado e é a mesma base usada nas versões anteriores deste plano. A leitura escolhida muda só a meta em reais. Ela **não muda** o custo máximo por matrícula nem o CPL máximo desta versão, que saem da verba e das 15 matrículas.

### 2.3 Custo máximo por matrícula

**Conta (igual nos dois cursos):** custo por matrícula máximo = verba do curso / matrículas da meta = R$ 2.000,00 / 15 = **R$ 133,33**.

- Esta é a meta oficial de custo por matrícula da mídia paga, escrita antes de subir. É conservadora: supõe que a mídia traz as 15 matrículas sozinha. Se a base de inscritos desde 17/08/2026 e o orgânico trouxerem parte (M menor que 15), a meta não é afrouxada depois de subir; a sobra vira economia ou vai a pedido de aprovação.
- Teste de viabilidade econômica (skill metas-de-custo, passo 4): o teto absoluto, sem custo variável e sem margem, é o próprio valor por matrícula da leitura escolhida. Mesmo na leitura mais baixa (A), o teto é R$ 5.000,00, R$ 4.000,00 e R$ 525,00, todos acima de R$ 133,33. Custo variável por aluno (V) e margem desejada (Md) continuam [CONFIRMAR], mas só mudariam a conclusão se V + Md passassem de R$ 391,67 por matrícula na Pedagogia na leitura A (R$ 525,00 menos R$ 133,33). A conta fecha: o limite é a verba, não a margem.
- Peso da verba sobre a meta em reais: Medicina Veterinária, de 2,67% (leitura A, integral) a 0,02% (leitura D2, noturno); Pedagogia, de 25,40% (leitura A) a 0,26% (leitura D2).
- Risco de caixa: a verba sai entre novembro de 2026 e fevereiro de 2027; a receita entra mês a mês a partir da matrícula (vencimento no dia 10).

### 2.4 CPL e custo por inscrito máximos em três cenários

Taxas de conversão: não há número do CRM nem histórico da conta (G2 do cmo). Os valores abaixo são **[SUPOSIÇÃO de cenário]**, escolhidos pelo gestor-de-midia para cobrir uma faixa larga e mostrar a sensibilidade; não são benchmark de mercado nem meta. Origem: nenhuma fonte externa foi fornecida; valores redondos para o conservador ficar abaixo e o otimista acima do base. Substituir pelos números do CRM (inscritos, avaliados, aprovados e matriculados desde 17/08/2026) antes da subida, em MP1. As mesmas taxas valem para os dois cursos até o CRM mostrar diferença.

| Cenário | Lead para inscrito [SUPOSIÇÃO] | Inscrito para matrícula [SUPOSIÇÃO] | Lead para matrícula (tc) | Custo por matrícula máximo | **CPL máximo** = R$ 133,33 x tc | **Custo por inscrito máximo** = R$ 133,33 x (inscrito para matrícula) | Leads necessários (15 / tc) | Inscritos necessários |
|---|---|---|---|---|---|---|---|---|
| Conservador | 20% | 10% | 2% | R$ 133,33 | R$ 2,67 | R$ 13,33 | 750 | 150 |
| Base | 40% | 12,5% | 5% | R$ 133,33 | R$ 6,67 | R$ 16,67 | 300 | 120 |
| Otimista | 50% | 20% | 10% | R$ 133,33 | R$ 13,33 | R$ 26,67 | 150 | 75 |

Valores por curso (iguais para Medicina Veterinária e Pedagogia, porque verba e meta são iguais). Conferência: CPL máximo x leads necessários = R$ 2.000,00 em cada cenário.

- **Se o formulário da LP for a própria inscrição (G13):** lead = inscrito, e a meta de CPL passa a ser a coluna "custo por inscrito máximo" (R$ 13,33, R$ 16,67 e R$ 26,67).
- **Custo por conversa de WhatsApp máximo:** não se aplica (não há campanha de mensagem). Se um dia houver: R$ 133,33 x taxa conversa para matrícula [CONFIRMAR].
- **Meta oficial para a subida:** cenário base, até o CRM trazer as taxas reais (MP1). Recomendação do gestor: aprovar o base como meta provisória e trocar pelas taxas reais uma única vez, antes de 16/11/2026, nunca depois de a campanha subir.
- **Leitura semanal:** tc mínima para um CPL observado caber na meta = CPL observado / R$ 133,33 (fórmula 11 abaixo).

### 2.5 Fórmulas (conta aberta, para trocar as suposições)

1. Custo por matrícula máximo: CPMmax = verba do curso / matrículas da meta = R$ 2.000,00 / 15
2. CPL máximo: CPLmax = CPMmax x tc
3. Custo por inscrito máximo: CPImax = CPMmax x (inscrito para matrícula)
4. Leads necessários: L = 15 / tc
5. Inscritos necessários: I = 15 / (inscrito para matrícula)
6. Verba semanal do canal (seção 3.3) / CPLmax = leads por semana que a verba compra
7. Verba diária sugerida = verba semanal do canal / 7
8. Meta em reais = 15 x valor do curso na leitura escolhida (2.2)
9. Teto econômico absoluto por matrícula = valor por matrícula da leitura escolhida, menos V, menos Md ([CONFIRMAR])
10. Se a mídia precisar trazer M matrículas (menos de 15, com a base e o orgânico): CPMmax continua R$ 133,33 como meta escrita; a diferença vira economia
11. tc mínima = CPL observado / CPMmax

### 2.6 Orçamento de teste

- Por conceito de criativo, antes de julgar: de 1,5 a 3 vezes o CPLmax (regra prática, não meta). Base: de R$ 10,00 a R$ 20,00 por conceito; conservador: de R$ 4,00 a R$ 8,00; otimista: de R$ 20,00 a R$ 40,00.
- Fase 1 (16/11 a 06/12/2026, R$ 600,00 por curso): toda funciona como teste, com 3 conceitos por curso.
- Da fase 2 em diante: 80% da verba semanal para os conceitos validados e 20% para conceito novo [regra prática, SUPOSIÇÃO de desenho].
- Condição de volume (regra prática do método): verba semanal do canal x 3 maior ou igual a conceitos ativos x 1,5 x CPLmax. Medicina Veterinária, Meta na fase 1: R$ 150,00 x 3 = R$ 450,00, contra 3 x 1,5 x R$ 6,67 = R$ 30,00 no base: passa. Google Search: R$ 50,00 x 3 = R$ 150,00 contra R$ 30,00: passa. Pedagogia, Meta: R$ 200,00 x 3 = R$ 600,00: passa. O limite real não é essa condição, e sim o volume absoluto (seção 3.5).

### 2.7 Frase para a diretoria

"Com R$ 2.000,00 por curso e meta de 15 matrículas, podemos gastar até R$ 133,33 para trazer cada aluno, o que é bem menos do que a primeira mensalidade de qualquer um dos dois cursos. A conta fecha. O risco é outro: R$ 2.000,00 compram poucos contatos por semana, então vamos concentrar a verba em um canal, usar a base de inscritos que já temos e decidir com números reais a partir da 3ª semana. Precisamos que o CEO diga qual é o 'valor do curso' para fechar a meta em reais e que o CRM nos passe as taxas reais do funil."

---

## 3. Canais, verba por fase e semana

### 3.1 Decisão de canais (com R$ 2.000,00 por curso)

| Canal | Medicina Veterinária | Pedagogia | Motivo |
|---|---|---|---|
| Meta (Instagram e Facebook) | **Ativo** (integral; noturno bloqueado até G8 e MP4) | **Ativo, bloqueado até G6, MP4 e MP1** | Canal principal de criação de demanda, já usado pela Ufape (ufape-geral.md). Facebook alcança pais e responsáveis e adultos de Goiânia [SUPOSIÇÃO]. Aceita público amplo 18+ por região e remarketing da LP |
| Google Search | **Ativo, pequeno**: busca de marca e um grupo genérico ("faculdade de veterinária em SP" e variações) | **Fora por verba** | Medicina Veterinária: captura quem já procura o curso; R$ 560,00 no ciclo. Pedagogia: com R$ 2.000,00, dividir verba tira volume da Meta, e o volume de busca local é [DADO NÃO FORNECIDO]; volta só com pedido de verba extra ou dado de volume |
| Google Performance Max | Fora | Fora | Precisa de volume de conversão que a conta não tem, controla menos público (risco de entrega para menores) e mistura canais |
| YouTube | **Fora por verba** (antes condicionado) | Fora | Com cerca de R$ 11,25 por semana no aquecimento (15% dos R$ 300,00 da fase 2, em 4 semanas), não gera volume para decidir em 2 ou 3 semanas. Shorts seguem no orgânico (plano do cmo) |
| TikTok | **Fora por verba** (antes teste condicionado) | Fora | Um terceiro canal com cerca de R$ 30,00 por semana não sai do aprendizado nem permite leitura em 3 semanas; parte da persona é menor de idade, o que pede cuidado extra (ECA e LGPD). Volta como pedido de verba extra ao cmo se a Meta bater a meta de CPL e houver perfil e produção (G11) |
| LinkedIn | Fora | Fora | Plano do cmo. Sem verba para canal de custo alto |

Resultado: Medicina Veterinária com Meta e Google Search; Pedagogia só com Meta. Os 8 canais da linha já foram avaliados pelo cmo (seção 4 do plano dele); aqui só os pagos. O orgânico, o WhatsApp e a ativação da base seguem no plano do cmo e são parte da meta de 15.

### 3.2 Verba por fase (por curso)

| Fase | Datas | Semanas | % da verba | Medicina Veterinária | Pedagogia (se desbloqueada até 16/11) | Papel |
|---|---|---|---|---|---|---|
| 1. Captação | 16/11 a 06/12/2026 | 3 | 30% | R$ 600,00 | R$ 600,00 | Teste de conceitos, cadastro na LP, público de remarketing |
| 2. Aquecimento | 07/12/2026 a 03/01/2027 | 4 | 15% | R$ 300,00 | R$ 300,00 | Remarketing de quem visitou a LP; menor pressão nas festas [SUPOSIÇÃO] |
| 3. Inscrições abertas (conversão) | 04/01 a 31/01/2027 | 4 | 35% | R$ 700,00 | R$ 700,00 | Conversão; janela provável das notas do Enem [CONFIRMAR] |
| 4. Reta final | 01/02 a 21/02/2027 | 3 | 20% | R$ 400,00 | R$ 400,00 | Remarketing e busca de marca; passos da matrícula; sem urgência sem número |
| Total | 16/11/2026 a 21/02/2027 | 14 | 100% | R$ 2.000,00 | R$ 2.000,00 | Pausa geral em 22/02/2027 (MP13) |

Percentuais por fase: mantidos da versão 2 [SUPOSIÇÃO de desenho], a aprovar em MP3.

**Pedagogia desbloqueada depois de 16/11:** as semanas da fase 1 que passarem sem anúncio não são gastas depois de uma vez. A parte não gasta da fase 1 é dividida igualmente entre as 7 semanas das fases 3 e 4 (até R$ 85,71 a mais por semana) e só é gasta se a campanha passar no critério de escalar (seção 5); o que não for gasto vira economia. Semanas do aquecimento antes do desbloqueio também viram economia.

### 3.3 Verba por canal e semana (por curso, em reais)

Divisão por canal na Medicina Veterinária: Meta 75% e Google Search 25% nas fases 1 a 3; Meta 60% e Google Search 40% na fase 4 (busca de marca pesa mais na reta final) [SUPOSIÇÃO de desenho, MP3]. Pedagogia: 100% Meta. Pesos semanais dentro das fases: os da seção 2.5 do estrategia-de-midia (fase 2: 30%, 30%, 20%, 20%; fase 4: 40%, 30%, 30%), com a regra das notas do Enem e do Sisu dele.

| Semana | Datas | Medicina Veterinária, total | Meta | Google Search | Pedagogia (Meta) |
|---|---|---|---|---|---|
| S1 | 16 a 22/11/2026 | R$ 200,00 | R$ 150,00 | R$ 50,00 | R$ 200,00 |
| S2 | 23 a 29/11/2026 | R$ 200,00 | R$ 150,00 | R$ 50,00 | R$ 200,00 |
| S3 | 30/11 a 06/12/2026 | R$ 200,00 | R$ 150,00 | R$ 50,00 | R$ 200,00 |
| S4 | 07 a 13/12/2026 | R$ 90,00 | R$ 67,50 | R$ 22,50 | R$ 90,00 |
| S5 | 14 a 20/12/2026 | R$ 90,00 | R$ 67,50 | R$ 22,50 | R$ 90,00 |
| S6 | 21 a 27/12/2026 | R$ 60,00 | R$ 45,00 | R$ 15,00 | R$ 60,00 |
| S7 | 28/12/2026 a 03/01/2027 | R$ 60,00 | R$ 45,00 | R$ 15,00 | R$ 60,00 |
| S8 | 04 a 10/01/2027 | R$ 175,00 | R$ 131,25 | R$ 43,75 | R$ 175,00 |
| S9 | 11 a 17/01/2027 | R$ 175,00 | R$ 131,25 | R$ 43,75 | R$ 175,00 |
| S10 | 18 a 24/01/2027 | R$ 175,00 | R$ 131,25 | R$ 43,75 | R$ 175,00 |
| S11 | 25 a 31/01/2027 | R$ 175,00 | R$ 131,25 | R$ 43,75 | R$ 175,00 |
| S12 | 01 a 07/02/2027 | R$ 160,00 | R$ 96,00 | R$ 64,00 | R$ 160,00 |
| S13 | 08 a 14/02/2027 | R$ 120,00 | R$ 72,00 | R$ 48,00 | R$ 120,00 |
| S14 | 15 a 21/02/2027 | R$ 120,00 | R$ 72,00 | R$ 48,00 | R$ 120,00 |
| **Total** | | **R$ 2.000,00** | **R$ 1.440,00** | **R$ 560,00** | **R$ 2.000,00** |
| 22/02/2027 | Início das aulas | R$ 0,00 | pausa | pausa | pausa |

Verba diária sugerida = verba semanal / 7 (por exemplo, S1 da Medicina Veterinária: R$ 21,43 na Meta e R$ 7,14 no Google). Medicina Veterinária com noturno desbloqueado: cada valor semanal se divide 50% integral e 50% noturno a partir da semana seguinte a MP8 [SUPOSIÇÃO de desenho].

### 3.4 Leads por semana esperados (verba / CPLmax)

Por curso, iguais nos dois cursos porque verba e meta são iguais. Não são previsão: é o volume que a verba compra se o CPL ficar exatamente no máximo do cenário.

| Fase | Verba | Conservador (CPL R$ 2,67) | Base (CPL R$ 6,67) | Otimista (CPL R$ 13,33) |
|---|---|---|---|---|
| 1. Captação (3 semanas) | R$ 600,00 | 225 leads (75 por semana) | 90 (30 por semana) | 45 (15 por semana) |
| 2. Aquecimento (4 semanas) | R$ 300,00 | 112,5 | 45 | 22,5 |
| 3. Conversão (4 semanas) | R$ 700,00 | 262,5 | 105 | 52,5 |
| 4. Reta final (3 semanas) | R$ 400,00 | 150 | 60 | 30 |
| Total | R$ 2.000,00 | 750 | 300 | 150 |
| Média por semana | R$ 142,86 | 53,6 | 21,4 | 10,7 |

Se o CPL observado passar do CPLmax do cenário aprovado, a verba compra menos leads do que os necessários (2.4) e a meta de 15 não vem só da mídia: ver 3.5.

### 3.5 Onde R$ 2.000,00 limitam o volume e o que fazer

| Limite | O que acontece | O que fazer |
|---|---|---|
| 1. Volume para o algoritmo aprender | A Meta indica cerca de 50 eventos de otimização por conjunto em 7 dias para sair da fase de aprendizado (Central de Ajuda da Meta, "Sobre a fase de aprendizado" [CONFIRMAR o número vigente na central]). Com R$ 150,00 por semana na Meta (fase 1), isso exigiria CPL de até R$ 3,00, perto do conservador. No base, a campanha tende a ficar em "aprendizado limitado" | 1 campanha e 1 conjunto por curso (e por turno, depois do noturno), público amplo 18+, posicionamentos automáticos, orçamento na campanha. Sem dividir em vários conjuntos. Se o aprendizado continuar limitado por 2 semanas e o CPL estiver acima do CPLmax, propor otimizar para um evento mais acima no funil (visualização da página de destino) só como teste, com aprovação (skill metas-de-custo, passo 6) |
| 2. Número de conceitos | Com cerca de 21 leads por semana no base, cada conceito recebe poucos leads; 3 conceitos levam de 2 a 3 semanas para ter leitura | No máximo 3 conceitos ativos por curso; 1 conceito novo a cada 2 semanas a partir da fase 2; nunca desligar todos os antigos ao mesmo tempo |
| 3. Canais | Um terceiro canal (TikTok, YouTube) e a busca da Pedagogia ficariam com menos de R$ 50,00 por semana | Fora por verba (3.1). Volta só por pedido de verba extra ao cmo, com a conta da seção 2 |
| 4. Remarketing | Com pouco tráfego, o público de visitantes da LP demora a atingir o tamanho mínimo exigido pela Meta | Campanha de remarketing separada só quando o público atingir o mínimo; até lá, o remarketing fica dentro da campanha ampla, sem verba extra |
| 5. Dois turnos na mesma verba | Integral e noturno dividem R$ 2.000,00: cada um fica com cerca de R$ 71,00 por semana depois do desbloqueio | Leitura da meta no curso (15); por turno só para criativo e atendimento. Se o noturno desbloquear tarde (depois de 04/01/2027), propor ao cmo manter o noturno só na busca e em remarketing, sem campanha ampla própria |
| 6. Meta de 15 só com a mídia | Se o CPL observado ficar acima do CPLmax, os R$ 2.000,00 não compram os leads necessários | Ordem das alavancas: (a) ativação da base de inscritos desde 17/08/2026 pelo CRM (sem custo de mídia; plano do cmo, 30/10); (b) melhorar a passagem inscrito para redação e redação para matrícula (copy-de-mensagens e atendimento); (c) trocar criativo antes de público; (d) conferir página e rastreamento; (e) só então pedido de verba extra ao cmo, separado, com a conta: verba necessária = 15 x custo por matrícula observado, menos o que já foi gasto. Nunca gastar acima dos R$ 2.000,00 sem aprovação |
| 7. Leitura estatística | Com pouco volume, uma semana ruim pode ser ruído; os últimos dias subcontam conversões | Decisão de desempenho só com 2 semanas seguidas; checagem de dados suficientes pela skill diagnostico-de-midia |

---

## 4. Estrutura de campanha (skill estrutura-de-campanha-paga)

### 4.1 Modelo escolhido

- **Medicina Veterinária: lançamento por fases**, com teste e escala dentro das fases, enxuto pela verba: 1 campanha Meta ampla por turno ativo e 2 campanhas de busca (marca e genérica). Motivo: captação com data fixa (aulas em 22/02/2027) e mensagem diferente por fase.
- **Pedagogia: local (Goiânia), enxuto.** 1 campanha Meta com 1 conjunto.
- **Orçamento na campanha** (Meta: orçamento de campanha; Google: orçamento por campanha), nunca no conjunto também.
- Integral e noturno ficam em campanhas separadas (leitura por turno e criativo diferente), com a mesma verba do curso (1.1). Exclusão cruzada de visitantes que clicaram no anúncio do outro turno no remarketing [SUPOSIÇÃO de desenho, a validar pelo anuncios-meta].

### 4.2 Nomenclatura

Padrão (D12 da seção 12 do plano do cmo; a Graduação mantém o prefixo grad_): linha_curso_plataforma_objetivo_publico_AAAAMM. Conjunto: nome da campanha + "__" + público. Anúncio (igual ao utm_content): conceito_formato_versão.

Valores fixos:
- linha: grad
- curso: medvet-integral, medvet-noturno, pedagogia
- plataforma: meta, google
- objetivo: cadastro (conversão na LP), busca (Google Search, conversão)
- público: amplo18 (18+ na região), rmk-lp30d (visitantes da LP nos últimos 30 dias), goiania18, marca, generica
- conceito: v1-preco, v2-pratica, v3-entrada (integral e noturno, ficha de oferta seção 5); p1-noite, p2-pratica, p3-preco, p4-ato (Pedagogia)
- formato: feed-4x5, feed-1x1, stories-9x16, reels-9x16, carrossel-1x1, rsa (anúncio de busca)

### 4.3 Mapa por fase (integral; noturno igual trocando o curso, depois de MP8; Pedagogia na 4.4)

**Fase 1, captação (16/11 a 06/12/2026)**
- grad_medvet-integral_meta_cadastro_amplo18_202611
  - conjunto: __amplo18 (18+, Grande São Paulo [SUPOSIÇÃO], posicionamentos automáticos, sem interesses)
  - anúncios: v1-preco, v2-pratica, v3-entrada (3 conceitos, formatos do criativos-de-anuncio)
- grad_medvet-integral_google_busca_marca_202611
  - grupo: marca (termos com "ufape" + veterinária ou vestibular)
- grad_medvet-integral_google_busca_generica_202611
  - grupo único: faculdade de veterinária em SP e variações próximas. Lista final de palavras e volumes: pesquisa-de-palavras-chave e anuncios-google [DADO NÃO FORNECIDO]. Negativas: "gratuita", "pública", "EAD", "concurso", "salário" [SUPOSIÇÃO, a validar]. Com R$ 50,00 por semana nas duas campanhas, a genérica só segue se trouxer cadastro com CPL até o CPLmax em 3 semanas; se não, a verba dela passa para a busca de marca e a Meta

**Fase 2, aquecimento (07/12/2026 a 03/01/2027)**
- grad_medvet-integral_meta_cadastro_amplo18_202611 continua (80% validados, 20% conceito novo)
- grad_medvet-integral_meta_cadastro_rmk-lp30d_202612 só se o público de visitantes tiver o tamanho mínimo da Meta; a verba sai da campanha ampla, sem acréscimo
- busca de marca e genérica seguem

**Fase 3, inscrições abertas (04/01 a 31/01/2027)**
- grad_medvet-integral_meta_cadastro_amplo18_202701 (escala), com os conceitos vencedores e mensagem de redação online, nota do Enem (média mínima de 300 pontos, edições de 2010 em diante) e desconto com regra
- grad_medvet-integral_meta_cadastro_rmk-lp30d_202701, se houver público
- busca de marca e genérica

**Fase 4, reta final (01/02 a 21/02/2027)**
- grad_medvet-integral_meta_cadastro_rmk-lp30d_202702 (passos da matrícula, aulas em 22/02/2027, documentos em até 30 dias; nada de "últimas vagas")
- busca de marca e genérica (40% da fase)
- campanha ampla só se o CPL da fase 3 estiver dentro da meta

Sem TikTok e sem YouTube nesta versão (3.1).

### 4.4 Mapa da Pedagogia (local, depois do desbloqueio)

- grad_pedagogia_meta_cadastro_goiania18_AAAAMM (AAAAMM do mês em que subir)
  - conjunto: __goiania18 (18+, Goiânia e região metropolitana [SUPOSIÇÃO], sem interesses; cuidado com raio pequeno demais, que encarece a entrega)
  - anúncios: até 3 conceitos ativos (p1-noite, p3-preco, p4-ato primeiro; p2-pratica na rotação)
- grad_pedagogia_meta_cadastro_rmk-lp30d_AAAAMM: só quando o público de visitantes tiver o tamanho mínimo exigido pela Meta, com verba tirada da campanha ampla
- Busca da Pedagogia: fora por verba (3.1)

### 4.5 Públicos: regras (ECA e LGPD)

- Idade mínima 18 anos em todo conjunto, em todas as plataformas. Nenhum público, semelhante ou de remarketing, pode ser configurado para menores. Parte da persona da Medicina Veterinária tem 17 anos [SUPOSIÇÃO do contexto]: a mensagem fala com a família e lembra o aceite do representante legal.
- Nenhuma segmentação ou exclusão por característica sensível (saúde, religião, orientação sexual, origem, renda, situação financeira) nem por emprego. Nada de interesse do tipo "professor" ou "trabalha em escola" na Pedagogia.
- Na busca do Google, a intenção vem da palavra; onde a plataforma permitir, faixas etárias abaixo de 18 ficam fora. Como menores podem ver anúncio de busca por contexto, o texto segue a regra de não pressionar menor [CONFIRMAR com o jurídico, ligado a G10 do cmo].
- Remarketing só por pixel e engajamento, configurado 18+.
- **Listas de contatos (base de inscritos, matriculados para exclusão, semelhantes) bloqueadas** até o jurídico validar a base legal e o tratamento de candidato menor (G10 do cmo e MP7). A base pode incluir menores de idade.
- Texto de anúncio nunca afirma situação de quem vê ("Você trabalha de dia?" bloqueia; "Para quem quer estudar veterinária à noite" passa).

### 4.6 UTM para a LP da Graduação (conferida com D11 e D12)

A plataforma gera a UTM; o gestor-de-midia confere. A squad não altera a LP. O padrão desta versão já seguia D11 (pago na Meta: utm_source meta, utm_medium paid_social; pago no Google: google e cpc) e D12 (utm_campaign = nome da campanha, prefixo grad_; utm_content = ID da peça; tudo minúsculo, sem acento, hífen dentro do bloco e sublinhado entre blocos; nenhum dado pessoal).

| Parâmetro | Meta | Google Search |
|---|---|---|
| utm_source | meta | google |
| utm_medium | paid_social | cpc |
| utm_campaign | nome da campanha | nome da campanha |
| utm_content | nome do anúncio | nome do anúncio |
| utm_term | público (amplo18, rmk-lp30d, goiania18) | {keyword} |

Exemplos (URL base [CONFIRMAR, G13]):
- faculdade.ufape.com.br/graduacao?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_medvet-integral_meta_cadastro_amplo18_202611&utm_content=v2-pratica_reels-9x16_v1&utm_term=amplo18
- faculdade.ufape.com.br/graduacao?utm_source=google&utm_medium=cpc&utm_campaign=grad_medvet-integral_google_busca_generica_202611&utm_content=v3-entrada_rsa_v1&utm_term={keyword}
- faculdade.ufape.com.br/graduacao/pedagogia?utm_source=meta&utm_medium=paid_social&utm_campaign=grad_pedagogia_meta_cadastro_goiania18_AAAAMM&utm_content=p1-noite_reels-9x16_v1&utm_term=goiania18

### 4.7 Protocolo de teste (com os valores do cenário base)

- Anúncio que gastar 2 vezes o CPLmax sem nenhum lead: pausar (regra prática, não meta; proposta ao humano). Base: R$ 13,33. Como o valor é baixo, só vale depois de 3 dias no ar, para não pausar por acaso [regra prática].
- Conceito que gastar de 1,5 a 3 vezes o CPLmax (base: de R$ 10,00 a R$ 20,00) com CPL até o CPLmax e passagem lead para inscrito no CRM igual ou acima da média do curso: promovido para a escala.
- Cadência: 1 conceito novo por curso a cada 2 semanas a partir da fase 2 (3.5).
- Uma mudança por vez no mesmo conjunto. Mudança de verba em campanha de escala: no máximo 20% por semana [regra prática], sempre dentro da tabela 3.3.

### 4.8 Checklist de pré-lançamento (humano executa; gestor-de-midia confere)

- [ ] Pixel e API de Conversões da Meta recebendo o evento de cadastro da LP; domínio verificado
- [ ] Tag do Google e conversão de cadastro criadas e testadas
- [ ] Evento certo selecionado em cada campanha (inscrição ou lead, conforme G13)
- [ ] UTM completa em todo anúncio (D11 e D12); origem chegando ao CRM com utm_campaign e utm_content
- [ ] Públicos de remarketing criados antes da fase 1, para começarem a acumular
- [ ] Idade 18+ e região em todo conjunto
- [ ] Criativos aprovados pelo qa-de-marketing (auditoria 11 e conformidade-educacional, 10/11/2026)
- [ ] Página de destino carrega, mostra dados da Ufape, contato e política de privacidade [CONFIRMAR, G13]
- [ ] Forma de pagamento ativa e limite de gasto da conta igual à verba aprovada (R$ 2.000,00 por curso, R$ 4.000,00 na Graduação, se MP2 aprovar)
- [ ] Inventário: nenhuma campanha de Graduação rodando fora da planilha [CONFIRMAR]; se houver, o gasto dela entra nos R$ 2.000,00 do curso ou é pausada com aprovação

---

## 5. Critérios de decisão (revisão semanal às segundas)

Ordem da revisão, parando na primeira causa real: verba gasta como planejado; tráfego (CPM, CPC, CTR); conversão (CPL, lead para inscrito, inscrito para redação, aprovado para matrícula no CRM); fadiga de criativo; página; rastreamento. Os últimos dias sempre subcontam conversões: nenhuma tendência é declarada só com eles.

| Decisão | Quando (regra prática, não meta; valores do cenário base) | Quem decide |
|---|---|---|
| Investigar | Plataforma, analytics e CRM não batem (diferença de leads acima de 15% na mesma semana); nenhuma decisão de desempenho vale até resolver | gestor-de-midia |
| Pausar anúncio | Gasto de 2 x CPLmax (R$ 13,33) sem lead, depois de 3 dias no ar | proposta ao humano |
| Ajustar | CPL entre R$ 6,67 e R$ 8,67 (1 a 1,3 x CPLmax) por 2 semanas, ou tc abaixo da tc mínima: trocar criativo antes de mexer em público; checar página e rastreamento antes de culpar o algoritmo | gestor-de-midia, dentro do plano |
| Manter | CPL até R$ 6,67 e passagem para inscrito estável | gestor-de-midia |
| Escalar | CPL até R$ 5,33 (0,8 x CPLmax) por 2 semanas seguidas, com passagem lead para inscrito igual ou acima da média do curso; aumento de até 20% por semana dentro dos R$ 2.000,00 (antecipa verba de semana seguinte do mesmo curso, sem passar do total) | proposta ao humano; acima da verba aprovada vai ao cmo como pedido de aprovação |
| Revisar o curso | CPL acima de R$ 8,67 por 2 semanas depois de um ajuste, ou custo por matrícula acumulado acima de R$ 133,33 a partir de C2 (04/01/2027) | cmo, com as alavancas da seção 3.5 |
| Remanejar entre cursos ou canais | Sempre | cmo (verba é por curso, decisão 15) |

Se a Ufape trocar o cenário base pelas taxas reais do CRM em MP1, os valores em reais desta tabela são recalculados uma vez, antes da subida.

Checagens do plano (estrategia-de-campanha): **C0 em 30/10/2026:** nenhuma campanha sobe, nem em teste, sem as metas numéricas desta versão aprovadas em MP1 (custo por matrícula R$ 133,33 e CPL do cenário escolhido) e a verba aprovada em MP2. Sem isso, MP11 não é pedido e a subida de 16/11/2026 é adiada. C1 em 30/11/2026; C2 em 04/01/2027; C3 em 25/01/2027. Relatório semanal ao cmo em até 200 palavras a partir de 23/11/2026.

---

## 6. Encomendas aos agentes do departamento

Todos seguem a skill estrutura-de-campanha-paga. Nenhum sobe nada: cada um entrega arquivo para um humano montar.

| Agente | Recebe | Verba | Meta | Entrega | Prazo |
|---|---|---|---|---|---|
| estrategia-de-midia | Esta versão (seções 2 e 3) | R$ 2.000,00 por curso, tabela 3.3 | R$ 133,33 por matrícula; CPL base R$ 6,67; custo por inscrito base R$ 16,67 | Nova versão do plano detalhado com os valores em reais por curso, canal e semana; funil reverso com os três cenários; tabela de leads por semana; regra de realocação dentro dos R$ 2.000,00; regra de entrada tardia do noturno e da Pedagogia. Arquivo: saidas/11-midia-paga/estrategia-de-midia-graduacao-2026-10-26.md | entregue com esta versão (26/10/2026) |
| criativos-de-anuncio (skill matriz-de-criativos) | Seções 1, 3.5, 4.2 e 4.5 | Teste de R$ 10,00 a R$ 20,00 por conceito (base) | Conceitos que passem na conformidade e permitam leitura por curso | Ajustar o portfólio já entregue (saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md) ao limite de 3 conceitos ativos por curso e à ordem de entrada (1.1 e 1.2); textos de busca só para a Medicina Veterinária; versões de TikTok e YouTube ficam guardadas (canais fora por verba) | 04/11/2026 |
| anuncios-meta | Seções 3.3, 3.5, 4.1 a 4.8 | Medicina Veterinária: R$ 1.440,00; Pedagogia: R$ 2.000,00, por semana conforme 3.3 | CPLmax e custo por matrícula do cenário aprovado | Estrutura das 4 fases do integral, do noturno (bloqueado) e da Pedagogia (bloqueada): 1 campanha e 1 conjunto por curso e turno, público 18+, região, remarketing por pixel só com público mínimo, orçamento de campanha, UTMs e checklist. Sem listas de contatos | 06/11/2026 |
| anuncios-google | Seções 3.1, 3.3, 4.3, 4.6 e 4.8 | Google Search da Medicina Veterinária: R$ 560,00, por semana conforme 3.3 | CPLmax do cenário aprovado; lance por conversão só depois de volume [regra prática] | Busca de marca e genérica (um grupo) da Medicina Veterinária, palavras e negativas com a pesquisa-de-palavras-chave, anúncios responsivos, configuração 18+ onde possível. Sem Performance Max, sem YouTube, sem busca da Pedagogia | 06/11/2026 |
| anuncios-tiktok | - | - | - | Sem encomenda nesta versão (canal fora por verba). A estrutura de teste fica para um eventual pedido de verba extra aprovado | - |
| analise-de-midia | Seção 5 | - | Valores da seção 5 | Modelo do relatório semanal (fatos, hipóteses, dados que faltam), leitura por curso contra R$ 133,33 por matrícula e CPL do cenário aprovado, conferência plataforma x analytics x CRM a partir de 23/11/2026 | 13/11/2026 |

anuncios-linkedin: sem encomenda (canal fora).

---

## 7. Pedidos de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| MP1 | Aprovar as metas desta versão por curso: custo por matrícula máximo R$ 133,33; CPL e custo por inscrito do cenário base (R$ 6,67 e R$ 16,67) como meta provisória; trocar pelas taxas reais do CRM uma única vez, antes de 16/11/2026 | Sem meta escrita antes de subir, nenhuma campanha pode ser julgada | sem custo | Metas fixas para toda a captação | Nova versão das metas antes de subir; depois de subir, metas não são reescritas para caber no resultado |
| MP2 | Aprovar o gasto da verba estimada: R$ 2.000,00 para Medicina Veterinária e R$ 2.000,00 para Pedagogia (R$ 4.000,00 na Graduação), e nomear quem aprova | Decisão 15 estima a verba; nada é pago sem aprovação humana | R$ 4.000,00 no ciclo | Subida possível em 16/11/2026 | Reduzir ou pausar no gerenciador, por humano |
| MP3 | Aprovar a divisão por fase (3.2), por canal e semana (3.3) e o orçamento de teste (2.6) | Define onde a verba entra em cada semana | dentro de MP2 | Calendário de verba fechado antes de 16/11/2026 | Nova versão aprovada pelo cmo |
| MP4 | Aprovar os públicos: 18+ em todos os conjuntos; Grande São Paulo e Goiânia e região com área confirmada pelo comercial; público amplo sem interesses; remarketing só por pixel e engajamento. Define o público adulto que desbloqueia noturno e Pedagogia | Regras para menores (G10 do cmo), ECA, LGPD e políticas das plataformas | sem custo | Públicos montados sem risco com menores nem dado sensível | Editar o público no gerenciador, por humano |
| MP5 | Suspenso nesta versão: teste de TikTok sai por verba (3.1). Volta só como pedido de verba extra ao cmo | - | - | - | - |
| MP6 | Suspenso nesta versão: YouTube de remarketing sai por verba (3.1) | - | - | - | - |
| MP7 | Decidir sobre listas de contatos (base de inscritos para exclusão ou semelhante) depois da validação do jurídico | Base pode ter menores; LGPD exige base legal | sem custo | Menos gasto com quem já se inscreveu, se aprovado | Excluir a lista da conta, por humano |
| MP8 | Desbloquear o anúncio pago do noturno quando G8 (campo turno) estiver corrigido e MP4 aprovado; a partir daí, a verba semanal da Medicina Veterinária se divide 50% e 50% entre turnos | Página precisa entregar o que o anúncio promete | dentro dos R$ 2.000,00 do curso | Noturno no ar no dia seguinte ao desbloqueio | Pausar as campanhas do noturno; verba volta ao integral |
| MP9 | Desbloquear o anúncio pago da Pedagogia quando G6 (página), MP4 e MP1 estiverem resolvidos | Página com texto de modelo | dentro dos R$ 2.000,00 do curso | Pedagogia no ar com meta escrita | Pausar as campanhas da Pedagogia |
| MP10 | Configurar rastreamento: pixel e API de Conversões, tag e conversão do Google, públicos de remarketing, envio da origem ao CRM (G13 do cmo) | Sem rastreamento não há decisão | sem custo de mídia | Leitura por curso, canal e criativo | Remover tag ou evento, por humano |
| MP11 | Subir cada campanha da fase 1 (integral) entre 11 e 13/11/2026, depois do checklist 4.8 e do qa de 10/11. Só é pedido depois de MP1 e MP2 aprovados | Montagem e publicação são feitas por humano | R$ 600,00 por curso na fase 1 | Captação a partir de 16/11/2026 | Pausar a campanha, por humano |
| MP12 | Subir as campanhas de cada fase seguinte (07/12, 04/01 e 01/02) com os criativos aprovados | Cada fase muda objetivo e mensagem | verba da fase (3.2) | Transição de fase no prazo | Pausar a campanha nova e manter a anterior |
| MP13 | Pausar todas as campanhas da Graduação 2027/1 em 22/02/2027 | Fim do ciclo | encerra o gasto | Relatório final até 05/03/2027 | Reativar no gerenciador, por humano |
| MP14 | Informar se existe campanha de Graduação rodando fora da planilha, com gasto e resultado | Inventário antes de subir; o gasto conta nos R$ 2.000,00 | sem custo | Leitura limpa desde a 1ª semana | Não se aplica |
| MP15 | **[CONFIRMAR com o CEO]** (a) Qual leitura de "valor do curso" vale (2.2: A, B, C1, C2, D1 ou D2); (b) se as 15 matrículas são a meta total do curso ou a parte da mídia paga; (c) se a Medicina Veterinária conta como 1 curso (15 matrículas e R$ 2.000,00 para os dois turnos) ou como 2 turmas; (d) como a meta de 15 convive com a turma mínima de 30 por turma do edital e a meta de 30 por turma do plano do cmo; (e) o período exato do ciclo (decisão 15) | Meta em reais, leitura da meta e risco de turma mínima dependem disso | sem custo | Meta fechada antes de 16/11/2026 | Nova versão deste plano |

Pedido de verba extra, se surgir, vai separado ao cmo, marcado como pedido de aprovação, com a conta da seção 3.5 (linha 6). Nada é publicado, pago ou alterado pela squad.

---

## 8. Auditorias deste plano

**auditorias/11-midia-paga.md**
- [ ] Plano aprovado com canais ativados e fora justificados: canais justificados na seção 3.1; aprovação humana pendente.
- [x] Metas de CPL e custo por matrícula escritas antes de subir: R$ 133,33 por matrícula e CPL em três cenários (2.3 e 2.4). Aprovação pendente (MP1); a subida segue bloqueada até MP1 e MP2.
- [ ] Verba dentro do valor aprovado, com aprovador: R$ 2.000,00 por curso (decisão 15), tabela 3.3 soma exatamente esse valor; aprovação do gasto e aprovador pendentes (MP2).
- [x] Nomenclatura padrão em campanhas, conjuntos e anúncios (4.2, D12).
- [ ] UTMs completas e origem no CRM: padrão conferido com D11 e D12 (4.6); URL e chegada ao CRM [CONFIRMAR] (G13, MP10).
- [ ] Pixel, API de Conversões e conversões do Google configurados e testados: no checklist 4.8; estado atual [DADO NÃO FORNECIDO]. TikTok e LinkedIn não se aplicam.
- [ ] Criativos aprovados na conformidade: dependem do qa de 10/11/2026.
- [x] Anúncios dentro das políticas das plataformas: regras de público, texto e destino nas seções 1 e 4.5.
- [x] Nenhum público com menores de 18 (4.5); possíveis menores na persona tratados pela mensagem para a família e pelo bloqueio de listas.
- [x] Spark Ad e post de docente promovido: não se aplicam (TikTok e LinkedIn fora).
- [ ] Relatório semanal ao cmo: começa em 23/11/2026.
- [x] Sem segmentação discriminatória nem exclusão por atributo sensível (4.5).
- [x] Públicos sem dados pessoais sem base legal: listas bloqueadas até o jurídico (MP7).
- [x] Dados de curso conferidos no catálogo e na ficha dos editais; carga horária da Pedagogia fora.
- [x] Destino de WhatsApp: não há campanha de WhatsApp; destino é a LP.
- [x] Números só das fontes fornecidas: verba e meta das decisões 15 e 16; preços e parcelas do catálogo e dos editais; taxas de conversão marcadas [SUPOSIÇÃO de cenário]; nenhum benchmark usado como meta; número de eventos da fase de aprendizado da Meta citado como regra da plataforma, [CONFIRMAR o número vigente].
- [x] Nenhuma alteração feita na plataforma sem humano: todo passo é pedido de aprovação (seção 7).

**auditorias/conformidade-educacional.md** (aplicada ao plano; cada anúncio passa de novo no qa)
- [x] Nome, modalidade, duração e turno batem com o catálogo; carga horária da Pedagogia fora de toda peça.
- [x] Os dois cursos estão "aberto" no catálogo.
- [x] Modalidade presencial clara; até 30% a distância fica no atendimento, sem esconder.
- [x] Atos citados como no catálogo, sem antecipar reconhecimento.
- [x] Nenhuma nota do MEC nem frase de certificação.
- [x] Nenhuma promessa de emprego, salário, aprovação ou concurso; redação é eliminatória.
- [x] Preço com valor cheio, parcelas, desconto, regra e validade; sem taxa escondida (a matrícula é a 1ª mensalidade; inscrição gratuita); reajuste sinalizado [CONFIRMAR]. As leituras de "valor do curso" da seção 2.2 são conta interna de meta e nunca vão para peça.
- [x] Sem urgência falsa: reta final fala de passos e datas do edital, sem "últimas vagas".
- [x] Prouni, Fies e financiamento fora.
- [ ] Autorização de uso de imagem do hospital e uso pela graduação: [CONFIRMAR] (G11). Docentes: autorização registrada pelas decisões 8 e 10.
- [x] Menores (ECA e LGPD): anúncio só 18+, sem menor identificável sem autorização dos responsáveis, listas bloqueadas, mensagem para a família.
- [ ] Formulário da LP com finalidade e política de privacidade: [CONFIRMAR] (G13). A squad não altera a LP.
- [x] Nenhum dado pessoal neste arquivo.
- [ ] Página de destino entrega o que o anúncio promete: noturno bloqueado até G8; Pedagogia bloqueada até G6.
- [x] Texto de anúncio não afirma característica pessoal de quem vê (4.5).
- [x] Sem escassez falsa, contador, botão falso, pessoa pública ou tentativa de driblar a análise.

**Resultado:** rascunho pronto para nova rodada do qa-de-marketing. Bloqueados até resposta: subida de qualquer campanha até MP1 e MP2; noturno (G8, MP4, MP8); Pedagogia (G6, MP4, MP1, MP9); listas de contatos (MP7); criativos com hospital (G11); meta em reais até MP15. Revisado por: gestor-de-midia (agente), versão 3. Data: 26/10/2026.

**Notas para arquivos de outros donos (não alterados por este agente):**
- Plano do cmo (cmo-graduacao, seções 1, 3 e 8): meta principal de 30 matrículas por turma e G3 com verba [CONFIRMAR]. As decisões 15 e 16 dão verba de R$ 2.000,00 e meta de 15 por curso; o conflito com a turma mínima de 30 está em MP15 para o cmo levar ao CEO.
- Plano do cmo, seção 4: TikTok em teste e YouTube leve no G1. Na mídia paga, os dois saem por verba nesta versão; no orgânico, a decisão do cmo continua.
- criativos-de-anuncio-graduacao-2026-10-26.md: portfólio pensado para mais canais e conceitos; o ajuste está na encomenda da seção 6.
- A nomenclatura sugerida pelo cmo usa "goiania" no campo público da Pedagogia; este plano usa "goiania18" para deixar a idade mínima explícita.

---

## 9. Fatos (com fonte)

- Verba estimada de R$ 2.000,00 de mídia por curso da Graduação no ciclo de captação; nada é pago sem aprovação humana (decisão 15, docs/execucao-2026-10-26.md).
- Meta de pelo menos 15 matrículas por curso; meta em reais de 15 vezes o valor do curso no catálogo; na Graduação a inscrição é gratuita e a meta conta matrículas (decisão 16).
- Mensalidade cheia R$ 10.000,00 (Medicina Veterinária) e R$ 1.050,00 (Pedagogia); com desconto R$ 5.000,00 (integral, 50%), R$ 4.000,00 (noturno, 60%), R$ 525,00 (Pedagogia, 50%); 6 parcelas por semestre; desconto só no 1º semestre de 2027 (catálogo; Editais 003/2026).
- Duração: integral 4 anos, noturno 5 anos, Pedagogia 4 anos (catálogo; editais).
- Matrícula confirmada com o pagamento da 1ª mensalidade e assinatura do contrato; sem taxa de matrícula; inscrição gratuita (editais 002 e 004/2026).
- Vagas: 45 integral, 45 noturno, 80 Pedagogia; turma mínima de 30 por turma; aulas em 22/02/2027; cancelamento com devolução de 80% até 2 dias antes das aulas (editais).
- Candidato menor precisa do aceite do representante legal na inscrição e na matrícula (Edital 002/2026).
- Padrão de UTM: D11 e D12, seção 12 do plano geral do cmo.
- Página do noturno mostra "INTEGRAL" no turno; página de Pedagogia com texto de modelo (plano do cmo, auditoria de 22/10/2026).

## 10. Suposições

- [SUPOSIÇÃO de cenário] Taxas de conversão: lead para inscrito 20%, 40% e 50%; inscrito para matrícula 10%, 12,5% e 20% (conservador, base, otimista). Sem fonte externa nem histórico; escolhidas para mostrar sensibilidade.
- [SUPOSIÇÃO] Leitura provisória de "valor do curso": B (1º semestre com desconto), até o CEO responder.
- [SUPOSIÇÃO de desenho] Percentuais por fase (30, 15, 35, 20); Meta 75% e Google 25% nas fases 1 a 3 e 60% e 40% na fase 4 da Medicina Veterinária; Pedagogia 100% Meta; 50% e 50% entre turnos depois do desbloqueio do noturno.
- [SUPOSIÇÃO de desenho] Pesos semanais do estrategia-de-midia; 3 conceitos ativos por curso.
- [SUPOSIÇÃO] Área geográfica: Grande São Paulo e Goiânia com região metropolitana.
- [SUPOSIÇÃO] Facebook alcança pais, responsáveis e adultos de Goiânia; menor pressão nas festas.
- Regras práticas, não metas: 1,5 a 3 x CPLmax por conceito; pausa com 2 x CPLmax sem lead depois de 3 dias; escala com 0,8 x CPLmax por 2 semanas; até 20% de aumento por semana; diferença acima de 15% entre fontes vira investigação.

## 11. Dados que faltam

- [CONFIRMAR com o CEO] Leitura de "valor do curso"; se 15 é meta total ou da mídia; Medicina Veterinária como 1 curso ou 2 turmas; convivência com a turma mínima de 30; período exato do ciclo (MP15).
- [CONFIRMAR] Aprovação do gasto de R$ 4.000,00 e aprovador (MP2).
- [CONFIRMAR] Taxas reais do funil no CRM (inscritos, avaliados, aprovados e matriculados desde 17/08/2026) para trocar o cenário (MP1; G2 do cmo).
- [CONFIRMAR] V (custo variável por aluno) e Md (margem desejada): não mudam a meta desta versão, só o teto econômico.
- [CONFIRMAR] Efeito do reajuste de dezembro e regra de renovação do desconto (G12): mudam as leituras C1 a D2.
- [CONFIRMAR] Se o formulário da LP é a inscrição; URL que recebe a UTM; origem no CRM; política de privacidade (G13).
- [CONFIRMAR na Central de Ajuda da Meta] Número vigente de eventos por semana para sair da fase de aprendizado.
- [DADO NÃO FORNECIDO] Estado do pixel, da API de Conversões e da tag do Google; histórico de CPL; volume e CPC dos termos de busca.
- [CONFIRMAR] Campanhas de Graduação ativas fora da planilha (MP14).
- [CONFIRMAR] Correção das páginas (G6, G8); validação jurídica de listas e de anúncio de busca visto por menores (G10).
- [CONFIRMAR] Data-limite interna de inscrição e matrícula (G4); datas do Enem 2026, das notas e do Sisu.
- [CONFIRMAR NO CATÁLOGO] Carga horária da Pedagogia; horário de prática e estágio do noturno.

---

## Próximo passo

Arquivo: saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md (versão 3). O plano detalhado do estrategia-de-midia foi atualizado na mesma rodada. Próximo agente: **criativos-de-anuncio** (ajuste do portfólio ao limite de 3 conceitos por curso, 04/11/2026). Antes de qualquer subida: MP1, MP2, MP4 e MP15 respondidos. Depois, nova rodada do qa-de-marketing.
