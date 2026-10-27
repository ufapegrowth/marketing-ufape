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
