import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.util.*;


class Solution {
    public int[] maxSlidingWindowTreeMap(int[] nums, int k) {
        if (k==1) {
            return nums;
        }

        int n = nums.length;
        var countMap = new TreeMap<Integer, Integer>(Collections.reverseOrder());
        var a = new int[n - (k-1)];

        for (int i=0; i<k; i++) {
            countMap.merge(nums[i], 1, Integer::sum);
        }
        a[0] = countMap.firstKey();

        for (int i=k; i<n; i++) {
            // remove the left most of the previous window
            int lmpw = i - k;
            countMap.merge(nums[lmpw], -1, Integer::sum);
            if (countMap.get(nums[lmpw]) == 0) {
                countMap.remove(nums[lmpw]);
            }

            // add the right most of the current window
            countMap.merge(nums[i], 1, Integer::sum);

            a[lmpw + 1] = countMap.firstKey();
        }
        return a;        
    }

    public int[] maxSlidingWindowDeque(int[] nums, int k) {
        if (k==1) {
            return nums;
        }

        int n = nums.length;
        if (k == n) {
            var max = Arrays.stream(nums).max().getAsInt();
            return new int[]{max};
        }

        var deq = new ArrayDeque<Integer>(k);
        var a = new int[n - (k-1)];

        for (int i=0; i<k; i++) {
             // 2. remove x < nums[i]
             while (!deq.isEmpty() && nums[deq.peekLast()] <= nums[i]) {
                deq.pollLast();
            }

            // 3. add i
            deq.offer(i);
        }
        a[0] = nums[deq.peek()];

        for (int i=k; i<n; i++) {
            var leftMost = i - k + 1;

            // 1. remove out-of-window element
            if (deq.peek() < leftMost) {
                deq.poll();
            } 

            // 2. remove x < nums[i]
            int x = nums[i];
            if (!deq.isEmpty()) {
                if (deq.size() > 100 && nums[deq.peek()] <= x) {
                    deq.clear();
                } else {
                    while (!deq.isEmpty() && nums[deq.peekLast()] <= x) {
                        deq.pollLast();
                    }
                }
            }

            // 3. add i
            deq.offer(i);
          
            a[leftMost] = nums[deq.peek()];
        }
        return a;
    }



    public static void main(String[] args) {
        String filename = "testcase.txt";
        try (BufferedReader in = new BufferedReader(new FileReader(new File(filename)))){
            while (true) {
                Solution s = new Solution();
                String numsStr = in.readLine();
                if (numsStr == null) {
                    break;
                }
                int[] nums = parseIntArray(numsStr);

                String kStr = in.readLine();
                int k = Integer.parseInt(kStr);

                String answerStr = in.readLine();
                int[] answer = parseIntArray(answerStr);

                // Solve
                int[] result = s.maxSlidingWindowDeque(nums, k);

                // Check
                if (Arrays.equals(result, answer)) {
                    System.out.println("OK");
                } else {
                    System.out.println("NG");
                    System.out.printf("result: %s\n", Arrays.toString(result));
                    System.out.printf("answer: %s\n", Arrays.toString(answer));
                }
            }
        } catch (Exception e){ 
            e.printStackTrace();
            System.exit(-1);
        }
    }

    private static int[] parseIntArray(String str) {
        //String str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]";
        String str1 = str.trim().substring(1, str.length()-1);
        int[] arr = Arrays.stream(str1.split(",")).
            map(String::trim).
            mapToInt(Integer::parseInt).
            toArray();
        return arr;
    }
}