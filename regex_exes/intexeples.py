import re

target_string = "Emma is a basketball player who was born on June 17, 1993"
# match method with pattern and target string using match()
result = re.findall(r"\w{3}", target_string)
# printing  match
print("Match: ", result)