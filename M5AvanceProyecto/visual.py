from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

# Se importa el modelo
from model import CarModel
import random

modeloAgentes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def agent_portrayal(agent):
    colors = ['red', 'green', 'blue']
    rand = random.randint(0, len(colors)-1)
    color = colors[rand]

    if agent.id == 0:
        portrayal = {"Shape": "rect",
                    "Color": 'black',
                    "Filled": "true",
                    "Layer": 0,
                    "w": 1,
                    "h": 1,
                    }
    elif agent.id == 1:
        portrayal = {"Shape": "rect",
                    "Color": 'gray',
                    "Filled": "true",
                    "Layer": 0,
                    "w": 1,
                    "h": 1,
                    }
    elif agent.id == 2:
        portrayal = {"Shape": "circle",
                    "Color": color,
                    "Filled": "true",
                    "Layer": 0,
                    "r": 0.5
                    }
    return portrayal

def wall_portrayal(agent):
    portrayal = {
        'Shape': 'square',
        'Color': 'black',
        'Filled': 'true',
        'Layer': 0,
        'r': 0.5
    }
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(CarModel,
                       [grid],
                       "Simulación ciudad EQUIPO 1",
                       {"n_cars": 5, "n_lights": 5, "width": 10, "height": 10})
                       
server.port = 8521  # Default
server.launch()