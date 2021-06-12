from skimage import color

import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = plt.imread('helmet_mkv_0000000000.jpg')
img2 = plt.imread('helmet_mkv_0000000004.jpg')
frame1 = color.rgb2gray(img1)
frame2 = color.rgb2gray(img2)

fft1 = np.fft.fft2(frame1)
fft2 = np.fft.fft2(frame2)
amp1 = np.abs(fft1)
amp2 = np.abs(fft2)
phase1 = np.angle(fft1)
phase2 = np.angle(fft2)

m_map1 = np.abs(np.fft.ifft2((amp2-amp1) * np.exp(1j * phase1)));
m_map2 = np.abs(np.fft.ifft2((amp2-amp1) * np.exp(1j * phase2)));
m_map = m_map1 * m_map2


fig, ax = plt.subplots(2, 2)
ax[0, 0].imshow(img1)
ax[0, 1].imshow(img2)
ax[1, 0].imshow(m_map1)
ax[1, 1].imshow(m_map2)

fig, ax = plt.subplots()
im = ax.imshow(m_map, cmap='gray')
fig.colorbar(im)
plt.show()