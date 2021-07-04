import brain
import tkinter as tk
from tkinter import *
# from PIL import ImageTk, Image
# import jupyter

root = tk.Tk()
root.title('Geo assistant')

root.resizable(width=True, height=True)
root.geometry("1540x790")

bg = PhotoImage(file="C:/Users/Claudiu/PycharmProjects/chatBotMe/asistent.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# text = Text(root, height=10, width=53)
# text.place()

# canvas = tk.Canvas(root, height=700, width=700, bg="Orange")
# canvas.pack()

# frame = tk.Frame(root, bg="Black")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


runAss = tk.Button(root, text="Run Geo", padx=10, pady=5, fg="Black", bg="White", command=brain.go_Geo, font="Jomhuria")
runAss.pack()

exit_program = tk.Button(root, text="Exit", padx=10, pady=5, fg="Black", bg="White", command=quit, font="Jomhuria")
exit_program.pack()

root.mainloop()
