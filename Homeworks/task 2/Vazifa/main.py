#OOP4-dars 6-masala
class Library:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.a = []

    def add(self):
        self.a.append((self.name, self.author, self.year))
        return self.a

    def search(self,name):
        for i in range(len(self.a)):
            if name == self.a[i][0]:
                return self.a
            
    def remove(self, name):
        for i in range(len(self.a)):
            if name == self.a[i][0]:
                self.a.remove(self.a[i])

    def str(self):
        return f'{self.name},     {self.author},     {self.year}'


a = [Library('O`tgan kunlar', 'Abdulla Qodiriy', 1921), Library('O`tgan kunlar', 'Abdulla Qodiriy', 1922),
     Library('O`tgan kunlar', 'Abdulla Qodiriy', 1923), Library('O`tgan kunlar', 'Abdulla Qodiriy', 1924),
     Library('O`tgan kunlar', 'Abdulla Qodiriy', 1925), Library('O`tgan kunlar', 'Abdulla Qodiriy', 1926),
     Library('O`tgan kunlar', 'Abdulla Qodiriy', 1920), Library("Ikki eshik orasida", 'Erkin Vohidov', 1986)]
f = []
for i in a:
    f.append(i.add()) # kitoblarni jamlab oldik

print("Barcha kitoblar: ")
for i in range(len(f)):
    print(i+1," - ", f[i]) # Hammasini ekranga chop etdik

for i in a:
    natija = i.search("Ikki eshik orasida")
    if natija:
        print("Qidiruv natijasi: ",natija)   #Qidirilayotgan Kitob haqida ma'lumotni chop etdik

for i in a:
    natija = i.remove("Ikki eshik orasida") #Kitobni o'chirdik


print("Barcha kitoblar: ") #Natijani ko'rish uchun hamma kitobni yana chop etdik
for i in range(len(f)):
    print(i+1," - ", f[i])

