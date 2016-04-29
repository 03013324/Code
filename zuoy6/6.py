import xlrd    #打开EXCEL文件
import numpy as np
import matplotlib.pyplot as plt
from  statistics import mean,stdev,variance #平均值 标准差 方差
excel = xlrd.open_workbook('data.xlsx')  
sheet = excel.sheets()[0]     #获取第一个sheet    

#输出平均值
for i in range(0,8):
    print('第',i+1,'列平均值为',mean(sheet.col_values(i)))

#标准差
for i in range(0,8):
    print('第',i+1,'列标准差为',stdev(sheet.col_values(i)))
 
    
#方差
for i in range(0,8):
    print('第',i+1,'列方差为',variance(sheet.col_values(i)))
 
# 计算系数
def xishu(xx,yy):        #用以计算皮尔逊相关系数r
    a,b,c=0,0,0
    for i in range(len(xx)):
        sum1=xx[i]-mean(xx)
        sum2=yy[i]-mean(yy)
        a+=(sum1*sum2)
        sum3=(xx[i]-mean(xx))**2
        sum4=(yy[i]-mean(yy))**2
        b+=sum3
        c+=sum4
    return a/((b*c)**0.5)  

for i in range(0,4):
    print ('相关系数分别为',xishu(sheet.col_values(2*i),sheet.col_values(2*i+1)))
#回归直线
def huigui(sj1,sj2):
    sj1s=np.array(sj1)
    sj2s=np.array(sj2)
    xsa,xsb=np.polyfit(sj1s,sj2s,1)
    y0=xsa*sj1s+xsb
    return y0


#作图 
for i in range (0,4):
    plt.figure(i)
    plt.plot(sheet.col_values(2*i),sheet.col_values(2*i),'ro') 
    plt.xlabel('x')
    plt.ylabel('y')   
    plt.plot(sheet.col_values(2*i),huigui(sheet.col_values(2*i),sheet.col_values(2*i+1))) 
plt.show()

