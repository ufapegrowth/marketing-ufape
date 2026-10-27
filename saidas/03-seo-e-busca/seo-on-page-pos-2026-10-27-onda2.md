# SEO on-page das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333), encomenda F4 da onda 2

- **Agente:** seo-on-page (departamento 03, SEO e Busca por IA)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** F4 do plano do CMO em versão 2 (saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md, seção 10, linha F4). O plano previa o nome seo-on-page-pos-2026-11-16.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Status:** rascunho para o qa-de-marketing (auditorias/03-busca.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada é publicado, enviado ou pago. Aplicar a marcação no site é ação do time do site (projeto ufape-site), depois da aprovação.
- **Consumidores:** otimizador-de-cta (F5), qa-de-marketing (F13) e a plataforma, que valida o formato de templates/pagina-da-turma.md.
- **Entradas lidas (todas em /home/user/marketing-ufape/):**
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 8, 11, 14, 16 e 18)
  - contexto/ufape-geral.md e contexto/pos-graduacao.md (inclusive "Padrão de nome")
  - contexto/catalogo-de-cursos.md (seção 2, linhas de 657, 341, 289, 68615 e 333; fonte única dos dados de curso)
  - Fichas em contexto/cursos/pos/: 657 inteira; 341, 289, 68615 e 333 só o bloco "Dados principais" (o texto das páginas dessas quatro chegou pela F3, que as leu inteiras)
  - templates/pagina-da-turma.md (limites: titulo_seo até 60 caracteres, descricao_seo até 155, resposta_citavel de 40 a 60 palavras, descricao_schema até 300, tudo sem número)
  - auditorias/03-busca.md (auditoria do departamento) e auditorias/conformidade-educacional.md
  - .claude/skills/visibilidade-em-ia/SKILL.md e .claude/skills/schema-de-curso/SKILL.md
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (seções 1, 2, 4, 8, 9 e 10)
  - F1: saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md (inteiro)
  - F3: saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md (inteiro)
- **Não aberto:** faculdade.ufape.com.br; a saída da F2 (as respostas dela chegam pela F3, que as usou sem reescrita); nenhuma busca na web nova (os resultados de busca vêm do F1).
- **Dados pessoais:** nenhum. Nenhum docente é nomeado.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape tem. [CONFIRMAR NO CATÁLOGO] é dado de curso que o catálogo não traz. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com o critério.

---

## 0. Como ler este arquivo e regras aplicadas às 5 turmas

1. **Limites usados** (templates/pagina-da-turma.md): `titulo_seo` até 60 caracteres, `descricao_seo` até 155, `resposta_citavel` de 40 a 60 palavras, `descricao_schema` até 300. Contei à mão, espaços e pontuação inclusos, e conferi duas vezes; o validador da plataforma tem a palavra final. Palavra com hífen conta como uma palavra (se o validador separar, cada resposta sobe no máximo 2 palavras e continua dentro do intervalo).
2. **Sem número em nenhum campo de texto** (nem algarismo, ordinal ou numeral romano), sem preço, data, local, carga horária, duração, vaga ou nome de docente. "Faculdade Ufape", "semipresencial" e "um" ou "uma" como artigo são os únicos termos que o texto leva além do conteúdo do curso (a F1 autoriza "semipresencial" no corpo).
3. **CP1 aplicada como trava:** nenhuma das 5 turmas leva cidade em `titulo_seo`, `descricao_seo`, `resposta_citavel`, `descricao_schema` ou resposta de FAQ. Em 289, a cauda de Goiânia (F1: 289-K1 e 289-K2, a melhor aposta da turma) fica só no dado (`local_e_datas`) e no JSON-LD (`location`). Se a pessoa do marketing aprovar a CP1, o cmo pede uma versão nova deste arquivo; nenhuma variante com cidade está escrita aqui.
4. **Sem as palavras proibidas da F3:** nenhum "MEC", "certificado", "reconhecida", "bolsa", "promoção", urgência ou contador, nenhum "especialista" como título, nenhum pré-requisito. 657 sem a parte "para quem" (U10). 341 sem promoção (OU10). 333 sem "coordenação" (OU12). Nenhum superlativo da ficha, nenhuma promessa de emprego, renda, aprovação ou resultado clínico.
5. **Divisão 68615 x 333 (F1, seção 4):** 68615 só usa o vocabulário de laboratório clínico (patologia clínica, laboratório clínico, pré-analítico, correlação clínico-laboratorial, controle de qualidade); 333 só usa o de leitura de lâminas (citopatologia, leitura de lâminas, coloração, microscopia). Nenhum dos dois campos de SEO de 68615 traz "citologia" ou "citopatologia", e nenhum de 333 traz "patologia clínica", "laboratório clínico" ou "hematologia". A única menção cruzada é a pergunta-ponte do FAQ, que já é texto da F3. "Mielograma" e "hemograma" ficam fora de todos os campos de SEO das duas.
6. **Nome padrão:** "Pós-graduação em <área>" (contexto/pos-graduacao.md). Em 657 e 68615 o nome do catálogo não traz "veterinária": o nome fica exatamente como no catálogo em todo campo, e a palavra entra fora do nome ("anestesia veterinária", "laboratório clínico veterinário", "para veterinários"), como pede a F1 ("sem trocar o nome do catálogo"; correção do qa na revisão F13a).
7. **Marca no título:** todos os títulos fecham com " | Ufape", para o padrão ser único nas 5 páginas [SUPOSIÇÃO].
8. **JSON-LD:** os valores de dado (nome, início, turma, carga horária, modalidade, cidade, preço) entram como chave `{{...}}` e não foram digitados, porque a plataforma monta o JSON-LD com os fatos do banco (template, seção "Marcação para buscadores e IA") e porque o texto proíbe número. A seção 7 mostra, só para conferência do qa, o valor que cada chave deve devolver segundo o catálogo. O FAQPage repete palavra por palavra as respostas que a F3 escreveu (o FAQ marcado tem de ser o que está visível, skill schema-de-curso).

