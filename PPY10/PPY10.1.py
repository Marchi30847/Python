r"""

import re

pattern=re.compile(r'\d+')

txt="123523533"

#first occurance in my string of pattern
match=re.search(pattern,txt)
print(match.group())

#checks if string begins with pattern
match=re.match(pattern,txt)
print(match.group())

#checks if whole string is a pattern
match=re.fullmatch(pattern,txt)
print(match.group())

txt2="12312asdsdasd3523523dfsfsdf234234sdfsdf34234"
match=re.split(pattern,txt2)
print(match)

match=re.findall(pattern,txt2)
print(match)


match=re.finditer(pattern,txt2)
for i in match:
    print(i.group())

text="abc123abc123"
match=re.sub(pattern,r'-',text)
print(match)

match=re.subn(pattern,r'-',text)
print(match)

match=re.escape("Today is 14.05.2025")
print(match)

text="My email is dabuldab@pjwstk.edu.pl and i like it."
pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
print(re.search(pattern,text).group())

"""


#Task1
import re

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*()]', password):
        return False

    return True

print(is_valid_password("Gooooooooooooool123#"))
print(is_valid_password("Password123!"))
print(is_valid_password("pass123!"))
print(is_valid_password("PASSWORD123"))
print(is_valid_password("Pa$$word"))
print(is_valid_password("GoodPass1#"))

#Task2
def parse_logs(log_text: str):
    logs = []

    pattern = re.compile(
        r'\[(.*?)]\s+(INFO|ERROR):.*?(?:User|user)\s+(\w+)', re.IGNORECASE
    )

    for match in re.finditer(pattern, log_text):
        date, log_type, user = match.groups()
        logs.append({
            'date': date,
            'log_type': log_type,
            'user': user
        })

    return logs

log_data = """
[2025-05-13 14:33:10] INFO: User Jan logged in
[2025-05-13 14:33:55] ERROR: Login error for user Anna
[2025-05-13 14:34:10] INFO: User Piotr logged out
"""

result = parse_logs(log_data)
for entry in result:
    print(entry)