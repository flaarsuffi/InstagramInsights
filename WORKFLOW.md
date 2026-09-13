# Workflow Automatizado — Squad Híbrida

## 🤖 Como Funciona

Cada membro da squad atualiza o board **através de comentários na issue**.

---

## 📋 Fluxo Padrão

### 1️⃣ **Pega uma Issue**
- Issue começa com label `backlog`
- Você clica em "Assign to me" ou comenta:
  ```
  /in-progress
  ```
- ✅ Label muda automaticamente para `in-progress`
- ✅ Issue move pra coluna "In Progress" no GitHub Project

### 2️⃣ **Trabalha**
- Commit codes, push, atualize conforme necessário
- Link PRs se houver código

### 3️⃣ **Termina a Issue**
- Comenta na issue:
  ```
  /done
  ```
- ✅ Label muda automaticamente para `done`
- ✅ Issue move pra coluna "Done" no GitHub Project
- ✅ GitHub comenta confirmando

---

## 🏷️ Labels Automáticos

| Label | Cor | Significado | Próximo Passo |
|-------|-----|-------------|---------------|
| `backlog` | ⚫ Cinza | Aguardando início | Comentar `/in-progress` |
| `in-progress` | 🟠 Laranja | Trabalhando agora | Comentar `/done` |
| `done` | 🟢 Verde | Concluído | Revisar próxima issue |

**Labels de Contexto** (adicionais):
- `design` — Tarefa de design (Sally)
- `dev` — Tarefa de desenvolvimento (Amelia)
- `qa` — Tarefa de QA

---

## 📌 Exemplos Reais

### Exemplo 1: Sally (Design)

```
Issue: #2 - DESIGN-02: Criar EXPERIENCE.md

Sally clica na issue e comenta:
  /in-progress

GitHub Actions:
  ✅ Remove label "backlog"
  ✅ Adiciona label "in-progress"
  ✅ Projeto move para coluna "In Progress"

(Sally trabalha...)

Quando termina, comenta:
  /done

GitHub Actions:
  ✅ Remove label "in-progress"
  ✅ Adiciona label "done"
  ✅ Projeto move para coluna "Done"
  ✅ Comenta: "✅ Issue marcada como concluída!"
```

### Exemplo 2: Amelia (Dev)

```
Issue: #4 - DEV-02: Script para puxar dados

Amelia comenta:
  /in-progress

(Depois de 3 dias de trabalho e 5 commits...)

Amelia comenta:
  /done

(Automático!)
Board atualiza.
```

---

## ✅ Checklist por Papel

### 👩‍🎨 Sally (Design)
- [ ] Pega issue de design
- [ ] Comenta `/in-progress`
- [ ] Trabalha em DESIGN.md, EXPERIENCE.md, etc
- [ ] Comenta `/done` quando pronto
- [ ] ✅ Próximo agente vê que design tá pronto

### 👩‍💻 Amelia (Dev)
- [ ] Pega issue que tem label `design` completo (done)
- [ ] Comenta `/in-progress`
- [ ] Desenvolve (commits, PRs)
- [ ] Comenta `/done` quando pronto
- [ ] ✅ QA pega e testa

### 🔍 QA
- [ ] Pega issue que tem label `dev` completo (done)
- [ ] Comenta `/in-progress`
- [ ] Testa conforme critérios de aceite
- [ ] Comenta `/done` quando validado
- [ ] ✅ Issue pronta pra deploy

---

## 🔗 Ver Status em Tempo Real

**GitHub Project:** https://github.com/flaarsuffi/InstagramInsights/projects
- Colunas automáticas: Backlog → In Progress → Done

**Sprint Board:** SPRINT.md (atualizado manualmente se quiser snapshot)

---

## 🚨 Erros Comuns

❌ **NÃO faça:**
- Esquecer de comentar `/in-progress` quando pega issue
- Comentar `/done` antes de realmente terminar
- Atualizar labels manualmente (deixa automático fazer)

✅ **FAÇA:**
- Comentar `/in-progress` quando pega
- Trabalhar normalmente
- Comentar `/done` quando termina
- Pronto!

---

## 🔄 Dependencies Entre Issues

Se uma issue depende de outra, use o link na descrição:

```
Bloqueado por: #3 (DEV-01)
Bloqueia: #4, #5 (DEV-02, DEV-03)
```

O board visual não move automaticamente (GitHub Projects não suporta), mas você consegue ver as dependências na issue.

---

## 📞 Dúvidas?

Se alguma coisa não funcionar:
1. Verifique a issue description (tem bloqueadores?)
2. Checa se comentou `/in-progress` corretamente
3. Vê GitHub Actions logs: https://github.com/flaarsuffi/InstagramInsights/actions

---

**Date:** 12 de Setembro de 2026 | **Owner:** John (PO)
