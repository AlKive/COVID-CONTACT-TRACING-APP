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
    #init function & create instance of variable
    
    #create functions for getting user's input using tkinter entry with label

        #first name label and entry
        
        #last name label and entry
        
        #Gender label and entry
        
        #last name label and entry
       
        #Age label and entry
        
        #Nationality label and entry

        #Vaccination Status label and entry

        #Phone Number label and entry
        
        #put terms and condition checkbox
 
        #fix spacing of widgets
  
        #create a save/add function for all user's info into a database ( i prefer excel as my database)

        #create save/add button               
    
        #create search button
            