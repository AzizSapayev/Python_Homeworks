def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Foydalanuvchi kiritadi
son = int(input("Sonni kiriting: "))
if is_prime(son):
    print("True")
else:
    print("False")
def digit_sum(k):
    k=str(k)
    s=0
    for i in k:
        s+=int(i)
    return s
print(digit_sum(1234674))


def funksiya(n):
    for i in range(n):
        if 2**i<n:
            print( 2**i)

        
print(funksiya(20))
