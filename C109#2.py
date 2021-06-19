from numpy import result_type
from pandas._config.config import reset_option
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("data.csv")
heightlist = df["Height(Inches)"].tolist()
mean = statistics.mean(heightlist)
mode = statistics.mode(heightlist)
median  = statistics.median(heightlist)
standartdivision = statistics.stdev(heightlist)

#print (mean)
#print (mode)
#print (median)
#print (standartdivision)

fig = ff.create_distplot([heightlist],["count"],show_hist=False)
fig.show()

firststart,firstend,secondstart,secondend,thirdstart,thirdend = mean - standartdivision,mean + standartdivision,mean - 2*standartdivision,mean + 2*standartdivision,mean - 3*standartdivision,mean + 3*standartdivision
firstlist = [result for result in heightlist if result > firststart and result < firstend]
secondlist = [result for result in heightlist if result > secondstart and result < secondend]
thirdlist = [result for result in heightlist if result > thirdstart and result < thirdend]

firstpercentage = len(firstlist)*100/len(heightlist)
secondpercentage = len(secondlist)*100/len(heightlist)
thirdpercentage = len(thirdlist)*100/len(heightlist)

print (firstpercentage)
print (secondpercentage)
print (thirdpercentage)
