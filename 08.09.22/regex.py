import re

text_to_be_searched = """some text mail@web.de some text
The application in this file will read the command line options using argparse.
This application should support positional arguments and be called like this: `./app3.py [FIRST_NAME] [LAST_NAME] [AGE]`
If age is not specified, it should be assumed that it Is 100. If the last name is not specified, it 
should be assumed that it is "Hanson". If the first name
is not specified, should be assumed that it is "Larry"."""

pattern = r"([A-Z][a-z].)"

suchen = re.findall(pattern, text_to_be_searched)

print(suchen)    # 
