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
	states []*state
}

type state struct {
	isActive bool
	pos      int
	m        *matcher
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
	m := &matcher{
		tokens: tokens,
	}
	states := []*state{
		{
			isActive: true,
			pos:      0,
			m:        m,
		}}
	m.states = states
	return m
}

func (m *matcher) matchState(c rune, s *state) (bool, []*state) {
	//fmt.Printf("MMMM %c, %d\n", c, m.pos)
	if c == 0 {
		if s.finished() {
			return true, nil
		}
		current := s.currentToken()
		if s.atLastToken() && current.repeat {
			return true, nil
		}
		s.isActive = false
		return false, nil
	}

	if s.finished() {
		s.isActive = false
		return false, nil
	}

	current := s.currentToken()
	if current.repeat {
		if current.char == '.' {
			// longest match, repeat forever
			// do not check the next token
			return true, nil
		} else {
			if current.char == c {
				// 2 possible paths:
				//    (a) stay this token
				//    (b) move to next token
				newStates := make([]*state, 0)
				newState := &state{
					isActive: true,
					pos:      s.pos + 1,
					m:        m,
				}
				_, newStates1 := m.matchState(c, newState)
				newStates = append(newStates, newState)
				newStates = append(newStates, newStates1...)
				return true, newStates

			} else {
				// move to the next token
				s.next()
				return m.matchState(c, s)
			}
		}

	} else {
		if current.char == '.' {
			s.next()
			return true, nil
		} else {
			if current.char == c {
				s.next()
				return true, nil

			} else {
				return false, nil
			}
		}
	}
}

func (m *matcher) match(c rune) bool {
	ret := false
	added := make([]*state, 0)
	for _, s := range m.states {
		if !s.isActive {
			continue
		}
		ok, newStates := m.matchState(c, s)
		if ok {
			ret = true
		} else {
			s.isActive = false
		}
		if newStates != nil {
			added = append(added, newStates...)
		}
	}
	m.states = append(m.states, added...)
	return ret
}

func (s *state) finished() bool {
	return s.pos == len(s.m.tokens)
}

func (s *state) currentToken() token {
	return s.m.tokens[s.pos]
}

func (s *state) atLastToken() bool {
	return s.pos == len(s.m.tokens)-1
}

func (s *state) next() {
	s.pos++
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
