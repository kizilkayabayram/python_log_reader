#!/usr/bin/python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime

if len(sys.argv) != 2:
    print("Give log file as an argument")
    quit()

file_name = sys.argv[1]
df = pd.read_csv(file_name, index_col='t')
df_T = df.T

time_ep = df_T.columns

disp_ax= False
disp_gx=False
disp_ex=False

if 'ax' in df_T.index.to_list():
    disp_ax=True

if 'gx' in df_T.index.to_list():
    disp_gx=True

if 'ex' in df_T.index.to_list():
    disp_ex=True

if disp_ax:
    # ACC
    fg0=plt.figure(0)
    fg0.suptitle('Acc', fontsize=20)

    ax_plt = df_T.loc['ax']
    ay_plt = df_T.loc['ay']
    az_plt = df_T.loc['az']

    plt.plot(time_ep,ax_plt,'b-', label='ax')
    plt.plot(time_ep,ay_plt,'g-', label='ay')
    plt.plot(time_ep,az_plt,'r-', label='az')
    plt.legend()
    plt.ylabel("m/s^2")

if disp_gx:
    # GYRO
    fg1=plt.figure(1)
    fg1.suptitle('Gyro', fontsize=20)

    gx_plt = df_T.loc['gx']
    gy_plt = df_T.loc['gy']
    gz_plt = df_T.loc['gz']

    plt.plot(time_ep,gx_plt,'b-', label='gx')
    plt.plot(time_ep,gy_plt,'g-', label='gy')
    plt.plot(time_ep,gz_plt,'r-', label='gz')
    plt.legend()
    plt.ylabel("rad/s")

if disp_ex:
    # Euler
    fg2=plt.figure(2)
    fg2.suptitle('Euler', fontsize=20)

    ex_plt = df_T.loc['ex']
    ey_plt = df_T.loc['ey']
    ez_plt = df_T.loc['ez']

    plt.plot(time_ep,ex_plt,'b-', label='ex')
    plt.plot(time_ep,ey_plt,'g-', label='ey')
    plt.plot(time_ep,ez_plt,'r-', label='ez')
    plt.legend()
    plt.ylabel("degrees")

plt.show()
