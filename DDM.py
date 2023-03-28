
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

# template code - run separately for each condition

# load the data
data = hddm.load_csv('./DDM.csv')
# create the model
m = hddm.HDDM(data, include=('v', 'a', 't', 'z'))

# find a good starting point which helps with the convergence.
m.find_starting_values()

m.sample(20000, burn=5000, thin =5)

# write the stats
m.print_stats('mregstats.txt')
# traces
traces = m.get_traces()
traces.to_csv('traces.csv')
