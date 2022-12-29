"""
Assignment No.: 1
Course: PROG12974
Submission date:sep 29 2022
Developed by: Orlando Companioni
Date created: sep 26 2022

The program takes input from the user then outputs the amount of money in
the bank after a certain number of years with compound interest

It also outputs all the inputs given by the user with their
appropriate label names
"""

#get the input from the user
principalAmount=float(input("Please enter the original amount \
deposited: "))
        
anualInterest=float(input("Please enter the annual interest rate: "))

num_compounded=int(input("Please enter the number of times  \
per year that the interest is compounded(12 or 4): "))

years=int(input("Please enter The number of years the \
account will be left to earn interest: "))

#process the input into the final amount

interestDecimal=anualInterest/100 #this is done to make it a decimal

totalAmount=principalAmount*(1+interestDecimal/num_compounded)**\
             (num_compounded*years)

#output all the information and its proper label
print(f"Total amount of money: {totalAmount:.7f}")
print(f"Principal amount: {principalAmount:.0f}")
print(f"Interest rate: {interestDecimal:.0%}")
print(f"Interest frequency: {num_compounded}")
print(f"Number of years: {years}")
print(f"Compound interest calculator by: Orlando companioni\
 99143587789")