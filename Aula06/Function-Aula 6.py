def fib(n):    # write Fibonacci series up to n
  """Retorna array com serie fibonacci até n."""

  result = []

  a, b = 0, 1
  while a < n:
      result.append(a)
      a, b = b, a+b


  return result    

# Now call the function we just defined:
series = fib(2000)
print(series)