import turtle
import tkinter

def main():
    def start():
        print("Start")
        #TODO write
    root=tkinter.Tk()
    root.title("Patience")
    cv=turtle.ScrolledCanvas(root,600,600,600,600)
    cv.tk_setPalette(background="green")
    cv.pack(side=tkinter.LEFT)
    
    bar=tkinter.Menu(root)
    fileMenu=tkinter.Menu(bar,tearoff=0)
    fileMenu.add_command(label="Start",command=start)
    bar.add_cascade(label="File",menu=fileMenu)
    root.config(menu=bar)
    
if __name__ == "__main__":
    main()
    tkinter.mainloop()