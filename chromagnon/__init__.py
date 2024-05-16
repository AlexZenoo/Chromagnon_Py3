# output = list()
# output_new = list()
# command_list = list()
# iterr = 0
# if output is None:
#    output = list()
print('__init__.py run! __name__ = ', __name__)
if 'output' not in globals():
    output = list()
else:
    print('output not list!')
if 'output_new' not in globals():
    output_new = list()
else:
    print('output_new not list!')
if 'command_list' not in globals():
    command_list = list()
else:
    print('command_list not list!')
if 'iterr' not in globals():
    iterr = 0
else:
    print('iterr not iterr!')
print('__init__.py done run! __name__ = ', __name__)
