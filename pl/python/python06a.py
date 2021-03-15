"""
Εύρεση της λέξης από το λεκτικό της εισόδου με το μεγαλύτερο μήκος
"""

txt = input()
words = txt.split(" ")
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)
