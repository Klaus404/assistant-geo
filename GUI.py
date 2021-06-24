import main
import tkinter as tk


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="Orange")
canvas.pack()

frame = tk.Frame(root, bg="Black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

runAss = tk.Button(root, text="Run Geo", padx=10, pady=5, fg="Black", bg="White", command=main.go_Geo)
runAss.pack()

exit_program = tk.Button(root, text="Exit", padx=10, pady=5, fg="Black", bg="White", command=exit)
exit_program.pack()

root.mainloop()
