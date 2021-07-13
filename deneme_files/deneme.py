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
            if bookid == row[0]:
                recoveryArray.remove(row)

    with open(booksFile,'w') as booksFile: 
        writer = csv.writer(booksFile)
        for row in recoveryArray:
            writer.writerow([row[0]],[row[1]],[row[2]])

deneme = Book(0,"deneme",True)

remove("books2.csv",deneme.bookid)

