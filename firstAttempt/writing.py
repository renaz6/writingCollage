#! /usr/bin/env python

import random
import textwrap

def main():
    middlesexText = open("blackstar").read().split()
    shakespeareText = open("uncleArthur").read().split()
    combinedText = middlesexText + shakespeareText
    finalText = random.sample(combinedText, 40)
    
    print(textwrap.fill(" ".join(str(x) for x in finalText), width = 50))

if __name__ == "__main__":
    main()