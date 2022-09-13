import re

text = """Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, 
        Brandenburg's capital."""

pattern = r"Frankfurt"

result = re.search(pattern, text)
print(result)