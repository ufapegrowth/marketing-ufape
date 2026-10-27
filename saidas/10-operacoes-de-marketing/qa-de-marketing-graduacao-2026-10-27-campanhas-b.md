# QA de marketing: conferência da versão 2 das campanhas pagas da Graduação 2027/1 (Meta e Google)

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: graduacao
- Data: 27/10/2026 (terça-feira)
- Escopo: só os itens da revisão anterior (saidas/10-operacoes-de-marketing/qa-de-marketing-graduacao-2026-10-27-campanhas.md) e problemas novos criados pela v2. Os arquivos revisados não foram editados.
- Arquivos revisados:
  - A1 saidas/11-midia-paga/anuncios-meta-graduacao-2026-10-26.md, versão 2 (383 linhas)
  - A2 saidas/11-midia-paga/anuncios-google-graduacao-2026-10-26.md, versão 2 (654 linhas)
- Entradas lidas: as mesmas da revisão anterior (CLAUDE.md, docs/execucao-2026-10-26.md, contexto/graduacao.md, catálogo seção 1, editais-2027-1.md, cmo-graduacao, cmo-geral 12.7, gestor-de-midia v3, estrategia-de-midia v3, criativos-de-anuncio, qa-d, auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md).
- Script: /tmp/claude-0/-home-user/266c34a1-9b23-5a3e-bf6a-85e9f1184970/scratchpad/qa-campanhas-grad/conta.py (mesmo da rodada anterior).

---

## 1. Vereditos

| Arquivo | Veredito | Correções obrigatórias |
|---|---|---|
| A1 anuncios-meta (v2) | **APROVADO** | 0 |
| A2 anuncios-google (v2) | **APROVADO** | 0 |

Os dois seguem para a aprovação humana (AM1 a AM12 e AG1 a AG11). Nada sobe sem MP1, MP2, MP4, MP10, G13 e G14. Anúncio com preço ou desconto também precisa de G7 e G12. AM12 fica com o cmo.

---

## 2. Itens da rodada anterior

### A1 anuncios-meta

| Item | Onde na v2 | Situação |
|---|---|---|
| M-1 trava G7 | L45, L47, L173, L179, L182, L185, L193, L196, L205, L206, L214 a L224 (cenários A e B), L255, L288, AM2, AM4, AM6, AM7 | Resolvido. Preço e desconto ficam bloqueados por G7 e G12. O cenário B (v3-entrada e v2-pratica; p1 e p2) não usa preço e mantém a verba da seção 4 |
| M-2 limites de gasto | L63 a L73, L83, L89 e L90, L115, L261, L264, AM9 | Resolvido. _202611 fica com R$ 675,00 (fases 1 e 2) e _202701 com R$ 765,00 (fases 3 e 4, e é ela que leva a fase 4). Os descontos de remarketing (até R$ 45,00, R$ 105,00 e R$ 48,00) são 20% de cada fase. Soma de R$ 1.440,00. A Meta fica com R$ 3.440,00 sem o Google, e o limite da conta deixa de ser trava |
| M-3 noturno | L78, L105, L107, L137, AM6 | Resolvido. A v2 diz "metade da verba semanal da Meta do curso" e o noturno sobe na segunda-feira seguinte a MP8. O limite do integral cai na mesma medida e o total fica em R$ 1.440,00 |
| M-4 regra de 25% | L115, L360 | Resolvido, com [SUPOSIÇÃO, CONFIRMAR na Central de Ajuda da Meta] |
| M-5 datas do Enem | L269, L293, L373 | Resolvido, com [CONFIRMAR no calendário oficial do Inep] |
| R-M1 "sua nota" | L171, L181, L195, L208, AM12 | Aplicado. O título passa a ser "Enem de 2010 em diante" (22 caracteres) até a semana E, e a decisão final fica com o cmo |
| R-M2 https:// | L235 a L239 | Aplicado |
| R-M3 data de término | L63, L264, AM9 | Aplicado (21/02/2027) |
| R-M4 posicionamentos | L153, L361, AM1 | Aplicado. Audience Network e Messenger ficam fora, com [SUPOSIÇÃO] |
| R-M5 aprendizado limitado | L226 | Aplicado, com a fonte (gestor 3.5) e o [CONFIRMAR] |
| R-M6 abertura da fase 3 | L186 | Aplicado. A linha visível traz "média mínima de 300 pontos, de 2010 em diante" |
| R-M7 ato | L172, AM12 | Levado ao cmo como pergunta |

