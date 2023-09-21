#1 feladat kerjunk be a felhasznalotol 2 darab egesz szamot es vizsgaljuk meg ezt a kovetkezorol melyk a nagyobb ertek illetve ha egyenlo
#2 feladat bekrunk a felhasznalotol 5 egesz szamot mindegyuikrol megvizsgaljujk hogy pozitiv vagy negativ illetve azt hogy 20 nal nagyobb mint 20
#bonusz feladat szamold meg hany van amely az 5 kozul ami pozitiv es meg nagyobb is




'''

#1 feladat
szam1 = int(input("szam1: "))
szam2 = int(input("szam2: "))

if szam1 > szam2:
    print(szam1, "(szam1) nagyobb mint (szam2)", szam2)
elif szam1 == szam2:
    print("a ket szam egyenlo",szam1, "=","szam2")
elif szam2 > szam1:
    print(szam2, "(szam2) nagyobb mint (szam1)", szam1)
    
'''

#feladat2

szam1 = int(input("szam1: "))
szam2 = int(input("szam2: "))
szam3 = int(input("szam3: "))
szam4 = int(input("szam4: "))
szam5 = int(input("szam5: "))

num = 0

if szam1 > 0 and szam1 < 20:
    print("szam1 nagyobb mint 0 es kevesebb a 20 nal")

elif szam1 > 0 and szam1 > 20:
    print("szam1 nagyobb mint 0 es tobb a 20 nal")
    num = num + 1
elif szam1 < 0:
    print("szam1 negativ")
    
if szam2 > 0 and szam2 < 20:
    print("szam2 nagyobb mint 0 es kevesebb a 20 nal")

elif szam2 > 0 and szam2 > 20:
    print("szam2 nagyobb mint 0 es tobb a 20 nal")
    num = num + 1
elif szam2 < 0:
    print("szam2 negativ")

if szam3 > 0 and szam3 < 20:
    print("szam3 nagyobb mint 0 es kevesebb a 20 nal")

elif szam3 > 0 and szam3 > 20:
    print("szam3 nagyobb mint 0 es tobb a 20 nal")
    num = num + 1
elif szam3 < 0:
    print("szam3 negativ")

if szam4 > 0 and szam4 < 20:
    print("szam4 nagyobb mint 0 es kevesebb a 20 nal")

elif szam4 > 0 and szam4 > 20:
    print("szam4 nagyobb mint 0 es tobb a 20 nal")
    num = num + 1
elif szam4 < 0:
    print("szam4 negativ")

if szam5 > 0 and szam5 < 20:
    print("szam5 nagyobb mint 0 es kevesebb a 20 nal")
  
elif szam5 > 0 and szam5 > 20:
    print("szam5 nagyobb mint 0 es tobb a 20 nal")
    num = num + 1
elif szam5 < 0:
    print("szam5 negativ")
print(num, " nagyobb mint 20")




















