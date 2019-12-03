import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\Ricky\\Desktop')
f = pd.read_csv('Military Expenditure.csv')
while True:
    names = list(f['Name'])
    req = input("Enter name of country whose military expenditure you would like to see(X to exit): ")
    if req == 'X':
        break
    else:
        if names.count(req)==0:
            print("Sorry, could not find name, please try again.")
            continue
        else:
            ind = names.index(req)
            x = [i for i in range(1960, 2019)]
            y = []
            for i in range(1960, 2019):
                try:
                    y.append(int(f[str(i)][ind])//10**7)
                except ValueError:
                    y.append(0)
            
            plt.axis([1960,2019,0,10000])
            plt.bar(x,y,align='center')
            plt.xlabel('Year')
            plt.ylabel('Military Expenditure in Crores')
            plt.show()
