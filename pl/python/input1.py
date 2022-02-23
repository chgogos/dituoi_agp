name = input("Εισάγετε όνομα: ")
age = int(input("Εισάγετε ηλικία: "))

print("Όνομα: " + name + ", ηλικία: " + str(age))  # 1ος τρόπος
print("Όνομα: %s, ηλικία: %d" % (name, age))  # 2ος τρόπος
print("Όνομα: {0}, ηλικία: {1}".format(name, age))  # 3ος τρόπος
print(f"Όνομα: {name}, ηλικία: {age}".format(name, age))  # 4ος τρόπος
