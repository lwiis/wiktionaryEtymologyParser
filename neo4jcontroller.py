from neo4j import GraphDatabase

class DbController(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def createWordNode(self, inputWord):
        with self._driver.session() as session:
            wordString = self._wordToString(inputWord)
            greeting = session.write_transaction(self._createWordNode, wordString)
            print(greeting)

    def _wordToString(self, inputWord):

        keys = list(inputWord.keys())
        key = keys.pop(0)
        txt = '{' + key + ': "' + str(inputWord[key]).replace("'","\\'").replace('"','\\"') + '"'

        for key in keys:
            # print(key)
            # print(inputWord[key])
            if key=='heads':
                continue 
            if key=='senses':
                continue
            if key=='categories':
                continue
                
            txt = txt + "," + key + ': "' + str(inputWord[key]).replace("'","\\'").replace('"','\\"') + '"'

        txt = txt + "}"

        return txt

    @staticmethod
    def _createWordNode(tx, inputWordString):
        # print(inputWord)
        # txt = "CREATE (n:word {word:'%s'}) RETURN n.word + ', node ' + id(n)" % (inputWord["word"])
        print(inputWordString)
        txt = "CREATE (n:word " + inputWordString + ") RETURN n.word + ', node ' + id(n)"
        print(txt)
        result = tx.run(txt)
        return result.single()[0]

