# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from matrices import Matrix,FMatrix,CMatrix,Identity

# =============================================================================
"""Example Inputs"""      
# =============================================================================
projectGrid="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# =============================================================================
# Valid Matrices
# =============================================================================
proj=Matrix(listed=projectGrid)
o=Matrix(dim=8,randomFill=0)
b=Matrix(1)
c=Matrix(dim=[2,4])
d=FMatrix([4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,ranged=[-1250,1250])
g=Matrix(dim=[3,6])
p=Matrix(5,ranged=[0,100])
q=FMatrix(4)

# =============================================================================
# String inputs Matrices
# =============================================================================
validStr1=Matrix(dim=[2,3],listed=" 34-52\n33a c9d88 hello\n--3-")
validStr2=Matrix(listed="312as45\ndid12,,,44\ncc352as45\ndid12,,,44\ncc3-5")
validStr3=Matrix(listed="\n\n\ndd34 5\n\n44\nn659")
validStr4=Matrix(dim=[22,3],listed="""ulke,boy,kilo,yas,cinsiyet
tr,130,30,10,e
tr,125,36,11,e
tr,135,34,10,k
tr,133,30,9,k
tr,129,38,12,e
tr,180,90,30,e
tr,190,80,25,e
tr,175,90,35,e
tr,177,60,22,k
us,185,105,33,e
us,165,55,27,k
us,155,50,44,k
us,160,58,39,k
us,162,59,41,k
us,167,62,55,k
fr,174,70,47,e
fr,193,90,23,e
fr,187,80,27,e
fr,183,88,28,e
fr,159,40,29,k
fr,164,66,32,k
fr,166,56,42,k
""")

# =============================================================================
# InvalidMatrices
# =============================================================================
#You have to give the matrix a valid dimension, or a list to get a dimension, or it won't be a valid matrix

#a=Matrix(0)
#v=Matrix()
#k=Matrix(dim=-1)
#l=Matrix(ranged=[0])
#m=Matrix(randomFill=1)

# =============================================================================
# Identity Matrices
# =============================================================================
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
for matrix in [proj,o,b,c,d,e,f,g,p,q]:
    print(matrix)
print('################################')     
# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving strings or a directory")
for matrix in [validStr1,validStr2,validStr3,validStr4]:
    print(matrix)
print('################################') 
# =============================================================================
"""PRINT THE IDENTITY MATRICES """
# =============================================================================
print('################################') 
print("Identity matrices")
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')     
# =============================================================================
"""PROPERTIES, METHODS CALLS"""   
# =============================================================================
print('################################')  
print("Attribute call outputs\n")
print('################\n')
      
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)

print('\n################\n')
      
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print(f)
print("f.delDim(4)")
print(f)
print("f.uptri.p")
f.uptri.p
print("f.lowtri.p")
f.lowtri.p
print("f-(f.lowtri@f.uptri)")#There is a %0.001 error due to rounding
print(f-(f.lowtri@f.uptri))
print('################')
      
print("g.dim:\n",g.dim)
print("g.inRange():\n",g.inRange())
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
      
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):\n",h)
print("h.avg():",h.avg())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary:\n",j.summary)

print('\n################')
      
print("proj=proj.subM(5,15).copy:\n")
proj=proj.subM(5,15).copy
print(proj)

print('################')
      
print("p:",p)
print("p.det:\n",p.det)
print("\np.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)

print('################')
      
print("p:")
print(p)
print("p.remove(c=1) and p.remove(r=2)")
p.remove(c=1)
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print('################\n')
      
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)

print("################")
      
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)

print('\n################')
      
print("id3:\n")
print(id3)

print('################')
      
print("id4:\n")
print(id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))

print('################')
      
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10))

# =============================================================================
"""OPERATIONS ON ELEMENTS"""    
# =============================================================================

print("################################")   
print("Operator examples")
print("################")
      
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))

print("################\n")
      
