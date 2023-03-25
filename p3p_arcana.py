"""

    ver2 of fusion path finder, based more on arcanas + base levels.
    dictionaries used:
        all_arcanas -> all arcanas
        persona_arcanas -> all arcanas and available persona, key: arcana, val: {(persona, base lvl)}
        normal_fusions -> normal fusion + results, key: curr arcana, val: {k: additional arcana, v: resulting arcana}
        triple_fusions -> triple fusion results, key: persona, val: (recipe)
        special_fusions -> personas with special fusion recipes, key: persona, val: (recipe)

    fusion things for reference:
    https://gamefaqs.gamespot.com/psp/971508-shin-megami-tensei-persona-3-portable/map/8014-fusion-chart
    https://arantius.github.io/persona-fusion-calculator/3portable.html?ref=dtf.ru#/list/name

    finding fusion paths assume that:
    - social links are maxed
    - all personas are in compendium
    - all social links are maxed for telos
    - all velvet room quests are complete

"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

all_arcanas = {'fool', 'magician', 'priestess', 'empress', 'emperor', 'hierophant', 'lovers', 'chariot', 'justice',
                'justice', 'hermit', 'fortune', 'strength', 'hanged man', 'death', 'temperance', 'devil', 'tower',
                'star', 'moon', 'sun', 'judgment', 'aeon'}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

persona_arcanas = {

    'fool': {('orpheus', 1), ('slime', 12), ('legion', 22), ('black frost', 34), ('ose', 44), ('decarabia', 50), ('loki', 58), ('susano o', 76), ('orpheus telos', 90)},
    'hierophant': {('omoikane', 7), ('berith', 13), ('shiisa', 26), ('flauros', 33), ('thoth', 41), ('hokuto seikun', 47), ('daisoujou', 53), ('kohryu', 66)},
    'fortune': {('fortuna', 17), ('empusa', 23), ('kusi mitama', 29), ('clotho', 38), ('lachesis', 45), ('atropos', 54), ('norn', 62)},
    'devil': {('lilim', 8), ('mokoi', 18), ('vetala', 24), ('incubus', 34), ('succubus', 43), ('pazuzu', 52), ('lilith', 61), ('abaddon', 68), ('beelzebub', 81)},
    'judgment': {('anubis', 59), ('trumpeter', 65), ('michael', 72), ('satan', 79), ('lucifer', 89), ('messiah', 90)},
    'magician': {('nekomata', 5), ('jack frost', 8), ('pyro jack', 14), ('hua po', 20), ('sati', 28), ('orobas', 34), ('rangda', 40), ('surt', 52)},
    'lovers': {('pixie', 2), ('alp', 6), ('tam lin', 13), ('narcissus', 20), ('queen mab', 27), ('saki mitama', 39), ('titania', 48), ('raphael', 61), ('cybele', 68)},
    'strength': {('valkyrie', 11), ('rakshasa', 16), ('titan', 23), ('jikokuten', 29), ('hanuman', 37), ('narasimha', 46), ('kali', 55), ('siegfried', 59)},
    'tower': {('eligor', 31), ('cu chulainn', 40), ('bishamonten', 60), ('seiten taisei', 67), ('masakado', 73), ('mara', 77), ('shiva', 82), ('chi you', 86)},
    'aeon': {('uriel', 63), ('nidhoggr', 69), ('ananta', 75), ('atavaka', 80), ('metatron', 87)},
    'priestess': {('apsaras', 3), ('unicorn', 11), ('high pixie', 21), ('sarasvati', 27), ('ganga', 35), ('parvati', 47), ('kikuri hime', 53), ('scathach', 64)},
    'chariot': {('ara mitama', 6), ('chimera', 9), ('zouchouten', 14), ('ares', 19), ('oumitsunu', 30), ('nata taishi', 37), ('koumokuten', 43), ('thor', 53)},
    'hanged man': {('inugami', 10), ('take minakata', 21), ('orthrus', 28), ('vasuki', 38), ('ubelluris', 48), ('hecatoncheires', 54), ('hell biker', 60), ('attis', 67)},
    'star': {('neko shogun', 19), ('setanta', 28), ('nandi', 39), ('kaiwan', 49), ('ganesha', 58), ('garuda', 65), ('kartikeya', 70), ('saturnus', 78), ('helel', 88)},
    'empress': {('leanan sidhe', 33), ('yaksini', 50), ('laksmi', 57), ('hariti', 62), ('gabriel', 69), ('mother harlot', 74), ('skadi', 80), ('alilat', 84)},
    'justice': {('angel', 4), ('archangel', 10), ('principality', 16), ('power', 25), ('virtue', 32), ('dominion', 42), ('throne', 51), ('melchizedek', 59)},
    'death': {('ghoul', 18), ('pale rider', 24), ('loa', 31), ('samael', 37), ('mot', 45), ('alice', 56), ('thanatos', 64)},
    'moon': {('gurr', 15), ('yamatano orochi', 26), ('girimehkala', 42), ('dionysus', 48), ('chernobog', 58), ('seth', 66), ('baal zebul', 71), ('sandalphon', 74)},
    'emperor': {('forneus', 7), ('oberon', 15), ('take mikazuchi', 24), ('king frost', 30), ('naga raja', 36), ('kingu', 46), ('barong', 52), ('odin', 57)},
    'hermit': {('yomotsu shikome', 9), ('naga', 17), ('lamia', 25), ('mothman', 32), ('taraka', 38), ('kurama tengu', 44), ('nebiros', 50), ('kumbhanda', 56), ('arahabaki', 60)},
    'temperance': {('nigi mitama', 12), ('mithra', 22), ('genbu', 29), ('seiryuu', 36), ('okuninushi', 44), ('suzaku', 51), ('byakko', 57), ('yurlungur', 64)},
    'sun': {('yatagarasu', 30), ('quetzalcoatl', 43), ('jatayu', 55), ('horus', 63), ('suparna', 70), ('vishnu', 78), ('asura', 85)}

}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

normal_fusions = {

    'fool': {'aeon': 'death', 'judgment': 'star', 'sun': 'empress', 'moon': 'fortune', 'star': 'aeon', 'tower': 'moon', 'devil': 'hermit', 'temperance': 'hierophant', 'death': 'strength', 'hanged man': 'magician', 'fortune': 'justice', 'hermit': 'priestess', 'justice': 'lovers', 'chariot': 'emperor', 'lovers': 'priestess', 'hierophant': 'hermit', 'emperor': 'chariot', 'empress': 'fortune', 'priestess': 'justice', 'magician': 'hierophant', 'fool': 'fool'},
    'hierophant': {'judgment': 'lovers', 'sun': 'temperance', 'moon': 'temperance', 'star': 'priestess', 'tower': 'temperance', 'temperance': 'strength', 'death': 'empress', 'hanged man': 'lovers', 'strength': 'priestess', 'fortune': 'emperor', 'hermit': 'chariot', 'justice': 'chariot', 'chariot': 'justice', 'lovers': 'magician', 'hierophant': 'hierophant', 'emperor': 'chariot', 'empress': 'priestess', 'priestess': 'chariot', 'magician': 'hermit', 'fool': 'hermit'},
    'fortune': {'aeon': 'devil', 'sun': 'temperance', 'moon': 'chariot', 'star': 'moon', 'tower': 'moon', 'devil': 'moon', 'temperance': 'lovers', 'hanged man': 'strength', 'fortune': 'fortune'},
    'devil': {'aeon': 'lovers', 'devil': 'devil', 'temperance': 'death', 'hanged man': 'moon', 'strength': 'fortune', 'fortune': 'moon', 'hermit': 'moon', 'hermit': 'death', 'chariot': 'hanged man', 'lovers': 'strength', 'empress': 'lovers', 'magician': 'temperance', 'fool': 'hermit'},
    'judgment': {'aeon': 'star', 'judgment': 'judgment', 'sun': 'star', 'star': 'temperance', 'tower': 'aeon', 'temperance': 'moon', 'strength': 'hanged man', 'justice': 'aeon', 'hierophant': 'lovers', 'emperor': 'hierophant', 'priestess': 'empress', 'fool': 'star'},
    'magician': {'sun': 'lovers', 'moon': 'priestess', 'star': 'empress', 'tower': 'empress', 'devil': 'temperance', 'temperance': 'death', 'hanged man': 'devil', 'fortune': 'emperor', 'hermit': 'chariot', 'justice': 'hierophant', 'chariot': 'devil', 'lovers': 'emperor', 'hierophant': 'hermit', 'emperor': 'temperance', 'empress': 'hanged man', 'priestess': 'lovers', 'magician': 'magician', 'fool': 'heirophant'},
    'lovers': {'hanged man': 'aeon', 'sun': 'hierophant', 'moon': 'empress', 'star': 'hierophant', 'tower': 'star', 'devil': 'strength', 'temperance': 'priestess', 'death': 'devil', 'hanged man': 'hermit', 'strength': 'hierophant', 'fortune': 'magician', 'hermit': 'justice', 'justice': 'chariot', 'chariot': 'emperor', 'lovers': 'lovers', 'hierophant': 'magician', 'emperor': 'chariot', 'empress': 'fortune', 'priestess': 'magician', 'magician': 'emperor', 'fool': 'priestess'},
    'strength': {'judgment': 'hanged man', 'sun': 'priestess', 'moon': 'hanged man', 'star': 'priestess', 'tower': 'devil', 'devil': 'fortune', 'temperance': 'moon', 'death': 'hanged man', 'hanged man': 'hermit', 'strength': 'strength', 'hermit': 'fortune', 'justice': 'temperance', 'chariot': 'justice', 'lovers': 'hierophant', 'hierophant': 'priestess', 'emperor': 'hanged man', 'empress': 'chariot', 'priestess': 'hermit', 'fool': 'hanged man'},
    'tower': {'aeon': 'moon', 'judgment': 'aeon', 'moon': 'fortune', 'tower': 'tower', 'temperance': 'devil', 'hanged man': 'death', 'fortune': 'devil', 'fortune': 'moon', 'justice': 'star', 'chariot': 'moon', 'lovers': 'star', 'hierophant': 'temperance', 'empress': 'chariot', 'magician': 'empress', 'fool': 'moon'},
    'aeon': {'aeon': 'aeon', 'judgment': 'star', 'sun': 'empress', 'star': 'devil', 'tower': 'moon', 'devil': 'lovers', 'temperance': 'star', 'hanged man': 'temperance', 'fortune': 'devil', 'hermit': 'star', 'chariot': 'death', 'lovers': 'hnaged man', 'empress': 'moon', 'priestess': 'empress', 'fool': 'death'},
    'priestess': {'aeon': 'empress', 'judgment': 'empress', 'sun': 'star', 'moon': 'star', 'star': 'justice', 'temperance': 'empress', 'death': 'emperor', 'hanged man': 'strength', 'strength': 'hermit', 'fortune': 'magician', 'hermit': 'strength', 'justice': 'lovers', 'chariot': 'magician', 'lovers': 'magician', 'hierophant': 'chariot', 'emperor': 'justice', 'empress': 'lovers', 'priestess': 'priestess', 'magician': 'lovers', 'fool': 'justice'},
    'chariot': {'aeon': 'death', 'moon': 'fortune', 'tower': 'moon', 'devil': 'hanged man', 'temperance': 'death', 'hanged man': 'fortune', 'strength': 'fortune', 'fortune': 'strength', 'hermit': 'temperance', 'justice': 'magician', 'chariot': 'chariot', 'lovers': 'emperor', 'hierophant': 'justice', 'emperor': 'hermit', 'empress': 'devil', 'priestess': 'magician', 'magician': 'devil', 'fool': 'emperor'},
    'hanged man': {'aeon': 'temperance', 'moon': 'empress', 'star': 'strength', 'tower': 'death', 'devil': 'moon', 'temperance': 'hierophant', 'death': 'devil', 'hanged man': 'hanged man', 'strength': 'hermit', 'fortune': 'strength', 'justice': 'fortune', 'chariot': 'priestess', 'lovers': 'hermit', 'hierophant': 'lovers', 'emperor': 'hermit', 'empress': 'chariot', 'priestess': 'strength', 'magician': 'devil', 'fool': 'magician'},
    'star': {'aeon': 'devil', 'judgment': 'temperance', 'sun': 'justice', 'moon': 'death', 'star': 'star', 'temperance': 'moon', 'hanged man': 'strength', 'strength': 'priestess', 'fortune': 'moon', 'hermit': 'chariot', 'justice': 'emperor', 'lovers': 'hierophant', 'hierophant': 'priestess', 'emperor': 'justice', 'empress': 'temperance', 'priestess': 'jsutice', 'magician': 'empress', 'fool': 'aeon'},
    'empress': {'aeon': 'moon', 'sun': 'lovers', 'moon': 'lovers', 'star': 'temperance', 'tower': 'chariot', 'devil': 'lovers', 'temperance': 'lovers', 'death': 'lovers', 'hanged man': 'chariot', 'strength': 'chariot', 'fortune': 'strength', 'hermit': 'lovers', 'justice': 'emperor', 'chariot': 'devil', 'lovers': 'fortune', 'hierophant': 'priestess', 'emperor': 'lovers', 'empress': 'empress', 'priestess': 'lovers', 'magician': 'hanged man', 'fool': 'fortune'},
    'justice': {'aeon': 'judgment', 'sun': 'emperor', 'star': 'emperor', 'tower': 'star', 'temperance': 'moon', 'death': 'moon', 'hanged man': 'priestess', 'strength': 'temperance', 'fortune': 'chariot', 'hermit': 'priestess', 'justice': 'justice', 'chariot': 'magician', 'lovers': 'chariot', 'hierophant': 'chariot', 'emperor': 'devil', 'empress': 'emperor', 'priestess': 'lovers', 'magician': 'hierophant', 'fool': 'lovers'},
    'death': {'moon': 'star', 'death': 'death', 'hanged man': 'devil', 'strength': 'hanged man', 'justice': 'moon', 'lovers': 'devil', 'hierophant': 'empress', 'emperor': 'moon', 'empress': 'lovers', 'priestess': 'emperor', 'fool': 'strength'},
    'moon': {'sun': 'temperance', 'moon': 'moon', 'star': 'death', 'tower': 'fortune', 'temperance': 'empress', 'death': 'star', 'hanged man': 'empress', 'strength': 'hanged man', 'fortune': 'chariot', 'hermit': 'magician', 'chariot': 'fortune', 'lovers': 'empress', 'hierophant': 'temperance', 'empress': 'lovers', 'priestess': 'star', 'magician': 'priestess', 'fool': 'fortune'},
    'emperor': {'hierophant': 'judgment', 'sun': 'empress', 'star': 'justice', 'temperance': 'hanged man', 'death': 'moon', 'hanged man': 'hermit', 'strength': 'hanged man', 'hermit': 'strength', 'justice': 'devil', 'chariot': 'hermit', 'lovers': 'chariot', 'hierophant': 'chariot', 'emperor': 'emperor', 'empress': 'lovers', 'priestess': 'justice', 'magician': 'temperance', 'fool': 'chariot'},
    'hermit': {'aeon': 'star', 'moon': 'magician', 'star': 'chariot', 'devil': 'death', 'temperance': 'hanged man', 'hanged man': 'fortune', 'strength': 'fortune', 'fortune': 'emperor', 'hermit': 'hermit', 'justice': 'priestess', 'chariot': 'temperance', 'lovers': 'justice', 'hierophant': 'emperor', 'empress': 'strength', 'priestess': 'magician', 'magician': 'emperor', 'fool': 'justice'},
    'temperance': {'aeon': 'star', 'judgment': 'moon', 'sun': 'star', 'moon': 'empress', 'star': 'moon', 'tower': 'devil', 'devil': 'death', 'temperance': 'temperance', 'hanged man': 'hierophant', 'strength': 'moon', 'fortune': 'lovers', 'hermit': 'hierophant', 'justice': 'moon', 'chariot': 'death', 'lovers': 'priestess', 'hierophant': 'strength', 'emperor': 'hanged man', 'empress': 'lovers', 'priestess': 'empress', 'magician': 'death', 'fool': 'hierophant'},
    'sun': {'aeon': 'empress', 'judgment': 'star', 'sun': 'sun', 'moon': 'temperance', 'star': 'justice', 'temperance': 'star', 'temperance': 'star', 'strength': 'priestess', 'fortune': 'temperance', 'justice': 'emperor', 'lovers': 'hierophant', 'hierophant': 'temperance', 'emperor': 'empress', 'empress': 'lovers', 'priestess': 'star', 'magician': 'lovers', 'fool': 'empress'}

}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPORTANT -> (highest lvl arcana, second highest lvl arcana, lowest lvl arcana)

triple_fusions = {

    'anubis': ('moon', 'chariot', 'magician'),
    'atropos': ('fortune', 'fortune', 'fortune'),
    'baal zebul': ('moon', 'moon', 'moon'),
    'barong': ('emperor', 'emperor', 'emperor'),
    'bishamonten': ('hermit', 'temperance', 'devil'),
    'byakko': ('temperance', 'temperance', 'temperance'),
    'chernobog': ('moon', 'moon', 'moon'),
    'chi you': ('priestes', 'aeon', 'fortune'),
    'cu chulainn': ('emperor', 'lovers', 'death'),
    'cybele': ('lovers', 'lovers', 'lovers'),
    'decarabia': ('fool', 'fool', 'fool'),
    'dominion': ('justice', 'justice', 'justice'),
    'eligor': ('devil', 'lovers', 'fool'),
    'ganesha': ('star', 'star', 'star'),
    'ganga': ('priestess', 'priestess', 'priestess'),
    'garuda': ('star', 'star', 'star'),
    'gurr': ('magician', 'justice', 'lovers'),
    'hanuman': ('strength', 'strength', 'strength'),
    'hecatoncheires': ('hanged man', 'hanged man', 'hanged man'),
    'hell biker': ('hanged man', 'hanged man', 'hanged man'),
    'high pixie': ('hanged man', 'hermit', 'lovers'),
    'hokuto seikun': ('hierophant', 'hierophant', 'hierophant'),
    'horus': ('hierophant', 'emperor', 'lovers'),
    'hua po': ('priestess', 'hanged man', 'chariot'),
    'jatayu': ('tower', 'lovers', 'hermit'),
    'kali': ('strength', 'strength', 'strength'),
    'kartikeya': ('star', 'star', 'star'),
    'kikuri hime': ('priestess', 'priestess', 'priestess'),
    'kingu': ('emperor', 'emperor', 'emperor'),
    'koumokuten': ('chariot', 'chariot', 'chariot'),
    'kumbhanda': ('hermit', 'hermit', 'hermit'),
    'kurama tengu': ('hermit', 'hermit', 'hermit'),
    'lachesis': ('fortune', 'fortune', 'fortune'),
    'legion': ('priestess', 'emperor', 'chariot'),
    'loki': ('fool', 'fool', 'fool'),
    'melchizedek': ('justice', 'justice', 'justice'),
    'mithra': ('hanged man', 'magician', 'lovers'),
    'mokoi': ('magician', 'justice', 'priestess'),
    'naga': ('hierophant', 'lovers', 'priestess'),
    'narasimha': ('strength', 'strength', 'strength'),
    'narcissus': ('fool', 'chariot', 'lovers'),
    'nata taishi': ('chariot', 'chariot', 'chariot'),
    'nebiros': ('hermit', 'hermit', 'hermit'),
    'neko shogun': ('devil', 'justice', 'lovers'),
    'oberon': ('chariot', 'lovers', 'fool'),
    'odin': ('emperor', 'emperor', 'emperor'),
    'orobas': ('magician', 'magician', 'magician'),
    'ose': ('chariot', 'devil', 'hermit'),
    'oumitsunu': ('chariot', 'chariot', 'chariot'),
    'parvati': ('priestess', 'priestess', 'priestess'),
    'pazuzu': ('devil', 'devil', 'devil'),
    'power': ('chariot', 'lovers', 'chariot'),
    'principality': ('emperor', 'hierophant', 'justice'),
    'queen mab': ('lovers', 'lovers', 'lovers'),
    'quetzalcoatl': ('star', 'hierophant', 'emperor'),
    'raja naga': ('emperor', 'emperor', 'emperor'),
    'rakshasa': ('hermit', 'hierophant', 'chariot'),
    'rangda': ('magician', 'magician', 'magician'),
    'raphael': ('lovers', 'lovers', 'lovers'),
    'saki mitama': ('lovers', 'lovers', 'lovers'),
    'satan': ('aeon', 'devil', 'hanged man'),
    'sati': ('magician', 'magician', 'magician'),
    'scathach': ('priestess', 'priestess', 'priestess'),
    'seiten taisei': ('moon', 'hermit', 'fortune'),
    'setanta': ('devil', 'emperor', 'fool'),
    'seth': ('moon', 'moon', 'moon'),
    'shiisa': ('priestess', 'chariot', 'hierophant'),
    'siegfried': ('strength', 'strength', 'strength'),
    'slime': ('justice', 'priestess', 'lovers'),
    'succubus': ('devil', 'devil', 'devil'),
    'suparna': ('sun', 'sun', 'sun'),
    'surt': ('magician', 'magician', 'magician'),
    'suzaku': ('temperance', 'temperance', 'temperance'),
    'take mikazuchi': ('hierophant', 'strength', 'hermit'),
    'take minakata': ('hermit', 'lovers', 'priestess'),
    'tam lin': ('lovers', 'justice', 'orpheus'),
    'taraka': ('hermit', 'hermit', 'hermit'),
    'thor': ('chariot', 'chariot', 'chariot'),
    'thoth': ('hierophant', 'hierophant', 'hierophant'),
    'throne': ('justice', 'justice', 'justice'),
    'titan': ('chariot', 'fool', 'justice'),
    'titania': ('lovers', 'lovers', 'lovers'),
    'trumpeter': ('tower', 'chariot', 'magician'),
    'uriel': ('moon', 'devil', 'lovers'),
    'vetala': ('devil', 'magician', 'hanged man'),
    'virtue': ('justice', 'justice', 'justice'),
    'vishnu': ('sun', 'sun', 'sun'),
    'yamatano orochi': ('temperance', 'priestess', 'hanged man'),
    'yatagarasu': ('chariot', 'magician', 'fool'),
    'yurlungur': ('temperance', 'temperance', 'temperance'),
    'zouchouten':('hierophant', 'chariot', 'lovers')

}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

special_fusions = {

    'alice': ('lilim', 'pixie', 'nata taishi', 'narcissus'),
    'arahabaki': ('omoikane', 'take minakata', 'okuninushi', 'kikuri hime'),
    'asura': ('yatagarasu', 'quetzalcoatl', 'jatayu', 'horus', 'suparna', 'vishnu'),
    'attis': ('inugami', 'take minakata', 'orthrus', 'vasuki', 'ubelluris'),
    'beelzebub': ('baal zebul', 'incubus', 'succubus', 'pazuzu', 'lilith', 'abaddon'),
    'black frost': ('king frost', 'jack frost', 'pyro jack', 'queen mab'),
    'daisoujou': ('mithra', 'ara mitama', 'kusi mitama', 'saki mitama', 'nigi mitama'),
    'girimehkala': ('gurr', 'rangda', 'vetala', 'taraka'),
    'kohryu': ('genbu', 'seiryuu', 'suzaku', 'byakko'),
    'lilith': ('lilim', 'vetala', 'incubus', 'succubus'),
    'lucifer': ('helel', 'satan', 'beelzebub', 'abaddon', 'samael'),
    'mara': ('incubus', 'mot', 'pazuzu', 'kumbhanda', 'zouchouten'),
    'masakado': ('bishamonten', 'jikokuten', 'koumokuten', 'zouchouten'),
    'messiah': ('orpheus', 'thanatos'),
    'metatron': ('michael', 'uriel', 'raphael', 'gabriel'),
    'norn': ('clotho', 'lachesis', 'atropos'),
    'orpheus': ('slime', 'legion'),
    'orpheus telos': ('thanatos', 'asura', 'chi you', 'metatron', 'helel', 'messiah'),
    'sandalphon': ('garuda', 'suzaku', 'yatagarasu', 'gurr', 'horus'),
    'shiva': ('barong', 'rangda'),
    'susano o': ('orpheus', 'legion', 'ose', 'black frost', 'decarabia', 'loki'),
    'thanatos': ('ghoul', 'pale rider', 'loa', 'samael', 'mot', 'alice')

}
