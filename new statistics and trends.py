# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 06:02:40 2022

@author: Lenovo
"""
#importing libraries
import pandas as pa
import matplotlib.pyplot as pyp
import numpy as n
from scipy import stats

"""
                      #BAR GRAPH 1
"""
def readFile(filename):
    '''
        This function is created to read csv files, to display transposed file
        and to display specific drop unwanted columns
    
        Returns
        -------
        df : variable for storing csv file
        df_t: variable for storing transposed csv file
        df_drop:variable for  storing unwanted columns 
    '''
    df = pa.read_csv(f"{filename}.csv")
    df_drop= df.drop(['Country Code', 'Indicator Name', \
                                'Indicator Code'], axis=1)
    df_t= pa.DataFrame.transpose(df)
    return df,df_drop,df_t

# calling function above to display dataframe
df,df_drop,df_t= readFile("ELECTRICITY HYDRO")
print("\nDataset for Bar Graph 1 : \n", df)
print("\nTransposed file of dataset: \n",df_t)
print("\nDropped columns from the dataset  : \n", df_drop)

#selecting the rows to be plotted 
select_row=df.iloc[[7,20,25,30,35,65,71,236],:]
print(select_row)

#removing NaN's
null_drop=select_row.dropna()
print(null_drop)

#setting the index
col=(select_row["Country Name"])

x=n.arange(len(col))

m1=(select_row["1971"])
m2=(select_row["1975"])
m3=(select_row["1980"])
m4=(select_row["1985"])
m5=(select_row["1990"])
m6=(select_row["1995"])
m7=(select_row["2000"])

#plotting the bar graph 
pyp.figure(figsize=(10,10))
pyp.title("Production From Hydroelecctricity Sources (% of total)")
pyp.bar(x-0.2,m1,0.1,label='1971')
pyp.bar(x-0.1,m2,0.1,label='1975')
pyp.bar(x+0,m3,0.1,label='1980')
pyp.bar(x+0.1,m4,0.1,label='1985')
pyp.bar(x+0.3,m5,0.1,label='1990')
pyp.bar(x+0.4,m6,0.1,label='1995')
pyp.bar(x+0.2,m7,0.1,label='2000')

# manipulating ticks on x & y axix
pyp.xticks(x,col,rotation=45)

pyp.xlabel("Countries uses Hydroelectric Sources in Production of Electricity")
pyp.ylabel("(% of total)")
pyp.savefig("Production of electricity from the Hydroelectric resources.png")
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.show()

#Applying Statistical tools 
mean_df_hydro= n.mean(df)
print("Average production of Electricity from Hydroelectric Sources = ",mean_df_hydro)

# calculating Normal Distribution of particular year through "scipy" module
print("\nNormal Distribution: \n", stats.skew(df["1971"]))

#calculating the standard deviation of particular dataset
std_dev= n.std(df)
print("standard deviation of production of electricity from the Hydroelectric source in each year=",std_dev)
"""                 

 BAR GRAPH 2
 
