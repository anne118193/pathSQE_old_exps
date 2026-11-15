import os
import numpy as np

########################################################################################################
# Define list of dictionaries, each describing data (run) sets to be combined in a single mde workspace 
# Authors: A. Savici, I. Zaliznyak, March 2019.
########################################################################################################
def define_data_set(T_Ei_conditions, **kwargs):
    shared_folder='/SNS/ARCS/IPTS-12995/shared/autoreduce/'
    raw_data_folder='/SNS/ARCS/IPTS-12995/data/'
    mde_folder='/SNS/ARCS/IPTS-12995/shared/Anne' # where to save or search for mde

    data_set_list=[]
    for T, E in T_Ei_conditions:
        data_set={'Runs':list(range(60792, 60992+1)), # list(range(60792, 61025));
                    'BackgroundRuns':list(range(62340, 62348)),   # Options: None;list of runs that are added together
                    'RawDataFolder':raw_data_folder,      #Options:raw_data_folder string
                    'MdeFolder':mde_folder,               #Options:mde_folder string
                    'MdeName':'Cu2O_{}K_{}meV_UBcorrected_ub'.format(T,E),
                    'BackgroundMdeName':'empty_Cu2O_{}K_{}meV_UBcorrected_ub'.format(T,E),      #Options:None;bg_mde_name string
                    'MaskingDataFile':'/SNS/ARCS/shared/autoreduce/vanadium_files/van58221.nxs',         #Options:None;data_file_name
                    'NormalizationDataFile':'/SNS/ARCS/shared/autoreduce/vanadium_files/van58221.nxs',   #Options:None;data_file_name
                    'SampleLogVariables':{'OmegaMotorName':'CCR12Rot','Temperature':T},   # 5K: 'CCR16Rot'; 300K: 'CCR12Rot'
                    'UBSetup': {'a':4.2467,'b':4.2467,'c':4.2467,'alpha':90,'beta':90,'gamma':90, 'u':'0,0,1', 'v':'1,0,0'}, 
                    #'UBSetup':{'ub':'0.12685824,-0.13193672,-0.01291855,0.06613873,0.07848529,-0.15209513,-0.11489062,-0.10049857,-0.10182034'},  # For Si 300K: 
                    #Data reduction options
                    'Ei':None,                             #Options: None;Ei_somehow_determined
                    'T0': None,                           #Options: None;T0_determined_from_mantid
                    'BadPulsesThreshold':None,            #Options: None;bg_pulses_threshold value
                    'TimeIndepBackgroundWindow':None,     #Options: None;[Tib_min,Tib_max]
                    'E_min':None,                         #Options: None;Emin
                    'E_max':None,                         #Options: None;Emax
                    'AdditionalDimensions':None,          #Options: None;list of triplets ("name", min, max)
                    'EfCorrectionFunction':None,          #Options:None;'HYSPEC_default_correction';Custom_Ef_Correction_Function_Name
                    }
        data_set_list.append(data_set)


    return data_set_list
