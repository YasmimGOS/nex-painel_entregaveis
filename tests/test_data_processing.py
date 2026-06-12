import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv('config/.env')

AREAS_MAP = {
    'bko': 'BackOffice',
    'ctb': 'Contabilidade',
    'fcs': 'Facilities',
    'fin': 'Financeiro',
    'i3d': 'Impressão 3D',
    'mnt': 'Manutenção',
    'nex': 'Núcleo de Excelência',
    'npe': 'Núcleo de Pessoas',
    'sti': 'Tecnologia',
    'jur': 'Setor Jurídico',
    'nia': 'Núcleo de IA',
    'nti': 'Núcleo de TI',
    'sup': 'Suprimentos'
}

def fetch_data():
    api_url = os.getenv('API_URL')
    api_token = os.getenv('API_TOKEN')
    headers = {'Authorization': f'Bearer {api_token}'} if api_token else {}

    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get('data', [])
            return data
        return []
    except Exception as e:
        print(f"Erro: {e}")
        return []

def process_data(raw_data):
    if not raw_data:
        print("Nenhum dado recebido")
        return pd.DataFrame()

    df = pd.DataFrame(raw_data)
    print(f"Total de registros carregados: {len(df)}")
    print(f"Colunas: {df.columns.tolist()}")

    # Filtrar apenas em_producao = True
    if 'em_producao' in df.columns:
        print(f"\nAntes do filtro em_producao: {len(df)} registros")
        print(f"Valores únicos em 'em_producao': {df['em_producao'].unique()}")
        print(f"Contagem: {df['em_producao'].value_counts()}")

        df = df[df['em_producao'] == True].copy()
        print(f"Depois do filtro em_producao: {len(df)} registros")

    # Identificar área
    if 'nome_processo' in df.columns:
        df['sigla'] = df['nome_processo'].str.split('-').str[0].str.lower()
        df['area_nome'] = df['sigla'].map(AREAS_MAP).fillna('Outros')

        print(f"\nDistribuição por área:")
        print(df['area_nome'].value_counts())

    return df

# Teste
print("="*80)
print("TESTE DE PROCESSAMENTO DE DADOS")
print("="*80)

dados = fetch_data()
df = process_data(dados)

if not df.empty:
    print(f"\n✅ Dados processados com sucesso!")
    print(f"Total de registros finais: {len(df)}")

    # Testar uma área específica
    area_teste = 'Contabilidade'
    df_area = df[df['area_nome'] == area_teste]
    print(f"\nRegistros para '{area_teste}': {len(df_area)}")

    if not df_area.empty:
        print(f"\nProcessos únicos em {area_teste}:")
        for processo in df_area['nome_processo'].unique()[:5]:
            count = len(df_area[df_area['nome_processo'] == processo])
            print(f"  - {processo}: {count} execuções")
else:
    print("\n❌ Nenhum dado processado")