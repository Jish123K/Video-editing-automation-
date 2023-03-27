import os

import tkinter as tk

from tkinter import filedialog, messagebox

from combo_creator import combo

class ComboWindow:

    def __init__(self, master):

        self.master = master

        master.title("Video Combining Tool")

        # select folder components

        input_details_file_label = tk.Label(master, text="Input Details ", font=("Arial", 25, "bold"))

        input_details_file_label.grid(row=0, column=0, padx=20, pady=10)

        select_file_label = tk.Label(master, text="Select the input folder")

        select_file_label.grid(row=1, column=0, padx=20, pady=5)

        self.select_folder_textbox = tk.Entry(master, width=50)

        self.select_folder_textbox.grid(row=2, column=0, padx=20, pady=5)

        browse_button = tk.Button(master, text="Browse", command=self.browse_folder)

        browse_button.grid(row=2, column=1, padx=5, pady=5)

        tip_label = tk.Label(master, text="Tip: We will create a combination of clips from the contents.", font=("Courier", 10))

        tip_label.grid(row=3, column=0, padx=20, pady=10)

        # status components && variables

        output_details_file_label = tk.Label(master, text="Options & Status", font=("Arial", 25, "bold"))

        output_details_file_label.grid(row=4, column=0, padx=20, pady=10)

        self.progress = tk.ttk.Progressbar(master, orient="horizontal", length=460, mode="determinate")

        self.progress.grid(row=5, column=0, padx=20, pady=5, columnspan=2)

        destination_file_label = tk.Label(master, text="Enter a File Name")

        destination_file_label.grid(row=6, column=0, padx=20, pady=5)

        self.output_file_name = tk.Entry(master, width=50)

        self.output_file_name.insert(0, "mycombo.mp4")

        self.output_file_name.grid(row=7, column=0, padx=20, pady=5)

        create_button = tk.Button(master, text="Create", command=self.call_combo)

        create_button.grid(row=7, column=1, padx=5, pady=5)

    # All Custom Methods

    # select folder path for input files

    def browse_folder(self):

        folder_path = filedialog.askdirectory()

        self.select_folder_textbox.delete(0, tk.END)

        self.select_folder_textbox.insert(0, folder_path)

    # set progress bar value

    def set_combo_progress(self, value):

        self.progress["value"] = value

        self.master.update_idletasks()

    # set status text

    def set_combo_status_tip_text(self, value):

        self.master.after(10, lambda: messagebox.showinfo("Info", value))

    # call combination video creation video

    def call_combo(self):

        input_folder = self.select_folder_textbox.get()

        output_file = self.output_file_name.get()

        if input_folder and output_file:

            combo.create_combo(self, input_folder, output_file)

        else:

            messagebox.showerror("Error", "Please select input folder and enter output file name")

def main():

    root = tk.Tk()

    app = ComboWindow(root)

    root.mainloop()

if __name__ == '__main__':

    main() 