print(f)
print("f=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("r.remove(r=2):")
r.remove(r=2)
print(r)
print("r.rank:",r.rank)
print("\nr[0]=r[1][:]")
r[0]=r[1][:]
print(r)
print("r.rank:",r.rank)    

print("################")
      
print("for i in range(len(e.matrix)): e[i][-i-1]=99")
for i in range(len(e.matrix)):e[i][i]=99
print(e)
print("\ne+=50:")
e+=50
print(e)
print("for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:\n")
for i in range(len(e.matrix)):e[i]=[b%2 for b in e[i]]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("################")
      
print("\nf.roundForm(3)>f.roundForm(1)")
print(f.roundForm(3)>f.roundForm(1))

# =============================================================================
""" STRING MATRICES' OUTPUTS"""
# =============================================================================
print("\n################################")
print("Strings' matrices:")
print("################\n")
      
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print("validStr"+str(numb+1)+":")
    print(strings)         
    print('################')
print("")

# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Numbers' range: {'Col 1': [1, 88], 'Col 2': [2, 98], 'Col 3': [0, 99], 'Col 4': [5, 97], 'Col 5': [2, 99], 'Col 6': [0, 94], 'Col 7': [0, 99], 'Col 8': [1, 89], 'Col 9': [0, 97], 'Col 10': [17, 97], 'Col 11': [3, 99], 'Col 12': [5, 80], 'Col 13': [0, 98], 'Col 14': [8, 88], 'Col 15': [12, 84], 'Col 16': [1, 97], 'Col 17': [4, 89], 'Col 18': [2, 93], 'Col 19': [5, 98], 'Col 20': [0, 95]}
Averages: {'Col 1': 35.8, 'Col 2': 49.85, 'Col 3': 41.65, 'Col 4': 52.2, 'Col 5': 52.7, 'Col 6': 48.6, 'Col 7': 46.4, 'Col 8': 40.3, 'Col 9': 40.3, 'Col 10': 63.9, 'Col 11': 50.75, 'Col 12': 46.6, 'Col 13': 43.6, 'Col 14': 51.85, 'Col 15': 42.75, 'Col 16': 47.1, 'Col 17': 40.75, 'Col 18': 44.6, 'Col 19': 52.6, 'Col 20': 54.4}

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 


Square matrix
Dimension: 8x8
Numbers' range: {'Col 1': [0, 0], 'Col 2': [0, 0], 'Col 3': [0, 0], 'Col 4': [0, 0], 'Col 5': [0, 0], 'Col 6': [0, 0], 'Col 7': [0, 0], 'Col 8': [0, 0]}
Averages: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0, 'Col 7': 0.0, 'Col 8': 0.0}

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 1x1
Numbers' range: {'Col 1': [0, 0]}
Averages: {'Col 1': 0.0}

0 


Dimension: 2x4
Numbers' range: {'Col 1': [2, 4], 'Col 2': [-4, 4], 'Col 3': [-3, -1], 'Col 4': [-1, 0]}
Averages: {'Col 1': 3.0, 'Col 2': 0.0, 'Col 3': -2.0, 'Col 4': -0.5}

 2  4 -3 -1 
 4 -4 -1  0 


Float Matrix
Dimension: 4x3
Numbers' range: {'Col 1': [-2.3975, 3.7187], 'Col 2': [-4.1139, 4.0331], 'Col 3': [-3.8114, 2.407]}
Averages: {'Col 1': -0.12, 'Col 2': -1.463, 'Col 3': -0.8688}

 0.4756 -4.0490 -3.8114 
-2.3975 -1.7220  2.4070 
-2.2770  4.0331 -1.3341 
 3.7187 -4.1139 -0.7368 


Square matrix
Dimension: 8x8
Numbers' range: {'Col 1': [0, 0], 'Col 2': [0, 0], 'Col 3': [0, 0], 'Col 4': [0, 0], 'Col 5': [0, 0], 'Col 6': [0, 0], 'Col 7': [0, 0], 'Col 8': [0, 0]}
Averages: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0, 'Col 7': 0.0, 'Col 8': 0.0}

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.5911, 786.4397], 'Col 2': [-1172.5631, 996.8718], 'Col 3': [-991.3664, 1215.7104], 'Col 4': [-71.5157, 569.8819], 'Col 5': [-35.376, 1143.2358], 'Col 6': [-1160.7398, 1059.6315]}
Averages: {'Col 1': -232.1963, 'Col 2': 473.0998, 'Col 3': 25.4454, 'Col 4': 314.401, 'Col 5': 572.4454, 'Col 6': 109.0211}

-1235.5911 -1172.5631  -454.8103   231.6343   -35.3760 -1160.7398 
  549.0669   711.6521  -633.2611   569.8819  1143.2358   352.7149 
 -797.0603   850.9062   417.9075   496.5723   405.5497  1059.6315 
   43.3267   869.5177  -991.3664   325.3115   374.2132  -599.9575 
  786.4397   582.2139   598.4924   334.5216   513.4495   562.6057 
 -739.3595   996.8718  1215.7104   -71.5157  1033.6000   439.8721 


Dimension: 3x6
Numbers' range: {'Col 1': [-3, 4], 'Col 2': [-2, 4], 'Col 3': [0, 3], 'Col 4': [1, 4], 'Col 5': [-3, 0], 'Col 6': [-5, 3]}
Averages: {'Col 1': 1.6667, 'Col 2': 1.0, 'Col 3': 2.0, 'Col 4': 2.6667, 'Col 5': -1.6667, 'Col 6': -0.3333}

 4  4  3  4 -3  1 
