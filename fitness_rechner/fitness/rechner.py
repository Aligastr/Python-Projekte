from gewicht import *
from math import *
import variablen
#import gewicht

#Gewicht in kg, groesse in m

def bmi(gewicht, groesse):
    BMI = round((gewicht / groesse ** 2), 2)
    return BMI

#Gewicht in kg, abnahme in kg
#Fett reduzieren
def abnehmen(gewicht, abnahme):
    return gewicht - abnahme

#Gewicht in kg, zunahme in kg
#
def zunehmen(gewicht, zunahme):
    return gewicht + zunahme

# Kcal Bedarf fuer Koerper

def kcal_bedarf(geschlecht, gewicht, groesse, alter):
    if geschlecht == "Man":
        groesse = groesse * 100
        kcal_man = 66.4 + (13.7 * gewicht) + (5 * groesse) - (6.8 * alter)
        print(f"Dein taegliches Bedarf in kcal ist : {kcal_man}")
    elif geschlecht == "Frau":
        groesse = groesse * 100
        kcal_frau = 655.1 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
        print(f"Dein taegliches Bedarf in kcal ist : {kcal_frau}")
    else:
        print("Unbekante Geschlecht")

def angenommene_kcal(fett, kohlenhydraten, eiweis):
    kcal = fett * 9 + kohlenhydraten * 4 + eiweis * 4
    
    return kcal