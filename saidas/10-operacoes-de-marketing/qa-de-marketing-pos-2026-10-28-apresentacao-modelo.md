# QA da apresentação modelo do plano de marketing da Pós-graduação (turma 68606)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 28/10/2026
- **Peça revisada:** apresentação de 72 slides, ordem em ferramentas/apresentacao-68606/project/deck.json, um HTML por slide em ferramentas/apresentacao-68606/project/slides/. Li o texto visível e o `<aside>` de todos os 72.
- **Regra de referência:** decisão 22 do CEO (docs/execucao-2026-10-26.md): a apresentação é o MODELO para todos os cursos, a 68606 é o primeiro preenchimento, o deck da The Growth Hub e a proposta do podcast entram só como referência nas lacunas, sempre marcados, e cada slide indica o que é fixo da linha e o que troca por turma.
- **Roteiros de origem:** saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606-estrategia.md (blocos A e B) e saidas/09-analytics-e-insights/relatorios-pos-2026-10-28-apresentacao-68606-materiais.md (blocos C e D).
- **Fontes primárias conferidas:** contexto/catalogo-de-cursos.md (seções 2 e 3, linhas 68606 e 68650); contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md (ficha inteira, inclusive os 38 participantes); saidas/10-operacoes-de-marketing/cursos/pos-68606.json (revisão 2, 28/10/2026); saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (seções 0, 1, 6A e 7, v5); saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md (cabeçalho e seção 6); saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md (seção 6, AD-A6-1); saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (seção 7).
- **Status:** rascunho de QA. Nada foi publicado, enviado ou pago. Não editei slides nem roteiros. A reconferência da versão 14 está na seção 7, no fim deste arquivo, e substitui o veredito da seção 1.

---

## 1. Veredito (primeira revisão)

**CORRIGIR.** (Substituído na reconferência da seção 7.)

Motivos que bloqueiam (detalhe na seção 2):

1. Contradição entre slides sobre o estado de duas fontes primárias que já mudaram: o JSON da 68606 (canais atualizados na revisão 2) e o gancho A6-02 (já trocado no arquivo do criador-de-ganchos). B4, B9, B14 e D10 dizem que está pendente; C12, C13 e o aside de D10 dizem que está feito (G1).
2. O slide do kit diz "O kit mínimo está escrito", contra o inventário do C1 (4 de 9 itens aprovados; posts, criativos e vídeo com 0) (G2).
3. Uso do deck da The Growth Hub sem a marca de referência em meta e conclusao, contra a decisão 22 (G4).
4. D6 tirou do texto visível as marcas [CONFIRMAR] e [DADO NÃO FORNECIDO] que o roteiro trazia (G9).
5. O exemplo de post de docente (C14, AD-A6-1) sai depois do início da turma sem a frase completa da regra do 3º módulo que a regra 6 e o OA12 exigem (G10).
6. auditorias/conformidade-educacional.md: dois itens seguem sem marcação para os exemplos de peça (página de destino em conformidade e política de privacidade no rodapé e no formulário). São pendências externas já declaradas no deck (C15, D8), mas pela regra o veredito é corrigir até a Ufape resolver ou até os exemplos saírem marcados como "não enviar antes do OA10 e da p04" (seção 4).

O resto confere: números, datas, nomes e titulações dos blocos novos batem com as fontes primárias; os textos de peça dos slides c* são literais da fonte (com as exceções avaliadas em G12); não há "certificado/reconhecido pelo MEC" como afirmação, nem "agência", nem telefone, nem urgência sem a regra completa; o nome "Pós-graduação em Gastroenterologia Veterinária" e o "Workshop Brasileiro de Neuromonitorização" estão corretos em todos os slides, com uma exceção de nome incompleto num teste de primeira linha (G11). Os slides das partes 03 e 04, já aprovados na reconferência, continuam com o conteúdo aprovado; os achados neles são só de selo, marca do deck e encaixe.

Depois das correções G1, G2, G4, G9 e G10, e com os ajustes G3, G5 a G8 e G11 a G19, a apresentação volta ao qa para uma reconferência curta (só os slides citados).

---

## 2. Achados

Legenda: **bloqueio** impede a aprovação; **ajuste** precisa entrar nesta rodada, mas sozinho não bloquearia.

### G1. Estado do JSON e do gancho A6-02 contraditório entre slides (bloqueio)

Fonte primária: pos-68606.json está na revisão 2 (28/10/2026), com o histórico "canais ... para: instagram ativo; facebook ativo; whatsapp ativo; podcast ativo ...; youtube ativo só no orgânico (pago fora); linkedin fora; tiktok fora; x fora", aplicado pelo cmo. Em criador-de-ganchos-pos-2026-10-26.md, seção 6, o A6-02 e o A6-08 já trazem "Pós-graduação em Gastroenterologia Veterinária". Os roteiros de origem são anteriores a essas mudanças; nos slides vale a fonte primária.

- **slides/b4.html, linha da tabela**
  - Atual: `JSON da 68606 | YouTube ativo, LinkedIn em teste | plano da onda 1 e decisão 21`
  - Correção: `JSON da 68606 | revisão 1: YouTube ativo, LinkedIn em teste, podcast fora | revisão 2 (28/10): plano da onda 1 e decisão 21`
  - No aside, trocar "JSON da 68606: gerado em 27/10 com os canais do plano geral; vale o plano da onda 1 mais a decisão 21." por "JSON da 68606: gerado em 27/10 com os canais do plano geral; atualizado pelo cmo na revisão 2 (28/10/2026) pelo plano da onda 1 e pela decisão 21."
- **slides/b14.html, aside**
  - Atual: "Pendência deixada pelo qa: atualizar os canais do JSON pela decisão 21 (slide de divergências)."
  - Correção: "Pendência deixada pelo qa, já resolvida: os canais do JSON foram atualizados pelo cmo na revisão 2 (28/10/2026), pela decisão 21."
- **slides/b9.html, aside**
  - Atual: "Correção do qa (F15): A6-02 com o nome padrão "Pós-graduação em Gastroenterologia Veterinária"; o arquivo do criador-de-ganchos ainda precisa da troca."
  - Correção: "Correção do qa (F15): A6-02 com o nome padrão "Pós-graduação em Gastroenterologia Veterinária"; a troca já foi feita no arquivo do criador-de-ganchos em 28/10/2026 (A6-02 e A6-08)."
