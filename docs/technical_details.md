# Detalhes Técnicos - Painel de Entregáveis RPA

## Arquitetura do Sistema

### Visão Geral

O sistema segue uma arquitetura MVC (Model-View-Controller) com camada de serviços adicional para separação de responsabilidades.

```
┌─────────────────────────────────────────────────┐
│              View Layer (main.py)               │
│   ┌─────────────────────────────────────────┐   │
│   │      UI Components (ui_components.py)   │   │
│   └─────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│         Controller (main_controller.py)         │
└────────────────┬────────────────┬───────────────┘
                 │                │
    ┌────────────▼──────┐    ┌───▼──────────────┐
    │  APIService       │    │  DataService     │
    │  (api_service.py) │    │ (data_service.py)│
    └────────────┬──────┘    └───┬──────────────┘
                 │                │
    ┌────────────▼────────────────▼──────────────┐
    │          Models (entregavel.py, kpi.py)    │
    └────────────────────────────────────────────┘
```

## Componentes Principais

### 1. Models (Modelos de Dados)

#### Entregavel
```python
@dataclass
class Entregavel:
    id_disparo: str
    nome_processo: str
    status: str
    resultado_esperado: int
    resultado_entregue: int
    # ... outros campos
```

**Responsabilidades:**
- Representar estrutura de dados de um entregável
- Prover propriedades computadas (area_sigla, concluido, etc.)

#### KPI
```python
@dataclass
class KPI:
    total_disparos: int
    execucoes_concluidas: int
    health_score: float
    # ... outros campos
```

**Responsabilidades:**
- Encapsular métricas calculadas
- Fornecer métodos de conversão (to_dict)

### 2. Services (Camada de Serviços)

#### APIService
**Responsabilidades:**
- Comunicação com API externa
- Tratamento de autenticação
- Parsing de resposta JSON

**Métodos principais:**
- `fetch_entregaveis()`: Busca dados da API
- `_get_headers()`: Gera headers de autenticação
- `_extract_data()`: Extrai dados da resposta

#### DataService
**Responsabilidades:**
- Processamento de dados brutos
- Cálculo de KPIs
- Filtragem e transformação de dados
- Preparação de dados para visualização

**Métodos principais:**
- `process_raw_data()`: Processa dados da API
- `calculate_kpis()`: Calcula indicadores
- `filter_by_area()`: Filtra por área
- `prepare_comparison_data()`: Prepara dados para gráficos
- `prepare_table_data()`: Prepara dados para tabelas

### 3. Controllers

#### MainController
**Responsabilidades:**
- Orquestrar comunicação entre View e Services
- Gerenciar cache de dados
- Aplicar filtros compostos
- Preparar dados para exportação

**Fluxo de dados:**
```
User Action → Controller → Service → Model → Service → Controller → View
```

### 4. View Layer

#### main.py
**Responsabilidades:**
- Configuração inicial do Streamlit
- Gerenciamento de estado da sessão
- Renderização de telas (Home e Dashboard)
- Handling de eventos de UI

#### UI Components
**Componentes reutilizáveis:**
- `render_logo()`: Logo da empresa
- `render_kpi_cards()`: Cards de métricas
- `render_comparison_chart()`: Gráfico de comparação
- `render_health_donut()`: Gráfico de saúde

### 5. Utils (Utilitários)

#### constants.py
- Mapeamento de áreas
- Paletas de cores (dark/light)
- Timeouts e configurações

#### helpers.py
- Configuração de locale
- Formatação de números

#### styles.py
- CSS customizado para Streamlit
- Estilos responsivos

## Fluxo de Dados

### 1. Carregamento Inicial
```
User Access
    ↓
main.py inicializa
    ↓
Cria MainController
    ↓
Controller.load_data() [com cache]
    ↓
APIService.fetch_entregaveis()
    ↓
DataService.process_raw_data()
    ↓
DataFrame processado retorna para View
```

### 2. Seleção de Área
```
User seleciona área
    ↓
st.session_state.area_atual = área
    ↓
st.rerun()
    ↓
render_dashboard_screen()
    ↓
Controller.get_area_data()
    ↓
DataService.filter_by_area()
```

