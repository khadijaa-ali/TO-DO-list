import pandas as pd
import os
fileName="todo_list.csv"
if os.path.exists("todo_list.csv"):
    df=pd.read_csv('todo_list.csv')
else:
    df=pd.DataFrame(columns=["Task" , "Status"])
    print("No Existing File Found ")

while True:
    choice=input("Enter you choice:")
    print("\n-----TODO LIST-------")
    print("1) Add a new task")
    print("2) View All Task")
    print("3) Mark a task as completed")
    print("4) Delete a task")
    print("5) Save & Exit ")
    if choice == "1":
        task=input("Enter Task:")
        status= input("Enter Status:")
        df.loc[len(df)] = [task,status]
        print("Task Added successfully!" )
    elif choice == "2":
        print("\n----Your To-Do List------")
        print(df)
    elif choice == "3" :
        print(df)
        task_input=input("Which task do you want to mark as complete?:")
        if task_input in df["Task"].values:
            row_index = df[df["Task"] == task_input].index[0]
            df.loc[row_index , "Status"]= "Completed"
            print("Task is marked as completed")
        else:
            print("No task found ")
    elif choice == "4":
        task_input=input("Which task do you want to delete:")
        if task_input in df["Task"].values:
            row_index  = df[df["Task"]==task_input].index[0]
            df=df.drop(index=row_index)
            df=df.reset_index(drop=True)
            print("Task deleted successfully!")
            
        else:
            print("No such task found")
    elif choice == "5":
        df.to_csv("todo_list.csv" , index=False)
        print("Data saved successfully.")
        break
    else:
        print("Invalid choice. Please try again.")