import tkinter as tk

# main window   
root = tk.Tk()
root.wm_geometry("300x400")

red_frame = tk.Frame(root, bg='red', width=200, height=200);
blue_frame = tk.Frame(root, bg='blue', width=200, height=200);
green_frame = tk.Frame(root, bg='green', width=100, height=200);
yellow_frame = tk.Frame(root, bg='yellow', width=100, height=200);

red_frame.grid(row = 4, column = 0, sticky = 'news', columnspan=3, padx=0, pady=0)
blue_frame.grid(row = 0, column = 0, sticky = 'news', columnspan=3, padx=0, pady=0)
green_frame.grid(row = 0, column = 4, sticky = 'news', columnspan=3, padx=0, pady=0)
yellow_frame.grid(row = 4, column = 4, sticky = 'news', columnspan=3, padx=0, pady=0)




tk.mainloop()