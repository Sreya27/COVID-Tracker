# IIIT DWD
# COVID_Tracker_3

import pandas as pd

# Reading confirmed cases file
df1=pd.read_csv("time_series_covid_19_confirmed.csv")

# code for adding the values as needed
w1 = df1["1/22/20"] + df1["1/23/20"] + df1["1/24/20"] + df1["1/25/20"] + df1["1/26/20"] + df1["1/27/20"] + df1["1/28/20"]
df1["Week1"]= w1
w2 = df1["1/29/20"] + df1["1/30/20"] + df1["1/31/20"] + df1["2/1/20"] + df1["2/2/20"] + df1["2/3/20"] + df1["2/4/20"]
df1["Week2"]= w2
w3 = df1["2/5/20"] + df1["2/6/20"] + df1["2/7/20"] + df1["2/8/20"] + df1["2/9/20"] + df1["2/10/20"] + df1["2/11/20"]
df1["Week3"]= w3
w4 = df1["2/12/20"] + df1["2/13/20"] + df1["2/14/20"] + df1["2/15/20"] + df1["2/16/20"] + df1["2/17/20"] + df1["2/18/20"]
df1["Week4"]= w4
w5 = df1["2/19/20"] + df1["2/20/20"] + df1["2/21/20"] + df1["2/22/20"] + df1["2/23/20"] + df1["2/24/20"] + df1["2/25/20"]
df1["Week5"]= w5
w6 = df1["2/26/20"] + df1["2/27/20"] + df1["2/28/20"] + df1["2/29/20"] + df1["3/1/20"] + df1["3/2/20"] + df1["3/3/20"]
df1["Week6"]= w6
w7 = df1["3/4/20"] + df1["3/5/20"] + df1["3/6/20"] + df1["3/7/20"] + df1["3/8/20"]+df1["3/9/20"] + df1["3/10/20"]
df1["Week7"]= w7
w8 = df1["3/11/20"] + df1["3/12/20"] + df1["3/13/20"] + df1["3/14/20"] + df1["3/15/20"] + df1["3/16/20"] + df1["3/17/20"]
df1["Week8"]= w8
w9 = df1["3/18/20"] + df1["3/19/20"] + df1["3/20/20"] + df1["3/21/20"] + df1["3/22/20"] + df1["3/23/20"] + df1["3/24/20"]
df1["Week9"]= w9
w10 = df1["3/25/20"] + df1["3/26/20"] + df1["3/27/20"] + df1["3/28/20"] + df1["3/29/20"] + df1["3/30/20"] + df1["3/31/20"]
df1["Week10"]= w10
w11 = df1["4/1/20"] + df1["4/2/20"] + df1["4/3/20"] + df1["4/4/20"] + df1["4/5/20"] 
df1["Week11"]= w11

print("(The cases considered here are from 22nd January to 5th April)")
print("The average number of confirmed cases per week are as follows:\n")

Total1 = df1['Week1'].sum()
Total1=int(Total1/7)
print("Week 1:",Total1,"confirmed\n")

Total2 = df1['Week2'].sum()
Total2=int(Total2/7)
print("Week 2:",Total2,"confirmed\n")

Total3 = df1['Week3'].sum()
Total3=int(Total3/7)
print("Week 3:",Total3,"confirmed\n")

Total4 = df1['Week4'].sum()
Total4=int(Total4/7)
print("Week 4:",Total4,"confirmed\n")

Total5 = df1['Week5'].sum()
Total5=int(Total5/7)
print("Week 5:",Total5,"confirmed\n")

Total6 = df1['Week6'].sum()
Total6=int(Total6/7)
print("Week 6:",Total6,"confirmed\n")

Total7 = df1['Week7'].sum()
Total7=int(Total7/7)
print("Week 7:",Total7,"confirmed\n")

Total8 = df1['Week8'].sum()
Total8=int(Total8/7)
print("Week 8:",Total8,"confirmed\n")

Total9 = df1['Week9'].sum()
Total9=int(Total9/7)
print("Week 9:",Total9,"confirmed\n")

Total10 = df1['Week10'].sum()
Total10=int(Total10/7)
print("Week 10:",Total10,"confirmed\n")