- **slides/d10.html, título e tabela**
  - Atual (título): "Cinco números e frases com mais de uma leitura."
  - Atual (linha): `Canais no mapa | o mapa trazia podcast "fora" e LinkedIn "teste"; a decisão 21 e o qa dizem outra coisa | orquestrador`
  - Correção: retirar a linha "Canais no mapa" (deixou de ser dúvida) e trocar o título para "Quatro números e frases <span>com mais de uma leitura.</span>". O aside pode ficar como está, porque já registra a revisão 2.

### G2. Slide do kit contradiz o inventário do C1 (bloqueio)

- **slides/kit.html, título**
  - Atual: "O kit mínimo está escrito. Falta inventário, página e aprovação."
  - Correção: "Quatro itens do kit estão escritos. <span>Cinco seguem pendentes, com a página.</span>"
  - Motivo: C1 e pos-68606.json mostram posts orgânicos 0 de 6, criativos 0 de 3 escritos pela squad, roteiro de vídeo 0 de 1 e página sem contar como entregue.
- **slides/kit.html, coluna "Inventário pendente"**
  - Atual: "Posts por docente: 1 de 38"
  - Correção: "Posts por docente: 1 de 38 (AD-A6-1 em rascunho)", para bater com C1 ("1 de 38 (AD-A6-1) | rascunho").

### G3. Contagem de dias atribuída ao mapa está errada (ajuste)

- **slides/d10.html, linha "Dias até o início"**
  - Atual: "10 dias de 28/10 a 07/11, mesma contagem do mapa"
  - Correção: "10 dias de 28/10 a 07/11; o mapa (27/10) registra 11 e o plano geral (26/10) cita 12"
  - Fonte: pos-68606.json, "dias_ate_inicio": 11, "gerado_em": "2026-10-27"; aside de b1 ("12 dias para o início").

### G4. Deck da The Growth Hub usado sem marca de referência (bloqueio, decisão 22)

- **slides/meta.html, cabeçalho e caixa "A conta fecha?"**
  - Atual: o cabeçalho tem só os dois selos de MODELO; a caixa diz "O deck cita CPA de R$ 210,51 na conta: se for custo por matrícula, já passa do teto."
  - Correção: acrescentar no cabeçalho o selo `<p style="font-size:24px;color:#d9ff83;border:1px solid #d9ff83;padding:6px 16px;border-radius:6px;white-space:nowrap">Referência do deck da The Growth Hub</p>` (mesmo padrão de publico.html) e trocar a frase por "Referência do deck da The Growth Hub para a lacuna "o que o CPA mede": CPA de R$ 210,51 na conta; se for custo por matrícula, já passa do teto."
- **slides/conclusao.html, coluna "Onde"**
  - Atual: "Cinco praças com 76,7% da base; SP com 55% da verba."
  - Correção: "Cinco praças com 76,7% da base e SP com 55% da verba (referência do deck da The Growth Hub)." e acrescentar no cabeçalho o selo "Referência do deck da The Growth Hub", com borda contínua escura, como nos outros slides.

### G5. Lista das lacunas em que o deck entra está incompleta (ajuste)

O deck aparece como referência em praças (pracas), divisão da verba por praça (verba, b15, d6), público no Meta (publico), CPA (meta, d5, decisoes) e painéis de leitura (proximos, d4). b0 e o aside do índice citam só duas lacunas.

- **slides/b0.html, tarja cinza**
  - Atual: "Referência do deck da The Growth Hub só para as lacunas: praças por cadastro e público base no Meta"
  - Correção: "Deck da The Growth Hub só como referência nas lacunas: base por praça, divisão da verba, público no Meta, CPA e painéis"
- **slides/indice.html, aside**
  - Atual: "O deck da The Growth Hub entra só como referência nas lacunas "onde está a base" (praças) e "como segmentar no Meta" (público base), marcadas nos slides."
  - Correção: "O deck da The Growth Hub entra só como referência nas lacunas "onde está a base" (praças), "como dividir a verba por praça", "como segmentar no Meta" (público base), "o que o CPA mede" e "painéis de leitura", marcadas nos slides."

### G6. Tarja de b4 descreve divergência como lacuna (ajuste)

- **slides/b4.html, tarja e tabela**
  - Atual (tarja): "Linhas em destaque: referência do deck da The Growth Hub para lacuna de divisão por praça e público"
  - Correção (tarja): "Linhas em destaque: divergência com o deck da The Growth Hub; vale a squad. Do deck fica só a referência para a divisão por praça e a idade de partida"
  - Atual (linha): "deck: R$ 3.000 · squad: R$ 2.000,00"
  - Correção: "deck: R$ 3.000,00 · squad: R$ 2.000,00" (mesmo formato de valor em todo o deck).

### G7. Selos de MODELO incompletos em slides que misturam campos (ajuste, decisão 22)

- **slides/canais.html:** tem só "fixo da linha", mas a coluna "Estado na 68606" e os motivos (6 posts do kit, 4 toques) trocam por turma (o próprio b4 trata os canais do JSON como "troca por turma"). Correção: acrescentar o selo "MODELO · troca por turma" e mudar o cabeçalho da coluna para "Estado na 68606 (troca por turma)".
- **slides/pracas.html:** tem só "troca por turma", mas a base de 10.447 cadastros e a divisão vêm do deck para a conta toda e valem para toda turma de Pós. Correção: acrescentar o selo "MODELO · fixo da linha" e, no rodapé, "Fixo da linha: base e divisão da conta. Troca por turma: só se o campus da turma mudar o peso de Goiás + DF."
- **slides/episodio-funil.html:** tem só "fixo da linha", mas a chamada ("Até 06/11, a data de início") e a UTM pos_68606 são da turma. Correção: acrescentar o selo "MODELO · troca por turma" e trocar "Até 06/11, a data de início; depois, a frase completa do 3º módulo." por "Até a véspera do início, a data de início; depois, a frase completa do 3º módulo (troca por turma: datas da ficha)."
- **slides/publico.html:** tem "fixo da linha" e o selo do deck, mas o título cita a área da turma ("Gastroenterologia não é interesse no Meta"). Correção: acrescentar o selo "MODELO · troca por turma" ou trocar o título para "A especialidade não é interesse no Meta. <span>O criativo faz a especialidade.</span>" e manter só "fixo da linha".

