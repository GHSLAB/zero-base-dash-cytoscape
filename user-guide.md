https://dash.plotly.com/cytoscape

## Dash Cytoscape User Guide
### Reference
A comprehensive list of all of the Cytoscape properties.

### Basic Usage & Elements
Overview of element declaration and manipulation.

### Layouts
Description of built-in layouts, and how to modify their properties. These include:

- Display Methods
- Fine-tuning the Layouts
- Physics-based Layouts
- Loading External Layout

### Styling
Methods to style elements with a CSS-like syntax. These include:

- The stylesheet parameter
- Basic selectors and styles
- Comparing data items using selectors
- Styling edges
- Displaying Images

### Callbacks
Methods to combine Dash callbacks to update your Cytoscape object. These include:

- Changing Layouts
- Interactively update styles
- Adding and removing elements

### Events and User Interactions
Overview of user-interaction events that trigger callbacks in Dash, and how to use them to update the Cytoscape component.

- Simple callback construction
- Click, tap and hover
- Selecting multiple elements
- Advanced usage of callbacks

### Biopython Examples
Examples of applications in bioinformatics using Biopython. These include:

- Parsing the Phylo object
- Defining layout and stylesheet
- Layout and Callbacks

### Exporting Images
This example shows how to export your Cytoscape graphs as images (jpg, png, svg).

### Making responsive graphs
This example shows how to build a responsive Cytoscape graph.

-----

# GUIDE

## Element Declaration
Each element is defined by a dictionary declaring its purpose and describing its properties. Usually, you specify what group the element belongs to (i.e., if it's a node or an edge), indicate what position you want to give to your element (if it's a node), or what data it contains. In fact, the data and position keys are themselves mapped to dictionaries, where each item specify an aspect of the data or position.

In the case of data, the typical keys fed to the dictionaries are:

- id: The index of the element, useful when you want to reference it
- label: The name associated with the element if you wish to display it

If your element is an edge, the following keys are required in your data dictionary:

- source: The id of the source node, which is where the edge starts
- target: The id of the target node, where the edge ends

The position dictionary takes as items the x and y position of the node. If you use any other layout than preset, or if the element is an edge, the position item will be ignored.

If we want a graph with two nodes, and an edge connecting those two nodes, we effectively need three of those element dictionaries, grouped as a list:

Notice that we also need to specify the id, the layout, and the style of Cytoscape. The id parameter is needed for assigning callbacks, style lets you specify the CSS style of the component (similarly to core components), and layout tells you how to arrange your graph. It is described in depth in part 2, so all you need to know is that 'preset' will organize the nodes according to the positions you specified.

The official Cytoscape.js documentation nicely outlines the JSON format for declaring elements.

### Boolean Properties
In addition to the properties presented above, the element dictionary can also accept boolean items that specify its state. We extend the previous example in the following way:

> ote that those boolean properties can be overwritten by certain Cytoscape parameters such as autoungrabify or autounselectify. Please refer to the reference for more information.


### Classes
Similarly to CSS classes, element classes are used to style groups of elements using a selector. We modify the previous example by giving the elements a class or multiple classes (separated by a space), and define a stylesheet that modifies the elements based on those classes.