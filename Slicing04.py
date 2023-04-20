def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    
    return s[0:n]
n=int(input(""))
s=input('')
print(main(s,n))