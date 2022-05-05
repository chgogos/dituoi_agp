monsterRevWords :: String -> String
monsterRevWords input = rejoinUnreversed (divideReversed input)
  where
    divideReversed s = go1 [] s
      where
        go1 divided [] = divided
        go1 [] (c : cs)
          | testSpace c = go1 [] cs
          | otherwise = go1 [[]] (c : cs)
        go1 (w : ws) [c]
          | testSpace c = (w : ws)
          | otherwise = ((c : w) : ws)
        go1 (w : ws) (c : c' : cs)
          | testSpace c =
            if testSpace c'
              then go1 (w : ws) (c' : cs)
              else go1 ([c'] : w : ws) cs
          | otherwise = go1 ((c : w) : ws) (c' : cs)
    testSpace c = c == ' '
    rejoinUnreversed [] = []
    rejoinUnreversed [w] = reverseList w
    rejoinUnreversed strings = go2 (' ' : reverseList newFirstWord) (otherWords)
      where
        (newFirstWord : otherWords) = reverseList strings
        go2 rejoined ([] : []) = rejoined
        go2 rejoined ([] : (w' : ws')) = go2 (rejoined) ((' ' : w') : ws')
        go2 rejoined ((c : cs) : ws) = go2 (c : rejoined) (cs : ws)
    reverseList [] = []
    reverseList w = go3 [] w
      where
        go3 rev [] = rev
        go3 rev (c : cs) = go3 (c : rev) cs