

def sum (a , b) :
    assert (type(a) is int and type(b) is int) , "Numbers must be int"
    assert (a >= 0 and b >= 0) , "arquments must be bigger than zero"
    return a + b

print(sum(5 , 2))
#print(sum('h' , 2))
#print(sum(-1 , 2))

#fo = open('Text.txt' , 'w')
#fo.write("hi python\n")
#fo.close()

try :
    fo = open('Text.txt' , 'r')
    text = fo.readline()
    print(text)

except Exception as error :
    print(error)

else :
    print('Ok')
    fo.close()
