# Metodli klasslarga doir misollar
# 1. Ixtiyoriy ikkita son berilgan. Bu sonlar ustida
# bajarilishi mumkin bo’lgan masalalarni yechish metodlarini o’z ichiga
# olgan klass tuzing. Masalan, bu sonlarning yig’indisini, ayirmasini,
# ko’paytmasini, nisbatini, maksimumini, mininumini, o’rta arifmetik
# qiymatini, o’rta geometrik qiymatini va h.k.larni toping. Asosiy
# programmada klass turidagi obyektlar hosil qiling. Ulardan foydalanib,
# masalalarni yeching.

import math

class matem():
    def yig(self, son1, son2):
        print("Yig'indisi: ", son1+son2)

    def ayir(self, son1, son2):
        print("Ayirmasi: ",son1-son2)

    def kopaytr(self, son1, son2):
        print("Kopaytmasi: ",son1*son2)

    def nisbat(self, son1, son2):
        print("Nisbati: ",son1/son2)
        
    def maxsimum(self, son1, son2):
        lst = [son1, son2]
        print("Maxsimum: ",max(lst))

    def minimum(self, son1, son2):
        lst = [son1, son2]
        print("Minimum: ",min(lst))
        
    def orta_arifmetik(self, son1, son2):
        sum = 0
        lst = [son1, son2]
        for i in range(len(lst)):
            sum +=lst[i]
        print("O'rta arifmetik: ", sum/len(lst))

        
    def orta_geometrik(self, son1, son2):
        sum = 1
        lst = [son1, son2]
        for i in range(len(lst)):
            sum*=lst[i]
        
        print("O'rta geometrik: ",math.pow(sum, 1/len(lst)))

if __name__ == "__main__":
    obj = matem()
    a = int(input("Son1 :"))
    b = int(input("Son2 :"))
    obj.yig(a,b)
    obj.ayir(a,b)
    obj.kopaytr(a,b)
    obj.nisbat(a,b)
    obj.maxsimum(a,b)
    obj.minimum(a,b)
    obj.orta_arifmetik(a,b)
    obj.orta_geometrik(a,b)

# 2. Tomonlarining uzunligi ma‟lum bo’lgan
# uchburchakka tegishli masalalarni yechish metodlarini o’z ichiga olgan
# klass yarating. Asosiy programmada klass turidagi obyektlar hosil qiling.
# Ulardan foydalanib, masalalarni yeching.
# 3. Ikki sondan eng kattasini va eng kichigini topish
# uchun klass yaratining. Asosiy programmada bu klass turidagi obyektlar
# yaratining. Klassdan foydalanib, ikkita sonning eng kattasini va eng
# kichigini toping. Xuddi shuningdek, uchta sonning maxsimum va
# minimumini topishda bu klassdan foydalaning.
# Parametrli klasslarga doir misollar
# 4. 6.1 va 6.2 bo’limlardagi misollarni parametrli klasslar
# yordamida yeching.
# 5. 1+2+3+…+n yig’indini va 1·2·3·...·n ko’paytmani
# hisoblashni o’z ichiga ilgan parametrili va bir nechta metodli klass yarating .
# Asosiy programmada bu klass turidagi obyekt hosil qiling. Masalalar
# yeching.
# 6. 1·1+2·2+3·3+...+n·n yig’indini hisoblang.
# 7. 1·n+2·(n ‒1)+3·(n ‒2)+...+n·1 yig’indini hisoblang.
# 8. Fibonachchi sonlari birinchi n tasining yig’indisini
# toping.
# 9. Berilgan K soniga karrali bo’lgan birinchi N ta sonni
# toping.
# 10. Berilgan K soniga qoldiqsiz bo’linadigan birinchi N
# ta sonni toping.
# 11. Ixtiyoriy n (0≤n≤9) raqamni switch operatoridan
# foydalanib, so’zlar bilan ifodalaydigan, ixtiyoriy hafta kuni m (1≤m≤7) ni
# mos haftaning kuni (dushanba, seshanba va h.k.) orqali ifodalaydigan,
# ixtiyoriy oy nomeri k (1≤k≤12) ni oy nomlari orqali ifodalaydigan
# parametri va uchta metodli klass yarating. Asosiy programmada bu klass
# turidagi obyekt hosil qiling. Masalalar yeching.
# Klass konstruktoriga doir misollar
# 12. Yuqoridagi misollarni klass konstruktori
# yordamida yeching.