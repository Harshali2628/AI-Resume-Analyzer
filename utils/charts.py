import plotly.graph_objects as go
import streamlit as st


def show_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 50], "color": "#ffcccc"},
                    {"range": [50, 75], "color": "#ffe599"},
                    {"range": [75, 100], "color": "#b6d7a8"},
                ],
            },
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_pie(matching, missing):

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Matching", "Missing"],
                values=[matching, missing],
                hole=0.5,
            )
        ]
    )

    fig.update_layout(
        title="Skill Match Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )