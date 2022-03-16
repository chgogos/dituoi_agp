# What is the output?

s = "Python"
d = {}
for i, d[i] in enumerate(s):
    pass
print(d)

# το ίδιο αποτέλεσμα και με το
d = dict(enumerate(s))
print(d)
