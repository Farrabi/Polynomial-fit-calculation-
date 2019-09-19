import numpy as np
import matplotlib.pyplot as plt

#REAL

data_r = np.genfromtxt("GeTe amo diel fct real.txt")
wavelength_r = np.array(data_r[:,][:,0])
Real = np.array(data_r[:,][:,1])
poly_fit_r = np.poly1d(np.polyfit(wavelength_r,Real, 16))




plt.plot(wavelength_r, Real, 'r')
plt.plot(wavelength_r, poly_fit_r(wavelength_r), 'b')
plt.show()

#IMAGINARY

data_i = np.genfromtxt("GeTe amo Im diel fct.txt")
wavelength_i = np.array(data_i[:,][:,0])
Im = np.array(data_i[:,][:,1])
poly_fit_i = np.poly1d(np.polyfit(wavelength_i,Im, 16))



plt.plot(wavelength_i, Im, 'r')
plt.plot(wavelength_i, poly_fit_i(wavelength_i), 'b')
plt.show()

print('wavelength')
for i in wavelength_r:
 print(i)
print('données_real')
for j in poly_fit_r(wavelength_r):
 print(j)
print('données_Im')
for k in poly_fit_i(wavelength_r):
 print(k)


with open("results.csv","w"
print(poly_fit(wavelength))

data = (np.array([wavelength, poly_fit(wavelength)]).transpose())

for i in wavelength:

print(i)

for j in poly_fit_r(wavelength):

print(j)

for k in poly_fit_i(wavelength):

print(k)






 
