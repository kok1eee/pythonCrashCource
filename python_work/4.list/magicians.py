magicians = ['alice','david','carolina']
for magician in magicians:
  print(f"{magician.title()}は素晴らしい手品を演じた！")
  print(f"私は{magician.title()}の次の手品が待ちきれない。\n")

print("みなさんありがとう。素晴らしい手品ショーでした。")

# スライスの練習
print("リストの最初の2つの要素です。")

for magician in magicians[:2]:
  print(magician.title())