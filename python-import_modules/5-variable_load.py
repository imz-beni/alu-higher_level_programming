#!/usr/bin/python3
with open("variable_load_5.py", "r") as file:
    content = file.read()

local_vars = {}
exec(content, {}, local_vars)

a = local_vars['a']
print(a)
