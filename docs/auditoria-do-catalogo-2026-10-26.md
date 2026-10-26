# Auditoria do catálogo: planilha x site (atualização)

Data: 26/10/2026
Fontes: planilha "DATAS CURSOS E PÓS (por data de início)" (alterada em 26/10/2026) e 179 páginas de produto de faculdade.ufape.com.br, lidas automaticamente com ferramentas/leitura-catalogo.
Resultado: `contexto/catalogo-de-cursos.md` e fichas em `contexto/cursos/`. Os pontos críticos de `docs/auditoria-do-catalogo-2026-10-22.md` continuam valendo até a Ufape decidir.

## 1. Regra de fonte (decisão de 26/10/2026)

- **Datas de início:** a planilha é a fonte da verdade. O site pode estar desatualizado.
- **Preço, parcelas, matrícula, carga horária, modalidade, turma, coordenação e status de venda:** vêm do site, porque a planilha não tem esses dados.

## 2. O que mudou desde 22/10/2026

- Nenhum preço mudou nos produtos que já estavam no catálogo.
- As 23 provas de bolsa de 27/11/2026 passam a ter preço no catálogo: inscrição de R$ 100,00 (site).
- Entraram produtos novos do site: Congresso Internacional do Paciente Grave Multidisciplinar (700), Workshop de Neuromonitorização teórico transmitido e gravado (68634), Grupo de Estudo em Internação e Terapia Intensiva anual 2026 (713), Grupo de Estudos em Cardiologia e Ecocardiografia Veterinária (68665), Aprimoramento em Cardiointensivismo Veterinário prático (68622), Aprimoramento Terapia Intensiva Veterinária (68668) e aprimoramentos sem venda (68613, 715).
- Entraram 13 provas de bolsa antigas, todas sem venda (avise-me). Não divulgar.
- Ficaram fora do catálogo: "Teste2026" (produto de teste, ainda à venda por R$ 2,00 no site), a página de recrutamento "Faça parte do corpo clínico da UFAPE!" (686) e a página de regras de estágio (638, fora do ar).

## 2a. Dado pessoal publicado no site (urgente, LGPD)

13 páginas de provas de bolsa antigas (680, 681, 682, 684, 685, 687, 688, 689, 690, 691, 693, 694 e 695) e a página do Programa de Aprimoramento em Terapia Intensiva (715) publicam a lista de aprovados com nome completo de candidatos. As fichas da squad tiveram esses nomes removidos em 26/10/2026 e o gerador das fichas passou a removê-los. A Ufape precisa decidir, com o jurídico, se mantém essas listas públicas e com que base legal; a squad não usa nem repete esses nomes. Achado do agente seo-tecnico.

## 3. Links da planilha que parecem trocados

Nestes casos a diferença de data parece vir do link, não do site desatualizado. O preço tirado do site pode ser de outra turma. Status: [CONFIRMAR].

| Código | Curso | Planilha | Site |
|---|---|---|---|
| 68662 | Pós-graduação em Odontologia Veterinária | 15/08/2026, turma V | 24 e 25/04/2027, turma V. A turma de 15/08/2026 no site é a 678 (turma IV) |
| 662 | Pós-graduação em Ortopedia Veterinária | 24/04/2027, turma V | 15 e 16/08/2026, turma IV |

## 4. Datas diferentes entre planilha e site (vale a planilha) (7)

| Código | Curso | Alerta |
|---|---|---|
| 68662 | Pós-graduação em Odontologia Veterinária | data diverge: planilha 15/08/2026, site 24/04/2027 |
| 698 | Pós-graduação em Ecocardiografia | data diverge: planilha 28/11/2026, site 28/11/2027 |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | data diverge: planilha 10/04/2027, site 24/04/2027 |
| 662 | Pós-graduação em Ortopedia Veterinária | data diverge: planilha 24/04/2027, site 15/08/2026 |
| 352 | Pós-graduação em Ventilação Mecânica | data diverge: planilha 24/05/2027, site 24/04/2027 |
| 606 | Curso de Diagnóstico por Imagem na Oftalmologia - Teórico - São Paulo | data diverge: planilha 01/08/2026, site 17/09/2026 |
| 623 | III curso de imersão teórico e prático em endoscopia digestiva- SÃO PAULO | data diverge: planilha 28/11/2026, site 01/08/2026 |

