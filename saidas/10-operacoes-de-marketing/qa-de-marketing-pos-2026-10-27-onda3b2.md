# QA de marketing: reconferência das correções D1 a D7 (O6) e M1 a M18 mais totais (O7), onda 3 da Pós, lote A

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 27/10/2026
- **Base:** saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda3b.md (seção 4)
- **Arquivos reconferidos (não editados):**
  - O6: /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-27-onda3.md
  - O7: /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-2026-10-27-onda3.md
- **Escopo:** só as linhas trocadas e uma amostra de 3 totais pela regra B1. Sem recontagem geral. Travessão, meia-risca e telefone já conferidos pelo orquestrador.

---

## 1. Vereditos

| Arquivo | Veredito | Motivo curto | Destino |
|---|---|---|---|
| O6, autoridade-docente-pos-2026-10-27-onda3.md | **APROVADO** | D1 a D7 aplicadas com o texto exato; os dois itens que bloqueavam (D1, D2) estão resolvidos | segue para a aprovação humana (AD-O6-1 a AD-O6-8, OC3) |
| O7, copy-de-mensagens-pos-2026-10-27-onda3.md | **APROVADO COM RESSALVAS** | M1 a M18 aplicadas com o texto exato; todos os itens que bloqueavam (M2 a M10) estão resolvidos; a conformidade passa inteira. Ressalva: o script contou o marcador "[dd/06/2027, CONFIRMAR NO CATÁLOGO, OU25]" com 41 caracteres nos 3 pós-início de 679, 68635 e 366, quando a regra do próprio arquivo (seção 0.3) e o rótulo dizem 10; 3 rótulos de corpo e 3 totais ficaram 31 caracteres acima (seção 3). Não bloqueia: os três toques são condicionados ao dia do 3º módulo e ficam muito abaixo de 1.024 | o orquestrador aplica as 6 trocas da seção 3 sem nova volta ao qa; depois segue para a aprovação humana do OC2 |

Nada é publicado, enviado ou pago a partir deste arquivo.

---

## 2. O que foi conferido

### O6

| Correção | Linha atual | Resultado |
|---|---|---|
| D1 (AD-A7-1, Cushing em cães) | 172 | aplicada: "ao Cushing em cães e ao diabetes mellitus em cães e em gatos," |
| D2 (AD-A1-3, módulo 8) | 202 | aplicada: "e o módulo de intubação, indução anestésica e anestesia geral inalatória." |
| D3 (regras do card) | 240 | aplicada com o texto exato |
| D4 (AD-O6-2, "Por que") | 676 | aplicada com o texto exato |
| D5 (nota de 68635) | 144 | aplicada: "(os módulos 21, 24 e 28 têm dia na ficha)" |
| D6 (pares da E20) | 52 | aplicada; 654 e 670 fora dos pares |
| D7 (Lista 3) | 750 | aplicada com o texto exato |

Observação sem correção: a linha 240 cita a onda2b, seção 4.3, duas vezes seguidas (a frase antiga "O plano (C22) e o qa da onda 2 ... aceitam" continua antes da frase da D3). É repetição, não erro de fato.

### O7

| Correção | Linha atual | Resultado |
|---|---|---|
| M1 (55 textos, 39 WhatsApp) | 19 | aplicada |
| M2 (E1 de 68609 sem a frase de aulas não transmitidas) | 1120 | aplicada |
| M3 (R3: 68632 à parte; "secretaria"; 68636 e 68609 sem a frase) | 1275 | aplicada, as três trocas |
| M4 (R4 em 68632) | 1276 | aplicada |
| M5 (9.1, antes do início sem a data do 3º módulo) | 1255 | aplicada |
| M6 (R1 de 679, 68635 e 366 com a regra completa) | 1273 | aplicada |
| M7 (R2 de 679, 68635 e 366 com a regra completa) | 1274 | aplicada |
| M8 (W2 de 679 e 9.3 sem "de laboratório"; rótulo 324; total 490 e 503) | 127, 129, 136 e 1285 | aplicada |
| M9 (68628, três dos quatro módulos de tratamento) | 1317 | aplicada |
| M10 (E1 de 366, "Trauma") | 520 | aplicada |
| M11 (E2 de 679, "coleta de amostras") | 152 | aplicada |
| M12 (pré-cabeçalho do E1 de 68628, 81, "presenciais") | 663 | aplicada |
| M13 (E2 de 68628, nome no padrão) | 734 | aplicada |
| M14 (E2 de 68617, sem a frase do guia) | 891 | aplicada |
| M15 (reservas de W3 com data absoluta) | 322, 460, 758, 907 e 1206 | aplicada nas 5; as linhas 174, 608 e 1055 (679, 366 e 68636) seguem com "abril", como pedido |
| M16 (10.2, 05/02, 19/02 e 03/05, ordem das datas) | 1415 | aplicada |
| M17 (10.1, A14 numa lista só) | 1411 | aplicada |
| M18 (pós-início de 679, 366 e 68636 com a troca de "abril de 2027") | 213, 647 e 1094 | a instrução de troca foi aplicada nas três; o total de 68636 (465 e 467) confere; os totais de 679 e 366 foram depois sobrescritos pelo script com o erro da seção 3 |

