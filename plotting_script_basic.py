# Created previously, significantly updated and cleaned up 
# JJW Dec. 13 2016
# This plots a bunch of useful diagnostic and other plots for each output
# of the frag.f90 code



import numpy as np
import json
import os
import sys
import glob
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/u/joshuajw/PlanetProject/mercury'))
if not path in sys.path:
    sys.path.insert(1, path)
import mercury_outputreader as mercury
import mercury_output_looker_ater as looker_ater


if len(sys.argv) == 1: #If no time array was passed in via the command line
    cwd = os.getcwd()
    if ('largeMFM' in cwd or
       'midMFM'   in cwd  or
       'onlymerging'  in cwd):
          times_ = (0.,100,300,2000,10000,3.00e5)
          final_time = 3e5
    elif 'smallMFM' in cwd:
          times_ = (0.,100,300,2000,10000,1.00e5)
          final_time = 1e5
    else:
        raise RuntimeError("Unrecognized current directory, as far as large/mid/smallMFM goes")

elif len(sys.argv) == 2:
    try:
        print "I was given my own time array, not using the default values:"
        print sys.argv[1]
        times_ = json.loads(sys.argv[1])
        if len(times_) != 6:
            raise TypeError("The times list passed in is length " + str(len(times_)) + ", not a 6")
    except ValueError:
        print "Got a ValueError trying to read in the times list. Quitting..."
        quit()
else:
    raise TypeError("I got " + str(len(sys.argv)) + " arguments to the code, wrong number!")


aei_files = filter(os.path.isfile, glob.glob('./*.aei'))

if not aei_files: #If there are no aei files, ask if user wants to run element7
    print "There are no .aei files"
    print "Yes is currently the default value to run elemen7"
    run_element7 = 'y'#raw_input("Do you want to run element7? (y/[n])")
    
    if run_element7 in ['y','yes','Y','Yes','YES']:
        print "Running element7..."
        os.system('/u/joshuajw/PlanetProject/mercury/element7')
    else:
        print "NOT running element7"

else:
    print "aei files already present"

######################################
## Enough for the preliminaries, now on to the main event!
###########################

names, aei = mercury.aei_aggregator() #Names and aei information for the bodies

#e_vs_a
mercury.plot_all_aeis_here(times=times_,a_limits=(0,0.04),names_and_aeifunctime=(names,aei))



#names_justorig, aei_justorig = mercury.aei_aggregator(just_original_bodies=True)
#print "done accruing names and aei's"

i_max,final_body_indices = mercury.final_body_determiner(aei,I_want_list_of_final_body_indices=True)
print final_body_indices
print "those were the final_body_indices"


"""
aes_forplotting = [item.a for item in aei]
times_forplotting= [item.time for item in aei]
if glob.glob("FRAG*.aei"): #If there exists FRAG*.aei files
    fig = looker_ater.plot_a_func_time(aes_forplotting,times_forplotting,which_are_final_bodies=final_body_indices,year_unit='kyr')
else:
    fig = looker_ater.plot_a_func_time(aes_forplotting,times_forplotting,which_are_final_bodies=final_body_indices,year_unit='kyr',title="No fragment .aei files found or plotted")
fig.savefig("a_func_time.pdf")


###########
mercury.plot_all_aeis_here(times=times_,a_limits=(0.002,0.046),names_and_aeifunctime = (names,aei),year_unit="kyr",  e_limits=(0.,0.1) )
###########
"""

time, aei_functime, num = mercury.aei_func_time(aei)
print "Number of final bodies, " + str(len(aei_functime[-1].name))
print "  Names: " + str(aei_functime[-1].name)
print "Number of non-fragment final bodies, " + str(len( [item for item in aei_functime[-1].name if 'F' not in item] ))
print "Number of final planets, " + str(len( [item for item in aei_functime[-1].a if item >= 0.0088781786] ))
print "Number of final planets outside 1.1 rroche, " + str(len( [item for item in aei_functime[-1].a if item >= 1.1*0.0088781786] ))




quit()



#fig = looker_ater.adhoc_number_insideoutside_roche(time, aei_functime, num)
#fig.savefig("num_func_time_inout_roche.pdf")
#print "done with num_func_time_inout_roche "


name_temp = aei_functime[-1].name
a_temp = aei_functime[-1].a
e_temp = aei_functime[-1].e
i_temp = aei_functime[-1].i
mass_temp = aei_functime[-1].mass
temp_aei_singletime = mercury.aei_singletime(name_temp,a_temp,e_temp,i_temp,mass_temp)

fig = looker_ater.plot_mutual_hill_radii(temp_aei_singletime)
fig.savefig("separation.pdf")


fig = mercury.plot_number_func_time(filename="condorstdout.out")
fig.savefig("number_bodies_func_time.png",dpi=150)


temp = [item for item in aei_functime[-1].name]
names_of_final_bodies = temp
print temp
thefile = open("final_bodies.txt","w")
for item in temp:
    thefile.write(item+'\n')

thefile.close()


#Mass func time
fig = mercury.plot_mass_func_time(names_of_final_bodies,final_time=final_time)
fig.savefig("mass_func_time.pdf")



collision_info_tuple = mercury.collision_info_extractor("info.out") #Extract already since we'll need it
    #for the plot_collisions_mtovermp_func_time() function

fig = mercury.plot_collision_scatterplot_simplifiedcollisionclassification(collision_info=collision_info_tuple)
fig.savefig("collision_scatterplot.png",dpi=150)

fig = mercury.plot_collisions_mtovermp_func_time(collision_info_tuple[0],whichonestofocus=[item for item in aei_functime[-1].name if 'F' not in item])
fig.savefig("collision_timing_sizes.png",dpi=150)

meanmedian_output = mercury.calc_average_mtovermp(collision_info_tuple[0],[item for item in aei_functime[-1].name if 'F' not in item])
np.savetxt("all_mean_median_mtmp.txt",meanmedian_output[0])
np.savetxt("selected_mean_median_mtmp.txt",meanmedian_output[1])



fig = mercury.plot_collision_scatterplot_simplifiedcollisionclassification(whichones=[item for item in aei_functime[-1].name], title="Just Final Bodies")
fig.savefig("collision_scatterplot_justfinalbodies.png")

fig = mercury.plot_collision_scatterplot_simplifiedcollisionclassification(whichones=[item for item in aei_functime[-1].name], title="Just Final Bodies, only outside Roche",outside_Roche=True)
fig.savefig("collision_scatterplot_justfinalbodies_rochecutoff.png")



initial_body_collisions = [item for item in collision_info_tuple[0] if (item.projectile_name in aei_functime[0].name or item.target_name in aei_functime[0].name) ]
final_body_collisions = [item for item in initial_body_collisions if (item.projectile_name in aei_functime[-1].name or item.target_name in aei_functime[-1].name) ]

num_final_mergers = 0
num_final_hitrun = 0
num_final_fragmentation = 0


for i in range(len(final_body_collisions)):
    if final_body_collisions[i].classification in [mercury.collision_type.GRAZING_FRAG,mercury.collision_type.NONGRAZING_FRAG]:
        num_final_fragmentation += 1
    elif final_body_collisions[i].classification == mercury.collision_type.HIT_AND_RUN:
        num_final_hitrun += 1
    else:
        num_final_mergers += 1

print ""

print "All final bodies:"
print "   merger fraction: " + str( float(num_final_mergers)/float(len(final_body_collisions)))
print "   frag   fraction: " + str( float(num_final_fragmentation)/float(len(final_body_collisions)))
print "   h&r    fraction: " + str( float(num_final_hitrun)/float(len(final_body_collisions)))
