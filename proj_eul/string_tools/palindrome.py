def is_palindrome(li):
    tag = True
    for i in range(len(li)/2+1):
        if li[i] != li[-i-1]:
            tag = False
    return tag

if __name__ == '__main__':
    print is_palindrome([1,2,5,2,1])
