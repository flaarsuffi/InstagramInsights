# Experience Design — Instagram Insights

## 🎯 Fluxo de Uso

### Etapa 1: Autorização (Uma única vez)

```
Usuário (você)
    ↓
Clica em link de autorização (enviado pra amiga)
    ↓
Amiga faz login no Instagram
    ↓
Aprova acesso aos dados
    ↓
Redirecionado com sucesso
    ↓
Pronto! Dados liberados pra análise
```

**Experiência:**
- Link gerado automaticamente no seu script
- Amiga clica, aprova em 30 segundos
- Sem necessidade de guardar senhas
- Uma única vez (reusa o token)

---

### Etapa 2: Análise (Automática, você roda)

```
Você roda: python analyze_instagram.py
    ↓
Script puxa TODOS os posts da página dela
    ↓
IA processa dados (impressões, reach, demographics, etc)
    ↓
Gera análises por nicho
    ↓
Calcula segmentações
    ↓
Monta recomendações
    ↓
Gera PDF + HTML
    ↓
Pronto! Envia pra amiga
```

**Duração:** ~5 minutos (depende do volume)
**Output:** 2 arquivos
- `instagram_insights_[data].pdf` (bonito, compartilhável, imprimível)
- `instagram_insights_[data].html` (interativo, exploração de dados)

---

### Etapa 3: Consumo (Amiga vê os resultados)

**Opção A — PDF (Estático)**
```
Abre arquivo PDF
    ↓
Vê summary executivo (números chave)
    ↓
Explora cada seção
    ↓
Lê recomendações
    ↓
Salva ou imprime
```

**Opção B — HTML (Interativo)**
```
Abre arquivo HTML no navegador
    ↓
Vê mesmos dados que PDF
    ↓
MAS consegue:
  - Clica em um gráfico, ele expande
  - Filtra dados por período
  - Hovers mostram valores exatos
  - Compartilha link se salvar em server (futuro)
```

---

## 🖱️ Interações no HTML

### 1. Navegação entre Seções

```
┌─ MENU LATERAL (ou Navbar) ─────────────────────┐
│ □ Dashboard                                    │
│ □ Performance por Nicho                        │
│ □ Segmentação de Público                       │
│ □ Tipos de Conteúdo                           │
│ □ Análise de Testes                           │
│ □ Recomendações                               │
└──────────────────────────────────────────────────┘

Comportamento:
- Clica em uma seção → scroll suave pra ela
- Seção ativa fica highlighted (Laranja)
- Mobile: Menu colapsável (hamburger)
```

---

### 2. Gráficos Interativos

**Performance por Nicho (Bar Chart)**
```
Hover sobre uma barra:
  └─ Mostra:
     - Nome do nicho
     - Número exato de impressões
     - Percentual do total
     - Cor muda (mais vibrante)

Clique (opcional):
  └─ Expande a visualização só daquele nicho
```

**Segmentação de Público (Pie Charts)**
```
Hover sobre um slice:
  └─ Mostra:
     - Local (SP, RJ, etc)
     - Percentual
     - Número absoluto de pessoas

Clique:
  └─ Mostra tabela detalhada com demographics
     (idade, gênero, se disponível)
```

---

### 3. Tabela de Testes

```
Hover sobre uma linha:
  └─ Linha fica destacada (fundo cinza)

Clique em "ℹ️ Ver Detalhes":
  └─ Abre modal/drawer com:
     - Screenshot do post (se tiver)
     - Descrição completa do teste
     - Análise detalhada
     - Data do post

Ordenação:
  - Clica no header da coluna → ordena ascendente
  - Clica de novo → descendente
  - Usa filtros simples (dropdown "Ver apenas: Top Performers")
```

---

### 4. Filtros Globais (Topo da página)

```
┌─────────────────────────────────────────────────┐
│ 📅 Período: [Últimos 30 dias ▼]                │
│ 🏷️  Mostrar: [Todos os nichos ▼]               │
│ 📊 Tipo: [Todos os tipos ▼]                    │
│ 🔄 Atualizar Dados                             │
└─────────────────────────────────────────────────┘

Comportamento:
- Muda filtro → gráficos e números se atualizam
- Botão "Atualizar Dados" → rodá análise de novo
- Sem recarregar página inteira
```

---

### 5. Exportação

