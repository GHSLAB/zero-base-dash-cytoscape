# layout
# 接收 name 的dict
# preset, random, grid, circle, concentric...
# https://js.cytoscape.org/#layouts
# 如果给出了 preset，则将根据元素中指定的位置渲染位置。
# 否则，位置将由 Cytoscape.js 在幕后根据布局字典的给定项计算

# 在大多数情况下，不会给出节点的位置。在这些情况下，可以使用其中一种内置方法。
# 让我们看看当 name 的值设置为 'circle' 或 'grid' 时会发生什么


from dash import Dash, html
import dash_cytoscape as cyto

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
        cyto.Cytoscape(
            id="cytoscape-layout-1",
            elements=elements,
            style={"width": "100%", "height": "350px"},
            layout={"name": "preset"},
        ),
        cyto.Cytoscape(
            id="cytoscape-layout-2",
            elements=elements,
            style={"width": "100%", "height": "350px"},
            layout={"name": "circle"},
        ),
        cyto.Cytoscape(
            id="cytoscape-layout-3",
            elements=elements,
            style={"width": "100%", "height": "350px"},
            layout={"name": "grid"},
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True, port="18060")
