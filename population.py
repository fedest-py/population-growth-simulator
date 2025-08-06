#******************************************************************************
# population.py
# Eduardo E
#

#ask user for the value initial population value

population_0 = int(input('Enter initial populational value: '))

#ask for years and growth rate for Model 1

print('Thank you, lets procede with Model 1')

num_years = float(input('Enter time period for MODEL 1: '))

print ('''Note: Enter the values for growth rate as percentage, but do not use '%' ''')

growth_rate = float(input('Enter relative growth rate for MODEL 1: '))

#Before anything, lets bring the math over

import math 

#now we update the initial population variable

population_0 = population_0 * (math.exp((growth_rate/100) * num_years))

#ask for years and growth rate for Model 2

print('Great, now for Model 2')

num_years = float(input('Enter time period for MODEL 2: '))

growth_rate = float(input('Enter relative growth rate for MODEL 2: '))

#update initial population

population_0 = population_0 * (math.exp((growth_rate/100) * num_years))

# ask for years and growth rate for Model 3

print('Finally, Model 3')

num_years = float(input('Enter time period for MODEL 3: '))

growth_rate = float(input('Enter relative growth rate for MODEL 3: '))

#update variable for final value

population_0 = population_0 * (math.exp((growth_rate/100) * num_years))

print('''Calculating....
Please Stand By''')


print('The final population is: ', population_0)













