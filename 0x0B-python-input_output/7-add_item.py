#!/usr/bin/python3
"""adds all arguments to a Python list, and
then save them to a file:
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
argv = __import__('sys').argv


def main():
    my_list = []
    try:
        my_list = load_from_json_file("add_item.json")
    except Exception as e:
        my_list = []
    av = argv[1:]
    for arg in av:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")


if __name__ == '__main__':
    main()
