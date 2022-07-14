from googletrans import Translator

t=Translator()
a=t.translate("Anh yêu Ngọc Anh" , src="vi", dest="en")
b=a.text
print(b)
#print(a)