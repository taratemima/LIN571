#Tara Edwards
#Sanghoun revised this file.


import nltk
from nltk import Nonterminal, nonterminals, Production, parse_cfg, ContextFreeGrammar
from nltk.parse import EarleyChartParser 

g = nltk.data.load("file:./grammar.cfg", format='cfg')    
f = nltk.data.load("file:./sentences.txt", format='raw')

numberofparses = 0
eparser = nltk.parse.EarleyChartParser(g)
lines = nltk.sent_tokenize(f)
	for line in lines:
	p = nltk.word_tokenize(line)
	print p
	trees = eparser.nbest_parse(p)
	for tree in trees:
		print tree
	numberofparses += len(trees)
	sentences_total = len(lines)
	print float(numberofparses)/float(sentences_total)



