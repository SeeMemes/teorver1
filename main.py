import math
import matplotlib.pyplot as plt
from termcolor import cprint
import scipy.stats as st


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
        if (i==len(num)-1):
            k += 2
            j -= num[i] - num[i - 1]
            mass[0].append(mass[0][len(mass[0])-1]+h)
            mass[1].append(k)
        elif ((j - (num[i] - num[i - 1])) >= 0):
            k += 1
            j -= (num[i] - num[i - 1])
        else:
            k += 1
            j -= num[i] - num[i - 1]
            if len(mass[0]) == 0:
                mass[0].append(num[i] + j - h/2)
            else:
                mass[0].append(mass[0][len(mass[0]) - 1] + h)
            mass[1].append(k)
            k = 0
            j = h
    return mass

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

cprint('Величина интервала: ', 'green')
h = (nodupe[len(nodupe) - 1] - nodupe[0]) / (1 + math.log(len(mass), 2))

massive = mass_get(nodupe, h)

mass_x = massive[0]
mass_n = massive[1]
mass_p = []
for i in range (len(mass_n)):
    mass_p.append(mass_n[i]/len(nodupe))

print('\t' + str(h))
plt.plot(mass_x, mass_p)
plt.title('Полигон частот групированной выборки')
plt.show()
plt.bar(mass_x, width=h, height=mass_p)
st.gaussian_kde(nodupe)
plt.title('Гистограмма частот групированной выборки')
plt.show()
