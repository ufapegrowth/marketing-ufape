# SEO on-page das 8 turmas de abril de 2027 da Pós-graduação (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609), encomenda O4, lote A, da onda 3

- **Agente:** seo-on-page (departamento 03, SEO e Busca por IA)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1 (lote A). O lote B (maio) entra em nova versão deste arquivo, sem mudar o nome. A turma 662 fica fora, em espera total (OU18); o registro está na seção 11.
- **Encomenda:** O4 do plano do CMO em versão 2 (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md, seção 10, linha O4; regras E1 a E22).
- **Status:** rascunho para o qa-de-marketing (auditorias/03-busca.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago. Aplicar a marcação no site é ação do time do site (projeto ufape-site), depois da aprovação.
- **Consumidores:** otimizador-de-cta (O5), qa-de-marketing (O18a) e a plataforma, que valida o formato de templates/pagina-da-turma.md. Próximo agente sugerido: **editor-de-conteudo**, que recebe este arquivo junto da O3 para revisar a voz antes da aprovação humana.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 12, 14, 16 e 18)
  - contexto/catalogo-de-cursos.md (seção 2, linhas das 8 turmas; fonte única dos dados de curso)
  - Fichas das 8 turmas em contexto/cursos/pos/: os fatos de curso vieram da O1 e da O3, que as leram inteiras e conferiram módulo a módulo; não reabri as fichas
  - templates/pagina-da-turma.md (limites: titulo_seo até 60 caracteres, descricao_seo até 155, resposta_citavel de 40 a 60 palavras, descricao_schema até 300, tudo sem número)
  - auditorias/conformidade-educacional.md e auditorias/03-busca.md
  - .claude/skills/visibilidade-em-ia/SKILL.md e .claude/skills/schema-de-curso/SKILL.md
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (versão 2, linhas 1 a 210: cabeçalho, seções 0 a 2 e abertura da seção 4; regras E1 a E22 e travas por turma)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda3.md (O1, inteiro)
  - saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md (O3, inteiro; o FAQPage repete o FAQ dela palavra por palavra)
  - saidas/03-seo-e-busca/seo-on-page-pos-2026-10-27-onda2.md (formato, já corrigido)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md (Q39 a Q55 e seções 5 a 8)
- **Não aberto:** faculdade.ufape.com.br; as fichas das turmas antigas (535, 665, 663, 68607, 664, 586, 654 e 670; só o que a O1 e o catálogo dizem delas); o lote B; nenhuma busca na web nova (os resultados de busca vêm da O1).
- **Dados pessoais:** nenhum. Nenhum docente é nomeado.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape ou o time do site tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo e a ficha não trazem. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com o critério.

---

## 0. Como ler este arquivo e regras aplicadas às 8 turmas

1. **Limites usados** (templates/pagina-da-turma.md): `titulo_seo` até 60 caracteres, `descricao_seo` até 155, `resposta_citavel` de 40 a 60 palavras, `descricao_schema` até 300. Contei à mão, espaços e pontuação inclusos, pelo método de soma por palavra e depois pela soma incremental; o orquestrador reconta por script e o validador da plataforma tem a palavra final. Palavra com hífen conta como uma palavra (se o validador separar, cada resposta sobe no máximo 3 palavras e continua dentro do intervalo).
2. **Sem número em nenhum campo de texto** (nem algarismo, ordinal, numeral romano ou número por extenso), sem preço, data, local, carga horária, duração, vaga ou nome de docente. "Um" e "uma" só como artigo. O único nome de local é o da instituição, "Faculdade Ufape".
3. **CP1 como trava:** nenhuma das 8 turmas leva cidade em `titulo_seo`, `descricao_seo`, `resposta_citavel`, `descricao_schema` ou resposta de FAQ. A cauda de cidade de 68632 e 68609 (O1: 68632-K1 e K2, 68609-K1 e K2, as melhores apostas das duas) fica só no dado (`local_e_datas`) e no JSON-LD (`location`, pela chave). Nenhuma variante com cidade está escrita aqui; se a pessoa do marketing aprovar a CP1, o cmo pede versão nova.
4. **Palavras e estruturas proibidas:** nenhum "MEC", "certificado", "reconhecida", "bolsa", urgência ou contador; nenhum `educationalCredentialAwarded`; nenhum "especialista" como título; nenhum superlativo da ficha (E14); nenhuma promessa de emprego, renda, aprovação ou resultado clínico.
5. **Nada de "É pensado para quem" que descreva público (revisão Q42 da onda 2).** Nenhuma `resposta_citavel` diz quem pode entrar: ela diz o que é o curso, em que é centrado e como funciona. O público da ficha (médicas e médicos veterinários) aparece só no FAQ, palavra por palavra como na O3.
6. **Nome do catálogo nunca muda (E2).** Todo campo que cita o curso usa "Pós-graduação em <nome do catálogo>" ou, no título, o nome sem o prefixo quando o nome com o prefixo passa de 60 caracteres (68635 e 366, decisão D1 abaixo). "Veterinária" entra fora do nome, como palavra de corpo, em 68632, 68635 e 68617, cujos nomes do catálogo não a trazem. 68609 sempre no singular.
7. **Vocabulário separado entre turmas da mesma área (O1, seção 4).** Cada turma só usa o termo que é dela; os termos das turmas irmãs aparecem apenas dentro das frases-ponte do FAQ, que repetem a O3. A tabela da seção 7.3 mostra, por turma, o que foi conferido como ausente nos cinco campos de SEO.
8. **Regra 8 em 68632 (OU3 aberta):** nenhum campo e nenhuma resposta de FAQ de 68632 fala de entrada depois do início, de matrícula até o 3º módulo ou do 3º módulo. O JSON-LD de 68632 não traz pergunta sobre o assunto.
9. **E4 e E5:** lista de módulos presenciais incompleta leva "entre eles", "entre outros" ou "entre outras". Nenhum campo diz que todos os presenciais são práticos. Conferência feita contra a O3 (listas de presenciais por turma) e a O1.
10. **P5 (68628 e 68617):** a chave `catalogo.turma` não entra na marcação dessas duas turmas (o número diverge entre planilha e site). `CourseInstance.name` usa só `catalogo.nome`.
11. **Datas em divergência (679, 366 e 68636):** `startDate` só é emitido pela plataforma quando `local_e_datas` ficar visível com a data confirmada (OU19, OU20 e OU21). Até lá a marcação sai sem `startDate`.
12. **Marca no título:** todos os títulos que cabem em 60 caracteres fecham com " | Ufape", para o padrão ser único [SUPOSIÇÃO].
13. **JSON-LD:** os valores de dado (nome, turma, início, carga horária, modalidade, cidade, preço) entram como chave `{{...}}` e não foram digitados. A seção 8 mostra, só para conferência do qa, o valor que cada chave deve devolver segundo o catálogo. O FAQPage repete palavra por palavra o FAQ da O3 (skill schema-de-curso: o FAQ marcado é o visível).

### Decisões deste agente que o qa deve conferir

- **D1. Título sem o prefixo "Pós-graduação em" em 68635 e 366.** O nome do catálogo de 68635 tem 64 caracteres com o prefixo e o de 366 tem 67; nenhum cabe em `titulo_seo` (60). Alterar o nome (cortar palavra, abreviar "Pós em") violaria E2 e a regra 2.4 da O1. Escolhi o nome sem o prefixo mais " | Ufape". O prefixo, a palavra "pós-graduação" e "semipresencial" vão na `descricao_seo` e na `resposta_citavel`. Alternativa, se o qa preferir: título com a forma digitada ("Pós-graduação em Fisioterapia Veterinária | Ufape", 49 caracteres), que a O1 marca como termo de busca e nunca como nome da página [SUPOSIÇÃO: o risco é E2].
- **D2. Título de 68632 sem "presencial".** Com o nome completo e a palavra "presencial" o título passa de 60. A distinção da turma V de 68632 (presencial) contra a 665 (semipresencial) fica na `descricao_seo`, na `resposta_citavel` e na `descricao_schema`.
- **D3. `resposta_citavel` sem frase de público nas 8 turmas.** O template diz "o que é e para quem é"; a revisão Q42 da onda 2 manda o "para quem" sair enquanto a ficha não traz pré-requisito.

---

## 1. Seção 679: Pós-graduação em Infectologia Veterinária

Palavra principal (O1, 679-K0): pós-graduação em infectologia veterinária. Página: a da turma 679.

### 1.1 Campos de SEO

**titulo_seo** (49 caracteres, limite 60):

> Pós-graduação em Infectologia Veterinária | Ufape

**descricao_seo** (151 caracteres, limite 155):

> Pós-graduação em Infectologia Veterinária, semipresencial: do diagnóstico às zoonoses e ao controle de infecção hospitalar, com prática de laboratório.

**resposta_citavel** (49 palavras, faixa de 40 a 60):

> A Pós-graduação em Infectologia Veterinária da Faculdade Ufape é um curso semipresencial de infectologia veterinária, do diagnóstico ao controle de infecção hospitalar. O programa trata de virologia, micologia, bacteriologia, antibioticoterapia e doenças infecciosas por sistema, com prática presencial nos módulos de laboratório, de zoonoses e de controle de infecção.

