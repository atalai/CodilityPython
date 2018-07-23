# Code by Aron Talai
# Pick random A and K below to test your code

#################
A=[3,8,9,7,6]	#
#A=[0,0,0]		#
k=4				#
#################

# init
shifted_a = [0] * len(A)
shifted_a_temp = [0] * len(A)

# temp init
shifted_a=A
shifted_a_temp=A

# main loop
for j in range(1,k+2):

    shifted_a=shifted_a_temp
    shifted_a_temp=[0]*len(A)

    # rotation loop
    for i in range(1,len(A)): #len=5

        shifted_a_temp[0]=shifted_a[len(A)-1]
        shifted_a_temp[i]=shifted_a[i-1]

print shifted_a #The requested answer is located in shifted_a

