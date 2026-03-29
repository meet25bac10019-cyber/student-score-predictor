# student score predictor 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle 

data=pd.read_csv("data.csv")
x=data[['hours_study','sleep_hours','attendance']]
y=data['marks']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
model=LinearRegression()
model.fit(x_train,y_train)

hours = int(input("enter total number of study hours  : "))
sleep = int(input("enter the total number of sleeping hours : "))
attendance = float(input("enter the class attendance % : "))
len=hours + sleep
if hours>24 or sleep>24 or attendance >100 or len>24 :
    print (" :ERROR: ")
else :
    input_data = pd.DataFrame([[hours,sleep,attendance]],columns=['hours_study','sleep_hours','attendance'])
    # prediction = model.predict([[hours,sleep,attendance]])
    prediction=model.predict(input_data)
    if prediction <=100 :
        print(f"predicted marks : {prediction[0]:.2f}")
    else :
        print(" :ERROR: ")
