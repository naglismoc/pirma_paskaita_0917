import random

print("hi")
print("sveiki studentai")
print("uzsakymai", "agrokultura", 'peugeot 807')

print("vienas " + " tekstas")

vardas = 'Petras'

print(vardas)

amzius = 24

is_man = True
should_eat_after_lesson = False
has_cat = False

print(str(7 + 10) + "labas")
print(7 * 'labas ;) ')


sugalvotas_skaicius = 17
print(sugalvotas_skaicius * sugalvotas_skaicius)
# case
#     when rnd_num = 1 then "vienas"
#     when rnd_num = 2 then "du"
#     ...
# end as col1
rnd_num = random.randint(1,6)
print(rnd_num)
# if rnd_num == 1:
#     print("vienas")
#     print("skaicius")

#
# if rnd_num == 1:
#     print("vienas")
# else:
#     print("kazkas kitas nei vienas")


if rnd_num == 1:
    print("vienas")

if rnd_num == 2:
    print("du")

if rnd_num == 3:
    print('trys')

if rnd_num == 4:
    print('keturi')

if rnd_num == 5:
    print('penki')

if rnd_num == 6:
    print('sesi')


#
# if rnd_num == 1:
#     print("vienas")
# elif rnd_num == 2:
#     print("du")
# elif rnd_num == 3:
#     print('trys')
# elif rnd_num == 4:
#     print('keturi')
# elif rnd_num == 5:
#     print('penki')
# elif rnd_num == 6:
#     print('sesi')


word = "nebeprisikiškiakopūsteliaujantiesiems"
print(word)
print(len(word))

if len(word) > 30 and len(word) < 40:
    print(word + " ilgis yra tarp 30 ir 40 simboliu")

if 30 < len(word) < 40:
    print(word + " ilgis yra tarp 30 ir 40 simboliu")


rnd_num = random.randint(1,6)
print(rnd_num)

print(13 / 5) # dalina paprastai, grazina skaiciu su kableliu
print(13 // 5)# viskas kas po kablelio nukandama ir ismetama. grazina tik sviekaja dali
print(13 % 5) #13 - 5 = 8; 8 - 5 = 3;

print(11 % 2)
print(11 % 2 == 0)
print("----------------")
print(rnd_num)

if rnd_num % 2 == 0 or rnd_num % 3 == 0:
    print(rnd_num,  " yra dvieju arba triju kartotinis")


count = 0
print(count)
count = count + 1
print(count)
count = count + 1
print(count)
count += 1
print(count)

name = 'Naglis'
surname = 'Mockevičius'
age = 35
curr_year = 2025

print("----------- uzd 1 -------------")
print("----------- uzd 2 -------------")
print("----------- uzd 3 -------------")
