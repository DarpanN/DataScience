import pandas as pd
import random


# data = []
# with open("toy_dataset.csv", "r") as f:
#     line = f.readline()
#     header = line.strip().split()


#     for line in f:
#         line = line.strip().split(',')
#         data.append(line)
    
#     print(data)

#     print(header)


   


# df = pd.read_csv('toy_dataset.csv')

# column = df['Number']

# print(df)
# counts = column.value_counts('Number')
# print(counts)





#1

# df = pd.read_csv('toy_dataset.csv')
# gender = df['Gender']
# counts = gender.value_counts()
# print("Number of males:", counts['Male'])
# print("Number of females:", counts['Female'])




#2

# import csv
# city_names = set()
# with open("toy_dataset.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         city_names.add(row["City"])

# unique_city_count = len(city_names)
# print("Number of unique city names:", unique_city_count)




#3

import csv
incomes = []
with open("toy_dataset.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["City"] == "Boston":
            incomes.append((row["Income"]))

max_income = max(incomes)
print("Maximum income:", max_income)





#4

# import pandas as pd
# df = pd.read_csv('toy_dataset.csv')
# grouped = df.groupby('City')['Income'].sum()
# highest_income_city = grouped.idxmax()
# print(f'The city with the highest total income is {highest_income_city}')



#5

# import pandas as pd
# df = pd.read_csv('toy_dataset.csv')
# filtered_df = df[df['Illness'] == 'Yes']
# grouped = filtered_df.groupby('Gender').size()
# print("Illness Male and Female ", grouped)



#6

# import pandas as pd
# df = pd.read_csv('toy_dataset.csv')
# grouped = df.groupby('Gender')['Income'].mean()
# print("Avg Income By ", grouped)



#7


import pandas as pd
df = pd.read_csv('toy_dataset.csv')

filtered_df = df[df['Income'] > 100000]

mean_age = filtered_df['Age'].mean()
print("Mean Age People Greater Than 100000: ", mean_age)



#8


# import pandas as pd

# df = pd.read_csv('toy_dataset.csv')
# filtered_df = df[(df['Age'] >= 60) & (df['Age'] <= 65)]
# grouped = filtered_df.groupby('City').size()
# most_population_city = grouped.idxmax()

# print(f'The city with the most population of people aged 60-65 is {most_population_city}')



print(df)




