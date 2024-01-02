class library():
    
    def __init__(self, listofbooks):
        self.books=listofbooks
        
    def displayAvailableBooks(self):
        print("The books are")
        for index,book in enumerate(self.books):
            print(index,"--->",book)
            
    def borrowbook(self,bookname):
        if bookname in self.books:
            print("the books name is {}, keep it's safe and return within 21 days")
            self.books.remove(bookname)
            return True
                
        else:
            print("the book is  already returned to someone else, keep wait until book keeps us")
            return False
        
    def returnbook(self,bookname):
        self.books.append(bookname)
        print('thanks for returning the particular book in the correct time.')



class students():
    def requestbook(self):
        self.book=input("Enter the book you want to borrow")
        return self.book

    def returnbook(self):
        self.book=input("Enter the  book you want to return")
        return self.book 
    
    pass

if __name__ == "__main__":
    centraLibrary = library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student=students()
    
    # centraLibrary.displayAvailableBooks()
    
    while (True):
        welcomemsg='''  \n  --welcome to class library
        Please to choose an option
        1. List all the books
        2.Request a bok
        3.Add/return a book
        4. Exit the library'''
    
        print(welcomemsg)
        
        a=int(input("Enter a choice:"))
        
        if a==1:
            centraLibrary.displayAvailableBooks()
            
        
        if a==2:
            centraLibrary.borrowbook(student.requestbook())
            
        if a==3:
            centraLibrary.returnbook(student.returnbook())
            
        if a==4:
            print("Thanks for coming")
            exit()
            
        else:
            "invalid syntax"
    
    
    
    
    
    
    