### Amostra de 3 totais pela regra B1 (contagem do qa, caractere a caractere)

| Toque | 1ª linha A / B | Corpo | Parte fixa | Total pela B1 | No arquivo | Resultado |
|---|---|---|---|---|---|---|
| 679 W3 (linha 184) | 56 / 54 | 252 (72 + 89 + 1 + 90) | 101 | 409 / 407 | 409 / 407 | confere |
| 679 W2 (linha 136) | 65 / 78 | 324 | 101 | 490 / 503 | 490 / 503 | confere |
| 679 pós-início (linha 213) | 59 / 61 | 357 com a data de 10 caracteres (75 + 34 + 87 + 10 + 1 + 73 + 39 + 38) | 51 | 467 / 469 | 498 / 500 | **não confere**: o arquivo usa corpo 388, que é 357 + 31, a diferença entre o marcador de 41 caracteres e a data de 10 |

O método do script está certo (primeira linha + 2 + corpo inteiro, [LINK] contando 0; 101 e 51 de parte fixa). O desvio é só de entrada: o marcador da data foi contado literalmente. Por isso conferi também os outros dois pós-início com o mesmo marcador: 68635 (linha 493, 408) e 366 (linha 641, 414) têm o mesmo excesso de 31; com a data de 10 caracteres dão 377 e 383, os valores da minha tabela 2.10 da onda3b. Os pós-início de 68628, 68617, 68636 e 68609 têm data real escrita e não são afetados.

### Conformidade educacional (só nas linhas trocadas)

| Item | O6 | O7 |
|---|---|---|
| Dados do curso batem com o catálogo e a ficha | atende (D1, D2) | atende (M2, M3, M8, M9, M10, M13, M14) |
| Urgência real e regra 7 | atende | atende (M5, M6, M7) |
| Página de destino entrega o prometido (regra 8 em 68632) | atende | atende (M3, M4) |
| Autorização de imagem e depoimento | atende (D3, D4, D7) | não se aplica |
| Demais itens | sem mudança desde a onda3b (atendem) | sem mudança desde a onda3b (atendem) |

Resultado: O6 Aprovado (x) Bloqueado ( ); O7 Aprovado (x) Bloqueado ( ). Humano: [CONFIRMAR, tabela de aprovação vazia em contexto/ufape-geral.md].

---

## 3. Correções (O7, não bloqueiam; aplicar antes do OC2)

679, pós-início (linhas 207 e 213):
- Trocar: "- **Corpo (388 caracteres, com a data do 3º módulo de 10 caracteres):**"
- Por: "- **Corpo (357 caracteres, com a data do 3º módulo de 10 caracteres):**"
- Trocar: "- **Total:** A, 498; B, 500."
- Por: "- **Total:** A, 467; B, 469."

68635, pós-início (linhas 493 e 499):
- Trocar: "- **Corpo (408 caracteres, com a data de 10 caracteres):**"
- Por: "- **Corpo (377 caracteres, com a data de 10 caracteres):**"
- Trocar: "- **Total:** A, 520; B, 522."
- Por: "- **Total:** A, 489; B, 491."

366, pós-início (linhas 641 e 647):
- Trocar: "- **Corpo (414 caracteres, com a data do 3º módulo de 10 caracteres):**"
- Por: "- **Corpo (383 caracteres, com a data do 3º módulo de 10 caracteres):**"
- Trocar: "- **Total:** A, 524; B, 526."
- Por: "- **Total:** A, 493; B, 495."

Para o script: em 679, 68635 e 366, contar "[dd/06/2027, CONFIRMAR NO CATÁLOGO, OU25]" como 10 caracteres (seção 0.3 do O7).

---

## [SUPOSIÇÃO]

- Contagem manual dos 3 totais da amostra e dos corpos de 68635 e 366 (derivados do de 679 pela diferença do nome do curso: mais 23 e menos 3 em 68635; mais 26 em 366).
- Leitura de que o erro de rótulo não bloqueia, como na onda2b (B11) e na onda3b (seção 2.10).

## Fontes

- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda3b.md (seções 2.10 e 4)
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-27-onda3.md (linhas 48 a 247 e 665 a 768)
- /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-2026-10-27-onda3.md (linhas 1 a 955 e 1050 a 1470)
