import serial, sys
import re
from pylab import *

strPort = sys.argv[2]   # serial port
ser=serial.Serial(strPort, 115200)
print("connected to: " + ser.portstr)

file=sys.argv[1]  # file name
regex = re.compile('\d+')  # for extracting number from strings
f=open(file,"w+")
y=[0]*100
data=[];itime=0
while True:
  try:
    itime=0
    line = ser.readline()
    match = regex.findall(str(line))   # extracting number from strings
    # "match[4]+"."+match[5]" is the first Tc value, ..., "match[22]+"."+match[23]" is the tenth Tc value.
    f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
    # match[1] is minutes, match[2] is seconds, match[3] is sub seconds.
    sec=float(match[1])*60.0+float(match[2])+float(match[3])*0.1
    data.append(itime*0.1)    # set time and temps to data
    data.append(float(match[4]+"."+match[5]))
    data.append(float(match[6]+"."+match[7]))
    data.append(float(match[8]+"."+match[9]))
    data.append(float(match[10]+"."+match[11]))
    data.append(float(match[12]+"."+match[13]))
    data.append(float(match[14]+"."+match[15]))
    data.append(float(match[16]+"."+match[17]))
    data.append(float(match[18]+"."+match[19]))
    data.append(float(match[20]+"."+match[21]))
    data.append(float(match[22]+"."+match[23]))
    if(match[3]=="0"):
      print(str(sec)+":"+f1)
    f.write(str(sec)+", "+f1+"\n")
    x=range(0, 100, 1)
    y.insert(0, data[1])
    y.pop(100)
    clf()
    ylim(0, 200)
    plot(x, y)
    pause(0.05)
    itime=itime+1
  except KeyboardInterrupt:
    print ('exiting')
    break
ser.flush()
ser.close()
f.close()