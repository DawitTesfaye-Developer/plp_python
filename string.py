#python string
# str1  = "hello dave \'what's new \'"
# print(str1)
# str1= 'hello nardiye'
# print(str1)

# print(str1[-2])
# print(str1[1:5]) 
#str1[0]='h'   # this will raise an error 

# str1 = str1.replace('nardiye', 'dave')
# str1 = """hello wellcome all of the my team from different countries you have great love for me i know 
#     that all of my ideas is with you"""
# name = 'nardiye'
# great = 'love you'
# str1 = great + ' ' + name
# str1 = 'premium calls'
# for i in str1:
#     print(i)
# print(len(str1))
# print('p' in 'premium')
# print('uu' not in 'premium')
# name= 'nardos'
# country = 'ethiopia'
# print(f'{name} is from {country}')
# print(str1.index('a'))
# print(str1)

### Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

# num1=input('Enter the numbers you want to comupute: ')
# int_list = [int(num) for num in num1.split()]
# total = sum(int_list)
# print(total)

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
    
# array = ('fareware', 'alem', 'gloy ','timing','aims')
# for book in array:
#        print(book)

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

# person_info={}

# person_info['name'] = input('Enter Your name:')
# person_info['age']  = input('Enter Your age:')
# person_info['country']  = input('Enter Your country:')
# person_info['city']  = input('Enter Your city:')

# print('\n personal information')
# print(person_info)

# print(sum)

#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
# input1 = input('Enter first numbers separated by spaces: ')
# set1 = set(map(int,input1.split()))
# creating a set from user input
# input2 = input('Enter second set of numbers separated by space: ')
# set2 = set(map(int, input2.split()))
# common_set= set1.union(set2)
# print('common elements: ', common_set )


#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = input('Enter the words separated by space:').split()
odd_length_words = [word for word in words if len(word) % 2 != 0]
print('words with odd length:', odd_length_words)