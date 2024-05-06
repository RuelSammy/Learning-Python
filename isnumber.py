import re

phoneNumRegex = re.compiler(r'(\d\d\d)-(\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')