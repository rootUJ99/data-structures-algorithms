package main

import "fmt"

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

func main() {
	createLPSTable("abbadabba")
}
