#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Bank:
    def __init__(self,Name,ID,Location):
        self.Name = Name
        self.ID = ID
        self.Location = Location
class Customer:
    def __init__(self):
        Number_of_Applications = int(input("Number of Applications accepted for today: "))
        Application = {}
        for x in range(Number_of_Applications):
            Application[x] = (str(input("Customer Name: ")),input("Customer's Email Address: "),input("Customer's Date Of Birth: "))

class Loan_Inquiery:
    def L_I(self):
        Country = input('Entry your Country name: ')
        NIC = input("Enter Your NIC: ")
        Loan_Type = input("Loan Type")
        Payment_Rang = float(input("Enter Your Loan Rang: "))
        if Country == 'Pakistan':
            print("Your Application For Loan is Accepted.. ")
            if Loan_Type == "Monyhly":
                    if Payment_Rang >50000:
                        return "Your loan duration is 1 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)
                    elif Payment_Rang >100000:
                        return "Your loan duration is 2 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)
                    else:
                        return "Your loan duration is 3 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)
        
            
            if Loan_Type == "Yearly":
                if Payment_Rang >50000:
                    return "Your loan duration is 1 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)
                elif Payment_Rang >100000:
                    return "Your loan duration is 2 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)
                else:
                    return "Your loan duration is 3 Year for {} Payment under range {}: ".format(Loan_Type,Payment_Rang)

        else:
            return "Sorry Application has not Accepted for {}".format(Country)

class Car:
    cars = {'Suzuki Cultus':2019,'Suzuki Bolan':2018, "Honda City":2017}
    for i in cars:
        inp = input('plz name: ')
        if inp in cars:
            print("OKI")
    
    
c = Bank("HBL",12345,'DHA')
a = Customer()
b = Loan_Inquiery()
print(" Your Bank for Appluing Loan is {} ".format(c.Name))
print("Your Bank Location: {} ".format(c.Location))
print(b.L_I())

# car.LoanCar('Honda',2016)
# print("The Car Company is {}".format(car.Company))
# print("The Car's model is {}".format(car.Model))
car = Car


# In[ ]:




