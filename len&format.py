isim = input('Lutfen adinizi girin : ')
yas = input('Yasinizi giriniz : ')
list = [isim, yas]
list
print("Listenin uzunlugu : {}".format(len(list)))
print("Ismin uzunlugu : {}".format(len(list[0])))
print("Yasin uzunlugu : {}".format(len(list[1])))

toplam = len(list[0]) + len(list[1])
print("Listedeki birinci ve ikinci elemanin uzunluklari toplami : {}".format(toplam))
