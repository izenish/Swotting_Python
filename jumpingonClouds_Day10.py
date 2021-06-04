n=1
# cloud=[0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0]
# print(x)
cloud=[0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# cloud=[0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0]
# count=0
# x=0
# i=0
# n=len(cloud)
# if(cloud[i]==0):
#         if(cloud[i+2]==0 and i<n):
#             print(f"currently i={i} value is {cloud[i+2]}")
#             i+=2
#             print(f"i is now {i}")
#             count+=1
#         elif(cloud[i+1]==0 and i<n):
#             print(f"currently i={i} value is {cloud[i+1]}")
#             i+=1
#             print(f"i is now {i}")
#             count+=1
#         # count+=1
# while(i<n-2):    
#         if(cloud[i+2]==0 and i<n):
#             print(f"currently i={i} value is {cloud[i+2]}")
#             i+=2
#             print(f"i is now {i}")
#             count+=1
#         elif(cloud[i+1]==0 and i<n):
#             print(f"currently i={i} value is {cloud[i+1]}")
#             i+=1
#             print(f"i is now {i}")
#             count+=1



        
# # if(cloud[n-2]==1):
# #     count+=1

# # print(count)
count=-1
        
cloud=[0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
for i in range(0,len(cloud)-1,2):
    if(cloud[i]==1):
        i-=1
        count+=1
    else:
        count+=1
no=len(cloud)-1
if(no%2==0):
    return count
else:
    return (count+1)