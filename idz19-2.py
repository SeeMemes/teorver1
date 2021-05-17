import numpy as np
from termcolor import cprint
import matplotlib.pyplot as plt


##############################
#           LOGIC            #
##############################
def f(x):
    return y_mean + rxy + (oy / ox * (x - x_mean))


##############################
#     PROGRAM BEGINNING      #
##############################
x = np.array([10, 13, 16, 19, 22, 25])
y = np.array([110, 130, 150, 170, 190, 210, 230, 250])
mx = np.array([8, 16, 18, 30, 18, 10])
my = np.array([1, 8, 20, 28, 20, 7, 14, 2])

m = np.array([
    [1, 3, 4, 0, 0, 0, 0, 0],
    [0, 5, 6, 5, 0, 0, 0, 0],
    [0, 0, 4, 8, 6, 0, 0, 0],
    [0, 0, 6, 15, 9, 0, 0, 0],
    [0, 0, 0, 0, 5, 6, 7, 0],
    [0, 0, 0, 0, 0, 1, 7, 2]
])

n = mx.sum()

cprint('Контроль входных значений: ', 'blue')
sxmx = np.sum(x * mx)
symy = np.sum(y * my)
sxmy = symx = np.sum([x[i] * np.sum(m[i][j] * y[j]) for i in range(6) for j in range(8)])
s_control_y = np.sum([(m[i][j] * y[j]) for i in range(6) for j in range(8)])
s_control_x = np.sum([(m[i][j] * x[i]) for i in range(6) for j in range(8)])
sum_x_sum_my = np.sum(x * symy)
sum_y_sum_mx = np.sum(y * sxmx)
print(f'\tКонтроль S(mx) = ' + str(mx.sum()) + ' = S(my) = ' + str(my.sum()))
print(f'\tКонтроль S(x * mx) = ' + str(sxmx) + ' = ' + str(s_control_x) + '; S(y * my) = ' + str(symy) + ' = ' + str(
    s_control_y))

cprint('Выборочное среднее: ', 'blue')
x_mean = sxmx / 100
y_mean = symy / 100
print(f'\tВыборочное среднее x: {x_mean}, y: {y_mean}')

cprint('Вычисляем выборочные дисперсии: ', 'blue')
dx = round(((1 / (n - 1)) * (np.sum(mx * (x ** 2)) - (1 / n) * (np.sum(mx * x)) ** 2)) * 100) / 100
dy = round(((1 / (n - 1)) * (np.sum(my * (y ** 2)) - (1 / n) * (np.sum(my * y)) ** 2)) * 100) / 100
print(f'\tВыборочная дисперсия по x: {dx}, y: {dy}')

cprint('Корреляционный момент: ', 'blue')
sxy = round(((1 / (n - 1)) * (sxmy - (1 / n) * (sxmx * symy))) * 100) / 100
print(f'\tКорреляционный момент: {sxy}')
ox = round(np.sqrt(dx) * 100) / 100
oy = round(np.sqrt(dy) * 100) / 100
print(f'\tСреднеквадратическое отклонение: ox = {ox}, oy = {oy}')
rxy = sxy / (ox * oy)
print(f'\tКоэффициент r = {round(rxy * 100) / 100}')
plt.xlim((x.min() - 2, x.max() + 2))
plt.xticks(x)
plt.yticks(y)

cprint('Строим линии регрессии и случайные точки: ', 'blue')
plt.plot(np.linspace(x.min() - 4, x.max() + 4, 2), f(np.linspace(x.min() - 4, x.max() + 4, 2)))
for i in range(6):
    for j in range(8):
        if m[i][j]:
            plt.scatter(x[i], y[j], c='c')
plt.show()
print(f'\tУравнение имеет вид: y = {y_mean - x_mean * rxy * oy / ox:.2f} + '
      f'{rxy * oy / ox:.2f}x')