-3  1  3  3 -2  3 
 4 -2  0  1  0 -5 


Square matrix
Dimension: 5x5
Numbers' range: {'Col 1': [44, 91], 'Col 2': [39, 100], 'Col 3': [25, 77], 'Col 4': [4, 97], 'Col 5': [0, 96]}
Averages: {'Col 1': 74.2, 'Col 2': 77.0, 'Col 3': 57.6, 'Col 4': 46.4, 'Col 5': 30.8}

 44 100  53  58   0 
 89  96  25   6  33 
 61  39  77  97   7 
 86  86  62  67  18 
 91  64  71   4  96 


Float Matrix
Square matrix
Dimension: 4x4
Numbers' range: {'Col 1': [-4.1854, 3.8744], 'Col 2': [-4.5352, 4.9944], 'Col 3': [-1.7099, 4.2012], 'Col 4': [-0.0555, 3.318]}
Averages: {'Col 1': -0.126, 'Col 2': -0.0746, 'Col 3': 0.772, 'Col 4': 1.7801}

-0.1787 -4.2036  2.1367  1.6936 
-0.0145  3.4461  4.2012  2.1643 
 3.8744 -4.5352 -1.5400 -0.0555 
-4.1854  4.9944 -1.7099  3.3180 

################################
################################
Matrices created by giving strings or a directory

Dimension: 2x3
Numbers' range: {'Col 1': [9, 34], 'Col 2': [-52, 88], 'Col 3': [3, 33]}
Averages: {'Col 1': 21.5, 'Col 2': 18.0, 'Col 3': 18.0}

 34 -52  33 
  9  88   3 


Dimension: 5x2
Numbers' range: {'Col 1': [3, 352], 'Col 2': [-5, 45]}
Averages: {'Col 1': 138.2, 'Col 2': 34.6}

312  45 
 12  44 
352  45 
 12  44 
  3  -5 


Dimension: 1x4
Numbers' range: {'Col 1': [34, 34], 'Col 2': [5, 5], 'Col 3': [44, 44], 'Col 4': [659, 659]}
Averages: {'Col 1': 34.0, 'Col 2': 5.0, 'Col 3': 44.0, 'Col 4': 659.0}

 34   5  44 659 


Dimension: 22x3
Numbers' range: {'Col 1': [125, 193], 'Col 2': [30, 105], 'Col 3': [9, 55]}
Averages: {'Col 1': 163.3636, 'Col 2': 62.1364, 'Col 3': 28.6818}

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################################
################################
Identity matrices

Identity Matrix
Dimension: 1x1

 1 


Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
################################
Attribute call outputs

################

d:

Float Matrix
Dimension: 4x3
Numbers' range: {'Col 1': [-2.3975, 3.7187], 'Col 2': [-4.1139, 4.0331], 'Col 3': [-3.8114, 2.407]}
Averages: {'Col 1': -0.12, 'Col 2': -1.463, 'Col 3': -0.8688}

 0.4756 -4.0490 -3.8114 
-2.3975 -1.7220  2.4070 
-2.2770  4.0331 -1.3341 
 3.7187 -4.1139 -0.7368 

d.matrix:

[[0.4756, -4.049, -3.8114], [-2.3975, -1.722, 2.407], [-2.277, 4.0331, -1.3341], [3.7187, -4.1139, -0.7368]]

################

f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Numbers' range: {'Col 1': [-1172.5631, 869.5177], 'Col 2': [-991.3664, 417.9075]}
Averages: {'Col 1': 314.8782, 'Col 2': -415.3826}

-1172.5631  -454.8103 
  711.6521  -633.2611 
  850.9062   417.9075 
  869.5177  -991.3664 
 


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.5911, 786.4397], 'Col 2': [-1172.5631, 996.8718], 'Col 3': [-991.3664, 1215.7104], 'Col 4': [-71.5157, 569.8819], 'Col 5': [-35.376, 1143.2358], 'Col 6': [-1160.7398, 1059.6315]}
Averages: {'Col 1': -232.1963, 'Col 2': 473.0998, 'Col 3': 25.4454, 'Col 4': 314.401, 'Col 5': 572.4454, 'Col 6': 109.0211}

-1235.5911 -1172.5631  -454.8103   231.6343   -35.3760 -1160.7398 
  549.0669   711.6521  -633.2611   569.8819  1143.2358   352.7149 
 -797.0603   850.9062   417.9075   496.5723   405.5497  1059.6315 
   43.3267   869.5177  -991.3664   325.3115   374.2132  -599.9575 
  786.4397   582.2139   598.4924   334.5216   513.4495   562.6057 
 -739.3595   996.8718  1215.7104   -71.5157  1033.6000   439.8721 

