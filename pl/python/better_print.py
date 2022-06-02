# https://rtpg.co/2022/05/30/improve-print-based-debugging.html

import time

words = "This is an example".split()
CSI = "\x1b["
CLEAR = CSI + "2J"
TOP_LEFT = CSI + ";H"
for word in words:
    print(CLEAR + TOP_LEFT)
    print(f"processing {word}...")
    time.sleep(1)
