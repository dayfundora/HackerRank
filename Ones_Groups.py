def check(i,j,l):
    n=len(matriz)
    m=len(matriz[0])
    if i<0 or j<0 or i>=n or j>=m or l[i][j]==-1 or l[i][j]==0:
        return 0
    else:
        l[i][j]=-1
        return 1+check(i,j+1,l)+check(i+1,j,l)+check(i-1,j,l)+check(i,j-1,l)

def ones_groups(matriz,arr):
    n=len(matriz)
    m=len(matriz[0])
    dic={}
    for i in range(n):
        for j in range(m):
            if matriz[i][j]==1:
                temp=check(i,j,matriz)
                if temp in dic:
                    dic[temp]+=1
                else:
                    dic[temp]=1
    result=[dic[elem] if elem in dic else 0 for elem in arr]    
        
matriz=[[1,1,1,1,1,1],
        [1,1,0,0,0,0],
        [0,0,0,1,1,1],
        [0,0,0,1,1,1],
        [0,0,1,0,0,0],
        [1,0,0,0,0,0]]
arr=[8,7,6,1]
ones_groups(matriz,arr)