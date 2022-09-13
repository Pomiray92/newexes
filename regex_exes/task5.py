import re
from tracemalloc import start

text = "Berlin is a city of culture 1985."

pattern = r"B\w{5}"

result = re.search(pattern, text)

print(result.span())