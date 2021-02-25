"""
Εύρεση της λέξης από το λεκτικό της εισόδου με το μεγαλύτερο μήκος
"""

txt = input()
words = txt.split(" ")
longest = max(words, key=len)  # pythonic
print(longest)
