
# import libraries
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from .supportingFunctions import *

# Assumptions:
# Amount received in shilling when withdraw occurs
leverage = 1 

# process time
process_lag = 7 # timesteps

# red cross drip amount
drip = 4000

# system initialization
agents = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p']

# system actors
system = ['external','cic']

# chamas
chama = ['chama_1','chama_2','chama_3','chama_4']

# traders
traders = ['ta','tb','tc'] #only trading on the cic. Link to external and cic not to other agents

allAgents = agents + system

mixingAgents = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','external']

UtilityTypesOrdered ={'Food/Water':1,
                    'Fuel/Energy':2,
                    'Health':3,
                    'Education':4,
                    'Savings Group':5,
                    'Shop':6}

utilityTypesProbability = {'Food/Water':0.6,
                    'Fuel/Energy':0.10,
                    'Health':0.03,
                    'Education':0.015,
                    'Savings Group':0.065,
                    'Shop':0.19}


R0 =  500 #thousand xDAI
kappa = 4 #leverage
P0 = 1/100 #initial price
S0 = kappa*R0/P0
V0 = invariant(R0,S0,kappa)
P = spot_price(R0, V0, kappa)

# Price level
priceLevel = 100

fractionOfDemandInCIC = 0.5
fractionOfActualSpendInCIC = 0.5

def create_network():
    # Create network graph
    network = nx.DiGraph()

    # Add nodes for n participants plus the external economy and the cic network
    for i in agents:
        network.add_node(i,type='Agent',tokens=400, native_currency = int(np.random.uniform(low=20, high=500, size=1)[0]))
        
        
    network.add_node('external',type='Contract',native_currency = 100000000,tokens = 0,delta_native_currency = 0, pos=(1,50))
    network.add_node('cic',type='Contract',tokens= S0, native_currency = R0,pos=(50,1))

    for i in chama:
        network.add_node(i,type='Chama')
        
    for i in traders:
        network.add_node(i,type='Trader',tokens=20, native_currency = 20, 
                        price_belief = 1, trust_level = 1)
        
    # Create bi-directional edges between all participants
    for i in allAgents:
        for j in allAgents:
            if i!=j:
                network.add_edge(i,j)

    # Create bi-directional edges between each trader and the external economy and the cic environment            
    for i in traders:
        for j in system:
            if i!=j:
                network.add_edge(i,j)
                
    # Create bi-directional edges between some agent and a chama node representing membershio      
    for i in chama:
        for j in agents:
            if np.random.choice(['Member','Non_Member'],1,p=[.50,.50])[0] == 'Member':
                network.add_edge(i,j)

    # Type colors 
    colors = ['Red','Blue','Green','Orange']
    color_map = []
    for i in network.nodes:
        if network.nodes[i]['type'] == 'Agent':
            color_map.append('Red')
        elif network.nodes[i]['type'] == 'Cloud':
            color_map.append('Blue')
        elif network.nodes[i]['type'] == 'Contract':
            color_map.append('Green')
        elif network.nodes[i]['type'] == 'Trader':
            color_map.append('Yellow')
        elif network.nodes[i]['type'] == 'Chama':
            color_map.append('Orange')
            
    pos = nx.spring_layout(network,pos=nx.get_node_attributes(network,'pos'),fixed=nx.get_node_attributes(network,'pos'),seed=10)
    nx.draw(network,node_color = color_map,pos=pos,with_labels=True,alpha=0.7)
    plt.savefig('images/graph.png')
    plt.show()
    return network