f.delDim(4)

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.5911, 786.4397], 'Col 2': [-1172.5631, 996.8718], 'Col 3': [-991.3664, 1215.7104], 'Col 4': [-71.5157, 569.8819], 'Col 5': [-35.376, 1143.2358], 'Col 6': [-1160.7398, 1059.6315]}
Averages: {'Col 1': -232.1963, 'Col 2': 473.0998, 'Col 3': 25.4454, 'Col 4': 314.401, 'Col 5': 572.4454, 'Col 6': 109.0211}

-1235.5911 -1172.5631  -454.8103   231.6343   -35.3760 -1160.7398 
  549.0669   711.6521  -633.2611   569.8819  1143.2358   352.7149 
 -797.0603   850.9062   417.9075   496.5723   405.5497  1059.6315 
   43.3267   869.5177  -991.3664   325.3115   374.2132  -599.9575 
  786.4397   582.2139   598.4924   334.5216   513.4495   562.6057 
 -739.3595   996.8718  1215.7104   -71.5157  1033.6000   439.8721 

f.uptri.p

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.5911, 0], 'Col 2': [-1172.5631, 190.5933], 'Col 3': [-835.3678, 7756.1072], 'Col 4': [-5326.8191, 672.8146], 'Col 5': [-9080.1734, 1127.5156], 'Col 6': [-4983.1522, 3183.7731]}
Averages: {'Col 1': -205.9319, 'Col 2': -163.6616, 'Col 3': 1077.6548, 'Col 4': -868.5745, 'Col 5': -1650.2405, 'Col 6': -879.4402}

-1235.5911 -1172.5631  -454.8103   231.6343   -35.3760 -1160.7398 
    0.0000   190.5933  -835.3678   672.8146  1127.5156  -163.0899 
    0.0000     0.0000  7756.1072 -5326.8191 -9080.1734  3183.7731 
    0.0000     0.0000     0.0000  -789.0771 -1456.2680 -1008.7330 
    0.0000     0.0000     0.0000     0.0000  -457.1414 -1144.6995 
    0.0000     0.0000     0.0000     0.0000     0.0000 -4983.1522 

f.lowtri.p

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-0.6365, 1], 'Col 2': [-0.861, 8.9117], 'Col 3': [-0.0529, 1.1517], 'Col 4': [-0.9879, 1], 'Col 5': [-3.4905, 1], 'Col 6': [0, 1]}
Averages: {'Col 1': 0.1879, 'Col 2': 3.6384, 'Col 3': 0.4062, 'Col 4': 0.0171, 'Col 5': -0.4151, 'Col 6': 0.1667}

 1.0000  0.0000  0.0000  0.0000  0.0000  0.0000 
-0.4444  1.0000  0.0000  0.0000  0.0000  0.0000 
 0.6451  8.4332  1.0000  0.0000  0.0000  0.0000 
-0.0351  4.3464  0.3383  1.0000  0.0000  0.0000 
-0.6365 -0.8610 -0.0529 -0.9879  1.0000  0.0000 
 0.5984  8.9117  1.1517  0.0904 -3.4905  1.0000 

f-(f.lowtri@f.uptri)

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [0.0, 0.0], 'Col 2': [0.0, 0.0], 'Col 3': [0.0, 0.0], 'Col 4': [0.0, 0.0], 'Col 5': [0.0, 0.0], 'Col 6': [0.0, 0.0]}
Averages: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0}

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 

################
g.dim:
 [3, 6]
g.inRange():
 {'Col 1': [-3, 4], 'Col 2': [-2, 4], 'Col 3': [0, 3], 'Col 4': [1, 4], 'Col 5': [-3, 0], 'Col 6': [-5, 3]}
g: 
Dimension: 3x6
Numbers' range: {'Col 1': [-3, 4], 'Col 2': [-2, 4], 'Col 3': [0, 3], 'Col 4': [1, 4], 'Col 5': [-3, 0], 'Col 6': [-5, 3]}
Averages: {'Col 1': 1.6667, 'Col 2': 1.0, 'Col 3': 2.0, 'Col 4': 2.6667, 'Col 5': -1.6667, 'Col 6': -0.3333}

 4  4  3  4 -3  1 
-3  1  3  3 -2  3 
 4 -2  0  1  0 -5 

g.remove(3):

Dimension: 2x6
Numbers' range: {'Col 1': [-3, 4], 'Col 2': [1, 4], 'Col 3': [3, 3], 'Col 4': [3, 4], 'Col 5': [-3, -2], 'Col 6': [1, 3]}
Averages: {'Col 1': 0.5, 'Col 2': 2.5, 'Col 3': 3.0, 'Col 4': 3.5, 'Col 5': -2.5, 'Col 6': 2.0}

 4  4  3  4 -3  1 
