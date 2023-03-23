# p3p-fusion-path
 A project that finds fusion paths between two Personas in Persona 3 Portable.

 Goal: Make a website where the user can input two Personas and get a fusion path
 between the two.

 Process:
 - Make a version of it in Python that prints out the resulting path in console
 - Translate version to (still deciding) that will be in website form

 I'm doing it in Python first just to make sure that my idea for finding fusion paths
 work. If it does, then translating it into a site would take out the wrestling with
 if the actual process works alongside and I can focus more on the front-end component.

 Once this P3P version works, I would like to try making a version for P5R, and maybe
 adding innate vs passed-down skills as well to the path.

3/22/2023
- Finished creating dictionary with personas where:
  -> key: {(recipe): result}
- Created a test of a bfs search on a smaller dictionary, then tested it on persona_list dictionary

When running the bfs search on persona_list, the path given was long for a fusion path that should be fairly short.
(Orpheus to unicorn should go orpheus + alp -> unicorn or something similar)
I also want to include a type of heuristic that would make paths a bit shorter, and for a while I was stuck on it
until I thought about adding base levels + Arcanas.

Going to redo the dictionary a bit then and add another dictionary with the levels and Arcanas for each Persona first,
then worry about heuristics + how that plays a role in the search.

Also read up more on the fusion chart and learned a bit more about how fusions are calculated.
I think with dictionaries for the base levels + the cheapest fusion recipes, it could make for a better fusion path.
