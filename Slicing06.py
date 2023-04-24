def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    a=n

    return s[a:]
s=input("")
n=int(input())
print(main(s,n))