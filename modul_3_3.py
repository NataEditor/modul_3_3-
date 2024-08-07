values_list = [6,8,10]
values_list2 = [2,'привет']
values_direct = {'a':123, 'b':456, 'c':678}

def appendet_to_list(item, list_my = None):
    if list_my is None:
        list_my=[]
        list_my.append(item)
    print(list_my)

def print_params(a=1, b='stroka', c=True):
    appendet_to_list(a, b)
    print(a,b,c)
    


print_params()
print_params(7)
print_params(b='None')
print_params(a='7',b=987)
print_params('you', 'next', False)
print_params(c=[1,2,3])
print_params(*values_list)
print_params(*values_list2)
print_params(**values_direct)
#appendet_to_list(values_direct)
print(values_direct)
print(values_list)
print(values_list2)