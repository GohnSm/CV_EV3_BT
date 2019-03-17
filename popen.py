import os
m=[2,3,4,17,27,22,14,15,18,23,24]
for n in m:
    os.system('echo '+str(n)+' > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio'+str(n)+'/direction')