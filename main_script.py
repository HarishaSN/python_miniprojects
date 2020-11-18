input_array=list()
for i in range(3):
    input_array.append(list(map(int,input().split(" "))))

def horizontal(a:list):
    for i in a:
        if(len(set(i))==1):
            return i[0]
            break
    return -1

                       
def vertical(a:list):
    for i in range(3):
        arr=list()
        for j in range(3):
            arr.append(a[j][i])
        if(len(set(arr))==1):
            return arr[0]
    return -1


def diagonal(a:list):
    arr=list()
    count=2
    arr.append([])
    for i in range(3):
        arr[-1].append(a[i][i])
    arr.append([])
    for j in range(3):
        arr[-1].append(a[j][count])
        count-=1
    for i in arr:
        if(len(set(i))==1):
            return i[0]
    return -1

i=horizontal(input_array)   #checking if any horizontal lines are equal
if(i!=-1):
    print(str(i)+"won")
    exit()
j=vertical(input_array)     #checking if any vertical lines are equal
if(j!=-1):
    print(str(j)+"won")
    exit()
k=diagonal(input_array)     #checking if any diagonals are equal
if(k!=-1):
   print(str(k)+"won")
   exit()
print("no one won")         #printing no one won when no one won

        
    
