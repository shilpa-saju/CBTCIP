#weather forecast

import tkinter as tk
from tkinter import ttk
#---------------------------------------------------------------

import requests
def action_getData():
    global city_name
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name.get()+"&appid=fa8a36553d15714a5cc2cbc1c2789ec4").json()
    w1.config(text="weather climate : "+data['weather'][0]['main'])
    w2.config(text="weather description : "+data['weather'][0]['description'])   
    w3.config(text="temperature: "+str(int(data['main']['temp']-273.15)))
    w4.config(text="pressure : "+str(data['main']['pressure']))

#---------------------------------------------------------------------

win=tk.Tk()
win.geometry("600x520")
win.resizable(False, False)
win.title("shilpa's weathervane")
win.configure(bg='white')

title_img=tk.PhotoImage(file='title.png')
tk.Label(win,image=title_img,bg='white').place(x=100,y=10)
underline=tk.PhotoImage(file='underline.png')
tk.Label(win,image=underline,bg='white').place(x=190,y=75)

city_name=tk.StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com=ttk.Combobox(win,text="shilpa's weathervane",textvariable=city_name,values=list_name,font=("arial",15,"bold"))
com.place(x=150,y=110)
#-------------------------------------------------------------------------
w1=tk.Label(win,text="weather climate :",font=("arial",15,"bold"),bg='white')
w1.place(x=60,y=220)

w2=tk.Label(win,text="weather description :",font=("arial",15,"bold"),bg='white')
w2.place(x=60,y=270)

w3=tk.Label(win,text="temperature :",font=("arial",15,"bold"),bg='white')
w3.place(x=60,y=320)

w4=tk.Label(win,text="pressure :",font=("arial",15,"bold"),bg='white')
w4.place(x=60,y=370)


#-------------------------------------------------------------------------

tk.Button(win,text="Done !",font=("arial",15,"bold"),command=action_getData,bg='white').place(x=230,y=150)

dev=tk.PhotoImage(file="developer.png")
tk.Label(win,image=dev,bg='white').place(x=460,y=370)

namex=tk.PhotoImage(file="myName.png")
tk.Label(win,image=namex,bg='white').place(x=450,y=500)




win.mainloop()

