from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)
    a_path = {}
    while not open_list.empty():
        currCell = open_list.get()[1]
        if currCell == goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E': child=(currCell[0],currCell[1]+1)
                if d=='W': child=(currCell[0],currCell[1]-1)
                if d=='N': child=(currCell[0]-1,currCell[1])
                if d=='S': child=(currCell[0]+1,currCell[1])
                temp_g = g_score[currCell]+1
                temp_f = temp_g + h(child, goal)
                if temp_f < f_score[child]:
                    g_score[child] = temp_g
                    f_score[child] = temp_f
                    open_list.put((temp_f, child))
                    a_path[child] = currCell
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[a_path[cell]] = cell
        cell = a_path[cell]
    return fwdPath

if __name__ == "__main__":
    m = maze(10, 10)
    m.CreateMaze(theme=COLOR.dark)
    start = (m.rows, m.cols)
    goal = (1,1)
    path = aStar(m, start, goal)
    a = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: path})
    l = textLabel(m, 'A* Path Length', len(path)+1)
    m.run()