-3  1  3  3 -2  3 

################
h=proj.subM(12,18,5,11):
 
Square matrix
Dimension: 7x7
Numbers' range: {'Col 1': [5, 97], 'Col 2': [25, 94], 'Col 3': [20, 99], 'Col 4': [7, 88], 'Col 5': [3, 55], 'Col 6': [44, 97], 'Col 7': [33, 99]}
Averages: {'Col 1': 57.1429, 'Col 2': 50.2857, 'Col 3': 49.7143, 'Col 4': 44.2857, 'Col 5': 22.2857, 'Col 6': 67.7143, 'Col 7': 69.2857}

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.avg(): {'Col 1': 57.1429, 'Col 2': 50.2857, 'Col 3': 49.7143, 'Col 4': 44.2857, 'Col 5': 22.2857, 'Col 6': 67.7143, 'Col 7': 69.2857}

h.det: 1287494735579.9985

h.rank: 7

h.rrechelon: 
Float Matrix
Square matrix
Dimension: 7x7
Numbers' range: {'Col 1': [0, 1.0], 'Col 2': [0, 1.0], 'Col 3': [0, 1.0], 'Col 4': [0, 1.0], 'Col 5': [0, 1.0], 'Col 6': [0, 1.0], 'Col 7': [0, 1.0]}
Averages: {'Col 1': 0.1429, 'Col 2': 0.1429, 'Col 3': 0.1429, 'Col 4': 0.1429, 'Col 5': 0.1429, 'Col 6': 0.1429, 'Col 7': 0.1429}

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 


h.inv:

Float Matrix
Square matrix
Dimension: 7x7
Numbers' range: {'Col 1': [-0.0195, 0.0398], 'Col 2': [-0.0745, 0.0605], 'Col 3': [-0.0501, 0.071], 'Col 4': [-0.0545, 0.063], 'Col 5': [-0.0317, 0.0197], 'Col 6': [-0.0622, 0.0471], 'Col 7': [-0.0487, 0.041]}
Averages: {'Col 1': 0.0046, 'Col 2': -0.0086, 'Col 3': 0.0091, 'Col 4': 0.0085, 'Col 5': -0.0032, 'Col 6': -0.0081, 'Col 7': -0.0052}

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0014  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [35, 97], 'Col 2': [25, 71], 'Col 3': [20, 99], 'Col 4': [3, 55], 'Col 5': [44, 97], 'Col 6': [33, 99]}
Averages: {'Col 1': 65.8333, 'Col 2': 43.0, 'Col 3': 50.1667, 'Col 4': 21.3333, 'Col 5': 66.8333, 'Col 6': 65.5}

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: {'Col 1': [-3, 4], 'Col 2': [1, 4], 'Col 3': [3, 3], 'Col 4': [3, 4]}
Averages: {'Col 1': 0.5, 'Col 2': 2.5, 'Col 3': 3.0, 'Col 4': 3.5}

 4  4  3  4 
-3  1  3  3 
 

j.summary:
 Matrix(dim=[2, 4],listed=[[4, 4, 3, 4], [-3, 1, 3, 3]],inRange={'Col 1': [-3, 4], 'Col 2': [1, 4], 'Col 3': [3, 3], 'Col 4': [3, 4]},randomFill=1)

################
proj=proj.subM(5,15).copy:


Dimension: 5x15
Numbers' range: {'Col 1': [8, 81], 'Col 2': [2, 70], 'Col 3': [16, 99], 'Col 4': [23, 97], 'Col 5': [4, 55], 'Col 6': [15, 81], 'Col 7': [0, 63], 'Col 8': [29, 89], 'Col 9': [0, 93], 'Col 10': [24, 92], 'Col 11': [4, 68], 'Col 12': [5, 67], 'Col 13': [1, 98], 'Col 14': [32, 88], 'Col 15': [30, 69]}
Averages: {'Col 1': 42.4, 'Col 2': 40.2, 'Col 3': 52.6, 'Col 4': 60.8, 'Col 5': 33.0, 'Col 6': 60.4, 'Col 7': 21.2, 'Col 8': 51.4, 'Col 9': 52.6, 'Col 10': 69.8, 'Col 11': 33.0, 'Col 12': 44.4, 'Col 13': 36.2, 'Col 14': 56.2, 'Col 15': 49.4}

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Numbers' range: {'Col 1': [44, 91], 'Col 2': [39, 100], 'Col 3': [25, 77], 'Col 4': [4, 97], 'Col 5': [0, 96]}
Averages: {'Col 1': 74.2, 'Col 2': 77.0, 'Col 3': 57.6, 'Col 4': 46.4, 'Col 5': 30.8}

 44 100  53  58   0 
 89  96  25   6  33 
 61  39  77  97   7 
 86  86  62  67  18 
 91  64  71   4  96 

