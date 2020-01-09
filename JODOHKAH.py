# A = True
# B = False
# if not A :
#    print ("A")
# else :
#    print ("B")
import random

print("--------- JODOHKAH?? ---------")
print("")
loop = True
while loop:
    cowok = input("Masukkan Nama Cowok = ")
    cewek = input("Masukkan Nama Cewek = ")

    print("")
    print("-------- umumumumu --------")
    print("")

    print("Nama Cowok = ", cowok)
    print("Nama cewek = ", cewek)

    confirm = input("Apakah nama yang dimasukkan sudah benar? y/n = ")
    if confirm == 'y':
        loop = False

match = random.randrange(0, 100)
print('Presentase ambi Pacar ', match, '%')
if match > 80:
    print("Rabi skuy")
elif match > 60:
    print("Pikir pikir dulu yakk")
elif match > 40:
    print("Yakin kowee??")
elif match > 20:
    print("skip")
elif match > 0:
    print("Selingkuh enak")
print("")

selingkuh = input("Punya Selingkuhan? y/n = ")
if selingkuh == 'y':
    selingkuhan = input("Masukkan Nama Selingkuhan = ")
    match2 = random.randrange(0, 100)
    print('Presentase ambi Selingkuhan ', match2, '%')
else:
    print("Oke sip mantap")
    loop = False
if match2 > match:
    print("Putus sama pacar, Lanjooot sama Selingkuhan")
else:
    print("Ojok Selingkuh gengsss, rapantes")

