import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,4,9,16,25,36,1])
plt.show()

plt.plot([7,8,9,10,11,12,13,14,15,16,17,18],[10,10,10,30,20,25,30,35,70,75,80,10], label='Vandaag')
plt.grid(True)
plt.title('Titelding.')
plt.xlabel('Tijd')
plt.ylabel('CPU load (%)')
plt.legend(loc='upper left') # best / upper/lower/left/right
plt.axis([7,18,0,100])
plt.annotate('Wat gebeurt hier?', xy=(17,80), xytext=(12,90),arrowprops=dict(facecolor='black'))
plt.show()