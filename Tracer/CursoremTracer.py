from tkinter import*

ws = Tk()
ws.geometry("1000x550")
ws.title("COVID Contact Tracing Form")

mainframe = Frame(ws, background ="light blue")
mainframe.pack(fill= "both", expand = True)


FirstNameButton = Button(mainframe,text ="First Name")
FirstNameButton.pack()

ws.mainloop()