---

## 1. Seção 657: Pós-graduação em Anestesiologia Avançada

Palavra principal (F1): pós-graduação em anestesiologia avançada veterinária. Página: a da turma 657.

### 1.1 Campos de SEO

**titulo_seo** (48 caracteres, limite 60):

> Pós-graduação em Anestesiologia Avançada | Ufape

O nome fica igual ao do catálogo; "veterinária" vai na descrição e na resposta citável.

**descricao_seo** (147 caracteres, limite 155; contagem do qa, a recontar por script):

> Pós-graduação em Anestesiologia Avançada, semipresencial: anestesia veterinária com hemodinâmica, ventilação do paciente especial e prática guiada.

**resposta_citavel** (54 palavras, faixa de 40 a 60):

> A Pós-graduação em Anestesiologia Avançada da Faculdade Ufape é um curso semipresencial de anestesia veterinária que leva a anestesia do protocolo à anestesia de precisão. O programa trata de fisiologia aplicada, hemodinâmica, ventilação do paciente especial, bloqueio neuromuscular e coagulação, com prática presencial guiada. O foco é a decisão crítica em pacientes de risco.

A resposta não diz quem pode entrar (U10). Nenhuma frase descreve público (U10): "O foco é a decisão crítica" fala do curso, não de quem entra.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Anestesiologia Avançada; pós-graduação em anestesiologia avançada veterinária.
- Área: anestesiologia veterinária; medicina veterinária; médica e médico veterinário (a profissão, sem requisito de entrada).
- Modalidade: pós-graduação semipresencial, com teoria online e módulos presenciais de prática.
- Conceitos do curso: anestesia de precisão; anestesia de protocolo; fisiologia aplicada; tomada de decisão crítica; gestão de riscos; hemodinâmica avançada, débito cardíaco e perfusão tecidual; ventilação do paciente especial e proteção pulmonar; bloqueio neuromuscular e ventilação monopulmonar; distúrbios de coagulação e uso racional de hemoderivados; avaliação viscoelástica do coágulo; TIVA e TCI; anestesia em cirurgias neurológicas e cardiotorácicas; dor e analgesia em felinos.
- Onde nomear: hero, sobre, matriz (dado) e faq.
- Não nomear como entidade (F1, seção 5.1): locorregional (é de 359), ventilação mecânica (é de 352 e de 68618), pets não convencionais e reanimação (Livres), "título" ou "prova" de especialista, EAD e residência.

**descricao_schema** (260 caracteres, limite 300):

> Pós-graduação em Anestesiologia Avançada da Faculdade Ufape, semipresencial. Anestesia veterinária da anestesia de protocolo à anestesia de precisão: fisiologia aplicada, hemodinâmica, ventilação, bloqueio neuromuscular, coagulação e prática presencial guiada.

