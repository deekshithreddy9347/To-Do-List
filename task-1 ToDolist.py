import tkinter
import tkinter.messagebox
import pickle
root1=tkinter.Tk()

'''Giving a title for To-Do list application done by me'''
root1.title("To-Do List Application done by:Deekshith")

def adding_task1():
    task1=entry_task1.get()
    if task1!="":
        allListbox_tasks.insert(tkinter.END,task1)
        entry_task1.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="SYSTEM WARNING!!!",message="you must enter a task not a null value")

def deleting_task1():
    try:
        task1_index=allListbox_tasks.curselection() [0]
        allListbox_tasks.delete(task1_index)
    except:
        tkinter.messagebox.showwarning(title="SYSTEM WARNING!!!",message="you must have to select a task")  
    
    
def updating_task1():
    try:
        update_task1=entry_task1.get()
        task2_index=allListbox_tasks.curselection() [0]
        task2_index=update_task1
        allListbox_tasks.update(task2_index)
        
    except:
        tkinter.messagebox.showwarning(title="SYSTEM WARNING!!!",message="you must have to select a task")


def saving_tasks1():
    tasks=allListbox_tasks.get(0,allListbox_tasks.size())
    pickle.dump(tasks,open("tasks.dat","wb"))
    



#Scroll bar
scrollbar_tasks1=tkinter.Scrollbar(root1)
scrollbar_tasks1.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#creating GUI based application
#application bar
allListbox_tasks=tkinter.Listbox(root1,height=13,width=60,bg="light blue")
allListbox_tasks.pack()

#Entry task bar
entry_task1=tkinter.Entry(root1,width=60)
entry_task1.pack()



#adding buttons like adding,deleting,updating,saving etc.. in To-do list application tasks
#adding button 
add_task_button=tkinter.Button(root1,text="ADD-TASK",width=30,bg="green",command=adding_task1)
add_task_button.pack()
#deleting button
delete_task_button=tkinter.Button(root1,text="DELETE-TASK",width=30,bg="green",command=deleting_task1)
delete_task_button.pack()
#updating button
update_task_button=tkinter.Button(root1,text="UPDATE-TASK",width=30,bg="green",command=updating_task1)
update_task_button.pack()
#Saving button
save_task_button=tkinter.Button(root1,text="SAVE-TASK",width=30,bg="green",command=saving_tasks1)
save_task_button.pack()
root1.mainloop()
























