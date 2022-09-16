
##########################################################################################################################
############################                       Trust                ################################################
#########################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hddm
import sys
import pickle
import os
import patsy
from patsy import dmatrix
from pandas import Series
from kabuki.analyze import check_geweke
from kabuki.analyze import gelman_rubin


# load the data
data = hddm.load_csv('./log_DDMTB.csv')
# create the model
m = hddm.HDDM(data)
# find a good starting point which helps with the convergence.
m.find_starting_values()

m.sample(20000, burn=5000, thin =5)
# write the stats
m.print_stats('TD_mregstats_long.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces_TD.csv')

##########################################################################################################################
############################                       Like                ################################################
#########################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hddm
import sys
import pickle
import os
import patsy
from patsy import dmatrix
from pandas import Series
from kabuki.analyze import check_geweke
from kabuki.analyze import gelman_rubin

# load the data
data = hddm.load_csv('./log_DDMLD.csv')
#create matrix

# create the model
m = hddm.HDDM(data)

# find a good starting point which helps with the convergence.
m.find_starting_values()
# start drawing 2000 samples and discarding 20 as burn-in (usually you want to have a longer burn-in period)

m.sample(20000, burn=5000, thin =5)

# write the stats
m.print_stats('LD_mregstats_long.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces_LD.csv')

##########################################################################################################################
############################                       Baseline                ################################################
#########################################################################################################################


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hddm
import sys
import pickle
import os
import patsy
from patsy import dmatrix
from pandas import Series
from kabuki.analyze import check_geweke
from kabuki.analyze import gelman_rubin

# load the data
data = hddm.load_csv('./log_DDMBL.csv')

# create the model
m = hddm.HDDM(data)
# find a good starting point which helps with the convergence.
m.find_starting_values()
# start drawing 2000 samples and discarding 20 as burn-in (usually you want to have a longer burn-in period)
m.sample(20000, burn=5000, thin =5)

# write the stats
m.print_stats('BL_mregstats_long.txt')

# traces
traces = m.get_traces()
traces.to_csv('traces_BL.csv')
