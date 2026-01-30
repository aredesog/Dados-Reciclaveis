import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Reciclagem no Brasil", page_icon="♻️", layout="wide")

# Carregar dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados_reciclagem_brasil.csv")

df = carregar_dados()

# Título
st.title("♻️ Reciclagem no Brasil (2015-2025)")

# Filtros
st.sidebar.header("🔍 Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
materiais = st.sidebar.multiselect("Material", sorted(df['material'].unique()), default=sorted(df['material'].unique()))

df_filtrado = df[(df['ano'].isin(anos)) & (df['material'].isin(materiais))]

# Métricas
if not df_filtrado.empty:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Taxa Média", f"{df_filtrado['taxa_reciclagem_pct'].mean():.1f}%")
    col2.metric("Total Reciclado", f"{df_filtrado['quantidade_reciclada_ton'].sum()/1000:.0f}k ton")
    col3.metric("CO2 Evitado", f"{df_filtrado['co2_evitado_kg'].sum()/1_000_000:.1f}M kg")
    col4.metric("Economia", f"R$ {df_filtrado['economia_gerada_brl'].sum()/1_000_000:.0f}M")
    
    st.markdown("---")
    
    # Gráficos
    col_esq, col_dir = st.columns(2)
    
    with col_esq:
        st.subheader("📈 Evolução da Taxa de Reciclagem")
        df_tempo = df_filtrado.groupby('ano')['taxa_reciclagem_pct'].mean().reset_index()
        fig1 = px.line(df_tempo, x='ano', y='taxa_reciclagem_pct', markers=True,
                       labels={'ano': 'Ano', 'taxa_reciclagem_pct': 'Taxa (%)'})
        fig1.update_traces(line_color='#2ecc71', line_width=3, marker_size=10)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col_dir:
        st.subheader("🔄 Taxa de Reciclagem por Material")
        df_material = df_filtrado.groupby('material')['taxa_reciclagem_pct'].mean().sort_values().reset_index()
        fig2 = px.bar(df_material, x='taxa_reciclagem_pct', y='material', orientation='h',
                      labels={'taxa_reciclagem_pct': 'Taxa (%)', 'material': ''},
                      color='taxa_reciclagem_pct', color_continuous_scale='Greens')
        st.plotly_chart(fig2, use_container_width=True)
    
    col_esq2, col_dir2 = st.columns(2)
    
    with col_esq2:
        st.subheader("📦 Volume Reciclado por Material")
        df_vol = df_filtrado.groupby('material')['quantidade_reciclada_ton'].sum().sort_values(ascending=False).reset_index()
        fig3 = px.bar(df_vol, x='material', y='quantidade_reciclada_ton',
                      labels={'material': 'Material', 'quantidade_reciclada_ton': 'Toneladas'},
                      color='quantidade_reciclada_ton', color_continuous_scale='Blues')
        st.plotly_chart(fig3, use_container_width=True)
    
    with col_dir2:
        st.subheader("💰 Economia Gerada por Material")
        df_econ = df_filtrado.groupby('material')['economia_gerada_brl'].sum().sort_values(ascending=False).reset_index()
        fig4 = px.bar(df_econ, x='material', y='economia_gerada_brl',
                      labels={'material': 'Material', 'economia_gerada_brl': 'Valor (R$)'},
                      color='economia_gerada_brl', color_continuous_scale='Mint')
        st.plotly_chart(fig4, use_container_width=True)
    
    # Tabela
    with st.expander("📋 Ver Dados"):
        st.dataframe(df_filtrado.style.format({
            'residuo_gerado_ton': '{:,.0f}',
            'quantidade_reciclada_ton': '{:,.0f}',
            'taxa_reciclagem_pct': '{:.1f}%',
            'economia_gerada_brl': 'R$ {:,.0f}',
            'co2_evitado_kg': '{:,.0f}'
        }), use_container_width=True)
        
        csv = df_filtrado.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Baixar CSV", csv, "dados.csv", "text/csv")
else:
    st.warning("⚠️ Sem dados para os filtros selecionados")

st.markdown("---")
st.markdown("<div style='text-align: center'>♻️ Dashboard de Reciclagem no Brasil | 2015-2025</div>", unsafe_allow_html=True)
