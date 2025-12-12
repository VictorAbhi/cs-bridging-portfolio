def karatsuba(x,y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y))) # Number of digits in the largest number
        print("n:", n)
        half_n = n // 2
        print("half_n:", half_n)

        a = x // 10**half_n
        b = x % 10**half_n
        c = y // 10**half_n
        d = y % 10**half_n

        print("a:", a, "b:", b, "c:", c, "d:", d)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        print("ac:", ac, "bd:", bd, "ad_plus_bc:", ad_plus_bc)

        return (ac * 10**(2 * half_n)) + (ad_plus_bc * 10**half_n) + bd
    
# Example usage:
if __name__ == "__main__":
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(f"Karatsuba multiplication of {x} and {y} is: {karatsuba(x, y)}")