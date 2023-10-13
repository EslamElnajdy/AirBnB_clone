#!/usr/bin/python3
"""The console module"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    """simple command interpreter"""
    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program Ctrl+D"""
        print()
        return True

    def emptyline(self) -> bool:
        """
        empty line
        """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            c = storage.classes()[line]()
            c.save()
            print(c.id)

    def do_show(self, line):
        """prints the string representation of an instance based on
            the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        destory method
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        all method
        """
        if line == "" or line is None:
            obj = [str(o) for k, o in storage.all().items()]
            print(obj)
        else:
            line = line.split(' ')
            if line[0] not in storage.classes():
                print("** class doesn't exist **", line)
            else:
                obj = [str(o) for k, o in storage.all().items()
                       if type(o).__name__ == line[0]]
                print(obj)

    def do_count(self, line):
        """
        count method
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line = line.split(' ')
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj = [str(o) for k, o in storage.all().items()
                       if type(o).__name__ == line[0]]
                print(len(obj))

    def do_update(self, line):
        """
        update method
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    value = args[3]
                    if args[3].isdigit():
                        if '.' in args[3]:
                            value = float(args[3])
                        else:
                            value = int(args[3])
                    else:
                        value = args[3].lstrip('"').rstrip('"')
                    setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
                    storage.all()[key].save()

    def default(self, line):
        """handels commands in form ClassName.method()
        default is a method that gets called when the user enters a command 
        that doesn't match any of the existing do_ methods.
        """

        parts = line.split('.')
        if len(parts) == 2:
            class_name = parts[0]
            method = parts[1]
            if class_name in storage.classes():
                if method == "all()":
                    # equivalent to typing in the cmd all ClassName
                    self.do_all(class_name)
                elif method == "count()":
                    self.do_count(class_name)
                elif method.startswith("show("):
                    id = method[5:-1]  # extracts id
                    self.do_show(class_name + " " + id)
                elif method.startswith("destroy("):
                    id = method[8:-1]
                    self.do_destroy(class_name + " " + id)
                else:
                    print("** Unknown syntax:", line)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
