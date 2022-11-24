import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np

dct = pd.read_csv("diabetes.csv")

# imports files
GluD = dct["Glucose"]
InsD = dct["Insulin"]
OutD = dct["Outcome"]

Glu=[]
Ins=[]
Out=[]
index = 0

for instance in GluD:
    Glu.append(float(instance))
for instance in InsD:
    Ins.append(float(instance))
for instance in OutD:
    Out.append(float(instance))

# print(Glu, Ins, Out)
# print(len(Glu), len(Ins), len(Out))

# Get rid of 0 values
cleanGlu=[]
cleanIns=[]
cleanOut=[]
for instance in Glu:
    if instance != 0 and Ins[index] != 0:
        cleanGlu.append(instance)
        cleanIns.append(Ins[index])
        cleanOut.append(Out[index])
    index+=1
Glu=cleanGlu
Ins=cleanIns
Out=cleanOut
# print(len(Glu), len(Ins), len(Out))

posGlu=[]
posIns=[]
negGlu=[]
negIns=[]
index = 0
for instance in Glu:
    if Out[index] == 1:
        posGlu.append(instance)
        posIns.append(Ins[index])
    else:
        negGlu.append(instance)
        negIns.append(Ins[index])
    index += 1
print(len(posGlu), len(posIns), len(negIns))
print(st.mean(posGlu), st.mean(posIns), st.mean(negGlu), st.mean(negIns))

plt.gcf().set_size_inches(16, 9)



ax1 = plt.subplot(2, 2, 1)
ax1.hist(posGlu)
plt.title("Positive Diabetes Glucose")


ax2 = plt.subplot(2, 2, 2, sharey=ax1, sharex=ax1)
ax2.hist(negGlu)
plt.title("Negative Diabetes Glucose")

ax3 = plt.subplot(2, 2, 3)
ax3.hist(posIns)
plt.title("Positive Diabetes Insulin")

ax4 = plt.subplot(2, 2, 4, sharey=ax3, sharex=ax3)
ax4.hist(negIns)
plt.title("Negative Diabetes Insulin")

plt.show()
    

