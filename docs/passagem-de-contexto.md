# Passagem de contexto: squad de marketing e plataforma Ufape

Documento para retomar o projeto em qualquer sessão nova do Claude Code. Comece pedindo: "leia docs/passagem-de-contexto.md do repositório marketing-ufape e continue de onde paramos".

Última atualização: 22/10/2026

## 1. Objetivo

Criar uma squad de marketing multiagente para a Ufape e operá-la dentro da plataforma da Ufape, na área de marketing do Admin, com entrada de demandas, acompanhamento das etapas e aprovação humana antes de publicar.

## 2. Quem é a Ufape

- Faculdade UFAPE (UFAPE - CURSOS ESPECIALIZADOS LTDA), focada em **Medicina Veterinária**. Sede em São Paulo, unidade em Goiânia, turmas online e cursos em Lima.
- Linhas: **Graduação** (Medicina Veterinária em SP, Pedagogia em Goiânia), **Pós-graduação** (mais de 40 especializações veterinárias, semipresenciais, com provas de bolsa) e **Cursos Livres** (práticos presenciais, online e gravados, minicursos, grupos de estudos, aprimoramento na Ufape Clínica, simpósios).
- Público principal de pós e cursos: **médicos veterinários formados**. Graduação: vestibulandos e pais.
- Detalhes: `contexto/ufape-geral.md` e contextos por linha.

## 3. Repositórios e serviços

| Recurso | Endereço | Papel |
|---|---|---|
| Squad de marketing | github.com/ufapegrowth/marketing-ufape | 55 agentes, 23 skills, 26 workflows, auditorias, contextos, catálogo e esta passagem |
| Plataforma atual | github.com/ufapegrowth/ufapecursos | App Lovable (TanStack Start + Supabase) com site, admin e portal juntos. Vai virar o `ufape-admin` |
| Banco | Supabase externo, projeto "Ufape", ref `whqaqvedqxiloyaogddq` | Compartilhado por todos os projetos. Acesso pelo conector validado em 22/10/2026 |
| Lovable | projeto 63c0438f-e99d-4f53-9951-539ca98894d1 | Não aparece na conta do conector do Lovable; confirmar workspace |
| Planilha de turmas | Google Sheets 1qydtZX-ulj-UzMC92SeHhU6JqXdHkFB_EuJhltJt1qE | "DATAS CURSOS E PÓS": pós, cursos livres, simpósios, provas de bolsa, visão de campanhas |
| Site atual | faculdade.ufape.com.br | Será substituído pela plataforma |

## 4. O que já foi feito

1. **Squad adaptada** a partir do material "The Claude Code Marketing Team (2026)" (original em `referencia-original/`): 11 departamentos, incluindo Mídia Paga (novo), WhatsApp no relacionamento e auditoria de conformidade educacional (MEC, CDC, Conar, LGPD). Guia em `docs/guia-de-adaptacao.md`.
2. **Catálogo e contextos:** leitura das 8 abas da planilha e de 161 páginas do site. Resultado em `contexto/catalogo-de-cursos.md` (163 itens), `contexto/cursos/` (160 fichas) e contextos geral e por linha (1ª versão, com suposições marcadas). Scripts em `ferramentas/leitura-catalogo/`.
3. **Auditoria planilha x site:** `docs/auditoria-do-catalogo-2026-10-22.md`. Pontos críticos: "CERTIFICADO PELO MEC" nas páginas de pós, produto de teste publicado (Teste2026), página de Pedagogia com texto de modelo, turmas iniciadas ainda à venda, datas e links divergentes.
4. **Mapeamento da plataforma `ufapecursos`** (resumo na seção 6).

## 5. Decisões tomadas

