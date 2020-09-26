from Tkinter import Frame , Label , CENTER
import  LogicsFinal
import Constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()  #to create a grid
        self.master.title('2048') #name of the grid
        self.master.bind("<key>",self.key_down)  #movement functions 
        self.commands ={c.KEY_UP:LogicsFinal.move_up , 
                        c.KEY_DOWN:LogicsFinal.move_down,
                        c.KEY_LEFT:LogicsFinal.move_left,
                        c.KEY_RIGHT:LogicsFinal.move_right
                        }
        self.grid_cells =[]    #create empty cells
        self.init_grid()       #create grids in the master grid
        self.init_matrix()      #change the matrix like adding '2' randomly at random place  
        self.update_grid_cells()  #change the UI

        self.mainloop()






        
