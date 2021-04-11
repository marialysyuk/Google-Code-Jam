There are two helpful observations:

1) "IMPOSSIBLE" case can be retrieved from the minimum and maximum amount of possible shifts. Because of the algorithm's structure the minimum amount of shifts is N-1
(this is the case when numbers are already sorted) and the maximum amount is N(N+1)/2-1 (this is the case when at each iteration the corresponding number is 
situated at the end of the sequence).

2) If it's possible to reversort at the target cost, then the procedure suggested is as follows. At each step the minimum cost is 1, then the part of the costs is
distributed equally by 1 among N-1 steps (if total costs is smaller than N-1, them among fist steps). If there is something left (total costs are larger than N-1),
then at each step I add costs till the maximum possible at this particular step. The remaining costs are corresponded to another steps similarly until costs are > 0.
