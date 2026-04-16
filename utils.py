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
    }.get(lang, {})import pandas as pd

def load_data(url):
    df = pd.read_csv(url)

    # normalizar nomes
    df.columns = df.columns.str.lower().str.strip()

    # mapear nomes reais → padrão
    rename_map = {
        'data de envio': 'data',
        'data envio': 'data',
        'date': 'data',
        'dia': 'data',

        'recebidas': 'recebidas',
        'received': 'recebidas',

        'tratadas': 'tratadas',
        'processed': 'tratadas'
    }

    df = df.rename(columns=rename_map)

    # validação
    if 'data' not in df.columns:
        raise ValueError("Coluna de data não encontrada")

    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    df['semana'] = df['data'].dt.isocalendar().week
    df['mes'] = df['data'].dt.month

    df['recebidas'] = pd.to_numeric(df['recebidas'], errors='coerce').fillna(0)
    df['tratadas'] = pd.to_numeric(df['tratadas'], errors='coerce').fillna(0)

    return import pandas as pd

def get_labels(lang):
    labels = {
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
    }

    return labels.get(lang, {})


def load_data(url):
    df = pd.read_csv(url)

    df.columns = df.columns.str.lower().str.strip()

    rename_map = {
        'data de envio': 'data',
        'data envio': 'data',
        'date': 'data',
        'dia': 'data',

        'recebidas': 'recebidas',
        'received': 'recebidas',

        'tratadas': 'tratadas',
        'processed': 'tratadas'
    }

    df = df.rename(columns=rename_map)

    if 'data' not in df.columns:
        raise ValueError("Coluna de data não encontrada")

    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    df['semana'] = df['data'].dt.isocalendar().week
    df['mes'] = df['data'].dt.month

    df['recebidas'] = pd.to_numeric(df['recebidas'], errors='coerce').fillna(0)
    df['tratadas'] = pd.to_numeric(df['tratadas'], errors='coerce').fillna(0)

    return SyntaxError em:
from utils import load_data, get_labels
from utils import load_data, get_labels
from utils import load_data, get_labels