import numpy as np
import  matplotlib.pyplot as mt
file1 = open('settings.txt', 'r')
p = list(map(float, file1.read().split('\n')))
file1.close()
data_arr = np.loadtxt('data.txt', dtype=int)
data_arr = data_arr * (3.3 / 256)
data_x = np.array([float(x) for x in range(len(data_arr))])
data_x = p[0] * data_x
fig, ax = mt.subplots(figsize=(16, 10), dpi=150)
large = 22; med = 16; small = 12    
mt.title('Процесс заряда и разряда в цепочке')
mt.xlabel("Время, с")
mt.ylabel("Напряжение, В")
mt.grid()
ax.plot(data_x, data_arr, '-*g', label='v(t)', marker='x', markersize=3) 
ax.legend()
ax.text(8, 2, 'Время зарядки 5.13c')
ax.text(8, 1.5, f'Время разрядки {data_x[-1] - 5.13}c')
mt.savefig('figure.png')
mt.show()