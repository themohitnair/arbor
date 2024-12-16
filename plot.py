import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime
import os
from config import PLOTS_DIR


def plot_throughput(throughputs: list[int], intervals: list[datetime]):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=intervals,
            y=throughputs,
            mode="lines",
            name="Line 1",
            line=dict(color="white", width=1),
        )
    )
    fig.update_layout(
        title=dict(
            text="Throughput Plot",
            font=dict(family="monospace", size=24, color="white"),
        ),
        xaxis=dict(
            title=dict(
                text="interval timestamps",
                font=dict(family="monospace", size=18, color="white"),
            ),
            showgrid=True,
            gridcolor="green",
            zeroline=False,
            linecolor="green",
            tickcolor="white",
            tickfont=dict(family="monospace", size=14, color="white"),
        ),
        yaxis=dict(
            title=dict(
                text="throughput", font=dict(family="monospace", size=18, color="white")
            ),
            showgrid=True,
            gridcolor="green",
            zeroline=False,
            linecolor="green",
            tickcolor="white",
            tickfont=dict(family="monospace", size=14, color="white"),
        ),
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(family="monospace", size=16, color="white"),
        template="plotly_dark",
    )
    pio.write_image(fig, os.path.join(PLOTS_DIR, "throughput.png"), scale=3)
