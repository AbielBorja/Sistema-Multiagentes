from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

# Se importa el modelo
from MoneyModel import MoneyModel

modeloAgentes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

'''
# Agentes del mismo color
def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    return portrayal
'''

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal

chart = ChartModule([{"Label": "Gini",
                    "Color": "Black"}],
                    data_collector_name = 'datacollector')


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(MoneyModel,
                       [grid, chart],
                       "Simulación ciudad EQUIPO 1",
                       {"N": 100, "width": 10, "height": 10})
server.port = 8521  # Default
server.launch()