## 5. Turma diferente entre planilha e site (3)

| Código | Curso | Alerta |
|---|---|---|
| 68628 | Pós-graduação em Oncologia Veterinária | turma diverge: planilha VI, site VII |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais | turma diverge: planilha VII, site V |
| 662 | Pós-graduação em Ortopedia Veterinária | turma diverge: planilha V, site IV |

## 6. Turma já iniciada e ainda à venda no site (36)

| Código | Curso | Alerta |
|---|---|---|
| 677 | Pós-graduação em Neurocirurgia e Neuro-oncologia Veterinária | turma já começou (11/07/2026) e segue à venda |
| 564 | Pós-graduação em Nutrologia Veterinária | turma já começou (18/07/2026) e segue à venda |
| 653 | Pós-graduação em Endoscopia Veterinária | turma já começou (15/08/2026) e segue à venda |
| 650 | Pós-graduação em Medicina de Felinos | turma já começou (15/08/2026) e segue à venda |
| 68662 | Pós-graduação em Odontologia Veterinária | turma já começou (15/08/2026) e segue à venda |
| 706 | Pós Graduação em Ultrassonografia de Pequenos Animais | turma já começou (15/08/2026) e segue à venda |
| 586 | Pós-graduação em Anestesiologia Veterinária (Direto ao ponto) | turma já começou (22/08/2026) e segue à venda |
| 554 | Pós-graduação em Dor e Cuidados Paliativos na Veterinária | turma já começou (22/08/2026) e segue à venda |
| 665 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | turma já começou (19/09/2026) e segue à venda |
| 666 | Pós-graduação em Terapia Intensiva e Emergência Veterinária | turma já começou (19/09/2026) e segue à venda |
| 68605 | Pós-graduação em Cardiologia Veterinária | turma já começou (17/10/2026) e segue à venda |
| 659 | Pós-graduação Cirurgia Cardiorrespiratória em Cães e Gatos | turma já começou (17/10/2026) e segue à venda |
| 68607 | Pós-graduação em Anestesiologia Veterinária | turma já começou (24/10/2026) e segue à venda |
| 68612 | Pós-graduação em Nefrologia e Urologia Veterinária | turma já começou (24/10/2026) e segue à venda |
| 575 | Urgencias y Emergencias en Perros y Gatos- LIMA | turma já começou (24/05/2025) e segue à venda |
| 605 | Curso de capacitación en Anestesiología Veterinaria- LIMA | turma já começou (01/11/2025) e segue à venda |
| 477 | Introdução a anestesia de Pets não Convencionais- SÃO PAULO | turma já começou (23/05/2026) e segue à venda |
| 500 | Curso internacional em Videocirurgia Aplicado | turma já começou (01/05/2026) e segue à venda |
| 621 | Curso de preparo de cadáveres e materiais biológicos de animais para Ensino, Pesquisa e Extensão- SÃO PAULO- SP | turma já começou (06/06/2026) e segue à venda |
| 599 | Curso de Criocirurgia em Medicina Veterinária | turma já começou (20/06/2026) e segue à venda |
| 617 | Curso de Anestesia e Tratamento da Dor em Gatos- SÃO PAULO | turma já começou (11/07/2026) e segue à venda |
| 606 | Curso de Diagnóstico por Imagem na Oftalmologia - Teórico - São Paulo | turma já começou (01/08/2026) e segue à venda |
| 718 | Curso de Aprimoramento em Cardiointensivismo Veterinário | turma já começou (29/08/2026) e segue à venda |
| 717 | Curso Premium Em Cirurgia de Tecidos Moles Em Pequenos Animais 100% Prático | turma já começou (01/08/2026) e segue à venda |
| 99 | Curso Prático de Imersão em Cirurgia Veterinária | turma já começou (26/09/2026) e segue à venda |
| 433 | Curso Prático de Imersão em Cirurgia Veterinária | turma já começou (03/10/2026) e segue à venda |
| 625 | Curso de castração de cães e gatos | turma já começou (01/10/2026) e segue à venda |
| 68668 | Aprimoramento Terapia Intensiva Veterinária | turma já começou (19/10/2026) e segue à venda |
| 488 | CURSO PREPARATÓRIO PARA PROVA DE TITULO DE ESPECIALISTA EM ANESTESIOLOGIA VETERINÁRIA | turma já começou (15/05/2024) e segue à venda |
| 535 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | turma já começou (25/07/2026) e segue à venda |
| 663 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | turma já começou (25/07/2026) e segue à venda |
| 678 | Pós-graduação em Odontologia Veterinária | turma já começou (15/08/2026) e segue à venda |
| 68663 | Grupo de Estudos em Ortopedia | turma já começou (21/10/2026) e segue à venda |
| 701 | Pós-graduação em Neurologia e Neurocirurgia Veterinária | turma já começou (11/07/2026) e segue à venda |
| 720 | Grupo de Estudos em Oftalmologia Veterinária | turma já começou (01/09/2026) e segue à venda |
| 721 | Grupo de Estudos em Gastroenterologia | turma já começou (27/05/2026) e segue à venda |

