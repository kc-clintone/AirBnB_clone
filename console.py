#!/usr/bin/python3
"""
The console
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.city import City
import re
import ast
import cmd
import shlex


def split_braces(e_arg):
    """
    Splits curly braces
    """
    braces = re.search(r"\{(.*?)\}", e_arg)

    if braces:
        x = shlex.split(e_arg[:braces.span()[0]])
        id = [i.strip(",") for i in x][0]
        res = braces.group(1)
        try:
            arguments = ast.literal_eval("{" + res + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arguments
    else:
        cmds = e_arg.split(",")
        if cmds:
            try:
                id = cmds[0]
            except Exception:
                return "", ""
            try:
                attr = cmds[1]
            except Exception:
                return id, ""
            try:
                attrv = cmds[2]
            except Exception:
                return id, attr
            return f"{id}", f"{attr} {attrv}"


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "
    acceptable_classes = ["BaseModel", "User", "Amenity", "Place", "Review",
                          "State", "City"]

    def blank_line(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_EOF(self, arg):
        """
        EOF or CTRL+D: exits the program
        """
        return True

    def do_quit(self, arg):
        """
        quit: exits the program
        """
        return True

    def do_create(self, arg):
        """
        create: make a new instance from BaseModel and save it to a JSON file
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
        else:
            my_instance = eval(f"{cmds[0]}()")
            storage.save()
            print(my_instance.id)

    def do_show(self, arg):
        """
        show: displays a string representation of an instance
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            k = "{}.{}".format(cmds[0], cmds[1])
            if k in objs:
                print(objs[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        destroy: removes an instance based on the class name and id provided
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            k = "{}.{}".format(cmds[0], cmds[1])
            if k in objs:
                del objs[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        all: displays the string representation of all instances/classes
        """
        objs = storage.all()
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            for k, v in objs.items():
                print(str(v))
        elif cmds[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if k.split('.')[0] == cmds[0]:
                    print(str(v))

    def do_count(self, arg):
        """
        count: counts the number of instances of a class
        """
        objs = storage.all()
        cmds = shlex.split(arg)
        if arg:
            this_class = cmds[0]
        x = 0
        if cmds:
            if this_class in self.acceptable_classes:
                for i in objs.values():
                    if i.__class__.__name__ == this_class:
                        x += 1
                print(x)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        update: updates an instance
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            obs = storage.all()
            k = "{}.{}".format(cmds[0], cmds[1])
            if key not in obs:
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                obj = obs[k]
                braces = re.search(r"\{(.*?)\}", arg)
                if braces:
                    try:
                        res = braces.group(1)
                        arguments = ast.literal_eval("{" + res + "}")
                        attrs = list(arguments.keys())
                        attrv = list(arguments.values())
                        try:
                            first_attr = attrs[0]
                            first_attr_value = attrv[0]
                            setattr(obj, first_attr, first_attr_value)
                        except Exception:
                            pass
                        try:
                            second_attr = attrs[1]
                            second_attr_value = attrv[1]
                            setattr(obj, second_attr, second_attr_value)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    attribute_name = cmds[2]
                    attribute_value = cmds[3]
                    try:
                        attribute_value = eval(attribute_value)
                    except Exception:
                        pass
                    setattr(obj, attribute_name, attribute_value)
                obj.save()

    def default(self, arg):
        """
        default: the default behaviour for the hbnb cmd
        """
        arguments_list = arg.split('.')
        this_class = arguments_list[0]
        cmds = arguments_list[1].split('(')
        new_method = cmds[0]
        other_args = cmds[1].split(')')[0]
        fn_dict = {
                'all': self.do_all,
                'update': self.do_update,
                'count': self.do_count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                }

        if new_method in fn_dict.keys():
            if new_method != "update":
                return fn_dict[new_method]("{} {}".format(this_class, other_args))
            else:
                if not this_class:
                    print("** class name missing **")
                    return
                try:
                    x, y = split_braces(other_args)
                except Exception:
                    pass
                try:
                    run = fn_dict[new_method]
                    return run("{} {} {}".format(this_class, x, y))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
