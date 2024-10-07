# app/components/charts.py

import streamlit as st
import plotly.graph_objects as go

def render_bar_chart(df):
    st.bar_chart(df, use_container_width=True)

def render_tempo_gauge(df):
    avg_tempo = df['Tempo'].mean()
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_tempo,
        title={'text': "Average Tempo"},
        gauge={
            'axis': {'range': [0, 250]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 60], 'color': "lightgray"},
                {'range': [60, 120], 'color': "gray"},
                {'range': [120, 180], 'color': "lightgray"},
                {'range': [180, 250], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': avg_tempo
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

def render_line_chart(df):
    st.line_chart(df, use_container_width=True)
