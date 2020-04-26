#IIIT DHARWAD
#COVID TRACKER 1
import pandas as pd
import matplotlib.pyplot as plt
import sys
import requests
from bs4 import BeautifulSoup

#creating variables for urls of the datasets and parsing the necessary information
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
death_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

r = requests.get("https://en.wikipedia.org/wiki/Developed_country#Rankings")
                 
intern = list()
soup = BeautifulSoup(r.text, "html.parser")

table = soup.find('table',{'class':'multicol'})
table_1 = table.find_all('a')

for i in table_1:
    intern.append(i.get('title'))
intern_countries = [i for i in intern if i]
del intern

#reading the csv file and shaping it into a 2D dataframe
df_c = pd.read_csv(confirmed_url, error_bad_lines=False)
df_d = pd.read_csv(death_url, error_bad_lines=False)

#removing the province column
df_c = df_c.loc[:,'Country/Region':]
df_d = df_d.loc[:,'Country/Region':]

#summing the values, so that theres only one row for each country
df_c = df_c.groupby('Country/Region').sum()
df_d = df_d.groupby('Country/Region').sum()

#making countries as index and all the dates as columns
df_c = df_c.loc[:,'1/22/20':]
df_d = df_d.loc[:,'1/22/20':]

#writing all the country names into a list
countries = list(df_c.index)
final_countries = list(set(intern_countries) & set(countries))
del intern_countries

while (1):
    print("\nEnter 1 to display graphs")
    print("Enter 2 to display the top twenty high-risk countries")
    print("Enter 3 to exit\n")
    num = int(input())
    
    if (num==1):
        
        print("\nEnter the country for which the graph is to be displayed\n")
        c = str(input())
        dates = list(df_c.columns.values.tolist())
        death_growth_per_day = list()

        if c in countries:
            for i,j in zip(df_c,df_d):
                temp = float((df_d.loc[c][j]/df_c.loc[c][i])*100)
                death_growth_per_day.append(temp)
            plt.plot(dates,death_growth_per_day)
            plt.title(c)
            plt.show()
        else:
            print("\nThe country name isn't valid")
    
    if (num==2):
        high_risk_countries = list()
        for i in final_countries:
            for j,x in zip(df_c,df_d):
                if (df_d.loc[i][x]==0) | (df_c.loc[i][j]==0):
                    death_rate = 0
                elif df_c.loc[i][j]!=0:
                    death_rate = (df_d.loc[i][x]/df_c.loc[i][j])*100
                else:
                    death_rate = 0
        
                two_percent = (2/100)*df_c.loc[i][j]
        
                if (death_rate!=0) & (death_rate>=two_percent):
            

                    if i in high_risk_countries:
                        break
                    else:
                        high_risk_countries.append(i)
        print("\nTop high risk countries to travel to for internships are:\n")
        for i in high_risk_countries:
            print(i)
        
    if (num==3):
        sys.exit(1)