A lista dos módulos presenciais está completa (três presenciais na ficha: laboratório, zoonoses e controle de infecção, conferidos pela O3). Sem "pequenos animais" nem "cães e gatos" (a ficha não restringe a espécie, O1 679-K3). Sem data nem mês (P3, OU19).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Infectologia Veterinária; pós-graduação em infectologia veterinária.
- Área: infectologia veterinária; doenças infecciosas e parasitárias; zoonoses; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com módulos online e prática presencial de laboratório, de zoonoses e de controle de infecção.
- Conceitos do curso: diagnóstico de doenças infecciosas; imunologia; helmintos e protozoários; virologia; micologia; bacteriologia; antibioticoterapia; infecções intra-abdominais; doenças infecciosas por sistema; controle de infecção hospitalar; vacinação; coleta, armazenamento e envio de amostras; prevenção e controle de zoonoses.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (O1, seção 6.1): citopatologia e citologia (333); hematologia e hemograma (68608); sepse, terapia intensiva e UTI como termo (68623; são conteúdo de módulo); clínica médica de pequenos animais como termo (68635; só na frase-ponte do FAQ); medicina de felinos e parasitologia como curso; saúde pública, vigilância e concurso; curso de antibioticoterapia (Cursos Livres 541); "pequenos animais" e "cães e gatos"; EAD; título de especialista; frases de certificação.

**descricao_schema** (285 caracteres, limite 300):

> Pós-graduação em Infectologia Veterinária da Faculdade Ufape, semipresencial. Infectologia do diagnóstico ao controle de infecção hospitalar: virologia, micologia, bacteriologia, antibioticoterapia e prática presencial nos módulos de laboratório, de zoonoses e de controle de infecção.

