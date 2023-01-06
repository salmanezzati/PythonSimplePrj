import os

if not os.path.exists("Files"):
    os.mkdir("Files")

fo = open('Files/Text_1.txt' , 'w')
fo.write("hi python\n")
fo.close()

fo = open('Files/Text_1.txt' , 'r')
print(fo.readline())
fo.close()


fo = open('Text_1.txt' , 'w')
# fo.write("hi python\n")
fo.write('my name : ')
fo.write('sam')
fo.close()

fo = open('Text_1.txt' , 'r')
print(fo.readline())
fo.close()


os.rename('Text_1.txt' , 'Text_2.txt')
# os.remove('Text_2.txt')
