def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    

    a=len(s)
    c=a-n
    b=s[c:]
    return b
s=input("")
n=int(input())
print(main(s,n))

