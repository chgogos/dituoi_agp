from WAEParser import parser


def read_input():
    result = ""
    while True:
        data = input("WAE: ").strip()
        if ";" in data:
            i = data.index(";")
            result += data[0 : i + 1]
            break
        else:
            result += data + " "
    return result


def main():
    while True:
        data = read_input()
        if data == "exit;":
            break
        try:
            tree = parser.parse(data)
            print(tree)
        except Exception as inst:
            print(inst.args[0])
            continue

main()

# WAE: {+ 1 2};
# ['+', ['num', 1.0], ['num', 2.0]]
# WAE: {+ 1 x};
# ['+', ['num', 1.0], ['id', 'x']]
# WAE: {with {{x 5}{y 3}} {+ x y}};
# ['with', [['x', ['num', 5.0]], ['y', ['num', 3.0]]], ['+', ['id', 'x'], ['id', 'y']]]
# WAE: {with {{x 5}{y 3}} {+ x }};  
# Syntax error in input!
# None
# WAE: exit;