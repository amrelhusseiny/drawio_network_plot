import xml.etree.ElementTree as ET

class NetPlot():
    def __init__(self):
        # Following defintions are neccessary to build the DrawIO template XML File : 
        # ------ Template Start ------ 
        self.mxfile = ET.Element('mxfile',host="Electron",agent="5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/19.0.0 Chrome/100.0.4896.160 Electron/18.3.2 Safari/537.36",type="device")
        self.diagram = ET.SubElement(self.mxfile,'diagram',id="diagram_1",name="Page-1")
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
        self.root = ET.SubElement(self.mxGraphModel,'root')
        self.mxCellID0 = ET.SubElement(self.root,'mxCell' , id="0")
        self.mxCellID1 = ET.SubElement(self.root,'mxCell' , id="1" , parent="0" , style=";html=1;") 
        # ------ Template End ------ 

    def _getMXgraphShape(self,nodeType):
        if nodeType == 'router':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=router;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50'}
        elif nodeType == 'l2_switch':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=l2_switch;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50'}
        elif nodeType == 'l3_switch':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=l3_switch;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50'}
        elif nodeType == 'firewall':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=firewall;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'64',
                    'height':'50'}
        elif nodeType == 'server':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=server;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'27',
                    'height':'50'}
        else : # Default if no shape selected
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=server;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'27',
                    'height':'50'}

    def addNode(self,nodeName,nodeDescription='',nodeType=''):
        shapeParameters = self._getMXgraphShape(nodeType)
        UserObject = ET.SubElement(self.root,
                            'UserObject', 
                            label=nodeName, 
                            Hostname=nodeName , 
                            Description=nodeDescription , 
                            placeholders="1",
                            id=nodeName)
        mxCell = ET.SubElement(UserObject,
                                'mxCell', 
                                style=("verticalLabelPosition=bottom;"
                                        "html=1;"
                                        "verticalAlign=top;"
                                        "aspect=fixed;align=center;"
                                        "pointerEvents=1;"
                                        f"{shapeParameters['style']}" # Shape is same for the whole Cisco19 library 
                                        ""),
                                parent="1",
                                vertex="1")
        mxGeometry = ET.SubElement(mxCell, 'mxGeometry',width=shapeParameters['width'] ,height=shapeParameters['height'] )
        mxGeometry.set('as','geometry')

    def addNodeList(self,nodeListOfDictionary):
        for node in nodeListOfDictionary:
            self.addNode(nodeName=node['nodeName'],nodeDescription=node['nodeDescription'],nodeType=node['nodeType'])
        return

    def addLink(self,sourceNodeID,destinationNodeID):
        mxCell = ET.SubElement(self.root,
                                'mxCell',
                                id=sourceNodeID+destinationNodeID, # temp ID suitable for single link scenario
                                value="",
                                style="endFill=0;endArrow=none;",
                                parent="1",
                                source=sourceNodeID,
                                target=destinationNodeID,
                                edge="1")
        mxGeometry = ET.SubElement(mxCell, 'mxGeometry')
        mxGeometry.set('as','geometry')

    def addLinkList(self,linkListOfDictionary):
        for link in linkListOfDictionary:
            self.addLink(sourceNodeID=link['sourceNodeID'] , destinationNodeID=link['destinationNodeID'] )
        return

    def display_xml(self):
        return ET.tostring(self.mxfile)   



    




















