import numpy as np
import matplotlib.pyplot as plt


file_path = 'ornek_ev_1_lidar_export.xyz'
data = np.loadtxt(file_path)


x = data[:, 0]
y = data[:, 1]
z = data[:, 2]


x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)


scaled_x = ((x - x_min) / (x_max - x_min)) * 999
scaled_y = ((y - y_min) / (y_max - y_min)) * 999


image = np.zeros((1000, 1000, 3), dtype=np.uint8)


for i in range(len(scaled_x)):
    x_coord = int(np.clip(scaled_x[i], 0, 999))
    y_coord = int(np.clip(scaled_y[i], 0, 999))
    image[y_coord, x_coord] = [128, 128, 128]

plt.imshow(image)
plt.axis('off')
plt.show()
