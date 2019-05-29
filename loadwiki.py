from lxml import etree

# infile = 'copyright.xml'
infile = 'enwiktionary-20190501-pages-meta-current.xml'
out = open('titles.txt', 'w')

namespace = '{%s}' % 'http://www.mediawiki.org/xml/export-0.10/'

context = etree.iterparse(infile, events=('end',), tag=namespace+'page')
# context = etree.iterparse(infile, events=('end',),)

for event, elem in context:
    if elem.text is None:
        continue

#     if elem.getparent() is None:
#         continue

#     parentElement = elem.getparent()
#     idElement = parentElement.find(namespace+'id')
    idElement = elem.find(namespace+'id')
    idValue = idElement.text.encode('utf-8')

    titleElement = elem.find(namespace+'title')
    titleValue = titleElement.text.encode('utf-8')

    # out.write('%s\n' % elem.text.encode('utf-8'))     
    print('tag = %s\n' % elem.tag.encode('utf-8'))
    print('text = %s\n' % elem.text.encode('utf-8'))
    print('id = %s\n' % idValue)
    print('title = %s\n' % titleValue)
 
    # It's safe to call clear() here because no descendants will be accessed
    elem.clear()
 
    # Also eliminate now-empty references from the root node to <Title> 
    while elem.getprevious() is not None:
        del elem.getparent()[0]

