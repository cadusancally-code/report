import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# =========================
# DADOS
# =========================
URL = "https://docs.google.com/spreadsheets/d/1Mb50lQlW5ygqYhfY8RcMnjakxTa2zF-Yp6QID4pmJ80/export?format=csv&gid=901404078"

df = pd.read_csv(URL)
df.columns = df.columns.str.strip()

# =========================
# CONFIGURAÇÃO
# =========================
st.sidebar.title("Configuração")

col_data = st.sidebar.selectbox("Coluna de Data", df.columns)
col_recebidas = st.sidebar.selectbox("Recebidas", df.columns)
col_tratadas = st.sidebar.selectbox("Tratadas", df.columns)

# =========================
# TRATAMENTO
# =========================
df['data'] = pd.to_datetime(df[col_data], errors='coerce')
df['recebidas'] = pd.to_numeric(df[col_recebidas], errors='coerce').fillna(0)
df['tratadas'] = pd.to_numeric(df[col_tratadas], errors='coerce').fillna(0)

# =========================
# KPI
# =========================
total_r = df['recebidas'].sum()
total_t = df['tratadas'].sum()
sla = (total_t / total_r * 100) if total_r > 0 else 0

c1, c2, c3 = st.columns(3)

c1.metric("Recebidas", int(total_r))
c2.metric("Tratadas", int(total_t))
c3.metric("SLA (%)", f"{sla:.2f}%")

# =========================
# GRÁFICO
# =========================
st.subheader("Evolução")

grafico = df.groupby('data')[['recebidas','tratadas']].sum()
st.line_chart(grafico)

# =========================
# TABELA
# =========================
st.subheader("Dados detalhados")

df_view = df[[col_data, col_recebidas, col_tratadas]]
st.dataframe(df_view)