# class Open_file:
#     def __init__(self,filename,mode):
#         self.filename=filename
#         self.mode=mode

#     def __enter__(self):
#         self.file=open(self.filename,self.mode)
        

#         return self.file

#     def __exit__(self,exc_type,exc_val,traceback):
#         self.file.close()




# with Open_file('sample.txt','w') as f:
#     f.write('Testing')

# print(f.closed)


#using a function
from contextlib import contextmanger

@contectmanager
def open_file(file,mode):
    f=open(file,mode)
    yield f.close()


with open_file('SamepleTextWithContextLib','w') as f:
    f.write('lorem ipsum dolor')

print(f.closed)