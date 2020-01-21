import math
print(f"")
print(f"PROGRAM ZA IZRAČUN AZIMUTA TER DOLŽINE LOKSODROME")
print(f"")
	## VNOS PODATKOV ##
print(f"Spodaj podaj koordinate točk (° ´ ˝): ")
print(f"(S presledkom loči stopinje, minute, sekunde)")
print(f"")
vrstica_laA = None
while vrstica_laA == None:
    vrstica_laA = input("λA: ")
    tocka_laA = vrstica_laA.split()
    if int(tocka_laA[0]) > 360 or int(tocka_laA[1]) > 59 or int(tocka_laA[2]) > 59:
        print("Napaka pri vnosu. Poskusi znova.")
        vrstica_laA = None
    else:
        break

vrstica_fiA = None
while vrstica_fiA == None:
    vrstica_fiA = input("φA: ")
    tocka_fiA = vrstica_fiA.split()
    if int(tocka_fiA[0]) > 360 or int(tocka_fiA[1]) > 59 or int(tocka_fiA[2]) > 59:
        print("Napaka pri vnosu. Poskusi znova.")
        vrstica_fiA = None
    else:
        break

vrstica_laB = None
while vrstica_laB == None:
    vrstica_laB = input("λB: ")
    tocka_laB = vrstica_laB.split()
    if int(tocka_laB[0]) > 360 or int(tocka_laB[1]) > 59 or int(tocka_laB[2]) > 59:
        print("Napaka pri vnosu. Poskusi znova.")
        vrstica_laB = None
    else:
        break

vrstica_fiB = None
while vrstica_fiB == None:
    vrstica_fiB = input("φB: ")
    tocka_fiB = vrstica_fiB.split()
    if int(tocka_fiB[0]) > 360 or int(tocka_fiB[1]) > 59 or int(tocka_fiB[2]) > 59:
        print("Napaka pri vnosu. Poskusi znova.")
        vrstica_fiB = None
    else:
        break

visina = 0
while visina == 0:
    visina = input("Vnesi višino leta:")
    if len(visina) > 0:
        visina = int(visina)
    else:
        print("Prišlo je do napake. Potrebno je vpisati število.")
        visina = 0
print(f"")
				
sAl = int(tocka_laA[0])
minAl = int(tocka_laA[1])
sekAl = float(tocka_laA[2])
sBl = int(tocka_laB[0])
minBl = int(tocka_laB[1])
sekBl = float(tocka_laB[2])
sAf = int(tocka_fiA[0])
minAf = int(tocka_fiA[1])
sekAf = float(tocka_fiA[2])
sBf = int(tocka_fiB[0])
minBf = int(tocka_fiB[1])
sekBf = float(tocka_fiB[2])

	# PRETVORBA IZ S MIN SEK V DECIMALNE SEKUNDE
tAl = sAl + minAl/60 + sekAl/3600
tBl = sBl + minBl/60 + sekBl/3600
tAf = sAf + minAf/60 + sekAf/3600
tBf = sBf + minBf/60 + sekBf/3600
#print (f"{tA}")

	# PRETVORBA V RADIANE
radAl = math.radians(tAl)
radBl = math.radians(tBl) 
radAf = math.radians(tAf) 
radBf = math.radians(tBf) 
#print (f"{radAl}")

R = 6371 #kilometri
p = 45 * math.pi/180

	#	AZIMUT	#

azimut_rad = math.atan(1/((1/(abs(radBl-radAl))) * math.log((math.tan(p+(radAf/2)))/(math.tan(p+(radBf/2))))))
#print (f"{azimut_rad:5.8f}")

if azimut_rad > 0 and azimut_rad < math.pi/2:
	azimut_rad = azimut_rad
elif azimut_rad > math.pi/2 and azimut_rad < 3*math.pi/2:
	azimut_rad = azimut_rad + math.pi
else:
	azimut_rad = azimut_rad	+ 2*math.pi
	
	# DOLŽINA #

#print(type(R))
#print(type(visina))
D = ( R + visina ) * ((radAf - radBf) / (math.cos(azimut_rad)))	
	
azimut_sto = (180*azimut_rad)/math.pi

print(f"Azimut v decimalnih stopinjah:")
print (f"{azimut_sto:.5f}") 
print(f"")
print(f"Dolžina loksodrome [m]:")
print (f"{D:.5f}") 

 













