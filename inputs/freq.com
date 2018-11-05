%mem=1000MB
%NProcShared=4
#P MP2 6-31G** Freq=HPModes pop=full gfinput 


0 1
 C
 C,1,cc2
 N,1,nc3,2,ncc3
 N,2,nc4,1,ncc4,3,dih4,0
 C,4,cn5,2,cnc5,1,dih5,0
 C,3,cn6,1,cnc6,2,dih6,0
 H,5,hc7,6,hcc7,3,dih7,0
 H,6,hc8,3,hcn8,1,dih8,0
 H,2,hc9,4,hcn9,5,dih9,0
 H,1,hc10,3,hcn10,6,dih10,0
      Variables:
 cc2=1.39513903
 nc3=1.34474977
 ncc3=122.36847125
 nc4=1.34478587
 ncc4=122.36763957
 dih4=0.
 cn5=1.34357055
 cnc5=115.2580225
 dih5=0.
 cn6=1.34380336
 cnc6=115.25043097
 dih6=0.
 hc7=1.08354524
 hcc7=120.82424778
 dih7=180.
 hc8=1.08353503
 hcn8=116.78008727
 dih8=180.
 hc9=1.08342009
 hcn9=116.74734996
 dih9=180.
 hc10=1.08349882
 hcn10=116.73763185
 dih10=180.

