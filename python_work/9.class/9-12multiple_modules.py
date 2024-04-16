from admin import Admin

person = Admin('masayoshi', 'tazawa', 'man', 31)

list = person.privileges.show_privileges()

print(f"{person.first_name} {person.last_name}がもっている権限は{list}")