### G8. Slides mistos sem dizer qual campo é fixo e qual troca (ajuste, decisão 22)

A decisão 22 pede que cada slide indique o que é fixo e o que troca. Os slides abaixo têm os dois selos e nenhuma indicação por campo. Para não estourar a altura, a marca entra na própria linha do campo.

- **slides/meta.html:** em "Meta em reais (uso interno): 15 x R$ 35.400,00 = R$ 531.000,00, ou 265,5 vezes a verba." acrescentar "(troca por turma: preço do catálogo)"; no título, nada muda (R$ 2.000,00, 15 e R$ 133,33 são fixos da linha, decisões 15 e 16).
- **slides/verba.html:** no parágrafo "Teto, não meta [...]" acrescentar no fim "Fixo da linha: fórmula e percentuais. Troca por turma: G e as datas das fases (ficha e PP15)."
- **slides/regua.html:** no parágrafo de rodapé, trocar "Textos aprovados pelo qa; cada envio espera aprovação humana (OA9)." por "Fixo da linha: teto, alertas e regras. Troca por turma: datas e textos (OA9 e copy-de-mensagens da onda). Cada envio espera aprovação humana."
- **slides/kit.html:** na caixa do número 9, acrescentar "Fixo da linha: itens e mínimos. Troca por turma: situação e pendências (JSON)."
- **slides/decisoes.html:** nas linhas 5, 6 e 10 (U11; OU3, OU6, OU8; podcast) acrescentar "· linha"; nas demais, "· turma".
- **slides/conclusao.html:** no parágrafo abaixo do valor, trocar "A captação da 68606 vai até 22/01/2027." por "A captação da 68606 vai até 22/01/2027 (troca por turma: véspera do 3º módulo)."

### G9. D6 perdeu as marcas [CONFIRMAR] e [DADO NÃO FORNECIDO] no texto visível (bloqueio)

O roteiro trazia uma coluna "Situação" com as marcas e o título "... gasto, leads, inscrições e matrículas são [CONFIRMAR]". O slide moveu tudo para o aside.

- **slides/d6.html, parágrafo de rodapé**
  - Atual: "Para outra turma: JSON da turma (numeros_agregados, metas), exportações do gerenciador e CRM."
  - Correção: "Situação de todos os itens: [CONFIRMAR]; leads: [DADO NÃO FORNECIDO]. Para outra turma: JSON da turma (numeros_agregados, metas), exportações do gerenciador e CRM."
  - Encaixe: o rodapé passa a duas linhas; a estimativa sobe para cerca de 796 px, dentro de 824 [SUPOSIÇÃO de estimativa].

### G10. Exemplo de post de docente sem a regra completa depois do início (bloqueio da peça e do modelo)

- **slides/c14.html, tela 3** (literal de autoridade-docente-pos-2026-10-26.md, AD-A6-1)
  - Atual: "[PONTO DE VISTA A CONFIRMAR COM O DOCENTE]" e "Fale com o time para saber como entrar na turma."
  - Problema: os Stories saem de 09 a 15/11, depois do início (07/11). A regra 6 do plano da onda 1 ("depois do início, frase completa da regra do 3º módulo") e o OA12 do pos-68606.json ("Publicar os posts de docente com chamada para a turma e a regra completa") pedem a frase inteira em toda chamada de entrada depois do início. Como a apresentação é modelo, o erro se repetiria em toda turma.
  - Correção na fonte (agente autoridade-docente, AD-A6-1, tela 3): "[PONTO DE VISTA A CONFIRMAR COM O DOCENTE]" e "A turma começou em 07/11/2026. A Ufape aceita matrícula até o 3º módulo do curso; nesta turma, o 3º módulo começa em 23/01/2027. Antes de pagar, o time explica como ficam os módulos que já aconteceram. Fale com o time para saber como entrar na turma."
  - Correção no slide, depois da fonte: copiar a tela 3 nova, literal. Até lá, acrescentar ao primeiro parágrafo de rodapé: "Antes de publicar: a tela 3 recebe a frase completa da regra do 3º módulo (regra 6, OA12)."

### G11. Nome do curso incompleto num teste de primeira linha (ajuste)

- **slides/c4.html, aside** (literal de copy-de-mensagens-pos-onda1, 6A.2)
  - Atual: "Primeira linha A (teste): "Olá, [nome]. Prática de cirurgia esofágica, gástrica e intestinal na Pós-graduação em Gastroenterologia.""
  - Correção na fonte (agente copy-de-mensagens, 6A.2, primeira linha A e a reserva "Grupo de discussão de casos com a coordenação, na Pós-graduação em Gastroenterologia."): trocar "Pós-graduação em Gastroenterologia" por "Pós-graduação em Gastroenterologia Veterinária". Depois, copiar a linha corrigida no aside de c4.

### G12. Exceções de literalidade registradas pelo fork

