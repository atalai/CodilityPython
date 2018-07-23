# Code by Aron Talai
# Pick random A to test your code

#####################
A=[1,3,6,4,1,2]
#Test_array=[4,1,3]
#####################

def solution(A):
    
    Test_array=sorted(A)
    
    if max(Test_array)<0:
        return 1
        
    for i in range(0,len(Test_array)):
        
        if i+1<len(Test_array):
            if Test_array[i]==Test_array[i+1] or Test_array[i+1]== 1 + Test_array[i]:
                pass
            else:
                return Test_array[i]+1
        else:
            return Test_array[i]+1
        
    pass