## 7. Página sem data de início ou com data em branco (11)

| Código | Curso | Alerta |
|---|---|---|
| 718 | Curso de Aprimoramento em Cardiointensivismo Veterinário | site sem data de início |
| 68668 | Aprimoramento Terapia Intensiva Veterinária | site sem data de início |
| 68618 | Curso de Ventilação Mecânica Aplicada à Anestesia Veterinária - Curso Teórico-Prático | site sem data de início |
| 593 | Curso Teórico/Prático de bloqueio locorregional em cães e gatos guiado por ultrassonografia- GOIÂNIA | site sem data de início |
| 576 | Curso Básico de Oftalmologia Em Cães e Gatos - São Paulo | site sem data de início |
| 589 | CURSO DE DIAGNÓSTICO POR IMAGEM NA OFTALMOLOGIA- TEÓRICO E PRÁTICO - SÃO PAULO | site sem data de início |
| 590 | Curso de Microcirurgia na Oftalmologia Veterinária - básico e avançado- SÃO PAULO | site sem data de início |
| 603 | Curso de Microcirurgia na Oftalmologia Veterinária - básico- SÃO PAULO | site sem data de início |
| 604 | Curso de Microcirurgia na Oftalmologia Veterinária - Avançado - São Paulo | site sem data de início |
| 404 | Curso Teórico e Prático em Colocação de Stent Traqueal em Cães | site sem data de início |
| 68611 | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária | site com data em branco (XX) |

## 8. Página sem venda ou fora do ar (25)

| Código | Curso | Alerta |
|---|---|---|
| 670 | Pós-graduação em Pneumologia Veterinária | página: link indisponivel |
| 539 | Curso de Urgência e Emergência | página: avise-me (sem venda) |
| 592 | Curso Teórico/Prático de bloqueio locorregional em cães e gatos guiado por ultrassonografia- SÃO PAULO | página: avise-me (sem venda) |
| 716 | Curso Prático de Ultrassonografia Point-of-Care (POCUS) em Emergência Veterinária | página: avise-me (sem venda) |
| 68656 | Prova de Bolsa de Estudos para Oftalmologia Veterinária | página: link indisponivel |
| 610 | Pós-graduação em Internação Veterinária | página: avise-me (sem venda) |
| 614 | Pós-graduação em Internação Veterinária | página: avise-me (sem venda) |
| 615 | Pós-graduação em Internação Veterinária | página: avise-me (sem venda) |
| 654 | Pós-graduação em Oncologia Veterinária | página: avise-me (sem venda) |
| 664 | Pós-graduação em Anestesiologia Veterinária | página: avise-me (sem venda) |
| 680 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Medicina de Felinos - Turma VI | página: avise-me (sem venda) |
| 681 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Gastroenterologia | página: avise-me (sem venda) |
| 682 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Endocrinologia de Pequenos Animais | página: avise-me (sem venda) |
| 684 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Hematologia Clínica de Pequenos Animais | página: avise-me (sem venda) |
| 685 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Oncologia Veterinária | página: avise-me (sem venda) |
| 68613 | Aprimoramento em Terapia Intensiva Veterinária | página: avise-me (sem venda) |
| 687 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Clínica Cirúrgica de Cães e Gatos | página: avise-me (sem venda) |
| 688 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Nefrologia e Urologia | página: avise-me (sem venda) |
| 689 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Clínica Médica e Emergência | página: avise-me (sem venda) |
| 690 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Terapia Intensiva e Emergência Veterinária | página: avise-me (sem venda) |
| 691 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu Semipresencial em Anestesiologia Veterinária | página: avise-me (sem venda) |
| 693 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Videocirurgia Veterinária | página: avise-me (sem venda) |
| 694 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Odontologia Veterinária | página: avise-me (sem venda) |
| 695 | Prova de Bolsa de Estudos para Pós-graduação Lato Sensu em Dermatologia Clínica Veterinária | página: avise-me (sem venda) |
| 715 | Programa de Aprimoramento em Terapia Intensiva Veterinária | página: avise-me (sem venda) |

