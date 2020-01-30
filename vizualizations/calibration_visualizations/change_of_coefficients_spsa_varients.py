'''
Created on 28 Jan 2020

@author: thenuwan.jayasinghe
'''
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('default')
import itertools

#This is to compare FDSA and SPSA with far estimates and close estimates - altogether 4 line plots in one plot
#load csvs as dataframes
 
spsa_vanila = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\1_Coding\\Experiments\\28012020_evaluate_spsa_varients\\results\\2_mumford_1_hp_13_ob_2\\far_cleaned\\spsa_vanila_far_29012020_cleaned.csv")
spsa_adaptiveStep = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\1_Coding\\Experiments\\28012020_evaluate_spsa_varients\\results\\2_mumford_1_hp_13_ob_2\\far_cleaned\\spsa_adaptive_step_far_29012020_cleaned.csv")
spsa_weight = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\1_Coding\\Experiments\\28012020_evaluate_spsa_varients\\results\\2_mumford_1_hp_13_ob_2\\far_cleaned\\spsa_weight_far_29012020_cleaned.csv")
spsa_aStepWeight = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\1_Coding\\Experiments\\28012020_evaluate_spsa_varients\\results\\2_mumford_1_hp_13_ob_2\\far_cleaned\\spsa_aStep_weight_far_29012020_cleaned.csv")

iteration_list = spsa_adaptiveStep.Iteration.tolist()
 
#spsa results to seperate lists

sv_inVehicleTime_est = spsa_vanila.invehicleTime_est.tolist()
#sv_accessTime_est = spsa_vanila.accessTime_est.tolist()
#sv_egressTime_est = spsa_vanila.egressTime_est.tolist()
#sv_transferWalkingTime_est = spsa_vanila.walkingTime_est.tolist()
sv_originWaitTime_est = spsa_vanila.originWaitTime_est.tolist()
sv_transferWaitTime_est = spsa_vanila.transferWaitTime_est.tolist()


sw_inVehicleTime_est = spsa_weight.invehicleTime_est.tolist()
#sw_accessTime_est = spsa_weight.accessTime_est.tolist()
#sw_egressTime_est = spsa_weight.egressTime_est.tolist()
#sw_transferWalkingTime_est = spsa_weight.walkingTime_est.tolist()
sw_originWaitTime_est = spsa_weight.originWaitTime_est.tolist()
sw_transferWaitTime_est = spsa_weight.transferWaitTime_est.tolist()
 

sa_inVehicleTime_est = spsa_adaptiveStep.invehicleTime_est.tolist()
#sa_accessTime_est = spsa_adaptiveStep.accessTime_est.tolist()
#sa_egressTime_est = spsa_adaptiveStep.egressTime_est.tolist()
#sa_transferWalkingTime_est = spsa_adaptiveStep.walkingTime_est.tolist()
sa_originWaitTime_est = spsa_adaptiveStep.originWaitTime_est.tolist()
sa_transferWaitTime_est = spsa_adaptiveStep.transferWaitTime_est.tolist()

saw_inVehicleTime_est = spsa_aStepWeight.invehicleTime_est.tolist()
#saw_accessTime_est = spsa_aStepWeight.accessTime_est.tolist()
#saw_egressTime_est = spsa_aStepWeight.egressTime_est.tolist()
#saw_transferWalkingTime_est = spsa_aStepWeight.walkingTime_est.tolist()
saw_originWaitTime_est = spsa_aStepWeight.originWaitTime_est.tolist()
saw_transferWaitTime_est = spsa_aStepWeight.transferWaitTime_est.tolist()
 
 
 
#multi line plot to see the change of in vehicle time estimate over the iterations
_prior = list(itertools.repeat(2.0,301))
    

_ = plt.plot(iteration_list, sv_originWaitTime_est, color = 'dimgrey',  linewidth = 1.0 , label = 'Vanila SPSA') #color = 'red'
_ = plt.plot(iteration_list, sw_originWaitTime_est, color = 'orangered', linewidth = 1.2 , label = 'Weight') #color = 'darkorange'
_ = plt.plot(iteration_list, sa_originWaitTime_est, color = 'dodgerblue', linewidth = 1.2, label = 'Adaptive Step') #color = 'royalblue'
_ = plt.plot(iteration_list, saw_originWaitTime_est, color = 'mediumseagreen', linewidth = 1.2 , label = 'Adaptive Step & Weight') #color = 'seagreen'

_ = plt.plot(iteration_list, _prior, linestyle = '-.', linewidth = 0.75, color = 'dimgray', label = 'Observed Value')
 
 
_ = plt.xlabel("Iteration")
_ = plt.ylabel('Estimated value the coefficient')
_ = plt.suptitle("Change of Origin Wait Time Coefficient")
_ = plt.title("alpha = 0.602, gamma = 0.101, c = 1.419, a = 4.833, A = 30.0", fontsize = 10)
 
_ = plt.legend()
     
plt.show()
#savepath = 'C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\1_Coding\\Experiments\\28012020_evaluate_spsa_varients\\results\\1_net_2_hp_13_ob_1\\cleaned_data\\inVehicle.svg'
#plt.draw()
#plt.savefig(savepath, bbox_inches = 'tight')   



