#Created 13 Feb 2017 JJW
#This checks that no collision inside the Roche radius is a merger
#AGBTG

import numpy as np
import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/u/joshuajw/PlanetProject/mercury'))
if not path in sys.path:
    sys.path.insert(1, path)
import mercury_outputreader as mercury



collision_info_tuple = mercury.collision_info_extractor("info.out")

temp = [item for item in collision_info_tuple[0] if ( item.radius <= 0.0088774023 and (item.classification == mercury.collision_type.SIMPLE_MERGER or item.classification == mercury.collision_type.EFFECTIVE_MERGER or item.classification == mercury.collision_type.GRAZE_MERGER )) and (item.classification != mercury.collision_type.GRAZING_FRAG) ]

if len(temp) != 0:
    print "There were " + str(len(temp)) + " mergers inside Roche radius"


for i in range(len(temp)):
    print ''
    print ''
    print item.radius
    print item.classification
    print item.target_name
    print item.projectile_name
    print item.vimpact_vescape_ratio
    print item.vgrazemerge_vescape_ratio

