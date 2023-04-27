"""
    finding fusion paths here
    https://www.redblobgames.com/pathfinding/a-star/introduction.html?
"""

from p3p_dict import persona_list, persona_stats
from queue import PriorityQueue

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
end_persona = "ose"

# used for search
end_persona_base_level = persona_stats[end_persona][0]

# initializing some stuff
frontier = PriorityQueue()
explored = [] # explored nodes

# push start persona
# inner tuple is -> persona, path so far, cost of path
frontier.put((1, (start_persona, [], 0)))

# while loop
while not frontier.empty():

    child = frontier.get() # pop child off queue
    path_so_far = child[1][1] # gets path from child obj
    explored.append(child[1][0]) # this persona has been explored now


    if child[1][0] == end_persona: # we've reached the end
        s = str(start_persona)

        for p in path_so_far: # iterating through entire path
            for pp in p[0]: # iterating through tuple with recipes
                s += " + " + pp
            s += " = " + p[1]
            print(s)
            s = p[1]

        break # exit out search -> we found path

    # for each recipe in that persona's list
    for adj in persona_list[child[1][0]]:

        if end_persona in adj: # if end persona is in this recipe, skip it -> don't want it in our queue
            continue

        # since we have base levels in persona_stats, we're going
        # to get the resulting persona's base level, which will be
        # included in the cost
        resulting_persona = persona_stats[persona_list[child[1][0]][adj]][0]

        # three things in cost:
        # resulting persona's level + how many are in recipe INCLUDING one we're on + current cost
        new_cost = resulting_persona + (len(adj) + 1) + child[1][2]

        # if the result of the recipe is not in explored, or the cost is better here
        if((persona_list[child[1][0]][adj] not in explored) or (new_cost < child[1][2])):

            # tuple -> (recipe, result)
            next_actions = path_so_far + [(adj, persona_list[child[1][0]][adj])] # next_actions = prev recipes + curr recipe, with resulting personas

            # our priority is going to be based on the new_cost + heuristic
            # where the heuristic is how far the result base level is from the level of the end result persona
            # ^ the thought is that if the (end result persona lvl - result base level) is big, then we're still
            # a bit away from the end result persona so this recipe might not be as good; if it's small, then
            # it might be good to look at the recipes that are closer to the end result persona
            priority = new_cost + (end_persona_base_level - resulting_persona)

            # push new cost + recipe, resulting persona into priority queue
            # the priority = cost, because we don't have heuristics
            # tuple being pushed is -> (resulting persona of adj recipe, path so far as next_actions, cost)
            frontier.put((new_cost, (persona_list[child[1][0]][adj], next_actions, new_cost)))
