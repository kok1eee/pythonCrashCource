cat = {'name':'mimi','owner':'masayoshi','breed':'scottish_fold'}

dog = {'name':'omochi','owner':'kousuke','breed':'pug'}

hamster = {'name':'hamtaro','owner':'ryo','breed':'Jungarian'}

pets = [cat,dog,hamster]

for pet in pets:
    print(f"{pet['name']}は{pet['owner']}が飼っていて{pet['breed']}という品種だ")