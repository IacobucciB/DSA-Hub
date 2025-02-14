def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False

def lgst_palindrome_prod() -> int:
    palindromes = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            aux = i * j
            if isPalindrome(aux):
                palindromes.append(aux)
    print(palindromes)
    return max(palindromes)

print(lgst_palindrome_prod())