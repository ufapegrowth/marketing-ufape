---
name: diagnostico-de-midia
description: Lê as métricas de Meta Ads e Google Ads de cima para baixo no funil, acha onde a captação quebrou e decide escalar, manter, ajustar ou pausar cada item.
---
# Diagnosticar a mídia paga

Propósito: Achar onde o funil de captação está quebrando, explicar por quê em linguagem simples e dar uma decisão clara para cada campanha, conjunto ou anúncio.

Passos:
1. Confirme o contexto mínimo: objetivo e evento de otimização (cadastro, mensagem, inscrição), metas de CPL e de custo por matrícula (se não houver, rode antes a skill metas-de-custo), período analisado e o que mudou nele (verba, criativo, página, oferta, calendário do vestibular), gasto e conversões do período. Use só exportações agregadas; remova qualquer dado pessoal antes de ler.
2. Aplique a regra dos dados suficientes (regra prática, não meta):
   - Só chame de perdedor o anúncio ou conjunto que já gastou entre 1,5 e 2 vezes o CPL máximo sem gerar lead.
   - Diferença entre anúncios com menos de 10 a 20 conversões de cada lado é ruído; diga isso.
   - Mudança grande (verba, público, criativo, lance) pode reiniciar o aprendizado; pese isso antes de mexer.
   - Olhe pelo menos de 3 a 7 dias. Um dia ruim não é tendência.
3. Leia o funil de cima para baixo. O primeiro elo fraco costuma ser a causa; o resto é consequência.

   | Etapa | Métricas | O que indica quando está ruim |
   |---|---|---|
   | Entrega | CPM | Público pequeno ou saturado, concorrência de vestibular, criativo fraco |
   | Atenção | Retenção nos 3 primeiros segundos, ThruPlay | A abertura do vídeo não para a rolagem |
   | Interesse | CTR do link, CPC do link | Mensagem ou oferta não gera clique, criativo desalinhado da persona |
   | Chegada | Visualizações da página divididas por cliques | Página lenta, pixel ou redirecionamento quebrado |
   | Conversão | Taxa de conversão da página, CPL | Página do curso, oferta, prova ou formulário fracos |
   | Matrícula | Custo por matrícula, taxa lead para matrícula (CRM) | Problema depois do lead: atendimento, tempo de resposta, preço |
   | Saturação | Frequência, CTR ao longo dos dias | Fadiga de criativo |

   Calcule as métricas derivadas que faltarem e mostre a conta. Compare a conta com ela mesma (semanas anteriores, melhores anúncios); referência externa só como faixa aproximada e marcada como estimativa.
4. Use a tabela de sintomas:
   - CPM subiu, CTR estável, CPL subiu: leilão mais caro (época de vestibular, público saturado). Renovar criativos, ampliar público.
   - CTR caindo dia após dia e frequência subindo: fadiga. Entrar com conceitos novos, não só títulos novos.
   - CTR bom e conversão ruim: o problema está depois do clique. Auditar página, formulário e pixel antes de mexer no anúncio.
   - Muitos cliques e poucas visualizações de página: carregamento ou rastreamento.
   - Retenção baixa, mas quem assiste vira lead: o corpo funciona, a abertura não. Testar ganchos novos.
   - Lead barato e matrícula cara: olhar o CRM, o tempo de primeira resposta no WhatsApp e a qualidade do lead.
   - Tudo estável e cai de repente: pagamento recusado, anúncio reprovado, página fora do ar, evento de pixel parado.
   - Um anúncio concentra quase todo o gasto: normal na entrega atual. Não pause os outros só por gastarem pouco; prepare substitutos.
5. Dê uma decisão por item:
   - ESCALAR: abaixo da meta com volume confiável por vários dias. Aumento gradual de verba, com o risco explicado.
   - MANTER: dentro da meta ou ainda aprendendo. Não mexer.
   - AJUSTAR: um elo específico está fraco. Dizer exatamente o que mudar, uma coisa por vez.
   - PAUSAR: já gastou o suficiente para julgar e está claramente fora da meta, sem sinal de recuperação.

Saída: resumo em duas frases (o que acontece e o gargalo principal), tabela item, métrica-chave, diagnóstico e decisão, até 5 ações em ordem de impacto com o porquê, as 2 ou 3 métricas a observar nos próximos dias com o valor que confirma ou derruba o diagnóstico, e as suposições feitas.

Verificações antes de terminar:
- Nenhum número foi inventado; dado ausente aparece como [DADO NÃO FORNECIDO].
- Nenhuma decisão foi tomada com volume insuficiente sem dizer que é ruído.
- Nenhuma recomendação muda várias coisas ao mesmo tempo no mesmo conjunto.
- Nenhum dado pessoal de aluno ou candidato foi lido ou citado.
