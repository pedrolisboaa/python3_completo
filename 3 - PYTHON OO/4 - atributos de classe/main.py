class A:
    vc = 123


if __name__ == '__main__':
    a = A()
    b = A()

    print(a.vc)
    print(b.vc)
    print(A.vc)