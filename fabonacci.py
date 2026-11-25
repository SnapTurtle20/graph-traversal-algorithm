e=int(input("enter position: "))
if e<0 or e>9:
   print("invalid position")
m=int(input("enter number of moves: "))
if m<0:
   print("enter positive number of moves")
o=m
a={1:[6,8],
   2:[7,9],
   3:[4,8],
   4:[3,9,0],
   6:[1,7,0],
   7:[2,6],
   8:[1,3],
   9:[2,4],
   0:[4,6]
   }
b={1:[[0,0] for _ in range(o+1)],
   2:[[0,0] for _ in range(o+1)],
   3:[[0,0] for _ in range(o+1)],
   4:[[0,0] for _ in range(o+1)],
   6:[[0,0] for _ in range(o+1)],
   7:[[0,0] for _ in range(o+1)],
   8:[[0,0] for _ in range(o+1)],
   9:[[0,0] for _ in range(o+1)],
   0:[[0,0] for _ in range(o+1)]
   }
c=[[-1,-1] for _ in range(o+1)]

def next(pos,moves):
    global a
    global b
    global o
    global c
    if not b[pos][moves][1]==1:
       for j in range(o+1):
           if pos==c[j][0]:
               for i in range(moves+1):
                   b[pos][moves][0]=0
       for i in range(o,-1,-1):
           if(c[i][0]==pos):
               c[i][1]=moves
               break
       c[(o - moves)][0] = pos
       d = []
       for i in range(len(c) - 1, o-moves, -1):
           d.append(i)
       for i in d:
           c[i] = [-1,-1]
       print(d)
       for i in range(len(c)):
           if not c[i][0]==-1 and ((not c[i][1]==-1 and o-i-moves>c[i][0]-c[i][1]) or c[i][1]==-1):
               b[c[i][0]][o-i-moves][0]+=1
       print(b)
       print(c)
       if not moves==0:
          for i in a[pos]:
             next(i,moves-1)
    b[pos][moves][1]=1
if (e==5 and m>=0) or m==0:
   print(1)
elif 0<=e<=9 and m>=0:
   next(e,m)
   print(b[e][m][0])