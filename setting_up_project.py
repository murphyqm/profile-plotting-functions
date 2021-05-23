#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 19/05/2021
by murphyqm

"""
import numpy as np
import pytesimal.load_plot_save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as plticker

import profile_plots

mantle_temp, core_temp, mantle_cr, core_cr = pytesimal.load_plot_save.read_datafile('variable_plot_for_paper.npz')

timestep = 1e11 # s
maxtime = 400 # myr

print(mantle_temp[0, :].shape) # gets you the temps for a certain depth
print(mantle_temp[:, 0].shape) # gets you temps for a certain time


# fig, ax = profile_plots.temp_through_time_plot(mantle_temp, 61, timestep)
# plt.show()

fig, ax2 = profile_plots.temp_across_depths_plot(mantle_temp, core_temp, 63114)
plt.show()