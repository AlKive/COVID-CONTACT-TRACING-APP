#PSEUDOCODE
#import tkinter 
from tkinter import*
from tkinter import ttk
import tkinter
import os
import openpyxl
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
    
    # address label and entry
    def address(self):
        self.ADDRESS = tkinter.Label(PERSONAL_INFORMATION, text="Address")
        self.ADDRESS.grid(row=7, column=0)
        self.ADDRESS_INPUT = tkinter.Entry(PERSONAL_INFORMATION)
        self.ADDRESS_INPUT.grid(row=7, column=1)    
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
    def add(self):
        accepted = self.accept_var.get()
        if accepted=="Accepted":
            firstname = self.FIRST_NAME_INPUT.get()
            lastname = self.LAST_NAME_INPUT.get()
            
            if firstname and lastname:
                    nationality  = self.NATIONALITY_INPUT.get()
                    age = self.AGE_INPUT.get()
                    address = self.ADDRESS_INPUT.get()
                    gender = self.GENDER_INPUT.get()
                    vaccination = self.VACCINATION_STATUS_INPUT.get()
                    phone = self.PHONE_INPUT.get()
                    
                    print("First name: ", firstname , "\n" , "Last name: ", lastname)
                    print("Age: ", age, "\n", "Nationality: ", nationality, "\n", "Gender :", gender)
                    print("Vaccination Status: ", vaccination, "\n", "Cellphone Number : ", phone, "\n", "Address :", address)

                    filepath =("C:\git\BSCPE 1ST YEAR 2ND SEM\OOP\ASSIGNMENTS\COVID-CONTACT-TRACING-APP\Tracer\data.xlsx")

                    if not os.path.exists(filepath):
                        workbook = openpyxl.Workbook()
                        sheet = workbook.active
                        heading = ["First Name", "Last Name", "Gender", "Age", "Nationality",
                                "Address", "Cellphone Number", "Vaccination status"]
                        sheet.append(heading)
                        workbook.save(filepath)
                    workbook = openpyxl.load_workbook(filepath)
                    sheet = workbook.active
                    sheet.append([firstname, lastname, gender, age, nationality, address,
                                phone, vaccination])
                    workbook.save(filepath)
                
            else:
                        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
                tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms and conditions")
    #create search method
    def searchByFirstName(self):
        FirstName = self.FIRST_NAME_INPUT.get()
        wb = openpyxl.load_workbook("C:\git\BSCPE 1ST YEAR 2ND SEM\OOP\ASSIGNMENTS\COVID-CONTACT-TRACING-APP\Tracer\data.xlsx")  
        sheet = wb.active  
        for row in sheet.iter_cols(min_row=1, min_col=1, max_row=1000, max_col=1):  
            for cell in row:  
                if FirstName == (cell.value):
                    messagebox.showinfo(title="FIRST NAME", message= FirstName + " Exists in the excel File.")  
                    break
            if FirstName != (cell.value):
                messagebox.showinfo(title="FIRST NAME", message= FirstName + " Does Not Exists in the excel File.") 
                break 
    def showdata(self):
        wb = openpyxl.load_workbook("C:\git\BSCPE 1ST YEAR 2ND SEM\OOP\ASSIGNMENTS\COVID-CONTACT-TRACING-APP\Tracer\data.xlsx")  
        sheet = wb.active 
        cells = sheet['A1','B7'] 
        # cells behave like range operator  
        for i1,i2 in cells:  
            print("{0:8} {1:8}".format(i1.value,i2.value))          
    #create save/add button 
    def button_add(self):
        button = tkinter.Button(PERSONAL_INFORMATION, text="Enter data", command= self.add)
        button.grid(row=9, column=2, sticky="news", padx=20, pady=10)    
            
    #create search button
    def button_search(self):
        button = tkinter.Button(PERSONAL_INFORMATION, text="Search data", command= self.searchByFirstName)
        button.grid(row=9, column=3, sticky="news", padx=20, pady=10)
        