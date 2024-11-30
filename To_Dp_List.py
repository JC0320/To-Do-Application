def display_menu():
    print(' list menu of assigment ')
    print('  1. add task ')
    print('  2. see task ')
    print('  3. delete task ')
    print('  4. quit the aplication ')

def add_task(tasks):
    task=input('enter the wanted task ').strip()
    if task:
        tasks.append(task)
        print(f"added task  {task} ")
    else:
       print("the task can't be empty ") 

def view_tasks(tasks):
    if tasks:
        print("list of tasks ")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
    else:
        print("there is no tasks to show ")

def delete_task(tasks):
    if tasks:
        try:
            view_tasks(tasks)
            index=int(input(" enter the task number that you wish to delete "))
            if 1<=index<=len(tasks):
                remove_tasks=tasks.pop(index-1)
                print(f"task deleted {remove_tasks}")
            else:
                print("number out of range ")
        except ValueError:
            print("need to input a valid number ")
    else:
        print("no tasks to delete ")


def main():
    tasks=[]
    while True:
        display_menu()
        option=int(input("select one option from 1-4: ").strip())
        if option ==1:
            add_task(tasks)
        elif option==2:
            view_tasks(tasks)
        elif option==3:
            delete_task(tasks)
        elif option==4:
            print("quitting the application")
            break
        else:
            print("option not valid, please try again")

if __name__ == "__main__":
    main()