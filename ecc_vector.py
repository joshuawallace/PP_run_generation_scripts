import numpy as np
import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/u/joshuajw/PlanetProject/mercury'))
if not path in sys.path:
    sys.path.insert(1, path)
import mercury_outputreader as mercury
import ecc_plotter as ecc


names, aei = mercury.aei_aggregator(pomega=True)

time, aei_functime, num = mercury.aei_func_time(aei)

fig = ecc.plot_ecc_vector_func_time(time, aei_functime)
fig.savefig("ecc_vector.png")
