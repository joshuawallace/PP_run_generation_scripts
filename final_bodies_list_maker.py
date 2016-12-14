import numpy as np
import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/u/joshuajw/PlanetProject/mercury'))
if not path in sys.path:
    sys.path.insert(1, path)
import mercury_outputreader as mercury
import mercury_output_looker_ater as looker_ater



names, aei = mercury.aei_aggregator()#just_original_bodies=True)

names_justorig, aei_justorig = mercury.aei_aggregator(just_original_bodies=True)
print "done accruing names and aei's"


time, aei_functime, num = mercury.aei_func_time(aei)
print "Number of final bodies, " + str(len(aei_functime[-1].name))
print "  Names: " + str(aei_functime[-1].name)
print "Number of non-fragment final bodies, " + str(len( [item for item in aei_functime[-1].name if 'F' not in item] ))



temp = [item for item in aei_functime[-1].name]
thefile = open("final_bodies.txt","w")
for item in temp:
    thefile.write(item+'\n')

thefile.close()

