import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

y0 = [0, 0]
t = np.linspace(0, 10, num=5000)


lambda_1 = 10
gama_1 = 1
lambda_2 = 100
gama_2 = 2

n = 1
c = 1

# n ve c sabit değerlerdir. Hill fonksiyonu tanımlanmasında katsayı olarak kullanılır.
# lambda_1 değişkeni bu modelde kullanılan Gen 1'in ifade edilme oranını gösterir.
# lambda_2 değişkeni bu modelde kullanılan Gen 2'nin ifade edilebileceği maksimum oranı gösterir.
# gama_1 değişkeni bu modelde kullanılan Gen 1'in bozunma oranını gösterir.
# lambda_1 değişkeni bu modelde kullanılan Gen 2'nin bozunma oranını gösterir.

parametreler = [lambda_1, gama_1, lambda_2, gama_2, n, c]


def simulasyon(variables, t, parametreler):
    gen1_ifade = variables[0]
    gen2_ifade = variables[1]

    lambda_1 = parametreler[0]
    gama_1 = parametreler[1]
    lambda_2 = parametreler[2]
    gama_2 = parametreler[3]
    n = parametreler[4]
    c = parametreler[5]

    dg1dt = lambda_1 - gama_1 * gen1_ifade

    dg2dt = (c ** n / (c ** n + gen1_ifade ** n)) * lambda_2 - gama_2 * gen2_ifade

    return [dg1dt, dg2dt]


y = odeint(simulasyon, y0, t, args=(parametreler,))

f, ax = plt.subplots(1)

line1, = ax.plot(t, y[:, 0], color="r", label="Gen 1 ifade oranı")
line2, = ax.plot(t, y[:, 1], color="b", label="Gen 2 ifade oranı")

ax.set_ylabel('İfade Oranı')
ax.set_xlabel('Birim Zaman')

ax.legend(handles=[line1, line2])

plt.show()
