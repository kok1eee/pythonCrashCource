favorite_languages = {
    'jan':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

language = favorite_languages['sarah'].title()
print(f"sarahの好きなプログラミング言語は{language}です。")

for name, language in favorite_languages.items():
    print(f"{name.title()}の好きなプログラミング言語は{language}です。")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}、あなたの好きなプログラミング言語は{language}ですね！")
if 'erin' not in favorite_languages.keys():
    print(f"Erin、投票してください！")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}、投票ありがとう。")

print("以下の言語が投票されました。")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
    }

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}の好きな言語")
    for language in languages:
        print(f"\t{language.title()}")
        