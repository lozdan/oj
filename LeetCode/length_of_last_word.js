/*
author: Daniel Lozano
source: LeetCode ( https://www.leetcode.com )
problem name: Problems > Length of Last Word
problem url: https://leetcode.com/problems/length-of-last-word/description/
*/

var lengthOfLastWord = function(s) {
    s = s.trim()
    var answer = 0;
    if (s.length === 0)
      return 0;
    else{
      var count = s.length - 1;
      while (count >= 0 && s[count] !== " "){
        answer++;
        count--;
      }
      return answer;
    }
};
