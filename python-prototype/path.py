from calc import *
from p3p_arcana import *
from queue import PriorityQueue


start_persona = input("Starting Persona: ").lower()
if(start_persona not in persona_stats):
    raise Exception("Persona " + start_persona + " does not exist.")

end_persona = input("Ending Persona: ").lower()
if(end_persona not in persona_stats):
    raise Exception("Persona " + end_persona + " does not exist.")

#start_persona = "orpheus"
#end_persona = "ose"

# used for search
end_persona_base_level = find_base_lvl(end_persona)

# initializing some stuff
frontier = PriorityQueue()
explored = [] # explored nodes

# push start persona
# inner tuple is -> persona, path so far, cost of path
frontier.put((1, (start_persona, [], 0)))

# START OF WHILE LOOP
while not frontier.empty():

    # taking off front of queue and putting it into explored
    child = frontier.get()
    path_so_far = child[1][1]
    explored.append(child[1][0])

    curr_persona_lvl = find_base_lvl(child[1][0]) # curr persona base level

    # we've reached the goal persona
    if child[1][0] == end_persona:
        # printing recipes but nice
        s = str(start_persona)
        for p in path_so_far: # iterating through entire path
            for p1 in p: # for each part of the recipe
                if p1 not in s: # if it's not in the stringfor this iterration
                    if p1 is not p[len(p)-1]: # if the persona is not the resulting one or not the one that was already put in
                        s += " + " + p1
                    else: # resulting persona
                        s += " = " + p1
            print(s)
            s = p[len(p)-1]
        break

    # find all recipes available for current persona using fcns from calc.py
    results = normal_spreads(child[1][0]) + special_spreads(child[1][0]) + triple_spreads(child[1][0])

    # there might be some dupes in this list
    # take first instance of persona and put that into list results_v1
    results_v1 = []
    results_v1_personas = []
    for rp in results:
        if(rp[len(rp)-1] not in results_v1_personas): # if persona not in list tracking personas, append
            results_v1.append(rp)
            results_v1_personas.append(rp[len(rp)-1])

    # for all recipes in results_v1
    for recipe in results_v1:

        # if end_persona is in the recipe and it's not the result but part of the recipe
        # don't bother with this recipe
        if end_persona in recipe and end_persona != recipe[len(recipe)-1]:
            continue

        # calculate the cost of this recipe:
        # cost of going from curr to this recipe + current cost
        new_cost = abs(find_base_lvl(recipe[len(recipe)-1]) - curr_persona_lvl) + child[1][2]

        # if we havent explored node or we have a better cost
        if ((recipe[len(recipe)-1] not in explored) or (new_cost < child[1][2])):
            next_actions = path_so_far + [recipe] # next_actions = prev recipes + curr recipe, with resulting personas

            # our priority is going to be based on the new_cost + heuristic
            # where heuristic is how far the resulting persona is away from the end persona based on base lvl
            priority = new_cost + abs((end_persona_base_level - find_base_lvl(recipe[len(recipe)-1])))
            frontier.put((priority, (recipe[len(recipe)-1], next_actions, new_cost))) # add it to frontier to be explored
