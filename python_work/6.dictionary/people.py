user_01 = {
    'first_name':'sato','last_name':'kazunari','age':24,'city':'omiya'
    }

user_02 = {
    'first_name':'masayoshi','last_name':'tazawa','age':31,'city':'adachi'
    }

user_03 = {
    'first_name':'hiroki','last_name':'kitazawa','age':29,'city':'shinagawa'
    }

people = [user_01,user_02,user_03]

for person in people:
    print(f"{person['first_name'].title()}{person['last_name'].title()}は{person['age']}歳で{person['city']}に住んでいる")
