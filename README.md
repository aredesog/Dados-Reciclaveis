# ♻️ Dashboard de Reciclagem no Brasil (2015-2025)

Aplicação web simples e interativa para análise de dados sobre reciclagem no Brasil na última década.

## 📊 Sobre o Projeto

Dashboard simplificado que apresenta dados nacionais de reciclagem no Brasil:
- **Período**: 2015 a 2025 .
- **6 Materiais Principais**: Plástico, Papel, Vidro, Metal, Orgânico e Eletrônico.
- Dados sintéticos para fins educacionais e de apresentação

## 🎯 Funcionalidades

### Dashboard Simples
- 📈 **4 Métricas Principais**: Taxa média, volume reciclado, CO2 evitado e economia gerada.
- 📊 **4 Visualizações**: Evolução temporal, taxa por material, volume e economia.
- 🔍 **Filtros**: Por ano e tipo de material.

### Análises Incluídas
- Evolução da taxa de reciclagem ao longo dos anos
- Comparação de taxa de reciclagem por material
- Volume total reciclado por tipo de material
- Economia gerada pela reciclagem de cada material


## 📁 Estrutura do Projeto

```
reciclavel/
│
├── app.py                              # Aplicação Streamlit principal
├── gerar_dados_reciclagem.py          # Script para gerar dados
├── dados_reciclagem_brasil_2005_2025.csv  # Dataset gerado
├── requirements.txt                    # Dependências Python
└── README.md                          # Este arquivo
```

## 📊 Estrutura dos Dados

O dataset contém as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| `ano` | Ano do registro (2005-2025) |
| `regiao` | Região do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste, Sul) |
| `nivel_infraestrutura` | Nível de infraestrutura de reciclagem (Alto, Médio, Baixo) |
| `material` | Tipo de material reciclável |
| `residuo_gerado_ton` | Quantidad# Aplicação Streamlit

```

## 📊 Estrutura dos Dados

O dataset reúne dados anuais sobre a reciclagem no Brasil entre 2015 e 2025, contemplando diferentes tipos de materiais recicláveis e seus impactos ambientais e econômicos.

## Colunas

| Coluna                    | Descrição 
|---------------------------|-----------
|  ano                      | Ano do registro (2015–2025). 
|  material                 | Tipo de material reciclável (6 categorias). Destaque para Metal (≈70% de taxa média de reciclagem), Papel/Papelão (≈65%) e Plástico, que apresenta maior     dificuldade de reciclagem. 
|  quantidade_reciclada_ton | Quantidade de material reciclada, em toneladas. 
|  rejeito_ton              | Quantidade de resíduos não reciclados, em toneladas. 
|  taxa_reciclagem_pct      | Taxa de reciclagem do material, em porcentagem (%). 
|  economia_gerada_brl      | Valor econômico estimado gerado pela reciclagem, em reais (R$). 
|  co2_evitado_kg           | Quantidade estimada de CO₂ evitada pela reciclagem, em quilogramas. 



## 🎯 Insights

- Metal e Papel/Papelão apresentam as maiores taxas de reciclagem
- Crescimento médio de 3% ao ano na taxa de reciclagem
- Materiais eletrônicos têm baixa taxa mas alto valor econômico
- Total de ~3 milhões de toneladas recicladas no período

---

**♻️ Desenvolvido para promover conscientização sobre reciclagem no Brasil**
