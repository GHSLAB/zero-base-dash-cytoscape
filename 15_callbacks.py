# https://dash.plotly.com/cytoscape/callbacks


from dash import Dash, html, dcc, Input, Output, State, callback
import dash_cytoscape as cyto
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style

app = Dash()

# data
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


default_stylesheet = [
    {
        "selector": "node",
        "style": {"background-color": "#BFD7B5", "label": "data(label)"},
    },
    {"selector": "edge", "style": {"line-color": "#A3C4BC"}},
]

# 布局
app.layout = html.Div(
    [
        fac.AntdTitle("回调布局切换", level=4),
        fac.AntdSelect(
            id="dropdown-update-layout",
            options=[
                {"label": name.capitalize(), "value": name}
                for name in ["grid", "random", "circle", "cose", "concentric"]
            ],
            value="grid",
            placeholder="请选择布局",
            style={"width": "300px"},
        ),
        cyto.Cytoscape(
            id="cytoscape-update-layout",
            layout={"name": "grid"},
            style={"width": "100%", "height": "250px"},
            elements=elements,
        ),
        fac.AntdTitle("以交互方式更新样式", level=4),
        fac.AntdSpace(
            [
                fac.AntdText("Node Color: "),
                fac.AntdColorPicker(id="node-color", value="#292929", showText=True),
                fac.AntdText("Edge Color: "),
                fac.AntdColorPicker(id="edge-color", showText=True),
            ]
        ),
        cyto.Cytoscape(
            id="cytoscape-stylesheet-callbacks",
            layout={"name": "cose"},
            stylesheet=default_stylesheet,
            style={"width": "100%", "height": "350px"},
            elements=elements,
        ),
        fac.AntdTitle("添加删除节点", level=4),
        fac.AntdSpace(
            [
                fac.AntdButton("添加节点", id="add-node", type="primary"),
                fac.AntdButton("删除节点", id="remove-node"),
            ]
        ),
        cyto.Cytoscape(
            id="cytoscape-elements-callbacks",
            layout={"name": "cose"},
            stylesheet=default_stylesheet,
            style={"width": "100%", "height": "450px"},
            elements=edges + nodes,
            userPanningEnabled=False,
        ),
    ],
    style=style(padding=10),
)


## 布局回调
@callback(
    Output("cytoscape-update-layout", "layout"),
    Input("dropdown-update-layout", "value"),
)
def update_layout(layout):
    return {"name": layout, "animate": True}


## 样式回调
@app.callback(
    Output("cytoscape-stylesheet-callbacks", "stylesheet"),
    [
        Input("edge-color", "value"),
        Input("node-color", "value"),
    ],
)
def update_stylesheet(line_color, bg_color):
    if line_color is None:
        line_color = "transparent"

    if bg_color is None:
        bg_color = "transparent"

    new_styles = [
        {"selector": "node", "style": {"background-color": bg_color}},
        {"selector": "edge", "style": {"line-color": line_color}},
    ]

    return default_stylesheet + new_styles


## 数据回调
@app.callback(
    Output("cytoscape-elements-callbacks", "elements"),
    [
        Input("add-node", "nClicks"),
        Input("remove-node", "nClicks"),
    ],
    State("cytoscape-elements-callbacks", "elements"),
)
def update_elements(add_nClicks, rev_nClicks, elements):
    current_nodes, deleted_nodes = get_current_and_deleted_nodes(elements)
    # If the add button was clicked most recently and there are nodes to add
    if add_nClicks and len(deleted_nodes):
        # We pop one node from deleted nodes and append it to nodes list.
        current_nodes.append(deleted_nodes.pop())
        # Get valid edges -- both source and target nodes are in the current graph
        cy_edges = get_current_valid_edges(current_nodes, edges)
        return cy_edges + current_nodes

    # If the remove button was clicked most recently and there are nodes to remove
    elif rev_nClicks and len(current_nodes):
        current_nodes.pop()
        cy_edges = get_current_valid_edges(current_nodes, edges)
        return cy_edges + current_nodes

    # Neither have been clicked yet (or fallback condition)
    return elements


def get_current_valid_edges(current_nodes, all_edges):
    """Returns edges that are present in Cytoscape:
    its source and target nodes are still present in the graph.
    """
    valid_edges = []
    node_ids = {n["data"]["id"] for n in current_nodes}

    for e in all_edges:
        if e["data"]["source"] in node_ids and e["data"]["target"] in node_ids:
            valid_edges.append(e)
    return valid_edges


def get_current_and_deleted_nodes(elements):
    """Returns nodes that are present in Cytoscape and the deleted nodes"""
    current_nodes = []
    deleted_nodes = []

    # get current graph nodes
    for ele in elements:
        # if the element is a node
        if "source" not in ele["data"]:
            current_nodes.append(ele)

    # get deleted nodes
    node_ids = {n["data"]["id"] for n in current_nodes}
    for n in nodes:
        if n["data"]["id"] not in node_ids:
            deleted_nodes.append(n)

    return current_nodes, deleted_nodes


if __name__ == "__main__":
    app.run(debug=True, port="18150")
