#! /usr/bin/env python

import random
import textwrap

def main():

    arthur = ''
    blackstar = ''

    with open("uncleArthur", "r") as m:
        arthur = []
        for line in m:
            arthur.append(line)

    with open("blackstar", "r") as r:
        blackstar = []
        for line in r:
            blackstar.append(line)

    combinedText = arthur + blackstar
    finalText = random.sample(combinedText, 20)
    
    print(textwrap.fill(" ".join(str(x) for x in finalText), width = 50))

if __name__ == "__main__":
    main()