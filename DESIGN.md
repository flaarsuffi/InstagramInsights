# Design System — Instagram Insights

## 🎨 Paleta de Cores

**Escolha:** Laranja Vibrante + Azul Profundo + Branco Limpo

```
🟠 Laranja Principal: #FF6B35 (destaque, alertas, chamada para ação)
🔵 Azul Secundário: #004E89 (fundo, estrutura, confiança)
⚪ Branco/Cinza: #F8F9FA (background, legibilidade)
```

**Uso:**
- Laranja: Cards de destaque, números chave, recomendações
- Azul: Headers, seções, tabelas
- Branco/Cinza: Fundos, espaçamento, texto secundário

---

## 📐 Layout — PDF + HTML

### Dashboard Executivo (Seção 1)

```
╔════════════════════════════════════════════════════════════════╗
║  🔷 INSTAGRAM INSIGHTS - ANÁLISE COMPLETA                      ║
║  Gerado em: 12 de Setembro de 2026                            ║
╚════════════════════════════════════════════════════════════════╝

╔─ HEADLINE PRINCIPAL ─────────────────────────────────────────╗
║ Seu Público está em: São Paulo, 18-24 anos, 65% Mulheres    ║
║ 📍 Fonte: Últimos [N] posts analisados                       ║
╚──────────────────────────────────────────────────────────────╝

┌─ CARDS — NÚMEROS CHAVE (4 em linha) ────────────────────────┐
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  │ 📊 IMPRESSÕES │  │ 👥 REACH     │  │ ⏰ MELHOR HR │  │ ⭐ TOP POST   │
│  │ 245.890      │  │ 125.430      │  │ 19h-21h      │  │ +2.5k eng.   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
│  (Laranja #FF6B35 - Bold, números grandes, destaque visual)
└────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title: `Roboto Bold 28px`, Azul #004E89
- Card Numbers: `Roboto Bold 36px`, Laranja #FF6B35
- Card Labels: `Roboto Regular 12px`, Cinza #666
- Card Background: `Branco #FFFFFF`, Sombra suave

---

### Gráfico 1: Performance por Nicho (Seção 2)

```
╔─ PERFORMANCE POR NICHO ──────────────────────────────────────╗
║ Como cada tema perform nos seus posts                        ║
╠──────────────────────────────────────────────────────────────╣
║                                                              ║
║  MARKETING    ██████████████░░░ 245 impressões/post         ║
║  DESIGN       ███████░░░░░░░░░░ 145 impressões/post         ║
║  GROWTH       █████████████░░░░ 210 impressões/post         ║
║  SOCIAL MEDIA ███████████░░░░░░ 180 impressões/post         ║
║  BRANDING     ██████░░░░░░░░░░░ 95 impressões/post          ║
║                                                              ║
╚──────────────────────────────────────────────────────────────╝

Cores do Gráfico:
- Barras: Gradiente Azul → Laranja
- Labels: Roboto 12px, Azul #004E89
- Valores: Roboto Bold 12px, Laranja #FF6B35
```

**Componentes:**
- Gráfico: Plotly (interativo em HTML, estático em PDF)
- Eixos: Roboto 11px, Cinza
- Altura: 300px, Largura: 100%

---

### Gráfico 2: Segmentação de Público (Seção 3)

```
╔─ SEGMENTAÇÃO DE PÚBLICO POR NICHO ───────────────────────────╗
║ Qual público vem de qual conteúdo                            ║
╠──────────────────────────────────────────────────────────────╣
║                                                              ║
║  MARKETING                  DESIGN                          ║
║  ┌─────────────────────┐   ┌─────────────────────┐          ║
║  │ SP: 40% 🟠          │   │ SP: 30% 🟠          │          ║
║  │ RJ: 20% 🔵          │   │ RJ: 35% 🔵          │          ║
║  │ MG: 15% ⚪          │   │ MG: 20% ⚪          │          ║
║  │ Outros: 25%         │   │ Outros: 15%         │          ║
║  └─────────────────────┘   └─────────────────────┘          ║
║                                                              ║
║  GROWTH                     SOCIAL MEDIA                    ║
║  ┌─────────────────────┐   ┌─────────────────────┐          ║
║  │ SP: 50% 🟠          │   │ SP: 45% 🟠          │          ║
║  │ RJ: 18% 🔵          │   │ RJ: 22% 🔵          │          ║
║  │ MG: 12% ⚪          │   │ MG: 18% ⚪          │          ║
║  │ Outros: 20%         │   │ Outros: 15%         │          ║
║  └─────────────────────┘   └─────────────────────┘          ║
║                                                              ║
╚──────────────────────────────────────────────────────────────╝
```

