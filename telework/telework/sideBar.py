import tkinter as tk
from PIL import Image, ImageTk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.pack_forget()
        self.is_open = False

        self.close_button = tk.Button(self, bg='#3B3C36', fg='white', command=self.close_sidebar)
        self.close_button.place(x=10, y=10)

        # logo pic
        self.logoside = Image.open('ps2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.self, image=logos, width='80', height="80", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=40, y=0)


        # self.label = tk.Label(self.close_button, text="X", font=('yu gothic ui', 16, 'bold'), bg='#3B3C36', fg='white')
        # self.label.place(x=10, y=10)

        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button1.place(x=10, y=200)

        self.button2 = tk.Button(self, text="Transactions", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button2.place(x=10, y=300)

        self.button3 = tk.Button(self, text="Account Settings", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button3.place(x=10, y=500)

    def toggle(self):
        if self.is_open:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)
            self.is_open = True
            self.animate_open()
        else:
            self.place_forget()
            self.is_open = False

    def close_sidebar(self):
        self.place_forget()
        # self.is_open = False


    def animate_open(self):
        if self.winfo_x() < 0:
            self.place(x=self.winfo_x() + 1, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_open)
        else:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)

