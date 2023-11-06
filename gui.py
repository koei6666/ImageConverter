from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import module

class Interface:
    def __init__(self, root):
        #root
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("480x120")

        #frame
        self.titleframe = ttk.Frame(root)
        self.mainframe = ttk.Frame(root)
        self.convertbframe = ttk.Frame(root)
        self.statusbframe = ttk.Frame(root)

        #buttons
        self.file_browser = ttk.Button(self.mainframe, text="Open File", command=lambda: self.file_dialog(self.status))
        self.convert = ttk.Button(self.convertbframe, text="Convert to JPEG", command=lambda: module.multiple_process(self.pathlist, self.status) )
        self.convert2base64 = ttk.Button(self.convertbframe, text="Convert to Base64", command=self.base64output)

        #text variables
        self.textbar_value = StringVar()
        self.statusbar_value = StringVar()

        #labels
        self.title = ttk.Label(self.titleframe, text="HEIC2JPEG Format Converter__", style="title.TLabel")
        self.textbar = ttk.Label(self.mainframe, textvariable=self.textbar_value)
        self.statusbar = ttk.Label(self.statusbframe, textvariable=self.statusbar_value)

        #pack
        self.titleframe.pack(fill=BOTH, expand=True)
        self.title.pack(side=LEFT)
        self.mainframe.pack()
        self.textbar.pack(anchor=CENTER)
        self.file_browser.pack(anchor=CENTER)
        self.convertbframe.pack()
        self.convert.pack(anchor=CENTER)
        self.statusbframe.pack()
        self.statusbar.pack(anchor=CENTER)
        self.convert2base64.pack(ancho=CENTER)

        #Style
        st = ttk.Style()
        st.configure("title.TLabel", font=("Helvetica",13,"bold"))

        #values
        self.pathlist = None




    def file_dialog(self, update_func):
        file_path = askopenfilename(title="Select Files to Convert.", filetypes=[("All Files", "*.*")], multiple=True)
        output = []
        count = 0
        for path in file_path:
            if path and module.is_image(path):
                output.append(path)
            else:
                count += 1
                update_func(f"{count} non HEIC file found, it will be deselected!")
        if output:
            self.label_updater(output)
            self.pathlist = output


    def label_updater(self, path_list, format=None):
        count = 0
        if path_list:
            count = len(path_list)
        if not format:
            format = "JPEG"
        text = f"{count} files selected to be converted to {format}."
        self.textbar_value.set(text)

    def status(self,status):
        self.statusbar_value.set(status)

    def base64output(self):

        file_path = askopenfilename(title="Select Files to Convert.", filetypes=[("All Files", "*.*")], multiple=False)

        text = module.base64cove(file_path)

        output_top = Toplevel(self.root)
        output_top.title("Base64 Output")

        result_frame = ttk.Frame(output_top)
        result_frame.pack(expand=True)

        result_text = Text(result_frame)
        result_text.pack(expand=True)

        result_text.insert(END, text)









def create_root():
    root = Tk()
    return root
