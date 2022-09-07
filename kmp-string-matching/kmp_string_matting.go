package main

import (
	"fmt"
)

// LPS stands for Longest Proper Prefix
func createLPSTable(pattern string) []int {
	pLen := len(pattern)
	LPS := make([]int, pLen)
	len := 0
	i := 1
	for i < pLen {
		if pattern[i] == pattern[len] {
			len += 1
			LPS[i] = len
			i += 1
		} else {
			if len != 0 {
				len = LPS[len-1]
			} else {
				LPS[i] = 0
				i += 1
			}
		}
	}
	fmt.Println(pLen, LPS)
	return LPS
}

func computeWithLPS(input string, pattern string) int {
	i := 0
	j := 0
	n := len(input)
	m := len(pattern)
	LPS := createLPSTable(pattern)
	for i < n {
		if input[i] == pattern[j] {
			i += 1
			j += 1
			if j == m {
				return i - j
			}
		} else {
			if j > 0 {
				j = LPS[j-1]
			} else {
				i += 1
			}
		}
	}
	return -1
}

func main() {
	input := "inyoyo"
	pattern := "yoyo"
	patternIndex := computeWithLPS(input, pattern)
	fmt.Println(patternIndex)
}
