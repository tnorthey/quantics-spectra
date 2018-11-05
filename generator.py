def generator_(tstep,istate,Nstate,Modes,xyzfile):
   ##################################################
   # generator_: Generates xyz files (with the spectral weighting in the comment line) for all Gaussians for time-step 'tstep' and state 'istate'   
   # Inputs:    tstep (int), time-step number (0,1,2,...)
   #            istate (int), electronic state (1,2,...)
   # 		Nstate (int), total number of states
   # 		Modes (int array), normal mode numbers e.g. [11,3,14,8]
   # 		xyzfile (str), path of xyz file containing initial coordinates (usually the equilibrium geometry)
   ##################################################

   from rw_xyz import *
   from quantics_reader import *
   from displace_coords import *
   from variables import *

   fname='inputs/output'

   AtomList,R0,comment = read_xyz(xyzfile)
   Nmode,Ng,Timeau,v = read_gwpcentres(Nstate,istate)
   Timefs,gWeights = read_output(fname,Nstate,Ng)   # Read time-steps (fs), and Gaussian weights      
   #au2ang = 0.52918
   
   print 'generator_: Generating xyz files for t = ' + str(Timefs[tstep]) + ' (fs)'
   
   ####################################################
   
   for j in range(Ng):			# Loop over Gaussians
      D=R0						# Starting coordinates
      # gWeights[column][row] = gWeights[Gaussian index][time-step 1: state 1, state 2, ...; time-step 2: state 1, state 2, ...; ...]
      A = gWeights[j][istate-1+Nstate*tstep]     
      for i in range(len(Modes)):			# Loop over modes
         imode=Modes[i]				# Mode number
         # v[column][row] = v[mode index][Gaussian index]
         Factor = v[i][Ng*tstep+j]*(0.172*(freqcm1[i])**.5)**-1	# Displacement factor 
         # print Factor
         D = displace_coords(D,imode,Factor)	# Displace coordinates along mode 'imode' by 'Factor'
      #if A>1e-2:				# Only write xyz file if weighting coeff. is non-negligible  
      fname='xyz/state' + str("%02d" % istate) + 'tstep' + str("%03d" % tstep) + 'g' + str("%02d" % (j+1))  + '.xyz'	# Output file name
      comment=str(A)
      write_xyz(AtomList,D,fname,comment)	# write to xyz
   ####################################################
   return

