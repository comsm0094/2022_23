from math import *


class Leaky:
    
    def __init__(self,tau,delta_t,v_0):
        self.v=v_0
        self.tau=tau
        self.delta_t=delta_t

    def update(self,input):
        self.v=(self.v-input)*exp(-self.delta_t/self.tau)+input
        return self.v


delta_t= 0.01
tau1=2

v0=0.75

leaky=Leaky(tau1,delta_t,v0)


freq=0.2

t=0
big_t=20

while t<big_t:
    input=0.25
    if sin(2*pi*freq*t)>0:
        input = 1.25
    v=leaky.update(input)
    print(t,v,input)
    t+=delta_t