p.det:
 -10820004.999999838

p.adj:
 
Float Matrix
Square matrix
Dimension: 5x5
Numbers' range: {'Col 1': [-4539901.0, 3755164.0], 'Col 2': [-18026140.0, 15485715.0], 'Col 3': [-19008288.0, 16169132.0], 'Col 4': [-27964678.0, 32980302.0], 'Col 5': [-1371545.0, 1398700.0]}
Averages: {'Col 1': 504932.8, 'Col 2': 2112632.0, 'Col 3': 2193123.4, 'Col 4': -3822251.6, 'Col 5': -192002.0}

  -985711.0000  -5030820.0000  -5170488.0000   8761782.0000    463525.0000 
   572608.0000   2974905.0000   3199419.0000  -5379331.0000   -247290.0000 
 -4539901.0000 -18026140.0000 -19008288.0000  32980302.0000   1398700.0000 
  3722504.0000  15159500.0000  15775842.0000 -27509333.0000  -1203400.0000 
  3755164.0000  15485715.0000  16169132.0000 -27964678.0000  -1371545.0000 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Numbers' range: {'Col 1': [-0.3471, 0.4196], 'Col 2': [-1.4312, 1.666], 'Col 3': [-1.4944, 1.7568], 'Col 4': [-3.0481, 2.5845], 'Col 5': [-0.1293, 0.1268]}
Averages: {'Col 1': -0.0467, 'Col 2': -0.1953, 'Col 3': -0.2027, 'Col 4': 0.3533, 'Col 5': 0.0177}

 0.0911  0.4650  0.4779 -0.8098 -0.0428 
-0.0529 -0.2749 -0.2957  0.4972  0.0229 
 0.4196  1.6660  1.7568 -3.0481 -0.1293 
-0.3440 -1.4011 -1.4580  2.5425  0.1112 
-0.3471 -1.4312 -1.4944  2.5845  0.1268 

################
p:

Square matrix
Dimension: 5x5
Numbers' range: {'Col 1': [44, 91], 'Col 2': [39, 100], 'Col 3': [25, 77], 'Col 4': [4, 97], 'Col 5': [0, 96]}
Averages: {'Col 1': 74.2, 'Col 2': 77.0, 'Col 3': 57.6, 'Col 4': 46.4, 'Col 5': 30.8}

 44 100  53  58   0 
 89  96  25   6  33 
 61  39  77  97   7 
 86  86  62  67  18 
 91  64  71   4  96 

p.remove(c=1) and p.remove(r=2)

Square matrix
Dimension: 4x4
Numbers' range: {'Col 1': [39, 100], 'Col 2': [53, 77], 'Col 3': [4, 97], 'Col 4': [0, 96]}
Averages: {'Col 1': 72.25, 'Col 2': 65.75, 'Col 3': 56.5, 'Col 4': 30.25}

100  53  58   0 
 39  77  97   7 
 86  62  67  18 
 64  71   4  96 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Numbers' range: {'Col 1': [39, 100], 'Col 2': [55, 55], 'Col 3': [53, 77], 'Col 4': [4, 97], 'Col 5': [0, 96]}
Averages: {'Col 1': 72.25, 'Col 2': 55.0, 'Col 3': 65.75, 'Col 4': 56.5, 'Col 5': 30.25}

100  55  53  58   0 
 39  55  77  97   7 
 86  55  62  67  18 
 64  55  71   4  96 

################

r: 
Dimension: 5x4
Numbers' range: {'Col 1': [0, 100], 'Col 2': [7, 97], 'Col 3': [18, 86], 'Col 4': [4, 96]}
Averages: {'Col 1': 53.2, 'Col 2': 55.0, 'Col 3': 57.6, 'Col 4': 58.0}

100  39  86  64 
 55  55  55  55 
 53  77  62  71 
 58  97  67   4 
  0   7  18  96 

p==r.t:

True
################
id2:
 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


id2.addDim(2): 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 

id2.matrix:
 [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

################
id3:


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 

################
id4:


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


id4.delDim(6):

All rows have been deleted

Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################
id4: 
Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


id4.addDim(10)):
 
Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Float Matrix
Dimension: 2x3
Numbers' range: {'Col 1': [-5.5265, 13.7694], 'Col 2': [-22.9714, -13.3411], 'Col 3': [-23.5395, 6.7443]}
Averages: {'Col 1': 4.1214, 'Col 2': -18.1562, 'Col 3': -8.3976}

 -5.5265 -22.9714   6.7443 
 13.7694 -13.3411 -23.5395 


