import random
import plotly.figure_factory as ff
import statistics

diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)

mean = statistics.mean(diceresult)
mode = statistics.mode(diceresult)
median = statistics.median(diceresult)
standardivision = statistics.stdev(diceresult)

#print (mean)
#print (mode)
#print (median)
#print (standardivision)

fig = ff.create_distplot([diceresult],["count"],show_hist=False)
fig.show()

firststart,firstend,secondstart,secondend,thirdstart,thirdend = mean - standardivision,mean + standardivision,mean - 2*standardivision,mean + 2*standardivision,mean - 3*standardivision,mean + 3*standardivision
firstlist = [result for result in diceresult if result > firststart and result < firstend]
secondlist = [result for result in diceresult if result > secondstart and result < secondend]
thirdlist = [result for result in diceresult if result > thirdstart and result < thirdend]

firstpercentage = len(firstlist)*100/len(diceresult)
secondpercentage = len(secondlist)*100/len(diceresult)
thirdpercentage = len(thirdlist)*100/len(diceresult)

print (firstpercentage)
print (secondpercentage)
print (thirdpercentage)
