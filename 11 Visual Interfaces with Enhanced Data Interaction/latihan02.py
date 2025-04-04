from tkinter import *
def submit():
  print("The temperature is: " + str(scale.get()) + " degrees Fahrenheit")

window = Tk()
scale = Scale(window,
              from_=212,
              to=32,
              length=600,
              orient=HORIZONTAL,
              font=('Consolas',20),
              
              tickinterval=10,
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#FFDD00',
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,
                text='Submit',
                command=submit)
button.pack()
window.mainloop()