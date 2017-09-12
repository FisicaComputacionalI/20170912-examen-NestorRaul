import numpy as np
import matplotlib.pyplot as plt
def f(s):
  return s+1997
def g(t):
  return 2*np.sin(t)+2015
s1 = np.arange(0, 20, 0.1)
t1 = np.arange(0, 20, 0.1)
plt.figure(1)
plt.subplot(211)
plt.title('FINAL')
plt.plot(s1, f(t1), 'b', t1, g(t1), 'k')
plt.subplot(212)
plt.plot(t1, g(t1))
plt.savefig('Final.png')
