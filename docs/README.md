# Painel de Entregáveis RPA

Painel de gestão e monitoramento de fluxos RPA (Robotic Process Automation) do Grupo Odilon Santos.

## 🎯 Funcionalidades

- **Monitoramento por Área**: Visualização organizada por áreas/departamentos
- **Métricas em Tempo Real**: Big numbers com indicadores de qualidade e performance
- **Gestão de Falhas**: Aba dedicada para análise e controle de erros
- **Duração Média**: Análise de tempo de execução dos fluxos
- **Filtros Avançados**: Busca por projeto e período de execução
- **Modo Escuro/Claro**: Alternância de temas para melhor experiência
- **Exportação Excel**: Download de relatórios completos

## 📋 Requisitos

- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

## 🚀 Instalação

1. Clone o repositório ou baixe os arquivos

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o arquivo `.env` na pasta `config/`:
```env
API_URL=https://integra.odilonsantos.com/api/Bpms/tabentregaveisprod
API_TOKEN=seu_token_aqui
HOST=192.168.148.12
PORT=8501
```

## 🎮 Uso

Execute o comando:

```bash
streamlit run main.py --server.port 8501 --server.address 192.168.148.12
```

Ou simplesmente:

```bash
streamlit run main.py
```

Acesse no navegador: `http://192.168.148.12:8501/`

## 📊 Estrutura de Dados

O painel consome dados da API que retorna informações com a seguinte estrutura:

```json
{
    "id_disparo": "ctb-apurar_diferenca_de_inventario_20260204_115102",
    "nome_processo": "ctb-Apurar Diferença de Inventário",
    "nome_fluxo": "ctb-apurar_diferenca_de_inventario",
    "frequencia_disparo": "Variável (Gatilho Zeev)",
    "horarios_disparo": "08:51",
    "tipo_fluxo": "PAD",
    "data_inicio": "2026-02-04T08:51:02-03:00",
    "data_fim": "2026-02-04T08:56:34-03:00",
    "duracao": "00:05:32",
    "tipo_arquivo": "Lançamento Mega",
    "status": "Concluído",
    "erros": null,
    "progresso": 100,
    "resultado_esperado": 1,
    "resultado_entregue": 1,
    "tipo_esperado": null,
    "dados_adicionais": "Fluxo v1.Empresa 2 Código 11847 Qtd. 7",
    "em_producao": true
}
```

## 🎨 Áreas Mapeadas

- BackOffice (bko)
- Contabilidade (ctb)
- Facilities (fcs)
- Financeiro (fin)
- Impressão 3D (i3d)
- Manutenção (mnt)
- Núcleo de Excelência (nex)
- Núcleo de Pessoas (npe)
- Tecnologia (sti)
- Setor Jurídico (jur)
- Núcleo de IA (nia)
- Núcleo de TI (nti)
- Suprimentos (sup)

## 📁 Estrutura do Projeto

```
nex-painel_entregaveis/
│
├── assets/
│   └── osac.jpg          # Logo da organização
│
├── config/
│   └── .env              # Configurações sensíveis
│
├── main.py               # Aplicação principal
├── requirements.txt      # Dependências Python
└── README.md            # Documentação
```

## 🔒 Segurança

- O arquivo `.env` não deve ser versionado (adicione ao `.gitignore`)
- O token de API deve ser mantido em sigilo
- Apenas fluxos com `em_producao: true` são exibidos

## 🛠️ Tecnologias

- **Streamlit**: Framework de interface web
- **Pandas**: Manipulação de dados
- **Plotly**: Visualizações interativas
- **Python-dotenv**: Gerenciamento de variáveis de ambiente
- **Requests**: Consumo de API REST

## 📝 Notas

- Cache de dados: 5 minutos (300 segundos)
- Apenas processos em produção são exibidos
- A identificação da área é feita pelo prefixo do nome do processo (ex: "ctb-" → Contabilidade)

---

**Desenvolvido para o Grupo Odilon Santos**