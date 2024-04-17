def get_formatted_name(city, country, population=''):
    """都市名と国名を組み合わせて返す"""
    if population:
        formatted_name = f"{city},{country} - 人口 {population}"
    else:
        formatted_name = f"{city},{country}"

    return formatted_name.title()