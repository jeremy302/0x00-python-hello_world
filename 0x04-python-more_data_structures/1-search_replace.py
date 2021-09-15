#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [v if v != search else replace for v in my_list]
