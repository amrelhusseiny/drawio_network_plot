import xml.etree.ElementTree as ET
 
class NetPlot():
    '''
        Creates the DrawIO Plot XML file , based on Jgraph template
    '''
    def __init__(self):
        # initiating the blocks needed for the DrawIO XML template , standard in every plot
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
        # Each Node and Edge are a child to the Parent id "1" 
        self.mxCellID1 = ET.SubElement(self.root,'mxCell' , id="1" , parent="0" , style=";html=1;") 

    def _getMXgraphShape(self,nodeType):
        # Defining the shape that can be used , it uses shapes already shipped with DrawIO application (More shapes will be added)
        # we are also using the "nodeLevel" variable to set the hirarichy of the plot if standards are not adhered by in using library
        if nodeType == 'router':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=router;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50',
                    'nodeLevel':'1'
                    }
        elif nodeType == 'l2_switch':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=l2_switch;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50',
                    'nodeLevel':'3'}
        elif nodeType == 'l3_switch':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=l3_switch;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'50',
                    'height':'50',
                    'nodeLevel':'2'}
        elif nodeType == 'firewall':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=firewall;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'64',
                    'height':'50',
                    'nodeLevel':'2'}
        elif nodeType == 'server':
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=server;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'27',
                    'height':'50',
                    'nodeLevel':'4'}
        else :
            return {'style':'shape=mxgraph.cisco19.rect;prIcon=server;fillColor=#FAFAFA;strokeColor=#005073;html=1;',
                    'width':'27',
                    'height':'50',
                    'nodeLevel':'4'}


    def addNode(self,nodeName,nodeDescription='',nodeType=''):
        shapeParameters = self._getMXgraphShape(nodeType)
        mxCell = ET.SubElement(self.root,
                                'mxCell', 
                                id=nodeName,
                                value=nodeName,
                                style=("verticalLabelPosition=bottom;"
                                        "html=1;"
                                        "verticalAlign=top;"
                                        "aspect=fixed;align=center;"
                                        "pointerEvents=1;"
                                        f"{shapeParameters['style']}"
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
        try: 
            for mxCell in self.root:
                print(mxCell.attrib['id'])
                print(type(mxCell.attrib['id']))
                print(sourceNodeID)
                print(type(sourceNodeID))
                if mxCell.attrib['id'] == sourceNodeID:
                    print('Element found' + {mxCell.attrib['id']})
                    break
            return
        except Exception as e:
            print(e)
        mxCell = ET.SubElement(self.root,
                                'mxCell',
                                id=sourceNodeID+destinationNodeID,
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

    def exportXML(self, filePath):
        with open(filePath,'wb') as file:
            tree = ET.ElementTree(self.mxfile)
            tree.write(file)
        return

    def __repr__(self):
        return str(self.display_xml())



    




















