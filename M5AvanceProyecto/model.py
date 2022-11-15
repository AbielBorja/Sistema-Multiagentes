from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

import random

# Agent class
class CarAgent(Agent):
    # Creates an agent with an unique_id and a fixed wealth
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.steps = 0
        self.id = 2

    ''' FUNCIONES MOVIMIENTO '''
    # Creates the agent action (step)
    def step(self):
        self.move()
        self.steps += 1

    # Creates the algorithm to move the agent
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    '''
    # Funcion Accion
    # Creates the algorithm to give money to another agent in the same cell
    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
    '''

class Road(Agent):
    # Creates an agent with an unique_id and a fixed wealth
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.id = 1

class Wall(Agent):
    # Creates an agent with an unique_id and a fixed wealth
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.id = 0

# Model class
class CarModel(Model):
    # Creates a model with N agents
    def __init__(self, n_cars, n_lights, width, height):
        self.running = True
        self.n_cars = n_cars
        self.n_lights = n_lights
        
        self.schedule = RandomActivation(self)

        self.grid = MultiGrid(width, height, torus=True)
        print(self.grid)
        self.datacollector = DataCollector(
            agent_reporters={"Steps": lambda a: a.steps})
        
        # Create borders
        for x in range(width):
            for y in range(height):
                if (y == 0 or y == 3 or y == 5 or y == 9) or (x == 4 or x == 5) or ((y == 1 or y == 2 or y == 6 or y == 7 or y == 8) and (x == 0 or x == 9)):
                    pass
                else:
                    wall = Wall(x, self)
                    self.grid.place_agent(wall, (x,y))

        # Create agents and attributes an action (schedule) and position in the grid
        for i in range(self.n_cars):
            a = CarAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            while not (self.grid.is_cell_empty((x, y))):
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))


    # Advance the model by one step
    def step(self):
        #self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n):
        for i in range(n):
            self.step()
