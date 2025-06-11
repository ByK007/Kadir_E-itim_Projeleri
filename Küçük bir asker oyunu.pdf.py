from random import randint

class Asker:
    def __init__(self):
        self.can=randint(30,70)
        self.hasar=randint(30,90)
        self.canli_mi=True

    def ol(self):
        self.canli_mi =False

    def hasar_al(self,alinan_hasar:int):
        if alinan_hasar >= self.can:
            self.ol()

        else:
            self.can -=alinan_hasar


class Oyuncu:
    def __init__(self):
        self.can=randint(300,600)
        self.hasar=randint(30,90)
        self.canli_mi = True

    def ol(self):
        self.canli_mi=False
        print("Oyun Bitti.Kaybettiniz :(" )
        quit()
        

    def hasar_al(self,alinan_hasar:int):
        if alinan_hasar >= self.can:
            self.ol()

        else:
            self.can -=alinan_hasar


askerler= [ Asker() for i in range(10) ]
oyuncu=Oyuncu()

for i in range(10):
    askerler.append(Asker())


oyuncu=Oyuncu()


while True:
    print("Oyuncu Bilgileri".center(30,"-"))
    print("Oyuncu Sağlık: {}    --- Oyuncu Hasar: {}".format(oyuncu.can,oyuncu.hasar))
    print("Askerler".center(15,"-"),end="\n")

    for i in askerler:
        print(i) 
    for numara,asker in enumerate(askerler):
        if asker.canli_mi:

            print("{}. Asker --- Can Değeri: {} --- Hasar Değeri: {}".format(numara, asker.can ,asker.hasar))

            secilen_asker=int(input("Saldırı için seçilen asker: "))

            if secilen_asker > len(askerler) -1 or secilen_asker < 0:
                print("Girilen asker numarası yanlış!")
                continue


            else:
                askerler[secilen_asker].hasar_al(oyuncu.hasar)

                if askerler[secilen_asker].canli_mi == False:
                    askerler.remove(askerler[secilen_asker])

                if askerler:
                    saldiran_asker= randint(0,len(askerler)-1)
                    oyuncu.hasar_al(askerler[saldiran_asker].hasar)

                else:
                    print("Tebrikler! Tüm düşmalar öldü,kazandın!")
                    quit()

    






























