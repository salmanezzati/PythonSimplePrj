



def parent():
    print("Do something in parent")

    def firstChild():
        print("Do something in firstChild")

    def secondChild():
        print("Do something in secondChild")

    firstChild()
    secondChild()

#firstChild()
parent()
