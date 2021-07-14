import csv

class Book():
    def __init__(self,bookid,name,isRead):
        self.bookid = bookid
        self.name = name
        self.isRead = isRead


def remove(booksFile,bookid):
    recoveryArray = []
    with open(booksFile,'r') as booksFile:
        reader = csv.reader(booksFile)
        for row in reader:
            recoveryArray.append(row)
            if bookid == int(row[0]):
                recoveryArray.remove(row)
    

    with open("desktop/codes/library_manager/deneme_files/books2.csv",'w') as booksFile: 
        writer = csv.writer(booksFile)
        for row in recoveryArray:
            writer.writerow([row[0],row[1],row[2]])


deneme = Book(0,"deneme",True)


def add(booksFile,bookid,bookName,isRead):
    newBook = Book(bookid,bookName,isRead)

    with open(booksFile,"a") as booksFile:
        writer = csv.writer(booksFile)
        writer.writerow([str(newBook.bookid),newBook.name,str(newBook.isRead)])
        
    
    print("added: ",newBook.name)


remove("desktop/codes/library_manager/deneme_files/books2.csv",deneme.bookid)
add("desktop/codes/library_manager/deneme_files/books2.csv",0,"deneme",True)

