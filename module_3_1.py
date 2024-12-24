calls = 0
def count_calls():
    global calls
    calls += 1
string = input('введите строку: ')
def string_info():
    a = len(string)
    b = string.upper()
    c = string.lower()
    count_calls()
    print(a, b, c)
stroka = input("введите строку: ")
spisok = input('введите список: ')
def is_contains():
    if stroka in spisok:
        print('true')
    else:
        print('false')
    count_calls()
string_info()
is_contains()
print(calls)


