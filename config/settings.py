"""
Gerenciador de configurações da aplicação.
Carrega variáveis de ambiente e fornece valores padrão.
"""

import os
from dotenv import load_dotenv

load_dotenv('config/.env')


class Settings:
    """Configurações centralizadas da aplicação"""

    API_URL = os.getenv(
        'API_URL',
        'https://integra.odilonsantos.com/api/Bpms/tabentregaveisprod'
    )
    API_TOKEN = os.getenv('API_TOKEN', '')

    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8501))

    @staticmethod
    def is_configured():
        """Verifica se as configurações essenciais estão definidas"""
        return bool(Settings.API_TOKEN)


settings = Settings()
