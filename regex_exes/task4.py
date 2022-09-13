import re

text = "Berlin is a city of culture."

pattern = r"in"

result = re.search(pattern, text)

print(result)