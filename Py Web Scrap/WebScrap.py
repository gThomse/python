from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import sys
import requests
import os

from bs4 import BeautifulSoup as bs

## **** Global Variables Block

url = ""
txt_f = ""

# ***** COMMENT LINE - CODE BLOCK

def html_words():
    key_words = ('script', 'java', 'javascript', 'browser', 'url' )
    return(key_words)

# ***** COMMENT LINE - CODE BLOCK

def with_in(_str):
    short_str = _str.lower()
    for s in short_str.split():
        if s in html_words():
            return (True)
    return (False)

def open_soup(url_web):

   try:
       page = requests.get(url_web)
       soup = bs(page.content, 'lxml')
   except:
         res = messagebox.showinfo('Error','URL not Valid - please retry')
##         sys.exit("Links not found - system exit called")       
   return (soup)

# ***** COMMENT LINE - CODE BLOCK

def write_to_file(txtfile, data):

    print (os.getcwd())
    with open(txtfile,"w") as outf:

        lastline = None
        body = data.prettify
        body_str = data.body.strings
        blankline_counter = 0

        for line in body_str:
            word_count = line.split()
            line_len = len(line.strip())
            blankline_counter = blankline_counter + 1 if line_len == 0 else 0
            
            if blankline_counter == 0 and line_len == 0:
                outf.write(f"{line}")
            elif line_len > 0:
                if not with_in (line):
                    if lastline != line and len(word_count) > 1:
                        outf.write(f"\n{line}")
                        lastline = line
                        
        res = messagebox.showinfo('Info',f'File written to {txtfile}')
              
##        print (f"Text output to {txtfile}\n")
    return

# ***** COMMENT LINE - CODE BLOCK
  
def n_form(width, height, title):
    out_file = "Scrapped_Web_Page.txt"
    initialsed = False
    output_to = ""
    
    def cmd_scrap():
        url = txt.get()
        txt_f = lbl_dest.cget("text")
        print (f"lenght of url {url} \n is {len(url)}\n")
        print (f"Length of file is {txt_f} \n is {len(txt_f)}\n")
        if len(url) > 0 and len(txt_f) > 0:
            soup = open_soup(url)
            write_to_file(txt_f, soup)
        elif len(txt_f) > 0:
            res = messagebox.showinfo('Error','Missing URL - please supply')
        else: 
            res = messagebox.showinfo('Error','Missing Destination - please supply')
        
    def cmd_exit():
        f = new_form
        local_str = "TxtFile.txt"
        print (initialsed )
        if initialsed == True:
            print (local_str, initialsed)
            f.destroy()
        else:
            print (local_str, initialsed)

    def cmd_file():
        output_to = ""
        print ("*** 1")
        output_to = file = filedialog.askdirectory(title = "Select Directory")
        lbl_dest.configure(text = output_to +'/' + out_file)
        print ("*** 9")

    new_form = Tk()

    # Haven't worked out how to return current values of geometry so.. work around... :) 
    short_str= str(width) + 'x' + str(height)
    # Sets window width and height from top left position.
    new_form.geometry(short_str)

    ##print(new_form.winfo_screenheight(),new_form.winfo_screenwidth())
    new_form.title(title)

    # Gets both half the screen width/height and window width/height

    positionRight = int(new_form.winfo_screenwidth()/2 - width/2)
    positionDown = int(new_form.winfo_screenheight()/2 - height/2)

    # Positions the window in the center of the page.
    new_form.geometry("+{}+{}".format(positionRight, positionDown))


    MyButton1 = Button(new_form, text="Scrap", width=10,command = cmd_scrap)
    MyButton1.place(x=450, y=25)
            
    MyButton2 = Button(new_form, text="Destination", width=10, command= cmd_file)
    MyButton2.place(x=50, y=100)

    MyButton3 = Button(new_form, text="Close", width=10, command= cmd_exit)
    MyButton3.place(x=600, y=25)
    initialsed = True

    lbl_dest = Label(new_form, text="")
    lbl_dest.place(x=146, y=103)

    lbl = Label(new_form, text="Please enter URL:")
    lbl.place(x=50, y=200)

    txt = Entry(new_form,width=90)
    txt.focus()
    txt.place(x=146, y=200)

    new_form.mainloop()

# ***** COMMENT LINE - CODE BLOCK

def process_data (data):
   # function to write output.
   return()
    
# ***** COMMENT LINE - CODE BLOCK

def main():
    
   n_form(725,300,"Web Scraper")   # Open up a new form to capture input

   print("Finished... \nHave a nice day\n")   
##   write_to_screen_body_text(soup)

##
##   process_data (soup)

# ***** COMMENT LINE - CODE BLOCK

## MAIN MAIN MAIN MAIN MAIN ##

if __name__ == '__main__' :
   main()
else:
   print ('Doing nothing')




