def primeira(palavra):
    """Exibe o primeiro caractere da string"""
    return palavra[0]


def meio(palavra):
    """Exibe toda a string exceto a primeira e a ultima parte da string."""
    return palavra[1:-1]


def ultima(palavra):
    """
    Exibe a ultima parte da string
    """
    return palavra[-1]


def palindrome(palavra):
    """
    Exibe True se a palavra for um palindromo
    """
    if len(palavra) <= 1:
        return True
    if primeira(palavra) != ultima(palavra):
        return False
    return palindrome(meio(palavra))


print(palindrome("bob"))
print(palindrome("dado"))
print(palindrome("radar"))
