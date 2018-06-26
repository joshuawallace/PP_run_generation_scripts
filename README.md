# Planet Project generation scripts

This code is used to generate the initial parameter files for running the N-body code Mercury for my research project published (here)[http://iopscience.iop.org/article/10.3847/1538-3881/aa8c08/meta].
Also scripts to submit the jobs on the local HTCondor system.

--------------

Listed below are descriptions of the various types of runs created and submitted.

---

normal_largeMFM_1 - normal initial conditions with large (1.2) MFM
normal_midMFM_1   - "                            " mid (0.8) MFM
normal_smallMFM_1 - "                            " small (0.4) MFM


control_notidal_largeMFM_1 - runs with no tidal considerations, large MFM
control_notidal_midMFM_1   - runs with no tidal considerations, mid MFM
control_notidal_smallMFM_1 - runs with no tidal considerations, small MFM

control_onlymerging_1  - runs with only complete mergers (MFM doesn't matter)

variation_bodymass_up_largeMFM_1 - mass of each initial body is twice that of
                                   the normal runs, with large MFM
variation_bodymass_up_midMFM_1   - mass of each initial body is twice that of
                                   the normal runs, with mid MFM
variation_bodymass_up_smallMFM_1 - mass of each initial body is twice that of
                                   the normal runs, with small MFM

variation_bodymass_down_largeMFM_1 - 
variation_bodymass_down_midMFM_1 -  same as above, but initial body mass half
variation_bodymass_down_smallMFM_1 - 


variation_numbody_up_largeMFM_1 - num of initial bodies is twice that of
                                   the normal runs, with large MFM
variation_numbody_up_midMFM_1   - num of initial initial bodies is twice that of
                                   the normal runs, with mid MFM
variation_numbody_up_smallMFM_1 - num of initial bodies is twice that of
                                   the normal runs, with small MFM

variation_numbody_down_largeMFM_1 - 
variation_numbody_down_midMFM_1 -  same as above, but num initial bodies half
variation_numbody_down_smallMFM_1 - 

(only three of each of the following)

variation_cusp_up_largeMFM_1 - move cusp up to 0.03 AU
variation_cusp_up_midMFM_1 -  move cusp up to 0.03 AU
variation_cusp_up_smallMFM_1 - move cusp up to 0.03 AU

variation_cusp_down_largeMFM_1 - 
variation_cusp_down_midMFM_1 -  same as above, cusp down to 0.015 AU
variation_cusp_down_smallMFM_1 -
