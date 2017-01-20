# Created previously, significantly modified
# JJW Jan 12 2017
# Based on plotting_script_basic.py
# This one just plots number of bodies as a function of time



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



fig = mercury.plot_number_func_time(filename="condorstdout.out")
fig.savefig("number_bodies_func_time.png",dpi=150)

