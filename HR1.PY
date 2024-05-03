Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by (I,J,K) on a 3D grid where the sum I+J+K of  is not equal to n . Here, 0<=ix;0<=j<=y;0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.
  if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans=[]
    for i in range(x+1):
     for j in range(y+1):
        for k in range(z+1):
         if i+j+k!=n:
                  ans.append([i,j,k])
    print(ans)
