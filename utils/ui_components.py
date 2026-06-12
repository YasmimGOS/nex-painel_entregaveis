"""
Componentes reutilizáveis de UI.
"""

import streamlit as st
import base64
import plotly.graph_objects as go
import pandas as pd
from utils.helpers import format_number_br


def render_logo(image_path: str, size: int, colors: dict):
    """Renderiza logo com círculo"""
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
        img_b64 = base64.b64encode(img_bytes).decode()

    st.markdown(f'''
        <div class="logo-circle">
            <img src="data:image/jpeg;base64,{img_b64}" width="{size}">
        </div>
    ''', unsafe_allow_html=True)


def render_logo_centered(image_path: str, size: int, colors: dict):
    """Renderiza logo centralizada"""
    with open(image_path, 'rb') as f:
        img_bytes = f.read()
        img_b64 = base64.b64encode(img_bytes).decode()

    st.markdown(f'''
        <div class="logo-sidebar-center">
            <div class="logo-circle">
                <img src="data:image/jpeg;base64,{img_b64}" width="{size}">
            </div>
        </div>
    ''', unsafe_allow_html=True)


def render_kpi_cards(kpi, area_nome: str, colors: dict, is_dark: bool):
    """Renderiza cards de KPI com scroll horizontal"""
    shadow = 'rgba(0,0,0,0.3)' if is_dark else 'rgba(0,0,0,0.1)'

    kpi_dict = kpi.to_dict()
    volume_fmt = format_number_br(kpi_dict['volume_entregue'])
    esperado_fmt = format_number_br(kpi_dict['resultado_esperado_total'])
    entregue_fmt = format_number_br(kpi_dict['resultado_entregue_total'])

    st.markdown(f"""
    <div class="kpi-scroll-wrapper">
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">Total de Disparos</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{kpi_dict['total_disparos']}</div>
        </div>
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">Volume ({area_nome})</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{volume_fmt}</div>
        </div>
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">Health Score</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{kpi_dict['health_score']}%</div>
        </div>
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">% Atingimento</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{kpi_dict['percentual_atingimento']}%</div>
        </div>
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">Esperado</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{esperado_fmt}</div>
        </div>
        <div style="background-color: {colors['card']}; padding: 20px; border-radius: 12px; border-left: 5px solid {colors['primary']}; box-shadow: 0 4px 15px {shadow}; min-width: 150px;">
            <div style="color: {colors['text_secondary']}; font-weight: 600; font-size: 14px;">Entregue</div>
            <div style="color: {colors['text']}; font-size: 2rem; font-weight: 700;">{entregue_fmt}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_comparison_chart(df_comparacao: pd.DataFrame, colors: dict):
    """Renderiza gráfico de comparação esperado vs entregue"""
    if df_comparacao.empty:
        st.info("Nenhum dado disponível para comparação")
        return

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df_comparacao['nome_processo'],
        x=df_comparacao['resultado_esperado'],
        name='Esperado',
        orientation='h',
        marker_color=colors['info'],
        text=df_comparacao['resultado_esperado'],
        textposition='outside',
        textfont=dict(size=22, color=colors['text']),
        width=0.35,
    ))

    fig.add_trace(go.Bar(
        y=df_comparacao['nome_processo'],
        x=df_comparacao['resultado_entregue'],
        name='Entregue',
        orientation='h',
        marker_color=colors['success'],
        text=df_comparacao['resultado_entregue'],
        textposition='outside',
        textfont=dict(size=22, color=colors['text']),
        width=0.35,
    ))

    altura_grafico = max(500, len(df_comparacao) * 60)

    fig.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=colors['text'], size=16),
        xaxis_title="Quantidade",
        yaxis_title="",
        margin=dict(t=20, b=20, l=10, r=10),
        height=altura_grafico,
        bargap=0.3,
        xaxis=dict(
            titlefont=dict(color=colors['text'], size=20),
            tickfont=dict(color=colors['text'], size=18)
        ),
        yaxis=dict(
            tickfont=dict(color=colors['text'], size=18)
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color=colors['text'], size=18)
        )
    )

    st.plotly_chart(fig, use_container_width=True)


def render_health_donut(kpi, colors: dict):
    """Renderiza gráfico donut de saúde"""
    kpi_dict = kpi.to_dict()

    fig = go.Figure(go.Pie(
        labels=['Sucesso (Concluído)', 'Falhas/Atenção'],
        values=[kpi_dict['execucoes_concluidas'], kpi_dict['execucoes_falhadas']],
        hole=.65,
        marker_colors=[colors['success'], colors['error']]
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=colors['text'], size=13),
        showlegend=True,
        margin=dict(t=30, b=10, l=10, r=10),
        height=350,
        legend=dict(
            font=dict(color=colors['text'], size=13)
        )
    )

    st.plotly_chart(fig, use_container_width=True)
