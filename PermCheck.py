# Code by Aron Talai
# Pick random A to test your code

#####################
Test_array=[4,1,3,2]
#Test_array=[4,1,3]
#####################


Num_of_int_in_array=len(Test_array)
Sample=[]

for i in range(1,Num_of_int_in_array+1):

	Sample.append(i)

Test_array=sorted(Test_array)

if Test_array==Sample:

	print("Permutational Array detected")

else:

	print("Non permutational Array detected")