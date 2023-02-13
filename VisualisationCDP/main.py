from pyvis.network import Network
from sys import argv
import json

switches = {}

file = argv[1]

with open (file + '.json', 'r') as f:
    switchesJSON = f.read()

switches = json.loads(switchesJSON)

net = Network('900px', '1500px')  # создаём объект графа

colorsArray = {'Cisco C921-4P':'#900020',
               'cisco WS-C2960CX-8PC-L':'#425E17',
               'Rocket Prism 5AC Gen2':'#D5713F'
               }
#color = '#00ff1e'
i = 0
# добавление узлов
'''net.add_nodes(
    [1, 2, 3, 4, 5],  # node ids
    label=['Node #1', 'Node #2', 'Node #3', 'Node #4', 'Node #5'],  # node labels
    # node titles (display on mouse hover)
    title=['Main node', 'Just node', 'Just node', 'Just node', 'Node with self-loop'],
    color=['#d47415', '#22b512', '#42adf5', '#4a21b0', '#e627a3']  # node colors (HEX)
)'''
for switch in switches:
    i += 1
    label = switches[switch]['ip'] + "\r\n" + switch
    sns = ''
    if switches[switch]['systemSerialNumbers']:
        sns += '\r\nserial num:'
        for sn in switches[switch]['systemSerialNumbers']:
            sns += '\r\n' + sn
    mns = ''
    if switches[switch]['motherboardSerialNumbers']:
        mns += '\r\nmotherboard:'
        for sn in switches[switch]['motherboardSerialNumbers']:
            mns += '\r\n' + sn
    title = switches[switch]['platform'] + sns + mns
    net.add_node(i, label = label, title = title)
    #print(net.nodes)
    if switches[switch]['platform'] in colorsArray:
        net.nodes[len(net.nodes) - 1]['color'] = colorsArray[switches[switch]['platform']]
        #print(len(net.nodes))
        #t = 1
    
    
    switches[switch]['index'] = i

# добавляем тот же список узлов, что и в предыдущем примере, добовляем ребра
'''net.add_edges([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)])'''
for switch in switches:
    for interface in switches[switch]['interfaces']:
        #print(switches[switch]['interfaces'][interface])
        for remoteSwitch in switches[switch]['interfaces'][interface]:
            if remoteSwitch in switches:
                title = interface + " " + switches[switch]['interfaces'][interface][remoteSwitch]
                net.add_edge(switches[switch]['index'], switches[remoteSwitch]['index'], title = title)
        



#net.barnes_hut()
net.show_buttons(filter_=['physics'])
net.show(file + '.html')  # save visualization in 'graph.html'