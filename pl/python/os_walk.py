# Διάσχιση υποκαταλόγων ενός καταλόγου, καταμέτρηση γραμμών αρχείων με επέκταση .cpp
import os

start_directory = "e:/git_repos/oop/"

c = 0
total_lines_c = 0
# διάσχιση υποκαταλόγων
for root, _, files in os.walk(start_directory, topdown=False):
    for file in files:
        if file.endswith(".cpp"):  # μόνο για τα .cpp αρχεία
            fp = os.path.join(root, file)  # πλήρες όνομα αρχείου
            print(fp)
            c += 1
            with open(
                fp, "r", encoding="utf-8"
            ) as f:  # άνοιγμα αρχείου fp με context manager
                lines = f.readlines()
                # lines = [x for x in lines if x != "\n"]  # α) αφαίρεση γραμμών που περιέχουν μόνο το σύμβολο αλλαγής γραμμής \n
                lines = [
                    x for x in lines if x.strip() != ""
                ]  # β) # αφαίρεση κενών γραμμών
                total_lines_c += len(lines)

print(f"Αρχεία C++ = {c}, συνολικός αριθμός γραμμών C++ κώδικα = {total_lines_c}")
