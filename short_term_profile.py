#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/06/2021
by murphyqm

"""
import numpy as np
import pytesimal.load_plot_save
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as plticker

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

# mantle_temp = pytesimal.load_plot_save.read_datafile('variable_plot_for_paper.npz')[0]
# temps1 = mantle_temp[depth1, :]
#
# mantle_temp = pytesimal.load_plot_save.read_datafile('workflow/variable_workflow_results.npz')[0]
# temps2 = mantle_temp[depth2, :]
#
# del mantle_temp

## Temperatures plot

# timestep = 1e11 # s
# maxtime = 400 # myr
# million_years, _, myr = pytesimal.load_plot_save.get_million_years_formatters(timestep, maxtime)
# formatter = FuncFormatter(million_years)
# times = np.arange(0, len(temps1))
# fig, ax = plt.subplots()
# ax.xaxis.set_major_formatter(formatter)
# ticker_step = (100 * myr) / timestep
# loc = plticker.MultipleLocator(
# 	base=ticker_step
# )
# ax.set_ylim(1000, 1500)
# ax.xaxis.set_major_locator(loc)
# ax.set_xlabel("Millions of years")
# ax.set_ylabel("Temperature (K)")
# plt.plot(times, temps1)
# plt.plot(times, temps2)
# plt.show()

print(cr1)


## Cooling rate plot

timestep = 1e11 # s
maxtime = 400 # myr
million_years, cooling_rate, myr = pytesimal.load_plot_save.get_million_years_formatters(timestep, maxtime)
formatter = FuncFormatter(million_years)
formatter2 = FuncFormatter(cooling_rate)
times = np.arange(0, len(cr1))

width = 6
height = 4



colour1 = '#e66101'
colour2='#5e3c99'

fig, ax = plt.subplots(figsize=(width,height))
# ax.xaxis.set_major_formatter(formatter)
# ax.yaxis.set_major_formatter(formatter2)
# ticker_step = (100 * myr) / timestep
# loc = plticker.MultipleLocator(
# 	base=ticker_step
# )
# ax.xaxis.set_major_locator(loc)
plt.plot(times, cr1, label=r"61 km depth; $r = 250$ km with $r_c = 125$ km", color=colour1, linestyle='dashed', linewidth=3, alpha=0.8)
plt.plot(times, cr2, label=r"45 km depth; $r = 300$ km with $r_c = 210$ km", color=colour2, linestyle='dotted', linewidth=3, alpha=0.8)
ax.invert_yaxis()
ax.set_xlabel("Timesteps (1e11 s)", )
ax.set_ylabel(r"Cooling rate (K/$\delta t$)", )

ax.set_title("Cooling rates at depth of pallasite genesis",)
plt.legend()

plt.savefig('timestep_coolingrate.png', bbox_inches='tight')
plt.show()
