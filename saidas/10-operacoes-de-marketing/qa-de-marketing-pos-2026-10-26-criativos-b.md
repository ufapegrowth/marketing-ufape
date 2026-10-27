# QA de marketing (segunda conferência): criativos das 14 turmas de Pós, versão 2

- **Agente:** qa-de-marketing (departamento 10 Operações de Marketing)
- **Linha:** pos
- **Data:** 26/10/2026 (rodada de 26/10; conferência feita em 27/10/2026)
- **Peça revisada:** saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md, versão 2 (27/10/2026). O arquivo não foi alterado.
- **Escopo pedido pelo orquestrador:** reconferir só as correções obrigatórias C1 a C7 da primeira revisão (saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-26-criativos.md) e verificar se a versão 2 criou problema novo.
- **Entradas lidas:** a versão 2 inteira; a primeira revisão do QA; as fichas de 68615, 657, 68636, 68609, 68632, 366, 662 e 68635 em contexto/cursos/pos/ (já lidas na primeira revisão e conferidas de novo contra o texto da v2); contexto/pos-graduacao.md (padrão de nome e kit); criador-de-ganchos-pos v2 (G8 e G10); estrategia-de-midia-pos v4 (seção 3.7, kit mínimo de 3 conceitos); auditorias/conformidade-educacional.md.
- **Dados pessoais:** nenhum.

---

## 1. Veredito

**CORRIGIR, só em 68635 e 366.** As sete correções obrigatórias da primeira revisão (C1 a C7) foram resolvidas. A versão 2 criou um problema novo: o selo curto nas artes de 68635 e 366. As outras 12 turmas estão aprovadas no texto e seguem para a aprovação humana, com os bloqueios de subida que já existiam (P3, P4, PP7, U10, PR7 e URL de 68617). A busca automática de travessão e meia-risca na v2 deu zero.

---

## 2. Correções obrigatórias da primeira revisão

| Item | Onde na v2 | Resultado |
|---|---|---|
| C1, 68615-c2 | linhas 174 e 175 | Resolvido. O objetivo da ficha aparece inteiro ("capacitar o médico veterinário a trabalhar em laboratórios clínicos", mais correlação clínico-laboratorial, coleta e gestão do laboratório). Nenhuma afirmação sobre o clínico; o recorte segue [CONFIRMAR NO CATÁLOGO]. O gancho agora tem resposta honesta |
| C2, 657-r1 | linha 361 | Resolvido. Os horários ficaram restritos aos módulos 1 a 4, como na ficha |
| C3, 68636 e 68609 | linhas 515, 522, 523, 536, 694 e 707 | Resolvido. A frase "Aulas presenciais não são transmitidas" saiu de 68636-c1, c2, r1 e da adaptação e de 68609-c2 e r1. Ficou "Cronograma sujeito a ajustes", que as duas fichas trazem. A regra 1.2 restringe a frase às 11 turmas cuja ficha a traz. AP17 registrado |
| C4, 68609-c1 e e916 | linhas 686 a 688 | Resolvido. "Como é o módulo 8 presencial em Goiânia" tem 39 caracteres (cabe nos 40) e 8 palavras na imagem (cabe no limite). A abertura "Um dos módulos presenciais em Goiânia" elimina a leitura de "só um presencial" |
| C5, 68632-c1 | linhas 743 e 744 | Resolvido. "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, presencial". "Um tema por módulo" virou "um por mês" |
| C6, 366-c1 e e916 | linhas 862 e 863 | Resolvido. "9 módulos presenciais de reabilitação" no título do anúncio e da imagem |
| C7, 662 | linhas 899 a 951 | Resolvido. c1, c2 e r2 trazem só nome, campus, data da planilha e "Faculdade UFAPE". Saíram modalidade, carga horária, módulos e público. O r2 não usa mais a frase do AP7 nem a de passagem e hotel. c3 e r1 viraram estrutura sem arte. Isso cumpre a regra G10 |

---

## 3. Problema novo da versão 2 (correção obrigatória)

