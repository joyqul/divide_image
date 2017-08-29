import Tkinter as tk

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
        self.fromDir.configure(text=result)

    def _ask_to_dir(self):
        result = self._ask_directory()
        self.toDir.configure(text=result)

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
        self.toDirBtn.grid(row=1, column=0)

        self.toDir = tk.Label(self, text='./')
        self.toDir.grid(row=1, column=1)


if __name__ == "__main__":
    window = tk.Tk()
    app = Application(window)
    app.master.title("Divide image tool")
    app.master.minsize(400, 400)
    app.mainloop()
