# def smith(x):
#     match x:
#             case _ if x>=90 and x<= 100:
#                 print("Grade A")
#             case _ if x>= 70 and x <= 89:
#               print("Grade B")
#             case _ :
#               print("Unknown Result")
# y=input("Enter your score: ")
# smith(int(y))

# polymorphism in class


import tkinter as tk

root = tk.Tk()

var0 = tk.StringVar(value='1')
var1 = tk.StringVar(value='0')
var2 = tk.StringVar(value='0')

def cb():
    print('--- languages ---')
    print('English', var0.get())
    print('German', var1.get())
    print('French', var2.get())

tk.Checkbutton(root, text='English', variable=var0, command=cb).pack()
tk.Checkbutton(root, text='German', variable=var1, command=cb).pack()
tk.Checkbutton(root, text='French', variable=var2, command=cb).pack()

root.mainloop()