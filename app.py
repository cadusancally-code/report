import streamlit as st
from utils import load_data, get_labels
from export import export_excel, export_png, export_ppt

st.set_page_config(layout="wide")

URL = "https://docs.google.com/spreadsheets/d/1Mb50lQlW5ygqYhfY8RcMnjakxTa2zF-Yp6QID4pmJ80/export?format=csv&gid=901404078"

df = load_data(URL)

# Idioma
lang = st.sidebar.selectbox("Idioma", ["PT", "EN", "ZH"])
labels = get_labels(lang)

# Filtros
st.sidebar.title(labels["filtros"])

equipes = st.sidebar.multiselect(
    "Equipe",
    df['equipe'].dropna().unique(),
    default=df['equipe'].dropna().unique()
)

periodo = st.sidebar.selectbox(
    labels["periodo"],
    ["Dia", "Semana", "Mês"]
)

df = df[df['equipe'].isin(equipes)]

# Agrupamento
if periodo == "Dia":
    grupo = df.groupby('data').sum(numeric_only=True)
elif periodo == "Semana":
    grupo = df.groupby('semana').sum(numeric_only=True)
else:
    grupo = df.groupby('mes').sum(numeric_only=True)

# KPIs
total_r = df['recebidas'].sum()
total_t = df['tratadas'].sum()

sla = (total_t / total_r * 100) if total_r > 0 else 0
backlog = total_r - total_t

c1, c2, c3, c4 = st.columns(4)

c1.metric(labels["recebidas"], int(total_r))
c2.metric(labels["tratadas"], int(total_t))
c3.metric(labels["sla"], f"{sla:.2f}%")
c4.metric("Backlog", int(backlog))

# Gráfico
st.subheader("Evolução")
st.line_chart(grupo[['recebidas', 'tratadas']])

# Tabela
st.subheader("Dados")
st.dataframe(df)

# Exportações
st.subheader("Exportar")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Excel"):
        file = export_excel(df)
        with open(file, "rb") as f:
            st.download_button("Download Excel", f, file_name=file)

with col2:
    if st.button("PNG"):
        file = export_png(df)
        with open(file, "rb") as f:
            st.download_button("Download PNG", f, file_name=file)

with col3:
    if st.button("PPT"):
        file = export_ppt(df)
        with open(file, "rb") as f:
            st.download_button("Download PPT", f, file_name=file)