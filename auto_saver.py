import pyautogui
import time as _time
import tkinter as tk
from tkinter import ttk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("690x520")
        self.title("Auto keybind tool")

        self.interval = ("1 sec", "2 secs", "5 secs", "10 secs", "30 secs (recommended)", "1 min", "2 mins", "5 mins", "10 mins", "30 mins") #time interval
        self.application = ("Visual Studio Code", "VSCodium", "Visual Studio", "PyCharm", "Notepad++", "Use universal keybinds / Others") #basically the most useless thing in this code
        self.keybindset0 = ("Ctrl+S", "Other specified") #universal keybind
        self.keybindset1 = ("Ctrl+S", "Other specified") #keybind for vscode
        self.keybindset2 = ("Ctrl+S", "Ctrl+Shift+S", "Other specified") #keybind for visual studio
        #i wonder why theres no 3?
        self.keybindset4 = ("Ctrl+S", "Ctrl+Shift+S", "Ctrl+Alt+S", "Other specified") #keybind for notepad++
        self.option_var0 = tk.StringVar(self)
        self.option_var1 = tk.StringVar(self)
        self.option_var2 = tk.StringVar(self)
        self.option_var3 = tk.StringVar(self)
        self.option_var4 = tk.StringVar(self)
        self.option_var5 = tk.StringVar(self)

        global paddings
        paddings = {"padx":40, "pady":5}

        self.widgets()
    
    def widgets(self):
        global label1, label2, label4, option_menu1, option_menu2, option_menu4

        #default time intervals
        label1 = ttk.Label(self, text='Interval (too low may lag your crap pc):')
        label1.place(x=25, y=42.5)
        option_menu1 = ttk.OptionMenu(self, self.option_var0, 'Unspecified', *self.interval, command=self.option0_changed)
        option_menu1.place(x=365, y=42.5) #30 (~object height) + 5 (top pady) + 5 (bottom pady) + pady/2

        #default applications
        label2 = ttk.Label(self, text='Application:')
        label2.place(x=25, y=82.5)
        option_menu2 = ttk.OptionMenu(self, self.option_var1, 'Unspecified', *self.application, command=self.option1_changed)
        option_menu2.place(x=365, y=82.5) #+40

        #default keybinds
        label4 = ttk.Label(self, text='Keybinds:')
        label4.place(x=25, y=122.5)
        option_menu4 = ttk.OptionMenu(self, self.option_var2, 'Unspecified', *self.keybindset0, command=self.option2_changed)
        option_menu4.place(x=365, y=122.5) #+40

        button = ttk.Button(self, text='Confirm and start', command=self.start)
        button.place(x=25, y=202.5)

        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=0)
    
    def specified1(self):
        try:
            label5.destroy()
            option_menu5.destroy()
        except NameError: pass
        global label4, option_menu4
        if self.option_var1.get() == "Visual Studio Code" or self.option_var1.get() == "VSCodium":
            label4.place(x=25, y=122.5)
            option_menu4 = ttk.OptionMenu(self, self.option_var2, 'Unspecified', *self.keybindset1, command=self.option2_changed)
            option_menu4.place(x=365, y=122.5) #inherited coordinates
        elif self.option_var1.get() == "Visual Studio":
            label4.place(x=25, y=122.5)
            option_menu4 = ttk.OptionMenu(self, self.option_var2, 'Unspecified', *self.keybindset2, command=self.option2_changed)
            option_menu4.place(x=365, y=122.5) #inherited coordinates
        elif self.option_var1.get() == "Notepad++":
            label4.place(x=25, y=122.5)
            option_menu4 = ttk.OptionMenu(self, self.option_var2, 'Unspecified', *self.keybindset4, command=self.option2_changed)
            option_menu4.place(x=365, y=122.5) #inherited coordinates
        elif self.option_var1.get() == "PyCharm" or self.option_var1.get() == "Use universal keybinds / Others":
            label4.place(x=25, y=122.5)
            option_menu4 = ttk.OptionMenu(self, self.option_var2, 'Unspecified', *self.keybindset0, command=self.option2_changed)
            option_menu4.place(x=365, y=122.5) #inherited coordinates (ughhhh repeated 4 times, are you satisfied yet?)

    def specified2(self):
        global label5, option_menu5
        if self.option_var2.get() == "Other specified":
            label5 = ttk.Label(self, text='Custom keybind (keys/hotkeys):')
            label5.place(x=25, y=162.5)
            option_menu5 = ttk.Entry(self, textvariable=self.option_var5)
            option_menu5.place(x=365, y=162.5) #+40, what did you expect
        else:
            try:
                label5.destroy()
                option_menu5.destroy()
                label4.place(x=25, y=122.5)
                option_menu4.place(x=365, y=122.5)
                return
            except NameError: pass

    def start(self):
        global interval, key0, key1, key2

        time = self.option_var0.get().lower()
        if time.endswith("(recommended)"):
            time.replace(" (recommended)", "")
        if time.split()[1] == 'secs' or time.split()[1] == 'sec':
            interval = int(time.split()[0])
        elif time.split()[1] == "mins" or time.split()[1] == 'min':
            interval = int(time.split()[0]) * 60

        keys = self.option_var2.get().lower()
        if keys == 'other specified':
            keys = self.option_var5.get().lower()
            keys = keys.replace(' ', '')
            if '+' in keys:
                subkeys = keys.split('+')
                if len(subkeys) > 2:
                    key0, key1, key2 = subkeys
                else:
                    key0, key1, key2 = subkeys[0], subkeys[1], None
            else:
                key0, key1, key2 = keys, None, None
                   
        else:
            if '+' in keys:
                subkeys = keys.split('+')
                if len(subkeys) > 2:
                    key0, key1, key2 = subkeys
                else:
                    key0, key1, key2 = subkeys[0], subkeys[1], None
            else:
                key0, key1, key2 = keys, None, None
    
        while True:
            print(key0, key1, key2)
            if key0 != None and key1 == None and key2 == None:
                pyautogui.hotkey(key0)
            elif key0 != None and key1 != None and key2 == None:
                pyautogui.hotkey(key0, key1)
            else:
                pyautogui.hotkey(key0, key1, key2)
                _time.sleep(interval)
            
    #debug
    def option0_changed(self, *args):
        self.output_label['text'] = f'[{self.option_var0.get()}]'

    def option1_changed(self, *args):
        self.output_label['text'] = f'[{self.option_var1.get()}]'
        self.specified1()

    def option2_changed(self, *args):
        self.output_label['text'] = f'[{self.option_var2.get()}]'
        self.specified2()

Main().mainloop()
