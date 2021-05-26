colors = ["black", "white", "blue", "yellow", "red"]
combinations = [(x, y) | x <- colors, y <- colors, x < y]