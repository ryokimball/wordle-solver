#!/usr/bin/env python3

import re

all_letters="eariotnslcudpmhgbfywkvxzjq"
scored_letters=[]
for i,c in enumerate(all_letters):
    scored_letters.append({'i':i,'c':c})

all_words_file="5letters.txt"
trying="begin"

instructions = ["\nEnter a string of numbers and letters, dividing positives and negatives with a pipe '|'"]
instructions.append("The number following a CAPITAL letter indicates position")
instructions.append("\te.g. 'Z5' has a z in the 5th position")
instructions.append("The digits following a lower-case letter indicate that the letter is used")
instructions.append("but it is not in those positions")
instructions.append("\te.g. 'b234' means there is not a b in the 2nd, 3rd, or 4th position (may be in 1st or 5th)")
instructions.append("All letters following a pipe '|' are rejected letters")
instructions.append("\te.g. 'Z5b234|acd' says there is no a, c, or d in the wordle")
instructions.append("You can enter just a pipe '|' to display ALL ranked matches")
instructions.append("just press enter (with no input) to exit.\n")

print("\n".join(instructions))

while(trying!=""):
    trying=input("Entry:\t")
    if trying=="":
        continue
    positive=trying.split('|')[0]
    negative=""
    if "|" in trying:
        negative=trying.split('|')[1].lower()
    positional=[{'c':c.lower(),'i':int(positive[positive.find(c)+1])-1} for c in re.findall('[A-Z]',positive)]
    nonpositional=[{'c':c[:1],'i':[int(i)-1 for i in c[1:]]} for c in re.findall('[a-z]\d+',positive)]
    print("POSITIONAL:")
    print(positional)
    print("NONPOSITIONAL:")
    print(nonpositional)
    matches=[]
    with open(all_words_file,"r") as words:
        for word in words:
            word=word.strip()
            match=True
            for c in negative:
                if c in word:
                    match=False
            if not match:
                continue
            for c in positional:
                if word[c['i']] != c['c']:
                    match=False
            if not match:
                continue
            for c in nonpositional:
                if c['c'] not in word or word.find(c['c']) in c['i']:
                    match=False
                    break
            if not match:
                continue
            if match:
                scoring=[c for c in scored_letters if c['c'] in word]
                # lower score is better
                points=sum([c['i'] for c in scoring])
                # words with repeated letters go to the end of the line
                for c in word:
                    if word.count(c) > 1:
                        points+=351
                matches.append({"word":word,"points":points})
    matches.sort(key=lambda x: x["points"])
    print([match["word"] for match in matches])