### A2 anuncios-google

| Item | Onde na v2 | Situação |
|---|---|---|
| G-1 regras de plataforma | L80, L137, L218, L225, L633 | Resolvido. A frase contraditória saiu. O orçamento é por campanha e o compartilhado fica só como reserva do AG2. Os limites de 15 e 4 e a "Força do anúncio" estão marcados e entraram na Lista 2 |
| G-2 faixa "desconhecida" | L404, L482, L530, L551 (AG5), L572, L643 | Resolvido. A decisão está no AG5, com as opções A e B e o efeito de cada uma no alcance. Vale a opção mais restrita (excluir "desconhecida") até o jurídico responder (G10) |
| R-G1 PDFs | L371, L536 | Aplicado |
| R-G2 limite de R$ 560,00 | L535, AG2 | Aplicado. A v2 avisa que a conta pode ser compartilhada [CONFIRMAR] |
| R-G3 etapa | L6 | Aplicado (etapa 5, como na Meta) |

---

## 3. Problemas novos

Não foi encontrado nenhum problema novo nos dois arquivos.

- **Recontagem do Google por script:** são 100 itens (títulos, descrições, ativos da fase 4, sitelinks e frases de destaque). Nenhuma divergência entre o declarado e o real e nenhum item acima do limite. Os textos dos anúncios e recursos não mudaram na v2. As fixações de desconto e de Enem continuam iguais.
- **Títulos novos da Meta:** "Enem de 2010 em diante" (22 caracteres), sempre com a descrição "Média mínima de 300 pontos". Assim o Enem aparece com a condição completa.
- **Verba:** as tabelas semanais e as diárias não mudaram e continuam batendo com o gestor v3. Nenhum curso passa de R$ 2.000,00 e a pausa segue em 22/02/2027.
- **UTM:** continua no padrão D11 e D12 e coerente entre Meta e Google.
- **Travessão e meia-risca:** nenhuma ocorrência de U+2014 ou U+2013 nos dois arquivos.

Auditorias (11 e conformidade-educacional): os itens que falharam na rodada anterior (verba e trava de gasto, preço sem G7 e público menor no Google) agora passam. Os demais continuam como estavam: os pendentes externos (G13, G14 e pixel ou conversões) seguem [CONFIRMAR].

---

## Lista 1. Fatos (com fonte)

- Itens da rodada anterior: qa-de-marketing-graduacao-2026-10-27-campanhas.md.
- Verba por semana e fase: gestor-de-midia v3, 3.2 e 3.3.
- Recontagem: 100 itens do Google, 0 divergências (script citado no cabeçalho).
- 0 ocorrências de U+2014 e U+2013 nos dois arquivos.

## Lista 2. Suposições

- [SUPOSIÇÃO] As regras de plataforma marcadas nos dois arquivos (gasto diário, posicionamentos, limites de ativos) valem até a conferência no gerenciador e no editor.

## Lista 3. Dados que faltam

- [CONFIRMAR] G7, G12, G13, G14, MP1, MP2, MP4, MP10 e MP15. Decisões do cmo em AM12. Jurídico no AG5 (G10). Se as contas de anúncio são compartilhadas com a Pós. Datas do Enem 2026 no calendário do Inep.

---

## Próximo passo

A1 e A2 seguem para a aprovação humana. A montagem é de 11 a 13/11/2026, em pausa. Nada é publicado, enviado ou pago sem aprovação humana.
