
import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# Parâmetros
anos = range(2015, 2026)
materiais = ['Plástico', 'Papel/Papelão', 'Vidro', 'Metal', 'Orgânico', 'Eletrônico']

# Taxa base de reciclagem por material
taxa_reciclagem_material = {
    'Plástico': 0.15,
    'Papel/Papelão': 0.65,
    'Vidro': 0.45,
    'Metal': 0.70,
    'Orgânico': 0.35,
    'Eletrônico': 0.20
}

dados = []

for ano in anos:
    # Melhoria de 3% ao ano
    fator_tempo = 1 + (ano - 2015) * 0.03
    
    for material in materiais:
        # Resíduo gerado no Brasil (toneladas)
        residuo_gerado = np.random.uniform(50000, 150000)
        
        # Taxa de reciclagem
        taxa_base = taxa_reciclagem_material[material]
        taxa_reciclagem = min(taxa_base * fator_tempo * np.random.uniform(0.9, 1.1), 0.95)
        
        # Cálculos
        quantidade_reciclada = residuo_gerado * taxa_reciclagem
        rejeito = residuo_gerado - quantidade_reciclada
        
        # Valor econômico (BRL)
        valor_ton = {
            'Plástico': 2000,
            'Papel/Papelão': 500,
            'Vidro': 300,
            'Metal': 5000,
            'Orgânico': 200,
            'Eletrônico': 15000
        }
        economia_gerada = quantidade_reciclada * valor_ton[material]
        
        # CO2 evitado (kg)
        co2_ton = {
            'Plástico': 1500, 'Papel/Papelão': 900, 'Vidro': 300,
            'Metal': 1800, 'Orgânico': 500, 'Eletrônico': 2000
        }
        co2_evitado = quantidade_reciclada * co2_ton[material]
        
        dados.append({
            'ano': ano,
            'material': material,
            'residuo_gerado_ton': round(residuo_gerado, 2),
            'quantidade_reciclada_ton': round(quantidade_reciclada, 2),
            'rejeito_ton': round(rejeito, 2),
            'taxa_reciclagem_pct': round(taxa_reciclagem * 100, 2),
            'economia_gerada_brl': round(economia_gerada, 2),
            'co2_evitado_kg': round(co2_evitado, 2)
        })

# Criar DataFrame
df = pd.DataFrame(dados)

# Estatísticas
print(f"✅ Total de registros: {len(df)}")
print(f"📅 Período: {df['ano'].min()} - {df['ano'].max()}")
print(f"♻️ Taxa média de reciclagem: {df['taxa_reciclagem_pct'].mean():.2f}%")
print(f"📦 Total reciclado: {df['quantidade_reciclada_ton'].sum()/1_000_000:.2f} milhões de ton")
print(f"💰 Economia total: R$ {df['economia_gerada_brl'].sum()/1_000_000_000:.2f} bilhões")

# Salvar
df.to_csv('dados_reciclagem_brasil.csv', index=False, encoding='utf-8-sig')
print("\n✅ Arquivo 'dados_reciclagem_brasil.csv' criado!")
