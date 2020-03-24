#Structure: 
#Read the contents of the excel sheet into csv file and took the data from the csv file.
#Using panda module, we obtained the data needed for forming questions.
#Using the random module, we obtain allocate random questions to each question paper and shuffle the options to get a unique answer key.

"""Assumptions: 
•	The file is stored in the path used, hence works only on this particular system.
•	User can only view only one question paper and its answer key at a time
•	There is no memory constraint
•	Each question paper may have one or two common questions.
•	All the questions are of the same type.
•	The first column “Number” has been deleted from the original file provided, and then the operations are performed.
•	The file from which the information is extracted is a CSV file of the original(edited) excel file."""



import sys
import pandas as pd 
import random

df=pd.read_csv('Questionpapers.csv',usecols=['Name','Symbol'])
#creating separate lists for name ans symbol
name=df['Name'].tolist()
symbol=df['Symbol'].tolist()
#creating a dictionary where question is the key and answer is its value
ori_dict={name[i]:[symbol[i]] for i in range(len(name))}
final_dict={}

#creating a choices dictionary and editing it to create questions and their choices

for i in name:
    for j in symbol:
        choices=random.sample(symbol,2)
        break
    final_dict[i]=choices
#print final_dict
result={key: value + final_dict[key] for key,value in ori_dict.items()}
#print(result)
#code to replace duplicate choices of a question
for i,j in result.items():
    if (j[0]==j[1])|(j[0]==j[2]):
        j[0]=random.choice( [x for x in symbol if (x!=j[1])&(x!=j[2])])
        #print(j) 

for i in result.values():
    random.shuffle(i)
    #print(i)
#printing question paper
print("You can only print one question paper set at a time")

while(1):

    print("\nEnter 1 to view a question paper: ")
    ch=int(input())
    print("\n")

    if ch==1:

        temp_n=random.sample(result.keys(),20)
        #print(temp_n)
        temp_s=[result[k] for k in temp_n]
        #print(temp_s)

        for i in range(20):
            print(str(i+1)+". What is the symbol of "+temp_n[i]+"?")
            print("A."+temp_s[i][0]+" B."+temp_s[i][1]+" C."+temp_s[i][2]+"\n")

        print("Answer key for the above question paper:\n")

        for i in temp_n:
            x=temp_n.index(i)+1
            if (ori_dict[i][0]==result[i][0]):
                print(str(x)+".A")

            elif (ori_dict[i][0]==result[i][1]):
                print(str(x)+".B")

            elif (ori_dict[i][0]==result[i][2]):
                print(str(x)+".C")

            else:
                print(str(x)+".None")

    else:
        print("Try Again!")
        sys.exit(1)
                

            
        
        
    






































































































































































































































































































































































































































































































































































































        
    