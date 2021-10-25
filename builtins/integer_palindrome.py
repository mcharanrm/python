#To verify given integer is valid palindrome or not

def palindrome_check_with_stack(N):
    ''' stack based approach '''

    # understand the given integer is a even length or odd lenth ??
    Q,R = divmod(len(str(N)), 2)
    if R == 0:
        #Procedure to work with even length palindromes
        LH = list(map(int,str(N)[:Q:]))
        RH = list(map(int,str(N)[Q::]))

        for item in RH:
            if item != LH.pop():
                return False

        if not LH:
            return True
    else:
        LH = list(map(int, str(N)[:Q:]))
        RH = list(map(int, str(N)[Q+R::]))

        for item in RH:
            if item != LH.pop():
                return False

        if not LH:
            return True


def palindrome_check_without_stack(N):
    ''' without stack based approach '''

    Q,R = divmod(len(str(N)), 2)
    if R == 0:
        # procedure for even length integer to verify it is a valid palindrome
        LH = int(str(N)[:Q:])
        RH = int(str(N)[Q::][::-1])

        if LH == RH:
            return True
        else:
            return False

    else:
        #procedure for odd length integer to verify it is a valid palindrome
        LH = str(N)[:Q:]
        RH = str(N)[Q+R::][::-1]

        if LH == RH:
            return True
        else:
            return False