## 9. Páginas com "CERTIFICADO PELO MEC" (46)

A squad não repete a frase até a regulação aprovar o texto oficial.

- 289 Pós-graduação em Cardiologia Veterinária
- 333 Pós Graduação em Citopatologia Veterinária
- 341 Pós Graduação em Medicina Interna Equina
- 359 Pós-graduação em Anestesiologia Locorregional Veterinária
- 366 Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária
- 382 Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos
- 535 Pós-graduação em Clínica Cirúrgica de Cães e Gatos
- 554 Pós-graduação em Dor e Cuidados Paliativos na Veterinária
- 564 Pós-graduação em Nutrologia Veterinária
- 578 Pós-graduação em Videocirurgia Veterinária
- 599 Curso de Criocirurgia em Medicina Veterinária
- 60 Pós-graduação em Medicina de Silvestres
- 650 Pós-graduação em Medicina de Felinos
- 653 Pós-graduação em Endoscopia Veterinária
- 654 Pós-graduação em Oncologia Veterinária
- 657 Pós-graduação em Anestesiologia Avançada
- 659 Pós-graduação Cirurgia Cardiorrespiratória em Cães e Gatos
- 662 Pós-graduação em Ortopedia Veterinária
- 663 Pós-graduação em Clínica Médica e Emergência de Pequenos Animais
- 664 Pós-graduação em Anestesiologia Veterinária
- 665 Pós-graduação em Clínica Cirúrgica de Cães e Gatos
- 666 Pós-graduação em Terapia Intensiva e Emergência Veterinária
- 678 Pós-graduação em Odontologia Veterinária
- 679 Pós-graduação em Infectologia Veterinária
- 68604 Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária
- 68605 Pós-graduação em Cardiologia Veterinária
- 68606 Pós-graduação em Gastroenterologia Veterinária
- 68607 Pós-graduação em Anestesiologia Veterinária
- 68608 Pós-graduação em Hematologia Veterinária
- 68609 Pós-graduação em Anestesiologia Veterinária
- 68610 Pós-graduação em Dermatologia Veterinária
- 68611 Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária
- 68612 Pós-graduação em Nefrologia e Urologia Veterinária
- 68615 Pós-graduação em Patologia Clínica
- 68616 Pós-graduação em Neurologia e Neurocirurgia Veterinária
- 68617 Pós-graduação em Endocrinologia de Pequenos Animais
- 68623 Pós-graduação em Terapia Intensiva e Emergência Veterinária
- 68628 Pós-graduação em Oncologia Veterinária
- 68629 Pós Graduação em Ultrassonografia de Pequenos Animais
- 68632 Pós-graduação em Clínica Cirúrgica de Cães e Gatos
- 68635 Pós-graduação em Clínica Médica e Emergência de Pequenos Animais
- 68636 Pós-graduação em Pneumologia Veterinária
- 68662 Pós-graduação em Odontologia Veterinária
- 698 Pós-graduação em Ecocardiografia
- 701 Pós-graduação em Neurologia e Neurocirurgia Veterinária
- 706 Pós Graduação em Ultrassonografia de Pequenos Animais
