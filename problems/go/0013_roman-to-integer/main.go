package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func romanToInt(s string) int {
	vmap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	smap := map[rune]int{
		'I': -1,
		'V': 1,
		'X': 1,
		'L': 10,
		'C': 10,
		'D': 100,
		'M': 100,
	}

	var x, p int
	for _, c := range s {
		v := vmap[c]
		x += v

		if p == smap[c] {
			x -= 2 * p
		}

		p = v
	}
	return x
}

const filename = "testcase.txt"

func main() {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("File access error!", err)
		os.Exit(1)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	for {
		var x string
		var correctAnswer int
		x, ok := readString(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ = readInt(sc)

		myAnswer := romanToInt(x)
		if myAnswer == correctAnswer {
			fmt.Println("OK")
		} else {
			fmt.Println("Wrong!")
			fmt.Println("Expected:", correctAnswer)
			fmt.Println("Actual:", myAnswer)
		}
	}
}

func readString(sc *bufio.Scanner) (string, bool) {
	if !sc.Scan() {
		return "", false
	}
	s := sc.Text()
	return strings.Trim(s, "\""), true
}

func readInt(sc *bufio.Scanner) (int, bool) {
	if !sc.Scan() {
		return 0, false
	}
	s := sc.Text()
	n, _ := strconv.Atoi(s)
	return n, true
}

func readInt32(sc *bufio.Scanner) (int32, bool) {
	if !sc.Scan() {
		return 0, false
	}
	s := sc.Text()
	n, _ := strconv.ParseInt(s, 10, 32)
	return int32(n), true
}

func readBool(sc *bufio.Scanner) (bool, bool) {
	if !sc.Scan() {
		return false, false
	}
	s := sc.Text()
	b, _ := strconv.ParseBool(s)
	return b, true
}
