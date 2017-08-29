import main as DivideImage
import Tkinter as tk

class Options:
    folder = None
    dest = None
    row = None
    col = None
    def __init__(self, folder=None, dest=None, row=1, col=1):
        self.folder = folder
        self.dest = dest
        self.row = row
        self.col = col


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def _ask_directory(self):
        from tkFileDialog import askdirectory
        self.update()
        result = askdirectory()
        return result

    def _ask_from_dir(self):
        result = self._ask_directory()
        if result:
            self.fromDir.configure(text=result)
            if self.toDirSameAsFromDir:
                self.toDir.configure(text=result)


    def _ask_to_dir(self):
        result = self._ask_directory()
        if result:
            self.toDir.configure(text=result)

    
    def _setToDirSameAsFromDir(self):
        newValue = not self.toDirSameAsFromDir
        self.toDirSameAsFromDir = newValue
        ## Disable toDirBtn when set same as fromDir
        self.toDirBtn['state'] = 'disabled' if newValue else 'normal'


    def _lock_ensure(self):
        self.sliceStatus.configure(text='slicing...')
        self.update()
        self.ensure['state'] = 'disabled'


    def _unlock_ensure(self, message='Done!'):
        self.sliceStatus.configure(text=message)
        self.ensure['state'] = 'normal'


    def _slice(self):
        self._lock_ensure()
        fromDir = self.fromDir.cget('text')
        toDir = self.toDir.cget('text')
        try:
            sliceInto = int(self.sliceIntoTextInput.get())
        except:
            self._unlock_ensure(message="please enter slice into value")
            return
        options = Options(folder=fromDir, dest=toDir, row=sliceInto)
        errMsgs = DivideImage.do_slice(options)
        newText = '\n'.join(errMsgs) if len(errMsgs) else 'Done!'
        self._unlock_ensure(message=newText)


    def createWidgets(self):
        self.fromDirBtn = tk.Button(self)
        self.fromDirBtn['text'] = 'fromDir'
        self.fromDirBtn['command'] = self._ask_from_dir
        self.fromDirBtn.grid(row=0, column=0)

        self.fromDir = tk.Label(self, text='./')
        self.fromDir.grid(row=0, column=1)

        self.toDirBtn = tk.Button(self)
        self.toDirBtn['text'] = 'to'
        self.toDirBtn['command'] = self._ask_to_dir
        self.toDirBtn['state'] = 'disabled'
        self.toDirBtn.grid(row=1, column=0)

        self.toDir = tk.Label(self, text='./')
        self.toDir.grid(row=1, column=1)

        self.toDirSameAsFromDir = True
        self.toDirSameAsFromDirBtn = tk.Checkbutton(self)
        self.toDirSameAsFromDirBtn['text'] = 'toDir same as fromDir'
        self.toDirSameAsFromDirBtn['command'] = self._setToDirSameAsFromDir
        self.toDirSameAsFromDirBtn['variable'] = self.toDirSameAsFromDir
        self.toDirSameAsFromDirBtn['onvalue'] = True
        self.toDirSameAsFromDirBtn['offvalue'] = False
        self.toDirSameAsFromDirBtn.select()
        self.toDirSameAsFromDirBtn.grid(row=2, column=0)

        self.sliceInto = tk.Label(self, text='horizon slice into')
        self.sliceInto.grid(row=3, column=0)

        self.sliceIntoTextInput = tk.Entry(self)
        self.sliceIntoTextInput.grid(row=3, column=1)

        self.ensure = tk.Button(self)
        self.ensure['text'] = 'ok'
        self.ensure['command'] = self._slice
        self.ensure.grid(row=4, column=0)

        self.sliceStatus = tk.Label(self, text="")
        self.sliceStatus.grid(row=5, column=0)

if __name__ == "__main__":
    window = tk.Tk()
    app = Application(window)
    app.master.title("Divide image tool")
    app.master.minsize(400, 400)
    app.mainloop()
