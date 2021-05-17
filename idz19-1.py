import math
from numpy import genfromtxt
import matplotlib.pyplot as plt
from termcolor import cprint
from tabulate import tabulate
import scipy.stats as st


def parse():
    a = genfromtxt("19-1.csv", delimiter=' ')
    return a


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
            print('\tif ' + str(prev[i]) + ' < x < ' + str(prev[i + 1]) + \
                  ' then f(x) = ' + str(round(sum * 100) / 100) + \
                  ' and the middle is ' + str(round(prev[i] - prev[i + 1])))
    new_mass.append(k / len(prev))
    sum += k / len(prev)
    print('\tif x > ' + str(prev[len(prev) - 1]) + ' then ' + ' f(x) = ' + str(round(sum * 100) / 100))

    return new_mass


def remove_dupes(prev):
    prev = list(dict.fromkeys(prev))
    return prev


def plot_empirical_cdf(sample):
    plt.hist(sample, histtype='step', cumulative=True, bins=len(sample) * 10)
    plt.title('График эмперической функции распределения')
    plt.show()


def line(y1, y2, x1, x2, x):
    if (x2 - x1 != 0):
        k = (y2 - y1) / (x2 - x1)
        return k * (x - x1) / y1
    else:
        return x1


def mass_get(num, h):
    mass = [[], []]
    j = h / 2
    k = 0
    for i in range(1, len(num)):
        if (i == len(num) - 1):
            k += 2
            j -= num[i] - num[i - 1]
            mass[0].append(mass[0][len(mass[0]) - 1] + h)
            mass[1].append(k)
        elif ((j - (num[i] - num[i - 1])) >= 0):
            k += 1
            j -= (num[i] - num[i - 1])
        else:
            k += 1
            j -= num[i] - num[i - 1]
            if len(mass[0]) == 0:
                mass[0].append(num[i] + j - h / 2)
            else:
                mass[0].append(mass[0][len(mass[0]) - 1] + h)
            mass[1].append(k)
            k = 0
            j = h
    return mass


##############################
#     PROGRAM BEGINNING      #
##############################

mass = parse()
mass.sort()
cprint('a) Вариационный ряд: ', 'green')
print('\t' + str(mass))

cprint('б) Экстремумы и размах: ', 'green')
w = mass[len(mass) - 1] - mass[0]
print('\tРазмах: ' + str(w))
h = w / 9
j = 0
mass_F = []
mass_x = []
left = []
right = []
for i in range(9):
    a = mass[j]
    k = 0
    while mass[j + k] <= a + h:
        if (j + k <= 98):
            k += 1
        else:
            break
    print("\t" + str(i + 1) + ". " + str(a) + " - " + str(mass[j + k]) + \
          " | " + str(a + (h / 2)) + " | " + str(k) + " | " + str(k / len(mass)) + \
          " | " + str((k / len(mass)) / h))
    mass_F.append(k / len(mass))
    mass_x.append(a + (h / 2))
    left.append(a)
    right.append(mass[j + k])
    j += k

mass_emp = []
mass_emp.append(0)
for i in range(1, 9):
    mass_emp.append(mass_emp[i - 1] + mass_F[i])
plt.plot(mass_x, mass_F)
plt.title('в.1) Полигон частот групированной выборки')
plt.show()

plt.bar(mass_x, width=h, height=mass_F)
st.gaussian_kde(mass_x)
plt.title('в.2) Гистограмма частот групированной выборки')
plt.show()

plt.plot(mass_x, mass_emp)
plt.title('в.3) График эмперической функции')
plt.show()

cprint('г) Выборочное среднее и выборочная дисперсия: ', 'green')

k = 0
for i in range(len(mass)):
    k += (mass[i])
mid = k / len(mass)
print('\tВыборочное среднее: ' + str(mid))
k = 0
for i in range(len(mass)):
    k += pow(mass[i] - mid, 2)
db = k / len(mass) - mid ** 2
print()
