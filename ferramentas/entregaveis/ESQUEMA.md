# Cronograma de entregáveis: esquema dos dados

Cada arquivo ferramentas/entregaveis/dados/<bloco>.json é uma lista de peças. Uma peça é uma unidade que sai para o público ou que alguém executa numa data: um post, um carrossel, um card de docente, um roteiro de vídeo, uma mensagem de WhatsApp, um e-mail, a publicação de uma página, a subida, a troca de fase ou a pausa de uma campanha paga, uma conferência ou uma aprovação humana com data.

Campos de cada peça:

| Campo | Tipo | Regra |
|---|---|---|
| id | texto | único no bloco: "<bloco>-<turma ou geral>-<tipo>-<n>" em minúsculas, sem acento |
| bloco | texto | pos-onda1, pos-marco, pos-abril, graduacao ou workshop |
| turmas | lista de texto | códigos das turmas da peça (ex. ["657"]); a Graduação usa "medicina-veterinaria" e "pedagogia"; o Workshop usa "workshop" |
| tipo | texto | post, carrossel, reels, story, card_docente, video, whatsapp, email, pagina, anuncio, campanha_subida, campanha_fase, campanha_pausa, conferencia, aprovacao, relatorio, inicio_turma, outro |
| canal | texto | instagram, facebook, tiktok, youtube, linkedin, x, whatsapp, email, site, meta_ads, google_ads, crm, interno |
| data | texto ou null | AAAA-MM-DD, só se a data estiver escrita no arquivo para esta peça. Nunca deduzida nem inventada |
| data_fim | texto ou null | para faixas (fase de campanha, janela de envio) |
| hora | texto ou null | "9h", "23h59", só se escrita |
| quando | texto ou null | quando não há data absoluta: o texto relativo do arquivo ("D+2 do cadastro", "véspera da prova") |
| titulo | texto | até 90 caracteres: o nome, o gancho ou a primeira linha da peça, copiado do arquivo (pode abreviar no fim de uma palavra, sem reticências) |
| status | texto | aguardando_aprovacao (revisada e aprovada pelo qa, espera a pessoa do marketing), em_correcao, a_fazer, suspenso, executado. Vem do diário e das revisões do qa; na dúvida, o do kit no JSON do curso |
| trava | lista de texto | códigos que seguram esta peça, como escritos no arquivo (ex. ["OU3", "P4"]); lista vazia se nenhuma |
| arquivo | texto | caminho relativo do arquivo onde está o texto da peça |
| linha | número | linha (base 1) onde começa o texto ou o bloco da peça nesse arquivo |
| fonte_da_data | texto | "arquivo:linha" de onde a data foi lida (pode ser outro arquivo, como o calendário do plano) |

Regras:
- Português do Brasil. Nunca travessão (U+2014) nem meia-risca (U+2013). Sem dado pessoal, sem nome de pessoa (docente aparece como "docente" ou pela função).
- Nenhuma data inventada. Peça sem data no arquivo entra com data null e "quando" preenchido.
- Uma peça repetida em canais diferentes no mesmo dia (o mesmo post no Instagram e no Facebook) pode ser uma peça só com o canal principal e a lista de canais em "titulo" ou repetida; prefira uma por canal quando o arquivo separar.
- Use a versão atual e aprovada de cada arquivo. Arquivos marcados no diário como substituídos ou "rascunho a revisar" não entram.

## Versão 2: texto da peça para leitura (campos novos)

Toda peça de tipo post, carrossel, reels, story, card_docente, video, whatsapp, email, pagina ou anuncio ganha dois campos. As outras (campanha_*, conferencia, aprovacao, relatorio, inicio_turma, outro) ficam com conteudo null e ganham só titulo_limpo.

| Campo | Tipo | Regra |
|---|---|---|
| titulo_limpo | texto | o título que uma pessoa da diretoria entende, sem código interno (sem "657-F1", "W1", "OB1", "AD-A1-1", "G1-AT2"): o gancho, o assunto ou a primeira linha da peça; para operação, uma frase simples ("Campanha no Meta entra na fase de conversão"). Até 100 caracteres |
| conteudo | objeto ou null | o texto que o público vê, copiado do arquivo, palavra por palavra |

Campos de conteudo:

| Campo | Tipo | O que vai |
|---|---|---|
| destaque | lista de {rotulo, texto} | o que abre a peça: "Gancho", "Primeira linha", "Assunto", "Pré-cabeçalho", "Título". Só a versão principal (A); as outras vão em variantes |
| arte | lista de texto | o texto de cada card, tela ou slide da arte, na ordem ("Card 1: ..."); no card de docente, o nome e a função ou o tema, como no arquivo |
| corpo | lista de texto | os parágrafos que o público lê: legenda, mensagem de WhatsApp, corpo do e-mail, texto do anúncio, blocos principais da página. Um parágrafo por item. Mantenha [nome], [LINK] e marcas como [T] e [CONFIRMAR] |
| roteiro | lista de texto | as cenas ou falas do vídeo, na ordem |
| chamada | texto ou null | o texto do botão ou da chamada para ação |
| variantes | lista de {rotulo, texto} | versões de teste e reservas ("Primeira linha B (teste)", "Assunto B") |
| observacao | texto ou null | uma frase simples sobre como sai, se o arquivo disser (ex. "O Facebook reaproveita no mesmo dia") |

Regras: copiar, nunca reescrever nem resumir o texto público. Nada de nota de produção (UTM, contagem de caracteres, conferências, template) dentro de destaque, arte, corpo ou roteiro. Se o arquivo não tiver texto público para a peça (por exemplo, toque ainda sem texto), conteudo fica null e titulo_limpo diz isso ("Mensagem ainda sem texto").
