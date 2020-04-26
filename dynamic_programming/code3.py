#M2[n,k]=〖max〗_(i=1)^n⁡{min⁡〖(M2[i,k-1],∑_(j=i+1)^j▒s_j 〗)}

#import sys
minimum = []
def min(a, b):
    if (a < b):
        return a
    else:
        return b

def LP2_recurse(arr,n,k):
    #print(arr)
    sum=0
    '''if k==1:
        return max(arr)
    if k==2:
        return min(arr[0],arr[n-1])
    '''
    if(k > 0):
        if(n == 1):
            return arr[0]
    if(k == 0):
        for x in range(1,len(arr)):
            print("Sum += Arr[",x,"] = ", arr[x])
            sum += arr[x]
            print("1 ",sum)
        return sum
    for i in range(0,n):
        sum = 0
        for j in range(i+1,n):
            #print("Sum += Arr[",j,"] = ", sum, arr[j])
            sum += arr[j]
        res_arr = arr[i+1:]
        print("2 ",sum)
        minimum.append(min(LP2_recurse(res_arr,len(res_arr),k-1),sum))
        print(minimum)
    return(max(minimum))
# Driver code
arr = [1,5,3,7,1,2]
#arr = [1,3,2,4,9,5]
size = len(arr)
print("Minimum Obtainable Value is", LP2_recurse(arr, size, 5))
