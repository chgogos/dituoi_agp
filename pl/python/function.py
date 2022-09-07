def repeat(text, times):
    repeated_text = ""
    for i in range(times):
        repeated_text += text + " "
    return repeated_text
    # return " ".join(text for _ in range(times)) # more pythonic way!

if __name__ == "__main__":
    name = input("Enter a name: ")
    if name == 'Guido':
        print(repeeeet(name) + '!!!') # no problem as long as name is not Guido
    else:
        print(repeat(name, 3))