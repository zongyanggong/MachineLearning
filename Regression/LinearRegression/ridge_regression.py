import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import SGDRegressor

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

ridge_reg = Ridge(alpha=0.4, solver='sag')
ridge_reg.fit(x, y)
print(ridge_reg.predict([[1.5]]))
print(ridge_reg.intercept_)
print(ridge_reg.coef_)

print('-' * 45)
ridge_reg = SGDRegressor(penalty='l2', alpha=0.01, max_iter=10000)
ridge_reg.fit(x, np.ravel(y))
print(ridge_reg.predict([[1.5]]))
print(ridge_reg.intercept_)
print(ridge_reg.coef_)