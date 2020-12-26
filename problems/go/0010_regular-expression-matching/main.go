package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isMatch(s string, p string) bool {
	fmt.Println("000 ", s, p)
	m := createMatcher(p)
	for _, c := range s {
		if !m.match(c) {
			fmt.Println("111")
			return false
		}
	}
	if !m.match(0) {
		fmt.Println("222")
		return false
	}
	return true

}

type token struct {
	repeat bool
	char   rune
}

type matcher struct {
	tokens []token
	pos    int
}

func createMatcher(p string) *matcher {
	tokens := make([]token, 0)
	p1 := []rune(p)
	for _, c := range p1 {
		if c == '*' {
			lastToken := tokens[len(tokens)-1]
			lastToken.repeat = true
			tokens[len(tokens)-1] = lastToken
		} else {
			tokens = append(tokens, token{
				repeat: false,
				char:   c,
			})
		}
	}
	return &matcher{
		tokens: tokens,
		pos:    0,
	}
}

func (m *matcher) match(c rune) bool {
	fmt.Printf("MMMM %c, %d\n", c, m.pos)
	if c == 0 {
		if m.finished() {
			return true
		}
		current := m.currentToken()
		if m.isLastToken() && current.repeat {
			return true
		}
		return false
	}

	if m.finished() {
		return false
	}

	current := m.currentToken()
	if current.repeat {
		if current.char == '.' {
			// longest match, repeat forever
			// do not check the next token
			return true
		} else {
			if current.char == c {
				return true

			} else {
				// move to the next token
				m.next()
				return m.match(c)
			}
		}

	} else {
		if current.char == '.' {
			m.next()
			return true
		} else {
			if current.char == c {
				m.next()
				return true

			} else {
				return false
			}
		}
	}
}

func (m *matcher) finished() bool {
	return m.pos == len(m.tokens)
}

func (m *matcher) isLastToken() bool {
	return m.pos == len(m.tokens)-1
}

func (m *matcher) next() {
	m.pos++
}

func (m *matcher) currentToken() token {
	return m.tokens[m.pos]
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
		s, ok := readString(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		p, ok := readString(sc)
		if !ok {
			fmt.Println("No more input.")
			break
		}
		correctAnswer, _ := readBool(sc)

		myAnswer := isMatch(s, p)
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
