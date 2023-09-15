import tkinter as do

tasks = []

def add_task():
    global tasks
    task=text_box.get("1.0", do.END)
    tasks.append(task)
    result_box.delete("1.0", do.END)
    result_box.insert("1.0", "Task added successfully")

def remove_task():
    global tasks
    delete = text_box.get("1.0", do.END)
    if delete in tasks:
        tasks.remove(delete)
        result_box.delete(1.0,do.END)
        result_box.insert("1.0", "Task removed successfully")
    else:
        result_box.delete(1.0,do.END)
        result_box.insert("1.0", "Task not found")
        

def display_tasks():
    global tasks
    text_box.delete(1.0,do.END)
    result_box.delete(1.0,do.END)
    text_box.insert("1.0", "tasks:\n")
    if len(tasks) == 0:
        result_box.insert("1.0", "No tasks found")
    else:
        for task in tasks:
            text_box.insert(do.END, task)

def clear_field():
    global tasks
    text_box.delete(1.0,"end")
    
    
root=do.Tk()
root.title("To-Do List")


text_box=do.Text(root,height=2,width=16,font=("ariel",24))
text_box.pack()

btn_1=do.Button(root,text="Add Task",command=add_task,width=10,font=("Arial",14),bg="blue",fg="white")
btn_1.pack()

btn_2=do.Button(root,text="Remove Task",command=remove_task,width=10,font=("Arial",14),bg="red",fg="white")
btn_2.pack()

btn_3=do.Button(root,text="Display Task",command=display_tasks,width=10,font=("Arial",14),bg="green",fg="white")
btn_3.pack()

clear=do.Button(root,text="clear screen",command=clear_field,width=10,font=("Arial",14),bg="black",fg="white")
clear.pack()

result_box=do.Text(root,height=1,width=22,font=("ariel",20))
result_box.pack()
root.mainloop()