# Code by Aron Talai
# Pick random A to test your code

#################
A=1041			#
#################


# Convert to Binary
Binary_num="{0:b}".format(A)
Indexs_of_ones=[]
Dist_between_ones=[]

print(Binary_num)
# Find index for all the 1's in given binary sequence
for i in range(0,len(Binary_num)):

	if int(Binary_num[i])==1:
		Indexs_of_ones.append(i)

# Find the distance between the 1 indices
for i in range(0,len(Indexs_of_ones)-1):

	if (Indexs_of_ones[i+1]-Indexs_of_ones[i]-1 >0):

		Dist_between_ones.append(Indexs_of_ones[i+1]-Indexs_of_ones[i]-1)

# Print the longest distance as "Binary Gap"
print (max(Dist_between_ones))
