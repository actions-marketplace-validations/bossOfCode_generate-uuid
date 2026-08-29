"""import"""
import secrets
import os
import random
import time
import warnings

# i refuse to use uuid.uuid7() lol

if os.environ.get("INPUT_NAMESPACE"):
    warnings.warn("No namespace or name needed for this version",
                  UserWarning)
    print("::warning:: No namespace or name needed for this version")

def insert(og: str,
           ins: str,
           idx: int) -> str:
    """
    Insert a string into a string
    at a certain index.
    """
    return og[:idx] + ins + og[idx:]

print("Version: 7")

UUID = ''
ADD = ''

EPOCH = round(time.time() * 1000)
EPOCHMILLI = format(EPOCH, 'x')

UUID = '0' + EPOCHMILLI + '-'

UUID = insert(UUID, '-', 8) + '7'

ADD = secrets.token_hex(2)[:3]
UUID = UUID + ADD + '-'

UUID = UUID + format(random.randint(8, 11), 'x')

ADD = secrets.token_hex(2)[:3]
UUID = UUID + ADD + '-'

ADD = secrets.token_hex(6)
UUID = UUID + ADD

os.system(f"echo 'uuid={UUID}' >> $GITHUB_OUTPUT")
os.system("echo 'safe=safe' >> $GITHUB_OUTPUT")
