from tkinter import *
from tkinter.ttk import *

def emptyTree(tree):
    for i in tree.get_children():
        tree.delete(i)

def createTree(tree, cols, yscroll, widths):#len(widths) must >= len(cols)
    #creates headings
    for i in range(len(cols)):
        tree.heading('#'+str(i+1), text = cols[i], anchor = W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    for i in range(len(cols)):
        tree.column('#'+str(i+1), stretch = NO, minwidth = widths[i], width = widths[i])
    tree.configure(yscroll=yscroll.set)#yscroll bar

def insertIntoTree(tree, values):
    if len(tree.get_children()) > 0:
        emptyTree(tree)
    for i in values:
        tree.insert("", END, "", values=i, tag='rowFont')

myGUI = Tk()

myCols = ['column'+str(x) for x in range(1,6)]
myTree = Treeview(myGUI, columns = myCols,selectmode = 'browse', height = 5)
#default selectmode is extended - with browse you can only select one item at a time
yscrollbar = Scrollbar(myGUI, orient='vertical', command=myTree.yview)
createTree(myTree, myCols, yscrollbar, (90,150,150,150,150))

myTree.grid(row = 1, column = 1, sticky = NSEW)
yscrollbar.grid(row =1, column = 1, sticky = E+NS)
#haven't messed around with stick a lot so you might be able to change it to something else
#i know that it's so you can have two things in the same grid cell

data = [['stuff'+str(x)+str(y) for x in range(1,6)] for y in range(1,10)]
insertIntoTree(myTree, data)



#haven't added code for this:
#to get the item that's selected in the treeview use - tree.focus()
#that returns a code e.g. first item will be I001
#then if you use -  tree.item(tree.focus())
#you get a dict with things in it
#for the tupe of values of that item in the tree - tree.item(tree.focus())['values']
