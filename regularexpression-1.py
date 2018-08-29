#Question 1
import re
a=('the text is venusgoyal98@gmail.com test')
b=list(a.split(' '))
for i in b:
    match=re.finditer('^[\w]*(@)(gmail.com|yahoo.com)',i)
    for i in match:
        print(i.group())


#Question 2
import re
a=('the text is +919465160606,')
b=list(a.split(' '))

for i in b:
    match=re.finditer('^[+91][6-9][0-9]{11}',i)
    for i in match:
        print(i.group())
