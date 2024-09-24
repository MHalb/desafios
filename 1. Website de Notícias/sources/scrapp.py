from bs4 import BeautifulSoup
import re, json

# o que melhorar?
## aprender a usar regex(extremamente útil pra raspar java-script)



with open("g1_html.html", "r", encoding='utf-8') as r:
	html = r.read()

pattern = r'{\s*"playlist": {(.*?)}\s*}\s*'
js_py_dict = json.loads(re.search(pattern, html, re.DOTALL)[0])

print(js_py_dict)
