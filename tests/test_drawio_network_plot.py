import unittest
import xml.etree.ElementTree as ET
from drawio_network_plot import NetPlot

class TestNetPlot(unittest.TestCase):

    def setUp(self):
        """Set up a new NetPlot object for each test."""
        self.plot = NetPlot()

    def test_add_node_with_all_attributes(self):
        """Test adding a single node with all new attributes."""
        self.plot.addNode(
            nodeName='TestRouter',
            nodeType='router',
            hostname='test-router-01',
            model='TestModel 1000',
            role='Core Router'
        )
        xml_string = self.plot.display_xml()
        root = ET.fromstring(xml_string)
        node_xml = root.find(".//*[@id='TestRouter']")
        self.assertIsNotNone(node_xml)
        self.assertIn('<b>TestRouter</b>', node_xml.get('value'))
        self.assertIn('H: test-router-01', node_xml.get('value'))
        self.assertIn('M: TestModel 1000', node_xml.get('value'))
        self.assertIn('R: Core Router', node_xml.get('value'))

    def test_add_link_with_labels(self):
        """Test adding a link with source and target labels."""
        self.plot.addNode(nodeName='NodeA', nodeType='server')
        self.plot.addNode(nodeName='NodeB', nodeType='server')
        self.plot.addLink(
            sourceNodeID='NodeA',
            destinationNodeID='NodeB',
            source_label='eth0',
            target_label='eth1'
        )
        xml_string = self.plot.display_xml()
        root = ET.fromstring(xml_string)
        link_xml = root.find(".//*[@id='NodeA-NodeB']")
        self.assertIsNotNone(link_xml)
        self.assertIn('sourceLabel=eth0', link_xml.get('style'))
        self.assertIn('targetLabel=eth1', link_xml.get('style'))

    def test_add_link_to_nonexistent_node(self):
        """Test that adding a link to a non-existent node does not create a link."""
        self.plot.addNode(nodeName='NodeA', nodeType='server')
        self.plot.addLink(sourceNodeID='NodeA', destinationNodeID='NonExistentNode')
        xml_string = self.plot.display_xml()
        root = ET.fromstring(xml_string)
        link_xml = root.find(".//*[@id='NodeA-NonExistentNode']")
        self.assertIsNone(link_xml)

    def test_add_node_list(self):
        """Test adding a list of nodes."""
        device_list = [
            {'nodeName': 'Router1', 'nodeType': 'router', 'hostname': 'r1', 'model': 'M1', 'role': 'Edge'},
            {'nodeName': 'Switch1', 'nodeType': 'l2_switch', 'hostname': 's1', 'model': 'M2', 'role': 'Access'},
        ]
        self.plot.addNodeList(device_list)
        xml_string = self.plot.display_xml()
        root = ET.fromstring(xml_string)
        router_node = root.find(".//*[@id='Router1']")
        switch_node = root.find(".//*[@id='Switch1']")
        self.assertIsNotNone(router_node)
        self.assertIsNotNone(switch_node)
        self.assertIn('H: r1', router_node.get('value'))
        self.assertIn('H: s1', switch_node.get('value'))

    def test_add_link_list(self):
        """Test adding a list of links."""
        device_list = [
            {'nodeName': 'NodeC', 'nodeType': 'server'},
            {'nodeName': 'NodeD', 'nodeType': 'server'},
        ]
        self.plot.addNodeList(device_list)
        connection_list = [
            {'sourceNodeID': 'NodeC', 'destinationNodeID': 'NodeD', 'source_label': 'p1', 'target_label': 'p2'},
        ]
        self.plot.addLinkList(connection_list)
        xml_string = self.plot.display_xml()
        root = ET.fromstring(xml_string)
        link_xml = root.find(".//*[@id='NodeC-NodeD']")
        self.assertIsNotNone(link_xml)
        self.assertIn('sourceLabel=p1', link_xml.get('style'))
        self.assertIn('targetLabel=p2', link_xml.get('style'))

if __name__ == '__main__':
    unittest.main()
