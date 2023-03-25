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

3/23/2023
After thinking about this a bit more, the final search looks like this:
1) Using a priority queue to search through recipes
2) For each recipe that that persona has:
- Find the "cost", which is the recipe's resulting persona's base level + how many personas are in recipe + current cost of path
- If that persona is not explored or the cost is better,
 - next_actions gets path with new recipe attached
 - Priority is determined by the cost + [(end persona base level) - (result persona base level)],
and the thought there is if the result persona's base level > end persona base level, that result persona
might be too far off for now and it might be better to look at resulting persona base levels that are closer
to the end persona's base level given where we are now
3) Push that into the queue

The result gives us something like this, if we're looking at a path from Orpheus to Ose:
orpheus + pixie + ara mitama = oberon
oberon + berith = ares
ares + mokoi + naga = ose

What I want to do next is test it with various different paths, and to make sure both dictionaries in p3p_dict.py are correct.

At the moment, the recipes used are the cheapest ones given by the fusion calculators linked in the comments, or the special
fusion recipes that are available. I did that because as you go up in levels, the possible fusion recipes tend to go up,
and I feel like calculating that and processing the results in this search could make it messy and maybe even slow it down with all
the possible branches. I'm a bit worried, though, that if because I'm limiting myself to the cheapest recipes, some paths might take longer
than what's actually needed. Maybe I'll go back and add a few more recipes? Not sure yet, and I think testing will help me decide.
