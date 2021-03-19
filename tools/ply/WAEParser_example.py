from WAEParser import parser


# data = '{+ 1 2};'
# data = '{+ x y};'
data = "{with {{x 5}{y 3}} {+ x y}};"
try:
    tree = parser.parse(data)
except Exception as inst:
    print(inst.args[0])
print(tree)


# ['with', [['x', ['num', 5.0]], ['y', ['num', 3.0]]], ['+', ['id', 'x'], ['id', 'y']]]