# def large_power(base,exponent):
#     if( base ** exponent > 5000):
#      return True
#     else:
#        return False
    
# print(large_power(4,3))

# ''' Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. '''
# def divsible_by_ten(num):
#     if num % 10 == 0:
#         return True
#     else:
#         return False
''' Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters.'''    
def calculate_discount(price, discount_percent):
        if discount_percent >= 20:
                discount = price * (discount_percent / 100)
                final_price = price - discount
                return final_price
        else:    
         final_price = price  # if no dis count is applied, return the original price
        return final_price
print(calculate_discount(100,20))

''' Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.'''

price = float(input("Enter Original price:"))
discount_percent = float(input("Enter Discount percent:"))
final_price = calculate_discount(price, discount_percent)
if final_price == price:
      print(f"No discount applied. The final price is: {final_price}")
else:
      print(f"The final price after applying the discount is: {final_price}")
