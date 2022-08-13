# drawio_network_plot
## Overview
- Package is mainly created for Network Automation , can be used in conjunction with other libraries to generate DrawIO plot for your Network (Service Provider ot Data Centter Network).
- Available devices : Router , L3_Switch , L2_switch , Firewall , Server ( More to be added )
- Output generated can be directly opened by DrawIO application (Desktop or Web version)

## Understanding the logic 
The "NetPlot" class is itself the plot , you initiate it and then you can do the following : 
- Add a Node or a Nodes list .
- Add an Edge or a list of Edges .
>Note : the edges has Source and Destination nodes , better to always put the Parent device in the Source node and the Child node in the Destination node , this will affect the way DrawIO does automatic Layouts .
