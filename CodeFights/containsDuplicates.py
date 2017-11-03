# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: containsDuplicates
# problem url: https://codefights.com/interview-practice/task/CfknJzPmdbstXhsoJ
# date: 8/5/2017

def containsDuplicates(a):
        a.sort()
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] == a[j]:
                    return True
        return False