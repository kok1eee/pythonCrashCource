filename = 'guest.txt'

def append():
    with open(filename,'a') as file_object:
        name = input("あなたのお名前を教えてください")
        file_object.write(name)

def write():
    with open(filename,'w') as file_object:
        name = input("あなたのお名前を教えてください")
        file_object.write(name)

write()