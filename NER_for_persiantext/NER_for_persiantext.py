from sklearn.datasets import load_files
import polyglot
from polyglot.downloader import downloader
import collections
from polyglot.text import Text

myfile = open("/media/elahe/e/work/data/newdata/myfile.txt")
txt = myfile.read()
print(txt)
text = Text(txt, hint_language_code='fa')
# print("Language Detected: Code={}, Name={}\n".format(text.language.code, text.language.name))

words = text.split()
word_counts = collections.Counter(words)

for entity in text.entities:
    text = " ".join(entity)

    if entity.tag == 'I-PER':
        print ('Names:')
        print (entity[0])


    elif entity.tag == 'I-ORG':
        print ('Organizations:')
        print (entity[0])


    elif entity.tag == 'I-LOC':
        print ('Locations:')
        print (entity[0])
