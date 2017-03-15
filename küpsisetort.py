pikkus = int(input("Mitu küpsist pikkuses? "))
laius = int(input("Mitu küpsist laiuses? "))
kõrgus = int(input("Mitu kihti? "))
küpsiseid_pakis = int(input("Mitu küpsist on pakis? "))

def pakke():
    küpsiste_arv = pikkus*laius*kõrgus
    pakkide_arv = küpsiste_arv/küpsiseid_pakis
    print("Sul on vaja " + str(round(pakkide_arv+0.49)) + " küpsisepakki.")

pakke()