def get_formatted_name(first_name,last_name):
    """フォーマットされたフルネームを返す"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)