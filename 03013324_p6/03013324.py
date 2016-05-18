# -*- coding: utf-8 -*-
import xlrd    #打开EXCEL文件
import numpy as np
import matplotlib.pyplot as plt
from  statistics import mean,stdev,pstdev,variance,pvariance #平均值 标准差 方差
from prettytable import PrettyTable

excel = xlrd.open_workbook('data.xlsx')  
sheet = excel.sheets()[0]     #获取第一个sheet   
xx=[]
yy=[]
xxdata=[]
yydata=[]

for i in range(0,4): #获取数据存放在xx，yy列表中
    xx.append(sheet.col_values(2*i))
    yy.append(sheet.col_values(2*i+1))
    
def setData(x,y):     #进行数据处理
    xdata={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}
    ydata={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}

    xdata['avg']=round(mean(x),3)
    ydata['avg']=round(mean(y),3)

    xdata['stdev']=round(stdev(x),3)
    ydata['stdev']=round(stdev(y),3)

    xdata['pstdev']=round(pstdev(x),3)
    ydata['pstdev']=round(pstdev(y),3)

    xdata['var']=round(variance(x),3)
    ydata['var']=round(variance(y),3)

    xdata['pvar']=round(pvariance(x),3)
    ydata['pvar']=round(pvariance(y),3)

    return  xdata,ydata

def fitData(x,y): #回归
    a,b = np.polyfit(x,y,1)
    predictedY = a*np.array(x) + b
    return a,b,predictedY

def chulidata():
    datax=[]
    datay=[]
    for i in range(0,4):
        aa,bb=setData(xx[i],yy[i])
        datax.append(aa)
        datay.append(bb)
    return datax,datay
   
def printdata():
    table = PrettyTable(["data set","x-avg", "x-std", "x-pstd", "x-var","x-pvar","y-avg", "y-std", "y-pstd", "y-var","y-pvar"])
    table.align= "l" 
    table.padding_width = 1 
    for i in range(0,4):
        table.add_row([i,xxdata[i]['avg'],xxdata[i]['stdev'],xxdata[i]['pstdev'],xxdata[i]['var'],xxdata[i]['pvar'],
                         yydata[i]['avg'],yydata[i]['stdev'],yydata[i]['pstdev'],yydata[i]['var'],yydata[i]['pvar']])
    print(table)

def printfigure(x,y,a,b, predictedY):
    plt.plot(x,y, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x,predictedY,
               label = 'Y by\nlinear fit, y = '
               + str(round(a, 5))+'*x+'+str(round(b, 5)))
    plt.legend(loc = 'best')

def showfigure():

    fig=plt.figure(figsize=(12.0,8.0))
    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

    figcol=2
    figrow=2

    for i in range(0,4):
        aa,bb,cc=fitData(xx[i],yy[i])
        fig.add_subplot(figrow, figcol,i+1)
        printfigure(xx[i],yy[i],aa,bb,cc)

    plt.show()


xxdata,yydata=chulidata()
printdata()
showfigure()