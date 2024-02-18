import numpy as np

B0 = 3.12e-5
Rearth = 6370e3
Mearth = 5.97e24

protonE1 = 100e6 * 1.6e-19
protonE2 = 200e6 * 1.6e-19

electronE1 = 1e6 * 1.6e-19
electronE2 = 0.1e6 * 1.6e-19

protonMass = 1.67e-27
electronMass = protonMass / 1836

e = 1.6e-19
G = 6.67e-11

protonV1 = np.sqrt((2*protonE1) / protonMass)
protonV2 = np.sqrt((2*protonE2) / protonMass)

electronV1 = np.sqrt((2*electronE1) / electronMass)
electronV2 = np.sqrt((2*electronE2) / electronMass)

pE1 = [protonMass, protonE1, protonV1]
pE2 = [protonMass, protonE2, protonV2]
eE1 = [electronMass, electronE1, electronV1]
eE2 = [electronMass, electronE2, electronV2]
lower_bounds = [1.2*Rearth, 4*Rearth]
upper_bounds = [3*Rearth, 11*Rearth] 


poss = [pE1, pE2, eE1, eE2]
poss_2 = [pE1, pE2, eE1, eE2, lower_bounds, upper_bounds]

B1 = [
       [protonE1, electronE1],
      [protonMass, electronMass]
      ]

B2 = [
       [protonE2, electronE2],
       [protonMass, electronMass]
]

for i in range(0, len(poss)):
       A = poss[i][0]*(poss[i][2]**2)
       B = -G*Mearth*poss[i][0]
       C = -B0*(Rearth**3)*e*poss[i][2]
       print(np.roots([A,B,C])/Rearth)


#-------------------------------------
       
def MagneticFieldStrength(Lower_Radius, Upper_Radius):
       lower =  B0 * (Rearth**3) / (Lower_Radius**3)      
       higher = B0 * (Rearth**3) / (Upper_Radius**3)   
       return [lower, higher]


def LarmorRadius(Energy, Mass, Lower_Radius, Upper_Radius):
       lower = (np.sqrt(2*Energy*Mass)*(Lower_Radius**3))/(B0*(Rearth**3)*e)
       upper = (np.sqrt(2*Energy*Mass)*(Upper_Radius**3))/(B0*(Rearth**3)*e) 
       return [lower/Rearth, upper/Rearth]

# First compute inner belt
print("----------------------------------------------------- \n Inner Belt:")

for i in range(0, len(B1)):
       print(LarmorRadius(B1[0][i], B1[1][i], lower_bounds[0], upper_bounds[0]))

# Then compute outer belt
print("--------------------------------------------------- \n Outer Belt:")
for i in range(0, len(B2)):
       print(LarmorRadius(B2[0][i], B2[1][i], lower_bounds[0], upper_bounds[0]))













    