Total11 = df1['Week11'].sum()
Total11=int(Total11/5)
print("Week 11:",Total11,"confirmed\n")

# Reading death cases file
df=pd.read_csv("time_series_covid_19_deaths.csv")

w1 = df["1/22/20"] + df["1/23/20"] + df["1/24/20"] + df["1/25/20"] + df["1/26/20"] + df["1/27/20"] + df["1/28/20"]
df["Week1"]= w1
w2 = df["1/29/20"] + df["1/30/20"] + df["1/31/20"] + df["02-01-2020"] + df["02-02-2020"] + df["02-03-2020"] + df["02-04-2020"]
df["Week2"]= w2
w3 = df["02-05-2020"] + df["02-06-2020"] + df["02-07-2020"] + df["02-08-2020"] + df["02-09-2020"] + df["02-10-2020"] + df["02-11-2020"]
df["Week3"]= w3
w4 = df["02-12-2020"] + df["2/13/20"] + df["2/14/20"] + df["2/15/20"] + df["2/16/20"] + df["2/17/20"] + df["2/18/20"]
df["Week4"]= w4
w5 = df["2/19/20"] + df["2/20/20"] + df["2/21/20"] + df["2/22/20"] + df["2/23/20"] + df["2/24/20"] + df["2/25/20"]
df["Week5"]= w5
w6 = df["2/26/20"] + df["2/27/20"] + df["2/28/20"] + df["2/29/20"] + df["03-01-2020"] + df["03-02-2020"] + df["03-03-2020"]
df["Week6"]= w6
w7 = df["03-04-2020"] + df["03-05-2020"] + df["03-06-2020"] + df["03-07-2020"] + df["03-08-2020"]+df["03-09-2020"] + df["03-10-2020"]
df["Week7"]= w7
w8 = df["03-11-2020"] + df["03-12-2020"] + df["3/13/20"] + df["3/14/20"] + df["3/15/20"] + df["3/16/20"] + df["3/17/20"]
df["Week8"]= w8
w9 = df["3/18/20"] + df["3/19/20"] + df["3/20/20"] + df["3/21/20"] + df["3/22/20"] + df["3/23/20"] + df["3/24/20"]
df["Week9"]= w9
w10 = df["3/25/20"] + df["3/26/20"] + df["3/27/20"] + df["3/28/20"] + df["3/29/20"] + df["3/30/20"] + df["3/31/20"]
df["Week10"]= w10
w11 = df["04-01-2020"] + df["04-02-2020"] + df["04-03-2020"] + df["04-04-2020"] + df["04-05-2020"] 
df["Week11"]= w11

print("(The cases considered here are from 22nd January to 5th April)")
print("The average number of daeath cases per week are as follows:\n")

Total1 = df['Week1'].sum()
Total1=int(Total1/7)
print("Week 1:",Total1,"deaths\n")

Total2 = df['Week2'].sum()
Total2=int(Total2/7)
print("Week 2:",Total2,"deaths\n")

Total3 = df['Week3'].sum()
Total3=int(Total3/7)
print("Week 3:",Total3,"deaths\n")

Total4 = df['Week4'].sum()
Total4=int(Total4/7)
print("Week 4:",Total4,"deaths\n")

Total5 = df['Week5'].sum()
Total5=int(Total5/7)
print("Week 5:",Total5,"deaths\n")

Total6 = df['Week6'].sum()
Total6=int(Total6/7)
print("Week 6:",Total6,"deaths\n")

Total7 = df['Week7'].sum()
Total7=int(Total7/7)
print("Week 7:",Total7,"deaths\n")

Total8 = df['Week8'].sum()
Total8=int(Total8/7)
print("Week 8:",Total8,"deaths\n")

Total9 = df['Week9'].sum()
Total9=int(Total9/7)
print("Week 9:",Total9,"deaths\n")

Total10 = df['Week10'].sum()
Total10=int(Total10/7)
print("Week 10:",Total10,"deaths\n")

Total11 = df['Week11'].sum()
Total11=int(Total11/5)
print("Week 11:",Total11,"deaths\n")

