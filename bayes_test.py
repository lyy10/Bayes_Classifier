# -*- coding: utf-8 -*-
# test
from math import sqrt
from math import exp
import Iris
import string
"""该程序为: 朴素贝叶斯分类器
   是基于概率框架下实施决策的一种方法。
   该分类器前提假设：属性条件独立性
   对于连续性属性值，考虑概率密度函数，函数为正态分布
   理论方法见书'机器学习-周志华'150-151页
   2018-04-20 by Lyy
   """
def Train(iris, setosa_item, label):
    """函数为训练模型函数
       iris 为模型类，类中包含对于类别的前验概率和属性基于类别的后验概率等等
       setosa 为带有setosa标签的数据列表
       label 为第几类值为0-2"""
    iris.D_c[label] = len(setosa_item)
    iris.P_c[label] = float(iris.D_c[label])/iris.D
    average =[0, 0, 0, 0]
    for item in setosa_item:
        for i in range(0,4):
            average[i] += item[i]
    for i in range(0,4):
        average[i] = float(average[i])/iris.D_c[label]
        iris.P_x_c[label][i][0] = average[i]
    viriance = [0, 0, 0, 0]
    for item in setosa_item:
        for i in range(0,4):
            viriance[i] += (average[i]-item[i])**2
    for i in range(0,4):
        viriance[i] = float(viriance[i])/iris.D_c[label]
    for i in range(0,4):
        iris.P_x_c[label][i][1] = viriance[i]

iris = Iris.IrisModel(3,4)
iris_object = open("iris_data.txt")
item = []
setosa_item = []
versicolor_item = []
virginica_item = []
#读文件,并将相关一类的标签分发到对应的列表中
for line in iris_object:
    for k in range(0,4):
        item.append(float(line.split(',')[k]))
    item.append(line.split(',')[4].strip())
    if item[4] == 'Iris-setosa':
        setosa_item.append(item)
    elif item[4] == 'Iris-versicolor':
        versicolor_item.append(item)
    else:
        virginica_item.append(item)
    item = []
############ 拆分数据 #############
sign = 0
for i in range(10,45): #修改测试集和训练集的比例
    item.append(setosa_item[i-sign])
    item.append(versicolor_item[i-sign])
    item.append(virginica_item[i-sign])
    del setosa_item[i-sign]
    del versicolor_item[i-sign]
    del virginica_item[i-sign]
    sign += 1
##################################
iris.D = len(setosa_item) + len(versicolor_item) + len(virginica_item)
print("训练集")
print(iris.D)
print("测试集")
print(len(item))
#调用函数进行训练
Train(iris,setosa_item,0)
Train(iris,versicolor_item,1)
Train(iris,virginica_item,2)
#print(iris.P_x_c)
iris_object.close

########## test #########
def Comput_P(iris, item, label):
    """使用模型计算相关的预测概率
       iris 为模型类
       item 为一个记录,预测该记录属于哪一类
       label 为计算该记录在label类上的对应预测概率,值为1-3"""
    P = 1
    P *= iris.P_c[label-1]
    for i in range(0,4):
        P *= 1/(sqrt(2*3.1415926)*sqrt(iris.P_x_c[label-1][i][1]))*(exp(-((item[i]-iris.P_x_c[label-1][i][0])**2/(2*iris.P_x_c[label-1][i][1]))))
    return P

#iris_test = open('test.txt')
#item = []
#for line in iris_test:
#    for k in range(0,4):
    #    item.append(float(line.split(',')[k]))
   # item.append(line.split(',')[4].strip())
right = 0
for i in item:
    P1 = Comput_P(iris, i, 1)
    P2 = Comput_P(iris, i, 2)
    P3 = Comput_P(iris, i, 3)
    #print(i)
    if P1 < P2:
        if P2 < P3:
            #print(" is Virginica")
            if i[4][5:] == "virginica":
                right += 1
        else:
            #print(" is Versicolor")
            if i[4][5:] == "versicolor":
                right += 1
    elif P1 < P3:
        #print(" is Virginica")
        if i[4][5:] == "virginica":
            right += 1
    else:
        #print(" is Setosa")
        if i[4][5:] == "setosa":
            right += 1
    #item = []
print(right/len(item))
