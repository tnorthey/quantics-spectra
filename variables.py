
# Number of geometries to generate
N = 1

# switch on (1) or off (0) random displacements
randm = 0

# if randm is on the random displacement will be in range [-a,a], if randm is off it will displace by exactly a
a = [2,-1]

# frequencies (cm-1) of selected modes
freqcm1 = [1722.4496, 3799.4476, 3925.0128] 

# selected modes
Modes = [1,2]
#nmodes = 2
nmodes = len(Modes)
#Modes = list(range(1, nmodes + 1 ))  # all modes


Ng = 10
Nstate = 2
Nt = 100

 #C    -0.696126    -1.136419     0.000000
 #C     0.696126    -1.136419     0.000000
 #N    -1.417532     0.000000     0.000000
 #N     1.417532     0.000000     0.000000
 #C     0.696126     1.136419     0.000000
 #C    -0.696126     1.136419     0.000000
 #H     1.250625     2.067160     0.000000
 #H    -1.250625     2.067160     0.000000
 #H     1.250625    -2.067160     0.000000
 #H    -1.250625    -2.067160     0.000000
mi = [12.011,12.011,12.011,
      12.011,12.011,12.011,
      14.007,14.007,14.007,
      14.007,14.007,14.007,
      12.001,12.001,12.001,
      12.001,12.001,12.001,
      1.008,1.008,1.008,
      1.008,1.008,1.008,
      1.008,1.008,1.008,
      1.008,1.008,1.008]

# frequencies (cm-1) of modes 11,3,14,8                          
freqcm1 = [1029.3835, 594.2562, 1261.8246, 913.7712]

