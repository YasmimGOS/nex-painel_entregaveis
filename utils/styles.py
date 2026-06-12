"""
Estilos CSS customizados para a aplicação Streamlit.
"""


def get_custom_css(colors: dict, is_dark_theme: bool) -> str:
    """
    Retorna CSS customizado baseado no tema.

    Args:
        colors: Dicionário com paleta de cores
        is_dark_theme: Se é tema escuro

    Returns:
        String com CSS
    """
    shadow = 'rgba(0,0,0,0.3)' if is_dark_theme else 'rgba(0,0,0,0.1)'

    return f"""
    <style>
    .stApp {{
        background-color: {colors['background']};
        color: {colors['text']};
    }}

    [data-testid="stMetric"] {{
        background-color: {colors['card']};
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid {colors['primary']};
        box-shadow: 0 4px 15px {shadow};
    }}

    [data-testid="stMetricValue"] {{
        color: {colors['text']};
        font-size: 2rem;
        font-weight: 700;
    }}

    [data-testid="stMetricLabel"] {{
        color: {colors['text_secondary']};
        font-weight: 600;
    }}

    div[data-testid="column"] {{
        min-width: 150px !important;
    }}

    .kpi-scroll-wrapper {{
        overflow-x: auto;
        overflow-y: hidden;
        display: flex;
        gap: 15px;
        padding: 10px 5px;
        margin-bottom: 20px;
        -webkit-overflow-scrolling: touch;
    }}

    .kpi-scroll-wrapper::-webkit-scrollbar {{
        height: 10px;
    }}

    .kpi-scroll-wrapper::-webkit-scrollbar-track {{
        background: {colors['card']};
        border-radius: 10px;
    }}

    .kpi-scroll-wrapper::-webkit-scrollbar-thumb {{
        background: {colors['primary']};
        border-radius: 10px;
    }}

    .kpi-scroll-wrapper::-webkit-scrollbar-thumb:hover {{
        background: {colors['text_secondary']};
    }}

    [data-testid="stMetric"] {{
        flex-shrink: 0;
        min-width: 140px;
        white-space: nowrap;
    }}

    .stButton>button {{
        background: {colors['card']};
        color: {colors['text']};
        border-radius: 12px;
        height: 70px;
        font-size: 15px;
        font-weight: 600;
        border: 2px solid {colors['border']};
        transition: all 0.3s ease;
    }}

    .stButton>button:hover {{
        border-color: {colors['primary']};
        color: {colors['primary']};
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(243, 140, 50, 0.3);
    }}

    .stDeployButton {{
        background-color: {colors['card']} !important;
        color: {colors['text']} !important;
    }}

    .stStatusWidget {{
        background-color: {colors['card']} !important;
    }}

    header[data-testid="stHeader"] {{
        background-color: {colors['background']} !important;
    }}

    [data-testid="stToolbar"] {{
        background-color: {colors['card']} !important;
    }}

    [data-testid="stToolbar"] button {{
        color: {colors['text']} !important;
    }}

    .stDownloadButton > button {{
        background-color: {colors['card']} !important;
        color: {colors['primary']} !important;
        border: 2px solid {colors['primary']} !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }}

    .stDownloadButton > button:hover {{
        background-color: {colors['primary']} !important;
        color: {colors['card']} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(239, 125, 30, 0.4) !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: {colors['sidebar']};
    }}

    [data-testid="stSidebar"] * {{
        color: {colors['text']};
    }}

    [data-testid="stSidebar"] .element-container {{
        margin-bottom: 0.5rem;
    }}

    .stMultiSelect > div {{
        background-color: {colors['card']} !important;
    }}

    .stMultiSelect input {{
        background-color: {colors['card']} !important;
        color: {colors['text']} !important;
    }}

    .stMultiSelect [data-baseweb="select"] > div {{
        background-color: {colors['card']} !important;
        color: {colors['text']} !important;
        border-color: {colors['border']} !important;
    }}

    .stDateInput input {{
        background-color: {colors['card']} !important;
        color: {colors['text']} !important;
        border-color: {colors['border']} !important;
    }}

    [data-baseweb="popover"] {{
        background-color: {colors['card']} !important;
    }}

    [role="listbox"] {{
        background-color: {colors['card']} !important;
    }}

    [role="option"] {{
        background-color: {colors['card']} !important;
        color: {colors['text']} !important;
    }}

    [role="option"]:hover {{
        background-color: {colors['primary']} !important;
        color: white !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {colors['text']} !important;
    }}

    .logo-circle {{
        border-radius: 50%;
        border: 2px solid {colors['primary']};
        padding: 5px;
        background-color: {colors['card']};
        display: inline-block;
        box-shadow: 0 2px 8px rgba(239, 125, 30, 0.3);
    }}

    .logo-circle img {{
        border-radius: 50%;
        display: block;
    }}

    .logo-sidebar-center {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 5px;
    }}
    </style>
    """
