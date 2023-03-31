from calc import *
from p3p_arcana import *
from queue import PriorityQueue

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
end_persona_base_level = find_base_lvl(end_persona)

# initializing some stuff
frontier = PriorityQueue()
explored = [] # explored nodes

# push start persona
# inner tuple is -> persona, path so far, cost of path
frontier.put((1, (start_persona, [], 0)))

# while loop for the whole search
while not frontier.empty():

    child = frontier.get() # pop child off queue
    path_so_far = child[1][1] # gets path from child obj
    explored.append(child[1][0]) # this persona has been explored now


    if child[1][0] == end_persona: # we've reached the end
        #s = str(start_persona)

        """
        for p in path_so_far: # iterating through entire path
            for pp in p[0]: # iterating through tuple with recipes
                s += " + " + pp
            s += " = " + p[1]
            print(s)
            s = p[1]
        """

        print(path_so_far)

        break # exit out search -> we found path

    # now we find the recipes using normal_spreads, special_spreads, and triple_spreads that our current persona can have
    # tuples should be (recipe parts, result) where the last persona is always the result of that fusion
    results = normal_spreads(child[1][0]) + special_spreads(child[1][0]) + triple_spreads(child[1][0])

    # filter results list of dupes
    # just take the first result of that persona and put it into list final_recipes
    final_recipes = []
    final_recipe_personas = []
    for rp in results: # for all results
        if (rp[len(rp)-1] not in final_recipe_personas): # if that persona is not in this list keeping track of that, append
            final_recipes.append(rp)
            final_recipe_personas.append(rp[len(rp)-1])

    # for each recipe possible
    for recipe in final_recipes:

        # if the recipe includes the end persona, don't include it in queue
        if end_persona in recipe:
            continue

        # calculate the cost of this recipe:
        # cost of going from curr to this recipe + cost of personas needed for this recipe compared to curr + current cost
        new_cost = abs(find_base_lvl(recipe[len(recipe)-1]) - find_base_lvl(child[1][0])) + child[1][2]

        # add cost of personas needed for this recipe compared to curr by finding out if it's a normal, triple, or special fusion
        lvl_cost = 0
        if (recipe[len(recipe)-1] in special_fusions_list): # if it's a special fusion
            for sr in recipe[0]:
                lvl_cost += find_base_lvl(sr)
            new_cost += abs(find_base_lvl(child[1][0]) - lvl_cost)
        elif ((len(recipe)-1) == 2): # if it's a triple fusion
            lvl_cost = find_base_lvl(recipe[0]) + find_base_lvl(recipe[1])
            new_cost += abs(find_base_lvl(child[1][0]) - lvl_cost)
        else: # normal fusion
            lvl_cost = find_base_lvl(recipe[0])
            new_cost += abs(find_base_lvl(child[1][0]) - lvl_cost)

        # if resulting persona is not in exlored, or this new cost is better than the one before
        if ((recipe[len(recipe)-1] not in explored) or (new_cost < child[1][2])):
            next_actions = path_so_far + [recipe] # next_actions = prev recipes + curr recipe, with resulting personas

            # our priority is going to be based on the new_cost + heuristic
            # where heuristic is how far the resulting persona is away from the end persona based on base lvl
            priority = new_cost + abs((end_persona_base_level - find_base_lvl(recipe[len(recipe)-1]))) # CHECK THIS
            # add it to frontier to be explored
            frontier.put((priority, (recipe[len(recipe)-1], next_actions, new_cost)))