((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Numbers' range: {'Col 1': [0.8469, 0.8945], 'Col 2': [0.7784, 0.9135], 'Col 3': [0.0334, 1.9243]}
Averages: {'Col 1': 0.8707, 'Col 2': 0.846, 'Col 3': 0.9789}

0.8469 0.9135 1.9243 
0.8945 0.7784 0.0334 

################


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.5911, 786.4397], 'Col 2': [-1172.5631, 996.8718], 'Col 3': [-991.3664, 1215.7104], 'Col 4': [-71.5157, 569.8819], 'Col 5': [-35.376, 1143.2358], 'Col 6': [-1160.7398, 1059.6315]}
Averages: {'Col 1': -232.1963, 'Col 2': 473.0998, 'Col 3': 25.4454, 'Col 4': 314.401, 'Col 5': 572.4454, 'Col 6': 109.0211}

-1235.5911 -1172.5631  -454.8103   231.6343   -35.3760 -1160.7398 
  549.0669   711.6521  -633.2611   569.8819  1143.2358   352.7149 
 -797.0603   850.9062   417.9075   496.5723   405.5497  1059.6315 
   43.3267   869.5177  -991.3664   325.3115   374.2132  -599.9575 
  786.4397   582.2139   598.4924   334.5216   513.4495   562.6057 
 -739.3595   996.8718  1215.7104   -71.5157  1033.6000   439.8721 

f=f.intForm

Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235, 786], 'Col 2': [-1172, 996], 'Col 3': [-991, 1215], 'Col 4': [-71, 569], 'Col 5': [-35, 1143], 'Col 6': [-1160, 1059]}
Averages: {'Col 1': -232.1667, 'Col 2': 472.6667, 'Col 3': 25.3333, 'Col 4': 314.0, 'Col 5': 572.1667, 'Col 6': 108.8333}

-1235 -1172  -454   231   -35 -1160 
  549   711  -633   569  1143   352 
 -797   850   417   496   405  1059 
   43   869  -991   325   374  -599 
  786   582   598   334   513   562 
 -739   996  1215   -71  1033   439 

f2=f.roundForm(3)

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-1235.59, 786.44], 'Col 2': [-1172.56, 996.87], 'Col 3': [-991.37, 1215.71], 'Col 4': [-71.52, 569.88], 'Col 5': [-35.38, 1143.24], 'Col 6': [-1160.74, 1059.63]}
Averages: {'Col 1': -232.195, 'Col 2': 473.1, 'Col 3': 25.445, 'Col 4': 314.3983, 'Col 5': 572.445, 'Col 6': 109.02}

-1235.5900 -1172.5600  -454.8100   231.6300   -35.3800 -1160.7400 
  549.0700   711.6500  -633.2600   569.8800  1143.2400   352.7100 
 -797.0600   850.9100   417.9100   496.5700   405.5500  1059.6300 
   43.3300   869.5200  -991.3700   325.3100   374.2100  -599.9600 
  786.4400   582.2100   598.4900   334.5200   513.4500   562.6100 
 -739.3600   996.8700  1215.7100   -71.5200  1033.6000   439.8700 

f2-f1

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: {'Col 1': [-0.59, 0.44], 'Col 2': [-0.56, 0.91], 'Col 3': [-0.81, 0.91], 'Col 4': [-0.52, 0.88], 'Col 5': [-0.38, 0.6], 'Col 6': [-0.96, 0.87]}
Averages: {'Col 1': -0.0283, 'Col 2': 0.4333, 'Col 3': 0.1117, 'Col 4': 0.3983, 'Col 5': 0.2783, 'Col 6': 0.1867}

-0.5900 -0.5600 -0.8100  0.6300 -0.3800 -0.7400 
 0.0700  0.6500 -0.2600  0.8800  0.2400  0.7100 
-0.0600  0.9100  0.9100  0.5700  0.5500  0.6300 
 0.3300  0.5200 -0.3700  0.3100  0.2100 -0.9600 
 0.4400  0.2100  0.4900  0.5200  0.4500  0.6100 
-0.3600  0.8700  0.7100 -0.5200  0.6000  0.8700 

################
r.remove(r=2):

Square matrix
Dimension: 4x4
Numbers' range: {'Col 1': [0, 100], 'Col 2': [7, 97], 'Col 3': [18, 86], 'Col 4': [4, 96]}
Averages: {'Col 1': 52.75, 'Col 2': 55.0, 'Col 3': 58.25, 'Col 4': 58.75}

100  39  86  64 
 53  77  62  71 
 58  97  67   4 
  0   7  18  96 

