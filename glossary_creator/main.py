import os
import re

# pattern = r"\\trans\{(?P<fa>.*)\}\{(?P<eng>.*)\}" 
pattern = r"\\trans\{(?P<fa>[،-ﯾ  \-»«]*)(?: \\.*)?\}\{(?P<eng>[A-Za-z0-9 \-()`'\"]*?(?: \\.*)?)(?:\;.*)*\}"

l = []
for f in os.listdir("../report"):
    if not f.endswith(".tex"):
        continue
    with open(f"../report/{f}") as content:
        res = re.findall(pattern, '\n'.join(content.readlines()))
        l = [*l, *res]

l=sorted(l, key=lambda x: x[-1])

bold = "\\textbf{"
lr = "\\lr{"
folan = "}"
rl = "\\rl{"
hfill = "\\hfill"
last_char = " "
last_word = " "


print("\\chapter*{واژه‌نامه}\n\\addcontentsline{toc}{section}{واژه‌نامه}")
print("\\begin{LTR}")
print("\\LTRmulticolcolumns\n\\raggedleft")
print("\\begin{multicols}{2}[]")
print("\\textbf{\\rl{کلمه} \\dotfill \\rl{معادل فارسی}}\\\\[1.2em]")
for item in l:
    if last_char < item[1][0]:
        last_char = item[1][0]
        print(f"\\raggedright {bold}{lr}{last_char}{folan}{folan} \\hrulefill \\\\ \\raggedleft")
    if last_word == item[1]:
        continue
    else:
        if item[1] in [last_word + "s", last_word[:-1]]:
            continue
        last_word = item[1]
    if item[0].endswith("‌های"):
        item = (item[0][:-1], item[1])
    if item[0].endswith("‌ای"):
        item = (item[0][:-2], item[1])
    if item[1] in ["Dynamic Games", "Non Perfect-information Games", "Incomplete-information Games", "Non-cooperative Games", "Stochastic Games"] and not item[0].startswith('بازی‌های'):
        item = ("بازی‌های "+item[0], item[1])
    print(f"{lr}{item[1]}{folan} \dotfill {rl}{item[0]}{folan}\\\\")
print("\\end{multicols}")
print("\\end{LTR}")
