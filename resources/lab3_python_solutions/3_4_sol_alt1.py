# Εναλλακτική, συντομότερη λύση για την άσκηση Ε3Α4

import xml.etree.ElementTree as ET

with open("ITC2021_Test8_SolGenMethodA.xml") as xml_f:
    tree = ET.ElementTree(file=xml_f)

matches = {}
for elem in tree.getroot()[1]:
    matches[(int(elem.attrib["home"]), int(elem.attrib["away"]))] = int(
        elem.attrib["slot"]
    )

nr_of_teams = max([t[0] for t in matches.keys()]) + 1
for team1 in range(nr_of_teams):
    for team2 in range(team1 + 1, nr_of_teams):
        slot1 = matches[(team1, team2)]
        slot2 = matches[(team2, team1)]
        print(
            f"Ομάδα {team1} εναντίον {team2} αγωνιστικές {slot1} & {slot2} διαφορά {abs(slot1-slot2)} "
        )
