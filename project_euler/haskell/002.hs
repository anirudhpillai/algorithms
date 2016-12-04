answer :: Int
answer = sum [ x | x <- takeWhile (<= 4000000) fibs, even x]
  where
    fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

main :: IO ()
main = print answer
