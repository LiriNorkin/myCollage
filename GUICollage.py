import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
import myCollage

root = tk.Tk()
root.title('Collage Maker')

label1 = tk.Label(root, text="Collage Maker", fg="black", bg="pink", height="30", width="70")
label1.pack()

global imgs
def open():
    filez = tk.filedialog.askopenfilenames(parent=root, title='Choose a file')
    imgs = list(filez)
    col = myCollage.myCollage(imgs)
    col.makeCollage()

button1 = tk.Button(root, text="Pick Images",command=open).pack()
#root.filename = filedialog.askopenfilename(initialdir="/tkinterGUI/images",title="Select Images For The Collage", filetypes=(("jpg files", "*.jpg"),("all files","*.*")))
#filez = tk.filedialog.askopenfilenames(parent=root, title='Choose a file')
#imgs = list(filez)
#    label2 = tk.Label(root, text=root.filename).pack()
#    img = ImageTk.PhotoImage(Image.open(root.filename))
#    imgLabel = tk.Label(image=img).pack()

root.mainloop()
