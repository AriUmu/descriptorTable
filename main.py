# coding=utf-8
# get 3 params  in hex
# print table with base, limit and type

def input_param(attr_name, default_value):
   print('Введите {} в hex'.format(attr_name))
   input_value = str(input())
   as_binary = 0
   try:
       as_binary = bin(int(input_value, 16))
   except:
       print('Введи нормально, написано же в hex')
       as_binary = bin(int(default_value, 16))
   return as_binary

def print_descriptor_table(base, limit, type):
    print(
        '-------------------------------------------------------------------|\n'
        '31       24|23|22|21|20| 19     16 |15|14 - 13|12| 11 - 8 |7      0|\n'
        '-------------------------------------------------------------------|\n'
        '  {} | 0| 0| 0| 0|           | 0|  00   | 0| {} |{}|  4\n'
        '-------------------------------------------------------------------|\n'
        '        {}           |       {}              |  0\n'
        '-------------------------------------------------------------------|\n'.format(base[2:10], type, base[10:18],base[18:36],limit)
    )

if __name__ == '__main__':
    base = input_param('base', 0xFFFFFFFF)
    limit = input_param('limit', 0xFF)
    type = input_param('type of segment (read/write/execute)', 0xF)
    print_descriptor_table(base,limit,type)

