from tkinter import *
from tkinter import messagebox,filedialog
from PIL import ImageTk, Image
import os
import glob
import pathlib

in_path=""
raw_imgs=[]
img=None
counter = 0
imgPil=None
imageFrame=None
index=0

SAVED_DIRECTORY= pathlib.Path(r'C:\Users\Irfan\Documents\Python\FYPSkinMeasure\CroppedImages_Wrinkles')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def editCounter():
    global counter
    top = Toplevel()
    frame = Frame(top)
    counterText = StringVar()
    counterText.set(str(counter))
    counterLabel = Label(frame,text="Counter")
    counterEntry = Entry(frame,bd=2,textvariable=counterText)
    counterConfirm = Button(top,text="Confirm",command=lambda: saveChangedCounter(top,counterEntry.get()))
    frame.pack()
    counterLabel.pack(side=LEFT)
    counterEntry.pack(side=RIGHT)
    counterConfirm.pack()
    
    top.mainloop()

def saveChangedCounter(top,countertext):
    global counter
    counter = int(countertext)
    top.withdraw()

def openFile(_event=None):
    global in_path,img,imgPil,imageFrame
    in_path=filedialog.askopenfilename(initialdir = "/Users/Irfan/Documents/Python/FYPSkinMeasure",title = "Select file",filetypes = (("JPG","*.jpg"),("all files","*.*")))
    handleDisplayImage(in_path)
    listAllImageFiles()

def listAllImageFiles():
    global raw_imgs,index
    directory = os.path.split(in_path)[0]
    
    raw_imgs = glob.glob(directory+"/*.jpg")
    for i, url in enumerate(raw_imgs):
        raw_imgs[i] = url.replace(os.sep,'/')
        
    index = raw_imgs.index(in_path)



def handleNextImage(_event=None):
    global raw_imgs,index
    if raw_imgs:
        if index<=len(raw_imgs):
            index+=1
            handleDisplayImage(raw_imgs[index])
        else:
            messagebox.showwarning("Warning","Out of bounds. No more next image")
def handlePrevImage(_event=None):
    global raw_imgs,index
    if raw_imgs:
        if index>0:
            index-=1
            handleDisplayImage(raw_imgs[index])
        else:
            messagebox.showwarning("Warning","Out of bounds. No more previous image")


def handleDisplayImage(file_url):
    global img,imgPil,imageFrame
    img = ImageTk.PhotoImage(Image.open(file_url))
    imgPil = Image.open(file_url)
    imageFrame = display.create_image(0,0,anchor=NW,image=img)
    display.config(scrollregion=display.bbox(ALL))
    display.tag_lower(imageFrame)

def handleCropImage(_event=None):
    global counter
    counter+=1
    saved = imgPil.crop(display.coords(cropFrame))
    path = os.path.join(SAVED_DIRECTORY,"img_"+str(counter)+".jpg")
    saved.save(path)
    infoText.set("Saved "+ "img_"+str(counter)+".jpg")


root = Tk()
root.title("Irfan's CustomImageCropper")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Edit counter", command=editCounter)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_separator()
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
# menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)



#declare & display the image file to canvas
display = Canvas(root)
display.pack(fill=BOTH,expand=1)
myscrollbar=Scrollbar(display,orient="vertical",command=display.yview)
display.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")

SAVED_DIRECTORY.mkdir(parents=True,exist_ok=True)



def callback(event):
    draw(event.x,event.y)

def draw(x,y):
    display.coords(cropFrame,x-32,y-32,x+32,y+32)

def OnMouseWheel(event):
    display.yview_scroll(int(-1*(event.delta/120)), "units")
    return "break" 


#create crop frame & assign draggable event
cropFrame = display.create_rectangle(0,0,100,100,outline="red")
display.bind('<B1-Motion>',callback)


#create horizontal layout at the bottom of GUI
buttonFrame = Frame(root)

buttonFrame.pack(side=BOTTOM)

#populate info label & button inside buttonFrame
infoText = StringVar()
infoLabel = Label(buttonFrame,textvariable=infoText)

prevButton= Button(buttonFrame,text="< Previous", command=handlePrevImage)
nextButton = Button(buttonFrame,text="Next >", command=handleNextImage)
cropButton = Button(buttonFrame,text="Crop", command=handleCropImage)

root.bind('d',handleNextImage)
root.bind('a',handlePrevImage)
root.bind('<space>',handleCropImage)
root.bind('o',openFile)
display.bind('<MouseWheel>',OnMouseWheel)

infoLabel.pack()
prevButton.pack(side=LEFT)
nextButton.pack(side=RIGHT)
cropButton.pack(side=LEFT)

root.mainloop()