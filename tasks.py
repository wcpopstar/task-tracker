
tasks = {}

def add_task(task, title):
    tasks[title] = task

def show_tasks(tasks):
    print(tasks)

while True:
    answer = input("Hello! What do you want? 1(Add task), 2(Show tasks) or 3(Exit): ")
    
    if answer == "1":
        task = input("Task: ")
        title = input("Title: ")
        while True:
            if title in tasks:
                print("This title already taken")
                title = input("Title: ")
            else:
                break
        add_task(task, title)
    elif answer == "2":
        show_tasks(tasks)
    elif answer == "3":
        break
    else:
        print("error")
