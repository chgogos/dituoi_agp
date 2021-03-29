import os

start_directory = "e:/git_repos/oop/"

c = 0
for root, _, files in os.walk(start_directory, topdown=False):
    for file in files:
        if file.endswith(".cpp"):
            print(os.path.join(root, file))
            c += 1

print(f"{c} .cpp files")
