def LP2_recurse(arr, n, k):
    #if n = 1, there is only 1 element left at the end of arr
    if n == 1:
        return arr[0]
    #if k == 1 then we are on our last segment
    #then return the cost of everything remaining
    if k == 1:
        sum = 0
        for i in range(0,n):
            sum += arr[i]
        return sum
    #array to keep track of all of our mins we find
    #eventually we will take the max of this as per LP2
    mins = []
    for i in range(1,n):
        #calculate the min
        sum = 0
        for j in range(i, n):
            sum += arr[j]
        #append to mins
        mins.append(min(LP2_recurse(arr,i,k-1),  sum  ))
        #print(mins)

    return max(mins)


# Driver code
#arr = [1,2,4]
#arr = [1,2,3,4,5,6,7,8,9]
#arr = [1,5,3,7,1,2]
#arr = [1,3,2,4,9,5]
arr = [10,6,7,3,8,5,7,9,11,7,15,10,12,6,19,7,3,12,14,6]
size = len(arr)
number_of_breaks = 4
print(LP2_recurse(arr, size, number_of_breaks))
