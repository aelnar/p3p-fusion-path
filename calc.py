"""
    all functions used to calculate fusions and other stuff
    to make search cleaner/easier

        fusion things for reference:
        https://gamefaqs.gamespot.com/psp/971508-shin-megami-tensei-persona-3-portable/map/8014-fusion-chart
        https://arantius.github.io/persona-fusion-calculator/3portable.html?ref=dtf.ru#/list/name

"""
from p3p_arcana import * # from p3p_arcana import all dictionaries

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# utility fcns
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# finds the base lvl of a given persona from persona_stats
def find_base_lvl(curr):
    return persona_stats[curr][0]

# finds the arcana of a given persona from persona_stats
def find_persona_arcana(curr):
    return persona_stats[curr][1]

# find persona that's after one passed in
def find_next_persona(curr):
    arcana = persona_stats[curr][1] # get arcana of curr persona
    cl = find_base_lvl(curr) # get curr persona's base lvl
    for p in persona_arcanas[arcana]: # for every persona in that arcana
        if(p[1] >= cl): # if the base lvl of the persona > curr persona's lvl
            return p # return that persona -> we found next persona

# find out if triple fusion is all the same arcana
def check_triple_arcana(spread):
    if(spread[0] == spread[1] == spread[2]):
        return True
    return False

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# fusion fcns
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# finds normal fusions based on current persona passed in
# normal fusions -> two personas
# returns a list of (other persona that's part of recipe, result)
def normal_spreads(curr):

    results = [] # return list with all possible fusions with curr persona

    cl = find_base_lvl(curr) # base level of current persona
    ca = find_persona_arcana(curr) # arcana of current persona

    for arcana in persona_arcanas: # for each arcana in persona_arcanas
        # find the fusion result of curr persona + this arcana
        fusion_result = normal_fusions[ca][arcana] # normal_fusions[curr persona][ps persona] -> resulting from fusion

        for ps in persona_arcanas[arcana]: # for each persona in each arcana; ps[0] -> name, ps[1] -> lvl
            # first, if ps is the curr persona, skip it
            if(ps[0] == curr):
                break

            lvl_result = ((cl + ps[1]) / 2) + 1 # get the lvl average of curr persona + ps[0]
            # for the fusion result, find the resulting persona around this base level
            for p in persona_arcanas[fusion_result]:
                # first highest level persona in arcana, and persona is not a special fusion
                if(p[1] >= lvl_result and p[0] not in special_fusions_list):
                    results.append((ps[0], p[0]))
                    break

    return results # return list

# special fusions
# if the curr persona is in a special fusion recipe, put that in a list of
# [(curr persona, result)]
def special_spreads(curr):

    results = [] # list of personas to be returned

    for sf in special_fusions: # for every special fusion persona
        if(curr in special_fusions[sf]):
            results.append((curr, sf))

    return results # return list

# used to find triple fusions for passed in persona
# a bit of work here i think i might go bald tbh !
def triple_spreads(curr):

    results = [] # will be returned at the end

    cl = find_base_lvl(curr) # base level of current persona
    ca = find_persona_arcana(curr) # arcana of current persona

    # if curr in triple fusion arcanas
    # see if it's a triple arcana fusion or not
    #       see where curr stands in lvls (ordered in triple fusions val)
    #       either go <- c -> or <- <- c or c -> ->
    for tf in triple_fusions: # for each triple fusion
        triple_arcana = check_triple_arcana(triple_fusions[tf]) # see if it's triple arcana spread

        if(triple_arcana == True): # we have a triple spread; we'll only look at curr arcana then
            # we love a nested loop /j
            for p1 in persona_arcanas[ca]:
                if(p1[0] == curr or p1[0] in special_fusions_list): # curr persona or it's a special fusion
                    continue
                for p2 in persona_arcanas[ca]:
                    if(p2[0] == curr or p2[0] in special_fusions_list): # curr persona or it's a special fusion
                        continue

        else:
            print("peepeepoopoo")

    return results # return list
