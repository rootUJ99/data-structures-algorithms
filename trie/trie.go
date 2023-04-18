package main

import (
	"fmt"
)

type DummyNode struct {
	stream *[2]string
}

func (d DummyNode) PrintDummy() {
	fmt.Println(&d.stream)
}

type Node struct {
	data        [26]*Node
	isEndofWord bool
}

type Trie struct {
	root *Node
}

func getAsciiVal(char rune) int {
	a := int(char) - int('a')
	return a
}

func ConstructTrie() *Trie {
	t := new(Trie)
	t.root = new(Node)
	return t
}

func (t Trie) Insert(word string) {
	newRoot := t.root
	for _, ele := range word {
		charAsIndex := getAsciiVal(ele)
		if newRoot.data[charAsIndex] == nil {
			newRoot.data[charAsIndex] = new(Node)
		}
		newRoot = newRoot.data[charAsIndex]
	}
	newRoot.isEndofWord = true
}

func (t Trie) Search(word string) int {
	newRoot := t.root
	for _, ele := range word {
		charAsIndex := getAsciiVal(ele)
		if newRoot.data[charAsIndex] == nil {
			return 0
		}
		newRoot = newRoot.data[charAsIndex]
	}
	if newRoot.isEndofWord {
		return 1
	}
	return 0
}

func main() {
	fmt.Println("yo")
	trie := ConstructTrie()

	trie.Insert("abcd")

	fmt.Println(trie.root)

	result := trie.Search("abcd")
	fmt.Println(result)

}
