n = 5
for i in range(1, n*2):
    spaces = abs(n - i)
    stars = n - spaces
    print(" " * spaces + "* " * stars)
    