### 1.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Anestesiologia Avançada da Faculdade Ufape, semipresencial. Anestesia veterinária da anestesia de protocolo à anestesia de precisão: fisiologia aplicada, hemodinâmica, ventilação, bloqueio neuromuscular, coagulação e prática presencial guiada.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "anestesiologia avançada" },
        { "@type": "Thing", "name": "anestesia de precisão" },
        { "@type": "Thing", "name": "hemodinâmica avançada" },
        { "@type": "Thing", "name": "bloqueio neuromuscular" }
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
          "name": "O que o curso traz além da rotina de anestesia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O curso vai para onde o protocolo não chega: hemodinâmica além da pressão arterial, ventilação do paciente especial, bloqueio neuromuscular, coagulação no transoperatório e anestesia em cirurgias neurológicas e cardiotorácicas. Nos módulos presenciais, a prática é guiada, com ventiladores e monitores hemodinâmicos na mão e execução de TIVA e TCI."
          }
        },
        {
          "@type": "Question",
          "name": "Dá para encaixar o curso na escala do centro cirúrgico?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A teoria é online, em fins de semana com data marcada no cronograma. O presencial fica só nos módulos de prática, também com mês marcado, então dá para montar a escala antes de começar."
          }
        },
        {
          "@type": "Question",
          "name": "Quanto vou pagar no total?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O total, as parcelas e a matrícula estão nesta página, assim como o cronograma de cada módulo presencial. Você vê as condições e o que vai praticar antes de decidir."
          }
        },
        {
          "@type": "Question",
          "name": "E se a turma não fechar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados."
          }
        }
      ]
    }
  ]
}
```

Notas de 657: sem `audience`, sem `coursePrerequisites` e sem `educationalCredentialAwarded` (U10 e certificação oculta). O item "Posso entrar depois que a turma começar?" é dado da turma (OU14); se a plataforma o exibir no FAQ, a plataforma o inclui no `mainEntity` com o texto exato que o editor digitou. O `offers.price` vem só do campo de total do catálogo; a prova de recuperação "cobrada separadamente" (OB1, item 7 da F3) não entra no preço [CONFIRMAR].

---

## 2. Seção 341: Pós-graduação em Medicina Interna Equina

Palavra principal (F1): pós-graduação em medicina interna equina. Página: a da turma 341.

### 2.1 Campos de SEO

**titulo_seo** (48 caracteres, limite 60):

> Pós-graduação em Medicina Interna Equina | Ufape

**descricao_seo** (152 caracteres, limite 155):

> Pós-graduação em medicina interna equina, semipresencial: do paciente crítico ao potro neonato, sistema por sistema. Teoria online e prática presencial.

**resposta_citavel** (53 palavras, faixa de 40 a 60):

> A pós-graduação em medicina interna equina da Faculdade Ufape é um curso semipresencial que percorre a clínica do cavalo sistema por sistema, do paciente crítico ao potro neonato, com teoria online e prática presencial em fins de semana. É pensada para médicas e médicos veterinários interessados em aprofundar o raciocínio clínico por sistema.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Medicina Interna Equina (o catálogo traz "Pós Graduação"; o nome padrão da linha é o que vai à página).
- Área: medicina interna equina; medicina equina; clínica de equinos; médica e médico veterinário de equinos (variação de corpo, F1 341-K2).
- Modalidade: pós-graduação semipresencial, com teoria online e práticas presenciais em fins de semana.
- Conceitos do curso: abordagem clínica do paciente equino; paciente crítico, choque e cuidados intensivos; preparação cirúrgica e manejo de feridas; cardiologia equina com eletrocardiograma e ecocardiograma; trato respiratório; sistema digestivo; sistema locomotor e claudicação; neonatologia, UTI neonatal e potros críticos; podologia; odontologia equina; medicina equina baseada em evidências; leitura crítica; estágio obrigatório.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (F1, seção 6.1 e negativas da Busca paga): pequenos animais, cães e gatos; ortopedia e cirurgia equina; medicina esportiva equina e aptidão esportiva; residência e título de especialista; promoção, desconto e bolsa; "hospital veterinário" e qualquer local de prática (OU11).

**descricao_schema** (231 caracteres, limite 300):

> Pós-graduação semipresencial em Medicina Interna Equina da Faculdade Ufape. Clínica do cavalo sistema por sistema, do paciente crítico ao potro neonato, com teoria online, prática presencial e leitura crítica baseada em evidências.

### 2.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação semipresencial em Medicina Interna Equina da Faculdade Ufape. Clínica do cavalo sistema por sistema, do paciente crítico ao potro neonato, com teoria online, prática presencial e leitura crítica baseada em evidências.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "medicina interna equina" },
        { "@type": "Thing", "name": "clínica de equinos" },
        { "@type": "Thing", "name": "neonatologia equina" },
        { "@type": "Thing", "name": "medicina equina baseada em evidências" }
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
          "name": "Pratiquei pouco com cavalos na faculdade. O curso ajuda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O curso começa pela abordagem clínica do paciente equino e prevê treinamento prático e demonstrativo na maioria dos temas, do paciente crítico à podologia."
          }
        },
        {
          "@type": "Question",
          "name": "Atendo a campo. Dá para viajar para as aulas presenciais?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A teoria é online. O presencial acontece em fins de semana, com as datas publicadas no cronograma antes de começar. Compre passagem e hotel só depois de a turma ser confirmada."
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

Notas de 341: `offers.price` só do campo de total; o campo de preço do catálogo traz o texto da promoção cortado (OU10), então a plataforma lê o total e nunca o texto do campo; o `offers` de 341 só sobe com o dado limpo. Sem `location` além da cidade até OU11 (o segundo local da ficha não entra em marcação nenhuma). Sem pergunta sobre onde são as aulas práticas (bloqueada até OU11) e sem frase de reembolso (ficha truncada).

---

## 3. Seção 289: Pós-graduação em Cardiologia Veterinária

Palavra principal (F1): pós-graduação em cardiologia veterinária. Cauda local (F1, 289-K1 e 289-K2): fica só no dado e no JSON-LD, por CP1.

### 3.1 Campos de SEO

**titulo_seo** (48 caracteres, limite 60; sem cidade):

> Pós-graduação em Cardiologia Veterinária | Ufape

**descricao_seo** (145 caracteres, limite 155; sem cidade):

> Pós-graduação em cardiologia veterinária semipresencial: da fisiologia ao laudo, com ecocardiograma na mão. Presencial só nos módulos de prática.

**resposta_citavel** (52 palavras, faixa de 40 a 60; sem cidade):

> A pós-graduação em cardiologia veterinária da Faculdade Ufape é um curso semipresencial que vai da fisiologia e do eletrocardiograma às cardiopatias e às emergências cardíacas, com ecocardiograma na prática. A teoria é acompanhada a distância, e só os módulos práticos são presenciais. É pensada para médicas e médicos veterinários interessados em cardiologia.

A resposta não diz "de cães e gatos": a ficha traz também cardiologia equina e de pets não convencionais no cronograma [CONFIRMAR NO CATÁLOGO]. Por isso 289-K3 ("especialização em cardiologia de cães e gatos") não é atendido neste texto, sem perda de página (a F1 o marca como apoio).

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Cardiologia Veterinária; pós-graduação em cardiologia veterinária.
- Área: cardiologia veterinária; medicina veterinária; médica e médico veterinário.
- Modalidade: pós-graduação semipresencial, com teoria acompanhada a distância e módulos presenciais de prática hands-on.
- Conceitos do curso: anatomia, fisiologia e semiologia circulatória; farmacologia cardiovascular e insuficiência cardíaca congestiva; radiografia; eletrocardiograma, taquiarritmias e bradiarritmias; ecocardiograma na prática (só como conteúdo dos módulos); interpretação crítica e laudo; cardiopatias adquiridas, de cães e de felinos, e congênitas; hipertensão arterial sistêmica; síndrome cardiorrenal; anestesia do paciente cardiopata; emergências cardíacas.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq. A cidade é entidade do dado e do JSON-LD (`location`), nunca do texto.
- Não nomear como entidade (F1, seção 7.1 e negativas da Busca paga): ecocardiografia como curso (é de 698), pneumologia e ventilação mecânica (68636 e 352), cardiologia em São Paulo, nome de concorrente e edital de concorrente, EAD, título de especialista, prova de bolsa.

**descricao_schema** (244 caracteres, limite 300; sem cidade):

> Pós-graduação semipresencial em Cardiologia Veterinária da Faculdade Ufape. Da fisiologia e do eletrocardiograma às cardiopatias e às emergências cardíacas, com ecocardiograma na prática, teoria a distância e presencial só nos módulos práticos.

### 3.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação semipresencial em Cardiologia Veterinária da Faculdade Ufape. Da fisiologia e do eletrocardiograma às cardiopatias e às emergências cardíacas, com ecocardiograma na prática, teoria a distância e presencial só nos módulos práticos.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "cardiologia veterinária" },
        { "@type": "Thing", "name": "eletrocardiograma" },
        { "@type": "Thing", "name": "cardiopatias" },
        { "@type": "Thing", "name": "emergências cardíacas" }
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
          "name": "Moro longe. Vou ter de viajar todo mês?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não. A teoria é acompanhada a distância; só os módulos com aula prática são presenciais, e as datas estão no cronograma. Compre passagem e hotel só depois de a turma ser confirmada."
          }
        },
        {
          "@type": "Question",
          "name": "Preciso da cardiologia completa ou só do exame?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aqui o ecocardiograma faz parte de um percurso maior, que vai da fisiologia e do eletrocardiograma às cardiopatias e às emergências."
          }
        },
        {
          "@type": "Question",
          "name": "Sou clínico geral, não cardiologista. Serve para mim?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários, e o curso começa pela anatomia, pela fisiologia e pela semiologia circulatória antes de chegar aos exames."
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
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados."
          }
        }
      ]
    }
  ]
}
```

