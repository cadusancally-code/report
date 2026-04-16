import pandas as pd

def load_data(url):
    df = pd.read_csv(url)

    df.columns = df.columns.str.lower().str.strip()

    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    df['semana'] = df['data'].dt.isocalendar().week
    df['mes'] = df['data'].dt.month

    df['recebidas'] = pd.to_numeric(df['recebidas'], errors='coerce').fillna(0)
    df['tratadas'] = pd.to_numeric(df['tratadas'], errors='coerce').fillna(0)

    return df


def get_labels(lang):
    return {
        "PT": {
            "title": "Dashboard Operacional",
            "recebidas": "Recebidas",
            "tratadas": "Tratadas",
            "sla": "SLA",
            "filtros": "Filtros",
            "periodo": "Período"
        },
        "EN": {
            "title": "Operational Dashboard",
            "recebidas": "Received",
            "tratadas": "Processed",
            "sla": "SLA",
            "filtros": "Filters",
            "periodo": "Period"
        },
        "ZH": {
            "title": "运营仪表板",
            "recebidas": "接收",
            "tratadas": "已处理",
            "sla": "SLA",
            "filtros": "筛选",
            "periodo": "周期"
        }
    }.get(lang, {})