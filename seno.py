import numpy as np
import matplotlib.pyplot as plt
def g(t):
  return 2*np.sin(t)+2015
t2 = np.arange(0, 10, 0.1)
plt.title('Nestor Raul')
plt.figure(1)
plt.plot(t2, g(t2), 'b')
plt.savefig('sin.png')
