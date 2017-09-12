import numpy as np
import matplotlib.pyplot as plt
def g(t):
  return t+1997
t1 = np.arange(0, 21.0, 1)
plt.title('Nestor Raul')
plt.ylabel('Anio')
plt.xlabel('Edad')
plt.figure(1)
plt.plot(t1, g(t1), 'b')
plt.savefig('Edad.png')
plt.show()

