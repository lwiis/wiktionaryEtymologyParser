import wiktextract
# import json    # or `import simplejson as json` if on Python < 2.6
from neo4jcontroller import DbController

filePath = 'enwiktionary-20190501-pages-meta-current.xml'

db = DbController('bolt://localhost:7687', 'neo4j', 'h6u4%kr')

def processWord(data):
    print(data)
    if not "lang" in data.keys():
        return
    # obj = json.loads(data)
    db.createWordNode(data)

ctx = wiktextract.parse_wiktionary(
    path = filePath, word_cb=processWord,
    capture_cb=None,
    languages=["English", "Translingual"],
    translations=False,
    pronunciations=False,
    redirects=True)