**Componentes:**
- Cards com Pizza Charts (Plotly)
- Cores: Laranja (principal), Azul (secundário)
- Layout: 2x2 grid, responsivo

---

### Tabela: Análise de Testes (Seção 5)

```
╔─ TESTES QUE VOCÊ FEZ ─────────────────────────────────────────╗
║ Comparando hashtags, textos e formatos                       ║
╠═════════════════════════════════════════════════════════════════╣
║ TESTE                              │ IMPRESSÕES │ ENG.  │ RESULT  ║
╠─────────────────────────────────────┼────────────┼───────┼─────────╣
║ #marketing #agencia                 │    500     │  50   │ ⚠️ Baixo║
║ #MarketingDigital #Growth           │    800     │  35   │ ✅ Melhor║
║ Post texto longo                    │    450     │  65   │ ✅ Melhor║
║ Post texto curto                    │    320     │  25   │ ❌ Ruim ║
║ Reels (Conteúdo)                    │   1.200    │  150  │ ✅ Top  ║
║ Carrossel (Conteúdo)                │    680     │  85   │ ✅ Bom  ║
╚═════════════════════════════════════════════════════════════════╝

Cores de Resultado:
🟢 ✅ Melhor: Fundo Laranja claro, badge verde
🟡 ⚠️ Médio: Fundo Cinza, badge amarelo
🔴 ❌ Ruim: Fundo Cinza escuro, badge vermelho
```

**Componentes:**
- Tabela: Roboto 11px
- Headers: Azul #004E89, Bold
- Striping: Alternado branco/cinza claro
- Ícones: Emoji para visual rápido

---

### Seção 6: Recomendações (Call-to-Action)

```
╔─ 🎯 RECOMENDAÇÕES PARA PRÓXIMOS POSTS ────────────────────────╗
║                                                              ║
║  ✅ Foque em REELS sobre MARKETING                          ║
║     └─ Seu público pega melhor em vídeo curto              ║
║                                                              ║
║  ✅ Melhor horário: 19h-21h (Terça/Quinta)                 ║
║     └─ Mais engajamento nesse período                      ║
║                                                              ║
║  ✅ Use hashtags genéricas > específicas                   ║
║     └─ #MarketingDigital funcionou 60% melhor             ║
║                                                              ║
║  ⚠️  Abandone textos muito curtos                          ║
║     └─ Público seu prefere explicação detalhada            ║
║                                                              ║
║  🧪 Teste CARROSSEL sobre DESIGN (próximo mês)             ║
║     └─ Seu público pede esse conteúdo (trending)           ║
║                                                              ║
╚──────────────────────────────────────────────────────────────╝

Estilo:
- Cada recomendação: Laranja #FF6B35 (ícone/borda)
- Texto principal: Roboto Bold 14px, Azul
- Explicação: Roboto Regular 12px, Cinza
```

---

## 📱 Responsividade

**PDF:** Formato A4 landscape (otimizado para impressão)
**HTML:** Adaptável mobile + desktop
- Desktop: 100% width, max-width 1200px
- Tablet: Gráficos em coluna
- Mobile: Cards empilhados, tabelas scrolláveis

---

## 🖼️ Hierarquia Visual

```
1. HEADLINE (maior, laranja, chamada)
2. Cards Números (destaque visual)
3. Gráficos (exploração de dados)
4. Tabelas (detalhamento)
5. Recomendações (call-to-action)
```

---

## 📦 Componentes Reutilizáveis

- **Card:** Branco, sombra suave, borda azul
- **Badge:** Laranja/Verde/Vermelho, ícone + texto
- **Gráfico:** Plotly (HTML interativo), Matplotlib (PDF estático)
- **Tabela:** Striping, hover effect (HTML), cores (PDF)
- **Button/Link:** Laranja #FF6B35, hover mais escuro

---

**Data:** 12 de Setembro de 2026 | **Designer:** Sally
