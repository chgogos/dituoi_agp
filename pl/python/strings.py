# keep 2 first letters of each word, print all at the same line

zen_text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""

for line in zen_text.split("\n"):
    for w in line.split():
        wl = w.lower()
        print(f"{wl[:2]} ", end="")
             