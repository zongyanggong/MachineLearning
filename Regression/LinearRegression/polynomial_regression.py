import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



x = 6 * np.random.rand(100, 1) - 3
y = 2 + 1 * x + 0.5 * x ** 2 + np.random.randn(100, 1)

plt.plot(x, y, 'b.')


x_train = x[:80]
y_train = y[:80]
x_test = x[80:]
y_test = y[80:]

# degree=1 under fit 欠拟合
# degree=3 over fit 过拟合
# degree=2 just right
d = {1: 'g-', 2: 'r+', 3: 'y*'}
for i in d:
    poly_features = PolynomialFeatures(degree=i, include_bias=True)
    x_poly_train = poly_features.fit_transform(x_train)
    x_poly_test = poly_features.fit_transform(x_test)

    print('-' * 45)
    print('Degree: ', i)
    print(x_train[0])
    print(x_poly_train[0])
    print(x_train.shape)
    print(x_poly_train.shape)
    linear_reg = LinearRegression(fit_intercept=False)
    linear_reg.fit(x_poly_train, y_train)
    print(linear_reg.intercept_)
    print(linear_reg.coef_)

    y_train_predict = linear_reg.predict(x_poly_train)
    y_test_predict = linear_reg.predict(x_poly_test)
    plt.plot(x_poly_train[:,1], y_train_predict, d[i])

    print('train:', mean_squared_error(y_train, y_train_predict))
    print('test: ', mean_squared_error(y_test, y_test_predict))

plt.show()


