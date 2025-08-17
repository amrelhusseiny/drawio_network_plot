import xml.etree.ElementTree as ET
import logging


class NetPlot:
    """
    A class to create Draw.io diagrams for network topologies.

    This class provides methods to add nodes and links, and then generate
    an XML file that can be opened and edited in Draw.io. It is designed
    to be used for network automation tasks, allowing for the programmatic
    creation of network diagrams.
    """
    def __init__(self):
        """
        Initializes the NetPlot object and creates the basic XML structure for a Draw.io file.
        """
        # Basic Draw.io file structure
        self.mxfile = ET.Element('mxfile', host="draw.io", type="device")
        self.diagram = ET.SubElement(self.mxfile, 'diagram', id="diagram_1", name="Page-1")
        self.mxGraphModel = ET.SubElement(self.diagram,
                                            'mxGraphModel',
                                            grid="1",
                                            gridSize="10",
                                            guides="1",
                                            tooltips="1",
                                            connect="1",
                                            arrows="1",
                                            fold="1",
                                            page="1",
                                            pageScale="1",
                                            pageWidth="850",
                                            pageHeight="1100",
                                            math="0",
                                            shadow="0")
        self.root = ET.SubElement(self.mxGraphModel, 'root')
        ET.SubElement(self.root, 'mxCell', id="0")
        ET.SubElement(self.root, 'mxCell', id="1", parent="0", style=";html=1;")

    def _getMXgraphShape(self, nodeType):
        """
        Returns the shape parameters for a given node type.
        This method defines the visual style of the nodes in the diagram.
        :param nodeType: The type of the node.
        :return: A dictionary with shape parameters.
        """
        shapes = {
            'router': {'prIcon': 'router', 'width': '50', 'height': '50', 'nodeLevel': '1'},
            'l2_switch': {'prIcon': 'l2_switch', 'width': '50', 'height': '50', 'nodeLevel': '3'},
            'l3_switch': {'prIcon': 'l3_switch', 'width': '50', 'height': '50', 'nodeLevel': '2'},
            'firewall': {'prIcon': 'firewall', 'width': '64', 'height': '50', 'nodeLevel': '2'},
            'server': {'prIcon': 'server', 'width': '27', 'height': '50', 'nodeLevel': '4'},
        }

        default_shape = {'prIcon': 'server', 'width': '27', 'height': '50', 'nodeLevel': '4'}
        shape_params = shapes.get(nodeType, default_shape)

        shape_params['style'] = (
            f"shape=mxgraph.cisco19.rect;prIcon={shape_params['prIcon']};"
            "fillColor=#FAFAFA;strokeColor=#005073;html=1;"
        )
        return shape_params

    def addNode(self, nodeName, nodeType='', hostname='', model='', role=''):
        """
        Adds a single node to the diagram.
        :param nodeName: The name of the node (must be unique).
        :param nodeType: The type of the node (e.g., 'router', 'l2_switch').
        :param hostname: The hostname of the device.
        :param model: The model of the device.
        :param role: The role of the device.
        """
        try:
            shapeParameters = self._getMXgraphShape(nodeType)

            value = f"<b>{nodeName}</b>"
            if hostname:
                value += f"<br>H: {hostname}"
            if model:
                value += f"<br>M: {model}"
            if role:
                value += f"<br>R: {role}"

            mxCell = ET.SubElement(self.root,
                                    'mxCell',
                                    id=nodeName,
                                    value=value,
                                    style=("verticalLabelPosition=bottom;"
                                            "html=1;"
                                            "verticalAlign=top;"
                                            "aspect=fixed;align=center;"
                                            "pointerEvents=1;"
                                            f"{shapeParameters['style']}"
                                            ""),
                                    parent="1",
                                    vertex="1")
            mxGeometry = ET.SubElement(mxCell, 'mxGeometry', width=shapeParameters['width'], height=shapeParameters['height'])
            mxGeometry.set('as', 'geometry')
        except Exception as e:
            logging.error(f'Error in adding Node: {e}')

    def addNodeList(self, nodeListOfDictionary):
        """
        Adds a list of nodes to the diagram from a list of dictionaries.
        :param nodeListOfDictionary: A list of dictionaries, where each dictionary represents a node.
        """
        try:
            for node in nodeListOfDictionary:
                self.addNode(
                    nodeName=node['nodeName'],
                    nodeType=node.get('nodeType', ''),
                    hostname=node.get('hostname', ''),
                    model=node.get('model', ''),
                    role=node.get('role', '')
                )
        except KeyError as e:
            logging.error(f"Missing required key in node dictionary: {e}")
        except Exception as e:
            logging.error(f'Error in adding Node List: {e}')

    def addLink(self, sourceNodeID, destinationNodeID, source_label='', target_label=''):
        """
        Adds a single link (edge) between two nodes.
        :param sourceNodeID: The ID of the source node.
        :param destinationNodeID: The ID of the destination node.
        :param source_label: The label to display at the source end of the link.
        :param target_label: The label to display at the target end of the link.
        """
        try:
            # Check if nodes exist before creating a link
            source_node = self.root.find(f".//mxCell[@id='{sourceNodeID}']")
            dest_node = self.root.find(f".//mxCell[@id='{destinationNodeID}']")

            if source_node is None:
                logging.warning(f"Source node '{sourceNodeID}' not found for link. Skipping.")
                return
            if dest_node is None:
                logging.warning(f"Destination node '{destinationNodeID}' not found for link. Skipping.")
                return

            style = "endFill=0;endArrow=none;html=1;"
            if source_label:
                style += f"sourceLabel={source_label};"
            if target_label:
                style += f"targetLabel={target_label};"

            mxCell = ET.SubElement(self.root,
                                    'mxCell',
                                    id=f"{sourceNodeID}-{destinationNodeID}",
                                    style=style,
                                    parent="1",
                                    source=sourceNodeID,
                                    target=destinationNodeID,
                                    edge="1")
            mxGeometry = ET.SubElement(mxCell, 'mxGeometry')
            mxGeometry.set('as', 'geometry')
        except Exception as e:
            logging.error(f'Error in adding Link: {e}')

    def addLinkList(self, linkListOfDictionary):
        """
        Adds a list of links to the diagram from a list of dictionaries.
        :param linkListOfDictionary: A list of dictionaries, where each dictionary represents a link.
        """
        try:
            for link in linkListOfDictionary:
                self.addLink(
                    sourceNodeID=link['sourceNodeID'],
                    destinationNodeID=link['destinationNodeID'],
                    source_label=link.get('source_label', ''),
                    target_label=link.get('target_label', '')
                )
        except KeyError as e:
            logging.error(f"Missing required key in link dictionary: {e}")
        except Exception as e:
            logging.error(f'Error in adding Link List: {e}')

    def display_xml(self):
        """
        Returns the XML content of the diagram as a string.
        :return: A string containing the XML for the diagram.
        """
        return ET.tostring(self.mxfile, encoding='unicode')

    def exportXML(self, filePath):
        """
        Exports the diagram to an XML file.
        :param filePath: The path to the output XML file.
        """
        with open(filePath, 'w') as file:
            xml_string = self.display_xml()
            file.write(xml_string)

    def __repr__(self):
        """
        Returns the XML content of the diagram when the object is printed.
        """
        return self.display_xml()