# QA de marketing: reconferência da mídia paga da Pós (versão 4)

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Revisão anterior:** /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-26-midia.md (correções QM1 a QM5)
- **Arquivos reconferidos (não editados):**
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (versão 4)
  - /home/user/marketing-ufape/saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (versão 4)
- **Entradas lidas:** as duas versões 4 inteiras; a revisão anterior; contexto/ufape-geral.md, contexto/pos-graduacao.md, docs/execucao-2026-10-26.md, auditorias/11-midia-paga.md, auditorias/conformidade-educacional.md e contexto/catalogo-de-cursos.md, como na revisão anterior.
- **Escopo:** só QM1 a QM5 e os problemas novos que a versão 4 possa ter criado. As contas da versão 3 já estavam certas, e os dois arquivos dizem que nenhum valor mudou. Conferi por amostra que os valores das tabelas 3.3 a 3.6 da estratégia e da tabela 12.6 do gestor são os mesmos da versão 3. Conferi também a nova divisão do aquecimento (56%, 14% e 30%): R$ 280,00, R$ 70,00 e R$ 150,00 sobre R$ 500,00.
- **Dados pessoais:** nenhum.
- **Travessão e meia-risca:** o coordenador informou que a busca automática de U+2014 e U+2013 deu zero nos dois arquivos. Na leitura desta revisão não achei nenhum. Não rodei busca automática própria.

---

## 1. Tabela de vereditos

| # | Ponto | Arquivo | Resultado | Onde |
|---|---|---|---|---|
| QM1 | Corpo do gestor sem provas, YouTube, LinkedIn e P6 | gestor | **Resolvido em parte** | Seções 1, 3, 5, 6, 9 e 11 alinhadas (linhas 57, 63, 64, 67, 199 a 211, 267 a 272, 287 a 307, 355, 359, 360, 364 a 366, 370, 388 a 438, 677 a 680). O teste de rastreio passou para 30/10 (linha 287). A recomendação final está corrigida (linha 370). Ficou um resíduo, que é QM6 |
| QM2 | Nenhuma peça com preço nem valor de inscrição até U11 | gestor | **Resolvido** | Linhas 456, 610, 612 e 421 |
| QM3 | Fonte única do limite de volume, do "frio sai" e da troca do rodízio | gestor e estratégia | **Resolvido** | Gestor: linhas 562 a 578, 584, 591 e 593, com a tabela igual à 3.6 da estratégia e a troca em R$ 27,00. Estratégia: linha 235, sem a nota de diferença na 3.6 nem na seção 9 |
| QM4 | Gatilho do rodízio de 657 e 341 em 21/12 | estratégia | **Resolvido** | Linha 263 (3.7, item 7), revisões 8, 10 e 11 (linhas 412, 414 e 415) e EM13 (linha 469) |
| QM5 | Regra única de 289 e 662, com a conversão protegida | estratégia | **Resolvido (opção a)** | 3.8 (linhas 267 a 274); recálculo em 30/11 e 30/12 (linhas 384, 390 e 446); checagem em 03/11 (linhas 382 e 408); EM15 (linha 471). Recomendação R7 abaixo |
| QM6 (novo) | Pedidos e encomendas do gestor ainda na lógica da verba nova e das provas | gestor | **Corrigir** | Detalhe na seção 2 |
| Conformidade | auditorias/conformidade-educacional.md | gestor e estratégia | Atende nos dois | O item de preço do gestor agora atende (QM2). Os itens pendentes externos seguem como na revisão anterior |
| Mídia paga | auditorias/11-midia-paga.md | gestor | **Falha** no item "verba dentro do valor aprovado" (QM6) | PP5 |
| Mídia paga | auditorias/11-midia-paga.md | estratégia | Atende, com pendências externas | |
| **Veredito** | | **gestor-de-midia-pos v4** | **CORRIGIR** (só QM6) | |
| **Veredito** | | **estrategia-de-midia-pos v4** | **APROVADO** | Segue para a aprovação humana de EM4, EM11 e EM13 a EM16. O pagamento depende de PP16, que fica no gestor |

**Destino:** o gestor-de-midia-pos volta ao gestor-de-midia só para QM6. A estrategia-de-midia-pos segue para a aprovação humana; nada sobe, muda ou gasta sem ela.

---

## 2. Correção obrigatória

### QM6. gestor-de-midia-pos: pedidos de aprovação e encomendas que contradizem a seção 12

QM1 tirou provas, YouTube, LinkedIn e P6 das seções que listei, mas alguns pedidos de aprovação ainda descrevem quanto se gasta pela lógica antiga da verba nova da linha (VN). Um humano que aprovar esses pedidos como estão escritos aprova uma regra de verba diferente da seção 12.5 e da 3.8 da estratégia.

