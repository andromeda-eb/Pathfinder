'''
    g score: distance travelled from start node to current node
    f score: distance travelled + distance to goal
'''
from queue import PriorityQueue, Queue

#manhatten
def get_distance(pos1, pos2):
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    return distance * 10

def draw_shortest_path(draw, grid, parents, end):
    parent = end

    while parent in parents:
        grid[parent[0]][parent[1]].set_shortest_path()
        parent = parents[parent]

    draw()

def breadth_first(window, draw, grid, start, end):
    queue = Queue()
    open_set = set()
    closed_set = set()
    queue.put(start)
    open_set.add((start))
    g_cost = { (i,j) : float("inf") for i in range(len(grid)) for j in range(len(grid[i]))}
    parents = {}
    g_cost[start] = 0

    while not queue.empty():
        current = queue.get()

        if current in closed_set:
            continue

        open_set.remove(current)
        closed_set.add(current)
        node = grid[current[0]][current[1]]

        if current == end:
            grid[start[0]][start[1]].set_shortest_path()
            draw_shortest_path(draw, grid, parents, end)
            break

        node.set_neighbours(grid)
        neighbours = node.get_neighbours()

        for cost, coords in neighbours:
            neighbour = grid[coords[0]][coords[1]]

            temp_g = g_cost[current] + cost
            # update parents for shortest path
            if temp_g < g_cost[coords]:
                g_cost[coords] = temp_g
                parents[coords] = current
            # add to queue if not already encountered
            if coords not in closed_set and coords not in open_set:
                queue.put(coords)

                if coords != end:
                    neighbour.set_open()

                open_set.add( ( coords ) )

            draw()

            node.set_closed()

# same as BFS but with stack data structure
def depth_first(window, draw, grid, start, end):
    stack = []
    open_set = set()
    closed_set = set()
    stack.append(start)
    open_set.add( (start) )
    g_cost = { (i,j) : float("inf") for i in range(len(grid)) for j in range(len(grid[i]))}
    parents = {}
    g_cost[start] = 0

    while len(stack) > 0:
        current = stack.pop()

        if current in closed_set:
            continue

        open_set.remove(current)
        closed_set.add(current)
        node = grid[current[0]][current[1]]
        node.set_closed()

        if current == end:
            grid[start[0]][start[1]].set_shortest_path()
            draw_shortest_path(draw, grid, parents, end)
            break

        node.set_neighbours(grid)
        neighbours = node.get_neighbours()

        for cost, coords in neighbours:
            neighbour = grid[coords[0]][coords[1]]

            temp_g = g_cost[current] + cost

            if temp_g < g_cost[coords]:
                g_cost[coords] = temp_g
                parents[coords] = current

            if coords not in closed_set and coords not in open_set:
                stack.append(coords)

                if coords != end:
                    neighbour.set_open()

                open_set.add( (coords) )

            draw()

            node.set_closed()

def djikstra(window, draw, grid, start, end):
    open_set = PriorityQueue()
    g_score = { (i, j) : float("inf") for i in range( len(grid) ) for j in range( len(grid[i]) ) }
    g_start = 0
    g_score[start] = g_start
    open_set.put( (g_start, start) )
    parents = { start : (-1, -1) }

    while not open_set.empty():
        current = open_set.get()[1]

        if current == end:
            grid[start[0]][start[1]].set_shortest_path()
            draw_shortest_path(draw, grid, parents, end)
            break

        node = grid[current[0]][current[1]]

        node.set_neighbours(grid)

        neighbours = node.get_neighbours()

        for cost, coords in neighbours:
            temp_g = g_score[current] + cost

            # add to queue if neighbour hasn't previously been encountered
            if g_score[coords] == float("inf"):

                g_score[coords] = temp_g

                open_set.put((temp_g, coords))

                parents[coords] = current

                grid[coords[0]][coords[1]].set_open()

                draw()

            # otherwise update parents table for shortest path
            elif temp_g < g_score[coords]:
                parents[coords] = current

        grid[current[0]][current[1]].set_closed()

        draw()

def a_star(window, draw, grid, start, end):
    open_set = PriorityQueue()  # stores f and coordinates of a node
    g_score = { (i, j) : float("inf") for i in range( len(grid) ) for j in range( len(grid[i]) ) }
    f_score = { (i, j) : float("inf") for i in range( len(grid) ) for j in range( len(grid[i]) ) }
    parents = {start: (-1,-1)}
    f_start = 0 + get_distance(start, end)
    open_set.put( (f_start, start) )
    g_score[start] = 0
    f_score[start] = f_start

    while not open_set.empty():
        current = open_set.get()[1]

        if current == end:
            grid[start[0]][start[1]].set_shortest_path()
            draw_shortest_path(draw, grid, parents, end)
            break

        node = grid[current[0]][current[1]]

        node.set_neighbours(grid)

        neighbours = node.get_neighbours()

        for cost, coords in neighbours:

            temp_g = g_score[current] + cost
            # update f score table for lowest path to neighbour
            if temp_g < g_score[coords]:
                temp_f = temp_g + get_distance(coords, end)

                open_set.put( (temp_f, coords))

                # mark as open if haven't previously encountered
                if g_score[coords] == float("inf"):
                    grid[coords[0]][coords[1]].set_open()

                g_score[coords] = temp_g

                f_score[coords] = temp_f

                parents[coords] = current

                draw()


        grid[current[0]][current[1]].set_closed()
