tokyo = {
    'name':'tokyo',
    'country':'japan',
    'population':'13000000',
    'fact':'serious'
    }

california = {
    'name':'california',
    'country':'usa',
    'population':'39000000',
    'fact':'friendly',
    }

beijing = {
    'name':'beijing',
    'country':'china',
    'population':'21000000',
    'fact':'egoistic'
    }

cities = [tokyo,california,beijing]

for city in cities:
    print(f"{city['name']}は{city['country'].title()}の街で人口は{city['population']}人います。人々の性格は{city['fact']}な人が多いです。")