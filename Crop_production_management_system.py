#Structure: 
#We read the contents of the excel sheet into csv file and took the data from the csv file.
#Using panda module, we obtained the data needed for a particular crop/year using groupby function.
#We tried plotting the graph using matplotlib by converting the csv file into list and summing the production of a particular crop in a particular year.

"""Assumptions: 
      1) The file is stored in the path used, hence works only on this particular system.
      2) User can only view one crop’s graph at a time
      3) There is no memory constraint
Constraint:
1)	If a year/crop is entered whose info is unavailable, then there is a compilation error."""



import sys
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt



df=pd.read_csv('CropsDataFile.csv',usecols=['Year','Crop_Name','Production'])
while(1):
    
    print("Enter 1 to retrive data year wise,")
    print("Enter 2 to retrive cropwise details")
    print("Enter 3 to exit system")
    ch=int(input())
    if ch==1:
       print("Enter year")
       yr=input()
       gk=df.groupby('Year')
       s=gk.get_group(yr)
       print(s) 
    elif ch==2:
       crop=input("Enter crop:",)
       gk=df.groupby('Crop_Name')
       s=gk.get_group(crop)
       print(s)
       
       print("\nenter 1 if you a graph\n")
       print("enter 2 if you want to exit\n")
       ch2=int(input())
       if ch2==1:
           ss=s.groupby('Year')['Production'].apply(lambda x: x.tolist()).to_dict()
           #print(ss)
           pro=list()
           sum=0
           for i in ss.values():
                for j in i:
                    sum+=float(j)
                pro.append(sum)
                sum=0
           #print(pro)
           year=list()
           for x in ss.keys():
               year.append(x)
           #print(year)
       
           plt.bar(year,pro)
           plt.xlabel('year')
           plt.ylabel('production')
           plt.title('Year wise production of crop')
           plt.show()
       else:
           sys.exit(1)
           
           
    elif ch==3:
       print("\nThank you for using our system!\nHave a good day!\n")
       sys.exit(1)
    else:
        print("Wrong Choice!! Try again!")

