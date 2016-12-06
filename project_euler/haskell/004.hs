answer :: Int
answer = maximum [x | i <- [100..999], j <- [i..999], let x = i*j,
                    show x == (reverse $ show x)]
