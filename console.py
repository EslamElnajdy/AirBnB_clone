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
        return super().emptyline()

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

    def do_destory(self, line):
        """
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

    def do_update(self, line):
        """
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
                    setattr(storage.all()[key], args[2], args[3].lstrip('"').rstrip('"'))
                    storage.all()[key].save()
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
