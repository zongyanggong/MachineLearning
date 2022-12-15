import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import SGDRegressor

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

lasso_reg = Lasso(alpha=0.01, max_iter=10000)
lasso_reg.fit(x, y)
print(lasso_reg.predict([[1.5]]))
print(lasso_reg.intercept_)
print(lasso_reg.coef_)

print('-' * 45)
lasso_reg = SGDRegressor(penalty='l1', alpha=0.01, max_iter=10000)
lasso_reg.fit(x, y)
print(lasso_reg.predict([[1.5]]))
print(lasso_reg.intercept_)
print(lasso_reg.coef_)