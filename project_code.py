'''
show the annual GDP of chongqing, total energy consumption, energy consumption 
composition and energy consumption per unit of GDP of selected year. 
Author: Xiaoxi Guo
Date: 27-05-2020
'''

from tkinter import *
from tkinter.ttk import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def readfile(filename):
    '''return a list contains year/gdp/total/coal/gas/oil/other 
       by given csv files
    '''
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    result = ''.join(lines)
    result = result.split('\n')
    result = result[1:-1]
    result1 = []
    for i in result:
        i = i.split(',')
        result1.append(i)
    return result1


class GDPEnergy:
    '''define the GDPEnergy class'''
    
    def __init__(self, window, result):
        '''setup the label, combobox and button on given window'''
        self.result = result
        self.years = list(range(1980, 2018))
        
        self.combo = Combobox(window, values=self.years, width = 8, justify = LEFT)
        self.combo.grid(row=1, column=0, padx=(0,20), pady=20)
        self.label = Label(window, text = "Please select the year you want to ch\
eck. ", font =('Arial', 18))
        self.label.grid(row=0, column=0, padx=(20, 0), pady=10)
        self.button = Button(window, text = "check", command=self.message)
        self.button.grid(row=2, column=0, pady = 20)
        self.label1 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial Black', 12))
        self.label1.grid(row=3, column=0, padx=(20, 0), pady=10)
        self.label2 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label2.grid(row=4, column=0, padx=(20, 0), pady=10)
        self.label3 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label3.grid(row=5, column=0, padx=(20, 0), pady=10)
        self.label4 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label4.grid(row=6, column=0, padx=(20, 0), pady=10)
        self.label5 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial Black', 12))
        self.label5.grid(row=7, column=0, padx=(20, 0), pady=10)
        self.label6 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label6.grid(row=8, column=0, padx=(20, 0), pady=10)
        self.label7 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label7.grid(row=9, column=0, padx=(20, 0), pady=10)
        self.label8 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label8.grid(row=10, column=0, padx=(20, 0), pady=10)
        self.label9 = Label(window, text = " ", justify = LEFT, width = 140, \
                            font =('Arial', 12))
        self.label9.grid(row=11, column=0, padx=(20, 0), pady=10) 
        
      
        
    def index(self):
        '''return the index of the year combobox provide'''
        return int(self.combo.get()) - 1980
    
    def gdp(self):
        '''return GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][1])/10
    
    def energy(self):
        '''return total energy consumption of the year'''
        i = GDPEnergy.index(self)
        return self.result[i][2]  
    
    def coal(self):
        '''return coal consumption of the year'''
        i = GDPEnergy.index(self)
        return self.result[i][3]
    
    def gas(self):
        '''return gas consumption of the year'''
        i = GDPEnergy.index(self)
        return self.result[i][4]  
    
    def oil(self):
        '''return oil consumption of the year'''
        i = GDPEnergy.index(self)
        return self.result[i][5] 
    
    def other(self):
        '''return other energy consumption of the year'''
        i = GDPEnergy.index(self)
        return self.result[i][6] 
    
    def uni_gdp_energy(self):
        '''return total energy consumption for per unit GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][2])/(float(self.result[i][1])/10)
    
    def uni_gdp_coal(self):
        '''return coal consumption for per unit GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][3])/(float(self.result[i][1])/10)
    
    def uni_gdp_gas(self):
        '''return gas consumption for per unit GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][4])/(float(self.result[i][1])/10) 
    
    def uni_gdp_oil(self):
        '''return oil consumption for per unit GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][5])/(float(self.result[i][1])/10)   
        
    def uni_gdp_other(self):
        '''return other energy consumption for per unit GDP of the year'''
        i = GDPEnergy.index(self)
        return float(self.result[i][6])/(float(self.result[i][1])/10)
    
    def per_coal(self):
        '''return the percentage of coal consumption of the year'''
        i = GDPEnergy.index(self)
        return 100 * float(self.result[i][3])/float(self.result[i][2])
    
    def per_gas(self):
        '''return the percentage of gas consumption of the year'''
        i = GDPEnergy.index(self)
        return 100 * float(self.result[i][4])/float(self.result[i][2])    
    
    def per_oil(self):
        '''return the percentage of oil consumption of the year'''
        i = GDPEnergy.index(self)
        return 100 * float(self.result[i][5])/float(self.result[i][2])    
    
    def per_other(self):
        '''return the percentage of other energy consumption of the year'''
        i = GDPEnergy.index(self)
        return 100 * float(self.result[i][6])/float(self.result[i][2])     
        

    def message(self):
        '''output of the current year's GDP and energy consumption information
        and a piechart show the constitution of the energy consumption in this year'''
        self.label1['text'] = 'The GDP and energy consumption information in \
Chongqing in {} is as follows:\n(For conversion convenience, all units of energy\
consumption are tons standard coal)'.format(self.combo.get())
        self.label2['text'] = 'The GDP in this year was {:.2f} billion \
yuan.'.format(GDPEnergy.gdp(self))
        self.label3['text'] = 'The total energy consumption in this year \
was {} tons of standard coal.'.format(GDPEnergy.energy(self))
        self.label4['text'] = 'The energy consumption for every billion yuan of\
GDP in this year was {:.2f} tons of standard coal.'.format(GDPEnergy.uni_gdp_energy(self))
        self.label5['text'] = 'The composition of energy consumption in {} is as \
follows:\n(For conversion convenience, all units of enerey consumption are\
tons of standard coal)'.format(self.combo.get())
        self.label6['text'] = 'The consumption of coal in this year was {} tons \
of standard coal, account for {:.2f}% energy consumption that year, every \
billion yuan consumed {:.2f} tons of standard coal.\
'.format(GDPEnergy.coal(self), GDPEnergy.per_coal(self), GDPEnergy.uni_gdp_coal(self))
        self.label7['text'] = 'The consumption of gas in this year was {} tons \
of standard coal, account for {:.2f}% energy consumption that year, every billion\
 yuan consumed {:.2f} tons of standard coal.'.\
format(GDPEnergy.gas(self), GDPEnergy.per_gas(self), GDPEnergy.uni_gdp_gas(self))
        self.label8['text'] = 'The consumption of oil in this year was {} tons\
of standard coal, account for {:.2f}% energy consumption that year, every billion\
 yuan consumed {:.2f} tons of standard coal.'.format(GDPEnergy.oil(self), \
GDPEnergy.per_oil(self), GDPEnergy.uni_gdp_oil(self))
        self.label9['text'] = 'The consumption of other energy in this year was\
{} tons of standard coal, account for {:.2f}% energy consumption that year, every\
 billion yuan consumed {:.2f} tons of standard coal.'.format(GDPEnergy.other(self),\
GDPEnergy.per_other(self), GDPEnergy.uni_gdp_other(self))

        matplotlib.use('TkAgg')
        pie = plt.figure(num = 'Pie chart of consumption of energy in {}'.\
format(self.combo.get()), figsize=(4.5, 4.5),facecolor="#F0F0F0") 
        pie.labels = ['Coal: {} tons'.format(GDPEnergy.coal(self)), 'Gas: {} tons'.\
format(GDPEnergy.gas(self)), 'Oil: {} tons'.format(GDPEnergy.oil(self)), 'Other: {} \
tons'.format(GDPEnergy.other(self))] 
        pie.sizes = [GDPEnergy.coal(self), GDPEnergy.gas(self), GDPEnergy.oil(self),\
                     GDPEnergy.other(self)] 
        pie.colors = ['blue', 'red', 'orange', 'green']
        pie.explode = (0.04, 0.04, 0.04, 0.04) 
        pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes, explode=pie.explode,
labels=pie.labels, colors=pie.colors, autopct='%3.2f%%', shadow=False,  startangle=90,  
pctdistance=1.4, textprops={'fontsize': 8, 'color' : '#000080'})
        plt.axis('equal')        
        for t in pie.text2:
            t.setsize = 8        
        canvas_statis = FigureCanvasTkAgg(pie, root)
        canvas_statis.get_tk_widget().place(x=0, y=0)

    
def main():
    '''set up the gui and run it'''
    result = readfile('chongqing.csv')
    window = Tk()
    window.title("Data on the relationship between chongqing's GDP \
and energy consumption from 1980 to 2017")
    test = GDPEnergy(window, result)
    window.mainloop()
    
main()
