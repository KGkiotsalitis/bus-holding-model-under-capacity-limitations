import numpy as np
import matplotlib.pyplot as plt
import random

zeta=300
M_2=100000000000
M_1=100000000000000
a_n_plus_1s=2500
ta=1.5
tb=4
l_n_1=50
beta_n_1=10
c_n_plus_1=60
c_n=60
Hs=600
lambda_s=0.02
phi_n=59
t=1500
di_1_s=1000


k=1+tb*lambda_s
h=(1+tb*lambda_s)*tb
theta=a_n_plus_1s+beta_n_1*ta+(beta_n_1*ta*lambda_s+(a_n_plus_1s-t)*lambda_s)*k*tb-t-Hs
x_analytic_solution=max(0,min(zeta,(c_n-phi_n)/lambda_s,((lambda_s*h+1)*theta-(t-di_1_s-Hs))/(1+(lambda_s*h+1)**2)))

'''
if t<di_1_s+Hs:
    if 0.5*((a_n_plus_1s+lambda_s*(a_n_plus_1s-t)*tb+beta_n_1*ta)-di_1_s)<Hs:
        x_analytic_solution=di_1_s+Hs-t
    else:
        x_analytic_solution=di_1_s+(0.5*((a_n_plus_1s+lambda_s*(a_n_plus_1s-t)*tb+beta_n_1*ta)-di_1_s)+Hs)*0.5-t
else:
    x_analytic_solution=0
print(x_analytic_solution)
'''

n_analytic_v_1=max(0,phi_n+x_analytic_solution*lambda_s-c_n)
n_analytic_v_2=max(0,l_n_1-beta_n_1-c_n_plus_1+(beta_n_1*ta*lambda_s+max(0,n_analytic_v_1)+(a_n_plus_1s-t-x_analytic_solution)*lambda_s)*k)
d_n_plus_1_s=a_n_plus_1s+beta_n_1*ta+(beta_n_1*ta*lambda_s+n_analytic_v_1+(a_n_plus_1s-t-x_analytic_solution)*lambda_s)*(1+tb*lambda_s)*tb-n_analytic_v_2*tb
Bigterm = ((lambda_s*h+1)*theta-(t-di_1_s-Hs))/(1+(lambda_s*h+1)**2)
busload_n_plus_1=l_n_1-beta_n_1+\
(beta_n_1*ta*lambda_s+max(0,phi_n+x_analytic_solution*lambda_s-c_n)+(a_n_plus_1s-(t+x_analytic_solution))*lambda_s)*(1+tb*lambda_s)

print('holding time:',x_analytic_solution)
print('departure time of trip n+1:',d_n_plus_1_s)
print('dispatching time of trip n:',t+x_analytic_solution)
print('bus load of trip n when departing from stop:',phi_n+x_analytic_solution*lambda_s)
print('headways:',t+x_analytic_solution-di_1_s,d_n_plus_1_s-t-x_analytic_solution)
print('headway squared deviation:',(t+x_analytic_solution-di_1_s-Hs)**2+\
      (d_n_plus_1_s-t-x_analytic_solution-Hs)**2)
print('in-vehicle passenger waiting times due to holding:',x_analytic_solution*(phi_n+x_analytic_solution*lambda_s))

out_of_veh_wait_time=(lambda_s*(t+x_analytic_solution-di_1_s) *  0.5*(t+x_analytic_solution-di_1_s) )
if phi_n+x_analytic_solution*lambda_s>c_n:
    out_of_veh_wait_time=out_of_veh_wait_time+(phi_n+x_analytic_solution*lambda_s-c_n)*(d_n_plus_1_s-t-x_analytic_solution)

out_of_veh_wait_time=out_of_veh_wait_time+(lambda_s*(d_n_plus_1_s-t-x_analytic_solution) * 0.5*(d_n_plus_1_s-t-x_analytic_solution))

print('out-of-vehicle passenger waiting times due to holding:',out_of_veh_wait_time)



