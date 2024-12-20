w, h, n = map(int, input().split())
if w%h==0 or h%w==0:
    print(w*h)
if w%h!=0:
    k=max(w,h)
    print(k*k)


