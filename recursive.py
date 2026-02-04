def countdown(n):
    if n <= 0:
        print('done')
    else:
        print(n)
        countdown(n-1)

countdown(5)


def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
