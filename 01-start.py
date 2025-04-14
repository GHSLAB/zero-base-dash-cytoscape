### https://dash.plotly.com/cytoscape

from dash import Dash, html
import dash_cytoscape as cyto
from feffery_dash_utils.style_utils import style

app = Dash()

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape-two-nodes",
            layout={"name": "preset"},
            style={"width": "100%", "height": "400px"},
            elements=[
                {
                    "data": {"id": "one", "label": "Node 1"},
                    "position": {"x": 0, "y": 0},
                },
                {
                    "data": {"id": "two", "label": "Node 2"},
                    "position": {"x": 200, "y": 200},
                },
                {"data": {"source": "one", "target": "two"}},
            ],
        )
    ],
    style=style(
        # border="2px solid #ccc",
        borderRadius="10px",
        # padding="10px",
        boxShadow="inset 0 0 10px #00000080"  # 新增内阴影效果
    ),
)

if __name__ == "__main__":
    app.run(debug=True)
