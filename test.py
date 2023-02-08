import os


path, dirs, files = next(os.walk('/train'))


print("There is")
print(len(files))
print("files in train")