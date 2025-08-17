from drawio_network_plot import NetPlot
import os

def main():
    """
    This example demonstrates the new features of the drawio-network-plot library,
    including custom node attributes (hostname, model, role) and link labels.
    """
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
    output_filename = 'new_features_example.xml'
    output_path = os.path.join(os.path.dirname(__file__), output_filename)
    plot.exportXML(output_path)

    print(f"Diagram '{output_path}' created successfully.")
    print("You can now open this file in Draw.io to see the result.")

if __name__ == "__main__":
    main()
