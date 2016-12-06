primes = sieve [2..]
  where sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]

answer :: Int
answer = primes !! 10001
