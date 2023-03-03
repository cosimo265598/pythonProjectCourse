# Python code to implement Conway's Game Of Life
import argparse
from re import T
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON=1
OFF=0
VALUES=[ON,OFF]
N = 128  # size of the one side
PROB=[0.6,0.4] #probabilità della scelta tra Values

class Game(object):
	def __init__(self) -> None:
		self.board=np.random.choice(VALUES, N*N, PROB).reshape(N, N)

	def countNeighbors(self):
		state = self.board
		n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
			state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
			state[2:,1:-1] + state[2:,2:])
		return n

	def checkRulesNeighbors(self):
		n = self.countNeighbors()

		state = self.board

		birth = (n == 3) & (state[1:-1,1:-1] == 0)
		survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)

		state[...] = 0
		state[1:-1,1:-1][birth | survive] = 1

		return state


def animate(frameNum, img, grid, N):
	# update data
	grid.checkRulesNeighbors()
	img.set_data(grid.board)
	return img,

def main():

	g=Game()
	updateInterval=50
	
	#animation
	fig, ax = plt.subplots()
	ax.axis('off')
	img = ax.imshow(g.board, interpolation='nearest')
	ani = animation.FuncAnimation(fig, animate, fargs=(img, g, N, ),
                                frames = 10,
                                interval=updateInterval,
                               save_count=50)
	plt.show()

# call main
if __name__ == '__main__':
	main()
