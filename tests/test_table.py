import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Criar dados de teste
data = {
    'nome_processo': ['Processo A', 'Processo B', 'Processo C'],
    'frequencia_disparo': ['Diária', 'Semanal', 'Mensal'],
    'horarios_disparo': ['08:00', '14:00', '18:00'],
    'tipo_fluxo': ['Tipo 1', 'Tipo 2', 'Tipo 3'],
    'data_inicio': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'data_fim': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'duracao': ['01:00:00', '02:00:00', '00:30:00'],
    'status': ['Concluído', 'Concluído', 'Falha'],
    'erros': ['Nenhum', 'Nenhum', 'Erro X']
}

df = pd.DataFrame(data)

st.title("Teste de Tabela")
st.write(f"Total de registros: {len(df)}")
st.write(f"Colunas: {df.columns.tolist()}")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=400
)