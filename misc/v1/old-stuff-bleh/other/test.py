from queue import PriorityQueue
import random

# test dict
dict = {
    'guff': {('1', '2'): 'fishstick', ('2'): 'jonesy', ('3'): 'meowscles'},
    'fishstick': {('6'): 'felicity fish', ('8'): 'dinosaur', ('2'): 'jonesy'},
    'jonesy': {('3', '4'): 'meowscles', ('5'): 'felicity fish'},
    'meowscles': {('6', '7'): 'felicity fish'},
    'felicity fish': {('8'): 'dinosaur'},
    'dinosaur': {('9'): 'fishstick'}
}

# queue and explored for bfs
frontier = PriorityQueue()
frontier.put((1, 'guff'))
explored = {} # dict for explored nodes -> key: curr, val: path
cost_so_far = {} # cost so far -> key: node, val: cost
path = {} # path of graph -> key: name of node, val: path taken
explored['guff'] = None
cost_so_far['guff'] = 0


while not frontier.empty():

    # take out from explored
    # curr is (priority #, key)
    curr = frontier.get()

    # add to path
    path[(curr[1])] = explored[(curr[1])]

    #print(cost_so_far)

    # at the end
    if(curr[1] == 'dinosaur'):
        for i in path:
            print(i, "from", path[i], "with cost", cost_so_far[i])

    for next in dict[curr[1]]: # looking at neighbors
        new_cost = cost_so_far[curr[1]] + 1 # the cost from where we are now +1 for the neighbor
        if dict[curr[1]][next] not in cost_so_far or new_cost < cost_so_far[dict[curr[1]][next]]: # neighbors not in cost
            cost_so_far[dict[curr[1]][next]] = new_cost
            priority = new_cost # priority = the new cost of getting to where we are vs
            frontier.put((priority, dict[curr[1]][next]))
            explored[str(dict[curr[1]][next])] = next
