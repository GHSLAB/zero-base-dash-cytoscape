###
# 每个元素都由一个字典定义
# data nodes
# id：元素的索引，在您想要引用它时很有用
# label：与元素关联的名称（如果您希望显示它）

# edge
# source：源节点的 ID，即 Edge 开始的位置
# target：边缘结束的目标节点的 ID

# 两个节点的图，及连接这两个节点的边，我需要其中三个元素字典，分组为一个列表
####

from dash import Dash, html
import dash_cytoscape as cyto

app = Dash()

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape-elements-basic",
            layout={"name": "preset"},
            style={"width": "100%", "height": "400px"},
            elements=[
                # The nodes elements
                {
                    "data": {"id": "one", "label": "Node 1"},
                    "position": {"x": 50, "y": 50},
                },
                {
                    "data": {"id": "two", "label": "Node 2"},
                    "position": {"x": 200, "y": 200},
                },
                # The edge elements
                {"data": {"source": "one", "target": "two", "label": "Node 1 to 2"}},
            ],
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True, port='18020')
