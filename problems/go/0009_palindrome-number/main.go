package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	if x%10 == 0 {
		return x == 0
	}

	xx := x
	yy := 0
	for xx > yy {
		// read
		a := xx % 10
		xx /= 10

		// write
		yy = yy*10 + a
	}

	return yy == xx || yy/10 == xx
}

func isPalindrome1(x int) bool {
	if x < 0 {
		return false
	}
	y := reverse(x)
	return x == y
}

func reverse(x int) int {
	xx := x
	yy := 0
	for xx != 0 {
		// read
		a := xx % 10
		xx /= 10

		// write
		if yy > (math.MaxInt32-a)/10 {
			// overflow
			return -1
		}
		yy = yy*10 + a
	}
	return yy
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
		var x int
		var correctAnswer bool
		x, ok := readInt(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ = readBool(sc)

		myAnswer := isPalindrome(x)
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

func readBool(sc *bufio.Scanner) (bool, bool) {
	if !sc.Scan() {
		return false, false
	}
	s := sc.Text()
	b, _ := strconv.ParseBool(s)
	return b, true
}
