import cmath
import evalpoly as ep
from PIL import Image
def draw(p):
    w,h=1920,1080
    bitmap=Image.new("RGB",(w,h),"white")
    pix=bitmap.load()
    for x in range(w):
        for y in range(h):
            #the center of the page corresponds to the number 0+0i
            zx = (1.5*(x-w/2))/(0.5*w)
            zy=(1.0*(y-h/2))/(0.5*h)
            z=complex(zx,zy)
            iter=255
            #evaluate polynomial on z until escape
            while iter>1:
                tmp=ep.poly(p,z)
                z=tmp
                iter-=1
                if mod(z)>4:
                    break
            #color pixel according to iter value. we want lighter colors for smaller iter.
            pix[x,y]=(iter << 21)+(iter << 10)+(iter*8)
            
    bitmap.show()

def mod(z):
    return (z.real*z.real)+(z.imag*z.imag)