Notas de 289: na segunda resposta, a F3 acrescenta uma frase sobre o guia de decisão que só vai ao ar com o guia A2 publicado e linkado. A marcação acima está sem essa frase. Quando o guia sair, a mesma frase entra aqui, igual à da página, no mesmo dia. A cidade vem da chave `catalogo.local_cidade` (valor esperado: Goiânia). O endereço de rua de Goiânia não existe no catálogo (a ficha diz só "Ufape Goiânia"): `streetAddress` fica fora até a Ufape informar [CONFIRMAR NO CATÁLOGO]. O telefone de vendas de Goiânia vem do dado ou do formulário, nunca da marcação.

---

## 4. Seção 68615: Pós-graduação em Patologia Clínica

Palavra principal (F1): pós-graduação em patologia clínica veterinária. Vocabulário: laboratório clínico (F1, seção 4).

### 4.1 Campos de SEO

**titulo_seo** (60 caracteres, limite 60; reserva sem "para veterinários": 42):

> Pós-graduação em Patologia Clínica para veterinários | Ufape

**descricao_seo** (136 caracteres, limite 155):

> Pós-graduação em Patologia Clínica, semipresencial: o laboratório clínico veterinário do pré-analítico ao laudo, com prática presencial.

**resposta_citavel** (52 palavras, faixa de 40 a 60):

> A Pós-graduação em Patologia Clínica da Faculdade Ufape é um curso semipresencial com foco no laboratório clínico veterinário: do pré-analítico ao laudo, com correlação clínico-laboratorial, controle de qualidade e prática presencial. O curso também trata de estruturar e administrar um laboratório. É pensada para médicas e médicos veterinários interessados em laboratório clínico.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Patologia Clínica; pós-graduação em patologia clínica veterinária (o catálogo não traz "veterinária"; ela entra no corpo, como pede a F1).
- Área: patologia clínica veterinária; laboratório clínico veterinário; análises clínicas veterinárias (variação de corpo, F1 68615-K3); médica e médico veterinário.
- Modalidade: pós-graduação semipresencial, com teoria online e módulos presenciais de prática.
- Conceitos do curso: fase pré-analítica, analítica e pós-analítica; correlação clínico-laboratorial; elaboração de laudos; bioquímica clínica, função renal e urinálise; hemostasia; eletrólitos e hemogasometria; distúrbios endócrinos; exame coproparasitológico; líquidos cavitários e líquor; testes imunológicos e PCR; microbiologia; controle de qualidade e biossegurança no laboratório clínico veterinário; estrutura e administração de um laboratório.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (F1, seções 4 e 8.1): citologia e citopatologia, leitura de lâminas (são de 333; a ponte entre as duas é só a pergunta do FAQ); hematologia e hemograma (são de 68608, onda 1); mielograma (de nenhuma das duas); histopatologia, anatomia patológica e necropsia; EAD; título de especialista; "referência nacional" e qualquer frase de reconhecimento da ficha.

**descricao_schema** (269 caracteres, limite 300):

> Pós-graduação em Patologia Clínica da Faculdade Ufape, semipresencial. O laboratório clínico veterinário do pré-analítico ao laudo: correlação clínico-laboratorial, controle de qualidade, biossegurança, prática presencial e como estruturar e administrar um laboratório.

