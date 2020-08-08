"""Расшифровываем строку где каждый символ смещен на 2 буквы по алфавиту"""
import string
from time import thread_time

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl" \
       "zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq()" \
       "gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
# Мой вариант
start = thread_time()
abc = "abcdefghijklmnopqrstuvwxyzab   ((()))'''..."

for i in text:
    print(abc[abc.find(i[0]) + 2], end="")

print(thread_time()-start)



# Правильный вариант через str.maketrans
#print()
#in_abc = "abcdefghijklmnopqrstuvwxyz"
#out_abc = in_abc[2:] + "ab"
#trantab = text.maketrans(in_abc, out_abc)
#print(text.translate(trantab))
text='map'
# код Zart
start = thread_time()
al = string.ascii_lowercase
table = str.maketrans(al, al[2:]+al[:2])
print(text.translate(table), end="")
print(thread_time()-start)