### 3. Aplicação de Filtros
```
User modifica filtros (sidebar)
    ↓
Controller.apply_filters(df, processos, tipos, status, periodo)
    ↓
DataFrame filtrado
    ↓
Controller.calculate_kpis(df_filtrado)
    ↓
KPIs exibidos
```

### 4. Exportação de Dados
```
User clica "Baixar Excel"
    ↓
Controller.prepare_excel_export()
    ↓
DataFrame limpo
    ↓
pd.ExcelWriter
    ↓
BytesIO buffer
    ↓
st.download_button
```

## Cache e Performance

### Estratégia de Cache
```python
@st.cache_data(ttl=300)  # 5 minutos
def load_data(_self) -> pd.DataFrame:
    # Cache invalidado automaticamente após 5 minutos
    # ou manualmente com st.cache_data.clear()
```

**Benefícios:**
- Reduz chamadas à API
- Melhora tempo de resposta
- Economia de recursos

## Tratamento de Erros

### APIService
```python
try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        return data
    return []
except requests.RequestException:
    return []
```

### DataService
```python
if not raw_data:
    return pd.DataFrame()

if df.empty:
    return df
```

## Testes

### Estrutura de Testes
```python
def test_process_data():
    raw_data = [...]
    service = DataService()
    df = service.process_raw_data(raw_data)
    assert len(df) == expected
```

**Áreas testadas:**
- Processamento de dados
- Cálculo de KPIs
- Filtragem por área

## Configuração

### Variáveis de Ambiente
```python
class Settings:
    API_URL = os.getenv('API_URL', default)
    API_TOKEN = os.getenv('API_TOKEN', '')
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8501))
```

### Streamlit Config
```toml
[theme]
primaryColor = "#EF7D1E"
backgroundColor = "#0A0A0A"
secondaryBackgroundColor = "#1A1A1A"

[server]
port = 8501
```

## Boas Práticas Implementadas

### DRY (Don't Repeat Yourself)
- Constantes centralizadas em `constants.py`
- Componentes de UI reutilizáveis
- Funções auxiliares em `helpers.py`

### Responsabilidade Única
- Cada classe tem uma função específica
- Separação clara de camadas
- Services especializados (API, Data)

### KISS (Keep It Simple, Stupid)
- Código direto e legível
- Evita otimizações prematuras
- Nomes autoexplicativos

### Nomes Significativos
```python
# Bom
def calculate_kpis(df: pd.DataFrame) -> KPI

# Ruim
def calc(data)
```

## Extensibilidade

### Adicionar Nova Área
1. Adicionar em `utils/constants.py`:
```python
AREAS_MAP = {
    ...
    'nova': 'Nova Área'
}
```

### Adicionar Novo KPI
1. Atualizar `models/kpi.py`:
```python
@dataclass
class KPI:
    ...
    novo_kpi: float
```

2. Atualizar `services/data_service.py`:
```python
def calculate_kpis(df):
    ...
    novo_kpi = calcular_novo_kpi(df)
    return KPI(..., novo_kpi=novo_kpi)
```

3. Atualizar `utils/ui_components.py`:
```python
def render_kpi_cards():
    # Adicionar card do novo KPI
```

## Troubleshooting

### Problema: Dados não carregando
**Diagnóstico:**
1. Verificar `config/.env` existe
2. Verificar API_TOKEN configurado
3. Testar conexão: `python tests/test_api.py`

### Problema: Área sem dados
**Diagnóstico:**
1. Verificar `em_producao = True` nos dados
2. Verificar prefixo do processo corresponde à área
3. Ver debug info no expander

### Problema: Erro de importação
**Diagnóstico:**
1. Verificar estrutura de pastas
2. Verificar `__init__.py` em todas as pastas
3. Reinstalar dependências: `pip install -r requirements.txt`

## Performance Tips

1. **Cache adequado**: Use TTL apropriado para seus dados
2. **Filtros eficientes**: Aplique filtros no DataFrame, não na exibição
3. **Lazy loading**: Carregue dados apenas quando necessário
4. **Chunks para Excel**: Para grandes volumes, considere chunks

## Segurança

### Checklist
- [ ] `.env` no `.gitignore`
- [ ] Token de API não hardcoded
- [ ] Validação de entrada de usuário
- [ ] HTTPS para API
- [ ] Logs sem informações sensíveis

---

Para mais informações, consulte o código-fonte ou entre em contato com a equipe de desenvolvimento.