### 4.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação em Patologia Clínica da Faculdade Ufape, semipresencial. O laboratório clínico veterinário do pré-analítico ao laudo: correlação clínico-laboratorial, controle de qualidade, biossegurança, prática presencial e como estruturar e administrar um laboratório.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "patologia clínica veterinária" },
        { "@type": "Thing", "name": "laboratório clínico veterinário" },
        { "@type": "Thing", "name": "correlação clínico-laboratorial" },
        { "@type": "Thing", "name": "controle de qualidade em laboratório clínico" }
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
          "name": "Serve para quem é clínico ou só para quem trabalha em laboratório?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O foco é o laboratório clínico, e a correlação clínico-laboratorial atravessa o curso: do pedido do exame à leitura do laudo."
          }
        },
        {
          "@type": "Question",
          "name": "Patologia clínica ou citopatologia: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório. A Pós-graduação em Citopatologia Veterinária é centrada na leitura de lâminas: células e tecidos ao microscópio, com discussão de casos. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Tem prática de verdade ou é tudo online?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A teoria é online e há módulos presenciais de prática: automação e prática de hemograma, bioquímica e urina, mielograma, coleta e confecção de lâminas e microbiologia. Essas aulas não são transmitidas."
          }
        },
        {
          "@type": "Question",
          "name": "O curso ensina a montar e administrar um laboratório?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Estruturar e administrar um laboratório está no objetivo do curso, junto com controle de qualidade, biossegurança e as boas práticas de laboratório em análises clínicas."
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
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados."
          }
        }
      ]
    }
  ]
}
```

Notas de 68615: o FAQ visível leva o nome "Pós-graduação em Citopatologia Veterinária" como link para a página de 333; na marcação o texto fica sem o link, e o link vai no HTML. O endereço de rua e o CEP de `location` ficam fora da marcação até a OU13 (a ficha traz CEP diferente do das outras páginas de São Paulo). A frase de reembolso e o aviso de passagem e hotel dependem da confirmação do qa e da secretaria (a F3 os marcou [CONFIRMAR]); se saírem da página, saem daqui no mesmo dia.

---

## 5. Seção 333: Pós-graduação em Citopatologia Veterinária

Palavra principal (F1): pós-graduação em citopatologia veterinária. Vocabulário: leitura de lâminas (F1, seção 4).

### 5.1 Campos de SEO

**titulo_seo** (50 caracteres, limite 60):

> Pós-graduação em Citopatologia Veterinária | Ufape

**descricao_seo** (143 caracteres, limite 155):

> Pós-graduação em citopatologia veterinária semipresencial: da coleta e da coloração à leitura de lâminas e à discussão de casos ao microscópio.

**resposta_citavel** (46 palavras, faixa de 40 a 60):

> A pós-graduação em citopatologia veterinária da Faculdade Ufape é um curso semipresencial centrado na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema, com módulos presenciais de prática. É pensada para médicas e médicos veterinários interessados em citopatologia.

**entidades:**

- Instituição: Faculdade Ufape (Ufape).
- Curso: Pós-graduação em Citopatologia Veterinária (o catálogo traz "Pós Graduação"; o nome padrão da linha é o que vai à página).
- Área: citopatologia veterinária; citologia veterinária; citodiagnóstico (F1 333-K6, só como variação de corpo); médica e médico veterinário.
- Modalidade: pós-graduação semipresencial, com teoria online e módulos presenciais de prática.
- Conceitos do curso: leitura de lâminas; discussão de casos; manejo de materiais biológicos, coleta, armazenamento e transporte de amostras; técnicas de coloração e microscopia; citologia básica e critérios de malignidade; processos inflamatórios e infecciosos; derrames cavitários e líquidos biológicos; neoplasias de células redondas, glandulares e mesenquimais; citologia esplênica e linfoma; imunocitopatologia, automação citopatológica e citoinclusão.
- Onde nomear: hero, sobre, para_quem, matriz (dado) e faq.
- Não nomear como entidade (F1, seções 4 e 9.1): patologia clínica, análises clínicas e laboratório clínico (são de 68615; a ponte é só a pergunta do FAQ); hematologia, hemograma e leucemias como curso (68608); mielograma (de nenhuma das duas); histopatologia, anatomia patológica e necropsia; "coordenação" e nome de coordenador (OU12); EAD; título de especialista; frases de superlativo da ficha.

**descricao_schema** (242 caracteres, limite 300):

> Pós-graduação semipresencial em Citopatologia Veterinária da Faculdade Ufape. Citopatologia centrada na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema, com módulos presenciais de prática.

### 5.2 JSON-LD (Course com CourseInstance e Offer, mais FAQPage)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "{{catalogo.nome}}",
      "description": "Pós-graduação semipresencial em Citopatologia Veterinária da Faculdade Ufape. Citopatologia centrada na leitura de lâminas: da coleta e da coloração à discussão de casos ao microscópio, sistema por sistema, com módulos presenciais de prática.",
      "url": "{{pagina.url_canonica}}",
      "inLanguage": "pt-BR",
      "provider": {
        "@type": "EducationalOrganization",
        "name": "Faculdade UFAPE",
        "url": "https://faculdade.ufape.com.br"
      },
      "about": [
        { "@type": "Thing", "name": "citopatologia veterinária" },
        { "@type": "Thing", "name": "leitura de lâminas" },
        { "@type": "Thing", "name": "citologia veterinária" },
        { "@type": "Thing", "name": "microscopia" }
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
          "name": "Citopatologia ou patologia clínica: qual eu faço?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Pós-graduação em Patologia Clínica é centrada no laboratório clínico, do pré-analítico ao laudo, com a citologia entre os exames do laboratório. A Pós-graduação em Citopatologia Veterinária é centrada na leitura de lâminas: células e tecidos ao microscópio, com discussão de casos. A escolha depende do trabalho que você quer fazer na rotina."
          }
        },
        {
          "@type": "Question",
          "name": "Vou treinar leitura de lâmina de verdade?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. O cronograma tem módulos presenciais de leitura de lâminas de citopatologia e discussão de casos. Outros módulos presenciais trabalham o manejo do material, a citologia esplênica e o linfoma e o mielograma."
          }
        },
        {
          "@type": "Question",
          "name": "Preciso já trabalhar em laboratório para acompanhar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "O público da turma são médicas e médicos veterinários. O curso abre com o manejo do material, a coloração e a microscopia, e passa pela citologia básica antes de entrar nos sistemas."
          }
        },
        {
          "@type": "Question",
          "name": "Vou ter de largar a rotina?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A teoria é online e o presencial fica nos módulos de prática, com as datas publicadas no cronograma antes de começar. Dá para planejar a agenda da clínica com antecedência."
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
            "text": "A turma só começa quando atinge o número mínimo de alunos. Por isso, a orientação é comprar passagem e hotel só depois de a turma ser confirmada. Se a turma não for confirmada, os valores de inscrição pagos podem ser reembolsados."
          }
        }
      ]
    }
  ]
}
```

