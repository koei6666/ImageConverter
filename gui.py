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

        #mainframe
        self.mainframe = ttk.Frame(root)

        #buttons
        self.file_browser = ttk.Button(self.mainframe, text="Open File", command=self.file_dialog)
        self.convert = ttk.Button(self.mainframe, text="Convert to JPEG", command=lambda: module.multiple_process(self.pathlist, self.status) )

        #text variables
        self.textbar_value = StringVar()
        self.statusbar_value = StringVar()

        #labels
        self.textbar = ttk.Label(self.mainframe, textvariable=self.textbar_value)
        self.statusbar = ttk.Label(self.mainframe, textvariable=self.statusbar_value)

        #pack
        self.mainframe.pack()
        self.textbar.pack(anchor=CENTER)
        self.file_browser.pack(anchor=CENTER)
        self.convert.pack(anchor=CENTER)
        self.statusbar.pack(anchor=CENTER)

        #values
        self.pathlist = None




    def file_dialog(self):
        file_path = askopenfilename(title="Select Files to Convert.", filetypes=[("All Files", "*.*")], multiple=True)
        output = []
        for path in file_path:
            if path and module.is_image(path):
                output.append(path)
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







def create_root():
    root = Tk()
    return root
