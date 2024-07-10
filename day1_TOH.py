def TOH(n,start,mid,dest):
    if n ==0:
        return
    TOH(n-1,start,dest,mid)
    print(f"Move disk {n} from {start} to {mid}")
    TOH(n-1,dest,mid,start)

n=3
TOH(n,'A','B','C')