#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21/05/2021
by murphyqm

"""
import pytesimal.setup_functions
import pytesimal.load_plot_save
import pytesimal.numerical_methods
import pytesimal.analysis
import pytesimal.core_function
import pytesimal.mantle_properties

# keeping these the same:

timestep = 1E11  # s
max_time = 400  # Myr
temp_core_melting = 1200.0  # K
core_cp = 850.0  # J/(kg K)
core_density = 7800.0  # kg/m^3
temp_init = 1600.0  # K
temp_surface = 250.0  # K
core_temp_init = 1600.0  # K
core_latent_heat = 270_000.0  # J/kg
kappa_reg = 5e-8  # m^2/s
dr = 1000.0  # m

# changing these:

r_planet = 300_000.0  # m
core_size_factor = 0.7  # fraction of r_planet
reg_m = 8_000.0  # megaregolith thickness in m
reg_fraction = reg_m / r_planet  # fraction of r_planet

(r_core,
 radii,
 core_radii,
 reg_thickness,
 where_regolith,
 times,
 mantle_temperature_array,
 core_temperature_array) = pytesimal.setup_functions.set_up(timestep,
                                                            r_planet,
                                                            core_size_factor,
                                                            reg_fraction,
                                                            max_time,
                                                            dr)

# We define an empty list of latent heat that will
# be filled as the core freezes
latent = []

core_values = pytesimal.core_function.IsothermalEutecticCore(
    initial_temperature=core_temp_init,
    melting_temperature=temp_core_melting,
    outer_r=r_core,
    inner_r=0,
    rho=core_density,
    cp=core_cp,
    core_latent_heat=core_latent_heat)

(mantle_conductivity,
 mantle_heatcap,
 mantle_density) = pytesimal.mantle_properties.set_up_mantle_properties(
    cond_constant='n',
    density_constant='n',
    heat_cap_constant='n'
)

top_mantle_bc = pytesimal.numerical_methods.surface_dirichlet_bc
bottom_mantle_bc = pytesimal.numerical_methods.cmb_dirichlet_bc

# Now we let the temperature inside the planestesimal evolve. This is the
# slowest part of the code, because it has to iterate over all radii and
# time.
# This will take a minute or two!
# The mantle property objects are passed in in the same way as in the
# example with constant thermal properties.

(mantle_temperature_array,
 core_temperature_array,
 latent,
 ) = pytesimal.numerical_methods.discretisation(
    core_values,
    latent,
    temp_init,
    core_temp_init,
    top_mantle_bc,
    bottom_mantle_bc,
    temp_surface,
    mantle_temperature_array,
    dr,
    core_temperature_array,
    timestep,
    r_core,
    radii,
    times,
    where_regolith,
    kappa_reg,
    mantle_conductivity,
    mantle_heatcap,
    mantle_density)

(core_frozen,
 times_frozen,
 time_core_frozen,
 fully_frozen) = pytesimal.analysis.core_freezing(core_temperature_array,
                                                  max_time,
                                                  times,
                                                  latent,
                                                  temp_core_melting,
                                                  timestep)

mantle_cooling_rates = pytesimal.analysis.cooling_rate(mantle_temperature_array,
                                                       timestep)
core_cooling_rates = pytesimal.analysis.cooling_rate(core_temperature_array,
                                                     timestep)

d_im = 147  # cz diameter in nm
d_esq = 158  # cz diameter in nm

imilac_cooling_rate = pytesimal.analysis.cooling_rate_to_seconds(
    pytesimal.analysis.cooling_rate_cloudyzone_diameter(d_im))
esquel_cooling_rate = pytesimal.analysis.cooling_rate_to_seconds(
    pytesimal.analysis.cooling_rate_cloudyzone_diameter(d_esq))

(im_depth,
 im_string_result,
 im_time_core_frozen,
 im_Time_of_Crossing,
 im_Critical_Radius) = pytesimal.analysis.meteorite_depth_and_timing(
    imilac_cooling_rate,
    mantle_temperature_array,
    mantle_cooling_rates,
    radii,
    r_planet,
    core_size_factor,
    time_core_frozen,
    fully_frozen,
    dr=1000,
)

(esq_depth,
 esq_string_result,
 esq_time_core_frozen,
 esq_Time_of_Crossing,
 esq_Critical_Radius) = pytesimal.analysis.meteorite_depth_and_timing(
    esquel_cooling_rate,
    mantle_temperature_array,
    mantle_cooling_rates,
    radii,
    r_planet,
    core_size_factor,
    time_core_frozen,
    fully_frozen,
    dr=1000,
)

print(f"Imilac depth: {im_depth}; Imilac timing: {im_string_result}")
print(f"Esquel depth: {esq_depth}; Esquel timing: {esq_string_result}")

meteorite_results_dict = {'Esq results':
                              {'depth': esq_depth,
                               'text result': esq_string_result},
                          'Im results':
                              {'depth': im_depth,
                               'text result': im_string_result,
                               'critical radius': im_Critical_Radius}}

# define folder and check it exists:
folder = 'workflow'
pytesimal.load_plot_save.check_folder_exists(folder)
# define a results filename prefix:
result_filename = 'variable_workflow_results'

pytesimal.load_plot_save.save_result_arrays(result_filename,
                                            folder,
                                            mantle_temperature_array,
                                            core_temperature_array,
                                            mantle_cooling_rates,
                                            core_cooling_rates)

run_ID = 'Example run with default variable properties'
cond_constant = 'n'
density_constant = 'n'
heat_cap_constant = 'n'

pytesimal.load_plot_save.save_params_and_results(
    result_filename, run_ID, folder, timestep, r_planet, core_size_factor,
    reg_fraction, max_time, temp_core_melting, mantle_heatcap.getcp(),
    mantle_density.getrho(), mantle_conductivity.getk(), core_cp, core_density,
    temp_init, temp_surface, core_temp_init, core_latent_heat,
    kappa_reg, dr, cond_constant, density_constant,
    heat_cap_constant, time_core_frozen, fully_frozen,
    meteorite_results=meteorite_results_dict,
    latent_list_len=len(latent))

fig_w = 6
fig_h = 9

pytesimal.load_plot_save.two_in_one(
    fig_w,
    fig_h,
    mantle_temperature_array,
    core_temperature_array,
    mantle_cooling_rates,
    core_cooling_rates, )