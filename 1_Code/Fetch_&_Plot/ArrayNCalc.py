# Array Manip / Calculations
import time # Time
import pandas_datareader.data as web #Database reader
import numpy as np #Numpy
import pandas as pd #Pandas Data Reader
import time #Time
import holidays
import string
from datetime import date
from math import floor #math floor
from math import pow #math pow
from datetime import datetime # Date
from datetime import timedelta # Adding to date

# Function by Jon
# assume that we are not storing confidence data in a dB, so we cannot calculate prediction over time
def CalculateConfidenceRating(predictedValues, historicalValues):
	# there will be more data points from historicalValues than predictedValues so
	# cut off part of historicalIndex, to make the two "list-indexes" the same length
	numDataPoints = len(predictedValues)
	historicalIndex = len(historicalValues) - numDataPoints
	
	percentError = [numDataPoints] # declare an array of size numDataPoints

	for i in range(0, numDataPoints - 1): # initialize array with all zeros
  		percentError.append(0)
		
	# perform percent error formula with each array elements from predictedValues and historicalValues
	for i in range(0, numDataPoints - 1):
		percentError[i] = 100 * abs(predictedValues[i] - historicalValues[historicalIndex + i]) / historicalValues[historicalIndex + i]
	
	avgPercentError = 0
	for i in range(0, numDataPoints - 1):  # sum elements from percentError
		avgPercentError += percentError[i]
	avgPercentError /= numDataPoints # find the average

	return avgPercentError # return avg percent error

	#Function by Vince
def CalculateRelativeACC(predictionValues,actualValues):

	limit=len(predictionValues)

	A=differenceBetweenDataPoints(predictionValues)

	B=differenceBetweenDataPointsLimit(actualValues,limit)

	Exe=0
	
	for x in range(0,limit-2):
		Exe+=abs(A[x]-B[x+1])/((abs(A[x])+abs(B[x+1]))/2)
		pass
	Exe=floor(Exe/200*100)
	return (Exe)

	#Function by Vince
def differenceBetweenDataPoints(Pulled_Data): # get the differences and normalize the data

	diff1=Pulled_Data[len(Pulled_Data)-1] - Pulled_Data[len(Pulled_Data)-2]

	diff2=Pulled_Data[len(Pulled_Data)-2] - Pulled_Data[len(Pulled_Data)-3]

	Difference_Array=np.array(diff1)

	Difference_Array=np.append(Difference_Array,diff2)

	for x in range(len(Pulled_Data)-3,0,-1):

		diff=Pulled_Data[x]-Pulled_Data[x-1]

		Difference_Array=np.append(Difference_Array,diff)

		pass

	Difference_Array=np.flip(Difference_Array,0)

	return Difference_Array
	#Function by Vince
def differenceBetweenDataPointsLimit(Pulled_Data,limit): # get the differences and normalize the data
	
	length=len(Pulled_Data)-1

	diff1=Pulled_Data[length] - Pulled_Data[length-2]

	diff2=Pulled_Data[length-2] - Pulled_Data[length-3]

	Difference_Array=np.array(diff1)

	Difference_Array=np.append(Difference_Array,diff2)

	for x in range(length-3,length-limit,-1):

		diff=Pulled_Data[x]-Pulled_Data[x-1]

		Difference_Array=np.append(Difference_Array,diff)

		pass

	Difference_Array=np.flip(Difference_Array,0)

	return Difference_Array
	#Function by Vince
def Normalize(differData,baseData):

	y=len(baseData)-1;

	l=len(differData)-1;

	differData[l]=baseData[y]+differData[l]

	y-=1
	for x in range(l,0,-1):
		Min=baseData[y]-.25*baseData[y]
		Max=.25*baseData[y]+baseData[y]
		differData[x]=baseData[y]+(differData[x]/(Max-Min))
		y-=1
		pass
		
	differData[0]=differData[1]
	differData[len(differData)-1]=differData[len(differData)-2]
	return differData

	#(Prediction DO NOT TOUCH WIHTOUT NOTIFYING ME)
	#Function by Vince
def setAxis(startYear): #find the number of days between two dates

	i=(int(time.strftime("%Y")) - int(startYear))*365 + currentDayCount() + int(time.strftime("%d"))+1

	return i;

	#(Gets the amount of days between 2 points)
	#Function by Vince
def currentDayCount(): #Find the month days

	i=int(time.strftime("%m"))

	sum=0;

	for x in range(1,12):

		day_inMonth=28 +(x+floor(x/8))%2 + 2 % x + 2*floor(1/x)

		sum+=day_inMonth

		if x==i-1:

			break
		pass

	return sum
	#Function by Vince
def getWorkDates(length):

	us_holidays = holidays.UnitedStates()

	a=np.array(datetime.now())

	for x in range(1,length):

		a=np.append(a,datetime.now())

		pass

	x=0

	for y in range(45,0,-1):
		
		Date=datetime.now()+timedelta(days=-y)

		if Date.weekday()<=4 and not (Date in us_holidays) :
			a[x]=Date
			x+=1
			pass

		if(x==length):
			break

		pass
		print(a)
	return a
	#(Prediction DO NOT TOUCH WIHTOUT NOTIFYING ME)C:\\cygwin\bin\Main.py
