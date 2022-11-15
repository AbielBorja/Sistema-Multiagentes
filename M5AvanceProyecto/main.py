'''
M5. Revisión de Avance

Fecha de Creación: 16 de noviembre, 2021
'''

import numpy as np
import random
import time

# Create Board
# De momento tengo un board setteado y no aleatorio
def create_board(rows, cols):
  '''
  0: Walls
  1: Road
  letras: Estacionamiento
  '''
  board = np.zeros((rows, cols), dtype=object)

  a = [0, 0, 0, 0, 0]
  b = [0, 1, 1, 0, 0]
  c = [1, 0, 0, 1, 1]

  board[2][1] = 'a'
  board[2][8] = 'b'
  board[6][8] = 'c'

  '''
  https://www.pythonpool.com/python-string-to-variable-name/

  https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string

  Para checar lo de los estacionamientos y el char usamos:

  #input String
  str = "a" # b o c
  
  #apply exec() method
  exec("%s = %d" % (str,aqui va el array))
  
  #print string
  print("output : ",Pythonpool)

  o

  a = [0, 0, 0, 0, 0]
  f'{a=}'.split('=')[0] este compara con una string
  '''

  x, y = 0, 0

  # Se llena el board
  while x < rows:
    while y < cols:
      if (x == 0 or x == 3 or x == 5 or x == 9) or (y == 4 or y == 5) or ((x == 1 or x == 2 or x == 6 or x == 7 or x == 8) and (y == 0 or y == 9)):
        board[x][y] = 1
      y += 1
    x += 1
    y = 0

  return board

# Initialize Agents
def init_agents(board, n_cars, n_lights):
  rows, cols = board.shape

  # Car Positions
  cars = np.ones((n_cars, 2), dtype=int)
  
  # Lights Positions
  lights = np.zeros((n_lights, 2), dtype=int)

  # pos
  arr = [[2,3], [6,6]]

  for i in range(len(lights)):
    lights[i] = arr[i]

  '''
  # Luces en lugares random por el momento
  for i in range(n_lights):
    x = random.randint(0, rows-1)
    y = random.randint(0, cols-1)

    pos = [x, y]

    while pos in lights:
      x = random.randint(0, rows-1)
      y = random.randint(0, cols-1)
      pos = [x, y]

    lights[i] = [x, y]
  '''
  return cars, lights

# Check Moves
def check_move():
  # movimiento random si hay mas de dos posiciones disponibles a mover
  return "no se"

# Play
def play():
  return ":0"

# Main
def main():
  print('\n--Start Simulation--')
  n_cars = 5
  n_lights = 2
  rows, cols = 10, 10

  print(f'Creating Board ({rows} x {cols})')
  board = create_board(rows, cols)
  print(board)

  print(f'\nInitialize Agents (Number of Cars: {n_cars}), (Number of Traffic Lights: {n_lights})')
  cars, lights = init_agents(board, n_cars, n_lights)
  print("Cars\n", cars)
  print("\nLights\n", lights)

if __name__ == '__main__':
  main()