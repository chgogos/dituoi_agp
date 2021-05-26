myReverse :: [Integer] -> [Integer]
reverselist [] = []
reverselist (h:t) = reverselist t ++ [h]