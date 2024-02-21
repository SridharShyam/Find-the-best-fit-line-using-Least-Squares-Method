# Implementation of Univariate Linear Regression
## AIM:
To implement univariate Linear Regression to fit a straight line using least squares.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Jupyter notebook

## Algorithm
1. Get the independent variable X and dependent variable Y.
2. Calculate the mean of the X -values and the mean of the Y -values.
3. Find the slope m of the line of best fit using the formula. 
<img width="231" alt="image" src="https://user-images.githubusercontent.com/93026020/192078527-b3b5ee3e-992f-46c4-865b-3b7ce4ac54ad.png">
4. Compute the y -intercept of the line by using the formula:
<img width="148" alt="image" src="https://user-images.githubusercontent.com/93026020/192078545-79d70b90-7e9d-4b85-9f8b-9d7548a4c5a4.png">
5. Use the slope m and the y -intercept to form the equation of the line.
6. Obtain the straight line equation Y=mX+b and plot the scatterplot.

## Program:
```
/*
Program to implement univariate Linear Regression to fit a straight line using least squares.
Developed by: SHYAM S
Register Number: 212223240156
*/
```
```
import numpy as np
import matplotlib.pyplot as plt
x=np.array(eval(input("Enter x values:")))
y=np.array(eval(input("Enter y values:")))
X=np.mean(x)
Y=np.mean(y)
num=0
den=0
for i in range(len(x)):
  num=num+((x[i]-X)*(y[i]-Y))
  den=den+((x[i]-X)**2)
m=num/den
c=Y-m*X
print("Slope:",m,"Intercept:",c)
Ypred=m*x+c
print("Y predicted:",Ypred)

plt.scatter(x,y)
plt.plot(x,Ypred,color='yellow')
plt.show()
```

## Output:
![image](https://github.com/SridharShyam/Find-the-best-fit-line-using-Least-Squares-Method/assets/144871368/b9b86c57-2b4c-453e-8dae-912c6d80bec4)


## Result:
Thus the univariate Linear Regression was implemented to fit a straight line using least squares using python programming.
