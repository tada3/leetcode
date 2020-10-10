package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convert(s string, numRows int) string {
	l := len(s)
	ss := []rune(s)
	ll := len(ss)
	a := numRows - 1
	if a == 0 {
		return s
	}
	p := l / a
	sb := make([]rune, ll)
	pos := 0
	for i := 0; i < numRows; i++ {
		for j := 0; j <= p; j++ {
			var idx int
			if j%2 == 0 {
				if i < a {
					idx = j*a + i
					if idx < ll {
						sb[pos] = ss[idx]
						pos++
					}
				}
			} else if i > 0 {
				idx = j*a + a - i
				if idx < ll {
					sb[pos] = ss[idx]
					pos++
				}
			}
		}
	}
	return string(sb)
}

func convert2(s string, numRows int) string {
	l := len(s)
	ss := []rune(s)
	ll := len(ss)
	a := numRows - 1
	if a == 0 {
		return s
	}
	p := l / a
	var sb strings.Builder
	sb.Grow(l)
	for i := 0; i < numRows; i++ {
		for j := 0; j <= p; j++ {
			var idx int
			if j%2 == 0 {
				if i < a {
					idx = j*a + i
					if idx < ll {
						sb.WriteRune(ss[idx])
					}
				}
			} else if i > 0 {
				idx = j*a + a - i
				if idx < ll {
					sb.WriteRune(ss[idx])
				}
			}
		}
	}
	return sb.String()
}

func convert1(s string, numRows int) string {
	l := len(s)
	ss := []rune(s)
	ll := len(ss)
	a := numRows - 1
	if a == 0 {
		return s
	}
	p := l / a
	var sb = make([]strings.Builder, numRows)
	for i := 0; i < numRows; i++ {
		sb[i].Grow(l)
		for j := 0; j <= p; j++ {
			var idx int
			if j%2 == 0 {
				if i < a {
					idx = j*a + i
					if idx < ll {
						sb[i].WriteRune(ss[idx])
					}
				}
			} else if i > 0 {
				idx = j*a + a - i
				if idx < ll {
					sb[i].WriteRune(ss[idx])
				}
			}
		}
	}
	var answer strings.Builder
	answer.Grow(l)
	for _, b := range sb {
		answer.WriteString(b.String())
	}

	return answer.String()
}

const filename = "testcase.txt"

func main() {
	fmt.Printf("Hello, world.\n")

	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("File access error!", err)
		os.Exit(1)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	for {
		var s, correctAnswer string
		var r int
		s, ok := readString(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		r, _ = readInt(sc)
		correctAnswer, _ = readString(sc)

		myAnswer := convert(s, r)
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
