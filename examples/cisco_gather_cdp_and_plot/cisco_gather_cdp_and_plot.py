from netmiko import ConnectHandler
import re 
from drawio_network_plot.drawio_network_plot import NetPlot

# ----------------- Getting live CDP Neigbors to gather links endpoints ---------------------------
def retieve_lldp_neigbor_hostname(devices_list):
    list_of_cdp_neighborship = []
    for device in devices_list:
        device_dictionary = {
                            'device_type': 'cisco_ios',  
                            'host': device['ip_address'],
                            'username': 'automation',
                            'password' : '1234567',
                        }
        net_connect = ConnectHandler(**device_dictionary)
        output = net_connect.send_command("show cdp neighbor")
        lines_list = output.splitlines()
        for line in lines_list:
            try:
                # regex to search the name of the device before the domain ID ".default" , then removing the word ".default" from the string
                link = {
                            'sourceNodeID' : device['nodeName'],
                            'destinationNodeID' : re.search('\S+\.default',line).group().replace('.default','') 
                            }
                # checking for duplication before adding new link : 
                if {'sourceNodeID':link['destinationNodeID'],'destinationNodeID':link['sourceNodeID']} not in list_of_cdp_neighborship:
                    list_of_cdp_neighborship.append(link)
            except:
                continue
        net_connect.disconnect()
    return list_of_cdp_neighborship

def main():
    # Lab Devices , must have the device type for the plotting library to work 
    devices = [
            {'nodeName':'Router_1','ip_address':'100.0.1.1','nodeType':'router','nodeDescription':'NA'},
            {'nodeName':'Router_2','ip_address':'100.0.1.2','nodeType':'router','nodeDescription':'NA'},
            {'nodeName':'Spine_1','ip_address':'100.0.2.1','nodeType':'l3_switch','nodeDescription':'NA'},
            {'nodeName':'Spine_2','ip_address':'100.0.2.2','nodeType':'l3_switch','nodeDescription':'NA'},
            {'nodeName':'Leaf_1','ip_address':'100.0.3.1','nodeType':'l2_switch','nodeDescription':'NA'},
            {'nodeName':'Leaf_2','ip_address':'100.0.3.2','nodeType':'l2_switch','nodeDescription':'NA'},
            {'nodeName':'Leaf_3','ip_address':'100.0.3.3','nodeType':'l2_switch','nodeDescription':'NA'}
            ]
    # Getting list of links for each device
    list_of_cdp_neighborship = retieve_lldp_neigbor_hostname(devices)
    for peering in list_of_cdp_neighborship:
        print(peering)

    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------
    # ----------------- Main Part : using library to generate XML DrawIIO format ---------------------------
    # Using the Plot library 
    x = NetPlot()
    x.addNodeList(devices)
    x.addLinkList(list_of_cdp_neighborship)

    print(x.display_xml())
    # - You can also directly generate an XML file using the built in function :
    # x.exportXML('examples/output.xml')
    # - You can add node by node and connection by connection : 
    # x.addNode(nodeName='Router_18',nodeType='router')
    # x.addLink('Router_17','Router_18')
    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()