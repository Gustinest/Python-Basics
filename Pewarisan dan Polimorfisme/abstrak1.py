import math
from abc import ABCMeta, abstractmethod

# Kelas Abstak
class DuaDimensi(metaclass=ABCMeta):

    # Metode abstra
    @abstractmethod
    def luas(self):
        pass
    
    @abstractmethod
    def keliling(self):
        pass
    
    # METODE NON ABSTRAK
    def cetakLuasdanKeliling(self, namaObjek):
        print('Luas %s = %f' % (namaObjek, self.luas()))
        print('Keliling %s = %f\n' % (namaObjek,self.keliling()))

# KELAS KONKKRIT, Turunan dari kelas dua dimensi
class PersegiPanjang(DuaDimensi):
    def __init__(self, p, l):
        self.__panjang = p
        self.__lebar = l

    def setPanjang(self, p):
        self.__panjang = p

    def getPanjang(self):
        return self.__panjang
    
    def setLebar(self, l):
        self.__lebar = l
    
    def getLebar(self):
        return self.__lebar
    
    #Implementasi metode luas() milik kelas dua dimensi
    def luas(self):
        return self.__panjang * self.__lebar
     #Implementasi metode keling() milik kelas dua dimensi
    def keliling(self):
        return 2 * (self.__panjang * self.__lebar)

class Lingkaran(DuaDimensi):
    def __init__(self,r):
        self.__radius = r

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius
    
    # Implementasi metode luas() milik kelas dua dimensi
    def luas(self):
        return math.pi * (self.__radius ** 2)
    
    #Implementasi metode keling() milik kelas dua dimensi
    def keliling(self):
        return 2 * math.pi * self.__radius
    
class SegitigaSiku2(DuaDimensi):
    def __init__(self, a, t):
        self.__alas = a
        self.__tinggi = t

    def setAlas(self, a):
        self.__alas = a

    def getAlas(self):
        return self.__alas

    def setTingi(self, t):
        self.__alas = t

    def getTinggi(self):
        return self.__tinggi
    
    def hipotenusa(self):
        return math.sqrt(
            (self.__alas ** 2) + (self.__tinggi ** 2)
        )
    
     # Implementasi metode luas() milik kelas dua dimensi
    def luas(self):
        return self.__alas * self.__tinggi / 2
    
    #Implementasi metode keling() milik kelas dua dimensi
    def keliling(self):
        return self.__alas + self.__tinggi + self.hipotenusa()
    
def main():
    # membuat objek dari kelas persefi panjang
    obj1 = PersegiPanjang(10, 8);
    obj1.cetakLuasdanKeliling('persegi panjang')

    # membuat objek dari kelas lingkaran
    obj2 = Lingkaran(3);
    obj2.cetakLuasdanKeliling('lingkaran')

    # Membuat objek dairi kelas segitogasiku2
    obj3 = SegitigaSiku2(3,4);
    obj3.cetakLuasdanKeliling('segitiga')

if __name__ == '__main__':
    main()
