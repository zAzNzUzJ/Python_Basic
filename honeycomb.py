
# x=int(input())
# y=int(input())
n=input().split()
x=int(n[0])
y=int(n[1])
row = x*2 +1
col = y*2 +1
matrix = [[str(0) for x in range(col)] for y in range(row)]


for i in range(1,row):
    for j in range(0,col,4):
        if i %2==0 and j !=col-1:
            matrix[i][j]="\\"
            matrix[i][j+1]="___"
            matrix[i][j+2]="/"
            if j!=0:
                matrix[i][j-1]="   "
        else :
            matrix[i][j]="/"
            matrix[i][j+1]="   "
            matrix[i][j+2]="\\"
            if j!=0:
                matrix[i][j-1]="___"
        if j%2==0:
            matrix[0][j]=" "
            matrix[0][j+1]="___"
            matrix[0][j+2]=" "
            if j!=0:
                matrix[0][j-1]="   "
            
        


# for j in range(0,col,2):
#     matrix[0][j]=" "
# for j in range(1,col,4):
#     matrix[0][j]="___"
# for j in range(3,col,4):
#     matrix[0][j]="   "
    

# for j in range(0,col):
#     if j%2==0:
#         matrix[0][j]=" "
#     else:
#         matrix[0][j]="___"
# for j in range(3,col,4):
#     matrix[0][j]="   "
        
    
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end="")
    print("")

    
            
