#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bikes:
    pass
class Models(Bikes):
    def __init__(self,Model_By_Year):
        self.Model_By_Year = Model_By_Year

class M_2018(Models):
    def __init__(self,Manufacturing_Company,Manufacturing_ID,Model_Name,Customer_ID,Customized_logo,Condition,Price,Place_of_Origin,Gross_Weight,Net_Weight,OEM):
        self.Manufacturing_Company = Manufacturing_Company
        self.Manufacturing_ID = Manufacturing_ID
        self.Model_Name = Model_Name
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Customized_logo = Customized_logo
        self.Price = Price 
        self.Condition = Condition
        self.Place_of_Origin = Place_of_Origin
        self.Gross_Weight = Gross_Weight
        self.Net_Weight = Net_Weight
        self.OEM = OEM     
class M_2017(Models):
    def __init__(self,Manufacturing_Company,Manufacturing_ID,Model_Name,Customer_ID,Customized_logo,Condition,Price,Place_of_Origin,Gross_Weight,Net_Weight,OEM):
        self.Manufacturing_Company = Manufacturing_Company
        self.Manufacturing_ID = Manufacturing_ID
        self.Model_Name = Model_Name
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Customized_logo = Customized_logo
        self.Price = Price 
        self.Condition = Condition
        self.Place_of_Origin = Place_of_Origin
        self.Gross_Weight = Gross_Weight
        self.Net_Weight = Net_Weight
        self.OEM = OEM   

class M_2016(Models):
    def __init__(self,Manufacturing_Company,Manufacturing_ID,Model_Name,Customer_ID,Customized_logo,Condition,Price,Place_of_Origin,Gross_Weight,Net_Weight,OEM):
        self.Manufacturing_Company = Manufacturing_Company
        self.Manufacturing_ID = Manufacturing_ID
        self.Model_Name = Model_Name
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Customized_logo = Customized_logo
        self.Price = Price 
        self.Condition = Condition
        self.Place_of_Origin = Place_of_Origin
        self.Gross_Weight = Gross_Weight
        self.Net_Weight = Net_Weight
        self.OEM = OEM   
        
class M_2015(Models):
    def __init__(self,Manufacturing_Company,Manufacturing_ID,Model_Name,Customer_ID,Customized_logo,Condition,Price,Place_of_Origin,Gross_Weight,Net_Weight,OEM):
        self.Manufacturing_Company = Manufacturing_Company
        self.Manufacturing_ID = Manufacturing_ID
        self.Model_Name = Model_Name
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Customized_logo = Customized_logo
        self.Price = Price 
        self.Condition = Condition
        self.Place_of_Origin = Place_of_Origin
        self.Gross_Weight = Gross_Weight
        self.Net_Weight = Net_Weight
        self.OEM = OEM   

class M_2014(Models):
    def __init__(self,Manufacturing_Company,Manufacturing_ID,Model_Name,Customer_ID,Customized_logo,Condition,Price,Place_of_Origin,Gross_Weight,Net_Weight,OEM):
        self.Manufacturing_Company = Manufacturing_Company
        self.Manufacturing_ID = Manufacturing_ID
        self.Model_Name = Model_Name
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Customized_logo = Customized_logo
        self.Price = Price 
        self.Condition = Condition
        self.Place_of_Origin = Place_of_Origin
        self.Gross_Weight = Gross_Weight
        self.Net_Weight = Net_Weight
        self.OEM = OEM           

Model_By_Year = [2015, 2019, 2013]
Manufacturing_Company = "Honda"
Manufacturing_ID = 11003
Model_Name = 2015
Customer_ID = 112233
Price = 2500
Condition = "Used"
Place_of_Origin = "Pakistan"
Gross_Weight = "167.6 lb "
Net_Weight = "76 kg"



print("The Model number of Bike is {}".format(Model_By_Year))
print("The Manufacturing Company is {}".format(Manufacturing_Company))
print("The Manufacturing ID is {}".format(Manufacturing_ID))
print('The Model Name is {}'.format(Model_Name))
print('The Customer ID is {}'.format(Customer_ID))
print('The Price of a Bike is {}'.format(Price))
print('The Condition of a Bike is {}'.format(Condition))
print('The of Place of Origin of a Bike is {}'.format(Place_of_Origin))
print('The Gross Weight of a Bike in lb is {}'.format(Gross_Weight))


# In[ ]:




