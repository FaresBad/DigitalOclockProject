from tkinter import *
import time



root = Tk()
root.title("My Digital O'clock")
root.geometry("800x500+0+0")
root.config(bg="blue")

def clock():
    #============== Set for my time zone ========================
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    #print(h,m,s)

    #change to PM if hour>12
    if int(h)>12 and int(m)>0:
        lbl_noon.config(text="PM")

    lbl_h.config(text=h)
    lbl_m.config(text=m)
    lbl_s.config(text=s)

    lbl_h.after(200,clock)

#===================== Hours Label ======================
lbl_h=Label(root,text="00",font=("times new roman",40,"bold"),bg="green",fg="white")
lbl_h.place(x=100,y=150,width=150,height=200)
lbl_txtH = Label(root, text="Hour", font=("times new roman", 40, "bold"), bg="green", fg="white")
lbl_txtH.place(x=100, y=360, width=150, height=50)

#===================== Minutes Label ======================
lbl_m = Label(root, text="00", font=("times new roman", 40, "bold"), bg="orange",fg="white")
lbl_m.place(x=250, y=150, width=150, height=200)
lbl_txtM = Label(root, text="Minute", font=("times new roman", 40, "bold"), bg="orange", fg="white")
lbl_txtM.place(x=250, y=360, width=150, height=50)

#===================== Seconds Label ======================
lbl_s = Label(root, text="00", font=("times new roman", 40, "bold"), bg="red",fg="white")
lbl_s.place(x=400, y=150, width=150, height=200)
lbl_txtS = Label(root, text="Second", font=("times new roman", 40, "bold"), bg="red", fg="white")
lbl_txtS.place(x=400, y=360, width=150, height=50)

#===================== Noon Label [AM Or PM] ======================
lbl_noon = Label(root, text="AM", font=("times new roman", 40, "bold"), bg="black", fg="white")
lbl_noon.place(x=550, y=150, width=150, height=200)
lbl_txtnoon = Label(root, text="Noon", font=("times new roman", 40, "bold"), bg="black", fg="white")
lbl_txtnoon.place(x=550, y=360, width=150, height=50)


clock()
root.mainloop()
