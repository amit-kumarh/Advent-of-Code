with open('input', 'r') as f: print(__import__('collections').Counter(__import__('re').findall(r'[a-z]+', f.read().strip())).most_common()[-1][0])

