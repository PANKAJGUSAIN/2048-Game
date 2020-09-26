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

#initializing grid
    def init_grid(self):
        #creating anpther frame inside Frame 
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width =c.SIZE , heigth=c.SIZE)
        background.grid()

        #adding cells
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                #creating another frame name cell inside background with color to be a color of a empty cell
                cell = Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width=c.SIZE/c.GRID_LEN ,
                            height = c.SIZE / c.GRID_LEN)
                #adding cells 
                cell.grid(row = i ,column=j ,padx = c.GRID_PADDING , 
                        pady = c.GRID_PADDING )
                
                #inside cell adding label grid which takes text
                t = Label(master=cell , text="" ,
                        bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                        justify=CENTER ,font=c.FONT , width =5 , height =2)

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
                
            
                              




        
