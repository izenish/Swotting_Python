x=[2,3]
for i in x:
    print(i)
# swap(x[0],x[1])- this doesnt work
x[0], x[1] = x[1], x[0]
for i in x:
    print("after swap",i)
