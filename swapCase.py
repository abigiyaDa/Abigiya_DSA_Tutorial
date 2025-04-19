def swap_case(s):
    swap=""
    for x in s:
        if(x.islower()):
            swap+=x.upper()
        else:
            swap+=x.lower()
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
