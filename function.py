def counting_system(n):
    s = 0
    while(n):
      s = s + n % 10
      n /= 10
