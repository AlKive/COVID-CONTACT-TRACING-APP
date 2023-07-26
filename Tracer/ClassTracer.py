#PSEUDOCODE
#import tkinter 
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
#create tkinter window    

ws = tkinter.Tk()
ws.geometry("1000x550")
ws.title("COVID Contact Tracing Form")
ws.configure(highlightbackground= "dark blue", highlightthickness= "3")

#create frame for necessary information 
mainframe = tkinter.Frame(ws, background= "light blue")
mainframe.pack(fill="both", expand= True)

#label the frame
PERSONAL_INFORMATION =tkinter.LabelFrame(mainframe, text="PERSONAL INFORMATION")
PERSONAL_INFORMATION.pack(side=TOP,padx=50, pady=30, fill= "both", expand= True)

#create class
class Tracer:
    #init function & create instance of variable
    def __init__(self):
          self.self  = self
    
#create functions for getting user's input using tkinter entry with label

    #first name label and entry
    def firstName(self):
        self.FIRST_NAME = tkinter.Label(PERSONAL_INFORMATION, text="First Name")
        self.FIRST_NAME.grid(row=0, column=0)
        self.FIRST_NAME_INPUT = tkinter.Entry(PERSONAL_INFORMATION)
        self.FIRST_NAME_INPUT.grid(row=0, column=1)
    
    #last name label and entry
    def lastName(self):
        self.LAST_NAME = tkinter.Label(PERSONAL_INFORMATION, text="Last Name")
        self.LAST_NAME.grid(row=1, column=0)
        self.LAST_NAME_INPUT = tkinter.Entry(PERSONAL_INFORMATION)
        self.LAST_NAME_INPUT.grid(row=1, column=1)

    #Gender label and entry
    def gender(self):
        self.GENDER = tkinter.Label(PERSONAL_INFORMATION, text="Gender")
        self.GENDER.grid(row=2, column=0)
        self.GENDER_INPUT = ttk.Combobox(PERSONAL_INFORMATION, values=["Male", "Female", "Transgender Male", "Transgender Female", "Prefer Not to Say"])
        self.GENDER_INPUT.grid(row=2, column=1)

    
    #Age label and entry
    
    #Nationality label and entry

    #Vaccination Status label and entry

    #Phone Number label and entry
    
    #put terms and condition checkbox

    #fix spacing of widgets

    #create a save/add function for all user's info into a database ( i prefer excel as my database)

    #create save/add button               

    #create search button
        