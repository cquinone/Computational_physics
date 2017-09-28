from Tkinter import *
import random 
import pdb
#make grid, for each cellgrab coords and where to go, finish loops and update grid based on big_c
#then ask if you want another step

def draw(canvas, w, h, grid,tot_step):
	maxcellnum = (11*tot_step)+(11*10)
	minnum = 0
	#mycolor = '#%02x%02x%02x' % (255, 0, 255)
	#canvas.create_rectangle(1, 1, 1+w, 1+h, fill=mycolor)
	ox = 1
	for col in grid:
		oy = 1
		for cell in col:
			c_pct = sum(cell)/240
			#print "c_pct:", c_pct
			mycolor = '#%02x%02x%02x' % (c_pct*(255), 0, 0)
			canvas.create_rectangle(ox, oy, ox+w, oy+h, fill=mycolor)
			#print "color, c_pct: ", mycolor, c_pct
			oy = oy + h
			#assign color to c_sum
		ox = ox + w


def update(grid, big_c):
	#print "here: ", big_c[0]
	for element in big_c:
		#print "element: ", element
		x_coord = element[1][0]
		y_coord = element[1][1]
		#print "looking at: ", grid[x_coord][y_coord]
		grid[x_coord][y_coord].remove(element[0])

	for element in big_c:
		x_coord = element[1][0]
		y_coord = element[1][1]	
		if element[2] == "u":
			grid[x_coord][y_coord-1].append(element[0])
		if element[2] == "d":
			grid[x_coord][y_coord+1].append(element[0])
		if element[2] == "r":
			grid[x_coord+1][y_coord].append(element[0])
		if element[2] == "l":
			grid[x_coord-1][y_coord].append(element[0])

	return grid

def hottest_coord(grid, cell, col_count, cell_count):
	direcs=["u","d","l","r"]
	max_n = max(cell)

	#check 4 ones around, and pick dir based on lowest sum:
	#pdb.set_trace()
	if col_count == 9:
		direcs.remove("r")
	if col_count == 0:
		direcs.remove("l")
	if cell_count == 0:
		direcs.remove("u")
	if cell_count == 9:
		direcs.remove("d")
	neighbors=[]
	min_neigh = 0
	for dir in direcs:
		if dir == "u":
			neighbors.append(sum(grid[col_count][cell_count-1]))
		if dir == "d":
			neighbors.append(sum(grid[col_count][cell_count+1]))
		if dir == "l":
			neighbors.append(sum(grid[col_count-1][cell_count]))
		if dir == "r":
			neighbors.append(sum(grid[col_count+1][cell_count]))
		min_neigh = min(neighbors)
		if min_neigh == neighbors[-1]:
			direc = dir
	#direc = random.choice(direcs)
	#if col_count == 0 and direc == "l":
	#	direc = "r"
	#if cell_count == 0 and direc == "u":
	#	direc = "d"
	#if col_count == 9 and direc == "r":
	#	direc = "l"
	#if cell_count == 9 and direc == "d":
	#	direc = "u"
	#print "dir: ", direc
	return [max_n,[col_count,cell_count],direc]


random.seed()
#make grid
grid = []
r = raw_input("random ? ")
if r == "yes" :
	for i in range(10):
		grid.append([])
	for col in grid:
		for i in range(1,11):
			tennum=[]
			for j in range(10):
				tennum.append(random.randint(1,10)+random.random())
			col.append(tennum)
else:
	for i in range(10):
		#make columns
		grid.append([])
	for col in grid:
		for j in range(1,11):
			#ten lists per column
			tennum=[]
			for k in range(10):
				if k % 2 == 0:
					print "did one", k
					tennum.append(random.randint(1,10)+random.random())
			col.append(tennum)



col_count = -1
tot_step = 0
while True:
	big_c=[]
	if tot_step % 500 == 0:
		step = raw_input("Step: ")
		if step == "no":
			break
	print tot_step
	tot_step = tot_step + 1	
	#if tot_step == 11:
	#	print "max steps reached: ", tot_step-1
	#	print ""
	#	break
	for col in grid:
		cell_count = -1
		col_count = col_count + 1
		for cell in col:
			if len(cell) < 2:
				print "skipping"
				cell_count = cell_count + 1
				continue
			cell_count = cell_count + 1
			#print "grid cell: ", grid[col_count][cell_count]
			#print "cell: ", cell
			#print ""
			big_c.append(hottest_coord(grid, cell, col_count, cell_count)) #list of tuples, 3 items -- num, grid coords, where to go coords
	col_count = -1
	grid = update(grid, big_c)	


print "visualizing...."
print ""
root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
draw(canvas, 50, 50,grid, tot_step)
root.mainloop()
#HERE WE WANT TO MAKE SOMEHTING TO COLOR THE CELLS ACCORDING TO TOTAL= LARGER IS REDDER, LOWER IS BLUER