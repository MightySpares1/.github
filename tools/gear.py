import math,sys
def gear(r_out,r_in,teeth,hole):
    pts=[]
    n=teeth*4
    for i in range(n):
        a=2*math.pi*i/n
        r=r_out if (i%4) in (1,2) else r_in
        pts.append(f"{r*math.cos(a):.1f},{r*math.sin(a):.1f}")
    d="M"+" L".join(pts)+" Z"
    d+=f" M{hole},0 A{hole},{hole} 0 1,0 {-hole},0 A{hole},{hole} 0 1,0 {hole},0 Z"
    return d
if __name__=="__main__":
    a=list(map(float,sys.argv[1:]))
    print(gear(a[0],a[1],int(a[2]),a[3]))
