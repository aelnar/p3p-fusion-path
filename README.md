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

 --- 4/18/2023 ---

 -> Note: Some combinations results in path.py stalling, and it might just be
 that the path isn't possible or it's taking super long.
 It's only 9/100 of them, so it works a 91% of the time.
 I might just have it time out if it's like this and prompt to try shorter paths.

 Final stats with 100 tests:

 Arcana Count:
 {'devil': 9, 'lovers': 7, 'aeon': 5, 'fool': 6, 'justice': 6, 'priestess': 8, 'chariot': 8, 'sun': 8, 'moon': 7, 'emperor': 6, 'hierophant': 6, 'tower': 7, 'temperance': 8, 'fortune': 4, 'empress': 6, 'star': 9, 'death': 5, 'strength': 6, 'hanged man': 7, 'magician': 8, 'hermit': 8, 'judgment': 5}

 The most used persona is apsaras with 57 uses.
 The most used arcana is devil with 9 uses.
 list of personas used zero times:  ['alice', 'alilat', 'arahabaki', 'atropos', 'attis', 'beelzebub', 'black frost', 'daisoujou', 'decarabia', 'girimehkala', 'hell biker', 'kali', 'kartikeya', 'kingu', 'kohryu', 'kusi mitama', 'lachesis', 'lamia', 'loa', 'mother harlot', 'nidhoggr', 'norn', 'orobas', 'orpheus telos', 'ose', 'pale rider', 'principality', 'raja naga', 'raphael', 'sandalphon', 'scathach', 'seiten taisei', 'shiisaa', 'shiva', 'siegfried', 'skadi', 'susano o', 'take mikazuchi', 'tam lin', 'thor', 'throne', 'titan', 'titania', 'trumpeter', 'virtue', 'yurlungur']

 --- 4/18/2023 (v1) ---

 Current results with more 88 tests:
 The most used persona is apsaras with 51 uses.
 The most used arcana is devil with 9 uses. (+ star, it's tied)
 list of personas used zero times:  ['alice', 'alilat', 'arahabaki', 'atropos', 'attis', 'beelzebub', 'black frost', 'daisoujou', 'decarabia', 'girimehkala', 'hell biker', 'kali', 'kartikeya', 'kingu', 'kohryu', 'kusi mitama', 'lachesis', 'lamia', 'loa', 'mother harlot', 'narasimha', 'nidhoggr', 'norn', 'orobas', 'orpheus telos', 'ose', 'pale rider', 'principality', 'raja naga', 'raphael', 'sandalphon', 'satan', 'scathach', 'seiten taisei', 'shiisaa', 'shiva', 'siegfried', 'skadi', 'susano o', 'take mikazuchi', 'tam lin', 'thor', 'throne', 'titan', 'titania', 'trumpeter', 'virtue', 'yurlungur']

 Arcana count:
 {'devil': 9, 'lovers': 7, 'aeon': 5, 'fool': 6, 'justice': 6, 'priestess': 8, 'chariot': 8, 'sun': 8, 'moon': 7, 'emperor': 6, 'hierophant': 6, 'tower': 7, 'temperance': 8, 'fortune': 4, 'empress': 6, 'star': 9, 'death': 5, 'strength': 5, 'hanged man': 7, 'magician': 8, 'hermit': 8, 'judgment': 4}

 A lot of the higher level + special fusion Personas aren't being used, and the least used Arcanas are Fortune and Judgment.
 Looking at the roster for the Judgment arcana, it's mostly high level, so it makes sense based on the results above.
 Not sure why Fortune is also lacking, but it is what is is sometimes.

 Going to just round out the tests to 100 and see the results from there.

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