Notas de 333: sem `instructor`, sem `Person` e sem coordenação (OU12). Sem pergunta sobre entrar depois do início (bloqueada até OU3). A data de início que a chave devolve é a do módulo 1 presencial, que cai em Sábado de Aleluia e Páscoa (OU17): se a Ufape mudar a data, só o dado muda, a marcação não.

---

## 6. Checagens

### 6.1 Contagens (limite usado por campo)

| Turma | titulo_seo (limite 60) | descricao_seo (limite 155) | resposta_citavel (40 a 60 palavras) | descricao_schema (limite 300) |
|---|---|---|---|---|
| 657 | 48 | 147 | 54 | 260 |
| 341 | 48 | 152 | 53 | 231 |
| 289 | 48 | 145 | 52 | 244 |
| 68615 | 60 | 136 | 52 | 269 |
| 333 | 50 | 143 | 46 | 242 |

Contagem manual, a conferir pelo validador. Só o título de 68615 está no limite exato (reserva de 42 caracteres na seção 4.1). Contagens de 657 e 68615 feitas à mão pelo qa: recontar por script.

### 6.2 Unicidade e canibalização (auditorias/03-busca.md)

- Títulos e descrições das 5 turmas são diferentes entre si. O título de 289 é igual ao que a turma 68605 (Cardiologia, São Paulo) teria no mesmo padrão. O catálogo marca 68605 como "verificar (turma já iniciada e com venda)": a página dela está no ar e vende, então as duas páginas disputam a consulta "pós-graduação em cardiologia veterinária". Chamado proposto: com a CP1 aprovada, a cidade entra no título das duas; sem a CP1, a página de 68605 sai de venda depois do 3º módulo (decisão 18) e recebe 301 para a próxima turma de Cardiologia de São Paulo ou para a página do curso [CONFIRMAR com o time do site].
- 68615 x 333: nenhum campo de SEO de uma usa a palavra principal da outra (itens 5 e 6 da seção 0 e listas "Não nomear" acima). A pergunta-ponte do FAQ é a única ligação, com a âncora cruzada da F1 (68615 liga a 333 por "Pós-graduação em Citopatologia Veterinária"; 333 liga a 68615 por "Pós-graduação em Patologia Clínica").
- 657: o termo genérico "pós-graduação em anestesiologia veterinária" é da página de 68609 e "locorregional" é da de 359: nenhum campo de 657 usa o genérico sozinho nem "locorregional" fora do conteúdo do módulo.
- 289: o termo "ecocardiografia" é da página de 698. Nenhum campo de SEO de 289 o usa; "ecocardiograma" aparece só como conteúdo da prática.

### 6.3 Checagem de extração (skill visibilidade-em-ia)

| Item | 657 | 341 | 289 | 68615 | 333 |
|---|---|---|---|---|---|
| Primeira frase da `resposta_citavel` diz o que é o curso | sim | sim | sim | sim | sim |
| Bloco de 40 a 60 palavras que faz sentido sozinho | sim | sim | sim | sim | sim |
| FAQ com perguntas reais (hipóteses da persona, F3) | sim | sim | sim | sim | sim |
| Marcação estruturada (Course, CourseInstance, Offer, FAQPage) | sim | sim, `offers` só com dado limpo (OU10) | sim | sim | sim |
| Coordenador ou docente identificado | pelo dado (`docentes`), fora da marcação | idem | idem | idem | só depois da OU12 |
| Data de atualização visível | [CONFIRMAR na plataforma] | idem | idem | idem | idem |
| Conteúdo principal sem depender de JavaScript | [CONFIRMAR com o time do site] | idem | idem | idem | idem |
| Tabela de comparação quando a pergunta compara | no guia A1 (pergunta 657-Q2) | no guia de 341 (341-Q4) | no guia A2 (289-Q3) | no guia A11 (68615-Q2 e Q3) | no guia A11 (333-Q3) |

Nenhum resultado de assistente de IA foi registrado: as 40 perguntas da F1 seguem "conferir manualmente", com o roteiro da skill (de 3 a 5 rodadas por assistente, taxa registrada).

