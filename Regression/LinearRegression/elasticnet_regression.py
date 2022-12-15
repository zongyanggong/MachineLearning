import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

elastic_reg = ElasticNet(alpha=0.01, l1_ratio=0.15)
elastic_reg.fit(x, y)
print(elastic_reg.predict([[1.5]]))
print(elastic_reg.intercept_)
print(elastic_reg.coef_)

print('*' * 45)
elastic_reg = SGDRegressor(penalty='elasticnet', alpha=0.01, l1_ratio=0.15)
elastic_reg.fit(x, y.reshape(-1,))
print(elastic_reg.predict([[1.5]]))
print(elastic_reg.intercept_)
print(elastic_reg.coef_)
