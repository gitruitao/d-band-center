# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:42:45 2019
Copyright: 24th August, Yaqiong Su, Eindhoven
@author: Yaqiong Su
"""
import numpy as np
from scipy.integrate import simps
import datetime
import time
import sys
# import pprint

######   timing   ######
start = time.time()
print ('********** d-band center from rwu **********')
### current time ###
start_time = datetime.datetime.now()
print ("Start time:       " + start_time.strftime('%Y.%m.%d-%H:%M:%S'))   #strftime可以自定义时间的输出格式

######   read DOS file from the output of split_dos script   ######
file = sys.argv[1] # pass paramter
#file = 'DOS16'  # the selected atom
energy = np.array([float(l.split()[0]) for l in open(file,'rb')])   # extract energy, 以二进制读模式打开
emin, emax = energy[0], 0.000  # integral energy range, 从最小值积分到费米能级
erange = (energy[0],energy[-1])
emask = (energy >= emin) & (energy <= emax) # bool to make a mapping between energy and dos
np.set_printoptions(threshold=np.inf)
# print(energy)


d_up_9 = np.array([float(l.split()[9]) for l in open(file,'rb')])   # extract d_up
d_up_11 = np.array([float(l.split()[11]) for l in open(file,'rb')])
d_up_13 = np.array([float(l.split()[13]) for l in open(file,'rb')])
d_up_15 = np.array([float(l.split()[15]) for l in open(file,'rb')])
d_up_17 = np.array([float(l.split()[17]) for l in open(file,'rb')])
d_up = d_up_9 + d_up_11 + d_up_13 + d_up_15 + d_up_17

d_down_10 = np.array([float(l.split()[10]) for l in open(file,'rb')])
d_down_12 = np.array([float(l.split()[12]) for l in open(file,'rb')])
d_down_14 = np.array([float(l.split()[14]) for l in open(file,'rb')])
d_down_16 = np.array([float(l.split()[16]) for l in open(file,'rb')])
d_down_18 = np.array([float(l.split()[18]) for l in open(file,'rb')])
d_down = d_down_10 + d_down_12 + d_down_14 + d_down_16 + d_down_18

d_total = d_up + d_down
# d_up = np.array([float(l.split()[5]) for l in open(file,'rb')])   # extract d_up
# d_down = np.array([float(l.split()[6]) for l in open(file,'rb')])   # extract d_down

x = energy[emask]
# print(x)
y1 = d_up[emask]
y2 = d_down[emask]
y3 = d_total[emask]

dbc_up   = simps(y1*x, x) / simps(y1, x)
dbc_down = simps(y2*x, x) / simps(y2, x)
dbc_total = simps(y3*x, x) / simps(y3, x)
dbc = []
dbc.append(dbc_up)
dbc.append(dbc_down)
dbc.append(dbc_total)
print ('dbc_up(eV), dbc_down(eV), dbc_total')
print (dbc)

##########   timing   #############
stop=time.time()
print("running time:     " + str(stop-start) + " seconds")
terminal_time = datetime.datetime.now()
print ("Terminal time:    " + terminal_time.strftime('%Y.%m.%d-%H:%M:%S'))   #strftime可以自定义时间的输出格式
print ('d-band center has been obtained')
print ('********** d-band center from rwu **********')
