from matplotlib import pyplot as plt

plt.title("Salary Data")
x = [20,30,40,50,60,70,80,90]
y = [15000,18000,25000,33000,39000,40000,42000,50000]
y2 = [8000,8700,9400,12000,15000,17878,20000,23670]
plt.xlabel("Age")
plt.ylabel("Salary")

plt.plot(x,y  ,label="High Salary")
plt.plot(x,y2 ,label="Less Salary")

plt.legend()
plt.show()
