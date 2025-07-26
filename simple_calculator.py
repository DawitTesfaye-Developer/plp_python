# Simple python calculator 


number1 = float(input('Enter first number:'));
number2 = float(input('Enter second number: '));

print('choose an operation')
print('1.Addition')
print('2.substraction')
print('3.multiplication')
print('4.Division')

select = input('select the choice the :    ' )


if select == '1':
    print('Result: ', number1 + number2)
    
elif select == '2':
    print('Result:', number1 - number2)
elif select == '3':
    print('Result:', number1 * number2)
elif select == '4':
    print('Result:', number1 / number2) if number2!=0  else 'undefined (division by zero)'
else:
    print('wrong way')     



# if('product = {number1 * number2}'): print(product)
# elif('addition = {number1 + number2}'): print(addition)
# elif('Substraction = {number1 - number2}'): print(Substraction)
# elif('division = {number1 / number2}') : print(division) 
# else: print('!! please select correctly')



