# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:14:08 2022

@author: sware
"""
#import pandas and matplotlib modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Define a function readf to read the csv files containing data
def readf(filename):
    df = pd.read_csv(filename)#read the data into df 
    #print("Standard Deviation\n", np.std(df))
    dft = df.set_index('Country Name').transpose()#transpose the data and save it into dft 
    return df, dft #return df and dft to readf function call

Countries =['Afghanistan','Bulgaria','Brazil','Jamaica','Philippines','Tajikistan','Yemen, Rep.'] #create array Country and select the countries that needs to be analyased 
#define a fucntion barchartdata 
def barchart_data(df): 
    df = df[['Country Name', '2000','2003','2006','2009','2012','2015']]
    df = df[(df['Country Name'] == "Afghanistan")|
            (df['Country Name'] == "Bulgaria")|
            (df['Country Name'] == "Brazil")|
            (df['Country Name'] == "Jamaica")|
            (df['Country Name'] == "Philippines")|
            (df['Country Name'] == "Tajikistan")|
            (df['Country Name'] == "Yemen, Rep.")]
    return df #return data df

#create function barplot along with arguments ie data and labels to plot the bar graph
def barplot(df, lab1, lab2):
    plt.figure(figsize=(25,18))#set the figure size
    dx = plt.subplot(1,1,1)
    x = np.arange(7)
    width = 0.1 #set the width of each bar
    bar1 = dx.bar(x, df["2000"], width, label='2000')#plot the first bar of year 2000
    bar2 = dx.bar(x+width, df["2003"], width, label='2003')#plot the first bar of year 2003
    bar3 = dx.bar(x+width*2, df["2006"], width, label='2006')#plot the first bar of year 2006
    bar4 = dx.bar(x+width*3, df["2009"], width, label='2009')#plot the first bar of year 2009
    bar4 = dx.bar(x+width*4, df["2012"], width, label='2012')#plot the first bar of year 2012
    bar4 = dx.bar(x+width*5, df["2015"], width, label='2015') #plot the first bar of year 2015   
    dx.set_xlabel("Countries",fontsize=40)#set the label to be displayed on x axis with fontsize 
    dx.set_ylabel(lab1,fontsize=40)#set the label to be displayed on y axis with fontsize 
    dx.set_title(lab2,fontsize=40)#set the title to be displayed with fontsize 
    dx.set_xticks(x, Countries,fontsize=30,rotation=90)#set the xtick value with fontsize and degree of rotation
    dx.legend(fontsize=30)#call the legedn fucntion to represent the labels
    plt.show()#call the show function to display the chart

#create function to display line graph along with the arguments ie data and the labels    
def lineplot(df,lab1,lab2):
    plt.figure(figsize=(25,15))#set the figure size
    ss=df.set_index('Country Name')#set Country Name as the index
    trans = ss.transpose()#transpose the data and save it to trans
    for i in range(len(Countries)):#for loop to select all the 6 countries one by one
        plt.plot(trans.index,trans[Countries[i]],label=Countries[i])#plot the linegraph using plot function
    plt.title(lab2,fontsize=40)#set the title to be displayed with fontsize
    plt.xlabel("Years",fontsize=40)#set the label to be displayed on x axis with fontsize 
    plt.ylabel(lab1,fontsize=40)#set the label to be displayed on y axis with fontsize 
    plt.xticks(fontsize=30)#set the xtick value with fontsize and degree of rotation
    plt.legend(fontsize=30)#call the legedn fucntion to represent the labels
    plt.show()#call the show function to display the chart
    
#call the readf fucntion to read all the csv files and assign these values to the respective variables-one to store the original data and the second one to store the transposed data    
f_data1, f_data2 =readf(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT2-Statistics and trends\Access to clean fuels.csv")
w_data1, w_data2 =readf(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT2-Statistics and trends\freshwater.csv")
e_data1, e_data2 =readf(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT2-Statistics and trends\electricity.csv")
o_data1, o_data2 =readf(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT2-Statistics and trends\electricity coal oil.csv")

#call the barchart function to display bar charts of the provided data
e_data1 =barchart_data(e_data1)
barplot(e_data1, "% of population","Access to electricity")
f_data1 =barchart_data(f_data1)
barplot(f_data1, "% of population","Access to clean fuels and technologies for cooking")

#call the lineplot function to display line charts of the provided data
o_data1 =barchart_data(o_data1)
lineplot(o_data1, "% of electricity","Electricity produced from oil,gas and coal sources")
w_data1 =barchart_data(w_data1)
lineplot(w_data1, "% of water","Freshwater withdrawal")





        
    