```
┌─────────────────────────────────────────────────┐
│ 💾 Salvar como:                                 │
│   ┌─ PDF Novo          (regenera versão PDF)   │
│   ├─ CSV (Tabelas)     (baixa dados brutos)    │
│   └─ Screenshot (PNG)  (captura visual)        │
└─────────────────────────────────────────────────┘
```

---

## 📱 Responsividade

### Desktop (1200px+)
```
┌─────────────────────────────────────────────────┐
│ LOGO          MENU (Sidebar)    [CONTEÚDO]     │
│               ┌──────────────┐  ┌─────────────┐ │
│               │ • Dashboard  │  │ Gráficos    │ │
│               │ • Performance│  │ em 2 colunas│ │
│               │ • Public     │  │             │ │
│               │ • Tests      │  │ Tabela full │ │
│               │ • Recs       │  │ width       │ │
│               └──────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────┘

Menu: Fixo na esquerda
Gráficos: Lado a lado
Tabelas: Full width com scroll horizontal se necessário
```

### Tablet (768px - 1200px)
```
┌──────────────────────────────────────┐
│ LOGO    MENU (Hamburger) 🍔          │
├──────────────────────────────────────┤
│                                      │
│ Gráficos em coluna única             │
│ (um em cima do outro)                │
│                                      │
│ Tabelas com scroll horizontal        │
│                                      │
└──────────────────────────────────────┘

Menu: Colapsável
Gráficos: Empilhados
Tabelas: Scrolláveis
```

### Mobile (< 768px)
```
┌──────────────────────┐
│ 🍔 LOGO              │
├──────────────────────┤
│ Cards (1 por linha)  │
│ Cards (1 por linha)  │
│ Gráficos (vertical)  │
│ Tabelas (scroll)     │
└──────────────────────┘

Menu: Drawer lateral (swipe)
Cards: Um por linha
Gráficos: Escala para mobile
Botões: Grandes (48px)
Texto: Aumentado
```

---

## ⌨️ Navegação por Teclado

- `Tab` → navega entre seções
- `Enter/Space` → expande/colapsa
- `Escape` → fecha modais/drawers
- `Ctrl/Cmd + S` → salva/exporta
- `Setas (↑↓)` → navega tabela

---

## 🎨 Estados de UI

### Normal
```
Cor: Cinza #666
Fundo: Branco #FFF
Opacity: 100%
```

### Hover
```
Cor: Laranja #FF6B35
Fundo: Cinza claro #F5F5F5
Opacity: 100%
Cursor: pointer
```

### Ativo/Selected
```
Cor: Branco #FFF
Fundo: Azul #004E89
Opacity: 100%
Underline: Laranja #FF6B35
```

### Disabled
```
Cor: Cinza claro #CCC
Opacity: 50%
Cursor: not-allowed
```

---

## 📊 Fluxo de Dados (Técnico)

```
[Dados brutos da Meta API]
          ↓
[Script Python — Processamento]
   ├─ Agrupa por nicho
   ├─ Calcula segmentação
   ├─ Gera recomendações
   └─ Exporta JSON interno
          ↓
[Gerador de Relatório]
   ├─ PDF (Matplotlib/ReportLab)
   └─ HTML (Jinja2 + Plotly + CSS)
          ↓
[Arquivos gerados]
   ├─ instagram_insights_[data].pdf
   └─ instagram_insights_[data].html
```

---

## 🔄 Ciclo Futuro (Recorrente)

Quando amiga aprovar MVP e quiser rodar periodicamente:

```
[Agendador — Cron/Schedule]
       ↓
[Roda script 1x por semana]
       ↓
[Atualiza dados]
       ↓
[Compara com semana anterior (Trending)]
       ↓
[Envia novo relatório]
       ↓
[Amiga vê mudanças/evoluções]
```

---

## 🎯 Princípios de Experiência

1. **Simplicidade:** Não sobrecarrega com opções
2. **Ação clara:** O que fazer é óbvio (recomendações destacadas)
3. **Exploração:** Gráficos convidam curiosidade, não intimidam
4. **Confiança:** Números são claros, fonte sempre visível
5. **Eficiência:** 30 segundos pra entender os principais insights
6. **Profissionalismo:** Aparência executiva (publicitária vai gostar)

---

**Data:** 12 de Setembro de 2026 | **Designer:** Sally
