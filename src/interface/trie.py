#Python Trie Implementation
#Coded by Robert Heumueller

__author__  = "Robert Heumueller <robert@heum.de>"
__date__    = "$10.06.2011 23:54:00$"

import logging
import sys
import string

class DictTrie(object):
	leaves = []
	min_length = 5
	def __init__(self):
		self.root = TrieNode(root = True)
	
	def addWord(self, word):
		self.root.addWord(word)
		
	def extend(self, l):
		for temp in l:
			self.addWord(temp)
		
	def __iter__(self):
		return iter(self.root.matching())
		
	def matching(self, prefix):
		return self.root.matching(prefix)

	
class TrieNode(object):
	delete_table  = string.maketrans(
		string.ascii_lowercase, ' ' * len(string.ascii_lowercase)
	)
	def __init__(self, word = "", root = False):
		self.isroot = root
		self.children = {}
		DictTrie.leaves.append(self)
		if word == "":
			return
		self.addWord(word)
		
	def addWord(self, word):
		word = word.lower()
		word = word.strip()
		word = word.encode("ascii", "ignore")
		word = word.translate(None, TrieNode.delete_table)
		if len(word) == 0:
			return
		
		if not self.children.has_key(word[0]):
			self.children[word[0]] = TrieNode(word[1:])
		else:
			self.children[word[0]].addWord(word[1:])
		if self in DictTrie.leaves:
			DictTrie.leaves.remove(self)
		
	def matching(self, prefix="", cur = "", words = []):
		prefix = prefix.lower()
		if len(self.children) > 0:
			for temp in self.children.keys():
				cur += temp
				self.children[temp].matching(prefix, cur)
				cur = cur[0:len(cur)-1]
		else:
			words.append(cur)
		if self.isroot:
			return [w for w in words if w.startswith(prefix)]

					
if __name__ == "__main__":
	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(message)s')
	test = DictTrie()
	test.addWord("Hallo")
	test.addWord("Hello")
	test.addWord("Helli")
	test.addWord("Welt")
	test.addWord("Weltuntergang")
	test.addWord("Morgen")
	
	for a in test:
		print a
	


					
	
