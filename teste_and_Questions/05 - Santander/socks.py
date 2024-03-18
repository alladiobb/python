def sockMerchant(n, ar):
  socks = {}
  pairs = 0
  for sock in ar:
    if sock in socks:
      socks[sock] += 1
      if socks[sock] % 2 == 0:
        pairs += 1
    else:
      socks[sock] = 1
  return pairs


n = 7
ar = [1, 2, 1, 2, 1, 3, 2, 1, 3, 2]
result = sockMerchant(n, ar)
print(result)  
