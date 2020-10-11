def fibo(n:int)->int:
    """
        fonction recursive fibonacci
        prend un entier positif en parametre
        returne f0 = F1 + F2 et ainsi de suite (connaitre principe suite fibo)
        
        >>>fibo(10)
        55
    """
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(10))
    
