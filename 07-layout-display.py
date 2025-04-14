# 微调布局

# 对于任何给定的名称项，布局接受一组键 字典
# 例如， 网格布局 将接受 row 和 cols
# 圆形布局 半径 和 startAngle 等
# 在圆形布局的情况下，我们可以强制节点以弧度为单位以某个角度开始和结束

# 对于 breadthfirst 布局，通过对图形执行广度优先搜索，从现有节点创建树。
# 默认情况下，会推断树的根，但也可以指定为一个选项。
# 如果我们选择 New York City 作为根，图表将如下所示：


from dash import Dash, html
import dash_cytoscape as cyto
import feffery_antd_components as fac
import math

app = Dash()

nodes = [
    {
        "data": {"id": short, "label": label},
        "position": {"x": 20 * lat, "y": -20 * long},
    }
    for short, label, long, lat in (
        ("la", "Los Angeles", 34.03, -118.25),
        ("nyc", "New York", 40.71, -74),
        ("to", "Toronto", 43.65, -79.38),
        ("mtl", "Montreal", 45.50, -73.57),
        ("van", "Vancouver", 49.28, -123.12),
        ("chi", "Chicago", 41.88, -87.63),
        ("bos", "Boston", 42.36, -71.06),
        ("hou", "Houston", 29.76, -95.37),
    )
]

edges = [
    {"data": {"source": source, "target": target}}
    for source, target in (
        ("van", "la"),
        ("la", "chi"),
        ("hou", "chi"),
        ("to", "mtl"),
        ("mtl", "bos"),
        ("nyc", "bos"),
        ("to", "hou"),
        ("to", "nyc"),
        ("la", "nyc"),
        ("nyc", "bos"),
    )
]

elements = nodes + edges

app.layout = html.Div(
    [
        fac.AntdText("grid布局"),
        cyto.Cytoscape(
            id="cytoscape-layout-4",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={"name": "grid", "rows": 3},
        ),
        fac.AntdText("circle布局"),
        cyto.Cytoscape(
            id="cytoscape-layout-5",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={
                "name": "circle",
                "radius": 250,
                "startAngle": math.pi * 1 / 6,
                "sweep": math.pi * 2 / 3,
            },
        ),
        fac.AntdText("breadthfirst布局 root nyc"),
        cyto.Cytoscape(
            id="cytoscape-layout-6",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={"name": "breadthfirst", "roots": '[id = "nyc"]'},
        ),
        fac.AntdText("breadthfirst布局 root van mtl"),
        cyto.Cytoscape(
            id="cytoscape-layout-7",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={"name": "breadthfirst", "roots": "#van, #mtl"},
        ),
        fac.AntdText("preset布局 positons from lat,lng"),
        cyto.Cytoscape(
            id="cytoscape-layout-8",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={
                "name": "preset",
                "positions": {node["data"]["id"]: node["position"] for node in nodes},
            },
        ),
        fac.AntdText("coze布局 力导向布局 Physics-based Layouts 基于物理的布局"),
        cyto.Cytoscape(
            id="cytoscape-layout-9",
            elements=elements,
            style={"width": "100%", "height": "250px"},
            layout={"name": "cose"},
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
