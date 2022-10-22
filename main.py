import tkinter
from PIL import Image, ImageTk
import random

window = tkinter.Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title('Roll the Dice')

heading = tkinter.Label(window, text='Let Us Dice The Roll!!😁',font='arial 20 bold',fg='black',bg='yellow').pack(pady=10)

dice = ['image/die1.png', 'image/die2.png', 'image/die3.png',
        'image/die4.png', 'image/die5.png', 'image/die6.png']

imagedice = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(window, image=imagedice)
ImageLabel.image = imagedice
ImageLabel.pack( expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage


# adding button, and command will use rolling_dice function
button = tkinter.Button(window, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)


window.mainloop()
