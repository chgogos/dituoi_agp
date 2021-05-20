from ortools.sat.python import cp_model

"""
    SEND
+   MORE
--------
=  MONEY
"""

model = cp_model.CpModel()

s = model.NewIntVar(1, 9, "S")
e = model.NewIntVar(0, 9, "E")
n = model.NewIntVar(0, 9, "N")
d = model.NewIntVar(0, 9, "D")
m = model.NewIntVar(1, 9, "M")
o = model.NewIntVar(0, 9, "O")
r = model.NewIntVar(0, 9, "R")
y = model.NewIntVar(0, 9, "Y")

letters = [s, e, n, d, m, o, r, y]

model.AddAllDifferent(letters)

# SEND + MORE = MONEY
model.Add(
    s * 1000 + e * 100 + n * 10 + d + m * 1000 + o * 100 + r * 10 + e
    == m * 10000 + o * 1000 + n * 100 + e * 10 + y
)

solver = cp_model.CpSolver()
status = solver.Solve(model)

for letter in letters:
    print(f'{letter} -> {solver.Value(letter)}')


# S -> 9
# E -> 5
# N -> 6
# D -> 7
# M -> 1
# O -> 0
# R -> 8
# Y -> 2

#    9567
# +  1085
# -------
#   10652