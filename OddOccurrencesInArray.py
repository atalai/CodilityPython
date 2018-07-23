# Code by Aron Talai
# Pick random A to test your code

#######################
#A=[9,3,9,3,9,7,9]	  #
#A=[1,1,1,10,11,10,2] #
A=[10,10,12,2,2,3,12] #			
#######################

# Sort to have numbers in order
sorted_a=sorted(A)

# the idea is that we are looking for a number which is different from it's 
# left and right side

# Main loop 
for i in range(1,len(A)):

	if (sorted_a[i-1]!=sorted_a[i]) and (sorted_a[i]!=sorted_a[i+1]):
		break # break when number found

answer=sorted_a[i]

print answer #The requested answer is located in sorted_a[i] 
