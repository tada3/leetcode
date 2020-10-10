package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func myAtoi(str string) int {
	r := []rune(str)

	len := len(r)
	pos := 0
	negative := false
	num := 0

	// skip whitespace
	for pos < len && r[pos] == ' ' {
		pos++
	}

	if pos < len {
		if r[pos] == '+' {
			pos++
		} else if r[pos] == '-' {
			negative = true
			pos++
		}
	}

	for pos < len && isDigit(r[pos]) {
		x := int(r[pos] - '0')
		if negative {
			x = -1 * x
		}

		if negative {
			if num < (math.MinInt32-x)/10 {
				return math.MinInt32
			}

		} else {
			if num > (math.MaxInt32-x)/10 {
				return math.MaxInt32
			}
		}

		num = num*10 + x
		pos++
	}

	return num
}

func isDigit(r rune) bool {
	return '0' <= r && r <= '9'
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
		var s string
		var correctAnswer int
		s, ok := readString(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ = readInt(sc)

		myAnswer := myAtoi(s)
		if myAnswer == correctAnswer {
			fmt.Println("OK")
		} else {
			fmt.Println("Wrong!")
			fmt.Println(myAnswer)
			fmt.Println(correctAnswer)
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
