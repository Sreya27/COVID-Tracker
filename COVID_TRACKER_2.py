import sys
import csv
lis=[]
def main():
    while True:
        print("\n\nEnter:\n1) if you wan to check high risk countries\n2) If you want to exit system")
        ch=int(input())
        if ch==1:
            print("Enter your age")
            age=input()
            if (int(age)<15):
                print("\nSorry,Invalid age!!!!")
            elif(int(age)>25):
                print("\nSorry,Invalid age!!!!")
            else:
                print("Enter the state you want to check:\n 1 for New York\n 2 for Massachusettes\n 3 for Pennselvania\n 4 for California\n 5 for Michigan\n 6 for Florida\n 7 for Texas\n 8 for Georgia\n 9 for Maryland \n 10 for Maharashtra\n 11 for Karnatka ")
                ch2= input()
                with open('agewise.csv','r') as f:
                    read=csv.reader(f)
                    for row in read:
                        lis.append(row)
                col1=[x[0] for x in lis]
                col2=[y[2] for y in lis]
                col3=[z[3] for z in lis]
                if ch2 in col1:
                    if (age>=col2):
                        if (age<=col3):
                            cases=[c[4] for c in lis]
                            if cases>=1000:
                                print("\n\nThe state is a high risk state for your age group!DO NOT TRAVEL!!!!")
                            elif (cases>=200):
                                print("\n\nThe state is at average risk for your age group!!!!")
                            elif cases<200:
                                print("\n\nThe state is at low risk for your age group, and safe to travel!!")
                f.close()
        elif ch==2:
            print("Thank You for using our system!")
            sys.exit(1)
        else:
            print("Unvalid choice! Try again")
main()
