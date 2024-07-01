from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string=task_field.get()
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))    
        list_update()    
        task_field.delete(0, 'end')  
    
def list_update():    
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  