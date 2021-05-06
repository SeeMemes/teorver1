import math
import numpy as np
import matplotlib.pyplot as plt
from termcolor import cprint
import scipy.stats as st
from tabulate import tabulate


##############################
#           LOGIC            #
##############################

def exp_value(mass):
    k = 0
    for i in range(len(mass)):
        k += mass[i]
    k /= len(mass)
    return k


def standard_deviation(mass):
    xi = exp_value(mass)
    k = 0
    for i in range(len(mass)):
        k += (xi - mass[i]) ** 2
    k /= len(mass)
    k **= 1 / 2
    return k


def empirical_mass(prev):
    new_mass = []
    sum = 0
    print('\tif x < ' + str(prev[0]) + ' then ' + ' f(x) = ' + str(sum))
    k = 1
    for i in range(len(prev) - 1):
        if (prev[i] == prev[i - 1]):
            k += 1
            continue
        else:
            new_mass.append(k / len(prev))
            sum += k / len(prev)
            k = 1
            print('\tif ' + str(prev[i]) + ' < x < ' + str(prev[i + 1]) + ' then f(x) = ' + str(round(sum*100)/100))
    new_mass.append(k / len(prev))
    sum += k / len(prev)
    print('\tif x > ' + str(prev[len(prev)-1]) + ' then ' + ' f(x) = ' + str(round(sum*100)/100))

    return new_mass

def remove_dupes(prev):
    prev = list(dict.fromkeys(prev))
    return prev

def plot_empirical_cdf(sample):
    plt.hist(sample, histtype='step', cumulative=True, bins=len(sample) * 10)
    plt.title('График эмперической функции распределения')
    plt.show()


##############################
#     PROGRAM BEGINNING      #
##############################

mass = [-0.26, -0.58, 1.49, -0.84, -1.54, 1.13, -1.33, -0.78, -1.68, -0.94, \
        -1.55, 1.54, 0.34, 0.58, -0.84, -1.58, -1.72, -0.49, 0.34, -0.14]
mass.sort()
cprint('Вариационный ряд: ', 'green')
print('\t' + str(mass))
cprint('Экстремумы и размах: ', 'green')
print('\tМинимум: ' + str(mass[0]) + '\tМаксимум: ' + str(mass[19]))
print('\tРазмах: ' + str(mass[19] - mass[0]))
cprint('Мат. ожидание и среднеквадрат. отклонение: ', 'green')
print('\tМатематическое ожидание: ' + str(exp_value(mass)) + '\n\tСреднеквадратическое отклонение: ' \
      + str(standard_deviation(mass)))
cprint('Эмперическая функция распределения: ', 'green')
e_mass = empirical_mass(mass)
plot_empirical_cdf(mass)
nodupe = remove_dupes(mass)
plt.plot(e_mass)
plt.title('Полигон частот групированной выборки')
plt.show()
plt.bar(nodupe, width=0.2, height=e_mass)
st.gaussian_kde(nodupe)
plt.title('Гистограмма частот групированной выборки')
plt.show()
