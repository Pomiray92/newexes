import re

text = "Berlin is a world city of culture, politics, media and science."

pattern = r" "

result = re.search(pattern, text)
print("The first white-space character is located at position:", result)