"""
# calling function above to display dataframe
df_coal,df_drop_coal,df_t= readFile("COAL")
print("\nDataset for Bar Graph 2 : \n", df_coal)
print("\nTransposed file of dataset: \n",df_t)
print("\nDropped columns from the dataset  : \n", df_drop_coal)


select_row=df_coal.iloc[[5,16,19,24,29,59,65,230],:]
print(select_row)


#remove Nan
null_drop=select_row.dropna()
print(null_drop)

col=(select_row["Country Name"])
#arranging the axis 
x=n.arange(len(col))
m1=(select_row["1971"])
m2=(select_row["1975"])
m3=(select_row["1980"])
m4=(select_row["1985"])
m5=(select_row["1990"])
m6=(select_row["1995"])
m7=(select_row["2000"])

#plotting bar graph 
pyp.figure(figsize=(10,10))
pyp.title("Production From Coal Sources (% of total)")
pyp.bar(x-0.2,m1,0.1,label='1971')
pyp.bar(x-0.1,m2,0.1,label='1975')
pyp.bar(x+0,m3,0.1,label='1980')
pyp.bar(x+0.1,m4,0.1,label='1985')
pyp.bar(x+0.3,m5,0.1,label='1990')
pyp.bar(x+0.4,m6,0.1,label='1995')
pyp.bar(x+0.2,m7,0.1,label='2000')

# manipulating ticks on x & y axis
pyp.xticks(x,col,rotation=45)
pyp.xlabel("Countries")
pyp.ylabel("(% of total)")

#bbox_to_anchor to place legend outside the axes such that the center left 
#corner of the legend is at position
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.savefig("Production of electricity from the coal resources.png")
pyp.show()

#Applying Statistical tools 
mean_df_coal= n.mean(df_coal)
print("Average production of Electricity from Coal Sources = ",mean_df_coal)

# calculating Normal Distribution of particular year through "scipy" module
print("\nNormal Distribution: \n", stats.skew(df["2000"]))
std_dev= n.std(df_coal)
print("standard deviation of production of Electricity from the Coal source in each year=",std_dev)

"""
line graph
"""
def readFile(a):
    '''
        This function is created to read csv files, to display transposed file
        and to display specific drop unwanted columns 
        
        Parameters
        ----------
        c : csv filename
    
        Returns
        -------
        population : variable for storing csv file
        population_t : variable for storing transposed csv file

    '''
    population = pa.read_csv("TOTAL POPULATION.csv");
    population = population.drop(['Country Code', 'Indicator Name', 'Indicator Code'], \
                   axis=1)
    population_t= pa.DataFrame.transpose(population)
    return population, population_t

# calling function above to display dataframe
population, population_t = readFile("TOTAL POPULATION .csv")
print("\nPopulation: \n", population)
print("\nTranposed Population: \n", population_t)


# populating header with header information
header3 = population_t.iloc[0].values.tolist()
population_t.columns = header3
print("\nPopulation Header: \n", population_t)


# removing first two lines
population_t = population_t.iloc[2:]
print("\nRemoving first two lines from population: \n", population_t)

# arranging length of column
print(len(population_t))

# extracting particular countries and storing it in a variable
population_t = population_t[population_t["Australia"].notna()]
population_t = population_t[population_t["Brazil"].notna()]
population_t = population_t[population_t["Canada"].notna()]
population_t = population_t[population_t["China"].notna()]
population_t = population_t[population_t["Colombia"].notna()]
population_t = population_t[population_t["Finland"].notna()]
population_t = population_t[population_t["United Kingdom"].notna()]
population_t = population_t[population_t["Tanzania"].notna()]

# indexing change as integer type
population_t.index = population_t.index.astype(int)

# plotting figure and adjusting figure size in plot
pyp.figure(figsize=(10,10))

# line graph plot
pyp.plot(population_t.index, population_t["Australia"], label="Australia", linestyle='dashed')
pyp.plot(population_t.index, population_t["Brazil"], label="Brazil", linestyle='dashed')
pyp.plot(population_t.index, population_t["Canada"], label="Canada", linestyle='dashed')
pyp.plot(population_t.index, population_t["China"], label="China", linestyle='dashed')
pyp.plot(population_t.index, population_t["Colombia"], label="Colombia", linestyle='dashed')
pyp.plot(population_t.index, population_t["Finland"], label="Finland", linestyle='dashed')
pyp.plot(population_t.index, population_t["United Kingdom"], label="United Kingdom", linestyle='dashed')
pyp.plot(population_t.index, population_t["Tanzania"], label="Tanzania", linestyle='dashed')

# manipulating ticks on x & y axis
pyp.xticks(fontsize=10)
pyp.yticks(fontsize=10)

pyp.title("Population Total", fontsize=10)
pyp.xlabel("Year", fontsize=10)
pyp.ylabel("Figures of population", fontsize=10)
pyp.savefig("TOATAL POPULATION WORLDWIDE.png")
pyp.legend(bbox_to_anchor=(1,0.5), loc="center left", fontsize=10)
pyp.show()

""" line graph 2"""
def readFile(d):
    '''
        This function is created to read csv files, to display transposed file
        and to display specific drop unwanted columns
        
        Parameters
        ----------
        d : csv filename
    
        Returns
        -------
        brth : variable for storing csv file
        brth_t : variable for storing transposed csv file

    '''
    brth = pa.read_csv("BIRTH RATE.csv");
    brth = pa.read_csv(d)
    brth = brth.drop(['Country Code', 'Indicator Name', 'Indicator Code']
                      , axis=1)
    brth_t = pa.DataFrame.transpose(brth)
    return brth, brth_t

# calling function above to display dataframe
brth, brth_t = readFile("BIRTH RATE.csv")
print("\nBirth rate : \n", brth)
print("\nTransposed data: \n", brth_t)

# populating header with header information
header4 = brth_t.iloc[0].values.tolist()
brth_t.columns = header4
print("\nHeader  of Birth rate: \n", brth_t)

# removing first two lines
brth_t = brth_t.iloc[2:]
print("\nRemoving first two lines from data: \n", brth_t)

# arranging length of column
print(len(brth_t))

# extracting particular countries and storing it in a variable
brth_t = brth_t[brth_t["Austria"].notna()]
brth_t = brth_t[brth_t["Brazil"].notna()]
brth_t = brth_t[brth_t["Canada"].notna()]
brth_t = brth_t[brth_t["China"].notna()]
brth_t = brth_t[brth_t["Colombia"].notna()]
brth_t = brth_t[brth_t["Finland"].notna()]
brth_t = brth_t[brth_t["United Kingdom"].notna()]
brth_t = brth_t[brth_t["Tanzania"].notna()]

# indexing change as integer type
brth_t.index = brth_t.index.astype(int)

# plotting figure and adjusting figure size in plot
pyp.figure(figsize=(10,10))

# line graph plot
pyp.plot(brth_t.index, brth_t["Australia"], label="Australia", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["Brazil"], label="Brazil", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["Canada"], label="Canada", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["China"], label="China", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["Colombia"], label="Colombia", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["Finland"], label="Finland", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["United Kingdom"], label="United Kindgdom", linestyle='dashed')
pyp.plot(brth_t.index, brth_t["Tanzania"], label="Tanzania", linestyle='dashed')

# manipulating ticks on x & y axis
pyp.xticks(fontsize=13)
pyp.yticks(fontsize=13)

pyp.title("Birth rate, crude (per 1,000 people)", fontsize=15)
pyp.xlabel("Year", fontsize=15)
pyp.ylabel("% of birth rate ", fontsize=15)
pyp.legend(bbox_to_anchor=(1.0,0.5), loc="center left", fontsize=13)
pyp.savefig("BIRTH RATE PER 1000 PEOPLE.png")
pyp.show()



    
  

    
  