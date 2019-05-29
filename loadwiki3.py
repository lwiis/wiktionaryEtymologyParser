import sys
import json
import os
import WiktionaryParser

# infile = 'copyright.xml'
infile = 'enwiktionary-20190501-pages-meta-current.xml'
# infile = 'amigo.xml'

# Open output file.
out_path = "words.json"
if out_path and out_path != "-":
    if out_path.startswith("/dev/"):
        out_tmp_path = out_path
    else:
        out_tmp_path = out_path + ".tmp"
    out_f = open(out_tmp_path, "w", buffering=1024*1024)
else:
    out_tmp_path = out_path
    out_f = sys.stdout

word_count = 0

def word_cb(data):
    global word_count
    word_count += 1
    out_f.write(json.dumps(data))
    out_f.write("\n")
    if not out_path or out_path == "-":
        out_f.flush()

def capture_cb(title, text):
    # return capture_page(title, text, args.pages_dir)
    return True

try:
    ctx = WiktionaryParser.parseWiktionary(
        # args.path,
        infile,
        word_cb,
        capture_cb,
        languages=["Portuguese", "Translingual"], #args.language,
        pronunciations=False, #args.pronunciations,
        translations=False, #args.translations,
        linkages=False, #args.linkages,
        compounds=False, #args.compounds,
        redirects=False #args.redirects
    )
finally:
    if out_path and out_path != "-":
        out_f.close()

if out_path != out_tmp_path:
    try:
        os.remove(out_path)
    except FileNotFoundError:
        pass
    os.rename(out_tmp_path, out_path)
