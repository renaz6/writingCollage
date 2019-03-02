#! /usr/bin/env python

import random
import textwrap

def main():
    middlesexText = open("middlesexText").read().split()
    shakespeareText = open("shakespeareText").read().split()
    combinedText = middlesexText + shakespeareText
    finalText = random.sample(combinedText, 40)
    
    print(textwrap.fill(" ".join(str(x) for x in finalText), width = 50))

if __name__ == "__main__":
    main()