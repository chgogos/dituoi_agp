pts :: Int -> Int
pts x =
  if x == 1
    then 10
    else
      if x == 2
        then 6
        else
          if x == 3
            then 4
            else
              if x == 4
                then 3
                else
                  if x == 5
                    then 2
                    else
                      if x == 6
                        then 1
                        else 0