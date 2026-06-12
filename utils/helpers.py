"""
Funções auxiliares e utilitárias.
"""

import locale
from typing import Union


def setup_locale():
    """Configura locale para português do Brasil"""
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except:
        try:
            locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        except:
            pass


def format_number_br(number: Union[int, float]) -> str:
    """
    Formata número com separador de milhar brasileiro.

    Args:
        number: Número a ser formatado

    Returns:
        String formatada (ex: 1.234.567)
    """
    return f"{int(number):,}".replace(",", ".")
