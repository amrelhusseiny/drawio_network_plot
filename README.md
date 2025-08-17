# Draw.io Network Plotter

## Overview

`drawio-network-plot` is a Python library for programmatically creating Draw.io diagrams of network topologies. It's designed for network automation engineers and anyone who needs to generate network diagrams from code. You can use it to visualize your network infrastructure, whether it's in a data center or a service provider network.

The library generates an XML file that can be directly imported into the Draw.io application (both desktop and web versions) for further editing or exporting to other formats like PNG, SVG, or PDF.

## Features

- **Programmatic Diagram Creation:** Define your network topology in Python and generate a Draw.io diagram from it.
- **Customizable Nodes:** Add nodes to your diagram with specific details:
    - `nodeName`: A unique identifier for the node.
    - `nodeType`: Determines the icon used for the node (e.g., `router`, `l3_switch`, `server`).
    - `hostname`: The hostname of the device.
    - `model`: The hardware model of the device.
    - `role`: The function of the device in the network.
- **Labeled Links:** Connect your nodes with links that can have labels at each end, perfect for showing interface names, IP addresses, or other connection details.
- **Standard Draw.io Shapes:** Uses built-in Cisco icon sets from Draw.io for a professional look.
- **Flexible Output:** Generate the diagram as an XML string or export it directly to a file.

## How It Works

The main component is the `NetPlot` class. Here’s the basic workflow:

1.  **Instantiate `NetPlot`:** Create an instance of the `NetPlot` class to start building your diagram.
2.  **Add Nodes:** Use the `addNode()` method for individual nodes or `addNodeList()` for a batch of nodes. Provide details like `nodeName`, `nodeType`, `hostname`, `model`, and `role`.
3.  **Add Links:** Use the `addLink()` method or `addLinkList()` to connect your nodes. You can add `source_label` and `target_label` to describe the connection points.
4.  **Generate Output:** Get the diagram as an XML string with `display_xml()` or save it to a file with `exportXML()`.

Once you open the generated file in Draw.io, the nodes and links will be stacked. To arrange them automatically, use one of Draw.io's layout options, such as **Arrange > Layout > Vertical Tree**.

## Example

Here's an example of how to create a simple data center topology:

```python
from drawio_network_plot import NetPlot

# Define the nodes in the topology
device_list = [
    # Routers
    {'nodeName': 'Router_1', 'nodeType': 'router', 'hostname': 'edge-router-01', 'model': 'Cisco ASR1000', 'role': 'Internet Gateway'},
    {'nodeName': 'Router_2', 'nodeType': 'router', 'hostname': 'edge-router-02', 'model': 'Cisco ASR1000', 'role': 'Internet Gateway'},
    # Core Switches
    {'nodeName': 'Core_switch_1', 'nodeType': 'l3_switch', 'hostname': 'core-switch-01', 'model': 'Cisco Nexus 9000', 'role': 'Spine'},
    {'nodeName': 'Core_switch_2', 'nodeType': 'l3_switch', 'hostname': 'core-switch-02', 'model': 'Cisco Nexus 9000', 'role': 'Spine'},
    # Leaf Switches
    {'nodeName': 'TOR_1', 'nodeType': 'l2_switch', 'hostname': 'leaf-switch-01', 'model': 'Cisco Nexus 5000', 'role': 'Top-of-Rack'},
    {'nodeName': 'TOR_2', 'nodeType': 'l2_switch', 'hostname': 'leaf-switch-02', 'model': 'Cisco Nexus 5000', 'role': 'Top-of-Rack'},
    # Servers
    {'nodeName': 'Server_1', 'nodeType': 'server', 'hostname': 'web-server-01', 'model': 'Dell PowerEdge', 'role': 'Web Server'},
    {'nodeName': 'Server_2', 'nodeType': 'server', 'hostname': 'db-server-01', 'model': 'Dell PowerEdge', 'role': 'Database Server'},
]

# Define the connections between the nodes
connection_list = [
    # Router to Core
    {'sourceNodeID': 'Router_1', 'destinationNodeID': 'Core_switch_1', 'source_label': 'Gi0/1', 'target_label': 'Eth1/1'},
    {'sourceNodeID': 'Router_1', 'destinationNodeID': 'Core_switch_2', 'source_label': 'Gi0/2', 'target_label': 'Eth1/1'},
    {'sourceNodeID': 'Router_2', 'destinationNodeID': 'Core_switch_1', 'source_label': 'Gi0/1', 'target_label': 'Eth1/2'},
    {'sourceNodeID': 'Router_2', 'destinationNodeID': 'Core_switch_2', 'source_label': 'Gi0/2', 'target_label': 'Eth1/2'},
    # Core to Leaf
    {'sourceNodeID': 'Core_switch_1', 'destinationNodeID': 'TOR_1', 'source_label': 'Eth1/3', 'target_label': 'Eth1/49'},
    {'sourceNodeID': 'Core_switch_1', 'destinationNodeID': 'TOR_2', 'source_label': 'Eth1/4', 'target_label': 'Eth1/49'},
    {'sourceNodeID': 'Core_switch_2', 'destinationNodeID': 'TOR_1', 'source_label': 'Eth1/3', 'target_label': 'Eth1/50'},
    {'sourceNodeID': 'Core_switch_2', 'destinationNodeID': 'TOR_2', 'source_label': 'Eth1/4', 'target_label': 'Eth1/50'},
    # Leaf to Server
    {'sourceNodeID': 'TOR_1', 'destinationNodeID': 'Server_1', 'source_label': 'Eth1/1', 'target_label': 'eth0'},
    {'sourceNodeID': 'TOR_2', 'destinationNodeID': 'Server_2', 'source_label': 'Eth1/1', 'target_label': 'eth0'},
]

# Create a new plot
plot = NetPlot()

# Add the nodes and links
plot.addNodeList(device_list)
plot.addLinkList(connection_list)

# Export the diagram to an XML file
plot.exportXML('datacenter_diagram.xml')

print("Diagram 'datacenter_diagram.xml' created successfully.")
```

## Output

After generating the XML file and applying a layout in Draw.io, your diagram will clearly show the network topology with all the specified details.

*(Note: The previous output image has been removed as it is now outdated. Please generate a new diagram using the updated code to see the new features in action.)*