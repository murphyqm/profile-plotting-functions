#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21/05/2021
by murphyqm

"""

import numpy as np
import pytesimal.load_plot_save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as plticker

import profile_plots

depth1 = 61
depth2 = 45

mantle_cr = pytesimal.load_plot_save.read_datafile('variable_plot_for_paper.npz')[2]
cr1 = mantle_cr[depth1, :]

mantle_cr = pytesimal.load_plot_save.read_datafile('workflow/variable_workflow_results.npz')[2]
cr2 = mantle_cr[depth2, :]

del mantle_cr


## Temperatures plot

# timestep = 1e11 # s
# maxtime = 400 # myr
# million_years, _, myr = pytesimal.load_plot_save.get_million_years_formatters(timestep, maxtime)
# formatter = FuncFormatter(million_years)
# temps1 = mantle_temp_250[depth1, :]
# temps2 = mantle_temp_300[depth2, :]
# times = np.arange(0, len(temps1))
# fig, ax = plt.subplots()
# ax.xaxis.set_major_formatter(formatter)
# ticker_step = (100 * myr) / timestep
# loc = plticker.MultipleLocator(
# 	base=ticker_step
# )
# ax.xaxis.set_major_locator(loc)
# plt.plot(times, temps1)
# plt.plot(times, temps2)
# plt.show()

## Cooling rate plot

timestep = 1e11 # s
maxtime = 400 # myr
million_years, cooling_rate, myr = pytesimal.load_plot_save.get_million_years_formatters(timestep, maxtime)
formatter = FuncFormatter(million_years)
formatter2 = FuncFormatter(cooling_rate)

times = np.arange(0, len(cr1))

width = 6
height = 4


# font
hfont = {'fontname':'Lato'}

colour1 = '#e66101'
colour2='#5e3c99'

fig, ax = plt.subplots(figsize=(width,height))
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter2)
ticker_step = (100 * myr) / timestep
loc = plticker.MultipleLocator(
	base=ticker_step
)
ax.xaxis.set_major_locator(loc)
plt.plot(times, cr1, label=r"61 km depth; $r = 250$ km with $r_c = 125$ km", color=colour1, linestyle='dashed', linewidth=3, alpha=0.8)
plt.plot(times, cr2, label=r"45 km depth; $r = 300$ km with $r_c = 210$ km", color=colour2, linestyle='dotted', linewidth=3, alpha=0.8)
ax.invert_yaxis()
ax.set_xlabel("Time (Myr)", **hfont)
ax.set_ylabel("Cooling rate (K/Myr)", **hfont)
plt.legend()  # prop={'family':'Lato'})
ax.set_title("Cooling rates at depth of pallasite genesis \n(depths based on Imilac metal cooling rate)", **hfont)
fig_name = "compare_cooling_rates.pdf"
plt.savefig(fig_name, bbox_inches='tight')
plt.show()
