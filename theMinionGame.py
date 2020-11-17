from string import ascii_uppercase


def minion_game(s):
    vowels = 'AEIOU'
    # list(set(ascii_uppercase) - set(vowels))

    kevsc = 0
    stusc = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)