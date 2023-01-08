import rechner
from math import *
from variablen import *




if __name__ == "__main__":
    
    print(f"Dein BMI: {rechner.bmi(gewicht, groesse)}")
    rechner.kcal_bedarf(geschlecht, gewicht, groesse, alter)
    print(rechner.angenommene_kcal(fett, kohlenhydraten, eiweis)) 