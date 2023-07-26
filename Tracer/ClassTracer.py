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
    def age(self):
        self.AGE = tkinter.Label(PERSONAL_INFORMATION, text="Age")
        self.AGE.grid(row=3, column=0)
        self.AGE_INPUT = tkinter.Spinbox(PERSONAL_INFORMATION, from_=1, to=100)
        self.AGE_INPUT.grid(row=3, column=1)

    #Nationality label and entry
    def national(self):
        #Nationality label and entry
        self.NATIONALITY = tkinter.Label(PERSONAL_INFORMATION, text="Nationality")
        self.NATIONALITY.grid(row=4, column=0)
        self.NATIONALITY_INPUT = ttk.Combobox(PERSONAL_INFORMATION, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        self.NATIONALITY_INPUT.grid(row=4, column=1)
        
    #Vaccination Status label and entry
    def vaccination(self):
        
        self.VACCINATION_STATUS = tkinter.Label(PERSONAL_INFORMATION, text="Vaccination Status")
        self.VACCINATION_STATUS.grid(row=7, column=0)
        self.VACCINATION_STATUS_INPUT = ttk.Combobox(PERSONAL_INFORMATION, values=["Unvaccinated", "1st Dose", "2nd Dose(Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"])
        self.VACCINATION_STATUS_INPUT.grid(row=7, column=1)

    #Phone Number label and entry
    def phone(self):
        self.PHONE = tkinter.Label(PERSONAL_INFORMATION, text= "Cellphone Number")
        self.PHONE.grid(row=6, column=0)
        self.PHONE_INPUT = tkinter.Entry(PERSONAL_INFORMATION)
        self.PHONE_INPUT.grid(row=6, column=1)
    
    #put terms and condition checkbox
    def accept(self):
        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = tkinter.Checkbutton(PERSONAL_INFORMATION, text= "I accept the terms and conditions.",
                                        variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=8, column=1)
    #fix spacing of widgets
    def separate(self):
        for widget in PERSONAL_INFORMATION.winfo_children():
            widget.grid_configure(padx=20, pady=10)

    #create a save/add function for all user's info into a database ( i prefer excel as my database)

    #create save/add button               

    #create search button
        