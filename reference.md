# Cytoscape Reference

https://dash.plotly.com/cytoscape/reference


id (string; optional): The ID used to identify this component in Dash callbacks.
id (string; optional)： 用于在Dash回调中标识此组件的 ID。

autoungrabify (boolean; optional): Whether nodes should be ungrabified (not grabbable by user) by default (if true, overrides individual node state).
autoungrabify (boolean; 可选)：默认情况下是否应取消抓取(用户无法抓取)节点(如果为 true，则覆盖单个节点状态)。

autolock (boolean; optional): Whether nodes should be locked (not draggable at all) by default (if true, overrides individual node state).
autolock (boolean;可选)：默认情况下是否应锁定节点(完全不可拖动)(如果为 true，则覆盖单个节点状态)。

autounselectify (boolean; optional): Whether nodes should be unselectified (immutable selection state) by default (if true, overrides individual element state).
autounselectify(boolean;可选)：默认情况下是否应取消选择节点(不可变选择状态)(如果为 true，则覆盖单个元素状态)。

autoRefreshLayout (boolean; optional): Whether the layout should be refreshed when elements are added or removed.
autoRefreshLayout(boolean; 可选)：在添加或删除元素时是否应刷新布局。

boxSelectionEnabled (boolean; optional): Whether box selection (i.e. drag a box overlay around, and release it to select) is enabled. If enabled, the user must taphold to pan the graph.
boxSelectionEnabled(boolean;可选)：是否启用框选择(即拖动框叠加层，然后释放它进行选择)。如果启用，用户必须长按才能平移图表。

