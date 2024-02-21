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