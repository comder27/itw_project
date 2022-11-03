from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time

fs=44100
aud=read("audio3.wav")[1]               #convert audio into array
runner=True
e=1.0                                   #amplification/attenuation factor
a=1                                     #speed up factor
a_s=0                                   #slow down factor
f=1                                     #flipping factor (1 or -1)
d=0                                     #delay factor
sd.play(aud,fs)
#input from user
while runner:
    print("1. Amplification")
    print("2. Attenuation")
    print("3. Speed up")
    print("4. Slow down")
    print("5. Flip")
    print("6. Delay")
    print("7. Play/Plot/Exit")
    menu = input("Enter your choice: ")
    menu=int(menu)
    if menu == 1:
        e = float(input("Enter amplification/atenuation factor: "))
    elif menu == 2:
        e = float(input("Enter amplification/atenuation factor: "))
    elif menu == 3:
        a = int(input("Enter speed up factor: "))
    elif menu == 4:
        a_s = int(input("Enter slow down factor: "))
    elif menu == 5:
        f = -1
    elif menu == 6:
        d = int(input("Enter delay: "))
    elif menu == 7:
        runner = False
    else:
        runner = False
data1=np.array([])                      #declaring empty array

#flipping sound
if(f==-1):
    data1=np.flipud(aud)
else:
    data1=aud

size=np.size(data1)                     #declaring size of audio array
fin=np.array([])
if(a_s==0):
    z=np.zeros((1, d*fs))[0]            #declaring array of zeroes
    r=np.append(z,data1[0:size-1:a])    #appending zeroes to original sound
    fin=e*r                             #final sound
else:
    z2=np.zeros((1,a_s*size))[0]         #declaring array of zeroes
    size2=np.size(z2)
    i=a_s
    j=0
    
    #slowing the sound
    while i<=size2-1:
        z2[i]=data1[j]
        i+=a_s
        j+=1
    z=np.zeros((1, d*fs))[0]
    r=np.append(z,z2)
    fin=e*r
plt.subplot(2,1,1)
plt.plot(aud)
plt.title('Original Sound Signal')
plt.subplot(2,1,2)
plt.plot(fin)
plt.title('Modified Sound Signal')
plt.show()
sd.play(fin,fs)
time.sleep(np.size(fin)//fs)

