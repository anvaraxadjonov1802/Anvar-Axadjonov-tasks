# Lug'atlar topshiriq
# 1-topshiriq
"""
# Lug’atni qiymatlari bo’yicha saralang.
dic = {
    "book" : 7,
    "notebook" : 10,
    "Phone" : 17,
    "PC" : 0,
}


# 1-usul
'''
natija = []
for i, j in dic.items():
    natija.append(j)
natija.sort()
print(natija)
'''

# 2-usul
'''
result = []

for key, values in dic.items():
    result.append(values)

uzunlik = len(result)

for i in range(uzunlik):
    min_idx = i
    for j in range(i+1, uzunlik):
        if result[j] < result[min_idx]:
            min_idx = j
        
    result[i], result[min_idx] = result[min_idx], result[i]         
print(result)
'''
"""

# 2-topshiriq
'''
# Lug’atni qiymatlari bo’yicha saralang.
dic = {
    1 : 7,
    3 : 10,
    5 : 17,
    2 : 0,
}
'''

# 3-topshiriq
'''
# Lug’atga yangi kalit va qiymat qo’shing.
dic = {}
dic["yangi kalit"] = "yangi qiymat"
print(dic)
'''

# 4-topshiriq
'''
# Berilgan uchta lug’atni birlashtiruvchi dastur tuzung.
dic1 = {
    1: "a",
    2: "b"
}
dic2 = {
    3: "c",
    4: "d"
}
dic3 = {
    5: "e",
    6: "f"
}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
'''

# 5-topshiriq
'''
# Berilgan qiymati Lug’atda bor yoki yo’qligini tekshiruvchi funksiya yarating

dic = {
    1: "user1",
    2: "user2",
    3: "user3"
}
lst = []
qidiruv = input(">> ")
for i , j in dic.items():
    lst.append(j)

if qidiruv in lst:
    print("Bor")
else:
    print("Yo'q")
'''

# 6-topshiriq
'''
# n butun soni berilgan. {1: 1, 2: 4, 3: 9, …, n: n2} ko’rinishidagi lug’at hosil qiling.

dic = {}
n = int(input(">> "))

for i in range(1, n+1):
    dic[i] = i**2
print(dic)
'''

# 7-topshiriq
'''
# Berilgan lug’atdagi qiymatlar yig’indisini hisoblang
dic = {
    1: 2,
    2: 12,
    3: 23,
    4: 24,
    5: 52,
    6: 27,
}
sum = 0
for i, j in dic.items():
    sum+=j
print(sum)
'''

# 8-topshiriq
'''
# Lug’atdan berilgan kalit bo’yicha qiymati o’chiradigan dastur tuzing.

dic = {
    1: 2,
    2: 12,
    3: 23,
    4: 24,
    5: 52,
    6: 27
}
dic.pop(int(input(">>")))
print(dic)
'''

# 9-topshiriq
'''
# Berilgan lug’atning bo’sh yoki bo’sh emasligini tekshiring.

def tekshir(dic):
    if dic.items():
        print("Bo'sh emas")
    else:
        print("Bo'sh")  


dic1 = {}
dic2 = {
    1:2
}

tekshir(dic1)    
tekshir(dic2)    
'''

# 10-topshiriq
'''
#Berilgan satrga ko’ra quyidagicha lug’at yarating:
# s = `assalom`
# d = {`a`: 2, `s`: 2, `l`: 1, `o`: 1, `m`: 1}

satr = input(">> ")
dic = {}
cont = 0

for i in satr:
    for j in satr:
        if i == j:
            cont += 1
    
    dic[i] = cont
    cont = 0
print(dic)
'''


# Sodda klasslarga doir misollar


# 1. Ixtiyoriy ikkita son berilgan. Ularning yig„indisini,
# ayirmasini, ko’paytmasini va nisbatini toping.








# 2. To’g„ri burchakli uchburchakning katetlari a va b.
# Uchburchakning yuzi va perimetrini toping.
# 3. Radiusi R bo’lgan aylananing uzunligini va doiraning
# yuzini toping.
# 4. Doiraning yuzi S. Uning radiusini toping.
# 5. A(x1,y1) va B(x2,y2) nuq‟talar koordinatalari bilan
# berilgan. Ular orasidagi masofani toping.
# 6. Tekislikda uchburchak uchlarining koordinatasi
# A(x1,y1) , B(x2,y2) va S(x3,y3). Uchburchakning yuzini toping.
# 7. Ikki sonning o’rta arifmetik va o’rta geometrik
# q‟iymatlarini toping.
# 8. To’g’ri to’rtburchak diagonali uchlarining
# koordinatalari berilgan. Uning yuzini toping.
# 9. Uch xonali butun son berilgan. Bu son raqamlarining
# yig’indisini va ko’paytmasini toping







