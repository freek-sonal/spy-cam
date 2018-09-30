import cv2
from cv2 import *
from tkinter import *
from PIL import Image, ImageTk
import io
import threading
import sys
import os

def resize(image):
    im = image
    new_siz = siz
    im.thumbnail(new_siz)
    return im

def size(event):
    global siz
    if siz == screenWH:
       siz = (500, 500)
    else:
        siz = screenWH
        win.state('zoomed')
    
    print ('size is: ', siz)

def view_frame_video():
            print(value)
            vc = cv2.VideoCapture(value)
            if vc.isOpened():
                rval , frame = vc.read()
            else:
                rval = False
        
            while rval:
                rval, frame = vc.read()
                #frame = cv2.flip(frame, 1)
                if rval: 
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                    #cv2.imshow('frame',cv2image)
                    img =Image.fromarray(cv2image)
                    img = resize(img)
                    imgtk = ImageTk.PhotoImage(img)
                    lbl.config(image=imgtk)
                    lbl.img = imgtk
                    if stop == True: 
                        vc.release()
                        break    
                    cv2.waitKey(1)
            vc.release()

def Stop_():
    global stop
    stop = True

def Play():
    stop = False
    t = threading.Thread(target=view_frame_video)
    t.start()

def walk_dir(root_dir, extension):
    file_list = []
    towalk = [root_dir]
    while towalk:
        root_dir = towalk.pop()
        for path in os.listdir(root_dir):
            full_path = os.path.join(root_dir, path).lower()
            if os.path.isfile(full_path) and full_path.endswith(extension):
                file_list.append((path.lower(), root_dir))
            elif os.path.isdir(full_path):
                towalk.append(full_path)
    return file_list

def get_list(event):
    
    try:
        global selpath
        sel = listbox1.curselection()
        selpath = [file_list[int(x)] for x in sel]
    except:
        info_label.config()

def onselect(evt):
    
    global value
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print(value)
    
win = Tk()
win.title("VIDEO PLAYER")
win.configure(background="#0a2845#")
win.geometry("1000x550")
stop = None
value=StringVar
screenWH = (win.winfo_screenwidth(), win.winfo_screenheight())
siz = (700, 700)

Label(text='                          VIDEO PLAY !!!                                                                   LIST',fg="white",bg="#0a2845#",font="times 16 bold").pack()
yscroll = Scrollbar(orient=VERTICAL)
yscroll.pack(side=RIGHT,ipady=70,padx=20)
list1=Listbox(bg="powder blue",height=30,width=40)
list1.pack(side=RIGHT,ipadx=20,ipady=10)


frm_1 = Frame(bg="#0a2845#")
frm_1.pack(anchor="w",expand=True)
lbl = Label(frm_1, bg="#0a2845#")
lbl.pack(padx=5)
lbl.bind('<Double-Button-1>', size)

Button(text='PLAY', command = Play,width=20,font="times 10 bold ").pack(side=LEFT,padx=5)
Button(text='STOP', command = Stop_,width=20,font="times 10 bold ").pack(side=LEFT,padx=5)



frm_2 = Frame(bg='grey')
frm_2.pack()
info_label = Label(frm_2,fg='RED',bg="#0a2845#",font="times 12 bold",width=30)
info_label.pack(ipadx=30)

fullpath_list = []

root_dir = r"E:\python_projects\videoplayer\Pc_Security_Python\recordergui"

extension = '.avi'

file_list = walk_dir(root_dir, extension)

file_list.sort()

for file in file_list:
    list1.insert(END, file[0])

file_num = len(file_list)
if  file_num > 0:
    info = "Loaded %d%s files from dir %s" % (file_num, extension, root_dir)
else:
    info = "No %s files i directory %s" % (extension, root_dir)
info_label.config(text=info)
 
list1.bind('<ButtonRelease-1>', get_list)
list1.bind('<<ListboxSelect>>', onselect)

win.mainloop()
