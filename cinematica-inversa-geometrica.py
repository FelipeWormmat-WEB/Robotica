import math

def calculate_theta1(x, y, l1, l2): 
    print('\n##### Θ1 #####')

    term1 = math.atan2(y, x)
    print('arctan2(y,x) = ',term1)
    
    term2_numerator = x**2 + y**2 + l1**2 - l2**2
    term2_denominator = 2 * l1 * math.sqrt(x**2 + y**2)
    term2 = math.acos(term2_numerator / term2_denominator)
    print('arccos(',term2_numerator,'/',term2_denominator,') = ',term2)

    theta1 = term1 + term2
    print('Θ1 = arctan2(',y,',',x,')',' + arccos(',term2_numerator,'/',term2_denominator,') = ',math.degrees(theta1))
    return theta1

def calculate_theta1_linha(x, y, l1, l2):
    print('\n##### Θ1\' #####')

    term1 = math.atan2(y, x)
    print('arctan2(y,x) = ',term1)

    term2_numerator = x**2 + y**2 + l1**2 - l2**2
    term2_denominator = 2 * l1 * math.sqrt(x**2 + y**2)
    term2 = math.acos(term2_numerator / term2_denominator)
    print('arccos(',term2_numerator,'/',term2_denominator,') = ',term2)

    theta1 = term1 - term2
    print('Θ1\' = arctan2(',y,',',x,')',' - arccos(',term2_numerator,'/',term2_denominator,') = ',math.degrees(theta1))
    return theta1

def calculate_theta2(x, y, l1, l2):
    print('\n##### Θ2 #####')

    term1_numerator = x**2 + y**2 - l1**2 - l2**2
    term2_denominator = 2*l1*l2
    theta2 = -math.acos(term1_numerator / term2_denominator)

    print('Θ2 = - arccos(',term1_numerator,'/',term2_denominator,') = ',math.degrees(theta2))
    return theta2
    
def calculate_theta2_linha(x, y, l1, l2):
    print('\n##### Θ2\' #####')

    term1_numerator = x**2 + y**2 - l1**2 - l2**2
    term2_denominator = 2*l1*l2
    theta2 = math.acos(term1_numerator / term2_denominator)

    print('Θ2\' = arccos(',term1_numerator,'/',term2_denominator,') = ',math.degrees(theta2))
    return theta2

def calculate_theta3(phi, theta1, theta2):
    print('\n##### Θ3 #####')
    theta3 = math.degrees(phi) - (math.degrees(theta1) + math.degrees(theta2))

    print('Θ3 =',math.degrees(phi),'- (',math.degrees(theta1),'+',math.degrees(theta2),') = ',theta3)
    return theta3

def calculate_theta3_linha(phi, theta1_linha, theta2_linha):
    print('\n##### Θ3\' #####')
    theta3=math.degrees(phi) - (math.degrees(theta1_linha) + math.degrees(theta2_linha))

    print('Θ3\' =',math.degrees(phi),'- (',math.degrees(theta1_linha),'+',math.degrees(theta2_linha),') = ',theta3)
    return theta3

# Exercicio 1
# L1 = 400
# L2 = 250
# L3 = 120
# Phi = math.radians(16.9)
# x3= 462.25
# y3= 93.96

# Exercicio 2 - COM GARRA
# L1 = 400
# L2 = 250
# L3 = 120
# Phi = math.radians(162.41)
# xGARRA= -508.29
# yGARRA= 514.11

L1 = float(input('L1 = '))
L2 = float(input('L2 = '))
L3 = float(input('L3 = '))
Phi = math.radians(float(input('Phi = ')))

GARRA = input('A questão é com garra? (s/n) ')

if GARRA == 's' or GARRA == 'S' or GARRA == 'sim' or GARRA == 'SIM':
    print('\nQuestão com GARRA')
    xGARRA= float(input('Informe o xGARRA: '))
    yGARRA= float(input('Informe o yGARRA: '))
    x3 = xGARRA - L3*math.cos(Phi)
    y3 = yGARRA - L3*math.sin(Phi)
else:
    x3= float(input('Informe o x3: '))
    y3= float(input('Informe o y3: '))

print('\nDesenvolvimento')

theta1 = calculate_theta1(x3,y3,L1,L2)
theta1_linha = calculate_theta1_linha(x3,y3,L1,L2)

theta2 = calculate_theta2(x3,y3,L1,L2)
theta2_linha = calculate_theta2_linha(x3,y3,L1,L2)

theta3 = calculate_theta3(Phi,theta1,theta2)
theta3_linha = calculate_theta3_linha(Phi,theta1_linha,theta2_linha)

print('\nResultado Final')

print('Θ1  =',round(math.degrees(theta1),2))
print('Θ1\' =',round(math.degrees(theta1_linha),2))

print('Θ2  =',round(math.degrees(theta2),2))
print('Θ2\' =',round(math.degrees(theta2_linha),2))

print('Θ3  =',round(theta3,2))
print('Θ3\' =',round(theta3_linha,2))

input()