### 6.4 Conformidade educacional (auditorias/conformidade-educacional.md, itens que tocam o SEO)

| Item | Situação |
|---|---|
| Nome, modalidade e dados batem com o catálogo | Sim: nada de dado digitado no texto; a marcação usa chaves do catálogo |
| Status "aberto" nas 5 | Sim (catálogo, seção 2) |
| Pós lato sensu sem "reconhecida pelo MEC" e sem nota MEC | Sim: nenhum "MEC", "certificado" ou "reconhecida" em nenhum campo; sem `educationalCredentialAwarded` |
| Sem promessa de emprego, salário, aprovação ou resultado clínico | Sim |
| Superlativos | Nenhum ("excelência", "de ponta", "referência nacional" e "oportunidade única" ficam fora) |
| Bolsa, desconto e promoção | Nenhum (341 sem promoção) |
| Urgência | Nenhuma; a regra do 3º módulo é dado da turma (OU14) e não entra em campo de SEO |
| Preço | Só pela chave `catalogo.preco_total` na marcação; nenhum valor no texto |
| Nenhum dado pessoal; nenhum docente nomeado | Sim |
| Sem travessão nem meia-risca | Conferido na escrita; a busca final é do orquestrador |

---

## 7. Conferência da marcação com o catálogo (só para o qa; não é texto de página)

Valor que cada chave deve devolver, segundo contexto/catalogo-de-cursos.md, seção 2. A plataforma preenche; qualquer divergência é erro de dado, não de marcação.

| Chave | 657 | 341 | 289 | 68615 | 333 |
|---|---|---|---|---|---|
| `catalogo.nome` (nome padrão da linha) | Pós-graduação em Anestesiologia Avançada | Pós-graduação em Medicina Interna Equina (catálogo: "Pós Graduação") | Pós-graduação em Cardiologia Veterinária | Pós-graduação em Patologia Clínica | Pós-graduação em Citopatologia Veterinária (catálogo: "Pós Graduação") |
| `catalogo.turma` | II | I | II | VII | I |
| `catalogo.modalidade` | Semipresencial | Semipresencial | Semi presencial (catálogo) | Semipresencial | Semipresencial |
| `catalogo.inicio_iso` (planilha) | 2027-03-13 | 2027-03-20 | 2027-03-20 | 2027-03-20 | 2027-03-27 |
| `catalogo.carga_horaria_h` | 360 | 500 | 500 | 500 | 500 |
| `catalogo.local_cidade` | São Paulo | São Paulo | Goiânia | São Paulo | São Paulo |
| `catalogo.preco_total` (valor do total, sem parcelas nem matrícula) | 48400.00 | 43500.00 | 35400.00 | 35400.00 | 28050.00 |
| `local.uf` | SP | SP | GO | SP | SP |

`local.uf`: o catálogo não traz a sigla; as siglas vêm de contexto/ufape-geral.md ("São Paulo, SP" e "Goiânia, GO") [CONFIRMAR NO CATÁLOGO]. `pagina.url_canonica`: o catálogo e a plataforma ainda não trazem a URL final das páginas novas; as fichas só têm a URL das páginas atuais [CONFIRMAR]. `catalogo.modalidade`: o valor vira o termo da marcação por uma regra da plataforma (por exemplo, semipresencial para "blended") [SUPOSIÇÃO]. `courseWorkload` no formato de duração ISO (PT360H) [SUPOSIÇÃO: formato escolhido por este agente, em conformidade com o schema.org].

---

## 8. Pedidos e observações para o qa e para a próxima etapa

1. **Para a F3 e o qa (observação, sem editar o arquivo alheio):** na página de 289 a F3 escreve "ecocardiografia com Doppler" no `sobre`. A F1 só autoriza "ecocardiograma" como conteúdo, sem tomar a palavra de 698. Este arquivo evita "ecocardiografia" em todo campo de SEO; cabe ao qa decidir se a ocorrência no `sobre` é conteúdo aceitável.
2. **Para a F3 e o qa:** a F3 usa "de cães e gatos" no hero e no `sobre` de 289 e marca a pendência [CONFIRMAR NO CATÁLOGO]; aqui o termo ficou fora. Se a Ufape confirmar, uma versão 2 deste arquivo pode incluí-lo em `resposta_citavel` (289-K3).
3. **Aplicação da marcação (time do site, depois da aprovação):** testar cada página com o validador de dados estruturados antes de publicar; publicar a marcação só junto com a página (OB1 do plano e da F3, prazo 03/12/2026); conferir que o FAQ marcado é o mesmo que está visível.
4. **Descrição e título são rascunho de SEO, não promessa:** nada aqui altera mídia, anúncio, CRM ou site.

**Próximo agente:** pela cadeia do plano (workflow /pagina-de-curso), a F5 é o otimizador-de-cta (formulário e CTA final, 17/11), depois o qa-de-marketing (19/11). O briefing de texto das páginas continua com o editor-de-conteudo, que deve receber este arquivo junto da F3 para revisar a voz antes da aprovação humana.

---

## Fatos (com fonte)

