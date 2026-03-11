from conduit.memory.short_term import MEMORY_FILE
import json

def run(args):
    ch = input("Confirm? (Y|n):")
    if ch == "Y":
        json.dump([], open(MEMORY_FILE,"w"))
    else:
        print("Cancelled!")

