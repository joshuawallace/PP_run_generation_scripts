import numpy as np
import json
import os
import sys
import glob
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/u/joshuajw/PlanetProject/mercury'))
if not path in sys.path:
    sys.path.insert(1, path)
import mercury_outputreader as mercury
import ecc_plotter as ecc



with open("final_bodies.txt", "r") as f:
    final_bodies = f.readlines()

final_bodies = [x.strip('\n') for x in final_bodies]
final_bodies = [val for val in final_bodies if 'F' not in val]
print final_bodies

names, aei = mercury.aei_aggregator(which_bodies=final_bodies)
print names

close_encounters = ecc.close_encounter_getter(names,threshold=8e-6)

time, aei_functime, num = mercury.aei_func_time(aei)


(num_func_time,split_over_roche) = mercury.numberofbodies_functime_reader('condorstdout.out')

fig = ecc.plot_average_ecc_func_time(time,[x.e for x in aei_functime], [val.number_outside_roche for val in split_over_roche],second_time = [val.time for val in split_over_roche], ce_to_plot=close_encounters)
fig.savefig("avg_ecc.png")
