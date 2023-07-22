# import os
# for i in range(1,27):
#     dir1 = open(f'file{i}.txt' , 'x')
file = open('file1.txt' , 'x')
file = open('file1.txt' , 'w')
for i in range(65,91):
    file.write("{} Ascii {}\n".format(chr(i),i))