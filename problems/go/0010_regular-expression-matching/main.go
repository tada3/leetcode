package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isMatch(s string, p string) bool {
	//fmt.Println("000 ", s, p)
	m := createMatcher(p)
	for _, c := range s {
		if !m.match(c) {
			return false
		}
	}
	if !m.match(0) {
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

func (m *matcher) matchState(c rune, s *state) []*state {
	//fmt.Printf("MMMM %c, %d, %d\n", c, c, s.pos)
	if c == 0 {
		if s.finished() {
			return nil
		}
		current := s.currentToken()
		if current.repeat {
			if s.atLastToken() {
				return nil
			}
			s.next()
			return m.matchState(c, s)
		}
		s.isActive = false
		return nil
	}

	if s.finished() {
		s.isActive = false
		return nil
	}

	current := s.currentToken()
	if current.repeat {
		if current.char == '.' {
			//fmt.Println("REPEAT ANY")
			newStates := make([]*state, 0)
			newState := &state{
				isActive: true,
				pos:      s.pos + 1,
				m:        m,
			}
			newStates1 := m.matchState(c, newState)
			newStates = append(newStates, newState)
			newStates = append(newStates, newStates1...)

			return newStates
		} else {
			if current.char == c {
				//fmt.Println("REPEAT MATCH")
				// 2 possible paths:
				//    (a) stay this token
				//    (b) move to next token
				newStates := make([]*state, 0)
				newState := &state{
					isActive: true,
					pos:      s.pos + 1,
					m:        m,
				}
				newStates1 := m.matchState(c, newState)
				newStates = append(newStates, newState)
				newStates = append(newStates, newStates1...)
				return newStates

			} else {
				//fmt.Println("REPEAT NOT MATCH")
				// move to the next token
				s.next()
				return m.matchState(c, s)
			}
		}

	} else {
		if current.char == '.' {
			//fmt.Println("ANY")
			s.next()
			return nil
		} else {

			if current.char == c {
				//fmt.Println("MATCH")
				s.next()
				return nil

			} else {
				//fmt.Println("NOT MATCH")
				s.isActive = false
				return nil
			}
		}
	}
}

func (m *matcher) match(c rune) bool {
	//fmt.Printf("match() %c\n", c)
	added := make([]*state, 0)
	for _, s := range m.states {
		if !s.isActive {
			continue
		}
		newStates := m.matchState(c, s)
		if newStates != nil {
			added = append(added, newStates...)
		}
	}
	m.states = append(m.states, added...)

	//for _, s := range m.states {
	//	fmt.Printf("XXX s=%+v\n", s)
	//}

	for _, s := range m.states {
		if s.isActive {
			return true
		}
	}
	return false
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