- Nome, local, modalidade, carga horária, turma, início, preço total e status "aberto" das 5 turmas: contexto/catalogo-de-cursos.md, seção 2 (valores só nas chaves da seção 7; nenhum no texto).
- Limites de caracteres e palavras, ausência de número no texto da IA, `descricao_schema` e regra de que a plataforma monta o JSON-LD com os fatos do banco: templates/pagina-da-turma.md.
- Palavra principal por turma, vocabulário próprio de 68615 e de 333, termos que não são de cada página, âncora cruzada, negativas da Busca paga e CP1: F1 (saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-27-onda2.md, seções 1, 3 a 9 e 12).
- Conteúdo do curso (módulos, prática presencial, teoria online, temas por sistema, objetivos de 68615), perguntas e respostas do FAQ, travas aplicadas e pendências: F3 (saidas/08-conversao/landing-page-pos-2026-10-27-onda2.md) e as fichas em contexto/cursos/pos/.
- 657: aulas práticas e presenciais não transmitidas; módulos presenciais de bloqueios locorregionais, hemodinâmica e ventilação, reanimação com avaliação viscoelástica e TIVA e TCI; público-alvo "exclusiva para médicos veterinários anestesistas já atuantes" (não repetido): ficha de 657.
- Nome padrão "Pós-graduação em <área>", sem frase de certificação, turma mínima, entrada até o 3º módulo (decisão 18) e prova de bolsa fora da onda (decisão 14): contexto/pos-graduacao.md e docs/execucao-2026-10-26.md.
- Nome da instituição ("Faculdade UFAPE") e site (faculdade.ufape.com.br); siglas SP e GO: contexto/ufape-geral.md.
- Estrutura e passos de Course, CourseInstance, FAQPage e a regra de que o FAQ marcado é o visível: .claude/skills/schema-de-curso/SKILL.md. Regras de extração e de não inventar resultado de IA: .claude/skills/visibilidade-em-ia/SKILL.md.
- Auditoria do departamento: auditorias/03-busca.md. Conformidade: auditorias/conformidade-educacional.md.
- Cadeia e datas (F4 em 16/11, F5 em 17/11, qa em 19/11, publicação até 03/12): plano do CMO, seções 7.2 e 10.

## [SUPOSIÇÃO]

- A marca " | Ufape" no fim dos 5 títulos, para padrão único (sem fonte; escolha do agente).
- "Veterinária" no título e na resposta citável de 657 e de 68615 (a F1 pede a palavra no corpo; o catálogo não a traz no nome).
- "É pensada para quem quer aprofundar a decisão crítica em pacientes de risco" em 657: descreve motivo, não requisito; escrito para não antecipar a resposta da U10.
- "É pensada para médicas e médicos veterinários interessados em <área>" em 341, 289, 68615 e 333: o público-alvo das fichas é "Médicos Veterinários" e o texto herda a forma da F3, como interesse e nunca como pré-requisito.
- "Clínica do cavalo" e "médica e médico veterinário de equinos" em 341 (variação de corpo da F1, ela mesma [SUPOSIÇÃO]).
- "Análises clínicas veterinárias" e "citodiagnóstico" como entidades de variação de corpo (F1: 68615-K3 e 333-K6, ambos [SUPOSIÇÃO] de que o candidato digita assim).
- Os valores de `about` e a escolha de `EducationalOrganization` como `provider`, de `courseWorkload` em duração ISO e de `courseMode` por regra da plataforma.
- Contagens de caracteres e palavras feitas à mão; hífen conta como parte da palavra.
- Que a marcação sem a frase do guia em 289 é a versão correta até a publicação do guia A2.
- Que o validador do template ignora "um" e "uma" como artigo (mesma suposição da F3).

## [CONFIRMAR]

- **CP1:** se a cidade pode entrar em `titulo_seo` e `resposta_citavel` por variável do dado (pesa em 289; sem a aprovação, a cauda de Goiânia depende do dado, do JSON-LD e do guia).
- **U10:** pré-requisito de 657; até a resposta, `resposta_citavel` sem "para quem" de entrada e sem `audience` nem `coursePrerequisites`.
- **OU3:** reposição de módulo perdido (333 sem pergunta ou campo de SEO sobre entrar depois do início).
- **OU10 e OU11:** promoção de 341 (campo de preço limpo antes de `offers`) e segundo local e formato do módulo 3 (nenhum local de prática na marcação).
- **OU12:** coordenação e corpo docente de 333 (sem `instructor`, sem "coordenação").
- **OU13:** CEP de 68615 (sem `streetAddress` nem `postalCode` na marcação até a resposta).
- **OU14:** se a regra do 3º módulo entra como item de dado no FAQ e na marcação.
- **OU17:** datas do módulo inicial de 333 e do módulo 3 de 341 (a chave `catalogo.inicio_iso` devolve o que a planilha traz).
- **[CONFIRMAR NO CATÁLOGO]:** se 289 pode ser descrita como "de cães e gatos"; sigla de UF (`local.uf`); endereço de rua de Goiânia; URL canônica das 5 páginas; slug de curso e de turma (F3).
- **Certificação:** texto oficial da regulação; até lá nenhum campo de SEO nem a marcação citam certificação.
- **Guia A2 (289):** publicado, com link, antes de a frase do guia entrar na resposta do FAQ e na marcação.
- **Reembolso:** redação final por turma (341 sem frase por texto truncado) e se vale para 68615; a marcação segue a página.
- **Prova de recuperação de 657 cobrada separadamente:** valor ou regra, para o preço da marcação mostrar a condição completa (OB1 da F3).
- **Revisão docente:** conferência técnica das respostas citáveis e das entidades por um docente de cada área antes da publicação.
- **Plataforma e time do site:** se a data de atualização fica visível, se o conteúdo principal aparece sem JavaScript e qual o formato aceito para `courseMode`.
- **Checagem em assistentes:** rodar as 40 perguntas da F1 de 3 a 5 vezes por assistente e registrar a taxa; sem isso não há nota de visibilidade.