# Reading recovered cases file
df2=pd.read_csv("time_series_covid_19_recovered.csv")

w1 = df2["1/22/20"] + df2["1/23/20"] + df2["1/24/20"] + df2["1/25/20"] + df2["1/26/20"] + df2["1/27/20"] + df2["1/28/20"]
df2["Week1"]= w1
w2 = df2["1/29/20"] + df2["1/30/20"] + df2["1/31/20"] + df2["2/1/20"] + df2["2/2/20"] + df2["2/3/20"] + df2["2/4/20"]
df2["Week2"]= w2
w3 = df2["2/5/20"] + df2["2/6/20"] + df2["2/7/20"] + df2["2/8/20"] + df2["2/9/20"] + df2["2/10/20"] + df2["2/11/20"]
df2["Week3"]= w3
w4 = df2["2/12/20"] + df2["2/13/20"] + df2["2/14/20"] + df2["2/15/20"] + df2["2/16/20"] + df2["2/17/20"] + df2["2/18/20"]
df2["Week4"]= w4
w5 = df2["2/19/20"] + df2["2/20/20"] + df2["2/21/20"] + df2["2/22/20"] + df2["2/23/20"] + df2["2/24/20"] + df2["2/25/20"]
df2["Week5"]= w5
w6 = df2["2/26/20"] + df2["2/27/20"] + df2["2/28/20"] + df2["2/29/20"] + df2["3/1/20"] + df2["3/2/20"] + df2["3/3/20"]
df2["Week6"]= w6
w7 = df2["3/4/20"] + df2["3/5/20"] + df2["3/6/20"] + df2["3/7/20"] + df2["3/8/20"]+df2["3/9/20"] + df2["3/10/20"]
df2["Week7"]= w7
w8 = df2["3/11/20"] + df2["3/12/20"] + df2["3/13/20"] + df2["3/14/20"] + df2["3/15/20"] + df2["3/16/20"] + df2["3/17/20"]
df2["Week8"]= w8
w9 = df2["3/18/20"] + df2["3/19/20"] + df2["3/20/20"] + df2["3/21/20"] + df2["3/22/20"] + df2["3/23/20"] + df2["3/24/20"]
df2["Week9"]= w9
w10 = df2["3/25/20"] + df2["3/26/20"] + df2["3/27/20"] + df2["3/28/20"] + df2["3/29/20"] + df2["3/30/20"] + df2["3/31/20"]
df2["Week10"]= w10
w11 = df2["4/1/20"] + df2["4/2/20"] + df2["4/3/20"] + df2["4/4/20"] + df2["4/5/20"] 
df2["Week11"]= w11

print("(The cases considered here are from 22nd January to 5th April)")
print("The average number of recovered cases per week are as follows:\n")

Total1 = df2['Week1'].sum()
Total1=int(Total1/7)
print("Week 1:",Total1,"recovered\n")

Total2 = df2['Week2'].sum()
Total2=int(Total2/7)
print("Week 2:",Total2,"recovered\n")

Total3 = df2['Week3'].sum()
Total3=int(Total3/7)
print("Week 3:",Total3,"recovered\n")

Total4 = df2['Week4'].sum()
Total4=int(Total4/7)
print("Week 4:",Total4,"recovered\n")

Total5 = df2['Week5'].sum()
Total5=int(Total5/7)
print("Week 5:",Total5,"recovered\n")

Total6 = df2['Week6'].sum()
Total6=int(Total6/7)
print("Week 6:",Total6,"recovered\n")

Total7 = df2['Week7'].sum()
Total7=int(Total7/7)
print("Week 7:",Total7,"recovered\n")

Total8 = df2['Week8'].sum()
Total8=int(Total8/7)
print("Week 8:",Total8,"recovered\n")

Total9 = df2['Week9'].sum()
Total9=int(Total9/7)
print("Week 9:",Total9,"recovered\n")

Total10 = df2['Week10'].sum()
Total10=int(Total10/7)
print("Week 10:",Total10,"recovered\n")

Total11 = df2['Week11'].sum()
Total11=int(Total11/5)
print("Week 11:",Total11,"recovered\n")

