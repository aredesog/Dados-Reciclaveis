# ♻️ Dashboard de Reciclagem no Brasil (2005-2025)

Aplicação interativa para análise de dados sobre reciclagem e gestão de resíduos no Brasil nas últimas duas décadas.

## 📊 Sobre o Projeto

Este projeto fornece uma análise abrangente dos dados de reciclagem no Brasil, divididos por:
- **5 Regiões**: Norte, Nordeste, Centro-Oeste, Sudeste e Sul
- **8 Tipos de Materiais**: Plástico, Papel/Papelão, Vidro, Metal, Orgânico, Eletrônico, Têxtil e Madeira
- **21 Anos de Dados**: De 2005 a 2025
- **Mais de 3.200 registros** com informações detalhadas

## 🎯 Funcionalidades

### Dashboard Interativo
- 📈 **Métricas Principais**: Taxa média de reciclagem, volume reciclado, CO2 evitado e economia gerada
- 🗺️ **Análise Regional**: Comparação entre as diferentes regiões do Brasil
- 📊 **Visualizações Dinâmicas**: Gráficos interativos com Plotly
- 🔍 **Filtros Avançados**: Por ano, região, material, nível de infraestrutura e coleta seletiva
- 💾 **Exportação de Dados**: Download dos dados filtrados em CSV

### Análises Incluídas
- Evolução temporal da taxa de reciclagem
- Top materiais mais reciclados
- Distribuição dos destinos de rejeitos
- Impacto da coleta seletiva
- Economia gerada por material
- CO2 evitado ao longo do tempo
- Comparação por nível de infraestrutura

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe este repositório**

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### Gerando os Dados

Execute o script para gerar os dados de reciclagem:
```bash
python gerar_dados_reciclagem.py
```

Isso criará o arquivo `dados_reciclagem_brasil_2005_2025.csv` com mais de 3.200 registros.

### Executando o Dashboard

Inicie a aplicação Streamlit:
```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no seu navegador em `http://localhost:8501`

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
| `residuo_gerado_ton` | Quantidade de resíduo gerado em toneladas |
| `quantidade_reciclada_ton` | Quantidade reciclada em toneladas |
| `rejeito_ton` | Quantidade não reciclada em toneladas |
| `taxa_reciclagem_pct` | Taxa de reciclagem em percentual |
| `destino_rejeito` | Destino do rejeito não reciclado |
| `economia_gerada_brl` | Economia gerada pela reciclagem em Reais (R$) |
| `co2_evitado_kg` | CO2 evitado pela reciclagem em kg |
| `coleta_seletiva` | Indica se há programa de coleta seletiva (Sim/Não) |

## 📈 Principais Insights

### Por Região
- **Sul e Sudeste**: Melhores taxas de reciclagem (~56-58%)
- **Centro-Oeste e Nordeste**: Taxas médias (~47%)
- **Norte**: Maior potencial de crescimento (~35%)

### Por Material
- **Metal**: Maior taxa de reciclagem (~70%)
- **Papel/Papelão**: Segunda maior taxa (~65%)
- **Plástico**: Necessita maior atenção (~15%)

### Tendências
- Crescimento médio de 4% ao ano na taxa de reciclagem
- Aumento na implementação de coleta seletiva
- Redução no uso de lixões e aterros controlados

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Framework para dashboard interativo
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas
- **NumPy**: Computação numérica

## 📝 Notas

- Os dados são sintéticos, gerados para fins educacionais e de demonstração
- As tendências e proporções são baseadas em estudos reais sobre reciclagem no Brasil
- O projeto pode ser expandido para incluir dados por estado específico

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Este projeto é parte do estudo sobre análise de dados ambientais.

## 📄 Licença

Este projeto é de uso educacional e demonstrativo.

---

**Desenvolvido para análise de dados de reciclagem no Brasil** 🇧🇷 ♻️
