# path="UDUUUDUDDD"
# steps=8
# count=0
# list=[]
# for x,y in enumerate(path):
#     print(x,y)
#     if(y=="U"):
#         list.append(x)


# print(list)
# # print(path[x-1] and path[x-2] and path[x+1])

# for x in list[1:-1]:
#     x1=path[x-1]
#     x2=path[x-2]
#     x3=path[x+1]

#     # if(path[x-1] and path[x-2] and path[x+1] =="D"):
#     if(x1+x2+x3=="DDD"):
#         count=count+1

        
#         # print(x1+x2+x3)

#         # print(f"In turn {x} path[x-1] is {path[x-1]} path[x-2] is {path[x-2] }and path[x+1] is {path[x+1]}")

# print(count)



# path="UDUUUDUDDD"
# length=10
# height=0
# # sealevel=0
# count=0
# # print("test")
# for i in path:
#     if i=="D":
#         height-=1
#         sealevel=-1
#     elif i=="U" and height<0:
#         height+=1
#     else:
        
#     if(height==0):
#         count+=1
# print(count)




path="UDUUUDUDDD"
length=10
height=0
count=0
# sealevel=0
for i in path:
    if i=="U" :
        height+=1
        if(height==0):
            count+=1
        
    elif i=="D":
        height-=1
        
print(count)