#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/06/2021
by murphyqm

"""

import profile_plots
import matplotlib.pyplot as plt
import pytesimal.load_plot_save
import numpy as np

mantle_temp = pytesimal.load_plot_save.read_datafile('variable_plot_for_paper.npz')[0]
core_temp = pytesimal.load_plot_save.read_datafile('variable_plot_for_paper.npz')[1]
#
# mantle_temp = pytesimal.load_plot_save.read_datafile('workflow/variable_workflow_results.npz')[0]
#
# del mantle_temp
time = 200_00
myr = 3.1536e+13
time_in_myr = time*1e11/myr

# label = r'$T = \frac{d_{km} + 25.1711}{0.0747}$'
fig, ax = profile_plots.temp_across_depths_plot(mantle_temp, core_temp, time,)
ax.set_ylabel('Depth (km)')
ax.set_xlabel('Temperature (K)')
ax.set_title('Temperature profile at ~63 Myr (20,000 time steps)')
plt.savefig('temp_depth_closeup.png', bbox_inches='tight')
ax.set_ylim(60,62)
ax.set_xlim(1140,1165)
plt.legend()
plt.show()

# full_temps = np.concatenate((mantle_temp[-1:0:-1, :], core_temp[-1:0:-1, :]), axis=0)
# x_temps = full_temps[:, time]
# y_depth = np.arange(1, len(x_temps)+1)
#
# x = [x_temps[59], x_temps[60], x_temps[61]]
# y = [y_depth[59], y_depth[60], y_depth[61]]
# x2 = [x_temps[59], x_temps[61]]
# y2 = [y_depth[59], y_depth[61]]
# plt.plot(x2, y2)
# plt.plot(x, y)
# plt.show()