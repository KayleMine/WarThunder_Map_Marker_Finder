from tkinter import *
import sys
#import time
#import os
#import signal
#import asyncio   
#from threading import Timer             
import win32gui, win32api, win32con, pywintypes
import traceback
import configparser
#import pdb

try:

    def read_config(name):
        config = configparser.ConfigParser()
        config.read(name, encoding='utf-8')
        conf = {}
        conf['print_x'] = config.get("Combinations", "print_x")
        conf['print_y'] = config.get("Combinations", "print_y")
        conf['print_distance'] = config.get("Combinations", "print_distance")
        conf['print_azimuth'] = config.get("Combinations", "print_azimuth")
        conf['print_scale'] = config.get("Combinations", "print_scale")
        conf['print_transparent'] = config.get("Combinations", "print_transparent")
        conf['print_time'] = config.get("Combinations", "print_time")
        return conf
    conf = read_config("code/buttons.ini")
    
    bg = ""
    fg = ""
    if conf['print_transparent'] == "1":
        bg = 'white'
        fg = 'yellow'
    else:
        bg = 'yellow'
        fg = 'black'        
    
    geometry = f"+{conf['print_x']}+{conf['print_y']}"
    
    code = sys.argv[1]

    root = 0
    
    if code == "true":

        distance = sys.argv[2]
        angel = sys.argv[3]
        scale = sys.argv[4]

        ######################################################################
        #Создание диалогового окна с результатами

        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text1 = f'Дист: {distance}'
        text2 = f'Азимут: {angel}'
        text3 = f'м. {scale}'
        
        if conf['print_distance'] == "1":
            label1 = Label(root, text=text1, font=('Roboto','19'), fg=fg, bg=bg)
            label1.pack(anchor="nw", padx=5)            
        if conf['print_azimuth'] == "1":
            label2 = Label(root, text=text2, font=('Roboto','19'), fg=fg, bg=bg)
            label2.pack(anchor="nw", padx=5)              
        if conf['print_scale'] == "1":   
            label3 = Label(root, text=text3, font=('Roboto','19'), fg=fg, bg=bg)
            label3.pack(anchor="nw", padx=5) 
                
        root.overrideredirect(True)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(root.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
    elif code == "errorArrow":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text1 = 'твой танк\nне найден'
        text2 = f'м. {scale}'
        label1 = Label(root, text=text1, font=('Roboto','19'), fg=fg, bg=bg)
        label1.pack(padx=5)
        if conf['print_scale'] == "1":   
            label2 = Label(root, text=text2, font=('Roboto','19'), fg=fg, bg=bg)
            label2.pack(padx=5)
        
        root.overrideredirect(True)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(root.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
    elif code == "errorMarker":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text1 = 'метка\nне найдена'
        text2 = f'м. {scale}'
        label1 = Label(root, text=text1, font=('Roboto','19'), fg=fg, bg=bg)
        label1.pack(padx=5)
        if conf['print_scale'] == "1":       
            label2 = Label(root, text=text2, font=('Roboto','19'), fg=fg, bg=bg)
            label2.pack(padx=5)
            
        root.overrideredirect(True)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(root.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        
    elif code == "AError":
        scale = sys.argv[2]
        root = Tk()
        root.configure(bg = bg)
        root.geometry(geometry) 
        text1 = 'буквы а е\nсовпадают'
        text2 = f'м. {scale}'
        label1 = Label(root, text=text1, font=('Roboto','19'), fg=fg, bg=bg)
        label1.pack(padx=5)
        if conf['print_scale'] == "1":
            label2 = Label(root, text=text2, font=('Roboto','19'), fg=fg, bg=bg)
            label2.pack(padx=5)
            
        root.overrideredirect(True)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)
        if conf['print_transparent'] == "1":
            root.wm_attributes("-transparentcolor", bg)
        
        hWindow = pywintypes.HANDLE(int(root.frame(), 16)) 
        exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        

    def selectWindow(event=1):
        try:
            toplist = []
            winlist = []
            def enum_callback(hwnd, results):
                winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

            win32gui.EnumWindows(enum_callback, toplist)
            wt = [(hwnd, title) for hwnd, title in winlist if 'war thunder' in title.lower()]
            # just grab the first window that matches
            #pdb.set_trace()
            if wt !=[]:
                wt = wt[0]
                # use the window handle to set focus
                win32gui.SetForegroundWindow(wt[0])  
            
        except Exception as e:

            if e.funcname == "SetForegroundWindow":
                pass
            else:
                file = open('error.log', 'a')
                file.write('\n\n')
                traceback.print_exc(file=file, chain=True)
                traceback.print_exc()
                file.close()
                

    root.after(0, selectWindow)   
    root.after(int(float(conf['print_time'])*1000), root.destroy)
    root.mainloop()        


    #arguments: 
    #how long to wait (in seconds), 
    #what function to call, 
    #what gets passed in
    #r = Timer(3.0, quitProcess, NONE)
    #s = Timer(2.0, nArgs, ("OWLS","OWLS","OWLS"))

    #r.start()
    #s.start()
    #async def quitProcess():
    #    await asyncio.sleep(3)
    #    quit()

    #asyncio.run(quitProcess())


    #timeout = 5
    #t = Timer(timeout, os._exit, [1])
    #t.start()
    #try:
    #    prompt = "У вас есть %d секунд чтобы ввести ответ...\n" % timeout
    #    answer = input(prompt)
    #finally:
    #    t.cancel()
    ######################################################################
except Exception as e:
    file = open('error.log', 'a')
    file.write('\n\n')
    traceback.print_exc(file=file, chain=True)
    traceback.print_exc()
    file.close()