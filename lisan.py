# -*- coding: cp1254 -*-
import string
print "Lisan Kripto"
print ""
print """Code: Kara Ayaz               e-mail: karaayaz_@outlook.com"""
print ""
print "MuRe Proje Ekibi"
print ""

kaynak= "defghijklmnoprstuvyzabc"
hedef = "abcdefghijklmnoprstuvyz"
while True:
    secim = raw_input("Şifrele (1), Şifre Çöz (2): ")
    if secim == "1":
        sifrenecek = raw_input("Şifrelenecek veriyi giriniz: ")
        cevirbir = string.maketrans(kaynak,hedef)
        soncevirbir = sifrenecek.translate(cevirbir)
        print soncevirbir
    elif secim =="2":
        cozulecek = raw_input("Çözülecek veriyi giriniz: ")
        ceviriki = string.maketrans(hedef,kaynak)
        sonceviriki = cozulecek.translate(ceviriki)
        print sonceviriki
