generateDivisors :: Int -> [Int]
generateDivisors x = x:[i | i <- [1.. (x `div` 2)], x `mod` i == 0]

triangularNumbers :: [Int]
triangularNumbers = [sum [1..i] | i <- [1..]]

answer :: Int
answer = head . filter (\x -> (length . generateDivisors $ x) > 500) $
            triangularNumbers
