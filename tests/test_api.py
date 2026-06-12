import requests
import json
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv('config/.env')

api_url = os.getenv('API_URL', 'https://integra.odilonsantos.com/api/Bpms/tabentregaveisprod')
api_token = os.getenv('API_TOKEN', '')

print(f"API_URL: {api_url}")
print(f"API_TOKEN: {api_token}")
print("-" * 80)

headers = {'Authorization': f'Bearer {api_token}'} if api_token else {}

try:
    print("Fazendo requisição...")
    response = requests.get(api_url, headers=headers, timeout=15)

    print(f"\nStatus Code: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    print("-" * 80)

    if response.status_code == 200:
        json_data = response.json()
        print(f"\nTipo de resposta: {type(json_data)}")

        if isinstance(json_data, dict):
            print(f"Keys disponíveis: {list(json_data.keys())}")

            # Tentar pegar dados de diferentes chaves
            for key in ['data', 'results', 'items']:
                if key in json_data:
                    data = json_data[key]
                    print(f"\nEncontrado dados em '{key}'")
                    print(f"Total de registros: {len(data) if isinstance(data, list) else 'N/A'}")
                    if isinstance(data, list) and len(data) > 0:
                        print(f"\nPrimeiro registro:")
                        print(json.dumps(data[0], indent=2, ensure_ascii=False))

                        # Verificar estrutura
                        print(f"\nCampos do primeiro registro:")
                        for campo in data[0].keys():
                            print(f"  - {campo}: {type(data[0][campo]).__name__}")
                    break
            else:
                print("\nNenhuma chave conhecida encontrada. Estrutura completa:")
                print(json.dumps(json_data, indent=2, ensure_ascii=False)[:1000])

        elif isinstance(json_data, list):
            print(f"Total de registros (lista direta): {len(json_data)}")
            if len(json_data) > 0:
                print(f"\nPrimeiro registro:")
                print(json.dumps(json_data[0], indent=2, ensure_ascii=False))

                # Verificar estrutura
                print(f"\nCampos do primeiro registro:")
                for campo in json_data[0].keys():
                    print(f"  - {campo}: {type(json_data[0][campo]).__name__}")
    else:
        print(f"\nErro na API!")
        print(f"Response text: {response.text[:500]}")

except Exception as e:
    print(f"\nErro: {e}")
    import traceback
    traceback.print_exc()