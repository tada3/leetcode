<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums)
    {
        $p = 1;
        $q = 0;
        while ($p < count($nums)) {
            if ($nums[$p] != $nums[$q]) {
                $nums[++$q] = $nums[$p];
            }
            $p++;
        }
        return $q + 1;
    }
}



function main($nums)
{
    echo "Input: nums = " . json_encode($nums) . "\n";
    $sol = new Solution();
    $ret = $sol->removeDuplicates($nums);
    echo ("Output: $ret, " . json_encode($nums) . "\n");
}

//$nums = [1, 1, 2];
//$nums = [0,0,1,1,1,2,2,3,3,4];
//$nums = [100];
//$nums = [1, 1, 1];
$nums = [1, 2, 3];

main($nums);
