"""
    finding fusion paths here
    https://www.redblobgames.com/pathfinding/a-star/introduction.html
"""

from p3p_dict import persona_list
from queue import PriorityQueue # for bfs

# name = persona_list['ose']
# for i in name:
#    print(i, name[i]) -> (recipe), (result)

# get the start and end personas for fusion path
# throw an exception if either start or end is not in list
"""
start_persona = input("Starting Persona: ").lower()
if(start_persona not in persona_list):
    raise Exception("Persona " + start_persona + " does not exist.")

end_persona = input("Ending Persona: ").lower()
if(end_persona not in persona_list):
    raise Exception("Persona " + end_persona + " does not exist.")
"""

start_persona = "orpheus"
end_persona = "unicorn"


"""
    frontier = Stack()      # stack for dfs
    explored = []       # explored nodes

    # starting state, action, cost
    # action is [] because since we're at the start, we have no moves so far
    frontier.push((problem.startingState(), [], 0))

    while not frontier.isEmpty():

        # get next state
        # path_so_far will become the current list of actions that's popped out of stack
        child = frontier.pop()
        path_so_far = child[1]

        if(child[0] not in explored):       # if we haven't explored position

            explored.append(child[0])       # exploring it, so add it to list

            if(problem.isGoal(child[0])):       # at goal state
                # give final path -> should have all actions due to how we're pushing to frontier
                return path_so_far

            for adj in problem.successorStates(child[0]):       # for each successor of child
                if(adj[0] not in explored):     # we haven't explored the child
                    # next_actions = the path so far (which is a list) +
                    # action (made as a list -> smashing 2 lists together basically)
                    next_actions = path_so_far + [adj[1]]
                    frontier.push((adj[0], next_actions, adj[2]))
"""

# dfs setup

# frontier, explored
frontier = [] # using list as a stack // append, pop
explored = [] # explored nodes

# adding starting persona as a node
# (persona, recipe, cost)
frontier.append((start_persona, None, 0))

# while frontier is not empty
while len(frontier) != 0:

    # get the next state
    child = frontier.pop()
    # path_so_far is going to be the path that we pass along arg
    # (persona, recipes)
    path_so_far = (child[0], child[1])

    # child not in explored list
    if(child[0] not in explored):

        explored.append(child[0]) # add child to explored list

        if(child[0] == end_persona): # we've reached end goal
            print(path_so_far)

        for adj in persona_list[child[0]]: # neighbors -> curr persona + a neighboring one = result
            # since adj is a tuple, for each one of adj that isn't in explored:
            


"""
# bfs setup with some extra steps

# frontier for bfs
frontier = PriorityQueue()
frontier.put((1, start_persona)) # (cost, persona)

# dict setup
explored = {} # dict for explored nodes -> key: curr, val: path ; nodes we've explored using bfs
cost_so_far = {} # cost so far for nodes and their paths -> key: node, val: cost ; costs of all paths

# starting point setup
explored[start_persona] = None
cost_so_far[start_persona] = 0

while not frontier.empty():

    # take out from explored - > curr is (priority #, key)
    curr = frontier.get()

    # adding this curr to the path with its recipe
    path_so_far =

    for next in persona_list[curr[1]]: # looking at neighbors
        new_cost = cost_so_far[curr[1]] + 1 # the cost from where we are now +1 for the neighbor
        if persona_list[curr[1]][next] not in cost_so_far or new_cost < cost_so_far[persona_list[curr[1]][next]]: # neighbors not in cost
            cost_so_far[persona_list[curr[1]][next]] = new_cost
            priority = new_cost # priority = the new cost of getting to where we are vs
            frontier.put((priority, persona_list[curr[1]][next]))
            explored[persona_list[curr[1]][next]] = next
"""
