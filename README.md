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

 -- 3/30/2023 --

 A new ver of path.py was made based on fusion results, but it takes forever.

 I want to think of a way to trim the amount of fusions being looked into, because
 it's definitely taking a toll on the runtime. I think trimming any Persona <= end_goal Persona
 from the frontier might make it run a little smoother.

 There's also definitely some spelling mistakes/range stuff that's being pointed out in this,
 so there's also that.

 So for the most part, now it's time to iron out any problems in path.py

 --- 3/25/2023 ---

 Going to try calculating paths using base levels + Arcana fusions rather than set recipes,
 just to really open up what recipes + paths it could take.

 There's two layers to it:

 Normal fusions between two Personas happen normally, and the Arcana combos are in one dictionary.
 This should be easy to implement, and a recipe will be added based on the current Persona's base level +
 any Persona >10 levels or so around it = a new Persona to reach. It'll be easy to limit which Personas
 we add and which ones we don't have to.

 Triple fusions are a different story. I didn't want it taking up time trying to find triple fusions that either
 didn't exist, or trying to find fusions that are levels above where we were that weren't necessary. There's also
 just so many combos for triple fusions.

 What I'm doing for triple fusions, then, is a mix of how I'm doing normal fusions and what I did beforehand.
 I'm going to find Personas that rely on triple fusions and put them in a dictionary, as well as the Arcana
 combos that make them up. If the current Persona is in the triple fusion recipe, is it worth it to try it?
 For all the possible Personas the current Persona can fit into, I'm going to see which one would best
 get us to our end goal Persona the quickest with end goal lvl - base lvl. After finding that, then I'm going to find the Personas that fit
 the Arcana combos + the resulting persona's base level range and go from there. I think doing it like this
 would help if the fusion path is going backwards, and covers if going up and down base levels. This will
 definitely be the most difficult thing to execute, but I'd rather try than not get it at all, ya know?

 So that's what's being worked on at the moment. If I can figure out normal + triple fusions and their
 relation to finding fusion paths, I can easily fit them into the search I have going on now, and it should
 result in better paths. :)

 --- 3/23/2023 ---

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
orpheus + pixie + ara mitama = oberon -> oberon + berith = ares -> ares + mokoi + naga = ose

What I want to do next is test it with various different paths, and to make sure both dictionaries in p3p_dict.py are correct.

At the moment, the recipes used are the cheapest ones given by the fusion calculators linked in the comments, or the special
fusion recipes that are available. I did that because as you go up in levels, the possible fusion recipes tend to go up,
and I feel like calculating that and processing the results in this search could make it messy and maybe even slow it down with all
the possible branches. I'm a bit worried, though, that if because I'm limiting myself to the cheapest recipes, some paths might take longer
than what's actually needed. Maybe I'll go back and add a few more recipes? Not sure yet, and I think testing will help me decide.
