import Shadow
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

x = in_object_1._beam.getshonecol(1)
z = in_object_1._beam.getshonecol(3)
xp = in_object_1._beam.getshonecol(4)
zp = in_object_1._beam.getshonecol(6)


amp = np.sqrt(xp**2+zp**2)
dir = np.arctan2(xp,zp)

from tkinter import messagebox
#messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
#if len(x)>1000:
#messagebox.showinfo("Title", "a Tk MessageBox")    


Nx = 101
Nz = 101
x_lin = np.linspace(np.min(x), np.max(x), Nx)
z_lin = np.linspace(np.min(z), np.max(z), Nx)
X, Z = np.meshgrid(x_lin,z_lin)
wfe = interpolate.griddata((x,z),amp,(X,Z),method='linear')

plt.imshow(wfe)
plt.show()