# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:12:28 2023

@author: ASUS 
"""

import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Syarat agar filter bisa dijalnkan
order = 5
fs = 50.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Demonstrate the use of the filter.

# First make some data to be filtered.
T = 3.0         # Waktu berlangsung
n = int(T * fs) # Seberapa banyak sampel yang digunakan
t = np.linspace(0, T, n, endpoint=False)
# Hasil dari diatas dijadikan data non-filtered dengan perumusan dibawah
data = np.sin(1.2*2*np.pi*t) + np.cos(9*2*np.pi*t) + np.sin(12.0*2*np.pi*t)

# Filter data
y = butter_lowpass_filter(data, cutoff, fs, order)

#Menampilkan hasil filtering 
plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('waktu [sec]')
plt.grid()
plt.legend()
plt.subplots_adjust(hspace=0.5)
plt.show()