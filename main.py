print("\n POKEMON DAMAGE CALCULATOR")

import random
damage = 0
level = 90
A = 205
D = 188
power = 110
target = 1
weather = 1
badge = 1
critical = 1
random1 = round(random.uniform(0.85,1.00),2)
stab = 1.5
type_e = 0.5
burn = 1
other = 1
modifier = target * weather * badge * critical * random1 * stab * type_e * other 
damage = ((((((2*level)/5)+2)*power*(A/D))/50)+2) * modifier

print("Damage Dealt by Charizard is :",round(damage, 2))