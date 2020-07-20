import winsound
import random
winsound.PlaySound("bg.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def display():
    global chances
    one="""            +---+
            |   |
            0   |
                |
                |
                |
           ======="""
    two="""            +---+
            |   |
            0   |
            |   |
                |
                |
           ======="""
    three="""              +---+
              |   |
              0   |
             /|   |
                  |
                  |
             ======="""
    four="""            +---+
            |   |
            0   |
           /|\  |
                |
                |
           ======="""
    five="""            +---+
            |   |
            0   |
           /|\  |
           /    |
                |
           ======="""
    zero="""            +---+
            |   |
                |
                |
                |
                |
           ======="""
    six="""            +---+
            |   |
            0   |
           /|\  |
           / \  |
                |
           ======="""
    if chances==5:
        print(one)
    elif chances==4:
        print(two)
    elif chances==3:
        print(three)
    elif chances==2:
        print(four)
    elif chances==1: 
        print(five)
    elif chances==0:
        print(six)
    else :
        print(zero)
def read():
    global word
    fruits=["AVOCADO","PASSION FRUIT","SAPODILLA","KIWI","BANANA","APPLE","ORANGE","JACKFRUIT","GRAPES","PEACH"]
    places=["BENGALURU","BARCELONA","LIVERPOOL","NEW YORK","NEW DELHI","DARJEELING","VATICAN CITY","ISTANBUL","MUNICH"]
    animals=["TIGER","ANTELOPE","LION","HIPPOPOTAMUS","PLATYPUS","GORILLA","CHEETAH","JAGUAR","ELEPHANT"]
    print("""Enter 1 for fruits \nEnter 2 for places\nEnter 3 for animals""")
    c=int(input())
    if c==1:
        word=list(random.choice(fruits))
    elif c==2:
        word=list(random.choice(places))
    elif c==3:
        word=list(random.choice(animals))
    else:
        print("Wrong Input!")
        read()
word=[]
read()
answer=[]
used=[]
count=0
chances=6
alen=0
display()
def game():
    global word,answer,used,count,chances,alen
    #print(word)
    for i in word:
        if i.isalpha():
            answer.append("_")
            alen+=1
        else:
            answer.append(" ")
    #print((" ").join(answer))
    #print(alen)
    while count<alen and chances>0:
        print("Chances left:",chances)
        print((" ").join(answer),end="\n")
    #   print("Used letters are: ",(" ").join(used),end="\n")
        c=input()
        c=c.upper()
        if c in word and c not in used:
             for i in range(len(word)):
                if word[i]==c:
                    answer[i]=c
                    count+=1
             used.append(c)
             winsound.PlaySound("cn.wav",winsound.SND_ALIAS)
        elif c in used:
            print("You have already guessed this letter")
        else :
            winsound.PlaySound("wr.wav",winsound.SND_ALIAS)
            used.append(c)
            chances-=1
        winsound.PlaySound("bg.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
        display()
        print("Used letters are: ",(" ").join(used),end="\n")
    if count==alen:
        winsound.PlaySound("win.wav",winsound.SND_ALIAS)

        print("CONGRATULATIONS!!YOU HAVE GUESSED THE WORD {} AND SAVED THE MAN!".format(("").join(word)))
    else :
                winsound.PlaySound("lose.wav",winsound.SND_ALIAS)
                print("YOU HAVE HANGED THE MAN (: ")
                print("THE ANSWER IS : ",(" ").join(word))  
            
game()
        