| Exceção | Avaliação | Correção |
|---|---|---|
| Link sem https e sem UTM no texto visível de c4 e c5 | Aceitável: o link completo, literal, está no aside dos dois slides. Risco: alguém copiar o link do balão sem UTM. | Em slides/c4.html e slides/c5.html, logo depois do link, acrescentar `<br><span style="color:#9fa49c">link completo, com https e UTM, nas notas</span>` (cor #5d6259 em c5). Encaixe: +32 px, cabe [SUPOSIÇÃO de estimativa]. |
| Número do WhatsApp retirado do aside de c9 | Aceitável. É número comercial, não dado pessoal, mas a regra da apresentação pede atenção a telefones e o número continua na fonte (6A.4) e em contexto/ufape-geral.md. | Nenhuma. |
| Perguntas R3 e R5 encurtadas em c17 | Aceitável: o sentido não muda e o texto inteiro está no aside. | Em slides/c17.html, no parágrafo de rodapé, acrescentar "Perguntas R2, R3 e R5 encurtadas; texto inteiro nas notas." |
| Pergunta R2 encurtada em c17 | Não aceitável como está: o corte tira "A página diz que" e "Já passou", e a pergunta passa a soar como regra da Ufape, quando a data de corte deixou de ser limite (decisão 18, OU8). | Atual: "R2 “A 1ª mensalidade é paga 30 dias antes. Ainda consigo entrar?” · vou confirmar". Correção: "R2 “A página diz: 1ª mensalidade 30 dias antes. Já passou, ainda consigo entrar?” · vou confirmar". |
| Situações abreviadas ("qa aprovado · aguarda ok humano", "aguarda OA9") | Aceitável, com um caso ambíguo. | Em slides/c2.html, linha "Respostas do time (10)": trocar "qa aprovado · aguarda ok" por "qa aprovado · aguarda ok humano". |

### G13. Encaixe em 824 px de altura útil (ajuste)

Estimativa por contagem de caracteres (cerca de 12 px por caractere a 24 px, 32 px a 64 px, células de tabela com cerca de 55 px por linha de texto) [SUPOSIÇÃO de estimativa; conferir no render]. Observação: o padding é 128 px em cima e 160 px embaixo, então a caixa de conteúdo tem 792 px; até 824 px o texto ainda não encosta no rodapé fixo.

| Slide | Estimativa | Situação | Correção |
|---|---|---|---|
| slides/c1.html | cerca de 821 px | no limite; passa da caixa de 792 px | Título atual: "Kit mínimo da turma: 4 itens aprovados pelo qa, 5 pendentes." Correção: "Kit da turma: <span>4 aprovados pelo qa, 5 pendentes.</span>" (uma linha, cerca de 67 px a menos). |
| slides/curso.html | cerca de 822 px | no limite; o selo novo faz a etiqueta quebrar em duas linhas | Etiqueta atual: "03 · O curso exemplo · Pós-graduação em Gastroenterologia Veterinária · São Paulo · 68606". Correção: "03 · Pós-graduação em Gastroenterologia Veterinária · 68606" (São Paulo já aparece em "Campus e coordenação"). |
| slides/d9.html | cerca de 812 px | apertado | Linha 1, coluna "Situação", atual: "“Profa. Ísis Carvalho” e “ESP. Isis de Carvalho Rodrigues Santana Lemes” podem ser a mesma pessoa". Correção: "“Profa. Ísis Carvalho” e “ESP. Isis de Carvalho Rodrigues Santana Lemes”: mesma pessoa?" |
| slides/c2.html | cerca de 778 px | cabe | Nenhuma. |
| slides/c17.html | cerca de 775 px | cabe, mesmo com a R2 de G12 | Nenhuma além de G12. |
| slides/d6.html | cerca de 762 px hoje; cerca de 796 px com G9 | cabe | Nenhuma além de G9. |

Os demais slides ficam entre 650 e 800 px na mesma estimativa. Os mais próximos do limite, sem correção necessária: b0 (cerca de 784 px, cerca de 790 px com G5), a6 (cerca de 790 px), b4 (cerca de 787 px), d3 (cerca de 785 px), calendario (cerca de 782 px).

### G14. Referências internas quebradas e marcadores de campo perdidos (ajuste)

Os slides não mostram os códigos C1 a C19 nem números de página, e o HTML engoliu os `<...>` dos campos.

- **slides/conclusao.html, aside:** "dez respostas da Ufape (slide 17)" passa a "dez respostas da Ufape (slide Decisões, 59 de 72)".
- **slides/c2.html, texto visível:** "decisão 14 (slide C18)" passa a "decisão 14 (slide Relacionado)". Mesma troca nos asides de c1, c12 e c15 ("slide C18" por "slide Relacionado") e de c1, c4 e c5 ("slide C2" por "slide Além do kit").
- **slides/c19.html, texto visível:** "pos-código.json" passa a "pos-&lt;código&gt;.json".
- **slides/b6.html, aside:** "nome sempre "Pós-graduação em área"" passa a "nome sempre "Pós-graduação em &lt;área&gt;"".
- **slides/b7.html, aside:** "pós-graduação em área" passa a "pós-graduação em &lt;área&gt;".
- **slides/c11.html, aside:** "(K área.x)" passa a "(K&lt;área&gt;.x)" e "pós-graduação em área veterinária" passa a "pós-graduação em &lt;área&gt; veterinária".
- **slides/b2.html, aside:** "UTM pos_código_AAAAMM do primeiro envio" passa a "UTM pos_&lt;código&gt;_&lt;AAAAMM do primeiro envio&gt;".

### G15. Valor de inscrição sem a marca de uso interno (ajuste)

- **slides/d2.html, linha "Em dúvida: U11, valor da inscrição", coluna "O que falta"**
  - Atual: "R$ 260,00 (CEO) ou R$ 250,00 (site; R$ 350,00 em 3 cursos)?"
  - Correção: "R$ 260,00 (CEO) ou R$ 250,00 (site; R$ 350,00 em 3 cursos)? · uso interno"

### G16. Acréscimo do podcast citado como se estivesse no JSON (ajuste)

- **slides/c1.html, aside**
  - Atual: "Fonte: pos-68606.json (kit.entregas, kit.acrescimos, kit.inventario) [...] pacote do podcast (acréscimo da decisão 21, a fazer)."
  - Correção: "pacote do podcast (acréscimo da decisão 21, a fazer; ainda não lançado em kit.acrescimos do JSON [CONFIRMAR com o cmo])". No mesmo aside, depois de "post por docente, autoridade-docente-pos-2026-10-26.md (38 docentes na ficha, 1 rascunho)", acrescentar "; no JSON o item ainda consta como inventario_pendente".

### G17. Registro da troca do A6-08 atribuído à F15 (ajuste)

- **slides/c13.html, aside**
  - Atual: "o A6-02 e o A6-08 traziam "pós de Gastroenterologia" no arquivo-fonte; os dois foram trocados para "Pós-graduação em Gastroenterologia Veterinária" no arquivo do criador-de-ganchos em 28/10/2026 (correção F15 do qa)."
  - Correção: "o A6-02 e o A6-08 traziam "pós de Gastroenterologia" no arquivo-fonte; os dois foram trocados para "Pós-graduação em Gastroenterologia Veterinária" no arquivo do criador-de-ganchos em 28/10/2026 (o A6-02 pela correção F15 do qa; o A6-08 na mesma troca). O cabeçalho do arquivo ainda diz versão 2 de 26/10 e não registra a mudança [CONFIRMAR com o orquestrador]."

### G18. Objeções da casa de mensagens sem a marca [SUPOSIÇÃO] (ajuste)

- **slides/c3.html, aside**
  - Atual: "Objeções e respostas (literal): ..."
  - Correção: "Objeções [SUPOSIÇÃO] e respostas (literal): ..." (a fonte, mensagens-pos seção 7, marca a coluna "Objeção [SUPOSIÇÃO]").

### G19. R8 também tem "vou confirmar" (ajuste de coerência com D1)

D1 diz que R2, R5 e R8 ficam em "vou confirmar" (OU8), e a fonte (copy-de-mensagens, R8) tem dois ramos de "vou confirmar" (A-C2 e OU8). C17 marca só R2, R4, R5 e R6.

- **slides/c17.html, balão R8**
  - Atual: "R8 “Tem bolsa ou desconto para entrar agora?”"
  - Correção: "R8 “Tem bolsa ou desconto para entrar agora?” · vou confirmar"
- **slides/c8.html (ajuste menor no mesmo bloco de peças):** o texto de pré-visualização aparece sem rótulo. Atual: "Turma IX começa em 07/11/2026. Veja o cronograma e as condições na página." Correção: "<b>Pré-visualização:</b> Turma IX começa em 07/11/2026. Veja o cronograma e as condições na página."

---

## 3. Conferência por foco pedido

### 3.1 Fidelidade aos roteiros e às fontes primárias

- **Curso (catálogo, linha 68606):** nome, São Paulo, semipresencial, 07/11/2026, turma IX, 500 h, 30x de R$ 1.180,00, R$ 35.400,00, matrícula R$ 250,00, status "aberto". Confere em curso, meta, b0, c4 a c9.
- **Ficha 68606:** módulos 1 (07 e 08/11/2026), 2 (19 e 20/12/2026), 3 (23 e 24/01/2027), todos online; presenciais 6 (17 e 18/04/2027), 13 (27 e 28/11/2027, endoscopia) e 21 (julho de 2028, videocirurgia); coordenação Esp. Maria Carolina Pappalardo; 38 nomes (39 linhas com a coordenação repetida). Contagem por titulação do slide docentes (17 Dr./Dra., 12 MSc., 6 Esp., 3 Profa.) confere. Dra. Cibele Figueira Carvalho, Dr. Rodolfo Oliveira Leal, DR. Fabrizio Grandi, DRA. VIVIANE DE MARCO e DRA. Maria Anete Lallo com a grafia e a caixa da ficha.
- **Mensagens (c4 a c9):** corpos, assuntos, pré-visualização, datas, horários, templates e UTM literais de copy-de-mensagens-pos-onda1 v5, seções 6A.1 a 6A.4. Links iguais a pagina_oficial do JSON; utm_campaign=pos_68606_202610 segue a regra 11.
- **Respostas (c17):** R1 e as notas literais da seção 7; tabela 7.2 confere (2º módulo 19 e 20/12/2026; 3º módulo 23 e 24/01/2027; gravação "não consta").
- **Ganchos (c12, c13, mensagem):** literais da seção 6 do criador-de-ganchos, já com o nome padrão no A6-02 e no A6-08.
- **AD-A6-1 (c14):** literal da seção 6 do autoridade-docente, inclusive a UTM pos_68606_202611 e o encaixe S3.
- **Casa A6 (c3):** promessa e pilares literais da seção 7 de mensagens-pos.
- **Prova 68650 (c18):** catálogo, seção 3: São Paulo, 27/11/2026. Confere.
- **Contas:** 87 dias de 28/10/2026 a 22/01/2027; 80 dias equivalentes com 14 dias pela metade; R$ 2.000,00 / 80 = R$ 25,00; fase 1 R$ 250,00 e fase 2 R$ 1.750,00; R$ 2.000,00 / 15 = R$ 133,33; 15 x R$ 35.400,00 = R$ 531.000,00. Os dias da semana de todas as datas (qua 28/10, qui 29/10, sex 06/11, qua 02/12, qua 16/12, ter 12/01, terças dos episódios, sex 22/01) conferem.
- **Onde o slide diverge do roteiro, vale o slide:** b9, b14 e d10 seguem o roteiro antigo; c12 e c13 seguem a fonte nova (G1). O título do roteiro do C1 ("4 escritos e aprovados; 5 seguem com inventário pendente") estava impreciso (o post de docente é rascunho, não inventário pendente); o slide corrigiu para "5 pendentes".

### 3.2 Marcas [SUPOSIÇÃO], [CONFIRMAR] e [DADO NÃO FORNECIDO]

Preservadas em a1 a a6, b2, b3, b6, b11 a b16, meta, verba, publico, canais, regua, pauta, c1, c2, c6, c8, c10, c11, c13, c14, c15, c17, c19, kit, d1 a d5, d7, d8 e d10. Faltas: d6 (G9) e c3 (G18).

### 3.3 Regra da decisão 22

- **Selos:** presentes nos 72 slides. Ajustes em canais, pracas, episodio-funil e publico (G7). Indicação por campo faltando em meta, verba, regua, kit, decisoes e conclusao (G8).
- **Deck só como referência e marcado:** marcado em b0, a6, b4, b15, verba, pracas, publico, proximos, d4, d5 e d6. Sem marca em meta e conclusao (G4). Lista de lacunas incompleta em b0 e no índice (G5).
- **Divergências deck contra squad com o que vale:** b4 (verba: vale decisão 15; cinco campanhas e idade: vale AP-1, idade do deck como partida), verba (recomendação do cmo), publico (idade), mensagem (nome abreviado trocado pelo nome padrão), meta (CPA em [CONFIRMAR]). Ajuste de redação da tarja em b4 (G6).

### 3.4 Regras gerais

- **Travessão e meia-risca:** nenhum encontrado na leitura dos 72 arquivos. O separador usado é o ponto médio (·). A varredura dos caracteres U+2014 e U+2013 é do orquestrador [SUPOSIÇÃO: a leitura não substitui a busca por caractere].
- **"Certificado/reconhecido pelo MEC":** não aparece como afirmação. A frase só é citada como problema da página (b7, b12, kit, c15, d2, d8, decisoes).
- **The Growth Hub:** sempre pelo nome (ou "deck TGH" em d4 e d5, com o nome completo no aside). Nunca "agência".
- **Dados pessoais e telefones:** nenhum telefone nos 72 slides. Nomes só de docentes, com autorização (decisões 8 e 10).
- **Preço:** marcado como uso interno em curso, meta e decisoes; falta a marca em d2 (G15).
- **Urgência:** nenhuma "últimas vagas", contador ou data do 3º módulo sozinha nas peças. Exceção de regra 6 no AD-A6-1 (G10).
- **"Pós-graduação em":** correto em todos os textos de peça; nome incompleto em um teste de primeira linha (G11). Os termos de busca K6.2 a K6.5 ("pós em ...") são palavras-chave, não nome de curso, e o slide já diz que K6.4 nunca vai para texto visível.
- **"Workshop Brasileiro de Neuromonitorização":** nome exato em b2, b10, regua, calendario e pauta. Nenhum "simpósio".

### 3.5 Coerência entre partes

- **Iguais em todos os slides:** R$ 2.000,00; 15 matrículas; R$ 133,33; R$ 25,00 por dia; 80 e 87 dias; 22/01/2027, 23h59; 23/01/2027; 38 docentes e lacuna de 37; 9 pendências; 6 toques (28/10, 29/10, 06/11, 02/12, 16/12, 12/01); 5 episódios de 24/11 a 19/01; 30%, 25%, 20%, 14% e 11%; 76,7% da base; CPA de R$ 210,51; 180 ganchos e 54 recomendados.
- **Divergentes:** estado do JSON e do A6-02 (G1); "kit escrito" contra o inventário (G2); dias até o início (G3); "vou confirmar" de R8 entre c17 e d1 (G19).
- **Índice contra partes:** as sete partes e o fechamento batem com a ordem do deck.json e com as etiquetas dos slides: 01 com a1 a a6; 02 com b1 a b16; 03 com curso a docentes; 04 com podcast, episodio-funil e pauta; 05 com c1 a c19; 06 com calendario, kit, decisoes e proximos; 07 com d1 a d10; "+" com conclusao e anexo. O b0 fica na abertura, como o índice explica no aside. Sem achado.

---

## 4. auditorias/conformidade-educacional.md, item por item (primeira revisão)

Aplicada aos exemplos de peça da apresentação: e-mails T1 e E2 (c8, c9), WhatsApp T2, W2, W3 e W4 (c4 a c7), textos de anúncio Meta (c10 e mensagem), palavras-chave Google (c11), ganchos (c12, c13), Stories AD-A6-1 (c14), respostas do time (c17) e a apresentação como documento interno.

**DADOS DO CURSO**
- [x] Nome, modalidade, carga horária, duração e turno batem com o catálogo e a ficha (Pós-graduação em Gastroenterologia Veterinária, semipresencial, 500 h, 24 módulos, turma IX).
- [x] Status "aberto" no catálogo. Depois de 07/11, o envio depende do OU9; a exceção da decisão 18 cobre o status "verificar" por turma iniciada (c9, d1).
- [x] Modalidade clara: teoria online e módulos presenciais com número e data.

**REGULAÇÃO (MEC)**
- [x] Graduação: não se aplica.
- [x] Pós lato sensu: nenhuma peça diz "reconhecida pelo MEC"; como o texto de validade aprovado não existe (p01), nenhuma peça afirma certificação.
- [x] Curso livre: não se aplica.
- [x] Nota MEC: não aparece.

**PROMESSAS E PROVAS**
- [x] Nenhuma promessa de emprego, salário, promoção ou aprovação.
- [x] Nenhum dado de empregabilidade ou satisfação em peça.
- [x] Nenhum superlativo; "referências nacionais" e "emergente e carente" ficam fora das peças.
- [x] Nenhuma comparação com concorrente em peça.

**PREÇO E CONDIÇÕES (CDC)**
- [x] Nenhuma peça mostra preço; todas mandam para "parcelas, total e matrícula" na página.
- [x] Nenhuma bolsa ou desconto oferecido (R8: "não tenho bolsa nem desconto confirmados").
- [x] Urgência real: a data do 3º módulo só aparece dentro da frase completa da regra. Ressalva de regra 6 no AD-A6-1, tratada em G10 (não há urgência falsa, mas falta a frase).
- [x] Prouni, Fies ou financiamento: não aparecem.

**PESSOAS E DADOS (LGPD E DIREITO DE IMAGEM)**
- [x] Docentes e coordenação com autorização registrada (decisões 8 e 10); nenhum depoimento.
- [x] Menores de idade: não aparecem.
- [ ] **Formulários com finalidade e link para a política de privacidade:** o rodapé do e-mail tem "Política de privacidade: [link]" e o endereço segue [CONFIRMAR] (p04); o formulário da página não tem política (D8). Bloqueia o envio dos e-mails e a mídia até a p04. O que muda: a Ufape informa o endereço e o CRM insere o link no rodapé; nos slides c8 e c9, acrescentar ao texto visível "Envio só depois da p04 (política de privacidade) e do OA10."
- [x] WhatsApp e e-mail só com opt-in, com "responda SAIR", botão "Sair" e descadastro em um clique.
- [x] Nenhum dado pessoal de aluno ou candidato; nenhum telefone nos slides.

**PLATAFORMAS**
- [x] Textos de anúncio sem segmentação discriminatória; público por profissão e formação (publico).
- [ ] **Página de destino entrega o que a peça promete:** a página oficial ainda tem a frase de certificação, a turma mínima de 20 e não traz a regra do 3º módulo (OA10; A7, A12, A13). Bloqueia envio e mídia, como o deck já registra em c15 e d8. O que muda: a Ufape corrige a página; até lá, os exemplos de peça levam a marca da linha acima.

**ANÚNCIOS (META E GOOGLE)**
- [x] Nenhum texto afirma ou insinua característica pessoal de quem vê ("para médicos veterinários formados" descreve o público do curso, como no exemplo que passa na auditoria).
- [x] Sem urgência falsa, contador ou elemento que imita a plataforma.
- [x] Sem pessoa pública nem parceria inexistente.
- [x] Sem caixa alta excessiva nos textos de anúncio. Os nomes em caixa alta (DRA. VIVIANE DE MARCO) estão na casa de mensagens e no gancho A6-01, como na ficha; se o A6-01 virar anúncio, vale revisar a caixa com a Ufape [SUPOSIÇÃO de risco de reprovação].
- [ ] **Página de destino com dados da Ufape, contato e política de privacidade:** mesma pendência da p04.
- [x] Nenhuma sugestão para driblar a análise.

**RESULTADO:** Aprovado ( ) Bloqueado (x)

Itens bloqueados e o que precisa mudar: política de privacidade (p04) e página de destino (OA10), ambos externos e já declarados no deck; até a resolução, os slides c8 e c9 dizem no texto visível que o envio espera a p04 e o OA10 (c4 a c7 já dependem do OA9, que cita a página). Além disso, G10 para o AD-A6-1.

Revisado por: qa-de-marketing (agente). Humano: [pessoa do marketing; responsável pela regulação, conforme contexto/ufape-geral.md, tabela de aprovação ainda sem nome].

Data: 28/10/2026.

---

## 5. auditorias/02-estrategia-e-posicionamento.md, item por item (apresentação como plano modelo)

- [x] **Uma única meta principal:** pelo menos 15 matrículas por turma (decisão 16), com R$ 133,33 por matrícula no máximo.
- [x] **Persona e curso nomeados:** P1, clínico de pequenos animais de 24 a 40 anos [SUPOSIÇÃO do contexto]; Pós-graduação em Gastroenterologia Veterinária, 68606.
- [x] **8 canais avaliados, com motivo para os de fora:** slide canais (LinkedIn, TikTok e X fora, com motivo), b9 e b16.
- [x] **Alternativa real nomeada:** residência, curso curto, EAD, adiar (a3, b6).
- [x] **Todo pilar tem prova:** prática com data (módulos 6, 13 e 21), quem ensina (coordenação e 38 nomes), condições claras (página e "a turma pode não ser formada").
- [ ] **Regras de voz com exemplos:** a voz segue [SUPOSIÇÃO] (b6) e os exemplos aprovados pela Ufape estão listados como lacuna (d4). Não é erro de redação; fica pendente da Ufape.
- [x] **Cabe no tempo e na verba:** nenhuma verba nova; podcast fora da verba de mídia, com custo [CONFIRMAR]; horas do time [CONFIRMAR U8].
- [x] **Nenhuma oferta, pilar ou resposta promete emprego, aprovação ou salário.**
- [x] **Preços e condições do catálogo ou marcados:** preço do catálogo, só uso interno; inscrição de R$ 260,00 em [CONFIRMAR U11]. Marca de uso interno faltando em d2 (G15).

---

## 6. Regra de aprovação e próximo passo (primeira revisão)

- A apresentação **volta para os agentes que a produziram**: o orquestrador, que montou os slides, aplica G1 a G9 e G11 a G19 nos HTML; o agente autoridade-docente corrige a tela 3 do AD-A6-1 (G10) e o agente copy-de-mensagens corrige o nome na primeira linha A e na reserva da 6A.2 (G11), cada um no próprio arquivo, e o orquestrador copia o texto novo para c14 e c4. Os roteiros do cmo (B4, B9, B14) e do relatorios (D10, nota do C13) ficaram desatualizados em relação à fonte primária; vale registrar a atualização neles.
- Depois, reconferência do qa só nos slides citados. Com APROVADO, segue para a aprovação humana (pessoa do marketing e, nas peças com regulação, o responsável indicado em contexto/ufape-geral.md).
- Nada é publicado, enviado ou pago a partir deste arquivo.

---

## Fatos (com fonte)

- Linha 68606 do catálogo: contexto/catalogo-de-cursos.md, seção 2; prova 68650: seção 3.
- Cronograma, presenciais, coordenação e 38 participantes: contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md.
- Revisão 2 do JSON com os canais da decisão 21, 9 pendências, dias_ate_inicio 11, acréscimos do kit sem o pacote do podcast: saidas/10-operacoes-de-marketing/cursos/pos-68606.json.
- Textos de e-mail, WhatsApp e respostas: saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md, seções 6A e 7 (v5).
- A6-02 e A6-08 com o nome padrão; cabeçalho ainda na versão 2 de 26/10: saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md.
- AD-A6-1, encaixe S3 (09 a 15/11) e UTM: saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md, seção 6.
- OA12 com "chamada para a turma e a regra completa": pos-68606.json, aprovacoes.
- Decisões 15, 16, 18, 21 e 22: docs/execucao-2026-10-26.md.

## [SUPOSIÇÃO]

- Estimativas de altura dos slides (G9, G12, G13 e seção 7), por contagem de caracteres; conferir no render.
- Ausência de travessão e meia-risca conferida por leitura, não por busca de caractere.
- Risco de reprovação de anúncio com nome em caixa alta, se o A6-01 virar anúncio.

## [CONFIRMAR]

- Endereço da política de privacidade (p04) e correção da página (OA10).
- Lançamento do pacote do podcast em kit.acrescimos do JSON (cmo).
- Nome do responsável humano por cada tipo de peça (contexto/ufape-geral.md, regras de aprovação).

## Fontes

- /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/deck.json e os 72 arquivos em /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/slides/
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-28-apresentacao-68606-estrategia.md
- /home/user/marketing-ufape/saidas/09-analytics-e-insights/relatorios-pos-2026-10-28-apresentacao-68606-materiais.md
- /home/user/marketing-ufape/contexto/ufape-geral.md; /home/user/marketing-ufape/contexto/pos-graduacao.md; /home/user/marketing-ufape/contexto/catalogo-de-cursos.md
- /home/user/marketing-ufape/contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json
- /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md
- /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md
- /home/user/marketing-ufape/docs/execucao-2026-10-26.md
- /home/user/marketing-ufape/auditorias/conformidade-educacional.md; /home/user/marketing-ufape/auditorias/02-estrategia-e-posicionamento.md

---

## 7. Reconferência (versão 14, 28/10/2026)

### 7.1 Veredito

**APROVADO**, com três ajustes de redação e um teste no render, listados em 7.3. Nenhum deles mexe em promessa, dado de curso, preço, marca [CONFIRMAR] ou [SUPOSIÇÃO], nem em conformidade. Por isso não pedem nova rodada do qa: o orquestrador aplica e confere no render.

A apresentação **segue para a aprovação humana** (pessoa do marketing e, nas peças com regulação, o responsável indicado em contexto/ufape-geral.md). Os exemplos de peça (e-mails e WhatsApp da régua, anúncios e Stories) continuam **sem envio nem publicação** até a p04 (política de privacidade) e o OA10 (correção da página). Isso agora está escrito no texto visível de c8 e c9, e c4 a c7 dependem do OA9, que cita a página. Nada é publicado, enviado ou pago a partir deste arquivo.

### 7.2 Item por item

| Item | Slides e fontes reconferidos | Resultado |
|---|---|---|
| G1 | b4 (linha e aside), b14 (aside), b9 (aside), d10 (linha retirada, título "Quatro números e frases") | Resolvido. Bate com pos-68606.json revisão 2 e com o criador-de-ganchos, seção 6. |
| G2 | kit (título e "Posts por docente: 1 de 38 (AD-A6-1 em rascunho)") | Resolvido. Coerente com c1. Encaixe estimado em cerca de 781 px. |
| G3 | d10, linha "Dias até o início" | Resolvido, com o texto pedido. |
| G4 | meta (selo e caixa), conclusao (selo e coluna "Onde") | Resolvido. Ver ajuste de encaixe do meta em 7.3. |
| G5 | b0 (tarja), indice (aside) | Resolvido, com o texto pedido. |
| G6 | b4 (tarja e linha "R$ 3.000,00") | Resolvido no texto visível. Sobra um "R$ 3.000" no aside (7.3, R1). |
| G7 | canais, pracas, episodio-funil (selos e textos), publico (título trocado, só "fixo da linha") | Resolvido. Ver nota de encaixe do pracas em 7.3. |
| G8 | meta, verba, regua, kit, decisoes, conclusao | Resolvido. Todas as linhas de decisoes levam "· linha" ou "· turma". |
| G9 | d6, rodapé com [CONFIRMAR] e [DADO NÃO FORNECIDO] | Resolvido. |
| G10 | c14 (tela 3) e autoridade-docente-pos, AD-A6-1 (linha 373) e registro datado (linha 778) | Resolvido. A tela 3 do slide é literal da fonte nova, com a frase completa da regra do 3º módulo. Novo título "Post de docente: a coordenação em 3 Stories." e grid de 3 colunas iguais cabem (cerca de 656 px). |
| G11 | c4 (aside) e copy-de-mensagens-pos-onda1, 6A.2 (primeira linha A e reserva, linhas 749 e 752) | Resolvido. A reserva não aparece no c4 e não precisa aparecer. |
| G12 | c4 e c5 (aviso do link completo), c17 (R2 com "A página diz", rodapé de encurtamento), c2 ("aguarda ok humano") | Resolvido. |
| G13 | c1 (título em uma linha), curso (etiqueta "03 · Pós-graduação em Gastroenterologia Veterinária · 68606"), d9 (linha 1 encurtada) | Resolvido. |
| G14 | conclusao, c2, c1, c4, c12, c19, b6, b7, c11, b2 | Resolvido, com uma sobra no aside do c15 (7.3, R2). A ausência em c5 confere: o aside de c5 nunca citou o C2. |
| G15 | d2 ("· uso interno") | Resolvido. |
| G16 | c1 (aside) | Resolvido. |
| G17 | c13 (aside) e criador-de-ganchos-pos, linha 686 ("28/10/2026: correção do item F15 ... A6-02 e A6-08 ...") | Resolvido. A troca do [CONFIRMAR com o orquestrador] pela citação da linha datada é aceitável, porque a linha existe na fonte. |
| G18 | c3 (aside, "Objeções [SUPOSIÇÃO]") | Resolvido. |
| G19 | c17 (R8 "· vou confirmar"), c8 ("Pré-visualização:") | Resolvido. |
| Conformidade | c8 e c9 ("Envio só depois da p04 (política de privacidade) e do OA10.") | Os dois itens externos ficam marcados nos exemplos de peça. A apresentação, como documento interno, passa; o envio das peças segue bloqueado até a p04 e o OA10. |

Regras gerais nos slides reconferidos: nenhum travessão ou meia-risca na leitura, nenhum "agência", nenhum telefone, nenhuma afirmação de certificação, nome "Pós-graduação em Gastroenterologia Veterinária" correto e marcas preservadas.

### 7.3 O que sobra (ajustes sem nova rodada do qa)

- **R1. slides/b4.html, aside.** Atual: "Verba: o deck usa R$ 3.000 por curso; vale a decisão 15 (R$ 2.000,00)". Correção: "Verba: o deck usa R$ 3.000,00 por curso; vale a decisão 15 (R$ 2.000,00)".
- **R2. slides/c15.html, aside.** Atual: "O hub de prova de bolsa de landing-page-pos-2026-10-26.md é das provas (suspensas; ver C18)." Correção: "O hub de prova de bolsa de landing-page-pos-2026-10-26.md é das provas (suspensas; ver slide Relacionado)."
- **R3. slides/meta.html, encaixe.** Com o selo novo, o "(troca por turma: preço do catálogo)" e a frase do deck, a estimativa sobe para cerca de 836 px, acima de 824 [SUPOSIÇÃO de estimativa]. Correção, só se o render confirmar que passa:
  - Na caixa, atual: "No cenário base, 200 leads consomem os R$ 2.000,00 inteiros. [...] Referência do deck da The Growth Hub para a lacuna "o que o CPA mede": CPA de R$ 210,51 na conta; se for custo por matrícula, já passa do teto. O que esse CPA mede: [CONFIRMAR com a The Growth Hub]."
  - Correção: "No cenário base, 200 leads consomem os R$ 2.000,00. Com CPL acima de R$ 18,00 por 2 semanas fechadas, a meta não fecha só com mídia em nenhum dos três cenários. Referência do deck da The Growth Hub para a lacuna "o que o CPA mede" [CONFIRMAR com a The Growth Hub]: CPA de R$ 210,51 na conta; se for custo por matrícula, já passa do teto."
  - A caixa cai de quatro para três linhas, cerca de 802 px, e a marca [CONFIRMAR] continua.
- **Teste no render, slides/pracas.html.** O rodapé com "Fixo da linha [...]" passou a duas linhas. A estimativa é de cerca de 817 px, dentro de 824 e acima da caixa de 792 px. Conferir no render. Se passar, retirar do rodapé "a squad não tinha esse dado." (a informação já está no aside de a6).

### 7.4 Fontes desta reconferência

- Slides em /home/user/marketing-ufape/ferramentas/apresentacao-68606/project/slides/: b0, b2, b4, b6, b7, b9, b14, indice, meta, verba, pracas, publico, canais, regua, episodio-funil, curso, c1, c2, c3, c4, c5, c8, c9, c11, c12, c13, c14, c15, c17, c19, kit, decisoes, d2, d6, d9, d10, conclusao.
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md (AD-A6-1 e registro datado no fim).
- /home/user/marketing-ufape/saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md (6A.2).
- /home/user/marketing-ufape/saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md (seção 6 e linha datada no fim).
- /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/cursos/pos-68606.json (revisão 2).
