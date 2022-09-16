
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


##########################################################################################################################
############################                       Trust                ################################################
#########################################################################################################################

# load the data
data = hddm.load_csv('./log_DDM_TrustType.csv')

# create the model
m = hddm.HDDM(data)
m.find_starting_values()

m.sample(20000, burn=5000, thin =5)

#
# write the stats
m.print_stats('TrustType_mregstats_long.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces_TrustType.csv')


##########################################################################################################################
############################                       Like					################################################
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
data = hddm.load_csv('./log_DDM_LikeType.csv')

# create the model
m = hddm.HDDM(data)
# find a good starting point which helps with the convergence.
m.find_starting_values()

m.sample(20000, burn=5000, thin =5)

# write the stats
m.print_stats('LikeType_mregstats_long.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces_LikeType.csv')


##########################################################################################################################
############################                       Like					################################################
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
data = hddm.load_csv('./log_DDM_Baseline.csv')

# create the model
m = hddm.HDDM(data)
# find a good starting point which helps with the convergence.
m.find_starting_values()

m.sample(20000, burn=5000, thin =5)

# write the stats
m.print_stats('Baseline_mregstats_long.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces_Baseline.csv')
