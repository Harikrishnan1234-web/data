#3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.random.rand(100,1)
y = 2 + 3*X + np.random.randn(100,1)

# Models
m1 = LinearRegression(fit_intercept=False).fit(X,y)
m2 = LinearRegression().fit(X,y)

# Plot
plt.scatter(X,y)
plt.plot(X, m1.predict(X),'r')
plt.plot(X, m2.predict(X),'b')
plt.show()

# Output
print(m1.coef_[0][0])
print(m2.intercept_[0], m2.coef_[0][0])


#2
import numpy as np, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
X = np.random.rand(100,1); y = 2 + 3*X + np.random.randn(100,1)

m = LinearRegression().fit(X,y)

print("Slope:", m.coef_[0][0], "Intercept:", m.intercept_[0])

plt.scatter(X,y); plt.plot(X,m.predict(X)); plt.show()