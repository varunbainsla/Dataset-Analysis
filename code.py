import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  LOADING THE DATA
data='data.xlsx'
d=pd.read_excel(data)




a=d[d['Company_status']== 'Active']

# FUNCTIONS TO PLOT GRAPHS FOR ANALYSIS
#  REMOVE "#" TO EXECUTE THE FUNTION


# Funtion to plot graph on the basis of Company Status
#p=d["Company_status"].value_counts()


# Funtion to plot graph on the basis of Registration Year
#d['year'] = pd.DatetimeIndex(d['DATE_OF_REGISTRATION']).year
#p=d["year"].value_counts()


#Funtion to plot graph on the basis of Company Sector
#p=d["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"].value_counts()


#Funtion to plot graph on the basis of Paidup by Authorized Capital
#d["auth/paid"]=d["PAIDUP_CAPITAL"]/d["AUTHORIZED_CAP"]
#p=d["auth/paid"].value_counts()


#Funtion to plot graph on the basis of Company Region
#d['address'] = d['Registered_Office_Address'].str.split(',').str[-1]
#d['address'] = d['address'].str.split('LH').str[0]
#d['address'] = d['address'].str.lower()
#p=d['address'].value_counts()    
#p.plot(kind='pie',autopct='%1.1f%%')
#plt.show()


#                                  Function to get company with highest Authorized capital
def max_auth():
    max_auth_cap=a[a.AUTHORIZED_CAP == a.AUTHORIZED_CAP.max()]
    print( max_auth_cap[["Company_Name","AUTHORIZED_CAP"]] )



#                                  Function to get company with highest Paidup capital
def max_paid():
    max_paid_cap=a[a.PAIDUP_CAPITAL == a.PAIDUP_CAPITAL.max()]
    print(max_paid_cap[["Company_Name","PAIDUP_CAPITAL"]])
                          




#                                  Function to classify companies on the basis of paidup by authorized percentage
def auth_cap(d):
    d["auth/paid"]=d["PAIDUP_CAPITAL"]/d["AUTHORIZED_CAP"]
    print(d["auth/paid"].value_counts())
    m=d["auth/paid"].max()
    
    date=d[d["auth/paid"] == m]
    print(date[["Company_Name","AUTHORIZED_CAP","PAIDUP_CAPITAL","auth/paid"]])



#                                  Function to classify companies on the basis of Registration year
def reg_date(d):
    #d['DATE_OF_REGISTRATION']=pd.to_datetime(d['DATE_OF_REGISTRATION'])
    #d=d.sort_values(by="DATE_OF_REGISTRATION")
    #print(d[["Company_Name","DATE_OF_REGISTRATION"]])
    d['year'] = pd.DatetimeIndex(d['DATE_OF_REGISTRATION']).year
    print(d["year"].value_counts())
    q=int(input("Enter the year::"))

    

    date=d[d["year"]==q]
    print(date[["Company_Name","DATE_OF_REGISTRATION"]])
  