#===============================================================================
#This is to compare FDSA and SPSA
# #load csvs as dataframes
# 
# spsa_df = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\Documents\\_Thesis\\Coding\\Experiments\\07012020\\results\\hyper_parameter_set_14\\hp_set14_SPSA_10012020_cleaned.csv")
# fdsa_df = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\Documents\\_Thesis\\Coding\\Experiments\\07012020\\results\\hyper_parameter_set_14\\hp_set14_FDSA_10012020_cleaned.csv")
# 
# iteration_list = fdsa_df.Iteration.tolist()
# 
# #spsa results to seperate lists
# 
# s_inVehicleTime_est = spsa_df.invehicleTime_est.tolist()
# s_accessTime_est = spsa_df.accessTime_est.tolist()
# s_egressTime_est = spsa_df.egressTime_est.tolist()
# s_transferWalkingTime_est = spsa_df.walkingTime_est.tolist()
# s_originWaitTime_est = spsa_df.originWaitTime_est.tolist()
# s_transferWaitTime_est = spsa_df.transferWaitTime_est.tolist()
# 
# #fdsa results to seperate lists
# f_inVehicleTime_est = fdsa_df.invehicleTime_est.tolist()
# f_accessTime_est = fdsa_df.accessTime_est.tolist()
# f_egressTime_est = fdsa_df.egressTime_est.tolist()
# t_transferWalkingTime_est = fdsa_df.walkingTime_est.tolist()
# f_originWaitTime_est = fdsa_df.originWaitTime_est.tolist()
# f_transferWaitTime_est = fdsa_df.transferWaitTime_est.tolist()
# 
# 
# 
# #multi line plot to see the change of in vehicle time estimate over the iterations
# _prior = list(itertools.repeat(3.0,301))
#    
# _ = plt.plot(iteration_list, _prior, linestyle = '-.', linewidth = 0.75, color = 'dimgray', label = 'Target')
# _ = plt.plot(iteration_list, f_transferWaitTime_est, linewidth = 1, color = 'royalblue', label = 'FDSA')
# _ = plt.plot(iteration_list, s_transferWaitTime_est, linestyle = '--',linewidth = 1, color = 'red', label = 'SPSA')
# 
# 
# _ = plt.xlabel("Iteration")
# _ = plt.ylabel('Estimated value the coefficient')
# _ = plt.suptitle("Change of Transfer Wait Time Coefficient")
# _ = plt.title("Close Estimates", fontsize = 10)
# 
# _ = plt.legend()
#     
# plt.show()
#===============================================================================

#===============================================================================
# #multi line plot to see the change of walking time estimate over the iterations
# _prior = list(itertools.repeat(2.0,301))
#   
# _ = plt.plot(iteration_list, _prior, linestyle = '-.', linewidth = 0.75, color = 'dimgray', label = 'Target')
# _ = plt.plot(iteration_list, ff_walkingTime_est,  linewidth = 1, color = 'royalblue', label = 'FDSA')
# _ = plt.plot(iteration_list, fc_walkingTime_est,  linewidth = 1, color = 'royalblue')
# _ = plt.plot(iteration_list, sf_walkingTime_est, linestyle = '--',linewidth = 1, color = 'red', label = 'SPSA')
# _ = plt.plot(iteration_list, sc_walkingTime_est, linestyle = '--',linewidth = 1, color = 'red')
# _ = plt.xlabel("Iteration")
# _ = plt.ylabel('Estimated value of the coefficient')
# _ = plt.title("Walk Time")
# _ = plt.legend() 
# 
# plt.savefig('Walk_Time_change_600dpi', dpi = 600)
#    
# plt.show()
#===============================================================================

#===============================================================================
# #multi line plot to see the change of Origin wait time estimate over the iterations
# _prior = list(itertools.repeat(3.0,301))
#   
# _ = plt.plot(iteration_list, _prior, linestyle = '-.', linewidth = 0.75, color = 'dimgray', label = 'Target')
# _ = plt.plot(iteration_list, ff_originWaitTime_est,  linewidth = 1, color = 'royalblue', label = 'FDSA')
# _ = plt.plot(iteration_list, fc_originWaitTime_est, linewidth = 1, color = 'royalblue')
# _ = plt.plot(iteration_list, sf_originWaitTime_est, linestyle = '--', linewidth = 1, color = 'red', label = 'SPSA')
# _ = plt.plot(iteration_list, sc_originWaitTime_est, linestyle = '--', linewidth = 1, color = 'red')
# _ = plt.xlabel("Iteration")
# _ = plt.ylabel('Estimated value of the coefficient')
# _ = plt.title("Origin Wait Time")
# _ = plt.legend()
# 
# plt.savefig('Origin_Wait_Time_change_600dpi', dpi = 600)
#    
# plt.show()
#===============================================================================

#===============================================================================
# #multi line plot to see the change of transfer wait time estimate over the iterations
# _prior = list(itertools.repeat(5.0,301))
#   
# _ = plt.plot(iteration_list, _prior, linestyle = '-.', linewidth = 0.75, color = 'dimgray', label = 'Target')
# _ = plt.plot(iteration_list, ff_transferWaitTime_est, linewidth = 1, color = 'royalblue', label = 'FDSA')
# _ = plt.plot(iteration_list, fc_transferWaitTime_est, linewidth = 1, color = 'royalblue')
# _ = plt.plot(iteration_list, sf_transferWaitTime_est, linestyle = '--',linewidth = 1, color = 'red', label = 'SPSA')
# _ = plt.plot(iteration_list, sc_transferWaitTime_est, linestyle = '--',linewidth = 1, color = 'red')
# _ = plt.xlabel("Iteration")
# _ = plt.ylabel('Estimated value of the coefficient')
# _ = plt.title("Transfer Wait Time")
# _ = plt.legend()
# 
# plt.savefig('Trasfer_Wait_Time_change_600dpi', dpi = 600)
#    
# plt.show()
#===============================================================================