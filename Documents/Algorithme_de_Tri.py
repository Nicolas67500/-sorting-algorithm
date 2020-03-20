from random import randint

# 1

def Listealea(n,m):
    liste = []
    for k in range(n):
        r = randint(0,m)
        liste.append(r)
    return liste
# 2
def minimunl(L):
    m=0
    for k in range(len(L)):
        if L[m]>=L[k]:
            m=k
    return m


# Etape 1

def tri_selection(L):
    for k in range(len(L)-1):
        m=k
        for i in range(k+1,len(L)):
            if L[i]<L[m]:
                m=i
        L[k],L[m] = L[m], L[k]

    return L

print(tri_selection([0,6,4,3,8,3]))


def tri_selection_bis(L):
    for k in range(len(L)-1):
        m = k
        for i in range(k+1, len(L)):
            if L[i] >L[m]:
                m = i
        L[k], L[m] = L[m], L[k]
    return L

def tri_fusion(L1,L2):
    t=[]
    for k in range(len(L1+L2)):
        if (L1!=[] and L2!=[] and L1[0]<=L2[0]):
            t.append(L1.pop(0))
        else:
            t.append(L2.pop(0))
    return t

def tri_fusion_complete(L):
    milieu=len(L)//2
    L1=L[0:milieu]
    L2=L[milieu:len(L)]
    if max(len(L1),len(L2))<=1:
        return tri_fusion(L1,L2)
    return tri_fusion(tri_fusion_complete(L1),tri_fusion_complete(L2))
