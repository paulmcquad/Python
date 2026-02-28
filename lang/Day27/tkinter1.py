import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(500, 300)

# Label
my_label = tkinter.Label(window, text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack(side='top')

my_label['text'] = 'new text'
my_label.config(text='new text')

# Button
def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=10)
input.pack()
input.get()


window.mainloop()