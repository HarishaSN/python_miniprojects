input_array=list()
for i in range(3):
    input_array.append(list(map(int,input().split(" "))))
print(input_array)

def horizontal(a:list):
    for i in a:
        if(len(set(i))==1):
            print(str(i[0])+" won")
            break
    return

#horizontal(input_array)
                       
def vertical(a:list):
    for i in range(3):
        arr=list()
        for j in range(3):
            arr.append(a[j][i])
        if(len(set(arr))==1):
            print(str(arr[0])+"won")
            break
    return

vertical(input_array)
    
