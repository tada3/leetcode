package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func intToRoman(num int) string {
	rvs := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	rmap := map[int]string{
		1:    "I",
		4:    "IV",
		5:    "V",
		9:    "IX",
		10:   "X",
		40:   "XL",
		50:   "L",
		90:   "XC",
		100:  "C",
		400:  "CD",
		500:  "D",
		900:  "CM",
		1000: "M",
	}
	var sb strings.Builder
	x := num
	for _, rv := range rvs {
		for {
			if x < rv {
				break
			}
			sb.WriteString(rmap[rv])
			x -= rv
		}
	}
	return sb.String()
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
		var correctAnswer string
		x, ok := readInt(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ = readString(sc)

		myAnswer := intToRoman(x)
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
