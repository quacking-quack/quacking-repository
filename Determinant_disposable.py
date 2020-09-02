def func(mat,cof,dets):
#this function splitting n-size matrix to n pair of coefficients and matrix of size n-1, until size==2,then finds determinants
    if len(mat)>2:
        cofactors=[]#list of pairs
        for i in range(len(mat)):
            if mat[0][i]==0:
                continue
            else:
                t = []#n-1 size matrix
                pair = []#pair of n-1 size matrix and coef 
                for j in range(1,len(mat)):
                    t.append([])
                    for k in range(len(mat)):
                        if k==i:
                            continue
                        else:
                            t[j-1].append(mat[j][k])
                pair.append(t)
                if i%2==0:
                    pair.append(cof*mat[0][i])
                else:
                    pair.append(cof*mat[0][i]*(-1))
                cofactors.append(pair)
        for i in range(len(cofactors)):
            func(cofactors[i][0],cofactors[i][1],dets)
    else:
        dets.append(cof*(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]))

n = int(input("Enter size of matrix: "))
if n<2:
    print("Matrix's size should be atleast 2")
else:
    mat = []#the original matrix
    dets = []#list for determinants of cofactors of size 2
    Sum = 0
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(int(input(f"{i}.{j}: ")))
    func(mat,1,dets)
    for i in range(len(dets)):
        Sum+=dets[i]
    print("Determinant =",Sum)
