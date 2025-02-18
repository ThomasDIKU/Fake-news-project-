# Import regular expression module
import re
from termcolor import colored
data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr''' 

# Create regular expression
pattern = re.compile("(^[A-Za-z]+) ?([1-9]+)[,]* ([, ]*[^,]+), ?T=([-0-9]+)degr?")

match = []
for data_line in data.split('\n'):
    
    print(data_line)
    match = pattern.match(data_line)
    
    if match:
        print(colored(match.group(4), 'red'))
    search = pattern.search(data_line)
    
    if search:
        print(colored(search.group(4), 'yellow'))
    findAll = pattern.findall(data_line)
    
    if findAll:
        print(colored(findAll, 'green'))

