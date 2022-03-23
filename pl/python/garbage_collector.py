import sys

x = "test"
rc = sys.getrefcount(x)
print(rc)

import gc

print(gc.get_threshold())