className (string; optional): Sets the class name of the element (the value of an element's html class attribute).
className (string;可选)：设置元素的类名(元素的 html class 属性的值)。

elements (list|dict; optional): A list of dictionaries representing the elements of the networks. 1. Each dictionary describes an element, and specifies its purpose. -group(string): Either 'nodes' or 'edges'. If not given, it's automatically inferred. -data(dictionary): Element specific data. -id(string): Reference to the element, useful for selectors and edges. Randomly assigned if not given. -label(string): Optional name for the element, useful whendata(label)is given to a style'scontentorlabel. It is only a convention. -parent(string): Only for nodes. Optional reference to another node. Needed to create compound nodes. -source(string): Only for edges. The id of the source node, which is where the edge starts. -target(string): Only for edges. The id of the target node, where the edge ends. -position(dictionary): Only for nodes. The position of the node. -x(number): The x-coordinate of the node. -y(number): The y-coordinate of the node. -selected(boolean): If the element is selected upon initialisation. -selectable(boolean): If the element can be selected. -locked(boolean): Only for nodes. If the position is immutable. -grabbable(boolean): Only for nodes. If the node can be grabbed and moved by the user. -classes(string): Space separated string of class names of the element. Those classes can be selected by a style selector. 2. Theofficial Cytoscape.js documentation offers an extensive overview and examples of element declaration. Alternatively, a dictionary with the format { 'nodes':[], 'edges':[]} is allowed at initialization, but arrays remain the recommended format.


## 元素 (list| 字典; optional)：
表示网络元素的字典列表。1. 每个字典描述一个元素，并指定其用途。-group(string)：'nodes' 或 'edges'。如果未给出，则会自动推断。-data(dictionary)：元素特定的数据。-id(string)：对元素的引用，对选择器和边缘很有用。如果未给出，则随机分配。-label(string)：元素的可选名称，当 data(label) 被赋予样式的内容或标签时很有用。这只是一个约定俗成。-parent(string)：仅适用于节点。对另一个节点的可选引用。创建复合节点时需要。-source(string)：仅适用于 Edge。源节点的 ID，即 Edge 的起点。-target(string)：仅适用于边缘。Edge 结束位置的目标节点的 ID。-position(dictionary)：仅适用于节点。节点的位置。-x(number)：节点的 x 坐标。-y(number)：节点的 y 坐标。-selected(boolean)：如果在初始化时选择了元素。-selectable(boolean)：如果可以选择元素。-locked(boolean)：仅适用于节点。如果位置是不可变的。-grabbable(boolean)：仅适用于节点。如果用户可以抓取和移动节点。-classes(string)：元素的类名的空格分隔字符串。这些类可以通过样式选择器进行选择。2. 官方 Cytoscape.js 文档提供了元素声明的广泛概述和示例。 或者，在初始化时允许使用格式为 { 'nodes'：[]， 'edges'：[]} 的字典，但数组仍然是推荐的格式。

generateImage (dict; optional): Dictionary specifying options to generate an image of the current cytoscape graph. Value is cleared after data is received and image is generated. This property will be ignored on the initial creation of the cytoscape object and must be invoked through a callback after it has been rendered. The'type'key is required. The following keys are supported: -type(string): File type to ouput of 'svg, 'png', 'jpg', or 'jpeg' (alias of 'jpg') -options(dictionary, optional): Dictionary of options to cy.png() / cy.jpg() or cy.svg() for image generation. See http://js.cytoscape.org/#core/exportfor details. For'output', only 'base64' and 'base64uri' are supported. Default:{'output': 'base64uri'}. -action(string, optional): Default:'store'. Must be one of the following: -'store': Stores the image data (only jpg and png are supported) inimageDataand invokes server-side Dash callbacks. -'download': Downloads the image as a file with all data handling done client-side. NoimageDatacallbacks are fired. -'both': Stores image data and downloads image as file. -filename(string, optional): Name for the file to be downloaded. Default: 'cyto'. If the app does not need the image data server side and/or it will only be used to download the image, it may be prudent to invoke'download'foractioninstead of'store'to improve performance by preventing transfer of data to the server.
generateImage (dict; optional)：指定选项以生成当前 cytoscape 图图像的字典。在接收到数据并生成图像后，将清除该值。此属性将在 cytoscape 对象的初始创建时被忽略，并且必须在呈现后通过回调调用。'type' 键是必需的。支持以下键： -type(string)：要输出的文件类型为 'svg'、'png'、'jpg' 或 'jpeg'(别名为 'jpg') -options(dictionary，可选)：用于图像生成的 cy.png() / cy.jpg() 或 cy.svg() 的选项字典。有关详细信息 ，请参阅 http://js.cytoscape.org/#core/export。对于 'output'，仅支持 'base64' 和 'base64uri'。默认值：{'output'： 'base64uri'}。-action(string， optional)： 默认值：'store'。必须为以下之一：-'store'：将图片数据(仅支持 jpg 和 png)存储在 imageData 中，并调用服务端的Dash回调。-'download'：将映像下载为文件，并在客户端完成所有数据处理。不会触发 imageData 回调。-'both'：存储图片数据并将图片下载为文件。-filename(string， optional)：要下载的文件的名称。默认值： 'cyto'。如果应用程序不需要图像数据服务器端和/或它仅用于下载图像，则调用 “download” 而不是 “store” 可能是谨慎的做法，通过阻止将数据传输到服务器来提高性能。

imageData (string; optional): String representation of the image requested with generateImage. Null if no image was requested yet or the previous request failed. Read-only.
imageData (string;可选)：使用 generateImage 请求的图像的字符串表示形式。如果尚未请求图像或上一个请求失败，则为 Null。只读。

layout (dict; optional): A dictionary specifying how to set the position of the elements in your graph. The'name'key is required, and indicates which layout (algorithm) to use. 1. The layouts available by default are: -random: Randomly assigns positions -preset: Assigns position based on thepositionkey in element dictionaries -circle: Single-level circle, with optional radius -concentric: Multi-level circle, with optional radius -grid: Square grid, optionally with numbers ofrowsandcols-breadthfirst: Tree structure built using BFS, with optionalroots-cose: Force-directed physics simulation 2. Some external layouts are also included. To use them, rundash_cytoscape.load_extra_layouts()before creating your Dash app. Be careful about using the extra layouts when not necessary, since they require supplementary bandwidth for loading, which impacts the startup time of the app. -cose-bilkent:https://github.com/cytoscape/cytoscape.js-cose-bilkent-cola:https://github.com/cytoscape/cytoscape.js-cola-euler:https://github.com/cytoscape/cytoscape.js-dagre-spread:https://github.com/cytoscape/cytoscape.js-spread-dagre:https://github.com/cytoscape/cytoscape.js-dagre-klay:https://github.com/cytoscape/cytoscape.js-klay3. The keys accepted bylayoutvary depending on the algorithm, but some keys are accepted by all layouts: -fit(boolean): Whether to render the nodes in order to fit the canvas. -padding(number): Padding around the sides of the canvas, if fit is enabled. -animate(boolean): Whether to animate change in position when the layout changes. -animationDuration(number): Duration of animation in milliseconds, if enabled. -boundingBox(dictionary): How to constrain the layout in a specific area. Keys accepted are eitherx1, y1, x2, y2orx1, y1, w, h, all of which receive a pixel value. 4. The complete list of layouts and their accepted options are available on theCytoscape.js docs. For the external layouts, the options are listed in the "API" section of the README. Note that certain keys are not supported in Dash since the value is a JavaScript function or a callback. Please visitthis issue for more information.
layout (dict; optional)：指定如何设置元素在图形中的位置的字典。'name' 键是必需的，它指示要使用的布局(算法)。1. 默认可用的布局是： -random：随机分配位置 -preset：根据元素字典中的位置键分配位置 -circle：单级圆，具有可选的半径 -concentric：多级圆，具有可选的半径 -grid：方形网格，可选行数和 cols-breadthfirst：使用 BFS 构建的树形结构 ，具有可选的 roots-cose： 力导向物理模拟 2.还包括一些外部布局。要使用它们，请在创建 Dash 应用程序之前运行 dash_cytoscape.load_extra_layouts() 。在不需要时小心使用额外的布局，因为它们需要补充带宽来加载，这会影响应用程序的启动时间。-cose-bilkent：https://github.com/cytoscape/cytoscape.js-cose-bilkent-cola：https://github.com/cytoscape/cytoscape.js-cola-euler：https://github.com/cytoscape/cytoscape.js-dagre-spread：https://github.com/cytoscape/cytoscape.js-spread-dagre：https://github.com/cytoscape/cytoscape.js-dagre-klay：https://github.com/cytoscape/cytoscape.js-klay3. 布局接受的键因算法而异，但所有布局都接受某些键：-fit(boolean)：是否渲染节点以适应画布。-padding(number)：如果启用了 fit，则画布两侧的内边距。 -animate(boolean)：是否在布局更改时为位置更改添加动画效果。-animationDuration(number)：动画的持续时间(以毫秒为单位)(如果启用)。-boundingBox(dictionary)：如何约束特定区域的布局。接受的键是 x1、y1、x2、y2 或 x1、y1、w、h，所有这些键都接收像素值。4. 布局的完整列表及其接受的选项可在 Cytoscape.js 文档中找到。对于外部布局，选项列在 README 的 “API” 部分中。请注意，Dash 不支持某些键，因为其值是 JavaScript 函数或回调。请访问本期了解更多信息。

minZoom (number; optional): A minimum bound on the zoom level of the graph. The viewport can not be scaled smaller than this zoom level.
minZoom (number;可选)：图表缩放级别的最小边界。视口的缩放不能小于此缩放级别。

maxZoom (number; optional): A maximum bound on the zoom level of the graph. The viewport can not be scaled larger than this zoom level.
maxZoom (number; optional)：图表缩放级别的最大值。视口的缩放不能大于此缩放级别。

mouseoverNodeData (dict; optional): The data dictionary of a node returned when you hover over it. Read-only.
mouseoverNodeData (dict; optional)：将鼠标悬停在节点上时返回的节点的数据字典。只读。

mouseoverEdgeData (dict; optional): The data dictionary of an edge returned when you hover over it. Read-only.
mouseoverEdgeData (dict; optional)：将鼠标悬停在边上时返回的边的数据字典。只读。

pan (dict; optional): Dictionary indicating the initial panning position of the graph. The following keys are accepted: -x(number): The x-coordinate of the position. -y(number): The y-coordinate of the position.
pan (dict; 可选)：指示图形的初始平移位置的字典。接受以下键：-x(number)：位置的 x 坐标。-y(number)：位置的 y 坐标。

panningEnabled (boolean; optional): Whether panning the graph is enabled (i.e., the position of the graph is mutable overall).
panningEnabled(boolean; 可选)：是否启用平移图形(即图形的位置总体上是可变的)。

responsive (boolean; optional): Toggles intelligent responsive resize of Cytoscape graph with viewport size change
响应式 (boolean;可选)：通过视口大小更改来切换 Cytoscape 图形的智能响应式大小调整

style (dict; optional): Add inline styles to the root element.
style (dict; optional)：将内联样式添加到根元素。

stylesheet (list; optional): A list of dictionaries representing the styles of the elements. 1. Each dictionary requires the following keys: -selector(string): Which elements you are styling. Generally, you select a group of elements (node, edges, both), a class (that you declare in the element dictionary), or an element by ID. -style(dictionary): What aspects of the elements you want to modify. This could be the size or color of a node, the shape of an edge arrow, or many more. 2. Boththe selector string andthe style dictionary are exhaustively documented in the Cytoscape.js docs. Although methods such ascy.elements(...)andcy.filter(...)are not available, the selector string syntax stays the same.
stylesheet (list; optional)：表示元素样式的字典列表。1. 每个字典都需要以下键：-selector(string)：您正在设置样式的元素。通常，您可以选择一组元素(节点、边、两者)、一个类(您在元素字典中声明)或按 ID 选择一个元素。-style(dictionary)：要修改元素的哪些方面。这可以是节点的大小或颜色、边缘箭头的形状等等。2. 选择器字符串和样式字典都详尽地记录在 Cytoscape.js 文档中。尽管 cy.elements(...) 和 cy.filter(...) 不可用，则选择器字符串语法保持不变。

selectedNodeData (list; optional): The list of data dictionaries of all selected nodes (e.g. using Shift+Click to select multiple nodes, or Shift+Drag to use box selection). Read-only.
selectedNodeData(列表; 可选)：所有选定节点的数据字典列表(例如，使用 Shift+单击选择多个节点，或使用 Shift+拖动使用框选择)。只读。

selectedEdgeData (list; optional): The list of data dictionaries of all selected edges (e.g. using Shift+Click to select multiple nodes, or Shift+Drag to use box selection). Read-only.
selectedEdgeData(列表; 可选)：所有选定边缘的数据字典列表(例如，使用 Shift+单击选择多个节点，或使用 Shift+拖动使用框选择)。只读。

tapNode (dict; optional): The complete node dictionary returned when you tap or click it. Read-only. 1. Node-specific items: -edgesData(dictionary) -renderedPosition(dictionary) -timeStamp(number) 2. General items (for all elements): -classes(string) -data(dictionary) -grabbable(boolean) -group(string) -locked(boolean) -position(dictionary) -selectable(boolean) -selected(boolean) -style(dictionary) 3. Items for compound nodes: -ancestorsData(dictionary) -childrenData(dictionary) -descendantsData(dictionary) -parentData(dictionary) -siblingsData(dictionary) -isParent(boolean) -isChildless(boolean) -isChild(boolean) -isOrphan(boolean) -relativePosition(dictionary)
tapNode (dict; optional)：点按或单击时返回的完整节点字典。只读。1. 节点特定项： -edgesData(dictionary) -renderedPosition(dictionary) -timeStamp(number) 2.通用项目(适用于所有元素)： -classes(string) -data(字典) -grabbable(boolean) -group(string) -locked(boolean) -position(字典) -selectable(boolean) -selected(boolean) -style(字典) 3.复合节点的项目： -ancestorsData(字典) -childrenData(字典) -descendantsData(字典) -parentData(字典) -siblingsData(字典) -isParent(boolean) -isChildless(boolean) -isChild(boolean) -isOrphan(boolean) -relativePosition(字典)

tapNodeData (dict; optional): The data dictionary of a node returned when you tap or click it. Read-only.
tapNodeData (dict;可选)：点按或单击节点时返回的节点的数据字典。只读。

tapEdge (dict; optional): The complete edge dictionary returned when you tap or click it. Read-only. 1. Edge-specific items: -isLoop(boolean) -isSimple(boolean) -midpoint(dictionary) -sourceData(dictionary) -sourceEndpoint(dictionary) -targetData(dictionary) -targetEndpoint(dictionary) -timeStamp(number) 2. General items (for all elements): -classes(string) -data(dictionary) -grabbable(boolean) -group(string) -locked(boolean) -selectable(boolean) -selected(boolean) -style(dictionary)


### tapEdge(dict;可选)
点按或单击它时返回的完整边缘词典。只读。
1. 特定于边缘的项目： -isLoop(boolean) -isSimple(boolean) -midpoint(字典) -sourceData(字典) -sourceEndpoint(字典) -targetData(字典) -targetEndpoint(字典) -timeStamp(数字) 
2. 常规项目(适用于所有元素)： -classes(string) -data(字典) -grabbable(boolean) -group(string) -locked(boolean) -selectable(boolean) -selected(boolean) -style(字典)

# tapEdgeData (dict;可选)
**只读**. 点按或单击边缘时返回的数据字典

### userPanningEnabled(boolean; 可选)
是否允许用户事件(例如拖动图表背景)平移图表

### userZoomingEnabled(boolean; 可选)
是否允许用户事件, 缩放图表

### zoom (number; 可选)
图表的初始缩放级别。您可以设置 minZoom 和 maxZoom 以设置缩放级别的限制

### zoomingEnabled (boolean; 可选)
是否启用缩放图形(即图形的缩放级别总体上是可变的)




## utils.Tree
A class to facilitate tree manipulation in Cytoscape.
一个在 Cytoscape 中促进树作的类。

param node_id: The ID of this tree, passed to the node data dict
param node_id：此树的 ID，传递给节点数据字典

param children: The children of this tree, also Tree objects
param children：此 Tree 的子项，也是 Tree 对象

param data: Dictionary passed to this tree's node data dict
param data：传递给此树的节点 data dict 的字典

param edge_data: Dictionary passed to the data dict of the edge connecting this tree to its parent
param edge_data：传递给将此树连接到其父级的边的数据字典的字典

Tree.is_leaf()  Tree.is_leaf()
return: If the Tree is a leaf or not.
返回： 树是否为叶子。

Tree.add_children(children)
Tree.add_children(儿童)
Add a list of children to the current children of a Tree.
将 children 列表添加到 Tree 的当前 children 中。

param children: List of Tree objects
param children：Tree 对象列表

Tree.get_edges()  Tree.get_edges()
Get all the edges of the tree in Cytoscape JSON format.
以 Cytoscape JSON 格式获取树的所有边缘。

return: List of dictionaries, each specifying an edge.
返回： 字典列表，每个字典指定一条边。

Tree.get_nodes()  Tree.get_nodes()
Get all the nodes of the tree in Cytoscape JSON format.
以 Cytoscape JSON 格式获取树的所有节点。

return: List of dictionaries, each specifying a node.
返回： 字典列表，每个字典指定一个节点。

Tree.get_elements()  Tree.get_elements()
Get all the elements of the tree in Cytoscape JSON format.
以 Cytoscape JSON 格式获取树的所有元素。

return: List of dictionaries, each specifying an element.
返回： 字典列表，每个字典指定一个元素。

Tree.find_by_id(search_id, method='bfs')
Tree.find_by_id(search_id， method='bfs')
Find a Tree object by its ID.
按 Tree 对象的 ID 查找对象。

param search_id: the queried ID
param search_id：查询的 ID

param method: Which traversal method to use. Either "bfs" or "dfs".
param method：使用哪种遍历方法。“bfs” 或 “dfs” 。

return: Tree object if found, None otherwise.
返回：tree 对象(如果找到)，否则为 None。

Tree.create_index()  Tree.create_index()
Generate the index of a Tree, and set it in place. If there was a previous index, it is erased. This uses a BFS traversal. Please note that when a child is added to the tree, the index is not regenerated. Furthermore, an index assigned to a parent cannot be accessed by its children, and vice-versa.
生成 Tree 的索引，并将其设置到适当的位置。如果存在以前的索引，则会将其擦除。这使用 BFS 遍历。请注意，将子项添加到树中时，不会重新生成索引。此外，分配给父级的索引不能被其子级访问，反之亦然。

return: Dictionary mapping node_id to Tree object.
返回： 字典映射 node_id 到 Tree 对象。