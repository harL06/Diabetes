import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


dct = pd.read_csv("diabetes.csv")

# imports files
BPd = dct["BloodPressure"]
BMId = dct["BMI"]

# Coverts file columns to lists
BP=[]
BMI=[]
index = 0

for instance in BPd:
    BP.append(float(instance))
for instance in BMId:
    BMI.append(float(instance))
    
# Prints averages/means of both lists
# print("Average BP:", st.mean(BP), "\nMode BP:", st.mode(BP), "\nMedian BP:", st.median(BP))
# print("Average BMI:",st.mean(BMI), "\nMode BMI:", st.mode(BMI), "\nMedian BMI:", st.median(BMI))



cleanBP=[]
cleanBMI=[]
for instance in BP:
    if instance != 0 and BMI[index] != 0:
        cleanBP.append(instance)
        cleanBMI.append(BMI[index])
    index+=1




plt.subplot(1, 1, 1)
plt.scatter(cleanBMI, cleanBP, color ='#D972FF')

plt.title("BMI against Blood Pressure")
plt.ylabel('Blood Pressue')
plt.xlabel('BMI')


plt.show()