| Linha | O que está escrito | Problema | Correção |
|---|---|---|---|
| 357 (PP5) | 662: "diária atual fora de VN até o lote 2, sem aumento (EM9)" | A seção 12.5 (linha 537) diz que a diária de 662 conta nos R$ 2.000,00 dela. A estratégia (3.8 e EM15) limita o gasto de 662 a R$ 500,00 até 05/01. Aprovar o PP5 como está deixa o gasto de 662 fora do teto do CEO | Trocar por "diária atual dentro dos R$ 2.000,00 de 662, limitada a R$ 500,00 até 05/01, com recálculo em 30/12 (estrategia-de-midia-pos, 3.8 e EM15)" |
| 68 (seção 1, linha "Ativas fora da onda 1") | "o gasto de 289 entre a aprovação de VN e 06/12 sai da parte de 289 em P3"; "a diária atual de 662 fica fora de VN" | O aviso da seção (linha 57) não cobre esta linha, e o texto contradiz a 12.5 | Marcar "Versão 3 e 4: as duas dentro dos R$ 2.000,00 da turma, regra da 3.8 da estratégia (EM15)" |
| 361 (PP9) | 289: "descontado da parte de 289 em P3"; "Quanto: diária atual, contada em P3" | P3 já não tem verba própria, e o limite de R$ 500,00 até 06/12 não aparece | Apontar para EM15: limite de R$ 500,00 até 06/12, o que passar sai da manutenção, nunca da conversão |
| 358 (PP6) e 363 (PP11) | "Quanto: parte de P3 [CONFIRMAR]" e "P4, 15% da verba nova" | São valores de verba de uma divisão que deixou de valer (PP2, linha 354) | "R$ 2.000,00 por turma, divisão da 12.5 (PP16)" |
| 322, 324 e 325 (seção 7) | Encomendas de provas: estrutura e rastreio das provas até 31/10, pacote de criativos das provas para 03/11, "P1" na coluna de verba | O aviso da linha 316 manda a 12.8 valer, mas a 12.8 não cancela as encomendas das provas para anuncios-meta, anuncios-google e criativos-de-anuncio. Um agente que lê a seção 7 pode montar a estrutura das provas, contra a decisão 14. Este ponto escapou da lista de QM1 na revisão anterior | Marcar as partes das provas como "suspenso (decisão 14)" ou pôr na 12.8 uma linha que suspenda as encomendas das provas |

**Por que é obrigatória:** o PP5 é um pedido de aprovação humana com o valor errado (auditoria 11, "verba dentro do valor aprovado"), e a seção 7 ainda encomenda trabalho das provas (decisão 14). As outras linhas são o mesmo tipo de resíduo e saem juntas.

---

## 3. Recomendações (não bloqueiam)

| # | Arquivo e linha | O que | Sugestão |
|---|---|---|---|
| R7 | estratégia, 271 e 273 (3.8, itens 2 e 4) | Se 289 passar de R$ 700,00 antes de 07/12, ou 662 passar de R$ 500,00 antes de 06/01, a "conversão protegida" e o teto de R$ 2.000,00 entram em conflito. Hoje o arquivo só prevê aviso [CONFIRMAR]. O teto vale por EM16, que pausa a turma em R$ 2.000,00, mas aí a conversão termina antes do corte | Escrever que o teto de R$ 2.000,00 (EM16) prevalece e que, nesse caso, a conversão é recalculada pelo saldo |
| R8 | estratégia, 480 (seção 9) | A nota diz que o gestor ainda fala de VN, P6, YouTube e provas nas seções 4.3, 6 e 7. Desde a versão 4 do gestor, a seção 6 já está alinhada | Atualizar a nota quando o gestor fechar QM6 |
| R9 | gestor, 715 | "Próximo agente: qa-de-marketing (conferência da versão 3)" | Trocar para a versão 4 ou 5 |
| R1 a R6 | revisão anterior | Não aplicadas (marcador no CPL base, nome "retorno sobre a verba", nomenclatura do PP4, entrada da onda 1 depois do vencimento, marcadores no funil de duas etapas) | Seguem como sugestão |

---

## Lista 1. Fatos (com fonte)

- QM1 a QM5 e as recomendações R1 a R6 (qa-de-marketing-pos-2026-10-26-midia.md).
- Versão 4 dos dois arquivos, com a lista das mudanças e "nenhuma conta mudou" (gestor, linhas 620 a 624; estratégia, linhas 534 a 538).
- Gasto de 289 e de 662 dentro dos R$ 2.000,00 da turma (gestor 12.5, linha 537; estratégia 3.8).
- Provas de bolsa sem peça nova até nova ordem (docs/execucao-2026-10-26.md, decisão 14).
- Busca automática de U+2014 e U+2013 com resultado zero nos dois arquivos (mensagem do coordenador).
- 14/12/2026 é segunda-feira; a semana de 14 a 20/12 tem 7 dias.

## Lista 2. Suposições

- [SUPOSIÇÃO] A estrategia-de-midia-pos pode seguir para a aprovação humana antes do gestor fechar QM6, porque QM6 não muda nenhuma regra nem valor da estratégia; o pagamento continua dependendo de PP16.
- [SUPOSIÇÃO] A conferência dos valores da versão 4 foi por amostra (tabelas 3.3 a 3.6 da estratégia e 12.6 do gestor), porque os dois arquivos declaram que nenhum valor mudou desde a versão 3, que foi conferida inteira.

## Lista 3. Dados que faltam

- [CONFIRMAR U11] Valor da inscrição da Pós.
- [CONFIRMAR] Gasto do ciclo da onda 1, de 289 (até 30/11) e de 662 (até 30/12), e as diárias atuais (PP15, EM15).
- [CONFIRMAR] Caminho se o gasto de 289 passar de R$ 700,00 ou o de 662 passar de R$ 500,00 antes da estrutura nova (R7).
- [CONFIRMAR] Ciclo exato e data de corte por turma; taxas i e k; Mmid.
- [CONFIRMAR] Quem aprova anúncios e verba (tabela de ufape-geral.md vazia; até lá, pessoa do marketing).

## Fontes

Internas: os arquivos listados no cabeçalho e a mensagem do coordenador sobre a busca de caracteres. Externas: nenhuma.
