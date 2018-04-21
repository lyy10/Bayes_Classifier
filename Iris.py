#Iris class
#including modole data 
class IrisModel(object):
    def __init__(self, label_n, item_n):
        self.P_c = []    #P(c)
        self.D_c = []    #D(c)
        self.D   = 0     #data num
        self.P_x_c = []  #P(xi|c)
        n = label_n
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
