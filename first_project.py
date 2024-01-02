print("welcome to my mini game project.")

playing=input("Are you want to play with me ?.")
if playing!="yes":
    quit()

print("Let's start with me")
mark=0
answer=input("are you learn python ? ") # 1
if answer.lower()=="yes":
    print("ok let's go next question")
    mark +=1  
else:
    print("incorrect!")
    
answer=input("what is full form of Py ? ") # 2

if answer.lower()=="python":
    print("ok let's go next question")
    mark +=1  
else:
    print("incorrect!")
 
answer=input("full form of OS ? ") # 3

if answer.lower()=="operating system":
    print("ok let's go next question")
    mark +=1  
else:
    print("incorrect!")
answer=input("what is  DSA stand for ? ") # 4

if answer.lower()=="data structure":
    print("ok let's go next question")
    mark +=1 
else:
    print("incorrect!")

answer=input("what means by program ? ") # 5

if answer.lower()=="coding":
    print("ok let's go next question")
    mark +=1  
else:
    print("incorrect!")

answer=input("bca stands for ? ") # 6

if answer.lower()=="bachelor of computer application":
    print("End of quiz and let calculate your score")
    mark +=1  
else:
    print("incorrect!")

print("your score is ",str ((mark//6)*100) , "mark")
print("correct is ",str(mark))


    

    