- A squad deixa de ser um sistema à parte e passa a rodar **dentro da área de marketing do Admin**, reaproveitando a infraestrutura de IA da plataforma.
- A plataforma será dividida em **três projetos Lovable independentes**, ligados ao mesmo Supabase, sem compartilhar estilos nem componentes visuais:
  - `ufape-site`: site institucional, LPs de curso (criadas a partir do cadastro do curso) e LP da Graduação, cada uma com seu tema;
  - `ufape-admin`: painel interno, squad de marketing, webhooks e rotinas (é o `ufapecursos` atual depois da separação);
  - `ufape-portal`: área do aluno.
- **Só o `ufape-admin` cria migrations.** Site e portal só leem o schema.
- Quando dois projetos precisam da mesma lógica de negócio, ela vai para o banco (função Postgres) ou para Edge Function do Supabase, nunca copiada.
- A squad grava **conteúdo** no banco (cursos, turmas, landing_pages, peças); o site só lê. Agentes nunca mexem em código das LPs.

## 6. Mapa da plataforma atual (ufapecursos)

- **Rotas:** 109 admin, 22 site, 17 portal, 14 api (webhooks e rotinas chamadas por pg_cron).
- **Código compartilhado entre frentes (pontes a cortar):** `components/ui` (nas 3 frentes), `modules/auth`, `modules/inscricao`, `modules/crm` e `modules/financeiro` (site e admin), `lib/pg` (site e admin), `modules/ai-core` (portal usa na correção de redação), `integrations/supabase`, `modules/data-core`.
- **IA existente:** `ai_agents` + `ai_agent_prompts` (versionado) + `executarAgente` (custo, tokens, trace, RAG) + `ai_tasks` com aprovação. Falta: workflow encadeado, execução em background (hoje síncrona, 45 s), tool calling nos agentes, adapter Anthropic com mais de 4.096 tokens.
- **Marketing existente:** Estúdio, Biblioteca, Acervo, Brand Studio (`brand_contexts` com a marca Ufape), Canais e Publicações (Instagram e Facebook). Padrão de aprovação a copiar: briefings acadêmicos.
- **Catálogo no banco:** `cursos` (45) e `turmas` (52), lidos pelo site público. Faltam: ato regulatório, status de venda, provas de bolsa, grupos de estudos.
- **Bugs encontrados:** papel `gestor` exigido nas regras de marketing não existe (só super_admin aprova peças); Copiloto grava coluna inexistente `agent_prompt_id`; `brand_kbs` nunca usado na geração.
- **Design:** `docs/admin-design-system.md` e `docs/design-isolation-contract.md` no repositório da plataforma.

## 7. Próximos passos

1. Inventário arquivo por arquivo da separação (site, admin, portal) e plano de corte das pontes.
2. Criar `ufape-site` no Lovable ligado ao Supabase `whqaqvedqxiloyaogddq`, portar rotas públicas, publicar e remover do admin.
3. Repetir para `ufape-portal`.
4. No admin: corrigir os bugs da seção 6, importar os 55 agentes para `ai_agents`, criar motor de workflows com worker e a tela da squad em `/admin/marketing`, começando por `/pagina-de-curso`.
5. Completar o catálogo do CMS com os dados da auditoria.

## 8. Pendências com a Ufape

- Domínios: site (assume faculdade.ufape.com.br?), admin e portal.
- Workspace do Lovable e quem cria os projetos novos.
- Webhooks e rotinas: ficam no admin ou viram Edge Functions?
- Quem aprova peças de marketing (para corrigir o papel `gestor`).
- Chave da Anthropic cadastrada em Dados e IA > Provedores?
- Itens [PREENCHER] e [SUPOSIÇÃO] dos contextos e pontos críticos da auditoria do catálogo, em especial o texto de certificação da pós.

## 9. Regras de trabalho

- Nunca usar travessão em textos gerados. Nunca chamar a TGH de "Agência".
- O `main` do `ufapecursos` sincroniza com o Lovable: trabalhar em branch e abrir PR, sem reescrever histórico publicado.
- Não alterar o banco sem plano aprovado; migrations só pelo admin.
