#Iris class
#including modole data 
class IrisModel(object):
    def __init__(self, label_n, item_n):
        self.P_c = []    #P(c)相关类别的先验概率列表
        self.D_c = []    #D(c)相关类别的训练样本总量
        self.D   = 0     #data num训练样本总量
        self.P_x_c = []  #P(xi|c)属性基于类别的后验概率的模型值,连续函数为正态分布的两个参数
        n = label_n
        #初始化相关参数
        while(n):
            self.P_c.append(0)
            self.D_c.append(0)
            self.P_x_c.append([])
            n = n -1
        for x in range(0,label_n):
            for i in range(0,item_n):
                self.P_x_c[x].append([])
                for j in range(0,2):
                    self.P_x_c[x][i].append([])
