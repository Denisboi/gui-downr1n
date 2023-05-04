import tkinter
import os
import customtkinter
import time
from PIL import Image  

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="15.7.5 - latest ios")
        self.label.pack(padx=20, pady=20)
        self.title("Error")
        
class Toplevelw(customtkinter.CTkToplevel):  
   def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.geometry("400x300")
    self.label = customtkinter.CTkLabel(self, text="Incorrect ios!")
    self.label.pack(padx=20, pady=20)
    self.title("Downgrade")
class Errorr(customtkinter.CTkToplevel):
   def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.geometry("600x400")
    self.label = customtkinter.CTkLabel(self, text="Error. " )
    self.label.pack(padx=20, pady=20)
    self.title("Error")
class Downgrade(customtkinter.CTkToplevel):
   def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.geometry("650x500")
    self.label = customtkinter.CTkLabel(self, text="Downgrade" )
    self.label.pack(padx=20, pady=20)
    self.title("Downgrade")
    self.ready = customtkinter.CTkButton(self, text="Ready", fg_color=("purple"), command=self.redy, hover_color=("gray"))
    self.ready.place(relx=0.65, rely=0.9, anchor=tkinter.CENTER)
   def redy(self):
    ios = customtkinter.CTkInputDialog(text="Type in an ios", title="Which an ios?")
    self.vers = ios.get_input()
    
    if self.vers == "14.0" or self.vers == "14.0.1" or self.vers == "14.1" or self.vers == "14.2" or self.vers == "14.3" or self.vers == "14.4" or self.vers == "14.5" or self.vers == "14.4.1" or self.vers == "14.4.2" or self.vers == "14.5.1" or self.vers == "14.6" or self.vers == "14.7" or self.vers == "14.7.1" or self.vers == "14.8" or self.vers == "15.0" or self.vers == "15.0.1" or self.vers == "15.0.2" or self.vers == "15.1" or self.vers == "15.2" or self.vers == "15.2.1" or self.vers == "15.3" or self.vers == "15.3.1" or self.vers == "15.4" or self.vers == "15.4.1" or self.vers == "15.5" or self.vers == "15.6" or self.vers == "15.6.1" or self.vers == "15.7" or self.vers == "15.7.1" or self.vers == "15.7.2" or self.vers =="15.7.3" or self.vers == "15.7.4":
     app.withdraw()
     os.system("sudo bash ./downr1n.sh --downgrade " + self.vers)

     self.ready.destroy()
     self.text = customtkinter.CTkLabel(self, text="Look in the terminal", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
     self.text.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
     
    elif self.vers == "15.7.5":
     self.text = customtkinter.CTkLabel(self, text="15.7.5 - latest ios", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
     self.text.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)  
    else:
     self.text = customtkinter.CTkLabel(self, text="Ios incorrect", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
     self.text.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)    
class App(customtkinter.CTk):
     customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
     customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
     
     
        

     

     def __init__(self):
        super().__init__()
        
        
        self.down = customtkinter.CTkButton(self, text="Downgrade", command=self.owngrade)
        self.down.place(relx=0.89, rely=0.9, anchor=tkinter.CENTER)
        self.boot = customtkinter.CTkButton(self, text="Boot", fg_color=("green"), command=self.boots, hover_color=("gray"))
        self.boot.place(relx=0.65, rely=0.9, anchor=tkinter.CENTER)
        self.title("Downgrade by Edwin170")
        self.minsize(600, 400)
        self.label = customtkinter.CTkLabel(master=self, text="Downr1n - tool for downgrade tethered checkm8 idevices ios 14, 15.", font=("/binaries/py/ofont.ru_Lilita One.ttf",17))
        self.label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        self.label2 = customtkinter.CTkLabel(master=self, text="Python script was created by Denisboi", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
        self.label2.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
        self.toplevel_window = None

        try:
         filee = open('d.txt', 'r')
         filee.close()
        except:
         print("Open with .sh file!")
         exit()
        

     
     def owngrade(self):
         
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
          self.toplevel_window = Downgrade(self)  # create window if its None or destroyed
         else:
          self.toplevel_window.focus()
     def Errors(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
          self.toplevel_window = Errorr(self)  # create window if its None or destroyed
         else:
          self.toplevel_window.focus()
         time.sleep(2)
         exit()
     def open_toplevel(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
          self.toplevel_window = Toplevelw(self)  # create window if its None or destroyed
         else:
          self.toplevel_window.focus()
     def open_Toplevelw(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
          self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
         else:
          self.toplevel_window.focus()
     
            
    
     def boots(self):
         ios = customtkinter.CTkInputDialog(text="Type in an ios", title="Which an ios?")
         self.vers = ios.get_input()
    
         if self.vers == "14.0" or self.vers == "14.0.1" or self.vers == "14.1" or self.vers == "14.2" or self.vers == "14.3" or self.vers == "14.4" or self.vers == "14.5" or self.vers == "14.4.1" or self.vers == "14.4.2" or self.vers == "14.5.1" or self.vers == "14.6" or self.vers == "14.7" or self.vers == "14.7.1" or self.vers == "14.8" or self.vers == "15.0" or self.vers == "15.0.1" or self.vers == "15.0.2" or self.vers == "15.1" or self.vers == "15.2" or self.vers == "15.2.1" or self.vers == "15.3" or self.vers == "15.3.1" or self.vers == "15.4" or self.vers == "15.4.1" or self.vers == "15.5" or self.vers == "15.6" or self.vers == "15.6.1" or self.vers == "15.7" or self.vers == "15.7.1" or self.vers == "15.7.2" or self.vers =="15.7.3" or self.vers == "15.7.4":
          
          os.system("sudo bash ./downr1n.sh --boot " + self.vers)
          
          self.text = customtkinter.CTkLabel(self, text="Look in the terminal", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
          self.text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
     
         elif self.vers == "15.7.5":
          self.text = customtkinter.CTkLabel(self, text="15.7.5 - latest ios", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
          self.text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)  
         else:
          self.text = customtkinter.CTkLabel(self, text="Ios incorrect", font=("/binaries/py/ofont.ru_Lilita One.ttf",14))
          self.text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER) 
    
             
if __name__ == "__main__":
    app = App()
    app.mainloop()

     


