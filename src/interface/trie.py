#Python Trie Implementation
#Coded by Robert Heumueller

__author__  = "Robert Heumueller <robert@heum.de>"
__date__    = "$10.06.2011 23:54:00$"

import logging
import sys
import string



class Trie(object):
	count = 0
	min_length = 5
	delete_table  = string.maketrans(
		string.ascii_lowercase, ' ' * len(string.ascii_lowercase)
	)
	def __init__(self, word = ""):
		self.character = ''
		self.children = []
		self.id = Trie.count
		Trie.count += 1
		if not word == "":
			self.character = word[0]
			self.add(word[1:])
			
	def __repr__(self):
		return "Trie Node "+ str(self.id)+" "+ self.character

			
	def matching(self, prefix, cur = "", words = []):
		if cur == "":
			prefix = prefix.lower()
		cur += self.character
		if len(self.children) > 0:
			for temp in self.children:
				temp.matching(prefix, cur)
		else:
			words.append(cur)
		if self.character == '':
			return [w for w in words if w.startswith(prefix)]
		
	def add(self, word):
		word = word.lower()
		word = word.encode("ascii", "ignore")
		word = word.translate(None, Trie.delete_table)
		if word == '':
			return
		for temp in self.children:
			if word.startswith(temp.character):
				temp.add(word[1:])
				return
		self.children.append(Trie(word))
		
	def addSentence(self, sentence):
		words = sentence.split()
		for word in words:
			if len(word) < Trie.min_length:
				continue
			self.add(word)
					
if __name__ == "__main__":
	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(message)s')
	test = Trie()
	test.addSentence("Hallo Welt! Wie geht es dir?") 
	print test.matching("w")

					
	
