def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

val = [40000, 35000, 38000, 15000, 12000, 20000, 10000] 
wt = [80, 70, 30, 10, 10, 12, 10] 
W = 100
n = len(val) 
print(knapSack(W, wt, val, n)) 
