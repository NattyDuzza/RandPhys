import numpy as np

B0 = 3.12e-5
Rearth = 6370e3
Mearth = 5.97e24

protonE1 = 100e6 * 1.6e-19
protonMass = 1.67e-27

e = 1.6e-19
G = 6.67e-11

protonV1 = np.sqrt((2*protonE1) / protonMass)

A = protonMass * (protonV1**2)
B = -G*Mearth*protonMass
C = -B0*(Rearth**3)*e*protonV1

print(np.roots([A, B, C]) / Rearth)
