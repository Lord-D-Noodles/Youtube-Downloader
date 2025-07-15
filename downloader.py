from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as Tk

window = Tk.Tk()


input_box = Tk.Entry(window)
window.geometry("100x100")
window.configure(bg="red")
input_box.pack()

def download(string):
    yt = YouTube(string, on_progress_callback=on_progress)
    print(yt.title)
    ys = yt.streams.get_lowest_resolution()
    ys.download(output_path = "downloads")

def get_input(Event = None): 
    html = input_box.get()
    print(html)
    download(html)

input_box.bind("<Return>", get_input)
Tk.mainloop()


