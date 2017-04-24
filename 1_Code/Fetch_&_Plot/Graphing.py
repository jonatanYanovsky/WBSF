# Graphing
import plotly.plotly as py #Plotly Api
from plotly.tools import FigureFactory as FF
import plotly.graph_objs as obj
from plotly import tools
import time #To get time and date
import pandas_datareader.data as web #Database Reader
import json # JavaScript Object Notation
from plotly.graph_objs import * #Plotly Objects
import numpy as np #Numpy for Matrix Handling
import ArrayNCalc
from datetime import datetime
from datetime import timedelta
import pytz

#Function by Jon
def rsiPlot(stockSymbol,Webster,Predict, startYear): #plots all the graphs together

	figure=obj.Scatter(y=Webster.High,x=Webster.index,line=dict(color=('rgb(0,50,100)')),name="Past Data for "+stockSymbol) #Past Data Line

	Predicts=obj.Scatter(y=Predict,x=ArrayNCalc.getWorkDates(len(Predict)),line=dict(color=('rgb(255,165,0)')),name="RSI for "+stockSymbol) #Prediction Line

	fig = tools.make_subplots(rows=2, cols=1)
	
	fig.append_trace(figure, 1, 1) # subplot positions
	fig.append_trace(Predicts, 2, 1)
	
	fig['layout']['xaxis2'].update(range=[datetime(int(startYear),1,1), datetime.now()])

	fig['layout']['yaxis1'].update(title='Dollars ($)') # format the axes
	fig['layout']['yaxis2'].update(title='RSI percentage (%)', range=[0, 100])
	
	return py.plot(fig, filename=stockSymbol+'_Line')


#Function by Vince
def makeLineGraph(stockSymbol,Webster,currentInfo): # Makes Line graph for both historic data (webster), current Stock Info (currentInfo)

	figure=obj.Scatter(y=Webster.High,x=Webster.index) # Line 

	currentFigure=obj.Trace(y=currentInfo[0]['LastTradePrice'],x=currentInfo[0]['LastTradeDateTime'],line=dict(color=('rgb(0,0,0)'))) # Current Point Data

	data=[figure,currentFigure]

	py.plot(data, filename=stockSymbol+'_Line')
#Function by Vince
def makeCandleStickGraph(stockSymbol,Webster): # Makes a Candle Stick Graph

	fig=FF.create_candlestick(Webster.Open,Webster.High,Webster.Low,Webster.Close,dates=Webster.index) # Past Data

	py.plot(fig,filename=stockSymbol+'_Candle',validate=False)

#Function by Vince
def totalTogether(stockSymbol,Webster,currentInfo,Predict,Pointy,Rsi): #plots all the graphs together

	# Does not work in linux!!!
	temp = Webster.index
	temp = temp.tz_localize("UTC")
	
	figure=obj.Scatter(y=Webster.High,x=temp,line=dict(color=('rgb(0,50,100)')),name="Past Data for "+stockSymbol) #Past Data Line

	currentFigure=obj.Trace(y=currentInfo[0]['LastTradePrice'],x=currentInfo[0]['LastTradeDateTime'],line=dict(color=('rgb(0,0,0)')),name='Current Data for '+stockSymbol) #Current Point

	Predicts=obj.Scatter(y=Predict,x=ArrayNCalc.getWorkDates(len(Predict)),line=dict(color=('rgb(255,165,0)')),name="Prediction "+stockSymbol) #Prediction Line

	point=obj.Trace(y=Pointy,x=datetime.now(pytz.utc) + timedelta(days=1),line=dict(color=pointColorMaker(Pointy,currentInfo)),name="Prediction "+stockSymbol) #point of prediciton

	RSI=obj.Scatter(y=Rsi,x=ArrayNCalc.getWorkDates(len(Rsi)),line=dict(color=('rgb(0,0,0)')),name="RSI for "+stockSymbol) #Prediction Line

	fig=tools.make_subplots(rows=2,cols=1)

	#data=Data([figure,currentFigure,Predicts, point]) #Data Array of Figures
	data=Data([Predicts, point,currentFigure,figure])
	fig.append_trace(data[0],1,1)
	fig.append_trace(data[1],1,1)
	fig.append_trace(data[2],1,1)
	fig.append_trace(data[3],1,1)

	fig.append_trace(RSI,2,1)


	fig['layout']['yaxis1'].update(title='Dollars ($)',domain=[0,0.7])
	fig['layout']['yaxis2'].update(title='RSI percentage (%)', range=[0, 100],domain=[0.8,1])

	return py.plot(fig, filename=stockSymbol+'_Line') #Plot The Function

#Function by Vince
def pointColorMaker(point,currentInfo):
	currentInfo=float(currentInfo[0]["LastTradePrice"])
	if(currentInfo>point):
		return "rgb(255,0,0)"
	if(currentInfo<point):
		return "rgb(0,255,0)"

	return "rgb(0,0,0)"
	
