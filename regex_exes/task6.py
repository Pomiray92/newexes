import re

text = "The rain in Spain."

pattern = r"ai"

result = re.findall(pattern, text)

print(len(result))