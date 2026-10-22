# Auditoria do catálogo: planilha x site

Data: 22/10/2026
Fontes: planilha "DATAS CURSOS E PÓS (por data de início)" (8 abas) e 161 páginas de produto de faculdade.ufape.com.br, lidas automaticamente.
Resultado consolidado: `contexto/catalogo-de-cursos.md` e fichas em `contexto/cursos/`.

Nada foi corrigido por suposição. Cada item abaixo precisa de uma decisão da Ufape; depois disso, o catálogo e a planilha são atualizados.

## 1. Visão geral

- A planilha cobre 42 turmas de pós, 28 cursos livres, 4 simpósios e 23 provas de bolsa.
- O site tem pelo menos **66 produtos à venda ou publicados que não estão na planilha**: cursos online gravados, minicursos, grupos de estudos, aprimoramento da Ufape Clínica, turmas de pós em outras datas e um produto de teste. Todos entraram no catálogo com a fonte "só no site".
- A Graduação (Medicina Veterinária em SP e Pedagogia em Goiânia) não está na planilha; os dados vieram do site.
- Simpósios e congressos da planilha não têm link; só o Simpósio Internacional de Coagulação foi achado no site (produto 202, online).

## 2. Pontos críticos (resolver primeiro)

1. **"CERTIFICADO PELO MEC" nas páginas de pós.** A pós lato sensu não tem certificado emitido nem reconhecido pelo MEC; o certificado é emitido pela instituição credenciada. A frase pode ser lida como propaganda enganosa (CDC e Conar) e aparece também em pelo menos um curso livre (Criocirurgia). Recomendação: a regulação da Ufape define o texto oficial (por exemplo, "certificado de especialização emitido pela Faculdade UFAPE, instituição credenciada pelo MEC", se for o caso) e o site é ajustado. Até lá, a squad não usa a frase.
2. **Produto de teste publicado:** [Teste2026](https://faculdade.ufape.com.br/produto/183/teste2026), dentro da categoria de Pós em Cardiologia, com preço de 12x de R$ 0,17. Retirar do ar.
3. **Página de Pedagogia com texto de modelo e conteúdo de outro curso:** aparecem os blocos "Adicione aqui a tabela/arquivo com a matriz curricular", "Adicione aqui os documentos para download", "Você pode repetir o bloco de coordenação aqui" e, no perfil do egresso, "Atue como defensor dos direitos dos animais", copiado da Medicina Veterinária.
4. **Medicina Veterinária, turno noturno:** o bloco do noturno (5 anos) mostra "INTEGRAL" no campo turno.
5. **Público da Pós em Nutrologia:** a página diz "graduandos e médicos veterinários". Pós lato sensu exige diploma de graduação; confirmar com a regulação.
6. **Pós em Pneumologia (turma VII, 10/04/2027):** o link da planilha está fora do ar. Existe outra página da mesma pós no site (produto 68636, início 17 e 18/04/2027); provavelmente a planilha aponta para a página antiga.
7. **Planilha com link trocado:** a linha "Pós Graduação em Citopatologia Veterinária" de 03/04/2027, turma IV, aponta para a página da Pós em **Infectologia** Veterinária.
8. **Provas de bolsa de Cardiologia:** as linhas de GO e SP estão com os links invertidos (a linha GO aponta para a página de São Paulo e vice-versa). A prova de bolsa de Oftalmologia está com o link fora do ar.
9. **Pós em Diagnóstico por Imagem (produto 68611):** página publicada com início "XX DE XX DE 202X".

## 3. Divergências e pendências por curso

### Data de início diferente entre planilha e site (7)

Decidir qual está certa e corrigir a outra fonte.

- [Pós-graduação em Odontologia Veterinária](https://faculdade.ufape.com.br/produto/68662/pos-graduacao-odontologia-veterinaria/sao-paulo): data diverge: planilha 15/08/2026, site 24/04/2027
- [Pós-graduação em Ecocardiografia](https://faculdade.ufape.com.br/produto/698/pos-graduacao-em-ecocardiografia): data diverge: planilha 28/11/2026, site 28/11/2027
- [Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária](https://faculdade.ufape.com.br/produto/366/pos-graduacao-fisioterapia-fisiatria-e-reabilitacao-veterinaria/sao-paulo): data diverge: planilha 10/04/2027, site 24/04/2027
- [Pós-graduação em Ortopedia Veterinária](https://faculdade.ufape.com.br/produto/662/pos-graduacao-em-ortopedia-veterinaria): data diverge: planilha 24/04/2027, site 15/08/2026; turma diverge: planilha V, site IV
- [Pós-graduação em Ventilação Mecânica](https://faculdade.ufape.com.br/produto/352/pos-graduacao-em-ventilacao-mecanica): data diverge: planilha 24/05/2027, site 24/04/2027
- [Curso de Diagnóstico por Imagem na Oftalmologia - Teórico - São Paulo](https://faculdade.ufape.com.br/produto/606/curso-diagnostico-por-imagem-na-oftalmologia-teorico/sao-paulo): data diverge: planilha 01/08/2026, site 17/09/2026
- [III curso de imersão teórico e prático em endoscopia digestiva- SÃO PAULO](https://faculdade.ufape.com.br/produto/623/iii-curso-de-imersao-teorico-e-pratico-em-endoscopia-digestiva-sao-paulo): data diverge: planilha 28/11/2026, site 01/08/2026

### Número da turma diferente entre planilha e site (2)

- [Pós-graduação em Oncologia Veterinária](https://faculdade.ufape.com.br/produto/68628/pos-graduacao-oncologia-veterinaria/sao-paulo): turma diverge: planilha VI, site VII
- [Pós-graduação em Endocrinologia de Pequenos Animais](https://faculdade.ufape.com.br/produto/68617/pos-graduacao-endocrinologia-de-pequenos-animais/v/sao-paulo): turma diverge: planilha VII, site V

### Turma já iniciada e ainda com botão de compra (30)

Nas pós semipresenciais pode ser intencional (entrada com a turma em andamento). Nos cursos de 1 ou 2 dias, a página deveria sair de venda ou ganhar nova data.

- [Pós-graduação em Neurocirurgia e Neuro-oncologia Veterinária](https://faculdade.ufape.com.br/produto/677/pos-graduacao-em-neurocirurgia-e-neuro-oncologia-veterinaria): início 11 e 12 de JULHO DE 2026
- [Pós-graduação em Nutrologia Veterinária](https://faculdade.ufape.com.br/produto/564/pos-graduacao-em-nutrologia-veterinaria): início 18 DE JULHO DE 2026
- [Pós-graduação em Endoscopia Veterinária](https://faculdade.ufape.com.br/produto/653/pos-graduacao-em-endoscopia-veterinaria): início 15 e 16 de agosto DE 2026
- [Pós-graduação em Medicina de Felinos](https://faculdade.ufape.com.br/produto/650/pos-graduacao-lato-em-medicina-de-felinos): início 15 e 16 de Agosto de 2026
- [Pós Graduação em Ultrassonografia de Pequenos Animais](https://faculdade.ufape.com.br/produto/706/pos-graduacao-em-ultrassonografia-de-pequenos-animais): início 15 DE AGOSTO DE 2026
- [Pós-graduação em Anestesiologia Veterinária (Direto ao ponto)](https://faculdade.ufape.com.br/produto/586/pos-graduacao-em-anestesiologia-veterinaria-direto-ao-ponto): início 22 E 23 DE AGOSTO DE 2026
- [Pós-graduação em Dor e Cuidados Paliativos na Veterinária](https://faculdade.ufape.com.br/produto/554/pos-graduacao-em-dor-e-cuidados-paliativos-na-veterinaria): início 22 e 23 de Agosto de 2026
- [Pós-graduação em Clínica Cirúrgica de Cães e Gatos](https://faculdade.ufape.com.br/produto/665/pos-graduacao-em-clinica-cirurgica-de-caes-e-gatos): início 19 e 20 de Setembro de 2026
- [Pós-graduação em Terapia Intensiva e Emergência Veterinária](https://faculdade.ufape.com.br/produto/666/pos-graduacao-em-terapia-intensiva-e-emergencia-veterinaria): início 19 e 20 setembro de 2026
- [Pós-graduação em Cardiologia Veterinária](https://faculdade.ufape.com.br/produto/68605/pos-graduacao-em-cardiologia-veterinaria): início 17 e 18 de outubro de 2026
- [Pós-graduação Cirurgia Cardiorrespiratória em Cães e Gatos](https://faculdade.ufape.com.br/produto/659/pos-graduacao-cirurgia-cardiorrespiratoria-em-caes-e-gatos): início 17 e 18 de Outubro de 2026
- [Pós-graduação em Ortopedia Veterinária](https://faculdade.ufape.com.br/produto/662/pos-graduacao-em-ortopedia-veterinaria): início 15 e 16 de Agosto de 2026
- [Urgencias y Emergencias en Perros y Gatos- LIMA](https://faculdade.ufape.com.br/produto/575/urgencias-y-emergencias-en-perros-y-gatos-lima): início 24 DE MAYO DEL 2025
- [Curso de capacitación en Anestesiología Veterinaria- LIMA](https://faculdade.ufape.com.br/produto/605/curso-de-capacitacion-en-anestesiologia-veterinaria-lima): início NOVEMBRO DE 2025
- [Introdução a anestesia de Pets não Convencionais- SÃO PAULO](https://faculdade.ufape.com.br/produto/477/introducao-a-anestesia-de-pets-nao-convencionais-sao-paulo): início 23 E 24 DE MAIO DE 2026
- [Curso internacional em Videocirurgia Aplicado](https://faculdade.ufape.com.br/produto/500/curso-internacional-em-videocirurgia-aplicado): início MAIO DE 2026
- [Curso de preparo de cadáveres e materiais biológicos de animais para Ensino, Pesquisa e Extensão- SÃO PAULO- SP](https://faculdade.ufape.com.br/produto/621/curso-de-preparo-de-cadaveres-e-materiais-biologicos-de-animais-para-ensino-pesquisa-e-extensao-sao-paulo-sp): início 06 E 07 DE JUNHO DE 2026
- [Curso de Criocirurgia em Medicina Veterinária](https://faculdade.ufape.com.br/produto/599/curso-de-criocirurgia-em-medicina-veterinaria): início 20 e 21 de Junho de 2026
- [Curso de Anestesia e Tratamento da Dor em Gatos- SÃO PAULO](https://faculdade.ufape.com.br/produto/617/curso-de-anestesia-e-tratamento-da-dor-em-gatos-sao-paulo): início 11 DE JULHO DE 2026
- [Curso de Diagnóstico por Imagem na Oftalmologia - Teórico - São Paulo](https://faculdade.ufape.com.br/produto/606/curso-diagnostico-por-imagem-na-oftalmologia-teorico/sao-paulo): início 17 DE SETEMBRO DE 2026
- [Curso de Aprimoramento em Cardiointensivismo Veterinário](https://faculdade.ufape.com.br/produto/718/curso-de-aprimoramento-em-cardiointensivismo-veterinario/ii/sao-paulo): início 29 E 30 AGOSTO de 2026
- [Curso Premium Em Cirurgia de Tecidos Moles Em Pequenos Animais 100% Prático](https://faculdade.ufape.com.br/produto/717/curso-premium-em-cirurgia-de-tecidos-moles-em-pequenos-animais-100-pratico/sao-paulo): início Agosto de 2026
- [Curso Prático de Imersão em Cirurgia Veterinária](https://faculdade.ufape.com.br/produto/99/curso-pratico-de-imersao-em-cirurgia-veterinaria/ii/goiania): início 26 e 27 de Setembro de 2026
- [Curso Prático de Imersão em Cirurgia Veterinária](https://faculdade.ufape.com.br/produto/433/curso-pratico-de-imersao-em-cirurgia-veterinaria): início 03 e 04 de Outubro de 2026
- [Curso de castração de cães e gatos](https://faculdade.ufape.com.br/produto/625/curso-de-castracao-de-caes-e-gatos): início OUTUBRO DE 2026
- [III curso de imersão teórico e prático em endoscopia digestiva- SÃO PAULO](https://faculdade.ufape.com.br/produto/623/iii-curso-de-imersao-teorico-e-pratico-em-endoscopia-digestiva-sao-paulo): início 01 E 02 DE AGOSTO DE 2026
- [Pós-graduação em Clínica Cirúrgica de Cães e Gatos](https://faculdade.ufape.com.br/produto/535/pos-graduacao-em-clinica-cirurgica-de-caes-e-gatos): início 25 e 26 de Julho de 2026
- [Pós-graduação em Neurologia e Neurocirurgia Veterinária](https://faculdade.ufape.com.br/produto/701/pos-graduacao-em-neurologia-e-neurocirurgia-veterinaria): início 11 e 12 de JULHO DE 2026
- [Pós-graduação em Odontologia Veterinária](https://faculdade.ufape.com.br/produto/678/pos-graduacao-em-odontologia-veterinaria): início 15 e 16 de agosto de 2026
- [Pós-graduação em Clínica Médica e Emergência de Pequenos Animais](https://faculdade.ufape.com.br/produto/663/pos-graduacao-em-clinica-medica-e-emergencia-de-pequenos-animais): início 25 DE JULHO DE 2026

### Página sem data de início (11)

- [Curso Teórico/Prático de bloqueio locorregional em cães e gatos guiado por ultrassonografia- GOIÂNIA](https://faculdade.ufape.com.br/produto/593/curso-teorico-pratico-de-bloqueio-locorregional-em-caes-e-gatos-guiado-por-ultrassonografia-goiania): sem data no site
- [Curso Básico de Oftalmologia Em Cães e Gatos - São Paulo](https://faculdade.ufape.com.br/produto/576/curso-basico-de-oftalmologia-em-caes-e-gatos/sao-paulo): sem data no site
- [CURSO DE DIAGNÓSTICO POR IMAGEM NA OFTALMOLOGIA- TEÓRICO E PRÁTICO - SÃO PAULO](https://faculdade.ufape.com.br/produto/589/curso-diagnostico-por-imagem-na-oftalmologia-teorico-pratico/sao-paulo): sem data no site
- [Curso de Microcirurgia na Oftalmologia Veterinária - básico e avançado- SÃO PAULO](https://faculdade.ufape.com.br/produto/590/curso-microcirurgia-na-oftalmologia-veterinaria-basico-e-avancado/sao-paulo): sem data no site
- [Curso de Microcirurgia na Oftalmologia Veterinária - básico- SÃO PAULO](https://faculdade.ufape.com.br/produto/603/curso-microcirurgia-na-oftalmologia-veterinaria-basico/sao-paulo): sem data no site
- [Curso de Microcirurgia na Oftalmologia Veterinária - Avançado - São Paulo](https://faculdade.ufape.com.br/produto/604/curso-microcirurgia-na-oftalmologia-veterinaria-avancado/sao-paulo): sem data no site
- [Curso Teórico e Prático em Colocação de Stent Traqueal em Cães](https://faculdade.ufape.com.br/produto/404/curso-teorico-e-pratico-em-colocacao-de-stent-traqueal-em-caes): sem data no site
- [Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária](https://faculdade.ufape.com.br/produto/68611/pos-graduacao-em-diagnostico-por-imagem-aplicado-a-clinica-medica-e-cirurgica-veterinaria): sem data no site
- [Curso Aprimoramento Extracurricular e Curricular](https://faculdade.ufape.com.br/produto/639/curso-aprimoramento-extracurricular-e-curricular): sem data no site
- [Curso Aprimoramento Profissionalizante](https://faculdade.ufape.com.br/produto/640/curso-aprimoramento-profissionalizante): sem data no site
- [Curso Aprimoramento Profissionalizante Aluno (Aluno de Pós UFAPE)](https://faculdade.ufape.com.br/produto/641/curso-aprimoramento-profissionalizante-aluno-aluno-de-pos-ufape): sem data no site

### Página só com "Avise-me" (sem venda) (8)

- [Curso de Urgência e Emergência](https://faculdade.ufape.com.br/produto/539/curso-urgencia-e-emergencia/vi/sao-paulo): fora de venda; não divulgar com chamada de compra
- [Curso Teórico/Prático de bloqueio locorregional em cães e gatos guiado por ultrassonografia- SÃO PAULO](https://faculdade.ufape.com.br/produto/592/curso-teorico-pratico-de-bloqueio-locorregional-em-caes-e-gatos-guiado-por-ultrassonografia-sao-paulo): fora de venda; não divulgar com chamada de compra
- [Curso Prático de Ultrassonografia Point-of-Care (POCUS) em Emergência Veterinária](https://faculdade.ufape.com.br/produto/716/curso-pratico-de-ultrassonografia-point-of-care-pocus-em-emergencia-veterinaria/iv/sao-paulo): fora de venda; não divulgar com chamada de compra
- [Pós-graduação em Internação Veterinária](https://faculdade.ufape.com.br/produto/614/pos-graduacao-em-internacao-veterinaria): fora de venda; não divulgar com chamada de compra
- [Pós-graduação em Internação Veterinária](https://faculdade.ufape.com.br/produto/610/pos-graduacao-em-internacao-veterinaria): fora de venda; não divulgar com chamada de compra
- [Pós-graduação em Internação Veterinária](https://faculdade.ufape.com.br/produto/615/pos-graduacao-em-internacao-veterinaria): fora de venda; não divulgar com chamada de compra
- [Pós-graduação em Oncologia Veterinária](https://faculdade.ufape.com.br/produto/654/pos-graduacao-em-oncologia-veterinaria): fora de venda; não divulgar com chamada de compra
- [Pós-graduação em Anestesiologia Veterinária](https://faculdade.ufape.com.br/produto/664/pos-graduacao-em-anestesiologia-veterinaria): fora de venda; não divulgar com chamada de compra

### Link fora do ar (2)

- [Pós-graduação em Pneumologia Veterinária](https://faculdade.ufape.com.br/produto/670/pos-graduacao-em-pneumologia-veterinaria): "O produto requisitado não está mais disponível"
- [Prova de Bolsa de Estudos para Oftalmologia Veterinária](https://faculdade.ufape.com.br/produto/68656/prova-de-bolsa-de-estudos-para-oftalmologia-veterinaria/sao-paulo): "O produto requisitado não está mais disponível"

## 4. Recomendações para a planilha

1. Incluir uma aba ou um filtro para Graduação, cursos online, minicursos, grupos de estudos e aprimoramento, ou assumir oficialmente que o catálogo da squad (`contexto/catalogo-de-cursos.md`) é a fonte completa.
2. Adicionar colunas que hoje só existem no site e que a squad usa: preço, condições, carga horária, modalidade, coordenação e status de venda.
3. Padronizar datas no formato DD/MM/AAAA (hoje há "SEM DATA", "COLOCAR DATA?", "MAIO DE 2026" e datas sem ano).
4. Quando uma turma nova abrir, trocar o link para a página nova e retirar a antiga de venda.
5. Na plataforma da squad, esta conferência pode rodar toda semana de forma automática, avisando quando planilha e site divergirem.
