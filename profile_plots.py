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


def temp_through_time_plot(mantle_temp, depth, timestep, fig=None, ax=None):
	maxtime = 400 # doesn't get used
	million_years, _, myr = pytesimal.load_plot_save.get_million_years_formatters(timestep, maxtime)
	formatter = FuncFormatter(million_years)
	temps = mantle_temp[depth, :]
	times = np.arange(0, len(temps))
	if (fig is None) and (ax is None):
		fig, ax = plt.subplots()
	ax.xaxis.set_major_formatter(formatter)
	ticker_step = (100 * myr) / timestep
	loc = plticker.MultipleLocator(
		base=ticker_step
	)
	ax.xaxis.set_major_locator(loc)
	plt.plot(times, temps)
	return fig, ax


def temp_across_depths_plot(mantle_temp, core_temp, time, fig=None, ax=None, label=''):
	full_temps = np.concatenate((mantle_temp[-1:0:-1, :], core_temp[-1:0:-1, :]), axis=0)
	x_temps = full_temps[:, time]
	y_depth = np.arange(1, len(x_temps)+1)
	if (fig is None) and (ax is None):
		fig, ax = plt.subplots()
	plt.plot(x_temps, y_depth, label)
	ax.set_ylim(len(x_temps)+5, -3)
	return fig, ax


def temp_across_mantle_depths_plot(mantle_temp, time, fig=None, ax=None):
	full_temps = mantle_temp
	x_temps = full_temps[:, time]
	y_depth = np.arange(1, len(x_temps)+1)
	if (fig is None) and (ax is None):
		fig, ax = plt.subplots()
	plt.plot(x_temps, y_depth)
	ax.set_ylim(len(x_temps)+5, -3)
	return fig, ax
