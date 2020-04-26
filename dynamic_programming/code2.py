#M2[n,k]=〖max〗_(i=1)^n⁡{min⁡〖(M2[i,k-1],∑_(j=i+1)^j▒s_j 〗)}

import sys
minimum = []
def max(a, b):
    if (a > b):
        return a
    else:
        return b

def LP2_recurse(arr,n,k):
    sum=0
    '''if k==1:
        return max(arr)
    if k==2:
        return min(arr[0],arr[n-1])
    '''
    if(k > 1):
        if(n == 0):
            return arr[0]
    if(k == 0):
        for x in range(0,n):
            sum += arr[x]
            print(sum)
            return sum
    for i in range(0,n):
        sum = 0
        for j in range(i+1,n):
            sum += arr[j]
        res_arr = arr[i:]
        #print(res_arr)
        minimum.append(max(LP2_recurse(res_arr,len(res_arr),k-1),sum))
    print(minimum)
    return(min(minimum))
# Driver code
arr = [1,5,3,7,1,2]
size = len(arr)
print("Max of Mins", LP2_recurse(arr, size, 3))
