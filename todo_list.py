
def show_todo_list(todo_list):
    print("\nYour To-Do List:")
    for item in todo_list:
        print(f"- {item}")

todo_list = []
while True:
    action = input("Add a task (or type 'exit' to stop): ")
    if action.lower() == "exit":
        break
    todo_list.append(action)

show_todo_list(todo_list)
    