from Voiture import Voiture
from Decapotable import Decapotable
from Ralley import Ralley
from RalleyDecapot import RalleyDecapot

# test Voiture class
print("-------  test Voiture class  -------")
v = Voiture()
print("before changing anything:")
v.affichage()
print("after changing vitesse:")
v.setVitesse(260)
v.affichage()
print("after changing lumiere:")
v.setLumOff()
v.affichage()
print("it's too darck, we should switch it on again:")
v.setLumOn()
v.affichage()

# test Decapotable class
print("-------  test Decapotable class  --------")

d = Decapotable()
print("before changing anything:")
d.affichage()
print("after changing vitesse:")
d.setVitesse(260)
d.affichage()
print("after changing lumiere:")
d.setLumOff()
d.affichage()
print("it's too darck, we should switch it on again:")
d.setLumOn()
d.affichage()
print("after changing eToit:")
d.setToitBas()
d.affichage()
print("it's too cold, switch it again: ")
d.setToitHaut()
d.affichage()

# test Ralley class
print("--------  test Ralley class  ----------")

r = Ralley()
print("vitesse > 200 as argument to setVitesse method:")
r.setVitesse(300)
r.affichage()

# test RalleyDeacapot class
print("-------  test RalleyDecapot class  -------")

rd = RalleyDecapot()
print("test vitesse with value <= 200:")
rd.setVitesse(190)
rd.affichage()
print("test vitesse with value > 200:")
rd.setVitesse(206)
rd.affichage()
print("test lumiere on:")
rd.setLumOn()
rd.affichage()
print("test lumiere off:")
rd.setLumOff()
rd.affichage()
print("test toit bas:")
rd.setToitBas()
rd.affichage()
print("test toit haut:")
rd.setToitHaut()
rd.affichage()

