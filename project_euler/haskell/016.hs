import Data.Char

answer :: Int
answer = sum . map digitToInt . show $ 2^1000
