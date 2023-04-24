from p3p_arcana import *

p_stats = {
    'abaddon': 4,
    'alice': 0,
    'alilat': 0,
    'alp': 3,
    'ananta': 6,
    'angel': 42,
    'anubis': 6,
    'apsaras': 57,
    'ara mitama': 33,
    'arahabaki': 0,
    'archangel': 8,
    'ares': 34,
    'asura': 1,
    'atavaka': 4,
    'atropos': 0,
    'attis': 0,
    'baal zebul': 1,
    'barong': 1,
    'beelzebub': 0,
    'berith': 4,
    'bishamonten': 3,
    'black frost': 0,
    'byakko': 2,
    'chernobog': 2,
    'chi you': 3,
    'chimera': 8,
    'clotho': 3,
    'cu chulainn': 1,
    'cybele': 4,
    'daisoujou': 0,
    'decarabia': 0,
    'dionysus': 15,
    'dominion': 2,
    'eligor': 10,
    'empusa': 1,
    'flauros': 6,
    'forneus': 26,
    'fortuna': 16,
    'gabriel': 2,
    'ganesha': 1,
    'ganga': 5,
    'garuda': 1,
    'genbu': 11,
    'ghoul': 3,
    'girimehkala': 0,
    'gurr': 16,
    'hanuman': 2,
    'hariti': 1,
    'hecatoncheires': 1,
    'helel': 1,
    'hell biker': 0,
    'high pixie': 1,
    'hokuto seikun': 3,
    'horus': 3,
    'hua po': 7,
    'incubus': 11,
    'inugami': 17,
    'jack frost': 5,
    'jatayu': 2,
    'jikokuten': 9,
    'kaiwan': 12,
    'kali': 0,
    'kartikeya': 0,
    'kikuri hime': 1,
    'king frost': 22,
    'kingu': 0,
    'kohryu': 0,
    'koumokuten': 3,
    'kumbhanda': 1,
    'kurama tengu': 1,
    'kusi mitama': 0,
    'lachesis': 0,
    'laksmi': 3,
    'lamia': 0,
    'leanan sidhe': 8,
    'legion': 13,
    'lilim': 11,
    'lilith': 1,
    'loa': 0,
    'loki': 1,
    'lucifer': 1,
    'mara': 1,
    'masakado': 1,
    'melchizedek': 3,
    'messiah': 1,
    'metatron': 1,
    'michael': 1,
    'mithra': 2,
    'mokoi': 2,
    'mot': 1,
    'mother harlot': 0,
    'mothman': 6,
    'naga': 4,
    'nandi': 9,
    'narasimha': 1,
    'narcissus': 3,
    'nata taishi': 1,
    'nebiros': 2,
    'neko shogun': 3,
    'nekomata': 7,
    'nidhoggr': 0,
    'nigi mitama': 12,
    'norn': 0,
    'oberon': 1,
    'odin': 3,
    'okuninushi': 5,
    'omoikane': 29,
    'orobas': 0,
    'orpheus': 27,
    'orpheus telos': 0,
    'orthrus': 8,
    'ose': 0,
    'oumitsunu': 1,
    'pale rider': 0,
    'parvati': 3,
    'pazuzu': 2,
    'pixie': 51,
    'power': 2,
    'principality': 0,
    'pyro jack': 14,
    'queen mab': 2,
    'quetzalcoatl': 2,
    'raja naga': 0,
    'rakshasa': 2,
    'rangda': 1,
    'raphael': 0,
    'saki mitama': 1,
    'samael': 2,
    'sandalphon': 0,
    'sarasvati': 19,
    'satan': 1,
    'sati': 2,
    'saturnus': 1,
    'scathach': 0,
    'seiryuu': 3,
    'seiten taisei': 0,
    'setanta': 1,
    'seth': 1,
    'shiisaa': 0,
    'shiva': 0,
    'siegfried': 0,
    'skadi': 0,
    'slime': 10,
    'succubus': 1,
    'suparna': 2,
    'surt': 1,
    'susano o': 0,
    'suzaku': 4,
    'take mikazuchi': 0,
    'take minakata': 5,
    'tam lin': 0,
    'taraka': 2,
    'thanatos': 2,
    'thor': 0,
    'thoth': 4,
    'throne': 0,
    'titan': 0,
    'titania': 0,
    'trumpeter': 0,
    'ubelluris': 4,
    'unicorn': 9,
    'uriel': 4,
    'valkyrie': 10,
    'vasuki': 3,
    'vetala': 1,
    'virtue': 0,
    'vishnu': 2,
    'yaksini': 3,
    'yamatano orochi': 2,
    'yatagarasu': 7,
    'yomotsu shikome': 17,
    'yurlungur': 0,
    'zouchouten': 2
}
# top 5/bottom 5 personas used
# top 5

top5 = []
p_list1 = list(p_stats)
for i in range(0, 5):
    max_num = 0
    max_persona = ''
    for j in range(len(p_list1)):
        if p_stats[p_list1[j]] > max_num:
            max_num = p_stats[p_list1[j]]
            max_persona = p_list1[j]

    p_list1.remove(max_persona)
    top5.append((max_persona, max_num))

# bottom 5
bottom5 = []
p_list2 = list(p_stats)
for i in range(0, 5):
    min_num = 100
    min_persona = ''
    for j in range(len(p_list2)):
        if p_stats[p_list2[j]] < min_num:
            min_num = p_stats[p_list2[j]]
            min_persona = p_list2[j]
    p_list2.remove(min_persona)
    bottom5.append((min_persona, min_num))

print(bottom5)

# most used persona
max_persona = max(p_stats, key=p_stats.get)
print("The most used persona is", max_persona, "with", p_stats[max_persona], "uses.")

# most used arcana
arcana_count = {}
for p in p_stats:
    if persona_stats[p][1] not in arcana_count.keys() and p_stats[p] != 0:
        arcana_count[persona_stats[p][1]] = 1
    elif p_stats[p] != 0:
        arcana_count[persona_stats[p][1]] += 1
    else:
        continue
max_arcana = max(arcana_count, key=arcana_count.get)
print("The most used arcana is", max_arcana, "with", arcana_count[max_arcana], "uses.")

# personas with 0 uses
zero_nj = []
for p in p_stats:
    if p_stats[p] == 0:
        zero_nj.append(p)
print("list of personas used zero times: ", zero_nj)"""
