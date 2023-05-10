# Производственная практика Косаринов Александр Пдо 31
'''
# 1
for i in range(1,101):
    s = ''
    if (i % 3 == 0):
        s += 'Fizz'
    if (i % 5 == 0):
        s += 'Buzz'
    if not s:
        s += str(i)
    print(s)
'''

'''
# 2
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z

a = [1, 4, 6]
b = [11, 33, 22]
print(sort_list(a, b))
'''

'''
# 3
result_list1 = []
result_list2 = []
result_list3 = []
df = []
fd = []
gf = []
sfg_list = ["bella","label","roller"] #["cool","lock","cook"]
print('список строк:',sfg_list)
df.append(sfg_list[0])
fd.append(sfg_list[1])
gf.append(sfg_list[2])

for x in df:
     for y in list(x):
       result_list1.append(y)

for x in fd:
     for y in list(x):
       result_list2.append(y)

for x in gf:
     for y in list(x):
       result_list3.append(y)

t = []

for item in result_list1:
    if item not in t:
        a_item = result_list1.count(item)
        b_item = result_list2.count(item)
        c_item = result_list3.count(item)
        min_count = min(a_item, b_item, c_item)
        for i in range(min_count):
            t.append(item)

print('буквы, которые встречаются в каждой из строк списка:', t)
'''

'''
# 4
def roman(num):
    roman_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,n in enumerate(num):
        if (i+1) == len(num) or roman_num[n] >= roman_num[num[i+1]]:
            result += roman_num[n]
        else:
            result -= roman_num[n]
    return result

a = list(input('Введите римские цифры:'))
b = (roman(a))
print(b)
'''