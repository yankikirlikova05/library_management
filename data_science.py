#satın alınacak listesindekilere satın alma linkleri eklenebilir (en ucuz falan ya da cimri.com linki)

import csv


booksFile = "books.csv"
#tüm kitapların olduğu csv dosyası olacak
#kitap class'ında kitap id, kitap adı, kitap okundu: true/false

class Book():
    def __init__(self,bookid,name,isRead):
        self.bookid = bookid
        self.name = name
        self.isRead = isRead
    

#removes any book from the csv file
#belki aynı anda belli id aralığındaki kitapları silme de eklenebilir
#bu fonksiyonun başka bi yerde test edilmesi lazım muhtemelen çalışmayacak, mantıktan eminim ama data türlerinde sıkıntı olabilir
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

#zaten okunacaklar listesinde olan bir kitabı okundaya çevirme eklenecek


def add(booksFile,bookid,bookName,isRead):

