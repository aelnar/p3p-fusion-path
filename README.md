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

  --- 4/13/2023 ---

  While testing combos, I kind of went on a detour and wanted to compile some data
  on what is being used for the recipes.

  So far with the tests I have, the Persona used most often is Pixie at 28, and the most
  used Arcana is the Fool at 10 uses. I want to run more tests but it's interesting to see
  these so far and to see if it'll change.

 --- 4/11/2023 ---

 A version where it's both calculating recipes based on the current Persona in the loop
 and finding a path exists now.

 The Orpheus -> Ose test path has gotten longer:
 orpheus + angel = alp
 alp + angel = chimera
 chimera + apsaras + inugami = hua po
 hua po + ara mitama = incubus
 incubus + yomotsu shikome + ara mitama = ose

 However, the progress on it should make sense. Time to test a bunch of other paths and see
 if there's anything that needs to be fixed.
