def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    a=len(s)
    b=a-n
    c=s[:b]
    return c
s=input("")
n=int(input())
print(main(s,n))