(||) :: Bool -> Bool -> Bool
True || _ = True
False || y = y