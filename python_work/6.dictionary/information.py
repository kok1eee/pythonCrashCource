person_information = {
    'first_name':'sato','last_name':'kazunari','age':24,'city':'omiya'
    }

print(person_information['first_name'])
print(person_information['last_name'])
print(person_information['age'])
print(person_information['city'])


favorite_numbers = {
    'itadori':1,
    'megumi':22,
    'nobara':4,
    'toge':9,
    'maki':6,
    'satoru':22
    }

for favorite_number in favorite_numbers:
    number = favorite_numbers[favorite_number]

    print(f"{favorite_number}の好きな番号は{number}です。")

error_glossary = {
    'SyntaxError':'プログラムが文法的に正しくないと判断された場合に発生します。',
    'IndentationError':'インデントが正しくない場合に発生するエラーです。',
    'NameError':'変数名の間違いやつづり間違いなど、名前が見つからなかった場合のエラーです。',
    'TypeError':'異なるデータ型同氏の演算や関数にて処理が行われた場合に発生するエラーです。',
    'ValueError':'型は正しくても、値が適切でない場合に発生するエラーです。',
    'AttributeError':'属性(Attribute)を呼び出す際に発生するエラーです。',
    'IndexError':'リスト型やタプル型に対して、要素数を超えたインデックス値を指定した場合に発生するエラーです。',
    'KeyError':'辞書型に対してキーを指定して取得する際に、存在しないキーを指定した際に発生するエラーです。',
    'ModuleNotFoundError':'読み込んだモジュールが見つからない場合に発生するエラーです。',
    'ZeroDivisionError':'数値に対する演算の際に、0で割り算等が行われた場合に発生するエラーです。'
    }

for error in error_glossary:
    content = error_glossary[error]
    print(f"{error}:{content}\n")

for name, value in error_glossary.items():
    print(f"{name}:{value}\n")

for name in error_glossary.keys():
    print(name)

for value in error_glossary.values():
    print(value)