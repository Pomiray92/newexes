from dataclasses import replace
import re

text = """Berlin is surrounded by the"""
               
pattern = r" "

result = re.sub(pattern, "-", text)

print(result)