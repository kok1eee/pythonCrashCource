style = ['lager','ale','ipa','stout','porter','white ale','weizen']

print(style[0])

print(style[0].title())

print(style[-1])

message = f"私の好きなスタイルは{style[2]}です。"
print(message)

style[0] = 'pilsner'
print(style)

style.append('lager')
print(style)

style = []

style.append('lager')
style.append('ale')
style.append('ipa')

print(style)

style.insert(1,'pilsner')
print(style)

del style[2]
print(style)

popped_style = style.pop()
print(style)
print(popped_style)

style = ['lager','ale','ipa','stout','porter','white ale','weizen']

last_drunk = style.pop(2)
print(f"私が最近飲んだスタイルは{last_drunk}のビールです。")

dislike_style = 'porter'
style.remove(dislike_style)
print(style)
print(f"\n{dislike_style}は黒ビールだし、度数も低いので好きじゃない")

style.sort()
print(style)

style.reverse()
print(style)

print(sorted(style))

print(len(style))