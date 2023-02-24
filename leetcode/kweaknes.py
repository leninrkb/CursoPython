class Solution:
    def kWeakestRows(self, mat, k):
        i={}
        j={}
        ln = len(mat)
        for r in range(ln):
            cn=0
            cm=0
            for c in range(ln):
                if mat[r][c]==1: cn+=1
                if mat[c][r]==1: cm+=1
            i[r]=cn
            j[r]=cm
        sm = mat[:]
        sortedi = sorted(i.items() ,key=lambda x: x[1])
        res = [sortedi[i][0] for i in range(len(sortedi))]
        print(res[:k])
        print(sm)




mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
#mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
k = 3
s = Solution()
s.kWeakestRows(mat,k)
