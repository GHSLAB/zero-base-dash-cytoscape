# 与 CSS 类类似，元素类用于使用选择器设置元素组的样式。
# 我们通过为元素提供一个或多个类（用空格分隔）来修改前面的示例，
# 并定义一个基于这些类修改元素的样式表。

from dash import Dash, html
import dash_cytoscape as cyto

app = Dash()

# 定义样式表
my_stylesheet = [
    # Group selectors
    {"selector": "node", "style": {"content": "data(label)"}},
    # Class selectors
    {"selector": ".red", "style": {"background-color": "red", "line-color": "red"}},
    {"selector": ".triangle", "style": {"shape": "triangle"}},
]

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape-elements-classes",
            layout={"name": "preset"},
            style={"width": "100%", "height": "400px"},
            stylesheet=my_stylesheet,
            elements=[
                {
                    "data": {"id": "one", "label": "Modified Color"},
                    "position": {"x": 75, "y": 75},
                    "classes": "red",  # Single class
                },
                {
                    "data": {"id": "two", "label": "Modified Shape"},
                    "position": {"x": 75, "y": 200},
                    "classes": "triangle",  # Single class
                },
                {
                    "data": {"id": "three", "label": "Both Modified"},
                    "position": {"x": 200, "y": 75},
                    "classes": "red triangle",  # Multiple classes
                },
                {
                    "data": {"id": "four", "label": "Regular"},
                    "position": {"x": 200, "y": 200},
                },
                # The edge elements
                {"data": {"source": "one", "target": "two"}, "classes": "red"},
                {"data": {"source": "two", "target": "three"}},
                {"data": {"source": "three", "target": "four"}, "classes": "red"},
                {"data": {"source": "two", "target": "four"}},
            ],
        )
    ]
)


if __name__ == "__main__":
    app.run(debug=True, port='18040')
