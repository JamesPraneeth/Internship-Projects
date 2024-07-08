import tkinter.ttk as ttk
from ttkbootstrap import Style
import tkinter
from tktooltip import ToolTip
import ttkbootstrap
from tkinter import messagebox

root = tkinter.Tk()
root.geometry('800x500')

instruction_x = 300
instruction_y = 350
border_color = 'black'
background_ = 'yellow'
foreground_ = 'black'
font_ = ('Noto Serif', 15)



style = Style(theme='solar')
style.configure('custom.TLabel', bordercolor = border_color,  background = background_, foreground = foreground_, font = font_, )



def function_board():
    function_fm = ttkbootstrap.Labelframe(root, text='Function',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20)

    def mbal_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='MBAL ',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def prosper_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='PROSPER ',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def gap_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='GAP',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def data_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='Allocate Data to DB',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def fft_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='FFT',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def schedule_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='Schedule',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def regression_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='Regression',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)

    def completeflow_fn():
        sample_fm = ttkbootstrap.Labelframe(root, text='Complete Flow',width=555, height = 450, style='info.TLabelframe').place(x=230, y= 20) 
        sample_label = ttkbootstrap.Label(sample_fm, text='Instructions can be placed here', style='custom.TLabel')
        sample_label.place(x=instruction_x,y=instruction_y)
    
    def confirm_exit():
        response = messagebox.askquestion("Exit", "Want to Exit")
        
        if response == 'yes':
            root.destroy()
        if response =='no':
            return
        if response == None:
            return
        

    def menu_board():
        menu_fm = ttkbootstrap.Labelframe(root, 
                                        text='Menu',
                                        width=175, 
                                        height = 450, 
                                        style='success.TLabelframe',).place(x=20, y= 20)
        
        mbal_button = ttkbootstrap.Button(menu_fm,
                                        text='MBAL', 
                                        padding=(58,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:mbal_fn()).place(x=30,y=40)
        
        propser_button = ttkbootstrap.Button(menu_fm,
                                        text='PROSPER', 
                                        padding=(50,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:prosper_fn()).place(x=30,y=90)
        
        gap_button = ttkbootstrap.Button(menu_fm,
                                        text='GAP', 
                                        padding=(62,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:gap_fn()).place(x=30,y=140)
        
        regression_button = ttkbootstrap.Button(menu_fm,
                                        text='Regression', 
                                        padding=(45,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:regression_fn()).place(x=30,y=190)
        
        data_button = ttkbootstrap.Button(menu_fm,
                                        text='Allocate Data\nfrom DB', 
                                        padding=(38,4), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:data_fn()).place(x=30,y=240)
        
        fft_button = ttkbootstrap.Button(menu_fm,
                                        text='FFT', 
                                        padding=(64,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:fft_fn()).place(x=30,y=290)
        
        schedule_button = ttkbootstrap.Button(menu_fm,
                                        text='Schedule', 
                                        padding=(49,10), 
                                        takefocus=False, 
                                        style='info.TButton',
                                        command=lambda:schedule_fn()).place(x=30,y=340)
        
        completeflow_button = ttkbootstrap.Button(menu_fm,
                                                text='Complete\nFlow', 
                                                padding=(47,4), 
                                                takefocus=False, 
                                                style='info.TButton',
                                        command=lambda:completeflow_fn()).place(x=30,y=390)
        
        exit_button = ttkbootstrap.Button(menu_fm,
                                                text='Exit', 
                                                padding=(10,4), 
                                                takefocus=False, 
                                                style='info.TButton',
                                        command=lambda:confirm_exit()).place(x=80,y=440)

    menu_board()

function_board()
root.mainloop()

                                  
