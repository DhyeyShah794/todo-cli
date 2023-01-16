import click


@click.group()
def my_commands():
    pass


@click.command()
@click.option('--name', prompt="Enter a name:" ,default="Dhyey", help="The person to greet.")
def greet(name):
    click.echo(f"Hello, {name}!")


PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial",
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-N", "--name", prompt="Enter the todo name", help="The name of the todo item.")
@click.option("-D", "--desc", prompt="Describe the todo", help="The description of the todo item.")
def add_todo(name, desc, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} - {desc} [Priority: {PRIORITIES[priority]}]\n")


@click.command()
@click.argument("todofile", type=click.Path(exists=True), required=0)
@click.argument("idx", type=int, required=1)
def delete_todo(todofile, idx):
    with open(todofile, "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open(todofile, "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.option("-P", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"{idx} - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"{idx} - {todo}")


my_commands.add_command(greet)
my_commands.add_command(add_todo)
my_commands.add_command(delete_todo)
my_commands.add_command(list_todos)

if __name__=="__main__":
    my_commands()
