// CALC FUNCTIONS

/*
--- UTILITY FUNCTIONS ---
*/

// finds the base lvl of a given persona from persona_stats
function find_base_lvl(curr){
    return persona_stats[curr][0];
}

// finds the arcana of a given persona from persona_stats
function find_persona_arcana(curr){
    return persona_stats[curr][1];
}


// find persona that's after one passed in
function find_next_persona(curr){
    arcana = persona_stats[curr][1]; // get arcana of curr persona
    cl = find_base_lvl(curr); // get curr persona's base lvl
    for (const p of persona_arcanas[arcana].entries()){ // for every persona in that arcana
        if(p[1][1] >= cl){ // if the base lvl of the persona > curr persona's lvl
            return p; // return that persona -> we found next persona
        }
    }
}


// find out if triple fusion is all the same arcana
function check_triple_arcana(spread){
    if(spread[0] == spread[1] == spread[2]){
        return true;
    }
    return false;
}

/*
--- FUSION CALC FCNS ---
*/

// normal spreads calculation fcn
function normal_spreads(curr){

    var results = []; // return list with all possible fusions with curr persona

    var cl = find_base_lvl(curr); // base level of current persona
    var ca = find_persona_arcana(curr); // arcana of current persona

    for (let arcana in persona_arcanas){ // for each arcana in persona_arcanas

        if (!(arcana in normal_fusions[ca])){ // this fusion result is not possible
            continue;
        }

        // find the fusion result of curr persona + this arcana
        fusion_result = normal_fusions[ca][arcana] // normal_fusions[curr persona][ps persona] -> resulting from fusion

        for (let ps in persona_arcanas[arcana]){ // for each persona in each arcana; persona_arcanas[arcana][ps][0] -> name, persona_arcanas[arcana][ps][1] -> lvl
            // first, if ps is the curr persona, skip it
            if(persona_arcanas[arcana][ps][0] == curr){
                continue;
            }

            var lvl_result = ((cl + persona_arcanas[arcana][ps][1] ) / 2) + 1; // get the lvl average of curr persona + ps[1]
            // for the fusion result, find the resulting persona around this base level
            for (let p in persona_arcanas[fusion_result]){ // persona_arcanas[fusion_result][p][0] -> name, persona_arcanas[fusion_result][p][1] -> lvl
                // first highest level persona in arcana, persona is not a special fusion, and not the same persona we're on, and it's not a persona in triple_fusions
                // WE'RE HERE
                if(persona_arcanas[fusion_result][p][1] > lvl_result && !(persona_arcanas[fusion_result][p][0] in special_fusions_list) &&
                persona_arcanas[fusion_result][p][0] != persona_arcanas[arcana][ps][0] && !(persona_arcanas[fusion_result][p][0] in triple_fusions)){
                    results.push([persona_arcanas[arcana][ps][0], persona_arcanas[fusion_result][p][0]]); // (second part of recipe, resulting persona)
                    break;
                }
            }
        }

    }

    return results; // return list
}

// special fusions fcn
// if the curr persona is in a special fusion recipe, put that in a list of [(recipe, result)]
function special_spreads(curr){

    var results = []; // list of personas to be returned
    var sf_list = [];

    for (let sf in special_fusions){ // for every special fusion persona
        // turn tuple into list, append resulting persona at end, then append it as a tuple again
        // makes it consistent with other fcns in this file
        if(special_fusions[sf].includes(curr)){
            sf_list = special_fusions[sf];
            sf_list.push(sf);
            results.push(sf_list);
        }
    }

    return results; //# return list
}

// triple fusions fcn - > used to find triple fusions for passed in persona
// a bit of work here i think i might go bald tbh !
// tuple is (p2, p3, result)
function triple_spreads(curr){

    var results = []; // will be returned at the end

    var cl = find_base_lvl(curr); // base level of current persona
    var ca = find_persona_arcana(curr); // arcana of current persona

    /*
    # if curr in triple fusion arcanas
    # see if it's a triple arcana fusion or not
    for tf in triple_fusions: # for each triple fusion

        triple_arcana = check_triple_arcana(triple_fusions[tf]) # see if it's triple arcana spread
        if(triple_arcana == True and ca in triple_fusions[tf]): # we have a triple spread; we'll only look if curr arcana is in that spread
            # we love a nested loop /j
            for p1 in persona_arcanas[ca]: # in each persona in curr persona arcana
                if(p1[0] == curr or p1[0] in special_fusions_list): # curr persona or it's a special fusion
                    continue
                for p2 in persona_arcanas[ca]:
                    if(p2[0] == curr or p2[0] in special_fusions_list or p1[0] == p2[0]): # curr persona or it's a special fusion or it's the same persona as p1
                        continue

                    # calculate the base lvl of these personas
                    lvl_avg = ((cl + p1[1] + p2[1]) / 3 ) + 5
                    # if calculated lvl average > tf base lvl and the (resulting base lvl - 10) <= max lvl of the lvls <= resulting base lvl and tf not in recipe
                    if(lvl_avg < find_base_lvl(tf) and (find_base_lvl(tf) - 10) <= max([cl, p1[1], p2[1]]) <= find_base_lvl(tf) and tf != p1[0] and tf != p2[0]):
                        results.append((p1[0], p2[0], tf))
        else: # not a triple spread; a mix of arcanas

            if(ca in triple_fusions[tf]): # if curr persona arcana is in these triple fusions

                # take out first instance of curr arcana -> sometimes recipe is something like chariot, chariot, lovers
                tf_list = list(triple_fusions[tf])
                tf_list.remove(ca)
                tf_final = tuple(tf_list)
                max_arcana = find_max_arcana(tf_final, ca) # need this for looping purposes /smile
                for p1 in persona_arcanas[max_arcana[0]]:
                        if (p1[0] in special_fusions_list): # dont use this if special fusion
                            continue
                        for p2 in persona_arcanas[max_arcana[1]]:
                            if (p2[0] in special_fusions_list): # dont use if special fusion
                                continue

                            # calculate the base lvl of these personas
                            lvl_avg = ((cl + p1[1] + p2[1]) / 3 ) + 5
                            # if calculated lvl average > tf base lvl and the (resulting base lvl - 10) <= max lvl of the lvls <= resulting base lvl and tf not in recipe
                            if(lvl_avg < find_base_lvl(tf) and (find_base_lvl(tf) - 10) <= max([cl, p1[1], p2[1]]) <= find_base_lvl(tf) and tf != p1[0] and tf != p2[0]):
                                results.append((p1[0], p2[0], tf))

    */
    return results; // return list
}

console.log(triple_spreads('orpheus'));
