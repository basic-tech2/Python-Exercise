try:   
    UserWeight = float(input('Weight: '))
except:
    print('Please enter a number')
    quit()
    
get_unit = input('(K)g or (L)bs: ')
weight_in_kg = UserWeight // 0.45
weight_in_lb = UserWeight * 0.45

if get_unit.upper() == 'K':
    print("Weight in Lbs: " + str(weight_in_lb))

elif get_unit.upper() == 'L':
    print("Weight in Kgs: " + str(weight_in_kg))

else:
    print('Please enter your  unit! ')