r.rank: 4

r[0]=r[1][:]

Square matrix
Dimension: 4x4
Numbers' range: {'Col 1': [0, 58], 'Col 2': [7, 97], 'Col 3': [18, 67], 'Col 4': [4, 96]}
Averages: {'Col 1': 41.0, 'Col 2': 64.5, 'Col 3': 52.25, 'Col 4': 60.5}

53 77 62 71 
53 77 62 71 
58 97 67  4 
 0  7 18 96 

Determinant is 0, can't get lower/upper triangular matrices
r.rank: 3
################
for i in range(len(e.matrix)): e[i][-i-1]=99

Square matrix
Dimension: 8x8
Numbers' range: {'Col 1': [0, 99], 'Col 2': [0, 99], 'Col 3': [0, 99], 'Col 4': [0, 99], 'Col 5': [0, 99], 'Col 6': [0, 99], 'Col 7': [0, 99], 'Col 8': [0, 99]}
Averages: {'Col 1': 12.375, 'Col 2': 12.375, 'Col 3': 12.375, 'Col 4': 12.375, 'Col 5': 12.375, 'Col 6': 12.375, 'Col 7': 12.375, 'Col 8': 12.375}

99  0  0  0  0  0  0  0 
 0 99  0  0  0  0  0  0 
 0  0 99  0  0  0  0  0 
 0  0  0 99  0  0  0  0 
 0  0  0  0 99  0  0  0 
 0  0  0  0  0 99  0  0 
 0  0  0  0  0  0 99  0 
 0  0  0  0  0  0  0 99 


e+=50:

Square matrix
Dimension: 8x8
Numbers' range: {'Col 1': [50, 149], 'Col 2': [50, 149], 'Col 3': [50, 149], 'Col 4': [50, 149], 'Col 5': [50, 149], 'Col 6': [50, 149], 'Col 7': [50, 149], 'Col 8': [50, 149]}
Averages: {'Col 1': 62.375, 'Col 2': 62.375, 'Col 3': 62.375, 'Col 4': 62.375, 'Col 5': 62.375, 'Col 6': 62.375, 'Col 7': 62.375, 'Col 8': 62.375}

149  50  50  50  50  50  50  50 
 50 149  50  50  50  50  50  50 
 50  50 149  50  50  50  50  50 
 50  50  50 149  50  50  50  50 
 50  50  50  50 149  50  50  50 
 50  50  50  50  50 149  50  50 
 50  50  50  50  50  50 149  50 
 50  50  50  50  50  50  50 149 

for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:


Square matrix
Dimension: 8x8
Numbers' range: {'Col 1': [0, 1], 'Col 2': [0, 1], 'Col 3': [0, 1], 'Col 4': [0, 1], 'Col 5': [0, 1], 'Col 6': [0, 1], 'Col 7': [0, 1], 'Col 8': [0, 1]}
Averages: {'Col 1': 0.125, 'Col 2': 0.125, 'Col 3': 0.125, 'Col 4': 0.125, 'Col 5': 0.125, 'Col 6': 0.125, 'Col 7': 0.125, 'Col 8': 0.125}

1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 

################

c%j

Dimension: 2x4
Numbers' range: {'Col 1': [-2, 2], 'Col 2': [0, 0], 'Col 3': [0, 2], 'Col 4': [0, 3]}
Averages: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 1.0, 'Col 4': 1.5}

 2  0  0  3 
-2  0  2  0 

################

f.roundForm(3)>f.roundForm(1)
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Numbers' range: {'Col 1': [9, 34], 'Col 2': [-52, 88], 'Col 3': [3, 33]}
Averages: {'Col 1': 21.5, 'Col 2': 18.0, 'Col 3': 18.0}

 34 -52  33 
  9  88   3 

################
validStr2:

Dimension: 5x2
Numbers' range: {'Col 1': [3, 352], 'Col 2': [-5, 45]}
Averages: {'Col 1': 138.2, 'Col 2': 34.6}

312  45 
 12  44 
352  45 
 12  44 
  3  -5 

################
validStr3:

Dimension: 1x4
Numbers' range: {'Col 1': [34, 34], 'Col 2': [5, 5], 'Col 3': [44, 44], 'Col 4': [659, 659]}
Averages: {'Col 1': 34.0, 'Col 2': 5.0, 'Col 3': 44.0, 'Col 4': 659.0}

 34   5  44 659 

################
validStr4:

Dimension: 22x3
Numbers' range: {'Col 1': [125, 193], 'Col 2': [30, 105], 'Col 3': [9, 55]}
Averages: {'Col 1': 163.3636, 'Col 2': 62.1364, 'Col 3': 28.6818}

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################
"""
# =============================================================================

