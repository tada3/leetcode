<?php
class Solution {

    /**
    * @param String $s
    * @return Boolean
    */
    function isValid($s) {
        $stack = new SplStack();
        foreach (str_split($s) as $c) {
            if ($c=='(' or $c=='{' or $c == '[') {
                $stack->push($c);
                continue;
            } 
            if ($stack->isEmpty()) {
                return false;
            }
            $p = $stack->pop();
            switch($p) {
                case '(':
                    if ($c != ')') {
                        return false;
                    }
                    break;
                case '{':
                    if ($c != '}') {
                        return false;
                    }
                    break;
                case ']':
                    if ($c != ']') {
                        return false;
                    }
                    break;
            }
        }
        return $stack->isEmpty();
    }
}

function main($s) {
    echo("Input: s = $s\n");
    $sol = new Solution();
    $ret = $sol->isValid($s);
    $ret1 = var_export($ret, true);
    echo("Output: $ret1\n");
}

//$s = "()";
//$s = "()[]{}";
//$s = "(]";
//$s = "([{{}}])";
//$s = "]";
$s = "(";

main($s);