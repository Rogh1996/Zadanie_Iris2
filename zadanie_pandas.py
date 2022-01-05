import pandas as pd

dane = pd.read_csv("iris.csv")

writer = pd.ExcelWriter('iris2.xlsx')

for group, data in dane.groupby('variety'):
    data.to_excel(writer,group)
writer.save()