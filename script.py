##Accepted units of measurement

#imports
import math

#-------------------------------------
# Basic Electrical Functions
#-------------------------------------

#Ohm's Law calculator class function
class ohmsLaw:

    def voltage(current, resistance):
        volts = float(current) * float(resistance)
        return volts

    def current(voltage, resistance):
        amps = float(voltage) / float(resistance)
        return amps

    def resistance(voltage, current):
        ohms = float(voltage) / float(current)
        return ohms


#Power calculator functions class
class power:

    def watts(current, voltage):
        pwr = float(current) * float(voltage)
        return pwr

    def amps(power, voltage):
        current = float(power) / float(voltage)
        return current

    def volts(power, current):
        voltage = float(power) / float(current)
        return voltage

#-------------------------------------
# Electrical/Electronic Component Functions
#-------------------------------------

#Inductance calculator functions class
class inductance:

    def none():
        return 0

#Capacitance calculator functions class
class capacitance:

    #parallel plate capacitor calculator function
    def para(dielectricConst, plateArea, distance):
    
        Er = float(dielectricConst)                 #dieletric constant
        A = float(plateArea)                        #surface area of plate in square metres 
        d = float(distance)                         #distance between plates in metres
        Eo = float(8.854e-12)                       #permittivity of free space

        C = (Eo * Er * A) / d                       #parallel plate capacitance equation
        return C                                    #return result in Farads

    #dielectric constant of water depending on temperature formula
    #   graphical equation of line of best fit taken to order of 2 for high accuracy
    #   data source: https://en.wikipedia.org/wiki/Water_(data_page)
    #   stored on onedrive : Scripts\WaterData.xlsx
    def dielectricConstant(temperature):            # y = 0.0007x2 - 0.3959x +88
                                                    #   where x = temperature & y = dielectric constant
        x = float(temperature)
        Ya = 0.0007 * math.pow(x, 2)
        Yb = 0.3959 * x
        y = Ya - Yb + 88
        return y

    #voltage potential of capaitor for given capacitance at given energy

    def voltage(capacitance, energy):                   #W = 1/2 C V2
        en = float(energy)
        cap = float(capacitance)
        v = math.sqrt(en / (0.5 * cap))     #V = sq root of V/0.5C
        return v


#capacitor reactance calculator function
def capReactance(freq, C):
    
    XC = 1/(2 * math.pi * freq * C)             #capacitor reactance equation
    return XC                                   #return result in Ohms


#inductor reactance calculator function
def  indReactance(freq, L):

    XL = 2 * math.pi * freq * L                 #inductor reactance equation
    return XL                                   #return result in Ohms
        

#resonant frequency calculator function
def Fr(L, C):
    
    L = float(L)                                #format inductance value as float
    C = float(C)                                #format capacitance value as float
    fr = 1/(2 * math.pi * math.sqrt(L*C))       #resonant frequency equation
    return fr                                   #return result

#-------------------------------------
# Chemistry Functions
#-------------------------------------

# enthalpy change functions class

class enthalpyChange:               # 2(H-O-H) -> 2H2 + O2

    def cycA():                     # breaking 2(H...O-H)
        cycle = 2 * 498700          # H-OH = +498.7kJ / mol
        return cycle
    
    def cycB():                     # forming H2
        cycle = 1 * 436400          # H-H = -436.4kJ / mol
        return cycle

    def cycC():                     # breaking 2(O...H)
        cycle = 2 * 428000          # O-H = +428kJ / mol
        return cycle

    def cycD():                     # forming H2 & O2
        H = 1 * 436400              # H-H = -436.4kJ / mol
        O = 1 * 498700              # O=O = -498.7kJ / mol
        cycle = H + O
        return cycle

    def average():
        return 464000               #average = 464kJ / mol

    def sum():
        endo = (float(enthalpyChange.cycA()) - float(enthalpyChange.cycB()) +
                float(enthalpyChange.cycC()) - float(enthalpyChange.cycD()))
        return endo

#mole quantities functions class
class mole:

    def mass(element):             # function returns molar mass in grams

        # elements
        if str(element) == "H":
            g = 1.0079
            return g
        
        elif str(element) == "O":
            g = 15.9994
            return g

        # molecules
        elif str(element) == "H2O":
            g = (2 * mole.mass("H")) + mole.mass("O")
            return g

        elif str(element) == "H2":
            g = 2 * mole.mass("H")
            return g

        elif str(element) == "O2":
            g = 2 * mole.mass("O")
            return g
        
        elif str(element) == "OH":
            g = mole.mass("H") + mole.mass("O")
            return g
        
        # mole.mass endif
        else:
            return 0

        
    # find number of moles for mass of given element/molecule
    def qty(mass, element):

        molMass = (mole.mass(element) / 1000)
        moles = mass / molMass
        return moles

#   
class water:

    def volume(weight, density):    #weight in grams, return volume in millilitres
       vol = weight / density
       return vol

    def weight(volume, density):
        mass = (volume * density)
        return mass

    #density of water depending on temperature formula
    #   graphical equation of line of best fit taken to order of 3 for accuracy of +/-2.5oC
    #   data source: https://www.simetric.co.uk/si_water.htm
    #   stored on onedrive : Scripts\WaterData.xlsx
    def density(temperature):       # y = 5E-08x3 - 8E-06x2 + 6E-05x + 0.9998
                                    #   where x = temp & y = density (g/cm3)
        x = float(temperature)
        Ya = math.expm1(5e-8) * math.pow(x, 3)
        Yb = math.expm1(8e-6) * math.pow(x, 2)
        Yc = math.expm1(6e-5) * x
        y = Ya - Yb + Yc + 0.9998
        y = y * 1000                # convert to kg/m3
        return y
        
        
    
       

#---------
# Main Program 
#---------

#MAIN
def main():
    
    plateL = 0.07           #m
    plateW = 0.07           #m
    gap = 0.001             #m
    temperature = 20        #oC
    print("Temperature =", temperature, "oC")
    
    volume = plateL * plateW * gap          #m3
    density = water.density(temperature)    #kg/m3
    weight = water.weight(volume, density)  #kg
    print("Volume =", volume, "m3")
    print("Density =", density, "kg/m3")
    print("Weight =", weight, "kg")

    moleQty = mole.qty(weight, "H2O")        #mol
    print("Mole Quantity =", moleQty, "moles")

    energy = enthalpyChange.sum() * moleQty     #Joules

    if energy > 0:
        print("Energy required =", energy, "Joules")

    elif energy < 0:
        print("Energy released =", energy, "Joules")

    else:
        print(energy)

    dielectric = capacitance.dielectricConstant(temperature)
    print("Dielectric Constant =", dielectric)

    plateArea = plateL * plateW
    capVal = capacitance.para(dielectric, plateArea, gap)
    print("Capacitance =", capVal, "F")

    reqV = capacitance.voltage(capVal, energy)
    print("Required Voltage =", reqV, "V")

        

#RUN
main()
