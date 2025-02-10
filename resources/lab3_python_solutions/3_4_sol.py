import xml.etree.ElementTree as ET

fn = "ITC2021_Test8_SolGenMethodA.xml"
xml_f = open(fn, "r", encoding="utf-8")
tree = ET.ElementTree(file=xml_f)
elem = tree.getroot()
teams = set()
matches = {}
if elem.tag == "Solution":
    for elem2 in elem:
        if elem2.tag == "Games":
            for elem3 in elem2:
                if elem3.tag == "ScheduledMatch":
                    home = int(elem3.attrib["home"])
                    away = int(elem3.attrib["away"])
                    slot = int(elem3.attrib["slot"])
                    matches[(home, away)] = slot  # matches[(0,1)] -> 33
                    teams.add(home)
xml_f.close()

# Υπολογισμός διαφοράς αγωνιστικών ανάμεσα σε κάθε αγώνα και στον επαναληπτικό του
nr_of_teams = len(teams)

for team1 in range(nr_of_teams):
    for team2 in range(team1 + 1, nr_of_teams):
        slot1 = matches[(team1, team2)]
        slot2 = matches[(team2, team1)]
        print(
            f"Ομάδα {team1} εναντίον {team2} αγωνιστικές {slot1} & {slot2} διαφορά {abs(slot1-slot2)} "
        )
