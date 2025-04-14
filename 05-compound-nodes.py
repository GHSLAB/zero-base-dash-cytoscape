# 复合节点
# Cytoscape.js 中引入的一个概念，复合节点是包含 （父） 或包含在另一个节点 （子） 内的节点。
# 父节点没有位置或大小，因为这些值是根据子节点的配置方式自动计算的。

from dash import Dash, html
import dash_cytoscape as cyto

app = Dash()

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape-compound",
            layout={"name": "preset"},
            style={"width": "100%", "height": "450px"},
            stylesheet=[
                {"selector": "node", "style": {"content": "data(label)"}},
                {"selector": ".countries", "style": {"width": 5}},
                {"selector": ".cities", "style": {"line-style": "dashed"}},
            ],
            elements=[
                # Parent Nodes
                {"data": {"id": "us", "label": "United States"}},
                {"data": {"id": "can", "label": "Canada"}},
                # Children Nodes
                {
                    "data": {"id": "nyc", "label": "New York", "parent": "us"},
                    "position": {"x": 100, "y": 100},
                },
                {
                    "data": {"id": "sf", "label": "San Francisco", "parent": "us"},
                    "position": {"x": 100, "y": 200},
                },
                {
                    "data": {"id": "mtl", "label": "Montreal", "parent": "can"},
                    "position": {"x": 400, "y": 100},
                },
                # Edges
                {"data": {"source": "can", "target": "us"}, "classes": "countries"},
                {"data": {"source": "nyc", "target": "sf"}, "classes": "cities"},
                {"data": {"source": "sf", "target": "mtl"}, "classes": "cities"},
            ],
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
