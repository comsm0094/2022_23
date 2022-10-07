import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import math

# f-dot = (f^2-1)

#f = 1+Ae^(2t) / (1-Ae^(2t)) where A =- (1-f0)/(1+f0)


def df(f):
    df=pow(f,2)-1
    return df

def soln(t,f0):
    bigA=(f0-1)/(1+f0)

    exp2t=math.exp(2*t)
    return (1+bigA*exp2t)/(1-bigA*exp2t)

delta_t=0.1

t0=0.0
t1=1.0

f0=0.9

t=t0
f=f0

f_v=[f0]
t_v=[t0]

soln_v=[f0]

while t<t1:
    t+=delta_t
    f+=delta_t*df(f)
    t_v.append(t)
    f_v.append(f)
    soln_v.append(soln(t,f0))
    
plt.plot(t_v,f_v)
plt.plot(t_v,soln_v)
fig = plt.gcf()
fig.set_size_inches(1.5, 1.5)
fig.savefig('test2png.png', dpi=100)

plt.savefig("example.png")
plt.show()
