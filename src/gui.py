from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk, Image
from enigma import enigma
from tkinter import simpledialog as sd
from file_writer import reset_file

# Initialization
reset_file()
win = Tk()
win.title('Enigma Simulator App')
win.tk.call('wm', 'iconphoto', win._w, PhotoImage(file='./assets/cryptography.png'))
width = int(1920*0.6)
height = int(1080*0.6)
win.geometry(f"{width}x{height}")
win.resizable(False,False)

# Frame
frame = Frame(win, width=width, height=height)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Background
img = ImageTk.PhotoImage(Image.open("./assets/Background.png"))
bg = Label(frame, image = img)
bg.pack()

# Initializing variables
file = "./txt/test.txt"
machine = enigma("./txt/test.txt")

# Placing widgets
reset_img = PhotoImage(file="./assets/Reset.png")
reset_button = Button(
    frame,
    image=reset_img,
    bg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: reset()
)
reset_button.place(
    x=785, y=43
)

text_img = PhotoImage(file="./assets/Text Box.png")
text_img_label = Label(frame, image=text_img, bg="#ffffff")
text_label = Text(
    frame, 
    width=39, 
    height=1, 
    bg="#f1f1f1",
    bd=0,
    relief='flat',
    font=("Inter,11"))
text_img_label.place(
    x=85, y=215
)
text_label.place(
    x=101, y=234
)

out_img = PhotoImage(file="./assets/Text Box.png")
out_img_label = Label(frame, image=out_img, bg="#ffffff")
out_label = Label(frame, text="", font=("Inter", 11))
out_img_label.place(
    x=600, y=215
)
out_label.place(
    x=603+(101-85), y=234
)

encrypt_img = PhotoImage(file="./assets/Encrypt.png")
encrypt_button = Button(
    frame,
    image=encrypt_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: encrypt(),
    bg="#ffffff"
)
encrypt_button.place(
    x=87, y=304 
)

decrypt_img = PhotoImage(file="./assets/Decrypt.png")
decrypt_btn = Button(
    frame,
    image=decrypt_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: decrypt(),
    bg="#ffffff"
)
decrypt_btn.place(
    x=325, y=304    
)

#Load an image in the script
photo = (Image.open("./assets/Photo.png"))
#Resize the Image using resize method
resized_image= photo.resize((80,70), Image.ANTIALIAS)
rezised = ImageTk.PhotoImage(resized_image)

photo_label = Label(frame, image=rezised, bg="#ffffff")
photo_label.place(
    x=1035, y=33
)

plug_in_img = PhotoImage(file='./assets/Plug In.png')
plug_in_btn = Button(
    frame,
    image=plug_in_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: plug_in(),
    bg="#ffffff"
)
plug_in_btn.place(
    x=88, y=393
)

plug_out_img = PhotoImage(file='./assets/Plug Out.png')
plug_out_btn = Button(
    frame,
    image=plug_out_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: plug_out(),
    bg="#ffffff"
)
plug_out_btn.place(
    x=325, y=393
)

setting_img = PhotoImage(file='./assets/Setting.png')
setting_btn = Button(
    frame,
    image=setting_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: check(),
    bg="#ffffff"
)
setting_btn.place(
    x=88, y=393+90
)

change_img = PhotoImage(file='./assets/Change.png')
change_btn = Button(
    frame,
    image=change_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: insert(),
    bg="#ffffff"
)
change_btn.place(
    x=325, y=393+90
)

# Add a Scrollbar(horizontal)
textbox = Frame(win, height=1)

# Add a text widget
text = Label(frame, width=76, height=21, font=("Arial", 7))

text.place(
    x=604, y=304
)

# Functionalities

def log():
    global text
    f = open("./output/out_read.txt")
    f = f.read()
    text['text'] = f
    text.update()

def check():
    global machine
    info = "Index starts from 0\n"
    info += f"Plugboard : \n{machine.pb.board}\n"
    info += f"Rotor 1 : \n{machine.rc.rotor_one.wiring}\n current index : {machine.rc.cnt_1}\n rotate index: {machine.rc.to_1}\n"
    info += f"Rotor 2 : \n{machine.rc.rotor_two.wiring}\n current index : {machine.rc.cnt_2}\n rotate index: {machine.rc.to_2}\n"
    info += f"Rotor 3 : \n{machine.rc.rotor_three.wiring}\n current index : {machine.rc.cnt_3}\n rotate index: {machine.rc.to_3}\n"
    info += f"Reflector: {machine.rf.wiring}\n"
    messagebox.showinfo(title="Settings", message=info)


def encrypt():
    global text_label
    global out_label
    global machine
    reset_file()
    input_text = text_label.get("1.0", "end-1c").upper()
    input_text = machine.encrypt_all(input_text)
    out_label['text'] = input_text
    out_label.update()
    log()
    
def decrypt():
    global text_label
    global out_label
    global machine
    reset_file()
    input_text = text_label.get("1.0", "end-1c").upper()
    input_text = machine.decrypt_all(input_text)
    out_label['text'] = input_text
    out_label.update()
    log()

def reset():
    global machine
    global out_label
    global text_label
    global file
    global text
    reset_file()
    machine = enigma(file)
    text_label.delete("1.0","end")

    out_label['text'] = ""
    out_label.update()
    text['text'] = ""
    text.update()

# change file input
def insert():
    global machine
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
    )
    machine = enigma(filename)

def plug_in():
    global machine
    alpha_1 = sd.askstring("Input", "Input Alphabet 1", parent=frame).upper()
    alpha_2 = sd.askstring("Input", "Input Alphabet 2", parent=frame).upper()
    machine.plug(alpha_1, alpha_2)

def plug_out():
    global machine
    alpha = sd.askstring("Input", "Input Alphabet", parent=frame).upper()
    machine.unplug(alpha)


# def cluster():
#     global out
#     global clustered
#     n = sd.askinteger("Input", "Input cluster number", parent=frame)

#     clustered = cluster_mst(out, n)
#     visualize_cluster(clustered)

#     graph_img = (Image.open("./img/Cluster.png"))
#     resized_image= graph_img.resize((400,350), Image.ANTIALIAS)
#     resized_graph_image = ImageTk.PhotoImage(resized_image)
#     change_image(resized_graph_image)

win.mainloop()