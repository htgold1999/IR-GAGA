# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:41:12 2022

@author: Hannah Gold
"""

# from magnetophotonicCrystal import magnetophotonicCrystal
import os
# from Find_reflectance.Magnetooptic2Magnetooptic import *
# from Find_reflectance.magnetophotonicCrystal import magnetophotonicCrystal
# from Find_reflectance.Refractive_index_data import *

# from Magnetooptic2Magnetooptic import *
# from magnetophotonicCrystal import magnetophotonicCrystal

# current_working_directory = os.getcwd()
# print("this path",current_working_directory)
# path =current_working_directory
# os.chdir(path)


#%%
import numpy as np 
import math
from math import *
import matplotlib.pyplot as plt
import cmath #
j=(cmath.sqrt(-1))
import scipy 

from scipy.interpolate import interp1d


      # Physical constants.
hbar = 1.05457e-34
eV = 1.60218e-19
c = 2.99792e8
k_B = 1.38065e-23
sigma = 5.67037e-8
m_e = 9.10938e-31
epsilon_0 = 8.85419e-12


# Material properties.
class Epsilon_Creator():
    #lambda_ is in meters
    def __init__(self,dont_care=0, dataframe=None,lambda__=None,N_=None,material_dict_indices_=None):
        #self.df=Data_frame_creator()
        self.df=dataframe
        self.dont_care=dont_care # if 1, we dont care about the proper wavelength range
        #dff=self.df["SiO2"]
        #print(dff["Epsilon"].astype(float).to_list())
        self.lambda_=lambda__ #lambda
        #self.omega=omega #omega
        self.N=N_ #number of layers
        #self.material_dict=material_dict # A dictionary of materials and their dielectric fuctions
        self.material_dict_indices=material_dict_indices_ #list of keys corresponding to materials in the material dictionary
    def df_to_wavelength_list(self,df):
          wavelength_list= df["Wavelength"].astype(float).to_list()  #converts the dataframe column to a pandas series of floats then a list of floats     
          #not done yet
          return wavelength_list
    def find_nearest(self,lst, value):
        #print("lambda value")
        #print(value)
        idx=np.argmin(np.abs(np.array(lst)-value))
        #print("nearest value")
        #print(lst[idx])
        
        return idx, lst[idx]
    
    def TiO2_eps(self,lambda_):
        if  self.dont_care:
            ##This data is for thin films, but the thicknesses are thin enough by the standards of the paper the data came from 
            material_df=self.df["TiO2"] # need to get refractive index given pandas dataframe
            real_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_R"].astype(float).to_list())
            imag_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_I"].astype(float).to_list())
            eps_TiO2 = real_num +j*imag_num
            eps_TiO2 =np.real(eps_TiO2)
        else:
            ##This data is for thin films, but the thicknesses are thin enough by the standards of the paper the data came from 
            material_df=self.df["TiO2"] # need to get refractive index given pandas dataframe
            real_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_R"].astype(float).to_list())
            imag_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_I"].astype(float).to_list())
            eps_TiO2 = real_num +j*imag_num
            #_______________________________
            # interp_1d= interp1d(material_df["Wavelength"].astype(float).to_list(),(material_df["Epsilon_R"]+j*material_df["Epsilon_I"]))
            
            # eps_TiO2 = interp_1d(lambda_micrometer)
            
            ##
            
            # wavelength_list=self.df_to_wavelength_list(material_df)
            # idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            # eps_TiO2=material_df["Epsilon_R"][idx] +j*material_df["Epsilon_I"][idx] 
            
       
        return eps_TiO2
    def SiO2_eps(self,lambda_):
        
        
        
        #print("self.df[SiO2]")
        #print(self.df)
        if (lambda_*1000000)<7:
            eps_SiO2=1+((((0.6961663)*lambda_**2)/((lambda_**2)-(0.0684043**2))) + (((0.4079426)*lambda_**2)/((lambda_**2)-(0.1162414**2))) + (((0.8974794)*lambda_**2)/((lambda_**2)-(9.896161**2))))
            eps_SiO2=eps_SiO2+0.00014657*j
        elif  self.dont_care:
            #materila_df=self.df["SiO2"] # need to get refractive index given pandas dataframe
            material_df=self.df["SiO2"] # need to get refractive index given pandas dataframe
            real_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_R"].astype(float).to_list())
            imag_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_I"].astype(float).to_list())
            eps_SiO2 = real_num +j*imag_num
            eps_SiO2 = np.real(eps_SiO2)
            
        else:
            #materila_df=self.df["SiO2"] # need to get refractive index given pandas dataframe
            material_df=self.df["SiO2"] # need to get refractive index given pandas dataframe
            real_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_R"].astype(float).to_list())
            imag_num=np.interp(lambda_,material_df["Wavelength"].astype(float).to_list(),material_df["Epsilon_I"].astype(float).to_list())
            eps_SiO2 = real_num +j*imag_num
            
            #eps_SiO2 = np.real(eps_SiO2)
            #_________________________________
            # interp_1d= interp1d(material_df["Wavelength"].astype(float).to_list(),(material_df["Epsilon_R"]+j*material_df["Epsilon_I"]))
            
            # eps_SiO2 = interp_1d(lambda_micrometer)
            
            
            # wavelength_list=self.df_to_wavelength_list(material_df)
            # idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            # eps_SiO2=material_df["Epsilon_R"][idx] +j*material_df["Epsilon_I"][idx] 
            
       
        return eps_SiO2
    
    def HfO2_eps(self,lambda_):
        
        lambda_micrometer=lambda_*1000000
        if  False:
            eps_SiO2=1.46**2
            eps_SiO2=(1.7 +j*0.3)**2
            eps_SiO2=(1.7 )**2
        elif self.dont_care:
        
            material_df=self.df["HfO2"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            eps_HfO2=material_df["Epsilon_R"][idx] +j*material_df["Epsilon_Im"][idx] 
                
            
        return eps_HfO2
    def MgO_eps(self,lambda_):
        
        if (lambda_*1000000)< 10:
            eps_MgO = 2.957019 + 0.0216485/(lambda_**2 - 0.0158650) - 0.0101373*lambda_**2 
            eps_MgO =eps_MgO +0.0200924859999999*j
        elif self.dont_care:
            material_df_0=self.df["MgO_n"] # need to get refractive index given pandas dataframe
            interp_n=np.interp(lambda_,material_df_0["Wavelength"].astype(float).to_list(),material_df_0["n"].astype(float).to_list())
            
            material_df_1=self.df["MgO_k"] # need to get refractive index given pandas dataframe
            interp_k=np.interp(lambda_,material_df_1["Wavelength"].astype(float).to_list(),material_df_1["k"].astype(float).to_list())
            eps_MgO = (interp_n+j*interp_k)**2
            eps_MgO = np.real(eps_MgO)
        else:
            material_df_0=self.df["MgO_n"] # need to get refractive index given pandas dataframe
            interp_n=np.interp(lambda_,material_df_0["Wavelength"].astype(float).to_list(),material_df_0["n"].astype(float).to_list())
            
            material_df_1=self.df["MgO_k"] # need to get refractive index given pandas dataframe
            interp_k=np.interp(lambda_,material_df_1["Wavelength"].astype(float).to_list(),material_df_1["k"].astype(float).to_list())
            
            eps_MgO = (interp_n+j*interp_k)**2
           
            #eps_MgO = np.real(eps_MgO)
            
            
        
        return eps_MgO
    def Pt_eps(self,lambda_):
        lambda_micrometer=lambda_*1000000
        if  0.00236 <= lambda_micrometer<=0.12157 or self.dont_care :
            omega_plasma=5.145*(eV/hbar) #Plasma Frequency of Pt [rad/sec]
            omega= (2*pi*c)/lambda_
            gamma_=(69.2*(10**-3))*(eV/hbar)  #drude damping
            eps_Pt= 1- ((omega_plasma**2)/((omega**2)+(j*omega*gamma_)))
        elif 0.248<= lambda_micrometer<= 12.4 :
            material_df=self.df["Pt"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            eps_Pt=material_df["Epsilon"][idx] 
        else:
            print("Other Pt_eps wavelengths not coded yet")
            eps_Pt=10000
        return eps_Pt
    def Ge_eps(self,lambda_):
        #in THz regime
        
        if self.dont_care :
           
            eps_Ge= 16
        
        else:
            print("Other Ge_eps wavelengths not coded yet")
            eps_Ge=10000
        return eps_Ge
    
    
    def Co2MnGa_eps (self,lambda_):
        lambda_micrometer=lambda_*1000000
        if 8.254<= lambda_micrometer<=99.9867 or self.dont_care:
            material_df=self.df["Co2MnGa"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_)
            eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
            # print("eps_t")
            # print(eps_t)
            eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
            g=material_df["g_R"][idx] + j*material_df["g_I"][idx]
        else:
            print("Other Co2MnGa_eps wavelengths not coded yet")
            eps_t=10000
            eps_l=10000
            g=0
        return eps_t,eps_l, g # z and x are transverse and longitudinal components (respectively) of the dielectric tensor see source https://dspace.mit.edu/bitstream/handle/1721.1/132930/PhysRevB.102.165417.pdf?sequence=1
    def weyl_material_1_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_1"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_1_EF_01_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_1_EF=0.1"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_1_EF_007_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_1_EF=0.07"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_1_EF_02_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_1_EF=0.2"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g
    def weyl_material_2_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_2"] # need to get refractive index given pandas dataframe
            
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        # # print("eps_t")
        # # print(eps_t)
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
        
        return eps_t,eps_l, g # z and x are transverse and longitudinal components (respectively) of the dielectric tensor see source https://dspace.mit.edu/bitstream/handle/1721.1/132930/PhysRevB.102.165417.pdf?sequence=1
    
    def weyl_material_2_EF_01_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_2_EF=0.1"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_2_EF_007_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_2_EF=0.07"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_2_EF_02_eps (self,lambda_):
        # lambda_micrometer=lambda_*1000000
        material_df=self.df["weyl_material_2_EF=0.2"] # need to get refractive index given pandas dataframe
        real_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_R"])
        imag_num_t=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_T_I"])
        eps_t = real_num_t +j*imag_num_t
        
        real_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_R"])
        imag_num_l=np.interp(lambda_,material_df["Wavelength"],material_df["Epsilon_L_I"])
        eps_l = real_num_l +j*imag_num_l
        
        g = np.interp(lambda_,material_df["Wavelength"],material_df["g"])
        
        
        
        # wavelength_list=self.df_to_wavelength_list(material_df)
        # idx,_=self.find_nearest(wavelength_list, lambda_)
        # eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
        
        # eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
        # g=material_df["g"][idx]
       
        return eps_t,eps_l, g 
    def weyl_material_3_eps (self,lambda_):
        lambda_micrometer=lambda_*1000000
        if self.dont_care:
            material_df=self.df["weyl_material_3"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_)
            eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
            # print("eps_t")
            # print(eps_t)
            eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
            g=material_df["g"][idx]
        else:
            print("Other weyl_material_3_eps wavelengths not coded yet")
            eps_t=10000
            eps_l=10000
            g=0
        return eps_t,eps_l, g
    
    def weyl_material_4_eps (self,lambda_):
        lambda_micrometer=lambda_*1000000
        if self.dont_care:
            material_df=self.df["weyl_material_4"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_)
            eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
            # print("eps_t")
            # print(eps_t)
            eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
            g=material_df["g"][idx]
        else:
            print("Other weyl_material_4_eps wavelengths not coded yet")
            eps_t=10000
            eps_l=10000
            g=0
        return eps_t,eps_l, g
    
    def weyl_material_5_eps (self,lambda_):
        lambda_micrometer=lambda_*1000000
        if self.dont_care:
            material_df=self.df["weyl_material_5"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_)
            eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
            # print("eps_t")
            # print(eps_t)
            eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
            g=material_df["g"][idx]
        else:
            print("Other weyl_material_5_eps wavelengths not coded yet")
            eps_t=10000
            eps_l=10000
            g=0
        return eps_t,eps_l, g
    def weyl_material_6_eps (self,lambda_):
        lambda_micrometer=lambda_*1000000
        if self.dont_care:
            material_df=self.df["weyl_material_6"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_)
            eps_t=material_df["Epsilon_T_R"][idx] + j*material_df["Epsilon_T_I"][idx] 
            # print("eps_t")
            # print(eps_t)
            eps_l=material_df["Epsilon_L_R"][idx] + j*material_df["Epsilon_L_I"][idx] 
            g=material_df["g"][idx]
        else:
            print("Other weyl_material_6_eps wavelengths not coded yet")
            eps_t=10000
            eps_l=10000
            g=0
        return eps_t,eps_l, g
    def Ag_eps(self,lambda_):
        lambda_micrometer=lambda_*1000000
        if  0.1879<= lambda_micrometer<=1.9370 or 2.480e-06<= lambda_micrometer<=248 or 0.270<= lambda_micrometer<=24.9 or self.dont_care:
            material_df=self.df["Ag"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            eps_Ag=material_df["Epsilon"][idx] 
        else:
            print("Other Ag_eps wavelengths not coded yet")
            eps_Ag=10000
        
        return eps_Ag
    def Au_eps(self,lambda_):
        lambda_micrometer=lambda_*1000000
        if  0.667<= lambda_micrometer<=286 or self.dont_care:
            material_df=self.df["Au"] # need to get refractive index given pandas dataframe
            wavelength_list=self.df_to_wavelength_list(material_df)
            idx,_=self.find_nearest(wavelength_list, lambda_micrometer)
            eps_Au=material_df["Epsilon"][idx] 
        else:
            print("Other Au_eps wavelengths not coded yet")
            eps_Au=10000
    def Air(self,lambda_):
        eps_Air=1
        
        return eps_Air
    # def material_dict(self):
    #     material_dict = { "Air": {"function": self.Air, "isotropic":1},"TiO2": {"function": self.TiO2_eps, "isotropic":1}, "SiO2": {"function":self.SiO2_eps,"isotropic":1}, 'MgO': {"function":self.MgO_eps,"isotropic":1}, 
    #                      "Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0}, "Ag": {"function":self.Ag_eps,"isotropic":1}, "Au": {"function":self.Au_eps,"isotropic":1}, "Pt": {"function":self.Pt_eps,"isotropic":1},
    #                      "weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0}, "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0},
    #                      "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0},"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
    #     return material_dict
    def material_dict(self):
        # material_dict = { 0:{"Air": {"function": self.Air, "isotropic":1}},1:{"TiO2": {"function": self.TiO2_eps, "isotropic":1}, "SiO2": {"function":self.SiO2_eps,"isotropic":1}}, 2:{'MgO': {"function":self.MgO_eps,"isotropic":1}, 
        #                   "Ag": {"function":self.Ag_eps,"isotropic":1}, "Au": {"function":self.Au_eps,"isotropic":1}, "Pt": {"function":self.Pt_eps,"isotropic":1}},3:{"Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0},
        #                   "weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0}, "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0},
        #                   "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0},"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
        
        #Makes sense to do it this way to avoid weyl_material_3+
        # material_dict = { 0:{"Air": {"function": self.Air, "isotropic":1}},1:{"TiO2": {"function": self.TiO2_eps, "isotropic":1}, "SiO2": {"function":self.SiO2_eps,"isotropic":1}}, 2:{'MgO': {"function":self.MgO_eps,"isotropic":1}}, 
        #                   3:{"Ag": {"function":self.Ag_eps,"isotropic":1}, "Pt": {"function":self.Pt_eps,"isotropic":1}},4:{"Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0}},
        #                   5:{"weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0}},
        #                   6:{ "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0}},
        #                   7:{ "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0}},8:{"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}}, 9:{"Ge":{"function":self.Ge_eps,"isotropic":1}}, 10:{"weyl_material_6":{"function":self.weyl_material_6_eps,"isotropic":0}}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
        material_dict = { 0:{"Air": {"function": self.Air, "isotropic":1}},1:{"TiO2": {"function": self.TiO2_eps, "isotropic":1}, "SiO2": {"function":self.SiO2_eps,"isotropic":1}}, 2:{'MgO': {"function":self.MgO_eps,"isotropic":1}}, 
                          3:{"Ag": {"function":self.Ag_eps,"isotropic":1}, "Pt": {"function":self.Pt_eps,"isotropic":1}},4:{"Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0}},
                          5:{"weyl_material_1_EF_02": {"function":self.weyl_material_1_EF_02_eps,"isotropic":0},"weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_1_EF_01": {"function":self.weyl_material_1_EF_01_eps,"isotropic":0},"weyl_material_1_EF_007": {"function":self.weyl_material_1_EF_007_eps,"isotropic":0},"weyl_material_2_EF_02": {"function":self.weyl_material_2_EF_02_eps,"isotropic":0},
                             "weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0},
                          "weyl_material_2_EF_01": {"function":self.weyl_material_2_EF_01_eps,"isotropic":0},"weyl_material_2_EF_007": {"function":self.weyl_material_2_EF_007_eps,"isotropic":0}},6:{ "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0}},
                          7:{ "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0}},8:{"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}}, 9:{"Ge":{"function":self.Ge_eps,"isotropic":1}}, 10:{"weyl_material_6":{"function":self.weyl_material_6_eps,"isotropic":0}}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
       
        
    
        #No TiO2 yes HfO2
        # material_dict = { 0:{"Air": {"function": self.Air, "isotropic":1}},1:{"SiO2": {"function":self.SiO2_eps,"isotropic":1}}, 2:{'MgO': {"function":self.MgO_eps,"isotropic":1},"HfO2": {"function":self.HfO2_eps,"isotropic":1}}, 
        #                   3:{"Ag": {"function":self.Ag_eps,"isotropic":1}, "Pt": {"function":self.Pt_eps,"isotropic":1}},4:{"Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0}},
        #                   5:{"weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0}},6:{ "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0}},
        #                   7:{ "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0}},8:{"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}}, 9:{"Ge":{"function":self.Ge_eps,"isotropic":1}}, 10:{"weyl_material_6":{"function":self.weyl_material_6_eps,"isotropic":0}}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
        
        #############################TEST/ trouble shooting
        # material_dict = { 0:{"Air": {"function": self.Air, "isotropic":1}},1:{"TiO2": {"function": self.TiO2_eps, "isotropic":1}, "SiO2": {"function":self.SiO2_eps,"isotropic":1}}, 2:{'MgO': {"function":self.MgO_eps,"isotropic":1}}, 3:{"Au": {"function":self.Au_eps,"isotropic":1}},4:{"Co2MnGa": {"function":self.Co2MnGa_eps,"isotropic":0},
        #                   "weyl_material_1": {"function":self.weyl_material_1_eps,"isotropic":0},"weyl_material_2": {"function":self.weyl_material_2_eps,"isotropic":0}},5:{ "weyl_material_3": {"function":self.weyl_material_3_eps,"isotropic":0},
        #                   "weyl_material_4": {"function":self.weyl_material_4_eps,"isotropic":0},"weyl_material_5": {"function":self.weyl_material_5_eps,"isotropic":0}}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic
        # 0:Air
        # 1:Dielectric
        # 2:Isotropic Metal
        # 3:Weyl Semi-metal
        # 4:Doped Semi-conductor (not here yet)
        
        
        
        return material_dict
    def create_epsilon(self):
        material_dict=self.material_dict()
        # if len(self.material_dict_indices)!=self.N:
        #     raise ValueError("Number of layers 'N' must match length of'material_dict_indices' ")
        epsilon=np.zeros((self.N,3),dtype=np.complex_)
        #epsilon=np.zeros((self.N,3))
        #lambda_ = 2*pi*c/self.omega
        count=0
        flat_list = [item for sublist in self.material_dict_indices for item in sublist]
        # print("flat_list")
        # print(flat_list)
        for ii in flat_list: ##Fix this for new material dictionary
            # print("material")
            # print(ii)
            # print("number")
            # print(ii[1])
            # print('material_dict[ ii[0]][ ii[1]]')
            # print(material_dict[ ii[0]][ ii[1]])
       
            if material_dict[ ii[0]][ ii[1]]["isotropic"]==1:
                g=0
                value=material_dict[ ii[0]][ ii[1]]["function"](self.lambda_)
                # print("value")
                # print(value)
                epsilon[count][0]= value
                # print("value")
                # print(value)
                epsilon[count][1]= value
                if ii[2]=='g':
                    epsilon[count][2]= g
                if ii[2]=='-g':
                    epsilon[count][2]= -g
                # print("g")
                # print(g)
                
            elif material_dict[ ii[0]][ ii[1]]["isotropic"]==0:
                 eps_T,eps_L, g=material_dict[ ii[0]][ ii[1]]["function"](self.lambda_)
                 # print("eps_T")
                 # print(eps_T)
                 epsilon[count][0]= eps_T
                 # print("eps_T")
                 # print(epsilon[count][0])
                 epsilon[count][1]= eps_L
                 # print("eps_L")
                 # print(epsilon[count][1])
                 if ii[2]=='g':
                     epsilon[count][2]= g
                 if ii[2]=='-g':
                     epsilon[count][2]= -g
                 # print("g")
                 # print(g)
                 
            else:
                epsilon[count][0]= 0
                epsilon[count][1]= 0
                epsilon[count][2]= 0
            count+=1
        
        return np.round_(epsilon,decimals = 4)
    
    
    
    
#     # TEST BENCH
# ############################################
# omega=30  
# N=2
# material_dict_indices=["SiO2","SiO2"]
# x=Epsilon_Creator(omega,N,material_dict_indices)    
# lambda_=1910*(10**-9)
# a=x.Au_eps(lambda_)  

# a0=1000000*400*(10**-9)
###################################################
##TO DO: need to find a quicker way to compare the lambda input with that of the
##dataframe (involves too many steps)


# data = np.genfromtxt('bulk_eps_ef60meV_fine.dat')#, skip_header=1,skip_footer=1,names=True,dtype=None, delimiter=' ')  # Dielectric tensor of CMG.
# E = data[:,0]  # Energy [eV].
# omega = eV*E/hbar  # Angular frequency [rad/s].
# k = omega/c  # Wavevector in air [1/m].
# lambda_ = 2*pi/k 
# lambda_ = np.linspace(300,700,445)*(10**-9)
# omega=2*pi*c/lambda_
# #omega=[55]
# N=14
# material_dict_indices = [1,2,1,2,1,2,1,2,1,2,1,2,1,2]
# if len(material_dict_indices)!=N:
#         print("Number of layers 'N' must match length of'material_dict_indices' ")
# material_dict = { 1: {"material": TiO2_eps, "isotropic":1}, 2: {"material":SiO2_eps,"isotropic":1}} #can have more information. isotropic:1 means it isotropic, isotropic:0 means it anisotropic

# theta = np.array([0])  # Angle of incidence [deg].
# theta = theta*(pi/180)  # Angle of incidence [rad].
# t=[80e-9,115e-9,80e-9,115e-9,80e-9,115e-9,80e-9,115e-9,80e-9,115e-9,80e-9,115e-9,80e-9,115e-9]

# R=np.empty((len(theta),len(omega)))
# pol = 'p'  # Polarization.

# for ii in range(0,len(theta)):
#     for jj in range(0,len(omega)):
#         epsilon=epsilon_creator(omega[jj],N, material_dict, material_dict_indices)
#         gamma=magnetophotonicCrystal(omega[jj], theta[ii], N, epsilon, t, pol)
#         R[ii][jj]=gamma*np.conj(gamma)
# plt.plot((hbar*omega/eV).T,R[0]) 
# #plt.plot((lambda_).T,R[0]) 
