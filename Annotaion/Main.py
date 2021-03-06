from Tkinter import *
import glob
import os

root = Tk()
root.title("HW5 - Ahmad Jarrar")
root.geometry("600x650")
global currentFileName


def crawl():
    print ("crawling..")
    content = webLink.get()
    print ("crawling: " + content)


def startAnno():
    index = 1
    for filename in glob.glob('*.txt'):
        listBoxFiles.insert(index, filename)
        index += 1


def on_file_select(event):
    global currentFileName
    TextArea.delete("1.0", END)
    file = listBoxFiles.get(listBoxFiles.curselection())
    currentFileName = file
    Filedir = os.path.dirname(__file__) + "/" + file
    print Filedir
    with open(Filedir, 'r') as content_file:
        content = str(content_file.read())
        print content
        TextArea.insert(INSERT, content)


def on_Tag_select(event):
    global currentFileName
    folderName = listBoxTags.get(listBoxTags.curselection())
    Filedir = os.path.dirname(__file__) + "/" + folderName + "/" + currentFileName
    print Filedir
    article = TextArea.get("1.0", END)
    text_file = open(Filedir, "w")
    text_file.write(article)
    text_file.close()


Label(root, text='Please enter a URL to crawl').pack(side=TOP, padx=10, pady=1)
# URL textBox
webLink = StringVar()
url = Entry(root, width=70, textvariable=webLink).pack(side=TOP, padx=10, pady=1)
# Button crawl
Button(root, text='Crawl', command=crawl).pack(side=TOP, padx=10, pady=1)
# Button annotation
Button(root, text='Start annotation', command=startAnno).pack(side=TOP, padx=10, pady=2)
# ListBox to show files
listBoxFiles = Listbox(root)
listBoxFiles.config(height=4, width=70)
listBoxFiles.bind('<<ListboxSelect>>', on_file_select)
listBoxFiles.pack()
# Article textBox
TextArea = Text()
ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack(expand=NO, fill=X)
Label(text='Please select an annotation:').pack(side=TOP, padx=10, pady=3)
# Tags selection listBox
listBoxTags = Listbox(root)
listBoxTags.config(height=4)
listBoxTags.insert(1, "Entertainment")
listBoxTags.insert(2, "Sport")
listBoxTags.insert(3, "News")
listBoxTags.bind('<<ListboxSelect>>', on_Tag_select)
listBoxTags.pack()
root.mainloop()
