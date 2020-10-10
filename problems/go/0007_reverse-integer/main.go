package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func reverse(x int) int {
	xx := x
	yy := 0
	for xx != 0 {
		a := xx % 10
		xx /= 10

		if a > 0 {
			if yy > (math.MaxInt32-a)/10 {
				return 0
			}
		} else {
			if yy < (math.MinInt32-a)/10 {
				return 0
			}
		}
		yy = yy*10 + a
	}
	return yy
}

func reverse1(x int) int {
	xx := int32(x)
	if xx == 0 {
		return 0
	}
	var p int32 = 1
	queue := make([]int32, 0)
	for {
		if xx == 0 {
			p /= 10
			break
		}
		var r int32
		p10 := p * 10
		if p10/10 != p {
			// Overflow
			r = xx / p
			queue = append(queue, r)
			break
		} else {
			q := (xx % p10)
			r = q / p
			queue = append(queue, r)
			p = p10
			xx -= q
		}
	}

	var y int32
	for _, t := range queue {
		s := t * p
		//fmt.Println(t, p, s, s/p)
		if s/p != t {
			// Overflow
			return 0
		}
		u := y + s
		if (s > 0 && u <= y) || (s < 0 && u >= y) {
			// Overflow
			fmt.Println(u, y)
			return 0
		}
		y = u
		p /= 10
	}
	return int(y)
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
		var x, correctAnswer int
		x, ok := readInt(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ = readInt(sc)

		myAnswer := reverse(x)
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