### 1.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Infectologia Veterinária da Faculdade Ufape, semipresencial. Infectologia do diagnóstico ao controle de infecção hospitalar: virologia, micologia, bacteriologia, antibioticoterapia e prática presencial nos módulos de laboratório, de zoonoses e de controle de infecção.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "infectologia veterinária" },
        { "@type": "Thing", "name": "doenças infecciosas e parasitárias" },
        { "@type": "Thing", "name": "zoonoses" },
        { "@type": "Thing", "name": "controle de infecção hospitalar" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Infectologia já aparece na clínica geral. Preciso de pós-graduação nisso?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aqui a infectologia é a área do curso: vírus, fungos, bactérias, helmintos e protozoários, antibioticoterapia, sepse, infectologia na UTI e as doenças infecciosas sistema por sistema, com prática presencial de laboratório."
          }
        },
        {
          "@type": "Question",
          "name": "Vou ter prática ou é tudo online?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A maior parte dos módulos é online. Os módulos presenciais trazem prática de laboratório: coleta, armazenamento e envio de amostras, coleta de material para exame de raiva no módulo de zoonoses e controle de infecção hospitalar. O cronograma mostra o mês de cada módulo presencial, então dá para planejar a agenda com antecedência."
          }
        },
        {
          "@type": "Question",
          "name": "Atendo na clínica. Serve para mim?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O curso parte do que a rotina clínica pede: prevenção e controle de zoonoses, diagnóstico e tratamento de doenças infecciosas e parasitárias."
          }
        },
        {
          "@type": "Question",
          "name": "Infectologia ou clínica médica ampla: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Infectologia Veterinária é centrada nas doenças infecciosas e parasitárias, do diagnóstico laboratorial ao controle de infecção hospitalar. A Pós-graduação em Clínica Médica e Emergência de Pequenos Animais é centrada na clínica médica, sistema por sistema, com a emergência do paciente grave no mesmo percurso. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 679:

- A pergunta da ponte (quarta) é item opcional na O3 [SUPOSIÇÃO: o qa decide se entra na página]. Se sair da página, sai da marcação no mesmo dia. O link para a página de 68635 só existe no HTML, depois da conferência dela (E19); na marcação o texto fica sem link.
- Sem frase de reembolso (a ficha de 679 não traz a linha; O3, seção 1.4) [CONFIRMAR com a secretaria].
- Sem item "Posso entrar depois que a turma começar?": é dado da turma (OU14), com o dia do 3º módulo [CONFIRMAR NO CATÁLOGO, OU25]. Se a plataforma o exibir, inclui no `mainEntity` o texto exato que o editor digitou, sem o mês antes do dia (E18).
- `startDate` só com a data confirmada (P3, OU19, pedido S7 da O1). Sem `audience`, sem `coursePrerequisites`, sem `educationalCredentialAwarded`.

---

## 2. Seção 68632: Pós-graduação em Clínica Cirúrgica de Cães e Gatos (presencial)

Palavra principal (O1, 68632-K0): pós-graduação em clínica cirúrgica de cães e gatos. Cauda local (68632-K1 e K2): só no dado e no JSON-LD, por CP1. Página: a da turma 68632. A turma é presencial: nenhum campo diz "semipresencial", "online" ou "a distância".

### 2.1 Campos de SEO

**titulo_seo** (58 caracteres, limite 60; sem "presencial", ver D2):

> Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Ufape

**descricao_seo** (138 caracteres, limite 155):

> Pós-graduação em Clínica Cirúrgica de Cães e Gatos presencial: dos princípios da cirurgia à alta complexidade, com aulas teórico-práticas.

**resposta_citavel** (48 palavras, faixa de 40 a 60):

> A Pós-graduação em Clínica Cirúrgica de Cães e Gatos da Faculdade Ufape é um curso presencial de clínica cirúrgica, dos princípios da cirurgia e dos acessos cirúrgicos aos procedimentos de alta complexidade. O cronograma percorre a cirurgia sistema por sistema e trata também do perioperatório, com aulas teórico-práticas.

Sem cidade (CP1). Sem "ortopedia", "osteossíntese" (termos reservados a 662), "videocirurgia" (578), "neurocirurgia" (68616) nem "fisioterapia" (366). Sem "coordenação" (OU34), "formar especialistas", "referência nacional" nem "garante" (E13 e E14). Regra 8: nenhuma palavra sobre entrar depois do início.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Clínica Cirúrgica de Cães e Gatos; pós-graduação em clínica cirúrgica de cães e gatos; clínica cirúrgica (veterinária).
- Área: clínica cirúrgica; cirurgia veterinária; cirurgia de cães e gatos; medicina veterinária.
- Modalidade: pós-graduação presencial, com aulas teórico-práticas.
- Conceitos do curso: princípios fundamentais da cirurgia; anatomia topográfica e acessos cirúrgicos; infecções, feridas e complicações cirúrgicas; sondas e drenos; trato urinário; trato gastrointestinal; herniorrafias; cirurgia oncológica e reconstrutiva; cirurgias torácicas; cirurgias cardiovasculares; odontologia e cavidade oral; cuidados perioperatórios avançados; cirurgia em felinos; paciente traumatizado; comunicação de más notícias e luto na medicina veterinária.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (O1, seção 7.1): semipresencial, online e a distância (a turma é presencial); ortopedia veterinária e osteossíntese (662, em espera); videocirurgia (578); neurocirurgia (68616; é conteúdo de módulo); fisioterapia e reabilitação como curso (366); anestesia como curso (68609, 657 e 359); pós em clínica cirúrgica semipresencial e em São Paulo (é da 665); Goiânia (CP1); coordenação (OU34); título de especialista, "formar especialistas", "referência nacional", "garante"; imersão em cirurgia e castração (Cursos Livres); EAD; residência.

**descricao_schema** (259 caracteres, limite 300):

> Pós-graduação em Clínica Cirúrgica de Cães e Gatos da Faculdade Ufape, presencial. Cirurgia sistema por sistema, dos princípios da cirurgia e dos acessos cirúrgicos aos procedimentos de alta complexidade, com aulas teórico-práticas e cuidados perioperatórios.

### 2.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Clínica Cirúrgica de Cães e Gatos da Faculdade Ufape, presencial. Cirurgia sistema por sistema, dos princípios da cirurgia e dos acessos cirúrgicos aos procedimentos de alta complexidade, com aulas teórico-práticas e cuidados perioperatórios.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "clínica cirúrgica" },
        { "@type": "Thing", "name": "cirurgia veterinária" },
        { "@type": "Thing", "name": "acessos cirúrgicos" },
        { "@type": "Thing", "name": "cuidados perioperatórios" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Opero na rotina, mas ainda travo nas cirurgias maiores. O que o cronograma traz?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O cronograma vai dos princípios da cirurgia e dos acessos cirúrgicos às cirurgias torácicas, às cardiovasculares, à neurocirurgia e aos procedimentos de alta complexidade, com aulas teórico-práticas."
          }
        },
        {
          "@type": "Question",
          "name": "É presencial. Como concilio com a clínica?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O curso é presencial e o cronograma já mostra quando acontece cada módulo, então dá para organizar a escala antes de começar. Compre passagem e hotel só depois de a turma ser confirmada."
          }
        },
        {
          "@type": "Question",
          "name": "Cirurgia, reabilitação ou videocirurgia: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Clínica Cirúrgica de Cães e Gatos é centrada na clínica cirúrgica, dos princípios da cirurgia aos procedimentos de alta complexidade. A Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária é centrada na reabilitação: avaliação, fisioterapia e recursos terapêuticos para pacientes com alterações neurológicas e ortopédicas. A Pós-graduação em Videocirurgia Veterinária é centrada na videocirurgia. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68632:

- **Regra 8 (OU3) e E22:** nenhuma pergunta, resposta, `description` ou campo de SEO trata de entrada depois do início ou do 3º módulo. Se a plataforma exibir o item de dado "Posso entrar depois que a turma começar?", este arquivo pede versão nova: o item não existe para 68632 enquanto OU3 estiver aberta.
- O FAQ nomeia "neurocirurgia", "reabilitação", "ortopédicas" e "videocirurgia" porque repete a O3 palavra por palavra (conteúdo de módulo e frase-ponte da área A4). Nenhum campo de SEO usa esses termos.
- A frase de reembolso e o alcance de "valores de inscrição" seguem a página [CONFIRMAR com a secretaria].
- Sem `instructor` e sem "coordenação" (OU34). `courseMode` deve devolver o termo de presencial; o valor esperado está na seção 8.

---

## 3. Seção 68635: Pós-graduação em Clínica Médica e Emergência de Pequenos Animais

Palavra principal (O1, 68635-K0): pós-graduação em clínica médica e emergência de pequenos animais. Página: a da turma 68635.

### 3.1 Campos de SEO

**titulo_seo** (55 caracteres, limite 60; sem o prefixo, ver D1):

> Clínica Médica e Emergência de Pequenos Animais | Ufape

**descricao_seo** (141 caracteres, limite 155):

> Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, semipresencial: clínica sistema por sistema e emergência do paciente grave.

**resposta_citavel** (47 palavras, faixa de 40 a 60):

> A Pós-graduação em Clínica Médica e Emergência de Pequenos Animais da Faculdade Ufape é um curso semipresencial que percorre a clínica médica sistema por sistema e inclui a emergência do paciente grave no mesmo percurso, da triagem à reanimação. Há prática presencial de semiologia, exames e atendimento.

Sem "terapia intensiva" nem "UTI" (termos de 68623; O1, seção 4). Sem "certificado", "certificação" nem "duas certificações" (OU35). Sem "cães e gatos" nem "especialização em clínica médica de cães e gatos" (O1, 68635-K5: a ficha não restringe a espécie). Sem número de horas (E1).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Clínica Médica e Emergência de Pequenos Animais; pós-graduação em clínica médica e emergência de pequenos animais.
- Área: clínica médica de pequenos animais; emergência veterinária; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com módulos online e prática presencial.
- Conceitos do curso: medicina interna e semiologia; patologia clínica; fluidoterapia e equilíbrio ácido-básico; clínica por sistema (cardiovascular, nefrologia, neurologia, pneumologia, gastroenterologia, infectologia, dermatologia, endocrinologia, oftalmologia, hematologia, oncologia, odontologia, medicina felina e diagnóstico por imagem; só como conteúdo da `matriz`, nunca como termo de SEO); triagem e monitoração do paciente grave; A-FAST e T-FAST; urgência e emergência; reanimação cardiopulmonar e trauma; interpretação do eletrocardiograma; hemogasometria.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (O1, seção 8.1): terapia intensiva, UTI veterinária e "terapia intensiva e emergência veterinária" (68623); internação veterinária (610, 614 e 615, sem venda); pós em cardiologia, neurologia, nefrologia, dermatologia, oncologia, endocrinologia, hematologia, infectologia, odontologia e oftalmologia como curso (páginas de cada área); medicina de felinos como pós; "duas certificações", "dupla certificação" e certificados por parte da carga (OU35); título de especialista; EAD; curso livre de urgência e emergência (539) e grupo de estudos (68666).

**descricao_schema** (247 caracteres, limite 300):

> Pós-graduação em Clínica Médica e Emergência de Pequenos Animais da Faculdade Ufape, semipresencial. Clínica médica sistema por sistema, com a emergência do paciente grave no mesmo percurso e prática presencial de semiologia, exames e atendimento.

### 3.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Clínica Médica e Emergência de Pequenos Animais da Faculdade Ufape, semipresencial. Clínica médica sistema por sistema, com a emergência do paciente grave no mesmo percurso e prática presencial de semiologia, exames e atendimento.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "clínica médica de pequenos animais" },
        { "@type": "Thing", "name": "emergência veterinária" },
        { "@type": "Thing", "name": "semiologia" },
        { "@type": "Thing", "name": "atendimento do paciente grave" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Faço plantão. Como encaixo os módulos presenciais?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A maior parte dos módulos é online. O cronograma mostra o mês de cada módulo presencial, então dá para planejar a escala com antecedência."
          }
        },
        {
          "@type": "Question",
          "name": "Clínica médica e emergência ou terapia intensiva: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Clínica Médica e Emergência de Pequenos Animais é centrada na clínica médica, sistema por sistema, com a emergência do paciente grave no mesmo percurso. A Pós-graduação em Terapia Intensiva e Emergência Veterinária é centrada no cuidado do paciente crítico. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "O curso é longo. Vale o tempo?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O cronograma completo está nesta página, com o tema de cada módulo: da medicina interna e da semiologia à urgência, à UTI e à internação. Você vê o percurso e a prática presencial antes de decidir."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68635:

- A pergunta "O curso é longo. Vale o tempo?" é da O3 e fica; a resposta não cita número de horas nem de módulos.
- Sem nenhuma frase de certificação, nem as "duas certificações" e os certificados por parte da carga da ficha (OU35). Sem local da prática de 68623 (OU26, E17).
- O item "Posso entrar depois que a turma começar?" é dado da turma (OU14), sem o mês do 3º módulo (E18; OU25). Reposição de módulo perdido [CONFIRMAR OU3].
- A frase de reembolso e o alcance de "valores de inscrição" seguem a página [CONFIRMAR com a secretaria]. Vagas: nenhum número (OU4).

---

## 4. Seção 366: Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária

Palavra principal (O1, 366-K0): pós-graduação em fisioterapia veterinária (forma digitada pelo candidato; o nome da página continua o do catálogo, E2). Página: a da turma 366.

### 4.1 Campos de SEO

**titulo_seo** (58 caracteres, limite 60; sem o prefixo, ver D1):

> Fisioterapia, Fisiatria e Reabilitação Veterinária | Ufape

**descricao_seo** (135 caracteres, limite 155):

> Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, semipresencial: da avaliação ao protocolo, com prática presencial.

**resposta_citavel** (42 palavras, faixa de 40 a 60):

> A Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária da Faculdade Ufape é um curso semipresencial de fisioterapia veterinária que parte da avaliação do aparelho locomotor para montar o protocolo. Trata de dor, cinesioterapia, recursos eletrofísicos, hidroterapia e terapias manuais, com prática presencial.

Sem data nem mês (P4, OU20). Sem "ortopedia" (termo reservado a 662), "fisioterapeuta" (a paga nega; o público da ficha é de médicos veterinários), "resolução", "conselho" nem "coordenação" (OU34). Sem "cães e gatos": a ficha traz animais de grande e pequeno porte, cavalo atleta e silvestres. Sem "primeira turma" (E1).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária; pós-graduação em fisioterapia veterinária (forma digitada, só no corpo).
- Área: fisioterapia veterinária; fisiatria veterinária; reabilitação veterinária; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com módulos online e prática presencial.
- Conceitos do curso: anatomia do sistema locomotor; fisiopatologia da dor; avaliação do aparelho locomotor e do paciente neurológico; protocolo de fisioterapia; hidroterapia; cinesioterapia; recursos eletrofísicos; terapias manuais; bandagem taping; biomecânica, órteses e próteses; reabilitação neurológica; reabilitação no cão idoso e no obeso; reabilitação em felinos e silvestres; manejo de feridas; medicina integrativa; cuidados paliativos.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (O1, seção 9.1): ortopedia veterinária e osteossíntese (662, em espera); clínica cirúrgica (68632) e videocirurgia (578); neurologia veterinária como pós (68616); fisioterapeuta, fisioterapia humana e pós para fisioterapeutas; resolução de conselho, registro profissional e "a área pertence à Medicina Veterinária" (frase normativa da ficha, à regulação); "fisioterapia animal" como termo de página (só lista e anúncio); medicina integrativa, acupuntura e cuidados paliativos como curso; fisioterapia equina e cavalo atleta; "cães e gatos"; coordenação; título de especialista; EAD.

**descricao_schema** (240 caracteres, limite 300):

> Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária da Faculdade Ufape, semipresencial. Da avaliação ao protocolo: dor, hidroterapia, recursos eletrofísicos, terapias manuais e prática presencial em fisioterapia veterinária.

### 4.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária da Faculdade Ufape, semipresencial. Da avaliação ao protocolo: dor, hidroterapia, recursos eletrofísicos, terapias manuais e prática presencial em fisioterapia veterinária.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "fisioterapia veterinária" },
        { "@type": "Thing", "name": "reabilitação veterinária" },
        { "@type": "Thing", "name": "hidroterapia" },
        { "@type": "Thing", "name": "recursos eletrofísicos" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Quero oferecer reabilitação, mas não sei por onde começar.",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O curso começa pela anatomia do sistema locomotor e pela fisiopatologia da dor e passa pela avaliação neurológica e ortopédica, que vem antes da montagem do protocolo de fisioterapia."
          }
        },
        {
          "@type": "Question",
          "name": "Tem prática de verdade ou é só teoria?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A maior parte dos módulos é online, e há módulos presenciais de prática, entre eles hidroterapia e cinesioterapia, recursos eletrofísicos, reabilitação neurológica e ortopédica, bandagem taping e terapias manuais. O cronograma mostra o mês de cada módulo presencial."
          }
        },
        {
          "@type": "Question",
          "name": "Fisioterapeuta pode fazer?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários."
          }
        },
        {
          "@type": "Question",
          "name": "Reabilitação ou cirurgia: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Clínica Cirúrgica de Cães e Gatos é centrada na clínica cirúrgica, dos princípios da cirurgia aos procedimentos de alta complexidade. A Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária é centrada na reabilitação: avaliação, fisioterapia e recursos terapêuticos para pacientes com alterações neurológicas e ortopédicas. A Pós-graduação em Videocirurgia Veterinária é centrada na videocirurgia. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 366:

- `startDate` só com a data confirmada (P4, OU20: planilha em abril e site e cronograma em outra data de abril). Se a data mudar, só o dado muda; a marcação não.
- Na marcação, `location` fica só com cidade e região; sem `streetAddress` nem `postalCode` até a Ufape confirmar o CEP (OU20).
- A resposta de "Fisioterapeuta pode fazer?" é a da O3 (366-Q2). Qualquer pergunta sobre atuação profissional depois do curso vai ao time e à regulação, sem texto pronto [REVISÃO REGULAÇÃO].
- Sem `instructor`, sem `Person` e sem "coordenação" (OU34). Sem item de entrada depois do início: bloqueado até OU20 e OU25 (E18).
- O FAQ nomeia "ortopédicas" porque repete a O3 palavra por palavra (conteúdo de módulo); nenhum campo de SEO usa o termo.

---

## 5. Seção 68628: Pós-graduação em Oncologia Veterinária (sem número de turma, P5)

Palavra principal (O1, 68628-K0): pós-graduação em oncologia veterinária. Página: a da turma 68628. "Presencial" (68628-K1) é termo de lista e de anúncio: nenhum campo descreve a turma como presencial.

### 5.1 Campos de SEO

**titulo_seo** (46 caracteres, limite 60):

> Pós-graduação em Oncologia Veterinária | Ufape

**descricao_seo** (139 caracteres, limite 155):

> Pós-graduação em Oncologia Veterinária, semipresencial: do diagnóstico ao tratamento, com quimioterapia, imunoterapia e discussão de casos.

**resposta_citavel** (50 palavras, faixa de 40 a 60):

> A Pós-graduação em Oncologia Veterinária da Faculdade Ufape é um curso semipresencial que vai do diagnóstico à escolha do tratamento. O programa trata de biologia do câncer, quimioterapia, imunoterapia, terapia alvo e neoplasia por neoplasia, com módulos presenciais, entre eles os de tratamento e os de discussão de casos clínicos.

Sem número de turma (P5). Sem "de pequenos animais" nem "cães e gatos" (a ficha traz neoplasias em animais exóticos). Sem "curso de eletroquimioterapia" (Cursos Livres 560; a eletroquimioterapia fica só como conteúdo de módulo, fora dos campos de SEO).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Oncologia Veterinária; pós-graduação em oncologia veterinária.
- Área: oncologia veterinária; oncologia clínica; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com a maior parte dos módulos online e módulos presenciais de tratamento e de discussão de casos.
- Conceitos do curso: introdução à oncologia; biologia do câncer; diagnóstico por imagem; síndrome paraneoplásica; quimioterapia antineoplásica e biossegurança; imunoterapia e terapia alvo; neoplasias por sistema; cuidado paliativo e tratamento de dor; psico-oncologia; nutrição do paciente oncológico; medicina integrativa; discussão de casos clínicos.
- Onde nomear: hero, sobre, para_quem, faq e matriz (dado, só depois da correção, O3 seção 5.3).
- Não nomear como entidade (O1, seção 10.1): número da turma; curso de eletroquimioterapia (560) e mini curso em oncologia (465); citologia e citopatologia (333); hematologia, linfomas e leucemias como curso (68608); cirurgia oncológica como pós (68632); radioterapia como curso ou centro; cuidados paliativos e dor como pós (554); "de pequenos animais" e "cães e gatos"; "presencial" como modalidade da turma; EAD; residência, mestrado e doutorado; título de especialista; São Paulo (CP1).

**descricao_schema** (255 caracteres, limite 300):

> Pós-graduação em Oncologia Veterinária da Faculdade Ufape, semipresencial. Do diagnóstico à escolha do tratamento: biologia do câncer, quimioterapia, imunoterapia, terapia alvo, neoplasias por sistema e discussão de casos clínicos nos módulos presenciais.

### 5.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Oncologia Veterinária da Faculdade Ufape, semipresencial. Do diagnóstico à escolha do tratamento: biologia do câncer, quimioterapia, imunoterapia, terapia alvo, neoplasias por sistema e discussão de casos clínicos nos módulos presenciais.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "oncologia veterinária" },
        { "@type": "Thing", "name": "quimioterapia antineoplásica" },
        { "@type": "Thing", "name": "imunoterapia" },
        { "@type": "Thing", "name": "neoplasias" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Não tenho estrutura para quimioterapia na clínica. O que o curso traz sobre o tratamento?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A quimioterapia antineoplásica é trabalhada no presencial junto com a biossegurança, e o curso trata também imunoterapia, terapia alvo, eletroquimioterapia e crioterapia."
          }
        },
        {
          "@type": "Question",
          "name": "Como funciona o semipresencial? Tenho de ir sempre?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A maior parte dos módulos é online. O presencial inclui, entre outros, os módulos de tratamento, módulos de neoplasias com discussão de casos e a visita de radioterapia, com o mês marcado no cronograma."
          }
        },
        {
          "@type": "Question",
          "name": "Atendo clínica geral. Oncologia é para mim?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O curso começa pela introdução à oncologia e pela biologia do câncer antes de chegar ao diagnóstico e ao tratamento."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68628:

- **P5:** `CourseInstance.name` sem a turma. A chave `catalogo.turma` não entra na marcação até a Ufape resolver o número (VII no site e VI na planilha; OU30).
- A `matriz` fica oculta até o cronograma ser corrigido (módulo com "Para definir" e módulos repetidos, O3 seção 5.3); por isso nenhum campo de SEO cita a lista de módulos como completa.
- Sem `instructor` (duplicata de docente, E15, OU30). O item "Posso entrar depois que a turma começar?" é dado da turma (OU14), com a data do 3º módulo pela ficha.
- Nível de entrada da pergunta de clínico geral [CONFIRMAR NO CATÁLOGO]. Alcance de "valores de inscrição" [CONFIRMAR com a secretaria].

---

## 6. Seções 68617, 68636 e 68609

As três últimas turmas do lote seguem a ordem da O3 (68617, 68636 e 68609) e têm as subseções 6.1, 6.2 e 6.3. As checagens do lote estão na seção 7.

### 6.1 Seção 68617: Pós-graduação em Endocrinologia de Pequenos Animais (sem número de turma, P5)

Palavra principal (O1, 68617-K0): pós-graduação em endocrinologia de pequenos animais. Página: a da turma 68617.

#### Campos de SEO

**titulo_seo** (59 caracteres, limite 60; margem de um caractere, recontar por script):

> Pós-graduação em Endocrinologia de Pequenos Animais | Ufape

**descricao_seo** (145 caracteres, limite 155):

> Pós-graduação em Endocrinologia de Pequenos Animais, semipresencial: da fisiologia hormonal à discussão de casos de Cushing, diabetes e tireoide.

**resposta_citavel** (47 palavras, faixa de 40 a 60):

> A Pós-graduação em Endocrinologia de Pequenos Animais da Faculdade Ufape é um curso semipresencial que vai da fisiologia hormonal à discussão de casos clínicos. O programa trata de síndrome de Cushing, diabetes, doenças da tireoide, distúrbios da calcemia e emergências endócrinas, com módulos presenciais de aula prática.

Os módulos presenciais da ficha são dois e ambos são de aula prática (conferido pela O3), então a frase não generaliza a prática (E5). Sem número de turma (P5). Sem "TCC" nem "trabalho de conclusão" (a ficha tem "Como montar seu TCC" no módulo 5 e a avaliação não cita TCC; [CONFIRMAR NO CATÁLOGO]). Sem "alopecia" com a letra X (E1). Sem "metabologia" (nome de agregador, O1 68617-K4: só lista e anúncio) e sem "cães e gatos" como recorte.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Endocrinologia de Pequenos Animais; pós-graduação em endocrinologia de pequenos animais.
- Área: endocrinologia de pequenos animais; endocrinologia veterinária; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com a maior parte dos módulos online e módulos presenciais de aula prática.
- Conceitos do curso: anatomia, histologia e fisiologia do sistema endócrino; mecanismos de ação hormonal; síndrome de Cushing; hipoadrenocorticismo; diabetes mellitus e cetoacidose diabética; hipotireoidismo e hipertireoidismo; distúrbios da calcemia; insulinoma e hipoglicemias; neoplasias adrenais e tireoidianas; dislipidemias; síndromes poliglandulares; emergências endócrinas; dosagens hormonais; diagnóstico diferencial de poliúria e polidipsia; imagem aplicada; discussão de casos clínicos.
- Onde nomear: hero, sobre, para_quem, faq e matriz (dado, só depois da correção, O3 seção 6.3).
- Não nomear como entidade (O1, seção 11.1): número da turma; "endocrinologia e metabologia" (só lista e anúncio); nefrologia e doença renal crônica como curso (68612 e prova 68653; são conteúdo de módulo); geriatria (699); dermatologia (68610); nutrologia (564); ultrassonografia, tomografia e ressonância como pós (68629 e 68604); curso de diabetes e mini curso de endocrinologia (Cursos Livres 542, 458, 103 e 104); TCC; marca de medicamento no cronograma; "cães e gatos" como recorte; EAD; título de especialista; "muita prática" e "presencial" como modalidade.

**descricao_schema** (235 caracteres, limite 300):

> Pós-graduação em Endocrinologia de Pequenos Animais da Faculdade Ufape, semipresencial. Da fisiologia hormonal à discussão de casos: Cushing, diabetes, tireoide, calcemia, emergências endócrinas e aula prática presencial no cronograma.

#### JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Endocrinologia de Pequenos Animais da Faculdade Ufape, semipresencial. Da fisiologia hormonal à discussão de casos: Cushing, diabetes, tireoide, calcemia, emergências endócrinas e aula prática presencial no cronograma.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "endocrinologia de pequenos animais" },
        { "@type": "Thing", "name": "síndrome de Cushing" },
        { "@type": "Thing", "name": "diabetes mellitus" },
        { "@type": "Thing", "name": "doenças da tireoide" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Sou clínico geral. Endocrinologia é para mim?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O curso começa pela fisiologia e pela anatomia do sistema endócrino e passa por síndrome de Cushing, diabetes mellitus e doenças tireoidianas, com discussão de casos ao longo do cronograma."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto do curso é presencial?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A maior parte do curso é online. Os módulos presenciais são de aula prática de atendimento, de anatomia, de ultrassonografia abdominal e de cirurgia do sistema endócrino, e o cronograma está nesta página."
          }
        },
        {
          "@type": "Question",
          "name": "Pós-graduação ou curso online mais curto?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A pós-graduação percorre a endocrinologia da fisiologia às emergências endócrinas, com discussão de casos e aula prática presencial."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68617:

- **P5:** `CourseInstance.name` sem a turma (V no site e VII na planilha; OU29).
- Na terceira resposta, a O3 acrescenta uma frase sobre o guia de decisão A7 ("Se você quer aprofundar só o diabetes ou só a tireoide, o guia de decisão da área mostra os caminhos lado a lado."), que só vai ao ar com o guia publicado e linkado. A marcação acima está sem essa frase. Quando o guia sair, a mesma frase entra aqui, igual à da página, no mesmo dia.
- URL "/v/" da página atual: conferida pelo time do site antes da subida e antes de qualquer envio (OU29, pedido S6 da O1). `pagina.url_canonica` deve devolver a URL final.
- Sem `instructor` (duplicata "Dr. Eric Vieira", E15). Item "Posso entrar depois que a turma começar?" é dado da turma (OU14), com a data do 3º módulo pela ficha. Sem pergunta sobre TCC. Nível de entrada [CONFIRMAR NO CATÁLOGO].

### 6.2 Seção 68636: Pós-graduação em Pneumologia Veterinária (data só no site)

Palavra principal (O1, 68636-K0): pós-graduação em pneumologia veterinária. Página: a da turma 68636.

#### Campos de SEO

**titulo_seo** (48 caracteres, limite 60):

> Pós-graduação em Pneumologia Veterinária | Ufape

**descricao_seo** (141 caracteres, limite 155):

> Pós-graduação em Pneumologia Veterinária, semipresencial: da fisiologia respiratória à endoscopia e à imagem, com aulas práticas presenciais.

**resposta_citavel** (43 palavras, faixa de 40 a 60):

> A Pós-graduação em Pneumologia Veterinária da Faculdade Ufape é um curso semipresencial centrado no sistema respiratório, da fisiologia às intervenções emergenciais no paciente respiratório. As aulas teóricas são a distância, e as aulas práticas presenciais incluem, entre outras, ultrassonografia pulmonar, laringotraqueobroncoscopia e rinoscopia.

Sem data (P3, OU21). Sem "cardiologia" (289), "ventilação mecânica" (352), "terapia intensiva" e "emergência" como pós (68623 e 68635), "pneumologista", "medicina humana", "especialidade", "escassez" nem "vácuo" (E14). Sem a frase de aulas "não transmitidas": a ficha de 68636 não a traz [CONFIRMAR].

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Pneumologia Veterinária; pós-graduação em pneumologia veterinária.
- Área: pneumologia veterinária; sistema respiratório; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com aulas teóricas a distância e aulas práticas presenciais.
- Conceitos do curso: anatomia das vias aéreas e fisiologia respiratória; semiologia e farmacologia respiratória; radiologia; hemogasometria; tomografia do trato respiratório; ultrassonografia pulmonar; laringotraqueobroncoscopia; rinoscopia; toracoscopia; síndrome do braquicefálico; dirofilariose e circulação pulmonar; doenças pleurais; tromboembolismo pulmonar; oncologia do trato respiratório; sedação no pneumopata; discussão de casos clínicos.
- Onde nomear: hero, sobre, para_quem, faq e matriz (dado, só depois da correção, O3 seção 7.3).
- Não nomear como entidade (O1, seção 12.1): cardiologia veterinária e ecocardiografia (289 e 698); ventilação mecânica como pós (352; o curso livre é de Cursos Livres); terapia intensiva e emergência como pós (68623 e 68635); diagnóstico por imagem, ultrassonografia e tomografia como pós (68604 e 68629); hemogasometria como curso (655 e 107); pneumologia humana, pneumologista e residência; "escassez de especialistas", "é uma especialidade" e "vácuo" (E14); "cães e gatos"; data; EAD; título de especialista.

**descricao_schema** (230 caracteres, limite 300):

> Pós-graduação em Pneumologia Veterinária da Faculdade Ufape, semipresencial. Da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais de imagem e endoscopia respiratória.

#### JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Pneumologia Veterinária da Faculdade Ufape, semipresencial. Da fisiologia respiratória às intervenções emergenciais, com aulas teóricas a distância e aulas práticas presenciais de imagem e endoscopia respiratória.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "pneumologia veterinária" },
        { "@type": "Thing", "name": "fisiologia respiratória" },
        { "@type": "Thing", "name": "endoscopia respiratória" },
        { "@type": "Thing", "name": "ultrassonografia pulmonar" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Serve para clínico ou só para quem trabalha com UTI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O curso começa pela anatomia das vias aéreas e pela fisiologia respiratória e chega às intervenções emergenciais no paciente respiratório."
          }
        },
        {
          "@type": "Question",
          "name": "Vou ver endoscopia e imagem na prática?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Laringotraqueobroncoscopia, rinoscopia e ultrassonografia pulmonar estão entre os módulos presenciais de aula prática. A maior parte dos módulos é online, e o cronograma mostra o mês de cada módulo presencial."
          }
        },
        {
          "@type": "Question",
          "name": "Pneumologia, cardiologia ou ventilação mecânica: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Pneumologia Veterinária é centrada no sistema respiratório, da fisiologia às intervenções emergenciais no paciente respiratório. A Pós-graduação em Cardiologia Veterinária é centrada na cardiologia, da fisiologia ao laudo. A Pós-graduação em Ventilação Mecânica é centrada na ventilação mecânica. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68636:

- `startDate` só com a data confirmada: a data existe só no site, sem linha na planilha (P3, OU21; a linha de 670 na planilha traz outra data). Até lá a marcação sai sem `startDate`.
- A pergunta da ponte nomeia "cardiologia" e "ventilação mecânica" só dentro dos nomes das outras pós-graduações, como na O3 (E11). Os links para 289 e 352 só existem no HTML, depois da conferência das páginas (E19); na marcação o texto fica sem link.
- Sem `instructor`. Item "Posso entrar depois que a turma começar?" é dado da turma (OU14), só depois de OU21. Nível de entrada [CONFIRMAR NO CATÁLOGO].

### 6.3 Seção 68609: Pós-graduação em Anestesiologia Veterinária

Palavra principal (O1, 68609-K0): pós-graduação em anestesiologia veterinária. Cauda local (68609-K1 e K2): só no dado e no JSON-LD, por CP1. Página: a da turma 68609 (pilar de Anestesiologia).

#### Campos de SEO

**titulo_seo** (51 caracteres, limite 60):

> Pós-graduação em Anestesiologia Veterinária | Ufape

**descricao_seo** (148 caracteres, limite 155):

> Pós-graduação em Anestesiologia Veterinária, semipresencial: da avaliação pré-anestésica à anestesia de pacientes especiais, com prática presencial.

**resposta_citavel** (43 palavras, faixa de 40 a 60):

> A Pós-graduação em Anestesiologia Veterinária da Faculdade Ufape é um curso semipresencial de anestesiologia clínica, da avaliação pré-anestésica à anestesia de pacientes especiais. Os módulos presenciais trazem, entre outros temas, sedação e monitoração, TIVA, intubação e reanimação cardiorrespiratória, com acompanhamento individualizado da evolução.

Nome sempre no singular (nunca "Anestesiologias Veterinárias", E2). Sem "avançada" (657) nem "locorregional" (359). Sem "prova", "título" nem "Especialista" (E13). Sem "hands-on" onde a ficha não o marca (só nos módulos de sedação, TIVA e anestesia em felinos e exóticos; E5). Sem "gravada" (vale só para os itens marcados na ficha, E3). Sem marcas de terceiros (RECOVER, ROTEM, Xlung, VetPain). Sem "cães e gatos" (a ficha fala em animais das diferentes espécies). Sem cidade (CP1).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Anestesiologia Veterinária; pós-graduação em anestesiologia veterinária.
- Área: anestesiologia veterinária; anestesia clínica; medicina veterinária.
- Modalidade: pós-graduação semipresencial, com módulos online e módulos presenciais de prática, com avaliação ao término dos módulos online e acompanhamento individualizado no presencial.
- Conceitos do curso: avaliação e medicação pré-anestésica; sedação e monitoração; intubação, indução e anestesia geral inalatória; TIVA e anestesia alvo-controlada; fisiologia cardiovascular e respiratória aplicadas à anestesia; farmacologia aplicada à anestesiologia; analgesia multimodal e avaliação da dor com escalas validadas; anestesia em pacientes especiais; anestesia em felinos e em animais exóticos; reanimação cardiorrespiratória; vias aéreas difíceis e acessos emergenciais.
- Onde nomear: hero, sobre, para_quem, faq e matriz (dado, só depois da correção, O3 seção 8.3).
- Não nomear como entidade (O1, seção 13.1): anestesiologia avançada (657); anestesiologia locorregional e bloqueios guiados por ultrassom (359; o módulo de bloqueios é conteúdo e só aparece no `sobre` e na frase-ponte do FAQ); pós em anestesiologia veterinária em São Paulo (68607); "Direto ao ponto" e EAD (586); prova ou curso preparatório de título de especialista (E13); residência; ventilação mecânica aplicada à anestesia como curso (68618 e 507); marcas e protocolos de terceiros (RECOVER, ROTEM, Xlung, VetPain); grupo de estudo, mini curso e aprimoramento (Cursos Livres); "cães e gatos" como recorte; "gravada"; bolsa; Goiânia (CP1).

**descricao_schema** (245 caracteres, limite 300):

> Pós-graduação em Anestesiologia Veterinária da Faculdade Ufape, semipresencial. Anestesiologia clínica da avaliação pré-anestésica à anestesia de pacientes especiais, com prática presencial, analgesia multimodal e acompanhamento individualizado.

#### JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Anestesiologia Veterinária da Faculdade Ufape, semipresencial. Anestesiologia clínica da avaliação pré-anestésica à anestesia de pacientes especiais, com prática presencial, analgesia multimodal e acompanhamento individualizado.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "anestesiologia veterinária" },
        { "@type": "Thing", "name": "avaliação pré-anestésica" },
        { "@type": "Thing", "name": "anestesia de pacientes especiais" },
        { "@type": "Thing", "name": "analgesia multimodal" }
      ],
      "offers": {
        "@type": "Offer",
        "price": "{{catalogo.preco_total}}",
        "priceCurrency": "BRL",
        "url": "{{pagina.url_canonica}}"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "name": "{{catalogo.nome}}, turma {{catalogo.turma}}",
        "courseMode": "{{catalogo.modalidade}}",
        "startDate": "{{catalogo.inicio_iso}}",
        "courseWorkload": "PT{{catalogo.carga_horaria_h}}H",
        "location": {
          "@type": "Place",
          "name": "Faculdade UFAPE",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "{{catalogo.local_cidade}}",
            "addressRegion": "{{local.uf}}",
            "addressCountry": "BR"
          }
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Quero entrar na anestesia. Preciso já ser anestesista?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários que querem atuar na anestesiologia veterinária clínica. O curso começa pela fisiologia cardiovascular e respiratória aplicada e pela farmacologia aplicada à anestesiologia."
          }
        },
        {
          "@type": "Question",
          "name": "Vou praticar ou só assistir?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Os módulos presenciais trazem hands-on de sedação e monitoração, de TIVA e anestesia alvo-controlada e de anestesia em felinos e em exóticos, além de intubação e indução, prática de bloqueios em modelos anatômicos e reanimação cardiorrespiratória, entre outros. No presencial, a evolução de cada aluno é acompanhada sob supervisão do corpo docente."
          }
        },
        {
          "@type": "Question",
          "name": "Anestesiologia, avançada ou locorregional: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Anestesiologia Veterinária é centrada na anestesiologia clínica, da avaliação pré-anestésica à anestesia de pacientes especiais. A Pós-graduação em Anestesiologia Avançada é centrada na transição da anestesia de protocolo para a anestesia de precisão. A Pós-graduação em Anestesiologia Locorregional Veterinária é centrada nas técnicas de anestesia locorregional. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula aparecem nesta página antes de qualquer pagamento."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. O reembolso dos valores de inscrição é devido se a turma não for confirmada."
          }
        }
      ]
    }
  ]
}
```

Notas de 68609:

- A pergunta da ponte nomeia "avançada" e "locorregional" só dentro dos nomes das outras pós-graduações, como na O3 (E11). Os links para 657 e 359 só existem no HTML, depois da conferência das páginas (E19). Sem recorte de quem pode entrar em 657 (U10) e em 359 (OU24).
- Sem o convite da prova de Especialista (E13, OU31). Sem marcas de terceiros. Sem `instructor` (duplicatas de docente, E15, OU31).
- O item "Posso entrar depois que a turma começar?" é dado da turma (OU14), com a data do 3º módulo pela ficha. Reposição de módulo perdido [CONFIRMAR OU3]. Experiência prévia da primeira pergunta [CONFIRMAR NO CATÁLOGO].

---

## 7. Checagens

### 7.1 Contagens (limite usado por campo)

Contagem à mão; o orquestrador reconta por script. Palavras de `resposta_citavel` contadas com hífen como uma palavra.

| Turma | titulo_seo (limite 60) | descricao_seo (limite 155) | resposta_citavel (40 a 60 palavras) | descricao_schema (limite 300) |
|---|---|---|---|---|
| 679 | 49 | 151 | 49 | 285 |
| 68632 | 58 | 138 | 48 | 259 |
| 68635 | 55 | 141 | 47 | 247 |
| 366 | 58 | 135 | 42 | 240 |
| 68628 | 46 | 139 | 50 | 255 |
| 68617 | 59 | 145 | 47 | 235 |
| 68636 | 48 | 141 | 43 | 230 |
| 68609 | 51 | 148 | 43 | 245 |

Pontos de atenção para a recontagem: `titulo_seo` de 68617 (59, margem de um caractere), de 68632 e de 366 (58); `descricao_seo` de 679 (151) e de 68609 (148); `descricao_schema` de 679 (285). Se algum campo passar do limite, a redução sugerida é: em 68617, trocar o título para o nome sem " | Ufape" (51); em 679, tirar "hospitalar" da `descricao_seo`; em 679, tirar "e de controle de infecção" da `descricao_schema`.

### 7.2 Unicidade e canibalização (auditorias/03-busca.md)

- Os 8 títulos e as 8 descrições são diferentes entre si; nenhum repete o texto de outra turma do lote nem das turmas já escritas na onda 2 (657, 341, 289, 68615 e 333).
- Cada turma leva uma palavra principal, igual à primeira semente da Busca paga da mesma turma (O1, seção 1), mas a forma digitada de 366 ("fisioterapia veterinária") entra no corpo e nunca como nome da página.
- Pares de turma antiga à venda: seção 9 (E20).

### 7.3 Separação de vocabulário entre turmas da mesma área (O1, seção 4), conferida nos cinco campos de SEO de cada turma

| Turma | Termos do próprio campo | Termos conferidos como ausentes nos campos de SEO (aparecem só nas frases-ponte do FAQ, que repetem a O3) |
|---|---|---|
| 679 (A14) | infectologia, doenças infecciosas, zoonoses, controle de infecção | citopatologia, hematologia, sepse, terapia intensiva, clínica médica, pequenos animais, cães e gatos |
| 68632 (A4) | clínica cirúrgica, cirurgia presencial, acessos cirúrgicos, perioperatório | ortopedia, osteossíntese, videocirurgia, neurocirurgia, fisioterapia, reabilitação, anestesia, semipresencial, online |
| 68635 (A3) | clínica médica, emergência do paciente grave, semiologia | terapia intensiva, UTI, cães e gatos, certificação, internação |
| 366 (A4) | fisioterapia, fisiatria, reabilitação, hidroterapia, recursos eletrofísicos | ortopedia, fisioterapeuta, clínica cirúrgica, videocirurgia, conselho, cães e gatos, coordenação |
| 68628 (A10) | oncologia, quimioterapia, imunoterapia, neoplasias | eletroquimioterapia como curso, citologia, hematologia, cirurgia oncológica como pós, pequenos animais, número da turma |
| 68617 (A7) | endocrinologia, Cushing, diabetes, tireoide, calcemia | nefrologia, geriatria, dermatologia, metabologia, TCC, número da turma |
| 68636 (A2) | pneumologia, sistema respiratório, endoscopia respiratória, ultrassonografia pulmonar | cardiologia, ventilação mecânica, terapia intensiva, pneumologista, especialidade, escassez |
| 68609 (A1) | anestesiologia clínica, avaliação pré-anestésica, pacientes especiais, TIVA | avançada, locorregional, especialista, prova, EAD, marcas de terceiros, "Anestesiologias" no plural |

Conferência feita por leitura dos campos finais; a busca por script é do orquestrador e do qa (E12).

### 7.4 Checagem de extração (skill visibilidade-em-ia)

| Item | 679 | 68632 | 68635 | 366 | 68628 | 68617 | 68636 | 68609 |
|---|---|---|---|---|---|---|---|---|
| Primeira frase da `resposta_citavel` diz o que é o curso | sim | sim | sim | sim | sim | sim | sim | sim |
| Bloco de 40 a 60 palavras que faz sentido sozinho | sim | sim | sim | sim | sim | sim | sim | sim |
| FAQ com perguntas reais (hipóteses da persona, O3) | sim | sim | sim | sim | sim | sim | sim | sim |
| Marcação estruturada (Course, CourseInstance, Offer, FAQPage) | sim, `startDate` só com a data confirmada | sim | sim | sim, `startDate` só com a data confirmada | sim, sem a turma | sim, sem a turma | sim, `startDate` só com a data confirmada | sim |
| Coordenador ou docente identificado | pelo dado, fora da marcação | sem coordenação (OU34) | pelo dado | sem coordenação (OU34) | pelo dado | pelo dado | pelo dado | pelo dado |
| Data de atualização visível | [CONFIRMAR na plataforma] | idem | idem | idem | idem | idem | idem | idem |
| Conteúdo principal sem depender de JavaScript | [CONFIRMAR com o time do site] | idem | idem | idem | idem | idem | idem | idem |
| Tabela de comparação quando a pergunta compara | guia A14 (679-Q5) | guia A4 (68632-Q4) | guia A3 (68635-Q3) | guia A4 (366-Q5) | guia A10 (68628-Q3) | guia A7 (68617-Q5) | guia A2 (68636-Q4) | guia A1 (68609-Q3) |

Nenhum resultado de assistente de IA foi registrado: as 64 perguntas da O1 (8 por turma) seguem "conferir manualmente", com o roteiro da skill (de 3 a 5 rodadas por assistente, taxa registrada).

### 7.5 Conformidade educacional (auditorias/conformidade-educacional.md, itens que tocam o SEO)

| Item | Situação |
|---|---|
| Nome, modalidade e dados batem com o catálogo | Sim: nenhum dado digitado no texto; a marcação usa chaves do catálogo; 68632 sem "semipresencial", as outras 7 com "semipresencial" |
| Status "aberto" nas 8 | Sim (catálogo, seção 2, linhas 79 a 87) |
| Pós lato sensu sem "reconhecida pelo MEC" e sem nota MEC | Sim: nenhum "MEC", "certificado" ou "reconhecida" em nenhum campo; sem `educationalCredentialAwarded` |
| Sem promessa de emprego, salário, aprovação ou resultado clínico | Sim |
| Superlativos | Nenhum (E14) |
| Bolsa, desconto e promoção | Nenhum |
| Urgência | Nenhuma; a regra do 3º módulo é dado da turma (OU14) e não entra em campo de SEO |
| Preço | Só pela chave `catalogo.preco_total` na marcação; nenhum valor no texto |
| Título de especialista e prova de Especialista (E13) | Nenhum |
| Nenhum dado pessoal; nenhum docente nomeado | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; a busca final é do orquestrador |

---

## 8. Conferência da marcação com o catálogo (só para o qa; não é texto de página)

Valor que cada chave deve devolver, segundo contexto/catalogo-de-cursos.md, seção 2. A plataforma preenche; qualquer divergência é erro de dado, não de marcação.

| Chave | 679 | 68632 | 68635 | 366 | 68628 | 68617 | 68636 | 68609 |
|---|---|---|---|---|---|---|---|---|
| `catalogo.nome` | Pós-graduação em Infectologia Veterinária | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária | Pós-graduação em Oncologia Veterinária | Pós-graduação em Endocrinologia de Pequenos Animais | Pós-graduação em Pneumologia Veterinária | Pós-graduação em Anestesiologia Veterinária |
| `catalogo.turma` | IV | V | V | I | não emitida (P5) | não emitida (P5) | VIII | VIII |
| `catalogo.modalidade` | Semipresencial | Presencial | Semipresencial | Semipresencial | Semipresencial | Semipresencial | Semipresencial | Semipresencial |
| `catalogo.inicio_iso` (planilha) | 2027-04-03 [CONFIRMAR OU19] | 2027-04-10 | 2027-04-10 | 2027-04-10 [CONFIRMAR OU20: o site traz outra data] | 2027-04-10 | 2027-04-17 | 2027-04-17 só no site [CONFIRMAR OU21] | 2027-04-24 |
| `catalogo.carga_horaria_h` | 500 | 500 | 750 | 500 | 500 | 500 | 500 | 500 |
| `catalogo.local_cidade` | São Paulo | Goiânia | São Paulo | São Paulo | São Paulo | São Paulo | São Paulo | Goiânia |
| `catalogo.preco_total` (total, sem parcelas nem matrícula) | 33000.00 | 33000.00 | 33000.00 | 33000.00 | 38940.00 | 36000.00 | 37950.00 | 32450.00 |
| `local.uf` | SP | GO | SP | SP | SP | SP | SP | GO |

Notas:

- `local.uf`: o catálogo não traz a sigla; as siglas vêm de contexto/ufape-geral.md ("São Paulo, SP" e "Goiânia, GO") [CONFIRMAR NO CATÁLOGO].
- `pagina.url_canonica`: o catálogo e a plataforma ainda não trazem a URL final das páginas novas; as fichas só têm a URL das páginas atuais, e 6 das 8 estão sem o "em" no endereço (pedido S5 da O1) [CONFIRMAR]. Em 68617 a URL atual termina em "/v/" (pedido S6).
- `catalogo.modalidade`: o valor vira o termo da marcação por regra da plataforma (por exemplo, semipresencial para "blended" e presencial para "onsite") [SUPOSIÇÃO].
- `courseWorkload` no formato de duração ISO (PT500H) [SUPOSIÇÃO: formato escolhido por este agente, em conformidade com o schema.org].
- 68628: o catálogo traz turma VII e a planilha traz VI; 68617: o catálogo traz V e a planilha traz VII. Por isso a chave de turma não entra na marcação das duas (P5).
- 366: a planilha traz o início em 10/04/2027 e o site, em outra data de abril; vale a planilha pela decisão 12, mas a O1 e a O3 pedem a confirmação (OU20). Em 679 e 68636 a data é a do site e só vale depois da confirmação.

---

## 9. Disputa de busca com turma antiga à venda (E20), registrada por turma

A regra proposta é a da O1, seção 5.2 (uma palavra principal, uma página; canonical para a página nova enquanto a antiga vende e 301 depois da data limite da antiga, quando é a mesma oferta; canonical próprio quando o campus ou a modalidade é outro). Nada disso é feito pela squad: são pedidos ao time do site, todos [CONFIRMAR]. As datas das turmas antigas são nota interna da O1 e não entram aqui.

| Turma nova | Turma antiga | Tipo | O que este arquivo faz | Pedido ao time do site (O1, seção 5.3) |
|---|---|---|---|---|
| 679 | nenhuma | sem turma antiga do mesmo curso | Nada a separar. Risco de destino: a linha "Citopatologia 03/04" da visão de campanhas aponta para esta página (P3) | S7: corrigir a linha e confirmar a data (OU19) |
| 68632 | 535 (Goiânia, presencial, mesma oferta em outra data) | mesma oferta | O título e a descrição de 68632 não têm como se diferenciar de 535: é a mesma oferta. A saída é canonical, não texto | S1: canonical da 535 para a 68632 e 301 depois da data limite; confirmar se a venda da 535 já terminou |
| 68632 | 665 (São Paulo, semipresencial, mesmo nome) | mesmo nome, outro campus e outra modalidade | O texto diz "presencial" na `descricao_seo`, na `resposta_citavel` e na `descricao_schema`; o título é o nome do catálogo, igual ao da 665 (D2). A cidade só entra no dado e no JSON-LD (`location`). Com a CP1 aprovada, a cidade entra no título das duas | S3: canonical próprio em cada uma; depois da data limite da 665, 301 para a página do curso ou para a próxima turma do mesmo campus, nunca para outro campus |
| 68635 | 663 (São Paulo, semipresencial, mesma oferta) | mesma oferta | Título e descrição iguais em substância aos da 663: é a mesma oferta em outra data. A saída é canonical | S2: canonical da 663 para a 68635 e 301 depois da data limite; confirmar se a venda da 663 já terminou |
| 366 | nenhuma | turma I | Nada a registrar | Nada |
| 68628 | 654 (São Paulo, semipresencial, sem venda) | mesma oferta, sem venda | O título de 68628 é o nome do catálogo, igual ao da 654. A página da 654 não vende, mas indexa | S4: 301 de 654 para a 68628 (já pode ser feito) |
| 68617 | nenhuma turma antiga do mesmo curso | URL "/v/" | Nada a separar em texto | S6: se existirem duas URLs com o mesmo conteúdo, canonical para a URL final (OU29) |
| 68636 | 670 (SP, encerrada, link fora do ar) | mesma oferta, encerrada | O título de 68636 é o nome do catálogo, igual ao da 670. A planilha traz a data de 10/04/2027 na linha de 670 e nenhuma na de 68636 (OU21) | S4: 301 de 670 para a 68636 (já pode ser feito) |
| 68609 | 68607 (São Paulo, semipresencial, mesmo nome) | mesmo nome, outro campus | Título e descrição de 68609 iguais em substância aos da 68607: a única diferença real é o campus, que a CP1 mantém fora do texto. Sem CP1, a diferença fica só em `location` e em `local_e_datas` | S3: canonical próprio em cada uma; com a CP1 aprovada, cidade no título das duas; depois da data limite da 68607, 301 para a próxima turma do mesmo campus |
| 68609 | 664 (Goiânia, mesma oferta, sem venda) | mesma oferta, sem venda | Mesmo título e mesma descrição em substância | S4: 301 de 664 para a 68609 |
| 68609 | 586 (EAD, "Direto ao ponto") | produto diferente | O texto de 68609 não usa "EAD" nem "Direto ao ponto"; a dúvida "EAD ou semipresencial" vai ao guia A1, não à página de venda | Sem canonical nem 301 |

Observações:

- **Provas de bolsa da mesma área** (68639 e 68640 em anestesiologia; 68643 e 68644 em clínica cirúrgica; 68645 em clínica médica e emergência; 68648 em endocrinologia; 68657 em oncologia; 68659 em pneumologia) competem pela consulta da área. Pela decisão 14 nenhum campo deste arquivo mira "bolsa", e o link interno entre prova e turma fica com a onda das provas [CONFIRMAR].
- **Decisão para a pessoa do marketing (CP1):** sem a cidade no título, 68632 x 665 e 68609 x 68607 só se separam por canonical e por dado; com a CP1, cidade e modalidade entram no título e na descrição dessas duas turmas (proposta do qa na Q55 da onda 2).
- Páginas antigas das turmas 535 e 663 podem ter passado da data limite da decisão 18 (O1, seção 1, item 3). Se ainda vendem, vendem fora da regra [CONFIRMAR com o time do site].

---

## 10. Pedidos e observações para o qa e para a próxima etapa

1. **Para o qa (D1):** decidir sobre os títulos de 68635 e 366 sem o prefixo "Pós-graduação em". A alternativa é a forma digitada em 366, com o risco de E2.
2. **Para o qa (D3):** conferir que a `resposta_citavel` sem frase de público atende o campo "o que é e para quem é" do template; se o qa preferir uma frase de público, ela precisa vir da ficha ("Médicos Veterinários") e não do pré-requisito.
3. **Para a O3 e o qa (observação, sem editar o arquivo alheio):** o `sobre` de 68609 cita "bloqueios locorregionais" como conteúdo de módulo e a frase-ponte nomeia "Anestesiologia Locorregional Veterinária". Os campos de SEO de 68609 não usam "locorregional"; cabe ao qa decidir se as duas ocorrências ficam como conteúdo.
4. **Para a O3 e o qa:** em 68617 a frase do guia A7 só entra na resposta do FAQ e na marcação com o guia publicado e linkado.
5. **Aplicação da marcação (time do site, depois da aprovação):** testar cada página com o validador de dados estruturados antes de publicar; publicar a marcação só junto com a página (prazo da O3: 10/12/2026); conferir que o FAQ marcado é o mesmo que está visível; emitir `startDate` de 679, 366 e 68636 só com a data confirmada.
6. **Descrição e título são rascunho de SEO, não promessa:** nada aqui altera mídia, anúncio, CRM ou site.

**Próximo agente:** editor-de-conteudo, com este arquivo e a O3, para revisar a voz antes da aprovação humana. Pela cadeia do plano (workflow /pagina-de-curso), a O5 é o otimizador-de-cta (formulário e CTA final) e depois o qa-de-marketing (O18a).

---

## 11. 662: registro de espera (OU18)

Nenhum campo foi escrito para 662. Espera total até a Ufape responder OU18 (24/04/2027 é turma nova de Ortopedia ou o módulo 9 da turma IV, e qual é a ficha de 2027). Efeito neste arquivo: "ortopedia veterinária" e "osteossíntese" ficam reservados a 662; nenhum campo de 68632 nem de 366 usa o termo (O1, seção 4), e o FAQ de 366 só traz "ortopédicas" como conteúdo da frase-ponte, palavra por palavra como na O3. Quando a resposta chegar, o plano prevê ciclo extra com a seção de 662 em nova versão deste arquivo.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início, preço total e status "aberto" das 8 turmas: contexto/catalogo-de-cursos.md, seção 2, linhas 79 a 87 (valores só nas chaves da seção 8; nenhum no texto).
- Limites de caracteres e palavras, ausência de número no texto da IA, `descricao_schema` e regra de que a plataforma monta o JSON-LD com os fatos do banco: templates/pagina-da-turma.md.
- Palavra principal por turma, tabela de quem fica com cada termo entre turmas da mesma área, termos que não são de cada página, pares de turma antiga e pedidos S1 a S7: O1 (saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda3.md, seções 1, 3 a 5 e 6 a 13).
- Conteúdo do curso (módulos, formato por módulo, prática presencial, temas por sistema), perguntas e respostas do FAQ, travas aplicadas e pendências por turma: O3 (saidas/08-conversao/landing-page-pos-2026-10-27-onda3.md) e as fichas em contexto/cursos/pos/, lidas pela O1 e pela O3.
- Listas de módulos presenciais usadas na conferência de E4 e E5: 679 com 3 presenciais (laboratório, zoonoses e controle de infecção); 68617 com 2 presenciais, ambos de aula prática; 68636 com aulas teóricas a distância e aulas práticas presenciais (legenda da ficha); 68609 com 10 presenciais, hands-on só nos módulos de sedação, TIVA e anestesia em felinos e exóticos (O1, seções 6, 11, 12 e 13; O3, seções 1.5, 6.5, 7.5 e 8.5).
- Regras E1 a E22 e travas por turma, OU3, OU14, OU18 a OU21, OU25, OU29 a OU31, OU34 e OU35: plano do CMO (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md, versão 2, seções 2 e 4).
- Revisão Q39 a Q55 da onda 2 (nome do catálogo não muda; "veterinária" entra fora do nome; sem frase de público na `resposta_citavel`; disputa com turma antiga): saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md.
- Matrícula até o 3º módulo (decisão 18), turma mínima de 15 (decisão 11), sem bolsa (decisão 14), datas da planilha (decisão 12): docs/execucao-2026-10-26.md.
- Nome da instituição ("Faculdade UFAPE") e site (faculdade.ufape.com.br); siglas SP e GO: contexto/ufape-geral.md, como usado na onda 2.
- Estrutura e passos de Course, CourseInstance, FAQPage e a regra de que o FAQ marcado é o visível: .claude/skills/schema-de-curso/SKILL.md. Regras de extração e de não inventar resultado de IA: .claude/skills/visibilidade-em-ia/SKILL.md.
- Auditoria do departamento: auditorias/03-busca.md. Conformidade: auditorias/conformidade-educacional.md.

## [SUPOSIÇÃO]

- A marca " | Ufape" no fim dos títulos que cabem em 60 caracteres (padrão único; sem fonte).
- O título de 68635 e de 366 sem o prefixo "Pós-graduação em" (D1) e o de 68632 sem a palavra "presencial" (D2).
- "Veterinária" como palavra de corpo em 68632, 68635 e 68617 (nomes do catálogo sem a palavra), como pede a O1 e a revisão Q39 a Q43 da onda 2.
- "Fisioterapia veterinária" no corpo de 366 (forma digitada pelo candidato, O1 366-K0) e "avaliação do aparelho locomotor" como leitura da ficha ("inspeção do aparelho locomotor").
- A pergunta opcional da ponte de 679 com 68635 entra na marcação; sai se o qa a tirar da página.
- Os valores de `about`, a escolha de `EducationalOrganization` como `provider`, `courseWorkload` em duração ISO e `courseMode` por regra da plataforma.
- Que a marcação de 68617 sem a frase do guia A7 é a versão correta até a publicação do guia.
- Que o validador do template ignora "um" e "uma" como artigo e conta "Pós-graduação", "pré-anestésica", "hands-on" e "teórico-práticas" como uma palavra cada (se separar, cada resposta sobe no máximo 3 palavras).
- Contagens de caracteres e palavras feitas à mão, a recontar por script.

## [CONFIRMAR]

- **CP1:** se a cidade pode entrar em `titulo_seo` e `resposta_citavel` por variável do dado (pesa em 68632 x 665 e 68609 x 68607; sem a aprovação, a diferença fica no dado, no JSON-LD e em canonical).
- **D1, D2 e D3:** decisão do qa sobre os títulos sem prefixo e sobre a `resposta_citavel` sem frase de público.
- **OU3:** reposição do módulo 1 presencial de 68632 (sem item de entrada depois do início em nenhum campo enquanto aberta).
- **OU14, OU25 e OU6:** se a regra do 3º módulo entra como item de dado no FAQ e na marcação; dia do 3º módulo de 679, 68635 e 366; leitura de "até o 3º módulo".
- **OU19, OU20 e OU21:** datas de 679, 366 e 68636 (e CEP de 366); `startDate` só depois da confirmação.
- **OU29 e OU30 (P5):** turma e URL de 68617 e turma de 68628; duplicatas de docentes (E15).
- **OU31 e OU34:** convite da prova de Especialista de 68609 e duplicatas de docentes; quem representa 68632 e 366 (nenhum campo diz "coordenação").
- **OU35:** texto da regulação sobre as duas certificações de 68635; até lá nenhum campo cita certificação.
- **OU4 e U11:** vagas e valor da inscrição; nenhum campo cita.
- **[CONFIRMAR NO CATÁLOGO]:** sigla de UF (`local.uf`); URL canônica das 8 páginas; slug de curso e de turma (O3); "de cães e gatos" e "de pequenos animais" onde a ficha não restringe a espécie; nível de entrada e experiência prévia; TCC em 68617; módulos de 68628 e de 68609 (24 ou 26).
- **Reembolso:** redação final por turma e alcance de "valores de inscrição"; em 679 a ficha não traz a linha (a marcação de 679 segue a página, sem a frase).
- **Turma antiga (E20):** regra de canonical e 301, fim de venda de 535 e 663 e quem executa (pedidos S1 a S7 da O1).
- **Guia A7 (68617):** publicado, com link, antes de a frase do guia entrar na resposta do FAQ e na marcação.
- **Links das pontes (E19):** páginas de 68635, 366, 657, 359, 68623, 578, 289 e 352 conferidas antes de o nome virar link.
- **Revisão docente e regulação:** conferência técnica das respostas citáveis e das entidades por um docente de cada área; quem pode atuar depois da pós de 366.
- **Plataforma e time do site:** se a data de atualização fica visível, se o conteúdo principal aparece sem JavaScript e qual o formato aceito para `courseMode`.
- **Checagem em assistentes:** rodar as 64 perguntas da O1 de 3 a 5 vezes por assistente e registrar a taxa; sem isso não há nota de visibilidade.
