
#this is the example I did in the lecture, de.py is one I had made earlier mostly to check I knew how to plot the soln.

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import math

# df/dt = f^2-1
#f = 1+Ae^(2t) / (1-Ae^(2t)) where A =- (1-f0)/(1+f0)

def dfdt(f):
    return pow(f,2)-1

class Soln:
    def __init__(self,f0):
        self.big_a=(f0-1)/(1+f0)

    def __call__(self,t):
        exp2t=math.exp(2*t)
        return (1+self.big_a*exp2t)/(1-self.big_a*exp2t) 

t0=0.0
t1=5.0

f0=0.9

delta_t=0.01

t=t0
f=f0

t_vector=[t0]
f_vector=[f0]
soln_vector=[f0]

soln=Soln(f0)
print(soln.big_a)

while t<t1:

    t+=delta_t
    f+=dfdt(f)*delta_t
    
    t_vector.append(t)
    f_vector.append(f)
    soln_vector.append(soln(t))
    
    
plt.plot(t_vector,f_vector)
plt.plot(t_vector,soln_vector)
plt.show()





