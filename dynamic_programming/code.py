import time

def LP2_dynamic(n,k,arr):
	#initialize total array
	total = [0] * (n+1)
	#initialize matrix / table
	M = [[0 for x in range(k+1)] for y in range(n+1)]
	#initialize traceback table
	Traceback = [[0 for x in range(k+1)] for y in range(n+1)]
	#first total will always be 0
	total[0] = 0
	#fill in preliminary totals
	for i in range(1,n+1):
		total[i] = arr[i-1] + total[i-1]

	#fill in remainder of matrix
	for i in range(1,n+1):
			M[i][1] = total[i]
	for i in range(1,k+1):
		M[1][i] = arr[0]


	for i in range (2,n+1):
		for j in range(2,k+1):
			M[i][j] = -1

			for x in range(1,i):
				p = min(M[x][j-1],total[i]-total[x])
				if M[i][j] < p:
					M[i][j] = p
					#keep track of traceback
					Traceback[i][j] = x
	#print out traceback table
	for i in range(n+1):
		for j in range(k+1):
			print(Traceback[i][j], end='   ')
		print('\n',end='')

	#traceback step
	temp = k
	#trace for end result
	trace = []
	temp = Traceback[n][k]
	trace.append(temp)
	i = 1
	while temp > 0:
		temp = Traceback[trace[i-1]][k-i]
		if temp == 0:
			break
		trace.append(temp)
		i = i+1


	#formatted output
	for i in range(0,len(arr)):
		if i in trace:
			print("D",arr[i],end=' ')
		else:
			print(arr[i],end=' ')
	print()
	#return fairness index
	return M[n][k]


def LP2_recurse(n,k,arr):

	if(n==1):
		return arr[0]

	total = [0] * (n+1)
	total[0] = 0

	for i in range(1,n+1):
		total[i] = arr[i-1] + total[i-1]

	if(k==1):
		return total[n]


	all_min_values=[]

	for i in range(1,n+1):

		totalDiff= total[n]-total[i]
		all_min_values.append(min(LP2_recurse(i,k-1,arr),total[n]-total[i]))


	return max(all_min_values)





#arr = [1,2,3,4,5,6,7,8,9]
#arr = [1,5,3,7,1,2]
#arr = [1,3,2,4,9,5]
arr = [10,6,7,3,8,5,7,9,11,7,15,10,12,6,19,7,3,12,14,6]
size = len(arr)
k = 4
print(LP2_dynamic(size,k,arr))
start = time.time()
print(LP2_recurse(size,k,arr))
print("n:",size,"k:",k,"time:", time.time()-start)
