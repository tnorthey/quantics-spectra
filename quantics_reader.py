def read_gwpcentres(Nstate,istate):
  ##################################################
  # read_gwpcentres: Read displacement factors from file 'gwpcentres' for state 'istate'.
  # Inputs: 	Nstate (int), the total number of states
  #		istate (int), the state to read
  # Outputs:	Time (float list), list of time in atomic units 
  # 		v (float array), displacement factors array with columns 0,1,...,Nmode-1 pertaining to modes 1,2,...,Nmode, rows correspond to Ng Gaussians
  ##################################################
  Time=[]; v=[]; c=0; x=0
  with open('inputs/gwpcentres','r') as f:
    for line in f:
      c+=1
      if c==1:					# Line 1 contains Nmode and Ng
        Nmode=int(line.split()[1])			# Number of modes
        for i in range(Nmode):
          v.append([])
        Ng=int(line.split()[2])			# Number of Gaussians
        rep=Nstate*(Ng+1)+1				# gwpcentres repeats every Nstate*(Ng+1)+1 lines
        print("There are Nmode = " + str(Nmode) + " modes in gwpcentres")
        print("There are Ng = " + str(Ng) + " Gaussians in gwpcentres")
     
      elif c>1:					# Lines >1 have time and displacement factors
        if (c-2)%rep==0:				# Repetition every 'rep' lines
          #print "t lines: " + line
          Time.append(float(line.split()[1]))	# List of time in atomic units
        elif (c-x-4-(istate-1)*(Ng+1))%rep==0:	# This fits the formatting of the gwpcentres file
          #print "v lines: " + line
          for imode in range(Nmode):
             v[imode-1].append(float(line.split()[imode-1]))
          x+=1					# counter causes Ng lines to be appended (which is what we want)
          if x==Ng:				# stop appending after Ng lines
            x=0					# reset counter 
  # Checks
  Nt = len(Time)
  print("There are Nt = " + str(Nt) + " total time-steps")
  print("Displacement factor array has " + str(len(v[0])) + " rows")
  if len(v[0])==Nt*Ng:
    print("There are Nt*Ng = " + str(Nt*Ng) + " rows of displacement factors, as there should be.")
  else:
    print("Error: There are " + str(Nt*Ng) +  " =/= Nt*Ng rows of displacement factors! Exiting...")
    return
  ##################################################
  return Nmode,Ng,Time,v 

def read_output(fname,Nstate,Ng):
   ##################################################
   # read_output: Read Gaussian weights (and state weights) from file 'output' for state 'istate'.
   # Inputs: 	Nstate (int), total number of states
   # 	 	Ng (int), total number of Gaussians
   # Outputs:	Time (float list), list of time in fs 
   # 		gWeights (float array), Gaussian populations with columns 0,1,...,Ng-1 pertaining to Gaussians 1,2,...,Ng
   ##################################################
   Time=[]; gWeights=[]
   X=0; c=0; j=0
   for i in range(Ng):
      gWeights.append([])
   with open(fname,'r') as f:
      for line in f:
         if line[1:5]=='Time':
            Time.append(float(line.split()[2]))
         elif line[1:len('Gross Gaussian Populations')+1]=='Gross Gaussian Populations':
            if Nstate>1:
               istate = int(line.split()[7])			# state number = 1,2,...
            X=(Ng-1)/7+1					# Causes the next X lines to be read in the following elif block
         elif X>0:
            c+=1						# Line counter for Gaussian populations part
            for i in range(7):
               j+=1
               string=line.split()[3:]
	       #gWeights[i+7*(c-1)].append(float(string.split()[i]))
               gWeights[i+7*(c-1)].append(float(string[i]))
               if j==Ng:					# break after Ng floats have been appended to gWeights
                  break
            if c==X:
               X=0; c=0; j=0					# reset counters
	       # print "X reset to 0"	
	 #else:	
	 #   print "Line not read."
   # Checks
   ##################################################
   return Time,gWeights

def read_ddtraj(fname):
   ##################################################
   # read_ddtraj:  Reads ddtraj file 'fname' (usually ddtraj.pl)
   # Inputs:    fname, the file name of the ddtraj file to read
   # Outputs:   AtomList (string list), list of atomic labels; 
   #            Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...
   ##################################################
   import re            # import regular expression
   pattern = re.compile("    \d          ")   # pattern to match
   with open(fname,'r') as f: # open file   
      AtomList=[]; Coords=[]
      for line in f:
         if pattern.match(line):
            #print line
            AtomList.append(line.split()[1])    # List of atomic labels
            for i in range(3,6):
                Coords.append(float(line.split()[i]))

   ##################################################dd
   return AtomList,Coords


