import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
#scikit-learn

NumRecords=500
IndependentVar= "Area"
DependentVar="Price"



#generate 500 random data points
area_list=[]
price_list=[]


for i in range(NumRecords):
    currentArea = 30 + i * 0.5
    currentPrice = currentArea * 3500000
    area_list.append(currentArea)
    price_list.append(currentPrice) 

data = {
    "Area": area_list,
    "Price": price_list

}


df=pd.DataFrame(data)
x=df[["Area"]]
y=df["Price"]

model=LinearRegression()
model.fit(x,y)

def calculatePrice(area):
    result = model.predict([[area]])[0]
    return result  
    