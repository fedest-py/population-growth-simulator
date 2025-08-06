# population-growth-simulator

This Python program models the exponential growth of a population over three time periods using the formula: 
P = P₀ * e^(rt)

Where:
- P is the final population
- P₀ is the initial population
- e is the Euler's number
- r is the annual growth rate
- t is time (years)


The program:
1. Prompts the user to enter the initial population.
2. Repeats the growth process three times, asking for:
   - A time-period (in years)
   - A relative growth rate (as a percentage)
3. Updates the population each time using the exponential growth formula.
4. Prints the final population value.

## Example:
Enter initial populational value: 300
Enter time period for MODEL 1: 4
Enter relative growth rate for MODEL 1: 1.2
Enter time period for MODEL 2: 2.5
Enter relative growth rate for MODEL 2: 5
Enter time period for MODEL 3: 1
Enter relative growth rate for MODEL 3: 2.1

Calculating....
Please Stand By
The final population is: 364.2288848868699

## Concepts Demonstrated:
- Mathematical modeling
- User input handling
- Using the `math` module
- Floating point calculations
