import random


def numbers(n=1000000):
    # Returns a random numbers
    # between 2**(n-1)+1 and 2**n-1'''
    a = []
    for i in range(200):
        x = random.randint(n, 10*n)
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0:
            a.append(x)
    return a


def check_prime(num=[2]):
    p = []
    while len(p) < 2:
        for i in num:
            pseudo = True
            for k in range(40):
                x = random.randint(2, i//2)
                while gcd(x, i) != 1:
                    x = random.randint(2, i//2)
                if pow(x, i-1, i) != 1:
                    pseudo = False
                    break
            if pseudo:
                p.append(i)
        if len(p) < 5:
            num = numbers()
    return p


def p_and_q(prime_list=[1]):
    p = prime_list.pop()
    q = prime_list.pop()
    while p == q:
        q = prime_list.pop()
    return p, q


def key_public(p=5, q=11):
    fn = (p-1)*(q-1)
    e = random.randint(2, fn)
    while gcd(e, fn) != 1:
        e = random.randint(2, fn)
    n = p*q
    return n, e


def gcd(a=1, b=1):
    if a < 0 or b < 0:
        return
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a=1, b=1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a % b)
    return y, x - a//b*y, d


def rsa_encrypt(message='TOP SECRET', n=55, e=3):
    encrypt = []
    for i in message:
        encrypt.append(pow(ord(i), e, n))
    return encrypt


def key_private(p=5, q=11, e=3):
    fn = (p-1) * (q-1)
    x, y, z = extended_gcd(fn, e)
    d = y % fn
    return d


def rsa_decrypt(encrypt=[], n=55, d=27):
    deciphered = []
    for c in encrypt:
        de = pow(c, d, n)
        deciphered.append(de)
    return deciphered


def preprocess(m='This is a a top secret'):
    m = m.upper()
    if len(m) != 0:
        s = ''
        for i in m:
            if not i.isspace():
                s+= i
    else:
        print('Expect a nonempty message. \n')
    return str(s)


def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)


def main():
    again = True
    message = ''

    user = input("Are you a public user or owner?")
    while again:
        if user == 'public':
            choice = input("1. encrypt a message 2. authenicate a digial signature?: ")
            if choice == "1":
                message = input("What is the message you want to encrypt?: ")
                num = numbers(1000000)
                print("before")
                pList = check_prime(num)
                while len(pList) <= 2:
                    num = numbers()
                    pList = check_prime(num)
                p, q = p_and_q(pList)
                n, e = key_public(p, q)
                print('\nPublic key:', n, e)
                m = preprocess(message)
                ciphered = rsa_encrypt(m, n, e)
                print('\nEncrypted message:\n', ciphered)

            if choice == "2":
                message = input("What is the message you want to encrypt?: ")
                num = numbers(1000000)
                pList = check_prime(num)
                while len(pList) <= 2:
                    num = numbers()
                    pList = check_prime(num)
                p, q = p_and_q(pList)
                n, e = key_public(p, q)
                m = preprocess(message)
                ciphered = rsa_encrypt(m, n, e)
                d = 160009
                m = 19070
                S = (m ** d) % n

                M1 = (S ** e) % n

                # If M = M1 only then Bob accepts
                # the message sent by Alice.

                if ciphered == M1:
                    print("As M = M1, Accept the\
                    message sent by Alice")
                else:
                    print("As M not equal to M1,\
                    Do not accept the message\
                    sent by Alice ")
                    break
                #digitalsignature

        if user == 'owner':
            choice2 = input("1. decipher text 2.Generate digital signature")
            if choice2 == "1":
                num = numbers(1000000)
                pList = check_prime(num)
                while len(pList) <= 2:
                    num = numbers()
                    pList = check_prime(num)
                p, q = p_and_q(pList)
                n, e = key_public(p, q)
                message = "RSA IS SECURE"
                m = preprocess(message)
                ciphered = rsa_encrypt(m, n, e)
                d = key_private(p, q, e)
                deciphered = rsa_decrypt(ciphered, n, d)
                print("Deciphered: \n")
                print(deciphered)
                de_text = ''
                for i in deciphered:
                    de_text += chr(i)

        again = input('Do you want to complete another task?')
        if again == "False":
            again = False



if __name__ == "__main__":
    main()

def fastExpo_rec (c,d,n):
    if d == 0:
        return 1
    if d%2 == 0:
        t = fastExpo_rec(c,d//2,n)
        return(t*t) %n
    else:
        t = fastExpo_rec(c, d//2,n)
        return c *(t**2%d)%n
