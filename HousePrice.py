import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
#scikit-learn


data={
    "Area": [45,60,72,85,95,110,120,130,150,160,175,180,200,220,250],
    "Price": [15000000,200000000,250000000,300000000,350000000,400000000,450000000,500000000,600000000,650000000]
}

df=pd.DataFrame(data)
x=df[["Area"]]
y=df["Price"]

model=LinearRegression()
model.fit(x,y)

def calculatePrice(area):
    result = model.predict([[area]])[0]
    return result  