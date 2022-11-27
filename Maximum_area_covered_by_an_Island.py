def maxAreaOfIsland(grid):
        row,col=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if(r<0 or r==row or c<0 or c==col or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        area=0
        for r in range(row):
            for c in range(col):
                area=max(area,dfs(r,c))
        return area
a,b=map(int,input().split())
arr=[]
for i in range(a):
    r=list(map(int,input().split()))
    arr.append(r)
print(maxAreaOfIsland(arr))