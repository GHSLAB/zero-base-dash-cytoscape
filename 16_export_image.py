from dash import Dash, dcc, html, Input, Output, ctx, callback
import dash_cytoscape as cyto

# enable svg export
cyto.load_extra_layouts()

app = Dash()
server = app.server

# Object declaration
basic_elements = [
    {"data": {"id": "one", "label": "Node 1"}, "position": {"x": 50, "y": 50}},
    {"data": {"id": "two", "label": "Node 2"}, "position": {"x": 200, "y": 200}},
    {"data": {"id": "three", "label": "Node 3"}, "position": {"x": 100, "y": 150}},
    {"data": {"id": "four", "label": "Node 4"}, "position": {"x": 400, "y": 50}},
    {"data": {"id": "five", "label": "Node 5"}, "position": {"x": 250, "y": 100}},
    {"data": {"id": "six", "label": "Node 6", "parent": "three"}, "position": {"x": 150, "y": 150}},
    {
        "data": {
            "id": "one-two",
            "source": "one",
            "target": "two",
            "label": "Edge from Node1 to Node2",
        }
    },
    {
        "data": {
            "id": "one-five",
            "source": "one",
            "target": "five",
            "label": "Edge from Node 1 to Node 5",
        }
    },
    {
        "data": {
            "id": "two-four",
            "source": "two",
            "target": "four",
            "label": "Edge from Node 2 to Node 4",
        }
    },
    {
        "data": {
            "id": "three-five",
            "source": "three",
            "target": "five",
            "label": "Edge from Node 3 to Node 5",
        }
    },
    {
        "data": {
            "id": "three-two",
            "source": "three",
            "target": "two",
            "label": "Edge from Node 3 to Node 2",
        }
    },
    {
        "data": {
            "id": "four-four",
            "source": "four",
            "target": "four",
            "label": "Edge from Node 4 to Node 4",
        }
    },
    {
        "data": {
            "id": "four-six",
            "source": "four",
            "target": "six",
            "label": "Edge from Node 4 to Node 6",
        }
    },
    {
        "data": {
            "id": "five-one",
            "source": "five",
            "target": "one",
            "label": "Edge from Node 5 to Node 1",
        }
    },
]

styles = {
    "output": {
        "overflow-y": "scroll",
        "overflow-wrap": "break-word",
        "height": "calc(100% - 25px)",
        "border": "thin lightgrey solid",
    },
    "tab": {"height": "calc(98vh - 115px)"},
}


app.layout = html.Div(
    [
        html.Div(
            className="eight columns",
            children=[
                cyto.Cytoscape(
                    id="cytoscape-image-export",
                    elements=basic_elements,
                    layout={"name": "preset"},
                    style={"height": "100vh", "width": "calc(100% - 500px)", "float": "left"},
                )
            ],
        ),
        html.Div(
            className="four columns",
            children=[
                dcc.Tabs(
                    id="tabs-image-export",
                    children=[
                        dcc.Tab(label="generate jpg", value="jpg"),
                        dcc.Tab(label="generate png", value="png"),
                    ],
                ),
                html.Div(
                    style=styles["tab"],
                    children=[
                        html.Div(
                            id="image-text",
                            children="image data will appear here",
                            style=styles["output"],
                        )
                    ],
                ),
                html.Div("Download graph:"),
                html.Button("as jpg", id="btn-get-jpg"),
                html.Button("as png", id="btn-get-png"),
                html.Button("as svg", id="btn-get-svg"),
            ],
        ),
    ]
)


@callback(
    Output("image-text", "children"),
    Input("cytoscape-image-export", "imageData"),
)
def put_image_string(data):
    return data


@callback(
    Output("cytoscape-image-export", "generateImage"),
    [
        Input("tabs-image-export", "value"),
        Input("btn-get-jpg", "n_clicks"),
        Input("btn-get-png", "n_clicks"),
        Input("btn-get-svg", "n_clicks"),
    ],
    prevent_initial_call=True,
)
def get_image(tab, get_jpg_clicks, get_png_clicks, get_svg_clicks):
    # 统一转换为小写
    ftype = tab.lower() if tab else "png"
    action = "store"

    if ctx.triggered:
        if ctx.triggered_id != "tabs-image-export":
            action = "download"
            # 提取后缀并转换为小写
            # noqa: E402, F821
            # 检查 triggered_id 是否为字符串类型
            if isinstance(ctx.triggered_id, str):
                ftype = ctx.triggered_id.split("-")[-1].lower()
            else:
                ftype = str(ctx.triggered_id).split("-")[-1].lower()
    
    # 验证文件类型有效性
    valid_types = ["svg", "png", "jpg", "jpeg"]
    if ftype not in valid_types:
        ftype = "png"
    elif ftype == "jpeg":  # 处理jpeg别名
        ftype = "jpg"

    return {"type": ftype, "action": action}


if __name__ == "__main__":
    app.run(debug=True, port="18190")
