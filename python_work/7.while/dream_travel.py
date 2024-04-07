responses = {}

polling_active = True

while polling_active:
    name = input('あなたのお名前は？')
    response = input('世界中どこでも好きなところに行けるとしたらどこに行きたいですか？')

    responses[name] = response

    repeat = input('他に誰か回答してくれますか？yes/no')

    if repeat == 'no':
        polling_active = False
    
    print('投票結果')
    for name,response in responses.items():
        print(f"{name}が行きたい国は{response}です")


