colors :: [[Char]]
colors = ["black", "white", "blue", "yellow", "red"]

combinations :: [([Char], [Char])]
combinations = [(x, y) | x <- colors, y <- colors, x < y]