lower_abc_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
upper_abc_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
lower_abc_en = 'abcdefghijklmnopqrstuvwxyz'
upper_abc_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crpt(decr, k, lower_abc, upper_abc):
    res = ''
    for c in decr:
        if c in lower_abc:
            l = lower_abc.index(c)
            n = (l+k)%len(lower_abc)
            res += lower_abc[n]
        elif c in upper_abc:
            u = upper_abc.index(c)
            n = (u+k)%len(upper_abc)
            res += upper_abc[n]
        else:
            res += c
    return res

s = "Блажен, кто верует, тепло ему на свете!" 
print(s, '=>', crpt(s, 10, lower_abc_ru, upper_abc_ru ))

s = "To be, or not to be, that is the question!"
print(s, '=>', crpt(s, 17, lower_abc_en, upper_abc_en ))

s = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг." 
print(s, '=>', crpt(s, -7, lower_abc_ru, upper_abc_ru ))

s = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
print(s, '=>', crpt(s, -25, lower_abc_en, upper_abc_en ))

s = "Hawnj pk swhg xabkna ukq nqj."
for n in range(26):
    print(s, '=>', crpt(s, (-1)*n, lower_abc_en, upper_abc_en ))