**N1. Selo com nome curto do curso em 68635 e 366.**
- **Onde:** 68635-c1 (linha 457), 68635-r2 (linha 485), 366-c1 (linha 863) e 366-r2 (linha 891), além das 4 adaptações e916 dessas peças, que levam o mesmo texto.
- **Problema:** para aliviar o texto na imagem (ajuste A7 da primeira revisão), o selo passou a "Clínica Médica e Emergência" e "Fisioterapia e Reabilitação Veterinária". Com isso, nenhuma linha das artes traz "Pós-graduação em <área>", e os dois nomes curtos alteram o nome do curso: o primeiro tira "de Pequenos Animais" e o segundo tira "Fisiatria". O selo funciona como rótulo do curso na arte, então lê-se como o nome de outro curso. Isso fere o padrão de nome da linha (contexto/pos-graduacao.md: "Pós-graduação em <área>" em títulos, peças e anúncios), a regra G8 da camada 2 e a regra 1.2 da própria v2. A sugestão de forma curta da primeira revisão estava errada nesse ponto; o padrão de nome vale mais que o ganho de entrega, que é só [SUPOSIÇÃO].
- **Correção:** voltar o selo para o nome completo ("Pós-graduação em Clínica Médica e Emergência de Pequenos Animais" e "Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária"), em duas linhas se precisar. Para aliviar a arte, encurtar o apoio, não o nome. Ajustar também a nota da seção 1.3 (linha 72), a nota A7 em "Mudanças desta versão" (linha 1055) e a iteração planejada de 366 (linha 858).

---

## 4. Outras conferências da versão 2 (sem correção obrigatória)

- **Ajuste A8 não aplicado** (gancho `pergunta` nos 14 r1): na primeira revisão era ajuste, não erro de conformidade. Aceito o motivo do agente (não mudar utm_content já conferido). A decisão fica com o orquestrador.
- **Kit mínimo de 662:** depois do C7, o frio de 662 tem só 2 conceitos com arte (c1 e c2); o c3 é estrutura. Hoje não bloqueia, porque 662 não sobe antes da correção de página (AP12). **Condição de subida:** o c3 precisa estar produzido e aprovado antes da estrutura nova de 662 subir, porque o kit mínimo nunca diminui e o rodízio da estratégia v4 (seção 3.7) pede 3 conceitos. O nome `662-c2-graduados_...` ficou com "graduados", sem afirmação no texto; é só rótulo interno e pode ficar.
- **Ajustes aplicados e conferidos sem problema:**
  - A1: o cabeçalho cita a estratégia v4.
  - A2: a frase de passagem e hotel tem como fonte contexto/pos-graduacao.md, com a ficha citada só onde a traz.
  - A3: o resumo e a seção 1.3 dizem certo de qual peça é cada adaptação.
  - A4: "Faculdade UFAPE" está no cartão final dos 14 vídeos.
  - A6: títulos dos cartões 1 em até 32 caracteres, com apoio separado.
  - A9: regra do AAAAMM pelo mês real da subida.
  - A10: registro para o revisor humano em 68635-c2.
- **Frase do AP7:** as 4 condições estão registradas na regra 1.2 e no AP7. O AP7 não é mais usado em 662, e 68636 e 679 estão marcados "só depois da liberação".
- **Nada novo de preço, MEC, bolsa, urgência ou turma mínima com número.** UTM e nomes dos anúncios iguais aos da v1, já conferidos.

---

## 5. Veredito por turma

| Turma | Texto |
|---|---|
| 68615, 289, 333, 657, 341, 68636, 68617, 68628, 68609, 68632, 679, 662 | aprovado (segue para a aprovação humana; bloqueios de subida mantidos; 662 só sobe com o c3 produzido) |
| 68635, 366 | corrigir (N1) |

O pacote volta para o criativos-de-anuncio só para o N1. Depois o QA confere esse item e o pacote segue para a pessoa do marketing. Nada é publicado, enviado ou pago antes disso.

---

## Lista 1. Fatos (com fonte)

- Nome oficial: "Pós-graduação em Clínica Médica e Emergência de Pequenos Animais" e "Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária" (catálogo, seção 2; fichas 68635 e 366).
- Padrão de nome da linha: contexto/pos-graduacao.md; G8 do criador-de-ganchos v2; regra 1.2 da v2.
- Kit mínimo de 3 conceitos no frio e rodízio: estrategia-de-midia-pos v4, seção 3.7.
- G10: 662 só com nome, campus e data da planilha (criador-de-ganchos v2, 0.5).
- Fichas de 68636 e 68609 sem a observação de aula presencial não transmitida; 657 com horário só nos módulos 1 a 4 (fichas).

## Lista 2. Suposições

- [SUPOSIÇÃO] Selo com nome completo pode reduzir um pouco a legibilidade e a entrega; a leitura de entrega da Meta segue sem fonte no repositório.

## Lista 3. Dados que faltam

- [CONFIRMAR] Página de 662 corrigida e c3 de 662 com conteúdo liberado antes da subida.
- [CONFIRMAR] Se as aulas presenciais de 68636 e 68609 são transmitidas (AP17).
- Demais pendências da primeira revisão seguem abertas (U10, U11, PR7, P3, P4, URL de 68617, páginas e rastreio).

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma.

Revisado por: qa-de-marketing (agente). Humano: [pendente].
Data: 26/10/2026.
