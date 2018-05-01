# NOTE: RUN THIS PROGRAME IN PYTHON 3 
from tkinter import *
from datetime import datetime
#time select 24 hours not 12 hours

def car():
	Type = int(var.get())
	start = getTimeI.get()
	end = getTimeO.get() 
	print (Type)
	print (start)
	FMT = '%H:%M'
	print (end)
	Time = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
	print (Time)

	if 0 <= Time.total_seconds() <= 3600 and Type == 1 :
		print('free Parking')

	elif 3601 <= Time.total_seconds() <= 10800 and Type == 1 : # 3601 is 1 hours and 1 minute, 10800 is 3 hours
		rate = 6
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate )) 

	elif 10801 <= Time.total_seconds() <= 21600 and Type == 1 : # 10801 is 3 hours and 1 minute, 21600 is 6 hours  
		rate = 14
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate )) 

	elif 21601 <= Time.total_seconds() <= 36000 and Type == 1 : # 21601 is 6 hours and 1 minute,  36000 is 10 hours  
		rate = 20
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	elif 36001 <= Time.total_seconds() <= 86400 and Type == 1 : # 36001 is 10 hours and 1 minute ,86400 is 24 hours 
		rate = 26
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	else:
		print('Wrong Input')

def van():

	Type = int(var.get())
	start = getTimeI.get()
	end = getTimeO.get() 
	print (Type)
	print (start)
	FMT = '%H:%M'
	print (end)
	Time = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
	print (Time)

	if 0 <= Time.total_seconds() <= 3600 and Type == 2 :
		print('free Parking')

	elif 3601 <= Time.total_seconds() <= 10800 and Type == 2 : # 10800 is 3 hours and 3601 is 1 hours and 1 minute  
		rate = 9
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	elif 10801 <= Time.total_seconds() <= 21600 and Type == 2 : # 10801 is 3 hours and 1 minute and 21600 is 6 hours  
		rate = 18
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	elif 21601 <= Time.total_seconds() <= 36000 and Type == 2 : # 21601 is 6 hours and 1 minute and 36000 is 10 hours  
		rate = 24
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	elif 36001 <= Time.total_seconds() <= 86400 and Type == 2 : # 36001 is 10 hours and 1 minute ,86400 is 24 hours 
		rate = 30
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	else:
		print('Wrong Input')

def disable():
	Type = int(var.get())
	start = getTimeI.get()
	end = getTimeO.get() 
	print (Type)
	print (start)
	FMT = '%H:%M'
	print (end)
	Time = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
	print (Time)

	if 0 <= Time.total_seconds() <= 3600 and Type == 3:
		print('free Parking')

	elif 3601 <= Time.total_seconds() <= 10800 and Type == 3 : # 3601 is 1 hours and 1 minute ,  10800 is 3 hours 
		rate = 3
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate )) 

	elif 10801 <= Time.total_seconds() <= 21600 and Type == 3 : # 10801 is 3 hours and 1 minute, 21600 is 6 hours  
		rate = 5
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate )) 

	elif 21601 <= Time.total_seconds() <= 36000 and Type == 3 : # 21601 is 6 hours and 1 minute,  36000 is 10 hours  
		rate = 8
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	elif 36001 <= Time.total_seconds() <= 86400 and Type == 3 : # 36001 is 10 hours and 1 minute ,86400 is 24 hours 
		rate = 11
		print('Parking fee for',Time,'hours is £', rate)
		ans.insert(INSERT, (rate ))

	else:
		print('Wrong Input')

def delete():
  getTimeI.delete(0, END)
  getTimeO.delete(0, END)
  ans.delete(0, END)
  print ("delete sucessful")

win = Tk()
win.geometry('500x400')

hello = Label(master = win, text = 'Car Parking',font=("Helvetica", 16), foreground="blue")
hello.pack(side=TOP)

askTime = Label(master = win, text = 'Enter Time In')
askTime.pack(side=TOP)
getTimeI = Entry(win,width=40,bg="white")
getTimeI.pack(side=TOP)

askTime = Label(master = win, text = 'Enter Time Out')
askTime.pack(side=TOP)
getTimeO = Entry(win,width=40,bg="red")
getTimeO.pack(side=TOP)

var = IntVar()
R1 = Radiobutton(win, text="Car", variable=var, value=1,
                  command=car)
R1.pack( side=TOP )
R2 = Radiobutton(win, text="Van", variable=var, value=2,
                  command=van)
R2.pack( side=TOP )
R3 = Radiobutton(win, text="Disable", variable=var, value=3,
                  command=disable)
R3.pack( side=TOP)

a = Label(master = win, text = 'charge is')
a.pack(side=TOP)
ans = Entry(win,width=40,bg="white")
ans.pack(side=TOP)

D = Button(win, text="clear data", width=9, command=delete)
D.pack()

win.mainloop()
