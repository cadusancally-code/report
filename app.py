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
st.subheader("📦 Total de Pedidos")

total_pedidos = df[col_data].count()
st.metric("Total de pedidos", total_pedidos)
st.subheader("📅 Pedidos por Data")

por_data = df.groupby(col_data).size().reset_index(name="quantidade")

st.dataframe(por_data)
st.line_chart(por_data.set_index(col_data))
col_assistente = st.sidebar.selectbox("Coluna Assistente", df.columns)
st.subheader("👤 Pedidos por Assistente")

por_assistente = df.groupby(col_assistente).size().reset_index(name="quantidade")

st.dataframe(por_assistente)
data_min = df['data'].min()
data_max = df['data'].max()

periodo = st.date_input("Filtrar período", [data_min, data_max])

df = df[(df['data'] >= pd.to_datetime(periodo[0])) & (df['data'] <= pd.to_datetime(periodo[1]))]
df = df.loc[:, ~df.columns.duplicated()]
# renomear colunas duplicadas automaticamente
cols = []
contador = {}

for col in df.columns:
    if col in contador:
        contador[col] += 1
        cols.append(f"{col}_{contador[col]}")
    else:
        contador[col] = 0
        cols.append(col)

df.columns = cols
total_pedidos = df['Código do pedido'].count()
cols = []
contador = {}

for col in df.columns:
    if col in contador:
        contador[col] += 1
        cols.append(f"{col}_{contador[col]}")
    else:
        contador[col] = 0
        cols.append(col)

df.columns = cols
# pegar todas colunas que tem "Código do pedido"
cols_pedido = [col for col in df.columns if "Código do pedido" in col]

# transformar em uma única coluna
df_pedidos = df[cols_pedido].melt(value_name="pedido").dropna()

# remover vazios
df_pedidos = df_pedidos[df_pedidos["pedido"] != ""]
total_pedidos = df_pedidos["pedido"].count()

st.metric("Total de pedidos", total_pedidos)
df_expandido = df.melt(
    id_vars=[col_data, col_assistente],
    value_vars=cols_pedido,
    value_name="pedido"
).dropna()

df_expandido = df_expandido[df_expandido["pedido"] != ""]
por_data = df_expandido.groupby(col_data).size()
st.line_chart(por_data)
por_assistente = df_expandido.groupby(col_assistente).size()
st.dataframe(por_assistente)
count()