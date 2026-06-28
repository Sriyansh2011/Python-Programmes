from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.geometry("650x400")
root.configure(bg="light blue")

img = ImageTk.PhotoImage(Image.open("app_img.jpg").resize((300,300)))
Label(root,image=img,bg="light blue").place(x=180,y=20)

Label(root,text="Welcome to Denomination Counter!",bg="light blue").place(relx=0.5,y=340,anchor=CENTER)

def topwin():
    top=Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("600x350")
    top.configure(bg="light grey")

    Label(top,text="Enter Total Amount",bg="light grey").place(x=220,y=50)
    amount = Entry(top)
    amount.place(x=200,y=80)

    entries = []
    for i, note in enumerate([2000,500,100]):
        Label(top,text=note,bg="light grey").place(x=180,y=200 + i*30)
        e=Entry(top,width=10)
        e.place(x=270,y=200 + i*30)
        entries.append(e)

    def calc():
        try:
            amt = int(amount.get())
            notes = [amt//2000,(amt%2000)//500,(amt%500)//100]

            for e,n in zip(entries,notes):
                e.delete(0,END)
                e.insert(0,n)
        except ValueError:
            messagebox.showerror("Error","Enter a valid number")
    Button(top, text="Calculate",command=calc,bg="brown",fg="white").place(x=240,y=140)

def msg():
    if messagebox.showinfo("Alert","Do You want to calculate the denomination count?") == "ok":
        topwin()

Button(root,text="Let's get started!", command=msg,bg="brown",fg="white").place(x=260, y=360)

root.mainloop()