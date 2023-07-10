import os

def write(txt):
    f = open("./output/out.txt", "a")
    f.write(txt + f"\n") 

def write_out(txt):
    f = open("./output/out_read.txt", "a")
    f.write(txt) 

def reset_file():
    os.remove("./output/out_read.txt")
    os.remove("./output/out.txt")
    f = open("./output/out_read.txt", "w")
    f.write("")
    f = open("./output/out.txt", "w")
    f.write("")
