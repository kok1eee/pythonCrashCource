users = {
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
        'location':'priceton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }

for username,user_info in users.items():
    print(f"\nユーザー名:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\t氏名:{full_name.title()}")
    print(f"\t場所:{location.title()}")
    