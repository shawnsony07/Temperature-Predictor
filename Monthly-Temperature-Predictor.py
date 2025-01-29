#_________________Imported Libraries.__________________#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#_________________Cost Function and Gradient Descent.______________#
def costFunction(X, y, theta):
    m = y.size
    prediction = np.dot(X, theta)
    sqrErrors = (prediction - y)**2
    J = 1/(2*m) * np.sum(sqrErrors)
    return J


def gradientDescent(X, y, theta, num_iters, alpha):
    m = y.size
    J = []
    for i in range(1, num_iters):
        h = (np.dot(X,theta))
        theta = theta - np.transpose((1/m) * np.dot(np.transpose(h - y), X))*alpha
        J.append(costFunction(X,y,theta))
    return theta, J
#_________________PLot Linear Regression Line.__________________#
fig1, ax1 = plt.subplots()
def PlotLinearLine(X, y):
    ax1.plot(X, y,label = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
    plt.xlabel('YEAR')
    plt.ylabel('log10(TEMPERATUREÂ°C)')
    plt.legend(loc = 'upper right',fontsize = 7)
    plt.tight_layout()
    plt.show()
#______________________main____________________________#
#_________________Data.__________________#
x = pd.read_csv('station.csv')
x.drop(x.index[0:39], inplace=True)
x['Ones'] = 1
#_________________Features and Target Variable._________________#
X = np.array(x[['Ones', 'YEAR']])
y = np.array(x[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']])
#_________________Intializing Parameters__________________#
theta = np.zeros((2, 1))
#_________________Making Data Linear._________________#
M = []
for i in y:
    for k in range(len(i)):
        if i[k]!=999.9:
            M.append(i[k])
m = np.mean(M)
for i in y:
    for k in range(len(i)):
        if i[k]==999.9:
            i[k]=m
y = np.log10(y)
X = np.log10(X)
#_________________Setting Learning Rate and Number of Iterations_________________#
alpha = 0.01
num_iters = 2000
#_________________Running the Linear Regression Algorithm.__________________#
(costFunction(X,y,theta))
theta, J = gradientDescent(X, y, theta, num_iters, alpha)
PlotLinearLine(x['YEAR'],np.dot(X , theta))
#________________Prediction______________#
n = int(input("Enter Year: "))
Months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
Month = int(input("Enter Month: (enter from 1- 12)"))
O = np.array([[1,n]])
P = np.round(10**np.dot(np.log10(O), theta),2)
print(f"The average temperature for the YEAR: {n} in :{Months[Month-1]} is {P[0][Month-1]}°C")