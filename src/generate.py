"""Import Operating System and UUID"""
import os
import uuid

VERSION = os.environ.get("INPUT_VERSION")
namespace = os.environ.get("INPUT_NAMESPACE")
name = os.environ.get("INPUT_NAME")

UUIDTYP = getattr(uuid, f"uuid{VERSION}")
OUTPUT = ""

versions = ["1", "3", "4", "5"]
namespaces = ["DNS", "URL", "OID", "X500"]

def print_in_os(argument):
    "print in both terminal and action logs"
    print(f"{argument}")
    os.system(f"echo {argument}")

print_in_os(f"Version: {VERSION}")

if VERSION in versions or namespace in namespaces:
    OUTPUT = UUIDTYP()
else:
    if not namespace in namespaces and namespace > "":
        raise ValueError(f"ERROR: namespace cannot be '{namespace}'; must be either DNS, URL, OID, "
                          + "or X500.")
    else:
        if not VERSION in versions and VERSION > "":
            raise ValueError(f"ERROR: VERSION {VERSION} does not exist")

OUTPUTSTR = str(OUTPUT)
FINAL = uuid.UUID(OUTPUTSTR)
SAFE = uuid.SafeUUID

os.system(f"echo 'uuid={FINAL}' >> $GITHUB_OUTPUT")
os.system(f"echo 'safe={SAFE}' >> $GITHUB_OUTPUT")

if SAFE == "unsafe":
    print_in_os("::warning title=UNSAFE::Your UUID may be unsafe for public use because" +
                " it may contain some of your device's personal info.")
