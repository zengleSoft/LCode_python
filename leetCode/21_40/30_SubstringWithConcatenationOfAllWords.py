#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 You are given a string, s, and a list of words, words, that are all of the same length.
 Find all starting indices of substring(s) in s that is a concatenation of each word in words
 exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''


class Solution(object):
    def findSubstring(self, s, words):
        word_len = len(words[0])
        start, end = 0, len(s) - word_len * len(words)
        res=set()
        while start <= end:
            tmp_start_str = s[start:start + word_len * len(words)]
            tmp_start_list = [tmp_start_str[i:i + word_len] for i in xrange(0, len(tmp_start_str), word_len)]
            tmp_end_str = s[end:end + word_len * len(words)]
            tmp_end_list = [tmp_end_str[i:i + word_len] for i in xrange(0, len(tmp_end_str), word_len)]
            tmp_flag_start, tmp_flag_end = True,True
            for word in words:
                if tmp_flag_start and word not in tmp_start_list:
                    tmp_flag_start = False
                elif word in tmp_start_list:
                    tmp_start_list.remove(word)
                if tmp_flag_end and word not in tmp_end_list:
                    tmp_flag_end = False
                elif word in tmp_end_list:
                    tmp_end_list.remove(word)
            if tmp_flag_start:
                res.add(start)
            if tmp_flag_end:
                res.add(end)
            start += 1
            end -= 1
        return list(res)

    def findSubstring(self,s,words):
        k = len(words[0])
        n = len(words)
        res=[]
        for i in range(len(s)-n*k+1):
            tmp_s=s[i:(i+n*k)]
            tmp_s_list = [tmp_s[j:j+k] for j in range(0,len(tmp_s),k)]
            for word in words:
                if word not in tmp_s_list:
                    break
                else:
                    tmp_s_list.remove(word)
            else:
                res.append(i)
        return res

if __name__ == '__main__':
    self = Solution()
    s = 'wordgoodgoodgoodbestword'
    words = ["word","good","best","good"]
    print self.findSubstring(s, words)