#                               Function to classify Companies on the basis of Activity sector
def activity(d):
    print(d["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"].value_counts())
    w=input("Enter the sector ::")

    
    sector=d[d["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"] == w]
    print(sector[["Company_Name","PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]])





#                             Function to classify companies on the basis of Class
def classs(d):
    print(d["Company_class"].value_counts())
    w=input("Enter the Company class ::")
    clas = d[d["Company_class"] == w]
    print(clas[["Company_Name","Company_class"]])



#                             Function to classify companies on the basis of Status
def status(d):
    print(d["Company_status"].value_counts())
    w=input("Enter the Company status ::")
    clas = d[d["Company_status"] == w]
    print(clas[["Company_Name","Company_status"]])


#                             Function to classify companies on the basis of paidup/auth_cap percentage
def percentage(d):
    d["percentage"]=(d["PAIDUP_CAPITAL"]/d["AUTHORIZED_CAP"])*100
    print(d["percentage"].value_counts())
    m=d["percentage"].max()
    n=d["percentage"].min()
    print("GIVE INPUT FOR FURTHER ANALYSIS:\n 1.HIGHEST PAIDUP BY AUTHORIZED CAPITAL % \n 2.LOWEST PAIDUP BY AUTHORIZED CAPITAL %")
    i=int(input("Enter your choice::"))
    if i==1:

        print("COMPANY/COMPANIES WITH HIGHEST PAIDUP BY AUTHORIZED CAPITAL PERCENTAGE ::")
        clas = d[d["percentage"] == m]
        print("\n",clas[["Company_Name","percentage"]])
    elif i==2:
        print("COMPANY/COMPANIES WITH LOWEST PAIDUP BY AUTHORIZED CAPITAL PERCENTAGE ::")
        clas = d[d["percentage"] == n]
        print("\n",clas[["Company_Name","percentage"]])
        xx= 23
    print("SELECT CRITERIA FOR FURTHER ANALYSIS: \n 1.REGISTRATION YEAR \n 2.SECTOR \n 3.COMPANY CLASS \n 4.COMPANY STATUS" )
    i=int(input("Enter your choice: "))
    if i==1:
        reg_date(clas);
    elif i==2:
        activity(clas);
    elif i==3:
        classs(clas);
    elif i==4:
        status(clas);
    else :
        print("INVALID INPUT")
        


#                                   Function to classify companies on the basis of Region
def region(d):
    d['address'] = d['Registered_Office_Address'].str.split(',').str[-1]
    d['address'] = d['address'].str.split('LH').str[0]
    d['address'] = d['address'].str.lower()
    

    #d['address'] = d['address'].to_list()

    #z=dict(d.dtypes)
    #print(z)
    
    #d['address'] = d['address'].str.split('unclassified').str[0]
    print(d["address"].value_counts())
    #print(d[["Company_Name","add"]])
    #d['address'] = d['address'].astype('|S')
    print("\nENTER REGION FOR FURTHER ANALYSIS: \n 1.Kargil unclassified \n 2.Leh unclassified \n 3.Unclassified")
    i=int(input("Enter your choice:"))
    if i==1:
        
        clas = d[d['add']== 'kargil unclassified']
        
        print(c)
        print("SELECT CRITERIA FOR FURTHER ANALYSIS: \n 1.REGISTRATION YEAR \n 2.SECTOR \n 3.COMPANY CLASS \n 4.COMPANY STATUS" )
        j=int(input("Enter your choice: "))
        if j==1:
            reg_date(clas);
        elif j==2:
            activity(clas);
        elif j==3:
            classs(clas);
        elif j==4:
            status(clas);
        else :
            print("INVALID INPUT")
    elif i==2:
        
        clas = d[d['address']=='leh unclassified']
        
        print("SELECT CRITERIA FOR FURTHER ANALYSIS: \n 1.REGISTRATION YEAR \n 2.SECTOR \n 3.COMPANY CLASS \n 4.COMPANY STATUS" )
        j=int(input("Enter your choice: "))
        if j==1:
            reg_date(clas);
        elif j==2:
            activity(clas);
        elif j==3:
            classs(clas);
        elif j==4:
            status(clas);
        else :
            print("INVALID INPUT")

    elif i==3:
        
        
        clas = d[d["address"] == 'unclassified']
        print(clas)

        print("SELECT CRITERIA FOR FURTHER ANALYSIS: \n 1.REGISTRATION YEAR \n 2.SECTOR \n 3.COMPANY CLASS \n 4.COMPANY STATUS" )
        j=int(input("Enter your choice: "))
        if j==1:
            reg_date(clas);
        elif j==2:
            activity(clas);
        elif j==3:
            classs(clas);
        elif j==4:
            status(clas);
        else :
            print("INVALID INPUT")
        


#                                                                   WELCOME SCREEN CODE

       


print("WELCOME TO DATA ANALYSIS OF COMPANIES LOCATED IN LEH & LADAKH REGION\n\n")

print("SELECT INPUT FOR ANALYSIS")
print(''' 1.TO GET COMPANY WITH HIGHEST AUTHORIZED CAPITAL VALUE \n 2.TO GET COMPANY WITH HIGHEST PAIDUP CAPITAL VALUE \n 3. CLASSIFICATION OF COMPANIES \n 4.PAIDUP BY AUTHORIZED CAPITAL % CLASSIFICATION \n 5. REGION BASED ANALYSIS OF COMPANIES''')

i=int(input("Enter your choice:"))

if(i==1):
    max_auth();
elif(i==2):
    max_paid();
elif(i==3):
    print("CLASSIFICATION BASED ON : ")
    print("1.AUTHORIZED BY PAIDUP CAPITAL \n 2.REGISTRATION YEAR \n 3.SECTOR \n 4.COMPANY CLASS \n 5.COMPANY STATUS")
    j=int(input("ENTER YOUR CHOICE:"))
    if j==1:
        auth_cap(d);
    elif j==2:
        reg_date(d);
    elif j==3:
        activity(d);
    elif j==4:
        classs(d);
    elif j==5:
        status(d);
    else :
        print("INVALID INPUT")
elif(i==4):
    percentage(d);

elif(i==5):
    region(d);

else:
    print("INVALID INPUT")

