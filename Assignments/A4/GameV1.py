# Python code to implement Conway's Game Of Life
import argparse
from re import T
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON=1
OFF=0
VALUES=[ON,OFF]
N = 100  # size of the one side
PROB=[0.4,0.6] #probabilità della schelata tra Values

def generateMatrix():
    return np.random.choice(VALUES, N*N, PROB).reshape(N, N)
        
def update(frameNum, img, grid, N):

	# copy grid since we require 8 neighbors
	# for calculation and we go line by line
	newGrid = grid.copy()
	for i in range(N):
		for j in range(N):

			# compute 8-neighbor sum
			# using toroidal boundary conditions - x and y wrap around
			# so that the simulation takes place on a toroidal surface.
			total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

			# apply Conway's rules
			if grid[i, j] == ON:
				if (total < 2) or (total > 3):
					newGrid[i, j] = OFF
			else:
				if total == 3:
					newGrid[i, j] = ON

	# update data
	img.set_data(newGrid)
	grid[:] = newGrid[:]
	return img,

# main() function
def main():
    updateInterval = 50
    grid=generateMatrix()

    beacon = [[1, 1, 0, 0],
				[1, 1, 0, 0],
				[0, 0, 1, 1],
				[0, 0, 1, 1]]


    padded = np.pad(beacon, pad_width=1, mode='edge')
    # Define matrices for neighboring pixels
    beacon=np.array([[1, 1, 0, 1],
				[0, 1, 0, 0],
				[0, 0, 1, 1],
				[1, 0, 1, 0]])
	
    center	= beacon[1:-1, 1:-1] # reference pixel
    top 	= beacon[:-2, 1:-1] 	# previous row, same column
    bottom 	= beacon[2:, 1:-1] 	# next row, same column
    left 	= padded[1:-1, :-2] 	# same row, previous column
    right 	= padded[1:-1, 2:] 	# previous row, next column

    #print(padded)
    #print(center)
    #print(top)
    #print(bottom)
    #print((center + top + bottom + left + right) / 5)
    #a= (beacon[0:-2,0:-2] + beacon[0:-2,1:-1] + beacon[0:-2,2:] + beacon[1:-1,0:-2] + beacon[1:-1,2:] + beacon[2:,0:-2] + beacon[2:,1:-1] + beacon[2:,2:])

    #a=(beacon[1:-1, 1:-1] +beacon[:-2, 1:-1] + beacon[2:, 1:-1]+ beacon[1:-1, :-2]+ beacon[1:-1, 2:])
    #print(beacon[1:-1, 1:-1])

    print(beacon)
    print(beacon[:3, :3])
    padded = np.pad(beacon[0:-2,0:-2], pad_width=1, mode='constant', constant_values=0)
    print(padded[0:-2,0:-2])
    print(np.sum(padded[0:-2,0:-2]))
	#animation
    #fig, ax = plt.subplots()
    #img = ax.imshow(grid, interpolation='nearest')
    #ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
    #                            frames = 10,
    #                            interval=updateInterval,
    #                           save_count=50)
    #plt.show()

# call main
if __name__ == '__main__':
	main()