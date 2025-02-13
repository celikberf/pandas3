import pandas as pd
import numpy as np

data = {
    'Column1' : [1,2,3,4,5],
    'Column2' : [10,20,13,20,25],
    'Column3' : ['abc','bcaa','ade','cb','dea']
}


df = pd.DataFrame(data)

def kareAl(x):
    return x * x

kareAl2 = lambda x : x * x

result = df
result = df["Column2"].unique() #tekrarlanan ifadeleri 1 kere alır
result = df["Column2"].nunique() #tekrarlanan sayıyı almadan kaç kolon oldugunu verir.
result = df["Column2"].value_counts() #hangi ifadeden kaç tane oldugunu verir
result = df["Column1"] * 2
result = df['Column1'].apply(kareAl)
result = df['Column1'].apply(kareAl2)
result = df['Column3'].apply(len) #kaç karakterli oldugunu verir
df["Column4"] = df['Column3'].apply(len)
result = df.columns
result = len(df.columns)
result = len(df.index) # satır bilgisi
result = df.info
result = df.sort_values("Column2") #sayıları b>k sıralar
result = df.sort_values("Column3") #alfabetik sıralar
result = df.sort_values("Column3",ascending= False) #z>a sıralar
df = df.pivot_table(index="Column1",columns="Column2",values="Column3")




print(df)