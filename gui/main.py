from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self._init_style()
        self._init_menu()
        self._init_text()
        self._init_sidebar()

    def _init_menu(self):
        self.menubar = MenuBar(self)
        self.master["menu"] = self.menubar

    def _init_text(self):
        self.text = InputText(self)
        self.text.pack(side=LEFT)

    def _init_sidebar(self):
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side=RIGHT)

    def _init_style(self):
        self.master.title = "Japp v. 0.1"
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

    def open_file(self):
        filename = filedialog.askopenfile(mode="r")

        with open(filename, "r"):
            content = filename.read()

        self.text.textarea.delete(INSERT, END)
        self.text.textarea.insert(INSERT, content)

class MenuBar(Menu):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.filemenu = Menu(self, tearoff=False)
        self.file_open = self.filemenu.add_command(label="Open...", command=lambda: self.master.open_file)

        self.add_cascade(label="File", menu=self.filemenu)

class InputText(LabelFrame):
    def __init__(self, master=None):
        super().__init__(master=master, text="Input text")
        self.master = master
        self.pack(fill="both", expand=True)
        self.textarea = Text(self)
        self.textarea.pack()

class Sidebar(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master

        self.lfr_options = LabelFrame(self, text="Options")
        self.lfr_options.pack()

        self.chk_autofuriganize = Checkbutton(self.lfr_options, text="Auto furiganize on load")
        self.chk_autofuriganize.pack()

        self.btn_save = Button(self, text="Save")
        self.btn_save.pack(expand=True)

        self.btn_load = Button(self, text="Load")
        self.btn_load.pack(expand=True)

if __name__ == "__main__":
    root = Tk()
    app = App(master=root)
    app.mainloop()
