"""
Testes para o DataService.
Valida processamento de dados e cálculo de KPIs.
"""

import pandas as pd
from services.data_service import DataService


def test_process_data():
    """Testa processamento básico de dados"""
    raw_data = [
        {
            'nome_processo': 'ctb-Processo Teste',
            'em_producao': True,
            'status': 'Concluído',
            'resultado_esperado': 10,
            'resultado_entregue': 8,
            'data_inicio': '2024-01-01T10:00:00'
        },
        {
            'nome_processo': 'fin-Outro Processo',
            'em_producao': True,
            'status': 'Falha',
            'resultado_esperado': 5,
            'resultado_entregue': 0,
            'data_inicio': '2024-01-01T11:00:00'
        },
        {
            'nome_processo': 'nex-Processo Desabilitado',
            'em_producao': False,
            'status': 'Concluído',
            'resultado_esperado': 20,
            'resultado_entregue': 20,
            'data_inicio': '2024-01-01T12:00:00'
        }
    ]

    service = DataService()
    df = service.process_raw_data(raw_data)

    print(f"\n✅ Total de registros processados: {len(df)}")
    print(f"   Esperado: 2 (apenas em_producao=True)")

    assert len(df) == 2, "Deveria ter apenas 2 registros (em_producao=True)"
    assert 'area_nome' in df.columns, "Coluna area_nome deveria existir"
    assert df['area_nome'].tolist() == ['Contabilidade', 'Financeiro'], "Áreas identificadas incorretamente"

    print("✅ Identificação de áreas: OK")


def test_calculate_kpis():
    """Testa cálculo de KPIs"""
    data = {
        'nome_processo': ['Processo 1', 'Processo 2', 'Processo 3'],
        'status': ['Concluído', 'Concluído', 'Falha'],
        'resultado_esperado': [10, 20, 15],
        'resultado_entregue': [10, 18, 5]
    }
    df = pd.DataFrame(data)

    service = DataService()
    kpi = service.calculate_kpis(df)

    print(f"\n✅ KPIs Calculados:")
    print(f"   Total Disparos: {kpi.total_disparos} (esperado: 3)")
    print(f"   Concluídas: {kpi.execucoes_concluidas} (esperado: 2)")
    print(f"   Health Score: {kpi.health_score:.1f}% (esperado: 66.7%)")
    print(f"   Volume Entregue: {kpi.volume_entregue} (esperado: 33)")
    print(f"   % Atingimento: {kpi.percentual_atingimento:.1f}% (esperado: 73.3%)")

    assert kpi.total_disparos == 3
    assert kpi.execucoes_concluidas == 2
    assert abs(kpi.health_score - 66.67) < 0.1
    assert kpi.volume_entregue == 33
    assert abs(kpi.percentual_atingimento - 73.33) < 0.1

    print("✅ Cálculo de KPIs: OK")


def test_filter_by_area():
    """Testa filtragem por área"""
    data = {
        'nome_processo': ['ctb-Processo 1', 'fin-Processo 2', 'ctb-Processo 3'],
        'area_nome': ['Contabilidade', 'Financeiro', 'Contabilidade']
    }
    df = pd.DataFrame(data)

    service = DataService()
    df_contabilidade = service.filter_by_area(df, 'Contabilidade')

    print(f"\n✅ Filtro por área:")
    print(f"   Total: {len(df_contabilidade)} (esperado: 2)")

    assert len(df_contabilidade) == 2
    assert all(df_contabilidade['area_nome'] == 'Contabilidade')

    print("✅ Filtro por área: OK")


if __name__ == '__main__':
    print("=" * 80)
    print("TESTES DO DATA SERVICE")
    print("=" * 80)

    try:
        test_process_data()
        test_calculate_kpis()
        test_filter_by_area()

        print("\n" + "=" * 80)
        print("✅ TODOS OS TESTES PASSARAM!")
        print("=" * 80)
    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
